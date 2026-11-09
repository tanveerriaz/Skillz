# Agentic Motion Graphics: agentic-motion-graphics

Source: [siyuanfeng636-cpu/agentic-motion-graphics](https://github.com/siyuanfeng636-cpu/agentic-motion-graphics) (SKILL.md at the repo root).
Licence: **not stated on the upstream SKILL.md page.** No licence was found in the listing checked 2026-11-09. Do not assume MIT or Apache.
This directory is an original Skillz adaptation distilled from the upstream skill description. It is not a copy of the upstream skill file, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream skill's documented six-step pipeline: reference contact-sheet → `scripts/script.json` → TTS → Whisper forced alignment → GSAP timeline tied to `timing.json` → lint / snapshot / render / QA. No upstream files, scripts, or assets are bundled here.

## Why this skill is marked draft

Its marketplace status is `draft` because the upstream licence is not stated. The flag is prominent in both `SKILL.md` and this file. Verify the upstream licence before commercial reuse; if the upstream adds a licence, update both files and promote the status to `stable`.

## Install and prerequisites

Follow the install steps in the upstream repo. Needs Node.js v22+, HyperFrames CLI (`npx hyperframes@0.8.71` in the upstream docs), ffmpeg, Python 3, `whisper.cpp` or `faster-whisper`, OpenAI TTS or ElevenLabs, and numpy/scipy for synthesised SFX.

## Caveats

- The pipeline depends on HyperFrames; the composition contract and runtime validation live in the repo's `hyperframes-core` skill.
- QA is only as good as the snapshot inspection; the loudness, duration, and black-frame checks are automated, the visual judgement is not.
