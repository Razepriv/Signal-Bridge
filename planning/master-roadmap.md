# Master Roadmap

> Single source of truth for every milestone, phase, and dependency.
> When this document and a phase's `plan.md` disagree, the `plan.md` wins; reconcile by editing this document.

**Total scope:** 6 milestones, 35 phases, ~157 markdown artefacts.
**Calendar:** Week 0 (M0) → Week 8+ (M5). PRD §10 maps to M1–M4.
**Critical path:** M0 → M1 → M2 → M3 → M4 → M5 (strictly sequential between milestones).

---

## Milestone summary

| ID | Milestone | PRD ref | Window | # Phases | Critical exit | Status |
|----|-----------|---------|--------|----------|---------------|--------|
| **M0** | Bootstrap & Architecture | new | Week 0 | 4 | ADRs locked, VPS reachable, accounts procured | 🟡 In Progress |
| **M1** | Foundation | §10.1 / Phase 1 | Week 1–2 | 7 | Demo TV alert → MT5 fill, signal logged, Telegram ping | ⚪ Pending |
| **M2** | Risk Engine & Lifecycle | §10.2 / Phase 2 | Week 3–4 | 7 | All 10 bridge rules + 5 EA rules enforced; BE/trail/partial working | ⚪ Pending |
| **M3** | Dashboard & Monitoring | §10.3 / Phase 3 | Week 5–6 | 7 | All 7 dashboard pages live; daily Telegram report | ⚪ Pending |
| **M4** | Hardening & Forward Test | §10.4 / Phase 4(a) | Week 7 + 2-wk demo | 5 | 2-week demo green, prod deploy, monitoring | ⚪ Pending |
| **M5** | Live & Handover | §10.4 / Phase 4(b) + new | Week 8+ | 5 | Pilot live, runbook signed, KT complete | ⚪ Pending |

Live status: [`milestone-tracker.md`](milestone-tracker.md).

---

## Full phase index

### M0 — Bootstrap & Architecture

| Phase | Name | Owner | Est. hrs | Parallel? |
|---|---|---|---|---|
| [P0.1](../milestones/M0_Bootstrap_and_Architecture/phases/P0.1_Repo_and_Tooling/) | Repo & tooling bootstrap | Lead | 4 | — |
| [P0.2](../milestones/M0_Bootstrap_and_Architecture/phases/P0.2_VPS_and_MT5_Environment/) | VPS & MT5 environment | Ops | 6 | with P0.4 |
| [P0.3](../milestones/M0_Bootstrap_and_Architecture/phases/P0.3_Architecture_Decision_Records/) | ADR lock-in | Lead | 2 | with P0.4 |
| [P0.4](../milestones/M0_Bootstrap_and_Architecture/phases/P0.4_Account_and_Vendor_Procurement/) | Account & vendor procurement | Owner | 4 | — |

### M1 — Foundation (gold-standard, fully populated)

| Phase | Name | Owner | Est. hrs | Parallel? |
|---|---|---|---|---|
| [P1.1](../milestones/M1_Foundation/phases/P1.1_Pine_Script_SMC_XAUUSD_M15/) | Pine Script SMC strategy (XAUUSD M15) | Strategy dev | 8 | with P1.2 |
| [P1.2](../milestones/M1_Foundation/phases/P1.2_FastAPI_Webhook_Bridge_Skeleton/) | FastAPI webhook bridge skeleton | Bridge dev | 6 | with P1.1 |
| [P1.3](../milestones/M1_Foundation/phases/P1.3_MT5_Python_Connector/) | MT5 Python connector | Bridge dev | 6 | after P1.2 |
| [P1.4](../milestones/M1_Foundation/phases/P1.4_End_to_End_Demo_Pipeline/) | End-to-end demo pipeline | Bridge dev | 8 | after P1.1+P1.3 |
| [P1.5](../milestones/M1_Foundation/phases/P1.5_Supabase_Schema_and_Signal_Log/) | Supabase schema + signal log | Bridge dev | 4 | with P1.6 |
| [P1.6](../milestones/M1_Foundation/phases/P1.6_Basic_Telegram_Notifications/) | Basic Telegram notifications | Bridge dev | 3 | with P1.5 |
| [P1.7](../milestones/M1_Foundation/phases/P1.7_M1_Integration_and_Stabilization/) | M1 integration & stabilization | Lead | 4 | — |

### M2 — Risk Engine & Lifecycle

| Phase | Name | Owner | Est. hrs | Parallel? |
|---|---|---|---|---|
| [P2.1](../milestones/M2_Risk_Engine_and_Lifecycle/phases/P2.1_Bridge_Level_Risk_Rules/) | Bridge-level risk rules | Bridge dev | 10 | with P2.2 |
| [P2.2](../milestones/M2_Risk_Engine_and_Lifecycle/phases/P2.2_Dedup_Expiry_Idempotency/) | Dedup, expiry, idempotency | Bridge dev | 4 | with P2.1 |
| [P2.3](../milestones/M2_Risk_Engine_and_Lifecycle/phases/P2.3_EA_Hybrid_Mode/) | EA hybrid mode | EA dev | 8 | — |
| [P2.4](../milestones/M2_Risk_Engine_and_Lifecycle/phases/P2.4_Position_Management_BE_Trail_Partial/) | Position management (BE / trail / partial) | EA dev | 6 | after P2.3 |
| [P2.5](../milestones/M2_Risk_Engine_and_Lifecycle/phases/P2.5_Execution_Feedback_Loop/) | Execution feedback loop | Bridge + EA | 5 | after P2.3 |
| [P2.6](../milestones/M2_Risk_Engine_and_Lifecycle/phases/P2.6_Error_Handling_and_Retry/) | Error handling & retry | Bridge dev | 6 | with P2.5 |
| [P2.7](../milestones/M2_Risk_Engine_and_Lifecycle/phases/P2.7_M2_Integration_and_Stabilization/) | M2 integration & stabilization | Lead | 4 | — |

