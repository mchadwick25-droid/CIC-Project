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
  carry, or a record whose rendering cannot be set apart as one quotation
  places nothing, and the sentence that introduced it goes with it.
- a story the conversation has already told keeps its first tagged
  sentence, as a reference back; later sentences tagged to it go.

Every other quotation rule (a quotation the voice typed, words attributed
without quotation marks, a quote record named under its speaker) is the
grounding net's, which knows each placed sentence from `placed_sentences`.
Deterministic string operations; no model call.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from engine.m4.grounding_net import QUOTE_MARKER, placed_key, quoted_span_positions, reads_as_lead, strip_tags
from engine.m4.rhythm import MAX_PLACED_QUOTES_PER_REPLY
from engine.prose import quote_aware_sentences

_MARKER_ID = re.compile(r"\[\[\s*quote\s*:\s*([a-z0-9_.-]+)\s*\]\]", re.IGNORECASE)
_TAG = re.compile(r"\[\[([a-z0-9_.-]+)\]\]")
_PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")

REASON_NOT_OFFERED = "quote record not in this turn's evidence"
REASON_ALREADY_VOICED = "quote record already voiced in this conversation"
REASON_SECOND_QUOTE = "second placed quote in one reply"
REASON_NOT_SETTABLE = "rendering cannot be set apart as one quotation"
REASON_LEAD_IN = "lead-in to a quote that was not placed"
REASON_STORY_RETOLD = "story already told in this conversation"


@dataclass(frozen=True)
class PlacementContext:
    """What one reply may place. `offered` is the quote record ids this
    turn's evidence carried; `voiced` the quote ids the conversation has
    already voiced; `told_stories` the story ids it has already told."""
    offered: frozenset[str] = frozenset()
    voiced: frozenset[str] = frozenset()
    told_stories: frozenset[str] = frozenset()
    max_quotes: int = MAX_PLACED_QUOTES_PER_REPLY

    @classmethod
    def for_evidence(cls, candidates: list[dict], **kwargs) -> "PlacementContext":
        """The context for a turn whose evidence carried `candidates`."""
        return cls(offered=frozenset(c["id"] for c in candidates if c.get("record_type") == "quote"), **kwargs)


@dataclass
class _Report:
    placed_sentences: dict[str, str] = field(default_factory=dict)
    removed: list[dict] = field(default_factory=list)

    def drop(self, sentence: str, why: str) -> None:
        self.removed.append({"sentence": strip_tags(sentence).strip(), "why": why})


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
    whitespace collapsed, to its record id), "removed" (each sentence removed, with why)}."""
    report = _Report()
    paragraphs_out: list[list[str]] = []
    story_seen: set[str] = set()

    for paragraph in (p for p in _PARAGRAPH_BREAK.split(tagged_text or "") if p.strip()):
        kept: list[str] = []
        sentences = quote_aware_sentences(paragraph)
        index = 0
        while index < len(sentences):
            sentence = sentences[index]
            index += 1

            marker = QUOTE_MARKER.search(sentence)
            if marker:
                lead = sentence[: marker.start()].strip()
                rest = sentence[marker.end():]
                reason, record = _placement_verdict(marker.group(0), repository_records, context, len(report.placed_sentences))
                composed = None
                if reason is None:
                    if not lead:
                        lead = _take_lead_in(kept, paragraphs_out)
                    rendering = record["modern_rendering"]
                    composed = f"{_lead_for_quote(lead)} “{rendering}” [[{record['id']}]]".strip()
                    if not _settable(composed, rendering):
                        reason, composed = REASON_NOT_SETTABLE, None
                if composed is None:
                    report.drop(f"{lead} {QUOTE_MARKER.sub('', sentence)}".strip() if lead else sentence, reason)
                    if not lead and (previous := _take_lead_in(kept, paragraphs_out, only_if_lead=True)):
                        report.drop(previous, REASON_LEAD_IN)
                else:
                    kept.append(composed)
                    report.placed_sentences[placed_key(strip_tags(composed))] = record["id"]
                    paragraphs_out.append(kept)
                    kept = []
                tail = re.sub(r"^[\s.,;:!?]+", "", rest)
                if tail:
                    if tail[0].islower() or tail[0].isdigit():
                        ended = _SENTENCE_END.search(tail)
                        tail = tail[ended.end():].strip() if ended else ""
                    if tail:
                        sentences.insert(index, tail)
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
        "placed": list(report.placed_sentences.values()),
        "placed_sentences": report.placed_sentences,
        "removed": report.removed,
    }


def _take_lead_in(kept: list[str], paragraphs_out: list[list[str]], *, only_if_lead: bool = False) -> str:
    """The sentence before a marker that stands alone: the previous sentence
    of this paragraph, or the previous paragraph's last when that paragraph
    is that one sentence or ends in a colon. With `only_if_lead` the
    sentence must also read as an introduction."""
    if kept:
        if only_if_lead and not reads_as_lead(kept[-1]):
            return ""
        return kept.pop()
    if paragraphs_out and paragraphs_out[-1]:
        previous = paragraphs_out[-1]
        if len(previous) == 1 or strip_tags(previous[-1]).rstrip().endswith(":"):
            if only_if_lead and not reads_as_lead(previous[-1]):
                return ""
            lead = previous.pop()
            if not previous:
                paragraphs_out.pop()
            return lead
    return ""


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
