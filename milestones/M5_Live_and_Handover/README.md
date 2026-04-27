# Milestone 5 — Live & Handover

**Window:** Week 8+
**PRD reference:** §10.4 (Phase 4 second half) + new (handover added during bootstrap)
**Phases:** 5
**Exit gate:** pilot live for ≥7 days with zero `CRITICAL` incidents; runbook signed; KT delivered.

## Purpose

Take SignalBridge from "demo-tested and hardened" to "running real money under operator control, with the operator able to keep it running independently." This is the **finish line** of the project.

## What ships

- Operator documentation: setup-from-zero guide, ops cheatsheet, escalation matrix (P5.1).
- Pilot live deployment with the smallest position size the broker allows (P5.2).
- 7-day live monitoring with daily KPI sweeps and any tuning the live data demands (P5.3).
- Final acceptance: KPI baselines vs PRD §11 targets, sign-off (P5.4).
- Handover package: everything the operator needs to run SignalBridge without the original developer (P5.5).

## Phases

| # | Phase |
|---|---|
| [P5.1](phases/P5.1_Operator_Documentation/) | Operator documentation |
| [P5.2](phases/P5.2_Pilot_Live_Deployment_Small_Size/) | Pilot live (small size) |
| [P5.3](phases/P5.3_Live_Monitoring_and_Tuning/) | Live monitoring & tuning |
| [P5.4](phases/P5.4_Final_Acceptance_and_Signoff/) | Final acceptance & sign-off |
| [P5.5](phases/P5.5_Handover_Package_and_KT/) | Handover package & KT |

## Exit

See [`exit-criteria.md`](exit-criteria.md). On exit, this repo is **closed for new feature work** without a v2.0 PRD; ongoing changes are operational only (config tweaks, runbook updates, security patches).
