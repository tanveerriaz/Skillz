---
name: docs-organization
description: Use when creating or moving documentation in a project. Keeps all docs in a single /docs tree with categorized subfolders, prevents stray markdown and SQL files scattered across the repo, and limits the project root to README, LICENSE, and CHANGELOG.
---

# Purpose

Keep project documentation findable and the repository root clean. Left unmanaged, markdown and SQL files accumulate in the root and random subfolders, making docs impossible to navigate. This skill centralizes documentation under `/docs` with a predictable category structure and a strict root-folder policy.

# When to Use

Use whenever creating a new documentation or SQL file, moving existing docs, or auditing a repo whose docs have sprawled. Apply it before adding any `.md` file to a project root.

# Inputs

- The document being created and its purpose (deployment, setup, troubleshooting, security, migration, review, roadmap, schema, etc.).
- The existing `/docs` structure, if any.

# Outputs

- The document placed in the correct `/docs` subfolder with a clear filename.
- A clean root containing only README, LICENSE, and CHANGELOG.
- An updated `docs/README.md` index when helpful.

# Procedure

1. **Decide the category** for the document, then place it accordingly:
   - Deployment guides → `docs/deployment/`
   - Setup / configuration → `docs/setup/`
   - Bug fixes / issues → `docs/troubleshooting/`
   - Security docs → `docs/security/`
   - Migrations → `docs/migration/`
   - Code reviews / analysis → `docs/reviews/`
   - Roadmaps / plans → `docs/roadmaps/`
   - Database schemas → `docs/database/schemas/`
   - Database migrations → `docs/database/migrations/`
   - General docs → `docs/`
2. **Name the file clearly** (e.g. `docs/deployment/railway-setup.md`), lowercase with hyphens.
3. **Keep the root minimal.** Only `README.md`, `LICENSE`, and `CHANGELOG.md` belong in the project root.
4. **Don't create docs that weren't requested.** Prefer editing an existing doc over adding a new one.
5. **Maintain an index** at `docs/README.md` so the documentation is navigable.

# Quality Checklist

- [ ] Document placed in the correct `/docs` subfolder
- [ ] Filename is lowercase-hyphenated and descriptive
- [ ] Root contains only README, LICENSE, CHANGELOG
- [ ] No duplicate doc created when an existing one could be edited
- [ ] Docs index updated if structure changed

# Edge Cases

- **SQL actively used by a script** may stay alongside that script rather than under `docs/database/`.
- **Monorepo with per-package docs:** each package may have its own `docs/`, but project-wide docs go in the root `docs/`.
- **Tool expects a file in a fixed location** (e.g. `CONTRIBUTING.md`): honor the tool's convention over this policy.

# Safety Rules

- Never scatter markdown in the project root beyond the three allowed files.
- Never put real data or credentials in docs or example SQL — use placeholders.
- Do not create unrequested README/CHANGELOG files just to "be thorough".

# Examples

**Good:** A new Railway guide goes to `docs/deployment/railway-setup.md`; the root stays clean; `docs/README.md` links to it.

**Bad:** Dropping `DEPLOY.md`, `NOTES.md`, and `fix_users.sql` in the project root.
