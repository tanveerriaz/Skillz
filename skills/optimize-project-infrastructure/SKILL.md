---
name: optimize-project-infrastructure
description: Plan, review, scaffold, and optimize project architecture and infrastructure with cost, speed, availability, security, and upgrade paths as explicit constraints. Use for new apps, websites, APIs, AI prototypes, agents, automations, data pipelines, games, mobile apps, deployment plans, hosting decisions, cloud comparisons, infrastructure reviews, cost audits, or migrations. Also use when creating deployment files or when a project is approaching release. Never deploy or mutate live infrastructure merely because this skill triggered.
---

# Optimize Project Infrastructure

Choose the smallest fast architecture that meets the real requirement. Reuse authorized existing capacity before adding services.

## Non-negotiable boundary

- Start in **advisory mode**.
- Inspect and recommend freely using read-only operations.
- Create local code, configuration, diagrams, and deployment manifests only when the user's build/change request authorizes that project work.
- Do not deploy, purchase, upgrade a plan, create cloud resources, expose a port, change DNS, add a public tunnel, delete a service, or migrate production data without explicit approval for the exact action.
- Before any live change, show target, expected monthly cost, availability impact, secrets/data involved, validation, and rollback.
- Treat "deploy", "ship", or equivalent explicit language as authorization only for the named project and target. Follow the active agent's normal approval rules.

## Workflow

1. Inspect the repository and existing deployment state before proposing a stack.
2. Classify the project using [references/decision-matrix.md](references/decision-matrix.md).
3. Inventory authorized existing infrastructure and subscriptions using read-only checks when that context is available.
4. Verify current prices from official provider sources when money is material. State the date, currency, assumptions, and whether tax is included.
5. Ask only questions that can change the architecture:
   - personal prototype or commercial product;
   - public, private, or household/team access;
   - expected users, geography, data volume, and traffic shape;
   - secrets, personal data, payments, or regulated information;
   - uptime and acceptable cold start;
   - realtime, background, native/Python, GPU, or long-running requirements;
   - likely scale in 3–12 months.
6. Recommend one default architecture and at most two meaningful alternatives.
7. Produce the decision record below.
8. If implementation is requested, scaffold only the selected tier. Do not provision its remote resources until explicitly approved.

When information is missing, make a reversible prototype assumption and label it. Do not introduce a paid service to avoid one minor unknown.

## Existing-stock priority

Prefer resources in this order when requirements permit:

1. Static files and browser execution.
2. Authorized local workstations for private inference, trusted batch work, development services, and temporary demos.
3. Existing static hosting or edge-function capacity.
4. Existing CI for builds and periodic batch work.
5. Existing managed auth, database, and storage when limits and failure behavior are acceptable.
6. Existing application hosting that fits the runtime and usage terms.
7. A new paid product only after documenting why the existing stock fails.

This is a priority, not a command. Availability, security, latency, platform terms, and operational burden may override it.

## Architecture rules

- Default frontend: React + TypeScript; Vite for client-only apps and Next.js only for genuine SSR/server features.
- Default styling: Tailwind with a small reusable component layer; do not install a large UI stack speculatively.
- Default validation: Zod at TypeScript boundaries and Pydantic for Python APIs.
- Keep API keys and privileged Supabase credentials out of browser bundles.
- Prefer a Worker to a container for a small stateless API/key proxy.
- Prefer one deployable service until independent scaling or native/runtime constraints justify a split.
- Prefer Postgres + pgvector when relational and vector data coexist.
- Do not add Redis, queues, search clusters, microservices, Kubernetes, or a second database without measured need.
- Use R2 for large public/generated media when egress cost matters.
- Use GitHub Actions or a scheduled job for periodic work; do not keep an HTTP service alive only to run cron.
- Never use an ephemeral container filesystem as production persistence.
- Pin runtimes, commit lockfiles, validate environment variables, add health checks to containers, and keep migrations in source control.
- Add a cost ceiling and AI request/token limits before public release.

## Required decision record

Return:

