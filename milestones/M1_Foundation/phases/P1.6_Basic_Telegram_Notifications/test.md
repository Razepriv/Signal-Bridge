# P1.6 — Basic Telegram Notifications — tests

> **TDD applies.** Tests are written *before* implementation. Coverage target ≥ 80%.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit | send() POSTs to https://api.telegram.org/bot<token>/sendMessage with chat_id and text | ⚪ |
| T2 | unit | send() multiple chat_ids → multiple POSTs in parallel | ⚪ |
| T3 | unit | Telegram returns 4xx → log error, do not retry | ⚪ |
| T4 | unit | Telegram returns 5xx → log error, retry once | ⚪ |
| T5 | unit | on_signal_received composes message with strategy/symbol/direction/SL/TP | ⚪ |
| T6 | unit | on_order_executed composes message with ticket/lot/spread/slippage | ⚪ |
| T7 | integration | [live] real bot delivers a startup ping to real chat ID | ⚪ |
| T8 | manual | Trigger a test webhook → verify Telegram message arrives on operator's phone | ⚪ |

## Seed test details

### T1 — send() POSTs to https://api.telegram.org/bot<token>/sendMessage with chat_id and text

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T2 — send() multiple chat_ids → multiple POSTs in parallel

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T3 — Telegram returns 4xx → log error, do not retry

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T4 — Telegram returns 5xx → log error, retry once

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T5 — on_signal_received composes message with strategy/symbol/direction/SL/TP

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T6 — on_order_executed composes message with ticket/lot/spread/slippage

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T7 — [live] real bot delivers a startup ping to real chat ID

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T8 — Trigger a test webhook → verify Telegram message arrives on operator's phone

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
