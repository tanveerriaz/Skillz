# Redesign Protocol

Read this when an existing site or app is in play. Misclassifying the mode is the biggest source of bad redesign output. For the hook-protection and verification loop (IDs, forms, auth, tests), use the `redesign-without-breaking` skill alongside this one.

## 1. Detect the mode first

- **Greenfield:** no existing site, or a full overhaul is approved. Use the dial baseline from `brief-and-dials.md`.
- **Redesign, preserve:** modernise without breaking the brand. Audit first, extract brand tokens, evolve gradually.
- **Redesign, overhaul:** new visual language on top of existing content. Treat visuals as greenfield; preserve content and information architecture.

If ambiguous, ask once: "Should this redesign preserve the existing brand, or are we starting visually from scratch?"

## 2. Audit before touching

Document the current state before proposing changes:

- **Brand tokens:** primary and accent colors, type stack, logo treatment, radii.
- **Information architecture:** page tree, primary nav, key conversion paths.
- **Content blocks:** what exists, what does work, what is filler.
- **Patterns to preserve:** signature interactions, a recognisable hero, the copy voice.
- **Patterns to retire:** AI tells, broken layouts, dead links, generic stock imagery, performance traps.
- **Dial reading of the existing site:** infer its current `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`. That is the starting point, not the baseline.
- **SEO baseline:** ranking pages, meta titles, structured data, OG cards. SEO migration is the top redesign risk.

## 3. Preservation rules

- Do not change information architecture unless asked. Keep slugs, anchor IDs, and nav labels stable.
- Extract brand colors before applying any palette rule. A brand that is already purple stays purple.
- Preserve the copy voice unless a rewrite is requested. Visual modernisation is not a content rewrite.
- Honor existing accessibility wins: focus states, alt text, keyboard navigation, contrast.
- Respect analytics events: do not rename buttons, form fields, or section IDs that tracking depends on.

## 4. Modernisation levers (priority order)

Apply in order and stop when the brief is satisfied:

1. **Typography refresh:** biggest visual lift per unit of risk.
2. **Spacing and rhythm:** section padding, vertical rhythm.
3. **Color recalibration:** desaturate, unify neutrals, keep the brand accent.
4. **Motion layer:** dial-appropriate micro-interactions on existing components.
5. **Hero and key-section recomposition** using the pattern vocabulary in `layout-and-content.md`.
6. **Full block replacement:** only when the existing block cannot be saved.

## 5. Decision tree

- IA, content, and SEO are sound: **targeted evolution** (levers 1-4). About 70% of the value at 40% of the risk.
- Visual debt is structural (broken IA, no design system, broken mobile): **full redesign** with strict content preservation.
- The brand itself is changing: **greenfield**.

## 6. What never changes silently

Never modify without explicit approval: URL structure and route slugs, primary nav labels, form field names or order (breaks analytics and autofill), the brand logo or wordmark, existing legal, consent, or cookie copy.
