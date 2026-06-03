# Migration Notes

How the Skillz marketplace was extracted from existing projects.

## Approach

Roughly 50 project folders under the builder's local `Projects` directory were scanned for **reusable, public-safe patterns** — not copied content. The goal was to capture recurring execution patterns (how work gets done well) and generalize them into tool-agnostic skills. No project-specific, private, or confidential material was carried over. Where a strong pattern lived inside a sensitive project, it was rewritten generically.

## What was scanned (high level)

The project set spanned several recurring types:

- **AI-assisted coding workflows** — agent rule files (`.cursor/rules/*.mdc`, `CLAUDE.md`, `AGENTS.md`) encoding discovery-first change processes, security rules, branch discipline, change logging, and release-note generation.
- **SaaS web apps** — server-rendered and API-backed apps with auth, payments, and managed-platform deployment, plus UI-enhancement conventions and documentation organization.
- **Local AI automations** — local-LLM + browser-automation tools with allowlist/safety constraints.
- **Document-processing tools** — batch OCR/extraction pipelines with per-item error isolation and cleanup.
- **Enterprise/programme delivery tooling** — initiative tracking, RAID, and status-report patterns, plus centralized LLM prompt design with anti-"AI slop" rules.
- **Dashboards and analytics** — data-layer and schema patterns (Postgres/Supabase-style), JSON-vs-tables decisions.
- **Founder experiments** — many prototypes that motivated the validation-loop and reusable-asset patterns.

## Reusable patterns extracted (→ skills)

| Pattern observed | Skill |
|------------------|-------|
| Discovery-first change workflow with approval gates | `agent-change-workflow` |
| Session/tool handoff continuity | `agent-handoff` |
| Durable agent memory/rule files | `agent-memory-file` |
| Centralized prompts + anti-slop output rules | `llm-prompt-design` |
| Golden-set evaluation for LLM features | `llm-eval-golden-set` |
| Local-LLM automation safety architecture | `local-first-ai-automation` |
| Three-approach pre-implementation thinking | `think-before-coding` |
| Structured pre-merge code review | `ai-code-review` |
| Reproduce → isolate → diagnose → validate | `bug-root-cause-analysis` |
| Single-responsibility lean file structure | `lean-project-structure` |
| Secret + private-data scanning before publishing | `public-repo-safety-scan` |
| Env-driven config with fail-fast validation | `secure-env-setup` |
| Input validation + prompt-injection defense | `input-validation-prompt-safety` |
| Managed-platform deploy readiness | `railway-deployment-check` |
| Repo readiness / handoff review | `repo-readiness-review` |
| Daily change journal + release notes | `change-log-release-notes` |
| Single `/docs` tree discipline | `docs-organization` |
| Idea/PRD → phased build plan | `prd-to-build-plan` |
| Idea → minimal MVP scoping | `saas-mvp-planner` |
| Experiment → validated reusable asset | `founder-validation-loop` |
| Generalized programme delivery + RAID + PSR | `enterprise-delivery-tracker` |
| Branch discipline + conventional commits | `git-release-hygiene` |
| Brand-safe, non-breaking UI changes | `safe-ui-enhancement` |
| Thin-handler / service / repository API layering | `api-service-pattern` |
| Postgres/Supabase schema + RLS design | `supabase-data-design` |
| Failure-isolated batch processing | `resilient-batch-processing` |

## What was skipped (by category)

- **Secrets & config:** `.env` files, key/cert files, credential and backup files — never read into skills.
- **Dependency & build artifacts:** `node_modules/`, `venv/`/`.venv/`, `dist/`, `build/`, `.next/`, `coverage/`, caches.
- **Logs & databases:** log folders, `*.log`, `*.sqlite`, `*.db`, data dumps.
- **Private/proprietary content:** any employer- or client-specific material, regulated-domain specifics, production system details, and internal URLs/IPs.
- **Personal data:** any real names, contact details, financial, or identity data present in sample inputs or fixtures.
- **One-off, non-reusable artifacts:** project-specific scripts and configs with no general value.

Sensitive content was excluded entirely and is not described in detail here, by design. The notes above describe only the **generalized pattern**, never the private source material.

## Assumptions

- Skills target the universal Agent Skills spec and should work across Claude Code, Codex, Cursor, GitHub Copilot/VS Code, and Antigravity.
- "Public-safe" is the default; when a pattern's safety was uncertain, it was generalized further or omitted.
- Generalized `source_projects` labels (e.g. `saas-web-app-project`, `ai-agent-project`) are used in `marketplace.json` instead of real project names.
- Quality was prioritized over quantity: 26 curated skills rather than one-skill-per-artifact.
