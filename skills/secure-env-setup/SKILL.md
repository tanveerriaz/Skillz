---
name: secure-env-setup
description: Use when setting up configuration and secrets for a project. Establishes environment-variable-driven config, a committed .env.example with placeholders, startup validation that fails fast on missing vars, and a clean separation between local, example, and production configuration — so no secret is ever hardcoded or committed.
---

# Purpose

Manage configuration safely. Hardcoded credentials and committed `.env` files are the root of most secret leaks. This skill makes every secret environment-driven, documents required vars via a placeholder-only `.env.example`, and validates configuration at startup so misconfiguration fails loudly instead of leaking or silently breaking.

# When to Use

Use when starting a project, when adding any new credential or external service, when preparing a repo for public sharing, or when onboarding someone who needs to know what config is required.

# Inputs

- The set of configuration values the app needs (keys, URLs, toggles).
- Which values are secret vs. safe-to-expose.
- The deployment target's way of setting env vars.

# Outputs

- All secrets read from environment variables — no literals in code.
- A committed `.env.example` with placeholders and no real values.
- A `.env` (gitignored) for local development.
- Startup validation that fails fast on missing required vars.

# Procedure

1. **Read every secret from the environment** (`os.getenv` / `process.env`); never inline a literal credential.
2. **Create `.env.example`** listing every required variable with a placeholder value (`SUPABASE_ANON_KEY=YOUR-ANON-KEY-HERE`). Commit this file.
3. **Keep `.env` local and gitignored.** Confirm `.env` and `.env.*` are in `.gitignore` before the first commit.
4. **Validate at startup.** Check all required vars are present; raise a clear error listing any that are missing, and exit rather than running half-configured.
5. **Validate format where cheap** (e.g. a Stripe secret should start with `sk_`) to catch wrong values early.
6. **Separate environments.** Set production values in the host's dashboard/secret store, never in the repo.
7. **Never log or echo secrets,** including in errors. On rotation, update local `.env` and the host's store, then revoke the old value.

# Quality Checklist

- [ ] No credential literals anywhere in code
- [ ] `.env.example` committed with placeholders only
- [ ] `.env` and `.env.*` gitignored
- [ ] Startup validation lists missing required vars and fails fast
- [ ] Format checks on critical keys
- [ ] Production secrets live in the host's secret store, not the repo
- [ ] Secrets never logged or printed

# Edge Cases

- **Publishable/anon keys:** safe to expose but still load from env so environments stay swappable.
- **Optional features:** make their vars optional and degrade gracefully when absent, rather than crashing.
- **Local vs. CI:** provide a CI secret store; never commit CI credentials.
- **Rotating a key:** update all environments, then revoke the old key; treat the old value as compromised.

# Safety Rules

- Never commit `.env` or any file with real secrets.
- Never put real values in `.env.example` — placeholders only.
- Never log, print, or include secrets in error messages.
- Fail fast on missing required configuration; don't run partially configured.

# Examples

See `templates/.env.example` for a placeholder-only template.

**Good:** `config.py` reads all keys via `os.getenv`, `validate_environment()` raises "Missing required env vars: ['STRIPE_SECRET_KEY']" on boot, `.env.example` documents every var with placeholders, and `.env` is gitignored.

**Bad:** `API_KEY = "sk-or-v1-realkey"` in `config.py`, with the real `.env` committed "by accident".
