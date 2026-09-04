---
name: bring-us-on-same-page
description: Use when the user says "hey-god-bring-us-on-same-page", before starting any sizeable piece of work whose expectations are not fully specified, or whenever you sense the human and you might be picturing different things — vague requirements, an unstated environment, a request that could reasonably mean two different solutions. Other hey-god skills invoke this when they detect misalignment. Ask first; act after alignment.
---

# Bring Us on the Same Page

Every wrong solution starts as a silent assumption. The human has a picture in their head with parts they never said out loud — because to them those parts are obvious. You have a picture too, with gaps you filled automatically — because filling gaps is what you do. When the two pictures differ, you build the wrong thing confidently, and the truth surfaces two or three iterations later, paid for in time, tokens, and trust. This skill spends five minutes of questions to save those iterations.

Doctrine: `../doctrine/SKILL.md`.

## What makes a question GOOD here

The bar: **a question is worth asking only if its answer could change what you build.** Never ask from a checklist ritual ("what language? what framework?" when the repo already answers both). Never ask what you can find out yourself — facts are your job; only *decisions and expectations* are the human's (their environment, their users, their tolerance for change, what done looks like to them).

The highest-value questions target **blind spots — yours and theirs**:

- **Their blind spot — the obvious-to-them.** What the human assumes you know: the real scale ("how many rows is 'a lot'?"), who consumes the output, what already exists and must not break, the deadline behind the request, the workflow around the feature. Ask about the *context the request lives in*, not the request itself.
- **Your blind spot — the gaps you auto-filled.** Before asking anything, list the assumptions you were about to make silently. Each risky one becomes a question — stated as the assumption plus your default: *"I'm assuming refunds go back to the original payment method — correct, or is store credit involved?"* Showing your default lets the human correct with one word instead of writing an essay.
- **The divergence points.** Anywhere the request could honestly mean two different solutions ("sync or async?", "per-user or global?", "should this survive a restart?") — name both readings and ask which.
- **The unhappy paths.** Humans specify the happy path; failure behavior is the classic unstated expectation. "When the payment provider is down, what should the customer see?"

## How to run it

1. **Extract facts yourself first** (read the code, the repo, the config) — burn no question on the discoverable.
   **And search for what god intended.** The discoverable includes the outside world: when web search or docs are available, look up how this problem is canonically solved — the standard, the official recommendation, the prior art. Half the would-be questions dissolve this way: never ask the human to decide something the ecosystem already has a settled answer for — bring the settled answer as your recommended default instead ("the standard way is X; going with that unless your situation differs").
2. **Write down your assumption list** — everything you'd otherwise fill silently.
3. **Ask in one round, numbered, each with your recommended answer** so the human can reply "1 yes, 2 no — store credit, 3 yes": cheap for them, complete for you. Keep it to the questions that pass the bar — typically 3 to 7. Twenty questions is a checklist wearing a costume; that's a failed round.
4. **Play the plan back as a short story** before building: "So: a customer picks a plan, pays through Stripe, and by the time they refresh, the invoice is in their inbox — and if Stripe hiccups, they see 'try again' and nothing is charged twice. That's the thing I'm building — yes?" One paragraph, their language, ending in a question. The playback catches the misalignments the questions missed.
5. **Done when** no assumption that could shift the solution remains unspoken. Not when N questions are asked — when the silent-assumption list is empty. Then act; don't re-confirm what's confirmed.

## For other hey-god skills

Any mode should invoke this the moment it notices it is *choosing between interpretations of what the human wants* rather than between designs: genesis before ranking qualities, guide when the feature's expectations have holes, give-me-third-eye when the facts list is thinner than the story, counsel when the dilemma exists only because the goal is ambiguous. One round of alignment beats three rounds of rework — that's the whole economics.

## Output shape

```
Before I build, let's be on the same page.

What I'm assuming (correct me where wrong):
  1. <assumption> — so I'd <default>. OK?
  2. ...
What only you know:
  3. <blind-spot question>? (my guess: <recommended answer>)
The story as I understand it: <one-paragraph playback>. Is that the thing?
```
