# P1.4 — End-to-End Demo Pipeline — tests

> **TDD applies.** Tests are written *before* implementation. Coverage target ≥ 80%.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit | dispatch_signal calls mt5_client.open_market with translated action/sl/tp | ⚪ |
| T2 | unit | BUY action → MT5Client.open_market(action='BUY') | ⚪ |
| T3 | unit | SELL action → MT5Client.open_market(action='SELL') | ⚪ |
| T4 | unit | Decimal->float conversion preserves precision via str() | ⚪ |
| T5 | unit | DispatchResult populated correctly from OrderResult | ⚪ |
| T6 | unit | MT5 retcode REJECTED → DispatchResult.status='FAILED' | ⚪ |
| T7 | unit | latency_ms calculated and included in response | ⚪ |
| T8 | integration | [live, VPS] webhook receives valid payload → MT5 history shows new ticket within 3 s | ⚪ |
| T9 | integration | [live, VPS] 5 sequential alerts produce 5 distinct tickets | ⚪ |
| T10 | manual | Trigger one alert from real TV chart and screenshot the MT5 fill | ⚪ |

## Seed test details

### T1 — dispatch_signal calls mt5_client.open_market with translated action/sl/tp

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T2 — BUY action → MT5Client.open_market(action='BUY')

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T3 — SELL action → MT5Client.open_market(action='SELL')

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T4 — Decimal->float conversion preserves precision via str()

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T5 — DispatchResult populated correctly from OrderResult

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T6 — MT5 retcode REJECTED → DispatchResult.status='FAILED'

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T7 — latency_ms calculated and included in response

- **Type:** unit
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T8 — [live, VPS] webhook receives valid payload → MT5 history shows new ticket within 3 s

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T9 — [live, VPS] 5 sequential alerts produce 5 distinct tickets

- **Type:** integration
- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `bridge/tests/...`

### T10 — Trigger one alert from real TV chart and screenshot the MT5 fill

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
