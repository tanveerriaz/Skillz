# Web Reference: Landing Pages, Marketing Sites, Section Comps

Read this after choosing the web surface. Shared rules (one system, readability, anti-generic) live in SKILL.md; this file holds the web-specific decisions and prompt template.

## 1. Output Rules

- One separate **horizontal** image per section. Never a tall full-page image, never a collage, never "one best image" for several sections.
- Aspect ratio: hero 16:9 or 21:9; content sections 16:9 or 16:10.
- Label each output "Section X of N: name".
- Default counts when the brief gives none:
  - hero → 1
  - landing page / site template / product page / portfolio → 6
  - full website / marketing site → 8
- If the generator renders one image per call, run the calls back to back in the same response until N is reached.

### Default section packs

| Pack | Sections |
|---|---|
| 4 | Hero, Features, Social proof, CTA |
| 6 | Hero, Trust bar, Features, Product showcase, Testimonials, CTA |
| 8 | Hero, Trust bar, Features, Product showcase, Benefits / use cases, Testimonials, Pricing, CTA |
| 12 | Hero, Trust bar, Feature grid, Product preview, Problem / solution, Benefits, Workflow, Metrics / proof / integration, Testimonials, Pricing, FAQ, CTA + footer |

Every section has a job: hook, prove, educate, or convert. The final section closes with one strong CTA and one trust cue.

## 2. Brief-to-Direction Mapping

Read the brief's style words and bias picks accordingly. The brief always overrides defaults.

| Brief says | Hero scale | Backgrounds | Gradients | Composition |
|---|---|---|---|---|
| minimalist, clean, swiss, typography-only | Mini | solid surfaces, subtle texture, one color-blocked diptych at most | skip or softest tonal | stacked center, generous negative space; suspend the full-bleed rule |
| editorial, magazine, fashion, art-directed | Mid or Giant | editorial side-image, duotone photo, graded photo | subtle tonal | off-grid offsets, asymmetric pulls, strong type contrast |
| cinematic, atmospheric, luxury, premium, bold | Giant | full-bleed image + tonal overlay, radial vignette + product, micro-noise gradient | palette-matched, welcome | bottom-left over image, centered low, image-as-canvas |
| SaaS, product, dashboard, fintech, infra | Mid | solid + inline asset, flat block + detail crop | very subtle | clear product framing, trust anchors, higher clarity |
| agency, studio, portfolio | Giant or Mini (decide) | vary boldly: full-bleed, diptych, duotone | editorial washes OK | off-grid, poster-like |
| e-commerce, shop, product page | Mid, product-led | full-bleed product photo, vignette + crop | never competing with product | product first; CTAs unmistakable |
| silent | pick one decisively | confident variety | subtle | mixed anchors |

Steer palette and type temperament to the named industry or region; do not ship a default neutral startup look unless the brief is intentionally generic SaaS.

## 3. System Choices (lock once per site)

Pick one from each list and keep it across every section image.

**Theme**
1. Pristine light — off-white, cream, paper; sharp dark text.
2. Deep dark — charcoal, graphite, zinc; glow only when justified.
3. Bold studio solid — oxblood, royal blue, forest, vermilion, emerald with crisp contrasting UI.
4. Quiet premium neutral — bone, sand, taupe, stone; restrained contrast.

**Typography character**
1. Clean grotesk  2. Refined grotesk  3. Expressive display  4. Compressed statement  5. Editorial serif + sans  6. Swiss rational sans with strong hierarchy

**Hero scale** (one per site; match brand mood)
- Giant statement — massive type, large image, dominant first viewport.
- Mid editorial — balanced type/image, cinematic but not screen-filling.
- Mini minimalist — small logo, short statement, thin CTA, mostly negative space. Mini means confident restraint, not weakness.

**Section system** (dominant structure)
1. Modular bento rhythm  2. Alternating editorial blocks  3. Poster-like stacked storytelling  4. Gallery-led cadence  5. Swiss grid discipline  6. Asymmetric marketing flow

**Signature components** (choose exactly 4, use across the site)
Diagonal staggered square masonry · 3D cascading card deck · hover-accordion slice row · gapless bento grid · brand marquee strip · turning polaroid arc · vertical rhythm lines · off-grid editorial layout · product UI panel stack · split testimonial quote wall · oversized metrics strip · layered image crop frames

