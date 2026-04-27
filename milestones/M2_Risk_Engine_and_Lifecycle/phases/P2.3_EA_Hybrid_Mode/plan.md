# P2.3 — EA Hybrid Mode (plan)

## Purpose

Upgrade the MQL5 EA so it can run its own SMC strategy AND accept commands written by the bridge into a watched file. EA enforces hard risk caps regardless of source.

## Scope

### In scope
- Define on-disk command protocol: bridge writes `commands.jsonl`, EA reads, processes, marks done
- EA OnTimer reads new lines from commands.jsonl and parses each as a single command
- Implement OPEN_BUY, OPEN_SELL, CLOSE, MODIFY_SL, MODIFY_TP, STATUS
- Hard risk caps: lot ≤ SYMBOL_VOLUME_MAX, SL ≥ STOPS_LEVEL, daily loss kill, equity floor 80%
- Add unit-test harness via `MetaTrader5/MQL5` strategy tester or Python wrapper around terminal launches

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

1. Define on-disk command protocol: bridge writes `commands.jsonl`, EA reads, processes, marks done
2. EA OnTimer reads new lines from commands.jsonl and parses each as a single command
3. Implement OPEN_BUY, OPEN_SELL, CLOSE, MODIFY_SL, MODIFY_TP, STATUS
4. Hard risk caps: lot ≤ SYMBOL_VOLUME_MAX, SL ≥ STOPS_LEVEL, daily loss kill, equity floor 80%
5. Add unit-test harness via `MetaTrader5/MQL5` strategy tester or Python wrapper around terminal launches

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
