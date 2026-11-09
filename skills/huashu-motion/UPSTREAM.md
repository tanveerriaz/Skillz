# huashu-motion

Source: [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion).
Licence: MIT for code and docs. Bundled GSAP and fonts keep their own licences; the author's cartoon character in the demos is not under MIT.
This directory is an original Skillz adaptation distilled from the upstream README and skill description. It is not a copy of the upstream skill file, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream skill's documented behaviour: one-line brief → three creative directions → single-file `index.html` film → ABC-notation score → click-to-fix editor → frame-by-frame render in local Chrome with FFmpeg. No upstream files, scripts, or assets are bundled here.

## Install and prerequisites

`npx skills add alchaincyf/huashu-motion`. Needs Node 22+, Chrome/Chromium/Edge, and FFmpeg; optional uv, Python 3.12, and whisper-cli.

## Caveats

- Only tested on macOS so far.
- Films of 4 seconds or longer end with a small "Made with huashu-motion" credit for the last 1.2 seconds unless switched off.
- Music and 23 SFX are generated locally with no paid API; the audio is described as CC0 or CC-BY instrument samples arranged by the skill. Verify the sample pack licence in the repo before commercial use.
- Popularity at last check (2026-11-09): roughly 1,900-2,005 stars.
