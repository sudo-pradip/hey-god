---
name: purify-me
description: Use when the user says "hey-god-purify-me" (or the old chant "hey-god-remove-my-sins") or asks to refactor, restructure, clean up, or fix bugs in shared code. Behavior-preserving change only; repays SINS.md debts first.
---

# Absolution — hey-god-purify-me

You know the Fowler catalog, the smells, and the moves — no recitation here. The defaults to displace: restructuring without a pinned baseline, big steps that can't be reverted, debugging forward through a broken refactor, and "improving" things nobody asked about. Refactoring means behavior-preserving; behavior + structure never change in the same step (Iron Law 4, ../doctrine/SKILL.md; rule IDs: ../doctrine/rules.md).

1. **Read the sins ledger first.** If `SINS.md` exists (debts recorded by forgive-me-for-my-sins), sins whose repay-when trigger has fired are the top-priority targets — shortcuts taken knowingly with the righteous path already written down. Repay those before hunting new smells; move repaid entries to `## Repaid` with the date.

2. **Decide whether to refactor at all.** Yes when: understanding requires it (bake the understanding in — rename, extract), a pending change is hard because of structure (*preparatory* refactoring: make the change easy, then make the easy change — highest ROI there is), or the third wince at the same spot (rule of three). **No** when: stable-and-untouched behind a clean interface (ugly can stay ugly); behavior unpinnable → contain instead, wrap and build clean outside (T1); release freeze imminent; module scheduled for deletion; published external API (needs deprecation, not a rename — B5); flexibility for imagined futures (D3). Rewrite-from-scratch is the most dangerous decision in software — only for small, well-tested units where it's *demonstrably* cheaper.

3. **Pin the baseline** (T1): run existing tests from green; no tests → characterization tests asserting what the code *actually does now*, including behavior that looks wrong (flag looks-wrong to the user as a question — someone may depend on it), through the stable boundary so the tests survive the restructuring they protect (T2).

4. **Small steps, always green.** Steps so small they feel silly; test after each; checkpoint at every green. **Red step → revert to green and take a smaller step — never debug forward.** Use the named catalog moves with their mechanics, not freehand restructuring. Wide-impact changes go expand → migrate → contract, each migration a green step; no long-lived refactor branches.

5. **Prioritize by compounding, not visibility:** (1) whatever blocks the actual task, (2) renames and dead-code deletion (cheap, safe, high yield), (3) knowledge duplication (D5), (4) structural moves. Fully finish one improvement over half-doing five.

6. **Bug fixes:** failing test that reproduces it FIRST (T3) — can't reproduce means you don't understand it yet. Fix at the root: one guard in the shared function beats N guards in N callers — and the lazy-looking call-site patch is usually a second bug. Fix minimally; structure improvements are a separate step after green. Then check the bug's siblings — bugs cluster (T4): same mistake in copy-pasted logic, same boundary unchecked elsewhere.

7. **Diff hygiene gate:** the diff reads as ONE story. Behavior fix + rename + restructure = three stories = three commits. Improvements beyond the task's footprint: **propose, don't perform.**

**Report:** what changed structurally and what behavior stayed pinned (and which tests prove it); root cause if a bug; sins repaid from the ledger; smells found but deliberately left, each with its reason, as proposals.
