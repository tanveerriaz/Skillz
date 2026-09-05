# Scroll-Page Variant: Editorial System on a Scrolling Landing Page

Read this when the brief asks for a website rather than a slide deck but wants the same restrained editorial character: typography as the graphic, generous negative space, one idea at a time, motion that reinforces hierarchy instead of performing. The deck's design system (palette, type, spacing discipline) carries over unchanged; only the container changes from slides to scroll.

## 1. Scenes instead of slides

- Treat each major section as a scene. One scene communicates one major idea, the same rule as one slide, one point.
- Prefer `min-height: 100svh` compositions for the hero and for scenes that carry a single statement or image. Use `svh` rather than `vh` so mobile browser chrome does not clip the composition.
- Content-heavy scenes (a short list, a pair of images) may run longer than a viewport; never force them to fit by shrinking type.
- Use a deliberate grid with controlled asymmetry and edge bleeding. Allow an image or headline to bleed off one edge when it strengthens the composition; never bleed on both sides.
- Optional: `scroll-snap-type: y proximity` on the page when most scenes are exactly one viewport. Skip snapping when scene heights vary; forced snap on uneven scenes feels broken.
- Keep the section count low. A landing page here is usually 5-8 scenes: hero, thesis, two to four supporting scenes, proof, call to action.

## 2. Typography

- One high-quality grotesk or display family. Weights and italic carry hierarchy; do not add a second family for emphasis.
- Display headlines: `clamp()`-based sizing, line-height 0.88-1.0, negative letter-spacing, deliberately placed line breaks, selective italic emphasis in the same family.
- Typography is often the primary graphic element. A scene can be a headline and negative space and nothing else.
- Body copy: 65-character maximum measure, relaxed leading, secondary text color. Short paragraphs; most scenes need one.
- Design the line breaks. If a headline wraps differently at a breakpoint, adjust the `clamp()` range or insert a controlled break rather than accepting an orphan.
- Check italic descender clearance when line-height is below 1.1.

## 3. Negative space and color

- Generous space between scenes and within them. Section padding scales with the viewport (`clamp(4rem, 12vw, 10rem)`) and shrinks proportionally on mobile.
- One dominant base color, one primary text color, at most one strong accent. Avoid timid multi-color palettes; the deck palette applies as is.
- One theme for the whole page. Do not alternate dark and light scenes for variety.
- Avoid: card grids unless functionally necessary, gradient-heavy backgrounds, heavy shadows, glassmorphism, decorative pills, unnecessary icons.

## 4. Images

- Art-direct every important image: crop, aspect ratio, `object-position`, scale, bleed, and focal point are explicit decisions, not defaults.
- One strong image per scene at most. Let it hold a large area rather than tiling several small ones.
- SVG for logos and illustrations; high-resolution WebP or AVIF for photography, with reserved space to avoid layout shift.

## 5. Motion limits

Default entrance for any element:

- `opacity 0 → 1`
- `translateY 12-20px → 0`
- `scale 0.985 → 1` where appropriate
- Duration 550-800ms
- Easing `cubic-bezier(0.22, 1, 0.36, 1)`
- Stagger related elements by 50-100ms

Rules:

- Motion reinforces hierarchy; it is never the subject. Every animation should be smaller than feels necessary.
- Animate only `transform` and `opacity`.
- Prefer native scrolling. Use a motion library for entrances, exits, and micro-interactions only.
- Use pinned or scrubbed timelines (GSAP ScrollTrigger or equivalent) only when the storytelling genuinely requires a sequence; a single controlled reveal per page is usually enough.
- No bouncing, no theatrical or oversized movement, no infinite loops on informational content, no scroll cues.
- Respect `prefers-reduced-motion`: entrances become instant, scrubbed sequences show their final state.

## 6. Interaction

- Native scroll plus optional CSS scroll snap. No scroll hijacking, no smooth-scroll libraries that change scroll feel.
- Hover and focus states are quiet: an underline, a color shift, a 1px movement. Visible focus rings remain.
- Navigation is minimal: a wordmark and one or two links, or none until the final scene.
- Touch targets at least 44px; body text never below 1rem.

## 7. Quality gate

Before finishing, answer each question honestly:

1. Can anything be removed?
2. Is the hierarchy obvious with animation disabled?
3. Is every animation smaller than necessary rather than larger?
4. Does every image have an intentional crop and focal point?
5. Are the headline line breaks deliberately designed at every breakpoint?
6. Does the page look like a designer made decisions rather than an assembly of components?
7. Do desktop, mobile, keyboard, and reduced-motion all work?

## 8. Edge cases

- **Dense product application:** keep the typographic discipline; drop the one-scene-per-viewport structure and cinematic sequencing around repeated tasks.
- **Client requires many sections:** group them into fewer scenes with internal sub-structure rather than adding more full-height sections.
- **Portfolio with many projects:** the index is one scene with a restrained list; each project gets its own page rather than more scenes.

## 9. Examples

**Good:** A quiet product narrative: a 100svh hero of one headline and one art-directed photograph, one controlled reveal on the thesis scene, three supporting scenes with alternating bleed, crisp responsive type, no shadows.

**Bad:** A dark template covered in glows, parallax on every image, three-card feature grids, a bouncing scroll arrow, and headlines that wrap to orphans on tablet.
