# P5.2 — Pilot Live Deployment (Small Size) (plan)

## Purpose

Switch to a real broker account with the smallest position size the broker allows. Run for 7 calendar days. No new features in this phase.

## Scope

### In scope
- Open / fund a real broker account
- Update MT5 terminal to live login
- Reduce risk params to 0.25% per trade, 1% daily DD, 2 trades/day
- Notify owner of go-live timestamp; start the 7-day clock
- Daily review during the pilot

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

1. Open / fund a real broker account
2. Update MT5 terminal to live login
3. Reduce risk params to 0.25% per trade, 1% daily DD, 2 trades/day
4. Notify owner of go-live timestamp; start the 7-day clock
5. Daily review during the pilot

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
