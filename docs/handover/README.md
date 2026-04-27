# Handover Package

> **Status:** stub. Populated during Milestone 5 — Live & Handover (`P5.5_Handover_Package_and_KT`).

The handover package is the deliverable that closes the project. When this folder is complete and signed, SignalBridge transitions from "in development" to "in production, owner-operated."

## What goes here (to be produced in M5 P5.5)

| Artefact | Purpose |
|---|---|
| `README.md` (this file, finalized) | Index of the handover package |
| `system-overview.md` | One-page system summary for non-engineering stakeholders |
| `operator-quickstart.md` | "From zero to first trade" — VPS rebuild instructions, repo clone, secrets restore, MT5 login, Telegram bot setup |
| `operator-cheatsheet.md` | The 10 most common ops tasks, each as a copy-pasteable runbook |
| `architecture-snapshot.pdf` | Frozen architecture diagram + ADRs at handover date |
| `credentials-rotation.md` | Procedure to rotate the webhook secret, MT5 password, Supabase keys, Telegram bot token |
| `kpi-baseline.md` | Live-trading KPI baselines from M5 P5.3 |
| `support-window.md` | What support is included post-handover, for how long, on what channels |
| `signoff.md` | Final sign-off page (developer + owner signatures, date, repo SHA) |

## Acceptance gate (M5 P5.4 → P5.5)

Handover cannot start until:

1. M5 P5.2 (pilot live deployment) has run for ≥7 calendar days with zero `CRITICAL` incidents.
2. M5 P5.3 has produced KPI baselines that hit or beat PRD §11 targets.
3. The owner has driven through the operator quickstart end-to-end on a fresh VPS to validate it (recorded video).
4. All M0–M5 phase `report.md` files are `Done` with no open `CRITICAL` or `HIGH` bugs.

Then `P5.5` produces this folder's full content, and `signoff.md` is signed.
