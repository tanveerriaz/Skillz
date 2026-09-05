# Image-to-Code Reference: From Generated Reference to Faithful Frontend

Read this when the task ends in code. It sits on top of `web.md` (generation rules) and adds the analysis and implementation discipline. The images are the design source; the code is the translation layer.

## 1. When Image-First Is Mandatory

Generate references before writing any layout code when the request is mainly visual: a beautiful hero, premium landing page, creative site, redesign, "more modern / more aesthetic" interface, marketing page, portfolio, multi-section concept, or anything described in visual terms.

Code-first is acceptable only when the task is mostly technical (bug fix, structural refactor), or the user already supplies a precise design system.

If image generation is unavailable, use the user's references and say so. Never code "from taste" while claiming an image basis.

## 2. Generation Rules Specific to Extraction

Follow `web.md` for composition and system choices, plus:

- One large image per section. Never compress several sections into one board — text, buttons, and spacing become unanalyzable.
- One complex section = one primary image + optional detail images (closer hero for headline/CTA/type; pricing cards; testimonials; navbar; feature cards; footer; a typography-and-spacing-only render).
- Unclear section = regenerate as a fresh standalone image with the same palette, type mood, button style, radius, and image treatment, but larger text, clearer spacing, cleaner structure. It is the same design, rendered for analysis.
- Never crop, zoom, or slice an earlier image to stand in for a section or detail. Crops distort spacing, type scale, margins, and proportions.
- More clear images beat fewer compressed ones. Generate an extra image rather than guess.

## 3. Website-Specific Design Constraints

These apply to both the generated images and the code.

**Hero and first view**
- Headline 1 line ideal, 2 good, 3 maximum. Reduce words rather than add lines.
- One focal point; obvious hierarchy; visible primary CTA; key visual; nothing else competing.
- Must read cleanly at a small laptop viewport (about 1280–1440 px wide, 700–800 px tall) without scrolling to find the CTA.
- No pills, fake stats, badge rows, logo strips, or pseudo-system labels ("00 orchestration layer", runtime markers, status chips) in the first screen.

**Anti-nested-box**
- No giant rounded wrapper around a whole section; no cards inside cards inside cards; no dashboard compartments without purpose.
- Use one framing move per section at most. Prefer open layouts, whitespace, and direct alignment.

**Micro-UI clutter**
- Remove decorative pills, filler chips, tiny badges, code-like tags, metadata rows, and pseudo-enterprise microcopy unless they carry real meaning. Prefer cleaner headings, fewer labels, stronger type.

**Media frames**
- Site imagery sits in fixed-aspect, repeatable modules with consistent radius (bounded hero frame, editorial crops at repeatable ratios, uniform card images, controlled gallery ratios). Multiple image moments across the site when the content supports them; all in one visual world.

## 4. Analysis Standard

Treat each image as a design specification. Analyze every section image in writing before coding. Do not skip from image to code on vibe.

For each section, record:

| Area | Extract |
|---|---|
| Identity | what the section is; its visual priority; its job |
| Text | headline, subheadline, CTA labels, section titles, pricing labels, feature names, nav and footer labels, testimonial names/roles if legible |
| Typography | size and weight relationships, line count, line-height feel, tracking feel, serif vs sans roles, display vs body contrast, heading rhythm, CTA text scale, calm vs aggressive |
| Spacing | headline→sub distance, text→button distance, card gaps, section top/bottom padding, side gutters, card padding, image→text distance, navbar spacing, overall cadence |
| Buttons and components | size, shape, radius, fill vs outline, icon use, primary vs secondary hierarchy, card structure, dividers, borders, shadows, inputs |
| Color | background, panel colors, accents, button fills, text hierarchy colors, border logic, shadow mood, image tint/grade, gradient intensity |
| Layout | grid logic, alignment, section ordering, density, repeated motifs, image treatment |
| Gaps | anything still unclear → generate a detail image before coding |

Goal: faithful spacing and type logic, not pixel OCR. If text or components are too small to read reliably, generate a closer image; do not guess.

## 5. Implementation Discipline

Build to match, not to be "inspired by."

Preserve: layout logic, spacing rhythm, section order, text/image balance, typography mood, component style, color logic, visual cleanliness, extracted copy.

Do not: simplify into a default template; replace distinctive sections with generic rows; compress generous spacing; flatten type into a stock hierarchy; swap the palette for default web colors; merge sections into repeated patterns absent from the images; reintroduce nested boxes or micro-clutter removed during analysis.

**Resolving missing detail** — in this order:
1. Preserve the visible design language.
2. Preserve layout and spacing logic.
3. Preserve the component family.
4. Preserve mood and polish level.
5. Generate a detail image.
6. Regenerate the section as a fresh standalone image.
7. Only then choose the most implementation-friendly faithful option.

**Responsive intent** — the images are desktop comps; implement so the hero and CTA remain visible at small laptop size, media frames keep their ratios, and stacking order on narrow widths follows the reading order visible in the image.

**Non-visual requirements** — verify functionality and accessibility (semantic structure, contrast, focus states, alt text, touch targets) separately from visual fidelity. Matching the picture does not prove the page works.

## 6. Workflow

1. Infer site type and section count (defaults in `web.md`); commit to the count.
2. Lock the visual system (`web.md` §3) and generate one image per section.
3. Generate detail or extraction images where text or components are small.
4. Regenerate unclear sections as fresh standalone images.
5. Write the analysis for every image using the §4 table.
6. Extract text, type, spacing, colors, buttons, components, and layout into a short spec.
7. Implement to match; invent only where the images are ambiguous, following §5 order.
8. Compare the build with the references side by side; fix drift; run the checklist.
9. Create final files only after the analysis pass is complete.

## 7. Prompt Additions (append to the `web.md` section template)

```
Rendered for analysis: text large and fully legible, buttons clearly inspectable, spacing visible, one section only.
No nested cards, no rounded section wrapper, no pills or status labels, no pseudo-system microcopy.
Hero headline max 3 lines; first view balanced for a small laptop.
```

For a detail image:

```
Detail render of [section] from the same design: same palette, type, button style, radius, and image treatment.
Focus on [headline + CTA | pricing cards | navbar | typography and spacing]. Larger text, clearer spacing, cleaner structure. Not a new design.
```

## 8. Image-to-Code Checklist

- [ ] References generated first; no layout code written before analysis.
- [ ] One image per section; extra detail images where needed; no crops of earlier renders.
- [ ] Written analysis exists for every image (text, type, spacing, buttons, color, layout, gaps).
- [ ] Hero headline ≤ 3 lines; first view clean at small laptop size.
- [ ] No nested-box wrappers; micro-UI clutter removed.
- [ ] Code preserves layout, spacing, type, color, and copy from the references.
- [ ] Build compared side by side with references; drift fixed.
- [ ] Media modules keep fixed ratios and consistent radius.
- [ ] Functional and accessibility checks passed independently of visual match.

## 9. Example Interpretations

- **"One hero for an AI startup"** → 1 hero image; if headline or buttons are small, 1 closer extraction render; analyze headline, sub, CTA, spacing, colors, media; implement the hero; check it at laptop width.
- **"8-section landing page"** → 8 section images plus detail renders where needed; analysis for all 8; regenerate any unclear section rather than cropping; sections open, not boxed; implement the full site from the references.
- **"Creative agency site, 4 sections"** → 4 images; very clean hero; readable text; per-section analysis; no cutouts from first renders; no pill microcopy or container overload; build from the 4 references.
