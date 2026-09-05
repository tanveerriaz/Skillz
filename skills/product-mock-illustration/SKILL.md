---
name: product-mock-illustration
description: Use when a slide, landing page or doc needs a picture of software and you would otherwise reach for a screenshot, stock image or icon grid — instead build a small, live, HTML/CSS mock of the UI (chat window, notification stack, settings panel, terminal, plugin list, approval dialog, phone/desktop frame) with soft blob mascots as avatars. Covers anatomy, sizing, layering and the rule that the mock's text carries the argument.
---

# Purpose

In this visual system the graphics *are* the product. Every concept is shown
as a miniature, believable piece of UI whose copy states the point the slide
is making. No stock photos, no abstract 3D renders, no icon-per-bullet.
This skill defines the reusable mock components and how to compose them.

# When to Use

- A slide title makes a claim about how software behaves → show the moment
  it behaves that way.
- A feature needs explaining → show its settings panel with the relevant
  toggle on.
- A safety/approval rule → show the dialog that asks, with "Not yet" as the
  default-styled button.
- Comparing tools → show two frames side by side, same task, different result.

Do not use for real screenshots that must be evidentially accurate (audits,
bug reports) or where the audience needs to recognise the actual product UI
pixel-for-pixel.

# Inputs

- The sentence the mock has to prove (its title).
- Which surface(s): chat, notifications, settings, terminal, browser,
  plugin list, form, phone.
- The cast: 1–3 named agents/people, each with a mascot colour.

# Outputs

- Self-contained HTML/CSS (optionally React) using `quiet-dark-tokens`.
- Optional idle motion from `restrained-product-motion`.

# Component anatomy

## Desktop window
`border-radius:18px; border:1px solid var(--line); background:#1b1b1b`
(opaque — windows never let the page show through). Title bar: 40px, three
traffic-light dots (10px, `#ff5f57 #febc2e #28c840`), optional mono URL or
title in `--dim`. Split panes are separated by a 1px `--line`, sidebar fill
`#181818`. Floating windows add `box-shadow:0 24px 70px #0008`.

## Chat surface
- User bubble: right-aligned, light fill (`#e9ebee` on dark), dark text,
  `border-radius:14px`, inline agent mentions as `--blue-soft` pills.
- Agent message: left-aligned; small avatar (21–25px) + name in 12px
  `--dim`; bubble `--panel-hi`, `border-radius:14px`.
