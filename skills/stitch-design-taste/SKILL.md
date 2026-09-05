---
name: stitch-design-taste
description: Use when a project will generate screens with Google Stitch and needs a DESIGN.md that Stitch can follow consistently. Translates a product brief and visual direction into a semantic design system file with named colors and hex codes, typography rules, component behaviors, layout and responsive principles, motion philosophy, and an explicit list of banned generic patterns.
---

# Purpose

Produce a `DESIGN.md` that acts as the single source of truth when prompting Google Stitch. Stitch interprets design through natural-language "visual descriptions" paired with exact values, so the file must be both evocative and precise. The result steers Stitch away from default output (purple gradients, Inter, three equal cards) and toward a system tied to one specific product.

# When to Use

- Starting a new Stitch project and no design system file exists yet.
- Revising a `DESIGN.md` because generated screens drift or look generic.
- Translating an existing brand or design system into Stitch's format.

Not for writing production CSS or components; this skill produces the specification Stitch consumes.

# Inputs

- Product brief: what it does, who uses it, platform (web or mobile).
- Brand direction or existing brand tokens, if any.
- Screen inventory and content hierarchy.
- Interaction needs (dashboards, marketing, forms, live data).
- Constraints: accessibility, regulated content, density expectations.

# Outputs

- `DESIGN.md` following `references/design-md-template.md`, with seven sections: atmosphere, color palette and roles, typography, component stylings, layout principles, motion and interaction, anti-patterns.
- Every color named by role with a hex code; every measurement in rem or px.

# Procedure

1. **Define the atmosphere.** Read the brief and set three dials: density (1 gallery-airy to 10 cockpit-dense), variance (1 symmetric to 10 chaotic), motion (1 static to 10 cinematic). Default `4 / 8 / 6`. Write two to four sentences of mood that name those levels.
2. **Map the palette.** One neutral base family (zinc, slate, or stone), one accent below 80% saturation, off-black for text. Give each color a descriptive name, hex code, and functional role. Ban purple and neon gradients and pure black explicitly.
3. **Set typography.** Display, body, and mono roles with named fonts. Inter is not the default; prefer faces such as Geist, Outfit, Cabinet Grotesk, or Satoshi. Generic serifs are banned; a distinctive modern serif is allowed only for editorial work with a stated reason, and never in dashboards. When density is 8 or above, all numbers are monospace.
4. **Describe components.** Buttons (flat, tactile press, no glow), cards (only when elevation means hierarchy; dividers or space in dense layouts), inputs (label above, error below, accent focus ring), loading skeletons, composed empty states, inline errors.
5. **Define layout and responsive rules.** Grid-first, max-width containment, no overlapping elements, no three-equal-cards rows, asymmetric hero when variance is above 4, dynamic viewport height, single-column collapse below 768px, fluid headline scaling, 44px tap targets, no horizontal scroll.
6. **Encode motion.** Spring physics with no linear easing, staggered reveals, micro-loops only on live-state components, transform and opacity only, reduced-motion respected.
7. **List the bans.** Copy the anti-pattern block from the template and add any product-specific tells (for example, "no emoji status labels" for a finance app).
8. **Fill the template.** Open `references/design-md-template.md`, replace every bracket, keep the section order, and compare against the full example at `DESIGN.md` in this skill folder.
9. **Review with the checklist below**, then hand the file to Stitch (paste into the project design context or reference it through the Stitch MCP server).

# Quality Checklist

- [ ] Every color has a name, a hex code, and a role.
- [ ] Exactly one accent; no purple or neon; no pure black.
- [ ] Typography names real fonts for display, body, and mono; bans are explicit.
- [ ] Dial levels are stated in the atmosphere section and match the layout and motion rules.
- [ ] Layout section states the mobile collapse, tap target size, and no-overlap rule.
- [ ] Anti-pattern list is present and includes copy tells, not only visual ones.
- [ ] Developer shorthand is translated into plain descriptive language.
- [ ] Rules are specific to this product, not a generic list of adjectives.

# Edge Cases

- **An existing design system is supplied:** map its tokens faithfully. Do not layer a conflicting aesthetic on top; only fill gaps (states, motion, bans) it leaves open.
- **Dashboard or data-heavy product:** raise density, drop variance to 3-5, sans-serif only, monospace numbers, dividers instead of cards.
- **Brand insists on purple or a serif:** allow it and write the constraint precisely (exact hex, exact face) so Stitch executes it with intent rather than defaulting to generic gradients.
- **Mobile app rather than web:** keep the same sections; replace max-width and breakpoint rules with safe-area, thumb-zone, and platform navigation notes.
- **Brief is vague on mood:** ask one question about the closest reference product before writing the atmosphere.

# Safety Rules

- Do not include private project data, internal URLs, or client names in the shared specification.
- Do not reference unlicensed fonts or assets as requirements; name licensed or open alternatives.
- Do not invent product content, metrics, or testimonials inside `DESIGN.md`.
- Do not present a generic template as finished work; every bracket must be replaced.

# Examples

**Good:** A `DESIGN.md` for a field-service scheduling app: "Cockpit-leaning density (7), moderate variance (5), quiet motion (3). Canvas Slate (#F8FAFC), Graphite Ink (#0F172A), single Signal Amber accent (#D97706) for the current job. Geist for display and body, Geist Mono for every time and distance value. No cards; jobs separate with 1px Whisper Borders."

**Bad:** "Modern, clean, premium feel with a nice dark theme and some accent colors." No hex codes, no fonts, no bans, nothing Stitch can apply consistently.
