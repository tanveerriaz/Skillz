# OpenMontage: openmontage

Source: [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage).
Licence: [AGPL-3.0](https://github.com/calesthio/OpenMontage/blob/main/LICENSE) — copyleft. If you modify it and run it as a networked service, you must release the source.
This directory is an original Skillz adaptation distilled from the upstream README and skill description. It is not a copy of the upstream skill files, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream repo's documented behaviour: 12 YAML pipeline manifests, Markdown director skills, 52 tools, budget governance (cost estimate before execution, default $10 cap, ~$0.50 per-action approval threshold, decision log), and rendering via Remotion, HyperFrames, and FFmpeg. No upstream files, scripts, or assets are bundled here.

## Install and prerequisites

`git clone https://github.com/calesthio/OpenMontage.git` then `make setup`. Needs Python 3.10+, FFmpeg, and Node.js 18+.

## Caveats

- Scale at last check (2026-11-09): roughly 71k-77k stars, #1 GitHub trending, no tagged releases yet (v0.1.0 on the main branch).
- Tests are mocked in the repo; treat provider claims as integrations, not tested results.
- Cloud video-generation adapters (Kling, Veo, Runway, Sora, and others) cost real money. The zero-key path (Piper TTS, open footage, Remotion/HyperFrames) is free.
- AGPL-3.0 copyleft applies to the system itself; read the licence before building products on it.
