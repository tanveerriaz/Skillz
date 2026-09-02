---
name: cinematic-minimal-web
description: Build premium, restrained, presentation-style websites with exceptional typography, graphics and subtle motion.
---

# Visual direction

Design websites as interactive editorial presentations, not collections
of UI components.

Prioritize:
- typography
- negative space
- composition
- art direction
- hierarchy
- extremely restrained motion

Avoid:
- generic SaaS layouts
- card grids unless functionally necessary
- gradient-heavy AI aesthetics
- excessive shadows
- glassmorphism
- decorative pills
- unnecessary icons
- large animated movements
- bouncing or theatrical effects

# Layout

Treat major sections as scenes.

Prefer 100svh compositions where appropriate.

Use a deliberate grid.
Allow controlled asymmetry and edge bleeding.

Use generous negative space.

One scene should normally communicate one major idea.

# Typography

Use one high-quality grotesk/display family where appropriate.

Display headlines:
- clamp-based sizing
- line-height: 0.88–1.0
- negative letter spacing
- deliberate line breaks
- selective italic emphasis

Typography should often serve as the primary graphic element.

# Color

Use a dominant base color, primary text color,
and at most one strong accent unless the concept requires otherwise.

Avoid timid multi-color palettes.

# Motion

Default animation:
opacity 0 → 1
translateY 12–20px → 0
scale 0.985 → 1 where appropriate

Typical duration:
550–800ms

Preferred ease:
cubic-bezier(0.22, 1, 0.36, 1)

Stagger related elements by 50–100ms.

Motion should reinforce hierarchy, never become the subject.

Use transform and opacity whenever possible.

Respect prefers-reduced-motion.

# Images

Art-direct every important image.

Explicitly control:
- crop
- aspect ratio
- object-position
- scale
- bleed
- visual focal point

Prefer SVG for logos and illustrations.
Use high-resolution WebP/AVIF for photography.

# Interaction

Prefer native scrolling and CSS scroll snap.

Use Motion for entrances, exits and micro-interactions.

Use GSAP/ScrollTrigger only when the storytelling genuinely
requires pinned or scrubbed timelines.

# Quality gate

Before finishing, ask:

1. Can anything be removed?
2. Is the hierarchy obvious without animation?
3. Is every animation smaller than necessary rather than larger?
4. Does every image have an intentional crop?
5. Are the line breaks deliberately designed?
6. Does this look like a designer made decisions, rather than
   an AI assembled components?
# Purpose

Build restrained editorial websites whose typography, graphics, and motion feel like one directed presentation.

# When to Use

Use for premium landing pages, portfolios, narrative product pages, and presentation-style web experiences.

# Inputs

Real content, audience, page goal, brand constraints, available imagery, and technical stack.

# Outputs

A responsive implementation with strong hierarchy, purposeful graphics, and subtle motion.

# Procedure

Follow the visual direction and implementation guidance above, choosing only patterns that support the page's thesis.

# Quality Checklist

- [ ] Typography carries the hierarchy without decorative clutter.
- [ ] Motion has a narrative or interaction purpose.
- [ ] Desktop, mobile, keyboard, and reduced-motion behavior are verified.

# Edge Cases

For dense product applications, retain the typographic discipline but reduce cinematic sequencing around repeated tasks.

# Safety Rules

Do not sacrifice readability, accessibility, performance, or truthful content for spectacle.

# Examples

**Good:** A quiet product narrative with one controlled reveal and crisp responsive type. **Bad:** A generic dark template covered in glows and scroll effects.
