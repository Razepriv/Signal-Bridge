# P1.1 — Pine Script SMC Strategy (XAUUSD M15) — tests

> Pine has no native unit test framework. Tests here are a mix of (a) Pine compile-time checks, (b) TradingView UI manual tests, (c) backtest acceptance numbers, (d) alert-payload validation against the bridge schema.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | compile | Strategy compiles without errors or warnings | ⚪ |
| T2 | manual | Alert template loads in TradingView alert UI | ⚪ |
| T3 | manual | Strategy attaches to XAUUSD M15 and renders SL/TP plots | ⚪ |
| T4 | manual | Test alert fires on next signal and reaches the tunnel listener | ⚪ |
| T5 | schema | Emitted JSON validates against the (forthcoming) Pydantic schema | ⚪ |
| T6 | backtest | Backtest 2024 produces ≥ 30 trades on XAUUSD M15 | ⚪ |
| T7 | backtest | Backtest profit factor ≥ 1.0 (positive expectancy on demo numbers) | ⚪ |
| T8 | manual | Alert fires only on bar close, never intra-bar | ⚪ |

## Seed test details

### T1 — Strategy compiles cleanly

- **Given** `pine/Gold_SMC_v1.pine` open in the TradingView Pine Editor
- **When** the user clicks **Save & Add to chart**
- **Then** zero compile errors or warnings; chart loads with strategy panel visible

### T2 — Alert template loads

- **Given** the strategy attached to a XAUUSD M15 chart
- **When** the user opens the alert UI and pastes `pine/alert-template.json` into the message body
- **Then** the UI accepts the body without parse errors; placeholders highlighted

### T3 — SL/TP plots render

- **Given** strategy attached
- **When** strategy generates a signal on a historical bar
- **Then** SL and TP horizontal lines appear on the chart at the expected price levels

### T4 — Alert fires and reaches tunnel

- **Given** alert configured with webhook URL pointing to the M0 Cloudflare Tunnel
- **When** the strategy fires its next live alert
- **Then** the M0 tunnel listener receives the POST body within 5 seconds of bar close; HTTP 200

### T5 — Payload validates

- **Given** the captured POST body from T4
- **When** validated against the Pydantic schema that P1.2 will publish (or `jq`-checked for required fields in this phase)
- **Then** every required field (`action`, `symbol`, `sl`, `strategy_id`, `timeframe`, `secret`, `timestamp`) is present and well-typed

### T6 — Backtest sample size

- **Given** strategy run over XAUUSD M15 for calendar year 2024 in TV strategy tester
- **When** results computed
- **Then** total trades ≥ 30 (statistical floor)

### T7 — Backtest positive expectancy

- **Given** same backtest as T6
- **When** profit factor computed
- **Then** profit factor ≥ 1.0 (PF ≥ 1.5 preferred but not exit-blocking)

### T8 — Bar-close-only alerts

- **Given** strategy in live mode with `alert()` or `alertcondition()` configured
- **When** an intra-bar tick crosses the trigger condition
- **Then** no alert fires until that bar closes — confirmed by observing TV alert log over a 1-hour live window

## Coverage target

N/A for Pine. Backtest acceptance criteria (T6, T7) are the proxy.

## Manual test steps

For T4 specifically:

1. Attach `Gold_SMC_v1` to TradingView XAUUSD M15 chart
2. Open Alerts panel → New alert → set condition to "Order fills only" → set webhook URL to `https://<m0-tunnel>/api/v1/webhook` → paste `pine/alert-template.json` body
3. Wait for next signal (or use `Replay` mode to fire one)
4. Tail the listener log on the VPS; confirm the JSON body shows up; copy it for T5
5. Save a screenshot of the listener log to `bugs.md` for traceability
