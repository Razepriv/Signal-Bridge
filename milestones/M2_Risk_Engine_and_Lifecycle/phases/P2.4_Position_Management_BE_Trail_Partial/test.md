# P2.4 — Position Management — BE / Trail / Partial (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Long XAUUSD with SL 50 pts, price moves +50 pts → SL moves to entry (BE) | ⚪ |
| T2 | unit/integration | Long XAUUSD with SL 50 pts, price moves +75 pts → SL trails at -25 pts behind | ⚪ |
| T3 | unit/integration | Long XAUUSD with SL 50 pts, price moves +50 pts → 50% closed, remainder BE | ⚪ |
| T4 | unit/integration | All three modes can be enabled simultaneously without conflict | ⚪ |

### Seed test details

### T1 — Long XAUUSD with SL 50 pts, price moves +50 pts → SL moves to entry (BE)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Long XAUUSD with SL 50 pts, price moves +75 pts → SL trails at -25 pts behind

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Long XAUUSD with SL 50 pts, price moves +50 pts → 50% closed, remainder BE

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — All three modes can be enabled simultaneously without conflict

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
