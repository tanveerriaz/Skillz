# Stack Conventions, Performance, and Design-System Sources

Read this when setting up the project, adding a dependency, wiring fonts and icons, or installing one of the real design systems from `brief-and-dials.md`.

## 1. Default stack (when no official design system is chosen)

- **Framework:** React or Next.js. Default to Server Components.
  - Global state works only in client components. In Next.js, wrap providers in a `"use client"` component.
  - Any component using Motion, scroll listeners, or pointer physics is an isolated leaf with `'use client'` at the top. Server components render static layout only.
- **Styling:** Tailwind v4 by default; v3 only when the existing project demands it. For v4 do not use the `tailwindcss` PostCSS plugin; use `@tailwindcss/postcss` or the Vite plugin.
- **Animation:** Motion, imported from `motion/react`. Library rules are in `motion-patterns.md`.
- **Fonts:** `next/font` on Next.js, otherwise self-host with `@font-face` and `font-display: swap`. Never link Google Fonts via `<link>` in production.
- **State:** local `useState` / `useReducer` for isolated UI; Zustand, Jotai, or context only to avoid deep prop drilling; never `useState` for continuous input values (use Motion values).

## 2. Icons

- Allowed libraries, in priority order: `@phosphor-icons/react`, `hugeicons-react`, `@radix-ui/react-icons`, `@tabler/icons-react`.
- `lucide-react` only when the user asks or the project already depends on it.
- Never hand-roll SVG icon paths. If a glyph is missing, add a second library or compose from primitives.
- One icon family per project. Standardize `strokeWidth` globally (`1.5` or `2`).

## 3. Dependency verification (mandatory)

Before importing any third-party package, check the dependency file. If it is missing, output the install command first. Never assume a library exists. If the project uses Tailwind, confirm v3 or v4 before touching config.

## 4. Performance guardrails

- Animate only `transform` and `opacity`. `will-change` only on elements that will animate.
- Grain and noise filters only on a fixed `pointer-events-none` pseudo-element, never on scrolling containers.
- Core Web Vitals targets: LCP under 2.5s (hero image `priority` or preloaded), INP under 200ms, CLS under 0.1 (reserve space for images, fonts, embeds). Run Lighthouse before calling a page done.
- Lazy-load anything below the fold. Be aware of bundle size.
- Z-index only for systemic layers (sticky nav, modals, overlays, grain). Document the scale in a constants file.
- Every `useEffect` that starts an animation or observer returns a cleanup.

## 5. Accessibility guardrails

- `prefers-reduced-motion` honored for anything above `MOTION_INTENSITY` 3.
- WCAG AA contrast minimum for text (4.5:1) and large text (3:1); AAA target for hero copy. Applies to buttons, form inputs, placeholders, focus rings, helper and error text.
- Visible focus rings, labels on every input, alt text on meaningful images, semantic landmarks, keyboard navigation.
- Touch targets at least 44px; body text at least `1rem`.
- Dark mode designed and tested alongside light mode (rules in `typography-and-color.md`).

## 6. Install commands per design system

```bash
# Material Web (Material 3)
npm install @material/web

# Fluent UI React (v9)
npm install @fluentui/react-components

# Fluent UI Web Components (framework-free)
npm install @fluentui/web-components @fluentui/tokens

# IBM Carbon
npm install @carbon/react @carbon/styles

# Radix Themes
npm install @radix-ui/themes

# shadcn/ui (open code, owned components)
npx shadcn@latest init
npx shadcn@latest add button card badge separator input

# Primer CSS (GitHub product / devtool UI)
npm install --save @primer/css

# Primer Brand (GitHub marketing UI)
npm install @primer/react-brand

# GOV.UK Frontend
npm install govuk-frontend

# USWDS (US Web Design System)
npm install uswds

# Atlassian Design System (Atlaskit)
yarn add @atlaskit/css-reset @atlaskit/tokens @atlaskit/button @atlaskit/badge @atlaskit/section-message @atlaskit/card

# Bootstrap 5.3
npm install bootstrap

# Shopify Polaris Web Components (Shopify apps only), in the app HTML head:
#   <meta name="shopify-api-key" content="%SHOPIFY_API_KEY%" />
#   <script src="https://cdn.shopify.com/shopifycloud/polaris.js"></script>
```

