---
name: motion-design-taste
description: "Judge and direct motion graphics by the taste rules that make a cut feel premium: one idea at a time, real imagery, odometer counters, kinetic type, cut-paper warmth, and music that matches the animation's energy."
license: MIT
---

# Purpose

Teach an agent (or a reviewer) the taste rules that separate a premium motion-graphics cut from a generic one, learned from reference reels and from blunt verdicts on real cuts. The rules are portable: they judge any narrated short-form video, and they direct a rebuild with specific fixes instead of vague notes.

# When to Use

Use when judging a cut, directing a rebuild, picking a look, or choosing music and voice. Use when a cut feels "dry", "basic", or "off" and the reason is not yet named. Do not use as a substitute for the build skill — this is the judging layer, not the renderer.

# Inputs

The cut under review (or its frames), the reference reels that set the bar, and the brief it was built to. A verdict needs something to compare against: no reference, no judgement.

# Outputs

A plain verdict ("better", "not yet", "way better") plus the specific things to keep and the specific things to change — a named fix per fault, not a mood.

# Procedure

1. **Watch the reference in full, then name the recipe.** Write down the exact technique in one paragraph: what moves, when, in what type, in what colour, on what beat. Borrow the technique only — never the creator's logos, wording, or assets.
2. **Judge the cut beat by beat against the rules below.** One fault per beat, named precisely.
3. **Give the verdict first, then the fixes.** A verdict without fixes is a shrug; fixes without a verdict are noise.

## The rules

- **One idea at a time.** One beat, one idea, 2–4 seconds. If two ideas share a beat, split the beat.
- **Huge negative space.** Let the frame breathe. A crowded frame reads as cheap at phone size.
- **One accent colour per scene**, sampled into the background glow. A second accent must earn its place.
- **Bold grotesk type, huge where it matters.** The key noun is the visual beat. Small type is for connective tissue only.
- **Slow soft eases and spring flips with real physicality.** Entrances ease out; flips need damping and stiffness that feel like a real object, verified frame by frame — no pops.
- **Real imagery, framed.** Real photos and screenshots, framed inside the style's own device (cards, torn-paper frames). Never AI slop, never stock-looking images, and never present generated imagery as a real photo.
- **Kinetic type that leads the beat.** The type changes on every spoken phrase (~every 1–2 s): giant keywords for the nouns, handwritten script for connective words, small pill labels for the little words. Density is a choice: maximalist kinetic type is loud on purpose; minimalism is spare on purpose. Pick one and commit.
- **A draw-on origin story.** Where the piece has an origin (a park, a first sketch), let it draw itself on screen.
- **Odometer counters.** Numbers roll vertically, digit by digit, right-most digits fastest, easing out to an exact landing with a soft settle (never a bounce), ~1.5–2 s, the comma holding still, then a still hold of at least 1 s so the final value reads. Never glitch, scramble, or Matrix rain over the number itself.
- **Cut-paper warmth.** Handmade devices — taped tags, torn frames, a small character that carries through the piece (for example, gaining a ray every time a question finds its answer). Warmth fits personal stories better than print-shop boldness.
- **Music must match the animation's energy.** A calm bed under lively pictures reads as a mismatch, not as restraint. If the pictures are upbeat, the music is upbeat.
- **The voice must suit the picture.** A voice that fits one cut can feel wrong on another; when it does, change the voice or its pace before touching the animation.
- **The loudest moment is the payoff.** The count-up landing or final beat is the loudest window in the piece. If the loudest moment sits anywhere else, the arc is broken.

# Quality Checklist

- [ ] The verdict names what is good and what is not, in plain words.
- [ ] Every fault has a named fix (a rule, a frame, a number — not "make it better").
- [ ] The reference recipe is written down before the cut is judged.
- [ ] The music and voice were judged against the pictures, not in isolation.
- [ ] The count-up, if any, follows the odometer rule exactly.

# Edge Cases

- A reference can be deliberately maximalist ("too much effects" is the point). Do not judge a maximalist cut by minimalist rules, or the reverse — name which game it is playing first.
- A style that wins at full size can lose at phone size (a halftone field that drowns the content). Judge at phone size.
- Taste is taught by verdicts, not by lists: keep the verdicts ("nope, dry, animation needs to be high quality") next to the rules they produced, so the next reviewer learns the same lesson.

# Safety Rules

- Do not present an invented mascot, colour, or logo as a real brand's.
- Do not borrow a creator's wording, assets, or logos — technique only.
- Do not call a cut finished because it is loud or busy; density is not quality.
- Do not soften a verdict to spare feelings; a plain verdict is what makes the next cut better.

# Examples

Good: "The animation is amazing; the voice and music don't match its energy. Keep the pictures, change the music to something upbeat and re-test the voice." The verdict is plain, the pictures are protected, and each fault has one fix.

Bad: "It's nice, maybe make it pop more." No verdict, no rule, no fix — the next cut guesses.

Practical starting prompt: "Use motion-design-taste to judge this cut against [reference]. Give me the verdict first, then the fixes, one per fault."
