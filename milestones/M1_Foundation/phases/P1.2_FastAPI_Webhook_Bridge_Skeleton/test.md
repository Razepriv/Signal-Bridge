# P1.2 — FastAPI Webhook Bridge Skeleton — tests

> **TDD applies.** Every test here is written *before* the corresponding implementation. Coverage target: ≥80% on `bridge/app/`.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit | Valid payload + correct secret → 202 with `request_id` | ⚪ |
| T2 | unit | Wrong secret → 401, no body persisted | ⚪ |
| T3 | unit | Missing required field → 422 with field path | ⚪ |
| T4 | unit | Invalid `action` enum value → 422 | ⚪ |
| T5 | unit | Malformed JSON body → 400 | ⚪ |
| T6 | unit | `entry`/`sl`/`tp` Decimal round-trip preserves precision | ⚪ |
| T7 | unit | `/api/v1/status` returns 200 + `{ok, started_at, uptime_seconds}` | ⚪ |
| T8 | unit | `/api/v1/health/mt5` returns 200 + `{connected: false, reason: ...}` (M1 stub) | ⚪ |
| T9 | unit | Auth uses constant-time compare (no early-return on prefix mismatch) | ⚪ |
| T10 | integration | Each request gets a unique `request_id` propagated to logs | ⚪ |
| T11 | integration | Webhook latency p95 < 50ms over 100 requests (no MT5 yet) | ⚪ |
| T12 | manual | Real TradingView-shaped payload via M0 tunnel returns 202 | ⚪ |

## Seed test details

### T1 — Happy path

- **Given** `Settings(secret="test_secret_123")` and a valid `AlertPayload` with `secret="test_secret_123"`
- **When** `POST /api/v1/webhook` with that body
- **Then** response status is `202`; body is `{"accepted": true, "request_id": "<uuid>"}`
- **Implemented in** `bridge/tests/test_webhook.py::test_happy_path`

### T2 — Wrong secret

- **Given** `Settings(secret="real")` and payload with `secret="wrong"`
- **When** POST to webhook
- **Then** `401`; response body `{"detail": "invalid_secret"}`; **no** signal row created (when P1.5 lands; for M1 P1.2 just check no side effects)
- **Implemented in** `bridge/tests/test_webhook.py::test_wrong_secret`

### T3 — Missing field

- **Given** payload missing `sl`
- **When** POST
- **Then** `422`; error body lists `loc: ["body", "sl"]`, `type: "missing"`
- **Implemented in** `bridge/tests/test_webhook.py::test_missing_required_field`

### T4 — Invalid action enum

- **Given** payload with `action="HOLD"` (not in BUY/SELL/CLOSE/MODIFY)
- **When** POST
- **Then** `422`; error mentions allowed values
- **Implemented in** `bridge/tests/test_webhook.py::test_invalid_action`

### T5 — Malformed JSON

- **Given** body `not-json`
- **When** POST with `Content-Type: application/json`
- **Then** `400` (FastAPI default for parse error); structured log emitted with `error="json_decode"`
- **Implemented in** `bridge/tests/test_webhook.py::test_malformed_json`

### T6 — Decimal precision

- **Given** payload with `entry=2350.123456789`
- **When** parsed by Pydantic
- **Then** stored as `Decimal("2350.123456789")` exactly (no float drift)
- **Implemented in** `bridge/tests/test_schemas.py::test_decimal_precision`

### T7 — Status endpoint

- **Given** app started at `t0`
- **When** `GET /api/v1/status` at `t0+5s`
- **Then** body `{ok: true, started_at: <iso>, uptime_seconds: 5}`
- **Implemented in** `bridge/tests/test_health.py::test_status`

### T8 — MT5 health stub

- **Given** P1.3 not yet done
- **When** `GET /api/v1/health/mt5`
- **Then** `200 {connected: false, reason: "not-yet-implemented"}`
- **Implemented in** `bridge/tests/test_health.py::test_mt5_health_stub`

### T9 — Constant-time compare

- **Given** correct secret of length N
- **When** auth tested with secrets of length N that differ at position 0 vs position N-1
- **Then** time difference between the two calls is below noise threshold (3σ); confirms `secrets.compare_digest` is in use
- **Implemented in** `bridge/tests/test_auth.py::test_constant_time_compare`

### T10 — request_id propagation

- **Given** webhook request
- **When** structured log captured via `structlog.testing.LogCapture`
- **Then** every log record from that request carries the same `request_id`
- **Implemented in** `bridge/tests/test_logging.py::test_request_id_propagation`

### T11 — Latency

- **Given** test client + 100 sequential POST requests with valid payloads
- **When** each request timed
- **Then** p95 < 50ms (the mt5/db stages are not yet wired)
- **Implemented in** `bridge/tests/test_perf.py::test_webhook_latency`

### T12 — TradingView shape (manual)

1. Start uvicorn on the VPS
2. `curl -X POST -H 'Content-Type: application/json' -d @bridge/tests/fixtures/sample_alerts/valid_buy_xauusd.json https://<m0-tunnel>/api/v1/webhook`
3. **Expected:** `202 {accepted: true, request_id: <uuid>}`

## Unit / Integration / E2E split

- **Unit (T1–T9):** in-process FastAPI `TestClient`; no network, no DB, no MT5.
- **Integration (T10, T11):** still in-process but exercises middleware + logging side-effects.
- **Manual (T12):** real network through the M0 tunnel.

## Fixtures & test data

- `bridge/tests/fixtures/sample_alerts/valid_buy_xauusd.json` — well-formed BUY
- `bridge/tests/fixtures/sample_alerts/valid_sell_xauusd.json` — well-formed SELL
- `bridge/tests/fixtures/sample_alerts/missing_sl.json` — missing required field
- `bridge/tests/fixtures/sample_alerts/wrong_secret.json` — wrong secret
- `bridge/tests/fixtures/sample_alerts/invalid_action.json` — `action="HOLD"`
- `bridge/tests/fixtures/sample_alerts/malformed.txt` — not JSON

## Coverage target

- ≥ 80% line coverage on `bridge/app/` after this phase (`pytest --cov=bridge/app --cov-fail-under=80`)
- Specifically: `auth.py`, `schemas.py`, `routes/webhook.py`, `routes/health.py` should be ≥ 95% each

## Manual test steps

For T12, save the curl output and the structured log line into `bugs.md → manual-evidence.md` for traceability.
