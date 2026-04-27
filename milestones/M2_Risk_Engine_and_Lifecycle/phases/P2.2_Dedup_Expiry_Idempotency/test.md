# P2.2 — Dedup, Expiry, Idempotency (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | Same payload sent twice within 60 s → second returns 409, no second order | ⚪ |
| T2 | unit/integration | Same payload after 60 s → still rejected by min-time-between-trades (R1.6) | ⚪ |
| T3 | unit/integration | Replay with edited timestamp but same body fields → caught by signal_hash mismatch handling | ⚪ |
| T4 | unit/integration | Clock skew of ±10 s between TV and bridge → still accepts non-stale signals | ⚪ |

### Seed test details

### T1 — Same payload sent twice within 60 s → second returns 409, no second order

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — Same payload after 60 s → still rejected by min-time-between-trades (R1.6)

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — Replay with edited timestamp but same body fields → caught by signal_hash mismatch handling

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — Clock skew of ±10 s between TV and bridge → still accepts non-stale signals

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
