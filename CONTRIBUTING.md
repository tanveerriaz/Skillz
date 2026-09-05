# Contributing to Skillz

Thanks for helping build a practical, public-safe library of AI-agent skills. Contributions are welcome — new skills, improvements to existing ones, fixes, and docs.

The bar is simple: every skill helps an AI agent do **one useful thing** better, repeatedly, and safely. Quality over quantity.

## Before you start

Read these two short docs — they define the format and the voice:

- [`docs/SKILL_AUTHORING_GUIDE.md`](docs/SKILL_AUTHORING_GUIDE.md) — structure, naming, activation descriptions, good/bad examples.
- [`docs/BRAND_STYLE_GUIDE.md`](docs/BRAND_STYLE_GUIDE.md) — voice (strategic, practical, clear, builder-first) and colors.

## Adding a new skill

1. Create `skills/<skill-name>/SKILL.md` with valid frontmatter (`name` matching the folder, a strong `description`) and all nine body sections: Purpose, When to Use, Inputs, Outputs, Procedure, Quality Checklist, Edge Cases, Safety Rules, Examples.
2. Follow the naming rules: lowercase, hyphen-separated, action-oriented, ≤ 64 chars, no leading/trailing hyphen, no private/project/client names.
3. Add `references/`, `scripts/`, `templates/`, or `examples/` only when they add real value — don't pad with empty folders.
4. Add a matching entry to `marketplace.json` (all required keys, `public_safe: true`, a generalized `source_projects` label).
5. List the skill in `docs/SKILL_INDEX.md` under its category.
6. Run validation locally (see below) and add a line to `CHANGELOG.md` under `Unreleased`.

## Improving an existing skill

Keep changes focused. If you tighten a procedure or fix an edge case, update the Quality Checklist or Examples to match, and note it in the changelog.

## Public-safety rules (non-negotiable)

This repo is public. Never include:

- secrets, API keys, tokens, passwords, or `.env` values
- private URLs, internal IPs, or production system details
- personal, financial, or medical data
- employer/client names or confidential, proprietary content

If a useful pattern comes from a private project, **generalize it** — never copy it directly. When unsure whether something is safe to share, leave it out.

## Validate before opening a PR

```bash
python3 scripts/validate.py
```

This checks frontmatter, naming, duplicates, `marketplace.json` structure and path resolution, and runs a secret / private-data scan. CI runs the same check on every PR — it must pass.

## Pull request checklist

- [ ] `python3 scripts/validate.py` passes locally
- [ ] Skill follows the authoring guide and brand voice
- [ ] `marketplace.json` and `docs/SKILL_INDEX.md` updated
- [ ] `CHANGELOG.md` updated under `Unreleased`
- [ ] No secrets, private data, or org-specific references
- [ ] PR description explains what the skill does and why it's reusable

## Commit style

Use conventional commits where you can: `feat(skill): add <name>`, `fix(<skill>): ...`, `docs: ...`, `chore: ...`.

## License

By contributing, you agree your contributions are licensed under the repository's [MIT License](LICENSE).
