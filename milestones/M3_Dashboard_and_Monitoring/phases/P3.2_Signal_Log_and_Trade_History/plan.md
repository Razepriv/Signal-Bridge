# P3.2 — Signal Log + Trade History (plan)

## Purpose

Two read-only pages: a searchable/filterable signal log and a closed-trade history with equity curve.

## Scope

### In scope
- Server component reading `signals` table with pagination, search, status filter
- Trade history page with filters by symbol, strategy, date range
- Equity curve chart (Recharts or Lightweight Charts)
- Export-to-CSV button for both tables

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

1. Server component reading `signals` table with pagination, search, status filter
2. Trade history page with filters by symbol, strategy, date range
3. Equity curve chart (Recharts or Lightweight Charts)
4. Export-to-CSV button for both tables

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
