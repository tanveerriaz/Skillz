---
name: skill-hygiene-audit
description: Use when a skills library (a skills/ folder, a marketplace repo, or an agent's installed skill set) has grown past ~20 entries, when agents pick the wrong skill, when activation descriptions overlap, or on a quarterly cadence — to measure every skill for size, overlap, description quality, staleness and provenance, then produce a retire / merge / slim / keep decision list and apply it safely.
---

# Purpose

Skill libraries rot in three ways: they bloat (a 1,500-line SKILL.md loads
on every activation), they overlap (four skills for "make it look
premium"), and they drift (a tool the author stopped using two quarters
ago). Rot makes agents pick badly and burn context. This skill is the
repeatable audit that keeps a library small, sharp and trustworthy.

# When to Use

- The library has > 20 skills or > 1 skill per topic.
- An agent activated the wrong skill, or two at once, for a plain request.
- Before publishing or versioning a marketplace.
- Quarterly, as maintenance.

# Inputs

- Path to the skills folder (each `<name>/SKILL.md`), plus the index /
  marketplace file if one exists.
- Optional: usage signals (which skills were invoked recently), the
  owner's current tool stack, and the library's stated purpose.

# Outputs

- An **audit table**: one row per skill with the six measures below and a
  proposed action.
- A **decision list** grouped as Retire · Merge · Slim · Keep · Add, each
  with a one-line reason.
- Applied changes on a branch, index/marketplace updated, validator
  passing, changelog entry.

# The six measures

| Measure | How to get it | Red flag |
|---|---|---|
| **Size** | `wc -l SKILL.md`; count of reference files | SKILL.md > 300 lines with no `references/` → everything loads every time |
| **Overlap** | Cluster descriptions by topic; read the top 30 lines of each in a cluster | > 2 skills whose "Use when" would match the same request |
| **Description quality** | Does it start with the trigger situation? Name inputs and payoff? | Topic-only ("Helps with design"), persona-only ("Elite architect"), or > 80 words |
| **Staleness** | Tool/platform named; last-updated date; owner still uses it? | Tool-specific to something unused in 90 days; dated claims older than a year |
| **Provenance** | Authored vs vendored third-party; upstream still maintained? | Vendored copy with no pinned upstream version |
| **Shape** | Required sections present; procedures numbered; checklist checkable | Prose-only, no procedure, no safety rules |

# Procedure

1. **Inventory**: script the size, section-presence and description
   fields into a table (a 20-line Python or shell script; keep it in
   `scripts/`).
2. **Cluster** skills by topic (design, deployment, agent workflow, …).
   Any cluster with > 2 members is a merge candidate.
3. **Score** each skill against the six measures; write one proposed
   action per row: Retire (superseded, unused, or persona-only) · Merge
   (same job, different wrapper) · Slim (good content, wrong shape) ·
   Keep · Mark external (third-party, pin upstream).
4. **Privacy pass**: grep the whole library for emails, local paths,
   employer/client names, personal names beyond the attribution fields,
   keys and tokens. Anything found is fixed in this same pass.
5. **Propose** the decision list with the numbers (before/after count,
   lines removed, share per category). Get the owner's yes before
   deleting; confirm hard-delete vs archive.
6. **Apply on a branch**: for merges, write the new skill with
   progressive disclosure (short SKILL.md + `references/`) before removing
   the sources; for slims, move catalogues to `references/` and leave a
   "which reference for which decision" table in SKILL.md.
7. **Update** the index/marketplace, README counts, plugin manifests and
   changelog; run the validator; open the PR with the audit table in the
   description.
8. **Install locally** (canonical folder + per-tool symlinks) and remove
   the retired ones from every tool's skills directory.

# Quality Checklist

- [ ] Every skill has a row and an action; no "review later".
- [ ] No cluster of the same job has more than one surviving skill unless
      the difference is stated in both descriptions.
- [ ] No SKILL.md > 300 lines without `references/`.
- [ ] Every description starts with the trigger situation.
- [ ] Vendored skills marked external with an upstream version.
- [ ] Privacy grep clean; validator passes; changelog written.
- [ ] Before/after numbers reported (count, lines, category share).

# Edge Cases

- Owner is attached to a persona-style skill → keep the *rules* it
  contains, drop the persona; show the diff.
- Two skills overlap but target different tools (Codex vs Cursor) → merge
  and put tool differences in an edge-case line, not a second skill.
- A skill is huge because it is a data set (fonts, palettes) → keep the
  data in `data/` or `references/`, shrink SKILL.md to the query
  procedure.
- No usage signals available → weight staleness by whether the named
  tool is in the owner's current stack.

# Safety Rules

- Never hard-delete without explicit confirmation; default to a branch
  where history preserves the removed files.
- Never publish a library that fails the privacy grep.
- Do not "improve" a third-party skill's content in place; wrap or
  replace it, and keep attribution.

# Examples

**Finding:** 21 of 54 skills are frontend; seven of them total ~6,900
lines (half the library's text); four are image-generation prompt banks
that duplicate each other.
**Decision:** merge the four into one 80-line SKILL.md with four
references (4,626 → 673 lines); retire two persona-style "elite designer"
skills whose rules already live in the remaining taste skill; slim the
1,243-line taste skill to 97 lines + references. Frontend share drops to
~24%; total text down ~45%.
