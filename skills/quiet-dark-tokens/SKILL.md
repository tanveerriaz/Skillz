---
name: quiet-dark-tokens
description: Use when styling any dark-mode web surface (deck, landing page, dashboard, app shell) that should look calm, premium and near-monochrome — one near-black ground, off-white text, a single accent blue, hairline borders, translucent panels, a display sans for headlines and a mono for labels. Gives the exact token set, type scale, radii, shadows and the rules for applying them so the output never drifts into gradient-heavy "AI aesthetic".
---

# Purpose

Encode one specific visual system — quiet, dark, editorial — as copy-pasteable
design tokens plus the rules for using them. The system is defined by
restraint: almost everything is a shade of the same off-white on the same
near-black, and colour appears only to mean something (a highlighted word, a
"stopped" state, a success tick, an error).

# When to Use

- Building a slide deck, talk site, landing page or product demo that should
  feel like a well-set magazine page on a dark screen.
- Skinning a product mock (chat UI, notification stack, settings panel) that
  sits inside such a page.
- Reviewing existing dark UI that "looks AI-generated" and pulling it back to
  something calmer.

Do not use for brand-heavy marketing pages that need a warm or saturated
palette, or for data-dense dashboards that need many categorical colours.

# Inputs

- The surface being built (deck / page / component) and its container width.
- Optional: one accent colour if the default blue is not wanted (keep it one).

# Outputs

- A `:root` token block (see `references/tokens.css`) dropped into the project.
- Components that only reference tokens — no hard-coded colours in rules.

# The tokens

```css
:root{
  --bg:#080a0d;                       /* page ground — blue-black, not pure black */
  --paper:#f3f5f7;                    /* primary text */
  --soft:#c1c6ce;                     /* secondary text, sub-headlines */
  --dim:#89919d;                      /* metadata, timestamps, mono labels */
  --line:rgba(243,245,247,.14);       /* every border is this hairline */
  --panel:rgba(243,245,247,.045);     /* card fill */
  --panel-hi:rgba(243,245,247,.075);  /* hover / raised card / pill fill */
  --blue:#80adff;        --blue-soft:rgba(128,173,255,.13);   /* accent + tint */
  --green:#70d6a3;       --green-soft:rgba(112,214,163,.12);  /* success, "done" */
  --red:#f08276;         --red-soft:rgba(240,130,118,.12);    /* danger, "undo?" */
  --display:"Universal Sans Display",ui-sans-serif,system-ui,sans-serif;
  --sans:"Universal Sans Text",ui-sans-serif,system-ui,sans-serif;
  --mono:"Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}
html,body{background:var(--bg);color:var(--paper);font-family:var(--sans);-webkit-font-smoothing:antialiased}
```

Font substitutes when the originals are unavailable: `Inter Display` /
`Inter Tight` for display, `Inter` for text, `Geist Mono` / `JetBrains Mono`
for mono. Never fall back to a serif or a rounded/geometric novelty face.

# Type scale

| Role | Face | Weight | Size | Tracking | Leading |
|---|---|---|---|---|---|
| Hero title (h1) | display | 400 | `clamp(70px, 8.5cqw, 124px)` | `-.05em` | `.96` |
| Slide / section title (h2) | display | 400 | `clamp(32px, 3.6cqw, 50px)` | `-.05em` | `.96` |
| Big statement in a card | display | 400 | `clamp(34px, 3.2cqw, 46px)` | `-.03em` | `1.08` |
| Plain note / lede | display | 400 | `clamp(20px, 1.9cqw, 27px)` | `-.02em` | `1.3` |
| Body / UI text | sans | 400 | 14–18px | `0` | `1.4–1.5` |
| Emphasis in UI | sans | 550 (or 500) | same as body | `0` | — |
| Eyebrow / label | mono | 500 | 12–13px | `.08em`, `uppercase` | `1` |
| Timestamps, counters, key hints | mono | 400 | 12–14px | `0` | `1` |

Rules:
- Headlines are **regular weight**, large, and tight. Weight is not how you
  make a headline heavy — size and tracking are. Never bold a headline.
