---
name: public-repo-safety-scan
description: Use before making a repository public, before a first push to a public remote, or when auditing a repo for safe sharing. Scans staged changes and the working tree for secrets, credentials, private URLs, internal IPs, personal data, and employer/client references, and blocks anything unsafe. Includes an installable pre-commit hook and a strong .gitignore baseline.
---

# Purpose

Make a repository safe to share publicly. Two classes of leak matter: machine secrets (API keys, tokens, private keys, `.env` files) and human/organizational data (client names, internal URLs, IP addresses, personal data, proprietary details). This skill catches both before code reaches a public remote, and provides automation so the check runs on every commit.

# When to Use

Use before flipping a repo to public, before the first push to a public remote, when preparing an open-source release, or when auditing an existing public repo. Also use whenever generating example config, seed data, or documentation that will ship publicly.

# Inputs

- The staged diff and/or full working tree to scan.
- The project's `.gitignore`.
- Context on what counts as private for this project (employer/client names, internal hostnames, IP ranges, real user data).

# Outputs

- A pass/fail safety result over the content being shared.
- A list of findings with file and line for anything unsafe.
- An installed pre-commit hook (`scripts/pre-commit`) that blocks unsafe commits.
- A `.gitignore` aligned to `references/gitignore-baseline.txt`.
- A short remediation note for each finding (rotate, redact, generalize, or remove).

# Procedure

1. **Scan for machine secrets** in staged content and filenames:
   - Provider keys / webhook secrets: `sk-`, `sk-or-v1-`, `sk_test_`, `sk_live_`, `pk_live_`, `whsec_`
   - JWTs: `eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{10,}`
   - DB URLs with credentials: `(postgres|mysql|mongodb)://.*:.*@`
   - Key/cert files: `.pem`, `.key`, `.p12`, `.pfx`, `id_rsa`, `id_ed25519`
   - Env files: `.env`, `.env.*`
2. **Scan for private/organizational data:**
   - Internal hostnames and private URLs (non-public domains, staging hosts).
   - Internal IPs (`10.`, `192.168.`, `172.16–31.`).
   - Real personal data (names, emails, phone numbers, IDs) in fixtures or docs.
   - Employer/client names and proprietary product/architecture details.
3. **Block on any finding.** Report file and line; do not proceed until resolved.
4. **Remediate:** rotate exposed secrets, move literals to environment variables, redact or replace personal data with fakes, and generalize org-specific references (see Examples).
5. **Verify `.gitignore`** covers env/key/backup/dump patterns before the first public push.
6. **Install the hook** from `scripts/pre-commit` so the scan runs automatically on every commit.

# Quality Checklist

- [ ] No API keys, tokens, JWTs, or DB credentials in tracked content
- [ ] No `.env`, key, cert, or backup files staged
- [ ] No internal URLs or private IP addresses
- [ ] No real personal data in fixtures, seeds, or docs
- [ ] No employer/client names or proprietary details
- [ ] Example/template files use placeholders only
- [ ] `.gitignore` matches the baseline
- [ ] Pre-commit hook installed and executable

# Edge Cases

- **Publishable/anon keys** are technically public but should still be env-driven so environments stay swappable.
- **History already contains a secret:** rotation is mandatory; history rewrite (filter-repo / BFG) reduces but does not undo exposure.
- **Sample data that resembles real records:** replace with clearly synthetic values that won't match live patterns.
- **Generalizing a domain skill:** keep the reusable pattern, drop the identifying context (see Examples).

# Safety Rules

- Never push a repo public without completing this scan.
- Never commit `.env`, key, or credential files.
- Treat any exposed secret as compromised — rotate it.
- When unsure whether something is safe to share, exclude it and document why.

# Examples

See `scripts/pre-commit` and `references/gitignore-baseline.txt`.

**Good (generalize, don't leak):** Replace "Use this for [specific bank name]'s regulatory tracking" with "Use this for enterprise regulatory initiative tracking where multiple teams manage intake, prioritization, delivery status, risks, and governance reporting."

**Bad:** Pushing a public repo whose `seed.sql` contains real customer emails and a `config.py` with a live `sk_live_` key.
