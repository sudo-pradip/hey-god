---
name: forgive-me-for-my-sins
description: Use when the user says "hey-god-forgive-me-for-my-sins" or the goal must be met NOW and the righteous path does not fit — deadline, prod fire, hard constraint — so a deliberate shortcut is taken and recorded as debt. The devil's bargain - shortcuts allowed, silence forbidden.
---

# Forgiveness — the devil's bargain

Sometimes the righteous path does not fit inside reality: production is on fire, the demo is tomorrow, the dependency can't move this quarter. Pretending the shortcut is clean is how codebases rot *silently* — this mode makes the shortcut loud. The devil grants the wish, and the debt is written down. The whole bargain: **any sin may be committed knowingly, none silently.**

Doctrine: `../doctrine/SKILL.md`; rule IDs: `../doctrine/rules.md`.

- **Goal first.** Meet the stated goal by the shortest workable path: duplicate the code, hardcode the value, add the fourth branch, skip the seam. Do not gold-plate the shortcut — a shortcut that takes long is the worst of both worlds.
- **Even the devil has limits.** Shortcuts are taken on *structure*, never on *safety*: no broken correctness, no swallowed errors hiding data loss, no security holes, no deleting or disabling existing passing tests, no lying names or comments — a shortcut mislabeled as clean design is the one unforgivable sin, because it can never be found and repaid. If the goal can't be met without crossing these, say so plainly; that wish is not granted.
- **Every sin goes in the ledger.** Maintain `SINS.md` at the repo root (create on first sin; if the repo has an existing debt register, use that). One entry per sin, written at the moment of sinning — not after, when memory has already forgiven itself:

```
## SIN-<n> — <date> — <short name>
Committed: <what shortcut, where — file/lines>
Instead of: <the righteous path, one line, rule ID>
Because: <the real constraint that forced it>
Interest: <how this gets worse — what each future change will pay>
Repay when: <concrete trigger — "next change touching X", "after v2 ships">
```

- **Tell the user the price at grant time.** End the response with the ledger entry just written, so the debt is agreed, not discovered.
- **The debt comes due.** `purify-me` reads `SINS.md` first and repays fired debts before hunting new smells; repaid entries move to `## Repaid` with the date — the history of forgiveness is kept, like ADRs, so the same debt is not re-argued.
