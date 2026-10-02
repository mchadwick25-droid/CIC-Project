"""Reading a review round's verdict wording."""
from __future__ import annotations

import re
from pathlib import Path

from .common import read_text

_VERDICT_LABEL = r"(?:(?:document\s+|recommended\s+)?(?:verdict|disposition|status)|recommendation)\s*:\s*(?:cleared review\s*[-–—]+\s*)?"
POSITIVE_VERDICT = re.compile(rf"^(?:{_VERDICT_LABEL})?approved to proceed\b", re.IGNORECASE)
NEGATIVE_VERDICT = re.compile(rf"^(?:{_VERDICT_LABEL})?not\b[^.\n]{{0,60}}?approved to proceed", re.IGNORECASE)
CLEARED_VERDICT = re.compile(r"^(?:document\s+|recommended\s+)?(?:verdict|disposition|status)\s*:.*\bcleared\b", re.IGNORECASE)
NOT_CLEARED = re.compile(r"\bnot\s+cleared\b", re.IGNORECASE)

APPROVED = "Approved to proceed"
NOT_APPROVED = "NOT APPROVED"
CLEARED = "CLEARED"
UNRECOGNISED = "UNRECOGNISED"


def verdict_lines(text: str) -> list[str]:
    return [re.sub(r"[*_`]", "", ln).lstrip("> -#\t ").strip() for ln in text.splitlines()]


def has_clearance(review_paths: list[Path]) -> bool:
    """True when a verdict line reads 'Approved to proceed' (alone or after a
    Verdict, Disposition or Status label) and no verdict line in any of the
    round's files reads 'Not approved to proceed'."""
    lines = [ln for p in review_paths for ln in verdict_lines(read_text(p))]
    if any(NEGATIVE_VERDICT.match(ln) for ln in lines):
        return False
    return any(POSITIVE_VERDICT.match(ln) for ln in lines)


def verdict_word(review_paths: list[Path]) -> str:
    """The wording a round's verdict uses: 'Approved to proceed', 'CLEARED'
    (the older wording), 'NOT APPROVED', or 'UNRECOGNISED'."""
    lines = [ln for p in review_paths for ln in verdict_lines(read_text(p))]
    if any(NEGATIVE_VERDICT.match(ln) for ln in lines):
        return NOT_APPROVED
    if any(POSITIVE_VERDICT.match(ln) for ln in lines):
        return APPROVED
    if any(CLEARED_VERDICT.match(ln) and not NOT_CLEARED.search(ln) for ln in lines):
        return CLEARED
    return UNRECOGNISED
