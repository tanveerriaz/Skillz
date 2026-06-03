---
name: agent-change-workflow
description: Use when an AI coding agent is asked to add, modify, refactor, or fix code in an existing codebase. Enforces a discovery-first workflow — search the repo before writing, analyze impact in plain language, gate risky changes behind explicit approval, then execute in small commits. Prevents duplicate implementations and silent breaking changes.
---

# Purpose

Give AI coding agents a disciplined, repeatable workflow for changing existing code. The default failure mode of agents is to jump straight to writing code, creating duplicate or parallel implementations and silently changing sensitive logic (auth, billing, schema). This skill forces search-before-code, plain-language impact analysis, and an approval gate for high-risk changes.

# When to Use

Use this whenever the agent is asked to add, modify, refactor, or fix anything in a codebase that already exists. It applies to feature work, bug fixes, and refactors alike. Do not use it for greenfield scaffolding where there is nothing to discover yet, or for pure question-answering.

# Inputs

- The user's change request (feature, fix, or refactor).
- Read access to the repository (to search code, routes, templates, config, env var names, and data models).
- Any existing change log, TODO markers, or partial implementations.
- The project's conventions (branch policy, commit style, test command) if documented.

# Outputs

- A short discovery summary: what already exists and where.
- A plain-language impact analysis: what will change, which files, and the risks.
- An explicit approval request when the change is high-risk.
- The implemented change as small, logical commits on the correct branch.
- An updated change log entry (see the change-log-release-notes skill).

# Procedure

1. **Discovery first.** Before proposing or writing code, run repo-wide searches (`rg` / `grep -R`) across routes, services, components, templates, UI strings, config keys, env var names, and data models. If the capability already exists, extend it — never create a parallel implementation.
2. **Context review.** Read the relevant existing files, the latest change log, and any TODO/NOTE markers or half-finished work.
3. **Impact analysis (plain words).** State what exists, what is missing or broken, what will change, which files will be touched, and the risks or side effects. No jargon, no assumptions.
4. **Approval gate.** Require explicit approval before proceeding if the change touches auth/permissions, database schema or row-level security, billing/payments, multiple modules at once, or if the requirements are ambiguous. For small, safe changes, explain the plan and proceed.
5. **Execute narrowly.** Work on the designated working branch only. Make small, logical commits. Do not bundle unrelated refactors.
6. **Verify.** Run the project's tests or smoke-check the affected flows before declaring the work done.
7. **Log.** Record what was searched, what was found, the plan, files changed, and test results in the change log.

# Quality Checklist

- [ ] Searched the repo before writing any code
- [ ] Confirmed no existing implementation to extend
- [ ] Impact analysis written in plain language
- [ ] Approval obtained for any high-risk change
- [ ] Changes confined to one branch and logically scoped commits
- [ ] Tests or smoke checks run and passing
- [ ] Change log updated

# Edge Cases

- **Ambiguous request:** stop and ask one clarifying question rather than guessing.
- **Discovery reveals two competing implementations already exist:** flag the duplication and propose consolidation before adding more.
- **Trivial typo or copy fix:** the full ceremony is overkill — note it briefly and proceed.
- **No tests exist:** smoke-check manually and note the testing gap as a follow-up.

# Safety Rules

- Never modify authentication, authorization, billing, or schema/RLS logic silently — always surface it and seek approval.
- Never introduce a duplicate or parallel implementation when one can be extended.
- Never commit secrets; defer to the secret-scanning-pre-commit skill.
- Never widen scope beyond the request without saying so.

# Examples

**Good:** "I searched `routes/`, `services/`, and templates for 'export'. An export service already exists in `services/export.py` handling CSV. Your request adds PDF export, so I'll extend that service rather than create a new one. Files touched: `services/export.py`, one route, one template button. No auth or billing impact — proceeding."

**Bad:** Immediately creating `services/pdf_export.py` without checking that `services/export.py` already exists, producing two parallel export paths.
