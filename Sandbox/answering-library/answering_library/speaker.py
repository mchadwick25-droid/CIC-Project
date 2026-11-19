"""Deterministic speaker state per passage: known, mixed or unknown.

known only when the edition is a single-author file (exactly one author id
across the bucket rows that claim it), the passage is not apparatus, and
nothing in the filename, division title or text points to another voice.
Dialogue, polemic, letter collections, conciliar acts and passages with
dense quotation of another speaker are mixed. Everything else is unknown.
"""
from __future__ import annotations

import re

FILENAME_MIXED = re.compile(
    r"(dialog|disputation|colloquy|acta|acts-of|councils?|concili|synod|canons|epistol|letters|lettres|"
    r"briefe|correspondence|contra|adversus|adversum|against|refutation|confutation|invective)",
    re.I,
)
TITLE_MIXED = re.compile(
    r"(dialog|disputation|colloquy|acta\b|acts?\b|council|concilium|synod|session|sessio|actio|canon|"
    r"letter|epistol|lettre|brief|contra\b|against|adversus|invective|question|quaestio|objection)",
    re.I,
)
_QUOTED = re.compile(r"“[^”]{15,}”|«[^»]{15,}»|„[^“]{15,}“|\"[^\"]{15,}\"")
_SAYING = re.compile(
    r"\b(inquit|inquiunt|dixit|dicit|dicunt|ait|aiunt|respondit|respondet|answered|replied|said|saith|asked|"
    r"quoth|dit|répondit|demanda|sagte|antwortete|fragte|ἔφη|εἶπεν|εἶπον|ἀπεκρίθη|ответил|сказал)\b",
    re.I,
)
_LABEL = re.compile(r"(?:^|\s)(?:[A-Z][A-Za-z]{1,12}|[QA])\s?[:.]\s+[A-Z]")
_SCRIPTURE_REF = re.compile(r"\b(?:[1-3]\s)?[A-Z][a-z]{2,8}\.?\s\d{1,3}[:,.]\s?\d{1,3}")

QUOTED_SHARE = 0.12
SAYING_PER_100 = 1.5
SCRIPTURE_PER_100 = 1.5
EMBEDDED_PER_100 = 1.5


def mixed_reasons(filename: str, title: str, text: str, words: int, embedded: int) -> list[str]:
    reasons = []
    if FILENAME_MIXED.search(filename):
        reasons.append("filename-genre")
    if title and TITLE_MIXED.search(title):
        reasons.append("division-title-genre")
    if text:
        quoted = sum(len(m.group(0)) for m in _QUOTED.finditer(text))
        if quoted / len(text) >= QUOTED_SHARE:
            reasons.append("quotation-density")
        per100 = 100.0 / max(words, 1)
        if len(_SAYING.findall(text)) * per100 >= SAYING_PER_100:
            reasons.append("speech-verbs")
        if len(_LABEL.findall(text)) >= 3:
            reasons.append("speaker-labels")
        if len(_SCRIPTURE_REF.findall(text)) * per100 >= SCRIPTURE_PER_100:
            reasons.append("scripture-references")
    if embedded * 100.0 / max(words, 1) >= EMBEDDED_PER_100:
        reasons.append("embedded-markup")
    return reasons


def classify(filename: str, authors: list[str], title: str, text: str, words: int,
             apparatus: bool, embedded: int = 0) -> dict:
    if apparatus:
        return {"state": "unknown", "voice": None}
    if mixed_reasons(filename, title, text, words, embedded):
        return {"state": "mixed", "voice": None}
    if len(authors) == 1:
        return {"state": "known", "voice": authors[0]}
    return {"state": "unknown", "voice": None}
