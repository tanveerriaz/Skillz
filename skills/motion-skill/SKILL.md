---
name: motion-skill
description: Use when motion must look its smoothest: standalone 60fps motion-graphic explainers, speech-synced B-roll and cutaways for talking-head videos, or isolating a subject from video backgrounds with Meta's SAM 2, running 100% locally.
license: MIT
---

# Purpose

Create standalone 60fps motion-graphic explainer videos, make speech-synced B-roll and cutaways for talking-head videos, and isolate subjects (people, products, hands) from video backgrounds using Meta's SAM 2 — running 100% locally, with nothing uploaded.

# When to Use

Use for explainer videos where smoothness is the point, for B-roll that must land on the spoken word, and for cutting a real person or product out of footage without a cloud service. Commands: `/motion`, `/motion b-roll`, `/motion panel`, `/motion separate`. Do not use when the job needs a full production pipeline with budgeting; a studio skill fits that better.

# Inputs

A brief and script for explainers; for B-roll mode, an existing talking-head video plus its transcript (`.srt` / `.vtt`); for SAM 2 mode, the video and the subject to isolate, plus the hardware available so the right model can be picked.

# Outputs

A 60fps MP4 explainer, full-frame cutaways, or transparent ProRes 4444 (`.mov`) overlay panels for picture-in-picture, and for SAM 2 mode the subject highlighted plus one mask PNG per frame. Nothing is built until the clip-by-clip plan is approved.

# Procedure

1. Take the brief and write the clip-by-clip plan; wait for approval before building anything.
2. For explainers, build continuous one-shape motion clips that never cut: a single shape morphs size, corners, and colour while content swaps with a short blur, and a realistic cursor drives changes with clicks and drags, every change landing on a spoken word or beat.
3. Render frame by frame with 4x subframe motion blur at 60fps.
4. For B-roll, sync cutaways to the talking-head video and transcript, as full-frame cutaways or transparent overlay panels.
5. For SAM 2, pick the model by hardware: large (~898 MB, NVIDIA 12GB+ VRAM), base-plus (~323 MB, smaller GPU or Apple Silicon), or tiny (~156 MB, CPU only, ~5s/frame, so separate only the section needed).
6. Inspect the frames before delivery.

# Quality Checklist

- [ ] The clip-by-clip plan was approved before any build.
- [ ] Every change lands on a spoken word or a beat; nothing moves off-beat.
- [ ] Motion blur is present; 60fps output is actually 60fps.
- [ ] Cutaways match the transcript timing; overlay panels are genuinely transparent.
- [ ] SAM 2 masks are clean; the subject is fully separated with no halo.

# Edge Cases

- The tiny SAM 2 model runs at ~5s/frame on CPU. Separate only the section needed, not the whole video.
- B-roll panels are ProRes 4444 `.mov`; confirm the editor accepts transparent ProRes before promising picture-in-picture.
- The skill is small and new: only 2 stars, 5 commits, created 2026-10-08. The capability is the outstanding part, not the adoption. It is far less battle-tested than the bigger video skills in this repo.

# Safety Rules

- Do not upload footage anywhere; SAM 2 runs locally by design. If a step asks for an upload, stop and check.
- Do not present a cut-out subject as if it was filmed that way; label composites as composites.
- Do not promise SAM 2 results on hardware that cannot run the chosen model.

# Examples

Good: "Make a 60fps explainer about how our sync engine works, and cut B-roll for my talking-head intro from the transcript." The agent plans clip by clip, gets approval, renders with motion blur, and syncs the cutaways.

Bad: "Separate my whole 10-minute video on CPU." The agent must explain the ~5s/frame cost and separate only the section needed, or pick a GPU model.

Practical starting prompt: "Use motion-skill to make a 60fps explainer about [subject]. Show me the clip-by-clip plan first."
