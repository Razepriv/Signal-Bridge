"""Generate seeded stub plan/test/bugs/report files for M0/M2/M3/M4/M5 phases.

Run from D:/Signal bridge/. M1 phases are populated separately.
Each phase gets four files with PRD-derived seed content.
"""
from __future__ import annotations

import os
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[2]  # D:/Signal bridge/
MILESTONES = ROOT / "milestones"

# (milestone_dir, phase_dir, phase_id, phase_name, purpose, seed_tasks, seed_tests)
PHASES: list[tuple[str, str, str, str, str, list[str], list[str]]] = [
    # ----- M0 Bootstrap -----
    (
        "M0_Bootstrap_and_Architecture", "P0.1_Repo_and_Tooling", "P0.1",
        "Repo & Tooling Bootstrap",
        "Initialize the git repo, define Python project layout, configure pre-commit and CI so every later commit is linted and type-checked.",
        [
            "git init and add remote pointing to Razepriv/Signal-Bridge",
            "Author root README.md and .gitignore (Python + Node + MT5 + secrets)",
            "Create pyproject.toml with Python 3.11+; pin ruff, black, mypy, pytest versions",
            "Set up pre-commit hooks (ruff, black, mypy --strict on bridge/)",
            "Create .github/workflows/ci.yml with lint + type-check + pytest jobs",
            "Push initial scaffold commit and verify CI green",
        ],
        [
            "Pre-commit hooks reject a deliberately badly-formatted file",
            "CI fails on a deliberately type-incorrect commit",
            "pytest collects 0 tests but exits 0 (empty bridge/ tree)",
            "git log --oneline -1 shows the bootstrap commit",
        ],
    ),
    (
        "M0_Bootstrap_and_Architecture", "P0.2_VPS_and_MT5_Environment", "P0.2",
        "VPS & MT5 Environment",
        "Provision the Windows Server VPS, install MT5 + Python 3.11, set up an HTTPS tunnel for dev webhook ingress.",
        [
            "Provision Windows Server 2022 VPS at chosen region (London or NY)",
            "Install MetaTrader 5 terminal; log in to demo broker account",
            "Install Python 3.11 and verify `pip install MetaTrader5` succeeds",
            "Install Cloudflare Tunnel (or ngrok for early dev) and forward to localhost:8000",
            "Run a dummy FastAPI listener and POST a test webhook through the tunnel",
            "Document VPS IP, RDP credentials, broker account in 1Password",
        ],
        [
            "RDP into VPS from operator workstation succeeds",
            "MT5 terminal shows logged-in account with demo balance",
            "`python -c \"import MetaTrader5; print(MetaTrader5.__version__)\"` succeeds",
            "External `curl https://<tunnel-url>/ping` returns 200 from the dummy listener",
        ],
    ),
    (
        "M0_Bootstrap_and_Architecture", "P0.3_Architecture_Decision_Records", "P0.3",
        "Architecture Decision Records (ADRs)",
        "Lock the three load-bearing decisions (bridge runtime, database, MT5 transport) into immutable ADRs.",
        [
            "Author ADR-0001 — bridge runtime: Python + FastAPI",
            "Author ADR-0002 — database: Supabase",
            "Author ADR-0003 — MT5 transport: in-process MetaTrader5 lib",
            "Cross-link ADRs from docs/architecture/README.md",
            "Review against PRD §3, §4.2, §6 — confirm no contradictions",
        ],
        [
            "All three ADRs have status `Accepted` and a date",
            "Each ADR explicitly lists rejected alternatives + reasoning",
            "docs/architecture/README.md links all three ADRs",
        ],
    ),
    (
        "M0_Bootstrap_and_Architecture", "P0.4_Account_and_Vendor_Procurement", "P0.4",
        "Account & Vendor Procurement",
        "Procure every external account and key the project depends on, before any code is written that needs them.",
        [
            "Open MT5 demo account at chosen broker; record server name + login + password",
            "Subscribe to TradingView Pro+ (required for webhook alerts)",
            "Create Telegram bot via @BotFather; record token; create personal/group chat; record chat ID",
            "Create Supabase project; record URL, anon key, service-role key",
            "Register domain (e.g. signalbridge.example.com); proxy via Cloudflare; enable SSL",
            "Save all credentials in 1Password (or equivalent) — never in repo",
        ],
        [
            "TradingView account can post a webhook to a public URL",
            "Telegram bot can send a test message to the recorded chat ID",
            "Supabase SQL editor accepts a `select 1` query",
            "Cloudflare DNS resolves the domain and serves a valid TLS cert",
        ],
    ),
    # ----- M2 Risk Engine -----
    (
        "M2_Risk_Engine_and_Lifecycle", "P2.1_Bridge_Level_Risk_Rules", "P2.1",
        "Bridge-Level Risk Rules",
        "Implement all 10 bridge-level risk rules from PRD §5.1. Each rule is a pure function with a unit test before any wiring into the webhook pipeline.",
        [
            "Define `RiskRule` interface and `RiskDecision { allow|reject, reason_code }`",
            "Implement R1.1 max risk per trade (1% equity)",
            "Implement R1.2 max daily DD (3% start-of-day equity)",
            "Implement R1.3 max open positions (3)",
            "Implement R1.4 max trades per day (6)",
            "Implement R1.5 correlated exposure cap (2 same-direction same-pair)",
            "Implement R1.6 min time between trades (5 min)",
            "Implement R1.7 max spread (40 pts XAUUSD)",
            "Implement R1.8 signal expiry (120 s from alert_timestamp)",
            "Implement R1.9 weekend guard",
            "Implement R1.10 news blackout (12:00–14:30 UTC)",
            "Wire all rules into the webhook pipeline as a chain; rejected signals get `signals.status='REJECTED'` + reason_code",
        ],
        [
            "Risk per trade > 1% of equity → reject + Telegram warning (R1.1)",
            "Daily DD ≥ 3% → halt all signals for the rest of the UTC day (R1.2)",
            "> 3 open positions → queue or reject new signal (R1.3)",
            "Spread > 40 points on XAUUSD → delay or reject (R1.7)",
            "`alert_timestamp` older than 120 s → reject as stale (R1.8)",
            "Saturday/Sunday → reject with reason `WEEKEND_GUARD` (R1.9)",
        ],
    ),
    (
        "M2_Risk_Engine_and_Lifecycle", "P2.2_Dedup_Expiry_Idempotency", "P2.2",
        "Dedup, Expiry, Idempotency",
        "Make the bridge safe to receive the same payload twice (replay attacks, TradingView retries) without firing two orders.",
        [
            "Define `signal_hash = sha256(symbol + action + sl + tp + alert_timestamp + strategy_id)`",
            "Add UNIQUE index on `signals.signal_hash` in a new migration",
            "On 23505 (unique violation) → return 409 + reason `DUPLICATE`",
            "Implement 60-second LRU cache for fast in-memory dedup (avoids DB round-trip)",
            "Add expiry check using `alert_timestamp` (already in P2.1 R1.8) and ensure clock-skew handled",
        ],
        [
            "Same payload sent twice within 60 s → second returns 409, no second order",
            "Same payload after 60 s → still rejected by min-time-between-trades (R1.6)",
            "Replay with edited timestamp but same body fields → caught by signal_hash mismatch handling",
            "Clock skew of ±10 s between TV and bridge → still accepts non-stale signals",
        ],
    ),
    (
        "M2_Risk_Engine_and_Lifecycle", "P2.3_EA_Hybrid_Mode", "P2.3",
        "EA Hybrid Mode",
        "Upgrade the MQL5 EA so it can run its own SMC strategy AND accept commands written by the bridge into a watched file. EA enforces hard risk caps regardless of source.",
        [
            "Define on-disk command protocol: bridge writes `commands.jsonl`, EA reads, processes, marks done",
            "EA OnTimer reads new lines from commands.jsonl and parses each as a single command",
            "Implement OPEN_BUY, OPEN_SELL, CLOSE, MODIFY_SL, MODIFY_TP, STATUS",
            "Hard risk caps: lot ≤ SYMBOL_VOLUME_MAX, SL ≥ STOPS_LEVEL, daily loss kill, equity floor 80%",
            "Add unit-test harness via `MetaTrader5/MQL5` strategy tester or Python wrapper around terminal launches",
        ],
        [
            "Bridge writes OPEN_BUY → EA opens position with exact lot/SL/TP",
            "Bridge writes lot 5.0 → EA refuses with INVALID_LOT (caps at 1.0)",
            "Bridge writes SL too close → EA refuses with INVALID_SL",
            "Daily loss > configured cap → EA closes all and stops accepting commands",
            "EA's own SMC strategy still fires when no bridge command queued",
        ],
    ),
    (
        "M2_Risk_Engine_and_Lifecycle", "P2.4_Position_Management_BE_Trail_Partial", "P2.4",
        "Position Management — BE / Trail / Partial",
        "Add per-ticket position management modes (breakeven, trailing stop, partial close) with config-driven enable/disable per strategy.",
        [
            "EA tracks per-ticket state in a map keyed by ticket",
            "Breakeven: when price moves 1×R favorable, set SL = entry",
            "Trailing: when price moves 1.5×R favorable, trail SL by 0.5×R",
            "Partial close: when price moves 1×R favorable, close 50%, BE remainder",
            "Config knob in strategy: which modes to enable",
            "Telegram notification on each state transition",
        ],
        [
            "Long XAUUSD with SL 50 pts, price moves +50 pts → SL moves to entry (BE)",
            "Long XAUUSD with SL 50 pts, price moves +75 pts → SL trails at -25 pts behind",
            "Long XAUUSD with SL 50 pts, price moves +50 pts → 50% closed, remainder BE",
            "All three modes can be enabled simultaneously without conflict",
        ],
    ),
    (
        "M2_Risk_Engine_and_Lifecycle", "P2.5_Execution_Feedback_Loop", "P2.5",
        "Execution Feedback Loop",
        "Close the loop: every fill/close on MT5 produces an executions/trades row in Supabase. Bridge reconciles missed events on a 30 s poll.",
        [
            "EA on OnTradeTransaction: write fill details to `feedback.jsonl`",
            "Bridge tail-reads `feedback.jsonl` and writes executions/trades rows",
            "Reconciler: every 30 s, query `mt5.history_deals_get(last 5 min)` and upsert any missing rows",
            "On close: compute pnl_usd, rr_achieved, duration_minutes, close_reason",
            "Slippage and spread_at_execution captured at fill time",
        ],
        [
            "Manual close in MT5 → `trades` row appears with `close_reason=MANUAL`",
            "TP hit → close_reason=TP_HIT, pnl > 0, rr_achieved ≈ planned",
            "SL hit → close_reason=SL_HIT, pnl < 0, rr_achieved ≈ -1",
            "EA crashes during close → reconciler picks it up within 30 s",
        ],
    ),
    (
        "M2_Risk_Engine_and_Lifecycle", "P2.6_Error_Handling_and_Retry", "P2.6",
        "Error Handling & Retry",
        "Make the bridge robust to MT5 / Supabase / Telegram outages without losing a trade or corrupting state.",
        [
            "MT5 disconnect → exp backoff retry: 1s, 2s, 4s, 8s, 16s; on final failure mark signal FAILED + Critical Telegram",
            "Supabase down → fall through to local SQLite WAL (.signalbridge/state/wal.db); replay on reconnect; preserve order",
            "Telegram down → drop after 1 retry; trade unaffected",
            "Circuit breaker on MT5 client: 3 consecutive failures → open for 60 s, no requests",
            "All retries logged with structured context for debugging",
        ],
        [
            "Kill MT5 between webhook and order_send → bridge retries 5 times then marks FAILED; one Telegram critical fires",
            "Block outbound to Supabase for 5 min → writes queue locally; on unblock all rows present, no duplicates",
            "Block outbound to Telegram for 5 min → no orders missed; Telegram message dropped silently after 1 retry",
            "Circuit breaker: simulate 3 MT5 failures → next request fails fast for 60 s without hitting MT5",
        ],
    ),
    (
        "M2_Risk_Engine_and_Lifecycle", "P2.7_M2_Integration_and_Stabilization", "P2.7",
        "M2 Integration & Stabilization",
        "Integration test the full M2 surface, run the demo gate, fix all CRITICAL/HIGH bugs, and exit M2.",
        [
            "Run end-to-end test: 12 synthetic signals exercising each rule R1.1–R1.10, plus dedup, plus a deliberate MT5 disconnect",
            "Measure latency p95 across the 12 signals; expect ≤ 2.5 s on demo",
            "Triage all CRITICAL/HIGH bugs from prior phases; close before exit",
            "Update planning/milestone-tracker.md to 🟢 Done",
            "Record G2 demo video and save to docs/handover/m2-demo.mp4",
        ],
        [
            "All 12 synthetic signals produce the expected rule decisions and DB rows",
            "Demo gate G2 video clearly shows each rule firing with the expected reason_code",
            "No open CRITICAL or HIGH bug across P2.*/bugs.md",
            "Coverage ≥ 80% on bridge/risk_engine/ and EA risk override module",
        ],
    ),
    # ----- M3 Dashboard -----
    (
        "M3_Dashboard_and_Monitoring", "P3.1_Nextjs_Scaffolding_and_Auth", "P3.1",
        "Next.js Scaffolding + Supabase Auth",
        "Stand up the Next.js 14 dashboard with Tailwind, shadcn/ui, and Supabase Auth gating all routes.",
        [
            "`npx create-next-app@latest dashboard` with App Router + TypeScript + Tailwind",
            "Install shadcn/ui and configure theme",
            "Install @supabase/ssr; wire login/logout flow",
            "Protect all `/(dashboard)/*` routes via middleware redirect to /login",
            "Create operator user in Supabase Auth (email/password)",
            "Deploy a stub home page to Vercel preview",
        ],
        [
            "Anonymous visit to / → redirected to /login",
            "Login with operator credentials → redirected to /dashboard",
            "Sign out → redirected to /login",
            "Service-role key not present in client bundle (verified via build inspection)",
        ],
    ),
    (
        "M3_Dashboard_and_Monitoring", "P3.2_Signal_Log_and_Trade_History", "P3.2",
        "Signal Log + Trade History",
        "Two read-only pages: a searchable/filterable signal log and a closed-trade history with equity curve.",
        [
            "Server component reading `signals` table with pagination, search, status filter",
            "Trade history page with filters by symbol, strategy, date range",
            "Equity curve chart (Recharts or Lightweight Charts)",
            "Export-to-CSV button for both tables",
        ],
        [
            "Signal log shows last 50 signals with correct status badges",
            "Filter by status=REJECTED reduces the list to just rejections",
            "Trade history equity curve matches the sum of `pnl_usd` over time",
            "CSV export contains the same rows as on-screen",
        ],
    ),
    (
        "M3_Dashboard_and_Monitoring", "P3.3_Realtime_Position_and_PnL", "P3.3",
        "Realtime Position + P&L",
        "Live tile showing open positions, unrealized P&L, and account equity, updated via Supabase Realtime.",
        [
            "Subscribe to `executions`, `trades`, `account_state` channels",
            "Compute unrealized P&L from open positions × current price",
            "Bridge writes account state heartbeat every 5 s",
            "Tile flashes amber on MT5 disconnect, red after 30 s",
        ],
        [
            "Open a position on demo MT5 → appears in tile within 2 s",
            "Close it → disappears from tile, P&L moves to realized day total",
            "Kill MT5 → tile flashes amber within 5 s, red within 30 s",
        ],
    ),
    (
        "M3_Dashboard_and_Monitoring", "P3.4_Execution_Quality_Analytics", "P3.4",
        "Execution Quality Analytics",
        "Slippage histogram, spread distribution, latency p50/p95/p99, fill rate over time.",
        [
            "Aggregate over `executions` and `signals` last 7/30/90 days",
            "Slippage histogram (10 bins)",
            "Latency percentiles per strategy_id",
            "Fill rate = filled / (total - rejected_by_risk)",
            "All charts handle zero-data state gracefully",
        ],
        [
            "Slippage histogram matches manually computed numbers from raw data",
            "p95 latency matches `quantile(latency_ms, 0.95)` from a SQL query",
            "Fill rate excludes rejections by design — verified with seeded data",
        ],
    ),
    (
        "M3_Dashboard_and_Monitoring", "P3.5_Configuration_UI", "P3.5",
        "Configuration UI",
        "Edit risk parameters and toggle strategies live, with confirmation modal and audit log. No code changes required to tune the system.",
        [
            "Form for each risk param (R1.1–R1.10) with min/max validation",
            "Strategy enable/disable toggles by strategy_id",
            "Telegram chat-target and severity-threshold settings",
            "Confirm modal showing diff before save",
            "Insert into `config_audit` on every save",
            "Safety lock: refuse save while market open AND DD > 1%",
        ],
        [
            "Edit max trades/day from 6 to 4, save → bridge rejects the 5th trade today",
            "Audit log row created with old + new value + operator email",
            "Try to save during market hours with DD = 1.5% → rejected with `SAFETY_LOCK`",
            "Disable a strategy → next signal from that strategy_id rejected with `STRATEGY_DISABLED`",
        ],
    ),
    (
        "M3_Dashboard_and_Monitoring", "P3.6_Enhanced_Telegram_Reports", "P3.6",
        "Enhanced Telegram Reports",
        "Daily and weekly digests, severity-aware throttling so the operator's phone doesn't drown in noise.",
        [
            "Daily report scheduled at session close UTC: trades, W/L, win rate, P&L, balance, equity, top winner/loser",
            "Weekly report Sun 22:00 UTC: weekly summary + slippage/latency stats + rule breach count",
            "Severity throttling: Info events bucketed (max 1 per 5 min); Warning unbuffered; Critical always immediate",
            "Inline buttons on Critical alerts: `Halt all`, `Mute 30 min`",
        ],
        [
            "Daily report fires at 22:00 UTC even with zero trades",
            "Inline 'Halt all' button → bridge sets `system.halted=true`; next signal rejected",
            "Critical event always delivered within 5 s regardless of throttling",
            "20 Info events in 1 minute → only 1 message delivered (bucketed)",
        ],
    ),
    (
        "M3_Dashboard_and_Monitoring", "P3.7_M3_Integration_and_Stabilization", "P3.7",
        "M3 Integration & Stabilization",
        "Cross-page integration test of the dashboard + Telegram, fix CRITICAL/HIGH bugs, exit M3.",
        [
            "Playwright test suite: 5 happy paths + 5 edges across pages",
            "Lighthouse run on each page; perf score ≥ 90, a11y ≥ 90",
            "Triage all CRITICAL/HIGH bugs",
            "Update milestone-tracker.md to 🟢 Done",
            "Record G3 demo video",
        ],
        [
            "Playwright suite green",
            "Lighthouse a11y ≥ 90 on all pages",
            "All P3.* report.md filled and signed",
            "G3 demo video saved to docs/handover/m3-demo.mp4",
        ],
    ),
    # ----- M4 Hardening -----
    (
        "M4_Hardening_and_Forward_Test", "P4.1_Stress_and_Chaos_Tests", "P4.1",
        "Stress & Chaos Tests",
        "Hammer the system with adverse conditions and verify it degrades gracefully without losing trades or corrupting state.",
        [
            "Rapid-fire 50 signals in 30 s; verify dedup + risk rules behave correctly",
            "Kill MT5 mid-order; verify retry + reconciliation",
            "Block Supabase egress for 5 min; verify local WAL replay",
            "Block Telegram for 5 min; verify trades unaffected",
            "Network partition between TV and VPS; verify graceful resume",
        ],
        [
            "S1 — 50 signals in 30 s: zero crashes, dedup correct, all risk rules applied",
            "S2 — Kill MT5: bridge reconnects within 30 s, retry queue drains, one Critical Telegram",
            "S3 — Supabase blackout: writes queue, reconnect → no rows lost, ordering preserved",
            "S4 — Telegram blackout: dropped after 1 retry, system unaffected",
            "S5 — Network partition: graceful resume within 1 alert post-restore",
        ],
    ),
    (
        "M4_Hardening_and_Forward_Test", "P4.2_Security_Hardening", "P4.2",
        "Security Hardening",
        "Lock the production attack surface to TLS, allowlists, rotation, secret scans, and dependency audits.",
        [
            "Cloudflare TLS termination; HTTP→HTTPS redirect",
            "Rate limit 10 req/s per source IP at Cloudflare",
            "Allowlist TradingView IPs; reject all other webhook source IPs with 403",
            "Operator IP allowlist on dashboard via Cloudflare Access",
            "Rotate webhook secret; document rotation procedure",
            "Verify Supabase RLS on every table",
            "Run pip-audit and npm audit; fix all High/Critical",
            "git-secrets scan in CI",
        ],
        [
            "Sec1 — All ingress over HTTPS",
            "Sec2 — Webhook rate limited",
            "Sec3 — TradingView IPs allowlisted",
            "Sec4 — Webhook secret rotated successfully",
            "Sec5 — Dashboard IP allowlisted",
            "Sec6 — Supabase RLS active on all tables",
            "Sec7 — git-secrets scan green",
            "Sec8 — pip-audit + npm audit zero High/Critical",
        ],
    ),
    (
        "M4_Hardening_and_Forward_Test", "P4.3_Demo_Forward_Test_2_Weeks", "P4.3",
        "Demo Forward Test (≥2 weeks)",
        "Run the full system on a demo broker for at least 14 calendar days unsupervised; collect KPIs against PRD §11.",
        [
            "Pick a demo broker with realistic XAUUSD spreads",
            "Configure conservative params: 0.5% per trade, 2% daily DD, 4 trades/day",
            "Daily review: open dashboard, scan for anomalies, log any in P4.3/bugs.md",
            "After 14 days: write summary report with KPIs, every issue, every fix verified",
        ],
        [
            "F1 — ≥30 trades captured",
            "F2 — Uptime ≥ 99.5%",
            "F3 — Zero rule breaches",
            "F4 — Avg slippage XAUUSD ≤ 5 pts",
            "F5 — End-to-end p95 latency ≤ 2.5 s",
            "F6 — Daily reports delivered every trading day",
            "F7 — Forward test report drafted",
        ],
    ),
    (
        "M4_Hardening_and_Forward_Test", "P4.4_VPS_Production_Deployment", "P4.4",
        "VPS Production Deployment",
        "Deploy the bridge as a real Windows service that survives reboots, plus monitoring and log aggregation.",
        [
            "Install NSSM; create `signalbridge` Windows service running uvicorn",
            "MT5 terminal auto-launch on boot via Task Scheduler; auto-login script",
            "Deploy dashboard to Vercel with production env vars",
            "Set up UptimeRobot to ping `/api/v1/status` every minute",
            "Deploy Loki+Grafana (Docker) for structured log aggregation",
        ],
        [
            "Reboot VPS → bridge service auto-starts; MT5 logs in; Telegram 'system startup' fires",
            "UptimeRobot detects a deliberate 5 min downtime and alerts within 2 min",
            "Grafana dashboard shows latest 1000 bridge log lines",
        ],
    ),
    (
        "M4_Hardening_and_Forward_Test", "P4.5_Backup_DR_Runbooks", "P4.5",
        "Backup, DR, Runbooks",
        "Make the system recoverable from total VPS loss in ≤2 hours, document everything an operator needs.",
        [
            "Upgrade Supabase to Pro tier; enable PITR + daily backups",
            "Configure VPS provider daily image snapshot; retention ≥7 days",
            "Author docs/runbook/* sections defined in docs/runbook/README.md",
            "Author DR runbook: VPS restore from snapshot, MT5 reconnect, Supabase reattach",
            "Execute end-to-end DR drill on a fresh VPS; time it; document",
        ],
        [
            "B1 — Supabase backups + PITR enabled",
            "B2 — VPS daily snapshot active",
            "B3 — All credentials in operator's password manager",
            "B4 — Recovery test: full rebuild from VPS snapshot in ≤2 hours, documented",
        ],
    ),
    # ----- M5 Live & Handover -----
    (
        "M5_Live_and_Handover", "P5.1_Operator_Documentation", "P5.1",
        "Operator Documentation",
        "Author every document an operator needs to keep SignalBridge running without the developer.",
        [
            "Author docs/handover/operator-quickstart.md (zero-to-first-trade)",
            "Author docs/handover/operator-cheatsheet.md (10 most common ops)",
            "Author docs/handover/credentials-rotation.md",
            "Author docs/handover/support-window.md",
            "Author docs/runbook/* missing sections",
            "Cross-reference all docs from README.md",
        ],
        [
            "Operator can rebuild the system on a fresh VPS using only operator-quickstart.md (recorded)",
            "Operator finds 'restart bridge' procedure in cheatsheet within 30 s",
            "Credentials rotation procedure includes webhook secret + MT5 + Supabase + Telegram",
        ],
    ),
    (
        "M5_Live_and_Handover", "P5.2_Pilot_Live_Deployment_Small_Size", "P5.2",
        "Pilot Live Deployment (Small Size)",
        "Switch to a real broker account with the smallest position size the broker allows. Run for 7 calendar days. No new features in this phase.",
        [
            "Open / fund a real broker account",
            "Update MT5 terminal to live login",
            "Reduce risk params to 0.25% per trade, 1% daily DD, 2 trades/day",
            "Notify owner of go-live timestamp; start the 7-day clock",
            "Daily review during the pilot",
        ],
        [
            "First live trade fills within target latency",
            "P&L tracked correctly across the 7 days",
            "Daily Telegram reports continue uninterrupted",
            "Zero CRITICAL incidents (intentional drills don't count)",
        ],
    ),
    (
        "M5_Live_and_Handover", "P5.3_Live_Monitoring_and_Tuning", "P5.3",
        "Live Monitoring & Tuning",
        "Tune any parameters the live data demands; capture KPI baselines against PRD §11. Bug-fixes only — no features.",
        [
            "Daily KPI sweep: K1–K7 from M5 exit-criteria",
            "Tune params if K1 (latency) or K3 (slippage) are off-target",
            "Log every tuning change in `config_audit` + a tuning journal in P5.3/report.md",
            "After 7 days, compute final baselines for handover",
        ],
        [
            "K1 latency p95 ≤ 2.0 s",
            "K2 fill rate ≥ 95%",
            "K3 slippage XAUUSD ≤ 3 pts",
            "K4 uptime ≥ 99.5%",
            "K5 risk-rule compliance 100%",
            "K6 dedup zero",
            "K7 daily reports 100%",
        ],
    ),
    (
        "M5_Live_and_Handover", "P5.4_Final_Acceptance_and_Signoff", "P5.4",
        "Final Acceptance & Sign-Off",
        "Verify all M5 exit criteria; if all green, sign off. If anything red, loop back to P5.3 for tuning.",
        [
            "Walk through M5 exit-criteria.md item by item",
            "Walk through risk-register.md; close mitigated risks",
            "Verify zero open CRITICAL/HIGH across the whole repo",
            "Owner countersigns; commit the sign-off in docs/handover/signoff.md",
        ],
        [
            "All M5 exit criteria checked off",
            "All P5.* report.md filled and signed",
            "Owner signature in signoff.md",
        ],
    ),
    (
        "M5_Live_and_Handover", "P5.5_Handover_Package_and_KT", "P5.5",
        "Handover Package & KT",
        "Produce the final handover folder; deliver a knowledge-transfer session with the operator. Project closed.",
        [
            "Author docs/handover/system-overview.md",
            "Generate docs/handover/architecture-snapshot.pdf at handover SHA",
            "Author docs/handover/kpi-baseline.md from P5.3 numbers",
            "Author docs/handover/signoff.md (final)",
            "Run a 60-min KT session with operator; record",
            "Tag the repo `v1.0.0` and freeze",
        ],
        [
            "All H1–H7 criteria from M5 exit-criteria met",
            "KT recording saved",
            "v1.0.0 git tag pushed",
            "Repo README updated with 'In production — see runbook'",
        ],
    ),
]


