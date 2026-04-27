# P2.6 — Error Handling & Retry (plan)

## Purpose

Make the bridge robust to MT5 / Supabase / Telegram outages without losing a trade or corrupting state.

## Scope

### In scope
- MT5 disconnect → exp backoff retry: 1s, 2s, 4s, 8s, 16s; on final failure mark signal FAILED + Critical Telegram
- Supabase down → fall through to local SQLite WAL (.signalbridge/state/wal.db); replay on reconnect; preserve order
- Telegram down → drop after 1 retry; trade unaffected
- Circuit breaker on MT5 client: 3 consecutive failures → open for 60 s, no requests
- All retries logged with structured context for debugging

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

1. MT5 disconnect → exp backoff retry: 1s, 2s, 4s, 8s, 16s; on final failure mark signal FAILED + Critical Telegram
2. Supabase down → fall through to local SQLite WAL (.signalbridge/state/wal.db); replay on reconnect; preserve order
3. Telegram down → drop after 1 retry; trade unaffected
4. Circuit breaker on MT5 client: 3 consecutive failures → open for 60 s, no requests
5. All retries logged with structured context for debugging

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
