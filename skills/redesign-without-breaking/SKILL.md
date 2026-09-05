---
name: redesign-without-breaking
description: Use when restyling, polishing, or visually upgrading an existing website or app without breaking its behavior. Scans the codebase, audits for generic AI design patterns, maps the JavaScript, auth, and analytics hooks a change could break, proposes changes before editing, applies fixes in priority order, and verifies function, responsiveness, and accessibility after each change. Works with any CSS framework or vanilla CSS.
---

# Purpose

Upgrade the visual quality of an existing interface while preserving every route, form, handler, and data contract it depends on. Redesigns fail in two ways: the visuals stay generic, or the upgrade silently breaks a login form because an ID was renamed. This skill runs one loop that prevents both: scan, diagnose, protect, fix, verify.

# When to Use

- Restyling pages, components, dashboards, auth screens, or landing pages that already work.
- Applying a brand to existing markup.
- Removing "AI template" patterns from a shipped product.
- Any visual enhancement where "do not break it" matters as much as "make it better".

Not for greenfield builds (use a design-direction skill) or framework migrations.

# Inputs

- The codebase, or the specific pages and components to change.
- The desired direction: preserve the brand, or overhaul the visuals while keeping content and structure.
- Brand reference if one exists (existing landing page, style source, or token file).
- Target viewports and any constraints (accessibility, regulated content, performance budgets).
- Access to run the app and its tests.

# Outputs

- A short audit listing generic patterns, weak points, and missing states found.
- A protected-elements list: IDs, classes, form fields, and `data-*` hooks that must not change.
- A change table (element, current, proposed, reason) for approval before non-trivial edits.
- Targeted code changes in the existing stack, applied in priority order.
- Verification notes: functionality re-tested, viewports checked, accessibility checks passed.

# Procedure

## 1. Scan

1. Identify the framework, styling method (Tailwind and its version, vanilla CSS, CSS-in-JS, component library), and dependency file.
2. Read the brand reference first. Extract exact colors, fonts, radii, shadows, button and card styles, spacing. Do not invent brand values. If no reference exists, define a minimal palette and type scale before touching anything.
3. Infer the current design level (symmetry, motion, density) so changes evolve the site rather than replacing it.

## 2. Diagnose

Run the audit below and list every hit. Do not fix yet.

- **Typography:** default or Inter-everywhere fonts; headlines without presence; body text wider than about 65 characters; only weights 400 and 700 in use; proportional numbers in data views (use `tabular-nums`); no tracking adjustments; orphaned last words (use `text-wrap: balance`).
- **Color and surfaces:** pure `#000000` backgrounds; more than one accent; accents above 80% saturation; mixed warm and cool grays; purple-blue "AI gradient"; pure-black shadows on light backgrounds; a single inverted-theme section dropped into an otherwise consistent page; inconsistent light direction across shadows.
- **Layout:** everything centered; three equal feature cards; `height: 100vh` heroes (use `min-height: 100dvh`); flexbox percentage math instead of Grid; no max-width container; uniform radius on every element; identical top and bottom section padding; buttons in card groups not bottom-aligned; misaligned baselines across side-by-side cards.
- **States and interaction:** no hover, active, or focus styles; zero-duration transitions; spinners instead of skeletons; missing empty and error states; `window.alert()` errors; links to `#`; no active nav indicator; animations on `top`, `left`, `width`, or `height`.
- **Content:** "John Doe", "Acme Corp", `99.99%`; lorem ipsum; "Elevate", "Seamless", "Unleash"; exclamation marks in success messages; Title Case On Every Header; identical dates or avatars.
- **Components:** border + shadow + white cards everywhere; accordion FAQ by default; three-tower pricing; modals for simple actions; four-column footer link farm.
- **Code quality:** div soup instead of semantic HTML; inline styles mixed with classes; hardcoded pixel widths; missing alt text; `z-index: 9999`; imports not in the dependency file; missing meta and OG tags.
- **Omissions:** no legal links, no 404 page, no form validation, no skip-to-content link, no way back from dead-end flows.

## 3. Protect

