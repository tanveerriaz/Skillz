---
name: llm-prompt-design
description: Use when building LLM-powered features (rewriting, summarizing, generating text) inside an app. Centralizes prompts in one place, separates role/tone from task structure from per-call context, and applies anti-"AI slop" rules so outputs read like a human wrote them and behavior is easy to change.
---

# Purpose

Make LLM features maintainable and the output human-sounding. Prompts scattered through a codebase drift and contradict; ungoverned prompts produce hype-filled "AI slop". This skill centralizes prompt building blocks and bakes in plain-English, no-hype output rules.

# When to Use

Use when adding any LLM feature (text rewrite, summarize, enhance, generate), when an app's AI output sounds robotic or salesy, or when prompt logic is duplicated across files and hard to tune.

# Inputs

- The task the LLM should perform and where it's invoked.
- The desired voice/role and output shape.
- Any per-call context (which screen/section/use case the call serves).

# Outputs

- A single module holding all prompt building blocks.
- Composable prompt parts: role/tone, output structure, anti-slop rules, and a per-call context hook.
- Predictable, human-sounding output that's easy to adjust in one place.

# Procedure

1. **Centralize prompts.** Put all prompt text and builders in one module (e.g. `prompts.py` / `llm/prompts.ts`); call it from feature code rather than inlining strings.
2. **Separate the layers:** a fixed role/tone block, an output-structure block (short line vs. paragraphs vs. bullets), an anti-slop rules block, and a per-call context label that tells the prompt where it's being used.
3. **Define role and tone** concretely (e.g. "senior program manager voice; no invented facts").
4. **Add anti-slop rules:** plain English, no hype, no clichéd chatbot closers ("I hope this helps!"), no buzzword padding, preserve the user's facts, don't invent details.
5. **Make output structure explicit** so the model returns the shape the UI expects.
6. **Pass usage context** so the same builder adapts to different screens without forking prompts.
7. **Test prompt composition** with simple assertions (the assembled prompt contains the required blocks) and spot-check output quality.
8. **Degrade gracefully:** if the LLM call fails or is disabled, keep the user's original text rather than blanking it.

# Quality Checklist

- [ ] All prompts live in one module
- [ ] Role/tone, structure, anti-slop, and context are separate, composable parts
- [ ] Anti-slop rules included (no hype, no invented facts, no clichéd closers)
- [ ] Output structure matches what the UI consumes
- [ ] Behavior changeable in one place
- [ ] Graceful fallback when the model is unavailable
- [ ] Prompt composition covered by a basic test

# Edge Cases

- **Model unavailable / no API key:** preserve user input; never replace it with an error string.
- **Output drifts from required shape:** tighten the structure block and add a format example.
- **Different screens, same task:** vary only the context label, not the whole prompt.
- **Sensitive content:** instruct the model not to invent facts and keep the user's wording.

# Safety Rules

- Never hardcode API keys in prompt modules (see secure-env-setup).
- Never let the model invent facts the user didn't provide.
- Never ship hype/marketing tone unless explicitly requested.
- Treat user-supplied text as untrusted data in the prompt (see input-validation-prompt-safety).

# Examples

**Good:** A `prompts` module exposes `build_rewrite_prompt(role, structure, context)`; an "enhance update" feature composes the PM-voice role + short-line structure + anti-slop rules + a `create_action` context label; tests assert all blocks are present.

**Bad:** A dozen feature files each containing their own f-string prompt, half of which produce "Unleash the power of your data! 🚀".
