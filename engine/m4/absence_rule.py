"""A sentence that says something is missing must rest on a record that says so.

A voice sentence that asserts an absence ("we have no", "nothing survives",
"no text", "none of", "we cannot give you") is kept only when a record it
cites states that absence about the same thing, and keeps that record's
scope: the years it names, or its own "so far as" limit. Otherwise the
sentence is withheld and the answer says less.

Support is read from the cited records' spoken fields only (the registry in
engine.m1.spoken_fields), never from build notes, prohibition fields, ids or
line numbers. The match is by whole words: the sentence's content words must
mostly appear in one absence sentence of one cited record. A sentence with no
content word once the cue words are set aside ("We cannot say more.") makes
no claim about the world and passes. Deterministic; no model call.
"""
from __future__ import annotations

import re

from engine.m1.spoken_fields import SHARED_SPOKEN_FIELDS, field_texts, fields_with_role
from engine.prose import sentences

REASON_ABSENCE_UNSUPPORTED = "states an absence that no record it cites states"
REASON_ABSENCE_SCOPE = "states an absence wider than the record it cites keeps"

R26_SENTENCE = "our record doesn't mention that christian tradition"

_CUES = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"\b(?:we|i|our record|the record)\s+(?:have|has|hold|holds)\s+(?:no|nothing|not)\b",
        r"\b(?:we|i)\s+(?:do\s+not|don't|cannot|can't|can\s+not)\s+(?:have|give|offer|show|point|name|quote|supply)\b",
        r"\bno\b[^.!?]{0,60}?\b(?:survives?|survived|reaches|reached|remains?|exists?|is\s+known|is\s+kept|is\s+held)\b",
        r"\bnothing\b[^.!?]{0,40}?\b(?:survives?|survived|reaches|reached|remains?|exists?|is\s+known)\b",
        r"(?<!almost\s)(?<!nearly\s)\bnone\s+of\b[^.!?]{0,60}?\b(?:survives?|survived|saved|kept|written|wrote|reached|reaches|left|remains?)\b",
    )
)
_SCOPE_MARKERS = (
    re.compile(r"\b(?:1[0-9]{3}|[2-9][0-9]{2})\b"),
    re.compile(r"\b(?:in|across|through(?:out)?|over|during)\s+(?:all\s+)?(?:our|the)\s+(?:\w+\s+)?years\b", re.IGNORECASE),
    re.compile(r"\b(?:so|as)\s+far\s+as\b", re.IGNORECASE),
    re.compile(r"\bour\s+(?:own\s+)?(?:record|shelf|sources)\b", re.IGNORECASE),
)
_NUMERAL = re.compile(r"\b(\d{3,4})\b")
_WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")
_FUNCTION_WORDS = frozenset({
    "that", "this", "with", "have", "from", "they", "their", "there", "were", "what", "when", "which", "would",
    "could", "does", "your", "ours", "also", "into", "than", "then", "them", "been", "being", "only", "give",
    "gives", "said", "says", "those", "these", "some", "such", "more", "most", "many", "much", "still", "yet",
    "here", "about", "there", "because", "other", "ever", "never", "while", "where", "whose", "will", "shall", "must",
})
_CUE_WORDS = frozenset({
    "survive", "survives", "survived", "survival", "record", "records", "exist", "exists", "remain", "remains",
    "reach", "reaches", "reached", "known", "kept", "held", "hold", "holds", "cannot", "nothing", "none", "name",
    "show", "point", "offer", "supply", "quote",
})
MATCH_SHARE = 0.25
MATCH_MINIMUM = 2


def _strings(value) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [t for key, v in value.items() if key != "speaker" for t in _strings(v)]
    if isinstance(value, list):
        return [t for v in value for t in _strings(v)]
    return []


def spoken_text(record: dict) -> str:
    """The prose of the fields the voice sees for this record: its type's
    spoken fields and the shared ones, nested lists and mappings included."""
    record_type = record.get("record_type") or ""
    out = []
    for name in [*fields_with_role(record_type), *SHARED_SPOKEN_FIELDS]:
        value = record
        for part in name.split("."):
            value = value.get(part) if isinstance(value, dict) else None
        out.extend(_strings(value))
    return " ".join(out)


def has_absence_cue(sentence: str) -> bool:
    return any(cue.search(sentence) for cue in _CUES)


def content_words(sentence: str) -> frozenset[str]:
    words = set()
    for word in _WORD.findall(sentence.lower()):
        word = word.strip("'’-")
        if len(word) < 4 or word in _FUNCTION_WORDS:
            continue
        if len(word) > 5 and word.endswith("s") and not word.endswith("ss"):
            word = word[:-1]
        if word in _CUE_WORDS:
            continue
        words.add(word)
    return frozenset(words)


_LIMIT_TYPES = frozenset({"honest_limit"})
_LIMIT_FIELDS = {"world_core": ("thinness", "cautions")}


def _candidates(record: dict) -> list[str]:
    """The sentences of a cited record that can back an absence: every
    sentence of a limit record (its whole statement is a limit), a world
    core's thinness and cautions, and any other sentence that carries an
    absence cue."""
    record_type = record.get("record_type")
    if record_type in _LIMIT_TYPES:
        return sentences(spoken_text(record))
    own = [t for name in _LIMIT_FIELDS.get(record_type, ()) for t in field_texts(record, name)]
    return [*sentences(" ".join(own)), *(s for s in sentences(spoken_text(record)) if has_absence_cue(s))]


def _years(record: dict) -> tuple[int, int] | None:
    years = (record.get("use_note") or {}).get("years")
    if isinstance(years, dict) and isinstance(years.get("from"), int) and isinstance(years.get("to"), int):
        return years["from"], years["to"]
    return None


def _keeps_scope(sentence: str, supporting: str, record: dict) -> bool:
    """True when the supporting sentence states no scope, or the claim states
    one too. A year in the claim must lie inside the record's own years."""
    window = _years(record)
    if any(marker.search(supporting) for marker in _SCOPE_MARKERS) and not any(m.search(sentence) for m in _SCOPE_MARKERS):
        return False
    if window is not None:
        return all(window[0] <= int(n) <= window[1] for n in _NUMERAL.findall(sentence))
    return True


def check_absence(sentence: str, cited: list[dict]) -> str | None:
    """None when the sentence makes no absence claim or the cited records
    back it with its scope; else the reason it is withheld."""
    if not has_absence_cue(sentence) or R26_SENTENCE in sentence.lower():
        return None
    claimed = content_words(sentence)
    if not claimed:
        return None
    scope_failed = False
    for record in cited:
        best: tuple[int, bool, str] | None = None
        for candidate in _candidates(record):
            shared = claimed & content_words(candidate)
            if len(shared) < min(MATCH_MINIMUM, len(claimed)) or len(shared) < MATCH_SHARE * len(claimed):
                continue
            rank = (len(shared), any(marker.search(candidate) for marker in _SCOPE_MARKERS), candidate)
            if best is None or rank[:2] > best[:2]:
                best = rank
        if best is None:
            continue
        if _keeps_scope(sentence, best[2], record):
            return None
        scope_failed = True
    return REASON_ABSENCE_SCOPE if scope_failed else REASON_ABSENCE_UNSUPPORTED
