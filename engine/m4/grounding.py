"""Deterministic grounding checks (Artifact-5 SS2: "deterministic grounding
checks run before citations is emitted - they gate decoration, never the
text"; "citations.drawn_on subset-of text-grounded set"). Explicitly narrow
and mechanical - same discipline as engine.m3.grading's register_check: a
real, tested check against a real known shape, not a general NLP grounding
classifier.

Two checks:
1. Every claimed drawn_on id must be a real repository record id - an
   invented id is disqualified outright, not merely downgraded.
2. A short excerpt of that record's own words must actually appear
   (normalized, verbatim-window match) inside the streamed answer - if it
   can't be found, the claim demotes to 'consulted' rather than being
   trusted at face value. This never touches the streamed text itself,
   only which citation badges get shown.

A third, independent, hard check: a do-not-voice-licensed quote's exact
text must never appear verbatim in the answer at all - not a citation
question but a content-licensing one, checked here because this is the one
place both the record license data and the streamed answer text are in
hand together.
"""
import re


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def _record_excerpt(record: dict) -> str | None:
    """The short piece of a record's own words worth checking for - not
    every record type carries the same field, checked in priority order."""
    for key in ("text", "statement", "plain_meaning", "quick_meaning", "tellable_as", "description", "positions"):
        value = record.get(key)
        if isinstance(value, str) and value.strip():
            return value
        if isinstance(value, list) and value and isinstance(value[0], str):
            return value[0]
    return None


def _excerpt_found(excerpt: str, normalized_answer: str, *, window_words: int = 6) -> bool:
    words = _normalize(excerpt).split()
    if not words:
        return False
    if len(words) <= window_words:
        return " ".join(words) in normalized_answer
    for start in range(0, len(words) - window_words + 1):
        if " ".join(words[start : start + window_words]) in normalized_answer:
            return True
    return False


def ground_citations(*, answer_text: str, claimed_drawn_on: list[str], repository_records: dict[str, dict]) -> dict:
    """repository_records: {record_id: record_dict} - build once from
    compiled/repository.json's records list keyed by "id"."""
    normalized_answer = _normalize(answer_text)
    drawn_on, consulted, unknown_ids = [], [], []

    for record_id in claimed_drawn_on:
        record = repository_records.get(record_id)
        if record is None:
            unknown_ids.append(record_id)
            continue
        excerpt = _record_excerpt(record)
        grounded = excerpt is not None and _excerpt_found(excerpt, normalized_answer)
        (drawn_on if grounded else consulted).append(record_id)

    return {"drawn_on": drawn_on, "consulted": consulted, "unknown_ids": unknown_ids}


def find_do_not_voice_violation(*, answer_text: str, quotes: list[dict]) -> str | None:
    """Returns the offending quote id if a do-not-voice-licensed quote's
    exact text appears verbatim in the answer, else None - independent of
    the citation-grounding logic above, and fires even if the model never
    claimed the quote as a citation at all."""
    normalized_answer = _normalize(answer_text)
    for quote in quotes:
        if quote.get("license") != "do-not-voice":
            continue
        if _normalize(quote["text"]) in normalized_answer:
            return quote["id"]
    return None
