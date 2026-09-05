---
name: design-reference-imagegen
description: Use when an agent should generate design-reference images before implementing UI — one horizontal image per website section, one framed screen per mobile screen, or one brand-guidelines board — or turn a generated/reference image into faithful frontend code. Runs a brief → generate → analyze → implement → verify loop with a shared palette and anti-generic rules, loading only the reference file for the chosen surface (web, mobile, brand, image-to-code).
---

# Purpose

Produce design references that a developer or coding model can build from, then (optionally) build from them without drift. Image generators default to clichés: centered dark heroes, purple-blue gradients, card spam, tiny unreadable text, one compressed collage for a whole site. This skill forces one readable image per unit of UI, one consistent visual system across the set, and a disciplined analysis step before any code.

# When to Use

- A user asks for a landing page, marketing site, hero, or section concepts as images.
- A user asks for mobile app screens, an onboarding/auth/checkout flow, or a phone-mockup presentation.
- A user asks for a logo system, brand board, or identity deck image.
- A visually important web build should start from a generated reference and end in code that matches it.
- Do not use for bug fixes, purely structural refactors, or when the user already supplies a complete design system.

# Inputs

- Brief: product, audience, goal, tone. Style words ("minimal", "editorial", "fintech") steer the direction.
- Surface: web sections, mobile screens, or brand board. Infer it if not stated.
- Count: sections, screens, or board layout. Use the defaults in the reference file when unspecified.
- Optional: existing brand assets, reference images, target stack and viewports (image-to-code only).

# Outputs

- Web: one horizontal image per section, labeled "Section X of N: name".
- Mobile: one framed screen image per screen, forming a logical flow.
- Brand: one grid board image (default 3x3) plus the prompt used.
- Image-to-code: the images above, a short written analysis (text, type, spacing, colors, components), and code that matches them.

# Procedure

1. **Brief.** Infer surface, category, primary goal, and count. Commit to the count out loud ("Generating 6 images, one per section"). Do not ask follow-up questions if a strong interpretation exists.
2. **Choose the surface.** Web, mobile, or brand. If the task ends in code, it is image-to-code on top of web.
3. **Read only the matching reference file:** `references/web.md`, `references/mobile.md`, `references/brand.md`. For builds, also read `references/image-to-code.md`. Do not load the others.
4. **Lock the system before generating.** Pick one palette (primary, secondary, accent, neutral scale), one typography character, one theme, and the surface-specific choices the reference file lists. Write them down; every image reuses them.
5. **Generate ONE image per screen, section, or board.** Never combine units into a collage or a tall page. Vary composition across units; never vary identity. Use the prompt template in the reference file.
6. **Analyze each image.** Check readability, hierarchy, consistency with the locked system, and the anti-generic rules. If an image fails, regenerate it as a fresh standalone image — never crop or zoom an earlier one.
7. **Implement (image-to-code only).** Extract text, type scale, spacing, colors, and components from the images, then build to match. Invent only what the images leave ambiguous.
8. **Verify.** Run the Quality Checklist. Count images against the committed count; regenerate any missing unit. For code, compare the build side by side with the references and fix drift.

# Quality Checklist

- [ ] Image count equals the committed section/screen/board count.
- [ ] Every image is one unit only: one section, one screen, or one board.
- [ ] All images share one palette, one type family, one CTA/button family, one radius and image treatment.
- [ ] Text is readable at normal viewing size; nothing relies on tiny labels.
- [ ] Composition varies across units (no anchor repeated more than twice in a row).
- [ ] No AI tells: purple-blue gradients, blobs, glass stacks, fake dashboards, nested cards, filler pills.
- [ ] Copy is short and believable; no "unleash / elevate / seamless", no "Acme / NovaCore" wordmarks.
- [ ] First unit (hero, first screen, cover panel) is calm with one focal point and one clear action.
- [ ] Image-to-code: analysis written before code; build matches references in layout, spacing, type, and color.

# Edge Cases

- **Generator renders one image per call:** generate sequentially in the same response until the set is complete. Do not stop early or summarize instead.
- **Very long sets (12+):** generate in batches, restating the locked system at the start of each batch.
- **User supplies a design system or brand:** preserve its assets; use generation only to extend missing screens or present the system.
- **Image generation unavailable:** work from supplied references and say so. Never describe an image that was not produced.
- **Minimalist brief:** suspend "must include imagery/full-bleed" rules; restraint is the design.
- **Detail too small to read or extract:** generate a closer standalone render of that unit, not a crop.

# Safety Rules

- Do not copy protected logos, marks, interfaces, or slogans; use references for quality and rhythm only.
- Do not fabricate real account data, endorsements, testimonials attributed to real people, or approvals.
- Do not include personal information or confidential brand material in prompts or images.
- Do not present a generated image as a screenshot of a real product.
- Do not skip the analysis step and code from memory of "good taste" when images exist.
- Do not crop earlier images to stand in for a fresh render.

# Examples

**Good (web):** "8-section fintech site" → commits to 8, locks ink/paper/one accent, generates 8 horizontal images with varied anchors (hero bottom-left over image, stacked-center closing CTA), palette identical throughout.

**Good (mobile):** "onboarding for a social app" → 3–4 framed screens, distinct compositions, short copy, same device scale and margins, logical progression to a permissions or home screen.

**Good (image-to-code):** hero + 3 sections generated, headline/CTA text and spacing extracted in writing, then built; the coded hero still reads as the same design at laptop width.

**Bad:** one tall image containing eight illegible sections; four unrelated phone mockups in different design systems; a brand board with paragraphs of tiny fake copy; strong references followed by a generic coded template.
