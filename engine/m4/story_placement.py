"""Stories are placed by code, on a world that switches story placement on.

A world's registry entry (records/worlds/<key>.yaml) sets
`story_placement: true`, and its package carries it in frame.json. On such a
world the evidence block lists each offered story with a telling, not yet
told, by its marker, and the directive names them (`with_placeable_stories`,
`story_lines`). The voice writes one sentence of its own that names who or
what the story is about and ends it with `[[story:<record id>]]`.

`place_stories` runs inside engine.m4.turn.apply_net, after the markdown
scrub and before quote placement:

- a valid marker becomes the voice's sentence, tagged with the story and
  ending in a colon, then the record's `telling` word for word, its
  paragraphs kept and each sentence tagged with the record before its
  closing punctuation, where the net's splitter keeps the tag. The telling
  stands as its own paragraphs; the voice's text goes on after it. A marker
  standing alone takes the sentence before it as its introduction; words
  after the marker in its sentence are cut.
- a marker for a story not offered this turn, one without a telling, one
  the conversation has already told, a second story in one reply, or an
  introduction that shares no word with the story's `tellable_as` or
  `use_note.means` places nothing, and its sentence goes with it.

Each placed sentence is returned in "placed_sentences", and the grounding
net verifies it against the telling word for word
(grounding_net._placed_story_verdict). Quote placement then runs over the
result and never takes a placed sentence as a quote's lead-in.
Deterministic string operations; no model call.
"""
from __future__ import annotations

import re

from engine.m4.grounding_net import STORY_MARKER, parse_tagged, placed_key, strip_tags
from engine.m4.quote_placement import (
    _MARKER_TAIL,
    _PARAGRAPH_BREAK,
    _SENTENCE_END,
    REASON_LEAD_IN,
    REASON_STORY_RETOLD,
    PlacementContext,
    _lead_for_quote,
    _Report,
    _take_lead_in,
)
from engine.prose import content_words, quote_aware_sentences

