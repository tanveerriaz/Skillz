---
name: safe-ui-enhancement
description: Use when restyling or improving an existing UI without breaking it. Reads the brand reference first, identifies the JavaScript and auth hooks a change might break, proposes changes before editing, and enforces responsive + accessibility checks — so visual upgrades stay on-brand and don't break functionality.
---

# Purpose

Improve interfaces without breaking them. UI edits routinely break things by renaming IDs that JavaScript relies on, altering forms that auth depends on, or drifting from the brand. This skill makes visual change deliberate: reference the brand, map the risky hooks, propose before editing, and verify responsive/accessible behavior.

# When to Use

Use when restyling pages, polishing components, applying a brand to existing markup, or doing any visual enhancement of a live UI — especially around auth screens, dashboards, landing pages, and forms.

# Inputs

- The component/page to change and the desired visual outcome.
- The brand reference (existing landing page or style source): colors, typography, button/card styles, spacing.
- The JavaScript and auth elements the markup depends on.

# Outputs

- A proposed change table (element → current → proposed → reason) for approval before editing.
- On-brand changes that preserve all functional hooks.
- Verified responsive behavior and accessibility.

# Procedure

1. **Read the brand reference first.** Extract exact colors/gradients, fonts, button and card styles, shadows, and spacing from the canonical source. Don't invent new brand values.
2. **Map functional dependencies.** Find element IDs/classes referenced by JS (`getElementById`, `querySelector`) and anything auth relies on (form actions, input names, OAuth handlers, `data-*` hooks). These are protected.
3. **Propose before editing.** Present a change table (element, current classes, proposed classes, reason). Wait for approval on anything non-trivial.
4. **Change incrementally.** One component at a time; verify in the browser before moving on.
5. **Preserve protected elements.** Never rename/remove IDs or alter form structures that JS or auth depend on without confirming the dependency is handled.
6. **Verify responsive.** Check mobile / tablet / desktop: touch targets ≥ 44px, readable text, no horizontal scroll.
7. **Verify accessibility.** Contrast ≥ 4.5:1, visible focus states, labels on inputs, alt text, semantic structure, keyboard navigation. Respect `prefers-reduced-motion`.

# Quality Checklist

- [ ] Brand values taken from the reference, not invented
- [ ] JS/auth-dependent elements identified and preserved
- [ ] Changes proposed (change table) before editing non-trivial UI
- [ ] One component changed and verified at a time
- [ ] Responsive across mobile/tablet/desktop
- [ ] Accessibility checks pass (contrast, focus, labels, keyboard)
- [ ] Functionality re-tested after the change

# Edge Cases

- **ID is used by JS and needs to change:** update the JS reference in the same change, or keep the ID and restyle via class.
- **Auth form restyle:** change only presentation; never touch action URLs, input names, or handlers.
- **No brand source exists:** define a minimal palette/typography first, then apply consistently.
- **Animation requests:** keep them subtle (≤ ~300ms), purposeful, and reduced-motion-aware.

# Safety Rules

- Never rename or remove IDs/classes that JavaScript depends on without handling the reference.
- Never alter form structures or input names that authentication relies on.
- Never use colors or type outside the brand palette.
- Never skip responsive and accessibility verification.

# Examples

**Good:** Proposed change table: `.login-btn` `px-4 py-2 bg-blue-500` → `px-6 py-3 bg-gradient-to-r from-orange-500 to-orange-600` (reason: match brand). After approval, restyle only, keep the button's ID and click handler, verify on mobile, confirm contrast ≥ 4.5:1.

**Bad:** Renaming `#submit-login` to `#cta` to "clean up", silently breaking the auth handler that targets the old ID.
