# HyperFrames text edition: hyperframes-core

Source: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes).
Pinned commit: [`cea0bad7931122bd93680006978c0d9007daa3d4`](https://github.com/heygen-com/hyperframes/commit/cea0bad7931122bd93680006978c0d9007daa3d4).
Source directory: [skills/hyperframes-core](https://github.com/heygen-com/hyperframes/blob/cea0bad7931122bd93680006978c0d9007daa3d4/skills/hyperframes-core).
Copyright 2026 HeyGen, Inc. Distributed under [Apache License 2.0](LICENSE).
This directory is a third-party exception to Skillz's root MIT license. It is an independent text adaptation, not an official HeyGen release or endorsement.

## What changed

`SKILL.md` was condensed and adapted to the Skillz section format, the retained references, and explicit browser-HTML versus optional-video modes. Plugin setup, auto-update/install, workflow routing, media generation, and bundled-script instructions were removed. Safety and verification instructions were scoped to the requested work.

Retained references carry modification notices. Links to omitted documents were changed to pinned upstream URLs where resolvable; these are optional reading, not bundled features. Typography's font-discovery script was removed. The minimal skeleton uses system fonts and explicit tween endpoints. Root-sizing and clip-visibility wording were aligned with the core contract; GSAP examples were adjusted to use timeline-owned motion where relevant. Internal skills, examples, scripts, runtime code, fonts, media, and package files are excluded.

`LICENSE` is an exact copy of the upstream root license at the pin. No upstream `NOTICE` file exists in that pinned tree. Attribution from the copied material is retained. Upstream [CREDITS.md](https://github.com/heygen-com/hyperframes/blob/cea0bad7931122bd93680006978c0d9007daa3d4/CREDITS.md) credits prior browser-video work and runtime dependencies; those runtime implementations and third-party assets are not redistributed here.

## Use without the full framework

Copy this whole skill folder (including references, LICENSE, and this file) into the consuming agent's project-local skill directory, or reference its `SKILL.md` directly. Load `hyperframes-creative` for visual direction and `hyperframes-animation` for GSAP motion; load `hyperframes-core` when producing HyperFrames-compatible video HTML. Each entrypoint names its prerequisites; copying just `SKILL.md` loses its supporting references.

For browser HTML, use a modern browser, ordinary CSS layout, and your own approved GSAP dependency if using GSAP recipes. Set stage dimensions and start/control the timeline yourself. Respect reduced motion. The `data-*` timing contract, `window.__hyperframes` helpers, font bundle, and paused-timeline registry require HyperFrames and do not run themselves in a browser.

Video export is optional and requires the separate HyperFrames CLI/runtime, Node.js 22+, Chrome/headless browser support, and FFmpeg. The source pin declares CLI version `0.8.174`; the skills pin is not a runtime installation or dependency lock. Set up an appropriate runtime deliberately in the output project, verify its version and prerequisites with `hyperframes doctor`, then use `hyperframes lint`, `hyperframes check`, representative `hyperframes snapshot --at 2` captures, and `hyperframes render` when video is requested. CLI commands here assume the runtime is already available. No runtime was installed or executed to publish these skills.

GSAP 3.14.2 is the example adapter version. GSAP, fonts, media, and other external dependencies retain their own licenses; this text-only distribution does not supply or relicense them. Network loading shown in snippets is illustrative; use approved local assets for offline deterministic export.

## Source inventory

Paths below are relative to `skills/hyperframes-core/` in the pinned source. Hashes identify the original upstream bytes, before the documented edits. The only additional files here are this provenance file and the copied root `LICENSE`.

| Source file | Upstream SHA-256 |
| --- | --- |
| `SKILL.md` | `a8d6fe52471be6bcf1816ba0b9eb16c6d1efc830c668de533d6bee8d41d86e11` |
| `references/minimal-composition.md` | `0884abd9feeeea48d0de3d517c3d074859b9c322318401a928b9d1f9ee2cf851` |
| `references/data-attributes.md` | `9da0123bbd9508c32b3ea11bf6ab8edbf4fd725ab35d51cce735a6b03f3b4a96` |
| `references/determinism-rules.md` | `415a3f08cf3be801e6ca381fd47959e787947da325a7ee30b8104b8b80198fd5` |
| `references/sub-compositions.md` | `7caf63046ea0d1915b51e4eb49897101e36dc716ea1195f9a34cef4ba9c18f64` |
| `references/variables-and-media.md` | `d905b18425dfbbcf232aa9557708425bdf4b52c13f999093e04c9f7f1428d6a1` |

Upstream root `LICENSE` SHA-256: `4259155fb06f127687ee7b0a8a3682d45132db0f2da26cbc0b7a2d1e796436b8`.
