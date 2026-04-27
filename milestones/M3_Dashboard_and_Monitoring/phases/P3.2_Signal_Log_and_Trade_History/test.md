# P3.2 — Signal Log + Trade History (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Signal log shows last 50 signals with correct status badges | ⚪ |
| T2 | unit/integration | Filter by status=REJECTED reduces the list to just rejections | ⚪ |
| T3 | unit/integration | Trade history equity curve matches the sum of `pnl_usd` over time | ⚪ |
| T4 | unit/integration | CSV export contains the same rows as on-screen | ⚪ |

### Seed test details

### T1 — Signal log shows last 50 signals with correct status badges

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Filter by status=REJECTED reduces the list to just rejections

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Trade history equity curve matches the sum of `pnl_usd` over time

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — CSV export contains the same rows as on-screen

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
