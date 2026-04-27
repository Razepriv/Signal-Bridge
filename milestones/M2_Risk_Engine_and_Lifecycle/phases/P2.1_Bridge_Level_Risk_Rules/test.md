# P2.1 — Bridge-Level Risk Rules (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Risk per trade > 1% of equity → reject + Telegram warning (R1.1) | ⚪ |
| T2 | unit/integration | Daily DD ≥ 3% → halt all signals for the rest of the UTC day (R1.2) | ⚪ |
| T3 | unit/integration | > 3 open positions → queue or reject new signal (R1.3) | ⚪ |
| T4 | unit/integration | Spread > 40 points on XAUUSD → delay or reject (R1.7) | ⚪ |
| T5 | unit/integration | `alert_timestamp` older than 120 s → reject as stale (R1.8) | ⚪ |
| T6 | unit/integration | Saturday/Sunday → reject with reason `WEEKEND_GUARD` (R1.9) | ⚪ |

### Seed test details

### T1 — Risk per trade > 1% of equity → reject + Telegram warning (R1.1)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Daily DD ≥ 3% → halt all signals for the rest of the UTC day (R1.2)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — > 3 open positions → queue or reject new signal (R1.3)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Spread > 40 points on XAUUSD → delay or reject (R1.7)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T5 — `alert_timestamp` older than 120 s → reject as stale (R1.8)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T6 — Saturday/Sunday → reject with reason `WEEKEND_GUARD` (R1.9)

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
