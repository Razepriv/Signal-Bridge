# P5.3 — Live Monitoring & Tuning (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | K1 latency p95 ≤ 2.0 s | ⚪ |
| T2 | unit/integration | K2 fill rate ≥ 95% | ⚪ |
| T3 | unit/integration | K3 slippage XAUUSD ≤ 3 pts | ⚪ |
| T4 | unit/integration | K4 uptime ≥ 99.5% | ⚪ |
| T5 | unit/integration | K5 risk-rule compliance 100% | ⚪ |
| T6 | unit/integration | K6 dedup zero | ⚪ |
| T7 | unit/integration | K7 daily reports 100% | ⚪ |

### Seed test details

### T1 — K1 latency p95 ≤ 2.0 s

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — K2 fill rate ≥ 95%

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — K3 slippage XAUUSD ≤ 3 pts

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — K4 uptime ≥ 99.5%

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T5 — K5 risk-rule compliance 100%

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T6 — K6 dedup zero

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T7 — K7 daily reports 100%

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
