# Motion Video Director: motion-video-director

Source: [Miftahul-Islam-Efaz/Motion-graphics-skill](https://github.com/Miftahul-Islam-Efaz/Motion-graphics-skill) (skill `motion-video-director`).
Licence: **not stated as MIT/Apache in the listing checked 2026-11-09; the skill folder carries its own LICENSE.md.** Check that file before commercial reuse. Do not assume a licence.
Note: an earlier listing named this repo under the author `mattypark`; that was wrong. The repo is `Miftahul-Islam-Efaz/Motion-graphics-skill`.
This directory is an original Skillz adaptation distilled from the upstream README and skill description. It is not a copy of the upstream skill file, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream skill's documented behaviour: approval-gated workflow (brief → ElevenLabs voiceover script with faster-whisper word timing → storyboard timed to the words → build → contact-sheet preview → render and mix to -14 LUFS), plus code-drawn motion graphics and real-footage editing (cuts, punch zooms, B-roll, text behind the subject, speed ramps, RVM/SAM2 cutouts). No upstream files, scripts, or assets are bundled here.

## Why this skill is marked draft

Its marketplace status is `draft` because no licence was stated in the listing. The flag is prominent in both `SKILL.md` and this file. Read the skill folder's LICENSE.md; if it confirms a usable licence, update both files and promote the status to `stable`.

## Install and prerequisites

`npx skills add Miftahul-Islam-Efaz/Motion-graphics-skill`, or the Claude Code plugin: `/plugin marketplace add Miftahul-Islam-Efaz/Motion-graphics-skill` then `/plugin install motion-video-director@motion-graphics-skill`. Needs Python 3.10+, FFmpeg/ffprobe, and Node 18+ with Playwright/Chromium for browser rendering. Optional: faster-whisper, rembg, demucs.

## Caveats

- Version at last check: v3.5.2, 139 stars, 22 forks (2026-11-09).
- A SkillsLLM automated scan passed with no high-severity issues but flagged two medium "secret-exfiltration" items (upstream SKILL.md lines 130/135, about credentials to an external endpoint). Review its `.env` / credential handling before entering API keys.
