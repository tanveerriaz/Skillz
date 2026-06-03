---
name: ai-code-review
description: Use to review a code change (PR, diff, or AI-generated edit) before merging. Checks correctness, security, performance, and maintainability in a fixed order, with severity-tagged findings and concrete fixes. Especially useful for reviewing code an AI agent just wrote, where confident-but-wrong output is common.
---

# Purpose

Catch defects before they merge. AI-generated code is fluent and often plausible but can be subtly wrong, insecure, or duplicative. This skill applies a consistent review pass — correctness, security, performance, maintainability — and reports findings by severity with actionable fixes rather than vague praise.

# When to Use

Use before merging any change: a pull request, a raw diff, or an edit an AI agent just produced. Use it especially after generating code, before declaring a task complete.

# Inputs

- The diff or set of changed files.
- The surrounding code and conventions (to judge consistency and duplication).
- The intended behavior the change should deliver.

# Outputs

- A review with findings grouped by severity (Blocker / Major / Minor / Nit), each with file:line, the problem, and a concrete fix.
- An explicit merge recommendation: approve, approve-with-changes, or request-changes.

# Procedure

1. **Confirm intent:** does the change actually do what was asked, including edge cases and error paths?
2. **Correctness:** logic errors, off-by-one, null/undefined handling, incorrect async/await, and untested branches.
3. **Security:** unvalidated input, injection (SQL/command/prompt), secrets in code, missing authz checks, and unsafe deserialization.
4. **Performance:** N+1 queries, unnecessary loops/allocations, missing pagination, and blocking calls on hot paths.
5. **Maintainability:** duplication of existing code, unclear naming, oversized functions, missing types, and dead/debug code left in.
6. **Consistency:** does it follow the project's conventions and reuse existing utilities rather than reinventing them?
7. **Report** each finding with severity, location, and a fix. End with a clear recommendation.

# Quality Checklist

- [ ] Change verified against intended behavior and edge cases
- [ ] Input validation and authz checked
- [ ] No secrets or debug statements introduced
- [ ] No obvious N+1 or unbounded queries
- [ ] No duplication of existing functionality
- [ ] Findings tagged by severity with concrete fixes
- [ ] Clear merge recommendation given

# Edge Cases

- **Huge diff:** review highest-risk files first (auth, payments, data access) and say what wasn't covered.
- **No tests included:** treat missing tests for non-trivial logic as a Major finding.
- **Generated boilerplate:** scan for the few lines that matter rather than nitpicking scaffolding.
- **Style-only disagreements:** mark as Nit; don't block on taste.

# Safety Rules

- Never approve a change that adds a secret, removes an authz check, or introduces injection risk.
- Never rubber-stamp ("looks good") without actually inspecting the diff.
- Distinguish blocking issues from preferences so reviews stay actionable.

# Examples

**Good:** "Blocker — `api/users.py:42`: SQL built via f-string with request input (injection). Use a parameterized query. Major — N+1 in `list_orders` (`services/orders.py:88`); prefetch with a join. Nit — rename `d` to `delta`. Recommendation: request-changes."

**Bad:** "Looks good to me, nicely written, approving."
