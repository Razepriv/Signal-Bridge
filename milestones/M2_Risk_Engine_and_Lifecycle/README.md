# Milestone 2 — Risk Engine & Lifecycle

**Window:** Week 3–4
**PRD reference:** §10.2 (Phase 2), §5 (Risk Engine)
**Phases:** 7
**Exit gate:** all 10 bridge-level rules + 5 EA-level rules enforced and proven by tests; BE / trail / partial close working.

## Purpose

M1 proved the wire works. **M2 makes the wire safe.** This milestone adds the dual-layer risk engine (PRD §5) so a bad signal cannot blow up an account, plus the EA hybrid mode so the EA can both run its own strategy and accept commands from the bridge with execution-time risk overrides.

## What ships

- **Bridge-level rules** (§5.1): max risk/trade, daily DD, max open, max trades/day, correlation cap, min time between trades, max spread, signal expiry, weekend guard, news blackout (P2.1).
- **Dedup + idempotency** (`signal_hash` UNIQUE index, 60 s window) (P2.2).
- **EA hybrid mode** — accept bridge commands and run own strategy with hard risk caps (P2.3).
- **Position management** — breakeven, trailing, partial close (P2.4).
- **Execution feedback loop** — EA reports back fill / slippage / errors (P2.5).
- **Error handling & retry** with exponential backoff and circuit breaker (P2.6).
- **Stabilization** + integration testing (P2.7).

## Phases

| # | Phase |
|---|---|
| [P2.1](phases/P2.1_Bridge_Level_Risk_Rules/) | Bridge-level risk rules |
| [P2.2](phases/P2.2_Dedup_Expiry_Idempotency/) | Dedup, expiry, idempotency |
| [P2.3](phases/P2.3_EA_Hybrid_Mode/) | EA hybrid mode |
| [P2.4](phases/P2.4_Position_Management_BE_Trail_Partial/) | Position management — BE / trail / partial |
| [P2.5](phases/P2.5_Execution_Feedback_Loop/) | Execution feedback loop |
| [P2.6](phases/P2.6_Error_Handling_and_Retry/) | Error handling & retry |
| [P2.7](phases/P2.7_M2_Integration_and_Stabilization/) | M2 integration & stabilization |

## Exit

See [`exit-criteria.md`](exit-criteria.md).
