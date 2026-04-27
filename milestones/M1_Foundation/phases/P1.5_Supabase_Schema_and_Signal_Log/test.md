# P1.5 — Supabase Schema + Signal Log — tests

> **TDD applies.** Tests are written *before* implementation. Coverage target ≥ 80%.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit | insert_signal writes a row with status RECEIVED | ⚪ |
| T2 | unit | update_signal_status transitions RECEIVED → VALIDATED → EXECUTED | ⚪ |
| T3 | unit | insert_execution writes ticket, fill_price, slippage, spread | ⚪ |
| T4 | unit | fire-and-forget pattern: webhook returns 202 even when supabase_client.insert hangs (timeout) | ⚪ |
| T5 | integration | [live] migration applies cleanly to a fresh Supabase project | ⚪ |
| T6 | integration | [live] RLS denies anon SELECT; allows service-role SELECT | ⚪ |
| T7 | integration | [live] full pipeline: webhook → signal row → execution row, both visible in SQL editor | ⚪ |
| T8 | integration | [live] webhook response time unchanged when DB write is slow (simulated 500ms latency) | ⚪ |

## Seed test details

### T1 — insert_signal writes a row with status RECEIVED

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T2 — update_signal_status transitions RECEIVED → VALIDATED → EXECUTED

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T3 — insert_execution writes ticket, fill_price, slippage, spread

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T4 — fire-and-forget pattern: webhook returns 202 even when supabase_client.insert hangs (timeout)

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T5 — [live] migration applies cleanly to a fresh Supabase project

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T6 — [live] RLS denies anon SELECT; allows service-role SELECT

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T7 — [live] full pipeline: webhook → signal row → execution row, both visible in SQL editor

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T8 — [live] webhook response time unchanged when DB write is slow (simulated 500ms latency)

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

## Unit / Integration / E2E split

- **Unit:** isolated, no I/O. Run on every commit.
- **Integration (`@pytest.mark.live`):** real Supabase test schema and/or live MT5 on VPS. Run pre-merge for code that needs it; pre-milestone-exit for full suite.
- **Manual:** captured into `bugs.md` (with screenshots) for traceability.

## Fixtures & test data

- See `bridge/tests/fixtures/` from P1.2; reuse where possible.
- This phase adds: _to be enumerated by implementer_

## Coverage target

- ≥ 80% line coverage on new code in this phase
- Run `pytest --cov=bridge/app --cov-fail-under=80`
