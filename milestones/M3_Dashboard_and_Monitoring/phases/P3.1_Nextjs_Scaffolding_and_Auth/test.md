# P3.1 — Next.js Scaffolding + Supabase Auth (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Anonymous visit to / → redirected to /login | ⚪ |
| T2 | unit/integration | Login with operator credentials → redirected to /dashboard | ⚪ |
| T3 | unit/integration | Sign out → redirected to /login | ⚪ |
| T4 | unit/integration | Service-role key not present in client bundle (verified via build inspection) | ⚪ |

### Seed test details

### T1 — Anonymous visit to / → redirected to /login

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Login with operator credentials → redirected to /dashboard

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Sign out → redirected to /login

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Service-role key not present in client bundle (verified via build inspection)

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
