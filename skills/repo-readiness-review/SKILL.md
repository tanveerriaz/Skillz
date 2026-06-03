---
name: repo-readiness-review
description: Use before publishing a repo, handing it off, or cutting a release. Runs a readiness pass over a repository — safety, structure, docs, dependencies, and runnability — and returns a go / fix-first verdict with a prioritized punch list, so what ships is clean and someone else can actually run it.
---

# Purpose

Decide whether a repository is ready to share, hand off, or release — and if not, exactly what to fix first. Repos accumulate stray files, missing docs, and "works on my machine" gaps. This skill is the single checkpoint that confirms a repo is safe, navigable, documented, and runnable by someone new.

# When to Use

Use before making a repo public, before handing a project to another developer or team, before a release/tag, or when auditing an inherited repo's health.

# Inputs

- The repository to review.
- The intended audience (public, internal handoff, release consumers).
- The expected way to set up and run the project.

# Outputs

- A go / fix-first verdict.
- A prioritized punch list (blockers first), each with the specific fix.
- Confirmation across five areas: safety, structure, docs, dependencies, runnability.

# Procedure

1. **Safety.** Run the public-repo-safety-scan: no secrets, `.env` files, private URLs, internal IPs, personal data, or employer/client references. Confirm `.gitignore` is strong. (Blocker if any fail.)
2. **Structure.** Lean layout, no stray build artifacts, no committed `node_modules`/`venv`/caches, docs in `/docs`, root limited to README/LICENSE/CHANGELOG.
3. **Docs.** README explains what it is, who it's for, setup, and run steps; `.env.example` documents required config; key decisions captured somewhere findable.
4. **Dependencies.** A complete, pinned manifest; lockfile present if applicable; no unused heavyweight deps.
5. **Runnability.** Clone-and-run mentally (or actually) from the README: install, configure, start. Note any undocumented step. A new person should reach a running app without insider knowledge.
6. **License.** Confirm a license decision (present or explicitly pending) for public repos.
7. **Verdict.** Give go or fix-first, with blockers listed before nice-to-haves.

# Quality Checklist

- [ ] Safety scan passed (no secrets/private data)
- [ ] `.gitignore` strong; no artifacts or vendored deps committed
- [ ] Docs in `/docs`; root limited to README/LICENSE/CHANGELOG
- [ ] README covers what/who/setup/run
- [ ] `.env.example` documents required config
- [ ] Dependency manifest complete and pinned
- [ ] A newcomer can run it from the README alone
- [ ] License decided or explicitly marked pending

# Edge Cases

- **Private internal handoff:** safety bar is lower than public, but secrets still don't belong in git — flag them.
- **Prototype not meant to ship:** scope the review to handoff-runnability; skip polish items.
- **Large monorepo:** review per-package readiness and the root orchestration.
- **No tests:** note as a risk; not necessarily a blocker for handoff, but call it out.

# Safety Rules

- Treat any secret, private URL, or personal data as a blocker for public repos.
- Never give a "go" verdict while a safety item is unresolved.
- Don't assume undocumented setup steps are obvious — if it's not in the README, it's missing.

# Examples

**Good:** "Fix-first. Blockers: (1) `config.py` has a live key — move to env + rotate; (2) `node_modules/` committed — gitignore and remove. Then: README missing run command; add `.env.example`. After these, it's a go."

**Bad:** "Looks ready, ship it" on a repo whose README is empty and whose `.env` is committed.
