# P3.4 — Execution Quality Analytics (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Slippage histogram matches manually computed numbers from raw data | ⚪ |
| T2 | unit/integration | p95 latency matches `quantile(latency_ms, 0.95)` from a SQL query | ⚪ |
| T3 | unit/integration | Fill rate excludes rejections by design — verified with seeded data | ⚪ |

### Seed test details

### T1 — Slippage histogram matches manually computed numbers from raw data

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — p95 latency matches `quantile(latency_ms, 0.95)` from a SQL query

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Fill rate excludes rejections by design — verified with seeded data

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
