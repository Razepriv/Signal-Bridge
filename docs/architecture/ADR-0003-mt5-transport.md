# ADR-0003 — MT5 Transport: In-Process `MetaTrader5` Python Library

**Status:** Accepted (2026-04-27)
**Deciders:** Webverse Arena (single dev)
**Context:** Milestone 0 — Bootstrap

## Context

The bridge needs to (a) read MT5 account state (balance, equity, spread, positions) and (b) send order commands (open, close, modify SL/TP). The PRD §3.2 lists three transport options between the bridge and MT5:

1. **Named pipe / TCP socket** to the EA running on the MT5 terminal.
2. **In-process** via the official `MetaTrader5` Python package on the same VPS.
3. **HTTP back-channel** where the EA polls a REST endpoint on the bridge.

ADR-0001 already locks the bridge runtime to **Python**, which makes option 2 a single `pip install MetaTrader5` away. Options 1 and 3 still require the EA to participate in the request path (write/read files, open sockets, poll), which couples bridge correctness to EA correctness on every command.

## Decision

**The bridge calls MT5 directly via the in-process `MetaTrader5` Python library.** The EA does **not** execute orders received from the bridge in MVP; the EA's role is its own standalone strategy plus broker-side risk overrides (lot caps, daily loss kill switch). The bridge is the only component issuing `order_send` calls.

Once M2 P2.3 introduces "hybrid mode," the EA will also accept commands written to a local file by the bridge, but **only as a redundant path** — the primary path remains in-process Python.

## Rationale

| Criterion | In-process Python | Pipe/Socket via EA | Polling REST | Decision |
|---|---|---|---|---|
| Latency | sub-ms | 5–50 ms (EA polling cycle) | 50–500 ms | ✅ In-process |
| Reliability | one process to monitor | bridge + EA must both be healthy | bridge + EA + network loop | ✅ In-process |
| Order correctness | direct `MqlTradeRequest` | EA must parse JSON, build request | same | ✅ In-process |
| Test surface | mock the lib | mock pipe + EA | mock HTTP + EA | ✅ In-process |
| Operational complexity | install pkg + login terminal | + EA file watch + retries | + heartbeat + reconnect | ✅ In-process |
| MQL5 risk override | EA still runs and enforces caps | same | same | Tied |

## Consequences

**Positive**

- The lowest-latency path the platform allows.
- The bridge owns one source of truth for what was sent to the broker.
- Tests can mock `MetaTrader5` cleanly (single import surface).
- Failures are localized: if MT5 is down, `mt5.initialize()` fails fast at startup; if the broker rejects an order, `mt5.order_send` returns an explicit retcode we can map to a Telegram alert.

**Negative / accepted trade-offs**

- The bridge process must run on the *same Windows VPS* as the MT5 terminal (the `MetaTrader5` package is Windows-only and assumes a local terminal). Locks deployment topology to a single Windows host. Acceptable: PRD §9.1 already mandates this.
- If the bridge crashes mid-order, we may lose the in-flight result. Mitigation: every dispatch writes a `signals` row with `status='DISPATCHED'` *before* `order_send` is called, then transitions to `EXECUTED` / `FAILED` after. On restart, `DISPATCHED` rows older than 30s are reconciled by scanning MT5 history for matching tickets.
- Hybrid mode (M2 P2.3) doubles the surface: file-watch path in EA + in-process path. Tests must cover both.

## Alternatives considered

- **TCP socket (bridge ↔ EA).** Rejected: doubles failure modes (socket open, EA OnTimer cycle, JSON parse). Acceptable as a *secondary* fallback in M2 P2.3.
- **Polling REST (EA polls bridge).** Rejected: latency is the dominant failure mode for this product, and polling adds it on the critical path.
- **MetaApi cloud connector.** Rejected: adds a vendor on the trade path, adds latency, and conflicts with our self-hosted constraint.

## Supersedes / superseded by

- Supersedes: nothing.
- Superseded by: nothing (current).

## References

- PRD §3.2 (Communication Protocol) — [`../PRD/SignalBridge_PRD_v1.md`](../PRD/SignalBridge_PRD_v1.md#32-communication-protocol)
- PRD §4.3 (Component 3 — MT5 EA) — same file
- ADR-0001 (Bridge runtime)
