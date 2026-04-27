# P5.4 — Final Acceptance & Sign-Off (plan)

## Purpose

Verify all M5 exit criteria; if all green, sign off. If anything red, loop back to P5.3 for tuning.

## Scope

### In scope
- Walk through M5 exit-criteria.md item by item
- Walk through risk-register.md; close mitigated risks
- Verify zero open CRITICAL/HIGH across the whole repo
- Owner countersigns; commit the sign-off in docs/handover/signoff.md

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

1. Walk through M5 exit-criteria.md item by item
2. Walk through risk-register.md; close mitigated risks
3. Verify zero open CRITICAL/HIGH across the whole repo
4. Owner countersigns; commit the sign-off in docs/handover/signoff.md

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
