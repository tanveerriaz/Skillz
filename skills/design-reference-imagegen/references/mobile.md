# Mobile Reference: App Screens and Flows

Read this after choosing the mobile surface. Shared rules (one system, readability, anti-generic) live in SKILL.md. This surface produces images only; it never writes SwiftUI, React Native, Flutter, or HTML.

## 1. Output Rules

- One image per screen. Never collapse a requested flow into one board with tiny screens.
- Screens are shown inside a clean phone mockup with a visible frame by default; the app content stays the focus. Omit the frame only when the user asks for raw screens or UI sheets, or when borderless presentation clearly serves the concept.
- Generate enough screens for the flow to feel real:
  - "N screens" → exactly N
  - onboarding → 3–4 distinct screens, not one
  - auth → separate sign-in / sign-up / recovery when useful
  - "app concept" → a meaningful set (typically 4–6), never one hero mockup
- If a detail is unclear, generate a fresh detail render or regenerate the screen. Never crop a region out of an earlier image.

## 2. Platform Mode (decide first, use one)

| Mode | Bias toward |
|---|---|
| iOS-native | clean top areas, tab bar, safe-area awareness, restrained chrome, native-feeling sheets and cards |
| Android-native | firmer component rhythm, clear app bar, bottom navigation, sheet logic, explicit states |
| Cross-platform neutral | universal navigation patterns, clean safe areas, less platform ornament, broadly buildable |

Do not mix iOS and Android patterns in one set.

## 3. Design Bible (lock before the second image)

Write down and hold constant across the whole set:
platform mode · device frame style and scale · palette · typography mood and scale · spacing system · corner radius · icon style · imagery treatment · texture intensity · decorative asset language · navigation model · card/list behavior · button style · shadow language.

Allowed to vary per screen: composition, feature emphasis, image placement, density, tempo, CTA placement, texture strength.
Never vary: product identity, design system, mockup quality, core spacing logic.

## 4. Style Choices (pick one each; hold across the set)

**Theme:** pristine light · deep dark · soft wellness neutral · premium monochrome · rich accent-driven · editorial luxe · playful consumer color · calm productivity minimal

**Typography:** clean system-like sans · refined grotesk · expressive display + clean body · soft humanist sans · sharp product sans with disciplined hierarchy

**Structure bias:** list-led utility · card-led modular · dashboard-led overview · media-led storytelling · profile-led identity · commerce browse/detail · chat-led conversation · wellness calm blocks

**Image art direction:** editorial photography · cinematic lifestyle · soft illustration · tactile abstract · premium product · mixed photo + vector · moody atmospheric · collage-lite layers

**Surface texture:** ultra-subtle grain · matte paper · foggy gradient · soft noise wash · blurred image haze · flat with one textured hero area · tactile monochrome · low-opacity technical pattern

**Palette logic:** monochrome + one accent · warm neutral + sharp dark · cool mineral + clean highlight · cream/charcoal/muted accent · rich dark + warm accent · soft wellness saturation · bright consumer palette, disciplined · desaturated premium + one bold hit

**Signature components (exactly 4):** hero metric card · compact stat strip · collection grid · media carousel · layered profile header · segmented control · bottom action sheet · framed product card stack · progress ring · message bubble system · settings group cells · photo-led card strip · sticky mini player · collection shelf · habit tracker block · checkout summary card · journal entry card · achievement tile row

**Decorative assets (exactly 2):** line icon cluster · orbit lines · dotted arcs · starburst micro-motif · rounded sticker accent · directional arrow system · fine grid · soft waveform · badge glyphs · geometric markers

**Motion-implied cues (exactly 2; visual hints only):** springy card lift · sheet rise · calm tab transition · staggered list reveal · dashboard fade-up · parallax header drift · carousel glide

## 5. Flow Logic

Screens must form a believable journey. Typical sequences:
onboarding → auth → home · home → browse → detail · profile → settings → edit · cart → checkout → confirmation · dashboard → activity → detail · welcome → permissions → personalized home.

For each screen ask: what action on the previous screen leads here, and does UI state carry forward (selected item, entered name, chosen plan)?

## 6. Screen Rules

**First screen (onboarding, welcome, home, auth):** one focal point; 1–3 short lines for the main statement; concise support; one clear action; no stats, chips, tags, or pill rows; if imagery sits behind text, protect it with a fade, mask, or scrim. It must not look like a website hero inside a phone.

**Onboarding:** vary composition and image/text/CTA balance across screens; short copy; no three identical icon-plus-headline slides; no early rating prompts; no motivational filler.

**Safe areas:** respect status bar, title region, bottom navigation, home indicator, sheet docking zone, and gesture space. Critical content never lives in unsafe regions. Screens are app screens, not edge-to-edge posters.

**Navigation:** tab bar / bottom navigation for major sections; stack feel for drill-down; sheets for secondary tasks; segmented controls for local switching. Never overload bottom navigation or make every action equally weighted.

**Layout:** avoid box-in-box-in-box. Prefer fewer, clearer containers, flatter structure, one strong structural move per screen. No floating-widget dashboards, fake system labels, or decorative pills.

**Imagery:** use it when the category benefits (social, commerce, travel, wellness, food, fashion, media, creator, marketplace). Forms: photography-led onboarding, image-backed headers with fades, product cards, collection shelves, editorial crops, atmospheric layers behind content. Keep media in fixed, repeatable frames with stable ratios and radius. Avoid filler thumbnails and one pretty screen followed by no imagery.

