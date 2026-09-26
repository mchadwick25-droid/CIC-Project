#!/usr/bin/env python3
"""Fail when a repo-relative path cited in a current Markdown file no longer resolves.

Scope: every .md that describes the tree as it is now — the canonical trees,
the reference library, standing documents, READMEs, CLAUDE.md. Dated records
(audits, decision logs, launch prompts, anything carrying a date in its name)
describe the tree as it was, and are not held to the current one. Vendored
texts, compiled packages, node_modules, git internals and Archive/ are never
scanned.

Usage:
  check_paths.py                      report every unresolved citation, exit 1 if any
  check_paths.py --baseline FILE      exit 1 only on citations NOT listed in FILE
  check_paths.py --write-baseline FILE  record the current set as the accepted baseline
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent if HERE.name == "tools" else Path.cwd()

SKIP_DIRS = (".git/", "node_modules/", "cic/texts/", "packages/", "Archive/", ".claude/",
             "Build/Ministry/Operations/Audits/", "Build/Ministry/Operations/Standing/Launch-Prompts/",
             "Build/Ministry/Operations/Markup-Queue/")
DATED = re.compile(r"(_|-)20\d\d-\d\d-\d\d|Decision[_-]Log|Change_Log|Thread_Launch|Handoff|_Tracking\.md|Task_Board|Move_Ledger")
PLACEHOLDER = re.compile(r"[<>\[\]{}*…]|\bSomeWorld\b|/code\b|/id\b|/name\b|/file\b|/locus\b|/key\b|/world\b")
TOKEN = re.compile(r"(?<![\w/.\-@:])((?:[A-Za-z0-9_.\-]+/)+[A-Za-z0-9_.\-]+)")
TRAIL = ".,;:)'\"`*_"


# Directories that exist only on some machines (git-ignored, per-session) are
# never citation roots: if they were, whether `.claude/settings.json` in a
# decision log counts as a repo path would depend on who runs the check.
LOCAL_ONLY_DIRS = {".git", "node_modules", ".claude"}


def top_level_dirs() -> set[str]:
    return {p.name for p in REPO.iterdir() if p.is_dir() and p.name not in LOCAL_ONLY_DIRS}


def in_scope(rel: str) -> bool:
    if any(rel.startswith(s) or f"/{s}" in rel for s in SKIP_DIRS):
        return False
    if rel.startswith("Build/Ministry/") and DATED.search(Path(rel).name):
        return False
    return True


def candidates(text: str, roots: set[str]):
    for m in TOKEN.finditer(text):
        tok = m.group(1).rstrip(TRAIL)
        if PLACEHOLDER.search(tok) or "**" in tok:
            continue
        if tok.split("/", 1)[0] in roots:
            yield tok


def scan() -> set[str]:
    roots = top_level_dirs()
    broken: set[str] = set()
    for p in REPO.rglob("*.md"):
        rel = p.relative_to(REPO).as_posix()
        if not in_scope(rel):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for tok in set(candidates(text, roots)):
            if not resolves(tok):
                broken.add(f"{rel}: {tok}")
    return broken


def resolves(tok: str) -> bool:
    target = REPO / tok.rstrip("/")
    if target.exists():
        return True
    # A filename wrapped across lines ("anf01_apostolic-fathers-justin-") or cited
    # by its stem ("cic/texts/anf01") resolves if exactly one entry carries that prefix.
    parent, stem = target.parent, target.name.rstrip("-_")
    if not parent.is_dir() or not stem:
        return False
    return sum(1 for p in parent.iterdir() if p.name.startswith(stem)) >= 1


def retired_present() -> list[str]:
    """Paths retired by a reorganization must stay absent — a branch that merely *adds* a
    file under one of them merges without conflict and silently resurrects the directory."""
    listing = REPO / "tools" / "retired_paths.txt"
    if not listing.exists():
        return []
    present = []
    for line in listing.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line and (REPO / line).exists():
            present.append(line)
    return present


def main(argv: list[str]) -> int:
    resurrected = retired_present()
    for r in resurrected:
        print(f"RETIRED PATH PRESENT: {r}  (see tools/retired_paths.txt — move its contents to the new home)")
    broken = scan()
    if "--write-baseline" in argv:
        out = Path(argv[argv.index("--write-baseline") + 1])
        out.write_text("\n".join(sorted(broken)) + "\n", encoding="utf-8")
        print(f"baseline written: {len(broken)} entries -> {out}", file=sys.stderr)
        return 0
    accepted: set[str] = set()
    if "--baseline" in argv:
        bl = Path(argv[argv.index("--baseline") + 1])
        if bl.exists():
            accepted = {l.strip() for l in bl.read_text(encoding="utf-8").splitlines() if l.strip()}
    new = sorted(broken - accepted)
    healed = sorted(accepted - broken)
    for line in new:
        print(line)
    if healed:
        print(f"\n{len(healed)} baseline entr{'y' if len(healed)==1 else 'ies'} now resolve — remove from the baseline:", file=sys.stderr)
        for line in healed:
            print(f"  {line}", file=sys.stderr)
    print(f"\n{len(new)} new unresolved path citation(s); {len(broken)} total; {len(accepted)} accepted in baseline; "
          f"{len(resurrected)} retired path(s) present", file=sys.stderr)
    return 1 if (new or resurrected) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
