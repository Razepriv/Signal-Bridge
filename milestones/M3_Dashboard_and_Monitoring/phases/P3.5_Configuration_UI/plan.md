# P3.5 — Configuration UI (plan)

## Purpose

Edit risk parameters and toggle strategies live, with confirmation modal and audit log. No code changes required to tune the system.

## Scope

### In scope
- Form for each risk param (R1.1–R1.10) with min/max validation
- Strategy enable/disable toggles by strategy_id
- Telegram chat-target and severity-threshold settings
- Confirm modal showing diff before save
- Insert into `config_audit` on every save
- Safety lock: refuse save while market open AND DD > 1%

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

1. Form for each risk param (R1.1–R1.10) with min/max validation
2. Strategy enable/disable toggles by strategy_id
3. Telegram chat-target and severity-threshold settings
4. Confirm modal showing diff before save
5. Insert into `config_audit` on every save
6. Safety lock: refuse save while market open AND DD > 1%

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
