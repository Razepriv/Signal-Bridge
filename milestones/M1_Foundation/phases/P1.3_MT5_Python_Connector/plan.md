# P1.3 — MT5 Python Connector — plan

## Purpose

Build the in-process MT5 client (per ADR-0003) that the bridge uses to (a) initialize the terminal, (b) read account state — balance, equity, spread — and (c) place / close / modify market orders. Wraps `MetaTrader5` Python lib behind a small typed surface so tests can mock it cleanly.

## Scope

### In scope
- `bridge/app/mt5_client.py` with class `MT5Client`
- `MT5Client.connect()` calls `mt5.initialize(...)` with creds from settings
- `MT5Client.account_info()` returns balance / equity / margin / leverage
- `MT5Client.symbol_tick(symbol)` returns bid / ask / spread (in points)
- `MT5Client.open_market(symbol, action, lot, sl, tp, magic, comment)` returns `OrderResult { ticket, fill_price, slippage, retcode }`
- `MT5Client.close_position(ticket)` returns `CloseResult`
- `MT5Client.modify(ticket, sl=None, tp=None)` returns `ModifyResult`
- Wire `/api/v1/health/mt5` to call `MT5Client.is_connected()` (replacing the stub from P1.2)
- Tests with mocked `MetaTrader5` module via `unittest.mock.patch`

### Out of scope
- Reconnect / retry logic (M2 P2.6)
- Risk checks before order_send (M2 P2.1)
- Hybrid-mode command file (M2 P2.3)
- Trailing / breakeven (M2 P2.4)

## Inputs / Prereqs

- [ ] M0 P0.2: VPS Python 3.11 + MT5 terminal + `pip install MetaTrader5` succeeded
- [ ] M0 P0.4: demo broker credentials in 1Password
- [ ] P1.2 done — bridge runs and exposes /health/mt5

## Deliverables

| Path | Description |
|---|---|
| `bridge/app/mt5_client.py` | MT5Client class |
| `bridge/app/mt5_types.py` | Typed dataclasses: OrderResult, CloseResult, ModifyResult |
| `bridge/app/routes/health.py` (updated) | Real `/health/mt5` impl |
| `bridge/app/main.py` (updated) | Lifespan event: connect on startup, shutdown on exit |
| `bridge/tests/test_mt5_client.py` | Mock-based unit tests |
| `bridge/tests/test_mt5_integration.py` | Marked `@pytest.mark.live` — skipped in CI, run manually on VPS |

## Task breakdown

Each task ≤ 2 hours. **Write tests first** (global TDD rule).

1. Pin `MetaTrader5>=5.0.45` in pyproject; install on VPS
2. Define dataclasses in `mt5_types.py` (frozen=True; immutable per global rule)
3. Implement `MT5Client.connect()`; reads settings; calls `mt5.initialize`; raises `MT5ConnectionError` on failure
4. Implement `account_info()` — wrap `mt5.account_info()`; convert NamedTuple to dataclass
5. Implement `symbol_tick()` — wrap `mt5.symbol_info_tick()`; compute spread in points using `symbol_info().point`
6. Implement `open_market()` — build `MqlTradeRequest` for `TRADE_ACTION_DEAL`; call `mt5.order_send`; map retcode to OrderResult
7. Implement `close_position()` — `TRADE_ACTION_DEAL` with opposite type, `position` = ticket
8. Implement `modify()` — `TRADE_ACTION_SLTP`
9. Update `/health/mt5` to call `mt5.terminal_info().connected`
10. Wire FastAPI lifespan to connect on startup; structured log on success/failure
11. Write all unit tests with `MetaTrader5` mocked; verify retcode mapping in detail
12. Write a marked integration test that runs on the VPS only (uses real demo terminal)

## Dependencies

- **Upstream:** P1.2 (the bridge skeleton)
- **Downstream:** P1.4 (end-to-end uses this)
- **External:** MT5 terminal must be running and logged in to the demo account

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| `mt5.initialize` succeeds but `account_info()` returns None due to terminal still loading | Medium | Medium | Retry account_info() up to 3× with 2 s sleep on first call after connect |
| Different brokers return different retcodes for the same condition | Medium | High | Map retcodes by category (success / requote / no_money / market_closed); fall through to a generic 'broker_error' bucket |
| `MetaTrader5` lib is Windows-only — CI is Linux | Medium | High | Mock-only unit tests on CI; live integration tests run on VPS only via `pytest -m live` |
| Order_send during volatile spread spike → unfavorable fill | Medium | Medium | Spread check before open_market; deferred to M2 P2.1 — track here as known gap |

## Exit Criteria

1. `MT5Client.connect()` succeeds against demo broker on VPS
2. `/api/v1/health/mt5` returns `{connected: true, ...}` when terminal up; `false` when down
3. All P1.3 unit tests pass with mocked `MetaTrader5`
4. `pytest -m live` on VPS opens and closes a 0.01 lot demo trade successfully
5. Coverage on `bridge/app/mt5_client.py` ≥ 90% (mock-based)
6. No open `CRITICAL` or `HIGH` bug
7. `report.md` filled and signed
