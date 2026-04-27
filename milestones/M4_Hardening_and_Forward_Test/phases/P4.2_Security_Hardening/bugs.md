# P4.2 — Security Hardening (bugs)

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
