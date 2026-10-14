"""Honest limits name their question.

A sentence the voice may say back must not end on a bare question word:
"We cannot tell you why." leaves the participant to guess what "why" asks.
The sentence names the question instead: "We cannot tell you why God let
the brothers die."

A sentence ends on a bare question word when its last word is how, why,
when, what, which, where or who, it does not end in a question mark, and
the sentence does not name the question. These shapes name it and are never
flagged:
- the word is a predicate after a form of "be" ("Person is who.", "which
  is which");
- it follows "not" in a contrast ("X is who, not what.");
- another question word stands earlier in the same clause ("who reads
  what", "who did what");
- it closes a list of questions the sentence has already opened ("how much
  to say, and when", "who wrote them, and when");
- it is "which" choosing among alternatives the sentence names ("her
  prudence, or his framing - we cannot tell you which");
- it is a noun after "the" ("the how") or the end of a hyphenated word
  ("know-how").
"""
from __future__ import annotations

import re

from engine.m1.loader import voiced_records
from engine.m1.spoken_fields import field_texts, shared_fields_with_role

QUESTION_WORDS = frozenset({"how", "why", "when", "what", "which", "where", "who"})
_EARLIER_QUESTION_WORDS = QUESTION_WORDS | {"whom", "whose", "whether"}
_NAMING_WORDS = frozenset({"is", "are", "was", "were", "be", "been", "being", "not", "the"})
_SENTENCE = re.compile(r"[^.!?]+(?:[.!?]+['\"”’)\]]*|$)")
_WORD = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")
_CLAUSE_BREAK = re.compile(r"[,;:—–()]|\s-\s")
_CLOSERS = "'\"”’)] \t\n"


def sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENTENCE.findall(text) if s.strip()]


def ends_on_bare_question_word(sentence: str) -> bool:
    """True when the sentence's last word is a question word whose question
    the sentence leaves unnamed."""
    body = sentence.rstrip(_CLOSERS)
    if body.endswith("?"):
        return False
    body = body.rstrip(".!" + _CLOSERS)
    if re.search(r"[-‐‑][A-Za-z]+$", body):
        return False
    clause = _CLAUSE_BREAK.split(body)[-1]
    words = [w.lower() for w in _WORD.findall(clause)]
    if not words or words[-1] not in QUESTION_WORDS:
        return False
    if len(words) > 1 and words[-2] in _NAMING_WORDS:
        return False
    if any(w in _EARLIER_QUESTION_WORDS for w in words[:-1]):
        return False
    before = [w.lower() for w in _WORD.findall(body)][:-1]
    if words[-2:-1] in (["and"], ["or"]) and any(w in _EARLIER_QUESTION_WORDS for w in before):
        return False
    if words[-1] == "which" and "or" in before:
        return False
    return True


def spoken_texts(rec: dict) -> list[tuple[str, str]]:
    """(field label, text) for every spoken field of a record: the fields the
    readability gate grades, then the shared nested fields such as the use
    note's meaning."""
    from engine.m1 import gates

    found = list(gates._readability_checks(rec.get("record_type"), rec))
    for field in shared_fields_with_role("voice-diet", "evidence-head"):
        found += [(field, text) for text in field_texts(rec, field)]
    return found


def bare_question_hits(records: dict[str, dict]) -> list[tuple[str, str, str]]:
    """(record id, field label, sentence) for each voiced record's spoken
    sentence that ends on a bare question word."""
    hits = []
    for rid, rec in sorted(voiced_records(records).items()):
        for label, text in spoken_texts(rec):
            for sentence in sentences(text):
                if ends_on_bare_question_word(sentence):
                    hits.append((rid, label, sentence))
    return hits
