---
name: design-taste-frontend
description: Use when building or redesigning a landing page, portfolio, marketing site, or editorial page and the result must not look like a generated template. Reads the brief, declares a design direction and three dials (variance, motion, density), picks a real design system or an honest aesthetic, and enforces typography, color, layout, imagery, motion, and anti-pattern rules with a mandatory pre-flight check. Not for dashboards, data tables, or multi-step product UI.
---

# Purpose

Ship frontend work that feels specific to its subject instead of assembled from defaults. LLM-generated pages fail in predictable ways: purple gradients, centered hero over a mesh, three equal cards, Inter everywhere, cream and brass for every "premium" brief, em-dashes in every headline. This skill replaces those reflexes with a reasoned direction, contextual rules, and a hard final check.

# When to Use

- Landing pages (SaaS, consumer, agency, event), portfolios, marketing and about pages, editorial or blog layouts.
- Redesigns of the above, in preserve or overhaul mode.
- Any brief where the user says "not generic", "premium", "does not look AI-made", or names a visual reference.

Not for dashboards, admin panels, data tables, wizards, code editors, native mobile, or realtime collaboration UIs. Say so, point to the right tool, and apply this skill only to the marketing surfaces.

# Inputs

- The brief: page kind, vibe words, references, audience, existing brand assets, constraints.
- Real content or a clear statement of what content is still missing.
- The existing codebase for redesigns (framework, styling method, dependency file).
- Available tooling: image generation, browser for verification, Lighthouse.

# Outputs

- A one-line Design Read and explicit dial values.
- A named foundation: an official design system package, or an honestly labelled aesthetic on Tailwind + native CSS.
- A responsive, dual-theme, reduced-motion-aware implementation with real imagery and full UI states.
- A completed pre-flight checklist.

# Procedure

Every rule is contextual. Read the brief first, then pull only the references the decision needs.

1. **Read the brief and declare the Design Read.** Follow `references/brief-and-dials.md`. State one line: "Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<system or aesthetic>." Ask at most one clarifying question, and only if the read genuinely diverges.
2. **Set the three dials.** `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`, baseline `8 / 6 / 4`, adjusted by the inference table in the same reference. Use these exact names.
3. **Detect redesign mode when a site exists.** Read `references/redesign-protocol.md`: greenfield, preserve, or overhaul. Audit brand tokens, IA, content, SEO, and the current dial reading before changing anything. Pair with the `redesign-without-breaking` skill for hook protection.
4. **Pick the foundation.** If the brief matches a real design system (Fluent, Material, Carbon, Polaris, Atlaskit, Primer, GOV.UK, USWDS, Radix, shadcn, Bootstrap), install the official package using `references/stack-conventions.md`. Otherwise build the aesthetic honestly. One system per project. Verify every dependency before importing.
5. **Choose type, palette, radius, and theme.** Read `references/typography-and-color.md`: sans display by default, serif only with a stated reason, one accent under 80% saturation, one gray family, one radius system, one page theme, dual mode with tested contrast.
6. **Compose the page.** Read `references/layout-and-content.md` for hero limits (2-line headline, 20-word subtext, 4 text elements, `pt-24` cap), nav on one line, eyebrow ration (1 per 3 sections), layout-family repetition ban, zigzag cap, bento cell rules, image strategy (generation tool first, then seeded placeholders, then labelled slots), content density, CTA intent, forms, and UI states.
7. **Add motion only where it communicates something.** Read `references/motion-patterns.md`: Motion for UI and reveals, GSAP only for pin and scrub using the canonical skeletons, no scroll listeners, `transform` and `opacity` only, reduced motion honored, marquee at most once.
8. **Sweep for AI tells.** Read `references/anti-patterns.md` and remove every hit: em-dashes, section-number eyebrows, scroll cues, decorative dots, locale strips, fake screenshots, poetic labels, generic names and numbers.
9. **Run the pre-flight check.** Work through `references/preflight-checklist.md` item by item. Open the page in both themes, at mobile and desktop, with reduced motion on. Fix every failure before delivering.
10. **Report.** State the Design Read, dials, foundation, any placeholder image slots still needed, and any checklist items the user must decide.

