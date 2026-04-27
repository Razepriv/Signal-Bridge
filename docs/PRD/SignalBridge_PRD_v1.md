# SignalBridge — Product Requirements Document

**TradingView-to-MetaTrader 5 Signal Bridge**
*Automated Signal Execution | Risk Engine | Telegram Alerts | Admin Dashboard*

| Field | Value |
|---|---|
| Product Name | SignalBridge |
| Version | 1.0 |
| Date | April 2026 |
| Author | Webverse Arena |
| Classification | CONFIDENTIAL |
| Target Users | Solo trader / small prop team (1–5 accounts) |
| Stack | Pine Script + Node.js/Python + MQL5 + Supabase + Telegram |
| Priority | MVP in 4 weeks, full system in 8 weeks |

> **Implementation note (added on bootstrap):** the Bridge runtime is locked to **Python 3.11+ + FastAPI** for fastest end-to-end signal-to-fill latency. See [`../architecture/ADR-0001-bridge-runtime.md`](../architecture/ADR-0001-bridge-runtime.md).

---

## 1. Executive Summary

SignalBridge is a secure, automated signal execution pipeline that connects TradingView chart analysis to MetaTrader 5 order execution. The system receives webhook alerts from TradingView Pine Script strategies, validates and enriches them through a backend bridge server, and forwards execution commands to a custom MT5 Expert Advisor that handles position sizing, risk management, and trade lifecycle management.

This PRD defines the full system architecture, component specifications, API contracts, risk controls, and deployment plan for building SignalBridge as a production-grade trading automation platform.

---

## 2. Problem Statement

### 2.1 Current Pain Points

- TradingView provides superior charting and Pine Script strategy development, but cannot execute trades on MetaTrader brokers directly.
- Manual trade execution from TradingView signals introduces latency (30–120 seconds), emotional interference, and missed entries.
- Existing bridge solutions (PineConnector, TradingConnector) lack custom risk engine integration, multi-account support, and granular logging.
- No unified dashboard to monitor signal flow, execution quality, slippage, and P&L across the entire pipeline.

### 2.2 Target Outcome

A fully automated, self-hosted signal execution system where:

1. TradingView Pine strategies generate structured trade signals.
2. A secure webhook server validates, deduplicates, and enriches signals.
3. MT5 EA receives commands and executes with proper lot sizing, SL/TP, and risk checks.
4. All activity is logged, monitored, and alerted via Telegram and a web dashboard.
5. Hard risk limits prevent catastrophic losses regardless of signal quality.

---

## 3. System Architecture

### 3.1 High-Level Data Flow

The system follows a unidirectional signal pipeline with feedback loops for monitoring:

| Layer | Component | Technology | Responsibility |
|---|---|---|---|
| 1. Signal Source | TradingView Pine Strategy | Pine Script v6 | Detect setups, generate structured alert payloads |
| 2. Transport | TradingView Webhook | HTTPS POST | Deliver JSON signal to bridge endpoint |
| 3. Bridge Server | SignalBridge API | Node.js + Express / **Python + FastAPI (locked)** | Validate, deduplicate, enrich, risk-check, forward to MT5 |
| 4. Execution | MT5 Expert Advisor | MQL5 | Receive commands, calculate lots, execute orders, manage positions |
| 5. Data Store | Supabase / PostgreSQL | SQL + Realtime | Signal log, trade log, config, P&L tracking |
| 6. Monitoring | Admin Dashboard + Telegram | Next.js + Telegram Bot API | Real-time status, alerts, daily reports |

### 3.2 Communication Protocol

- **TradingView → Bridge:** HTTPS POST webhook with JSON body. TradingView sends the alert payload to a public HTTPS endpoint on the bridge server.
- **Bridge → MT5:** Two options supported — (A) Named pipe / TCP socket on localhost (EA polls or listens), or (B) MT5 Python integration via the official MetaTrader5 Python package running on the same VPS. **Option B is recommended for MVP and is the locked choice.**
- **MT5 → Bridge (feedback):** EA posts execution results (fill price, slippage, ticket) back to bridge via HTTP or writes to a shared file/database that the bridge polls.

