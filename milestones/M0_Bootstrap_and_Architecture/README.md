# Milestone 0 — Bootstrap & Architecture

**Window:** Week 0 (pre-development)
**PRD reference:** new (added during bootstrap to fill the "no setup phase" gap)
**Phases:** 4
**Exit gate:** ADRs locked, VPS reachable, accounts procured, repo green on `main`.

## Purpose

Lay the rails so M1 onward never gets blocked by missing infrastructure, missing decisions, or missing accounts. Nothing here ships product features — but every later milestone assumes this is done.

## Phases

| # | Phase | Why it exists |
|---|---|---|
| [P0.1](phases/P0.1_Repo_and_Tooling/) | Repo & tooling bootstrap | Git remote, `.gitignore`, `pyproject.toml`, pre-commit, CI skeleton |
| [P0.2](phases/P0.2_VPS_and_MT5_Environment/) | VPS & MT5 environment | Provision Windows Server, install MT5, install Python 3.11, set up tunnel for dev webhook ingress |
| [P0.3](phases/P0.3_Architecture_Decision_Records/) | ADR lock-in | ADR-0001 (Python+FastAPI), ADR-0002 (Supabase), ADR-0003 (in-process MT5 lib) |
| [P0.4](phases/P0.4_Account_and_Vendor_Procurement/) | Account & vendor procurement | Demo broker, TradingView Pro+, Telegram bot, Supabase project, domain + Cloudflare SSL |

## Parallelism

P0.2 and P0.4 can run in parallel with P0.1/P0.3 once the repo is initialized.

## Exit

See [`exit-criteria.md`](exit-criteria.md). When all are ✓, mark milestone status `🟢 Done` in the [tracker](../../planning/milestone-tracker.md) and proceed to M1.