- Exactly one word or number in a hero title may be `color:var(--blue)`.
  That is the only decorative colour on a title slide.
- Titles are set flush-left with `max-width` ≈ 30ch so they wrap into two
  or three deliberate lines.
- Labels are mono, uppercase, letter-spaced, and coloured `--blue` when they
  name a field (OUTCOME, SOURCES, CONSTRAINTS) or `--dim` when they are
  metadata.
- Use `cqw` (container query units) for anything on a scaled stage so the
  type tracks the slide, not the viewport.

# Surfaces

- Card: `border:1px solid var(--line); background:var(--panel); border-radius:16–22px; padding:16–36px`.
- Raised / hovered card: swap fill to `--panel-hi`. No border colour change.
- Callout / "stop" state: `background:var(--blue-soft); border:1px solid rgba(128,173,255,.36)`.
- Success chip: `--green-soft` fill, `--green` text. Danger: `--red-soft` / `--red`.
- Pill: `border-radius:999px; padding:5px 10px; font:500 13px/1 var(--mono); background:var(--panel-hi); color:var(--soft)`.
- Keyboard chip: `border:1px solid var(--line); border-radius:5px; padding:3px 7px; font:400 12px/1 var(--mono); color:var(--dim)`.
- Floating window / notification mock: opaque fill `#262626eb`, `border-radius:18px`, `box-shadow:0 24px 70px #0008`.
- Sidebar / secondary pane: `#181818`–`#1a1a1a` solid, separated by a `--line` hairline, never a shadow.

Radii by size: 5px (key chips) · 8–10px (inputs, inline tags) · 12–14px
(list rows, avatars in squares) · 16–18px (cards, windows) · 20–22px (large
feature cards) · 999px (pills) · 50% (dots, avatars).

Shadows exist only to lift a floating object off the ground and are always
soft and far: `0 24px 70px rgba(0,0,0,.5)` to `0 28px 80px rgba(0,0,0,.53)`.
Flat cards on the page get **no** shadow — the hairline border does the work.

# Procedure

1. Paste the token block; set `html,body` ground and text once.
2. Set the four type roles (h1, h2, note, label) as global rules before
   building any component.
3. Build every surface from `--line` + `--panel`/`--panel-hi`. If you reach
   for a hex value inside a component, stop and ask which token it is.
4. Add colour last, and only where it carries meaning: one accent word,
   field labels, success/danger states, an active tab (`--blue-soft` fill).
5. Run the checklist.

# Quality Checklist

- [ ] No gradients anywhere except inside illustrated mascots/icons.
- [ ] No glassmorphism (`backdrop-filter`) on cards.
- [ ] At most one accent hue on screen besides green/red status.
- [ ] Every border is `var(--line)`; every card fill is `--panel` or `--panel-hi`.
- [ ] Headlines are weight 400 with negative tracking; no bold headlines.
- [ ] Mono is used only for labels, timestamps, counters and key hints.
- [ ] Contrast: `--dim` on `--bg` is the floor (~4.5:1); never go dimmer for text.
- [ ] Background is `#080a0d`, not `#000`.

# Edge Cases

- Light-mode requirement → do not invert these values; use
  `references/light-variant.css` (warm bone ground, off-black text, same
  structure and rules).
- Brand demands a saturated accent → keep the structure, swap `--blue` and
  `--blue-soft` only; do not add a second accent.
- Data visualisation → pull in a categorical palette from a dataviz skill;
  keep chart chrome (axes, grid) on `--line`/`--dim`.

# Safety Rules

- Do not copy proprietary font files; reference by name with fallbacks and
  let the project license fonts.
- Do not lift logos, wordmarks or mascot artwork from reference sites.

# Examples

Good: a title slide — black-blue ground, 110px regular headline with one blue
word, a 20px `--soft` byline, and one floating notification card at the right
with a 70px soft shadow. Nothing else.

Bad: the same slide with a purple-to-blue gradient headline, three glowing
cards with frosted glass, and an icon next to every line.
