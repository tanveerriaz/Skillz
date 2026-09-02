---
name: pixel-recap
description: Turn event or product photos into a short 8-bit pixel-art recap video with a narrative arc, ready for LinkedIn/social. Use when the user wants an event recap video, a pixel-art/retro video from photos, an animated post asset, or says "make a recap like the meetup video". Covers the creative method (read the room's visual language, medium-proves-message, narrative arc) and the technical pipeline (photo stylization, shot script, fal.ai reference-to-video, delivery).
---

# Pixel Recap — 8-bit story videos from real photos

Turn a folder of photos into a 15-second pixel-art recap video that *proves* the story it tells, not just decorates it.

## The creative method (do this BEFORE any tooling)

1. **Find the thesis, not the highlights.** A recap is an argument, not a slideshow. Ask: what did this event/product *conclude*? One sentence. Everything in the video must serve it.
   - Example: "Agents become teammates the moment you can see them working."

2. **Let the room choose the style.** Look at what the participants themselves built, wore, projected, demoed. If multiple people independently converged on a visual language (pixel art, terminal aesthetics, hand-drawn, neon), that IS the style. Adopting the community's own dialect beats imposing an outsider's aesthetic. If no convergence exists, default to a style that embodies the thesis.

3. **Ground in reality, then translate.** Stylize the REAL photos rather than generating scenes from scratch. Authenticity first, style second — viewers must recognize the actual room, people, screens. The style transfer is the bridge from "what happened" to "what it meant."

4. **Structure the arc as one continuous idea.** The classic 5-shot/15s shape:
   - Shot 1 (0–3s): establish the real world (wide shot, recognizable location)
   - Shot 2 (3–6s): dive into the smallest detail that carries the thesis (a notch, a cursor, a widget) — the protagonist wakes up here
   - Shots 3–4 (6–12s): escalate through 2 increasingly immersive worlds, with a twist/energy peak in shot 4
   - Shot 5 (12–15s): pull back to the opening location — but now transformed by the thesis (the boundary has dissolved). Close on a text stamp that lands the argument in ≤5 words.

5. **Give it a protagonist.** One recurring character (mascot, sprite, object) that appears in shot 2 and is still there at the end. Continuity is what makes 15 seconds feel like a story instead of a montage.

6. **Medium proves message.** Final check: if the video's own form doesn't demonstrate the thesis, rework it. A video about "seeing agents work" must let you watch something work.

## The technical pipeline

### Step 1 — Stylize photos into 8-bit stills (deterministic, no AI)
Run `scripts/pixelate.py` (requires Pillow). Key parameters and why:
- **EXIF transpose first** — phone photos are often stored rotated; skipping this silently ruins references.
- Saturation ×1.45, contrast ×1.15 — punchy retro palette.
- Downscale to a **160-px-wide grid** (the "true" resolution), quantize to **~40 colors** (median cut, no dither), upscale nearest-neighbor to 1280 px. This is the same constraint math old consoles imposed by hardware — it looks honest because it is.

### Step 1b — Generate the shots that have no photograph (local, free)
Some shots in the arc are metaphor, not record: the escalating interior worlds of shots 3–4, and the protagonist sprite. Those have no source photo. Generate them locally rather than paying a video model to invent them mid-shot.

- Local model: **FLUX.2 Klein 4B** via the MCP tool `generate_image` (`http://127.0.0.1:7878/mcp`). Free, on-device, ~30s for 1280×720, unlimited iteration.
- **Always run Klein output through `scripts/pixelate.py`.** Klein does not produce pixel art when you ask it to — prompting "8-bit, chunky pixels, no anti-aliasing" yields a smooth illustration with pixel-art *composition*. The 8-bit look comes from the deterministic quantize step, never from the model. So: prompt Klein for the **scene** (subject, lighting, camera, palette direction), then let Step 1 impose the style. Same treatment as a photograph — which is the point: generated and photographed shots go through one identical stylizer, so they cut together.
- Pass a fixed `seed` and feed the previous still as a `reference_images` entry (i2i, up to 3) to hold the protagonist consistent across shots.
- **Keep the grounded shots photographic.** Shots 1 and 5 — the real room you establish in and return to — must come from Step 1 stylization. That authenticity is what makes the recap an argument rather than a cartoon; generate all five and you have a nice pixel film about an event that looks like nothing in particular. Shot 2 goes either way, depending on whether the detail carrying the thesis was actually photographed.
- This is also the cheapest lever on the whole pipeline: locking the storyboard locally for free means buying **one** animation pass instead of re-rolling a paid generation until the composition reads right.

### Step 2 — Build compact references (≤9 images)
- Pick one reference per shot + one for the protagonist + one for branding. 5–7 total is the sweet spot — and on H3 the first 5 are free, so 5 refs is also the price break.
- For the protagonist: crop it from the highest-res source photo, then downscale→quantize(8 colors)→nearest-upscale for a clean sprite sheet look.
- Compress: 480 px wide, palette PNG. Each ref lands at 8–15 KB — matters if you have to move them through constrained channels.

### Step 3 — Generate via fal.ai reference-to-video

**Default: MiniMax H3.** `minimax/h3/reference-to-video` — flat per-second billing, native stereo audio, 2K.
- Price: 768P $0.08/s, 2K $0.13/s, 4K $0.16/s. First 5 reference images free, extras $0.08 each. A 15s 2K recap is ~$1.95.
- Payload: `prompt`, `reference_image_urls` (up to 9), `resolution: "2K"`, `aspect_ratio: "16:9"` (9:16 if mobile-first), `duration: 15`. Audio is native and always on — there is no `generate_audio` flag.
- **Cite references as `Image 1`, `Image 2`… in the prompt text** — plain words, matching upload order. This is not Seedance's `@Image1` syntax; using `@` here silently loses the anchoring.
- Also accepts `reference_video_urls` and `reference_audio_urls` (up to 3 each, 2–15s). Feeding your own chiptune track as `Audio 1` makes it sync picture to your music instead of inventing a score. Total reference files across all modalities: 12.

Run `scripts/generate_fal.py REFS_DIR PROMPT_FILE` (defaults to H3 at 2K). Use the prepared venv — Homebrew Python is PEP 668–managed, so a bare `pip install` fails:
```
export FAL_KEY=...
~/.agents/venvs/pixel-recap/bin/python scripts/generate_fal.py refs/ prompt.txt
```

**Alternatives, in order of when to reach for them:**
- `bytedance/seedance-2.0/reference-to-video` — the premium option, and **token-billed, not per-second**: a measured 15s 1080p run cost **$10.23** (731k tokens × $0.014/1k ≈ 2,000 tokens per output frame). Cost scales with duration × fps × resolution, so it is not knowable in advance the way H3's is. Reach for it only if H3's motion quality genuinely fails the brief. `bytedance/seedance-2.0/fast/reference-to-video` caps at 720p for roughly a third less.
- `fal-ai/ltx-2.3/image-to-video/fast` — $0.04/s at 1080p, the budget floor. Single start image (+ optional `end_image_url`), so there is no multi-shot anchoring: you generate each shot as its own clip and hard-cut in ffmpeg, and you rewrite the shot script as one prompt per clip. Its audio is generated per clip, so for a multi-clip cut disable it and lay one continuous track underneath (`fal-ai/ace-step`, $0.0002/s). Use when synced audio does not matter. Note `fal-ai/ltx-2/*` was deprecated 15 Aug 2026 — always pin `2.3`.

**Prompt shape (all models):** numbered shots with explicit timestamps, one image anchor per shot, plus a one-line global style directive ("8-bit retro pixel-art, chunky pixels, limited palette, chiptune soundtrack").

- Auth: `Authorization: Key $FAL_KEY` header. Never hardcode the key; read from env.
- Poll `status_url` every 60–120s; a 15s clip takes several minutes.
- If the execution environment cannot reach fal.ai (egress allowlist), fall back to any authenticated surface with open network — e.g., drive the user's browser and call the API from a page context with the refs as data URIs.

### Step 4 — Deliver and verify
- Output is H.264/AAC MP4 — LinkedIn-ready as-is. If a mobile picker rejects it, the issue is almost always *where* it's saved (iOS: "Save Video" → Photos, not Files) rather than the codec. Verify by reading the container's fourCCs (`avc1`/`mp4a`) before assuming a transcode is needed.
- Always deliver the stylized stills alongside the video — they double as post images and future references.

## Guardrails
- IP: default to an ORIGINAL sprite character; only use a real brand mascot if the user explicitly confirms after being told the trademark risk.
- People: pixelation is not anonymization at 160-px grids for close-ups; get comfort from the user before featuring recognizable faces.
- Cost: confirm model, resolution and duration before generating. On H3 the bill is knowable up front — seconds × rate, plus $0.08 per reference beyond the fifth. On Seedance it is not: it bills tokens against output frames, and a 15s 1080p run measured **$10.23**. Never quote a Seedance price from its per-second rate card; that figure understated a real bill by 2.25×.
- Do all visual iteration locally on FLUX.2 Klein, where it is free. One paid generation off a storyboard the user has already approved beats three blind re-rolls — that discipline is worth more than any model choice.
# Purpose

Turn real event or product photographs into a short pixel-art recap whose visual treatment supports a clear story.

# When to Use

Use for retro recap videos, animated social assets, and image-led event or product narratives.

# Inputs

Approved source photos, event context, intended thesis, target duration, delivery format, and rights information.

# Outputs

A narrative arc, shot script, stylized assets, generated motion clips, final edit, and provenance record.

# Procedure

Follow the thesis, visual-language, stylization, shot-planning, generation, assembly, and verification workflow above.

# Quality Checklist

- [ ] Every shot supports the thesis rather than merely decorating it.
- [ ] People and important source details remain recognizable and respectful.
- [ ] The final video passes duration, frame, audio, and delivery checks.

# Edge Cases

When source coverage is thin, shorten the story or use clearly labelled connective graphics instead of inventing events.

# Safety Rules

Use only authorized photos, avoid altering identity or implying false actions, and remove private metadata and visible personal data.

# Examples

**Good:** A 15-second arc that turns three approved moments into a clear conclusion. **Bad:** Unrelated pixel transitions over every photo with no narrative.
