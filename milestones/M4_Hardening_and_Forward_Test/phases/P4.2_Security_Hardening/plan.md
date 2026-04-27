# P4.2 — Security Hardening (plan)

## Purpose

Lock the production attack surface to TLS, allowlists, rotation, secret scans, and dependency audits.

## Scope

### In scope
- Cloudflare TLS termination; HTTP→HTTPS redirect
- Rate limit 10 req/s per source IP at Cloudflare
- Allowlist TradingView IPs; reject all other webhook source IPs with 403
- Operator IP allowlist on dashboard via Cloudflare Access
- Rotate webhook secret; document rotation procedure
- Verify Supabase RLS on every table
- Run pip-audit and npm audit; fix all High/Critical
- git-secrets scan in CI

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

1. Cloudflare TLS termination; HTTP→HTTPS redirect
2. Rate limit 10 req/s per source IP at Cloudflare
3. Allowlist TradingView IPs; reject all other webhook source IPs with 403
4. Operator IP allowlist on dashboard via Cloudflare Access
5. Rotate webhook secret; document rotation procedure
6. Verify Supabase RLS on every table
7. Run pip-audit and npm audit; fix all High/Critical
8. git-secrets scan in CI

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
