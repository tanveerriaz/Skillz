# Curiosity Fieldbook house style

Use this reference as a portable visual foundation when a project needs an evidence-led, editorial, dark interface and no stronger brand direction has been supplied.

## Contents

- [Core idea](#core-idea)
- [Portable tokens](#portable-tokens)
- [Typography](#typography)
- [Geometry and spacing](#geometry-and-spacing)
- [Structural grammar](#structural-grammar)
- [Image treatment](#image-treatment)
- [Motion](#motion)
- [Interaction and accessibility](#interaction-and-accessibility)
- [Reusable signature, not a copied page](#reusable-signature-not-a-copied-page)
- [Avoid](#avoid)
- [Implementation workflow](#implementation-workflow)

## Core idea

Build a **curiosity fieldbook**: an annotated field notebook crossed with restrained systems cartography. Make routes, evidence, chronology, status, and useful starting points visible. The work should feel personal, credible, technically literate, and editorial—not like a generic AI product template.

Use real artifacts as visual material: portraits, product captures, public activity, source documents, event photographs, diagrams, and live states. Prefer evidence to decorative illustration. Never regenerate or reshape a real person's identifiable features.

## Portable tokens

| Role | Value | Rule |
|---|---|---|
| Carbon | `#090909` | Primary canvas |
| Night | `#050505` | Deep evidence sections |
| Black panel | `#131313` | Quiet section contrast |
| Raised panel | `#171717` | Cards and controls |
| Soft white | `#F4F4F0` | Primary text |
| Silver | `#C9C9C3` | Secondary text |
| Smoke | `#90908B` | Supporting copy and labels |
| Hairline | `#30302D` | Dividers and structural borders |
| Electric blue | `#5B76FF` | Focus and primary interaction signal |
| Blue soft | `#B8C4FF` | Links or labels on dark surfaces |
| Signal red | `#DF2B20` | Rare contextual status signal; not a decorative accent |

Use cobalt as interface punctuation, not as a large decorative fill. Keep most surfaces monochrome. Reserve red for a meaningful live, place, or status marker. Do not introduce additional brand colors casually.

## Typography

- Use **Switzer** for display and body. Use weights 300–600.
- Use **IBM Plex Mono** for dates, states, labels, filters, formats, measurements, and machine-readable affordances. Use weights 400–500.
- Bundle Switzer and IBM Plex Mono only from licensed project assets or authorized font sources. Otherwise use the fallback stacks below.
- Set body copy at 16px or larger with at least 1.5 line height.
- Set display type light or medium, tightly tracked, and compact in line height. Typical large-title tracking is `-0.05em` to `-0.075em`; never allow letters to collide.
- Use 8–11px uppercase mono labels sparingly. They encode metadata; they do not decorate empty space.
- Prefer a clear thesis, short supporting copy, and precise labels over marketing superlatives.

Fallback stacks:

```css
--tr-display: "Switzer", "Helvetica Neue", Arial, sans-serif;
--tr-body: "Switzer", "Helvetica Neue", Arial, sans-serif;
--tr-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
```

## Geometry and spacing

- Use a `1280px` maximum shell with fluid gutters: `min(1280px, calc(100vw - 48px))` on desktop and `calc(100% - 32px)` on small screens.
- Build hierarchy with scale, whitespace, hairlines, alignment, image proportion, and contrast—not layers of rounded containers.
- Use square corners or a `2px` radius. A circle is valid when its meaning or control shape calls for one.
- Make major sections spacious: roughly `clamp(78px, 9vw, 126px)` vertically.
- Use asymmetric editorial grids. A useful section introduction pairs a larger thesis column with a narrower context column.
- Let images carry visual weight. Avoid framing every element as a card.
- Keep hover lift at `4px` or less.

## Structural grammar

Choose only structures that match the project. The portfolio currently demonstrates this sequence:

1. Sticky global navigation separated by one hairline.
2. Portrait- or artifact-led thesis hero with oversized ghost type, vertical utility labels, and quiet proof counters.
3. A compact current-state strip.
4. A horizontally moving evidence ribbon that supplies human context.
5. Three or four beginner-friendly doorways before the complete catalog.
6. Chronological trails that connect a question to what it changed or produced.
7. A filterable live lab with real projects, tools, demos, and learning.
8. A darker proof register for shipping signals, credentials, or verified activity.
9. Long-form evidence sections for learning, notes, events, tools, about, and contact.

Adapt the grammar by surface:

- **Landing or portfolio:** thesis hero → evidence → starting points → catalog → proof → human close.
- **Product or SaaS:** compact thesis → primary task → live evidence → workflow → proof; keep cinematic treatment to one moment.
- **Dashboard or application:** persistent navigation → status strip → task/evidence grid → chronological activity; omit a large hero after onboarding.
- **Editorial or documentation:** thesis header → mono metadata/formats → readable article measure → evidence callouts → related trails.

Do not use section numbers unless order is meaningful. Do not create a bento grid merely to fill a page.

## Image treatment

- Prefer real photography and product evidence over stock imagery or synthetic decoration.
- Grade photography with restrained desaturation, contrast, and brightness; restore natural color on hover, focus, tap, or another clear user intent.
- Preserve faces, expressions, identity, and documentary details exactly.
- Use responsive derivatives sized for the layout. Keep unnecessarily large originals out of production bundles.
- Caption evidence with compact mono metadata when the date, place, source, or state matters.

## Motion

- Use `cubic-bezier(.16, 1, .3, 1)` for purposeful 180–320ms transitions.
- Choose one orchestrated motion idea per surface: a slow evidence ribbon, a single counter rise, a chronological route, a reading-paced relay, or a color reveal.
- Stop or simplify continuous motion on hover/focus when it helps inspection.
- Respect `prefers-reduced-motion`; stop marquees and route animations and remove nonessential transforms.
- Avoid ambient blobs, endless decorative particles, and scattered reveal effects.

## Interaction and accessibility

- Give every interactive element a visible `3px` electric-blue focus ring with offset.
- Keep touch targets at least `44px` where practical.
- Use native elements first. Use `aria-pressed` for filters and `aria-expanded` for disclosures.
- Apply `inert` to hidden interactive regions when supported; never leave hidden mobile-nav or dialog controls focusable.
- Keep body text at WCAG AA contrast. Smoke is supporting text only; verify it at the chosen size and weight.
- Respect reduced motion and keyboard navigation from the first implementation pass.
- Use plain, honest labels. Call a rule-based guide a rule-based guide, not AI. Say “For agents” rather than “API” unless it is actually an API.

## Reusable signature, not a copied page

Keep these constants when using this visual direction:

- carbon field, restrained cobalt signals, and near-monochrome surfaces;
- Switzer plus IBM Plex Mono;
- square geometry and hairline structure;
- evidence before ornament;
- editorial scale and asymmetric composition;
- visible chronology, status, sources, and useful routes;
- one controlled, content-specific motion idea.

Change the signature moment to fit the subject. It might be a live simulation, a product state, a trace, a before/after, a source artifact, or a portrait. Do not reuse the exact studio-portrait hero when the project has a more truthful artifact.

## Avoid

- Purple AI gradients, warm cream startup palettes, green or orange brand systems, and ambient glow blobs.
- Glass cards, generic bento dashboards, large rounded card stacks, and pill-heavy navigation.
- Emoji as interface icons.
- Decorative motion that does not reveal state, route, evidence, or causality.
- Unsupported proof, invented metrics, private activity presented as public, or simulated “live” states.
- Dense mono copy, low-contrast body text, decorative vertical labels, or huge type that breaks on mobile.

## Implementation workflow

1. Identify the page's audience, single job, evidence, and truthful signature artifact.
2. Start from `assets/curiosity-fieldbook.css` or map its tokens into the project's existing theme system.
3. Select the smallest suitable structural sequence from this reference.
4. Design mobile and desktop together; below roughly `760px`, stack editorial splits and turn horizontal stories into readable vertical flows or user-controlled scrollers.
5. Add only one signature motion system.
6. Verify type loading, contrast, keyboard flow, touch size, reduced motion, and responsive images.
7. Compare the result with the current project brief. Keep the house DNA, but remove any portfolio-specific structure that does not serve this product.
