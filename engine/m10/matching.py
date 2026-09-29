"""Loose subject matching between a listed item and a ledger."""
from __future__ import annotations

import re

_STOP = frozenset(
    "this that with from have been were will would should could which their there these those about into "
    "than then them they what when where while whether does doing done also only must need needs still "
    "open item items question questions gap gaps before after against between under over each every "
    "world doc build step review round".split()
)
_TOKEN = re.compile(r"[a-z0-9]{4,}")


def tokens(text: str) -> set[str]:
    text = re.sub(r"`[^`]*`", " ", text.lower())
    text = re.sub(r"[*_#>|\[\]()]", " ", text)
    return {t for t in _TOKEN.findall(text) if t not in _STOP and not t.isdigit()}


def best_overlap(item: str, chunks: list[str]) -> float:
    wanted = tokens(item)
    if not wanted:
        return 1.0
    best = 0.0
    for chunk in chunks:
        have = tokens(chunk)
        best = max(best, len(wanted & have) / len(wanted))
    return best


def matched(item: str, chunks: list[str], threshold: float = 0.6) -> bool:
    return best_overlap(item, chunks) >= threshold


def split_chunks(text: str) -> list[str]:
    """Ledger entries: each heading section, list item, table row or paragraph."""
    chunks: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            if current:
                chunks.append(" ".join(current))
                current = []
            continue
        if s.startswith("#") or re.match(r"^(?:[-*]|\d+[.)])\s", s) or s.startswith("|"):
            if current:
                chunks.append(" ".join(current))
                current = []
        current.append(s)
    if current:
        chunks.append(" ".join(current))
    return chunks
