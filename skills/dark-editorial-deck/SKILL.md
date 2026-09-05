---
name: dark-editorial-deck
description: Use when asked to build a talk, keynote, workshop or product-walkthrough as a web page (HTML/React) rather than PowerPoint — a hash-routed, keyboard-driven, 16:9 stage that scales with the window, one sentence per slide, live product mocks instead of images, and a mono HUD of key hints. Orchestrates quiet-dark-tokens, plain-instruction-voice, product-mock-illustration and restrained-product-motion into one deck; ships a starter template.
---

# Purpose

Turn a talk into a single-page web deck that looks like a well-set editorial
spread on a dark screen: large regular-weight titles, generous space, a
few living UI mocks, and almost no chrome. This skill is the assembly
guide; the four companion skills supply tokens, voice, graphics and motion.

# When to Use

- "Make me a deck / slides / a talk site for ___" where the audience will
  watch it on a projector or share a URL afterwards.
- Converting an outline or a PowerPoint into something presentable in a
  browser.
- A product 101, onboarding walkthrough or workshop that benefits from
  keyboard-driven, sectioned pacing.

Not for long-form scrolling articles (use a scroll-page skill), nor for
decks that must be exported to .pptx (use a pptx skill).

# Inputs

- Outline or transcript; the single outcome the audience should leave with.
- Cast of products/agents/people that recur.
- Optional: sections (the deck supports numbered sections jumpable by key).

# Outputs

- `index.html` (or a Vite/React app) with: hash routing (`#12`), ←/→ and
  1–9 section keys, `N` notes toggle, `F` fullscreen, a bottom-left HUD of
  key chips, a bottom-right mono counter `Section · 12 / 28`.
- One slide per idea; speaker notes as hidden `<aside>` per slide.

# Deck architecture

```
.deck            grid: 1fr auto; height 100%; background #080808
 ├ .stage-wrap   place-items:center; padding 20px 20px 6px; overflow hidden
 │  └ .stage-box (aspect 16/9, sized by JS to fit)  → .stage (1920×1080 logical,
 │                transform:scale(k); padding 45px 62px; container-type:inline-size)
 │                 └ .slide  flex column; gap 20px; h1/h2 first, then one flexible child
 └ .hud          flex; key chips left, counter right; 12px mono; --dim
```

- The stage is a fixed 1920×1080 canvas scaled with `transform:scale()`
  to fit the window, so layout never reflows; type uses `cqw` so it tracks
  the stage.
- Content sits in the upper-middle: title starts ~28% down, not centred
  vertically — the lower third stays airy.
- Left margin 62px on the stage; titles flush to it. Nothing centred except
  full-bleed statement slides.

# Slide archetypes (use only these)

| Archetype | Layout | Notes |
|---|---|---|
| **Title** | grid `1.05fr .95fr`; h1 left with one blue word + byline; a mock stack right | Opens the deck and each act |
| **Statement** | h2 alone, or h1 for a 3-line question | The slide *is* the sentence. Nothing else |
| **Title + mock** | h2 then one window/mock at 55–75% width | The workhorse |
| **Title + spec rows** | h2, optional tab pills, 5 full-width label/value rows | For "write it in five parts" content |
| **Three cards** | h2, three `--panel` cards with mascot + name + mono eyebrow + note, one callout bar beneath | Comparisons, roles |
| **Two takeaways** | two large cards, each a mono label + 40px display sentence | Section summary |
| **Comparison table** | h2, mono-headed table, ≤ 6 words per cell, dated note | Always carries a date |
| **Close** | h2 imperative + one final mock or nothing | Ends with an action |

# Procedure

1. **Outcome first.** Write "By the end you will have ___" — it becomes
   slide 3 and the filter for every other slide.
2. **One sentence per slide.** Convert the outline into ≤ 30 titles using
   `plain-instruction-voice`. Group into 2–4 sections; sections get number
   keys.
3. **Assign an archetype** to each slide from the table. If a slide needs
   two archetypes, split it.
4. **Cast the mocks.** For each Title+mock slide write the mock's copy
   before its markup (`product-mock-illustration`). Reuse the same 3–6
   mascots.
5. **Drop in tokens** (`quiet-dark-tokens`) and the stage scaffold from
   `templates/deck-starter.html`. Build slides as `<section class="slide">`.
6. **Motion**: title/mocks `rise-in` on slide change; ambient loops only on
   mocks that stay >10s (`restrained-product-motion`). Slide change itself
   is a cut (no cross-fade) — content entrance provides the motion.
7. **HUD**: key chips `← Prev · → Next · N Notes · F Fullscreen · 1 Intro
   · 2 <Section>…`; counter right. HUD is `--dim` mono 12px, never brighter.
8. **Notes**: `N` reveals a `--panel` drawer at the bottom with the current
   slide's `<aside>`.
9. **Test**: 1280×720 and 2560×1440 windows, keyboard only, reduced
   motion on, projector contrast (dim text still ≥ 4.5:1).

# Quality Checklist

- [ ] ≤ 30 slides; every title ≤ 9 words with a full stop.
- [ ] Every slide uses one archetype; no bullet lists anywhere.
- [ ] No images except mascot SVGs and one optional wordmark on the title.
- [ ] Stage scales with `transform`, not media queries; type in `cqw`.
- [ ] Hash routing works on reload; ←/→, number keys, N, F all bound.
- [ ] HUD present, dim, mono; counter shows `Section · n / total`.
- [ ] Companion checklists (tokens, voice, mocks, motion) all pass.

# Edge Cases

- Speaker needs a light room → do not invert the palette; raise `--dim` to
  `#a3aab5` and increase title size one step.
- Must embed a live demo → open it in a new tab from a key chip; never
  iframe inside the stage.
- Scrolling landing page instead of a deck → read `references/scroll-page-variant.md`.
- Needs PDF export → add `@media print{.stage{transform:none}.slide{page-break-after:always}}`
  and print at 1920×1080.

# Safety Rules

- Do not embed API keys or private URLs in a deck that will be deployed.
- Any claim about third-party products carries a date and a "check current
  docs" note.

# Examples

Outline line: "Explain that the bot asks before irreversible actions."
→ Slide (Title + mock): "Set what it has to ask before doing." with a
settings window where only "Ask before sending" is on, and an approval
card overlapping: "STOPPED BEFORE SENDING · Send this reply to Acme? · Not
yet · Send".
