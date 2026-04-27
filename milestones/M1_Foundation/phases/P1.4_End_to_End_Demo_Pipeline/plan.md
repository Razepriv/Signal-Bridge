# P1.4 — End-to-End Demo Pipeline — plan

## Purpose

Wire P1.1 (Pine alert) through P1.2 (webhook) through P1.3 (MT5 client) so that a real TradingView alert on a demo XAUUSD M15 chart triggers a real (demo) MT5 fill end-to-end. This phase is the M1 milestone's celebration moment — the proof the wires are connected.

## Scope

### In scope
- Wire the webhook handler to call `MT5Client.open_market` after auth + validation succeed
- Use a fixed `lot_size = 0.01` for M1 (no risk engine yet — that's M2)
- Translate `AlertPayload.action` to MT5 order type (`BUY`→buy, `SELL`→sell)
- Translate `entry`/`sl`/`tp` from Decimal to float for the MT5 lib (preserve precision via str)
- Capture `alert_timestamp` server-side latency on entry; log it
- Live demo recording (≤5 min) saved to `docs/handover/m1-demo.mp4`
- Latency report written to phase `report.md`

### Out of scope
- Risk gating (M2 P2.1)
- Dedup (M2 P2.2)
- Telegram (P1.6 — runs in parallel)
- Supabase write (P1.5 — runs in parallel; this phase fills the in-memory dispatch only)

## Inputs / Prereqs

- [ ] P1.1 done — Pine strategy attached to demo TV chart and emitting alerts
- [ ] P1.2 done — bridge accepts and validates webhook payloads
- [ ] P1.3 done — MT5 client opens / closes orders on demo broker
- [ ] M0 tunnel forwarding HTTPS to localhost:8000

## Deliverables

| Path | Description |
|---|---|
| `bridge/app/dispatch.py` | `dispatch_signal(payload, mt5_client) -> DispatchResult` |
| `bridge/app/routes/webhook.py` (updated) | After auth+validate, call dispatch and include the result in the response |
| `bridge/tests/test_dispatch.py` | Unit tests with mocked MT5Client |
| `bridge/tests/test_e2e_pipeline.py` | [live, VPS] fires synthetic webhooks at the running bridge and asserts MT5 fills |
| `docs/handover/m1-demo.mp4` | Live recording (≤5 min) |
| `milestones/M1_Foundation/phases/P1.4_End_to_End_Demo_Pipeline/report.md` (latency table) | Captured p50/p95/p99 latencies |

## Task breakdown

Each task ≤ 2 hours. **Write tests first** (global TDD rule).

1. Define `DispatchResult { signal_id, ticket, fill_price, slippage_pts, status, retcode }`
2. Implement `dispatch_signal(payload, mt5_client)` — calls `mt5_client.open_market(...)`
3. Update webhook handler to call `dispatch_signal` after validation; return DispatchResult in response body
4. Add `latency_ms` calc: `(now - parse(alert_timestamp)).total_seconds() * 1000`
5. Unit-test the dispatch path with `MT5Client` mocked
6. Run live integration test on VPS with real demo MT5
7. Trigger 5 manual TV alerts and capture the latency for each
8. Record the demo video; save to `docs/handover/m1-demo.mp4`

## Dependencies

- **Upstream:** P1.1, P1.2, P1.3
- **Downstream:** P1.5, P1.6 (those add storage/notify around this dispatch); P1.7 (stabilization)
- **External:** MT5 demo broker reachable; TradingView Pro+ active; M0 tunnel up

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Pine alert payload doesn't actually match Pydantic schema | High | Medium | T5 in P1.1 catches early; this phase has T-E2E that re-validates |
| MT5 broker rejects 0.01 lot (some brokers have higher minimums) | Medium | Medium | Make `lot_size` a setting; choose a broker that supports 0.01 in M0 P0.4 |
| Latency over 3 s due to broker server distance | High | Low | Co-locate VPS in the broker's region (M0 P0.2); measured here |
| TradingView's `{{timenow}}` arrives in unexpected format | Low | Low | Pydantic validator parses ISO-8601; fixture covers the actual TV format |

## Exit Criteria

1. Real TV alert → MT5 fill on demo broker (verifiable in MT5 history)
2. End-to-end p95 latency ≤ 3 s over a 5-alert sample
3. `m1-demo.mp4` recorded and saved
4. All P1.4 unit + live tests pass
5. No open `CRITICAL` or `HIGH` bug
6. `report.md` filled, including the latency table