```text
Project type:
Stage and audience:
Recommended architecture:
Why this is the smallest suitable design:
Components and deployment targets:
Existing subscriptions/capacity reused:
Prototype monthly incremental cost:
Production monthly incremental cost:
Availability and latency:
Security and data controls:
What runs locally, if anything:
What is deliberately not included:
Upgrade triggers:
Deployment approval status: NOT REQUESTED | REQUESTED
```

Include a compact component diagram when three or more runtime components interact.

## Cost discipline

- Separate **sunk subscription cost** from **incremental project cost**.
- Show SGD and source currency when practical.
- Model idle cost, usage cost, storage, egress, database, AI tokens, domains, backups, and monitoring.
- Do not call a free tier "$0 forever"; list its limiting dimension and failure behavior.
- Prefer an account-level shared paid tier over one paid service per prototype.
- Include a scale trigger such as users, requests, storage, latency, job duration, or revenue.
- For an existing deployment, use actual 30–90 day utilization before estimating savings when that data is accessible.

## Local workstation policy

Use an authorized local workstation for workloads that benefit from local compute and do not require public-cloud availability, such as private inference, trusted batch work, development services, temporary demos, build caches, and artifact preparation.

- Treat local models and services as development dependencies unless the deployment target explicitly provides them.
- Do not make a personal workstation the default public production origin.
- Never recommend router port forwarding or a public tunnel by default.
- Persist approved production assets in the project's normal asset store or repository.
- Record model versions, prompts, seeds when available, source assets, rights, and output locations when reproducibility matters.
- Require explicit approval and authenticated private access before making a local service remotely reachable.

## Scaffolding phases

**Phase 1 — plan:** architecture record, cost range, risks, and upgrade path.

**Phase 2 — local scaffold:** repository layout, application code, Dockerfile only if needed, `.env.example`, CI, tests, and inactive deployment config.

**Phase 3 — preview:** after explicit approval, create the minimum remote resources and a non-production deployment with limits.

**Phase 4 — production:** after explicit approval, configure domain/DNS, backups, monitoring, budgets, smoke tests, and rollback.

Never skip directly from idea to Phase 4.

## Existing deployment reviews

For utilization reviews:

1. List live projects and services read-only.
2. Join each service to its repository, runtime, traffic role, and database.
3. Flag static apps on paid containers, duplicates, idle services, stale previews, oversized databases, unnecessary caches, and direct-to-browser AI keys.
4. Rank actions by monthly savings, effort, risk, and reversibility.
5. Make no cleanup change until the user approves the exact service.

## Cross-cloud requests

Support AWS, Azure, GCP, Fly, Render, or other platforms when required. Compare them against existing stock on:

- incremental monthly cost;
- latency for the expected users;
- cold starts and availability;
- operational work;
- lock-in and migration cost;
- compatibility with the runtime.

Do not introduce a hyperscaler merely for theoretical scale.
# Purpose

Select the smallest suitable architecture while making cost, availability, security, operations, and upgrade triggers explicit.

# When to Use

Use for new systems, infrastructure reviews, hosting decisions, deployment plans, cost audits, or migrations.

# Inputs

Repository state, audience, traffic shape, data sensitivity, runtime needs, availability target, budget, and authorized existing capacity.

# Outputs

A decision record, compact component diagram when useful, cost range, security controls, and upgrade path.

# Procedure

Follow the advisory boundary, decision matrix, existing-stock priority, architecture rules, and phased implementation workflow above.

# Quality Checklist

- [ ] The recommendation is the smallest design that meets stated requirements.
- [ ] Costs, limits, failure behavior, and upgrade triggers are dated and explicit.
- [ ] Live changes remain separately authorized and reversible.

# Edge Cases

When requirements are missing, make a reversible prototype assumption and label it rather than adding speculative infrastructure.

# Safety Rules

Never expose local services, provision paid resources, change DNS, migrate production data, or deploy without authorization for the exact action.

# Examples

**Good:** A static-first design with one edge function and a documented scale trigger. **Bad:** Kubernetes, multiple databases, and paid queues for an unvalidated prototype.
