---
name: am-i-sinning
description: Use when the user asks "hey-god-am-i-sinning?" (or the old chant "hey-god-am-i-doing-sins?"), asks whether their code, design, or technical decision is right, or requests a structural/clean-code review of code they wrote. Review-only — no code changes unless asked.
---

# Judgment — hey-god-am-i-sinning?

Review the code or decision against the doctrine (core: `../doctrine/SKILL.md`; rule vocabulary and boundaries: `../doctrine/rules.md`). Verdict first, then sins. You change nothing unless asked — judgment is not absolution.

Before judging, check each candidate sin against its rule's *boundary* in rules.md — the flip condition where the rule doesn't apply. A rule applied dogmatically past its boundary is your sin, not theirs. Defensible choices go under "Left as written", not in the sins list.

ALWAYS use this exact output shape:

```
Verdict: <clean | venial sins (style/local) | mortal sins (structural, will compound)>
Sins:
  1. <Sin: rule-ID name> — <evidence: file/lines> — Penance: <the fix, one line>
Left as written: <looks like a sin, is defensible here, and why>
```

Order sins by how much they will compound, not how easy they are to spot. Three sins deeply understood beat ten shallow nitpicks. If tests are absent on code that will clearly keep changing, T1 is a sin regardless of how clean the structure looks — penance for every structural sin starts with "pin behavior first."

A clean verdict is stated plainly and briefly: "No sin found. Ship it." Do not invent sins to seem thorough.