PLAN_TPL = """\
# {phase_id} — {phase_name} (plan)

## Purpose

{purpose}

## Scope

### In scope
{in_scope_bullets}

### Out of scope
- Anything not listed above; defer to the appropriate later phase.

## Inputs / Prereqs

- [ ] All upstream phases marked Done in [milestone-tracker.md](../../../../planning/milestone-tracker.md)
- [ ] Prior milestone exit criteria met
- [ ] Required vendor accounts active (see [planning/risk-register.md](../../../../planning/risk-register.md))

## Deliverables

| Path | Description |
|---|---|
| _to be filled at phase kickoff_ | _path of artefact_ |

## Task breakdown

Each task ≤ 2 hours. Ordered.

{task_list}

## Dependencies

- **Upstream:** see milestone roadmap
- **Downstream:** the phase numbered immediately after this one in the same milestone, plus `P*.7` (or `P4.5` for M4) integration phase
- **External:** see [risk-register.md](../../../../planning/risk-register.md)

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| _filled at kickoff_ | | | |

## Exit Criteria

1. All tasks above complete with code committed
2. All acceptance tests in [`test.md`](test.md) pass
3. Coverage ≥ 80% on new code
4. No open `CRITICAL` or `HIGH` bug in [`bugs.md`](bugs.md)
5. [`report.md`](report.md) filled and signed
"""

