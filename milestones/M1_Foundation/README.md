# Milestone 1 — Foundation

**Window:** Week 1–2
**PRD reference:** §10.1 (Phase 1)
**Phases:** 7 (all fully populated as the gold-standard reference)
**Exit gate:** demo TV alert lands on bridge → MT5 fills → Telegram pings; everything logged.

## Purpose

Stand up the **end-to-end happy path** with no risk engine, no dashboard, no fancy Telegram, no production hardening — just **proof that the wires are connected**. The first MT5 fill triggered by a TradingView webhook is the celebration moment for this milestone.

## What ships

By the end of M1:

- A Pine Script SMC strategy on XAUUSD M15 firing structured JSON alerts (P1.1).
- A FastAPI bridge with secret auth and Pydantic-validated payload parsing (P1.2).
- A Python MT5 connector that opens market orders with SL/TP (P1.3).
- An end-to-end demo on a demo broker (P1.4).
- Supabase tables with every signal and execution logged (P1.5).
- Telegram bot pinging on signal-received and order-executed (P1.6).
- One round of integration testing and bug-bash before M2 (P1.7).

## Phases

| # | Phase | Owner | Est. hrs |
|---|---|---|---|
| [P1.1](phases/P1.1_Pine_Script_SMC_XAUUSD_M15/) | Pine Script SMC strategy | Strategy dev | 8 |
| [P1.2](phases/P1.2_FastAPI_Webhook_Bridge_Skeleton/) | FastAPI webhook bridge skeleton | Bridge dev | 6 |
| [P1.3](phases/P1.3_MT5_Python_Connector/) | MT5 Python connector | Bridge dev | 6 |
| [P1.4](phases/P1.4_End_to_End_Demo_Pipeline/) | End-to-end demo pipeline | Bridge dev | 8 |
| [P1.5](phases/P1.5_Supabase_Schema_and_Signal_Log/) | Supabase schema + signal log | Bridge dev | 4 |
| [P1.6](phases/P1.6_Basic_Telegram_Notifications/) | Basic Telegram notifications | Bridge dev | 3 |
| [P1.7](phases/P1.7_M1_Integration_and_Stabilization/) | M1 integration & stabilization | Lead | 4 |

## Parallelism

```
P1.1 ─┐
      ├─▶ P1.4 ─▶ P1.7
P1.2 ─┴─▶ P1.3 ─┘
P1.5 ─┐
P1.6 ─┴─ run alongside P1.4
```

P1.1 (Pine) is independent of the bridge stack. P1.5 + P1.6 can run alongside P1.3/P1.4 since they don't share files. P1.7 serializes the milestone exit.

## Explicit non-goals (deferred to later milestones)

- **No risk engine** beyond a hard sanity cap in the bridge — full rules in M2.
- **No dedup / expiry** — M2.
- **No EA hybrid mode** — M2 (bridge calls MT5 directly via Python lib only).
- **No dashboard** — M3.
- **No daily reports / formatted Telegram** — M3.
- **No security hardening / TLS / IP allowlist** — M4 (dev tunnel is fine for M1).

## Exit

See [`exit-criteria.md`](exit-criteria.md).
