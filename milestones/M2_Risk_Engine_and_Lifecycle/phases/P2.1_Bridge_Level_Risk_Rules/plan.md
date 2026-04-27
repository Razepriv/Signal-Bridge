# P2.1 — Bridge-Level Risk Rules (plan)

## Purpose

Implement all 10 bridge-level risk rules from PRD §5.1. Each rule is a pure function with a unit test before any wiring into the webhook pipeline.

## Scope

### In scope
- Define `RiskRule` interface and `RiskDecision { allow|reject, reason_code }`
- Implement R1.1 max risk per trade (1% equity)
- Implement R1.2 max daily DD (3% start-of-day equity)
- Implement R1.3 max open positions (3)
- Implement R1.4 max trades per day (6)
- Implement R1.5 correlated exposure cap (2 same-direction same-pair)
- Implement R1.6 min time between trades (5 min)
- Implement R1.7 max spread (40 pts XAUUSD)
- Implement R1.8 signal expiry (120 s from alert_timestamp)
- Implement R1.9 weekend guard
- Implement R1.10 news blackout (12:00–14:30 UTC)
- Wire all rules into the webhook pipeline as a chain; rejected signals get `signals.status='REJECTED'` + reason_code

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

1. Define `RiskRule` interface and `RiskDecision { allow|reject, reason_code }`
2. Implement R1.1 max risk per trade (1% equity)
3. Implement R1.2 max daily DD (3% start-of-day equity)
4. Implement R1.3 max open positions (3)
5. Implement R1.4 max trades per day (6)
6. Implement R1.5 correlated exposure cap (2 same-direction same-pair)
7. Implement R1.6 min time between trades (5 min)
8. Implement R1.7 max spread (40 pts XAUUSD)
9. Implement R1.8 signal expiry (120 s from alert_timestamp)
10. Implement R1.9 weekend guard
11. Implement R1.10 news blackout (12:00–14:30 UTC)
12. Wire all rules into the webhook pipeline as a chain; rejected signals get `signals.status='REJECTED'` + reason_code

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
