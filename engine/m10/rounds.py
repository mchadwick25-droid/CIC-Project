"""Review-round counter (check e)."""
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


def cycle_state(found: dict[int, list[Path]], root: Path = REPO_ROOT) -> tuple[int, list[str]]:
    """The round the current cycle starts at, and the reasons any `Cycle reset`
    was not honoured. The cycle starts at the first round unless the latest round whose
    file carries an earned `Cycle reset` field restarts it; all files stay on
    record."""
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


def cycle_start(found: dict[int, list[Path]], root: Path = REPO_ROOT) -> int:
    return cycle_state(found, root)[0]


def cycle_rounds(found: dict[int, list[Path]], root: Path = REPO_ROOT) -> dict[int, list[Path]]:
    """The review files counted against the cap."""
    start = cycle_start(found, root)
    return {n: paths for n, paths in found.items() if n >= start}


def unhonoured(found: dict[int, list[Path]], root: Path = REPO_ROOT) -> str:
    """The text to append to a cap finding when a reset was ignored."""
    notes = cycle_state(found, root)[1]
    return "; " + "; ".join(notes) if notes else ""


def check_rounds(code: str, doc: int, root: Path = REPO_ROOT, *, check_new: bool = False, new_round: int | None = None) -> tuple[list[Finding], int]:
    all_found = review_files(code, doc, root)
    found = cycle_rounds(all_found, root)
    note = unhonoured(all_found, root)
    count = len(found)
    where = rel(root / "Build" / "worlds" / code, root)
    label = f"Doc_{doc:02d}" if doc else "Step 0"
    findings: list[Finding] = []
    if count > ROUND_CAP:
        rounds = ", ".join(str(n) for n in sorted(found))
        findings.append(Finding(where, "roundcount-cap", f"{label} has {count} review rounds ({rounds}); the cap is {ROUND_CAP}; {ROUTE_MESSAGE}{note}"))
    if check_new:
        start = cycle_start(all_found, root)
        if new_round is not None and new_round - start + 1 > ROUND_CAP:
            findings.append(Finding(where, "roundcount-new", f"round {new_round} of {label} would pass the cap of {ROUND_CAP}; {ROUTE_MESSAGE}{note}"))
        elif count >= ROUND_CAP and (new_round is None or new_round not in all_found):
            findings.append(Finding(where, "roundcount-new", f"{label} already has {count} review rounds; a new round file would be round {count + 1}; {ROUTE_MESSAGE}{note}"))
    return findings, count
