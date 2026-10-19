---
name: hyperframes-animation
description: Use when animating HTML with GSAP or authoring seekable HyperFrames video motion. Includes timeline sequencing, easing, stagger, transforms, SVG path drawing, waterfall text entries, and tactile press reactions.
license: Apache-2.0
---

> Modified for Skillz: condensed and adapted from HeyGen HyperFrames at the source pin in [UPSTREAM.md](UPSTREAM.md). Copyright 2026 HeyGen, Inc.; [Apache-2.0](LICENSE).

# Purpose

Compose deliberate HTML motion from a small set of reusable recipes. Keep video animation deterministic and seekable; explicitly drive browser-only animation when no HyperFrames runtime is present.

# When to Use

Use for title and word reveals, SVG drawing, interface demonstrations, button reactions, and timeline choreography. This curated edition focuses on GSAP. Full scene blueprints, other runtime adapters, analysis scripts, and transition installers are outside its scope.

# Inputs

The desired visual result, existing HTML/CSS, timing, target medium, and an approved GSAP dependency. For video, also supply the composition ID and finite duration.

# Outputs

Animated HTML with an intentional timeline and an explicit browser or video playback mode. Recipes are text snippets: define their placeholders, selectors, constants, and CSS before using them.

# Procedure

1. Establish the mode. Browser-only HTML needs ordinary layout dimensions, its own animation driver, and licensed library/font loading. HyperFrames video requires the separate runtime and the core composition contract.
2. Read [GSAP](adapters/gsap.md) and [timelines and labels](adapters/gsap-timeline-and-labels.md) when building the timeline. Use one root timeline and labels for meaningful beats. Prefer explicit `fromTo` endpoints. Child timelines manually added within the same composition must not be paused; framework-loaded sub-compositions register their own timelines and must not be manually nested.
3. Read [easing and stagger](adapters/gsap-easing-and-stagger.md) to select character and rhythm, and [transforms and performance](adapters/gsap-transforms-and-perf.md) before complex motion. Use transform aliases and opacity; measure geometry once at setup. Keep independent entrance and ambient motion on separate wrappers when they would compete.
4. Select only recipes that fit the brief:
   - [SVG path draw](rules/svg-path-draw.md): progressively reveal a measured outline; draw connectors between meaningful anchors.
   - [Waterfall entry](rules/waterfall-entry.md): stagger words or elements with decreasing gaps and varied visual weight.
   - [Press-release spring](rules/press-release-spring.md): compress an existing button, release continuously, and synchronize its reaction. Reserve strong bounce/glow for a playful brief.
5. For video, put every animated effect on the registered paused timeline, including ambient loops. Do not use free-running `gsap.to`, event-driven state, unseeded random order, or realtime spring integrators. Bound repeats by the root duration. Do not animate a timed clip's `display`, `visibility`, or `autoAlpha`; use an inner wrapper.
6. For browser-only HTML, load GSAP through the project's chosen dependency setup, build the timeline after DOM/fonts are ready, and call `.play()` explicitly. Use controls or event handlers only for the requested interaction. Respect `prefers-reduced-motion`, offer pause/replay for sustained motion when appropriate, and keep the final content readable without animation.
7. Inspect the first frame, key beats, end state, and backward seeks. For video, follow `hyperframes-core` validation and inspect the render only when video output is requested. For browser HTML, test the actual viewport, reduced motion, and interaction.

# Quality Checklist

- [ ] The chosen medium has an explicit playback driver.
- [ ] Position parameters and labels express the intended order.
- [ ] Entrances, reactions, reading time, and exits form a coherent rhythm.
- [ ] No conflicting concurrent transforms or framework clip-visibility overrides.
- [ ] Video seeks reproduce the same frames; browser motion respects reduced-motion preferences.
- [ ] Recipe placeholders and dependencies are resolved before calling the result runnable.

# Edge Cases

- Adapter snippets that show `gsap.to` describe API syntax. In video mode use `tl.to`/`tl.fromTo` on the registered timeline; realtime event examples are browser-only.
- The deterministic core contract governs renderer correctness. Property recommendations and energetic recipe styles are craft guidance; prefer transforms for smoothness and preserve the requested visual intent.
- Framework font bundles, text-fitting helpers, and automatic clip timing do not exist in plain browser HTML. Supply equivalent layout/loading behavior or omit those features.

# Safety Rules

- Do not install packages, extra skills, or omitted scripts automatically. Obtain runtime dependencies only within the user's authorized project setup.
- Do not publish private captures, credentials, or user assets with this reusable skill.
- Preserve library and asset licenses; the Apache-2.0 license here covers the skill text, not a redistributed GSAP runtime.
- State which browser/render checks actually ran. Reading a snippet does not prove a working animation.

# Examples

Browser-only, assuming GSAP and the target element are already loaded:

```js
const tl = gsap.timeline({ paused: true });
tl.fromTo(".title", { y: 40, opacity: 0 },
  { y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }, 0.2);
if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
  tl.progress(1).pause();
} else {
  tl.play();
}
```

For HyperFrames video, register the completed paused timeline as `window.__timelines["main"] = tl` instead of using the browser playback block, and give the root `data-composition-id="main"` with a finite duration. See [UPSTREAM.md](UPSTREAM.md) for dependencies and provenance.
