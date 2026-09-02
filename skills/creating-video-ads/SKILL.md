---
name: creating-video-ads
description: Use when a user asks to turn a website URL, product page, brief, or existing advertisement into a short-form video ad, Reel, TikTok, Short, product demo, launch video, revised voiceover cut, or deployment-ready MP4.
---

# Creating Video Ads

## Overview

Build ads from product truth outward. A polished render is not deployment-ready if its positioning, claims, local context, voice, security, or delivery integrity is wrong.

## Workflow

1. **Inspect before scripting.** Read project instructions, product code/copy, prior ads, brand assets, and the supplied URL. Browse current websites when needed. Separate verified capabilities from requested marketing claims.
2. **Correct the brief.** Challenge unsupported ordering, download, endorsement, trust, user-count, partner, price, or certification claims. Do not encode third-party feedback blindly.
3. **Approve the design.** **REQUIRED SUB-SKILL:** Use `superpowers:brainstorming` for a new creative direction. Present the corrected positioning, audience, duration, format, story beats, asset strategy, and CTA before implementation.
4. **Isolate production.** Create a distinctly named project/version. Preserve previous ads and unrelated application changes. Never commit, push, publish, deploy, spend money, or upload externally without authorization.
5. **Capture product truth.** Prefer real browser/app recordings and real result data over fabricated UI. Use owned or licensed assets; add culturally specific imagery only when accurate. Never present synthetic people as testimonials.
6. **Write to timing.** Use the template in [references/brief-template.md](references/brief-template.md). Make each spoken claim visible or provable. Keep CTA wording consistent with the actual product surface.
7. **Generate natural audio.** Prefer a suitable human or neural regional voice. Generate scene-aligned takes, correct pronunciation, and adjust wording/rate before using time compression. Keep music below narration.
8. **Build and inspect.** For URL-based HTML video work, **REQUIRED SUB-SKILL:** Use `hyperframes:website-to-hyperframes`, then `hyperframes:hyperframes` and `hyperframes:hyperframes-cli`. Otherwise follow the target project's established video stack.
9. **Apply quality gates.** Read [references/quality-gates.md](references/quality-gates.md). Fix layout, contrast, timing, factual, cultural, audio, and security failures before rendering.
10. **Render and prove delivery.** Render a uniquely named master. Run `scripts/verify_video.sh` with the final composition source. If copying to iCloud or another authorized destination, verify byte equality and SHA-256. **REQUIRED SUB-SKILL:** Use `superpowers:verification-before-completion` before claiming success.

## Verification Command

```bash
"${CODEX_HOME:-$HOME/.codex}/skills/creating-video-ads/scripts/verify_video.sh" \
  --video /absolute/path/final.mp4 \
  --source-root /absolute/path/composition \
  --destination /absolute/path/delivered.mp4
```

Use `--allow-claims` only when every flagged phrase is supported by inspected product evidence.

## Common Mistakes

- Treating a consultant or AI review as product truth.
- Saying “app,” “download,” or “order” for a browser-only discovery product.
- Matching natural voice with generic or culturally vague visuals.
- Rendering before checking hero frames and complete media decode.
- Reporting an upload from file presence without checksum evidence.
# Purpose

Turn product truth into a short video advertisement that is persuasive, locally credible, and ready for its delivery channel.

# When to Use

Use for short-form ads, Reels, TikToks, Shorts, product demos, launch cuts, or revised voiceover versions.

# Inputs

Product source, audience, market, claim evidence, desired duration, aspect ratio, assets, and delivery requirements.

# Outputs

A structured concept, script, shot plan, rendered video, and verification record appropriate to the request.

# Procedure

Use the research, scripting, production, localization, security, and delivery workflow above; verify product claims before rendering.

# Quality Checklist

- [ ] The hook, proof, and call to action match the product and audience.
- [ ] Claims and localized details are verified.
- [ ] The final export passes visual, audio, duration, and integrity checks.

# Edge Cases

When source material is incomplete, narrow the claim and use clearly labelled placeholders instead of inventing product behavior.

# Safety Rules

Never fabricate testimonials, performance claims, prices, endorsements, or product capabilities; keep credentials and private footage out of renders.

# Examples

**Good:** A 20-second vertical ad grounded in the live product with readable captions and a verified CTA. **Bad:** A polished montage whose claims do not appear in the source.
