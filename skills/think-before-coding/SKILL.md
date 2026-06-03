---
name: think-before-coding
description: Use before writing or changing any non-trivial code. Forces evaluation of at least three distinct solution approaches with brief trade-offs before implementing, so the chosen design fits the existing codebase instead of being the first idea that came to mind.
---

# Purpose

Counter the instinct to implement the first idea. For any non-trivial change, briefly considering three distinct approaches surfaces better designs, reveals constraints early, and produces code that fits the project's existing patterns. The cost is a few lines of reasoning; the payoff is fewer rewrites and less accidental complexity.

# When to Use

Use before writing or modifying non-trivial code: new features, refactors, anything with design choices around where logic lives or which abstraction to use. Skip it for trivial edits (typos, copy changes, one-line config tweaks) where deliberation adds no value.

# Inputs

- A clear statement of the problem to solve.
- Knowledge of the existing stack, patterns, and constraints.

# Outputs

- A short list of three distinct approaches with one-line pros/cons each.
- A chosen approach with a one-line rationale tied to project fit.

# Procedure

1. **State the problem** precisely — what must be solved or improved.
2. **Outline three distinct approaches.** Distinct means genuinely different, e.g.:
   - Different algorithms or data structures.
   - Different placement of logic (component vs. hook vs. service vs. backend).
   - Different change levels (minimal fix vs. refactor vs. new abstraction).
   - Different library/API vs. the existing stack.
3. **Compare briefly** on simplicity, performance, maintainability, and fit with existing code. A few bullets per option is enough.
4. **Choose and justify.** Prefer the option with minimal change that reuses existing patterns, unless a heavier option is clearly warranted.
5. **Implement** the chosen approach.

# Quality Checklist

- [ ] Problem stated clearly
- [ ] Three genuinely distinct approaches listed
- [ ] Each compared on at least one trade-off
- [ ] Chosen approach justified by project fit
- [ ] Heavier approaches rejected for a stated reason

# Edge Cases

- **Only one viable approach truly exists:** say so and explain why the alternatives don't apply.
- **Trivial change:** skip — note that deliberation isn't warranted.
- **All three are close:** pick the smallest-footprint option and move on; don't over-analyze.

# Safety Rules

- Do not skip straight to coding on a non-trivial change.
- Do not pad with fake alternatives just to reach three — distinctness matters more than count.

# Examples

**Good:** "Need to debounce search input. (1) Inline setTimeout in the component — simplest, but duplicated if reused. (2) A `useDebounce` hook — reusable, fits our hooks folder. (3) Move filtering server-side with a debounced request — best for large datasets but bigger change. Choosing (2): reusable and matches existing patterns; data is small enough not to need (3)."

**Bad:** Immediately adding a `setTimeout` in the component without considering reuse or server-side options.
