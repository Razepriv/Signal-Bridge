# P0.3 — Architecture Decision Records (ADRs) (plan)

## Purpose

Lock the three load-bearing decisions (bridge runtime, database, MT5 transport) into immutable ADRs.

## Scope

### In scope
- Author ADR-0001 — bridge runtime: Python + FastAPI
- Author ADR-0002 — database: Supabase
- Author ADR-0003 — MT5 transport: in-process MetaTrader5 lib
- Cross-link ADRs from docs/architecture/README.md
- Review against PRD §3, §4.2, §6 — confirm no contradictions

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

1. Author ADR-0001 — bridge runtime: Python + FastAPI
2. Author ADR-0002 — database: Supabase
3. Author ADR-0003 — MT5 transport: in-process MetaTrader5 lib
4. Cross-link ADRs from docs/architecture/README.md
5. Review against PRD §3, §4.2, §6 — confirm no contradictions

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
