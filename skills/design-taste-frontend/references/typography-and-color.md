# Typography, Color, Shape, and Theme

Read this when choosing fonts, palette, corner radius, or light/dark strategy. Every rule has an override path; none fires without a reason.

## 1. Typography

### Defaults
- Display and headlines: `text-4xl md:text-6xl tracking-tighter leading-none`.
- Body: `text-base text-gray-600 leading-relaxed max-w-[65ch]`.
- Control hierarchy with weight and color, not raw scale. Oversized H1s that only shout are a tell.

### Sans-serif choice
- Discouraged as default: `Inter`. Prefer `Geist`, `Outfit`, `Cabinet Grotesk`, `Satoshi`, or a brand-appropriate face.
- Inter is fine when the user asks for a neutral, standard, Linear-style feel, or for public-sector and accessibility-first sites.
- Pairings worth knowing: `Geist` + `Geist Mono`; `Satoshi` + `JetBrains Mono`; `Cabinet Grotesk` + `Inter Tight`; `GT America` + `IBM Plex Mono`.
- Sans display families for creative, agency, premium-consumer, and portfolio briefs: Geist Display, ABC Diatype, Söhne Breit, Cabinet Grotesk Display, Migra Sans, GT Walsheim, Inter Display, PP Neue Montreal. Sans display is the default for the same reason black is the default in fashion.

### Serif discipline
- Serif is very discouraged as the default for any project. "It feels creative or premium" is not a reason. "Creative brief = serif" is the most-tested AI tell in production rounds.
- Serif is acceptable only when the brand brief names a serif, or the aesthetic is genuinely editorial, luxury, publication, heritage, or vintage and you can say why this specific serif fits this specific brand.
- Banned as defaults: `Fraunces` and `Instrument Serif` (the two LLM-favorite display serifs).
- If a serif is justified, rotate through a pool and do not reuse the same one on consecutive projects: PP Editorial New, GT Sectra Display, Cardinal Grotesque, Reckless Neue, Tiempos Headline, Recoleta, Cormorant Garamond, Playfair Display, EB Garamond, IvyPresto, Migra, Editorial Old, Saol Display, Domaine Display, Canela, Schnyder, Tobias, ITC Galliard.
- Serif is always wrong in dashboards and dense software UI.

### Emphasis inside headlines
Emphasize a word with italic or bold of the same family. Do not inject a serif word into a sans headline (or the reverse) for visual interest. Mixed-family emphasis reads as amateur.

### Italic descender clearance (mandatory)
Italic display words containing `y g j p q` get clipped by `leading-none`. Use `leading-[1.1]` minimum and reserve `pb-1` or `mb-1` on the wrapper. Audit every italic display word before shipping.

### Numbers
Data-heavy layouts (`VISUAL_DENSITY` 8+) use `font-mono` or `font-variant-numeric: tabular-nums` for every number.

## 2. Color

### Core rules
- Maximum one accent color. Saturation below 80% by default.
- Neutral bases (Zinc, Slate, Stone) with one high-contrast accent (emerald, electric blue, deep rose, burnt orange, and so on).
- One gray family per project. Do not mix warm and cool grays.
- No pure `#000000` and no pure `#ffffff`. Off-black and off-white keep depth.
- When a shadow is used, tint it toward the background hue. No pure-black drop shadows on light backgrounds.
- No neon or outer glows by default. Use inner borders or subtle tinted shadows.
- No gradient text on large headers.

### The purple rule
The "AI purple-blue glow" aesthetic is discouraged as a default: no automatic purple button glows, no random neon gradients. Override: if the brand is already purple or violet, embrace it and execute with intent (consistent palette, harmonised neutrals, restrained gradients).

### Color consistency lock (mandatory)
Once an accent is chosen it is used identically across the whole page. A warm-gray site does not get a blue CTA in section seven. A rose-accented site does not get a teal badge in the footer. Audit every component before shipping.

### Premium-consumer palette ban (mandatory)
For cookware, wellness, artisan, luxury, heritage craft, and DTC home-goods briefs the LLM default is warm cream + brass or clay or oxblood + espresso text. Banned as default hex families:

- Backgrounds: `#f5f1ea`, `#f7f5f1`, `#fbf8f1`, `#efeae0`, `#ece6db`, `#faf7f1`, `#e8dfcb`
- Accents: `#b08947`, `#b6553a`, `#9a2436`, `#9c6e2a`, `#bc7c3a`, `#7d5621`
- Text: `#1a1714`, `#1a1814`, `#1b1814`

Rotate through alternatives instead; never ship the same family twice in a row:

- Cold luxury: silver-gray + chrome + smoke
- Forest: deep green + bone + amber accent
- Black and tan: true off-black + warm tan, no beige
- Cobalt + cream: saturated blue against one neutral, no brass
- Terracotta + slate: warm rust against cool gray
- Olive + brick + paper: muted olive with a brick-red accent
- Monochrome + one pop: off-white, off-black, one bright accent

Override: cream + brass is acceptable only when the brand names those colors, or the identity is genuinely vintage or warm-craft and you can articulate why.

## 3. Shape consistency lock (mandatory)

Pick one corner-radius system per page: all sharp (0), all soft (12-16px), or all pill for interactive elements. Mixed systems are allowed only under a documented rule ("buttons pill, cards 16px, inputs 8px") applied everywhere. Round buttons in a square layout, or square cards on a pill-button page, is broken design.

## 4. Cards and materiality

- Use cards only when elevation communicates real hierarchy. Otherwise group with `border-t`, `divide-y`, or negative space.
- At `VISUAL_DENSITY` above 7, generic card containers are banned; metrics breathe in plain layout.
- Glassmorphism, when the design read calls for it (premium consumer, media overlays, Apple-adjacent), goes beyond `backdrop-blur`: add a 1px inner border (`border-white/10`) and an inner highlight (`shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]`). Provide a solid fallback under `prefers-reduced-transparency`. Not for dashboards, public sector, or plain B2B.

## 5. Page theme lock (mandatory)

The page has one theme. Sections do not invert.

- If the page is dark, every section is dark. No warm-paper light section sandwiched between dark ones, and the reverse.
- Tints within the same family are fine (`bg-zinc-950` next to `bg-zinc-900`). Flipping to `bg-amber-50` inside a `bg-zinc-950` page is broken.
- Exception: a brief that explicitly asks for one deliberate "color block" theme switch, once per page, with a strong transition.
- With Radix Themes or shadcn/ui, set the theme once at the layout root. Sections never override it.

## 6. Dark mode protocol

Dual-mode by default for any consumer-facing page. Never ship light-only or dark-only without explicit instruction (print-emulating editorial is the usual exception).

- Token strategy, pick one per project: Tailwind `dark:` variants on every color utility (`bg-white dark:bg-zinc-950`), or CSS variables with semantic tokens (`--surface`, `--surface-elevated`, `--text-primary`, `--accent`) swapped under `[data-theme="dark"]` or `@media (prefers-color-scheme: dark)`.
- This skill does not prescribe dark-mode hex values. It enforces: WCAG AA contrast minimum for body text (AAA target for hero copy), hierarchy parity (a CTA that pops in light pops in dark), brand fidelity (do not desaturate the brand away), no pure black or white.
- Default to `prefers-color-scheme`. Add a manual toggle only if either mode would lose key brand expression.
- Open the page in both modes during development. Never ship a page seen in only one.
