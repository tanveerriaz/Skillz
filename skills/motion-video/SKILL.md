---
name: motion-video
description: "Use when a 9:16 motion-graphic explainer must be narrated, kinetic, and never generic: the voiceover leads, the scenes follow, and the look comes from a library of 11 distinct styles, with zero paid APIs."
license: MIT
---

# Purpose

Teach an AI agent to make 9:16 motion-graphic explainer videos — narrated, kinetic, never generic. A full production playbook plus a library of visual styles and animation techniques, with zero paid APIs. The agent extracts the story, writes and voices the script, picks a visual identity from the style library, builds scenes from the template, designs sound, renders, checks its own frames, and hands over the MP4.

# When to Use

Use for narrated 9:16 explainers, social cuts, and launch explainers where the voiceover leads and the visuals follow. Use when every video must look different. Do not use for 16:9 longform or real-footage editing; this skill is built for vertical, narrated, code-drawn explainers.

# Inputs

The story or topic, the message, and the target length, plus the voice to use. The agent picks the style from the library; the user can also name one of the 11 styles directly.

# Outputs

A 9:16 MP4 with narration, kinetic type, and designed sound, built from a Remotion template. The 11 styles are each a one-page recipe — palette, type, texture, motion behaviour, and signature transition — with the rule "never ship two videos with the same look": cinematic, pixel-rpg, editorial-paper, cut-paper, risograph, bauhaus, ukiyoe, schematic, noir-halftone, chalk-lecture, art-deco.

# Procedure

1. Extract the story from the brief and write the script.
2. Voice the script first; timing is VO-first, scenes second.
3. Pick a visual identity from the style library and build the scenes from the template.
4. Design the sound: SFX are synthesised locally with numpy and ffmpeg, so no APIs or keys are needed.
5. Render, check the frames, fix what is wrong, and hand over the MP4.

# Quality Checklist

- [ ] The voiceover was recorded before the scenes were timed; no scene fights the narration.
- [ ] The chosen style is applied consistently: palette, type, texture, motion, and transition all match the recipe.
- [ ] The look differs from the last video made with this skill.
- [ ] Frames were checked after the render; defects were fixed.
- [ ] The MP4 is 9:16, plays end to end, and has audio.

# Edge Cases

- The skill is new and small: only 6 stars, 25 commits, created 2026-10-11. Treat its templates as a starting point and verify the render.
- Its TTS interface was built against a `tts` CLI (a Hatch tts skill). Swap in any equivalent TTS command; the interface is `tts speak --voice <id> --output <file> --text <text>`.
- Two starters are included: a cinematic starter (Remotion + React + TypeScript) and a pixel-RPG starter (hand-drawn sprites with chiptune included).

# Safety Rules

- Do not reuse a style recipe as a brand identity; the styles are looks, not logos.
- Do not ship music or SFX you have not cleared; the synthesised SFX are local, but any supplied track needs rights.
- Do not present generated footage as real product footage.

# Examples

Good: "Make a 45-second 9:16 explainer about how our pricing works, in the risograph style, narrated." The agent writes and voices the script, builds the scenes to the voice, and renders.

Bad: "Make an explainer in the same style as last time." The skill's rule is never to ship two videos with the same look; the agent must pick a different style or ask.

Practical starting prompt: "Use motion-video to make a [duration] 9:16 narrated explainer about [subject] in the [style] style. Voiceover first."
