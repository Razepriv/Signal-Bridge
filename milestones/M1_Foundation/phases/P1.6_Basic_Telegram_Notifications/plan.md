# P1.6 — Basic Telegram Notifications — plan

## Purpose

Send the operator a Telegram message on three M1 events: signal received, order executed, dispatch failed. Formatting and throttling are deliberately minimal — this is the 'is anything happening?' channel. Daily reports, weekly reports, and severity-aware throttling come in M3 P3.6.

## Scope

### In scope
- `bridge/app/telegram.py` — async client wrapping `python-telegram-bot`
- Three message types: signal_received, order_executed, dispatch_failed
- Plain-text formatting; emoji prefix per type
- Settings: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_IDS` (comma-separated)
- Fire-and-forget: never block the webhook response
- Tests with mocked Telegram HTTP

### Out of scope
- Daily / weekly digests (M3 P3.6)
- Inline buttons (M3 P3.6)
- Severity throttling / muting (M3 P3.6)
- Telegram /commands inbound (M3 P3.6)

## Inputs / Prereqs

- [ ] M0 P0.4: bot created via @BotFather, token in 1Password, chat ID known
- [ ] P1.4 done — dispatch returns DispatchResult we can format

## Deliverables

| Path | Description |
|---|---|
| `bridge/app/telegram.py` | `TelegramNotifier` async client |
| `bridge/app/notifications.py` | Event handlers: on_signal_received, on_order_executed, on_dispatch_failed |
| `bridge/tests/test_telegram.py` | Mocked-HTTP tests |

## Task breakdown

Each task ≤ 2 hours. **Write tests first** (global TDD rule).

1. Pin `python-telegram-bot>=21.0` in pyproject
2. Implement `TelegramNotifier.send(text, chat_ids)` — async, fire-and-forget under the hood
3. Compose the 3 message templates (with all the relevant fields from each event)
4. Wire notifier into the webhook flow at the right points (after signal insert, after fill, on dispatch failure)
5. Tests with mocked aiohttp/httpx returning success/failure

## Dependencies

- **Upstream:** P1.4 (dispatch result format); runs alongside P1.5
- **Downstream:** M3 P3.6 enhances this
- **External:** Telegram API reachable

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Bot token leaks | Critical | Low | .env + 1Password + secret scan |
| Telegram outage spams retries | Low | Low | One retry max in M1; full retry in M2 P2.6 |
| Wrong chat_id → silent fail | Medium | Medium | On-startup self-test sends a `system startup` message and asserts 200 |

## Exit Criteria

1. Test alert triggers a 'Signal received' Telegram message within 5 s
2. Successful fill triggers an 'Order executed' Telegram message within 5 s of fill
3. Dispatch failure triggers a 'Dispatch failed' Telegram message
4. Webhook latency unchanged (notifications fire-and-forget)
5. Tests pass; coverage on telegram.py ≥ 80%
6. No open CRITICAL/HIGH bug
7. `report.md` filled and signed
