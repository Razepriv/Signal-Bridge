# M1 Exit Criteria

All must be true before declaring M1 complete and starting M2.

## Functional

- [ ] **F1:** A TradingView alert on the M1 Pine strategy fires → JSON arrives at `POST /api/v1/webhook` on the bridge.
- [ ] **F2:** Bridge validates the shared secret. Wrong secret → `401`, no DB write. Correct secret → `202 Accepted`.
- [ ] **F3:** Bridge writes a `signals` row with `status='RECEIVED'`, `received_at` server-side, and the original payload in `raw_payload`.
- [ ] **F4:** Bridge calls `mt5.order_send` with the signal's `symbol`, `action`, `sl`, `tp` and the M1 fixed `lot_size` (0.01 — risk engine is M2).
- [ ] **F5:** On fill, an `executions` row is written with `ticket`, `fill_price`, `slippage`, `spread_at_execution`, `status='FILLED'`.
- [ ] **F6:** The corresponding `signals.status` transitions `RECEIVED → VALIDATED → EXECUTED` (no `REJECTED`/`FAILED` for a happy-path payload).
- [ ] **F7:** Telegram bot delivers an `Order executed` message containing ticket, symbol, direction, entry, lot, SL, TP within 5 seconds of fill.

## Non-functional

- [ ] **N1:** End-to-end p95 latency (alert_timestamp → executed_at) ≤ **3 seconds** on demo (M1 budget; M5 target is 2 s).
- [ ] **N2:** Bridge unit + integration test coverage ≥ **80%** on `bridge/` (`pytest --cov`).
- [ ] **N3:** All M1 acceptance tests in each phase's `test.md` pass.
- [ ] **N4:** No open `CRITICAL` or `HIGH` bug in any `P1.*/bugs.md`.

## Documentation

- [ ] **D1:** `docs/architecture/data-flow.md` re-reviewed and timing tables updated with M1-measured numbers.
- [ ] **D2:** Each `P1.*/report.md` filled with `Status: Done`, deliverables ✓, sign-off filled.
- [ ] **D3:** `planning/milestone-tracker.md` shows M1 as `🟢 Done`.

## Demo gate (mandatory)

- [ ] **G1:** Live demo recording (≤5 min): operator triggers a TradingView alert manually → bridge logs receipt → MT5 fills → Telegram message received → operator opens Supabase and shows the `signals` + `executions` rows. Saved to `docs/handover/m1-demo.mp4` (or linked from there).
