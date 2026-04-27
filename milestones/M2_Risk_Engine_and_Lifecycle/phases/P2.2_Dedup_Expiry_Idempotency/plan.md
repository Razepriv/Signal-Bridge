# P2.2 — Dedup, Expiry, Idempotency (plan)

## Purpose

Make the bridge safe to receive the same payload twice (replay attacks, TradingView retries) without firing two orders.

## Scope

### In scope
- Define `signal_hash = sha256(symbol + action + sl + tp + alert_timestamp + strategy_id)`
- Add UNIQUE index on `signals.signal_hash` in a new migration
- On 23505 (unique violation) → return 409 + reason `DUPLICATE`
- Implement 60-second LRU cache for fast in-memory dedup (avoids DB round-trip)
- Add expiry check using `alert_timestamp` (already in P2.1 R1.8) and ensure clock-skew handled

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

1. Define `signal_hash = sha256(symbol + action + sl + tp + alert_timestamp + strategy_id)`
2. Add UNIQUE index on `signals.signal_hash` in a new migration
3. On 23505 (unique violation) → return 409 + reason `DUPLICATE`
4. Implement 60-second LRU cache for fast in-memory dedup (avoids DB round-trip)
5. Add expiry check using `alert_timestamp` (already in P2.1 R1.8) and ensure clock-skew handled

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
