# Visual design and QA

The template combines a newspaper's serif masthead, ruled columns and editorial hierarchy with bank-inspired navy, blue and green. It is not a reproduction of an official bank brand. Use official logos only when supplied/authorized; avoid implying endorsement.

## Layout details

- Desktop (1440px): centred 1260px paper, fluid outer margins, 2:1 lead/briefing split, three supporting columns, thin vertical rules, shared quantitative strip.
- Laptop (1280px): fluid gutters and slightly smaller masthead, preserving line length and strong first-screen hierarchy.
- iPad/tablet (768–1024px): two-column story grid, wrapping masthead/controls, no narrow three-column body text. Portrait lead stacks above the rail.
- Phone (390px, also 320px): single reading column, 18px gutters, wrapping buttons, search fills the row, large tap targets and no horizontal scrolling.
- Serif titles and sans-serif utilities use system fonts (Georgia; Arial/Segoe UI). No font CDN, icon library or external script.
- Use whitespace and rules, not floating-card repetition, gradients, fake market tickers or unexplained live dots. Do not imply a current feed from a static edition.
- Charts carry visible values, denominators and units. Decorative visuals do not pretend to be news photographs.

## Accessibility and motion

- Native links/buttons, explicit input labels, landmarks and clearly visible focus rings.
- Touch controls have at least 44px hit areas where practical. Hover is never required to access content; source references also work by tap and keyboard.
- Filters have aria-pressed; result count is a polite status. Clear restores the full view.
- Citation links degrade to ledger anchors. Escape and Close dismiss the source dialog; focus returns to the link. Native dialog provides focus containment.
- No reporting relies on JavaScript. No autoplay, ticker, flashing, parallax or number-counting.
- Motion only clarifies state changes, <=180ms. Honor prefers-reduced-motion and a manual toggle. Do not claim full WCAG certification from basic checks.
- Print includes all stories, explicit source details/URLs and the sample label. Pagination varies by printer.

## Required tests

1. Renderer tests: missing/duplicate IDs, nonexistent references, nonfinite metrics, invalid totals, timezone-free timestamps and unsafe URL schemes fail.
2. Trace facts/calculations to actual inputs; structural tests are not fact checks.
3. Inspect 1440, 1280, 1024, 768 and 390px widths, plus 320px stress test and long text. Check clipping, overflow, reading order and tap targets.
4. Search a known phrase and nonexistent phrase, combine with section filters, clear. Each citation opens its exact entry and closes by Escape/button.
5. Keyboard through controls; confirm dialog focus return and 200% text/zoom usability.
6. Emulate reduced motion and disable JavaScript; content stays readable.
7. Inspect print after filtering; all stories return, controls and modal do not print, ledger details appear.
8. Verify no unexpected network requests. Never bundle cookies, tokens, credentials or unnecessary private communications.

Report completed checks and untested environments. Do not describe untested email-body or native Teams rendering as verified.

## Exact template tokens

- Navy #071F4B; blue #006EAA; green #007C42; pale mint #E7F3EB. Body ink #182739, secondary text #526274, rules #C8D1D8, paper #FFFEFB, surrounding canvas #F0F3F5. Focus outline #B95C00, 3px with 4px offset.
- Desktop interior gutters 38px, lead gap 36px, supporting-story gap 28px; tablet gutters 24px, phone gutters 18px. Fine rules 1px; masthead rule 3px.
- Desktop masthead up to 82px, lead headline up to 50px, supporting headline 27px, body 15–16px. Phone masthead 45px, lead 36px, supporting headline 29px and body 16px. Line height 1.65 for reporting prose, 1.06–1.13 for headlines.
- Maximum desktop paper width 1260px. Layout changes at 1100px, 820px and 520px. Utility text is smaller than reporting prose and remains secondary. Long URLs wrap in source details.
- Buttons/search are at least 44px high except secondary clear and inline citations; citations enlarge on phone. Native focus and content order are preserved; no hover-only actions.
- Motion duration 160ms, limited to subtle article entrance and state transitions. The operating-system reduced-motion preference takes precedence; the control reports the system state truthfully.
