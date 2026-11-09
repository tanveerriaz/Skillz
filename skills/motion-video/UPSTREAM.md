# motion-video: motion-video

Source: [nxrskyaa/muse-motion-skills](https://github.com/nxrskyaa/muse-motion-skills).
Licence: [MIT](https://github.com/nxrskyaa/muse-motion-skills/blob/main/LICENSE).
This directory is an original Skillz adaptation distilled from the upstream README and skill description. It is not a copy of the upstream skill file, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream skill's documented behaviour: VO-first production playbook, 11 one-page style recipes (cinematic, pixel-rpg, editorial-paper, cut-paper, risograph, bauhaus, ukiyoe, schematic, noir-halftone, chalk-lecture, art-deco), Remotion templates, and locally synthesised SFX with numpy and ffmpeg. No upstream files, scripts, or assets are bundled here.

## Install and prerequisites

Clone the repo, then: `cd template && npm install && ./scripts/fonts.sh && python3 scripts/sfx.py`. Write `scripts/script.txt` as `ID|text` lines, run `./scripts/vo.sh`, then `npx remotion render src/index.ts Video out.mp4`. Needs Node 18+, ffmpeg, Python 3, and a `tts` command. Nothing else, no API keys.

## Caveats

- Only 6 stars, 25 commits, created 2026-10-11 — new and small.
- Its TTS interface was built against a `tts` CLI (Hatch tts skill). Swap in any equivalent TTS command.
- Zero paid APIs is a design rule of the skill, not a promise about any track you supply yourself.
