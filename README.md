# SignalBridge

**TradingView → MetaTrader 5 automated signal execution platform.**
Webhook ingest → risk engine → MT5 EA → Telegram alerts → admin dashboard.

[![Status](https://img.shields.io/badge/status-bootstrap-blue.svg)](#status)
[![License](https://img.shields.io/badge/license-proprietary-lightgrey.svg)](#license)
[![PRD](https://img.shields.io/badge/PRD-v1.0-green.svg)](docs/PRD/SignalBridge_PRD_v1.md)

---

## What this is

SignalBridge takes a Pine Script alert from TradingView, validates and risk-checks it on a Python+FastAPI bridge, then executes the trade on MetaTrader 5 via the official MT5 Python integration — all on a single Windows VPS for sub-2-second latency. Every signal, execution, and trade is logged to Supabase, summarized on a Next.js dashboard, and broadcast to Telegram.

> Read the full product spec in [`docs/PRD/SignalBridge_PRD_v1.md`](docs/PRD/SignalBridge_PRD_v1.md).

## Status

This repo is currently in **Milestone 0 — Bootstrap & Architecture**. No application code has been written yet; what's here is the scaffolding (PRD copy, ADRs, planning, milestone folders) needed to execute the project end-to-end without surprises.

| Milestone | What it ships | Status |
|---|---|---|
| [M0 — Bootstrap & Architecture](milestones/M0_Bootstrap_and_Architecture/) | Repo, VPS, ADRs, accounts | 🟡 In Progress |
| [M1 — Foundation](milestones/M1_Foundation/) | Pine + FastAPI + MT5 + Supabase + Telegram demo | ⚪ Pending |
| [M2 — Risk Engine & Lifecycle](milestones/M2_Risk_Engine_and_Lifecycle/) | Dual-layer risk, dedup, position management | ⚪ Pending |
| [M3 — Dashboard & Monitoring](milestones/M3_Dashboard_and_Monitoring/) | Next.js dashboard, analytics, daily reports | ⚪ Pending |
| [M4 — Hardening & Forward Test](milestones/M4_Hardening_and_Forward_Test/) | 2-week demo, security, prod deploy | ⚪ Pending |
| [M5 — Live & Handover](milestones/M5_Live_and_Handover/) | Pilot live, runbook, KT, sign-off | ⚪ Pending |

Live status board: [`planning/milestone-tracker.md`](planning/milestone-tracker.md).

## Repository layout

```
docs/                           ← PRD, architecture, runbooks, handover
  PRD/                          ← original docx + markdown extract
  architecture/                 ← system overview + ADRs
  runbook/                      ← operations runbook (filled in M4/M5)
  handover/                     ← handover package (filled in M5)
planning/                       ← cross-milestone planning artefacts
  master-roadmap.md             ← all milestones, phases, dependencies
  milestone-tracker.md          ← live status board
  risk-register.md              ← cross-cutting risks
  templates/                    ← phase-plan / phase-test / phase-bugs / phase-report templates
  scripts/                      ← scaffold verification scripts
milestones/                     ← work itself, organized milestone → phase
  M0_*/, M1_*/, M2_*/, …
    README.md
    exit-criteria.md
    phases/
      P*.*_<Name>/
        plan.md   test.md   bugs.md   report.md
```

## Tech stack (locked)

| Layer | Choice | Rationale |
|---|---|---|
| Strategy | Pine Script v6 | TradingView native |
| Bridge | **Python 3.11 + FastAPI** | Direct `MetaTrader5` lib, lowest latency — see [ADR-0001](docs/architecture/ADR-0001-bridge-runtime.md) |
| Executor | MQL5 EA | Broker-side risk override + standalone fallback |
| Database | **Supabase (Postgres)** | Realtime subs + auth + free tier — see [ADR-0002](docs/architecture/ADR-0002-database.md) |
| Dashboard | Next.js 14 + Tailwind + shadcn/ui | Realtime via Supabase JS |
| Alerts | Telegram Bot API | Free, instant, group-friendly |
| Hosting | Windows Server 2022 VPS | Co-located with MT5 terminal |

## Quick links

- 📘 **PRD:** [docs/PRD/SignalBridge_PRD_v1.md](docs/PRD/SignalBridge_PRD_v1.md)
- 🗺️ **Master roadmap:** [planning/master-roadmap.md](planning/master-roadmap.md)
- 📊 **Live tracker:** [planning/milestone-tracker.md](planning/milestone-tracker.md)
- ⚠️ **Risk register:** [planning/risk-register.md](planning/risk-register.md)
- 🏗️ **Architecture overview:** [docs/architecture/README.md](docs/architecture/README.md)
- ✅ **M1 exit criteria:** [milestones/M1_Foundation/exit-criteria.md](milestones/M1_Foundation/exit-criteria.md)

## How to use this repo (for the implementer)

1. **Pick a milestone** from `milestones/`. Read its `README.md` and `exit-criteria.md`.
2. **Pick a phase** within it. Read its `plan.md` first.
3. **Write tests first** (`test.md` lists the acceptance set; the global rule is ≥80% coverage with TDD — see CLAUDE.md).
4. **Track bugs** in `bugs.md` as they're found. Phase cannot exit with any open `CRITICAL` or `HIGH` bug.
5. **Complete the phase** by filling in `report.md`, marking `Status: Done`, and getting sign-off.
6. **Move to the next phase.**

When all phases in a milestone are `Done` and `exit-criteria.md` is fully ✓, the milestone is closed; move to the next one.

## License

Proprietary — © Webverse Arena 2026. All rights reserved.
