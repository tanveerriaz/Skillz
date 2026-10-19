# HyperFrames text edition: hyperframes-animation

Source: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes).
Pinned commit: [`cea0bad7931122bd93680006978c0d9007daa3d4`](https://github.com/heygen-com/hyperframes/commit/cea0bad7931122bd93680006978c0d9007daa3d4).
Source directory: [skills/hyperframes-animation](https://github.com/heygen-com/hyperframes/blob/cea0bad7931122bd93680006978c0d9007daa3d4/skills/hyperframes-animation).
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

Paths below are relative to `skills/hyperframes-animation/` in the pinned source. Hashes identify the original upstream bytes, before the documented edits. The only additional files here are this provenance file and the copied root `LICENSE`.

| Source file | Upstream SHA-256 |
| --- | --- |
| `SKILL.md` | `dfbbc2dc7907fa11fa3ae5bdb4f4c1fe7970c09f7c6e75248faf449bc67eb735` |
| `adapters/gsap.md` | `b713fb43561ae76358b915219e0d9992f85730c14c57ed08c4af8e1961ed5e89` |
| `adapters/gsap-easing-and-stagger.md` | `6e1c0e1c9a775d76415b6c3632224985141d7564be45e4a67475d855bc357b4e` |
| `adapters/gsap-timeline-and-labels.md` | `41263d8b42369a9799d7476e384acb59cce563672994c9f659eb3599e5042578` |
| `adapters/gsap-transforms-and-perf.md` | `8054f52890b7d780f508338cf906b3d74667b2ade9a8fc5c8f0a4a3807688613` |
| `rules/svg-path-draw.md` | `92eb6b9f1b5c22b1c64c7a649c35d1db0b7a3b65805dbe0acb1e79d3e5768839` |
| `rules/waterfall-entry.md` | `d9b8a3df6c59e0af6eef1f3f3d7ffb8058c8983976e4ce150566215770ff7c50` |
| `rules/press-release-spring.md` | `cce4096a827f5f7e8f643d95791865428df2de973289019243923de8789f0467` |

Upstream root `LICENSE` SHA-256: `4259155fb06f127687ee7b0a8a3682d45132db0f2da26cbc0b7a2d1e796436b8`.
