# P0.4 — Account & Vendor Procurement (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | TradingView account can post a webhook to a public URL | ⚪ |
| T2 | unit/integration | Telegram bot can send a test message to the recorded chat ID | ⚪ |
| T3 | unit/integration | Supabase SQL editor accepts a `select 1` query | ⚪ |
| T4 | unit/integration | Cloudflare DNS resolves the domain and serves a valid TLS cert | ⚪ |

### Seed test details

### T1 — TradingView account can post a webhook to a public URL

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Telegram bot can send a test message to the recorded chat ID

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Supabase SQL editor accepts a `select 1` query

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Cloudflare DNS resolves the domain and serves a valid TLS cert

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
