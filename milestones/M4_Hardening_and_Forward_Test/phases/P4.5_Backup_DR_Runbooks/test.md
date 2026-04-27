# P4.5 — Backup, DR, Runbooks (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | B1 — Supabase backups + PITR enabled | ⚪ |
| T2 | unit/integration | B2 — VPS daily snapshot active | ⚪ |
| T3 | unit/integration | B3 — All credentials in operator's password manager | ⚪ |
| T4 | unit/integration | B4 — Recovery test: full rebuild from VPS snapshot in ≤2 hours, documented | ⚪ |

### Seed test details

### T1 — B1 — Supabase backups + PITR enabled

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — B2 — VPS daily snapshot active

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — B3 — All credentials in operator's password manager

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — B4 — Recovery test: full rebuild from VPS snapshot in ≤2 hours, documented

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