---

## 4. Component Specifications

### 4.1 Component 1 — TradingView Pine Script Strategy

The Pine Script strategy runs on TradingView charts and generates alert payloads when trade conditions are met.

**Requirements**

- Must be a strategy (not indicator) to leverage `strategy.entry/exit` events and realistic backtesting.
- Support multiple strategy types via `strategy_id` field (breakout, SMC pullback, mean reversion, etc.).
- Generate structured JSON alert payload with all fields needed for execution.
- Include server-side alert conditions (not client-side) for reliability.
- Support XAUUSD (gold) on M15 timeframe as primary, extensible to other symbols/TFs.

**Alert Payload Schema**

| Field | Type | Required | Description |
|---|---|---|---|
| `action` | string | Yes | BUY \| SELL \| CLOSE \| MODIFY |
| `symbol` | string | Yes | e.g. XAUUSD, EURUSD |
| `entry` | float | No | Suggested entry price (market if omitted) |
| `sl` | float | Yes | Stop-loss price level |
| `tp` | float | No | Take-profit price level |
| `strategy_id` | string | Yes | e.g. `smc_lo_v1`, `breakout_v2` |
| `timeframe` | string | Yes | e.g. 15, 60, 240 |
| `rr` | float | No | Reward:risk ratio (calculated if tp + sl given) |
| `confidence` | float | No | 0.0–1.0 signal confidence score |
| `secret` | string | Yes | Shared secret for authentication |
| `timestamp` | string | Yes | ISO 8601 alert timestamp |

### 4.2 Component 2 — Bridge Server (SignalBridge API)

The bridge is the central orchestrator. It receives webhooks, validates them, applies risk rules, and dispatches commands to MT5.

**Tech Stack**

| Layer | Technology | Justification |
|---|---|---|
| Runtime | **Python 3.11+** (locked) | Direct MT5 Python lib integration, lowest end-to-end latency |
| Framework | **FastAPI** (locked) | Async-ready, Pydantic validation, automatic OpenAPI |
| Database | Supabase (PostgreSQL) | Realtime subscriptions, auth, edge functions, free tier |
| Queue | BullMQ-equivalent / in-memory (Redis optional) | Signal deduplication, retry logic, rate limiting |
| Hosting | Same Windows VPS as MT5 | Minimum latency between bridge and MT5 terminal |

