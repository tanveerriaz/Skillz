---
name: saas-mvp-planner
description: Use when shaping a SaaS or app idea into a buildable MVP. Pins down the core user, the one problem, the smallest valuable solution, a basic user journey, and what to deliberately leave out — so you build the thinnest thing that's actually useful instead of a bloated v1.
---

# Purpose

Turn a SaaS idea into a focused, buildable MVP. The common failure is building too much: a v1 stuffed with features nobody asked for. This skill forces a single core user, a single problem, and the smallest solution that delivers real value, with everything else explicitly deferred.

# When to Use

Use when you have a product idea and need to decide what to actually build first, when a planned v1 is sprawling, or when validating whether an idea is tight enough to start.

# Inputs

- The idea and the user it's for.
- The problem you believe it solves.
- Any constraints (time, stack, solo vs. team).

# Outputs

- A one-line problem statement and target user.
- The core value the MVP must deliver.
- A minimal feature set (and an explicit "not now" list).
- A basic happy-path user journey.
- The single riskiest assumption to test first.

# Procedure

1. **Name one core user.** Resist "everyone" — pick the user who feels the pain most.
2. **State one problem** in a sentence. If there are several, choose the sharpest.
3. **Define the core value:** the one outcome the user gets. The MVP exists to deliver this.
4. **Cut to the minimal feature set** that delivers that value — typically a single core loop (sign in → do the one thing → get the result).
5. **Write the "not now" list.** Everything tempting that doesn't serve the core loop goes here. This list is the point.
6. **Sketch the happy path** as a short user journey so the build has a spine.
7. **Identify the riskiest assumption** (will they use it? will it work? will they pay?) and how the MVP tests it.
8. **Sanity-check feasibility** against constraints; if the MVP is still too big, cut again.

# Quality Checklist

- [ ] Exactly one core user named
- [ ] One problem stated in a sentence
- [ ] Core value is a single clear outcome
- [ ] Feature set is the minimum for that value
- [ ] Explicit "not now" list exists
- [ ] Happy-path journey defined
- [ ] Riskiest assumption identified and testable

# Edge Cases

- **"It's for everyone":** pick the sharpest segment for the MVP; broaden later.
- **Two-sided marketplace:** seed one side first; don't build both at full strength.
- **Regulated/complex domain:** scope the MVP to a non-regulated slice or a manual-in-the-loop version to validate demand first.
- **Idea depends on scale to work:** find a smaller proxy to test the core assumption cheaply.

# Safety Rules

- Don't build features outside the core loop in the MVP — defer them.
- Don't confuse "what's impressive" with "what delivers the core value".
- Keep any example data public-safe; don't model the MVP on confidential client specifics.

# Examples

**Good:** "User: solo founder drowning in receipts. Problem: expense tracking is manual. Core value: photo → categorized expense. MVP: upload receipt, auto-extract amount/date, list view. Not now: multi-user, reports, integrations. Riskiest assumption: extraction is accurate enough to trust — test on 50 real receipts."

**Bad:** A v1 plan with teams, roles, dashboards, integrations, and billing — before anyone has confirmed the core action is useful.
