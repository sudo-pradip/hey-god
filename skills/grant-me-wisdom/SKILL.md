---
name: grant-me-wisdom
description: Use when the user says "hey-god-grant-me-wisdom" (or the old chant "hey-god-help-me-taking-right-decision") or is confused between technical options — which approach, which method, and especially the quick-fix-now vs right-but-longer-way dilemma. Also use when you yourself are genuinely torn between designs.
---

# Counsel — hey-god-grant-me-wisdom

For when the user (or you) is torn between paths — most often *the quick fix now vs the right-but-longer way*. Doctrine and rule vocabulary: `../doctrine/SKILL.md`, `../doctrine/rules.md`.

The default you must displace: presenting a balanced menu and letting the asker keep their confusion, or agreeing with whichever option their message leaned toward. Counsel means carrying the decision to a pick.

Procedure:

1. **State the decision in one sentence.** If you can't, the confusion is upstream — name what's actually unresolved first (that may be the real answer).
2. **List the real options, always including "do nothing."** Collapse fake variants; two or three real options is normal.
3. **For each option: the trade-off it makes (Iron Law 3), the rules that bear on it (by ID), and what it costs at the second and tenth change** — not just today. The quick fix is honestly cheaper *today*; say so. The question is who pays later, and how much.
4. **ONE recommendation with its named cost.** Never a menu without a pick. State the condition under which the other option would be right instead — that's what makes the pick trustworthy rather than opinionated.
5. **If the righteous path truly doesn't fit reality right now** (deadline, prod fire, hard constraint): say so plainly and route to `forgive-me-for-my-sins` — take the shortcut *with the debt written down* rather than pretending it's clean.

## Resolving dilemmas — the deciding questions

Every line of code is a walk we chose; each decision shapes the future, and there will always be tension between *what is needed now* and *what god intended*. Rules alone don't resolve these — "one thing well" can argue both sides of the same dilemma. What decides is asking the questions that make the rule computable. Run them in order; usually one of the first three settles it.

1. **The name test (N1).** Merge the two things and name the result honestly. If the honest name needs an "and" (`lakehouse_query_and_refresh_metadata`), it's two things — split. If one honest name still covers both (`lakehouse_catalog` covering browse+describe), they may be one thing.
2. **The actor test (S1).** Do they change for the same reason, at the request of the same stakeholder/workflow? Different change-drivers → separate units, whatever the surface similarity.
3. **The separability test (ISP/CRP).** Will any caller ever want one without the other? If yes, merging taxes every such caller forever — split. If they are always used together in the same breath, splitting is ceremony.
4. **The depth test (D1).** Which option gives the simpler *interface* relative to what it hides? A split that produces two shallow fragments sharing state is worse than one deep unit; a merge that bloats the signature with mode flags (D7) is worse than two clean ones.
5. **The 10th-change test.** Play each option forward: when the 5th sibling feature arrives, which structure absorbs it with a local change?
6. **Look for the dissolving third option.** The best resolution often makes the dilemma vanish: maybe the new thing shouldn't be *visible* at all — pulled below the interface (D8), done automatically when needed (E1). Always ask "is there a design where nobody has to choose?" before choosing.
7. **Tie-breaker: reversibility.** Still genuinely equal? Pick the option that is cheaper to undo, note it (A5-lightweight: a comment), and move — an even dilemma isn't worth a day of debate, because you've kept the exit.

Worked example — `lakehouse_query` exists; `refresh_metadata` is needed. Add it in, or dedicated tool? Name test: `lakehouse_query_and_refresh` needs an "and" → two things. Actor test: querying serves readers; metadata refresh is maintenance — different drivers. Separability: callers query constantly, refresh rarely → merging taxes every query call. Three of three say **dedicated tool**. But question 6 first: if refresh only exists because queries fail on stale metadata, the god-intended design may be that `lakehouse_query` detects staleness and refreshes *internally* — no new surface at all, dilemma dissolved. That check — "should this even be a choice?" — comes before the choice.

Output shape:

```
The decision: <one sentence>
Options:
  A. <option> — buys <X>, costs <Y>; at the 10th change: <Z>  [rules: ...]
  B. ...
Deciding questions: <name test: ... | actor test: ... | separability: ...>
Third option check: <does a design exist where nobody has to choose?>
Counsel: <the pick> — accepting <its cost>. Choose <other> instead if <condition>.
```
