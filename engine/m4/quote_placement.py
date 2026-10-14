"""Quotes are placed by code, never typed by the voice.

The voice marks where a quote goes, and which record, with
`[[quote:<record id>]]`, written as the last thing in the sentence that
introduces it. `place_quotes` runs inside engine.m4.turn.apply_net, on the
voice's tagged text after the markdown scrub and before the grounding net,
and returns tagged text the net checks:

- a valid marker becomes the lead-in the voice wrote, then the record's
  `modern_rendering` in curly quotation marks, then the record's ordinary
  citation tag, and the quote ends its paragraph. The lead-in's closing
  punctuation becomes a colon; a marker standing alone takes the sentence
  before it as its lead-in; words after the marker in its sentence are cut.
- a marker for a record that is not in this turn's evidence, one the
  conversation has already voiced, a marker past the one quote a reply may
  carry, a record whose rendering cannot be set apart as one quotation, or
  a placement the net's own placed-quote check refuses
  (grounding_net.placed_quote_holds) places nothing, and the sentence that
  introduced it goes with it. Only a quote that is placed counts toward
  the one a reply may carry.
- a story the conversation has already told keeps its first tagged
  sentence, as a reference back; later sentences tagged to it go.

Stories are placed the same way, on a world whose package switches story
placement on (frame.json `story_placement`). The voice writes one sentence
of its own that names who or what the story is about and ends it with
`[[story:<record id>]]`. A valid marker becomes that sentence, tagged with
the story and ending in a colon, then the record's `telling` word for word,
its paragraphs kept and each sentence tagged with the record. The telling
stands as its own paragraphs; the voice's text goes on after it. A marker
for a story not offered this turn, one the conversation has already told, a
second story in one reply, or an introduction that names nothing the story
is about places nothing, and its sentence goes with it.

Every other quotation rule (a quotation the voice typed, words attributed
without quotation marks, a sentence tagged to a quote record not yet placed,
or giving its words) is the grounding net's, which knows each placed
sentence from `placed_sentences`.
Deterministic string operations; no model call.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from engine.m4.grounding_net import (
    QUOTE_MARKER,
    STORY_MARKER,
    QuotationIndex,
    parse_tagged,
    placed_key,
    placed_quote_holds,
    quoted_span_positions,
    reads_as_lead,
    strip_tags,
)
from engine.m4.rhythm import MAX_PLACED_QUOTES_PER_REPLY
from engine.prose import content_words, quote_aware_sentences

_MARKER_ID = re.compile(r"\[\[\s*quote\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)
_STORY_MARKER_ID = re.compile(r"\[\[\s*story\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)
# A tag goes before a sentence's closing punctuation and closing marks, the
# place the net's sentence splitter keeps it with its own sentence.
_CLOSING = re.compile(r"([.!?]+[\"'\u201d\u2019)]*)\s*$")
_TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")
_PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")
# What may follow a marker and still end its sentence: closing punctuation,
# and the closing mark of a quotation the voice typed around it.
_MARKER_TAIL = re.compile(r"^[\s.,;:!?\"'\u201d\u2019\u00bb)\]]+")

REASON_NOT_OFFERED = "quote record not in this turn's evidence"
REASON_ALREADY_VOICED = "quote record already voiced in this conversation"
REASON_SECOND_QUOTE = "second placed quote in one reply"
REASON_NOT_SETTABLE = "rendering cannot be set apart as one quotation"
REASON_PLACED_MISMATCH = "placed quote does not match its record"
REASON_LEAD_IN = "lead-in to a quote that was not placed"
REASON_STORY_RETOLD = "story already told in this conversation"
REASON_STORY_NOT_OFFERED = "story record not offered for placement this turn"
REASON_SECOND_STORY = "second placed story in one reply"
REASON_STORY_SUBJECT = "introduction names nothing the story is about"
MAX_PLACED_STORIES_PER_REPLY = 1


@dataclass(frozen=True)
class PlacementContext:
    """What one reply may place. `offered` is the quote record ids this
    turn's evidence carried; `voiced` the quote ids the conversation has
    already voiced; `told_stories` the story ids it has already told;
    `offered_stories` the story ids this turn may place (empty on a world
    that does not place stories)."""
    offered: frozenset[str] = frozenset()
    voiced: frozenset[str] = frozenset()
    told_stories: frozenset[str] = frozenset()
    offered_stories: frozenset[str] = frozenset()
    max_quotes: int = MAX_PLACED_QUOTES_PER_REPLY
    max_stories: int = MAX_PLACED_STORIES_PER_REPLY

    @classmethod
    def for_evidence(cls, candidates: list[dict], **kwargs) -> "PlacementContext":
        """The context for a turn whose evidence carried `candidates`."""
        return cls(offered=frozenset(c["id"] for c in candidates if c.get("record_type") == "quote"), **kwargs)


@dataclass
class _Report:
    placed_sentences: dict[str, str] = field(default_factory=dict)
    placed_drafts: dict[str, str] = field(default_factory=dict)
    removed: list[dict] = field(default_factory=list)
    stories: list[str] = field(default_factory=list)

    def drop(self, sentence: str, why: str, *, draft: str | None = None) -> None:
        self.removed.append({"sentence": strip_tags(sentence).strip(), "why": why, "draft": (draft or sentence).strip()})


def _lead_for_quote(lead: str) -> str:
    lead = lead.strip()
    if not lead:
        return ""
    trailing_tags = ""
    while True:
        match = re.search(r"(\s*\[\[[a-z0-9_.-]+\]\])\s*$", lead)
        if not match:
            break
        trailing_tags = match.group(1) + trailing_tags
        lead = lead[: match.start()]
    lead = re.sub(r"[\s.!?;,:]+$", "", lead)
    return f"{lead}{trailing_tags}:" if lead else ""


def _settable(composed: str, rendering: str) -> bool:
    if len(quote_aware_sentences(composed)) != 1 or _PARAGRAPH_BREAK.search(composed):
        return False
    return any(inner == rendering for _o, _c, inner in quoted_span_positions(strip_tags(composed)))


def place_quotes(tagged_text: str, *, repository_records: dict[str, dict], context: PlacementContext) -> dict:
    """The voice's tagged text with its quote markers placed, as the module
    docstring describes. Returns {"text", "placed" (record ids, in order),
    "placed_sentences" (each placed sentence's text, tags stripped and
    whitespace collapsed, to its record id), "placed_drafts" (the same keys,
    to the sentence as the voice wrote it, marker included), "removed" (each
    sentence removed, with why, and as the voice wrote it in "draft")}."""
    report = _Report()
    index = QuotationIndex(repository_records)
    paragraphs_out: list[list[str]] = []
    story_seen: set[str] = set()

    for paragraph in (p for p in _PARAGRAPH_BREAK.split(tagged_text or "") if p.strip()):
        kept: list[str] = []
        sentences = quote_aware_sentences(paragraph)
        position = 0
        while position < len(sentences):
            sentence = sentences[position]
            position += 1

            story_marker = STORY_MARKER.search(sentence)
            if story_marker:
                lead = sentence[: story_marker.start()].strip()
                drafted = sentence[: story_marker.end()].strip()
                reason, record = _story_verdict(story_marker.group(0), repository_records, context, len(report.stories))
                if reason is None and not lead:
                    lead = _take_lead_in(kept, paragraphs_out, report.placed_sentences)
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
                    report.stories.append(record["id"])
                else:
                    report.drop(STORY_MARKER.sub("", drafted).strip() or drafted, reason, draft=drafted)
                    if not lead and (previous := _take_lead_in(kept, paragraphs_out, report.placed_sentences, only_if_lead=True)):
                        report.drop(previous, REASON_LEAD_IN)
                tail = _MARKER_TAIL.sub("", sentence[story_marker.end():])
                if tail:
                    if tail[0].islower() or tail[0].isdigit():
                        ended = _SENTENCE_END.search(tail)
                        tail = tail[ended.end():].strip() if ended else ""
                    if tail:
                        sentences.insert(position, tail)
                continue

            marker = QUOTE_MARKER.search(sentence)
            if marker:
                lead = sentence[: marker.start()].strip()
                rest = sentence[marker.end():]
                drafted = sentence[: marker.end()].strip()
                placed_quotes = sum(1 for rid in report.placed_sentences.values() if rid not in report.stories)
                reason, record = _placement_verdict(marker.group(0), repository_records, context, placed_quotes)
                composed = None
                if reason is None:
                    if not lead:
                        lead = _take_lead_in(kept, paragraphs_out, report.placed_sentences)
                        drafted = f"{lead} {drafted}".strip()
                    rendering = record["modern_rendering"]
                    composed = f"{_lead_for_quote(lead)} “{rendering}” [[{record['id']}]]".strip()
                    if not _settable(composed, rendering):
                        reason, composed = REASON_NOT_SETTABLE, None
                    elif not placed_quote_holds(composed, repository_records, index, record["id"]):
                        # decided here, as the net decides it, so a quote the
                        # net would refuse never takes the reply's one place
                        reason, composed = REASON_PLACED_MISMATCH, None
                if composed is None:
                    report.drop(QUOTE_MARKER.sub("", drafted).strip() or drafted, reason, draft=drafted)
                    if not lead and (previous := _take_lead_in(kept, paragraphs_out, report.placed_sentences, only_if_lead=True)):
                        report.drop(previous, REASON_LEAD_IN)
                else:
                    kept.append(composed)
                    report.placed_sentences[placed_key(strip_tags(composed))] = record["id"]
                    report.placed_drafts[placed_key(strip_tags(composed))] = drafted
                    paragraphs_out.append(kept)
                    kept = []
                tail = _MARKER_TAIL.sub("", rest)
                if tail:
                    if tail[0].islower() or tail[0].isdigit():
                        ended = _SENTENCE_END.search(tail)
                        tail = tail[ended.end():].strip() if ended else ""
                    if tail:
                        sentences.insert(position, tail)
                continue

            story_tags = [t for t in _TAG.findall(sentence) if t in context.told_stories]
            if story_tags:
                if any(t in story_seen for t in story_tags):
                    report.drop(sentence, REASON_STORY_RETOLD)
                    continue
                story_seen.update(story_tags)

            kept.append(sentence)
        if kept:
            paragraphs_out.append(kept)

    return {
        "text": "\n\n".join(" ".join(p) for p in paragraphs_out if p),
        "placed": list(dict.fromkeys(report.placed_sentences.values())),
        "placed_sentences": report.placed_sentences,
        "placed_drafts": report.placed_drafts,
        "removed": report.removed,
    }


def _take_lead_in(
    kept: list[str], paragraphs_out: list[list[str]], placed: dict[str, str], *, only_if_lead: bool = False,
) -> str:
    """The sentence before a marker that stands alone: the previous sentence
    of this paragraph, or the previous paragraph's last when that paragraph
    is that one sentence or ends in a colon. With `only_if_lead` the
    sentence must also read as an introduction. A sentence code placed is
    never taken."""
    if kept:
        if only_if_lead and not reads_as_lead(kept[-1]):
            return ""
        return kept.pop()
    if paragraphs_out and paragraphs_out[-1]:
        previous = paragraphs_out[-1]
        if placed_key(strip_tags(previous[-1])) in placed:
            return ""
        if len(previous) == 1 or strip_tags(previous[-1]).rstrip().endswith(":"):
            if only_if_lead and not reads_as_lead(previous[-1]):
                return ""
            lead = previous.pop()
            if not previous:
                paragraphs_out.pop()
            return lead
    return ""


def _story_verdict(
    marker: str, repository_records: dict[str, dict], context: PlacementContext, placed_so_far: int
) -> tuple[str | None, dict | None]:
    """(reason it cannot be placed, None) or (None, the story record)."""
    found = _STORY_MARKER_ID.fullmatch(marker)
    record_id = found.group(1).lower() if found else None
    record = repository_records.get(record_id) if record_id else None
    if record is None or record.get("record_type") != "story" or record_id not in context.offered_stories:
        return REASON_STORY_NOT_OFFERED, None
    if not (record.get("telling") or "").strip():
        return REASON_STORY_NOT_OFFERED, None
    if record_id in context.told_stories:
        return REASON_STORY_RETOLD, None
    if placed_so_far >= context.max_stories:
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


def _placement_verdict(
    marker: str, repository_records: dict[str, dict], context: PlacementContext, placed_so_far: int
) -> tuple[str | None, dict | None]:
    """(reason it cannot be placed, None) or (None, the quote record)."""
    found = _MARKER_ID.fullmatch(marker)
    record_id = found.group(1).lower() if found else None
    record = repository_records.get(record_id) if record_id else None
    if record is None or record.get("record_type") != "quote" or record_id not in context.offered:
        return REASON_NOT_OFFERED, None
    if record_id in context.voiced:
        return REASON_ALREADY_VOICED, None
    if placed_so_far >= context.max_quotes:
        return REASON_SECOND_QUOTE, None
    if not (record.get("modern_rendering") or "").strip():
        return REASON_NOT_OFFERED, None
    return None, record
