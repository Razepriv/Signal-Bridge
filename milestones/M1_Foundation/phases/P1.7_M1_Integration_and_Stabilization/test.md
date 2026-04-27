# P1.7 — M1 Integration & Stabilization — tests

> **TDD applies.** Tests are written *before* implementation. Coverage target ≥ 80%.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | integration | [live] smoke run #1 — full pipeline TV→MT5→Supabase→Telegram | ⚪ |
| T2 | integration | [live] smoke run #2 | ⚪ |
| T3 | integration | [live] smoke run #3 | ⚪ |
| T4 | integration | [live] smoke run #4 | ⚪ |
| T5 | integration | [live] smoke run #5 | ⚪ |
| T6 | integration | Bridge stays up for 24 hours unattended without restart (idle test on VPS) | ⚪ |
| T7 | manual | Owner walks through the demo video and signs off | ⚪ |

## Seed test details

### T1 — [live] smoke run #1 — full pipeline TV→MT5→Supabase→Telegram

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T2 — [live] smoke run #2

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T3 — [live] smoke run #3

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T4 — [live] smoke run #4

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T5 — [live] smoke run #5

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T6 — Bridge stays up for 24 hours unattended without restart (idle test on VPS)

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T7 — Owner walks through the demo video and signs off

- **Type:** manual
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
