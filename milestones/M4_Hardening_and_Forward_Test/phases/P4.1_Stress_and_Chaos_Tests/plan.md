# P4.1 — Stress & Chaos Tests (plan)

## Purpose

Hammer the system with adverse conditions and verify it degrades gracefully without losing trades or corrupting state.

## Scope

### In scope
- Rapid-fire 50 signals in 30 s; verify dedup + risk rules behave correctly
- Kill MT5 mid-order; verify retry + reconciliation
- Block Supabase egress for 5 min; verify local WAL replay
- Block Telegram for 5 min; verify trades unaffected
- Network partition between TV and VPS; verify graceful resume

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

1. Rapid-fire 50 signals in 30 s; verify dedup + risk rules behave correctly
2. Kill MT5 mid-order; verify retry + reconciliation
3. Block Supabase egress for 5 min; verify local WAL replay
4. Block Telegram for 5 min; verify trades unaffected
5. Network partition between TV and VPS; verify graceful resume

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
