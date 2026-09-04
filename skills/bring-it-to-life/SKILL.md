---
name: bring-it-to-life
description: Use when the user says "hey-god-bring-it-to-life" (or the old chant "hey-god-help-me-in-feature") or is adding a feature, endpoint, integration, or capability to an existing codebase.
---

# Guide — hey-god-bring-it-to-life

You know how to write the feature. The defaults to displace: starting to code before locating where this kind of change *lives*, writing in your preferred style instead of the codebase's, and quietly widening shared things for one consumer. Sequence and criteria:

1. **Find the neighborhood before designing anything.** Grep the feature's domain nouns; find the last similar merged change (`git log`) — recent accepted precedent beats any general principle. Identify the style in play, because the right move differs: plugin systems want a plugin, event systems want a new event + subscriber (never a widened payload — B4), services want the change in the data's owner. Read the conventions — error style, naming vocabulary (N2), test patterns, DI — and conform even where you'd choose differently (Iron Law 1, ../doctrine/SKILL.md; rule IDs: ../doctrine/rules.md). Read relevant ADRs; if the feature forces a significant decision, write one (A5). *Done when: you can name the file(s) where the last similar feature landed.*

2. **Choose the insertion point — this exact ladder, stop at the first rung that holds:**
   1. A seam exists → new implementation/plugin/handler, working code unedited (S2).
   2. No seam, *first* divergence → plain conditional, edit directly. One honest `if`; no strategy pattern for a second case that may never come (D3, D4).
   3. Same conditional now in ≥2 places → the seam is born NOW (D4): preparatory refactor as its own green step, then the feature through it.
   4. Fits no existing module → that's a signal: propose a new module with a one-paragraph rationale; never wedge it into the nearest-sounding one.

3. **Policy and detail stay separated as you build** (B1): new business rules in policy, new I/O at the edge, external calls behind an interface defined next to the use case that needs it (B6). No framework type smuggled inward.

4. **Contract discipline** on anything with external callers (B5, S3): additive only; verify "no one uses this" with evidence, never assumption; a truly breaking change gets versioning or expand–migrate–contract as separate visible steps.

5. **Tests ride with the feature**: in the codebase's test style, through the boundary (T2); untested shared code you touch gets a characterization test first (T1) — part of the feature's cost, not extra credit; cover the boundaries and each error branch you added (T4).

6. **Blast-radius gate before finishing.** *Every changed line must trace to the feature.* One module + tests = healthy. Ripples across many modules = wrong insertion point (back to step 2) or real structural debt — say so and *propose* the restructuring, don't silently perform it.

**Report:** where it lives and why; seam used or seam created (and why now); contract impact (none/additive/versioned); tests added; deliberately-NOT-built with its add-when trigger; proposed cleanups.
