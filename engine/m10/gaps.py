"""Open-item ledger completeness (check g)."""
from __future__ import annotations

import re
from pathlib import Path

from .common import REPO_ROOT, Finding, read_text, rel, review_dirs, world_dir
from .matching import matched, split_chunks

LEDGER_NAME = "Open_Gaps_Tracking.md"
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_OPEN_HEADING = re.compile(r"\b(open\s+(?:items?|questions?|gaps?)|unresolved|carried\s+forward|known\s+gaps?)\b", re.IGNORECASE)
_INLINE = re.compile(r"^\s*(?:[-*]\s*)?\**\s*(?:open\s+item|open\s+question|open\s+gap|gap)\b\**\s*(?:\d+\s*)?[:—–-]\s*(\S.*)$", re.IGNORECASE)
_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_BARE_REF = re.compile(r"\b(?:gap|entry|item|open item)\s*#?\s*\d+\b|(?<!\w)#\d+\b", re.IGNORECASE)
_LIST_MARK = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+")
_NON_ITEM = re.compile(r"^\s*(?:none\b|no open|nothing\b|n/a\b|\|?\s*[-:| ]+\|?\s*$)", re.IGNORECASE)


def phase_documents(code: str, root: Path = REPO_ROOT) -> list[Path]:
    base = world_dir(code, root)
    if not base.is_dir():
        return []
    paths: dict[Path, None] = {}
    for directory in review_dirs(code, root):
        for path in sorted(directory.glob("*.md")):
            if path.name == LEDGER_NAME or path.name.startswith("Open_Gaps"):
                continue
            paths[path] = None
    return list(paths)


def extract_items(text: str) -> list[tuple[int, str]]:
    items: list[tuple[int, str]] = []
    lines = text.splitlines()
    level: int | None = None
    for no, line in enumerate(lines, 1):
        h = _HEADING.match(line)
        if h:
            depth = len(h.group(1))
            if level is not None and depth <= level:
                level = None
            if _OPEN_HEADING.search(h.group(2)):
                level = depth
            continue
        s = line.strip()
        if not s or s.startswith("|") and set(s) <= set("|-: "):
            continue
        inline = _INLINE.match(line)
        if inline:
            items.append((no, inline.group(1).strip()))
        elif level is not None and (_LIST_MARK.match(line) or s.startswith("|")) and not _NON_ITEM.match(s):
            items.append((no, _LIST_MARK.sub("", s).strip("| ")))
    return items


def check_gaps(code: str, root: Path = REPO_ROOT) -> list[Finding]:
    base = world_dir(code, root)
    ledger = base / LEDGER_NAME
    where = rel(ledger, root)
    if not ledger.is_file():
        return [Finding(where, "gaps-ledger", "Open_Gaps_Tracking.md does not exist")]
    ledger_text = read_text(ledger)
    chunks = split_chunks(ledger_text)
    findings: list[Finding] = []
    for no, line in enumerate(ledger_text.splitlines(), 1):
        if _BARE_REF.search(line) and not _DATE.search(line):
            findings.append(Finding(f"{where}:{no}", "gaps-crossref", "cross-reference cites a bare number; cite the subject and the date"))
    for path in phase_documents(code, root):
        for no, item in extract_items(read_text(path)):
            if not matched(item, chunks):
                snippet = item if len(item) <= 110 else item[:107] + "..."
                findings.append(Finding(f"{rel(path, root)}:{no}", "gaps-unmatched", f"open item has no Open_Gaps_Tracking.md entry: {snippet}"))
    return findings
