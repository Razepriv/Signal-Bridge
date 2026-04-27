# Risk Register (Cross-Cutting)

> Risks that span multiple milestones or affect the project as a whole live here. Phase-local risks live in each phase's `plan.md → Risks & Mitigations`.

**Reviewed:** 2026-04-27 (bootstrap). Owner: Webverse Arena.

## Severity / likelihood matrix

| Likelihood ↓ / Severity → | Low | Medium | High | Critical |
|---|---|---|---|---|
| **High** | watch | mitigate | mitigate | **escalate** |
| **Medium** | watch | watch | mitigate | mitigate |
| **Low** | accept | watch | watch | mitigate |

---

## Active risks

| ID | Risk | Severity | Likelihood | Owner | Mitigation | Status |
|---|---|---|---|---|---|---|
| **R-01** | VPS downtime during market hours | High | Low | Ops | Auto-restart services (NSSM), UptimeRobot heartbeat → Telegram, daily VPS image snapshot | Open |
| **R-02** | MT5 terminal disconnects from broker | High | Medium | Bridge dev | EA auto-reconnect, bridge `mt5.shutdown()`+`initialize()` retry loop, Telegram `Critical` alert on failure to reconnect within 30 s | Open |
| **R-03** | TradingView webhook delays / drops | Medium | Low | Bridge dev | Signal `timestamp` expiry (120 s), log every receive attempt, fallback to EA standalone strategy | Open |
| **R-04** | Throughput ceiling — bridge process GIL contention at >1 req/s | Medium | Low | Bridge dev | Single worker is sufficient at MVP; if cadence rises, refactor MT5 client into a process pool. Re-measure at end of M2 P2.7 | Open |
| **R-05** | Supabase free-tier quota breach (500 MB / 50 K MAU) | Low | Low | Owner | Metric on DB size + MAU in M3 dashboard; upgrade to Pro ($25/mo) before 80% utilization | Open |
| **R-06** | Incorrect lot sizing produces oversized position | **Critical** | Low | Bridge dev + EA dev | Dual-layer risk check (bridge §5.1 + EA §5.2), hard lot cap, daily loss kill switch in EA. Verified by M2 P2.1 acceptance tests | Open |
| **R-07** | Stale or duplicate signal executed | Medium | Medium | Bridge dev | `signals.signal_hash` UNIQUE index, 60 s dedup window, `timestamp` expiry, 5 min min-time-between-trades | Open |
| **R-08** | Strategy generates poor live signals (drawdown) | High | Medium | Owner | 2-week demo forward test (M4 P4.3), daily P&L review, strategy disable toggle in dashboard (M3 P3.5) | Open |
| **R-09** | Webhook endpoint compromised (spammed / spoofed) | High | Low | Bridge dev | Shared-secret auth, rate limiting (10 req/s), IP allowlist for TradingView, HTTPS only, body-not-URL secret | Open |
| **R-10** | Pine Script logic divergence between TV backtest and live alert | Medium | Medium | Strategy dev | Server-side alerts only, alert-on-bar-close only, side-by-side replay test in M2 P2.7 | Open |
| **R-11** | Telegram bot blocked / token rotated unexpectedly | Low | Low | Owner | Multiple chat targets configured, daily liveness ping, runbook procedure to rotate token (M5 P5.1) | Open |
| **R-12** | Schema drift between bridge code and Supabase | Medium | Low | Bridge dev | Migrations in `db/migrations/*.sql` versioned in git, CI step verifies live schema matches latest migration | Open |
| **R-13** | Single-developer key-person risk | High | Medium | Owner | Handover package (M5 P5.5) must let a non-author rebuild the system from zero — validated by recorded run-through | Open |
| **R-14** | Broker policy change (EAs disallowed, hedging removed) | High | Low | Owner | Maintain demo accounts on 2 brokers; runbook covers broker swap procedure (M5 P5.1) | Open |
| **R-15** | Cloudflare / DNS outage breaks webhook ingress | Medium | Low | Ops | Direct VPS IP fallback documented in runbook; UptimeRobot monitors webhook URL externally | Open |

## Closed risks

(none)

---

## Process

- Reviewed at every milestone exit (P*.7 / P4.5 / P5.4).
- New risks added by anyone — assign severity/likelihood + propose mitigation in same edit.
- A risk is **closed** only when its mitigation is *implemented and verified*, not when it's planned.
