# Platform inventory — refresh before routing

Copy to `DEPLOY.md` in the project (or a private notes file). Fill from each
platform's usage page or CLI. Mark **blocked** at > 80% of any limit.

| Platform | Tier | Limit that bites first | Used / limit | % | Status | Checked |
|---|---|---|---|---|---|---|
| Edge/static host (e.g. Cloudflare Pages / Vercel Hobby) | free | builds/mo · requests/day | | | | |
| Serverless functions | free | invocations · CPU-ms | | | | |
| Managed containers (e.g. Railway / Fly / Render) | usage-based | $ credit remaining · vCPU-hours | | | | |
| Managed Postgres (e.g. Supabase) | free | DB size · MAU · egress | | | | |
| CI (GitHub Actions) | free | minutes/mo | | | | |
| LLM API router (e.g. OpenRouter) | prepaid | $ balance | | | | |
| Home server | owned | RAM headroom · disk free · uptime | | | | |
| Cloud account (e.g. GCP/AWS free tier) | free | credits · always-free caps | | | | |

## Running services (monthly review)

| Service | Platform | Sleeps on idle? | Last traffic | $/mo actual | Action (keep / sleep / delete / move) |
|---|---|---|---|---|---|
| | | | | | |

## Headroom checks (automatable)

- Static/edge host: `wrangler pages project list` / dashboard usage API.
- Containers: `railway status` / platform usage endpoint → credit remaining.
- Postgres: `select pg_database_size(current_database());` vs tier cap.
- CI minutes: `gh api /user/settings/billing/actions`.
- LLM router: `GET /api/v1/auth/key` (balance/limit fields).
- Home server: `vm_stat` / `free -g`, `df -h`, `uptime`.

A small script that writes these into the table above (and exits non-zero
on any **blocked** row) is the ideal pre-flight for an agent's deploy step.
