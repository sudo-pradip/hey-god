---
name: build-a-new-world
description: Use when the user says "hey-god-build-a-new-world" (or the old chant "hey-god-help-to-build-new-world") or is starting a new project, service, or major component from (near-)empty — project setup, architecture design, greenfield builds.
---

# Genesis — hey-god-build-a-new-world

You already know the architecture styles, their trade-offs, and hexagonal layering — no lesson here. What you don't do by default is *sequence the decisions and stop yourself from deciding too much*. The failure to displace: choosing too much, too early, from fashion — scaffolding a cathedral when the requirement was a chapel. Work the checklist; each step has a hard completion criterion.

1. **Rank the driving qualities.** ≤3, ordered, stated to the user (A6, ../doctrine/rules.md) — proposed by you if they have no opinion, never silently assumed. Collect hard constraints as decisions-already-made. *Done when: the ranking and constraints are written down.*

2. **Choose the style by the ranking, not by habit.** Default is modular monolith, domain-partitioned (A3, A4); deviate only where a ranked quality demands it, and name what the deviation costs (A1). Find the quantum lines — where parts need different -ilities or deploy cadence — and put hard boundaries there only. *Done when: the style and each deviation has a one-line cost attached.*

3. **Sort every pending decision into two piles.** Decide-now (expensive to reverse): platform, data ownership, sync-vs-async between quanta, public contract shapes, tenancy. Defer-behind-a-seam (A2): DB vendor, framework specifics, caching, broker, providers. For each deferral the deliverable is the *interface plus the simplest working implementation* (in-memory, flat file) — not a promise to build the fancy one later. *Done when: no pending decision is in neither pile.*

4. **Skeleton with the Dependency Rule built in** (B1): per domain module, core / ports / adapters (use the ecosystem's native names — the shape matters, not the words). Composition root is the one dirty place. Scaffold only what the first 1–2 use cases need — an empty folder tree for imagined features is D3 in filesystem form. *Done when: every planned file traces to the first slice.*

5. **Design it twice.** Sketch one meaningfully different alternative (different style, cut, or quantum lines), compare against the ranking, pick, record. Ten minutes here routinely saves a week. *Done when: the rejected alternative and the reason are in the ADR.*

6. **ADRs for the style and each decide-now item** (A5) — Consequences must contain at least one genuine cost; an ADR with only upsides is marketing. `docs/adr/NNNN-slug.md`.

7. **Make boundaries self-enforcing on day one.** Rules in a README decay: add the ecosystem's dependency-direction check (import-linter, ArchUnit, dependency-cruiser, deptrac…) asserting no cycles (B2) and core-imports-no-adapters (B1), wired into CI with tests and lint. A performance budget only if it was a ranked quality. *Done when: the check runs in CI and you've seen it pass.*

8. **First vertical slice, test-first, through the use-case boundary** (T2) — one thin end-to-end use case before broadening; the first component cut is always somewhat wrong and the slice finds it cheap.

**Report:** chosen style + accepted trade-off; decide-now decisions; deferrals each with its seam; where the ADRs live.
