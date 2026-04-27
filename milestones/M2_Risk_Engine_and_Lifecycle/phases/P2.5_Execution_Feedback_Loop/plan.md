# P2.5 — Execution Feedback Loop (plan)

## Purpose

Close the loop: every fill/close on MT5 produces an executions/trades row in Supabase. Bridge reconciles missed events on a 30 s poll.

## Scope

### In scope
- EA on OnTradeTransaction: write fill details to `feedback.jsonl`
- Bridge tail-reads `feedback.jsonl` and writes executions/trades rows
- Reconciler: every 30 s, query `mt5.history_deals_get(last 5 min)` and upsert any missing rows
- On close: compute pnl_usd, rr_achieved, duration_minutes, close_reason
- Slippage and spread_at_execution captured at fill time

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

1. EA on OnTradeTransaction: write fill details to `feedback.jsonl`
2. Bridge tail-reads `feedback.jsonl` and writes executions/trades rows
3. Reconciler: every 30 s, query `mt5.history_deals_get(last 5 min)` and upsert any missing rows
4. On close: compute pnl_usd, rr_achieved, duration_minutes, close_reason
5. Slippage and spread_at_execution captured at fill time

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
