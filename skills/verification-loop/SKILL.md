---
name: verification-loop
description: Use when an AI agent's output (code, data transformation, document, config, analysis) will be relied on and the cost of a silent error is high — to separate the builder from an independent verifier, define what "verified" means before building, replay a golden set, and block the merge/ship until the verifier passes. Also use to review an agent workflow that currently trusts its own summary of what it did.
---

# Purpose

Agents are fluent, and fluency is not correctness. The single most
effective control is structural: the thing that produced the work does
not get to grade it. This skill installs a builder → verifier → gate loop
so "it says it's done" becomes "an independent check says it's done".

# When to Use

- Before merging agent-written code or accepting an agent-produced
  migration, report, spreadsheet, or config.
- When an agent workflow has more than two steps and no step re-checks an
  earlier one.
- After any incident where an agent reported success and was wrong.
- When choosing between more model capability and more checking (the
  answer is usually checking).

Not needed for throwaway exploration where nothing downstream depends on
the output.

# Inputs

- The task and its acceptance criteria (if none exist, writing them is
  step 1).
- Access to run the artefact: tests, a shell, a renderer, a sample of real
  inputs.
- A golden set if one exists (see `llm-eval-golden-set`), or 5–10
  representative inputs with known-good outputs.

# Outputs

- A **verification spec**: checkable statements written before building.
- A **verifier** run — a separate agent/session or a script — that has
  not seen the builder's reasoning and reports pass/fail per statement
  with evidence.
- A **gate decision**: ship / fix / escalate, logged with the evidence.

# The loop

```
spec ──► build ──► verify (independent) ──► gate
  ▲                                           │
  └──────────── fix (builder, with findings) ◄┘   max 3 rounds, then escalate
```

Independence means the verifier gets: the spec, the artefact, the inputs.
It does **not** get: the builder's transcript, its summary, or its claims.

# Procedure

1. **Write the spec first.** 5–15 statements of the form "Given X, the
   output shows/returns/contains Y". Each must be checkable by running
   something or opening something — not by reading the code and nodding.
   Include at least one negative case and one boundary case.
2. **Build.** The builder works to the spec. It may run its own checks,
   but those do not count toward the gate.
3. **Hand off cleanly.** Package: artefact + spec + inputs + how to run.
   Strip the builder's narrative. If the verifier is a fresh agent
   session, the prompt is "Here is a spec and an artefact. Verify each
   statement by executing, not by reading. Report evidence."
4. **Verify by execution.** For each statement: run it, capture the
   evidence (test output, rendered screenshot, query result, diff), mark
   PASS / FAIL / CANNOT-CHECK. CANNOT-CHECK is a spec defect, not a pass.
5. **Replay the golden set** where one exists; any regression is a FAIL.
6. **Gate.** All PASS → ship. Any FAIL → back to builder with the
   evidence only (not the verifier's guess at the fix). Three rounds
   without convergence → escalate to a human with the trail.
7. **Record.** Store spec, evidence and decision next to the artefact
   (PR description, `/docs/verification/`, or the ticket).

# What "verify by execution" looks like

| Artefact | Not verification | Verification |
|---|---|---|
| Code change | reading the diff | running tests + one manual scenario from the spec |
| Data transform | "row counts look right" | reconcile totals to source, spot-check 10 rows, check nulls per column |
| Document / report | skimming | every number traced to its source; every claim dated |
| Web page | "renders fine" | screenshot at 2 widths, keyboard-only pass, console clean |
| Config / infra | "applied successfully" | read back the live state and diff against intent |
| LLM feature | one happy-path prompt | golden set replay with pass/fail per case |

# Quality Checklist

- [ ] Spec written before building, every line executable.
- [ ] Verifier had no access to the builder's transcript or summary.
- [ ] Every statement has evidence attached, not a checkmark.
- [ ] CANNOT-CHECK items were converted into checkable ones or escalated.
- [ ] Golden set replayed when one exists.
- [ ] Gate decision and evidence are stored where the next person looks.
- [ ] Round count ≤ 3; escalation path used if exceeded.

# Edge Cases

- No tests exist → the spec becomes the first tests; write them as
  scripts the verifier runs.
- Verifier and builder are the same model → still separate sessions and
  strip context; different model families add diversity when available.
- Non-deterministic outputs (LLM text) → verify properties (contains
  required fields, no banned phrases, length bounds, cites sources),
  not exact strings.
- Time pressure → shrink the spec to the 3 statements whose failure would
  hurt most; never skip the independence.

# Safety Rules

- A builder that reports "all tests pass" without a verifier run has not
  passed the gate.
- Never let the verifier fix the artefact; findings go back to the
  builder so the verifier stays independent for the next round.
- Evidence containing personal or secret data is redacted before it is
  stored with the decision.

# Examples

**Spec line (good):** "Given the sample CSV, running `python
etl.py sample.csv` produces `out.parquet` with 1,204 rows, zero null
`customer_id`, and a `total_amount` sum of 48,211.20 matching the source."
**Spec line (bad):** "The ETL handles the data correctly."

**Verifier report row:** `#4 PASS — sum(total_amount)=48211.20 (query
attached) · #5 FAIL — 3 rows null customer_id (ids listed)`.
