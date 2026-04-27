# P0.1 — Repo & Tooling Bootstrap (plan)

## Purpose

Initialize the git repo, define Python project layout, configure pre-commit and CI so every later commit is linted and type-checked.

## Scope

### In scope
- git init and add remote pointing to Razepriv/Signal-Bridge
- Author root README.md and .gitignore (Python + Node + MT5 + secrets)
- Create pyproject.toml with Python 3.11+; pin ruff, black, mypy, pytest versions
- Set up pre-commit hooks (ruff, black, mypy --strict on bridge/)
- Create .github/workflows/ci.yml with lint + type-check + pytest jobs
- Push initial scaffold commit and verify CI green

### Out of scope
- Anything not listed above; defer to the appropriate later phase.

## Inputs / Prereqs

- [ ] All upstream phases marked Done in [milestone-tracker.md](../../../../planning/milestone-tracker.md)
- [ ] Prior milestone exit criteria met
- [ ] Required vendor accounts active (see [planning/risk-register.md](../../../../planning/risk-register.md))

## Deliverables

| Path | Description |
|---|---|
| _to be filled at phase kickoff_ | _path of artefact_ |

## Task breakdown

Each task ≤ 2 hours. Ordered.

1. git init and add remote pointing to Razepriv/Signal-Bridge
2. Author root README.md and .gitignore (Python + Node + MT5 + secrets)
3. Create pyproject.toml with Python 3.11+; pin ruff, black, mypy, pytest versions
4. Set up pre-commit hooks (ruff, black, mypy --strict on bridge/)
5. Create .github/workflows/ci.yml with lint + type-check + pytest jobs
6. Push initial scaffold commit and verify CI green

## Dependencies

- **Upstream:** see milestone roadmap
- **Downstream:** the phase numbered immediately after this one in the same milestone, plus `P*.7` (or `P4.5` for M4) integration phase
- **External:** see [risk-register.md](../../../../planning/risk-register.md)

## Risks & Mitigations

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| _filled at kickoff_ | | | |

## Exit Criteria

1. All tasks above complete with code committed
2. All acceptance tests in [`test.md`](test.md) pass
3. Coverage ≥ 80% on new code
4. No open `CRITICAL` or `HIGH` bug in [`bugs.md`](bugs.md)
5. [`report.md`](report.md) filled and signed
