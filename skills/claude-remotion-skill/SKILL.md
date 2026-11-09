---
name: claude-remotion-skill
description: Use when building or editing professional motion-graphics videos with Remotion (React + TypeScript): springs, staggered choreography, colour grades, film grain, Ken Burns, word-synced captions, and sound design, from a single prompt.
license: MIT
---

# Purpose

Teach Claude Code, Claude Desktop, or Claude AI to create and edit professional motion-graphics videos with Remotion (React + TypeScript). The skill encodes motion-design craft as rules, not recipes: springs, staggered choreography, colour grades, film grain, Ken Burns, word-synced captions, and sound design, from a single prompt.

# When to Use

Use for AI video editing, B-roll, captions, and sound design in Remotion, and for any Remotion video where the motion must look professional rather than merely move. Use when standardising on Remotion; the HyperFrames counterpart in this repo is `hyperframes-core`. Do not use for HTML-to-MP4 work; that contract belongs to HyperFrames.

# Inputs

One prompt describing the video, the message, the audience, and the look, plus any brand colours, fonts, and reference material. The agent also needs the Remotion project or a blank one to work in.

# Outputs

A Remotion project (React + TypeScript) and a rendered MP4, with the render → inspect frames → fix → re-render loop completed at least once. Captions are word-synced; sound design is part of the deliverable, not an afterthought.

# Procedure

1. Read the brief and confirm the format, duration, and look.
2. Build the composition with the skill's motion rules: springs for natural movement, staggered choreography for grouped elements, colour grades and film grain for finish, Ken Burns for stills.
3. Add word-synced captions and sound design.
4. Render, inspect the frames, fix what is wrong, and re-render. This loop is mandatory, not optional.
5. Verify the final render end to end before delivery.

# Quality Checklist

- [ ] Motion follows the skill's rules: no linear slides, no identical entrances, no unreadable speed.
- [ ] Captions sync to the spoken words.
- [ ] Colour grade and grain are consistent across scenes.
- [ ] Frames were inspected after the last render; defects found were fixed and re-rendered.
- [ ] The video plays end to end with audio at the requested format and duration.

# Edge Cases

- The core idea, from the upstream repo: "Remotion is never the bottleneck — motion-design craft is." A weak video in Remotion is a craft failure, not a tool failure; fix the motion, not the renderer.
- A composition that renders but was never frame-inspected is not finished. The loop is the skill.
- Remotion is free and open source; the skill also needs a Claude subscription or API access.

# Safety Rules

- Do not present generated footage as real product footage or real customer results.
- Do not ship music or SFX you have not cleared for the use.
- Do not skip the inspect step to save time; the loop exists because first renders are rarely right.

# Examples

Good: "Use the Remotion skill to make a 30-second product explainer with word-synced captions and a warm grade." The agent builds the composition, renders, inspects the frames, fixes the timing, and re-renders.

Bad: "Make a Remotion video" with no subject, message, or duration. The agent must ask for the brief first.

Practical starting prompt: "Use claude-remotion-skill to build a [duration] Remotion video about [subject]. Render, inspect the frames, fix, and re-render before delivery."