## Which reference for which decision

| Decision | Read |
|---|---|
| What is this brief, what dials, real system or aesthetic, out of scope | `references/brief-and-dials.md` |
| Existing site: preserve or overhaul, what to audit, what never changes | `references/redesign-protocol.md` |
| Fonts, serif question, palette, radius, theme lock, dark mode | `references/typography-and-color.md` |
| Hero, nav, sections, bento, images, logos, copy length, CTAs, forms, states, pattern names | `references/layout-and-content.md` |
| Any animation, scroll effect, GSAP or Motion choice, physics | `references/motion-patterns.md` |
| Final sweep for banned patterns and copy tells | `references/anti-patterns.md` |
| Stack setup, icons, dependencies, performance, install commands, doc links, glass approximation | `references/stack-conventions.md` |
| Before delivering anything | `references/preflight-checklist.md` |

# Quality Checklist

- [ ] Design Read declared and dials stated with reasons.
- [ ] Foundation named; official package used when a real system applies; no mixed systems.
- [ ] One accent, one gray family, one radius system, one page theme; both modes tested.
- [ ] Sans display by default; any serif justified and not Fraunces or Instrument Serif.
- [ ] Hero fits the viewport with at most 4 text elements; nav on one line.
- [ ] Eyebrows ≤ ceil(sections / 3); no layout family repeated; no 3 consecutive zigzags.
- [ ] Real images in place or labelled slots reported; no div-built screenshots.
- [ ] Zero em-dashes; no anti-pattern hits remain.
- [ ] Motion motivated, isolated in client leaves, reduced-motion safe; no scroll listeners.
- [ ] Empty, loading, and error states present; contrast passes WCAG AA.
- [ ] Full pre-flight checklist completed.

# Edge Cases

- **Brief is a dashboard or product UI:** say it is out of scope, recommend Fluent, Carbon, Atlaskit, or Polaris, and apply this skill only to marketing pages.
- **Brand is already purple, or already uses a serif:** keep it and execute it well. Brand overrides the default bans.
- **No image tool and no assets:** leave labelled placeholder slots and list them at the end. Do not fill with hand-drawn SVG.
- **Public-sector or accessibility-critical audience:** dials drop to low variance and motion; Inter and a real system (GOV.UK, USWDS) are correct choices.
- **Motion cannot ship reliably in scope:** lower `MOTION_INTENSITY` to 3 and ship clean static work rather than half-built animation.
- **Content is genuinely dense (specs, catalogues):** move it to a dedicated page or a proper component; do not stretch the landing page.
- **User asks for emojis or a playful chat-native tone:** allow emojis sparingly; otherwise they stay out.

# Safety Rules

- Do not overwrite established brand rules, IA, slugs, nav labels, or legal copy without approval.
- Do not fabricate testimonials, metrics, logos, or credentials; mark sample data as sample.
- Do not trade readability, contrast, keyboard access, or reduced-motion support for visual novelty.
- Do not import a dependency that is not in the project's dependency file without stating the install step.
- Do not hand-roll a design system's CSS when the official package exists.
- Do not deliver until every pre-flight item is honestly ticked.

# Examples

**Good:** "Reading this as: developer portfolio for hiring managers, with a calm Linear-style language, leaning toward Tailwind v4 + Geist + `whileInView` reveals. Dials 6 / 5 / 4." Asymmetric split hero with a generated black-and-white workspace photo, two eyebrows across seven sections, one emerald accent, dark and light tested, zero em-dashes, pre-flight complete.

**Bad:** Centered hero on a purple mesh, "Elevate your workflow" in Fraunces, three equal feature cards, an eyebrow above every section, `Scroll ↓` at the hero bottom, a fake dashboard built from divs, `window.addEventListener('scroll')` driving parallax, and the same cream-and-brass palette as the last three projects.
