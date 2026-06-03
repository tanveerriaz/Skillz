---
name: agent-handoff
description: Use when ending an AI-agent work session, switching tools (e.g. Cursor to Claude Code), or handing work to a teammate. Produces a self-contained handoff note so the next agent or person can resume without re-reading the whole codebase — covering goal, state, decisions, open threads, and exact next steps.
---

# Purpose

Make AI-agent work resumable. Context is lost between sessions, tools, and people, which causes rework and contradictory changes. This skill captures just enough state — goal, what changed, why, what's left — so the next agent or human can pick up cleanly.

# When to Use

Use at the end of a work session, before switching between AI tools, when pausing a long task, or when transferring ownership to someone else. Also use when a task is blocked and needs a different agent or person to continue.

# Inputs

- The original objective and current status.
- Files changed this session and the reasoning behind key decisions.
- Open questions, blockers, and known risks.
- The project's branch/commit state.

# Outputs

- A single handoff note (markdown) the next worker can act on without prior context, structured as: Goal, Current State, Key Decisions, Files Touched, Open Threads, Next Steps, How to Verify.

# Procedure

1. **State the goal** in one or two sentences — what "done" looks like.
2. **Describe current state:** what works, what's partial, what's untested. Include the branch and last commit.
3. **Record key decisions** and the reasoning, so the next worker doesn't relitigate or reverse them blindly.
4. **List files touched** with a one-line purpose each.
5. **Capture open threads:** unanswered questions, blockers, and risks.
6. **Write exact next steps** as an ordered, actionable list — not vague intentions.
7. **Add a verification path:** the command to run or the flow to click to confirm things still work.

# Quality Checklist

- [ ] Goal stated in plain language
- [ ] Current state distinguishes done / partial / untested
- [ ] Branch and last commit noted
- [ ] Key decisions captured with reasoning
- [ ] Next steps are concrete and ordered
- [ ] A verification command or flow is included
- [ ] No secrets or private data in the note

# Edge Cases

- **Mid-refactor handoff:** explicitly flag files in an inconsistent state so the next worker doesn't ship them.
- **Blocked on an external dependency:** name the dependency and what's needed to unblock.
- **Handoff to a different tool:** note any tool-specific context (e.g. memory files, rules) the new tool should load.
- **Very short session:** a compact 5-line note is fine — match effort to the work done.

# Safety Rules

- Never include secrets, tokens, or private data in a handoff note.
- Never claim work is verified if it wasn't — say "untested".
- Never bury blockers; surface them at the top.

# Examples

**Good:** "Goal: add CSV export to reports. State: export works for the summary table on `dev` (commit a1b2c3); detail-table export is stubbed and untested. Decision: reused `services/export.py` rather than a new module. Next: 1) implement `export_detail()`, 2) wire the button in `reports.html`, 3) run `pytest tests/test_export.py`. Verify: open /reports, click Export, expect a 2-sheet file."

**Bad:** "Did some work on exports, mostly done, continue where I left off."
