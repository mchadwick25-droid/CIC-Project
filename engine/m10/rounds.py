"""Review-file counter (check e).

Every review-type file of the current cycle on a document counts toward the
cap, whatever its verdict and whether or not its name carries a round number.
The current cycle starts at the first round, or at the latest round whose file
carries an earned `Cycle reset` header field; every file stays on record. One
exception: a review the project lead orders after a document has escalated at
the cap does not count when a "Cap ruling" entry in the System Hub Decision Log
names its file and three counted files of the cycle already precede it.
"""
from __future__ import annotations

import re
from pathlib import Path

from .common import PLACEHOLDER, REPO_ROOT, Finding, read_text, rel, review_dirs
from .reviewfile import cycle_reset
from .verdicts import has_clearance

ROUND_CAP = 3
ROUTE_MESSAGE = "route to project lead"
LIBRARY_LOG = Path("Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md")
ACCEPTED_RULINGS = ("The three-round cap counts from significant new material",)
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


def _entry_titles(path: Path) -> set[str]:
    """Titles of the dated entries ('## <date> — <title>') of a decision log."""
    if not path.is_file():
        return set()
    return {m.group(1).strip() for m in re.finditer(r"^##\s+\d{4}-\d{2}-\d{2}\s+[—–-]+\s+(.+?)\s*$", read_text(path), re.MULTILINE)}


def ruling_titles(root: Path = REPO_ROOT) -> set[str]:
    """Titles a `Cycle reset` field may cite: the accepted rulings that exist
    in the Library decision log, and every entry title of a Build/Ministry
    decision log."""
    titles = _entry_titles(root / LIBRARY_LOG) & set(ACCEPTED_RULINGS)
    ministry = root / "Build" / "Ministry"
    if ministry.is_dir():
        for path in ministry.rglob("*.md"):
            if re.search(r"decision[-_ ]?log", path.name, re.IGNORECASE):
                titles |= _entry_titles(path)
    return titles


def rounds_of(files: list[Path]) -> dict[int, list[Path]]:
    """The files whose names carry a round number, grouped by that number."""
    found: dict[int, list[Path]] = {}
    for path in files:
        n = round_number(path)
        if n is not None:
            found.setdefault(n, []).append(path)
    return found


def _reset_problem(n: int, text: str, found: dict[int, list[Path]], root: Path) -> str | None:
    """Why a `Cycle reset` on round n is not honoured, or None when it is."""
    if PLACEHOLDER.match(text):
        return "the field is empty or a placeholder"
    if not any(title in text for title in ruling_titles(root)):
        return "the field does not cite, by its exact title, an entry of the Library decision log or a Build/Ministry decision log that exists"
    before = found.get(n - 1)
    if not before or not has_clearance(before):
        return f"round {n - 1} did not clear review ('Approved to proceed'), so nothing was changed after a clearance"
    return None


def cycle_state(files: list[Path], root: Path = REPO_ROOT) -> tuple[int, list[str]]:
    """The round the current cycle starts at, and the reasons any `Cycle reset`
    was not honoured. The cycle starts at the first round unless the latest
    round whose file carries an earned `Cycle reset` field restarts it; all
    files stay on record."""
    found = rounds_of(files)
    notes = []
    for n in sorted(found, reverse=True):
        for path in found[n]:
            text = cycle_reset(path)
            if text is None:
                continue
            problem = _reset_problem(n, text, found, root)
            if problem is None:
                return n, notes
            notes.append(f"the Cycle reset in {path.name} is not honoured: {problem}")
    return 1, notes


def cycle_start(files: list[Path], root: Path = REPO_ROOT) -> int:
    return cycle_state(files, root)[0]


def cycle_files(files: list[Path], root: Path = REPO_ROOT) -> list[Path]:
    """The review files of the current cycle: those from the cycle's first round
    on, and every file whose name carries no round number (it cannot be shown to
    come before a reset, so it counts)."""
    start = cycle_start(files, root)
    return [p for p in files if round_number(p) is None or round_number(p) >= start]


def unhonoured(files: list[Path], root: Path = REPO_ROOT) -> str:
    """The text to append to a cap finding when a reset was ignored."""
    notes = cycle_state(files, root)[1]
    return "; " + "; ".join(notes) if notes else ""


def _series_order(files: list[Path]) -> list[Path]:
    return sorted(files, key=lambda p: (round_number(p) is None, round_number(p) or 0, p.name))


def _counted(files: list[Path], root: Path) -> list[Path]:
    ruled = ruled_names(root)
    counted: list[Path] = []
    for path in _series_order(cycle_files(files, root)):
        if path.name in ruled and len(counted) >= ROUND_CAP:
            continue
        counted.append(path)
    return counted


def counted_review_files(code: str, doc: int, root: Path = REPO_ROOT) -> list[Path]:
    """The review files that count toward the cap: those of the current cycle,
    except a file a Cap ruling names once the cap of files is already counted
    before it. Files are taken in round-number order, then by name."""
    return _counted(review_files(code, doc, root), root)


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


def check_rounds(code: str, doc: int, root: Path = REPO_ROOT, *, check_new: bool = False, new_round: int | None = None) -> tuple[list[Finding], int]:
    all_files = review_files(code, doc, root)
    files = _counted(all_files, root)
    note = unhonoured(all_files, root)
    count = len(files)
    where = rel(root / "Build" / "worlds" / code, root)
    label = f"Doc_{doc:02d}" if doc else "Step 0"
    findings: list[Finding] = []
    if count > ROUND_CAP:
        findings.append(Finding(where, "roundcount-cap", f"{cap_message(label, count)}: {', '.join(p.name for p in files)}; {ROUTE_MESSAGE}{note}"))
    if check_new:
        start = cycle_start(all_files, root)
        if new_round is not None and new_round - start + 1 > ROUND_CAP:
            findings.append(Finding(where, "roundcount-new", f"round {new_round} of {label} would pass the cap of {ROUND_CAP}; {ROUTE_MESSAGE}{note}"))
        elif count >= ROUND_CAP and (new_round is None or new_round not in rounds_of(all_files)):
            findings.append(Finding(where, "roundcount-new", f"{label} already has {count} review files; a new review file would be number {count + 1}; {ROUTE_MESSAGE}{note}"))
    return findings, count
