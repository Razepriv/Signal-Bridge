# P1.3 — MT5 Python Connector — tests

> **TDD applies.** Tests are written *before* implementation. Coverage target ≥ 80%.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit | connect() success → MT5Client.is_connected() true | ⚪ |
| T2 | unit | connect() failure → raises MT5ConnectionError with retcode | ⚪ |
| T3 | unit | account_info returns balance/equity/margin from a mocked NamedTuple | ⚪ |
| T4 | unit | symbol_tick computes spread = (ask - bid) / point correctly | ⚪ |
| T5 | unit | open_market BUY → builds MqlTradeRequest with type=ORDER_TYPE_BUY | ⚪ |
| T6 | unit | open_market success retcode 10009 → OrderResult.status='FILLED' | ⚪ |
| T7 | unit | open_market retcode 10006 (requote) → OrderResult.status='REQUOTE' | ⚪ |
| T8 | unit | open_market retcode 10019 (no money) → OrderResult.status='REJECTED' | ⚪ |
| T9 | unit | close_position uses TRADE_ACTION_DEAL with opposite type | ⚪ |
| T10 | unit | modify(ticket, sl=...) sends TRADE_ACTION_SLTP | ⚪ |
| T11 | integration | [live, VPS] full happy-path 0.01 lot BUY+CLOSE on demo XAUUSD | ⚪ |
| T12 | integration | [live, VPS] /health/mt5 transitions correctly when terminal restarted | ⚪ |

## Seed test details

### T1 — connect() success → MT5Client.is_connected() true

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T2 — connect() failure → raises MT5ConnectionError with retcode

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T3 — account_info returns balance/equity/margin from a mocked NamedTuple

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T4 — symbol_tick computes spread = (ask - bid) / point correctly

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T5 — open_market BUY → builds MqlTradeRequest with type=ORDER_TYPE_BUY

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T6 — open_market success retcode 10009 → OrderResult.status='FILLED'

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T7 — open_market retcode 10006 (requote) → OrderResult.status='REQUOTE'

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T8 — open_market retcode 10019 (no money) → OrderResult.status='REJECTED'

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T9 — close_position uses TRADE_ACTION_DEAL with opposite type

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T10 — modify(ticket, sl=...) sends TRADE_ACTION_SLTP

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T11 — [live, VPS] full happy-path 0.01 lot BUY+CLOSE on demo XAUUSD

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T12 — [live, VPS] /health/mt5 transitions correctly when terminal restarted

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
