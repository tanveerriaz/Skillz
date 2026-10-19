---
name: hyperframes-gsap-adapter
description: GSAP animation API reference for HyperFrames. Use when writing seekable GSAP timelines in HyperFrames compositions, including gsap.to(), from(), fromTo(), set(), timeline position parameters, labels, easing, stagger, finite repeats, and transform performance.
---

> Modified for Skillz: curated standalone text edition of [HyperFrames source](https://github.com/heygen-com/hyperframes/blob/cea0bad7931122bd93680006978c0d9007daa3d4/skills/hyperframes-animation/adapters/gsap.md). Copyright 2026 HeyGen, Inc.; Apache-2.0. See [license](../LICENSE) and [provenance](../UPSTREAM.md).

# HyperFrames GSAP

## Contents

- [HyperFrames Contract](#hyperframes-contract)
- [Core Tween Methods](#core-tween-methods)
- [Common vars (cheatsheet)](#common-vars-cheatsheet)
- [Animated Property Guidance](#animated-property-guidance)
- [References](#references)
- [Best Practices](#best-practices)
- [Do Not](#do-not)
- [Credits And References](#credits-and-references)

GSAP usage scoped to HyperFrames' seek-driven render model. This skill is the GSAP reference _as constrained by HyperFrames_ — for the framework's broader composition contract see `hyperframes-core`.

## HyperFrames Contract

HyperFrames controls GSAP through its `gsap` runtime adapter. Create a paused timeline, register it on `window.__timelines` with the exact `data-composition-id` after adding its tweens, and let HyperFrames seek it. Setup may run inside an async callback; register the completed timeline at the end of that callback.

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  tl.fromTo(".title", { y: 48, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }, 0);
  tl.to(".accent", { scaleX: 1, duration: 0.5, ease: "power2.out" }, 0.25);

  window.__timelines["main"] = tl; // key must equal data-composition-id on the composition root
</script>
```

- The registry key must match the composition root's `data-composition-id`.
- Bracket and dot syntax both register: `window.__timelines["main"] = tl` and `window.__timelines.main = tl` are equivalent (the linter recognizes both). Bracket form is required when the id isn't a valid identifier (e.g. contains `-`).
- Do not call `tl.play()` for render-critical motion.
- Building inside an async callback such as `document.fonts.ready` is supported and common. What breaks is **registering the key before the build finishes**: an empty timeline registered early is treated as ready and nested empty, so it renders blank (`lint`: `gsap_timeline_registered_before_async_build`, error). Assign `window.__timelines[id] = tl` at the end of the callback. Do not drive render-critical motion from timers or event handlers.
- Keep loops finite. HyperFrames renders finite video durations.
- **Render duration comes from `data-duration` on the composition root, not from GSAP timeline length.** Do not pad the timeline with empty tweens like `tl.set({}, {}, 283)` to "extend" it. (Some external docs show this trick; in HyperFrames it conflicts with the seek-driven duration model — set `data-duration` instead.)

## Core Tween Methods

- **gsap.to(targets, vars)** — animate from current state to `vars`. Most common.
- **gsap.from(targets, vars)** — animate from `vars` to current state (entrances).
- **gsap.fromTo(targets, fromVars, toVars)** — explicit start and end.
- **gsap.set(targets, vars)** — apply immediately (duration 0).

Always use **camelCase** property names (e.g. `backgroundColor`, `rotationX`).

## Common vars (cheatsheet)

- **duration** — seconds (default 0.5).
- **delay** — seconds before start.
- **ease** — `"power1.out"` (default), `"power3.inOut"`, `"back.out(1.7)"`, `"elastic.out(1, 0.3)"`, `"none"`. See `./gsap-easing-and-stagger.md`.
- **stagger** — number or object. See `./gsap-easing-and-stagger.md`.
- **repeat** — prefer a finite number computed from the visible duration. An infinite repeat requires a finite root `data-duration` to bound export.
- **yoyo** — alternates direction with repeat.
- **overwrite** — `false` (default), `true`, or `"auto"`.
- **immediateRender** — default `true` for from()/fromTo(). Set `false` on later tweens targeting the same property+element.
- **onComplete**, **onStart**, **onUpdate** — callbacks.

For transforms, autoAlpha, clearProps, and SVG specifics see `./gsap-transforms-and-perf.md`.

## Animated Property Guidance

Prefer the following properties for predictable, efficient animation:

- **Compositor-cheap**: `opacity`, `x`, `y`, `scale`, `scaleX`, `scaleY`, `rotation`, `rotationX`, `rotationY`, `skewX`, `skewY`, `transformOrigin`
- **Visual fills**: `color`, `backgroundColor`, `borderColor`, `borderRadius`
- **CSS variables**: `"--hue": 180` etc.
- **Media `volume`** (on `<audio>` / `<video>`): do not tween it for fades or ducking; use the `data-automation` volume lane (see the optional upstream [editing recipes](https://github.com/heygen-com/hyperframes/blob/cea0bad7931122bd93680006978c0d9007daa3d4/skills/hyperframes-core/references/creator-editing-recipes.md)). A lane wins over a tween on the same element.
- **DOM text `innerText`** (for numeric counters): tween it directly, e.g. `tl.to(el, { innerText: 100, snap: { innerText: 1 } })` — `snap` keeps it integer; the GSAP inspector recognizes it as a counter. Equivalent to the `onUpdate`-proxy form in [../rules/counting-dynamic-scale.md](https://github.com/heygen-com/hyperframes/blob/cea0bad7931122bd93680006978c0d9007daa3d4/skills/hyperframes-animation/rules/counting-dynamic-scale.md) (optional upstream reference); prefer that proxy form for locale formatting (`toLocaleString`) or suffix logic, and pair it with a separate transform-scale tween when the number should grow.

**Avoid** (use the transform alias instead):

- `width` / `height` / `top` / `left` / `right` / `bottom` / `margin*` / `padding*` — trigger layout reflows. Use `scaleX/Y` (with `transformOrigin`) or `x` / `y`.

**Forbidden** (breaks the renderer or the clip lifecycle):

- `display`, raw `visibility` **on a clip element**: never duration-tween these. HyperFrames owns a clip's visibility and `lint` rejects it. For show/hide, animate a non-clip child with `autoAlpha` or a zero-duration timeline set at an explicit boundary; never set `display`, `visibility`, or `autoAlpha` on the timed clip container. Animate inner elements to preserve framework visibility control.
- Anything driven by `Math.random()`, `Date.now()`, `performance.now()`, or event handlers — animation state must be deterministic from time alone.

> **Note**: the preferred-properties list is guidance, not a strict allowlist. The framework applies a denylist. Other properties, including `width`, `height`, `filter`, `clipPath` and `strokeDashoffset`, are legitimate targets; prefer transforms and opacity where you have the choice, for performance rather than correctness. See the companion core skill's [determinism rules](../../hyperframes-core/references/determinism-rules.md) when that skill is present, or the [pinned upstream reference](https://github.com/heygen-com/hyperframes/blob/cea0bad7931122bd93680006978c0d9007daa3d4/skills/hyperframes-core/references/determinism-rules.md).

## References

- `./gsap-timeline-and-labels.md` — timeline creation, position parameter (`+=`, `<`, `>`), labels, nesting, sub-comp `fromTo` preference, playback control.
- `./gsap-easing-and-stagger.md` — easing families, stagger objects, function-based values, `gsap.matchMedia()`, `gsap.defaults()`.
- `./gsap-transforms-and-perf.md` — transform aliases, autoAlpha, `quickTo`, `will-change`, performance rules.
- For progressive SVG reveals, use [SVG Path Draw](../rules/svg-path-draw.md). Audio extraction and analysis scripts are outside this text edition.

## Best Practices

- Use camelCase property names; prefer transform aliases and autoAlpha.
- Prefer timelines over chained tweens with delays; use the position parameter.
- Add labels with `addLabel()` for readable sequencing.
- Pass defaults into the timeline constructor.
- Store the tween/timeline return value when controlling playback.

## Do Not

- Animate layout properties (`width`/`height`/`top`/`left`) when transforms suffice.
- Use both `svgOrigin` and `transformOrigin` on the same SVG element.
- Chain animations with `delay` when a timeline can sequence them.
- Create tweens before the DOM exists.
- Use infinite `repeat: -1` without a finite root `data-duration` (with one, export clips to that window); when a loop must end before the composition does, use a finite repeat count computed from the visible duration.

## Credits And References

- HyperFrames adapter source: `packages/core/src/runtime/adapters/gsap.ts`.
- GSAP documentation: https://gsap.com/docs/v3/
- GSAP timeline pause and seek behavior: https://gsap.com/docs/v3/GSAP/Timeline/pause%28%29/