**Narrative spine** (choose 1; thread through visuals and copy)
Artifact/collectible · journey/waypoints · precision instrument · living system/garden · stage/spotlight · archive/dossier

**Second-read moment** (exactly 1, placed once on the page)
Asymmetric bleed that respects hierarchy · one oversized numeral or punctuation mark serving structure · one material switch (paper vs gloss vs metal) · narrow vertical side-rail note · macro crop carrying brand color. It must aid scan order or brand recall, not decorate.

**Motion-implied cues** (exactly 2; visual hints, not code)
Scrubbing text reveal · pinned narrative · staggered float-up · parallax drift · accordion expansion · cinematic fade-through

## 4. Per-Section Choices (vary these)

**Composition anchor** — each section picks one; at least 3 different anchors per site; never the same anchor more than twice in a row.
- Centered statement
- Top-left lead, support bottom-right
- Bottom-left text over background image
- Bottom-right CTA cluster
- Left-third caption + right-two-thirds visual (the overused default — use sparingly, never twice in a row)
- Right-third caption + left-two-thirds visual
- Centered low (text in lower 40% over image)
- Off-grid editorial offset
- Stacked center (label / headline / sub / CTA)
- Image-as-canvas with text in a clean safe area

**Background mode** — pick one per section; never the same mode more than three in a row.
Solid + inline asset · subtle texture/paper/grid · full-bleed image + tonal overlay · editorial side-image (50/50, 60/40, 40/60) · image-as-canvas · flat color block + detail crop · cinematic tonal gradient · atmospheric single-tone graded photo · duotone photo · radial vignette + product crop · micro-noise gradient over solid · color-blocked diptych

**CTA style** — vary at least once per site; primary action stays unmistakable.
Primary pill · outline/ghost · underlined inline link with arrow · full-width banner · oversized headline + tiny CTA hint · CTA as caption under a strong visual

**Section size** — mix large art-directed, medium editorial, and mini near-empty sections so the scroll has rhythm.

**Cross-section contrast** — vary background intensity at least twice across the page (lighter → richer → calmer).

For non-minimalist briefs, include at least one full-bleed (or duotone/atmospheric) background and at least one mini minimalist section in any multi-section site.

## 5. Hero Rules

- Before rendering, ask: "Am I drafting text-left / image-right out of habit?" If yes, pick another anchor unless the brief truly needs the classic.
- Headline: 5–10 strong words, 1–3 lines. Reduce words rather than add lines.
- One focal point. Short supporting text. One obvious primary action.
- No pills, fake stats, badge rows, tiny logo strips, or pseudo-system labels ("00 orchestration layer") in the first viewport.
- The hero usually carries a strong visual: product, art-directed photo, or media element.
- The first view must still read cleanly at a small laptop width: headline, supporting text, CTA, focal visual, nothing else competing.

## 6. Typography, Spacing, Color, Imagery

**Typography**
- Clear size contrast, obvious reading order, strong display moments, brief supporting text.
- Prefer medium/normal/light weights, tight tracking, controlled line counts.
- Avoid extra-bold everywhere, gradient text, 6-line headings, lazy all-caps, more than two type moods.

**Spacing**
- Leave more space between sections than a default render would; keep section gaps even and controlled.
- Separate dense sections with calm ones. Small sections still get generous surrounding space.
- No cramped section next to an empty one; no filling every gap.

**Color**
- One palette: 1 primary, 1 secondary, 1 accent (CTA/highlight only), one neutral scale. No per-section theme swaps.
- Full-bleed images must tonally match the palette; use overlays so text stays readable; accent color stays constant regardless of image.
- Allowed gradients: low-chroma palette-matched tonal (ink→graphite, cream→sand), single-hue grades behind photos, soft vignettes, noise-textured depth, editorial washes.
- Banned gradients: rainbow/mesh blobs, purple→blue, pink→orange, neon halos, gradient text, anything competing with imagery.
- Materials (paper, glass, brushed metal, matte, soft blur) are welcome when the structure stays readable.

