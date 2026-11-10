---
name: huashu-motion
description: "Use when a one-line brief should become a 30-second product launch film: animated motion graphics in code, an original score composed in ABC notation from sampled instruments, and voiceover, with a click-to-fix editor for revisions."
license: MIT
---

# Purpose

Make a 30-second product launch film from a one-line brief, with no video-generation model. The agent offers three creative directions, builds the chosen film as code (GSAP, Canvas, Three.js, SVG in a single `index.html`), composes an original score in ABC notation played by sampled instruments, adds voiceover, and opens an in-browser editor where you click a frame and say what to change.

# When to Use

Use for product launch films, announcement cuts, and 30-second hero videos where the music must be original and the film must be revisable frame by frame. Use when the brief is one line and the deliverable is a finished film. Do not use for longform video or real-footage editing; this skill draws every frame in code.

# Inputs

One line describing the product, plus the product URL or site when available so the agent can ground the film in real copy and visuals. The agent offers three creative directions; the user picks one before the build starts.

# Outputs

An MP4 (also exportable as transparent MOV, WebM, GIF, or a share page) with composed music, SFX, and optional narration, plus the single-file `index.html` source and the ABC-notation score. Twelve starter templates are available when the brief fits one.

# Procedure

1. Point the agent at the product or site and read the brief.
2. Present three creative directions and wait for the user to pick one.
3. Build the whole film as code in a single `index.html` (GSAP, Canvas, Three.js, SVG).
4. Write the score in ABC notation and render it with sampled instruments; add the 23 locally generated SFX and the optional voiceover (macOS system voices, Kokoro, or the user's own recording).
5. Open the in-browser editor; the user clicks a frame and describes the change, and the agent edits the code.
6. Render frame by frame in local Chrome with FFmpeg and verify the final frames before delivery.

# Quality Checklist

- [ ] The film follows the chosen creative direction, not a generic template.
- [ ] Music, SFX, and voiceover sit at distinct levels; nothing masks the narration.
- [ ] The end credit, when present, is intentional: films of 4 seconds or longer end with a small "Made with huashu-motion" credit for the last 1.2 seconds unless switched off.
- [ ] Frames were inspected after the last edit; the render matches the editor preview.

# Edge Cases

- The skill is tested on macOS so far; other platforms are untested, so verify the render path before promising delivery on them.
- The bundled GSAP and fonts keep their own licences, and the author's cartoon character in the demos is not under MIT. Only the code and docs are MIT.
- The audio is described as CC0 or CC-BY instrument samples arranged by the skill. Verify the sample pack licence in the repo before commercial use.

# Safety Rules

- Do not present the demo character or any bundled asset as your own brand character.
- Do not ship the film commercially until the sample pack licence is confirmed for the tracks used.
- Do not bake a commercial trending song into the film; the score is composed for the film.

# Examples

Good: "Make a 30-second launch film for my note-taking app." The agent offers three directions, builds the chosen one with its own score, and lets you click a frame to fix a line of copy.

Bad: "Make a 5-minute documentary." The skill is built for 30-second launch films; longform needs a different pipeline.

Practical starting prompt: "Use huashu-motion to make a 30-second launch film for [product]. Offer three creative directions first."
