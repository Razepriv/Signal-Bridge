# P5.1 — Operator Documentation (plan)

## Purpose

Author every document an operator needs to keep SignalBridge running without the developer.

## Scope

### In scope
- Author docs/handover/operator-quickstart.md (zero-to-first-trade)
- Author docs/handover/operator-cheatsheet.md (10 most common ops)
- Author docs/handover/credentials-rotation.md
- Author docs/handover/support-window.md
- Author docs/runbook/* missing sections
- Cross-reference all docs from README.md

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

1. Author docs/handover/operator-quickstart.md (zero-to-first-trade)
2. Author docs/handover/operator-cheatsheet.md (10 most common ops)
3. Author docs/handover/credentials-rotation.md
4. Author docs/handover/support-window.md
5. Author docs/runbook/* missing sections
6. Cross-reference all docs from README.md

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
