"""Populate P1.3 through P1.7 with full detail (P1.1 and P1.2 are already populated by hand)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
M1 = ROOT / "milestones" / "M1_Foundation" / "phases"

PHASES = {
    "P1.3_MT5_Python_Connector": {
        "id": "P1.3",
        "name": "MT5 Python Connector",
        "owner": "Bridge dev",
        "hours": 6,
        "purpose": (
            "Build the in-process MT5 client (per ADR-0003) that the bridge uses to (a) initialize the terminal, "
            "(b) read account state — balance, equity, spread — and (c) place / close / modify market orders. "
            "Wraps `MetaTrader5` Python lib behind a small typed surface so tests can mock it cleanly."
        ),
        "in_scope": [
            "`bridge/app/mt5_client.py` with class `MT5Client`",
            "`MT5Client.connect()` calls `mt5.initialize(...)` with creds from settings",
            "`MT5Client.account_info()` returns balance / equity / margin / leverage",
            "`MT5Client.symbol_tick(symbol)` returns bid / ask / spread (in points)",
            "`MT5Client.open_market(symbol, action, lot, sl, tp, magic, comment)` returns `OrderResult { ticket, fill_price, slippage, retcode }`",
            "`MT5Client.close_position(ticket)` returns `CloseResult`",
            "`MT5Client.modify(ticket, sl=None, tp=None)` returns `ModifyResult`",
            "Wire `/api/v1/health/mt5` to call `MT5Client.is_connected()` (replacing the stub from P1.2)",
            "Tests with mocked `MetaTrader5` module via `unittest.mock.patch`",
        ],
        "out_of_scope": [
            "Reconnect / retry logic (M2 P2.6)",
            "Risk checks before order_send (M2 P2.1)",
            "Hybrid-mode command file (M2 P2.3)",
            "Trailing / breakeven (M2 P2.4)",
        ],
        "prereqs": [
            "M0 P0.2: VPS Python 3.11 + MT5 terminal + `pip install MetaTrader5` succeeded",
            "M0 P0.4: demo broker credentials in 1Password",
            "P1.2 done — bridge runs and exposes /health/mt5",
        ],
        "deliverables": [
            ("`bridge/app/mt5_client.py`", "MT5Client class"),
            ("`bridge/app/mt5_types.py`", "Typed dataclasses: OrderResult, CloseResult, ModifyResult"),
            ("`bridge/app/routes/health.py` (updated)", "Real `/health/mt5` impl"),
            ("`bridge/app/main.py` (updated)", "Lifespan event: connect on startup, shutdown on exit"),
            ("`bridge/tests/test_mt5_client.py`", "Mock-based unit tests"),
            ("`bridge/tests/test_mt5_integration.py`", "Marked `@pytest.mark.live` — skipped in CI, run manually on VPS"),
        ],
        "tasks": [
            "Pin `MetaTrader5>=5.0.45` in pyproject; install on VPS",
            "Define dataclasses in `mt5_types.py` (frozen=True; immutable per global rule)",
            "Implement `MT5Client.connect()`; reads settings; calls `mt5.initialize`; raises `MT5ConnectionError` on failure",
            "Implement `account_info()` — wrap `mt5.account_info()`; convert NamedTuple to dataclass",
            "Implement `symbol_tick()` — wrap `mt5.symbol_info_tick()`; compute spread in points using `symbol_info().point`",
            "Implement `open_market()` — build `MqlTradeRequest` for `TRADE_ACTION_DEAL`; call `mt5.order_send`; map retcode to OrderResult",
            "Implement `close_position()` — `TRADE_ACTION_DEAL` with opposite type, `position` = ticket",
            "Implement `modify()` — `TRADE_ACTION_SLTP`",
            "Update `/health/mt5` to call `mt5.terminal_info().connected`",
            "Wire FastAPI lifespan to connect on startup; structured log on success/failure",
            "Write all unit tests with `MetaTrader5` mocked; verify retcode mapping in detail",
            "Write a marked integration test that runs on the VPS only (uses real demo terminal)",
        ],
        "deps_up": "P1.2 (the bridge skeleton)",
        "deps_down": "P1.4 (end-to-end uses this)",
        "deps_ext": "MT5 terminal must be running and logged in to the demo account",
        "risks": [
            ("`mt5.initialize` succeeds but `account_info()` returns None due to terminal still loading", "Medium", "Medium", "Retry account_info() up to 3× with 2 s sleep on first call after connect"),
            ("Different brokers return different retcodes for the same condition", "Medium", "High", "Map retcodes by category (success / requote / no_money / market_closed); fall through to a generic 'broker_error' bucket"),
            ("`MetaTrader5` lib is Windows-only — CI is Linux", "Medium", "High", "Mock-only unit tests on CI; live integration tests run on VPS only via `pytest -m live`"),
            ("Order_send during volatile spread spike → unfavorable fill", "Medium", "Medium", "Spread check before open_market; deferred to M2 P2.1 — track here as known gap"),
        ],
        "exit": [
            "`MT5Client.connect()` succeeds against demo broker on VPS",
            "`/api/v1/health/mt5` returns `{connected: true, ...}` when terminal up; `false` when down",
            "All P1.3 unit tests pass with mocked `MetaTrader5`",
            "`pytest -m live` on VPS opens and closes a 0.01 lot demo trade successfully",
            "Coverage on `bridge/app/mt5_client.py` ≥ 90% (mock-based)",
            "No open `CRITICAL` or `HIGH` bug",
            "`report.md` filled and signed",
        ],
        "tests": [
            ("unit", "connect() success → MT5Client.is_connected() true"),
            ("unit", "connect() failure → raises MT5ConnectionError with retcode"),
            ("unit", "account_info returns balance/equity/margin from a mocked NamedTuple"),
            ("unit", "symbol_tick computes spread = (ask - bid) / point correctly"),
            ("unit", "open_market BUY → builds MqlTradeRequest with type=ORDER_TYPE_BUY"),
            ("unit", "open_market success retcode 10009 → OrderResult.status='FILLED'"),
            ("unit", "open_market retcode 10006 (requote) → OrderResult.status='REQUOTE'"),
            ("unit", "open_market retcode 10019 (no money) → OrderResult.status='REJECTED'"),
            ("unit", "close_position uses TRADE_ACTION_DEAL with opposite type"),
            ("unit", "modify(ticket, sl=...) sends TRADE_ACTION_SLTP"),
            ("integration", "[live, VPS] full happy-path 0.01 lot BUY+CLOSE on demo XAUUSD"),
            ("integration", "[live, VPS] /health/mt5 transitions correctly when terminal restarted"),
        ],
    },
    "P1.4_End_to_End_Demo_Pipeline": {
        "id": "P1.4",
        "name": "End-to-End Demo Pipeline",
        "owner": "Bridge dev",
        "hours": 8,
        "purpose": (
            "Wire P1.1 (Pine alert) through P1.2 (webhook) through P1.3 (MT5 client) so that a real TradingView "
            "alert on a demo XAUUSD M15 chart triggers a real (demo) MT5 fill end-to-end. This phase is the "
            "M1 milestone's celebration moment — the proof the wires are connected."
        ),
        "in_scope": [
            "Wire the webhook handler to call `MT5Client.open_market` after auth + validation succeed",
            "Use a fixed `lot_size = 0.01` for M1 (no risk engine yet — that's M2)",
            "Translate `AlertPayload.action` to MT5 order type (`BUY`→buy, `SELL`→sell)",
            "Translate `entry`/`sl`/`tp` from Decimal to float for the MT5 lib (preserve precision via str)",
            "Capture `alert_timestamp` server-side latency on entry; log it",
            "Live demo recording (≤5 min) saved to `docs/handover/m1-demo.mp4`",
            "Latency report written to phase `report.md`",
        ],
        "out_of_scope": [
            "Risk gating (M2 P2.1)",
            "Dedup (M2 P2.2)",
            "Telegram (P1.6 — runs in parallel)",
            "Supabase write (P1.5 — runs in parallel; this phase fills the in-memory dispatch only)",
        ],
        "prereqs": [
            "P1.1 done — Pine strategy attached to demo TV chart and emitting alerts",
            "P1.2 done — bridge accepts and validates webhook payloads",
            "P1.3 done — MT5 client opens / closes orders on demo broker",
            "M0 tunnel forwarding HTTPS to localhost:8000",
        ],
        "deliverables": [
            ("`bridge/app/dispatch.py`", "`dispatch_signal(payload, mt5_client) -> DispatchResult`"),
            ("`bridge/app/routes/webhook.py` (updated)", "After auth+validate, call dispatch and include the result in the response"),
            ("`bridge/tests/test_dispatch.py`", "Unit tests with mocked MT5Client"),
            ("`bridge/tests/test_e2e_pipeline.py`", "[live, VPS] fires synthetic webhooks at the running bridge and asserts MT5 fills"),
            ("`docs/handover/m1-demo.mp4`", "Live recording (≤5 min)"),
            ("`milestones/M1_Foundation/phases/P1.4_End_to_End_Demo_Pipeline/report.md` (latency table)", "Captured p50/p95/p99 latencies"),
        ],
        "tasks": [
            "Define `DispatchResult { signal_id, ticket, fill_price, slippage_pts, status, retcode }`",
            "Implement `dispatch_signal(payload, mt5_client)` — calls `mt5_client.open_market(...)`",
            "Update webhook handler to call `dispatch_signal` after validation; return DispatchResult in response body",
            "Add `latency_ms` calc: `(now - parse(alert_timestamp)).total_seconds() * 1000`",
            "Unit-test the dispatch path with `MT5Client` mocked",
            "Run live integration test on VPS with real demo MT5",
            "Trigger 5 manual TV alerts and capture the latency for each",
            "Record the demo video; save to `docs/handover/m1-demo.mp4`",
        ],
        "deps_up": "P1.1, P1.2, P1.3",
        "deps_down": "P1.5, P1.6 (those add storage/notify around this dispatch); P1.7 (stabilization)",
        "deps_ext": "MT5 demo broker reachable; TradingView Pro+ active; M0 tunnel up",
        "risks": [
            ("Pine alert payload doesn't actually match Pydantic schema", "High", "Medium", "T5 in P1.1 catches early; this phase has T-E2E that re-validates"),
            ("MT5 broker rejects 0.01 lot (some brokers have higher minimums)", "Medium", "Medium", "Make `lot_size` a setting; choose a broker that supports 0.01 in M0 P0.4"),
            ("Latency over 3 s due to broker server distance", "High", "Low", "Co-locate VPS in the broker's region (M0 P0.2); measured here"),
            ("TradingView's `{{timenow}}` arrives in unexpected format", "Low", "Low", "Pydantic validator parses ISO-8601; fixture covers the actual TV format"),
        ],
        "exit": [
            "Real TV alert → MT5 fill on demo broker (verifiable in MT5 history)",
            "End-to-end p95 latency ≤ 3 s over a 5-alert sample",
            "`m1-demo.mp4` recorded and saved",
            "All P1.4 unit + live tests pass",
            "No open `CRITICAL` or `HIGH` bug",
            "`report.md` filled, including the latency table",
        ],
        "tests": [
            ("unit", "dispatch_signal calls mt5_client.open_market with translated action/sl/tp"),
            ("unit", "BUY action → MT5Client.open_market(action='BUY')"),
            ("unit", "SELL action → MT5Client.open_market(action='SELL')"),
            ("unit", "Decimal->float conversion preserves precision via str()"),
            ("unit", "DispatchResult populated correctly from OrderResult"),
            ("unit", "MT5 retcode REJECTED → DispatchResult.status='FAILED'"),
            ("unit", "latency_ms calculated and included in response"),
            ("integration", "[live, VPS] webhook receives valid payload → MT5 history shows new ticket within 3 s"),
            ("integration", "[live, VPS] 5 sequential alerts produce 5 distinct tickets"),
            ("manual", "Trigger one alert from real TV chart and screenshot the MT5 fill"),
        ],
    },
    "P1.5_Supabase_Schema_and_Signal_Log": {
        "id": "P1.5",
        "name": "Supabase Schema + Signal Log",
        "owner": "Bridge dev",
        "hours": 4,
        "purpose": (
            "Apply the database migrations for `signals`, `executions`, `trades` (PRD §6) and wire the bridge to "
            "log every signal received and every execution result. M1 logging is fire-and-forget — failure to "
            "write does NOT block the order."
        ),
        "in_scope": [
            "`db/migrations/0001_initial.sql` — signals, executions, trades, signal_status_enum, execution_status_enum",
            "RLS enabled (deny-all by default); service-role key has full access",
            "`bridge/app/supabase_client.py` — thin async wrapper",
            "Bridge writes a `signals` row on receive (status RECEIVED), updates to VALIDATED then EXECUTED/FAILED",
            "Bridge writes an `executions` row on fill",
            "Trades table left empty in M1 (filled in M2 P2.5 — execution feedback loop)",
        ],
        "out_of_scope": [
            "Trade lifecycle writes (M2 P2.5)",
            "Local SQLite WAL fallback (M2 P2.6)",
            "Realtime subscriptions consumption (M3 P3.3)",
            "Config / audit tables (M3 P3.5)",
        ],
        "prereqs": [
            "M0 P0.4: Supabase project + URL + service-role key",
            "P1.2 done — bridge accepts payloads",
        ],
        "deliverables": [
            ("`db/migrations/0001_initial.sql`", "DDL for signals, executions, trades, enums, indices, RLS"),
            ("`db/README.md`", "How migrations are applied; never edit a committed migration"),
            ("`bridge/app/supabase_client.py`", "Async wrapper around `supabase` Python client"),
            ("`bridge/app/repositories/signals.py`", "`insert_signal`, `update_signal_status`"),
            ("`bridge/app/repositories/executions.py`", "`insert_execution`"),
            ("`bridge/tests/test_repositories.py`", "Tests against a Supabase test schema"),
        ],
        "tasks": [
            "Author migration SQL (`signals` table per PRD §6.1, `executions` per §6.2, `trades` per §6.3)",
            "Add CHECK constraints on enums (status, action)",
            "Add indices: `signals(received_at)`, `signals(strategy_id)`, `signals(signal_hash)` (UNIQUE — prepared for M2)",
            "Apply migration to Supabase project (SQL editor or `supabase db push`)",
            "Enable RLS on all three tables; default deny",
            "Implement async Supabase client wrapper with timeout",
            "Implement signals & executions repositories",
            "Update webhook → dispatch path: insert signal RECEIVED before dispatch, transition statuses, insert execution after fill",
            "Make all DB writes fire-and-forget via `asyncio.create_task` so they never block the response",
            "Add tests against a Supabase test project (separate from prod)",
        ],
        "deps_up": "P1.2; runs alongside P1.4",
        "deps_down": "P1.7 stabilization checks DB has the expected rows after each test alert",
        "deps_ext": "Supabase project reachable; service-role key present",
        "risks": [
            ("Schema migrations not idempotent → CI re-runs fail", "Medium", "Medium", "All migrations use IF NOT EXISTS / CREATE OR REPLACE; numbered, never edited in place"),
            ("Service-role key exposed", "Critical", "Low", ".env in gitignore; pre-commit secret scan; key only on VPS"),
            ("Supabase write blocks bridge response", "High", "Low", "Fire-and-forget via asyncio.create_task; tests confirm response time unaffected"),
            ("RLS misconfigured letting anon writes through", "Critical", "Low", "Test from anon key explicitly fails; deny-all default"),
        ],
        "exit": [
            "Migration applied to Supabase; `select * from signals` works as service role",
            "RLS verified: anon key can SELECT zero rows; service role can SELECT all",
            "Webhook + dispatch flow inserts signal + execution rows",
            "Latency of webhook response unaffected (still p95 < 50 ms — DB writes off path)",
            "All tests pass; coverage on repositories ≥ 80%",
            "No open CRITICAL/HIGH bug",
            "`report.md` filled and signed",
        ],
        "tests": [
            ("unit", "insert_signal writes a row with status RECEIVED"),
            ("unit", "update_signal_status transitions RECEIVED → VALIDATED → EXECUTED"),
            ("unit", "insert_execution writes ticket, fill_price, slippage, spread"),
            ("unit", "fire-and-forget pattern: webhook returns 202 even when supabase_client.insert hangs (timeout)"),
            ("integration", "[live] migration applies cleanly to a fresh Supabase project"),
            ("integration", "[live] RLS denies anon SELECT; allows service-role SELECT"),
            ("integration", "[live] full pipeline: webhook → signal row → execution row, both visible in SQL editor"),
            ("integration", "[live] webhook response time unchanged when DB write is slow (simulated 500ms latency)"),
        ],
    },
    "P1.6_Basic_Telegram_Notifications": {
        "id": "P1.6",
        "name": "Basic Telegram Notifications",
        "owner": "Bridge dev",
        "hours": 3,
        "purpose": (
            "Send the operator a Telegram message on three M1 events: signal received, order executed, dispatch failed. "
            "Formatting and throttling are deliberately minimal — this is the 'is anything happening?' channel. "
            "Daily reports, weekly reports, and severity-aware throttling come in M3 P3.6."
        ),
        "in_scope": [
            "`bridge/app/telegram.py` — async client wrapping `python-telegram-bot`",
            "Three message types: signal_received, order_executed, dispatch_failed",
            "Plain-text formatting; emoji prefix per type",
            "Settings: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_IDS` (comma-separated)",
            "Fire-and-forget: never block the webhook response",
            "Tests with mocked Telegram HTTP",
        ],
        "out_of_scope": [
            "Daily / weekly digests (M3 P3.6)",
            "Inline buttons (M3 P3.6)",
            "Severity throttling / muting (M3 P3.6)",
            "Telegram /commands inbound (M3 P3.6)",
        ],
        "prereqs": [
            "M0 P0.4: bot created via @BotFather, token in 1Password, chat ID known",
            "P1.4 done — dispatch returns DispatchResult we can format",
        ],
        "deliverables": [
            ("`bridge/app/telegram.py`", "`TelegramNotifier` async client"),
            ("`bridge/app/notifications.py`", "Event handlers: on_signal_received, on_order_executed, on_dispatch_failed"),
            ("`bridge/tests/test_telegram.py`", "Mocked-HTTP tests"),
        ],
        "tasks": [
            "Pin `python-telegram-bot>=21.0` in pyproject",
            "Implement `TelegramNotifier.send(text, chat_ids)` — async, fire-and-forget under the hood",
            "Compose the 3 message templates (with all the relevant fields from each event)",
            "Wire notifier into the webhook flow at the right points (after signal insert, after fill, on dispatch failure)",
            "Tests with mocked aiohttp/httpx returning success/failure",
        ],
        "deps_up": "P1.4 (dispatch result format); runs alongside P1.5",
        "deps_down": "M3 P3.6 enhances this",
        "deps_ext": "Telegram API reachable",
        "risks": [
            ("Bot token leaks", "Critical", "Low", ".env + 1Password + secret scan"),
            ("Telegram outage spams retries", "Low", "Low", "One retry max in M1; full retry in M2 P2.6"),
            ("Wrong chat_id → silent fail", "Medium", "Medium", "On-startup self-test sends a `system startup` message and asserts 200"),
        ],
        "exit": [
            "Test alert triggers a 'Signal received' Telegram message within 5 s",
            "Successful fill triggers an 'Order executed' Telegram message within 5 s of fill",
            "Dispatch failure triggers a 'Dispatch failed' Telegram message",
            "Webhook latency unchanged (notifications fire-and-forget)",
            "Tests pass; coverage on telegram.py ≥ 80%",
            "No open CRITICAL/HIGH bug",
            "`report.md` filled and signed",
        ],
        "tests": [
            ("unit", "send() POSTs to https://api.telegram.org/bot<token>/sendMessage with chat_id and text"),
            ("unit", "send() multiple chat_ids → multiple POSTs in parallel"),
            ("unit", "Telegram returns 4xx → log error, do not retry"),
            ("unit", "Telegram returns 5xx → log error, retry once"),
            ("unit", "on_signal_received composes message with strategy/symbol/direction/SL/TP"),
            ("unit", "on_order_executed composes message with ticket/lot/spread/slippage"),
            ("integration", "[live] real bot delivers a startup ping to real chat ID"),
            ("manual", "Trigger a test webhook → verify Telegram message arrives on operator's phone"),
        ],
    },
    "P1.7_M1_Integration_and_Stabilization": {
        "id": "P1.7",
        "name": "M1 Integration & Stabilization",
        "owner": "Lead",
        "hours": 4,
        "purpose": (
            "Run the full M1 surface end-to-end, exercise the demo gate G1, fix any CRITICAL/HIGH bugs uncovered, "
            "update timing tables in data-flow.md, and close out the milestone. **No new features in this phase.**"
        ),
        "in_scope": [
            "End-to-end smoke: 5 manual TV alerts → bridge → MT5 fills → Supabase rows → Telegram messages",
            "Latency measurements: p50, p95, p99 captured to `report.md`",
            "Bug triage: walk through every P1.* `bugs.md`, close all CRITICAL/HIGH",
            "Update `docs/architecture/data-flow.md` Section 6 with M1-measured numbers",
            "Update `planning/milestone-tracker.md` to 🟢 Done",
            "Record G1 demo video and save to `docs/handover/m1-demo.mp4` (if not already done in P1.4)",
        ],
        "out_of_scope": [
            "Any new feature (defer to M2)",
            "Performance tuning beyond fixing bugs (defer to M4 P4.1)",
        ],
        "prereqs": [
            "P1.1 through P1.6 all marked Done",
            "All P1.* tests passing in CI",
        ],
        "deliverables": [
            ("`docs/handover/m1-demo.mp4`", "G1 demo recording (≤5 min)"),
            ("`docs/architecture/data-flow.md` (updated)", "M1 latency baselines filled in"),
            ("`planning/milestone-tracker.md` (updated)", "M1 marked Done"),
            ("`milestones/M1_Foundation/phases/P1.7_M1_Integration_and_Stabilization/report.md`", "Cumulative M1 report including KPI vs target table"),
        ],
        "tasks": [
            "Run end-to-end smoke 5 times; record latency numbers per run",
            "Open every P1.* `bugs.md`; for each CRITICAL/HIGH, fix in code, add a test, mark FIXED",
            "Re-run full pytest suite; coverage ≥ 80%",
            "Update data-flow.md timing table for the 'End of M1 P1.7' row",
            "Record demo video covering: TV alert → bridge log → MT5 fill → Supabase rows → Telegram message — narrated walkthrough",
            "Update milestone-tracker.md status; add 'Recent changes' entry",
            "Send completion message to owner",
        ],
        "deps_up": "All of P1.1–P1.6",
        "deps_down": "M2 cannot start until this phase is Done",
        "deps_ext": "Owner availability for demo review and sign-off",
        "risks": [
            ("Latency p95 misses the 3-second M1 budget", "High", "Low", "Triage broker location (M0 choice) and bridge handler synchronicity; if unfixable in M1, escalate to M4 P4.1 with a documented exception"),
            ("Multiple cross-phase bugs surface only at integration", "Medium", "Medium", "Time-box bug fixing to 2× the original bug severity's effort; escalate beyond that"),
        ],
        "exit": [
            "All M1 acceptance criteria from `milestones/M1_Foundation/exit-criteria.md` ✓",
            "Latency p95 ≤ 3 s on demo over 5 runs",
            "All P1.* `report.md` show Status: Done",
            "Zero open CRITICAL/HIGH bugs across all P1.*",
            "Demo video recorded and saved",
            "Tracker updated",
            "Owner sign-off captured in `report.md`",
        ],
        "tests": [
            ("integration", "[live] smoke run #1 — full pipeline TV→MT5→Supabase→Telegram"),
            ("integration", "[live] smoke run #2"),
            ("integration", "[live] smoke run #3"),
            ("integration", "[live] smoke run #4"),
            ("integration", "[live] smoke run #5"),
            ("integration", "Bridge stays up for 24 hours unattended without restart (idle test on VPS)"),
            ("manual", "Owner walks through the demo video and signs off"),
        ],
    },
}

PLAN_TPL = """\
# {pid} — {name} — plan

