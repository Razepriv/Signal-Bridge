# P4.5 — Backup, DR, Runbooks (plan)

## Purpose

Make the system recoverable from total VPS loss in ≤2 hours, document everything an operator needs.

## Scope

### In scope
- Upgrade Supabase to Pro tier; enable PITR + daily backups
- Configure VPS provider daily image snapshot; retention ≥7 days
- Author docs/runbook/* sections defined in docs/runbook/README.md
- Author DR runbook: VPS restore from snapshot, MT5 reconnect, Supabase reattach
- Execute end-to-end DR drill on a fresh VPS; time it; document

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

1. Upgrade Supabase to Pro tier; enable PITR + daily backups
2. Configure VPS provider daily image snapshot; retention ≥7 days
3. Author docs/runbook/* sections defined in docs/runbook/README.md
4. Author DR runbook: VPS restore from snapshot, MT5 reconnect, Supabase reattach
5. Execute end-to-end DR drill on a fresh VPS; time it; document

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
