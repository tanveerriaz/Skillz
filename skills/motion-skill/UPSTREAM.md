# Motion Skill: motion-skill

Source: [mrrajrumel/motion-skill](https://github.com/mrrajrumel/motion-skill).
Licence: [MIT](https://github.com/mrrajrumel/motion-skill/blob/main/LICENSE).
This directory is an original Skillz adaptation distilled from the upstream README and skill description. It is not a copy of the upstream skill file, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream skill's documented behaviour: 60fps one-shape motion clips with 4x subframe motion blur, speech-synced B-roll and transparent ProRes 4444 overlay panels, and local SAM 2 subject isolation with hardware-matched models. No upstream files, scripts, or assets are bundled here.

## Install and prerequisites

`git clone https://github.com/mrrajrumel/motion-skill.git ~/.claude/skills/motion` (or into `.claude/skills/motion` for one project); also works in Claude.ai Projects and Google Antigravity. Commands: `/motion`, `/motion b-roll`, `/motion panel`, `/motion separate`. Needs Python 3.10+ (numpy), ffmpeg with `prores_ks` for transparent panels, and Node.js 18+ (Playwright rendering).

## Caveats

- Only 2 stars, 5 commits, created 2026-10-08 — small and new, far less battle-tested than the bigger video skills. The capability is the outstanding part, not the adoption.
- SAM 2 model sizes: large ~898 MB (NVIDIA 12GB+ VRAM), base-plus ~323 MB (smaller GPU / Apple Silicon), tiny ~156 MB (CPU only, ~5s/frame).
