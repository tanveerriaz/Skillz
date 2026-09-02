# Skill Index

49 skills across 14 categories. Each skill lives in `skills/<name>/SKILL.md` and is compatible with Claude Code, Codex, Cursor, GitHub Copilot / VS Code, and Antigravity.

## ai-agent-workflows

- **agent-change-workflow** — Search the repo before writing code, analyze impact in plain language, gate risky changes behind approval, then execute in small commits. _Use when an agent modifies an existing codebase._
- **agent-handoff** — Write a self-contained handoff note so the next agent or person can resume without re-reading the code. _Use at the end of a session or when switching tools._
- **agent-memory-file** — Author and maintain CLAUDE.md / AGENTS.md / .cursorrules with durable, concise project context. _Use to give agents consistent ground truth._
- **llm-prompt-design** — Centralize prompts, separate role/tone/structure/context, and apply anti-AI-slop rules. _Use when building LLM features that must sound human and stay maintainable._
- **llm-eval-golden-set** — Build a golden set + eval runner to catch LLM-feature regressions. _Use before changing a prompt or model._
- **local-first-ai-automation** — Safe architecture for local-LLM + browser automations with allowlists and no destructive actions. _Use for personal automations with no cloud SaaS._
- **full-output-enforcement** — Deliver exhaustive requested outputs without silent omissions or placeholder shortcuts. _Use when completeness is part of correctness._

## coding

- **think-before-coding** — Evaluate at least three approaches with trade-offs before implementing. _Use before any non-trivial change._
- **ai-code-review** — Review a diff for correctness, security, performance, and maintainability with severity-tagged fixes. _Use before merging, especially AI-generated code._

## debugging

- **bug-root-cause-analysis** — Reproduce → isolate → diagnose → fix → validate, fixing the cause not the symptom. _Use for any bug or "works here but not there" issue._

## architecture

- **lean-project-structure** — Single-responsibility files, clear layer boundaries, size limits, no file sprawl. _Use when scaffolding or untangling a project._
- **optimize-project-infrastructure** — Select the smallest suitable architecture with explicit cost, availability, security, and upgrade triggers. _Use for infrastructure plans, reviews, cost audits, and migrations._

## security

- **public-repo-safety-scan** — Scan for secrets, private URLs, internal IPs, personal data, and client references before going public. _Use before publishing or auditing a repo._
- **secure-env-setup** — Env-driven config, placeholder-only `.env.example`, fail-fast startup validation. _Use when setting up config and secrets._
- **input-validation-prompt-safety** — Validate input, allowlist, and harden prompts against injection. _Use when accepting external input or building LLM prompts._

## deployment

- **railway-deployment-check** — Verify runtime files, env vars, and start command for managed platforms; favor auto-detection; plan rollback. _Use before/while deploying to Railway, Render, or Fly.io._

## documentation

- **change-log-release-notes** — Daily change journal + release notes derived only from the logs. _Use throughout dev and at release time._
- **docs-organization** — Keep docs in one categorized `/docs` tree; keep the root minimal. _Use when creating or moving docs._
- **prd-to-build-plan** — Turn an idea or PRD into a phased plan with scope, milestones, and acceptance criteria. _Use before building a sizeable feature._
- **publish-build-journey** — Turn verified build milestones into privacy-checked private story drafts with an explicit publication gate. _Use after meaningful builds, experiments, deployments, or corrections._

## product

- **saas-mvp-planner** — One core user, one problem, smallest valuable solution, explicit not-now list. _Use when shaping a SaaS idea into an MVP._
- **hackathon-pitch-coach** — Narrow a hackathon brief into a problem, golden demo path, build plan, and judge-ready story. _Use when choosing what to build or preparing the pitch._
- **creating-video-ads** — Turn product truth into a verified short-form advertisement and delivery-ready render. _Use for Reels, TikToks, Shorts, demos, and launch cuts._
- **pixel-recap** — Turn approved event or product photographs into a short pixel-art story. _Use for retro recap videos and animated social assets._

## banking-domain

