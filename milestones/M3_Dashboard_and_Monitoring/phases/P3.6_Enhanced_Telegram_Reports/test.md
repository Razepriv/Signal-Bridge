# P3.6 — Enhanced Telegram Reports (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Daily report fires at 22:00 UTC even with zero trades | ⚪ |
| T2 | unit/integration | Inline 'Halt all' button → bridge sets `system.halted=true`; next signal rejected | ⚪ |
| T3 | unit/integration | Critical event always delivered within 5 s regardless of throttling | ⚪ |
| T4 | unit/integration | 20 Info events in 1 minute → only 1 message delivered (bucketed) | ⚪ |

### Seed test details

### T1 — Daily report fires at 22:00 UTC even with zero trades

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Inline 'Halt all' button → bridge sets `system.halted=true`; next signal rejected

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Critical event always delivered within 5 s regardless of throttling

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — 20 Info events in 1 minute → only 1 message delivered (bucketed)

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
