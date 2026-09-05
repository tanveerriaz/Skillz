---
name: restrained-product-motion
description: Use when adding animation to a dark editorial deck, landing page or product mock and the brief is "alive but calm" — content that rises in once, UI mocks that idle with millimetre-scale drift, mascots that blink and float, glows that breathe. Gives exact durations, easings, distances and loop structures, plus what is banned (bounce, parallax, big slides, spinners).
---

# Purpose

Motion in this system does two jobs only: (1) tell the eye that a new thing
has arrived, and (2) make a static product mock feel like a live app that is
quietly working. Everything else is noise. This skill fixes the numbers so an
agent cannot "add some animation" and end up with a bouncing landing page.

# When to Use

- Slide/section entrances on a talk deck or scroll page.
- Idle loops on in-page product mocks (windows, notifications, terminals).
- Mascot / avatar micro-life (blink, float).
- Attention cues (a glowing divider, a breathing toggle) that must not distract.

Do not use for data transitions in charts, page-route transitions in a real
app, or anything the user has to wait for (use a progress indicator instead).

# Inputs

- The element class: *content* (text, cards), *mock* (a fake window or
  device), *mascot* (illustrated character), *cue* (glow, pulse).
- Whether the element is on screen for a long time (deck slide, hero) or
  briefly (list row).

# Outputs

- CSS keyframes + `animation` declarations, or framer-motion `initial /
  animate / transition` props, following the tables below.
- A `prefers-reduced-motion` block that removes loops and shortens entrances.

# The motion grammar

## 1. Entrance — one time, then still

| Element | Keyframes | Duration | Easing | Stagger |
|---|---|---|---|---|
| Content (title, note, card) | `opacity 0→1`, `translateY(11px)→0` | 280–400ms | `cubic-bezier(.22,1,.36,1)` | 40–60ms per sibling |
| Side panel / detail pane | `opacity 0→1`, `translateX(18px)→0` | 280ms | same | — |
| Nested content inside a pane | `opacity 0→1`, `translateX(8px)→0` | 240ms, 50ms delay | same | — |
| Window / mock "opening" | `opacity 0→1`, `scale(.94) translateY(8px)→1` | 380ms | `cubic-bezier(.2,.8,.2,1)` | — |
| Scrim / overlay | `opacity 0→1` | 220ms | `ease` | — |

```css
@keyframes rise-in{0%{opacity:0;transform:translateY(11px)}to{opacity:1;transform:translateY(0)}}
.enter{animation:rise-in .32s cubic-bezier(.22,1,.36,1) both}
.enter:nth-child(2){animation-delay:.05s}.enter:nth-child(3){animation-delay:.1s}
```

Distances are 8–18px. Never more. An entrance that travels 40px reads as a
"slide"; this system never slides.

## 2. Ambient loops — the mock is alive

Long (5–12s), tiny (1–5px), `ease-in-out`, `infinite`, and the element
spends most of the loop at rest. Loops are desynchronised by giving each
element a different duration, not a delay.

| Loop | What moves | Amplitude | Period |
|---|---|---|---|
| Window drift | two overlapping windows drift in opposite directions | 2–5px, one keyframe at 45% | 7–8s |
| Desktop drift | whole mock scene | ≤6px, `alternate` | 12s |
| Pointer tour | a fake cursor visits 2–3 spots, "clicks" (`scale(.82)`) | 15–30px steps, holds between | 4.8–5.8s |
| Hand-off pills | avatar pills expand/collapse to show who is being asked | width/opacity | 7.2s |
| Toggle breathe | `filter:brightness(1→1.08)` | — | 3.4s |
| Glow line | divider `opacity .25→.9→.25` | — | 2–3s |

```css
@keyframes preview-terminal{0%,to{transform:translateZ(0)}45%{transform:translate3d(2px,-2px,0)}}
@keyframes preview-browser{0%,to{transform:translateZ(0)}45%{transform:translate3d(-2px,2px,0)}}
@keyframes glow-line{0%,to{opacity:.25}50%{opacity:.9}}
```

## 3. Mascot micro-life

A character should blink and settle, nothing more. Blink twice per loop with
irregular spacing; float once per loop with a tiny tilt.

```css
/* eyes: scaleY collapse, origin center */
@keyframes blink{0%,44%,48%,79%,83%,to{transform:scaleY(1)}46%,81%{transform:scaleY(.08)}}
/* body: barely there */
@keyframes float{0%,46%,to{transform:translateY(0) rotate(0)}50%{transform:translateY(-1px) rotate(-1.8deg)}55%{transform:translateY(0) rotate(1deg)}60%{transform:rotate(0)}}
.face__eye{transform-origin:center;animation:blink 6.5s ease-in-out infinite}
.face{animation:float 9s ease-in-out infinite}
```

## 4. Interaction feedback

- Hover/active: `transition: background .14s, transform .16s`; at most
  `translateY(-1px)` or a `--panel → --panel-hi` fill change.
- Selection / detail reveal: `transform .6s cubic-bezier(.22,1,.36,1)`.
- Nothing scales above 1.02 on hover.

## 5. Banned

Bounce/elastic easings · parallax · letter-by-letter text reveals · typing
effects on headlines · infinite spinners as decoration · rotating gradients ·
particles · anything that moves more than 18px on entrance · anything that
loops faster than 3s (except blink) · autoplay video backgrounds.

# Procedure

1. Classify each animated element (content / mock / mascot / cue).
2. Apply the entrance table once per element; stagger siblings by 40–60ms.
3. For long-lived mocks, add **one** ambient loop per window and, if there is
   a cursor, one pointer tour. Give each loop a distinct period.
4. Add mascot blink/float only to illustrated characters.
5. Add the reduced-motion block (below). Test at 0.5× speed: if anything
   looks like it is "performing", cut its amplitude in half.

```css
@media (prefers-reduced-motion:reduce){
  *{animation-iteration-count:1!important;animation-duration:.01ms!important;transition-duration:.01ms!important}
}
```

# Quality Checklist

- [ ] Every entrance ≤ 400ms, ≤ 18px, ease-out curve, runs once (`both`).
- [ ] Every loop ≥ 3s (blink excepted), ≤ 6px, spends >50% of its time at rest.
- [ ] No two loops share the same duration.
- [ ] Nothing on the page moves while the reader is meant to be reading a headline, except mascots and glows.
- [ ] Reduced-motion block present.
- [ ] GPU-friendly: only `opacity`, `transform`, `filter` are animated.

# Edge Cases

- Framer-motion project: map entrances to
  `initial={{opacity:0,y:11}} animate={{opacity:1,y:0}} transition={{duration:.32,ease:[.22,1,.36,1]}}`;
  keep ambient loops in CSS — they are cheaper and do not re-render.
- A mock has five windows → animate the two in front; leave the rest static.
- Presenter wants "more energy" → increase *contrast of timing* (longer
  rests, sharper entrances), not amplitude.

# Safety Rules

- Never animate on scroll with JS listeners that block the main thread; use
  CSS or `IntersectionObserver` once.
- Respect `prefers-reduced-motion` unconditionally.

# Examples

Good: a notification card rises 11px into place in 320ms; behind it a fake
terminal and browser drift 2px in opposite directions every 7–8s; the mascot
blinks twice every 6.5s. The slide feels like a live desk.

Bad: cards fly in from the left over 900ms with a bounce, the headline types
itself out, and a gradient blob rotates behind everything.
