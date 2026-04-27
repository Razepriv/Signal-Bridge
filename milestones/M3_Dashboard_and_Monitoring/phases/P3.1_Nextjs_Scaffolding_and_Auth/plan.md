# P3.1 — Next.js Scaffolding + Supabase Auth (plan)

## Purpose

Stand up the Next.js 14 dashboard with Tailwind, shadcn/ui, and Supabase Auth gating all routes.

## Scope

### In scope
- `npx create-next-app@latest dashboard` with App Router + TypeScript + Tailwind
- Install shadcn/ui and configure theme
- Install @supabase/ssr; wire login/logout flow
- Protect all `/(dashboard)/*` routes via middleware redirect to /login
- Create operator user in Supabase Auth (email/password)
- Deploy a stub home page to Vercel preview

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

1. `npx create-next-app@latest dashboard` with App Router + TypeScript + Tailwind
2. Install shadcn/ui and configure theme
3. Install @supabase/ssr; wire login/logout flow
4. Protect all `/(dashboard)/*` routes via middleware redirect to /login
5. Create operator user in Supabase Auth (email/password)
6. Deploy a stub home page to Vercel preview

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
