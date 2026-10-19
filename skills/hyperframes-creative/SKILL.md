---
name: hyperframes-creative
description: Use when choosing visual direction for animated HTML or HTML video compositions. Guides subject-specific palettes, typography, frame hierarchy, layers, readable scale, and scene rhythm.
license: Apache-2.0
---

> Modified for Skillz: condensed and adapted from HeyGen HyperFrames at the source pin in [UPSTREAM.md](UPSTREAM.md). Copyright 2026 HeyGen, Inc.; [Apache-2.0](LICENSE).

# Purpose

Give animated HTML a deliberate visual identity through content, type, color, composition, and timing. Keep design decisions specific to the subject and requested medium.

# When to Use

Use for animated landing-page sections, HTML explainers, title cards, product mockups, and design-led video frames. This skill chooses the look; animation mechanics belong in `hyperframes-animation`, and video composition structure belongs in `hyperframes-core`.

# Inputs

The subject, audience, content, brand constraints, desired mood, and target medium. For video, also establish aspect ratio and duration. Read an existing `frame.md`, then `design.md`, then `DESIGN.md` when present; follow the user's current brief when it resolves a conflict.

# Outputs

A concise visual direction and HTML/CSS composition with intentional palette, type roles, focal hierarchy, and scene rhythm. This folder supplies instructions and references, not assets or rendering software.

# Procedure

1. Read [house-style.md](references/house-style.md) and [video-composition.md](references/video-composition.md) for substantial visual work. The references describe a video house style, not universal webpage rules. Apply responsive layout, usable text sizes, keyboard access, and reduced motion to browser HTML.
2. Interpret the prompt into concrete content. Use real supplied content or clearly synthetic examples; decorative UI must not invent product claims. Name the composition's main idea before decorating it.
3. Declare background, foreground, and accent colors. Preserve supplied brand colors. Question habitual gradient text, cyan-on-dark, identical cards, and centered equal-weight stacks. Use them only when they serve this concept.
4. Read [typography.md](references/typography.md). Assign display, body, and data/utility voices. Create purposeful contrast and verify actual font weights, glyph coverage, and licensing. Video font bundles described there exist only in the separate runtime; plain HTML needs its own font loading.
5. Compose the end state before animation. Choose background, content, and accent roles where the concept benefits from layers. Make the reading path clear. For video, test larger text, stronger structure, and encoding-safe backgrounds at the final viewing size. For web, keep the interface responsive and usable.
6. Read [motion-principles.md](references/motion-principles.md) for substantial motion. Plan build, reading time, and resolve. Vary ease, duration, direction, and rhythm with intent. A restrained brand or reduced-motion preference takes precedence over energetic house defaults and decorative quotas.
7. Implement only the requested scenes and content. Inspect still frames and playback; check hierarchy, clipping, contrast, font loading, timing, and final holds. In video mode, also use the core skill's runtime validation.

# Quality Checklist

- [ ] Palette and type choices fit this subject and brand.
- [ ] One clear reading path; details support the message.
- [ ] Text remains readable at the actual viewport or video playback size.
- [ ] Motion has purpose and leaves time to read.
- [ ] Browser HTML supports reduced motion and keyboard use where interactive.
- [ ] Screenshots/playback were inspected when available; any untested output is identified.

# Edge Cases

- A minimal logo sting, lower third, technical test, or intentionally sparse frame may need little decoration. Do not fill empty space mechanically.
- The references' font bans and numeric styling suggestions are house preferences. A user's brand, chosen typeface, language coverage, and actual medium take precedence.
- A video frame is fixed-size; a landing page must reflow. Do not transplant video-scale text, frame density, or perpetual ambient motion into a webpage without adapting it.

# Safety Rules

- Do not add narration, music, extra scenes, captions, or generated assets unless the request calls for them.
- Use approved public or synthetic content in reusable examples; keep private source material in its own project.
- Preserve asset licenses. This skill grants no rights to external fonts, trademarks, media, or animation libraries.
- Do not install runtimes or invoke omitted upstream scripts as part of choosing visual direction.

# Examples

Good: a warm editorial HTML explainer with one expressive display face, quiet body type, meaningful rules, and a staged SVG reveal.

Bad: an unrelated neon gradient, three identical feature cards, and the same entrance on every element regardless of content.

Practical starting prompt: "Use hyperframes-creative and hyperframes-animation to design a 10-second animated HTML product introduction. Deliver browser HTML and respect reduced motion." See [UPSTREAM.md](UPSTREAM.md) for the text-only scope and optional video runtime.
