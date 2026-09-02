# Validation Report

Automated validation run over the Skillz marketplace.
Date: 2026-09-02 · Skills: 49 · Categories: 14

## Summary

| Check | Result |
|-------|--------|
| SKILL.md frontmatter (name + description) | ✅ 49/49 valid |
| Frontmatter name matches folder name | ✅ 49/49 match |
| Naming convention (lowercase, hyphenated, ≤64, no edge hyphens) | ✅ all pass |
| Required body sections (9 per skill) | ✅ all present |
| Duplicate skill names | ✅ none |
| marketplace.json valid JSON | ✅ valid |
| marketplace entries ↔ skill folders | ✅ 49 ↔ 49, no orphans |
| Required marketplace keys per entry | ✅ all present |
| marketplace paths resolve to real folders | ✅ all resolve |
| `public_safe: true` on every entry | ✅ all true |
| Category coverage (used vs. declared) | ✅ 14/14, no undeclared |
| Docs present | ✅ all six present |

## Frontmatter validation

All 49 `SKILL.md` files contain a valid `---` frontmatter block with a `name` and a description of sufficient length. Each `name` exactly matches its folder name.

## Naming validation

All names match `^[a-z0-9]+(-[a-z0-9]+)*$`, are ≤ 64 characters, and have no leading/trailing hyphens. Names are action-oriented and free of private project, employer, or client references.

## Duplicate check

No duplicate skill names across folders or marketplace entries.

## Body structure check

Every skill includes all nine required sections: Purpose, When to Use, Inputs, Outputs, Procedure, Quality Checklist, Edge Cases, Safety Rules, Examples.

## marketplace.json validation

Parses as valid JSON. Contains 49 skill entries, one per folder, with no orphan entries and no folders missing an entry. Every entry has all required keys (`name`, `description`, `path`, `category`, `source_projects`, `tags`, `compatibility`, `status`, `public_safe`, `last_updated`), `public_safe` is `true`, and every `path` resolves to an existing directory. All 14 declared categories are used; no entry uses an undeclared category.

## Link / reference check

All relative Markdown links in all skill folders resolve to files that exist. Installer metadata, caches, and machine-specific source records were excluded from imported skills.

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
| Gitleaks working-tree scan | ✅ zero findings |
| Absolute paths containing the local username | ✅ none |

Note: the strings that look like secret patterns inside `public-repo-safety-scan` and `secure-env-setup` are **detection patterns and placeholders** (e.g. `YOUR-API-KEY-HERE`), not real values.

## Issues found and fixes applied

1. **Personalized frontend guidance** — generalized into the portable Curiosity Fieldbook visual system and removed personal names, domains, and local file paths.
2. **Machine-specific infrastructure guidance** — excluded private subscription, domain, device, local-service, and machine-capacity references; retained a generic local-workstation policy.
3. **Personal publishing defaults** — replaced names, profiles, locations, private project trails, and personal sign-offs with explicit user-approval gates.
4. **Third-party standalone skills** — preserved or restored their MIT/Apache license files and recorded upstream project attribution in the marketplace manifest.
5. **Vendor-managed packages and duplicates** — excluded Herdr, Hyperframes, skill-discovery packages, caches, installer metadata, and duplicate aliases rather than republishing them as original work.

## Remaining recommendations

- Keep the repository validator, per-skill validator, Gitleaks scan, personal-data scan, and executable syntax checks in the release workflow.
- Recheck upstream licenses and provenance when importing future third-party skills.
