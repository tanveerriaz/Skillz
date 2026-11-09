---
name: agentic-motion-graphics
description: Use when a video must be produced like a shoot: research a reference, write a scene-by-scene script, voice it, align every word to the timeline with forced alignment, and render HTML/GSAP scenes to MP4 through HyperFrames.
license: not stated — verify before commercial reuse
---

# Purpose

Produce a motion-graphics video end to end as code, never in a video editor. The agent researches a reference, writes the script, generates the voiceover, extracts word-level timestamps, binds the GSAP timeline to the spoken words, and renders to MP4 via the HyperFrames CLI.

> **Licence not stated — verify before commercial reuse.** The upstream SKILL.md page states no licence. Do not assume MIT or Apache. Check the upstream repo for a licence before using this skill's output commercially.

# When to Use

Use for SaaS product launches (30-60s, 16:9), article or paper explainers (1-3 min, SVG characters), longform-to-shortform viral cuts (45-90s, 9:16), personalised commercial proposals (1.5-2.5 min), and dynamic presentation decks. Use when the voiceover must drive the visuals word by word. Do not use when the job needs real footage; every frame is drawn in HTML/SVG and animated with GSAP.

# Inputs

A product URL, essay or paper, longform transcript or video, client proposal, or static deck, plus the target format, duration, and voice. The agent also needs a reference video when the brief asks for a specific style; it builds a contact sheet from it first.

# Outputs

An MP4 (16:9 1920x1080 at 30/60fps or 9:16 1080x1920) with word-synced captions and voiceover, plus the working files: `scripts/script.json`, `timing.json` (millisecond word timestamps), the `index.html` composition, and the render log. The mix targets ~-14 LUFS.

# Procedure

1. Research the source and build a contact sheet from the reference video.
2. Write the scene-by-scene script as `scripts/script.json`.
3. Generate the voiceover (OpenAI TTS or ElevenLabs), trim silence, and adjust tempo with ffmpeg.
4. Run Whisper forced alignment to produce `timing.json` with millisecond-accurate word timestamps.
5. Build `index.html` with a GSAP timeline tied to `timing.json`, and generate procedural SFX and music on the same BPM clock via `scripts/synth_sfx.py`.
6. Lint, snapshot, render, and QA: inspect snapshots, check loudness to ~-14 LUFS, confirm duration matches within 100 ms, and run a black-frame check.

# Quality Checklist

- [ ] Every visual beat lands on the word that carries it; no drift between voice and picture.
- [ ] The script fits the target duration before rendering starts.
- [ ] Snapshots were inspected at scene boundaries; no clipped type or empty frames.
- [ ] Loudness measures ~-14 LUFS; duration matches the script within 100 ms.
- [ ] No black frames in the render.

# Edge Cases

- A reference video sets style only; its footage, wording, and assets are never reused.
- Longform source material is cut to the shortform format first; the script is rewritten for the target duration, not compressed after the fact.
- If forced alignment drifts on a noisy voiceover, re-trim the audio and re-align before rebuilding the timeline.

# Safety Rules

- **Licence not stated: do not use this skill's output commercially until the upstream licence is confirmed.** This skill's marketplace status is `draft` for that reason.
- Do not present generated footage as real product footage or real customer results.
- Do not ship music or SFX you have not cleared; the synthesised SFX are procedural, but any supplied track needs rights.
- Do not skip the snapshot QA step; a bad frame in a rendered video is expensive to redo.

# Examples

Good: "Turn this product page into a 45-second 9:16 launch video. Voiceover first, visuals on the words." The agent researches the page, scripts it, voices it, aligns the words, and renders.

Bad: "Make the video exactly like this reference ad." The agent must borrow the structure and pacing, not the reference's wording, footage, or brand assets.

Practical starting prompt: "Use agentic-motion-graphics to turn [URL or document] into a [duration] [format] video. Voiceover drives the visuals."
