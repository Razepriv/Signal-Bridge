# ADR-0001 — Bridge Runtime: Python 3.11+ + FastAPI

**Status:** Accepted (2026-04-27)
**Deciders:** Webverse Arena (single dev)
**Context:** Milestone 0 — Bootstrap

## Context

The PRD §4.2 listed two viable bridge runtimes: **Node.js + Express** or **Python 3.11+ + FastAPI**, with Python flagged as recommended for MVP because of the official `MetaTrader5` Python integration. The user's primary success metric is **end-to-end signal-to-fill latency under 2 seconds at p95** (PRD §11), so the runtime choice is dominated by *how the bridge talks to MT5*.

Two transport models for the bridge ↔ MT5 path:

1. **In-process Python:** the FastAPI app imports `MetaTrader5` directly and calls `mt5.order_send(...)` in the same process. Single hop. ~milliseconds.
2. **Out-of-process (any runtime):** Node/Express opens a TCP socket / named pipe / HTTP call to a sidecar Python service that owns the `MetaTrader5` library. Two hops, plus serialization. ~tens of milliseconds even on localhost.

For MVP, we only need *one* webhook source (TradingView) and *one* MT5 terminal. Throughput is bounded by TradingView's webhook cadence (effectively <1/sec). The bottleneck is single-request latency, not concurrency.

## Decision

**Use Python 3.11+ with FastAPI for the bridge runtime.** The bridge will use the in-process `MetaTrader5` Python integration (see ADR-0003) and run as a single `uvicorn` worker on the same Windows VPS as the MT5 terminal.

## Rationale

| Criterion | Python + FastAPI | Node.js + Express | Decision |
|---|---|---|---|
| Latency to MT5 | In-process, sub-ms | Cross-process, +5–20 ms | ✅ Python |
| Webhook ingest perf | Async (Starlette/Uvloop equivalent) — 1 req/s ceiling regardless | Async (libuv) — 1 req/s ceiling regardless | Tied |
| MT5 lib quality | Official, well-maintained | Community Node bindings, stale/incomplete | ✅ Python |
| Pydantic validation | Native, declarative | Need Zod/io-ts | ✅ Python |
| Dev experience | Type hints, FastAPI auto-OpenAPI | Express needs more glue | ✅ Python |
| Deployment | `uvicorn` + NSSM/Windows Service | `pm2-windows` | Tied |
| Single-language stack | All Python except EA(MQL5) and dashboard(JS) | Two languages on backend | ✅ Python |

## Consequences

**Positive**

- One language across bridge, tests, scripts, and ops glue.
- Lowest possible bridge↔MT5 latency without any IPC.
- Pydantic gives us schema validation on the wire and in the DB layer for free.
- FastAPI's auto-generated OpenAPI doc accelerates the dashboard's API integration in M3.

**Negative / accepted trade-offs**

- The bridge is single-process, single-language — a future high-throughput multi-account world (v2.0) may need to refactor the MT5 client out into a worker service. Acceptable: out of MVP scope.
- The bridge cannot share Node.js / npm tooling with the dashboard. Acceptable: dashboard is independent.
- GIL contention is a non-issue at <1 req/s; if cadence rises (e.g., M3 high-frequency strategies), we'll spawn a worker pool. Tracked in [risk-register.md](../../planning/risk-register.md) as `R-04 Throughput ceiling`.

## Alternatives considered

- **Node.js + Express + Python sidecar.** Rejected: adds a hop on the critical path with no offsetting benefit at MVP scale.
- **Go.** Rejected: no first-party `MetaTrader5` lib, would require socket bridge to a Python or C++ MT5 shim.

## Supersedes / superseded by

- Supersedes: nothing.
- Superseded by: nothing (current).

## References

- PRD §4.2 (Bridge tech stack table) — [`../PRD/SignalBridge_PRD_v1.md`](../PRD/SignalBridge_PRD_v1.md#42-component-2--bridge-server-signalbridge-api)
- PRD §11 (Latency KPI) — same file
- ADR-0003 (MT5 transport)
