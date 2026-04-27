# Phase Bugs — {{Milestone ID}} / {{Phase ID}} — {{Phase name}}

> Template. Copy to a phase folder. Active bugs only — closed bugs move to the milestone-level archive in `report.md`.

## Severity definitions

| Severity | Definition | Exit-blocking? |
|---|---|---|
| **CRITICAL** | Causes data loss, financial loss, or full system outage. | ✅ Yes — blocks phase exit |
| **HIGH** | Breaks a primary acceptance test or KPI target; no clean workaround. | ✅ Yes — blocks phase exit |
| **MEDIUM** | Affects UX/quality but workaround exists; defer if needed. | ❌ No — but track |
| **LOW** | Cosmetic, typo, log-level. | ❌ No |

## Active bugs

| ID | Severity | Title | Repro | Owner | Status | Found-on | Fixed-on |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Bug template (copy when adding)

### B-NN — Title

- **Severity:** CRITICAL / HIGH / MEDIUM / LOW
- **Status:** OPEN / IN PROGRESS / FIXED / WONTFIX
- **Found:** YYYY-MM-DD by …
- **Owner:** …
- **Affected commit / version:** …

**Repro**

1. …
2. …
3. **Expected:** …
4. **Actual:** …

**Logs / screenshots**

```
…
```

**Root cause** (filled at fix time)

…

**Fix**

- Commit: …
- File(s): …
- Test added: `tests/...`
