---
name: lean-project-structure
description: Use when scaffolding a new project or untangling a messy one. Establishes a lean, single-responsibility file layout with clear layer boundaries (routes vs. business logic vs. data vs. presentation), file/function size limits, and a "no unnecessary files" rule so the codebase stays navigable as it grows.
---

# Purpose

Keep codebases navigable and maintainable by giving each file one job and each layer a clear boundary. Projects rot when routes hold business logic, files sprawl, and helpers multiply. This skill sets a lean structure and the rules that keep it lean.

# When to Use

Use when starting a new project, when a file or function has grown unwieldy, when logic is leaking across layers, or when onboarding to a codebase that needs reorganizing.

# Inputs

- The project type and stack (web app, API, CLI, automation, etc.).
- The current file layout, if one exists.
- The team's tolerance for structure vs. speed.

# Outputs

- A documented folder/file layout with one responsibility per file.
- Layer boundaries (entry/routing, business logic, data access, presentation).
- File and function size limits and a "create files only when needed" rule.

# Procedure

1. **Separate layers.** Entry/routing files wire requests to logic and nothing more; business logic lives in dedicated modules; data access is isolated; presentation/templates hold no logic.
2. **One responsibility per file.** Name files for what they do (`ocr_engine`, `export_service`, `auth`), and keep unrelated concerns out.
3. **Cap size.** Set practical limits (e.g. entry file stays thin; functions do one thing, ~40 lines; split when longer). Adjust to the language.
4. **Avoid file sprawl.** Don't create READMEs, helpers, or configs that aren't needed yet. Prefer extending an existing file when the change fits.
5. **Centralize config** at the top of the relevant module or in one config file; don't scatter constants.
6. **Ensure runtime dirs exist** (e.g. output/upload folders) at startup rather than assuming them.
7. **Document the layout** in the agent memory file or `/docs` so it's enforced going forward.

# Quality Checklist

- [ ] Routing/entry layer free of business logic
- [ ] Business logic and data access in separate modules
- [ ] Each file has a single clear responsibility
- [ ] Functions do one thing and stay within size limits
- [ ] No unnecessary files created
- [ ] Config centralized, not scattered
- [ ] Layout documented for future contributors

# Edge Cases

- **Tiny scripts/prototypes:** a single file is fine — don't over-structure throwaway code.
- **Framework conventions:** follow the framework's expected layout rather than fighting it.
- **Monorepo:** apply the same boundaries per package; keep shared code in a clearly named shared module.
- **Legacy code:** refactor incrementally toward the structure; don't rewrite everything at once.

# Safety Rules

- Never put business logic in route handlers "just for now" — it never moves later.
- Never import heavy libraries directly into entry/routing files.
- Don't add abstraction layers before they earn their keep.

# Examples

**Good:** `app.py` holds only routes (thin); `ocr_engine.py` does extraction; `excel_writer.py` does formatting; `templates/` holds HTML; `static/` holds CSS. No inline styles, no logic in `app.py`.

**Bad:** A 2,000-line `app.py` mixing routes, OCR, Excel generation, and inline HTML strings.
