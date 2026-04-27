# P5.3 — Live Monitoring & Tuning (plan)

## Purpose

Tune any parameters the live data demands; capture KPI baselines against PRD §11. Bug-fixes only — no features.

## Scope

### In scope
- Daily KPI sweep: K1–K7 from M5 exit-criteria
- Tune params if K1 (latency) or K3 (slippage) are off-target
- Log every tuning change in `config_audit` + a tuning journal in P5.3/report.md
- After 7 days, compute final baselines for handover

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

1. Daily KPI sweep: K1–K7 from M5 exit-criteria
2. Tune params if K1 (latency) or K3 (slippage) are off-target
3. Log every tuning change in `config_audit` + a tuning journal in P5.3/report.md
4. After 7 days, compute final baselines for handover

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
