---
name: agent-memory-file
description: Use when setting up or maintaining a project's AI-agent memory file (CLAUDE.md, AGENTS.md, .cursorrules, or copilot-instructions). Captures the durable project context an agent needs every session — stack, structure, conventions, guardrails — in one place, kept concise and free of secrets.
---

# Purpose

Give AI agents reliable, durable project context. Without a memory file, every session re-derives the stack, conventions, and rules — inconsistently. This skill defines what belongs in an agent memory file (and what doesn't) so any compatible tool loads the same ground truth.

# When to Use

Use when starting a project that AI agents will work on, when conventions keep getting violated across sessions, or when consolidating scattered rules into one canonical file. Applies to `CLAUDE.md`, `AGENTS.md`, `.cursor/rules/*.mdc`, and `copilot-instructions.md`.

# Inputs

- The project's tech stack and runtime.
- Folder structure and where things belong.
- Coding conventions, branch policy, and test commands.
- Non-negotiable guardrails (security, branches, scope).

# Outputs

- A concise memory file an agent reads at session start, covering: project overview, stack (with "do not deviate" items), structure, conventions, workflow rules, and guardrails.

# Procedure

1. **Lead with a one-paragraph overview:** what the project is and its core constraint (e.g. local-only, no build step, regulated domain).
2. **Pin the stack** explicitly, marking anything that must not change.
3. **Map the structure:** where routes, services, components, tests, and docs live, and any single-responsibility rules.
4. **State conventions:** code style, naming, commit format, and the test/lint command.
5. **State workflow rules:** branch policy, approval gates, and the change process to follow.
6. **List guardrails** as short imperatives the agent must always honor.
7. **Keep it lean.** Memory files are read every session — prune anything stale or low-signal. Link to deeper docs rather than inlining them.
8. **Point editors at the canonical copy** if multiple tools are used, so they share one source.

# Quality Checklist

- [ ] One-paragraph project overview present
- [ ] Stack pinned, with non-negotiables marked
- [ ] Structure and "where things go" rules included
- [ ] Conventions and test command documented
- [ ] Guardrails written as short imperatives
- [ ] File is concise (signal over completeness)
- [ ] No secrets, private URLs, or org-specific confidential data

# Edge Cases

- Multiple agent tools on one machine → keep `AGENTS.md` as the canonical file and have `CLAUDE.md` / `.cursor/rules` reference it; install shared skills once in `~/.agents/skills/<name>` and symlink into each tool's skills folder rather than copying.

- **Multiple tools in use:** keep one canonical file and have others reference it to avoid drift.
- **Monorepo:** consider a root memory file plus scoped per-package notes.
- **Rules conflict:** state precedence explicitly (e.g. "security rules override all others").
- **File growing large:** split deep material into `/docs` and keep the memory file as an index.

# Safety Rules

- Never put secrets, tokens, or credentials in a memory file — it is committed.
- Never include client/employer confidential details in a public repo's memory file.
- Keep guardrails explicit; an unstated rule is an unenforced rule.

# Examples

**Good:** A 60-line `AGENTS.md` with overview, pinned stack, structure map, commit convention, "work on `dev` only", and a guardrails list ("never merge without approval", "never commit `.env`").

**Bad:** A 600-line file mixing the full API reference, changelog, and meeting notes that no agent will read in full.
