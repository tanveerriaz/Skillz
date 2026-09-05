# Motion: Rules, Libraries, and Canonical Skeletons

Read this before adding any animation, scroll effect, or physics interaction.

## 1. Motion must be motivated

Before adding an animation, answer "what does this communicate?" Valid answers: hierarchy (drawing attention to the right thing), storytelling (revealing in a sequence that matches a narrative), feedback (acknowledging an action), state transition (showing something changed). "It looked cool" is not valid. Each ScrollTrigger, marquee, and pinned section needs a one-sentence reason or it is removed.

## 2. Rules by dial

- `MOTION_INTENSITY` 1-3: `:hover` and `:active` only.
- 4-7: entry transitions on the hero, scroll reveals on key sections, hover physics on CTAs. `transition: 0.3s cubic-bezier(0.16, 1, 0.3, 1)`.
- 8-10: scroll-driven choreography, pinned sequences, parallax.
- **Motion claimed = motion shown.** Above 4 the page must actually move. If working motion cannot ship in scope, drop the dial to 3 and ship a clean static page. Never half-build motion (cut-off triggers, jumpy entries, missing cleanup).
- **Marquee max one per page.** Two horizontal marquees is lazy filler.
- **Perpetual micro-interactions** (pulse, typewriter, float, shimmer) only above 5 and only where the section benefits (status, live feeds, AI feel). Informational sections stay still. Use spring physics (`type: "spring", stiffness: 100, damping: 20`), never linear easing.
- **Magnetic or pointer physics** only above 5 and only for premium, playful, or agency briefs. Implement with Motion values outside the React render cycle.

## 3. Library choice

- **Motion** (`import { motion } from "motion/react"`): default for UI, bento, state changes, and simple scroll reveals. `framer-motion` still works as a legacy alias; prefer `motion/react` in new code.
- **GSAP + ScrollTrigger**: only for real pin or scrub work (sticky stacks, horizontal pans, scrubbed timelines). Isolate in leaf client components with `useEffect` cleanup.
- **Three.js / WebGL**: canvas backgrounds and 3D scenes, same isolation rule.
- Never mix GSAP or Three.js with Motion in the same component tree; they fight over frames.
- Every motion component is a `'use client'` leaf. Server components render static layout only.

## 4. Forbidden patterns

- `window.addEventListener("scroll", ...)` is banned. Use Motion `useScroll()`, ScrollTrigger, IntersectionObserver, or CSS scroll-driven animations (`animation-timeline: view()`).
- No `window.scrollY` or scroll progress in React state; no `requestAnimationFrame` loops that touch React state. Use `useMotionValue` and `useTransform`.
- Never `useState` for continuous input (mouse position, scroll progress, magnetic hover). It re-renders the tree every frame and collapses on mobile.
- Animate only `transform` and `opacity`. Never `top`, `left`, `width`, `height`. Use `will-change: transform` only on elements that actually animate.
- Grain and noise filters only on a fixed `pointer-events-none` pseudo-element (`fixed inset-0 z-[60] pointer-events-none`), never on scrolling containers.
- Do not wrap static content in Motion `layout` props "for safety"; use `layout` and `layoutId` only for real visible reorders, expansions, and shared elements.
- `staggerChildren` requires parent variants and children in the same client component tree. CSS alternative: `animation-delay: calc(var(--index) * 100ms)`.

## 5. Reduced motion (mandatory)

Anything above `MOTION_INTENSITY` 3 honors `prefers-reduced-motion`. In Motion use `useReducedMotion()` and degrade to static. In CSS gate under `@media (prefers-reduced-motion: no-preference)` or disable under `reduce`. Infinite loops, parallax, scroll hijacks, and magnetic physics collapse to static or instant.

## 6. Scroll-reveal stagger (lightest option)

For "items appear as they enter the viewport" with no pinning, prefer Motion's `whileInView` over GSAP.

```tsx
"use client";
import { motion, useReducedMotion } from "motion/react";

export function RevealStagger({ items }: { items: string[] }) {
  const reduce = useReducedMotion();
  return (
    <ul className="grid gap-6">
      {items.map((item, i) => (
        <motion.li
          key={item}
          initial={reduce ? false : { opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.6, delay: i * 0.06, ease: [0.16, 1, 0.3, 1] }}
        >
          {item}
        </motion.li>
      ))}
    </ul>
  );
}
```

Use for feature lists, testimonial grids, logo walls. Save GSAP for actual pin and scrub work.

## 7. Sticky stack (GSAP)

A "card stack on scroll" must be a real sticky stack, not a sequential reveal list. Common failure: `start: "top center"` fires halfway through the scroll. Fix: `start: "top top"`.

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function StickyStack({ cards }: { cards: React.ReactNode[] }) {
  const ref = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !ref.current) return;
    const ctx = gsap.context(() => {
      const cardEls = gsap.utils.toArray<HTMLElement>(".stack-card");
      cardEls.forEach((card, i) => {
        if (i === cardEls.length - 1) return;
        ScrollTrigger.create({
          trigger: card,
          start: "top top",
          endTrigger: cardEls[cardEls.length - 1],
          end: "top top",
          pin: true,
          pinSpacing: false,
        });
        gsap.to(card, {
          scale: 0.92,
          opacity: 0.55,
          ease: "none",
          scrollTrigger: { trigger: cardEls[i + 1], start: "top bottom", end: "top top", scrub: true },
        });
      });
    }, ref);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <div ref={ref} className="relative">
      {cards.map((card, i) => (
        <div key={i} className="stack-card sticky top-0 min-h-[100dvh] flex items-center justify-center">
          {card}
        </div>
      ))}
    </div>
  );
}
```

Critical points: `start: "top top"`, `pin: true`, every card except the last is pinned, and each card's shrink is driven by the next card's trigger.

## 8. Horizontal pan (GSAP)

Common failure: the track starts moving before the section is pinned, so the user sees half a slide. Same fix: pin the wrapper at `"top top"` and scrub the inner track.

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function HorizontalPan({ children }: { children: React.ReactNode }) {
  const wrap = useRef<HTMLDivElement>(null);
  const track = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !wrap.current || !track.current) return;
    const ctx = gsap.context(() => {
      const distance = track.current!.scrollWidth - window.innerWidth;
      gsap.to(track.current, {
        x: -distance,
        ease: "none",
        scrollTrigger: {
          trigger: wrap.current,
          start: "top top",
          end: () => `+=${distance}`,
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true,
        },
      });
    }, wrap);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <section ref={wrap} className="relative overflow-hidden">
      <div ref={track} className="flex h-[100dvh] items-center">
        {children}
      </div>
    </section>
  );
}
```

Critical points: `start: "top top"`, `pin: true`, `end: "+=${distance}"` (scroll length equals horizontal travel), `scrub: 1`.

## 9. Cleanup

Every `useEffect` animation returns a cleanup (`ctx.revert()`, observer disconnect). Lazy-load anything below the fold; Motion is not tiny and Three.js is large.
