# Milestone 3 — Dashboard & Monitoring

**Window:** Week 5–6
**PRD reference:** §10.3 (Phase 3), §8 (Admin Dashboard)
**Phases:** 7
**Exit gate:** all 7 dashboard pages live; daily Telegram report delivered.

## Purpose

M2 made the system safe but invisible. **M3 makes it observable.** Build the Next.js admin dashboard (PRD §8) on top of the Supabase realtime feed, plus the daily/weekly Telegram reports that turn raw events into a digest the owner actually reads.

## What ships

- Next.js 14 + Tailwind + shadcn/ui scaffold with Supabase Auth (P3.1).
- Dashboard pages: home, signal log, trade history, execution quality, risk monitor, configuration, system health (P3.2–P3.5 across pages).
- Realtime position + P&L using Supabase Realtime subscriptions (P3.3).
- Execution quality analytics: slippage histogram, latency p50/p95/p99, fill rate, spread distribution (P3.4).
- Configuration UI to edit risk params and toggle strategies live (P3.5).
- Enhanced Telegram: daily report at session close, weekly report Sunday, severity-aware throttling (P3.6).
- Stabilization (P3.7).

## Phases

| # | Phase |
|---|---|
| [P3.1](phases/P3.1_Nextjs_Scaffolding_and_Auth/) | Next.js scaffolding + Supabase auth |
| [P3.2](phases/P3.2_Signal_Log_and_Trade_History/) | Signal log + trade history |
| [P3.3](phases/P3.3_Realtime_Position_and_PnL/) | Realtime position + P&L |
| [P3.4](phases/P3.4_Execution_Quality_Analytics/) | Execution quality analytics |
| [P3.5](phases/P3.5_Configuration_UI/) | Configuration UI |
| [P3.6](phases/P3.6_Enhanced_Telegram_Reports/) | Enhanced Telegram reports |
| [P3.7](phases/P3.7_M3_Integration_and_Stabilization/) | M3 integration & stabilization |

## Exit

See [`exit-criteria.md`](exit-criteria.md).
