---
name: hyperframes-core
description: Use when authoring HyperFrames HTML compositions for optional video rendering. Covers data attributes, clip timing, sub-compositions, variables, media, and deterministic seekable timelines.
license: Apache-2.0
---

> Modified for Skillz: condensed and adapted from HeyGen HyperFrames at the source pin in [UPSTREAM.md](UPSTREAM.md). Copyright 2026 HeyGen, Inc.; [Apache-2.0](LICENSE).

# Purpose

Build renderable HTML compositions with explicit frame dimensions, timed clips, and seekable animation. This is a text-only skill; the HyperFrames runtime is separate.

# When to Use

Use before writing or editing HyperFrames composition HTML. For browser-only animated pages, use the creative and animation skills; browsers do not implement HyperFrames data attributes by themselves.

# Inputs

- The content, target dimensions, duration, and intended output (HTML or video).
- Existing composition files and approved local media, if any.
- A separately configured HyperFrames runtime when previewing or rendering video.

# Outputs

A composition HTML file, its required local assets, and an honest validation result. Deliver a video only when requested and the rendering runtime is available.

# Procedure

1. Read [minimal-composition.md](references/minimal-composition.md), [data-attributes.md](references/data-attributes.md), and [determinism-rules.md](references/determinism-rules.md). Write the visible end state in HTML/CSS first.
2. Give the top-level root `data-composition-id`, `data-width`, `data-height`, and an explicit finite `data-duration`. Keep it directly in `<body>`, outside `<template>`. Use `width: 100%; height: 100%`; the runtime applies the pixel dimensions.
3. Give visible timed elements `class="clip"`, stable IDs, `data-start`, and `data-duration`. The visibility window is `[start, start + duration)`, so resolve important motion before its final frame. Track indices are editor lanes; use CSS stacking for visual layers.
4. Register exactly one completed, paused GSAP timeline per composition on `window.__timelines["<composition-id>"]`. The key matches the root ID. Build after fonts/layout are ready, then register. Let HyperFrames seek it; do not call `.play()` in video mode. Prefer explicit `fromTo` endpoints and compute geometry once during setup.
5. Center with flex/grid or `xPercent`/`yPercent`. Avoid combining CSS initial transforms with GSAP transforms on the same property. Animate inner wrappers rather than taking over a timed clip's `display`, `visibility`, or `autoAlpha`.
6. For modular scenes, read [sub-compositions.md](references/sub-compositions.md): styles and scripts belong inside the sub-composition `<template>`. Match host ID, inner composition ID, and timeline registry key. Do not manually add a sub-composition timeline to its host.
7. For variables or media, read [variables-and-media.md](references/variables-and-media.md). Give audio/video unique IDs; use real local fallback sources. The framework owns media playback. Time a video or its plain wrapper, never both. Keep video sound with `data-has-audio="true"`, or use `muted` for silent footage.
8. If the separate CLI is available, run `hyperframes lint`, then `hyperframes check`. Inspect snapshots at scene midpoints and boundaries. After lint errors, zero sampled layout/contrast checks mean validation did not run. Render with `hyperframes render` when the requested deliverable includes video; inspect the resulting file.

# Quality Checklist

- [ ] Root dimensions, finite duration, and timeline key agree.
- [ ] Clip windows contain their animations and important end states have reading time.
- [ ] Same timestamp produces the same frame after forward and backward seeks.
- [ ] Text fits; fonts and media resolve locally for rendering.
- [ ] Lint, browser checks, and representative snapshots were inspected, or the missing runtime is explicitly reported.

# Edge Cases

- A static root duration is read at compile time; changing it later in JavaScript does not extend the render. A shorter timeline holds its final state until the root duration ends.
- For HDR or shader transitions, put the background on a full-bleed child because layered compositing may force composition roots transparent.
- Source references occasionally discuss other adapters or advanced editing. Those optional documents link to the pinned upstream and are not bundled tooling.

# Safety Rules

- Do not add clocks, unseeded randomness, live input state, or render-time network fetches to rendered visual state.
- Do not silently install, update, or globally install HyperFrames, skills, fonts, or helper packages. Runtime setup is a separate user-directed step.
- Use only approved assets and preserve their licenses. Do not put recordings, credentials, private captures, or personal material in reusable skill folders.
- Do not claim preview or render success from static HTML inspection alone.

# Examples

Good: a five-second title card with one paused timeline, a title entrance on an inner element, local licensed assets, and a readable final hold.

Bad: a title driven by `setInterval`, a mismatched timeline key, and media fetched during each render frame.

For a complete starting document, use [minimal-composition.md](references/minimal-composition.md). For runtime requirements and source attribution, read [UPSTREAM.md](UPSTREAM.md).
