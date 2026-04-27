# P2.7 — M2 Integration & Stabilization (plan)

## Purpose

Integration test the full M2 surface, run the demo gate, fix all CRITICAL/HIGH bugs, and exit M2.

## Scope

### In scope
- Run end-to-end test: 12 synthetic signals exercising each rule R1.1–R1.10, plus dedup, plus a deliberate MT5 disconnect
- Measure latency p95 across the 12 signals; expect ≤ 2.5 s on demo
- Triage all CRITICAL/HIGH bugs from prior phases; close before exit
- Update planning/milestone-tracker.md to 🟢 Done
- Record G2 demo video and save to docs/handover/m2-demo.mp4

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

1. Run end-to-end test: 12 synthetic signals exercising each rule R1.1–R1.10, plus dedup, plus a deliberate MT5 disconnect
2. Measure latency p95 across the 12 signals; expect ≤ 2.5 s on demo
3. Triage all CRITICAL/HIGH bugs from prior phases; close before exit
4. Update planning/milestone-tracker.md to 🟢 Done
5. Record G2 demo video and save to docs/handover/m2-demo.mp4

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