4. Search for functional dependencies before proposing any change: `getElementById`, `querySelector`, `data-*` attributes, form `action` URLs, input `name` values, OAuth and auth handlers, analytics event selectors, test selectors, and anchor IDs used in links. Write them down as the protected list.
5. Present the change table (element, current classes or styles, proposed, reason). Wait for approval on anything non-trivial. Trivial changes (spacing, color tokens, font swap) can proceed.

## 4. Fix

Apply in this order. Stop when the brief is satisfied.

6. **Font swap** with proper loading (`font-display: swap`, self-hosted or framework font loader).
7. **Color cleanup:** one accent, one gray family, off-black, tinted shadows, one theme for the whole page.
8. **Hover, active, focus states** and 200-300ms transitions on `transform` and `opacity` only.
9. **Layout and spacing:** Grid, max-width container, consistent radius scale, aligned baselines, `100dvh`.
10. **Replace generic components** with alternatives that fit the content (zig-zag, asymmetric grid, side-by-side FAQ, inline editing).
11. **Add loading, empty, and error states** matching the layout shape.
12. **Typography scale polish** as the last pass.

Rules while fixing: change one component at a time; restyle protected elements via class only; if a protected ID must change, update the reference in the same change; never add a library without checking the dependency file first; keep every change small enough to review.

## 5. Verify

13. After each component: run the app, exercise the affected route, form, or action, and run existing tests.
14. Check mobile, tablet, and desktop: no horizontal scroll, touch targets at least 44px, readable text.
15. Check accessibility: contrast at least 4.5:1 for text and 3:1 for large text, visible focus rings, labels on inputs, alt text, keyboard navigation, `prefers-reduced-motion` respected.
16. Re-audit: confirm the diagnose list is cleared and no protected element changed.

# Quality Checklist

- [ ] Brand values taken from the reference, not invented.
- [ ] Protected list written before the first edit; nothing on it renamed or removed.
- [ ] Change table presented before non-trivial edits.
- [ ] One accent, one gray family, one theme, one radius scale across the page.
- [ ] Hover, active, and focus states exist on every interactive element.
- [ ] Loading, empty, and error states present where data loads or forms submit.
- [ ] Existing routes, forms, auth, analytics, and tests still work.
- [ ] Mobile, tablet, and desktop verified; no horizontal scroll.
- [ ] Contrast, focus, labels, alt text, keyboard navigation, reduced motion verified.
- [ ] No new dependency added without checking the dependency file.

# Edge Cases

- **ID used by JS must change:** update the JS reference in the same change, or keep the ID and restyle via a class.
- **Auth form restyle:** change presentation only. Never touch action URLs, input names, hidden fields, or handlers.
- **No design system exists:** introduce the smallest token layer (colors, type scale, spacing, radius) needed for consistency. Do not build a full component library.
- **Brand is already purple or uses a serif:** keep it. Execute it well rather than replacing it with a generic neutral palette.
- **Tailwind version unknown:** check before editing config; v3 and v4 configure differently.
- **Animation requested:** keep it under about 300ms, purposeful, and disabled under `prefers-reduced-motion`.
- **SEO-sensitive site:** keep slugs, anchor IDs, headings order, and meta tags stable unless asked.

# Safety Rules

- Never rename or remove IDs, classes, `data-*` hooks, or form fields that JavaScript, auth, tests, or analytics depend on without handling the reference.
- Never change URL structure, nav labels, legal or consent copy, or the logo without explicit approval.
- Never migrate frameworks or styling libraries as part of a redesign.
- Never replace real content or evidence with placeholder filler.
- Never skip functional, responsive, and accessibility verification.
- Never modify production systems outside the requested scope.

# Examples

**Good:** Audit finds Inter, three equal cards, and a login button with `#submit-login` targeted by an auth handler. Protected list records the ID. Change table proposes a font swap, a 2-column zig-zag replacing the cards, and new padding and hover states on `.login-btn` via class only. After approval, each change is applied and the login flow is re-tested on mobile and desktop with contrast confirmed at 4.5:1.

**Bad:** Renaming `#submit-login` to `#cta` to "clean up", swapping the whole page for a generic dark landing template, and shipping without opening the login form.
