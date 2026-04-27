# ADR-0002 — Database: Supabase (Managed Postgres)

**Status:** Accepted (2026-04-27)
**Deciders:** Webverse Arena (single dev)
**Context:** Milestone 0 — Bootstrap

## Context

We need persistence for three core tables — `signals`, `executions`, `trades` (PRD §6) — plus configuration, audit logs, and metrics over time. The dashboard (M3) needs **realtime subscriptions** to render live position updates and a streaming signal log without polling.

Constraints:

- Single dev, no DBA, no ops budget.
- The bridge VPS already runs MT5 and FastAPI; adding Postgres + replication + backups there is a maintenance burden we don't want.
- Free or near-free tier preferred for MVP.
- Must support row-level security (RLS) since the dashboard will eventually be multi-user.

## Decision

**Use Supabase (managed PostgreSQL with auth, realtime, and storage) for all persistent data.** Use Supabase's free tier through MVP; upgrade to Pro ($25/mo) if/when we cross the 500 MB DB or 50 K MAU caps.

## Rationale

| Criterion | Supabase | Self-hosted Postgres on VPS | SQLite (file) | Decision |
|---|---|---|---|---|
| Realtime subs | ✅ built-in | ❌ manual LISTEN/NOTIFY plumbing | ❌ | ✅ Supabase |
| RLS / Auth | ✅ Postgres RLS + Supabase Auth | ✅ but DIY auth | ❌ | ✅ Supabase |
| Backups | ✅ daily automatic | ❌ DIY | ❌ DIY | ✅ Supabase |
| Cost (MVP) | $0 free tier | VPS RAM + ops time | $0 | ✅ Supabase |
| Cost (scale) | $25/mo Pro | VPS upgrade + DBA time | N/A | Tied |
| Dashboard integration | ✅ first-class JS client | manual REST | ❌ | ✅ Supabase |
| Latency (bridge→DB) | ~50–200 ms (region-dependent) | ~1 ms (localhost) | sub-ms | ❌ Supabase loses |

The latency hit is *not* on the critical path: the signal-to-fill latency budget is dominated by the bridge→MT5 hop (in-process per ADR-0001), and DB writes happen *asynchronously after* the order is sent. We log fire-and-forget so a slow Supabase round-trip never delays a fill.

## Consequences

**Positive**

- Realtime out of the box → simplifies the M3 dashboard substantially.
- RLS enables future multi-tenant or copy-trading expansion (PRD §14) without a rewrite.
- Daily backups, point-in-time recovery on Pro — eliminates a major operational risk.
- One vendor for DB + auth + storage + realtime; less surface area to learn.

**Negative / accepted trade-offs**

- Vendor lock-in. Mitigation: schema is plain Postgres (`db/migrations/*.sql`); we can migrate to any Postgres host with `pg_dump`/`pg_restore` if needed.
- Internet dependency for the bridge's writes. Mitigation: DB writes are off the critical path; if Supabase is unreachable, the bridge logs to a local SQLite WAL and replays on reconnect (implemented in M2 P2.6).
- Free-tier limits: 500 MB DB, 2 GB egress, 50 K MAU. Tracked in [risk-register.md](../../planning/risk-register.md) as `R-05 Supabase quota`.

## Alternatives considered

- **Self-hosted Postgres on the same VPS.** Rejected: extra ops, no realtime sub framework, manual backups, no benefit unless we already had a DBA.
- **SQLite local file.** Rejected: no realtime, no multi-process safety, no future multi-tenancy.
- **MongoDB / DynamoDB.** Rejected: relational queries (P&L by day, slippage histograms) are far more natural in SQL.

## Supersedes / superseded by

- Supersedes: nothing.
- Superseded by: nothing (current).

## References

- PRD §6 (Database Schema) — [`../PRD/SignalBridge_PRD_v1.md`](../PRD/SignalBridge_PRD_v1.md#6-database-schema-supabase)
- PRD §8.2 (Dashboard tech stack) — same file
