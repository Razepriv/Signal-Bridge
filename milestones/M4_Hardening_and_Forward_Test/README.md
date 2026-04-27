# Milestone 4 — Hardening & Forward Test

**Window:** Week 7 + a 2-week demo forward test running in parallel
**PRD reference:** §10.4 (Phase 4, first half)
**Phases:** 5
**Exit gate:** 2-week demo green; security hardened; production deploy live with monitoring.

## Purpose

M3 made the system observable. **M4 makes it production-ready.** Stress-test it, lock down the security surface, deploy it like a real service, and let it run on demo for two weeks of unsupervised market exposure to find the bugs that only show up in the wild.

## What ships

- Stress / chaos tests: rapid-fire signals, MT5 disconnects mid-order, Supabase outages, Telegram outages (P4.1).
- Security hardening: TLS via Cloudflare, IP allowlist, rate limiting, secret rotation, secrets out of code (P4.2).
- 2-week demo forward test on a real broker demo account, daily review, KPI collection (P4.3, runs in parallel).
- VPS production deployment via Windows services, monitoring, log aggregation (P4.4).
- Backup, DR, runbook draft (P4.5).

## Phases

| # | Phase |
|---|---|
| [P4.1](phases/P4.1_Stress_and_Chaos_Tests/) | Stress & chaos tests |
| [P4.2](phases/P4.2_Security_Hardening/) | Security hardening |
| [P4.3](phases/P4.3_Demo_Forward_Test_2_Weeks/) | Demo forward test (≥2 weeks) |
| [P4.4](phases/P4.4_VPS_Production_Deployment/) | VPS production deployment |
| [P4.5](phases/P4.5_Backup_DR_Runbooks/) | Backup, DR, runbooks |

## Exit

See [`exit-criteria.md`](exit-criteria.md).
