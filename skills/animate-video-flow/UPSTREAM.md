# animate-video-flow: animate-video-flow

Source: original Skillz skill — no upstream repository. Written from the production runs that built a 54-second narrated cut-paper video and then rebuilt it with a swapped music track (November 2026).

Licence: MIT.

This skill is a production flow that drives the `animate` skill (cth9191/animate, MIT) as its build engine. It does not copy or replace that skill: the look styles, the build workflow, and the measured delivery checks belong to `animate`; this skill adds the intake, look-check discipline, loudness post-step, encode verification, delivery rules, and the music-swap procedure proven across those runs.

## What changed

Nothing upstream to diff against. The flow was written fresh in the Skillz nine-section format from what the runs actually required: verify facts before writing; voice first; full-size look-check frames judged at phone size; storyboard per beat; real imagery only; licence-verified music; measured BPM/grid for a music swap with word-led cuts kept on their words; two-pass linear loudnorm to −18 LUFS when single-pass dynamic loudnorm collapses the arc; verification on the encode itself (ffprobe, loudness, frames, count-up, voice-vs-music, tail).

## Install and prerequisites

Use alongside the `animate` skill and a TTS voice of your choice. Needs ffmpeg and Python 3 for the loudness and verification steps. No API keys. The music-swap procedure needs a licensed track file (Mixkit and Pixabay are the usual sources; verify the licence on the track's own page).

## Caveats

- The flow assumes the `animate` skill is available as the build engine; without it, the look-check and measured-check steps have no implementation.
- BPM figures must be measured by onset analysis from the audio; estimates (including half-time feels) have been wrong before.
- The two-pass linear loudnorm fix is a mix-time workaround, not a change to the export tool — the skill's export tool is left untouched and the review tool validates the result.
