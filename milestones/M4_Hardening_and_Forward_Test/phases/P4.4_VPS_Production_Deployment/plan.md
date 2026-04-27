# P4.4 — VPS Production Deployment (plan)

## Purpose

Deploy the bridge as a real Windows service that survives reboots, plus monitoring and log aggregation.

## Scope

### In scope
- Install NSSM; create `signalbridge` Windows service running uvicorn
- MT5 terminal auto-launch on boot via Task Scheduler; auto-login script
- Deploy dashboard to Vercel with production env vars
- Set up UptimeRobot to ping `/api/v1/status` every minute
- Deploy Loki+Grafana (Docker) for structured log aggregation

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

1. Install NSSM; create `signalbridge` Windows service running uvicorn
2. MT5 terminal auto-launch on boot via Task Scheduler; auto-login script
3. Deploy dashboard to Vercel with production env vars
4. Set up UptimeRobot to ping `/api/v1/status` every minute
5. Deploy Loki+Grafana (Docker) for structured log aggregation

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
