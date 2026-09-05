# Pre-Flight Checklist

Run every item before delivering code. If a single box cannot be honestly ticked, the page is not done. Fix it first.

## Direction

- [ ] Design Read declared in one line before generating.
- [ ] Dial values explicit and reasoned from the brief, not silently the baseline.
- [ ] Design system chosen from `brief-and-dials.md` if applicable, or the aesthetic labelled honestly.
- [ ] Redesign mode detected and audit performed (if applicable).
- [ ] One design system per project (no Material + shadcn mixing).

## Typography and color

- [ ] Zero em-dashes (`—`) or en-dash separators (`–`) anywhere visible.
- [ ] Page theme lock: one theme (light, dark, or auto) for the whole page; no section inverts.
- [ ] Color consistency lock: one accent, used identically across all sections.
- [ ] Shape consistency lock: one corner-radius system.
- [ ] Serif discipline: no Fraunces or Instrument Serif without explicit brand justification; different serif from the previous project.
- [ ] Premium-consumer palette check: not the cream + brass + oxblood + espresso family; different from the previous premium-consumer project.
- [ ] Italic descender clearance: every italic word with `y g j p q` has `leading-[1.1]` minimum plus a `pb-1` reserve.
- [ ] Dark-mode tokens defined and the page tested in both modes.

## Hero and navigation

- [ ] Hero fits the viewport: headline 2 lines max, subtext 20 words and 4 lines max, CTA visible without scroll, font scale planned with the image.
- [ ] Hero top padding at most `pt-24` at desktop.
- [ ] Hero stack: max 4 text elements; no tagline under CTAs, no trust micro-strip inside the hero.
- [ ] Logo wall under the hero, not inside it, built from real SVG logos or generated marks, logo-only with no category labels.
- [ ] No version labels, decoration text strips, or scroll cues in the hero.
- [ ] Navigation on one line at desktop, height 80px or less.

## Sections and layout

- [ ] Eyebrow count (mechanical): `uppercase tracking` labels above headlines ≤ ceil(sections / 3); hero counts as one.
- [ ] Split-header ban: no "big headline left, small paragraph right" section headers.
- [ ] Zigzag cap: no 3 consecutive image + text splits.
- [ ] Layout family repetition: no two sections share a family; 8 sections use at least 4 families.
- [ ] Bento has rhythm, exact cell count (no empty cells), and 2-3 visually varied cells.
- [ ] Long lists (> 5 items) use a proper component, not a default `<ul>` with `divide-y`.
- [ ] No `border-t` plus `border-b` on every row of lists or spec tables.
- [ ] No scoring or progress bars with filled tracks as comparison visuals.
- [ ] Mobile collapse explicit for every multi-column layout; `min-h-[100dvh]`, never `h-screen`.

## Content and imagery

- [ ] Real images used (generation tool, then seeded Picsum, then labelled slots); no div-based fake screenshots, no hand-drawn decorative SVGs, no text-only "minimalism".
- [ ] No pills or labels overlaid on images; no decorative photo-credit captions.
- [ ] Copy self-audit done: every visible string re-read; nothing grammatically broken or hallucinated.
- [ ] Content density sane: no 20-row tables, no fake-precise specs without justification, sub-paragraphs ≤ 25 words.
- [ ] Quotes ≤ 3 lines with clean attribution.
- [ ] No duplicate CTA intent; no CTA label wrapping at desktop.
- [ ] Button and form contrast pass WCAG AA against their actual backgrounds.
- [ ] No AI tells from `anti-patterns.md`: section-number eyebrows, micro-meta sentences, floating corner sub-text, locale or weather strips, decorative dots, version footers, "Quietly in use at", poetic section labels, generic names, Acme-style brands, filler verbs.

## Motion and engineering

- [ ] Every animation justified in one sentence (hierarchy, storytelling, feedback, state); no GSAP for show.
- [ ] Motion claimed = motion shown: if `MOTION_INTENSITY > 4`, the page actually animates.
- [ ] Marquee at most once per page.
- [ ] Sticky-stack and horizontal-pan follow the canonical skeletons (`start: "top top"`, `pin: true`, correct scrub).
- [ ] No `window.addEventListener('scroll')`; no continuous values in React state.
- [ ] Reduced motion respected for everything above `MOTION_INTENSITY` 3.
- [ ] Motion isolated in `'use client'` leaf components; every `useEffect` has cleanup.
- [ ] Empty, loading, and error states provided.
- [ ] Cards omitted in favor of spacing where possible.
- [ ] Icons from an allowed library only; one family; no hand-rolled paths.
- [ ] Every import exists in the dependency file.
- [ ] Core Web Vitals plausibly met (LCP < 2.5s, INP < 200ms, CLS < 0.1).
