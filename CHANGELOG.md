# Changelog

All notable changes to Skillz are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project aims to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- _Add new skills and changes here before the next release._

## [0.4.0] - 2026-09-05

Library audit: 54 → 47 skills, frontend share 39% → ~26%, roughly 45% less skill text, three new categories.

### Added

- **payments-message-decoder** — ISO 20022 / SWIFT MT decoding, validation, MT↔MX mapping, rejection diagnosis, synthetic fixtures. First skill in the new `payments` category.
- **agent-approval-gates** — reversible/irreversible action classification, human approval gates enforced in prompt + config + code, five-part task brief, gate tests. New `agent-safety` category.
- **verification-loop** — independent builder/verifier separation, executable spec first, golden-set replay, evidence-based gate. New `verification` category.
- **cost-aware-deploy-router** — cheapest-correct platform routing with quota/credit headroom pre-flight and a platform inventory template.
- **skill-hygiene-audit** — the repeatable audit that produced this release (six measures, retire/merge/slim/keep).

### Changed

- **design-reference-imagegen** replaces `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit` and `image-to-code` (4,626 → 673 lines; short SKILL.md + per-surface references).
- **redesign-without-breaking** replaces `redesign-existing-projects` + `safe-ui-enhancement`.
- **design-taste-frontend** slimmed from 1,243 lines to 97 + eight reference files; persona language and dead block-library schema removed.
- **stitch-design-taste** slimmed to 73 lines + a DESIGN.md template reference.
- **dark-editorial-deck** gains `references/scroll-page-variant.md` (absorbs `cinematic-minimal-web`).
- **quiet-dark-tokens** gains `references/light-variant.css` (absorbs `minimalist-ui`'s warm palette).
- **agent-memory-file** documents the `AGENTS.md` + `~/.agents/skills` cross-tool convention.
- **ui-ux-pro-max** marked `status: external` with pinned upstream.

### Removed

- `design-taste-frontend-v1` (legacy), `full-output-enforcement` (obsolete anti-truncation prompt), `gpt-taste` and `high-end-visual-design` (persona prompts duplicating design-taste-frontend), `minimalist-ui` and `cinematic-minimal-web` (folded in), `scroll-world` (vendored; link upstream instead), `scrapecreators-api` (unused), plus the four imagegen sources and two redesign sources listed above.

## [0.3.0] - 2026-09-05

### Added

- **Quiet-dark design family (5 skills):** `dark-editorial-deck`, `quiet-dark-tokens`, `product-mock-illustration`, `restrained-product-motion`, `plain-instruction-voice` — a reverse-engineered, generalised design system for calm dark editorial decks and product explainers: exact tokens and type scale, motion grammar with fixed durations/easings, live HTML mock components with original mascots, a plain second-person writing voice, and a working `deck-starter.html` template (hash routing, keyboard nav, section keys, notes, HUD).

## [0.1.0] - 2026-06-03

Initial public release.

### Added

- **26 reusable Agent Skills** across 14 categories (ai-agent-workflows, coding, debugging, architecture, security, deployment, documentation, product, banking-domain, devops, frontend, backend, data, founder-ops), each following the [agentskills.io](https://agentskills.io/specification) `SKILL.md` format with Purpose, When to Use, Inputs, Outputs, Procedure, Quality Checklist, Edge Cases, Safety Rules, and Examples.
- **Skill helpers** where useful: a pre-commit secret-scan hook and `.gitignore` baseline (`public-repo-safety-scan`), daily-log and release-notes templates (`change-log-release-notes`), a placeholder `.env.example` (`secure-env-setup`), and a starter golden set (`llm-eval-golden-set`).
- **`marketplace.json`** — human- and agent-readable index with per-skill metadata.
- **Documentation:** `README.md`, plus `docs/` covering `SKILL_INDEX`, `SKILL_AUTHORING_GUIDE`, `MIGRATION_NOTES`, `VALIDATION_REPORT`, `PUBLICATION_CHECKLIST`, and `BRAND_STYLE_GUIDE`.
- **Branding:** slate + amber identity with `assets/skillz-banner.svg/.png`, `skillz-logo.svg`, and a 1280×640 `skillz-social-preview.png`.
- **Installable plugin marketplace:** `.claude-plugin/marketplace.json` and `plugin.json` so the library installs via `/plugin marketplace add tanveerriaz/Skillz`.
- **Quality gate:** `scripts/validate.py` and a GitHub Actions workflow running frontmatter, naming, JSON, path-resolution, and secret/private-data checks on every push and PR.
- **MIT License.**

### Security

- All content is public-safe: no secrets, private URLs, internal IPs, personal data, or employer/client references. Patterns drawn from private projects were generalized, not copied.

[Unreleased]: https://github.com/tanveerriaz/Skillz/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/tanveerriaz/Skillz/releases/tag/v0.1.0
