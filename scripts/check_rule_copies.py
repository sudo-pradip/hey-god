#!/usr/bin/env python3
"""Verify all cross-agent mirrors of the hey-god doctrine are in sync with AGENTS.md.

The Cursor copy (.mdc) is allowed its own frontmatter; its body must match.
Exit 0 = in sync; exit 1 = drift (CI-friendly, like ponytail's check-rule-copies).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = (ROOT / "AGENTS.md").read_text()

COPIES = {
    # --- existing mirrors ---
    ".clinerules/hey-god.md": lambda t: t,
    ".windsurf/rules/hey-god.md": lambda t: t,
    "CLAUDE.md.example": lambda t: t,
    ".cursor/rules/hey-god.mdc": lambda t: t.split("---\n", 2)[2].lstrip("\n"),
    # --- new platform mirrors ---
    ".github/copilot-instructions.md": lambda t: t,
    ".agents/rules/hey-god.md": lambda t: t,
    ".qoder/rules/hey-god.md": lambda t: t,
    ".kiro/steering/hey-god.md": lambda t: t,
}

drift = []
for rel, body in COPIES.items():
    p = ROOT / rel
    if not p.exists():
        drift.append(f"MISSING: {rel}")
    elif body(p.read_text()).strip() != CANONICAL.strip():
        drift.append(f"OUT OF SYNC: {rel}")

if drift:
    print("hey-god rule copies drifted from AGENTS.md:")
    print("\n".join(" - " + d for d in drift))
    print("Fix: edit AGENTS.md, then re-copy (see README).")
    sys.exit(1)
print(f"All {len(COPIES)} rule copies in sync with AGENTS.md.")
