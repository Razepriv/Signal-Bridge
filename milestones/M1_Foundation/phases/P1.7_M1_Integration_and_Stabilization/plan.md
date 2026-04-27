# P1.7 — M1 Integration & Stabilization — plan

## Purpose

Run the full M1 surface end-to-end, exercise the demo gate G1, fix any CRITICAL/HIGH bugs uncovered, update timing tables in data-flow.md, and close out the milestone. **No new features in this phase.**

## Scope

### In scope
- End-to-end smoke: 5 manual TV alerts → bridge → MT5 fills → Supabase rows → Telegram messages
- Latency measurements: p50, p95, p99 captured to `report.md`
- Bug triage: walk through every P1.* `bugs.md`, close all CRITICAL/HIGH
- Update `docs/architecture/data-flow.md` Section 6 with M1-measured numbers
- Update `planning/milestone-tracker.md` to 🟢 Done
- Record G1 demo video and save to `docs/handover/m1-demo.mp4` (if not already done in P1.4)

### Out of scope
- Any new feature (defer to M2)
- Performance tuning beyond fixing bugs (defer to M4 P4.1)

## Inputs / Prereqs

- [ ] P1.1 through P1.6 all marked Done
- [ ] All P1.* tests passing in CI

## Deliverables

| Path | Description |
|---|---|
| `docs/handover/m1-demo.mp4` | G1 demo recording (≤5 min) |
| `docs/architecture/data-flow.md` (updated) | M1 latency baselines filled in |
| `planning/milestone-tracker.md` (updated) | M1 marked Done |
| `milestones/M1_Foundation/phases/P1.7_M1_Integration_and_Stabilization/report.md` | Cumulative M1 report including KPI vs target table |

## Task breakdown

Each task ≤ 2 hours. **Write tests first** (global TDD rule).

1. Run end-to-end smoke 5 times; record latency numbers per run
2. Open every P1.* `bugs.md`; for each CRITICAL/HIGH, fix in code, add a test, mark FIXED
3. Re-run full pytest suite; coverage ≥ 80%
4. Update data-flow.md timing table for the 'End of M1 P1.7' row
5. Record demo video covering: TV alert → bridge log → MT5 fill → Supabase rows → Telegram message — narrated walkthrough
6. Update milestone-tracker.md status; add 'Recent changes' entry
7. Send completion message to owner

## Dependencies

- **Upstream:** All of P1.1–P1.6
- **Downstream:** M2 cannot start until this phase is Done
- **External:** Owner availability for demo review and sign-off

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Latency p95 misses the 3-second M1 budget | High | Low | Triage broker location (M0 choice) and bridge handler synchronicity; if unfixable in M1, escalate to M4 P4.1 with a documented exception |
| Multiple cross-phase bugs surface only at integration | Medium | Medium | Time-box bug fixing to 2× the original bug severity's effort; escalate beyond that |

## Exit Criteria

1. All M1 acceptance criteria from `milestones/M1_Foundation/exit-criteria.md` ✓
2. Latency p95 ≤ 3 s on demo over 5 runs
3. All P1.* `report.md` show Status: Done
4. Zero open CRITICAL/HIGH bugs across all P1.*
5. Demo video recorded and saved
6. Tracker updated
7. Owner sign-off captured in `report.md`