## Purpose

{purpose}

## Scope

### In scope
{in_scope}

### Out of scope
{out_of_scope}

## Inputs / Prereqs

{prereqs}

## Deliverables

| Path | Description |
|---|---|
{deliverables}

## Task breakdown

Each task ≤ 2 hours. **Write tests first** (global TDD rule).

{tasks}

## Dependencies

- **Upstream:** {deps_up}
- **Downstream:** {deps_down}
- **External:** {deps_ext}

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
{risks}

## Exit Criteria

{exit_criteria}
"""

TEST_TPL = """\
# {pid} — {name} — tests

> **TDD applies.** Tests are written *before* implementation. Coverage target ≥ 80%.

## Test list

| ID | Type | Title | Status |
|---|---|---|---|
{test_table}

## Seed test details

{test_details}

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
"""

BUGS_TPL = """\
# {pid} — {name} — bugs

## Severity definitions

| Severity | Definition | Exit-blocking? |
|---|---|---|
| **CRITICAL** | Data loss, financial loss, or full outage. | ✅ Yes |
| **HIGH** | Breaks a primary acceptance test or KPI target; no clean workaround. | ✅ Yes |
| **MEDIUM** | Affects UX/quality but workaround exists. | ❌ No |
| **LOW** | Cosmetic, typo, log-level. | ❌ No |