_STORY_MARKER_ID = re.compile(r"\[\[\s*story\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)
_CLOSING = re.compile(r"([.!?]+[\"'”’)]*)\s*$")

REASON_STORY_NOT_OFFERED = "story record not offered for placement this turn"
REASON_SECOND_STORY = "second placed story in one reply"
REASON_STORY_SUBJECT = "introduction names nothing the story is about"
MAX_PLACED_STORIES_PER_REPLY = 1

STORY_OFFERS_LINE = "Stories you may place this turn, and no others: {offers}."
STORY_PLACE_LINE = (
    "To tell one, write one sentence of your own that names who or what it is about, and end it with its "
    "marker (\"Our sayings tell of Abba Moses at Scete: [[story:id]]\" is the shape). Code sets the whole story "
    "in after it. Place at most one. Never tell the story yourself, before or after the marker."
)


def with_placeable_stories(turn_evidence: dict, repository_records: dict[str, dict]) -> dict:
    """The evidence with each story that may be placed marked `placeable`:
    one with a telling, not already told in this conversation."""
    candidates = [
        {**c, "placeable": True}
        if c["record_type"] == "story" and not c.get("used_in_round") and not c.get("already_told_this_session")
        and ((repository_records.get(c["id"]) or {}).get("telling") or "").strip()
        else c
        for c in turn_evidence["candidates"]
    ]
    return {**turn_evidence, "candidates": candidates}


def story_lines(offers: list[dict]) -> list[str]:
    """The directive's story lines: the stories this reply may place, by
    marker and what each is about; none when no story may be placed."""
    if not offers:
        return []
    listed = "; ".join(f"[[story:{c['id']}]] ({' '.join((c.get('head') or '').split())})" for c in offers)
    return [STORY_OFFERS_LINE.format(offers=listed), STORY_PLACE_LINE]


def place_stories(tagged_text: str, *, repository_records: dict[str, dict], context: PlacementContext) -> dict:
    """The voice's tagged text with its story markers placed, as the module
    docstring describes. Returns {"text", "placed" (story ids), "placed_sentences"
    (each placed sentence's text, tags stripped and whitespace collapsed, to
    its record id), "placed_drafts" (each introduction's text to the
    sentence as the voice wrote it, marker included), "removed"}."""
    report = _Report()
    placed: list[str] = []
    paragraphs_out: list[list[str]] = []
    if not STORY_MARKER.search(tagged_text or ""):
        return {"text": tagged_text or "", "placed": [], "placed_sentences": {}, "placed_drafts": {}, "removed": []}

    for paragraph in (p for p in _PARAGRAPH_BREAK.split(tagged_text or "") if p.strip()):
        kept: list[str] = []
        sentences = quote_aware_sentences(paragraph)
        position = 0
        while position < len(sentences):
            sentence = sentences[position]
            position += 1
            marker = STORY_MARKER.search(sentence)
            if not marker:
                kept.append(sentence)
                continue
            sealed = frozenset(placed)
            lead = sentence[: marker.start()].strip()
            drafted = sentence[: marker.end()].strip()
            reason, record = _story_verdict(marker.group(0), repository_records, context, len(placed))
            if reason is None and not lead:
                lead = _take_lead_in(kept, paragraphs_out, sealed)
                drafted = f"{lead} {drafted}".strip()
            if reason is None and not _names_story_subject(lead, record):
                reason = REASON_STORY_SUBJECT
            if reason is None:
                intro = _story_intro(lead, record["id"])
                kept.append(intro)
                report.placed_drafts[placed_key(strip_tags(intro))] = drafted
                paragraphs_out.append(kept)
                kept = []
                for block in _telling_paragraphs(record):
                    for tagged in block:
                        report.placed_sentences[placed_key(strip_tags(tagged))] = record["id"]
                    paragraphs_out.append(block)
                placed.append(record["id"])
            else:
                report.drop(STORY_MARKER.sub("", drafted).strip() or drafted, reason, draft=drafted)
                if not lead and (previous := _take_lead_in(kept, paragraphs_out, sealed, only_if_lead=True)):
                    report.drop(previous, REASON_LEAD_IN)
            tail = _MARKER_TAIL.sub("", sentence[marker.end():])
            if tail:
                if tail[0].islower() or tail[0].isdigit():
                    ended = _SENTENCE_END.search(tail)
                    tail = tail[ended.end():].strip() if ended else ""
                if tail:
                    sentences.insert(position, tail)
        if kept:
            paragraphs_out.append(kept)

    return {
        "text": "\n\n".join(" ".join(p) for p in paragraphs_out if p),
        "placed": placed,
        "placed_sentences": report.placed_sentences,
        "placed_drafts": report.placed_drafts,
        "removed": report.removed,
    }


def _story_verdict(
    marker: str, repository_records: dict[str, dict], context: PlacementContext, placed_so_far: int
) -> tuple[str | None, dict | None]:
    """(reason it cannot be placed, None) or (None, the story record)."""
    found = _STORY_MARKER_ID.fullmatch(marker)
    record_id = found.group(1).lower() if found else None
    record = repository_records.get(record_id) if record_id else None
    if record is None or record.get("record_type") != "story" or not (record.get("telling") or "").strip():
        return REASON_STORY_NOT_OFFERED, None
    if record_id in context.told_stories:
        return REASON_STORY_RETOLD, None
    if record_id not in context.offered_stories:
        return REASON_STORY_NOT_OFFERED, None
    if placed_so_far >= MAX_PLACED_STORIES_PER_REPLY:
        return REASON_SECOND_STORY, None
    return None, record


def _names_story_subject(lead: str, record: dict) -> bool:
    """The introduction shares a content word with what the story is about:
    its tellable_as or its use note's meaning."""
    subject = " ".join(filter(None, [record.get("tellable_as"), (record.get("use_note") or {}).get("means")]))
    return bool(content_words(strip_tags(lead)) & content_words(subject))


def _story_intro(lead: str, record_id: str) -> str:
    """The voice's introduction, tagged with the story, ending in a colon."""
    intro = _lead_for_quote(lead)
    if f"[[{record_id}]]" in intro:
        return intro
    return f"{intro[:-1]} [[{record_id}]]:"


def _telling_paragraphs(record: dict) -> list[list[str]]:
    """The record's telling as paragraphs of sentences, each sentence tagged
    with the record before its closing punctuation."""
    tag = f" [[{record['id']}]]"
    out = []
    for paragraph in _PARAGRAPH_BREAK.split(record["telling"].strip()):
        block = []
        for sentence in parse_tagged(paragraph):
            raw = sentence["raw"].strip()
            end = _CLOSING.search(raw)
            block.append(f"{raw[: end.start()]}{tag}{end.group(1)}" if end else f"{raw}{tag}")
        if block:
            out.append(block)
    return out
