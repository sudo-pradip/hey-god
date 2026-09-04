
<p align="center">
  <img src="assets/god-eye.gif" alt="hey-god" width="200" />
</p>

<p align="center">
  <strong><font size="6">Heygod</font></strong>
</p>
<p align="center">
  <em>Software that can change without fighting you.</em>
</p>



## Table of Contents

- [The problem](#the-problem)
- [The old excuse is dead](#the-old-excuse-is-dead)
- [The invocations](#the-invocations)
- [What's actually inside (and what deliberately isn't)](#whats-actually-inside-and-what-deliberately-isnt)
- [Install](#install)
- [Repo layout](#repo-layout)



## The problem

Day by day, people gain access to the finest AI models. Companies have access to increasingly similar capabilities, yet some struggle while others build better software as time goes on. The difference is no longer the model. It’s how you use it.

Agents are smart now. They've read every book we could feed them like SOLID, Clean Architecture, the Fowler catalog. There is no knowledge gap. So there's no point teaching an agent *how to cook*, what it needs is someone insisting on **what good taste is**, direction, reasoning, and rules it holds itself to when nobody's watching.

Meanwhile, the layers have shifted. Programming languages are becoming the new low-level layer, what assembly was to C, code is becoming to specs. Spec-driven development is how **humans express software now**. That doesn't mean nobody cares how the low-level layer is generated, it means we've **abstracted that layer to the agent, and the agent must care on our behalf**. The human owns the spec; the agent owns the code; and the moment that contract breaks, you can see it:

- **The moment a human has to open the code**, the agent went wrong somewhere.
- **The moment each new feature takes longer than the last**, the code is shaping wrong.
- **The moment the result stops matching the spec**, the structure is fighting the intent.
- **The moment a small change burns hundreds of tokens**, you are paying interest on invisible debt.

The gap is not agent capability and it's not human skill. **The gap is discipline.**

## The old excuse is dead

"Clean code is a long-term investment, it pays off later." That framing no longer holds, for two reasons.

First, **there is no "later" anymore.** Decisions change left and right, pivots that took months now happen in days. Structure is not a savings account; it's the *steering system*. Clean boundaries are what let a human change their mind on Tuesday and ship it Wednesday. The goal is simple: **make every change as fast as possible, adapt to anything, and let the human never worry about internals.**

Second, **the up-front cost argument is gone.** With a human, discipline cost weeks. With an agent, the disciplined version and the sloppy version take nearly the same time to build, the agent types both at the same speed. You're no longer paying extra for structure; you're only choosing whether the *next* change is cheap or expensive.

## The invocations

hey-god is a plugin: a core doctrine plus one skill per invocation.

| Say | You get |
|---|---|
| `hey-god am i sinning?` | Verdict + sins by rule ID + penance for each |
| `hey-god grant me wisdom` | Quick-fix vs right-way, priced at the 10th change, ONE pick |
| `hey-god build a new world` | New-project sequence: qualities → style → seams → ADRs → first slice |
| `hey-god bring it to life` | The insertion-point ladder; every changed line traces to the feature |
| `hey-god purify me` | Safe refactoring: behavior pinned first, small green steps, ledger debts repaid |
| `hey-god forgive me for my sins` | The devil's bargain: shortcut granted NOW, debt written in `SINS.md` |
| `hey-god give me third eye` | A calm outsider re-measures the problem the conversation inflated |
| `hey-god bring us on same page` | Blind-spot questions + assumptions surfaced BEFORE building, kills the 2-3 wasted iterations |
| `hey-god show me the pain` | Your system as a story, components as characters, pain named where it lives |
| `hey-god god mode` | Autonomous run-to-merge on the righteous path, aligns once, then no more questions until the PR is in main |
| `hey-god devil mode` | ⚠ Berserk run-to-merge, shortcuts unlimited, every sin auto-billed to `SINS.md`, gates convinced but never broken |

No invocation needed for normal work, the doctrine applies to any coding task with lasting structure.

## What's actually inside (and what deliberately isn't)

- **No lessons.** The agent already knows the rules; re-teaching them is dead weight. Rules are cited by ID (D3, LSP, T1) and the rulebook stores only each rule's *boundary*, the condition where it flips, because a knowledgeable agent's failure mode is dogma, not ignorance.
- **Counter-rationalization armor.** The excuses agents actually make under pressure ("abstraction will save time later", "no time for the test first"), pre-refuted.
- **Permission to do less.** Scope discipline, "propose don't perform", the right to push back on the spec, overriding the agent's trained urge to over-help.
- **The sins ledger (`SINS.md`).** Shortcuts are allowed; silence is not. Every deliberate shortcut is recorded with its interest rate and repay-when trigger. Absolution collects.
- **Third Eye.** Long conversations amplify problems, the model builds a story, absorbs your bias, inherits stale conclusions. Facts kept, story dropped, problem re-measured at true size.
- **Same-page alignment.** Wrong solutions start as silent assumptions, the human's unstated context, the agent's auto-filled gaps. One round of blind-spot questions (each with a recommended answer) plus a story playback, before any effort is spent.
- **Speaks human.** All modes answer in plain words and short stories by default, components as real things with jobs, consequences as what you'll feel, because humans reply better to stories, and better replies mean fewer iterations. Technical on request.

## Install

### Claude Code

```
/plugin marketplace add sudo-pradip/hey-god
/plugin install hey-god@hey-god
```

Two separate prompts. Skills appear namespaced (`hey-god:am-i-sinning`, `hey-god:give-me-third-eye`, …); the doctrine triggers on any structural coding work with no invocation needed. Also works from the Claude desktop app's Code tab, and in Cowork via the same plugin.

### Codex

```
codex plugin marketplace add sudo-pradip/hey-god
codex plugin add hey-god@hey-god
```

Run `codex` and start a new thread. The VS Code Codex extension reads `AGENTS.md`, which this repo ships, so it also works from a checkout with no setup (`~/.codex/AGENTS.md` makes it global).

### GitHub Copilot CLI

```
copilot plugin marketplace add sudo-pradip/hey-god
copilot plugin install hey-god@hey-god
```

In an interactive Copilot CLI session, use the slash equivalents:

```
/plugin marketplace add sudo-pradip/hey-god
/plugin install hey-god@hey-god
```

Copilot CLI fallback (instruction-only mode): it reads `AGENTS.md` and `.github/copilot-instructions.md` in a project, or copy the rules into `~/.copilot/copilot-instructions.md` to run hey-god in every project.

### Gemini CLI

```
gemini extensions install https://github.com/sudo-pradip/hey-god
```

Loads the ruleset as always-on context every session. The skills ship too, activated when a task needs them.

### Antigravity CLI

```
agy plugin install https://github.com/sudo-pradip/hey-god
```

Reuses the `gemini-extension.json`. Until the Gemini → Antigravity migration completes, `gemini extensions install` still works too. To run it as an always-on rule instead, drop the ruleset into `.agents/rules/`.

### Pi agent harness

```
pi install git:github.com/sudo-pradip/hey-god
```

### Devin CLI

```
devin plugins install sudo-pradip/hey-god
```

Skills are available as `hey-god:am-i-sinning`, `hey-god:grant-me-wisdom`, and so on.

### Grok Build

```
grok plugin install sudo-pradip/hey-god --trust
```

Enable the plugin: `/plugins` → Space on `hey-god`, or in `~/.grok/config.toml`:

```toml
[plugins]
enabled = ["hey-god"]
```

`AGENTS.md` still works instruction-only from a checkout without the plugin.

### Hermes Agent

```
hermes plugins install sudo-pradip/hey-god --enable
```

Restart Hermes after installing.

### OpenCode

Add to `opencode.json`:

```json
{ "plugin": ["./.opencode/plugins/hey-god.mjs"] }
```

OpenCode also auto-loads this repo's `AGENTS.md`, so the rules hold even without the plugin.

### Qoder

Qoder auto-loads `AGENTS.md` from the repo root as always-on context, so running hey-god from a checkout works with zero setup. For per-project rules, copy `.qoder/rules/hey-god.md` into your project's `.qoder/rules/`.

### Cursor

```
mkdir -p .cursor/rules && curl -o .cursor/rules/hey-god.mdc https://raw.githubusercontent.com/sudo-pradip/hey-god/main/.cursor/rules/hey-god.mdc
```

### Windsurf

Copy `.windsurf/rules/hey-god.md` into your project's `.windsurf/rules/`.

### Cline

Copy `.clinerules/hey-god.md` into your project's `.clinerules/`.

### Kiro

Copy `.kiro/steering/hey-god.md` to `~/.kiro/steering/` (global) or `.kiro/steering/` in your project.

### Aider / CodeWhale / Amp / Jules / Junie

These all read `AGENTS.md` from the project root, which this repo ships, zero setup from a checkout.

### Swival

```
swival skills add --global https://github.com/sudo-pradip/hey-god
swival skills add hey-god
```

Also reads `AGENTS.md` from the project root and `~/.config/swival/AGENTS.md` globally.

### Any other agent (instruction-file fallback)

Place `AGENTS.md` in your project root, or append `CLAUDE.md.example` to your `CLAUDE.md`. Any agent that reads project instructions gets the full doctrine, the single-file mirrors are self-contained.

### Skill files only (no plugin)

Copy the `skills/*` folders into `~/.claude/skills/`. Note: the sub-skills reference `../doctrine/` by relative path, so copy the whole set together.

### Uninstall

```
/plugin remove hey-god                              # Claude Code
codex plugin remove hey-god                          # Codex
copilot plugin remove hey-god                        # Copilot CLI
devin plugins remove hey-god                         # Devin
grok plugin uninstall hey-god                        # Grok Build
pi uninstall hey-god                                 # Pi
```

### Updating

`/plugin marketplace update hey-god` then reinstall, or re-run the curl for file-based installs. All mirrors are generated from `AGENTS.md`; `scripts/check_rule_copies.py` in CI guarantees they never drift, so any single file you grab is always current.

## Repo layout

```
.agents/rules/              Antigravity CLI always-on rule
.claude-plugin/             marketplace.json + plugin.json (the two-command Claude install)
.codex-plugin/              plugin.json (the two-command Codex install)
.devin-plugin/              plugin.json (Devin CLI plugin install)
.github/                    copilot-instructions.md (GitHub Copilot)
.grok-plugin/               plugin.json (Grok Build plugin install)
.kiro/steering/             hey-god.md (Kiro steering rule)
.qoder-plugin/              plugin.json (Qoder plugin install)
.qoder/rules/               hey-god.md (Qoder per-project rules)
skills/
  doctrine/                 core: laws, workflow, scope discipline, rules.md (IDs + boundaries)
  am-i-sinning/          grant-me-wisdom/   build-a-new-world/   bring-it-to-life/
  purify-me/           forgive-me-for-my-sins/              give-me-third-eye/
  bring-us-on-same-page/    show-me-the-pain/    god-mode/    devil-mode/
AGENTS.md                   canonical single-file mirror (Codex, Aider, Amp, Jules, CodeWhale)
gemini-extension.json       Gemini CLI / Antigravity CLI extension manifest
opencode.json               OpenCode plugin config
plugin.json                 Pi agent harness / generic plugin marker
plugin.yaml                 Hermes Agent manifest
.cursor/rules/  .clinerules/  .windsurf/rules/  CLAUDE.md.example
scripts/check_rule_copies.py   CI check: mirrors never drift from AGENTS.md
```

To change the doctrine: edit the skills, condense into `AGENTS.md`, re-copy the mirrors, run `python3 scripts/check_rule_copies.py`.

**Human owns the spec. Agent owns the code. hey-god keeps the contract.**

*The sinner is always welcome.*
