# Rule Vocabulary — recall handles, not lessons

**Load this reference when:** citing a sin by ID, or checking a rule's *boundary* — the condition where it flips.

You already know every rule here — SOLID, YAGNI, the Dependency Rule, connascence, deep modules, the Fowler catalog. This sheet exists for two things only: **(1) a stable ID vocabulary** so verdicts are precise and greppable ("Sin: D3", "Penance per D4"), and **(2) each rule's boundary** — the non-obvious flip condition, because the failure mode of a knowledgeable agent is not ignorance but *dogmatic application*. Never explain a rule to the user or to yourself; name it, apply it, and check its boundary.

## A — Architecture

| ID | Recall | Boundary — when it flips |
|---|---|---|
| A1 | Everything is a trade-off; name the cost | Never flips. A choice with no named cost is an unexamined choice. |
| A2 | Defer details (DB, framework, UI) behind seams; decide policy first | A detail that IS a hard constraint gets promoted to a recorded decision, not left "deferrable" in name only. |
| A3 | Default modular monolith; distribute only for demonstrated need | Split only where parts need *different* operational characteristics or deploy cadence — those lines, no others. |
| A4 | Partition by domain, not technical layer; the repo screams the business | Tiny codebases where any partitioning is ceremony. |
| A5 | ADR for significant decisions: context, decision, consequences *incl. at least one real cost* | Cheap-to-reverse decisions need a code comment, not an ADR. |
| A6 | Rank ≤3 driving qualities before choosing structure | "Simplicity ×3" is a valid ranking for small projects. |

## B — Boundaries

| ID | Recall | Boundary |
|---|---|---|
| B1 | Dependency Rule: policy never names its details | The composition root is the one sanctioned dirty place. |
| B2 | No module cycles | Never flips. |
| B3 | No tunneling (sibling internals, another service's tables) | Never flips within your control; missing API on the owner = the real task. |
| B4 | Strong coupling inside a boundary only; weak across | Modules released/versioned together may share more. |
| B5 | Contracts evolve additively; never break existing callers | Zero verified consumers, or a versioned deprecation path. |
| B6 | Wrap volatile third-party APIs | Stdlib and ecosystem-canonical libraries: wrapping is shallow indirection. |

## S — SOLID

| ID | Recall | Boundary |
|---|---|---|
| S1 | SRP = one *actor* per module | "Reason to change" means a stakeholder, not any edit — don't shatter cohesion in SRP's name. |
| S2 | OCP: extend through an existing seam over editing working code | Don't invent the seam speculatively — see D3/D4 for when the seam is born. |
| S3 | LSP: substitutes honor the original's promises | Never flips. Applies to endpoints and services, not just subtypes. |
| S4 | ISP: split fat interfaces by client | Small cohesive interfaces: splitting is ceremony. |
| S5 | DIP: nothing important depends on *volatile* concretions | Stable concretions (stdlib, value objects) are fine to depend on. |

## D — Design

| ID | Recall | Boundary |
|---|---|---|
| D1 | Deep modules: simple interface, real functionality behind it | Thin adapters at true boundaries (B6, humble views) are allowed shallow. |
| D2 | Hide *decisions* (format, algorithm, protocol), not just data | Getter/setter ceremony is exposure, not hiding. |
| D3 | YAGNI: no abstraction without a second concrete use | Ports at known volatility lines (B1, B6) are bought for isolation, not reuse. |
| D4 | Seam is born at the *second* duplicated conditional, not the first | Compiler-checked exhaustive matches may stay conditionals. |
| D5 | DRY is about knowledge, not text — false duplication stays duplicated | Same *business rule* twice = unify immediately. |
| D6 | Extract when the piece gains a simpler interface and an intent name — never to hit a line count | The rule contains its balance. |
| D7 | Parameter objects at 3+; flags that *fork* become two functions | Keyword args; a bool that *configures* (case_sensitive=) is fine. |
| D8 | Pull complexity downward: defaults over mandatory config | Policy the caller owns must surface, not default. |

## N — Naming & comments

| ID | Recall | Boundary |
|---|---|---|
| N1 | Names reveal intent AND side effects | Tiny scopes keep conventional short names. |
| N1a | Grammar by kind: noun things, verb actions, predicate booleans | Codebase/ecosystem convention wins (Iron Law 1). |
| N2 | One word per concept; the domain's existing vocabulary | Never flips. |
| N3 | `Manager/Util/data/process` = design smell wearing a name | A small honest utils file is not a crisis; a growing one is. |
| N4 | Comment the why and the contract, never narration; commented-out code dies | Never flips. |
| N5 | Interface comment before body, as a design test | Internal helpers skip the ceremony. |

## E — Errors

| ID | Recall | Boundary |
|---|---|---|
| E1 | Best handling is none: define errors out of existence | Domain outcomes the caller must act on are modeled, never swallowed. |
| E2 | No null where absence is expressible | FFI/serialization edges; convert at the boundary. |
| E3 | Handle where handling is possible; context attaches at the throw site | B6 boundaries translate foreign exception zoos — that's purposeful. |
| E4 | No catch-and-continue wallpaper | Top-level supervisors that log, convert, and keep the system alive. |

## T — Tests

| ID | Recall | Boundary |
|---|---|---|
| T1 | Characterization test before changing untested code | Pure additions touching nothing shared; unpinnable legacy → wrap and build outside (sprout/wrap). |
| T2 | Test through the stable boundary, not volatile internals | Tricky pure algorithms: their interface IS stable. |
| T3 | Bug → failing test → fix, in that order | Never flips. |
| T4 | Test boundaries and error paths, not coverage numbers | Never flips. |
| T5 | Fast, independent, one concept, diagnostic failures | Integration tiers may be slower — as a separate smaller ring. |
