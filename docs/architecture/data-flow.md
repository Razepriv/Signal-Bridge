# Data Flow — End-to-End Signal Lifecycle

This document traces a signal from a Pine Script alert firing on TradingView all the way to a trade closing on MT5, with timing budgets, error paths, and storage boundaries.

---

## 1. Happy path (ASCII sequence)

```
TradingView          Bridge (FastAPI)                   MT5 Terminal     Supabase    Telegram
     │                       │                                │              │           │
  t0 │ alert fires           │                                │              │           │
     │──── HTTPS POST ────▶  │                                │              │           │
  t1 │                       │ verify secret → 200 ack        │              │           │
     │                       │ Pydantic validate              │              │           │
     │                       │ insert signals row (RECEIVED) ─┼─────────────▶│           │
  t2 │                       │ dedup check (last 60s)         │              │           │
     │                       │ risk gate (DD, OPEN, MAX/D)    │              │           │
     │                       │ spread check ◀────── mt5.symbol_info_tick()   │           │
     │                       │ enrich (rr, lot, srv ts)       │              │           │
     │                       │ status → VALIDATED ────────────┼─────────────▶│           │
  t3 │                       │ mt5.order_send() ─────────────▶│              │           │
     │                       │                          ◀── retcode + ticket │           │
     │                       │ insert executions row ─────────┼─────────────▶│           │
  t4 │                       │ status → EXECUTED ─────────────┼─────────────▶│           │
     │                       │ Telegram "Order executed" ─────┼──────────────┼─────────▶ │
  t5 │                       │                                │              │  notif    │
                                                              │              │           │
                                                              ▼              │           │
                                                        position open        │           │
                                                              │              │           │
                                                              ▼              │           │
                                                       SL or TP hits         │           │
                                                              │              │           │
                                              EA OnTradeTransaction          │           │
                                              writes trades row ─────────────▶│           │
                                              Telegram "Trade closed" ───────┼──────────▶│
```

---

## 2. Latency budget

End-to-end target (PRD §11): **< 2 seconds at p95** from `alert_timestamp` to `executed_at`.

| Hop | Target p95 | Notes |
|---|---:|---|
| TradingView → bridge (network) | 500 ms | TradingView's webhook delivery is the largest variance source. Co-locate the VPS in London or NY to minimize. |
| Bridge ingest (parse + auth + Pydantic) | 10 ms | Profile in M1 P1.2 tests. |
| Risk gate (in-memory rules + 1 spread query) | 30 ms | `mt5.symbol_info_tick()` is sub-ms; daily DD/open count come from in-memory cache refreshed each tick. |
| `mt5.order_send` round trip to broker | 200–800 ms | Broker-dependent. Track per broker in M4 P4.3. |
| Executions row write (async, off path) | n/a | Fire-and-forget; failure does not block the response. |
| Telegram notify (async, off path) | n/a | Fire-and-forget. |
| **Total bridge→fill** | **~1500 ms** | Headroom of ~500 ms vs. the 2 s p95 target. |

If we miss this budget, the suspect order is: (1) broker latency → switch broker / change colo, (2) bridge GIL contention → spawn a worker pool, (3) network hop → check VPS provider.

---

## 3. Storage boundaries

| Data | System | Owner | Retention |
|---|---|---|---|
| Raw webhook payload | Supabase `signals.raw_payload` (jsonb) | Bridge | 90 days |
| Decoded signal | Supabase `signals` (typed columns) | Bridge | 90 days |
| Execution result | Supabase `executions` | Bridge | 1 year |
| Trade lifecycle | Supabase `trades` | EA + bridge reconciler | 5 years |
| MT5 raw logs | VPS filesystem | MT5 terminal | 30 days, rotated |
| Bridge structured logs | stdout → Loki (M4) | Bridge | 14 days |
| Telegram messages | Telegram cloud | Telegram | unbounded (read by user) |

The **EA writes nothing** to Supabase directly in MVP; trade-close events are written by a bridge reconciler that polls `mt5.history_deals_get()` every 30 s. Direct EA→Supabase writes are out of scope (would require credentials in EA — explicit non-goal in PRD §9.3).

---

## 4. Failure paths

### 4.1 Webhook unauthenticated
- Bridge returns `401`; signal is **not** persisted (avoids log-flood from spammers).
- `bridge_logs` records the source IP for rate-limit decisions.

### 4.2 Validation fails (missing field, bad type)
- Bridge returns `422` with field-level errors.
- Signal row is **still written** with `status='REJECTED'` and `rejection_reason='VALIDATION_FAILED'` for forensics.

### 4.3 Risk rule violation
- Bridge returns `200` (TradingView shouldn't retry); signal row is `REJECTED` with the exact rule code (e.g., `DAILY_DD_HIT`, `MAX_OPEN_POS`).
- Telegram sends a `Warning` notification.

### 4.4 MT5 down or `order_send` fails
- Bridge returns `503` (server-side problem, TradingView may retry — but our dedup will catch the replay).
- Signal row is `FAILED` with `mt5_retcode` populated.
- Telegram sends a `Critical` notification.
- Bridge initiates `mt5.shutdown()` + `mt5.initialize()` retry loop (max 5 attempts, exponential backoff).

### 4.5 Supabase unreachable
- DB writes are fire-and-forget through a small in-process queue; if the queue backs up beyond N items, fall through to a local SQLite WAL file (`.signalbridge/state/wal.db`) for replay on reconnect.
- The trade still goes through. Operational priority is *the order*, not the audit trail.

### 4.6 Telegram unreachable
- Drop the message after one retry. Trades and DB writes are unaffected.

---

## 5. Idempotency & dedup

- Bridge computes `signal_hash = sha256(symbol + action + sl + tp + alert_timestamp + strategy_id)` on receipt.
- Unique index on `signals.signal_hash` enforces single-execution; duplicate receives short-circuit to `REJECTED status='DUPLICATE'`.
- Min-time-between-trades (5 min default) is a separate rule — even non-duplicate signals on the same pair within 5 min are rejected.

(Implemented in M2 P2.2.)

---

## 6. Timing on hold

These timings will be re-measured at each milestone and updated in this document:

- **End of M1 P1.7** — measure baseline latency (no risk engine).
- **End of M2 P2.7** — measure with full risk engine + dedup + retry path.
- **End of M4 P4.3** — production-realistic 2-week forward test.
- **End of M5 P5.3** — live with real broker.