**Imagery**
- Images are structural, not decoration: art-directed product shots, editorial photography, framed panels, layered crops, UI crops with purpose.
- Several sections in a multi-section site should carry meaningful imagery; mix at least two distinct crop types (macro + environment, portrait + widescreen).
- Media sits in fixed-aspect, repeatable frames with consistent radius.
- Avoid tiny thumbnails, stock clichés, irrelevant scenery, one hero image then text-only pages, fake dashboards standing in for real visuals.
- Charts and KPI strips only when the site type needs them (analytics, infra, pricing). Otherwise keep proof human: quotes, timelines, real workflow screenshots.
- Skip unreadable "trusted by" logo tickers and three identical stat columns unless requested.

## 7. Component Execution Notes

- **Staggered square masonry:** square blocks, strong vertical stagger, curated not messy.
- **Cascading card deck:** physical stack with depth logic; tactile, not gimmicky.
- **Accordion slice row:** compressed slices that read as expandable through proportion and emphasis.
- **Gapless bento:** mathematically clean grid, large visual blocks mixed with small dense panels, no accidental gaps.
- **Polaroid arc:** clustered rotated imagery, styled and intentional.
- **Off-grid editorial:** asymmetry with control; still readable and structured.
- **Product UI panel stack:** layered interface crops telling a product story; not a fake dashboard.
- **Vertical rhythm lines:** fine rules reinforcing order; never clutter.

## 8. Prompt Template (per section)

```
Website section reference image, horizontal [16:9 | 21:9 | 16:10], one section only.
Section: [X of N — name]. Job: [hook | prove | educate | convert].
Brand: [product, audience, tone]. Theme: [theme]. Palette: [primary, secondary, accent, neutrals — identical across all sections].
Typography: [character]; headline [n] lines max; supporting text brief.
Composition anchor: [anchor]. Background mode: [mode]. CTA style: [style].
Hero scale (site-wide): [giant | mid | mini]. Section size: [large | medium | mini].
Imagery: [what the image shows, crop type, treatment/grade, frame ratio].
Signature component in this section: [one of the 4].
Narrative spine: [spine]. Second-read moment: [only if this is the chosen section].
Copy: [headline], [sub], [CTA label] — short, believable, no filler words, no fake wordmarks.
Style: implementation-friendly UI comp, clear hierarchy, generous even spacing, readable text.
Exclude: purple-blue gradients, glowing blobs, glass stacks, nested cards, pill clutter, fake stats, logo tickers, gradient text.
```

## 9. Web Checklist

- [ ] N images for N sections, every one horizontal and single-section.
- [ ] Hero scale chosen and executed; hero is not a reflexive text-left / image-right.
- [ ] At least 3 anchors used; no anchor more than 2 in a row; no background mode more than 3 in a row.
- [ ] At least one full-bleed/duotone/atmospheric section and one mini section (non-minimalist briefs).
- [ ] CTA style varied at least once; primary action unmistakable in every convert section.
- [ ] Palette, type family, radius, image treatment identical across all images.
- [ ] Section spacing even; page breathes; no cramped/empty whiplash.
- [ ] Exactly one second-read moment; narrative spine visible without clutter.
- [ ] Conversion path readable: hook → proof → action.
- [ ] No AI slop in layout, visuals, typography, copy, or density.

## 10. Example Interpretations

- **"Hero for an AI startup"** → 1 image; mid or giant hero; bottom-left text over full-bleed atmosphere/product image with dark tonal overlay; outline CTA + small label; deep dark or bold studio theme; no dashboard spam, no purple glow.
- **"8 sections for a fintech site"** → 8 images; mid hero; anchors rotate (centered low, right-third caption, bottom-left over chart visual, stacked center for closing CTA); backgrounds mix solid, one full-bleed, editorial side-image at use cases; ink + paper + one accent; path hook → proof bar → features → use case → testimonial → pricing → FAQ → CTA.
- **"Creative agency, 12 sections"** → 12 images; giant or mini hero (decide); off-grid appears 2–3 times; full-bleed at hero and showcase, side-image at case studies, solid + accent for process; one bold recurring accent; closing CTA is mini minimalist with a single action.
