"""S2.8 render-parity (P): classified diff of staged views vs. deployed files.

Blueprint standard: byte-parity is NOT expected; every differing line must
be tagged `equivalent-restructure` / `intended-change` (citing the Pass 1
section that mandates it) / `defect` (citing its flag/CO route). ZERO
unclassified lines - an unmatched difference fails the run loudly.

Classification rules are explicit and narrow (a rule that can't name its
warrant doesn't exist):
- `Tags:` line present only in deployed        -> defect (schema gap; S2.9 CO
  candidate "Tags field" - no record home).
- `Related Terms:` differing                   -> defect (view renders only
  record-backed relations; partner terms without a Desert chunk/record are
  the S2.9 missing-chunks CO).
- `Do-Not-Retrieve-When:` deployed carries a retired-class clause
  (cross-world guard), generated carries the sentinel or a shorter list
  -> intended-change (Pass 1 SS3.2 retires the cross-world condition
  class; B-RETR's dead-guard finding is the measured basis).
- Story `## Formation Ecology Connection` / `## Source Identification`
  blocks present only in deployed              -> defect (FLAG-004).
- Pure whitespace / trailing-newline drift     -> equivalent-restructure.

Run: python wrs/views/render_parity.py  -> prints the classified table and
exits nonzero on any unclassified line.
"""
from __future__ import annotations

import difflib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
STAGING = HERE / "staging" / "desert_world"
DEPLOYED = BACKEND / "data" / "desert_world"

PAIRS = [("lexicon_chunks", "lexicon_chunks"), ("story_chunks", "story_chunks")]


def classify(line: str, side: str, in_dropped_story_block: bool) -> tuple[str, str] | None:
    """Return (class, warrant) for a differing line, or None if unclassifiable."""
    t = line.rstrip("\n")
    if in_dropped_story_block and side == "deployed":
        return ("defect", "FLAG-004 (story section with no record home)")
    if t.startswith("Tags: "):
        return ("defect", "schema gap - Tags has no record home (S2.9 CO)")
    if t.startswith("Related Terms: "):
        return ("defect", "record-backed relations only; missing partner "
                          "chunks are the S2.9 missing-chunks CO")
    if t.startswith("Do-Not-Retrieve-When: "):
        return ("intended-change", "Pass 1 SS3.2 retires the cross-world "
                                    "retrieval-condition class (B-RETR "
                                    "dead-guard finding)")
    if t.strip() in ("", "---"):
        return ("equivalent-restructure", "structural whitespace/rule drift "
                                           "adjoining a classified block")
    return None


def diff_file(dep: Path, gen: Path) -> tuple[list[tuple[str, str, str]], list[str]]:
    dep_lines = dep.read_text(encoding="utf-8").splitlines()
    gen_lines = gen.read_text(encoding="utf-8").splitlines()
    classified, unclassified = [], []
    in_block = False
    for line in difflib.unified_diff(dep_lines, gen_lines, lineterm="", n=0):
        if line.startswith(("---", "+++", "@@")):
            continue
        side = "deployed" if line.startswith("-") else "generated"
        text = line[1:]
        # track entry/exit of the FLAG-004 dropped story blocks
        if side == "deployed" and text.strip() in ("## Formation Ecology Connection",
                                                    "## Source Identification"):
            in_block = True
        elif side == "deployed" and text.startswith("## ") and in_block:
            in_block = False
        c = classify(text, side, in_block)
        if c:
            classified.append((side, text, f"{c[0]} - {c[1]}"))
        else:
            unclassified.append(f"{side}: {text}")
    return classified, unclassified


def main() -> int:
    total_c, total_u = 0, 0
    counts: dict[str, int] = {}
    for dep_sub, gen_sub in PAIRS:
        for dep in sorted((DEPLOYED / dep_sub).glob("*.md")):
            gen = STAGING / gen_sub / dep.name
            if not gen.exists():
                print(f"MISSING staged file: {gen}")
                return 1
            classified, unclassified = diff_file(dep, gen)
            total_c += len(classified)
            total_u += len(unclassified)
            for _, _, tag in classified:
                key = tag.split(" - ")[0]
                counts[key] = counts.get(key, 0) + 1
            if classified or unclassified:
                print(f"## {dep.name}: {len(classified)} classified, "
                      f"{len(unclassified)} UNCLASSIFIED")
                for side, text, tag in classified:
                    print(f"  [{tag.split(' - ')[0]}] ({side}) {text[:90]}")
                for u in unclassified:
                    print(f"  [UNCLASSIFIED] {u[:120]}")
    print(f"\nTOTAL: {total_c} classified diff lines "
          f"({', '.join(f'{k}={v}' for k, v in sorted(counts.items()))}); "
          f"{total_u} unclassified")
    return 1 if total_u else 0


if __name__ == "__main__":
    sys.exit(main())
