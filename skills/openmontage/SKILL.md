---
name: openmontage
description: "Use when one skill is not enough and the job needs a full film: research, narration, music, subtitles, and a costed plan, across 12 production pipelines, with a human approving creative choices and a budget cap before anything runs."
license: AGPL-3.0
---

# Purpose

Turn an AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex) into a video production studio from one plain-language prompt. There is no orchestration program of its own: the agent reads YAML pipeline manifests and Markdown director skills and runs the production. Every pipeline follows research → proposal → script → scene plan → assets → edit → compose, with human approval on creative choices.

> **AGPL-3.0 — copyleft.** If you modify OpenMontage and run it as a networked service, you must release the source. Read the licence before building products on it.

# When to Use

Use for a full film with research, narration, music, subtitles, and a costed plan: animated explainers, avatar spokespersons, character animation, cinematic pieces, clip factories, documentary montages, hybrid cuts, localisation/dubbing, podcast repurposes, screen demos, and talking heads. Use when the job spans more than one craft. Do not use for a single 30-second promo; a smaller skill is faster there.

# Inputs

One plain-language prompt describing the film, the audience, and the outcome, plus the chosen pipeline (or none, and the agent picks). The agent also needs the budget cap and any API keys for paid providers; the zero-key path needs none.

# Outputs

A finished video with narration, music, subtitles, and a decision log for every provider choice, plus the costed plan that preceded it. Demo shorts are listed at about $0.15-$1.33. Rendering uses Remotion for data-driven explainers, HyperFrames (HTML/CSS/GSAP) for motion-graphics-heavy work, and FFmpeg for assembly, encoding, subtitles, and mixing.

# Procedure

1. Pick the pipeline from the 12 available and confirm the brief.
2. Research, then write the proposal and script, and get human approval on the creative choices.
3. Plan the scenes, gather assets, and present the cost estimate. The default budget cap is $10, with a ~$0.50 per-action approval threshold.
4. Produce the edit: generate or gather footage, record narration, add music and subtitles.
5. Compose the final video and log every provider decision.
6. Review the finished film against the brief before delivery.

# Quality Checklist

- [ ] A cost estimate was presented and approved before execution; spend stayed under the cap.
- [ ] Human approval was obtained on the proposal, script, and scene plan.
- [ ] Narration, music, and subtitles are present and in sync.
- [ ] The decision log records every provider choice and its cost.
- [ ] The final film matches the brief; any deviation is flagged, not hidden.

# Edge Cases

- The zero-key path (Piper TTS offline narration, open footage, Remotion/HyperFrames) makes genuinely free documentary montages. Cloud video-generation adapters (Kling, Veo, Runway, Sora, and others) are available but cost real money; that is the key difference from the pure-code skills.
- Documentary montage builds a corpus of real footage from Archive.org, NASA, and Wikimedia Commons (plus Pexels/Unsplash with free keys), ranked by meaning with CLIP embeddings, so it can cut real footage, not just animate stills.
- Tests in the repo are mocked; treat provider claims as integrations, not tested results. There were no tagged releases yet at last check (v0.1.0 on the main branch).

# Safety Rules

- **AGPL-3.0 copyleft: modifying OpenMontage and running it as a networked service requires releasing the source.** Do not build a closed hosted product on it without reading the licence.
- Do not start a paid generation run without the user's approval of the cost estimate.
- Do not use footage or music without confirming its licence; open sources still carry terms.
- Do not present generated footage as real events or real people.

# Examples

Good: "Make a 2-minute documentary montage about the history of the bicycle, with narration and subtitles, and keep it under $2." The agent estimates the cost, gathers open footage, narrates with Piper, and delivers the film with a decision log.

Bad: "Make a video" with no subject, length, or budget. The agent must ask for the brief and the budget cap first.

Practical starting prompt: "Use openmontage to make a [length] [pipeline] about [subject]. Budget cap $[amount]. Approve the proposal before you produce anything."
