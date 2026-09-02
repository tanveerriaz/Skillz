# Hackathon Pitch Playbook

This playbook distils [How to hack a Hackathon: Pitch Perfect](https://medium.com/@agrimsingh/how-to-hack-a-hackathon-pitch-perfect-8c3057fe617b) into reusable working patterns. It is a paraphrase and adaptation, not a reproduction of the article.

## Problem framing card

```text
Target person:
Situation:
Current workaround:
Pain, risk, or opportunity:
Evidence:
Assumptions still unverified:
Why this event/theme is a fit:
```

Prefer evidence from direct conversations. When that is unavailable, use credible public sources and label the gap. A useful solution should fit into the target person's established behaviour where possible, rather than requiring an implausible change of habit.

## Product promise card

```text
For [specific person] in [specific situation],
we help them [recognisable outcome]
by [mechanism].

Success looks like:
The one capability everything depends on:
What is real in the prototype:
What is simulated or prepared:
```

If the critical capability fails, the rest of the product should not be treated as convincing. Make that capability work end to end before adding supporting features.

## Feature scoring matrix

Score each candidate from 1 (low) to 5 (high).

| Feature | Rubric value | Demo value | Effort | Failure risk | Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| Critical capability |  |  |  |  | Must-have |
| Supporting feature |  |  |  |  | Must-have / Stretch / Cut |
| Memorable moment |  |  |  |  | Must-have / Stretch / Cut |

Keep the feature when rubric and demo value clearly outweigh effort and failure risk. Limit the golden path to the critical capability plus one or two supporting features.

## Golden demo script

```text
1. Context: In one sentence, show who has the problem and when it occurs.
2. Action: Let the user perform one clear, realistic action.
3. Response: Make the critical technical capability visible.
4. Outcome: Show the meaningful change for the user.
5. Proof: State what worked, what was measured, and what was prepared.
```

Aim for a path that can be repeated without explanation. A memorable visual, device, or interaction is useful only when it sharpens the message and is reliable enough to rehearse.

## Timeboxed build plan

Allocate percentages of the remaining time rather than assuming a fixed event length.

| Phase | Target | Suggested share |
| --- | --- | ---: |
| Setup and scope | Dependencies ready, promise agreed, owners assigned | 10% |
| First end-to-end path | Rough golden path works once | 25% |
| Core reliability | Critical capability works repeatedly | 30% |
| Demo and visual polish | Flow is legible and memorable | 15% |
| Pitch assets and fallback | Slides, fixture, recording, submission files | 10% |
| Rehearsal and freeze | Timed runs, recovery practice, final upload | 10% |

Move the first end-to-end milestone earlier when integrations are uncertain. Prepare accounts, packages, hardware, starter code, test data, and credentials before the event when rules permit.

## Rubric-to-proof map

| Judging dimension | Weight | Proof in build | Proof in pitch | Time emphasis |
| --- | ---: | --- | --- | ---: |
| Problem / impact |  |  |  |  |
| Originality |  |  |  |  |
| Technical execution |  |  |  |  |
| Usability / design |  |  |  |  |
| Demo / presentation |  |  |  |  |

Spend build and speaking time in proportion to the actual rubric. If the rubric is unavailable, mark these dimensions as provisional rather than presenting them as official criteria.

## Three-minute pitch structure

```text
0:00-0:25  Human problem and evidence
0:25-0:40  One-sentence promise
0:40-1:55  Live golden-path demonstration
1:55-2:25  Critical technical differentiation
2:25-2:45  Impact, limitations, and what is real
2:45-3:00  Memorable close and next step
```

Adjust the timing to the event. Keep the problem, context, status quo, and solution clear enough that technical detail strengthens the story instead of replacing it.

## Judge objection sheet

Prepare concise, evidence-based answers.

```text
Why this problem?
Why this user and moment?
Why is the current workaround insufficient?
What is technically difficult or differentiated?
What did you build during the event?
What is simulated, manually prepared, or future work?
How do you know the core capability works?
What are the privacy, safety, and accessibility limits?
What would you validate next?
```

## Demo fallback ladder

1. Retry the live path once using a known-good input.
2. Switch to a controlled local fixture that exercises the same interface.
3. Show a short recording of the successful path.
4. Use screenshots only as the final fallback.

Tell judges when a fixture or recording is being used. Never imply that a simulated dependency is live.

## Freeze checklist

- [ ] Golden path passes repeatedly with realistic and known-good inputs.
- [ ] Presenter can recover from the likeliest failure without derailing the story.
- [ ] Demo device, display, network, audio, accounts, and permissions are checked.
- [ ] Fixture and recording contain no secrets or personal data.
- [ ] Pitch fits the time limit with room for transitions.
- [ ] Claims distinguish demonstrated capability from future work.
- [ ] Submission files, links, eligibility requirements, and upload status are verified.
- [ ] Feature changes are frozen before the final rehearsal.
