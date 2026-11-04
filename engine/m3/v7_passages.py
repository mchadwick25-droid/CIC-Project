"""Source passages for a record's cited works, read through engine.m4.source_windows.

A passage is the window source_windows finds for each source of the record: the lines the quote's
words, the locus line numbers, or the locus division or chapter name, inside the surrounding
division, with the path of division titles. A source whose passage is not found gives no text and
an entry in `unresolved` labelled "passage not located".

A request's cap is the window's word count (source_windows.fit_step.CONTEXT_MAX_WORDS). A smaller
cap keeps the block's own lines whole and adds words either side of them alternately.
"""
from pathlib import Path

from engine.m4 import fit_step, source_windows

DIVISION_MAX_WORDS = fit_step.CONTEXT_MAX_WORDS
MAX_PASSAGES_PER_RECORD = 5
LABEL = "passage not located"


def _anchor_span(words: list[str], texts_root: Path, block: dict) -> tuple[int, int]:
    """Where the block's own lines sit in its word list: (start, length)."""
    path = str(texts_root / block["file"])
    first, last = (int(n) for n in block["lines"].split("-"))
    anchor = [w for n in range(first, last + 1) for w in source_windows._line_words(path, n)]
    probe = anchor[:5]
    for start in range(len(words) - len(probe) + 1):
        if words[start:start + len(probe)] == probe:
            return start, len(anchor)
    return 0, 0


def _cut(block: dict, texts_root: Path, cap: int) -> tuple[str, bool]:
    """The window cut to cap words, keeping the block's own lines whole and adding words either side alternately."""
    words = block["text"].split()
    if len(words) <= cap:
        return block["text"], block["trimmed"]
    start, length = _anchor_span(words, texts_root, block)
    lo, hi = start, min(start + length, len(words))
    while hi - lo < cap and (lo > 0 or hi < len(words)):
        if lo > 0:
            lo -= 1
        if hi - lo < cap and hi < len(words):
            hi += 1
    return " ".join(words[lo:hi]), True


def _reason(source: dict | None) -> str:
    if not source:
        return f"{LABEL}: no source record"
    if source.get("kind") == "unvendored":
        return f"{LABEL}: the source is not vendored"
    if source.get("kind") is None:
        return f"{LABEL}: the cited record is a project record, not a vendored text"
    return f"{LABEL}: the locus and the record's words did not resolve in the vendored text"


def resolve_record(record: dict, records: dict[str, dict], texts_root: Path, cap: int = DIVISION_MAX_WORDS) -> dict:
    """{"passages": [...], "unresolved": [{"record_id", "source_id", "reason"}]} for one record."""
    sources = record.get("sources") or []
    if not sources:
        return {"passages": [], "unresolved": [{"record_id": record["id"], "source_id": None, "reason": f"{LABEL}: the record names no source"}]}
    passages, unresolved = [], []
    for entry in sources:
        found = source_windows.context_blocks({**record, "sources": [entry]}, records, texts_root)
        if not found:
            unresolved.append({"record_id": record["id"], "source_id": entry.get("source_id"),
                               "reason": _reason(records.get(entry.get("source_id") or ""))})
            continue
        block = found[0]
        text, trimmed = _cut(block, texts_root, cap)
        passages.append({"record_id": record["id"], "source_id": block["source_id"], "locus": entry.get("locus") or "",
                         "file": block["file"], "division_path": block["division_path"], "lines": block["lines"],
                         "trimmed": trimmed, "text": text})
    for cut in passages[MAX_PASSAGES_PER_RECORD:]:
        unresolved.append({"record_id": record["id"], "source_id": cut["source_id"],
                           "reason": f"cut by the {MAX_PASSAGES_PER_RECORD}-passage cap"})
    return {"passages": passages[:MAX_PASSAGES_PER_RECORD], "unresolved": unresolved}
