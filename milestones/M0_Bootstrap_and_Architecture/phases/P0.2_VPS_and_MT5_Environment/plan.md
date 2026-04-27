# P0.2 — VPS & MT5 Environment (plan)

## Purpose

Provision the Windows Server VPS, install MT5 + Python 3.11, set up an HTTPS tunnel for dev webhook ingress.

## Scope

### In scope
- Provision Windows Server 2022 VPS at chosen region (London or NY)
- Install MetaTrader 5 terminal; log in to demo broker account
- Install Python 3.11 and verify `pip install MetaTrader5` succeeds
- Install Cloudflare Tunnel (or ngrok for early dev) and forward to localhost:8000
- Run a dummy FastAPI listener and POST a test webhook through the tunnel
- Document VPS IP, RDP credentials, broker account in 1Password

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

1. Provision Windows Server 2022 VPS at chosen region (London or NY)
2. Install MetaTrader 5 terminal; log in to demo broker account
3. Install Python 3.11 and verify `pip install MetaTrader5` succeeds
4. Install Cloudflare Tunnel (or ngrok for early dev) and forward to localhost:8000
5. Run a dummy FastAPI listener and POST a test webhook through the tunnel
6. Document VPS IP, RDP credentials, broker account in 1Password

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
