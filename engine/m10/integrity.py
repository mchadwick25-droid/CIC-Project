"""Record Integrity read.

  integrity  the Construction Framework's Record Integrity Principle, checked
             at freeze in four parts: every open item an earlier document
             lists has an Open_Gaps_Tracking.md entry; no superseded file or
             second live version of a document sits unmarked in the world
             folder; no Construction Notes file states a record count the
             records contradict; the deployed artifact is checked directly,
             so a fix described as applied is found there or is a finding

Three parts of the Principle cannot be checked by a script and are left out:
that a fix closes the earlier documents in the same change set, that a fix
recommendation is executed or deferred with a stated reason, and that
Construction Notes describe a defect as open only while it is. The open-items
part covers the deferred half of the second. A person reads the rest.
"""
from __future__ import annotations

import re
from pathlib import Path

from .common import REPO_ROOT, Finding, Report, emit, read_text, rel, world_dir
from .deployed import _COUNTED_TYPES, _NUM, _num, check_deployed, load_records
from .gaps import check_gaps

SUPERSEDED_MARKER_LINES = 20
_MARKER = re.compile(r"\b(?:superseded|withdrawn)\b", re.IGNORECASE)
_SUPERSEDED_NAME = re.compile(r"(?:^|[_\-. ])(?:superseded|old|prior|previous|backup|bak)(?:[_\-. ]|$)", re.IGNORECASE)
_NOT_A_DOCUMENT = re.compile(r"review|history|open_gaps|manifest|readme|transcript|(?:^|[_\-. ])(?:round\d*|log|ledger|index)(?:[_\-. ]|$)", re.IGNORECASE)
_ROLES = (
    ("Doc_NN", re.compile(r"^(Doc_?\d+)", re.IGNORECASE)),
    ("Construction Notes", re.compile(r"construction[_ ]notes", re.IGNORECASE)),
    ("Permanent Prompt", re.compile(r"permanent[_ ]prompt", re.IGNORECASE)),
    ("World Profile", re.compile(r"world[_ ]profile", re.IGNORECASE)),
    ("Capsule Core", re.compile(r"capsule[_ ]core", re.IGNORECASE)),
)


def is_marked_superseded(path: Path) -> bool:
    lines = read_text(path).splitlines()[:SUPERSEDED_MARKER_LINES]
    return any(_MARKER.search(line) for line in lines)


def world_documents(code: str, root: Path = REPO_ROOT) -> list[Path]:
    """Files outside Archive/ that are documents of the world: the world
    folder's own files and its Representative/ folder."""
    base = world_dir(code, root)
    found: list[Path] = []
    for directory in (base, base / "Representative"):
        if directory.is_dir():
            found.extend(p for p in sorted(directory.iterdir()) if p.is_file() and p.suffix in {".md", ".txt", ".docx"} and not _NOT_A_DOCUMENT.search(p.name))
    return found


def check_superseded(code: str, root: Path = REPO_ROOT) -> list[Finding]:
    findings: list[Finding] = []
    documents = world_documents(code, root)
    for path in documents:
        if _SUPERSEDED_NAME.search(path.stem) and path.suffix != ".docx" and not is_marked_superseded(path):
            findings.append(Finding(rel(path, root), "i:superseded-unmarked", f"the file name marks it as an earlier version, and it sits outside Archive/ without a 'superseded' line in its first {SUPERSEDED_MARKER_LINES} lines"))
    for role, pattern in _ROLES:
        groups: dict[str, list[Path]] = {}
        for path in documents:
            match = pattern.search(path.name)
            if match:
                key = match.group(1).lower().replace("_", "") if role == "Doc_NN" else role
                groups.setdefault(key, []).append(path)
        for key, paths in sorted(groups.items()):
            live = [p for p in paths if not (p.suffix != ".docx" and is_marked_superseded(p)) and not _SUPERSEDED_NAME.search(p.stem)]
            if len(live) > 1:
                names = ", ".join(p.name for p in live)
                findings.append(Finding(rel(live[0].parent, root), "i:two-live-versions", f"{len(live)} unmarked files stand as the {role if role != 'Doc_NN' else key}: {names}"))
    return findings


def construction_notes_files(code: str, root: Path = REPO_ROOT) -> list[Path]:
    return [p for p in world_documents(code, root) if re.search(r"construction[_ ]notes", p.name, re.IGNORECASE) and p.suffix == ".md" and not is_marked_superseded(p)]


def check_stated_counts(code: str, root: Path = REPO_ROOT) -> list[Finding]:
    """A Construction Notes file that states 'N <type> records' where the
    records hold a different number contradicts the record store."""
    records = load_records(code, root)
    findings: list[Finding] = []
    if not records:
        return findings
    for path in construction_notes_files(code, root):
        text = read_text(path)
        for record_type, noun in _COUNTED_TYPES.items():
            actual = sum(1 for r in records.values() if r.get("record_type") == record_type)
            pattern = re.compile(rf"\b({_NUM})\s+(?:checked\s+|verbatim\s+)?{noun}\s+records?\b", re.IGNORECASE)
            for match in pattern.finditer(text):
                if _num(match.group(1)) != actual:
                    findings.append(Finding(rel(path, root), "i:count-contradiction", f"states '{match.group(0)}', the records hold {actual}"))
    return findings


def check_integrity(code: str, root: Path = REPO_ROOT, *, check_stale: bool = False) -> list[Report]:
    base = world_dir(code, root)
    if not base.is_dir():
        return [Report("integrity", [Finding(rel(base, root), "i:no-world", "the world folder does not exist")])]
    open_items = Report("integrity open items", [Finding(f.path, f"i:{f.check}", f.reason) for f in check_gaps(code, root)])
    superseded = Report("integrity superseded files", check_superseded(code, root))
    counts = Report("integrity stated counts", check_stated_counts(code, root))
    counts.notes.append(f"{len(construction_notes_files(code, root))} Construction Notes file(s) read")
    applied = check_deployed(code, root, check_stale=check_stale)
    deployed = Report(
        "integrity deployed artifact",
        [Finding(f.path, f"i:deployed:{f.check}", f.reason) for f in applied.findings],
        applied.notes,
    )
    return [open_items, superseded, counts, deployed]


def add_parser(subparsers) -> None:
    p = subparsers.add_parser("integrity", help="the Record Integrity read at freeze: open items logged, no unmarked superseded files, stated counts match, the deployed artifact holds what was applied")
    p.add_argument("world_code")
    p.add_argument("--json", action="store_true", help="print one JSON document instead of lines")
    p.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root to check (default: this repository)")
    p.add_argument("--stale", action="store_true", help="also recompile the pinned package and check it against its manifest")


def run(args) -> int:
    return emit(check_integrity(args.world_code, args.root, check_stale=args.stale), as_json=args.json)
