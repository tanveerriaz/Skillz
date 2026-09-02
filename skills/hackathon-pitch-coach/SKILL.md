---
name: hackathon-pitch-coach
description: Use when choosing what to build for a hackathon or preparing its demo and pitch. Turns a brief, idea, time limit, and judging rubric into a focused problem, reliable golden path, timeboxed build plan, and judge-ready story.
---

# Purpose

Optimise for a convincing demonstrated outcome within a hackathon's constraints. The goal is not to produce a large product; it is to prove the most important promise clearly, memorably, and credibly.

# When to Use

Use before or during a hackathon when selecting a problem, narrowing scope, prioritising features, planning a short build, designing a demo, or preparing the final pitch. Do not use this as a general product strategy or full production project-planning skill.

# Inputs

- Challenge brief, theme, and required technologies.
- Time remaining, submission format, team capacity, and available tools.
- Judging rubric, if available.
- Candidate idea, target user, current workaround, and supporting evidence.
- Known technical, privacy, accessibility, or data constraints.

# Outputs

- Recommended problem and evidence-based rationale.
- One-sentence product promise and critical dependency.
- Golden demo path with must-have, stretch, and cut features.
- Timeboxed build, polish, rehearsal, and submission plan.
- Rubric-to-proof mapping, pitch storyline, judge objections, and fallback plan.

# Procedure

1. **Establish the judging context.** Extract the challenge, format, time, audience, team, tools, rubric, eligibility requirements, and submission constraints. Convert rubric weights into build and pitch priorities. If no rubric exists, label assumptions and use problem clarity, originality, technical proof, usability, and demo quality as provisional dimensions.
2. **Choose the problem through evidence.** Identify the person, situation, current workaround, consequence, and evidence. Prefer direct user input; otherwise use credible public information and separate facts from assumptions. Extend trusted behaviour where possible instead of assuming technology should replace it.
3. **Define a testable promise.** Write: “For [specific person] in [specific situation], we help them [outcome] by [mechanism].” State who benefits, how the solution works, how success is recognised, and which capability everything else depends on.
4. **Design the golden demo.** Select the critical capability and make it reliable before adding breadth. Build a short path: context → user action → visible system response → meaningful outcome. Add no more than one or two supporting features. Include a memorable moment only when it reinforces the problem and can be rehearsed safely.
5. **Plan against the clock.** Set milestones for setup, first end-to-end demo, core reliability, visual polish, pitch assets, rehearsal, and submission. Prepare dependencies, starter code, accounts, devices, test data, and backups early. Assign clear ownership for message, scope, time, and integration.
6. **Build the pitch around proof.** Use: human problem → why it matters → solution promise → live demonstration → technical differentiation → impact and next step. Emphasise the dimensions with the greatest rubric weight. Clearly distinguish what is real, simulated, manually prepared, or future work.
7. **Rehearse and freeze.** Run the golden path repeatedly with realistic inputs. Remove fragile scope, prepare a recovery path for the most likely failure, verify submission artefacts, and freeze changes before the final presentation.

# Quality Checklist

- [ ] Target user and situation are specific.
- [ ] Problem claims are supported by evidence or explicitly labelled assumptions.
- [ ] Product promise is understandable in one sentence.
- [ ] Critical dependency is identified and demonstrated.
- [ ] Golden path is short, visible, and repeatable.
- [ ] Must-have scope is separated from stretch and cut scope.
- [ ] Plan includes reliability, polish, rehearsal, and submission time.
- [ ] Pitch emphasis follows the judging rubric.
- [ ] Demo fallback is tested or prepared.

# Edge Cases

- **No direct user access:** use credible public evidence, state uncertainty, and avoid presenting assumptions as user research.
- **No rubric:** use provisional dimensions and explain how the recommendation would change if the rubric appears.
- **Very short build window:** move the first end-to-end demo earlier and cut integrations or polish that do not prove the core promise.
- **Many attractive features:** rank each by rubric value, demo value, effort, and failure risk; keep only the highest-value items.
- **High-risk live integration:** provide a controlled fixture or recorded fallback while being transparent about what is simulated.
- **Team disagreement:** return to the target user, critical dependency, judging rubric, and time remaining as decision criteria.

# Safety Rules

- Never fabricate user research, metrics, technical capability, or validation.
- Do not expose private, personal, confidential, or regulated data in examples or demos.
- Do not use spectacle that obscures the problem or misleads judges about what works.
- Do not expand scope silently; put new ideas in stretch or cut scope.
- Do not claim a prototype is production-ready without evidence.
- Keep backups and demo fixtures free of secrets, credentials, and real customer data.

# Examples

**Good:** A team has 90 minutes and a broad wellbeing theme. The skill narrows the idea to one specific user moment, identifies the recommendation engine as the critical dependency, builds one reliable journey, maps it to the rubric, and reserves the last 15 minutes for rehearsal and submission.

**Bad:** A team builds a portal, mobile app, analytics dashboard, and chatbot without identifying the single outcome the judges must believe, then discovers during the pitch that the core integration is unreliable.

For detailed scripts, scoring matrices, and reusable pitch structures, read [references/pitch-playbook.md](references/pitch-playbook.md).
