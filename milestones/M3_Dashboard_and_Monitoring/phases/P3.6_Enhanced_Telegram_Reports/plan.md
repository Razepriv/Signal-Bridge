# P3.6 — Enhanced Telegram Reports (plan)

## Purpose

Daily and weekly digests, severity-aware throttling so the operator's phone doesn't drown in noise.

## Scope

### In scope
- Daily report scheduled at session close UTC: trades, W/L, win rate, P&L, balance, equity, top winner/loser
- Weekly report Sun 22:00 UTC: weekly summary + slippage/latency stats + rule breach count
- Severity throttling: Info events bucketed (max 1 per 5 min); Warning unbuffered; Critical always immediate
- Inline buttons on Critical alerts: `Halt all`, `Mute 30 min`

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

1. Daily report scheduled at session close UTC: trades, W/L, win rate, P&L, balance, equity, top winner/loser
2. Weekly report Sun 22:00 UTC: weekly summary + slippage/latency stats + rule breach count
3. Severity throttling: Info events bucketed (max 1 per 5 min); Warning unbuffered; Critical always immediate
4. Inline buttons on Critical alerts: `Halt all`, `Mute 30 min`

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
