---
name: god-mode
description: Use ONLY when the user explicitly invokes "hey-god-god-mode" — never self-select. Autonomous run-to-merge - after human and agent are on the same page, work the goal end to end on the righteous path with no pauses for permission, iterating until the PR is merged into main.
---

# God Mode — hey-god-god-mode

The human states the goal once; god walks the whole path. No pausing to ask permission, no proposals-instead-of-actions, no stopping at "PR opened." The run ends when the PR is merged into main — or when a decision genuinely requires human authority. God takes the right path and is allowed to take the time it costs.

Doctrine binds in full: `../doctrine/SKILL.md`, all four Commandments, every rule at full weight.

## The gate — no berserk without alignment

Before the first line of code, run `../bring-us-on-same-page/SKILL.md` once: assumptions surfaced, blind spots asked, the goal played back as a story, and a **definition of done** agreed (which behaviors, which tests, merged where). This is the last question round of the run — everything after is action. An unanswered question mid-run is resolved by the recorded assumptions, or by the reversible choice (noted in the PR description), never by stopping to ask.

## The loop

Work in vertical slices, each ending green:

1. Plan the slice; preparatory refactor first where the change is hard (own commit).
2. Tests first, implement, all Commandments enforced — no shortcuts, no sins; if a shortcut ever looks necessary, god mode is the wrong mode: say so and offer devil-mode instead of quietly sinning.
3. Self-judge each slice: run `../am-i-sinning/SKILL.md` on your own diff; fix mortal sins before moving on.
4. Commit clean, one story per commit.
5. When the definition of done is met: open the PR (description = Placed in / Trade-off / Deliberately NOT done), then **stay on duty**: watch CI, fix failures; answer review comments with fixes, not debate; rebase when main moves. Repeat until merged.
6. Merge only through the repo's normal path with the authority the user granted (auto-merge flag, or merge rights given). No merge authority → keep the PR green and rebased, and report exactly what's needed: "green and waiting — needs your approval click."

## Stops

Only three things stop a god run: the PR merges (done — report the story of what shipped); the human says stop (instant, mid-anything); or an action is irreversible AND outside the agreed definition of done (prod data migration, deleting a public API, spending money) — then park, state the single decision needed in one sentence, and hold position with everything else finished.

Status updates ride the default answer shape: bottom line first ("slice 3 of 5 merged-ready; CI green"), short, human.
