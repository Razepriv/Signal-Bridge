# P5.1 — Operator Documentation (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Operator can rebuild the system on a fresh VPS using only operator-quickstart.md (recorded) | ⚪ |
| T2 | unit/integration | Operator finds 'restart bridge' procedure in cheatsheet within 30 s | ⚪ |
| T3 | unit/integration | Credentials rotation procedure includes webhook secret + MT5 + Supabase + Telegram | ⚪ |

### Seed test details

### T1 — Operator can rebuild the system on a fresh VPS using only operator-quickstart.md (recorded)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Operator finds 'restart bridge' procedure in cheatsheet within 30 s

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Credentials rotation procedure includes webhook secret + MT5 + Supabase + Telegram

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