## Active bugs

| ID | Severity | Title | Repro | Owner | Status | Found-on | Fixed-on |
|---|---|---|---|---|---|---|---|
| _none yet_ | | | | | | | |

## Bug template (copy when adding)

```
### B-NN — Title

- Severity: CRITICAL / HIGH / MEDIUM / LOW
- Status: OPEN / IN PROGRESS / FIXED / WONTFIX
- Found: YYYY-MM-DD by …
- Owner: …
- Affected commit: …

Repro:
1. …
2. …
3. Expected: …
4. Actual: …

Logs / screenshots: …

Root cause (filled at fix time): …

Fix:
- Commit: …
- File(s): …
- Test added: …
```
"""

REPORT_TPL = """\
# {pid} — {name} — report

## Status

| Field | Value |
|---|---|
| **Status** | Pending |
| **Owner** | {owner} |
| **Started** | — |
| **Completed** | — |
| **Effort (planned)** | {hours} hours |
| **Effort (actual)** | — |

## What shipped

| Deliverable | Path | Shipped? | Notes |
|---|---|---|---|
{deliv_status}

## Tests

| Set | Result |
|---|---|
| Unit | — |
| Integration (live) | — |
| Manual | — |
| Coverage | — |

## Bugs closed in this phase

| ID | Severity | Title | Closed-on |
|---|---|---|---|
| _none yet_ | | | |

