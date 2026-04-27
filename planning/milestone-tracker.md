# Milestone Tracker (Live Status)

> Update this file whenever a phase changes state. Single source of truth for "where are we?".
> Conventions: `⚪ Pending` → `🟡 In Progress` → `🟢 Done` → `🔴 Blocked` → `⚫ Cancelled`.

**Last updated:** 2026-04-27 (bootstrap)

---

## At a glance

| Milestone | Status | % Complete | Active phase | Blockers |
|---|---|---:|---|---|
| M0 — Bootstrap | 🟡 In Progress | 0% | P0.1 Repo & Tooling | none |
| M1 — Foundation | ⚪ Pending | 0% | — | M0 |
| M2 — Risk Engine | ⚪ Pending | 0% | — | M1 |
| M3 — Dashboard | ⚪ Pending | 0% | — | M2 |
| M4 — Hardening | ⚪ Pending | 0% | — | M3 |
| M5 — Handover | ⚪ Pending | 0% | — | M4 |

---

## Phase board

### M0 — Bootstrap & Architecture

| Phase | Status | Owner | Started | Completed | Notes |
|---|---|---|---|---|---|
| P0.1 Repo & Tooling | 🟡 In Progress | Lead | 2026-04-27 | — | Scaffold initialized in this commit |
| P0.2 VPS & MT5 Environment | ⚪ Pending | Ops | — | — | |
| P0.3 ADR lock-in | 🟢 Done | Lead | 2026-04-27 | 2026-04-27 | ADR-0001/0002/0003 written |
| P0.4 Account & Vendor Procurement | ⚪ Pending | Owner | — | — | |

### M1 — Foundation

| Phase | Status | Owner | Started | Completed | Notes |
|---|---|---|---|---|---|
| P1.1 Pine Script SMC (XAUUSD M15) | ⚪ Pending | Strategy dev | — | — | |
| P1.2 FastAPI Webhook Bridge Skeleton | ⚪ Pending | Bridge dev | — | — | |
| P1.3 MT5 Python Connector | ⚪ Pending | Bridge dev | — | — | |
| P1.4 End-to-End Demo Pipeline | ⚪ Pending | Bridge dev | — | — | |
| P1.5 Supabase Schema + Signal Log | ⚪ Pending | Bridge dev | — | — | |
| P1.6 Basic Telegram Notifications | ⚪ Pending | Bridge dev | — | — | |
| P1.7 M1 Integration & Stabilization | ⚪ Pending | Lead | — | — | |

### M2 — Risk Engine & Lifecycle

| Phase | Status | Owner | Started | Completed | Notes |
|---|---|---|---|---|---|
| P2.1 Bridge-Level Risk Rules | ⚪ Pending | | | | |
| P2.2 Dedup, Expiry, Idempotency | ⚪ Pending | | | | |
| P2.3 EA Hybrid Mode | ⚪ Pending | | | | |
| P2.4 Position Management | ⚪ Pending | | | | |
| P2.5 Execution Feedback Loop | ⚪ Pending | | | | |
| P2.6 Error Handling & Retry | ⚪ Pending | | | | |
| P2.7 M2 Integration & Stabilization | ⚪ Pending | | | | |

### M3 — Dashboard & Monitoring

| Phase | Status | Owner | Started | Completed | Notes |
|---|---|---|---|---|---|
| P3.1 Next.js Scaffolding + Auth | ⚪ Pending | | | | |
| P3.2 Signal Log + Trade History | ⚪ Pending | | | | |
| P3.3 Realtime Position + P&L | ⚪ Pending | | | | |
| P3.4 Execution Quality Analytics | ⚪ Pending | | | | |
| P3.5 Configuration UI | ⚪ Pending | | | | |
| P3.6 Enhanced Telegram Reports | ⚪ Pending | | | | |
| P3.7 M3 Integration & Stabilization | ⚪ Pending | | | | |

### M4 — Hardening & Forward Test

| Phase | Status | Owner | Started | Completed | Notes |
|---|---|---|---|---|---|
| P4.1 Stress & Chaos Tests | ⚪ Pending | | | | |
| P4.2 Security Hardening | ⚪ Pending | | | | |
| P4.3 Demo Forward Test (≥2 wk) | ⚪ Pending | | | | |
| P4.4 VPS Production Deployment | ⚪ Pending | | | | |
| P4.5 Backup, DR, Runbooks | ⚪ Pending | | | | |

### M5 — Live & Handover

| Phase | Status | Owner | Started | Completed | Notes |
|---|---|---|---|---|---|
| P5.1 Operator Documentation | ⚪ Pending | | | | |
| P5.2 Pilot Live Deployment | ⚪ Pending | | | | |
| P5.3 Live Monitoring & Tuning | ⚪ Pending | | | | |
| P5.4 Final Acceptance & Sign-Off | ⚪ Pending | | | | |
| P5.5 Handover Package & KT | ⚪ Pending | | | | |

---

## Open blockers (cross-cutting)

| ID | Blocker | Affected | Owner | Target resolution |
|---|---|---|---|---|
| (none yet) | | | | |

---

## Recent changes

- **2026-04-27** — Project bootstrap: folder structure created, PRD copied to `docs/PRD/`, ADRs 0001/0002/0003 locked, M1 fully populated, M0/M2–M5 stubs seeded. Initial commit pushed.
