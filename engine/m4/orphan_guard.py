"""Sentences left without their referent by a removal.

`orphaned_sentences` reads the voice's own draft against what apply_net took
out of it and what it kept. A sentence is listed when it is the first kept
sentence after a removed run in the voice's text, opens with an anaphor
(a pronoun, a demonstrative, "the same", or a connective such as "but" or
"so"), and no kept sentence stands before it in its own paragraph of the
draft, so nothing left in that paragraph can be what it points back to.
The list is a report; it removes nothing.
Deterministic string operations; no model call.
"""
from __future__ import annotations

import re

from engine.m4.grounding_net import strip_tags
from engine.prose import quote_aware_sentences

_PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
_MARKER = re.compile(r"\[\[\s*(?:quote|story)\s*:[^\]]*\]\]", re.IGNORECASE)
_PRONOUN = r"(?:he|she|it|they|his|her|its|their|him|them|this|that|these|those)"
_ANAPHOR = re.compile(
    r"^[\"'“‘(]*(?:" + _PRONOUN + r"|the\s+same|such|(?:so|yet|but|then)|and\s+" + _PRONOUN + r")\b",
    re.IGNORECASE,
)
_MIN_CONTAINED = 20


def _same(sentence: str) -> str:
    return " ".join(sentence.split())


def _status(sentence: str, removed: list[str], kept: list[str]) -> str:
    if any(d and (sentence in d or (d in sentence and len(d) > _MIN_CONTAINED)) for d in removed):
        return "removed"
    if any(f and (sentence == f or sentence in f or (f in sentence and len(f) > _MIN_CONTAINED)) for f in kept):
        return "kept"
    return "unknown"


def orphaned_sentences(draft_text: str, removed: list[dict], sentences: list[dict]) -> list[str]:
    """The kept sentences, as shown (tags and quote markers off), that open
    with an anaphor right after a removed run with no kept sentence before
    them in their own draft paragraph. `removed` and `sentences` are
    apply_net's: each entry's "draft" is the sentence as the voice wrote it."""
    removed_drafts = [_same(e.get("draft") or e.get("sentence") or "") for e in removed]
    kept_drafts = [_same(e.get("draft") or e.get("sentence") or "") for e in sentences]
    drafted: list[tuple[int, str]] = []
    for index, paragraph in enumerate(p for p in _PARAGRAPH_BREAK.split(draft_text or "") if p.strip()):
        drafted += [(index, _same(s)) for s in quote_aware_sentences(paragraph)]
    status = [_status(s, removed_drafts, kept_drafts) for _p, s in drafted]
    orphaned = []
    for i, (paragraph, sentence) in enumerate(drafted):
        if status[i] != "kept" or i == 0:
            continue
        before = i - 1
        while before >= 0 and status[before] == "unknown":
            before -= 1
        if before < 0 or status[before] != "removed":
            continue
        shown = _same(strip_tags(_MARKER.sub("", sentence)))
        if not _ANAPHOR.match(shown):
            continue
        if any(drafted[k][0] == paragraph and status[k] == "kept" for k in range(i)):
            continue
        orphaned.append(shown)
    return orphaned