- Hand-off strip: a row of avatar pills with a mono label ("Asking Inbox
  Manager…") that animates through the cast.
- Composer: 44px, `--line` border, mono placeholder "Message <room>", mic
  icon right.

## Notification card (stack)
`padding:16px 18px; gap:14px; border-radius:18px; background:#262626eb`.
Row = avatar (42px) · title (sans 550, 16px) + one-line body (`--soft`,
14px) · timestamp (mono 12–14px `--dim`, top-right). Stack 2–3 cards,
offset 24–34px, last one is the *approval* card:

## Approval dialog ("stopped before …")
`background:var(--blue-soft); border:1px solid rgba(128,173,255,.36);
border-radius:16px`. Eyebrow in mono uppercase `--blue` ("STOPPED BEFORE
SENDING"), question in sans 18px, two buttons: secondary outlined
(`--line`) and primary filled `--blue` with dark text. The secondary
("Not yet") sits first.

## Settings / rules panel
List rows 56px, `--line` dividers, label left, control right. Toggles are
44×24, on = `--blue`. The rule being discussed is the only one switched on.

## Terminal
Mono 10–12px, `#ffffff52` text on `#0f0f0f`, `padding:13px`, 3–6 lines,
last line a blinking block cursor. Never colourise output.

## Plugin / app list
Row = 32px rounded-square icon (12px radius, single brand colour, one white
letter or glyph) · name (15px) + descriptor (12px `--dim`) · trailing state:
`✓ Added` in `--green` or an outlined `Add` button.

## Spec table (five-part task)
Full-width rows, `--panel` fill, 22px radius, mono uppercase `--blue` label
in a 150px left column, sans 16px sentence right. Rows: OUTCOME · SOURCES ·
CONSTRAINTS · DELIVERABLE · REVIEW POINT.

## Blob mascot (agent avatar)
A soft, glossy, single-hue 3D-ish blob: circle, cloud, cube, pyramid or
teardrop; two small white eyes with dark pupils; a specular highlight
top-left; rendered as inline SVG (a filled path + radial gradient + two eye
ellipses in a `<g class="eyes">`). One shape + one hue per agent, kept
constant everywhere that agent appears. Sizes: 21px (in-message) · 25px
(card) · 42px (notification) · 84px (feature card). Use `--green`/teal,
orange, violet, blue, pink, amber hues — never the page accent alone.
Do not copy an existing product's mascot artwork; draw your own shapes.

# Composition rules

1. **One mock proves one sentence.** The title says it; the mock's own
   copy shows it happening. If the mock needs a caption, the mock is wrong.
2. **Real words, right register.** Mock text follows `plain-instruction-voice`:
   "Four reply drafts are waiting for you. Nothing was sent." Never lorem
   ipsum, never "Lorem Company Inc."
3. **Scale to the stage.** A window is 55–75% of stage width on a
   title-plus-mock slide, 100% on a full-mock slide. Text inside a mock is
   never below 12px at 1080p.
4. **Layer with offsets, not perspective.** Stacks overlap by 24–34px with
   alternating ±10px horizontal offset; no 3D tilt, no reflections.
5. **Colour budget.** Mascots and app icons carry all the hue; chrome is
   grey. Status uses green/red tokens only.
6. **Idle motion optional, tiny.** If the slide is on screen >10s, add one
   ambient loop (window drift) and mascot blink. Otherwise static.
7. **Reuse the cast.** The same 3–6 agents (shape + colour + name) recur
   across the whole deck so the audience learns them.

# Procedure

1. Write the title sentence. Decide which surface would visibly prove it.
2. Pick the cast members involved; assign or reuse mascots.
3. Build the frame (window/phone) → layout (panes) → rows/bubbles → copy.
4. Style only with tokens. Check the colour budget.
5. If it is an approval moment, make the dialog the brightest thing on the
   slide (`--blue-soft`), everything else grey.
6. Add optional idle motion; run the checklist.

# Quality Checklist

- [ ] No stock imagery, no icon-per-bullet, no abstract decoration.
- [ ] Every string in the mock is a real sentence in the product's voice.
- [ ] Windows are opaque; only their shadows are soft.
- [ ] Mascot shape+colour per agent is identical across all slides.
- [ ] Approval/stop moments are the only `--blue-soft` surfaces.
- [ ] Smallest text ≥ 12px at 1080p; mock ≤ 75% width beside a title.
- [ ] No 3D tilt, reflections, device bezels with fake glare.

# Edge Cases

- Need to show a real third-party product → keep its silhouette (layout)
  but use your tokens and neutral wordmark text; do not reproduce its logo.
- Mobile surface → 390×844 frame, 44px radius, same components at 16px base.
- Very dense UI (a full CRM) → show one pane, crop the rest behind the
  stage edge; never shrink a full screenshot.

# Safety Rules

- Never paste real user data, emails, names or amounts into a mock; invent
  plausible, obviously generic ones.
- Do not lift proprietary SVG mascots, icons or wordmarks from other sites.

# Examples

Title: "Set what it has to ask before doing." → a settings window; four
rows; only "Ask before sending" is toggled on and highlighted; a
notification card overlaps the corner reading "STOPPED BEFORE SENDING —
Send this reply to Acme? [Not yet] [Send]".

Title: "Once you have a few Bots, put them in a room." → a chat window,
"Launch room · Three Bots in this chat", one user bubble, three short agent
replies each with its blob avatar, a members pane on the right.
