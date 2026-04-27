# P0.2 — VPS & MT5 Environment (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | RDP into VPS from operator workstation succeeds | ⚪ |
| T2 | unit/integration | MT5 terminal shows logged-in account with demo balance | ⚪ |
| T3 | unit/integration | `python -c "import MetaTrader5; print(MetaTrader5.__version__)"` succeeds | ⚪ |
| T4 | unit/integration | External `curl https://<tunnel-url>/ping` returns 200 from the dummy listener | ⚪ |

### Seed test details

### T1 — RDP into VPS from operator workstation succeeds

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — MT5 terminal shows logged-in account with demo balance

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — `python -c "import MetaTrader5; print(MetaTrader5.__version__)"` succeeds

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — External `curl https://<tunnel-url>/ping` returns 200 from the dummy listener

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
