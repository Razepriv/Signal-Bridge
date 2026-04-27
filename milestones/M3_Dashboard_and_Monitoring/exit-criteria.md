# M3 Exit Criteria

All must be true before declaring M3 complete and starting M4.

## Pages live

- [ ] **D1** Dashboard Home — live P&L, open positions, recent signals, MT5 status indicator, account summary
- [ ] **D2** Signal Log — searchable / filterable table; status, latency, execution result columns
- [ ] **D3** Trade History — closed trades, P&L, RR, duration, close reason, equity curve chart
- [ ] **D4** Execution Quality — slippage histogram, spread distribution, fill rate, latency p50/p95/p99
- [ ] **D5** Risk Monitor — current exposure, daily DD gauge, remaining trade budget, risk parameter editor
- [ ] **D6** Configuration — edit risk params, toggle strategies, Telegram settings, MT5 connection config
- [ ] **D7** System Health — uptime, last heartbeat, error log, MT5 terminal status

## Realtime

- [ ] Position table updates within 2 s of MT5 fill (Supabase Realtime channel verified)
- [ ] Signal log appends in real time without manual refresh

## Auth

- [ ] Single admin user via Supabase Auth (email/password)
- [ ] Routes protected; unauthenticated users redirected to `/login`
- [ ] Service-role key never exposed to the client

## Configuration UI safety

- [ ] Risk param edits show a confirmation modal with diff before save
- [ ] Each save creates an audit log row in Supabase (`config_audit` table)
- [ ] No write succeeds while market is open *and* DD > 1% (safety lock)

## Telegram reports

- [ ] Daily report delivered at session close (UTC) with: trades, W/L, win rate, P&L, balance, equity, top loser, top winner
- [ ] Weekly report delivered Sunday 22:00 UTC with: weekly P&L, win rate, slippage stats, latency stats, rule breach count
- [ ] Severity-aware throttling: `Info` events do not flood; `Critical` always delivered immediately

## Tests + reports

- [ ] Dashboard E2E tests via Playwright (5 happy paths + 5 edge)
- [ ] Bridge tests still ≥ 80% coverage
- [ ] All `P3.*/test.md` acceptance tests pass
- [ ] No open `CRITICAL` or `HIGH` bug in any `P3.*/bugs.md`
- [ ] All `P3.*/report.md` filled and signed

## Demo gate

- [ ] **G3:** Live demo (≤10 min): operator opens dashboard, walks through all 7 pages with real data from M1+M2 testing, edits a risk parameter live, triggers a signal, watches it land in the log + position table in real time. Recording saved to `docs/handover/m3-demo.mp4`.