TEST_TPL = """\
# {phase_id} — {phase_name} (tests)

## Acceptance Tests

Tests are written **before** implementation per the [TDD rule](../../../../.claude/rules/common/testing.md).

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
{test_table}

### Seed test details

{test_details}

## Unit / Integration / E2E split

- **Unit:** isolated, no I/O. Run on every commit.
- **Integration:** real Supabase test schema; mocked MT5 (`unittest.mock` on `MetaTrader5` module).
- **E2E:** demo broker, demo Telegram chat, real network. Run pre-milestone-exit.

## Fixtures & test data

- _to be defined at kickoff_

## Coverage target

- ≥ 80% line coverage on new code (`pytest --cov`)
- For dashboard work: ≥ 70% Playwright coverage on user-facing flows

## Manual test steps

For tests marked `[manual]`:

1. _to be defined at kickoff_
"""

TEST_DETAIL_TPL = """\
### T{n} — {title}

- **Given** _state_
- **When** _action_
- **Then** _expected_
- **Implemented in** `_test path_`
"""

BUGS_TPL = """\
# {phase_id} — {phase_name} (bugs)

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
# {phase_id} — {phase_name} (report)

## Status

| Field | Value |
|---|---|
| **Status** | Pending |
| **Owner** | TBD |
| **Started** | — |
| **Completed** | — |
| **Effort (planned)** | _see plan.md_ |
| **Effort (actual)** | — |

## What shipped

| Deliverable | Path | Shipped? | Notes |
|---|---|---|---|
| _filled at completion_ | | | |

## Tests

| Set | Result |
|---|---|
| Unit | — |
| Integration | — |
| E2E | — |
| Manual | — |

## Bugs closed in this phase

| ID | Severity | Title | Closed-on |
|---|---|---|---|
| _none yet_ | | | |

## Metrics

| Metric | Target | Achieved |
|---|---|---|
| _filled at completion_ | | |

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


def render_in_scope(tasks: list[str]) -> str:
    return "\n".join(f"- {t}" for t in tasks)


def render_task_list(tasks: list[str]) -> str:
    return "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))


def render_test_table(tests: list[str]) -> str:
    return "\n".join(f"| T{i+1} | unit/integration | {t} | ⚪ |" for i, t in enumerate(tests))


def render_test_details(tests: list[str]) -> str:
    return "\n\n".join(TEST_DETAIL_TPL.format(n=i+1, title=t) for i, t in enumerate(tests))


def main() -> None:
    written = 0
    for milestone, phase_dir, phase_id, phase_name, purpose, tasks, tests in PHASES:
        base = MILESTONES / milestone / "phases" / phase_dir
        base.mkdir(parents=True, exist_ok=True)

        plan = PLAN_TPL.format(
            phase_id=phase_id,
            phase_name=phase_name,
            purpose=purpose,
            in_scope_bullets=render_in_scope(tasks),
            task_list=render_task_list(tasks),
        )
        test = TEST_TPL.format(
            phase_id=phase_id,
            phase_name=phase_name,
            test_table=render_test_table(tests),
            test_details=render_test_details(tests),
        )
        bugs = BUGS_TPL.format(phase_id=phase_id, phase_name=phase_name)
        report = REPORT_TPL.format(phase_id=phase_id, phase_name=phase_name)

        for fname, content in [
            ("plan.md", plan),
            ("test.md", test),
            ("bugs.md", bugs),
            ("report.md", report),
        ]:
            path = base / fname
            if path.exists():
                continue  # don't overwrite a file an earlier step populated
            path.write_text(content, encoding="utf-8")
            written += 1

    print(f"Wrote {written} stub files across {len(PHASES)} phases.")


if __name__ == "__main__":
    main()
