# P4.4 — VPS Production Deployment (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Reboot VPS → bridge service auto-starts; MT5 logs in; Telegram 'system startup' fires | ⚪ |
| T2 | unit/integration | UptimeRobot detects a deliberate 5 min downtime and alerts within 2 min | ⚪ |
| T3 | unit/integration | Grafana dashboard shows latest 1000 bridge log lines | ⚪ |

### Seed test details

### T1 — Reboot VPS → bridge service auto-starts; MT5 logs in; Telegram 'system startup' fires

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — UptimeRobot detects a deliberate 5 min downtime and alerts within 2 min

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Grafana dashboard shows latest 1000 bridge log lines

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
