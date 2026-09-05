---
name: plain-instruction-voice
description: Use when writing copy for a talk deck, tutorial, onboarding flow, product explainer or documentation page and the goal is to be understood by a non-technical audience in one read — short declarative sentences, second person, concrete nouns, one idea per screen, explicit "where it stops" rules, and no hype or jargon. Also use to edit existing copy down to this register.
---

# Purpose

Produce writing that sounds like a calm expert explaining something across a
table: every sentence is short, true, checkable and about the reader. The
style does the persuading; adjectives are not allowed to.

# When to Use

- Slide titles, notes and speaker text for a 101-style talk.
- Onboarding, empty states, tooltips and setup guides.
- Explaining an AI/agent product to people who will never read a model card.
- Rewriting marketing or engineering copy that is too clever or too dense.

Do not use for legal text, API references (those need completeness over
brevity), or persuasive essays where argument structure matters more than
plain statement.

# Inputs

- The subject and the single outcome the reader should have at the end.
- The audience's vocabulary level (default: smart, busy, non-technical).
- Any hard constraints the reader must respect (safety, approval, cost).

# Outputs

- Titles: one sentence, sentence case, full stop, ≤ 9 words.
- Notes: 1–3 sentences, ≤ 30 words each, `--soft` colour in the visual system.
- Labels: single uppercase mono words that name a slot (OUTCOME, SOURCES,
  CONSTRAINTS, DELIVERABLE, REVIEW POINT).

# The voice rules

1. **One idea per screen.** If a title has an "and", split the slide —
   unless the "and" *is* the idea ("Each Bot has its own memory. They all
   share one computer.").
2. **Titles are sentences with full stops.** Not headings, not fragments,
   not questions — except one deliberate question per section to change
   gear ("How far can you push it?").
3. **Second person, present tense, active voice.** "You type the password,
   not the Bot." Never "users can", never "it is possible to".
4. **Concrete nouns over categories.** "Gmail, Slack, your calendar, your
   CRM" beats "your productivity tools". Name the thing.
5. **Say where it stops.** Every instruction about a system that acts on the
   reader's behalf includes the stopping rule: "Stop after the drafts are
   saved." "Nothing goes out without me." The stop is written as carefully
   as the task.
6. **Reassure with facts, not adjectives.** "Nothing was sent." "Nothing you
   typed ends up in the chat." Never "secure", "seamless", "powerful",
   "magical", "supercharge", "unlock", "effortless".
7. **Ban the vocabulary of the machine.** No "model", "context window",
   "token", "sandbox", "LLM", "inference", "prompt engineering". If the
   product has its own five nouns, use exactly those and no others.
8. **Numbers are small and specific.** "Start with two Bots. Not five."
   "Fourteen receipts logged. Three are missing a category."
9. **Admit limits plainly, then say what you did.** "Sometimes a website
   blocks it." → "So I let it use my Mac." Limits build trust; hiding them
   spends it.
10. **Date anything that will rot.** "Written in September 2026. These
    products change often. Check the current docs before you quote this."
11. **The close is an instruction, not a summary.** End with the one thing
    to do next: "Give it something you already hate doing."
12. **Speaker/UI text in mocks is written the same way.** Fake chat
    messages, notifications and bot replies use the identical register:
    "Four reply drafts are waiting for you. Nothing was sent."

# Sentence mechanics

- Average ≤ 12 words; maximum ≈ 22.
- No semicolons. Colons only to introduce a list of ≤ 4 items.
- No em-dashes for drama; use a full stop and start again.
- No exclamation marks. No emoji in body copy.
- Contractions are fine in speech-like lines ("wasn't built in"), rare in
  instructions.
- Parallel structure across a list: same tense, same subject, same length.

# Procedure

1. Write the outcome sentence first: "By the end you will have ___." Every
   slide must earn its place against it.
2. Draft each title as a full sentence. Cut until ≤ 9 words without losing
   the verb.
3. Under each title, write the one note that answers "so what?" or "how?".
   If you need two notes, you have two slides.
4. Find every claim about the system acting alone and add the stopping rule.
5. Strip: adjectives of quality, machine vocabulary, hedges ("basically",
   "simply", "just"), and any sentence that restates the title.
6. Read aloud. Anything you would not say to a colleague at a table gets
   rewritten.

# Quality Checklist

- [ ] Every title is one sentence, sentence case, with a full stop.
- [ ] No banned words (secure, seamless, powerful, magical, unlock, leverage,
      robust, cutting-edge, model, token, context window, sandbox).
- [ ] Every "it will do X" has a matching "it stops at Y".
- [ ] Second person throughout; no "users".
- [ ] Any date-sensitive claim carries its date.
- [ ] Final slide is an imperative the reader can act on today.

# Edge Cases

- Technical audience → keep the register; you may reintroduce *product*
  nouns (plugin, MCP server, PR) but still not model-internals vocabulary.
- Must include a comparison table → keep cells to ≤ 6 words, mark the date,
  add the "check current docs" line.
- Regulatory or safety content → the stopping rule becomes the headline,
  not the footnote.

# Safety Rules

- Never promise a capability you have not seen work. Write what happened,
  not what should happen.
- Never describe an irreversible action (send, pay, delete) without the
  approval step in the same sentence or the next.

# Examples

**Before:** "Leverage our powerful plugin ecosystem to seamlessly connect
your favourite productivity tools and unlock next-level automation."
**After:** "Plugins are how a Bot gets into your apps. Gmail, Slack, your
calendar, your CRM. Add one once; every Bot can use it."

**Before:** "The agent autonomously triages your inbox using advanced
LLM-based classification."
**After:** "It sorts your inbox into Needs me today, Waiting on others,
Newsletters and Everything else. It does not send, archive or delete
anything."
