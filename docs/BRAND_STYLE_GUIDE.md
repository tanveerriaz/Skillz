# Brand Style Guide

How Skillz sounds and what it stands for.

## Identity

**Skillz — Reusable AI-agent skills for builders who ship.**
Curious mind. Builder mode! 🇸🇬

Alternate tagline: _From prompt chaos to repeatable execution._

## Voice

Strategic, practical, clear, builder-focused. Skillz reads like a disciplined delivery partner: someone who has shipped real systems, respects the reader's time, and explains the next concrete step. Friendly but professional. Banking-grade discipline without the corporate stiffness.

## Principles

- **Builder-first.** Real steps over theory. Every skill ends in something the reader can do.
- **Security-first.** Guard secrets, private data, and destructive actions by default.
- **Repeatable execution.** Standardize what works so it can be reused.
- **Practical AI workflows.** Useful in real projects, not demos.
- **Reusable agent skills.** Generalized to work across stacks and tools.

## Preferred phrases

- builder-first
- ship real systems
- repeatable execution
- security-first
- practical AI workflows
- from prompt chaos to execution
- reusable agent skills

## Avoid

- revolutionary
- game-changing
- magic
- unleash AI
- 10x everything
- fully autonomous without review
- buzzword padding, corporate fluff, vague AI claims
- private references (employer, client, project codenames, internal systems)

## Formatting conventions

- Plain English; short sentences; active voice.
- Numbered procedures for steps; checkboxes for checklists; imperatives for safety rules.
- Show a concrete **Good** and **Bad** example wherever it clarifies.
- No emoji in skill bodies (the repo identity line is the one exception).
- Keep skills lean — signal over length. If a section has nothing real to say, tighten it; don't pad.

## Colors

Skillz uses a **slate + amber** identity: a dark, focused base (the discipline) with a warm amber/orange accent (the builder energy). It deliberately stands apart from the purple/coral palettes common in the Claude-skills ecosystem.

| Token | Hex | Use |
|-------|-----|-----|
| Slate 950 (base) | `#0B1220` | Banner background (darkest) |
| Slate 900 | `#0F172A` | Primary dark background, badge label |
| Slate 800 | `#1E293B` | Secondary surface / gradient end |
| Slate 400 | `#94A3B8` | Muted text / secondary signature |
| Slate 200 | `#E2E8F0` | Light text on dark |
| Amber 300 | `#FCD34D` | Highlight / chips |
| Amber 400 | `#FBBF24` | Accent (lighter) |
| Amber 500 | `#F59E0B` | **Primary accent** (wordmark, badges) |
| Orange 500 | `#F97316` | Accent gradient end / energy |

Gradient: `#FBBF24 → #F59E0B → #F97316` for the wordmark and accent bars.
Badges: amber foreground on `labelColor=0F172A` (slate-900).

Brand assets live in `assets/` (`skillz-banner.svg`, `skillz-logo.svg`). Keep new visuals on this palette; clean, Apple-like spacing; no clutter.

## Tone test

Before shipping copy, ask: would a skeptical senior engineer or founder find this useful and honest? If it sounds like marketing or an AI wrote it to impress, rewrite it plainer.
