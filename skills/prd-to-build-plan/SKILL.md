---
name: prd-to-build-plan
description: Use to turn a product idea, PRD, or feature request into a phased, buildable plan. Converts intent into goals, non-goals, scope, a phased milestone breakdown, and acceptance criteria an AI agent or developer can execute step by step — replacing "build me X" with a sequenced plan.
---

# Purpose

Bridge product intent and implementation. A one-line request ("build a dashboard") gives an agent nothing to sequence. This skill turns an idea or PRD into a phased plan with explicit scope, milestones, and acceptance criteria, so building is ordered and verifiable.

# When to Use

Use when handed a PRD, feature idea, or vague "build X" request before writing code; when a task is too big to do in one pass; or when you need to align on scope and sequence before committing effort.

# Inputs

- The product idea, PRD, or feature description.
- Known constraints (stack, timeline, must-haves, must-not-haves).
- The definition of success, if stated.

# Outputs

- A build plan with: goal, non-goals, in/out-of-scope, phased milestones (each independently shippable), acceptance criteria per phase, dependencies/risks, and a suggested first step.

# Procedure

1. **Restate the goal** in one or two sentences and confirm the problem being solved.
2. **Set non-goals** explicitly — what this will not do — to prevent scope creep.
3. **Define scope:** the minimal set of capabilities for the goal; defer the rest to "later".
4. **Phase the work** into milestones that each deliver something runnable/verifiable (e.g. Phase 1 = data + read view; Phase 2 = create/edit; Phase 3 = polish). Avoid a single monolithic phase.
5. **Write acceptance criteria** per phase — observable conditions that prove it's done.
6. **Surface dependencies and risks** (data, external services, unknowns) up front.
7. **Recommend the first step** so execution can start immediately.
8. **Keep it lean.** Match plan depth to the size of the work; a small feature gets a short plan.

# Quality Checklist

- [ ] Goal restated clearly
- [ ] Non-goals explicit
- [ ] Scope minimized to what the goal needs
- [ ] Phases are independently shippable and ordered
- [ ] Each phase has acceptance criteria
- [ ] Dependencies and risks identified
- [ ] A concrete first step proposed

# Edge Cases

- **Vague request:** infer a reasonable scope, state assumptions, and proceed — don't stall on a question that has a sensible default.
- **Huge PRD:** identify the core loop and phase the rest behind it.
- **Conflicting requirements:** flag the conflict and propose a resolution rather than building both.
- **Research needed first:** add a discovery phase before implementation phases.

# Safety Rules

- Never expand scope silently; new scope goes in "later" or a new phase.
- Never start coding a large feature without a phased plan.
- Don't invent requirements the source didn't state — mark inferences as assumptions.

# Examples

**Good:** "Goal: weekly metrics dashboard. Non-goals: real-time, multi-tenant. Scope: 4 KPIs, week view. Phase 1: data layer + KPI cards (accept: cards show correct totals). Phase 2: trend chart + week filter. Phase 3: empty/error states. First step: define the data shape."

**Bad:** Receiving "build a dashboard" and immediately writing UI with no scope, phases, or acceptance criteria.