## Metrics

| Metric | Target | Achieved |
|---|---|---|
| Coverage on new code | ≥ 80% | — |
| Latency impact (vs baseline) | no regression | — |

## Deviations from plan

- _none yet_

## Lessons learned

- _filled at completion_

## Sign-off

| Role | Name | Date | Signature / SHA |
|---|---|---|---|
| Developer | | | |
| Reviewer | | | |
| Owner | | | |
"""


def render_bullets(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items)


def render_numbered(items: list[str]) -> str:
    return "\n".join(f"{i+1}. {x}" for i, x in enumerate(items))


def render_checkboxes(items: list[str]) -> str:
    return "\n".join(f"- [ ] {x}" for x in items)


def render_deliverables(items: list[tuple[str, str]]) -> str:
    return "\n".join(f"| {p} | {d} |" for p, d in items)


def render_deliv_status(items: list[tuple[str, str]]) -> str:
    return "\n".join(f"| {d} | {p} | ⚪ | |" for p, d in items)


def render_risks(items: list[tuple[str, str, str, str]]) -> str:
    return "\n".join(f"| {r} | {s} | {l} | {m} |" for r, s, l, m in items)


def render_test_table(items: list[tuple[str, str]]) -> str:
    return "\n".join(f"| T{i+1} | {t} | {title} | ⚪ |" for i, (t, title) in enumerate(items))


def render_test_details(items: list[tuple[str, str]]) -> str:
    out = []
    for i, (t, title) in enumerate(items):
        out.append(f"### T{i+1} — {title}\n\n- **Type:** {t}\n- **Given** _state_\n- **When** _action_\n- **Then** _expected_\n- **Implemented in** `bridge/tests/...`")
    return "\n\n".join(out)


def main() -> None:
    written = 0
    for dirname, p in PHASES.items():
        base = M1 / dirname
        base.mkdir(parents=True, exist_ok=True)

        plan = PLAN_TPL.format(
            pid=p["id"],
            name=p["name"],
            purpose=p["purpose"],
            in_scope=render_bullets(p["in_scope"]),
            out_of_scope=render_bullets(p["out_of_scope"]),
            prereqs=render_checkboxes(p["prereqs"]),
            deliverables=render_deliverables(p["deliverables"]),
            tasks=render_numbered(p["tasks"]),
            deps_up=p["deps_up"],
            deps_down=p["deps_down"],
            deps_ext=p["deps_ext"],
            risks=render_risks(p["risks"]),
            exit_criteria=render_numbered(p["exit"]),
        )
        test = TEST_TPL.format(
            pid=p["id"],
            name=p["name"],
            test_table=render_test_table(p["tests"]),
            test_details=render_test_details(p["tests"]),
        )
        bugs = BUGS_TPL.format(pid=p["id"], name=p["name"])
        report = REPORT_TPL.format(
            pid=p["id"],
            name=p["name"],
            owner=p["owner"],
            hours=p["hours"],
            deliv_status=render_deliv_status(p["deliverables"]),
        )

        for fname, content in [("plan.md", plan), ("test.md", test), ("bugs.md", bugs), ("report.md", report)]:
            path = base / fname
            path.write_text(content, encoding="utf-8")
            written += 1

    print(f"Wrote {written} files across {len(PHASES)} M1 phases (P1.3–P1.7).")


if __name__ == "__main__":
    main()
