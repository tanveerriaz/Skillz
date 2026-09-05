# Skill Authoring Guide

How to write a Skillz skill that's focused, reusable, and public-safe.

## The one rule

Every skill helps an AI agent do **one useful thing** better, repeatedly, and safely. If a skill tries to do many things, split it. If it can't be reused outside one project, generalize it or leave it out.

## Folder structure

```
skills/<skill-name>/
  SKILL.md          # required
  references/       # optional: deeper material the agent can read on demand
  scripts/          # optional: runnable helpers (shell, python)
  templates/        # optional: files to copy and fill in
  examples/         # optional: concrete sample inputs/outputs
```

Add the optional folders only when they add real value. Don't pad a skill with empty directories.

## SKILL.md format

```markdown
---
name: <skill-name>
description: <clear activation description — when to use this skill>
---

# Purpose
# When to Use
# Inputs
# Outputs
# Procedure
# Quality Checklist
# Edge Cases
# Safety Rules
# Examples
```

- **name** — must exactly match the folder name.
- **description** — the most important field. It is how an agent decides to activate the skill. Lead with the trigger condition ("Use when..."), then what it does and the value. Be specific about the situation, not just the topic.

## Naming rules

- lowercase only
- hyphen-separated
- maximum 64 characters
- must not start or end with a hyphen
- action-oriented and easy to remember
- public-safe (no private project, employer, or client names)

**Good names:** `agent-handoff`, `repo-readiness-review`, `secure-env-setup`, `saas-mvp-planner`, `railway-deployment-check`, `bug-root-cause-analysis`, `prd-to-build-plan`, `ai-code-review`, `public-repo-safety-scan`, `git-release-hygiene`, `founder-validation-loop`.

**Bad names:** `my-employer-process`, `alex-project-helper`, `random-prompts`, `project1-skill`, `ai-stuff`, `super-agent`, `fix-everything`.

## Activation-description guidance

The description should make activation obvious. Compare:

- **Weak:** "Helps with deployment." (topic only — when does it fire?)
- **Strong:** "Use before or during deploying a small-to-medium web app to a managed platform (Railway, Render, Fly.io). Verifies runtime files, env vars, and start command, and plans rollback."

Name the situation, the inputs, and the payoff. An agent should be able to match a user's task to the description without guessing.

## Writing style

Follow `docs/BRAND_STYLE_GUIDE.md`: strategic, practical, clear, builder-focused. Plain English. No hype, no buzzword padding, no corporate fluff. Procedures are numbered, concrete steps. Checklists are checkable. Safety rules are imperatives.

## Good vs. bad skill

**Good:** `bug-root-cause-analysis` — one job (find and fix the real cause), a clear loop (reproduce → isolate → diagnose → fix → validate), checkable quality items, explicit safety rules, and a concrete good/bad example.

**Bad:** `fix-everything` — vague scope, no clear activation, not reusable, impossible to validate.

## Public-safety checklist (every skill)

- [ ] No secrets, keys, tokens, or `.env` values
- [ ] No private URLs or internal IPs
- [ ] No personal, financial, or medical data
- [ ] No employer/client names or confidential, proprietary details
- [ ] Examples and templates use generic, synthetic, placeholder content
- [ ] Any pattern drawn from a private project is generalized, not copied
- [ ] When unsure whether something is safe, it's excluded

## Before you submit

1. `SKILL.md` frontmatter has `name` (matching the folder) and a strong `description`.
2. Name follows the rules and is unique across the repo.
3. All nine body sections are present and substantive.
4. A matching entry exists in `marketplace.json`.
5. The skill is listed in `docs/SKILL_INDEX.md` under its category.
6. The safety checklist passes.
