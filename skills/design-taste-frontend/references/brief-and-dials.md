# Brief Inference, Dials, and System Selection

Read this before any code. Most generated design output is bad because the model jumps to a default aesthetic instead of reading the brief.

## 1. Read the signals

1. **Page kind:** landing (SaaS, consumer, agency, event), portfolio (developer, designer, studio), redesign (preserve or overhaul), editorial or blog.
2. **Vibe words the user used:** "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "Apple-like", "playful", "serious B2B", "editorial", "glassy", "dark tech".
3. **Reference signals:** URLs linked, screenshots pasted, products or competitors named.
4. **Audience:** procurement panel, design-conscious consumer, recruiter scanning a portfolio. The audience picks the aesthetic, not the agent's taste.
5. **Existing brand assets:** logo, color, type, photography. For redesigns these are starting material, not optional input.
6. **Quiet constraints:** accessibility-first audiences, public sector, regulated industries, trust-first commerce, children's products. These override aesthetic preference.

## 2. Declare the Design Read

Before any code, state one line:

> "Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<design system or aesthetic family>."

Examples:

- "Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion."
- "Reading this as: solo designer portfolio for hiring managers, with an editorial, kinetic-type language, leaning toward native CSS + scroll-driven animation + custom typography."
- "Reading this as: redesign of a public-sector service site, with a trust-first language, leaning toward GOV.UK Frontend or USWDS."

If the read genuinely diverges, ask exactly one clarifying question ("Closer to Linear-clean or Awwwards-experimental?"). If you can infer confidently, do not ask.

## 3. Anti-default discipline

Do not default to: purple gradients, centered hero over a dark mesh, three equal feature cards, glassmorphism on everything, infinite micro-animations everywhere, Inter + slate-900. Reach past these deliberately based on the design read.

## 4. The three dials

Every layout, motion, and density decision is gated by three values. Use these exact names; do not invent aliases.

- `DESIGN_VARIANCE` (1 = perfect symmetry, 10 = artistic chaos)
- `MOTION_INTENSITY` (1 = static, 10 = cinematic physics)
- `VISUAL_DENSITY` (1 = art gallery, 10 = cockpit)

Baseline `8 / 6 / 4` unless the design read overrides. Overrides happen conversationally, never by asking the user to edit files.

### Dial inference from signals

| Signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| minimalist, clean, calm, editorial, Linear-style | 5-6 | 3-4 | 2-3 |
| premium consumer, Apple-like, luxury, brand | 7-8 | 5-7 | 3-4 |
| playful, wild, Awwwards, experimental, agency | 9-10 | 8-10 | 3-4 |
| landing page, portfolio, marketing site (default) | 7-9 | 6-8 | 3-5 |
| trust-first, public sector, regulated, accessibility-critical | 3-4 | 2-3 | 4-5 |
| redesign, preserve | match existing | +1 | match existing |
| redesign, overhaul | +2 | +2 | match existing |

### Use-case presets

| Use case | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| Landing, SaaS mainstream | 7 | 6 | 4 |
| Landing, agency or creative | 9 | 8 | 3 |
| Landing, premium consumer | 7 | 6 | 3 |
| Portfolio, designer or studio | 8 | 7 | 3 |
| Portfolio, developer | 6 | 5 | 4 |
| Editorial or blog | 6 | 4 | 3 |
| Public-sector service | 3 | 2 | 5 |

### What each level means

**DESIGN_VARIANCE**
- 1-3 Predictable: symmetrical 12-column grid, equal fr units, equal paddings, centered alignment.
- 4-7 Offset: negative-margin overlaps, mixed image aspect ratios (4:3 next to 16:9), left-aligned headers over centered content.
- 8-10 Asymmetric: masonry, fractional grids (`2fr 1fr 1fr`), large empty zones (`padding-left: 20vw`).
- Mobile override: for 4-10, every asymmetric layout collapses to strict single column below 768px.

**MOTION_INTENSITY**
- 1-3 Static: no automatic animation; `:hover` and `:active` only.
- 4-7 Fluid CSS: `transition: 0.3s cubic-bezier(0.16, 1, 0.3, 1)`, `animation-delay` cascades on load, `transform` and `opacity` only.
- 8-10 Choreography: scroll-triggered reveals, parallax, scroll-driven animation (CSS `animation-timeline` or GSAP ScrollTrigger), Motion hooks. Never `window.addEventListener('scroll')`.

**VISUAL_DENSITY**
- 1-3 Art gallery: huge section gaps (`py-32` to `py-48`).
- 4-7 Daily app: standard spacing (`py-16` to `py-24`).
- 8-10 Cockpit: tight padding, no card boxes, 1px lines separate data, `font-mono` for all numbers.

## 5. Pick the foundation: real system or aesthetic

Do not invent CSS for things that have an official package. Do not pretend an aesthetic trend is an official system.

### Briefs that call for a real design system

| Brief reads as | Reach for |
|---|---|
| Microsoft-style enterprise SaaS, dashboards | `@fluentui/react-components` or `@fluentui/web-components` |
| Google-style, Material-flavored product | `@material/web` + Material 3 tokens |
| IBM-style B2B, enterprise analytics | `@carbon/react` + `@carbon/styles` |
| Shopify app surfaces | Polaris web components or Polaris React (required) |
| Atlassian or Jira-style product | `@atlaskit/*` + `@atlaskit/tokens` |
| GitHub-style devtool or community page | `@primer/css`, or `@primer/react-brand` for marketing |
| UK public-sector service | `govuk-frontend` |
| US public-sector, trust-first | `uswds` |
| Fast local-business or agency MVP | Bootstrap 5.3 |
| Modern accessible React foundation | `@radix-ui/themes` |
| Modern SaaS where you own the components | shadcn/ui (never ship its default state) |
| Tailwind-based modern SaaS or AI marketing | Tailwind v4 utilities + `dark:` variant (default for indie builds) |

Honesty rules: install and use the official package; do not recreate its CSS by hand; do not import a system's tokens and override 90% of them. One system per project. Install commands and canonical docs are in `stack-conventions.md`.

### Briefs that are an aesthetic, not a system

Build with native CSS + Tailwind + a maintained component library. Comment honestly about what is borrowed inspiration.

| Aesthetic | Honest implementation |
|---|---|
| Glassmorphism, frosted glass | `backdrop-filter`, layered borders, highlight overlays, solid fallback under `prefers-reduced-transparency` |
| Bento (Apple-style tile grids) | CSS Grid with mixed cell sizes |
| Brutalism | native CSS, monospace, raw borders |
| Editorial, magazine | asymmetric grid, generous whitespace, type-led hierarchy |
| Dark tech, hacker | mono type, one accent, terminal motifs |
| Aurora, mesh gradients | SVG or layered radial gradients |
| Kinetic typography | native CSS and scroll-driven animations; GSAP only for pinned sequences |
| Apple Liquid Glass | Apple platforms only. No official web CSS exists. Label web versions as approximations (see `stack-conventions.md`) |

## 6. Out of scope

This skill is not for dashboards or admin panels (use Fluent, Carbon, Atlassian, Polaris), data tables (TanStack Table, AG Grid), multi-step forms and wizards, code editors (Monaco, CodeMirror), native mobile (Apple HIG, Material), or realtime collaboration UIs. If the brief is one of these, say so, point to the right tool, and apply this skill only to the marketing and landing surfaces.
