# P4.1 — Stress & Chaos Tests (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit/integration | S1 — 50 signals in 30 s: zero crashes, dedup correct, all risk rules applied | ⚪ |
| T2 | unit/integration | S2 — Kill MT5: bridge reconnects within 30 s, retry queue drains, one Critical Telegram | ⚪ |
| T3 | unit/integration | S3 — Supabase blackout: writes queue, reconnect → no rows lost, ordering preserved | ⚪ |
| T4 | unit/integration | S4 — Telegram blackout: dropped after 1 retry, system unaffected | ⚪ |
| T5 | unit/integration | S5 — Network partition: graceful resume within 1 alert post-restore | ⚪ |

### Seed test details

### T1 — S1 — 50 signals in 30 s: zero crashes, dedup correct, all risk rules applied

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T2 — S2 — Kill MT5: bridge reconnects within 30 s, retry queue drains, one Critical Telegram

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T3 — S3 — Supabase blackout: writes queue, reconnect → no rows lost, ordering preserved

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T4 — S4 — Telegram blackout: dropped after 1 retry, system unaffected

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`


### T5 — S5 — Network partition: graceful resume within 1 alert post-restore

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