**API Endpoints**

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/webhook` | Receive TradingView alerts |
| GET | `/api/v1/status` | System health check |
| GET | `/api/v1/signals` | List recent signals with execution status |
| GET | `/api/v1/positions` | Current open positions from MT5 |
| POST | `/api/v1/command` | Manual command to MT5 (close all, modify, etc.) |
| GET | `/api/v1/stats` | P&L stats, win rate, slippage report |
| PUT | `/api/v1/config` | Update risk parameters live |
| GET | `/api/v1/health/mt5` | MT5 connection status check |

**Webhook Processing Pipeline**

1. Receive POST request with JSON body.
2. **Authenticate:** validate shared secret matches configured value.
3. **Parse and validate:** check all required fields, types, ranges.
4. **Deduplicate:** reject if identical signal received within 60-second window.
5. **Risk gate:** check daily loss limit, max open positions, max trades per day.
6. **Spread check:** query MT5 for current spread, reject if above threshold.
7. **Enrich:** add server timestamp, calculated RR, lot size suggestion.
8. **Dispatch:** send execution command to MT5 via Python bridge.
9. **Log:** write signal + execution result to Supabase.
10. **Notify:** send Telegram alert with signal details and execution confirmation.

### 4.3 Component 3 — MT5 Expert Advisor (Executor)

The EA runs on the MT5 terminal and handles all broker-facing operations. It can operate in three modes:

- **Standalone mode:** full SMC strategy logic built-in (current `Gold_SMC_v7.mq5`).
- **Bridge mode:** listens for commands from SignalBridge API and executes them.
- **Hybrid mode:** runs own strategy AND accepts external signals (recommended).

**Bridge Command Protocol**

The EA reads commands from a local file, named pipe, or TCP socket. Each command is a single-line JSON:

| Command | Parameters | Action |
|---|---|---|
| `OPEN_BUY` | symbol, sl, tp, lot, strategy_id | Open a buy position with specified parameters |
| `OPEN_SELL` | symbol, sl, tp, lot, strategy_id | Open a sell position with specified parameters |
| `CLOSE` | ticket or close_all=true | Close specific position or all positions |
| `MODIFY_SL` | ticket, new_sl | Move stop-loss for a position |
| `MODIFY_TP` | ticket, new_tp | Move take-profit for a position |
| `STATUS` | none | EA responds with account balance, equity, open positions |

**EA Risk Overrides**

Even when receiving external commands, the EA enforces its own safety limits:

- Maximum lot size cap (e.g., 1.0 lots regardless of signal).
- Minimum SL distance (respects broker `STOPS_LEVEL` and `FREEZE_LEVEL`).
- Maximum daily loss kill switch (closes all and stops accepting commands).
- Maximum simultaneous open positions.
- Spread check before every execution.
- Account trade permission verification.

---

## 5. Risk Engine Specification

The risk engine operates at two layers: the **bridge server** (pre-execution) and the **MT5 EA** (execution-time). Both layers must independently enforce limits so that no single point of failure can bypass risk controls.

### 5.1 Bridge-Level Risk Rules

| Rule | Default | Configurable | Action on Breach |
|---|---|---|---|
| Max risk per trade | 1% of equity | Yes | Reject signal, log, alert |
| Max daily drawdown | 3% of starting equity | Yes | Halt all signals for day |
| Max open positions | 3 | Yes | Queue or reject new signals |
| Max trades per day | 6 | Yes | Reject, notify via Telegram |
| Max correlated exposure | 2 same-direction on same pair | Yes | Reject duplicate direction |
| Min time between trades | 5 minutes | Yes | Reject, log as duplicate |
| Max spread | 40 points for XAUUSD | Yes | Delay or reject signal |
| Signal expiry | 120 seconds from alert timestamp | Yes | Reject stale signals |
| Weekend guard | No execution Sat/Sun | No | Reject with reason code |
| News blackout | No trades 12:00–14:30 UTC | Yes | Queue until window closes |

### 5.2 EA-Level Risk Rules

These are hardcoded in the EA as a final safety net:

- Lot size cannot exceed `SYMBOL_VOLUME_MAX` or configured cap.
- SL distance cannot be less than `SYMBOL_TRADE_STOPS_LEVEL`.
- Daily loss of configured USD amount triggers full halt.
- Account equity below 80% of day-start balance triggers emergency close-all.
- Invalid prices (`ask <= 0`, `bid <= 0`) block all execution.

---

## 6. Database Schema (Supabase)

### 6.1 `signals` table

| Column | Type | Description |
|---|---|---|
| `id` | uuid PK | Auto-generated signal ID |
| `received_at` | timestamptz | Server receive timestamp |
| `alert_timestamp` | timestamptz | TradingView alert timestamp |
| `strategy_id` | text | Strategy identifier |
| `symbol` | text | Trading symbol |
| `action` | text | BUY / SELL / CLOSE / MODIFY |
| `entry_price` | decimal | Suggested entry price |
| `sl_price` | decimal | Stop-loss level |
| `tp_price` | decimal | Take-profit level |
| `confidence` | decimal | Signal confidence score |
| `status` | text | RECEIVED / VALIDATED / REJECTED / EXECUTED / FAILED |
| `rejection_reason` | text | Why signal was rejected (if applicable) |
| `latency_ms` | integer | Time from alert to bridge receive |

### 6.2 `executions` table

| Column | Type | Description |
|---|---|---|
| `id` | uuid PK | Execution record ID |
| `signal_id` | uuid FK | Reference to signals table |
| `ticket` | bigint | MT5 order ticket number |
| `fill_price` | decimal | Actual fill price |
| `slippage` | decimal | `fill_price - entry_price` |
| `lot_size` | decimal | Executed lot size |
| `executed_at` | timestamptz | Execution timestamp |
| `spread_at_execution` | decimal | Spread in points at time of execution |
| `status` | text | FILLED / PARTIAL / REJECTED / ERROR |
| `error_code` | integer | MT5 error code if failed |

### 6.3 `trades` table

| Column | Type | Description |
|---|---|---|
| `id` | uuid PK | Trade lifecycle record |
| `execution_id` | uuid FK | Reference to executions table |
| `ticket` | bigint | MT5 position ticket |
| `open_price` | decimal | Position open price |
| `close_price` | decimal | Position close price (null if open) |
| `pnl_usd` | decimal | Realized P&L including commission/swap |
| `rr_achieved` | decimal | Actual reward:risk ratio achieved |
| `duration_minutes` | integer | How long position was open |
| `close_reason` | text | TP_HIT / SL_HIT / TRAILING / MANUAL / BRIDGE_CLOSE |
| `be_moved` | boolean | Was breakeven triggered |
| `partial_closed` | boolean | Was partial close executed |

---

## 7. Telegram Notification System

All critical events produce Telegram notifications. The bot sends to configured chat IDs (personal and/or group).

| Event | Priority | Content |
|---|---|---|
| Signal received | Info | Strategy, symbol, direction, entry, SL, TP |
| Signal rejected | Warning | Rejection reason, risk rule breached |
| Order executed | High | Ticket, entry, lot, SL, TP, spread, slippage |
| Trade closed | High | P&L, RR achieved, close reason, day stats |
| Breakeven set | Info | Ticket, new SL, RR at trigger |
| Partial close | Info | Lots closed, remaining, RR at trigger |
| Daily loss hit | Critical | Day P&L, limit, all trading halted |
| MT5 disconnected | Critical | Connection lost, retry count, last known state |
| Daily report | Info | Trades, W/L, win rate, P&L, balance, equity |
| System startup | Info | Config summary, MT5 connection status |

---

## 8. Admin Dashboard (Web UI)

A lightweight Next.js dashboard deployed on the same VPS or on Vercel, connected to Supabase for real-time data.

### 8.1 Pages

1. **Dashboard Home** — live P&L, open positions, recent signals, MT5 status indicator, account summary.
2. **Signal Log** — searchable/filterable table of all signals with status, latency, execution result.
3. **Trade History** — all closed trades with P&L, RR, duration, close reason, equity curve chart.
4. **Execution Quality** — slippage histogram, spread distribution, fill rate, latency percentiles.
5. **Risk Monitor** — current exposure, daily drawdown gauge, remaining trade budget, risk parameter editor.
6. **Configuration** — edit risk parameters, strategy enable/disable toggles, Telegram settings, MT5 connection config.
7. **System Health** — uptime, last heartbeat, error log, MT5 terminal status.

### 8.2 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14 + Tailwind CSS + shadcn/ui |
| Charts | Recharts or Lightweight Charts |
| Data | Supabase JS client + Realtime subscriptions |
| Auth | Supabase Auth (email/password, single admin user) |
| Hosting | Vercel (free tier) or same VPS as bridge |

---

## 9. Deployment Architecture

### 9.1 VPS Requirements

| Spec | Minimum | Recommended |
|---|---|---|
| OS | Windows Server 2019 | Windows Server 2022 |
| CPU | 2 vCPU | 4 vCPU |
| RAM | 4 GB | 8 GB |
| Storage | 40 GB SSD | 80 GB SSD |
| Network | 100 Mbps | 1 Gbps |
| Location | Near broker server | London / New York (depending on broker) |
| Uptime | 99.5% | 99.9% |

### 9.2 Services on VPS

- **MetaTrader 5 Terminal** — running 24/5, logged into broker, EA attached to XAUUSD M15 chart.
- **Python Bridge Server** — `uvicorn` managed by NSSM/Windows Service or `pm2-windows`, auto-restart on crash.
- **Supabase Client** — reads/writes to hosted Supabase instance.
- **Telegram Bot** — integrated into bridge server (no separate process).
- **Optional:** Nginx / Cloudflare Tunnel reverse proxy with SSL for webhook endpoint security.

### 9.3 Security

- Webhook endpoint protected by shared secret in request body (not URL).
- HTTPS/TLS on webhook endpoint (required by TradingView).
- IP whitelist for admin dashboard access.
- Supabase Row Level Security (RLS) enabled.
- No trading credentials stored in code; MT5 login handled by terminal.
- Rate limiting on webhook endpoint (max 10 requests/second).

---

## 10. Development Phases & Timeline

> **Bootstrap mapping:** the 4 PRD phases below map to milestones **M1–M4**. Two new milestones **M0 (Bootstrap)** and **M5 (Live & Handover)** wrap them. See [`../../planning/master-roadmap.md`](../../planning/master-roadmap.md).

### 10.1 Phase 1 — Foundation (Week 1–2) → **M1**

| Task | Output | Est. Hours |
|---|---|---|
| Pine Script strategy for XAUUSD SMC | Working strategy with alert conditions | 8 |
| Webhook bridge server (FastAPI) | POST endpoint, validation, logging | 6 |
| MT5 Python connector | Read balance, open/close orders programmatically | 6 |
| Signal-to-execution pipeline | End-to-end: TV alert to MT5 order on demo | 8 |
| Supabase schema + signal logging | Tables created, signals logged | 4 |
| Basic Telegram notifications | Alerts for signals and executions | 3 |

### 10.2 Phase 2 — Risk Engine + Management (Week 3–4) → **M2**

| Task | Output | Est. Hours |
|---|---|---|
| Full risk engine in bridge | All rules from §5 implemented | 10 |
| Deduplication and signal expiry | No duplicate or stale executions | 4 |
| EA hybrid mode (strategy + bridge) | EA accepts both local and external signals | 8 |
| Position management (BE, trail, partial) | Per-ticket tracking, all management modes | 6 |
| Execution feedback loop | EA reports fill, slippage back to bridge | 5 |
| Error handling and retry logic | Graceful handling of all failure modes | 6 |

### 10.3 Phase 3 — Dashboard + Monitoring (Week 5–6) → **M3**

| Task | Output | Est. Hours |
|---|---|---|
| Admin dashboard (Next.js) | All pages from §8 built | 16 |
| Real-time position and P&L display | Live updates via Supabase Realtime | 6 |
| Execution quality analytics | Slippage, spread, latency charts | 6 |
| Configuration UI | Edit risk params, toggle strategies live | 5 |
| Enhanced Telegram (daily reports, alerts) | Formatted reports, error escalation | 4 |

### 10.4 Phase 4 — Hardening + Live (Week 7–8) → **M4 + M5**

| Task | Output | Est. Hours |
|---|---|---|
| Demo forward testing (2 weeks minimum) | Trade log, execution quality report | Continuous |
| Stress testing (rapid signals, disconnects) | System handles edge cases gracefully | 8 |
| VPS deployment + SSL + monitoring | Production-ready deployment | 6 |
| Documentation (setup guide, runbook) | Operator can deploy and troubleshoot | 5 |
| Live deployment (small size) | First real trades with monitoring | 4 |

---

## 11. Success Metrics & KPIs

| Metric | Target | Measurement |
|---|---|---|
| Signal-to-execution latency | < 2 seconds (95th percentile) | Timestamp diff: TV alert to MT5 fill |
| Execution fill rate | > 95% of valid signals filled | Filled / (Total - Rejected by risk) |
| Average slippage | < 3 points on XAUUSD | `abs(fill_price - signal_entry)` |
| System uptime | > 99.5% during market hours | Monitoring heartbeat checks |
| Risk rule compliance | 100% — zero breaches | Audit log of all risk checks |
| Signal deduplication | Zero duplicate executions | Count of duplicate signals caught |
| Daily report delivery | 100% on trading days | Telegram delivery confirmation |

---

## 12. Cost Estimate

### 12.1 Development Cost

| Item | Hours | Notes |
|---|---|---|
| Phase 1 — Foundation | 35 | Solo dev (AI-assisted), Week 1–2 |
| Phase 2 — Risk Engine | 39 | Solo dev (AI-assisted), Week 3–4 |
| Phase 3 — Dashboard | 37 | Solo dev (AI-assisted), Week 5–6 |
| Phase 4 — Hardening | 23+ | Solo dev (AI-assisted), Week 7–8 |
| **Total development** | **~134 hours** | Self-built, 8 weeks |

### 12.2 Monthly Operating Costs

| Service | Provider | Monthly Cost |
|---|---|---|
| Windows VPS (4 vCPU, 8GB) | Contabo / Hetzner / DigitalOcean | $15–30 USD |
| Supabase (Free tier) | Supabase | $0 (up to 500MB, 50K MAU) |
| TradingView Pro+ | TradingView (for webhooks) | $25–50 USD |
| Domain + SSL | Cloudflare (free SSL) | $10/year |
| Telegram Bot | Telegram | Free |
| **Total monthly** | — | **$40–80 USD** |

---

## 13. Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| VPS downtime during market hours | High | Low | Auto-restart services, UptimeRobot monitoring, Telegram alert on heartbeat failure |
| MT5 terminal disconnects from broker | High | Medium | EA auto-reconnect, bridge detects via health check, Telegram critical alert |
| TradingView webhook fails/delays | Medium | Low | Signal expiry window, log all attempts, fallback to EA standalone mode |
| Incorrect lot sizing causing oversized positions | Critical | Low | Dual-layer risk check (bridge + EA), hard lot cap, daily loss kill switch |
| Stale/duplicate signals executed | Medium | Medium | Timestamp expiry (120s), dedup by signal hash, min 5-min gap between trades |
| Strategy generates poor signals in live | High | Medium | Demo forward test 2+ weeks, daily review, strategy disable toggle in dashboard |
| Webhook endpoint compromised | High | Low | Shared secret auth, rate limiting, IP allowlist, HTTPS only |

---

## 14. Future Scope (v2.0+)

- **Multi-account execution:** fan out signals to multiple MT5 accounts with independent risk profiles.
- **Multi-symbol support:** extend beyond XAUUSD to forex pairs, indices, crypto CFDs.
- **Strategy marketplace:** allow multiple Pine strategies to send signals, each with its own risk allocation.
- **ML signal filtering:** train a model on execution quality data to auto-adjust confidence thresholds.
- **Mobile app:** React Native app for monitoring and manual override on the go.
- **Backtesting integration:** replay historical signals through the bridge to validate risk engine behavior.
- **Copy trading:** expose signals via API for other users to subscribe (white-label potential).

---

## Appendix A — Example TradingView Alert Message

The following is configured in TradingView alert settings as the webhook message body. Placeholders like `{{strategy.order.action}}` are replaced by TradingView at alert time:

```json
{
  "action": "{{strategy.order.action}}",
  "symbol": "XAUUSD",
  "entry": {{close}},
  "sl": {{plot("SL")}},
  "tp": {{plot("TP")}},
  "strategy_id": "smc_lo_v1",
  "timeframe": "15",
  "confidence": 0.8,
  "secret": "YOUR_SECRET",
  "timestamp": "{{timenow}}"
}
```

## Appendix B — MT5 Python Bridge Example

Minimal Python script that receives commands and places MT5 orders:

```python
import MetaTrader5 as mt5
from fastapi import FastAPI, Request

app = FastAPI()
mt5.initialize()

@app.post("/execute")
async def execute(request: Request):
    cmd = await request.json()
    # Validate, calculate lot, place order
    # Return fill result
```

## Appendix C — Recommended Broker Requirements

- MT5 platform support (not MT4-only).
- XAUUSD with tight spreads (< 30 points during London session).
- No restrictions on EA / automated trading.
- Hedging account mode supported.
- Reliable server uptime and execution speed.

---

**END OF DOCUMENT**
