"""Spoken text that talks to the question instead of answering it.

A witness, term or story the voice may say back must start with the answer.
Two shapes break that: a first sentence that ends in a question mark (the
question restated, or one nobody asked), and a second-person stage direction
that tells the voice how to organise its reply ("your second question",
"start with the part", "you asked", "as you asked").
"""
from __future__ import annotations

import re

from engine.m1 import gates

SPOKEN_TYPES = ("doctrinal_witness", "term", "story")

_STAGE_DIRECTION = re.compile(
    r"\b(?:your second question|start with the part|you asked|as you asked)\b", re.IGNORECASE
)
_FIRST_SENTENCE = re.compile(r".+?(?:[.!?]+['\"”’)]*)(?=\s|$)", re.DOTALL)


def _first_sentence(text: str) -> str:
    text = text.strip()
    match = _FIRST_SENTENCE.match(text)
    return match.group(0) if match else text


def _ends_in_question(sentence: str) -> bool:
    return sentence.rstrip().rstrip("'\"”’)").endswith("?")


def scaffolding_hits(records: dict[str, dict]) -> list[tuple[str, str, str]]:
    """(record id, field label, reason) for each spoken field that opens on a
    question or carries a second-person stage direction."""
    hits: list[tuple[str, str, str]] = []
    for rid, rec in sorted(records.items()):
        record_type = rec.get("record_type")
        if record_type not in SPOKEN_TYPES:
            continue
        for label, text in gates._readability_checks(record_type, rec):
            if _ends_in_question(_first_sentence(text)):
                hits.append((rid, label, "the first sentence ends in a question mark"))
            if match := _STAGE_DIRECTION.search(text):
                hits.append((rid, label, f"second-person stage direction: {match.group(0)!r}"))
    return hits
