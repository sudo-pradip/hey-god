---
name: show-me-the-pain
description: Use when the user says "hey-god-show-me-the-pain" (or the old chant "hey-god-where-is-pain-point"), asks what's wrong with their system, why changes are slow or expensive, where the mess is, or wants to understand their codebase's problems without reading code. Explains the system as a story — components as real-world characters, relationships as the plot, and the pain named where it lives.
---

# Where Is the Pain Point

A human cannot act on "high efferent coupling in the service layer." They act instantly on "every order, no matter what it's for, has to pass through one clerk's desk — and that clerk also does the invoicing, so when you change invoicing, orders stop." Humans think in stories and places; give them the system as a small world of characters, and the pain becomes visible without reading a line of code.

Doctrine: `../doctrine/SKILL.md`; cite rule IDs from `../doctrine/rules.md` only in the technical appendix, if asked.

## How to build the story

1. **Survey first** (Iron Law 1): read the code enough to know the real components, who calls whom, where changes have historically clustered (`git log` — the files touched by every second commit are where the pain lives), and where the duplicated knowledge sits.
2. **Cast the components as real things.** Pick one coherent world — a shop, a kitchen, a post office, a hospital — and keep it for the whole story. Each component becomes a character or place with a job: the database is the warehouse, the API layer is the reception desk, the queue is the conveyor belt, the shared util module is the one drawer everyone throws things into. The casting must be *faithful*: one character per component, relationships mirror actual dependencies — the story is a map, not a decoration.
3. **Tell the plot as a journey.** Follow one real request through the world: "an order walks in the front door…". Relationships appear naturally as hand-offs. Where the code is clean, the hand-off is boring — say so and move on.
4. **Point at the pain, concretely.** Pain is where the story stops being boring: the character doing three jobs (S1), the hallway everyone cuts through (B3), the same instruction pinned on five walls (D5), the clerk who must approve everything (bottleneck), the room nobody dares enter (untested legacy). For each pain point say — in story terms, then one plain sentence — **what it costs today** ("adding a payment method means renovating two rooms") and **what it will cost at the tenth change**.
5. **Rank the pain by compounding**, not by ugliness. The messy-but-stable room nobody enters is not a pain point (ugly-but-stable can stay ugly); the slightly-untidy hallway everyone walks through hourly is.

## Output shape

```
Your system, as a <world>:
<the story — one or two short paragraphs, the journey of one request>

Where it hurts:
  1. <story name — e.g. "the clerk with three jobs"> — <plain one-liner of the real cost today and at the 10th change>
  2. ...
Doesn't hurt (leave alone): <the ugly-but-stable places, so nobody "fixes" them>
First thing worth fixing: <one pick> — because <cost it removes>.
```

**Stay in human language.** No rule IDs, no jargon, no class names in the story (file/class names may appear in parentheses after each pain point so a developer can navigate). Go technical only if the user asks — then append a plain technical section mapping each character to its module, each pain to its rule ID and penance.
