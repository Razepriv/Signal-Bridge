# P2.5 — Execution Feedback Loop (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Manual close in MT5 → `trades` row appears with `close_reason=MANUAL` | ⚪ |
| T2 | unit/integration | TP hit → close_reason=TP_HIT, pnl > 0, rr_achieved ≈ planned | ⚪ |
| T3 | unit/integration | SL hit → close_reason=SL_HIT, pnl < 0, rr_achieved ≈ -1 | ⚪ |
| T4 | unit/integration | EA crashes during close → reconciler picks it up within 30 s | ⚪ |

### Seed test details

### T1 — Manual close in MT5 → `trades` row appears with `close_reason=MANUAL`

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — TP hit → close_reason=TP_HIT, pnl > 0, rr_achieved ≈ planned

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — SL hit → close_reason=SL_HIT, pnl < 0, rr_achieved ≈ -1

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — EA crashes during close → reconciler picks it up within 30 s

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


## Unit / Integration / E2E split

- **Unit:** isolated, no I/O. Run on every commit.
- **Integration:** real Supabase test schema; mocked MT5 (`unittest.mock` on `MetaTrader5` module).
- **E2E:** demo broker, demo Telegram chat, real network. Run pre-milestone-exit.

## Fixtures & test data

- _to be defined at kickoff_

## Coverage target

- ≥ 80% line coverage on new code (`pytest --cov`)
- For dashboard work: ≥ 70% Playwright coverage on user-facing flows

## Manual test steps

For tests marked `[manual]`:

1. _to be defined at kickoff_
