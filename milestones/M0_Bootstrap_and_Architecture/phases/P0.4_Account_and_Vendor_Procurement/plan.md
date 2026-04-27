# P0.4 — Account & Vendor Procurement (plan)

## Purpose

Procure every external account and key the project depends on, before any code is written that needs them.

## Scope

### In scope
- Open MT5 demo account at chosen broker; record server name + login + password
- Subscribe to TradingView Pro+ (required for webhook alerts)
- Create Telegram bot via @BotFather; record token; create personal/group chat; record chat ID
- Create Supabase project; record URL, anon key, service-role key
- Register domain (e.g. signalbridge.example.com); proxy via Cloudflare; enable SSL
- Save all credentials in 1Password (or equivalent) — never in repo

### Out of scope
- Anything not listed above; defer to the appropriate later phase.

## Inputs / Prereqs

- [ ] All upstream phases marked Done in [milestone-tracker.md](../../../../planning/milestone-tracker.md)
- [ ] Prior milestone exit criteria met
- [ ] Required vendor accounts active (see [planning/risk-register.md](../../../../planning/risk-register.md))

## Deliverables

| Path | Description |
|---|---|
| _to be filled at phase kickoff_ | _path of artefact_ |

## Task breakdown

Each task ≤ 2 hours. Ordered.

1. Open MT5 demo account at chosen broker; record server name + login + password
2. Subscribe to TradingView Pro+ (required for webhook alerts)
3. Create Telegram bot via @BotFather; record token; create personal/group chat; record chat ID
4. Create Supabase project; record URL, anon key, service-role key
5. Register domain (e.g. signalbridge.example.com); proxy via Cloudflare; enable SSL
6. Save all credentials in 1Password (or equivalent) — never in repo

## Dependencies

- **Upstream:** see milestone roadmap
- **Downstream:** the phase numbered immediately after this one in the same milestone, plus `P*.7` (or `P4.5` for M4) integration phase
- **External:** see [risk-register.md](../../../../planning/risk-register.md)

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| _filled at kickoff_ | | | |

## Exit Criteria

1. All tasks above complete with code committed
2. All acceptance tests in [`test.md`](test.md) pass
3. Coverage ≥ 80% on new code
4. No open `CRITICAL` or `HIGH` bug in [`bugs.md`](bugs.md)
5. [`report.md`](report.md) filled and signed
