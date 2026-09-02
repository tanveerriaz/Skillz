---
name: publish-build-journey
description: Turn a meaningful completed build, experiment, deployment, model comparison, failure, or architectural correction into a chronological, image-supported private blog draft with a strict privacy review and explicit publication gate. Use after a demonstrable milestone; when the user says capture this, write about this, publish the thought process, make a blog or social post, or document the journey; or when substantial work ends with a transferable lesson. Do not trigger for routine edits, trivial fixes, unfinished work, or background operations.
---

# Publish Build Journey

Convert completed work into a useful public-learning story without treating tool output, local files, or private context as publishable by default.

## Non-negotiable contract

- Ask once before creating a draft: “This build has a useful story. Would you like me to prepare a private build-journey draft with verified visuals?”
- Do not interrupt routine work or ask after every edit. Offer only after a meaningful milestone with evidence or a changed understanding.
- Treat “yes” as permission to prepare a private draft, not to publish, deploy, post, upload, or message anyone.
- Create drafts outside the public site tree, preferably in an ignored `drafts/` or `.build-journeys/` directory.
- Never read `.env`, credential stores, browser storage/history, shell history, private agent memory, keychains, cookies, or secret-management systems to enrich a story.
- Never publish from inference. Separate verified facts, personal interpretation, and clearly labelled sample/demo material.
- Require explicit approval of the exact copy and exact assets before moving anything into a public directory.
- Require separate authority for commit, push, deployment, LinkedIn posting, newsletter sending, or any other external side effect.

## Workflow

### 1. Decide whether there is a story

Offer a draft only when at least two are true:

- A working artifact, deployment, or repeatable result exists.
- A first attempt failed or materially changed.
- A tool/model comparison affected the approach.
- The work produced a transferable lesson.
- Verified visuals or public evidence exist.
- Another builder would gain a clear starting point.

If the work is unfinished, record a short private note only when asked. Do not manufacture a conclusion.

### 2. Obtain drafting consent

Ask the single closing question above. If declined or unanswered, continue the original task and do nothing else. If accepted, state that the draft will remain local and unpublished.

### 3. Gather bounded evidence

Prefer these sources, in order:

1. User-provided context and explicitly approved personal observations.
2. Public URLs and public repository documentation.
3. The current task’s changed files, test results, and verified screenshots.
4. User-approved excerpts from private work, rewritten at a safe level of abstraction.

Do not scan unrelated repositories, personal folders, logs, messages, calendars, or agent memories. Do not copy raw prompts or terminal output without reviewing every line.

Read [references/story-structure.md](references/story-structure.md) before drafting. For a reusable voice and tool taxonomy, read [references/voice-and-tool-taxonomy.md](references/voice-and-tool-taxonomy.md).

### 4. Build a private chronology

Copy [assets/build-journey-template.md](assets/build-journey-template.md) into the private draft location. Preserve uncertainty and distinguish:

- `Verified`: observable from a public source or executed check.
- `Reflection`: the author's interpretation or lesson.
- `Demo/sample`: fictional, mock, generated, or illustrative material.
- `Private abstraction`: safe summary with implementation details intentionally omitted.

Write from the human side: question, attempt, friction, correction, evidence, lesson, starting point. Do not write a feature-release press release.

### 5. Select visual evidence

Read [references/media-evidence.md](references/media-evidence.md) whenever images, diagrams, audio, or video are considered.

- Prefer real project captures over generated decoration.
- Label generated images, sample data, and fictional interfaces.
- Use before/after or attempt/correction pairs when they explain the lesson.
- Never use a screenshot merely because it is attractive.
- Review the visible frame for terminals, tabs, notifications, usernames, paths, coordinates, account data, and unrelated people.
- Sanitize media into a new file; never overwrite the original.

### 6. Run the privacy preflight

Read [references/privacy-policy.md](references/privacy-policy.md) in full before any publication-ready output.

Run:

```bash
python3 scripts/privacy_scan.py <draft-path> --json
```

For raster images, create metadata-stripped copies:

```bash
python3 scripts/sanitize_media.py <image> --output-dir <safe-output-dir>
```

A clean automated scan is necessary but insufficient. Perform a human-semantic review for employer-confidential context, exact location, personal relationships, private architecture, and facts that become sensitive only in combination.

### 7. Present the review packet

Provide:

- Proposed title and one-sentence thesis.
- Draft path and asset list.
- Public URLs and evidence used.
- Items removed, generalized, or still uncertain.
- Privacy scan result and any warnings.
- Intended destinations, each unchecked by default: website, LinkedIn, newsletter, other.

Ask: “Please review this exact draft and asset set. Should I revise it, approve it for one named destination, or keep it private?”

Do not accept vague earlier enthusiasm as publication approval. Approval must identify the version and destination.

### 8. Publish only the approved version

After exact approval:

- Move or transform only the approved copy and sanitized assets.
- Preserve the canonical Markdown source and generate HTML/JSON mirrors when the destination supports them.
- Add dates, public evidence links, alt text, disclosure labels, and machine-readable metadata.
- Re-run the privacy scan on the final public files.
- Show the final diff or preview.
- Request separate authorization before commit, push, deploy, or external posting unless the user explicitly included that action in the approval.

## Failure rules

- If a secret or likely credential is found, stop and report only its category and file/line; never echo the value.
- If media cannot be sanitized or visually inspected, exclude it.
- If public/private provenance is unclear, classify it as private and ask for a safe public source.
- If the story depends on employer or client details, rewrite at the principle level or keep it private.
- If a tool’s role cannot be verified, say “experimented with” rather than implying expertise, endorsement, or daily use.

## Cross-tool adapters

Use the same contract in Codex, Claude Code, Cursor, Hermes, OpenClaw, and other agent environments. Tools without skill support may use [assets/portable-closing-instruction.md](assets/portable-closing-instruction.md) as a custom instruction. Never weaken the consent or privacy gates to fit a platform.
# Purpose

Transform a verified build milestone into a useful private story draft without treating private work as automatically publishable.

# When to Use

Use after meaningful builds, experiments, deployments, comparisons, failures, or corrections when the user requests or accepts a story draft.

# Inputs

Approved context, current-task evidence, public sources, sanitized visuals, intended audience, and destination constraints.

# Outputs

A private chronological draft, evidence and asset list, privacy report, and explicit publication decision point.

# Procedure

Follow the consent, bounded-evidence, chronology, media, privacy, review-packet, and exact-approval workflow above.

# Quality Checklist

- [ ] Facts, reflection, samples, and private abstractions are clearly distinguished.
- [ ] Every visual has provenance and has been inspected after sanitization.
- [ ] Publication, commit, push, deploy, and posting permissions remain separate.

# Edge Cases

When provenance or consent is unclear, keep the material private and request an approved public source.

# Safety Rules

Never inspect secret stores or unrelated personal context for story material, and never publish without exact version-and-destination approval.

# Examples

**Good:** A local draft based on verified current-task evidence with secrets and locations removed. **Bad:** Turning shell history and private screenshots into a public post without review.
