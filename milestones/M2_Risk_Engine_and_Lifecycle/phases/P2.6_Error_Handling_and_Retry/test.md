# P2.6 — Error Handling & Retry (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Kill MT5 between webhook and order_send → bridge retries 5 times then marks FAILED; one Telegram critical fires | ⚪ |
| T2 | unit/integration | Block outbound to Supabase for 5 min → writes queue locally; on unblock all rows present, no duplicates | ⚪ |
| T3 | unit/integration | Block outbound to Telegram for 5 min → no orders missed; Telegram message dropped silently after 1 retry | ⚪ |
| T4 | unit/integration | Circuit breaker: simulate 3 MT5 failures → next request fails fast for 60 s without hitting MT5 | ⚪ |

### Seed test details

### T1 — Kill MT5 between webhook and order_send → bridge retries 5 times then marks FAILED; one Telegram critical fires

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Block outbound to Supabase for 5 min → writes queue locally; on unblock all rows present, no duplicates

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Block outbound to Telegram for 5 min → no orders missed; Telegram message dropped silently after 1 retry

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Circuit breaker: simulate 3 MT5 failures → next request fails fast for 60 s without hitting MT5

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
