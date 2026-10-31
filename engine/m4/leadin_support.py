"""The facts a quote's lead-in states must be supported by a source document.

A lead-in names its speaker (the placed-quote check) and may add more: a
place, an addressee, a role, a kind of text, an occasion, a time. Each such
detail is allowed when the quote record, the speaker's figure record, one of
the quote's source records, or the edition text around the quote's cited
lines supports it, and refused when none does. The first supporting span is
kept so the reader can be shown where it came from.

Details are read by rule from the lead-in's own words (extract_details);
support is a word match against a pool of spans, tried in this order: the
quote record's fields (source loci included), the speaker's figure record and
the quote's source records, then the edition (the volume title, the headings
above the cited lines, and the lines around them). A detail with no
supporting span is unresolved, and placement then writes the plain lead-in
from the record's speaker. Deterministic string work; no model call.
"""
from __future__ import annotations

import functools
import re
from pathlib import Path

from engine.m4.grounding_net import strip_tags

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTEXT_RADIUS_LINES = 30
SNIPPET_CHARS = 60

_LOCUS = re.compile(r"(cic/texts/[\w./-]+?),?\s*lines?\s*(\d+)(?:\s*[-–]\s*(\d+))?")
_MARKUP = re.compile(r"<[^>]+>")
_HEADING = re.compile(r'<div[1-4][^>]*\btitle="([^"]+)"')
_VOLUME_TITLE = re.compile(r"<DC\.Title>(.*?)</DC\.Title>", re.S)
_WORD = re.compile(r"[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ'’-]*")
_NUMBER = re.compile(r"\b\d{2,4}\b")
_TIME = re.compile(
    r"\b(?:(?:a|one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s+(?:and a half\s+)?)?"
    r"(?:years?|decades?|centur(?:y|ies))(?:\s+and a half)?\s+(?:earlier|later|before|after|ago)\b"
    r"|\b(?:first|second|third|fourth|fifth|sixth)\s+century\b|\b(?:earlier|later)\b",
    re.IGNORECASE,
)

# Words that make a claim about the speaker's rank, the kind of text, or the
# occasion. Each must be found in a source span.
ROLE_WORDS = (
    "bishop", "presbyter", "priest", "deacon", "emperor", "proconsul", "martyr", "confessor", "pope",
    "catechumen", "teacher", "governor", "prefect", "monk", "abbot", "judge", "magistrate",
    "friend", "brother", "sister", "mother", "father", "son", "daughter", "disciple", "pupil", "colleague",
)
OCCASION_WORDS = (
    "council", "synod", "conference", "debate", "trial", "sentence", "persecution", "plague", "baptism",
    "ordination", "election", "exile", "deathbed", "conversion", "imprisonment", "siege", "banishment",
)
# A genre word in the lead-in is supported by any of the cue words beside it.
GENRE_CUES = {
    "spoken": (("preach", "sermon", "homil", "discourse"), ("homil", "sermon", "preach", "discourse", "beloved", "brethren")),
    "written": (
        ("wrote", "writes", "written", "letter", "epistle", "treatise", "book"),
        ("epistle", "letter", "treatise", "address", "book", "wrote", "writes", "written", "writing", "tractate"),
    ),
}
# Capitalised words that are not a name to be sourced.
NOT_A_NAME = frozenset({
    "In", "I", "It", "He", "She", "They", "We", "This", "That", "The", "A", "An", "And", "But", "So", "Then", "English",
    "Here", "There", "As", "When", "After", "Before", "While", "On", "At", "For", "To", "Of", "With", "From", "By", "His", "Her",
    "Their", "Our", "One", "Another", "Later", "Earlier",
    "Church", "Churches", "Scripture", "Scriptures", "Gospel", "Gospels", "Christ", "Lord", "God", "Holy", "Spirit",
    "Bible", "Testament", "Psalm", "Psalms", "Word", "Catholic",
})


PROSE_SKIP_KEYS = frozenset({
    "id", "record_type", "world_id", "schema_version", "status", "register", "canon_cells", "license", "source_id",
    "confidence", "speaker_or_author", "target", "type",
})
_RECORD_ID = re.compile(r"\b[a-z0-9]+\.[a-z_]+\.[a-z0-9][a-z0-9.-]*\b")
_LINE_NUMBERS = re.compile(r"\blines?\s*\d+(?:\s*[-–]\s*\d+)?", re.IGNORECASE)


@functools.lru_cache(maxsize=64)
def _file_lines(path: str) -> tuple[str, ...]:
    return tuple(Path(path).read_text(encoding="utf-8", errors="replace").splitlines())


