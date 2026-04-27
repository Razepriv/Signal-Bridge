# P3.5 — Configuration UI (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Edit max trades/day from 6 to 4, save → bridge rejects the 5th trade today | ⚪ |
| T2 | unit/integration | Audit log row created with old + new value + operator email | ⚪ |
| T3 | unit/integration | Try to save during market hours with DD = 1.5% → rejected with `SAFETY_LOCK` | ⚪ |
| T4 | unit/integration | Disable a strategy → next signal from that strategy_id rejected with `STRATEGY_DISABLED` | ⚪ |

### Seed test details

### T1 — Edit max trades/day from 6 to 4, save → bridge rejects the 5th trade today

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Audit log row created with old + new value + operator email

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Try to save during market hours with DD = 1.5% → rejected with `SAFETY_LOCK`

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Disable a strategy → next signal from that strategy_id rejected with `STRATEGY_DISABLED`

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
