---
name: llm-eval-golden-set
description: Use when an LLM feature needs to stay reliable across prompt or model changes. Builds a small golden set of representative inputs with expected qualities and a repeatable eval script, so you can measure quality and catch regressions instead of eyeballing one example.
---

# Purpose

Stop LLM features from silently regressing. Prompt tweaks and model swaps change behavior in ways one manual test won't reveal. This skill creates a golden set (curated inputs + expected qualities) and a runner that scores output, turning "seems fine" into a measurable, repeatable check.

# When to Use

Use when you have an LLM feature in production or about to ship, before changing a prompt or model, or when you keep getting surprised by quality drift. Use it as the validation step for any AI-output feature.

# Inputs

- Representative real-world inputs the feature must handle (including tricky/edge cases).
- The expected qualities or acceptance criteria for each output.
- The feature's callable entry point.

# Outputs

- A `golden_set.json` of input → expected-qualities cases.
- A `run_evals` script that runs each case and reports pass/fail or a score.
- A baseline you can re-run after every prompt/model change.

# Procedure

1. **Curate cases.** Pick a small, diverse set (10–30) covering common inputs, edge cases, and past failures. Quality of coverage beats quantity.
2. **Define expectations per case.** Specify checkable qualities: must include X, must not invent Y, correct format, length bounds, correct classification — whatever defines "good" for that input.
3. **Store as data** (`golden_set.json`) so cases are versioned and reviewable.
4. **Write a runner** that loads the set, calls the feature for each input, and evaluates output against the expectations (string/format checks for objective criteria; an LLM-as-judge or rubric for subjective ones).
5. **Establish a baseline** score and record it.
6. **Re-run on every change** to the prompt, model, or surrounding logic; compare to baseline and investigate drops.
7. **Grow the set** by adding any new real-world failure as a case so it can't regress again.

# Quality Checklist

- [ ] Golden set covers common, edge, and past-failure inputs
- [ ] Each case has explicit, checkable expectations
- [ ] Cases stored as versioned data
- [ ] Runner is repeatable and reports clear pass/fail or score
- [ ] Baseline recorded
- [ ] Re-run wired into the change workflow
- [ ] New failures added back as cases

# Edge Cases

- **Subjective quality:** use a rubric or LLM-as-judge with a fixed grading prompt; keep it consistent across runs.
- **Non-deterministic output:** run multiple samples or assert on stable properties rather than exact strings.
- **Small team / no infra:** a plain script and JSON file is enough; don't over-build.
- **Expensive calls:** keep the set small and run the full suite only on meaningful changes.

# Safety Rules

- Never put real personal data or secrets in the golden set — use synthetic, public-safe inputs.
- Never ship a prompt/model change without re-running the evals.
- Don't game the set by tuning prompts to memorize cases; keep cases representative.

# Examples

See `examples/golden_set.json` for a starter format.

**Good:** A 20-case `golden_set.json` plus `run_evals.py`; after a prompt change the score drops from 19/20 to 14/20, revealing a regression before release.

**Bad:** Testing a new prompt on one cherry-picked input, shipping it, and discovering in production it now hallucinates on common queries.
