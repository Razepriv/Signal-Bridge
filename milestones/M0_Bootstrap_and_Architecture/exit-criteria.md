# M0 Exit Criteria

All must be true before declaring M0 complete and starting M1.

## Repository

- [ ] `Razepriv/Signal-Bridge` exists on GitHub with the bootstrap structure on `main`
- [ ] `.gitignore` covers Python, Node, MT5, Supabase, secrets
- [ ] `pyproject.toml` defines Python 3.11+ as required interpreter and pins ruff/black/mypy/pytest versions
- [ ] Pre-commit hooks run (`ruff`, `black`, `mypy --strict` on `bridge/`)
- [ ] GitHub Actions CI runs on PRs and `push` to `main` — lint + type-check + pytest jobs all green on the empty scaffold

## VPS / MT5

- [ ] Windows Server 2022 VPS reachable over RDP from operator workstation
- [ ] MetaTrader 5 terminal installed and logged in to the demo broker account
- [ ] Python 3.11 installed system-wide; `pip install MetaTrader5 fastapi uvicorn supabase python-telegram-bot pydantic-settings structlog` succeeds
- [ ] Cloudflare Tunnel (or ngrok during early dev) provides an HTTPS URL routable to `localhost:8000` on the VPS
- [ ] A test webhook hitting that URL is logged by a dummy FastAPI listener

## Architecture decisions

- [ ] ADR-0001 (bridge runtime) committed with status `Accepted`
- [ ] ADR-0002 (database) committed with status `Accepted`
- [ ] ADR-0003 (MT5 transport) committed with status `Accepted`
- [ ] `docs/architecture/data-flow.md` reviewed and matches PRD §3.1

## Accounts / vendors

- [ ] Demo MT5 broker account credentials saved in 1Password (or equivalent) — never in repo
- [ ] TradingView Pro+ subscription active (required for webhook alerts)
- [ ] Telegram bot created via @BotFather, token saved, target chat ID known
- [ ] Supabase project created, anon + service-role keys saved, URL recorded
- [ ] Domain registered (e.g., `signalbridge.example.com`) and proxied via Cloudflare with SSL

## Phase reports

- [ ] `P0.1/report.md` → `Done`
- [ ] `P0.2/report.md` → `Done`
- [ ] `P0.3/report.md` → `Done`
- [ ] `P0.4/report.md` → `Done`
- [ ] No open `CRITICAL` or `HIGH` bug across `P0.*/bugs.md`

## Tracker

- [ ] `planning/milestone-tracker.md` shows M0 as `🟢 Done`
- [ ] M0 completion entry added to "Recent changes"
