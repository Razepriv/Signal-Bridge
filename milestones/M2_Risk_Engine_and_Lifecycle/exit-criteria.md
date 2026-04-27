# M2 Exit Criteria

All must be true before declaring M2 complete and starting M3.

## Bridge-level risk rules (PRD §5.1)

- [ ] **R1.1** Risk per trade > 1% of equity → reject with `RISK_PER_TRADE_EXCEEDED`
- [ ] **R1.2** Daily DD ≥ 3% → halt all signals for the rest of the UTC trading day
- [ ] **R1.3** > 3 open positions → reject with `MAX_OPEN_POSITIONS`
- [ ] **R1.4** > 6 trades on the day → reject with `MAX_TRADES_PER_DAY`
- [ ] **R1.5** Same direction on same pair already open → reject with `CORRELATED_EXPOSURE`
- [ ] **R1.6** < 5 min since last trade → reject with `MIN_TIME_BETWEEN_TRADES`
- [ ] **R1.7** Spread > 40 points on XAUUSD → reject with `MAX_SPREAD_EXCEEDED`
- [ ] **R1.8** `alert_timestamp` older than 120 s → reject with `STALE_SIGNAL`
- [ ] **R1.9** Saturday or Sunday → reject with `WEEKEND_GUARD`
- [ ] **R1.10** Inside 12:00–14:30 UTC news blackout → queue and execute on close (or reject if owner config says so)

## EA-level risk rules (PRD §5.2)

- [ ] **R2.1** Lot size > `SYMBOL_VOLUME_MAX` or > configured cap → EA refuses, returns `INVALID_LOT`
- [ ] **R2.2** SL distance < `SYMBOL_TRADE_STOPS_LEVEL` → EA refuses
- [ ] **R2.3** Daily loss > configured USD → EA closes all and stops accepting commands
- [ ] **R2.4** Equity < 80% of day-start balance → EA emergency close-all
- [ ] **R2.5** Invalid prices (`ask <= 0` or `bid <= 0`) → EA refuses

## Dedup + idempotency (P2.2)

- [ ] Identical payload received twice within 60 s → first one executes, second one returns `409 DUPLICATE`
- [ ] `signals.signal_hash` UNIQUE index in place
- [ ] Replay attack (same payload, different `timestamp`) → still rejected by min-time-between-trades

## Position management (P2.4)

- [ ] Breakeven trigger: when price moves 1×R in our favor, SL moves to entry — confirmed in M2 test fixture
- [ ] Trailing: when price moves 1.5×R in favor, SL trails by 0.5×R — confirmed
- [ ] Partial close: at 1×R close 50% of position, BE the remainder — confirmed
- [ ] All three modes are togglable per-strategy via config

## Feedback loop (P2.5)

- [ ] EA writes `executions.fill_price`, `slippage`, `spread_at_execution` for every fill
- [ ] On close (TP/SL/manual), EA writes the `trades` row with `pnl_usd`, `rr_achieved`, `close_reason`
- [ ] If EA write fails, bridge reconciler picks it up within 30 s by polling MT5 history

## Error handling (P2.6)

- [ ] MT5 disconnects mid-order → bridge retries with exp backoff (5 attempts: 1s, 2s, 4s, 8s, 16s) → on final failure, signal status `FAILED` + `Critical` Telegram
- [ ] Supabase unreachable → DB writes queue to local SQLite WAL and replay on reconnect; trade still executes
- [ ] Telegram unreachable → drop after one retry; trade unaffected

## Tests + reports

- [ ] Coverage ≥ 80% on `bridge/risk_engine/` and EA risk override module
- [ ] All `P2.*/test.md` acceptance tests pass
- [ ] No open `CRITICAL` or `HIGH` bug in any `P2.*/bugs.md`
- [ ] All `P2.*/report.md` filled and signed

## Demo gate

- [ ] **G2:** Live demo (≤10 min): trigger 12 synthetic signals on a demo account that exercise every rule from R1.1 through R1.10, plus dedup, plus a deliberate MT5 disconnect during execution to verify retry. Recording saved to `docs/handover/m2-demo.mp4`.
