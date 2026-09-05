# DESIGN.md Template for Google Stitch

Copy this structure, replace every bracketed value, and keep the section order. Stitch reads natural-language "visual descriptions" backed by exact values, so every rule pairs a descriptive phrase with a hex code, rem value, or pixel value in parentheses. A complete filled example lives at `../DESIGN.md`.

## Writing rules

- Describe, then quantify: "Deep Charcoal Ink (#18181B)", not "dark text".
- Name colors by role, not appearance: "Muted Steel, secondary text and metadata".
- Translate developer shorthand into words Stitch understands: "generously rounded corners (2.5rem)", not `rounded-xl`.
- Use the same terminology in every section.
- Encode the bans. The anti-pattern list is what keeps the output premium.
- Avoid em-dashes in the file itself; Stitch may echo them into generated copy.

## Template

```markdown
# Design System: [Project Title]

## 1. Visual Theme & Atmosphere
[Two to four sentences describing mood, density, variance, and motion intensity.
Name the dial levels. Example: "A restrained, gallery-airy interface with confident
asymmetric layouts and fluid spring-physics motion. Clinical yet warm, like a well-lit
architecture studio. Density 4, variance 8, motion 6."]

## 2. Color Palette & Roles
- **Canvas White** (#F9FAFB): primary background surface
- **Pure Surface** (#FFFFFF): card and container fill
- **Charcoal Ink** (#18181B): primary text, off-black depth
- **Muted Steel** (#71717A): secondary text, descriptions, metadata
- **Whisper Border** (rgba(226,232,240,0.5)): card borders and 1px structural lines
- **[Accent Name]** ([#XXXXXX]): the single accent for CTAs, active states, focus rings
Constraints: one accent only, saturation below 80%, no purple or neon, never pure black (#000000).
One gray family for the whole system.

## 3. Typography Rules
- **Display:** [Font]: track-tight, controlled scale, hierarchy through weight and color rather than size
- **Body:** [Font]: relaxed leading, 65-character maximum line length, secondary neutral color
- **Mono:** [Font]: code, metadata, timestamps, and all numbers when density is 8 or above
- **Banned:** Inter as the default; generic serifs (Times New Roman, Georgia, Garamond, Palatino);
  any serif in dashboards or software UI. If a serif is justified for editorial work, use a
  distinctive modern serif and say why.

## 4. Component Stylings
- **Buttons:** flat fill in the accent, no outer glow, tactile 1px downward press on active,
  ghost or outline for secondary. One primary CTA per screen.
- **Cards:** [radius] corners, diffused shadow tinted to the background hue, used only when
  elevation communicates hierarchy. In dense layouts replace cards with top dividers or space.
- **Inputs:** label above, helper text optional, error text below, focus ring in the accent color,
  no floating labels, no placeholder-as-label.
- **Loading:** skeleton shapes matching the final layout, no circular spinners.
- **Empty states:** composed, showing how to add the first item, not a bare "No data".
- **Errors:** clear inline messages next to the field or action.

## 5. Layout Principles
[Grid-first responsive structure. Asymmetric or split-screen hero when variance is above 4.
No three-equal-cards feature rows; use a two-column zig-zag, asymmetric grid, or horizontal scroll.
Max-width containment (about 1400px, centered). Elements never overlap; each occupies its own zone.
Full-height sections use dynamic viewport height, never a fixed screen height.
Below 768px every multi-column layout collapses to one column; no horizontal scrolling.
Headlines scale fluidly; body text never below 1rem; tap targets at least 44px;
section gaps shrink proportionally on small screens.]

## 6. Motion & Interaction
[Spring physics for interactive elements (stiffness 100, damping 20), no linear easing.
Staggered cascade reveals for lists. Perpetual micro-loops (pulse, shimmer, float) only on
components that show live state. Animate transform and opacity only. Respect reduced-motion.]

## 7. Anti-Patterns (Banned)
- No emojis anywhere
- No Inter as the default font; no generic serifs; no serif in dashboards
- No pure black (#000000); no neon or outer-glow shadows; no oversaturated accents
- No gradient text on large headers; no custom mouse cursors
- No overlapping elements; no three-column equal card layouts; no centered hero above variance 4
- No generic names ("John Doe", "Acme", "Nexus"); no fake round numbers (99.99%, 50%)
- No AI copywriting cliches ("Elevate", "Seamless", "Unleash", "Next-Gen")
- No filler UI text ("Scroll to explore", "Swipe down", scroll arrows, bouncing chevrons)
- No secondary "Learn more" link beside the primary CTA
- No broken external image links; use seeded placeholder services or SVG avatars
```

## Hero guidance (include in section 5 when the screen has a hero)

- The hero is the first impression. One headline, one supporting line, one primary CTA.
- Signature technique at high creativity levels: inline image typography, where small rounded photos sit between words at type height as visual punctuation. On mobile these images stack below the headline.
- Text never overlaps images. No "scroll to explore" cues.