- **enterprise-delivery-tracker** — Generalized multi-team programme delivery: intake, prioritization, RAID, status, governance. Organization-agnostic and public-safe. _Use for enterprise/regulated delivery tracking._

## devops

- **git-release-hygiene** — Working-branch-only policy, conventional commits, approval gate before merge/deploy. _Use when committing, branching, or releasing._
- **repo-readiness-review** — Readiness pass over safety, structure, docs, dependencies, and runnability with a go / fix-first verdict. _Use before publishing, handoff, or release._

## frontend

- **safe-ui-enhancement** — Restyle UI without breaking JS/auth hooks; read the brand reference; verify responsive + accessibility. _Use when improving an existing interface._
- **brandkit** — Create coherent premium brand boards, logo systems, identity decks, and visual-world presentations. _Use for image-led brand-system work._
- **cinematic-minimal-web** — Build restrained presentation-style websites with editorial typography and purposeful motion. _Use for premium landing pages and portfolios._
- **design-taste-frontend** — Design distinctive landing pages, portfolios, and redesigns without generic generated-interface patterns. _Use for subject-specific frontend direction._
- **design-taste-frontend-v1** — Preserve the original high-agency design behavior for exact backward compatibility. _Use only when v1 behavior is required._
- **frontend-design** — Design intentional interfaces with subject-specific identity and an optional Curiosity Fieldbook visual system. _Use for web art direction and implementation._
- **gpt-taste** — Create expressive, high-variance marketing interfaces with advanced GSAP motion. _Use for explicitly experimental visual briefs._
- **high-end-visual-design** — Improve interface craft through precise typography, spacing, depth, composition, and motion. _Use for premium visual polish._
- **image-to-code** — Generate and inspect visual references, then implement a faithful responsive website. _Use for image-first web builds._
- **imagegen-frontend-mobile** — Generate consistent premium mobile screen concepts and flows. _Use for image-only iOS, Android, or cross-platform concepts._
- **imagegen-frontend-web** — Generate one implementation-friendly horizontal image for every website section. _Use for section-level web design references._
- **industrial-brutalist-ui** — Design dense Swiss-grid and tactical-telemetry interfaces with restrained analog texture. _Use for deliberate industrial-brutalist products._
- **minimalist-ui** — Create calm editorial interfaces through flat structure, warm monochrome color, and disciplined spacing. _Use for quiet document-style products._
- **redesign-existing-projects** — Upgrade visual quality without breaking behavior, data, or integration contracts. _Use for safe redesigns of existing sites and apps._
- **scroll-world** — Build scroll-scrubbed landing pages that move through connected generated scenes. _Use for approved immersive narrative sites._
- **stitch-design-taste** — Translate a visual direction into a semantic DESIGN.md for Google Stitch. _Use for consistent Stitch screen generation._
- **ui-ux-pro-max** — Query a local design knowledge base for product-, stack-, and platform-specific UI guidance. _Use for design, implementation, and UX review decisions._

## backend

- **api-service-pattern** — Thin handler / service / repository layering with validation, consistent errors, and DI. _Use when building or refactoring endpoints._

## data

- **supabase-data-design** — Consistent naming, RLS by default, sensible indexes, tables-vs-JSON guidance. _Use when designing a Postgres/Supabase schema._
- **resilient-batch-processing** — Process many files/records so one bad item never stops the run; isolate, log, clean up, summarize. _Use for OCR, imports, and bulk transforms._
- **scrapecreators-api** — Retrieve permitted public social-media data through documented API endpoints. _Use for scoped profile, post, video, transcript, ad, trend, and engagement research._

## founder-ops

- **founder-validation-loop** — Hypothesis → cheapest test → signal → decide → capture, turning experiments into reusable assets. _Use when running experiments or extracting reusable wins._

## Compatibility notes

All skills use the universal `SKILL.md` format and are tool-agnostic. Skills that ship a `scripts/` helper (e.g. `public-repo-safety-scan`) assume a POSIX shell with Git. Skills that ship `templates/` or `examples/` (change-log, secure-env-setup, llm-eval-golden-set) are starting points to copy and adapt.
