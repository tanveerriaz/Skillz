# Skill Index

47 skills across 17 categories. Each skill lives in `skills/<name>/SKILL.md` and is compatible with Claude Code, Codex, Cursor, GitHub Copilot / VS Code, and Antigravity.


## ai-agent-workflows

- **agent-change-workflow** — Discovery-first workflow for changing existing code: search before writing, analyze impact in plain language, gate risky changes behind approval, then execute in small commits.
- **agent-handoff** — Produce a self-contained handoff note so the next agent or person can resume work without re-reading the codebase.
- **agent-memory-file** — Set up and maintain a project's AI-agent memory file (CLAUDE.md, AGENTS.md, .cursorrules) with durable, concise, secret-free project context.
- **llm-eval-golden-set** — Build a small golden set of inputs with expected qualities and a repeatable eval script to measure LLM-feature quality and catch regressions.
- **llm-prompt-design** — Centralize LLM prompts, separate role/tone from structure from per-call context, and apply anti-AI-slop rules for human-sounding, maintainable output.
- **local-first-ai-automation** — Build personal automations on a local LLM and browser automation with allowlisted triggers, no destructive actions, and graceful timeouts.
- **skill-hygiene-audit** — Use when a skills library has grown past ~20 entries or agents pick the wrong skill — measure size, overlap, description quality, staleness and provenance, then retire/merge/slim safely.

## coding

- **ai-code-review** — Review a change for correctness, security, performance, and maintainability with severity-tagged findings and concrete fixes.
- **think-before-coding** — Evaluate at least three distinct solution approaches with brief trade-offs before implementing, so the chosen design fits the existing codebase.

## debugging

- **bug-root-cause-analysis** — Disciplined reproduce -> isolate -> diagnose -> fix -> validate loop so the real cause is fixed and the fix is proven before closing.

## architecture

- **lean-project-structure** — Scaffold or untangle a project into a lean, single-responsibility layout with clear layer boundaries and a no-unnecessary-files rule.
- **optimize-project-infrastructure** — Select the smallest suitable architecture while making cost, availability, security, operations, and upgrade triggers explicit.

## security

- **input-validation-prompt-safety** — Validate external input before use, allowlist commands and senders, and harden LLM prompts against injection so untrusted input cannot break logic or hijack an agent.
- **public-repo-safety-scan** — Scan staged changes and the working tree for secrets, private URLs, internal IPs, personal data, and client references before a repo goes public.
- **secure-env-setup** — Environment-variable-driven config with a placeholder-only .env.example and startup validation, so no secret is ever hardcoded or committed.

## deployment

- **cost-aware-deploy-router** — Use when deciding where a workload should run across a personal platform mix — pick the cheapest platform that meets requirements, check quota and credit headroom first, record the decision.
- **railway-deployment-check** — Verify runtime files, env vars, and start command for managed-platform deploys (Railway, Render, Fly.io), favor auto-detection, and plan rollback.

## documentation

- **change-log-release-notes** — Maintain a daily change journal during development and generate user-readable release notes derived only from those logs.
- **docs-organization** — Keep all documentation in a single categorized /docs tree, prevent stray markdown and SQL files, and keep the project root minimal.
- **prd-to-build-plan** — Convert a product idea or PRD into a phased, buildable plan with goals, non-goals, scope, milestones, and acceptance criteria.
- **publish-build-journey** — Turn a verified build milestone into a privacy-checked private story draft with an explicit publication gate.

## product

- **creating-video-ads** — Turn a product source or brief into a verified short-form video advertisement and delivery-ready render.
- **hackathon-pitch-coach** — Turn a hackathon brief, time limit, and rubric into a focused problem, golden demo path, build plan, and judge-ready story.
- **pixel-recap** — Turn approved event or product photographs into a short pixel-art recap with a clear narrative arc.
- **saas-mvp-planner** — Shape a SaaS idea into a buildable MVP: one core user, one problem, the smallest valuable solution, a happy-path journey, and an explicit not-now list.

## banking-domain

- **enterprise-delivery-tracker** — Generalized, organization-agnostic structure for multi-team programme delivery: intake, prioritization, RAID, status reports, and governance updates.

## devops

- **git-release-hygiene** — Safe Git workflow: working-branch-only policy, conventional commits, and an explicit-approval gate before any merge to main or production deploy.
- **repo-readiness-review** — Run a readiness pass over a repo (safety, structure, docs, dependencies, runnability) and return a go / fix-first verdict with a prioritized punch list.

## frontend

- **dark-editorial-deck** — Build a talk or product 101 as a hash-routed, keyboard-driven 16:9 web deck with one sentence per slide, live mocks and a mono HUD; ships a starter template.
- **design-reference-imagegen** — Use when an agent should generate design-reference images (web pages, mobile screens, brand boards) before implementing UI, or turn a reference image into code — one short procedure with per-surface references.
- **design-taste-frontend** — Design distinctive landing pages, portfolios, and redesigns that avoid generic generated-interface patterns.
- **frontend-design** — Design and implement intentional web interfaces with subject-specific identity, disciplined typography, and honest interaction language.
- **industrial-brutalist-ui** — Design dense mechanical interfaces using Swiss grid discipline, tactical telemetry, and restrained analog texture.
- **plain-instruction-voice** — Write talk, onboarding and product copy in short declarative second-person sentences with explicit stopping rules and no machine jargon.
- **product-mock-illustration** — Illustrate concepts with small live HTML/CSS product mocks (chat, notifications, settings, terminal, approval dialogs) and original blob mascots instead of stock images.
- **quiet-dark-tokens** — Apply a calm near-monochrome dark design system: exact tokens, type scale, radii, shadows and rules for one accent colour on a blue-black ground.
- **redesign-without-breaking** — Use when upgrading an existing UI to premium quality without breaking JS, auth or data hooks — scan, diagnose generic patterns, protect the hooks, fix in place, verify.
- **restrained-product-motion** — Add calm motion to decks, pages and product mocks: one-time rise-in entrances, millimetre-scale idle loops, blinking mascots, reduced-motion by default.
- **stitch-design-taste** — Translate a visual direction into a semantic DESIGN.md that Google Stitch can apply consistently across screens.
- **ui-ux-pro-max** — Use a searchable design knowledge base to make evidence-backed UI decisions across products, platforms, and technology stacks. _(external — pinned upstream)_

## backend

- **api-service-pattern** — Clean backend layering: thin route handler, service layer, repository for data access, with validation, consistent errors, and dependency injection.

## data

- **resilient-batch-processing** — Process many files or records so one bad item never stops the run: isolate failures, log with identifiers, clean up temp files, and summarize results and errors.
- **supabase-data-design** — Design Postgres/Supabase-style schemas with consistent naming, row-level security by default, sensible indexes, and a clear tables-vs-JSON decision.

## founder-ops

- **founder-validation-loop** — Turn experiments into validated, reusable assets via a tight hypothesis -> cheapest test -> signal -> decide -> capture loop.

## payments

- **payments-message-decoder** — Use when reading, explaining, mapping, validating or generating ISO 20022 (pain/pacs/camt) or SWIFT MT payment messages, diagnosing rejections, or building parsers and synthetic fixtures.

## agent-safety

- **agent-approval-gates** — Use when building or reviewing an agent that acts on a user's behalf — classify actions as reversible/irreversible, gate the irreversible ones behind a human approval, write the stopping rule into the task, and test that the gate fires.

## verification

- **verification-loop** — Use when an agent's output will be relied on — separate builder from an independent verifier, write an executable spec first, replay a golden set, and gate the ship decision on evidence.
