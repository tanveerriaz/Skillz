# Layout, Hero, Imagery, Content, and States

Read this when composing sections, writing the hero, choosing images, trimming copy, or wiring UI states.

## 1. Hero discipline (hard rules)

- **Fits the initial viewport.** Headline max 2 lines on desktop, subtext max 20 words and 3-4 lines, CTAs visible without scroll. Too much copy means reduce scale or cut copy. A value proposition that needs more than 20 words is unclear.
- **Font scale planned with the asset.** Default range `text-4xl md:text-5xl lg:text-6xl`. Use `text-6xl md:text-7xl` only when the headline is 3-5 words. A 4-line hero headline is a font-size error.
- **Top padding cap `pt-24`** at desktop. Content floating halfway down reads as a bug. Need more air? Increase type or asset size, not padding.
- **Max 4 text elements:** (1) eyebrow or brand strip or neither, (2) headline, (3) subtext, (4) CTAs (one primary, at most one secondary).
- **Banned inside the hero:** tagline under the CTAs ("Works with GitHub, GitLab..."), trust micro-strip, pricing teaser, feature bullets, social-proof avatar row. All of these move to a section directly below.
- **Logo wall lives under the hero,** never inside its flex row.
- **Hero needs a real visual.** Text + gradient blob is a placeholder, not a hero.
- **Anti-center bias:** centered hero is avoided when `DESIGN_VARIANCE > 4`. Use split screen, left content + right asset, asymmetric whitespace, or scroll-pinned structures. Centered is fine for editorial, manifesto, and launch-announcement briefs where the message is the design.

## 2. Navigation

- Renders on one line at desktop. If items do not fit at 1024px, condense labels, drop secondary items, or move to a menu.
- Height 64-72px by default, 80px maximum. No oversized "agency" bars.

## 3. Section composition

- **Layout family repetition ban.** A layout family (three-column cards, full-width quote, split text + image) appears at most once per page. Eight sections need at least four families.
- **Zigzag cap.** Max 2 consecutive image + text splits. The third in a row fails pre-flight. Break with a full-width section, vertical stack, bento, marquee, or another family.
- **Split-header ban.** "Big headline left, small explainer paragraph right" as a section header is banned by default. Stack headline above body (max 65ch). Use the split only when the right column carries a visual or interactive element.
- **Eyebrow restraint (the most violated rule).** An eyebrow is the small uppercase wide-tracked label above a headline (`text-[11px] uppercase tracking-[0.18em]`). Max 1 eyebrow per 3 sections; the hero counts as one. If section A has one, the next two cannot. Mechanical check: count `uppercase tracking` labels above headlines; if count > ceil(sections / 3), fail. The usual fix is to delete it; the headline is enough.
- **Mobile collapse declared per section.** Every multi-column layout states its `< 768px` fallback in the same component.

## 4. Bento and feature grids

- Rhythm, not repetition: alternate full-width rows, asymmetric tiles, vertical breaks. Never six identical left-image right-text rows.
- Exact cell count: 3 items = 3 cells (1+2, 2+1, asymmetric trio); 5 items = 5 cells (2+3, hero+4). An empty cell means the grid was planned wrong. Reshape it; never paste a blank tile.
- Background diversity: at least 2-3 cells carry real visual variation (image, brand-appropriate gradient, pattern, tint). Six white-on-white text cards read as default output.
- No three equal feature cards. Use a 2-column zig-zag (within the cap), asymmetric grid, scroll-pinned, or horizontal scroll.

## 5. Images and visual assets

Landing pages and portfolios are visual products. Text-only pages with fake screenshot divs are slop.

Priority order:
1. **Image generation tool first.** If any image tool is available, generate section-specific assets (hero photography, product shots, textures) at the right aspect ratio.
2. **Real web images second.** `https://picsum.photos/seed/{descriptive-seed}/{w}/{h}` with a seed describing the section, brand URLs supplied in the brief, or open-license sources when allowed.
3. **Last resort: labelled slots.** `<!-- TODO: hero product photo, 1600x1200 -->` and a closing note listing every placement that needs a real image. Do not fill the gap with hand-drawn SVG illustrations or div-built "screenshots".

Rules:
- Even minimalist sites need 2-3 real images (hero, one product or lifestyle shot, one supporting image). Generate restrained black-and-white photography if the brief is quiet.
- **Logo walls use real SVG logos**: Simple Icons (`https://cdn.simpleicons.org/{slug}/{hex}`), or devicon for tech stacks. For invented brands, generate a simple SVG monogram in the page style rather than a plain text wordmark. Logos must render in both themes.
- **Logo-only rule:** no industry or category label under each logo. Alt text and an optional link are enough.
- **Div-based fake screenshots are banned** (fake task lists, fake terminals, fake dashboards). Use a real screenshot, a generated image, a real mini component preview, or editorial photography.
- Hand-rolled decorative SVGs only when the brief asks, or for a single simple geometric mark you are confident in.
- Icons come from a library (see `stack-conventions.md`); never draw icon paths by hand.

