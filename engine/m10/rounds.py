"""Review-file counter (check e).

Every review-type file on a document counts toward the cap, whatever its
verdict and whether or not its name carries a round number. One exception: a
review the project lead orders after a document has escalated at the cap does
not count when a "Cap ruling" entry in the System Hub Decision Log names its
file.
"""
from __future__ import annotations

import re
from pathlib import Path

from .common import REPO_ROOT, Finding, rel, review_dirs

ROUND_CAP = 3
ROUTE_MESSAGE = "route to project lead"
DECISION_LOG = "Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md"
_SECTION = re.compile(r"^#{2,4}[ \t]+(.*)$", re.MULTILINE)
_LOGGED_FILE = re.compile(r"`([^`\s/]+\.md)`")

# The one naming rule. A file is a review file when its name carries one of
# these words as a whole name part (split on _ - . or space): Review, Recheck,
# SpotCheck, Check or Verification. "Prereview" and "TruncationCheck" carry the
# word inside a longer one and do not count.
REVIEW_WORDS = r"(?:Review|Recheck|Spot_?Check|Check|Verification)"
_REVIEW_NAME = re.compile(rf"(?:^|[_\-. ]){REVIEW_WORDS}(?=$|[_\-. \d])", re.IGNORECASE)
_ROUND = re.compile(r"Round_?(\d+)", re.IGNORECASE)


def is_review_name(name: str) -> bool:
    return bool(_REVIEW_NAME.search(name))


def round_number(path: Path) -> int | None:
    m = _ROUND.search(path.name)
    return int(m.group(1)) if m else None


def _doc_prefix(doc: int) -> re.Pattern:
    return re.compile(r"Step_?0(?!\d)" if doc == 0 else rf"Doc_?0*{doc}(?!\d)", re.IGNORECASE)


def review_files(code: str, doc: int, root: Path = REPO_ROOT) -> list[Path]:
    """Every review-type file of the document under Build/worlds/<code>/ and its
    Review-Artifacts/ folder, in name order."""
    prefix = _doc_prefix(doc)
    found = [
        path
        for directory in review_dirs(code, root)
        for path in directory.glob("*.md")
        if prefix.search(path.name) and is_review_name(path.name)
    ]
    return sorted(found, key=lambda p: (p.name, str(p)))


def ruled_names(root: Path = REPO_ROOT) -> set[str]:
    """File names that an entry headed "Cap ruling" in the decision log names in
    backticks. Each is a review the project lead ordered under that ruling."""
    log = root / DECISION_LOG
    if not log.is_file():
        return set()
    text = log.read_text(encoding="utf-8")
    marks = list(_SECTION.finditer(text))
    names: set[str] = set()
    for i, m in enumerate(marks):
        if "cap ruling" not in m.group(1).lower():
            continue
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        names.update(_LOGGED_FILE.findall(text[m.end():end]))
    return names


def counted_review_files(code: str, doc: int, root: Path = REPO_ROOT) -> list[Path]:
    """The review files that count toward the cap: all of them, except a file a
    Cap ruling names once the cap of files is already on record before it. Files
    are taken in round-number order, then by name."""
    ruled = ruled_names(root)
    counted: list[Path] = []
    in_series_order = sorted(review_files(code, doc, root), key=lambda p: (round_number(p) is None, round_number(p) or 0, p.name))
    for path in in_series_order:
        if path.name in ruled and len(counted) >= ROUND_CAP:
            continue
        counted.append(path)
    return counted


def latest_review(files: list[Path]) -> tuple[str, list[Path]]:
    """(description, files) of the latest review: the files of the highest round
    number when any name carries one, otherwise the last file by name."""
    numbered = {p: round_number(p) for p in files if round_number(p) is not None}
    if numbered:
        top = max(numbered.values())
        return f"round {top}", [p for p in files if numbered.get(p) == top]
    return (files[-1].name, files[-1:]) if files else ("none", [])


def cap_message(label: str, count: int) -> str:
    return f"{label} has {count} review files; the cap is {ROUND_CAP}"


def clearance_message(label: str, description: str) -> str:
    return f"latest review ({description}) of {label} does not say 'Approved to proceed'"


def check_rounds(code: str, doc: int, root: Path = REPO_ROOT, *, check_new: bool = False) -> tuple[list[Finding], int]:
    files = counted_review_files(code, doc, root)
    count = len(files)
    where = rel(root / "Build" / "worlds" / code, root)
    label = f"Doc_{doc:02d}" if doc else "Step 0"
    findings: list[Finding] = []
    if count > ROUND_CAP:
        findings.append(Finding(where, "roundcount-cap", f"{cap_message(label, count)}: {', '.join(p.name for p in files)}; {ROUTE_MESSAGE}"))
    if check_new and count >= ROUND_CAP:
        findings.append(Finding(where, "roundcount-new", f"{label} already has {count} review files; a new review file would be number {count + 1}; {ROUTE_MESSAGE}"))
    return findings, count
