# P2.4 — Position Management — BE / Trail / Partial (plan)

## Purpose

Add per-ticket position management modes (breakeven, trailing stop, partial close) with config-driven enable/disable per strategy.

## Scope

### In scope
- EA tracks per-ticket state in a map keyed by ticket
- Breakeven: when price moves 1×R favorable, set SL = entry
- Trailing: when price moves 1.5×R favorable, trail SL by 0.5×R
- Partial close: when price moves 1×R favorable, close 50%, BE remainder
- Config knob in strategy: which modes to enable
- Telegram notification on each state transition

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

1. EA tracks per-ticket state in a map keyed by ticket
2. Breakeven: when price moves 1×R favorable, set SL = entry
3. Trailing: when price moves 1.5×R favorable, trail SL by 0.5×R
4. Partial close: when price moves 1×R favorable, close 50%, BE remainder
5. Config knob in strategy: which modes to enable
6. Telegram notification on each state transition

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