## 7. Canonical sources (read before reinventing)

- **Material Web:** https://github.com/material-components/material-web , https://material-web.dev/theming/material-theming/ , https://m3.material.io/develop/web
- **Fluent UI:** https://fluent2.microsoft.design/get-started/develop , https://github.com/microsoft/fluentui , https://learn.microsoft.com/en-us/fluent-ui/web-components/
- **Carbon:** https://carbondesignsystem.com/ , https://github.com/carbon-design-system/carbon
- **Shopify Polaris:** https://shopify.dev/docs/api/app-home/web-components , https://polaris-react.shopify.com/components
- **Atlassian:** https://atlassian.design/get-started/develop , https://atlassian.design/tokens/design-tokens
- **Primer:** https://primer.style/ , https://github.com/primer/css , https://github.com/primer/brand
- **GOV.UK:** https://design-system.service.gov.uk/ , https://github.com/alphagov/govuk-frontend
- **USWDS:** https://designsystem.digital.gov/documentation/developers/ , https://github.com/uswds/uswds
- **Bootstrap:** https://getbootstrap.com/docs/5.3/layout/grid/
- **Tailwind:** https://tailwindcss.com/docs/dark-mode , https://tailwindcss.com/blog/tailwindcss-v4
- **Radix Themes:** https://www.radix-ui.com/themes/docs/components/theme , https://github.com/radix-ui/themes
- **shadcn/ui:** https://ui.shadcn.com/docs , https://github.com/shadcn-ui/ui
- **Native CSS:** MDN pages for `backdrop-filter`, `prefers-color-scheme`, `prefers-reduced-motion`, Grid layout, and scroll-driven animations; https://drafts.csswg.org/scroll-animations-1/
- **Apple Liquid Glass (Apple platforms only):** https://developer.apple.com/design/human-interface-guidelines/materials , https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass

## 8. Apple Liquid Glass: honest web approximation

Apple documents Liquid Glass for Apple platforms inside its Human Interface Guidelines and platform APIs. There is no official `liquid-glass.css` for websites. Any web version built from `backdrop-filter`, transparent backgrounds, layered borders, highlight overlays, and gradients is frosted-glass glassmorphism, not Liquid Glass. Label it that way in code comments.

```css
.liquid-glass-web-approx {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  border-radius: 999px;
  border: 1px solid rgb(255 255 255 / .32);
  background:
    linear-gradient(135deg, rgb(255 255 255 / .30), rgb(255 255 255 / .08)),
    rgb(255 255 255 / .12);
  backdrop-filter: blur(24px) saturate(180%) contrast(1.05);
  -webkit-backdrop-filter: blur(24px) saturate(180%) contrast(1.05);
  box-shadow:
    inset 0 1px 0 rgb(255 255 255 / .48),
    inset 0 -1px 0 rgb(255 255 255 / .12),
    0 18px 60px rgb(0 0 0 / .18);
}

.liquid-glass-web-approx::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background:
    radial-gradient(circle at 20% 0%, rgb(255 255 255 / .55), transparent 34%),
    linear-gradient(90deg, rgb(255 255 255 / .18), transparent 42%, rgb(255 255 255 / .14));
  pointer-events: none;
}

.liquid-glass-web-approx::after {
  content: "";
  position: absolute;
  inset: 1px;
  border-radius: inherit;
  border: 1px solid rgb(255 255 255 / .14);
  pointer-events: none;
}

@media (prefers-color-scheme: dark) {
  .liquid-glass-web-approx {
    border-color: rgb(255 255 255 / .18);
    background:
      linear-gradient(135deg, rgb(255 255 255 / .16), rgb(255 255 255 / .04)),
      rgb(15 23 42 / .42);
    box-shadow:
      inset 0 1px 0 rgb(255 255 255 / .22),
      0 18px 60px rgb(0 0 0 / .42);
  }
}

@media (prefers-reduced-transparency: reduce) {
  .liquid-glass-web-approx {
    background: rgb(255 255 255 / .96);
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }
}
```

`prefers-reduced-transparency` has uneven browser support; test it, and keep enough contrast even without blur.
