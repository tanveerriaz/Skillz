---
name: input-validation-prompt-safety
description: Use when building code that accepts external input or passes user text into an LLM prompt or a shell/command layer. Enforces validate-before-use, allowlisting, length and type checks, output trimming, and prompt-injection defenses so untrusted input can't break logic, leak data, or hijack an AI agent.
---

# Purpose

Treat all external input as untrusted. Two related risks: classic injection (command, SQL, path) and prompt injection (user text steering an LLM to ignore rules or exfiltrate data). This skill applies validation, allowlisting, and prompt hardening so input can't compromise behavior.

# When to Use

Use when writing handlers that accept user input, when constructing LLM prompts from user-supplied text, when executing or shelling out based on input, or when building bots/automations that act on incoming messages.

# Inputs

- The input sources (form fields, API params, chat messages, file uploads).
- Where the input flows (database, shell, LLM prompt, file path).
- The set of legitimate values or commands.

# Outputs

- Validation at every entry point (type, length, format).
- Allowlist enforcement for commands/senders/values.
- Hardened prompt construction with clear instruction/data separation.
- Bounded, sanitized outputs.

# Procedure

1. **Validate before use.** Reject input that isn't the expected type, exceeds a length cap, or fails a format check. Return early on invalid input.
2. **Allowlist, don't blocklist.** Accept only known-good commands, senders, or values; reject everything else by default.
3. **Parameterize data paths.** Use parameterized queries (no string-built SQL), safe path joins (no concatenation), and never `eval` or run raw shells on input.
4. **Separate instructions from data in prompts.** Keep the system/role instructions fixed; insert user text as clearly delimited data, and instruct the model to treat it as untrusted content, not commands.
5. **Constrain the model's authority.** Don't give an LLM-driven agent destructive capabilities triggered directly by raw user text; gate sensitive actions behind explicit checks.
6. **Bound outputs.** Trim/limit response length, escape content rendered back to users, and never echo secrets.
7. **Rate-limit and log.** Throttle to prevent abuse and log actions for an audit trail (without logging sensitive values).

# Quality Checklist

- [ ] Every external input validated for type, length, and format
- [ ] Allowlist enforced for commands/senders/values
- [ ] Queries parameterized; no string-built SQL
- [ ] No `eval` or raw shell execution on input
- [ ] Prompt separates fixed instructions from untrusted user data
- [ ] Sensitive actions gated, not directly triggerable by raw input
- [ ] Outputs bounded and escaped; rate limiting in place

# Edge Cases

- **Legitimate long input:** set a sensible cap and tell the user the limit rather than truncating silently.
- **Rich/structured input:** validate the structure (schema), not just length.
- **Multilingual/Unicode:** normalize before validating to avoid bypass via encoding tricks.
- **Trusted internal calls:** still validate at the boundary; "internal" callers get compromised too.

# Safety Rules

- Never pass unvalidated input into a shell, query, file path, or `eval`.
- Never let user text override an agent's system instructions.
- Never log secrets or full sensitive payloads.
- Reject by default; accept only what you've explicitly allowed.

# Examples

**Good:** A chat automation accepts only messages prefixed `/ai`, from allowlisted senders, under 1,500 chars; user text is inserted into the prompt as delimited untrusted data; replies are trimmed to 1,000 chars; no shell execution.

**Bad:** Passing a raw chat message straight into `os.system(message)` or interpolating it into a system prompt that grants file-deletion powers.
