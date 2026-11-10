---
name: motion-studio
description: "Use when one prompt should become a finished motion-graphics video: a promo, explainer, or launch cut built from HTML/CSS/Three.js scenes, with voiceover, captions, and a mixed soundtrack, without opening After Effects or Premiere."
license: MIT
---

# Purpose

Turn a single prompt into a finished motion-graphics video. The agent acts as motion designer, editor, and sound mixer: it writes the script and storyboard, renders HTML/CSS/Three.js scenes frame by frame in headless Chromium, adds voiceover and a music/SFX mix, and delivers a loudness-normalised MP4.

# When to Use

Use for 30-second promos, product explainers, and launch cuts in 9:16, 16:9, 1:1, or 4:5. Use when the brief is one sentence and the deliverable is a finished video, not an editable timeline. Do not use when the job needs real camera footage or frame-accurate editing of existing clips; this skill draws every frame in code.

# Inputs

One prompt describing the product, the audience, the message, and the call to action, plus optional brand colours, aspect ratio, duration, and an owned music track. The agent derives the script, scene list, and `storyboard.json` from the prompt; no timeline file or editor project is supplied.

# Outputs

A 1080p MP4 with word-synced captions burned in plus an `.srt` file, a music bed ducked under the voice, and SFX. The pipeline is `storyboard.json -> tts.py -> plan.py -> render.mjs -> video.mp4`, with `sfx.py` and `mix.py` for the sound pass. The mix targets -14 LUFS.

# Procedure

1. Expand the prompt into a script and a `storyboard.json` of timed scenes.
2. Generate preview stills of the scenes and confirm the look before rendering.
3. Generate the voiceover with ElevenLabs, free Microsoft neural voices (edge-tts), Piper (offline), macOS `say`, or espeak.
4. Build the timeline plan, then render scenes frame by frame in headless Chromium.
5. Add synthesised, copyright-free SFX (whooshes, pops, risers, clicks) and a music bed, ducking the bed under the voice.
6. Mix and loudness-normalise to -14 LUFS, then verify duration, audio presence, and final frames before delivery.

# Quality Checklist

- [ ] Every scene matches the script beat it illustrates; no filler scenes.
- [ ] Kinetic type is readable at the final playback size; captions sync word by word.
- [ ] Transitions (push, whip, zoom, iris, wipe, blur) and camera moves (drift, orbit, tilt, pan) serve the message, not the demo reel.
- [ ] Music ducks under the voice; the mix measures -14 LUFS.
- [ ] The MP4 plays end to end with audio; duration matches the brief.

# Edge Cases

- A supplied music track is used only as `"music": {"file": "assets/track.mp3"}`. Use tracks you have the rights to; the skill ships no cleared commercial music.
- Counters, lists, before/after frames, terminal typing, and screenshots in device frames are built-in scene types; real-time 3D (Three.js) scenes cost more render time than flat scenes.
- If a preview still looks wrong, fix the storyboard and re-preview; do not patch the rendered video.

# Safety Rules

- Do not bake a commercial trending song into a video. Use a track you own or that is cleared for commercial use, and keep its credit with the video.
- Do not present generated footage as real product footage or real customer results.
- Do not install or run tools beyond the stated prerequisites without the user's approval.

# Examples

Good: "Make a 30-second vertical promo video for my app Plantly: it reminds you to water plants. Use green colors and end with 'Download free'." The agent storyboards the watering reminder, renders the scenes, voices the script, and delivers the MP4.

Bad: "Make a video about my app" with no product, audience, or call to action. The agent must ask for the missing brief instead of inventing product claims.

Practical starting prompt: "Use motion-studio to make a 30-second vertical promo for [product]. The message is [message] and the call to action is [CTA]."
