# Operations Runbook

> **Status:** stub. This runbook is populated incrementally during M4 (`P4.4_VPS_Production_Deployment`, `P4.5_Backup_DR_Runbooks`) and finalized in M5 (`P5.1_Operator_Documentation`).

The runbook is the single document an on-call operator reads to keep SignalBridge healthy in production. By the end of M5 it must answer every operational question without anyone needing to read the source code.

## Required sections (to be filled during M4/M5)

1. **Service inventory** — what runs where, on which ports, owned by which Windows service.
2. **Start / stop / restart procedures** — exact commands and expected output for each service.
3. **Health checks** — how to verify the bridge, MT5 terminal, Supabase connection, and Telegram bot are healthy.
4. **Common alerts and responses** — for each Telegram `Critical` event, the exact remediation steps.
5. **Disconnection recovery** — MT5 reconnect, Supabase reconnect, broker-side outages.
6. **Risk parameter changes** — how to safely edit risk params live without restarting.
7. **Strategy enable / disable** — turning a Pine strategy off without touching TradingView.
8. **Backup and restore** — Supabase point-in-time recovery, EA settings backup, VPS image snapshots.
9. **Disaster recovery** — full rebuild from zero, RTO/RPO targets.
10. **Incident logging** — where post-mortems live, the template to use.
11. **Maintenance windows** — when to deploy, how to gate against market hours.
12. **Escalation contacts** — who gets called for what, and at which severity.

## Cross-references

- Cross-cutting risks: [`../../planning/risk-register.md`](../../planning/risk-register.md)
- Architecture: [`../architecture/README.md`](../architecture/README.md)
- Handover doc (final): [`../handover/README.md`](../handover/README.md)
