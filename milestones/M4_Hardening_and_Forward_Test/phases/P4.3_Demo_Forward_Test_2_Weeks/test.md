# P4.3 — Demo Forward Test (≥2 weeks) (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | F1 — ≥30 trades captured | ⚪ |
| T2 | unit/integration | F2 — Uptime ≥ 99.5% | ⚪ |
| T3 | unit/integration | F3 — Zero rule breaches | ⚪ |
| T4 | unit/integration | F4 — Avg slippage XAUUSD ≤ 5 pts | ⚪ |
| T5 | unit/integration | F5 — End-to-end p95 latency ≤ 2.5 s | ⚪ |
| T6 | unit/integration | F6 — Daily reports delivered every trading day | ⚪ |
| T7 | unit/integration | F7 — Forward test report drafted | ⚪ |

### Seed test details

### T1 — F1 — ≥30 trades captured

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — F2 — Uptime ≥ 99.5%

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — F3 — Zero rule breaches

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — F4 — Avg slippage XAUUSD ≤ 5 pts

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T5 — F5 — End-to-end p95 latency ≤ 2.5 s

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T6 — F6 — Daily reports delivered every trading day

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T7 — F7 — Forward test report drafted

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
