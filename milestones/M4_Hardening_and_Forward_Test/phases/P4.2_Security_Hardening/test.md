# P4.2 — Security Hardening (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Sec1 — All ingress over HTTPS | ⚪ |
| T2 | unit/integration | Sec2 — Webhook rate limited | ⚪ |
| T3 | unit/integration | Sec3 — TradingView IPs allowlisted | ⚪ |
| T4 | unit/integration | Sec4 — Webhook secret rotated successfully | ⚪ |
| T5 | unit/integration | Sec5 — Dashboard IP allowlisted | ⚪ |
| T6 | unit/integration | Sec6 — Supabase RLS active on all tables | ⚪ |
| T7 | unit/integration | Sec7 — git-secrets scan green | ⚪ |
| T8 | unit/integration | Sec8 — pip-audit + npm audit zero High/Critical | ⚪ |

### Seed test details

### T1 — Sec1 — All ingress over HTTPS

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Sec2 — Webhook rate limited

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Sec3 — TradingView IPs allowlisted

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Sec4 — Webhook secret rotated successfully

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T5 — Sec5 — Dashboard IP allowlisted

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T6 — Sec6 — Supabase RLS active on all tables

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T7 — Sec7 — git-secrets scan green

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T8 — Sec8 — pip-audit + npm audit zero High/Critical

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
