# P3.3 — Realtime Position + P&L (plan)

## Purpose

Live tile showing open positions, unrealized P&L, and account equity, updated via Supabase Realtime.

## Scope

### In scope
- Subscribe to `executions`, `trades`, `account_state` channels
- Compute unrealized P&L from open positions × current price
- Bridge writes account state heartbeat every 5 s
- Tile flashes amber on MT5 disconnect, red after 30 s

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

1. Subscribe to `executions`, `trades`, `account_state` channels
2. Compute unrealized P&L from open positions × current price
3. Bridge writes account state heartbeat every 5 s
4. Tile flashes amber on MT5 disconnect, red after 30 s

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
