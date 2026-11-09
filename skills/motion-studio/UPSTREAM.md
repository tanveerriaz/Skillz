# Motion Studio: motion-studio

Source: [BMatiashchuk99/Claude-Skills](https://github.com/BMatiashchuk99/Claude-Skills), skill directory `skills/motion-studio`.
Licence: [MIT](https://github.com/BMatiashchuk99/Claude-Skills/blob/main/LICENSE) — "use it for anything, including commercial videos."
This directory is an original Skillz adaptation distilled from the upstream README and skill description. It is not a copy of the upstream skill file, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream skill's documented behaviour: prompt → script and `storyboard.json` → preview stills → TTS → timeline plan → headless-Chromium render → SFX/music mix at -14 LUFS. No upstream files, scripts, or assets are bundled here; the skill is guidance only, and the upstream repo must be installed separately to run its pipeline.

## Install and prerequisites

`git clone https://github.com/BMatiashchuk99/Claude-Skills.git` then `./install.sh`. Needs Node.js 18+, FFmpeg, Python 3.9+, and Playwright/Chromium.

## Caveats

- The skill's SFX are synthesised and copyright-free; it ships no cleared commercial music. Supply your own track and confirm you have the rights to it.
- Voice options range from paid (ElevenLabs) to free/offline (edge-tts, Piper, macOS `say`, espeak); quality varies by choice.
- Rendering is frame-by-frame in headless Chromium, so a 30-second video takes minutes, not seconds.
