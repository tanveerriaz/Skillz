# Publication Checklist

Run through this before pushing Skillz to the public GitHub repository.

## Safety

- [x] Secret scan completed (no live keys, tokens, or JWTs)
- [x] No `.env` files (only a placeholder-only `.env.example` template)
- [x] No credential, key, or certificate files
- [x] No private URLs
- [x] No internal IP addresses
- [x] No personal data
- [x] No financial data
- [x] No medical data
- [x] No employer/client confidential data or names
- [x] `.gitignore` covers env, keys, artifacts, logs, and OS noise

## Structure & content

- [x] 49 skills, each with a valid `SKILL.md`
- [x] All skill names follow the naming convention; no duplicates
- [x] All nine body sections present per skill
- [x] `marketplace.json` is valid JSON and matches the skill folders
- [x] README complete (what / why / who / usage / categories / contributing / philosophy)
- [x] `docs/` complete: SKILL_INDEX, SKILL_AUTHORING_GUIDE, MIGRATION_NOTES, VALIDATION_REPORT, PUBLICATION_CHECKLIST, BRAND_STYLE_GUIDE

## Pending decisions

- [ ] **License selected and `LICENSE` file added.** Recommended: MIT (maximally permissive) or Apache-2.0 (permissive + patent grant). Currently no license file — add one before relying on others to reuse the skills.

## Git

- [ ] Git repository initialized (see Phase 5 commands)
- [ ] Git remote configured to `https://github.com/tanveerriaz/Skillz.git`
- [ ] `git status` reviewed; no sensitive files staged
- [ ] **Manual push only** — do not auto-push; review the diff first

## Final gate

- [ ] Re-run `public-repo-safety-scan` immediately before the first push
- [ ] Confirm the public repo's visibility and description match the brand identity
