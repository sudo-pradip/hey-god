---
name: show-me-the-pain
description: Use when the user says "hey-god-show-me-the-pain" (or the old chant "hey-god-where-is-pain-point"), asks what's wrong with their system, why changes are slow or expensive, where the mess is — or asks to explain a specific problem, bug, error, or concept in plain language. Two modes - the system-wide pain audit told as a story, and the on-demand layman explanation of one pain/concept with an ASCII flow and a classified root cause.
---

# Show Me the Pain

A human cannot act on "high efferent coupling in the service layer." They act instantly on "every order, no matter what it's for, has to pass through one clerk's desk — and that clerk also does the invoicing, so when you change invoicing, orders stop." Give the human the truth in their language, sized to act on — whether the question is "what's wrong with my whole system" or "explain this one thing that's breaking."

Doctrine: `../doctrine/SKILL.md`; rule IDs only in a technical appendix, and only if asked.

**Both modes share the voice:** plain layman's language, bottom line first, define jargon in one phrase at first use, **no bluff** — a guess is labeled a guess, an unknown is "I don't know yet, here's how I'd find out." Keep it short; depth on request.

## Mode 1 — The system audit (the story)

For "what's wrong with my system / why is every change slow":

1. **Survey first** (Iron Law 1): read enough code to know the real components, who calls whom, and where changes historically cluster (`git log` — files touched by every second commit are where the pain lives).
2. **Cast the components as real things** in one coherent world — a shop, a kitchen, a post office. Each component is a character or place with a job: the database is the warehouse, the API layer the reception desk, the shared util module the one drawer everyone throws things into. The casting must be *faithful* — one character per component, relationships mirroring actual dependencies. The story is a map, not decoration.
3. **Tell one real request's journey** through the world; hand-offs are the relationships. Where the code is clean, the hand-off is boring — say so and move on.
4. **Point at the pain** where the story stops being boring — the character with three jobs (S1), the hallway everyone cuts through (B3), the same instruction pinned on five walls (D5) — each with its cost today and at the 10th change. **Rank by compounding**, not ugliness; the messy room nobody enters is not a pain point.

```
Your system, as a <world>: <the journey, one-two paragraphs>
Where it hurts:
  1. <story name> — <plain cost today and at the 10th change> (file/class in parentheses)
Doesn't hurt (leave alone): <the ugly-but-stable places, so nobody "fixes" them>
First thing worth fixing: <one pick> — because <cost it removes>.
```

## Mode 2 — Explain one pain or concept (on demand)

For "explain this", "why does X break", "what is this error/setting/pipeline actually doing": plain layman's language, bottom line first. Name **every tool and setting involved** — what it is, its purpose, and a real-world analogy — then show how they connect in a simple ASCII flow diagram, with the break point marked. Investigate before explaining (read the code, run the reproduction, search the error verbatim — no bluff means no explaining from vibes).

ALWAYS use this exact shape:

```
Bottom line: <what's happening / what this is, one-two sentences>

1. Affected area:   <which part of the system/user experience feels it>
2. Scenarios:       <when it shows up — the real situations that trigger it>
3. Input:           <what goes in when it happens — the data/request/event>
4. Components:      <each tool/setting involved — what it is, its purpose, real-world analogy>
5. Where it breaks:
      input → [component A] → [component B] → ✗ [component C] → expected outcome
                                              ↑ breaks here: <one line>
6. Root cause:      <classified — OUR HANDLING (our code/config does the wrong thing)
                     | UPSTREAM (a lib/package/external service behaves this way — cite the
                       issue/doc if found) | COMBINED (upstream quirk + our missing guard)>
```

The root-cause classification matters because the fix differs: our handling → fix the code (route to `../purify-me/SKILL.md` or `../bring-it-to-life/SKILL.md`); upstream → pin/patch/wrap it (B6) and link the evidence; combined → guard at our boundary and note the upstream watch. If the conversation has been circling this problem for a while, hand it to `../give-me-third-eye/SKILL.md` instead — deflation first, explanation after.

Stay in human language throughout; file/class names in parentheses so a developer can navigate. Go fully technical only when asked — then append a mapping of each character/component to its module and each pain to its rule ID and penance.