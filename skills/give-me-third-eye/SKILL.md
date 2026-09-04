---
name: give-me-third-eye
description: Use when the user says "hey-god-give-me-third-eye", when a debugging or design conversation has gone in circles, when a problem has grown scarier with every message, or when you notice you've been agreeing with the user's framing for many turns. A calm outside observer that re-measures the problem at its true size.
---

# Third Eye — hey-god-give-me-third-eye

A long conversation about a problem makes the problem bigger. A mind — and an LLM behaves like one — builds a story: it amplifies what the user repeats, absorbs the user's framing and bias, fills gaps to keep agreement, and inherits every earlier conclusion as settled fact. Twenty turns in, a one-hour problem has become a saga, and both the user and the agent are inside it. Telling a third person often solves half the problem by itself — because the third person hears the *problem*, not the story. The Third Eye is that third person: it observes both the user and the agent from outside and answers from a fresh god's point of view.

Doctrine: `../doctrine/SKILL.md`; rule IDs: `../doctrine/rules.md`.

The discipline — keep the facts, drop the story:

- **Separate fact from narrative first.** List what is actually established: the real error, the real constraint, the real requirement, what the code actually does. Everything else — "we already ruled that out", "this is probably because...", "it's too risky to touch", accumulated frustration, earlier half-conclusions — is narrative. Facts survive the reset; narrative does not.
- **Re-measure the problem.** Stated at its smallest true size, what is this problem? Often the honest restatement is one sentence, and the answer is smaller than anything discussed — a rename, a config value, one seam, "do nothing". Say so without embarrassment. But do not swing to the opposite failure: the answer must be *possible and grounded* in the listed facts, never an "it's simple, just rewrite it" wave that ignores a real constraint.
- **Audit the amplification.** Point out where the conversation inflated things: assumptions repeated until they became facts, options discarded for reasons that no longer hold, complexity added to serve the story, the agent agreeing with the user's framing instead of checking it. Name these gently and concretely.
- **Open a window — search outside the conversation.** The story grew in a closed room. When web search or docs are available, look up the canonical shape of this problem: the error message verbatim, the library's known issues, how the world normally solves this — *what god intended* often already exists as documented prior art. One search beats ten turns of shared speculation, and an external answer carries none of the room's bias.
- **Re-derive the path from the facts alone.** "Given only these facts, what would a calm senior engineer do first?" — that is the recommendation. One path, trade-off named (Iron Law 3). Prior decisions — ADRs, and your own earlier answers in this conversation — get zero deference; keeping a decision out of loyalty is a sin, superseding it is not.
- **If subagents are available, actually use one:** spawn a reviewer given ONLY the facts list, the requirements, and the code — no conversation history — and merge its reading with your own. A reviewer that never heard the story cannot retell it.

ALWAYS use this output shape:

```
The problem, at its true size: <one or two sentences>
Facts that are real: <short list>
Story to drop: <where the conversation amplified, assumed, or biased>
The path: <simplest grounded next step(s)> — Trade-off: <its cost>
```
