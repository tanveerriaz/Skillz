---
name: git-release-hygiene
description: Use when committing, branching, or releasing in a Git project that protects its main branch. Enforces a working-branch-only policy, conventional commit messages, and an explicit-approval gate before any merge to main or production deploy. Prevents accidental merges and direct pushes to protected branches.
---

# Purpose

Provide a safe, predictable Git workflow for teams and AI agents working in repositories with a protected main/production branch. The most damaging Git mistakes are merging to main without approval and pushing directly to production. This skill makes the working branch the only place changes happen and turns merges and releases into deliberate, human-approved actions.

# When to Use

Use whenever committing code, creating branches, or preparing a release in a project that has a protected main/production branch and a separate working/integration branch. Use it especially when an AI agent is operating Git on the user's behalf.

# Inputs

- The current branch and the project's branch naming convention.
- The change being committed (to write an accurate commit message).
- An explicit user instruction when a merge or production deploy is intended.

# Outputs

- Commits on the correct working branch with conventional messages.
- A clean push to the working branch (never to main unless explicitly requested).
- Merges and deploys performed only on explicit user instruction.

# Procedure

1. **Confirm the branch.** Verify you are on the designated working branch (`develop`/`dev`/`Dev`). If not, switch to it. All work happens here.
2. **Use a branch type prefix** for focused work: `feature/*`, `fix/*`, `ui/*`, `refactor/*`, `docs/*`, `chore/*`.
3. **Write conventional commits:** `type(scope): short description`, where type is one of `feat`, `fix`, `ui`, `refactor`, `docs`, `chore`. Keep commits small and logical.
4. **Run the pre-commit checklist** (see Quality Checklist) before each commit.
5. **Push to the working branch only.** Interpret "deploy", "push", and "commit changes" as commit-and-push to the current working branch — never as a merge.
6. **Gate merges and deploys.** Only merge to main or trigger a production deploy when the user explicitly says so (e.g. "merge to main"). Otherwise, never merge branches.
7. **Hand off releasing** to the human unless explicitly asked to perform it.

# Quality Checklist

- [ ] On the correct working branch
- [ ] Commit message follows `type(scope): description`
- [ ] Code runs without errors
- [ ] No hardcoded secrets or debug statements left in
- [ ] Change is logically scoped (no unrelated edits)
- [ ] No merge or production deploy performed without explicit approval

# Edge Cases

- **User says "deploy" or "ship it":** this means commit and push to the working branch, not merge to main. Confirm if genuinely ambiguous.
- **Working branch does not exist:** create it from main, then proceed; do not commit to main.
- **Hotfix needed on production:** still seek explicit approval before touching main; document the exception.
- **Detached HEAD or wrong branch checked out:** stop and resolve branch state before committing.

# Safety Rules

- Never merge any branches unless the user explicitly requests that specific merge.
- Never push directly to the protected main/production branch.
- Never trigger an automatic production deploy on the user's behalf.
- This branch-protection rule takes precedence over convenience.

# Examples

**Good:** "You said 'push the changes.' I committed `fix(auth): handle expired session redirect` and pushed to `dev`. I did not merge to `main` — say 'merge to main' when you want that."

**Bad:** Interpreting "push the changes" as `git checkout main && git merge dev && git push`, deploying untested work to production.
