# M5 Exit Criteria — Final Sign-Off

All must be true before declaring the project complete and handing over.

## Live KPIs (PRD §11 targets)

Measured during P5.3 over a minimum 7 calendar days of live trading:

- [ ] **K1** Signal-to-execution latency p95 ≤ **2.0 seconds**
- [ ] **K2** Execution fill rate ≥ **95%** of valid signals
- [ ] **K3** Average slippage on XAUUSD ≤ **3 points**
- [ ] **K4** System uptime ≥ **99.5%** during market hours
- [ ] **K5** Risk-rule compliance — **100%**, zero breaches
- [ ] **K6** Signal dedup — zero duplicate executions
- [ ] **K7** Daily report delivery — **100%** on trading days

## Operational

- [ ] **O1** Pilot ran ≥ 7 calendar days with zero `CRITICAL` incidents (a `Critical` Telegram event triggered for a real failure counts; ones triggered by *intentional* drills do not)
- [ ] **O2** Operator (= owner) has restarted bridge + dashboard at least once successfully using only the runbook
- [ ] **O3** Operator has rotated the webhook secret at least once successfully
- [ ] **O4** Operator has temporarily disabled and re-enabled a strategy via the dashboard

## Handover package (P5.5)

- [ ] **H1** `docs/handover/operator-quickstart.md` exists; operator did a fresh-VPS rebuild from it (recorded video saved)
- [ ] **H2** `docs/handover/operator-cheatsheet.md` covers the 10 most common ops tasks
- [ ] **H3** `docs/handover/architecture-snapshot.pdf` frozen with handover-date system snapshot
- [ ] **H4** `docs/handover/credentials-rotation.md` complete
- [ ] **H5** `docs/handover/kpi-baseline.md` lists the live-trading numbers from K1–K7
- [ ] **H6** `docs/handover/support-window.md` defines what post-handover support is included
- [ ] **H7** `docs/handover/signoff.md` signed by developer + owner with date and final commit SHA

## Documentation hygiene

- [ ] All milestone `README.md` and `exit-criteria.md` updated with final status
- [ ] All `P*.*/report.md` marked `Done`
- [ ] No open `CRITICAL` or `HIGH` bug anywhere in the repo
- [ ] `docs/runbook/` is complete (every section listed in [docs/runbook/README.md](../../docs/runbook/README.md) is filled)
- [ ] `planning/risk-register.md` reviewed: closed risks moved to "Closed risks", remaining risks have current mitigations

## Tracker

- [ ] `planning/milestone-tracker.md` shows M0–M5 all `🟢 Done`
- [ ] Final entry in "Recent changes": handover date, final SHA, sign-off names
