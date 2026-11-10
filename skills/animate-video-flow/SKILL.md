---
name: animate-video-flow
description: Produce a finished narrated 9:16 video with the animate skill: look check, storyboard, build, measured delivery checks, loudnorm, verify, deliver — plus the music-swap procedure.
license: MIT
---

# Purpose

Turn a brief and a set of verified facts into a finished, verdict-ready narrated 9:16 video using the `animate` skill as the build engine. This is the production flow, not the animation engine: it covers intake, the look check, storyboarding, the build, the measured delivery checks, loudness, verification on the encode itself, and delivery for a human verdict — plus how to swap the music afterwards without rebuilding the animation.

# When to Use

Use for narrated explainers, launch films, and personal-site videos where the voiceover leads and the visuals follow, built with the `animate` skill. Use the music-swap procedure when the track changes after the cut is approved. Do not use for 16:9 longform, real-footage editing, or un-narrated montages.

# Inputs

The story and every fact it states, verified against the real source (only real numbers go on screen); the voice to use; the target length; reference reels the requester sends; the music choice (composed bed or a licensed track). The requester may also name one of the `animate` skill's styles directly.

# Outputs

A 9:16 MP4 at −18 LUFS with narration, designed sound, and real imagery; look-check frames for each candidate style with the winner named and justified; a storyboard with times per beat; a `LOG.md` of fixes and compromises; a verification report on the encode itself. Nothing is posted or published by this skill — delivery is for a human verdict.

# Procedure

1. **Intake — verify the facts.** Check every claim and number against the source before writing. Only real numbers appear on screen. Write the script, then record the voiceover first: the voice is the clock, and scenes are timed to it, not the other way round.
2. **Story check.** The script must pass narration density (≤3.5 words per second per line; re-record any line that fails). Identify the spoken words the hard cuts will land on.
3. **Look check — judge full-size frames, at phone size.** Build full-size frames for EACH candidate style for the same two beats (hook + origin). Judge them at phone size, pick the winner, and record why it won and what the loser did wrong. Keep the losing frames — they are the alternative if the verdict changes.
4. **Storyboard.** One row per beat: time range, picture, motion, sound. Keep one idea per beat and one dominant accent per scene.
5. **Build.** Follow the `animate` skill's own workflow (intake → story check → look check → storyboard → build → measured delivery checks). Real imagery only, framed in the style's own device (for example torn-paper frames); never AI slop, never stock-looking images, no watermark, no whoosh SFX, no brand assets you do not own.
6. **Music.** Either a bed composed in code, or a track whose licence was verified on the track's own page (licence-free for commercial and social-media use, no attribution required where stated). Never bake a commercial trending song into the file; platform trending sounds are added at post time instead. For a **music swap** after the cut is approved: measure the track's real BPM and beat grid by onset analysis — never trust a published or estimated figure — trim or loop the best stretch to fit the story arc, re-time era boundaries and hard cuts onto the grid, keep word-led cuts on their spoken words and report the offset in frames, and preserve the arc (swell at the peak, thin at the low point, silence before the payoff, loudest at the landing).
7. **Loudness.** The skill exports around −14 LUFS; normalise to −18 LUFS as a post step. Warning: single-pass dynamic loudnorm can compress a deliberate dynamic arc (the gift-vs-peak gap collapses and the loudest window moves). If the arc collapses, mix with a two-pass linear loudnorm (constant gain) that replicates the export's mix exactly. Do not modify the export tool.
8. **Verify on the encode itself, then deliver.** ffprobe (duration, 1080×1920, 30fps), loudness (−18 LUFS target, true peak), frames read across every scene, the count-up landing exactly on its final value and holding, voice ~10 dB above the ducked music, tail check. Deliver the file for a verdict. Never post without sign-off on the exact media, caption, and account.

# Quality Checklist

- [ ] Every fact and number on screen traces to a verified source.
- [ ] Voiceover recorded before scenes were timed; narration density passes.
- [ ] Look check ran on full-size frames for every candidate style; the winner and its reasons are recorded.
- [ ] Story arc passes 6/6 (gift loudest, silence before the payoff, journey music present, gift held, goodbye decays).
- [ ] Word hits pass (hard cuts within 2 frames of their spoken words); text passes with no cut-off or overlap; dead beats pass; determinism holds.
- [ ] Count-up lands exactly on its final value and holds for at least 1 second; the loudest 100 ms window sits in the payoff act.
- [ ] Loudness is −18 LUFS with a safe true peak; voice sits ~10 dB above the ducked music.
- [ ] Frames were read from the delivered encode across all scenes; defects were fixed and logged.
- [ ] The delivered file is untouched by later rebuilds; a rebuild writes a new file.

# Edge Cases

- A cut cannot sit on both a beat and its spoken word: keep the word, report the offset, and move on. Voice-led deviations are deliberate, not defects.
- A style that looks good large can fail at phone size (a halftone field that is loud across the whole frame, for example). Judge at phone size or the check is meaningless.
- The review player for the `animate` skill runs on localhost; a remote browser cannot reach it. Review by reading frames on the build machine instead.
- Some sources block direct downloads from the build machine (Pixabay has returned 403). Keep a second licensed source ready (Mixkit) rather than stalling.
- Scheduling can be disabled for an account even when posting works; the fallback is a timed live post after review.

# Safety Rules

- Do not put an unverified fact or number on screen, and never present generated imagery as a real photo of a place or product.
- Do not ship music or SFX you have not cleared; a supplied track needs its licence verified on its own page.
- Do not bake a commercial trending song into the file.
- Do not present an invented mascot, colour, or logo as a real brand's.
- Do not post, publish, or share the video; delivery is for a human verdict.

# Examples

Good: "Make a 55-second 9:16 narrated video about my site in cut paper, using the animate skill. Voiceover first, look check both cut paper and riso, music is a licensed trap track — measure its grid and cut to it." The agent verifies the facts, voices first, runs the look check, builds, swaps the music on the measured grid, loudnorms to −18 LUFS, verifies the encode, and hands over the MP4.

Bad: "Make the video with a trending song baked in and post it." The skill refuses the baked commercial track and the unapproved post; the trending sound is a post-time option, and posting needs sign-off on the exact media, caption, and account.

Practical starting prompt: "Use animate-video-flow to make a [duration] 9:16 narrated video about [subject] in the [style] style. Voiceover first, look check included, deliver the MP4 for my verdict."