def extract_details(lead: str, speaker_words: frozenset[str]) -> list[dict]:
    """The factual details a lead-in states beyond its speaker: names, numbers,
    roles, occasions, kinds of text and times. Each is {"kind", "text",
    "needs": the words any one of which supports it}."""
    plain = strip_tags(lead)
    plain = re.sub(r"^\s*In today[’']s English,?\s*", "", plain)
    details: list[dict] = []
    for match in _WORD.finditer(plain):
        word = re.sub(r"['’]s$", "", match.group(0))
        if word[0].isupper() and word not in NOT_A_NAME and word.lower() not in speaker_words:
            if not any(d["text"] == word for d in details):
                details.append({"kind": "name", "text": word, "needs": (word,)})
    for number in _NUMBER.findall(plain):
        details.append({"kind": "number", "text": number, "needs": (number,)})
    lowered = plain.lower()
    for word in ROLE_WORDS:
        if re.search(rf"\b{word}(?:s|es)?\b", lowered):
            details.append({"kind": "role", "text": word, "needs": (word,)})
    for word in OCCASION_WORDS:
        if re.search(rf"\b{word}(?:s|es)?\b", lowered):
            details.append({"kind": "occasion", "text": word, "needs": (word,)})
    for genre, (triggers, cues) in GENRE_CUES.items():
        trigger = next((t for t in triggers if re.search(rf"\b{t}", lowered)), None)
        if trigger:
            details.append({"kind": "genre", "text": trigger, "needs": cues})
    for time in _TIME.finditer(plain):
        phrase = time.group(0)
        details.append({"kind": "time", "text": phrase, "needs": (phrase,) if " " in phrase else ()})
    return details


# What a record says the speaker must not do or claim never supports a detail.
PROHIBITION_KEYS = frozenset({"not_for", "claim_guards", "do_not_retrieve_when", "prefer_instead", "retrieve_when", "relations"})
_PATH = re.compile(r"cic/texts/\S+")


def _record_text(record: dict) -> str:
    parts: list[str] = []

    def walk(value):
        if isinstance(value, str):
            parts.append(_LINE_NUMBERS.sub(" ", _RECORD_ID.sub(" ", _PATH.sub(" ", value))))
        elif isinstance(value, dict):
            for key, item in value.items():
                if key not in PROHIBITION_KEYS and key not in PROSE_SKIP_KEYS:
                    walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(record)
    return "\n".join(parts)


def _edition_spans(record: dict, texts_root: Path) -> list[tuple[str, str]]:
    spans: list[tuple[str, str]] = []
    for source in record.get("sources") or []:
        for found in _LOCUS.finditer(source.get("locus") or ""):
            relative, first, last = found.group(1), int(found.group(2)), int(found.group(3) or found.group(2))
            path = texts_root / relative
            if not path.exists():
                continue
            lines = _file_lines(str(path))
            if first > len(lines):
                continue
            head = "\n".join(lines[:200])
            if title := _VOLUME_TITLE.search(head):
                spans.append((f"{relative}#volume-title", _MARKUP.sub(" ", title.group(1))))
            for number in range(min(first, len(lines)), 0, -1):
                if heading := _HEADING.search(lines[number - 1]):
                    spans.append((f"{relative}, line {number} (heading)", heading.group(1)))
                    break
            low, high = max(1, first - CONTEXT_RADIUS_LINES), min(len(lines), last + CONTEXT_RADIUS_LINES)
            spans.append((f"{relative}, lines {low}-{high}", _MARKUP.sub(" ", "\n".join(lines[low - 1: high]))))
    return spans


def support_pool(record: dict, records: dict[str, dict], texts_root: Path) -> list[tuple[str, str]]:
    """The spans a lead-in detail may be supported by, in the order they are
    tried: (span id, text)."""
    pool: list[tuple[str, str]] = [(f"record {record['id']}", _record_text(record))]
    speaker = (record.get("speaker_or_author") or "").split()
    if speaker and speaker[0] in records:
        pool.append((f"record {speaker[0]}", _record_text(records[speaker[0]])))
    for source in record.get("sources") or []:
        source_record = records.get(source.get("source_id") or "")
        if source_record:
            pool.append((f"record {source_record.get('id')}", _record_text(source_record)))
    pool += _edition_spans(record, texts_root)
    return pool


def _supporting_span(detail: dict, pool: list[tuple[str, str]]) -> dict | None:
    for span_id, text in pool:
        for need in detail["needs"]:
            if detail["kind"] == "name":
                found = re.search(rf"(?<![\w]){re.escape(need)}(?:s|es|'s|’s)?(?![\w])", text)
            elif detail["kind"] in ("number", "time"):
                found = re.search(rf"(?<![\w]){re.escape(need)}(?![\w])", text, re.IGNORECASE)
            elif detail["kind"] == "genre":
                found = re.search(rf"(?<![\w]){re.escape(need)}", text, re.IGNORECASE)
            else:
                found = re.search(rf"(?<![\w]){re.escape(need)}(?:s|es)?(?![\w])", text, re.IGNORECASE)
            if found:
                start = max(0, found.start() - SNIPPET_CHARS)
                snippet = " ".join(text[start: found.end() + SNIPPET_CHARS].split())
                return {"detail": detail["text"], "kind": detail["kind"], "span": span_id, "snippet": snippet}
    return None


def check_leadin(
    lead: str, record: dict, records: dict[str, dict], *, speaker_words: frozenset[str], texts_root: Path = REPO_ROOT
) -> dict:
    """{"supported": [{"detail", "kind", "span", "snippet"}], "unresolved":
    [{"detail", "kind"}]} for a lead-in to the quote `record`."""
    details = extract_details(lead, speaker_words)
    if not details:
        return {"supported": [], "unresolved": []}
    pool = support_pool(record, records, texts_root)
    supported, unresolved = [], []
    for detail in details:
        found = _supporting_span(detail, pool)
        if found:
            supported.append(found)
        else:
            unresolved.append({"detail": detail["text"], "kind": detail["kind"]})
    return {"supported": supported, "unresolved": unresolved}
