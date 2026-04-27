# M4 Exit Criteria

All must be true before declaring M4 complete and starting M5.

## Stress / chaos (P4.1)

- [ ] **S1** Rapid-fire 50 signals in 30 s — system either accepts/dedups all correctly or rejects with reason; no crashes, no DB inconsistency.
- [ ] **S2** Kill MT5 terminal mid-order — bridge reconnects within 30 s, retry queue drains, Telegram critical alert fires once and stops once recovered.
- [ ] **S3** Supabase blackout 5 min — bridge queues writes locally; on reconnect, no rows lost, ordering preserved.
- [ ] **S4** Telegram blackout — events drop after 1 retry; system unaffected.
- [ ] **S5** Network partition between TV and VPS — signals during partition are lost (TV doesn't retry); when restored, normal operation resumes within 1 alert.

## Security (P4.2)

- [ ] **Sec1** All ingress over HTTPS via Cloudflare; HTTP redirects to HTTPS.
- [ ] **Sec2** Webhook endpoint rate-limited to 10 req/s per source IP.
- [ ] **Sec3** TradingView IP ranges allowlisted at Cloudflare; all other IPs return `403`.
- [ ] **Sec4** Webhook secret rotated; rotation procedure documented in runbook.
- [ ] **Sec5** Dashboard accessible only from operator's IP allowlist.
- [ ] **Sec6** Supabase RLS enabled on all tables; service-role key only on the VPS, never in dashboard bundle.
- [ ] **Sec7** No secret in git history (`git secrets`-equivalent scan green).
- [ ] **Sec8** Dependency vulnerability scan (pip-audit, `npm audit`) — zero `High` or `Critical`.

## Forward test (P4.3) — must run ≥ 14 calendar days

- [ ] **F1** ≥ 30 trades captured in `trades` table during the test
- [ ] **F2** ≥ 99.5% uptime measured (UptimeRobot)
- [ ] **F3** Zero rule breaches (`rejection_reason` for risk rules logged correctly, no executions outside config)
- [ ] **F4** Average slippage on XAUUSD ≤ 5 points (M5 tightens to ≤3)
- [ ] **F5** End-to-end latency p95 ≤ 2.5 s (M5 tightens to ≤2)
- [ ] **F6** Daily reports delivered every trading day, no gaps
- [ ] **F7** Forward test report drafted in `P4.3/report.md` summarising every issue found and how fixed

## Production deployment (P4.4)

- [ ] **P1** Bridge runs as a Windows service via NSSM, auto-restart on failure
- [ ] **P2** MT5 terminal auto-launches on VPS boot and logs into broker
- [ ] **P3** Dashboard deployed to Vercel with production env vars
- [ ] **P4** UptimeRobot monitors `/api/v1/status` every minute
- [ ] **P5** Loki + Grafana (or alternative) collect bridge structured logs

## Backup / DR (P4.5)

- [ ] **B1** Supabase Pro upgraded; daily backups + PITR enabled
- [ ] **B2** VPS daily image snapshot from provider; retention ≥7 days
- [ ] **B3** Telegram bot token + Supabase keys + MT5 password backed up to operator's password manager
- [ ] **B4** Recovery test executed: full rebuild from VPS snapshot in ≤2 hours, documented

## Reports

- [ ] All `P4.*/report.md` filled and signed
- [ ] No open `CRITICAL` or `HIGH` bug across `P4.*/bugs.md`
- [ ] Risk register reviewed and updated

## Demo gate

- [ ] **G4:** Forward-test summary report published as `docs/handover/m4-forward-test-report.md` with all metrics, all issues found, all fixes verified.
