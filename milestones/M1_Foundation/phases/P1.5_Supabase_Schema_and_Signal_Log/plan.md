# P1.5 — Supabase Schema + Signal Log — plan

## Purpose

Apply the database migrations for `signals`, `executions`, `trades` (PRD §6) and wire the bridge to log every signal received and every execution result. M1 logging is fire-and-forget — failure to write does NOT block the order.

## Scope

### In scope
- `db/migrations/0001_initial.sql` — signals, executions, trades, signal_status_enum, execution_status_enum
- RLS enabled (deny-all by default); service-role key has full access
- `bridge/app/supabase_client.py` — thin async wrapper
- Bridge writes a `signals` row on receive (status RECEIVED), updates to VALIDATED then EXECUTED/FAILED
- Bridge writes an `executions` row on fill
- Trades table left empty in M1 (filled in M2 P2.5 — execution feedback loop)

### Out of scope
- Trade lifecycle writes (M2 P2.5)
- Local SQLite WAL fallback (M2 P2.6)
- Realtime subscriptions consumption (M3 P3.3)
- Config / audit tables (M3 P3.5)

## Inputs / Prereqs

- [ ] M0 P0.4: Supabase project + URL + service-role key
- [ ] P1.2 done — bridge accepts payloads

## Deliverables

| Path | Description |
|---|---|
| `db/migrations/0001_initial.sql` | DDL for signals, executions, trades, enums, indices, RLS |
| `db/README.md` | How migrations are applied; never edit a committed migration |
| `bridge/app/supabase_client.py` | Async wrapper around `supabase` Python client |
| `bridge/app/repositories/signals.py` | `insert_signal`, `update_signal_status` |
| `bridge/app/repositories/executions.py` | `insert_execution` |
| `bridge/tests/test_repositories.py` | Tests against a Supabase test schema |

## Task breakdown

Each task ≤ 2 hours. **Write tests first** (global TDD rule).

1. Author migration SQL (`signals` table per PRD §6.1, `executions` per §6.2, `trades` per §6.3)
2. Add CHECK constraints on enums (status, action)
3. Add indices: `signals(received_at)`, `signals(strategy_id)`, `signals(signal_hash)` (UNIQUE — prepared for M2)
4. Apply migration to Supabase project (SQL editor or `supabase db push`)
5. Enable RLS on all three tables; default deny
6. Implement async Supabase client wrapper with timeout
7. Implement signals & executions repositories
8. Update webhook → dispatch path: insert signal RECEIVED before dispatch, transition statuses, insert execution after fill
9. Make all DB writes fire-and-forget via `asyncio.create_task` so they never block the response
10. Add tests against a Supabase test project (separate from prod)

## Dependencies

- **Upstream:** P1.2; runs alongside P1.4
- **Downstream:** P1.7 stabilization checks DB has the expected rows after each test alert
- **External:** Supabase project reachable; service-role key present

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Schema migrations not idempotent → CI re-runs fail | Medium | Medium | All migrations use IF NOT EXISTS / CREATE OR REPLACE; numbered, never edited in place |
| Service-role key exposed | Critical | Low | .env in gitignore; pre-commit secret scan; key only on VPS |
| Supabase write blocks bridge response | High | Low | Fire-and-forget via asyncio.create_task; tests confirm response time unaffected |
| RLS misconfigured letting anon writes through | Critical | Low | Test from anon key explicitly fails; deny-all default |

## Exit Criteria

1. Migration applied to Supabase; `select * from signals` works as service role
2. RLS verified: anon key can SELECT zero rows; service role can SELECT all
3. Webhook + dispatch flow inserts signal + execution rows
4. Latency of webhook response unaffected (still p95 < 50 ms — DB writes off path)
5. All tests pass; coverage on repositories ≥ 80%
6. No open CRITICAL/HIGH bug
7. `report.md` filled and signed
