# P2.3 — EA Hybrid Mode (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Bridge writes OPEN_BUY → EA opens position with exact lot/SL/TP | ⚪ |
| T2 | unit/integration | Bridge writes lot 5.0 → EA refuses with INVALID_LOT (caps at 1.0) | ⚪ |
| T3 | unit/integration | Bridge writes SL too close → EA refuses with INVALID_SL | ⚪ |
| T4 | unit/integration | Daily loss > configured cap → EA closes all and stops accepting commands | ⚪ |
| T5 | unit/integration | EA's own SMC strategy still fires when no bridge command queued | ⚪ |

### Seed test details

### T1 — Bridge writes OPEN_BUY → EA opens position with exact lot/SL/TP

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Bridge writes lot 5.0 → EA refuses with INVALID_LOT (caps at 1.0)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Bridge writes SL too close → EA refuses with INVALID_SL

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Daily loss > configured cap → EA closes all and stops accepting commands

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T5 — EA's own SMC strategy still fires when no bridge command queued

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