## 6. Content density

Landing pages live on the first impression. Cut ruthlessly.

- Default section shape: headline up to 8 words, sub-paragraph up to 25 words, one visual or one CTA. More must be justified by the section's job.
- No data-dump sections (20-row tables, 30-row award lists, giant pricing matrices). Use the top 3-5 highlights + "View full list", a marquee or carousel for breadth, or a separate page if the data is the product.
- Lists over 5 items need a different component, not a longer list: two-column grouped split, card grid with image + label, tabs or accordion for categories, horizontal scroll-snap pills, carousel, marquee.
- **Spec sheets** (cookware, hardware, apparel, artisan goods): a long table with `border-b` on every row is the AI default and is banned. Use a 2-column spec card grid (name, large value, one-line "why it matters"), scroll-snap pills, 3 grouped clusters with one soft divider each, or 3-4 hero specs as display tiles with the rest under a disclosure.
- One copy register per page. Do not mix technical mono metadata, editorial prose, and marketing punch unless the brand voice calls for it.
- Fake-precise numbers (`92%`, `4.1×`, `5.8 mm`) are fine only from real data or when marked as sample data. AI-invented spec precision is banned.

### Copy self-audit (mandatory before shipping)
Re-read every visible string: headlines, eyebrows, buttons, body, captions, alt text, footer, errors. Rewrite anything grammatically broken, with an unclear referent, or that reads like an LLM trying to sound thoughtful (mock-humble asides, forced metaphors, faux-craftsman labels). A plain functional sentence beats a clever one that does not track.

## 7. Quotes and testimonials

- Max 3 lines of quote body. Cut longer originals; a landing-page quote is a snippet.
- Attribution is name + role (+ company). Never name only.
- Use typographic quotation marks or none. No em-dashes anywhere in quotes or attribution (see `anti-patterns.md`).

## 8. CTAs

- **No duplicate intent.** "Get in touch", "Contact us", "Let's talk", "Start a project" are all "contact". Pick one label and use it in nav, hero, and footer. Same for signup intent ("Try free", "Get started") and portfolio intent ("View work", "Browse projects").
- **No wrapping at desktop.** A CTA label on 2+ lines is broken: shorten to 1-3 words or widen the button.
- **Contrast check.** Every button's text passes WCAG AA against its own background (4.5:1, or 3:1 for 18px+). White-on-white, transparent-on-page with no border, and ghost buttons over photos without a scrim are banned.
- Tactile feedback: `:active` uses `-translate-y-[1px]` or `scale-[0.98]`.

## 9. Forms and UI states

- Label above input, helper text present in markup, error text below, `gap-2` between blocks. Never placeholder-as-label.
- Form contrast: inputs, placeholders, focus rings, helper and error text all pass WCAG AA against the section background.
- Always implement the full cycle: skeleton loaders shaped like the final layout (no generic spinners), composed empty states that show how to populate, inline error states for forms and toasts only for transient messages.

## 10. Layout mechanics

- Breakpoints: `sm 640`, `md 768`, `lg 1024`, `xl 1280`, `2xl 1536`.
- Contain pages with `max-w-[1400px] mx-auto` or `max-w-7xl`.
- Full-height sections use `min-h-[100dvh]`, never `h-screen` (iOS Safari address-bar jump).
- Grid over flex math: never `w-[calc(33%-1rem)]`; use `grid grid-cols-1 md:grid-cols-3 gap-6`.
- Z-index only for systemic layers (sticky nav, modals, overlays, grain). Document the scale in a constants file; no scattered `z-50`.

## 11. Pattern vocabulary

Names to design and communicate with. Reach for them only when the design read calls for it.

- **Heroes:** asymmetric split; editorial manifesto (type only); video or media mask (type as a window); kinetic type; curtain reveal; scroll-pinned.
- **Navigation:** dock magnification; magnetic button; gooey menu; dynamic-island status pill; radial menu; floating speed dial; mega-menu reveal with staggered fade.
- **Layout:** bento grid; masonry; chroma grid (animating gradient borders); split-screen scroll; sticky-stack sections.
- **Cards:** parallax tilt; spotlight border; glassmorphism panel; holographic foil; swipe stack; morphing modal (button expands into dialog).
- **Galleries:** dome gallery; coverflow carousel; drag-to-pan grid; accordion image slider; hover image trail; glitch image.
- **Typography:** kinetic marquee; text mask reveal; text scramble; circular text path; gradient stroke animation; letters dodging the cursor.
- **Micro-interactions:** particle button; skeleton shimmer; directional hover fill; ripple click; animated SVG line drawing; mesh gradient background; lens-blur depth.

Motion implementations for the scroll patterns are in `motion-patterns.md`.
