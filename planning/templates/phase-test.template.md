# Phase Tests — {{Milestone ID}} / {{Phase ID}} — {{Phase name}}

> Template. Copy to a phase folder and fill in.

## Acceptance Tests

Each test is *given / when / then*. Tests must be written **before** the implementation (TDD) per [global rule](../../../../.claude/rules/common/testing.md). All tests must be automated unless explicitly marked `[manual]`.

### Test list

| ID | Type | Title | Status |
|---|---|---|---|
| T1 | unit | … | ⚪ |
| T2 | integration | … | ⚪ |
| T3 | e2e | … | ⚪ |
| T4 | manual | … | ⚪ |

### T1 — …

- **Given** …
- **When** …
- **Then** …
- **Implemented in** `path/to/test_file.py::test_name`

### T2 — …

…

## Unit / Integration / E2E split

- **Unit:** isolated, no I/O. Run on every commit.
- **Integration:** real Supabase test schema, mocked MT5. Run pre-merge.
- **E2E:** demo broker, demo Telegram chat, real network. Run pre-milestone-exit.

## Fixtures & test data

- `tests/fixtures/sample_alerts.json` — 12 well-formed payloads + 8 malformed
- `tests/fixtures/mt5_responses.py` — mocked `mt5.order_send` retcodes

## Coverage target

- ≥ 80% line coverage on new code in this phase (`pytest --cov`).
- Run `pytest --cov=bridge --cov-fail-under=80` in CI.

## Manual test steps

For tests marked `[manual]`:

1. …
2. …
3. **Expected:** …

(Embed screenshots in `bugs.md` if a manual test fails.)
