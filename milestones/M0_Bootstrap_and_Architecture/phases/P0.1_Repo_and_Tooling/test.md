# P0.1 — Repo & Tooling Bootstrap (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Pre-commit hooks reject a deliberately badly-formatted file | ⚪ |
| T2 | unit/integration | CI fails on a deliberately type-incorrect commit | ⚪ |
| T3 | unit/integration | pytest collects 0 tests but exits 0 (empty bridge/ tree) | ⚪ |
| T4 | unit/integration | git log --oneline -1 shows the bootstrap commit | ⚪ |

### Seed test details

### T1 — Pre-commit hooks reject a deliberately badly-formatted file

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — CI fails on a deliberately type-incorrect commit

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — pytest collects 0 tests but exits 0 (empty bridge/ tree)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — git log --oneline -1 shows the bootstrap commit

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
