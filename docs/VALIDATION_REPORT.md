# Validation Report

Automated validation run over the Skillz marketplace.
Date: 2026-06-03 · Skills: 26 · Categories: 14

## Summary

| Check | Result |
|-------|--------|
| SKILL.md frontmatter (name + description) | ✅ 26/26 valid |
| Frontmatter name matches folder name | ✅ 26/26 match |
| Naming convention (lowercase, hyphenated, ≤64, no edge hyphens) | ✅ all pass |
| Required body sections (9 per skill) | ✅ all present |
| Duplicate skill names | ✅ none |
| marketplace.json valid JSON | ✅ valid |
| marketplace entries ↔ skill folders | ✅ 26 ↔ 26, no orphans |
| Required marketplace keys per entry | ✅ all present |
| marketplace paths resolve to real folders | ✅ all resolve |
| `public_safe: true` on every entry | ✅ all true |
| Category coverage (used vs. declared) | ✅ 14/14, no undeclared |
| Docs present | ✅ all six present |

## Frontmatter validation

All 26 `SKILL.md` files contain a valid `---` frontmatter block with a `name` and a `description` of sufficient length. Each `name` exactly matches its folder name.

## Naming validation

All names match `^[a-z0-9]+(-[a-z0-9]+)*$`, are ≤ 64 characters, and have no leading/trailing hyphens. Names are action-oriented and free of private project, employer, or client references.

## Duplicate check

No duplicate skill names across folders or marketplace entries.

## Body structure check

Every skill includes all nine required sections: Purpose, When to Use, Inputs, Outputs, Procedure, Quality Checklist, Edge Cases, Safety Rules, Examples.

## marketplace.json validation

Parses as valid JSON. Contains 26 skill entries, one per folder, with no orphan entries and no folders missing an entry. Every entry has all required keys (`name`, `description`, `path`, `category`, `source_projects`, `tags`, `compatibility`, `status`, `public_safe`, `last_updated`), `public_safe` is `true`, and every `path` resolves to an existing directory. All 14 declared categories are used; no entry uses an undeclared category.

## Link / reference check

Skill bodies reference sibling files that exist:
- `public-repo-safety-scan` → `scripts/pre-commit`, `references/gitignore-baseline.txt` ✅
- `change-log-release-notes` → `templates/daily-log.md`, `templates/release-notes.md` ✅
- `secure-env-setup` → `templates/.env.example` ✅
- `llm-eval-golden-set` → `examples/golden_set.json` ✅

## Public-safety scan

| Scan | Result |
|------|--------|
| Sensitive files (`.env`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `id_rsa`) | ✅ none (only a placeholder `.env.example`) |
| JWT tokens | ✅ none |
| Live provider keys (`sk_live_`, `sk-or-v1-`, `whsec_`) | ✅ none |
| Database URLs with real credentials | ✅ none (only `USER:PASSWORD` placeholder) |
| Internal IPs (10.x / 192.168.x / 172.16–31.x) | ✅ none |
| Real email addresses | ✅ none (only `example` placeholders) |
| Employer/client names | ✅ none |

Note: the strings that look like secret patterns inside `public-repo-safety-scan` and `secure-env-setup` are **detection patterns and placeholders** (e.g. `YOUR-API-KEY-HERE`), not real values.

## Issues found and fixes applied

1. **Renamed folders** during curation needed frontmatter sync — fixed: `git-release-hygiene` and `public-repo-safety-scan` frontmatter names updated to match folders.
2. **Real bank name in a negative example** (`public-repo-safety-scan`) — replaced with a generic `[specific bank name]` placeholder so no real organization is named anywhere, even in a "what not to do" example.

## Remaining recommendations

- Choose and add a `LICENSE` file before publishing (see Publication Checklist). MIT or Apache-2.0 are common for reusable skill libraries.
- The placeholder `.env.example` is ignored by the `.env.*` rule in `.gitignore`; force-add it (`git add -f skills/secure-env-setup/templates/.env.example`) if you want it tracked.
- Consider a lightweight CI check (run the validation script on PRs) to keep the marketplace consistent as it grows.
