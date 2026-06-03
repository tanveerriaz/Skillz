---
name: bug-root-cause-analysis
description: Use when investigating a bug, error, or "works here but not there" behavior. Runs a disciplined reproduce → isolate → diagnose → fix → validate loop so the real cause is fixed, not just the symptom, and the fix is proven before closing.
---

# Purpose

Fix the actual cause of a bug, not a surface symptom. Under time pressure, agents and developers patch the first thing that looks wrong, which masks defects and creates regressions. This skill enforces reproduction before theorizing and validation before closing.

# When to Use

Use when given an error message or stack trace, when behavior diverges from expectation, when something works in one environment but not another, or when a bug reappears after a previous "fix".

# Inputs

- The symptom: error text, stack trace, or a description of wrong behavior.
- Steps to reproduce, or enough context to derive them.
- The relevant code, logs, and environment differences.

# Outputs

- A confirmed reproduction.
- A root cause statement explaining why the bug happens.
- A targeted fix addressing the cause.
- Evidence the fix works and the symptom is gone, plus a regression check.

# Procedure

1. **Reproduce first.** Establish reliable steps that trigger the bug. If it can't be reproduced, gather more data before changing code.
2. **Isolate.** Narrow the failure: which layer, which input, which commit. Use bisection, logging, or minimal test cases to shrink the search space.
3. **Form a hypothesis** about the cause and predict what you'd observe if it's right; then test that prediction.
4. **Confirm the root cause** — the underlying reason, not the first suspicious line. Ask "why" until you reach something that, if changed, prevents the bug.
5. **Fix at the cause.** Make the smallest change that addresses the root, not a symptom mask.
6. **Validate.** Re-run the reproduction: symptom gone. Add or update a test that would have caught it. Check nearby flows for regressions.
7. **Note environment factors** if the bug was environment-specific (config, versions, data).

# Quality Checklist

- [ ] Bug reproduced reliably before any change
- [ ] Failure isolated to a specific layer/input/commit
- [ ] Root cause stated, not just the symptom
- [ ] Fix targets the cause and is minimal
- [ ] Reproduction re-run and now passes
- [ ] Regression test added or updated
- [ ] Environment-specific factors documented

# Edge Cases

- **Cannot reproduce:** add logging/observability and gather conditions; do not "fix" blindly.
- **Heisenbug (intermittent):** look for race conditions, ordering, or shared state; reproduce under load or with timing changes.
- **Multiple contributing causes:** fix the primary cause, document the others, and decide if they need follow-up.
- **Works locally, fails in prod:** compare config, versions, data, and permissions before touching logic.

# Safety Rules

- Never close a bug without re-running the reproduction.
- Never patch a symptom when the cause is reachable.
- Never disable a test to make a build green — fix the cause.
- Avoid speculative shotgun changes; change one thing at a time.

# Examples

**Good:** "Reproduced 500 on /checkout with empty cart. Isolated to `total()` dividing by item count. Root cause: no guard for zero items. Fix: return 0 for empty cart. Validated: /checkout now returns 200; added `test_empty_cart_total`."

**Bad:** Wrapping the checkout handler in a broad try/except so the 500 disappears, leaving the divide-by-zero in place.
