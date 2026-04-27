# P1.2 — FastAPI Webhook Bridge Skeleton — bugs

## Severity definitions

| Severity | Definition | Exit-blocking? |
|---|---|---|
| **CRITICAL** | Data loss, financial loss, or full outage. | ✅ Yes |
| **HIGH** | Breaks a primary acceptance test or KPI target; no clean workaround. | ✅ Yes |
| **MEDIUM** | Affects UX/quality but workaround exists. | ❌ No |
| **LOW** | Cosmetic, typo, log-level. | ❌ No |

## Active bugs

| ID | Severity | Title | Repro | Owner | Status | Found-on | Fixed-on |
|---|---|---|---|---|---|---|---|
| _none yet_ | | | | | | | |

## Watchlist (potential issues found while writing tests, not yet bugs)

- Pydantic `Decimal` field default may render as float in JSON unless `model_config` is set — verify in T6 before moving on
- FastAPI's default 422 body shape may differ from what tests expect; pin the shape in T3/T4 explicitly
- `secrets.compare_digest` requires equal-length inputs — if attacker sends a much-longer secret, length leaks; add a fast prefix length-check that does not short-circuit on length

## Bug template (copy when adding)

```
### B-NN — Title

- Severity: CRITICAL / HIGH / MEDIUM / LOW
- Status: OPEN / IN PROGRESS / FIXED / WONTFIX
- Found: YYYY-MM-DD by …
- Owner: …
- Affected commit: …

Repro:
1. …
2. …
3. Expected: …
4. Actual: …

Logs / screenshots: …

Root cause (filled at fix time): …

Fix:
- Commit: …
- File(s): …
- Test added: …
```