### M3 — Dashboard & Monitoring

| Phase | Name | Owner | Est. hrs | Parallel? |
|---|---|---|---|---|
| [P3.1](../milestones/M3_Dashboard_and_Monitoring/phases/P3.1_Nextjs_Scaffolding_and_Auth/) | Next.js scaffolding + auth | UI dev | 4 | — |
| [P3.2](../milestones/M3_Dashboard_and_Monitoring/phases/P3.2_Signal_Log_and_Trade_History/) | Signal log + trade history | UI dev | 6 | with P3.3 |
| [P3.3](../milestones/M3_Dashboard_and_Monitoring/phases/P3.3_Realtime_Position_and_PnL/) | Realtime position + P&L | UI dev | 6 | with P3.2 |
| [P3.4](../milestones/M3_Dashboard_and_Monitoring/phases/P3.4_Execution_Quality_Analytics/) | Execution quality analytics | UI dev | 6 | with P3.5 |
| [P3.5](../milestones/M3_Dashboard_and_Monitoring/phases/P3.5_Configuration_UI/) | Configuration UI | UI dev | 5 | with P3.4 |
| [P3.6](../milestones/M3_Dashboard_and_Monitoring/phases/P3.6_Enhanced_Telegram_Reports/) | Enhanced Telegram (daily reports) | Bridge dev | 4 | — |
| [P3.7](../milestones/M3_Dashboard_and_Monitoring/phases/P3.7_M3_Integration_and_Stabilization/) | M3 integration & stabilization | Lead | 3 | — |

### M4 — Hardening & Forward Test

| Phase | Name | Owner | Est. hrs | Parallel? |
|---|---|---|---|---|
| [P4.1](../milestones/M4_Hardening_and_Forward_Test/phases/P4.1_Stress_and_Chaos_Tests/) | Stress & chaos tests | Bridge dev | 8 | with P4.2 |
| [P4.2](../milestones/M4_Hardening_and_Forward_Test/phases/P4.2_Security_Hardening/) | Security hardening | Bridge dev | 6 | with P4.1 |
| [P4.3](../milestones/M4_Hardening_and_Forward_Test/phases/P4.3_Demo_Forward_Test_2_Weeks/) | Demo forward test (≥2 wk) | Owner | continuous | runs over P4.4 + P4.5 |
| [P4.4](../milestones/M4_Hardening_and_Forward_Test/phases/P4.4_VPS_Production_Deployment/) | VPS production deployment | Ops | 6 | — |
| [P4.5](../milestones/M4_Hardening_and_Forward_Test/phases/P4.5_Backup_DR_Runbooks/) | Backup, DR, runbooks | Ops | 5 | with P4.4 |

### M5 — Live & Handover

| Phase | Name | Owner | Est. hrs | Parallel? |
|---|---|---|---|---|
| [P5.1](../milestones/M5_Live_and_Handover/phases/P5.1_Operator_Documentation/) | Operator documentation | Lead | 6 | with P5.2 |
| [P5.2](../milestones/M5_Live_and_Handover/phases/P5.2_Pilot_Live_Deployment_Small_Size/) | Pilot live (small size) | Owner + lead | 4 + monitoring | — |
| [P5.3](../milestones/M5_Live_and_Handover/phases/P5.3_Live_Monitoring_and_Tuning/) | Live monitoring & tuning | Owner | continuous | — |
| [P5.4](../milestones/M5_Live_and_Handover/phases/P5.4_Final_Acceptance_and_Signoff/) | Final acceptance & sign-off | Owner | 2 | — |
| [P5.5](../milestones/M5_Live_and_Handover/phases/P5.5_Handover_Package_and_KT/) | Handover package & KT | Lead + owner | 6 | — |

---

## Dependency graph (high level)

```
M0 ─▶ M1 ─▶ M2 ─▶ M3 ─▶ M4 ─▶ M5
              ▲
              │
              └─ M2 P2.5 (feedback loop) requires M2 P2.3 (EA hybrid mode)
```

Within each milestone, parallel-eligible phases are flagged in the tables above. The "stabilization" phase (`P*.7` or `P4.5`) is always last and serializes the milestone exit.

---

## Per-milestone cumulative effort

| Milestone | Phases | Est. hours | Cumulative |
|---|---|---|---|
| M0 | 4 | 16 | 16 |
| M1 | 7 | 39 | 55 |
| M2 | 7 | 43 | 98 |
| M3 | 7 | 34 | 132 |
| M4 | 5 | 25 + ≥2 wk monitoring | 157 + monitoring |
| M5 | 5 | 18 + monitoring | 175 + monitoring |

(PRD §12.1 estimated 134 dev hours; the +41 hours difference is the bootstrap + handover scope we explicitly added in M0/M5.)
