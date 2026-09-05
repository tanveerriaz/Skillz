# Anti-Patterns: The AI Tells

Signatures the model reaches for when it tries to "look designed". Treat every item as a hard ban unless the brief explicitly asks for it. Typography, color, and layout bans that have their own rules live in `typography-and-color.md` and `layout-and-content.md`; this file collects the rest.

## 1. Em-dash ban (the single most-violated tell)

The em-dash (`—`) is completely banned in anything visible to the user. No "sparingly" allowance. The agent has historically ignored soft limits, so the rule is binary: zero.

- Headlines: use a period or comma.
- Eyebrows, labels, pills, button text, captions, nav items: use line breaks, columns, or hairlines.
- Body copy: two sentences, a comma, parentheses, or a colon.
- Quote attribution: a spaced hyphen (` - `) or a line break with a lighter-weight name.
- The en-dash (`–`) is banned as a separator too. Ranges use a plain hyphen (`2018-2026`, `40-80k`).

Permitted dashes: the hyphen (`-`) and the minus sign in math. One `—` or `–` anywhere on the page fails pre-flight.

## 2. Content and data ("Jane Doe" effect)

- No generic names: "John Doe", "Sarah Chan", "Jack Su". Use realistic, locale-appropriate names.
- No generic avatars (SVG "egg", user icon). Use believable photo placeholders or a deliberate style.
- No fake-perfect numbers: `99.99%`, `50%`, `1234567`. Use organic values (`47.2%`, `+1 (312) 847-1928`).
- No startup-slop brand names: "Acme", "Nexus", "SmartFlow", "Cloudly". Invent contextual names that sound real.
- No filler verbs: "Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionize". Concrete verbs only.
- No emojis in code, markup, or visible text unless the user asks for a playful or chat-native feel, and then sparingly.

## 3. Hero and top of page

- No version labels as eyebrows (`V0.6`, `BETA`, `INVITE-ONLY PREVIEW`, `EARLY ACCESS`) unless the brief is about launch status.
- No "Brand · No. 01"-style micro-meta sub-eyebrows.
- No decoration text strip at the hero bottom (`BRAND. MOTION. SPATIAL.`, `DESIGN · BUILD · SHIP`, `ESTD. 2018 · CITY`). Acceptable only as a real sticky nav with links or real status information.
- No scroll cues: `Scroll`, `↓ scroll`, `Scroll to explore`, animated mouse-wheel icons, bouncing chevrons. The viewer knows what scrolling is.
- No div-built fake product UI in the hero (fake task list, fake terminal, fake dashboard). Use a real screenshot, a generated image, a real component preview, or nothing.
- No fake version footers inside mock screenshots (`v0.6.2-rc.1`, `last sync 4s ago · main`).

## 4. Section labels and numbering

- No section-number eyebrows: `00 / INDEX`, `001 · Capabilities`, `06 · how it works`. Eyebrows, when allowed at all, name the topic in plain language.
- No `01 / 4` pagination on images or bento tiles.
- No "Index of Work, 2018-2026"-style range labels as eyebrows.
- No generic step labels: "Step 1 / Step 2", "Stage 1", "Phase 01", "Pass One". The step content is the label ("Install", "Configure", "Ship").
- No micro-meta sentences under eyebrows ("Each of these is a feature we ship today, not a roadmap promise."). Eyebrow + headline + body is the limit.
- No floating top-right sub-text in section headers. Put the body under the headline or build a clean aligned two-column header.
- No vertical rotated text unless the brief is explicitly experimental and the rotation serves the composition.
- No crosshair or hairline grid lines drawn as decoration. Lines organize real content or do not exist.

## 5. Separators, dots, and flourishes

- The middle dot (`·`) is rationed: max one per line in metadata strips. Never the default separator for everything.
- Zero decorative status dots by default. A colored dot before nav items, list rows, badges, or "ONE Q4 SLOT OPEN" is a tell. Allowed only for real semantic state (live server status, real availability), at most one per section.
- No `<br>`-broken-and-italicized headlines as a default move ("for thirty\<br\>*years.*"). Headlines read naturally first.
- No custom mouse cursors. Outdated, hostile to accessibility and performance.

## 6. Marketing copy tells

- No "Quietly in use at" or "Quietly trusted by" social-proof headers. Use "Trusted by", "Used at", "Customers include", or let the logos speak.
- No poetic section labels for quotes, blog, or sidebars: "From the field", "Field notes", "Currently on the bench", "On our desks", "Loose plates". Use "Testimonials", "Latest writing", "Now working on", or no label.
- No mock-humble industry asides ("We respect the French ones") in body copy.
- No locale, city, time, or weather strips (`CITY 14:23 · 18°C`, "1200-690 City, Country" in the footer, "Working with founders from City" in the hero). Allowed only for a genuinely distributed studio, a travel brand, or a real physical venue. One contact address in the footer is fine.
- No "Reservation 412 of 800" live-stock counters unless it is a real limited run with real data.

## 7. Images, pills, and captions

- No pills, labels, or tags overlaid on images (`Brand · 02`, `PLATE · BRAND`, `Field notes - journal`). Let the image stand alone or caption it below.
- No photo-credit captions as decoration (`Field study no. 12 · Photographer Name`, `Plate 03 · House archive`, `Frame XII · 35mm`) under stock or placeholder images. Credit only a real photographer for a real photo. Otherwise skip, or use a one-line functional caption ("The 6-quart, in sage.").
- No broken Unsplash links. Use seeded Picsum, generated images, or real assets.
- No hand-rolled SVG icons; use an allowed icon library. Hand-drawn decorative SVGs only on request.

## 8. Lists, dividers, and scoring

- No `border-t` plus `border-b` on every row of a long list or spec table. One divider style, used sparsely, or a different component (see `layout-and-content.md`).
- No scoring or progress bars with filled background tracks as comparison visuals on a marketing page. Use a number with a small icon, or a thin inline bar without a track.
- No version footers on marketing, landing, or portfolio pages (`v1.4.2`, `Build 0048`). Those are devtool fixtures.

## 9. Components and libraries

- shadcn/ui is allowed but never in its default state. Customize radii, colors, shadows, and type to the project.
- No Lucide icons unless requested or already in the project.
- No three equal feature cards, no accordion-FAQ-by-default, no glassmorphism on everything, no infinite loops on every card.
- Code ships clean: no dead debug code, no arbitrary `z-50` spam, no imports that are not in the dependency file.
