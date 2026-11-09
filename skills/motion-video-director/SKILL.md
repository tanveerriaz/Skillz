---
name: motion-video-director
description: Use when one skill must do the whole production: plan, animate, edit real footage and talking-head clips, voice, and sound-design complete videos with Claude Code, Codex, or Cursor, rendering everything locally with no After Effects or Premiere.
license: not stated — verify before commercial reuse
---

# Purpose

Turn a coding agent into a video production team. Plan, animate, edit, voice, and sound-design complete videos with Claude Code, Codex, or Cursor. Everything renders locally, with no After Effects or Premiere. Unlike the code-only video skills, this one also edits raw footage and talking-head clips.

> **Licence not stated in the listing — verify the licence file before commercial reuse.** The skill folder carries its own LICENSE.md; check it before using this skill's output commercially. Do not assume a licence.

# When to Use

Use for complete videos that mix code-drawn motion graphics (Canvas, SVG, Three.js, GSAP) with edited real footage: cuts, punch zooms, captions, B-roll, text behind the subject, speed ramps, and subject cutouts. Use when the job needs both a motion designer and an editor. Do not use for a single 30-second promo when a smaller skill is faster.

# Inputs

A brief describing the video, the audience, and the outcome, plus any raw footage, talking-head clips, product pages, and references. The agent works through approval gates, so the user must be available to approve the voiceover script and storyboard.

# Outputs

An MP4 in 9:16, 16:9, or 1:1 with voiceover, captions, and a -14 LUFS mix, plus the storyboard, the voiceover script with word-level timing, and a PROGRESS.md log so a new session can resume the job.

# Procedure

1. Take the brief and write the ElevenLabs voiceover script, with word-level timing via faster-whisper.
2. Build a storyboard timed to the words and get approval at the gate.
3. Build the motion graphics in code (kinetic typography, 3D text, UI mockups, cursor animation, stickers, particles, Lottie, Three.js product shots, camera fly-throughs) and edit the footage (cuts, punch zooms, B-roll, text behind the subject, speed ramps, subject cutouts with RVM or SAM2).
4. Preview with a contact sheet and fix what is wrong.
5. Render and mix to -14 LUFS, and log progress in PROGRESS.md throughout.

# Quality Checklist

- [ ] The storyboard was approved before the build started.
- [ ] Voiceover timing matches the visuals word by word.
- [ ] The contact-sheet preview was inspected; defects were fixed before the final render.
- [ ] The mix measures -14 LUFS; the MP4 plays end to end with audio.
- [ ] PROGRESS.md records the state, so the job can resume in a new session.

# Edge Cases

- Assets come from Firecrawl, Freesound, Pixabay, Unsplash, and LottieFiles; the agent can also browse Pinterest and Behance with Playwright for references. References are for style only, never for reuse.
- A SkillsLLM automated scan passed with no high-severity issues, but flagged two medium "secret-exfiltration" items (SKILL.md lines 130/135, about credentials to an external endpoint). Review its `.env` and credential handling before entering API keys.
- Subject cutouts (RVM, SAM2) need the optional dependencies; without them, cutouts are skipped, not faked.

# Safety Rules

- **Licence not stated in the listing: check the skill folder's LICENSE.md before commercial reuse.** This skill's marketplace status is `draft` for that reason.
- Review the skill's credential handling before entering API keys, given the flagged secret-exfiltration items.
- Do not present edited footage as unedited reality, and do not reuse reference material from Pinterest or Behance.
- Do not ship music, SFX, fonts, or stock without confirming their licences.

# Examples

Good: "Make a 60-second product video: animate the features in code, then cut in my talking-head clip with captions and B-roll." The agent scripts the voiceover, storyboards to the words, builds both halves, previews, and renders.

Bad: "Edit my video" with no footage, brief, or target length. The agent must ask for the material and the brief first.

Practical starting prompt: "Use motion-video-director to make a [duration] [format] video about [subject]. Approve the voiceover script and storyboard before you build."
