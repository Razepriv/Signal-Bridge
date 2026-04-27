# P3.7 — M3 Integration & Stabilization (plan)

## Purpose

Cross-page integration test of the dashboard + Telegram, fix CRITICAL/HIGH bugs, exit M3.

## Scope

### In scope
- Playwright test suite: 5 happy paths + 5 edges across pages
- Lighthouse run on each page; perf score ≥ 90, a11y ≥ 90
- Triage all CRITICAL/HIGH bugs
- Update milestone-tracker.md to 🟢 Done
- Record G3 demo video

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

1. Playwright test suite: 5 happy paths + 5 edges across pages
2. Lighthouse run on each page; perf score ≥ 90, a11y ≥ 90
3. Triage all CRITICAL/HIGH bugs
4. Update milestone-tracker.md to 🟢 Done
5. Record G3 demo video

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