**Image-behind-text:** bottom-to-top fade into the background color, side fade masks, soft blur overlays, scrims under headline and CTA. Text stays readable; the treatment reads as intentional, not random opacity.

**Texture:** grain, noise, paper, fog, blurred photo layers are welcome at subtle-to-medium strength to avoid sterile flat backgrounds. Texture supports mood; it never competes with the interface.

**Iconography:** a consistent custom-feeling icon system with one stroke or fill logic and some character. Avoid generic developer-library icon defaults and mixed weights.

**Copy:** short headlines, believable button labels, real-feeling screen titles, minimal support text. No lorem ipsum, long paragraphs, or inspirational filler.

**Text size:** if text feels small, the screen is not finished. Fix by simplifying layout, cutting content, enlarging type, or splitting into another screen. Readable beats dense, clever, or decorative.

**Spacing:** generous gaps between blocks, clean internal padding, calm screens alternating with denser ones, touch-friendly sizes.

**Complexity:** cleanliness is the goal, not minimalism. Rich, layered, expressive screens are fine when hierarchy and readability hold.

## 7. Device Mockup Rules

- One device style and one scale across the set (unless mixed devices are requested).
- Phone centered or clearly aligned; even margins on all four sides; the phone never touches the canvas edge.
- Consistent bezels, soft controlled shadow, no awkwardly cropped frames.
- Multiple phones in one canvas: same scale, equal gutters, clean alignment, no random overlap.
- The frame supports the UI; visual emphasis stays inside the screen.

## 8. Category Bias

| Category | Prefer |
|---|---|
| Fintech | trust, calm spacing, clear numbers, restrained accent, transaction clarity, no chart spam |
| Health / fitness | strong metric hierarchy, readable progress modules, airy spacing, optimistic imagery or wellness texture |
| Productivity | list/card discipline, simple navigation, calm density, clear task hierarchy |
| Social | profile/feed rhythm, media moments, clear split between creating and browsing, expressive imagery |
| Commerce | browse/detail/cart clarity, strong product imagery, stable card proportions, clean checkout |
| Wellness / lifestyle | soft materials, calm type, breathing room, tactile backgrounds, soft fades |

## 9. Prompt Template (per screen)

```
Mobile app screen reference, [iOS | Android | neutral] mode, shown inside a clean [iPhone-style | Android-style | generic] phone mockup with visible frame, centered, even margins, soft shadow; app content is the focus.
Screen: [X of N — name]. Comes after [previous screen] via [action]. Carries forward: [state].
App: [category, product, audience]. Theme: [theme]. Palette: [logic + colors — identical across all screens].
Typography: [character]; headline max 3 lines; body comfortably readable; labels never tiny.
Structure: [structure bias]. Navigation: [tab bar | stack | sheet | segmented]. Safe areas respected (status bar, home indicator).
Imagery: [art direction; where it sits; fade/mask treatment if behind text; frame ratio].
Texture: [treatment, subtle]. Decorative assets: [the 2 chosen, used sparingly]. Icons: consistent custom [stroke | fill] system.
Components on this screen: [from the 4 chosen].
Copy: [title], [key labels], [CTA] — short and believable.
Style: app-native, one focal point, fewer clearer containers, generous spacing, premium and specific, not template-like.
Exclude: purple-blue gradients, glass cards, blobs, nested card stacks, widget dashboards, pill/badge clutter, tiny text, website-hero-in-a-phone, generic library icons.
```

## 10. Regenerate When

Text too small · spacing unclear · navigation looks fake · screen looks like a website · crowded first screen · repetitive onboarding · inconsistent image framing · nested cards · flat generic background · weak or missing imagery · poor fade behind text · timid or absent creative accents · muddy or generic palette · set drifts across design systems · uneven or sloppy mockup framing.

## 11. Mobile Checklist

- [ ] Platform mode chosen and consistent; no iOS/Android mixing.
- [ ] Screen count matches the request or fully covers the flow; no lazy collage.
- [ ] Flow order is believable; state carries forward.
- [ ] Design bible held across all screens: palette, type, radius, icons, frame, spacing.
- [ ] First screen: one focal point, short copy, one action, no chip rows.
- [ ] Safe areas respected; navigation pattern clear.
- [ ] No box-in-box clutter; fewer, clearer containers.
- [ ] Imagery purposeful and framed consistently; fades protect any text over images.
- [ ] Text comfortably readable at normal viewing size on every screen.
- [ ] Mockups same device, same scale, even margins, frame not dominating.
- [ ] Screens vary in composition without leaving the design system.
- [ ] Icons feel intentional, not library defaults; palette clean and specific.

## 12. Example Interpretations

- **"Premium fitness app"** → iOS or neutral; 4–5 screens (welcome, home, workout detail, progress, profile); calm metric hierarchy; soft texture or imagery; consistent frame and scale; no chart spam.
- **"5-screen ecommerce app"** → exactly 5 (browse, category, product detail, cart, checkout); strong product imagery in fixed frames; editorial fades on headers; product-first hierarchy; consistent framing across all 5.
- **"Onboarding for a social app"** → 3–4 screens with distinct layouts; photography-led with fade-to-background treatments; short copy; first screen cleanest; ends at permissions or personalized home; same mockup and margins throughout.
