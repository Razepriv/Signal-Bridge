# P3.4 — Execution Quality Analytics (plan)

## Purpose

Slippage histogram, spread distribution, latency p50/p95/p99, fill rate over time.

## Scope

### In scope
- Aggregate over `executions` and `signals` last 7/30/90 days
- Slippage histogram (10 bins)
- Latency percentiles per strategy_id
- Fill rate = filled / (total - rejected_by_risk)
- All charts handle zero-data state gracefully

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

1. Aggregate over `executions` and `signals` last 7/30/90 days
2. Slippage histogram (10 bins)
3. Latency percentiles per strategy_id
4. Fill rate = filled / (total - rejected_by_risk)
5. All charts handle zero-data state gracefully

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
