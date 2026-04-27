# Architecture Overview

This folder describes **how SignalBridge is built** — the moving parts, the contracts between them, and the rationale for each major technology choice.

For *what* SignalBridge does and *why* we're building it, read the [PRD](../PRD/SignalBridge_PRD_v1.md). For the work breakdown, read [`planning/master-roadmap.md`](../../planning/master-roadmap.md).

---

## Components at a glance

```
┌──────────────────┐
│  TradingView     │  ← Pine Script v6 strategy
│  Pine Strategy   │
└────────┬─────────┘
         │  HTTPS POST (JSON, shared-secret auth)
         ▼
┌──────────────────────────────────┐
│  FastAPI Bridge (Python 3.11+)   │  ← validate, dedup, risk-check, enrich
│  ├── webhook router              │
│  ├── risk engine                 │
│  ├── MT5 client                  │  ← MetaTrader5 Python lib (in-process)
│  ├── supabase client             │
│  └── telegram bot                │
└────────┬──────────────┬──────────┘
         │              │
         ▼              ▼
┌────────────┐   ┌──────────────┐
│  MT5       │   │  Supabase    │   ← signals, executions, trades, config
│  Terminal  │   │  (Postgres)  │
│  + EA      │   └──────┬───────┘
└────────────┘          │
                        ▼
              ┌──────────────────┐
              │  Next.js 14      │   ← Realtime via Supabase JS
              │  Admin Dashboard │
              └──────────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │  Telegram Bot    │
              │  (notifications) │
              └──────────────────┘
```

All components except the dashboard run on **a single Windows VPS**, co-located with the MT5 terminal. The dashboard runs on Vercel (or the same VPS, optional).

---

## Architecture Decision Records (ADRs)

The "why" behind each load-bearing choice is captured as a numbered ADR. Read them in order:

| # | Title | Decision |
|---|---|---|
| [ADR-0001](ADR-0001-bridge-runtime.md) | Bridge runtime — Python + FastAPI vs Node.js | **Python 3.11+ + FastAPI** |
| [ADR-0002](ADR-0002-database.md) | Database — Supabase vs self-hosted Postgres | **Supabase (managed Postgres)** |
| [ADR-0003](ADR-0003-mt5-transport.md) | MT5 transport — in-process Python lib vs socket/named pipe | **In-process `MetaTrader5` lib** |

When a new architecturally significant decision is made, add `ADR-NNNN-<slug>.md` here. **Never delete or edit** a superseded ADR — mark it `Superseded by ADR-XXXX` instead.

---

## Data flow

The end-to-end signal lifecycle (from a Pine alert firing to a Telegram fill confirmation) is documented in [`data-flow.md`](data-flow.md), including sequence diagrams, latency budget, and failure paths.

---

## Non-functional requirements (NFRs)

| Concern | Target | Owner component | Verified in |
|---|---|---|---|
| End-to-end latency | <2 s p95 (alert→fill) | Bridge + MT5 | M4 P4.1 stress test |
| Fill rate | >95% of valid signals | Bridge risk engine + EA | M4 P4.3 forward test |
| Slippage on XAUUSD | <3 points | EA execution path | M4 P4.3 forward test |
| Uptime | >99.5% during market hours | VPS + auto-restart + heartbeat | M4 P4.4 monitoring |
| Risk-rule compliance | 100% (zero breaches) | Bridge + EA dual layer | M2 P2.7 integration test |
| Signal dedup | Zero duplicates | Bridge `signals.hash` unique idx | M2 P2.2 |
| Daily report delivery | 100% on trading days | Telegram bot scheduler | M3 P3.6 |

These targets are reaffirmed in each milestone's `exit-criteria.md` and verified in the corresponding stabilization phase (`P*.7` or `P4.3`).

---

## Contracts (cross-component)

- **TV → Bridge:** JSON payload defined in PRD §4.1 and validated by `bridge/app/schemas.py` (Pydantic). Backwards-compatible additions allowed; field removals are breaking and require an ADR.
- **Bridge ↔ MT5:** in-process function calls via `MetaTrader5` Python lib. The bridge is the *only* component that calls MT5 — the EA reads commands written by the bridge into a watched file/socket (M2 P2.3 onward).
- **Bridge ↔ Supabase:** SQL via `supabase-py` and `asyncpg`. Schema lives in `db/migrations/*.sql` (versioned, never edited in place — always a new migration).
- **Bridge ↔ Telegram:** outbound HTTP via `python-telegram-bot` async client. Inbound commands (e.g., `/halt`) are handled in M3 P3.6.
- **Dashboard ↔ Supabase:** Realtime subscriptions (read-only) + `supabase-js` for config writes.
