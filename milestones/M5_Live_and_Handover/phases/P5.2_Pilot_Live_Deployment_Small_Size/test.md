# P5.2 — Pilot Live Deployment (Small Size) (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | First live trade fills within target latency | ⚪ |
| T2 | unit/integration | P&L tracked correctly across the 7 days | ⚪ |
| T3 | unit/integration | Daily Telegram reports continue uninterrupted | ⚪ |
| T4 | unit/integration | Zero CRITICAL incidents (intentional drills don't count) | ⚪ |

### Seed test details

### T1 — First live trade fills within target latency

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — P&L tracked correctly across the 7 days

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Daily Telegram reports continue uninterrupted

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Zero CRITICAL incidents (intentional drills don't count)

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
