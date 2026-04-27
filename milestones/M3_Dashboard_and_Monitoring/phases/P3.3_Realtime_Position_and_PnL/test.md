# P3.3 — Realtime Position + P&L (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Open a position on demo MT5 → appears in tile within 2 s | ⚪ |
| T2 | unit/integration | Close it → disappears from tile, P&L moves to realized day total | ⚪ |
| T3 | unit/integration | Kill MT5 → tile flashes amber within 5 s, red within 30 s | ⚪ |

### Seed test details

### T1 — Open a position on demo MT5 → appears in tile within 2 s

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Close it → disappears from tile, P&L moves to realized day total

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Kill MT5 → tile flashes amber within 5 s, red within 30 s

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
