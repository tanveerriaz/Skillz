---
name: railway-deployment-check
description: Use before or during deploying a small-to-medium web app to a managed platform (Railway, Render, Fly.io, or similar). Verifies the required runtime files, environment variables, and start command, favors the platform's auto-detection over custom build overrides, and includes a rollback plan — so deploys are predictable, not trial-and-error.
---

# Purpose

Make managed-platform deploys boring and predictable. Most deploy failures come from fighting the platform's auto-detection with custom build config, or from missing env vars and start commands. This skill confirms the few things that actually matter and keeps configuration minimal.

# When to Use

Use before a first deploy, when a deploy is failing, or when setting up CI/auto-deploy on a managed host (Railway, Render, Fly.io, and similar PaaS). Applies to typical web apps with a single web process.

# Inputs

- The app's runtime and start command.
- The list of required environment variables (from `.env.example`).
- The platform and how it deploys (e.g. GitHub-integration auto-deploy on push).

# Outputs

- Confirmed runtime/config files present and correct.
- All required env vars set in the platform's dashboard.
- A working start command via the platform's expected mechanism.
- A documented rollback path.

# Procedure

1. **Provide the runtime essentials:** a start command the platform expects (e.g. a `Procfile` with `web: <server> --host 0.0.0.0 --port $PORT`), a runtime version pin if supported, and a complete dependency manifest.
2. **Prefer auto-detection.** Let the platform detect the language and install dependencies. Avoid custom build/install overrides unless genuinely required.
3. **Keep custom build config minimal.** If a build config file is needed, use the smallest viable form; don't reimplement steps the platform already does (e.g. don't run the package manager manually before it's available).
4. **Set environment variables** in the platform dashboard/secret store — every var from `.env.example`. Never commit production secrets.
5. **Bind to the platform's port.** Use the injected `$PORT` and host `0.0.0.0`; don't hardcode a port.
6. **Use the platform's deploy trigger** (e.g. push-to-main via GitHub integration) rather than ad-hoc CLI pushes, unless the team standard is otherwise.
7. **Smoke-test after deploy:** health endpoint, a core flow, and that env-dependent features work.
8. **Document rollback:** how to redeploy the previous version and what signals trigger a rollback.

# Quality Checklist

- [ ] Start command present in the platform's expected form
- [ ] Runtime version pinned (if supported) and dependency manifest complete
- [ ] Relying on auto-detection; no unnecessary build overrides
- [ ] All required env vars set in the platform, none committed
- [ ] App binds to `$PORT` / `0.0.0.0`
- [ ] Post-deploy smoke test passes
- [ ] Rollback path documented

# Edge Cases

- **Build keeps failing:** try removing custom build config entirely and let auto-detection run before adding anything back.
- **App boots but 502s:** usually a port-binding issue — confirm `$PORT` and host binding.
- **Env-dependent feature broken in prod:** a var is missing or misnamed in the dashboard.
- **Native dependency needs a system package:** add only that, minimally, rather than rewriting the whole build.

# Safety Rules

- Never commit production secrets; set them in the platform's secret store.
- Never auto-trigger a production deploy without the team's agreed trigger.
- Never deploy untested changes straight to production.
- Always know the rollback before you deploy.

# Examples

**Good:** A web app deploys via GitHub push: `Procfile` defines the web process binding to `$PORT`, runtime pinned, deps listed, no custom build config, env vars set in the dashboard, health check green after deploy.

**Bad:** A `build` config that manually invokes the package manager before the runtime is provisioned, failing every deploy, with the real `.env` committed to make it "work".
