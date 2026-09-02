# Decision Matrix

## Project routing

| Project shape | Default | Add only when needed |
|---|---|---|
| Landing page, proposal, portfolio, deck | Vite/static on Cloudflare | R2 for large assets |
| Browser tool or calculator | Vite/static on Cloudflare | Worker for secrets/shared state |
| Small AI utility | Static UI + Cloudflare Worker | D1/KV for quotas; Railway only for Python/native work |
| Personal Next.js app | Vercel Free or Cloudflare | Supabase if durable shared state is needed |
| Commercial Next.js product | Compare Vercel Pro, Cloudflare, and Railway | Choose based on SSR compatibility and actual usage |
| Authenticated CRUD SaaS | Next.js/Vite + Supabase | R2 for media; background job when proven |
| AI/RAG/data product | Static/Next frontend + Railway FastAPI + Postgres/pgvector | Separate worker only for sustained queues |
| Scraper/report/batch | GitHub Actions or Mac Mini | Railway job for private network, long runtime, or heavy native work |
| Local/private AI | Mac Mini + Tailscale + local model/store | Cloud deployment only for remote/public users |
| Browser/mobile game | Vite/Three/Capacitor on Cloudflare | R2 assets; Supabase/Worker for multiplayer |
| WordPress/PHP/content | Existing Hostinger | Cloudflare CDN/DNS |

## Escalation ladder

Move one step at a time:

```text
static
→ static + Worker
→ full-stack serverless
→ frontend + container API
→ container API + database
→ database + asynchronous worker
```

Require evidence before each step.

## Performance tie-breakers

1. Serve cacheable assets at the edge.
2. Put compute near the database.
3. Avoid cross-cloud chatter in a request path.
4. Prefer fewer network hops over microservice purity.
5. Use the Mac Mini for Singapore/private workloads only when residential connectivity and recovery time are acceptable.
6. Benchmark a representative request before buying capacity.

## Questions that change the answer

- Does any request require a private key?
- Must the first page be indexed or server-rendered?
- Can a job wait for a schedule?
- Can users tolerate a cold start?
- Does code require Python, FFmpeg, Playwright, native libraries, or a persistent socket?
- Is shared durable data required?
- Does data contain PII, financial information, health information, or credentials?
- Is the app commercial?
- What breaks if the service is unavailable for an hour?

## Common rejected defaults

- Railway for a static Vite app.
- A Python API for a single model-provider proxy.
- Separate frontend/backend services for an early CRUD prototype.
- Redis without a measured cache/queue need.
- A vector database when Postgres/pgvector is sufficient.
- Kubernetes or a hyperscaler for speculative scale.
- Public Mac Mini port forwarding.
