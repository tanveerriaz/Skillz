---
name: local-first-ai-automation
description: Use when building a personal automation that runs locally with a local LLM (e.g. Ollama) and/or browser automation, with no paid SaaS. Establishes a safe architecture — allowlisted triggers, command prefixes, no destructive actions, graceful timeouts — for tools that act on your behalf without cloud dependencies.
---

# Purpose

Build personal automations that run entirely on your machine, using a local model and browser automation instead of paid cloud services — while staying safe. Automations that read messages and act are powerful and risky; this skill defines the guardrails that keep a local agent useful without letting it do damage.

# When to Use

Use when building a local assistant or bot (e.g. a chat-triggered command runner), integrating a local LLM via its HTTP API, or automating a web app via browser control for personal use. Use it when you want zero external SaaS and full local control.

# Inputs

- The trigger source (a chat app, a folder watcher, a hotkey) and how messages/events arrive.
- The local model endpoint (e.g. `http://localhost:11434/api/generate`) and chosen model.
- The set of allowed senders and commands.

# Outputs

- A layered design: listener → parser/validator → prompt builder → local model client → response trimmer → responder.
- Safety controls: allowlist, command prefix, no destructive operations, rate limiting, audit logging.
- A tool that runs locally with no paid dependencies.

# Procedure

1. **Layer the pipeline.** Keep the listener, command parsing/validation, prompt building, model call, and response sending in separate modules.
2. **Gate triggers.** Only act on an explicit command prefix (e.g. `/ai`) and only from allowlisted senders/sources; ignore everything else.
3. **Validate input** (type, length cap, format) before building any prompt — see input-validation-prompt-safety.
4. **Call the local model** over its HTTP API with `stream: false` (or streamed if you handle it), and handle timeouts/failures gracefully.
5. **Forbid destructive actions.** No shell execution, no file deletion, no irreversible operations triggered by a message.
6. **Shape responses.** Send an immediate "processing…" ack, trim final output to a sane length, and split long replies.
7. **Be human-paced.** Add a small delay and rate-limit to avoid spammy or bot-like behavior and to respect platform terms.
8. **Log actions** to a local audit trail (without logging sensitive content).

# Quality Checklist

- [ ] Pipeline split into clear single-purpose modules
- [ ] Command prefix + sender allowlist enforced
- [ ] Input validated before prompting
- [ ] Local model calls handle timeouts/failures
- [ ] No shell execution, deletion, or destructive ops
- [ ] Responses trimmed and rate-limited
- [ ] Actions logged locally; no secrets in logs

# Edge Cases

- **Model is slow or down:** ack the request, then return a clear failure message instead of hanging.
- **Browser session expires (e.g. QR/login):** detect and prompt for a one-time manual re-auth rather than looping.
- **Burst of messages:** rate-limit and process one at a time.
- **Ambiguous command:** reply with usage/help rather than guessing.

# Safety Rules

- Never execute raw shell commands or delete files based on a message.
- Never act on non-allowlisted senders or un-prefixed messages.
- Respect the target platform's personal-use terms; keep it non-commercial unless permitted.
- Keep everything local; don't quietly send data to third-party services.

# Examples

**Good:** A local "chat → model" tool: browser automation reads messages, accepts only `/ai ...` from your own number, sends the text to a local model, trims the reply to ~1,000 chars, and logs each action. No cloud APIs, no shell access.

**Bad:** A bot that executes any received text as a shell command, or that auto-replies to everyone with no rate limit.
