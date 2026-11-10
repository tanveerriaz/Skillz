---
name: video-shotcraft
description: "Use when a product promo must be built from your real pages, not generated footage: capture real screenshots, storyboard from a library of tuned shot recipes, animate in Remotion, cut to the beat, add sound design, and check every frame."
license: Apache-2.0
---

# Purpose

Make a cinematic product promo from your real screenshots. The agent inspects the product, captures real pages in a headless browser, picks shots from a library of tuned motion recipes, storyboards the film, animates it with Remotion, cuts it to the beat, adds sound design, checks every frame, and hands over a finished MP4 you can keep editing.

# When to Use

Use for product promos, launch films, and feature announcements where the product itself must be on screen. Use when every frame should be drawn by code from your own screenshots and copy. Do not use when the brief needs generated characters or footage you do not own; this skill is explicitly not a video generator.

# Inputs

The product URL or live pages, the message and call to action, the target duration, and the music or SFX direction. The agent captures full-page 2x textures and element crops itself; supply the pages, not screenshots, when possible.

# Outputs

An MP4 (1920x1080, 30fps, h264) with music and sound design, plus the full Remotion source, a Motion Workbench (CapCut-style browser editor) project, and an optional JianYing/CapCut draft export. The bundled template "Ink Press" is a 36.2-second, 10-shot film in a paper-ink-amber style with a pinned cinematic SFX pass.

# Procedure

1. Inspect the product read-only and capture real pages via headless browser (full-page 2x textures, element crops).
2. Write the product brief from what was captured, not from assumptions.
3. Storyboard from the shot recipe library: 124 recipe cards / 150 shots in 10 categories, distilled from official product films including ClickUp, Perplexity, Slack, Notion, Figma, Framer, Raycast, Superhuman, and Loom.
4. Build the Remotion project with each shot as a React component, using the reusable components (2.5D page camera, captions, flash cuts, digit rolls).
5. Sync the cut to the beat, add sound design with the Freesound SFX search/download tools, and run frame QA on every shot.
6. Render the MP4 and hand over the Motion Workbench project for further edits.

# Quality Checklist

- [ ] Every shot shows the real product; no placeholder UI or invented screens.
- [ ] The storyboard follows a recipe card per shot; no improvised camera moves.
- [ ] Cuts land on the beat; captions and digit rolls are legible at playback size.
- [ ] Every frame was checked; no clipped type, stretched textures, or dead frames.
- [ ] The Remotion source renders cleanly from a fresh checkout.

# Edge Cases

- The skill is Apache-2.0, but Remotion itself is free for individuals and small teams; companies may need a paid Remotion licence. Check before a company ships with it.
- The 149 bundled SFX assets and any Freesound downloads carry their own licences. Check those SFX licences before a commercial launch.
- A page that changes between capture and render invalidates its textures; re-capture before rendering if the product shipped in between.

# Safety Rules

- Do not present screenshots of a staging or mock environment as the live product.
- Do not use Freesound or bundled SFX commercially until their licences are checked.
- Do not invent product claims in the copy; every claim comes from the inspected product.

# Examples

Good: "Make a promo for my product." The agent captures the real pages, storyboards from the recipe cards, animates in Remotion, and delivers the MP4 plus the editable project.

Bad: "Make a promo that looks like the Loom film." The agent may borrow the recipe structure, not Loom's footage, wording, or brand.

Practical starting prompt: "Use video-shotcraft to make a [duration] promo for [product URL]. The message is [message]."
