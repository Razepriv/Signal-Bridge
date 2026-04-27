# P1.1 — Pine Script SMC Strategy (XAUUSD M15) — plan

## Purpose

Author a TradingView Pine Script v6 **strategy** (not indicator) that detects Smart Money Concepts setups on XAUUSD M15 and emits a structured JSON alert payload conforming to PRD §4.1 every time `strategy.entry` fires. This is the upstream signal source for everything that follows.

## Scope

### In scope
- Pine v6 strategy file `pine/Gold_SMC_v1.pine`
- Inputs for SL/TP in points (+ live `plot()` outputs so `{{plot("SL")}}` resolves in alerts)
- One `strategy_id` value (`smc_lo_v1`) — no strategy_id-switching this phase
- Server-side alert condition (using `alert()` / `alertcondition()`) so the alert fires on bar close, not tick
- The alert message body matching PRD Appendix A exactly (with `{{strategy.order.action}}` placeholders)
- Backtest configuration: realistic commission, slippage, account size

### Out of scope
- Multiple strategies / strategy marketplace (PRD §14, deferred to v2.0)
- Multi-timeframe / multi-symbol (M2 + later)
- News blackout in Pine (handled bridge-side in M2 P2.1)
- Confidence scoring beyond a static value (M3+)

## Inputs / Prereqs

- [ ] M0 P0.4: TradingView Pro+ subscription active
- [ ] Operator workstation can edit and save Pine scripts in the TradingView Pine Editor
- [ ] Webhook secret value chosen and saved in 1Password (will be substituted into the alert template)

## Deliverables

| Path | Description |
|---|---|
| `pine/Gold_SMC_v1.pine` | The strategy source |
| `pine/alert-template.json` | Copy-paste payload body for TradingView alert UI (with `<SECRET>` placeholder) |
| `pine/README.md` | How to import into TradingView, set inputs, attach an alert |
| `pine/backtest-2024.csv` | Exported one-year backtest result on demo account |

## Task breakdown

Each task ≤ 2 hours.

1. **Skeleton:** create `Gold_SMC_v1.pine` with `strategy()` declaration, default qty 1, commission, slippage, hedging mode off
2. **SMC detection:** code the entry signal (BOS / CHOCH / order block tap — keep first version simple, ~30 lines)
3. **SL / TP plot lines:** add `plot(sl, "SL")` and `plot(tp, "TP")` on the chart so `{{plot("SL")}}` resolves
4. **Strategy entry:** `strategy.entry("LONG"/"SHORT", strategy.long/short)` and `strategy.exit` with `stop=` / `limit=`
5. **Alert message:** craft the `alert()` call with the exact JSON body matching PRD Appendix A
6. **Backtest:** run on XAUUSD M15 for 2024 calendar year; export performance summary
7. **Sanity test:** trigger a manual alert and confirm it lands at any HTTP listener via the M0 tunnel
8. **Doc:** write `pine/README.md` and `pine/alert-template.json`

## Dependencies

- **Upstream:** M0 P0.4 (TV Pro+, secret value)
- **Downstream:** P1.4 (end-to-end demo) needs this to fire
- **External:** TradingView platform availability

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Pine logic divergence between TV backtest and live alert behavior | Medium | Medium | Use server-side alerts only; fire on bar close; replay-test in M2 P2.7 |
| TradingView webhook IP changes drop our allowlist | High | Low | Maintain TV's published IP list; alerts to runbook (M4 P4.2) |
| Backtest looks great, live performance dies | High | Medium | Risk register R-08; mandatory 2-week demo forward test in M4 P4.3 |
| Alert payload schema changes (TV adds/renames placeholders) | Low | Low | Pin to `{{strategy.order.action}}` and `{{plot}}` (stable); document schema version |

## Exit Criteria

1. `Gold_SMC_v1.pine` compiles in Pine Editor with zero errors and zero warnings
2. Backtest on XAUUSD M15 (2024) completes; results exported to `pine/backtest-2024.csv`
3. A test alert fires within 30 s of attaching the strategy and lands at the M0 tunnel listener with valid JSON
4. JSON payload validates against the Pydantic schema that will be authored in P1.2 (manual `jq` check is fine for now; full coupling at P1.4)
5. All acceptance tests in [`test.md`](test.md) pass
6. No open `CRITICAL` or `HIGH` bug in [`bugs.md`](bugs.md)
7. [`report.md`](report.md) filled and signed
