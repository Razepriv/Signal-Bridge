# P1.2 — FastAPI Webhook Bridge Skeleton — plan

## Purpose

Stand up the **FastAPI bridge** that receives TradingView webhooks. This phase defines the HTTP surface, the request schema, the auth check, the structured logging, and the health endpoint — everything *before* the order is sent to MT5 (which is P1.3+P1.4). It produces a runnable service that accepts well-formed payloads, persists nothing yet, and returns 202 / 401 / 422 with correct semantics.

## Scope

### In scope
- FastAPI app at `bridge/app/main.py` runnable via `uvicorn bridge.app.main:app --port 8000`
- Pydantic schemas matching PRD §4.1 alert payload (`bridge/app/schemas.py`)
- Settings via `pydantic-settings` reading from `.env` (never commit secrets)
- Endpoints:
  - `POST /api/v1/webhook` — auth + validate + (stub) accept
  - `GET  /api/v1/status` — bridge OK + uptime
  - `GET  /api/v1/health/mt5` — stub returning `{"connected": false}` until P1.3
- Auth middleware: constant-time compare of `secret` field; reject `401`
- Structured logging via `structlog` with `request_id` correlation per request
- Pytest scaffolding under `bridge/tests/` with ≥80% coverage on this phase's code
- Production-ish error handling: malformed JSON → `400`, missing field → `422`, wrong secret → `401`

### Out of scope
- MT5 connection (P1.3)
- Supabase writes (P1.5)
- Telegram notification (P1.6)
- Risk engine rules (M2)
- Dedup (M2 P2.2)
- Rate limiting / TLS / IP allowlist (M4 P4.2)

## Inputs / Prereqs

- [ ] M0 P0.1: repo + Python + pre-commit + CI green
- [ ] M0 P0.2: VPS Python 3.11 ready and tunnel forwarding to localhost:8000
- [ ] `.env.example` defined; `.env` committed to 1Password (NOT git)

## Deliverables

| Path | Description |
|---|---|
| `bridge/pyproject.toml` (or update root) | Project deps: fastapi, uvicorn, pydantic, pydantic-settings, structlog, pytest, pytest-cov, httpx |
| `bridge/app/__init__.py` | Package marker |
| `bridge/app/main.py` | FastAPI app + router wiring |
| `bridge/app/schemas.py` | Pydantic models: `AlertPayload`, `WebhookResponse`, `StatusResponse` |
| `bridge/app/settings.py` | `Settings(BaseSettings)` reading from `.env` |
| `bridge/app/auth.py` | `verify_secret(payload_secret, configured_secret) -> bool` constant-time |
| `bridge/app/logging.py` | structlog config; per-request `request_id` middleware |
| `bridge/app/routes/webhook.py` | The webhook handler |
| `bridge/app/routes/health.py` | Status + MT5-health endpoints |
| `bridge/tests/conftest.py` | Pytest fixtures (test client, settings override) |
| `bridge/tests/test_webhook.py` | All P1.2 acceptance tests |
| `bridge/tests/test_schemas.py` | Schema validation edge cases |
| `bridge/tests/fixtures/sample_alerts.json` | Valid + invalid payloads |
| `.env.example` | Template with `SIGNALBRIDGE_SECRET=`, `LOG_LEVEL=INFO`, `MT5_LOGIN=` etc. |

## Task breakdown

Each task ≤ 2 hours. **Write the test in `bridge/tests/...` before the implementation** per the global TDD rule.

1. **Pyproject + deps:** add fastapi, uvicorn, pydantic v2, pydantic-settings, structlog, pytest, pytest-cov, httpx; pin versions
2. **Settings module:** `Settings(BaseSettings)` with prefix `SIGNALBRIDGE_`; required field `secret`; load from `.env`
3. **Logging module:** structlog config with JSON renderer in prod, console in dev; `RequestIdMiddleware` adds `request_id` to log context
4. **Schemas:** `AlertPayload` matching PRD §4.1; strict types (`Decimal` for prices, `Literal["BUY","SELL","CLOSE","MODIFY"]` for action); `WebhookResponse`, `StatusResponse`
5. **Auth helper:** `verify_secret(provided, expected)` using `secrets.compare_digest` (constant-time)
6. **Webhook route:** wire it all together — body parse → secret check → schema validate → return `202 {accepted: true, request_id: ...}` (no DB / MT5 yet)
7. **Health routes:** `/status` returns `{ok: true, started_at, uptime_seconds}`; `/health/mt5` returns `{connected: false, reason: "not-yet-implemented"}`
8. **Tests T1–T12** (see `test.md`) — write them first, then make them pass
9. **Run locally and via M0 tunnel:** post a real TradingView-shaped payload from `curl` and confirm 202

## Dependencies

- **Upstream:** M0 done; P1.1 not strictly required (we use a fixture payload here)
- **Downstream:** P1.3 plugs the MT5 client into this bridge; P1.4 is the end-to-end test
- **External:** none (all in-process)

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Pydantic v1 vs v2 syntax confusion | Low | Medium | Pin pydantic v2; lint config blocks v1-style validators |
| `Decimal` vs `float` precision drift on prices | Medium | Medium | Use `Decimal` end-to-end; add a property test for round-trip |
| Constant-time compare misused (using `==`) | High | Medium | Test T9 explicitly probes timing-attack resistance via a benchmark |
| `.env` accidentally committed | Critical | Low | `.gitignore` + pre-commit `git-secrets` hook |
| Async/sync mismatch in route handler | Medium | Medium | All handlers are `async def`; lint rule requires it |

## Exit Criteria

1. `uvicorn bridge.app.main:app` starts cleanly on the VPS
2. `curl -X POST .../webhook -d <valid payload>` returns `202` with a `request_id`
3. `curl -X POST .../webhook -d <wrong secret>` returns `401`
4. `curl -X POST .../webhook -d <missing field>` returns `422`
5. `curl /api/v1/status` returns `200 {ok: true, ...}`
6. `pytest --cov=bridge/app --cov-fail-under=80` is green
7. All T1–T12 in [`test.md`](test.md) pass
8. No open `CRITICAL` or `HIGH` bug in [`bugs.md`](bugs.md)
9. [`report.md`](report.md) filled and signed
