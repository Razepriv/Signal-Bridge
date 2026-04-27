# P2.7 — M2 Integration & Stabilization (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | All 12 synthetic signals produce the expected rule decisions and DB rows | ⚪ |
| T2 | unit/integration | Demo gate G2 video clearly shows each rule firing with the expected reason_code | ⚪ |
| T3 | unit/integration | No open CRITICAL or HIGH bug across P2.*/bugs.md | ⚪ |
| T4 | unit/integration | Coverage ≥ 80% on bridge/risk_engine/ and EA risk override module | ⚪ |

### Seed test details

### T1 — All 12 synthetic signals produce the expected rule decisions and DB rows

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Demo gate G2 video clearly shows each rule firing with the expected reason_code

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — No open CRITICAL or HIGH bug across P2.*/bugs.md

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Coverage ≥ 80% on bridge/risk_engine/ and EA risk override module

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
