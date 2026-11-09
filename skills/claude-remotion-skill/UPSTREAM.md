# Claude Remotion Skill: claude-remotion-skill

Source: [haidrrrry/claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill).
Licence: [MIT](https://github.com/haidrrrry/claude-remotion-skill/blob/main/LICENSE) — use it, fork it, ship videos with it.
This directory is an original Skillz adaptation distilled from the upstream README and skill description. It is not a copy of the upstream skill file, and it is not an official release or endorsement by the upstream author.

## What changed

`SKILL.md` was written fresh in the Skillz nine-section format from the upstream skill's documented behaviour: 10 non-negotiable motion rules plus a mandatory render → inspect frames → fix → re-render loop, covering springs, staggered choreography, colour grades, film grain, Ken Burns, word-synced captions, and sound design. No upstream files, scripts, or assets are bundled here.

## Install and prerequisites

`git clone https://github.com/haidrrrry/claude-remotion-skill.git`. Needs Remotion (free, open source) and a Claude subscription or API access.

## Caveats

- The skill is a discipline layer, not a renderer. Remotion does the rendering; the skill makes the motion worth rendering.
- Upstream framing: "Remotion is never the bottleneck — motion-design craft is."
