---
name: cost-aware-deploy-router
description: Use when deciding where to run or deploy a workload for a solo builder or small team — a static site, an API, a scheduled job, a long-running agent, a database, or a local-model task — across a personal platform mix (e.g. Vercel, Cloudflare, Railway, Supabase, a home server, a cloud free tier). Picks the cheapest platform that meets the workload's real requirements, checks quota and credit headroom before routing, and records the decision so agents stop defaulting to the same paid platform.
---

# Purpose

Small teams accumulate platforms the way kitchens accumulate gadgets, and
agents deploy to whichever one they saw last. The result is paying for
compute that a free tier or an idle home machine would have handled. This
skill makes the routing decision explicit, cost-first and repeatable, and
refuses to route to a platform that is out of quota.

# When to Use

- "Where should this run?" for any new service, job, site or model task.
- Before an agent runs `deploy`, `railway up`, `vercel --prod`, or starts
  a local inference job.
- Monthly, to review what is running where and what it costs.
- When a bill or a quota warning arrives.

Not for enterprise landing-zone decisions with compliance-driven placement;
this is a builder-stack skill.

# Inputs

- **Workload profile**: type (static / serverless API / always-on service /
  cron job / queue worker / database / local model inference), expected
  traffic or run frequency, latency needs, state (stateless / needs disk /
  needs Postgres), secrets, public or private.
- **Platform inventory** with current tier and headroom (see the
  `references/platform-inventory.template.md`): remaining free-tier units,
  credit balance, CI minutes, machine RAM/disk if a home server is in the
  mix.
- Hard constraints: data-residency, uptime target, "must not touch
  employer infrastructure", budget cap per month.

# Outputs

- A **routing decision** in one table row: workload → platform → tier →
  estimated monthly cost → why → fallback.
- Pre-flight result: headroom OK / blocked (with the blocking quota).
- An entry in the project's `DEPLOY.md` (or agent memory file) so future
  agents reuse the decision.

# Decision order

Route to the first row whose requirements the workload meets:

| # | Workload shape | First choice | Because | Fallback |
|---|---|---|---|---|
| 1 | Static site, SPA, docs | Edge/static host free tier (Cloudflare Pages, Vercel Hobby) | $0, global CDN, zero ops | GitHub Pages |
| 2 | Serverless API, webhooks, < ~100k req/mo | Edge functions / serverless free tier | $0–5, scales to zero | Managed container sleeping on idle |
| 3 | Scheduled job (minutes/day) | Platform cron on free tier, or GitHub Actions schedule if < CI minute cap | $0 | Home server cron |
| 4 | Always-on service, low traffic, personal | Home server (if 24/7 and reachable via tunnel) | sunk cost, no per-service fee | Managed container with sleep-on-idle |
| 5 | Always-on service, public, needs uptime | Managed container platform (Railway/Fly/Render) | predictable $5–15 | Cloud VM small tier |
| 6 | Postgres / auth / storage | Managed Postgres free tier (Supabase) | $0 until real usage | SQLite on the service for single-tenant |
| 7 | Local model inference, batch or private | Home server GPU/NPU (if RAM headroom) | $0 marginal, private | Pay-per-token API via router (OpenRouter) |
| 8 | Interactive LLM at scale | Pay-per-token API | no idle cost | — |

Tie-breakers: fewer platforms in play beats marginal savings; a platform
you already monitor beats a new one; anything with customer data prefers
the platform with the clearest data-location story.

# Procedure

1. **Profile the workload** in one line: type · traffic · state · secrets ·
   public? · uptime need · budget.
2. **Refresh the inventory**: for each candidate platform read current
   usage against its free-tier or credit limits (CLI, dashboard, or the
   monitor described in `references/headroom-checks.md`). Mark any at
   > 80% as **blocked** for new workloads this cycle.
3. **Walk the decision table** top-down; take the first unblocked match.
4. **Estimate cost** for 30 days at 1× and 5× expected load. If 5× crosses
   a paid boundary, note the trigger and the fallback.
5. **Check sleep behaviour**: for anything not needing < 1s cold start,
   enable scale-to-zero / sleep-on-idle so many side projects cost nothing
   while idle.
6. **Record** the decision (table row + date + headroom snapshot) in
   `DEPLOY.md`; add the deploy command and the rollback command.
7. **Deploy** via the platform's CLI; verify health; confirm the
   inventory delta matches the estimate.
8. **Monthly review**: list running services, actual spend per platform,
   idle services to sleep or delete, and platforms to consolidate.

# Quality Checklist

- [ ] Workload profiled before any platform is named.
- [ ] Headroom checked; no routing to a platform > 80% of quota.
- [ ] Decision row recorded with date, cost estimate, fallback.
- [ ] Sleep-on-idle enabled where latency allows.
- [ ] Cost estimate covers 1× and 5× load with the paid-boundary trigger.
- [ ] No employer/client workload routed to personal infrastructure, and
      vice versa.
- [ ] Secrets set via the platform's env store, never in the repo.

# Edge Cases

- Home server is the cheapest but the workload is public-facing → still
  prefer a managed platform unless a tunnel with auth and uptime alerting
  is already in place.
- Free tier changes (they do) → re-run the inventory step; do not trust a
  months-old `DEPLOY.md` row.
- Many tiny idea projects → one managed platform with sleep-on-idle beats
  spreading them; consolidate rather than optimise each.
- Model inference needs more RAM than the home machine has headroom for
  → route to pay-per-token, log it, do not swap-thrash the home machine.

# Safety Rules

- Never deploy anything containing employer, client or regulated data to
  personal infrastructure, regardless of cost.
- Never store platform tokens in the repo or in `DEPLOY.md`.
- Do not delete or downgrade a running service to save cost without the
  owner's confirmation; sleep it and flag it.

# Examples

**Ask:** "Deploy this FastAPI webhook receiver."
**Decision row:** `webhook-receiver · Cloudflare Workers (or Vercel
Functions) · free · ~$0 · stateless, bursty, < 50k req/mo · fallback:
Railway with sleep-on-idle (~$5)`. Pre-flight: Cloudflare 12% of daily
request quota → OK.

**Ask:** "Run nightly QLoRA eval on 300 prompts."
**Decision row:** `nightly-eval · home server · n/a · $0 marginal · needs
14 GB RAM, 20 GB free of 64 → OK · fallback: OpenRouter at ~$0.40/run`.
