# P4.3 — Demo Forward Test (≥2 weeks) (plan)

## Purpose

Run the full system on a demo broker for at least 14 calendar days unsupervised; collect KPIs against PRD §11.

## Scope

### In scope
- Pick a demo broker with realistic XAUUSD spreads
- Configure conservative params: 0.5% per trade, 2% daily DD, 4 trades/day
- Daily review: open dashboard, scan for anomalies, log any in P4.3/bugs.md
- After 14 days: write summary report with KPIs, every issue, every fix verified

### Out of scope
- Anything not listed above; defer to the appropriate later phase.

## Inputs / Prereqs

- [ ] All upstream phases marked Done in [milestone-tracker.md](../../../../planning/milestone-tracker.md)
- [ ] Prior milestone exit criteria met
- [ ] Required vendor accounts active (see [planning/risk-register.md](../../../../planning/risk-register.md))

## Deliverables

| Path | Description |
|---|---|
| _to be filled at phase kickoff_ | _path of artefact_ |

## Task breakdown

Each task ≤ 2 hours. Ordered.

1. Pick a demo broker with realistic XAUUSD spreads
2. Configure conservative params: 0.5% per trade, 2% daily DD, 4 trades/day
3. Daily review: open dashboard, scan for anomalies, log any in P4.3/bugs.md
4. After 14 days: write summary report with KPIs, every issue, every fix verified

## Dependencies

- **Upstream:** see milestone roadmap
- **Downstream:** the phase numbered immediately after this one in the same milestone, plus `P*.7` (or `P4.5` for M4) integration phase
- **External:** see [risk-register.md](../../../../planning/risk-register.md)

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| _filled at kickoff_ | | | |

## Exit Criteria

1. All tasks above complete with code committed
2. All acceptance tests in [`test.md`](test.md) pass
3. Coverage ≥ 80% on new code
4. No open `CRITICAL` or `HIGH` bug in [`bugs.md`](bugs.md)
5. [`report.md`](report.md) filled and signed
