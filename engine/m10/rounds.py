"""Review-round counter (check e)."""
from __future__ import annotations

import re
from pathlib import Path

from .common import REPO_ROOT, Finding, rel, review_dirs

ROUND_CAP = 3
ROUTE_MESSAGE = "route to project lead"


def _patterns(doc: int) -> list[re.Pattern]:
    prefix = r"Step_?0(?!\d)" if doc == 0 else rf"Doc_?0*{doc}(?!\d)"
    return [
        re.compile(rf"{prefix}_(?:[A-Za-z]+_)*?(?:Review|SpotCheck|Recheck)_?Round_?(\d+)", re.IGNORECASE),
        re.compile(rf"{prefix}_Round_?(\d+)_Review", re.IGNORECASE),
    ]


def review_files(code: str, doc: int, root: Path = REPO_ROOT) -> dict[int, list[Path]]:
    patterns = _patterns(doc)
    found: dict[int, list[Path]] = {}
    for directory in review_dirs(code, root):
        for path in sorted(directory.glob("*.md")):
            for pattern in patterns:
                m = pattern.search(path.name)
                if m:
                    found.setdefault(int(m.group(1)), []).append(path)
                    break
    return found


def check_rounds(code: str, doc: int, root: Path = REPO_ROOT, *, check_new: bool = False, new_round: int | None = None) -> tuple[list[Finding], int]:
    found = review_files(code, doc, root)
    count = len(found)
    where = rel(root / "Build" / "worlds" / code, root)
    label = f"Doc_{doc:02d}" if doc else "Step 0"
    findings: list[Finding] = []
    if count > ROUND_CAP:
        rounds = ", ".join(str(n) for n in sorted(found))
        findings.append(Finding(where, "roundcount-cap", f"{label} has {count} review rounds ({rounds}); the cap is {ROUND_CAP}; {ROUTE_MESSAGE}"))
    if check_new:
        if new_round is not None and new_round > ROUND_CAP:
            findings.append(Finding(where, "roundcount-new", f"round {new_round} of {label} would pass the cap of {ROUND_CAP}; {ROUTE_MESSAGE}"))
        elif count >= ROUND_CAP and (new_round is None or new_round not in found):
            findings.append(Finding(where, "roundcount-new", f"{label} already has {count} review rounds; a new round file would be round {count + 1}; {ROUTE_MESSAGE}"))
    return findings, count
