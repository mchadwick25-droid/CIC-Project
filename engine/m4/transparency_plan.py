"""The engine-owned Transparency Plan: one complete, deterministic account
of every record a turn cited and where each one's mark goes, computed
once here instead of reconstructed by the frontend.

**References.** Every `record_id` appearing anywhere in `citations`
appears in `references` exactly once, by construction:
`set(r["record_id"] for r in references) == set(rid for c in citations
for rid in c["record_ids"])` holds for any input (this module's own
completeness-invariant test). A record whose id resolves to nothing in the
repository is skipped here, never crashed on.

**Elements.** One entry per distinct grounded element, each placed at
the element it grounds, never reduced to one mark per sentence:
- `quote` - a cited `quote` record. Its mark follows the quoted words: the
  first quotation in the sentence whose words `grounding_net` verifies
  verbatim in that record. A quote record cited on a sentence that
  quotes none of its words has no quoted words to follow, so its mark
  ends the sentence.
- `story` - a cited `story` record. Its mark sits at the end of its
  telling: the end of the last sentence of a contiguous run of sentences
  citing it. Any sentence that does not cite the story (withheld,
  untagged, or citing something else) ends the run; a later run of the
  same story is a second element with `repeat: true`.
- `term` / `figure` - a lexicon word or a figure's name, from
  `term_glosses`/`name_bridge`, placed on the word itself.
Every other cited record - a `doctrinal_witness`, gravity, force,
contested claim, honest limit, or a term/figure cited without its own
word said - is a general reference: it goes to `end_references`, shown
at the end of the reply, not marked inside it.

Each element: `{record_id, record_type, world_key, confidence, repeat,
kind, sentence_index, char_start, char_end, surface}`. `sentence_index`
indexes `net_result["sentences"]` - the same list `unverified_claims`
indexes, so one reply has one index space. `char_start`/`char_end` are
offsets into that sentence's own tag-stripped text, `surface ==
sentence[char_start:char_end]`, and the mark renders at `char_end`.

**Sentences.** `sentences` gives each net sentence's own span in the
reply's `text` (`{index, text_start, text_end}`), so the frontend places
marks by offset, never by searching the text again. A sentence not found
in `text` gets no span, and elements on it fall back to `end_references`
- disclosed, never dropped.

**Streaming.** `ElementBuilder` is fed one cleared sentence at a time
and only ever adds elements: a quote element
is emitted with its own sentence; a story element is emitted when the
next sentence clears without that story, or at `finish()`. The
whole-turn path below feeds the same builder, so a streamed reply and a
whole reply produce the same elements for the same text.

**Mark cap.** A word mark that overlaps an earlier word mark in the same
sentence is not drawn. Then at most `mark_cap(len(sentences))` elements
stay inline: max(3, min(8, ceil(sentences / 2))). Over the cap, term marks
drop first, then figures, then stories, the latest first within each kind;
quote marks never drop. A dropped element's record moves to
`end_references`: its inline prominence is lost, never its disclosure. The
app applies the same rule (VoiceTurnBody.tsx), so on a capped plan its clamp
changes nothing.

**Confidence.** Each element and reference carries the cited record's
own `confidence` envelope verbatim; this module renders nothing.

**unverified_claims** is a plain count plus which `net_result
["sentences"]` indexes failed verification - for M7's own reporting,
never for a participant.

Additive: stored as `voice_event["transparency"]`, never in
`engine.m4.events.REQUIRED_KEYS["voice_turn"]`; it reads `apply_net`'s
output after the fact and feeds nothing upstream.
"""
from __future__ import annotations

import math

from engine.m4.citation_cards import resolve_source_card
from engine.m4.grounding_net import _span_in_records, quoted_span_positions

INLINE_CITED_KINDS = {"quote": "quote", "story": "story"}
MARK_CAP_FLOOR = 3
MARK_CAP_CEILING = 8
CAP_DROP_ORDER = ("figure", "story")


def mark_cap(sentence_count: int) -> int:
    return max(MARK_CAP_FLOOR, min(MARK_CAP_CEILING, math.ceil(sentence_count / 2)))


def _drawn_within_cap(elements: list[dict], sentence_count: int) -> list[dict]:
    """The elements that render inline: overlapping word marks removed, then
    the cap applied in CAP_DROP_ORDER, latest first. A term (lexicon) mark is
    a connection, never a decoration: it is outside the cap, neither counted
    nor dropped. Quotes are never dropped. `elements` is in plan order."""
    last_word_end: dict[int, int] = {}
    drawn = []
    for element in elements:
        if element["kind"] in ("term", "figure"):
            if element["char_start"] < last_word_end.get(element["sentence_index"], 0):
                continue
            last_word_end[element["sentence_index"]] = element["char_end"]
        drawn.append(element)
    over = sum(1 for e in drawn if e["kind"] != "term") - mark_cap(sentence_count)
    dropped: set[int] = set()
    for kind in CAP_DROP_ORDER:
        for i in reversed([i for i, e in enumerate(drawn) if e["kind"] == kind]):
            if over <= 0:
                break
            dropped.add(i)
            over -= 1
    return [e for i, e in enumerate(drawn) if i not in dropped]


class ElementBuilder:
    """The quote and story elements of one reply, built sentence by
    sentence, add-only: `add_sentence` returns the elements that sentence
    completes, `finish` returns whatever the turn's end completes. Nothing
    returned is ever changed or withdrawn afterwards."""

    def __init__(self, *, repository_records: dict[str, dict], world_key: str):
        self._records = repository_records
        self._world_key = world_key
        self._counts: dict[str, int] = {}
        self._open_stories: dict[str, dict] = {}

    def _element(self, record_id: str, kind: str, sentence_index: int, sentence: str, char_start: int, char_end: int) -> dict:
        record = self._records.get(record_id) or {}
        seen = self._counts.get(record_id, 0)
        self._counts[record_id] = seen + 1
        return {
            "record_id": record_id,
            "record_type": record.get("record_type"),
            "world_key": self._world_key,
            "confidence": record.get("confidence"),
            "repeat": seen > 0,
            "kind": kind,
            "sentence_index": sentence_index,
            "char_start": char_start,
            "char_end": char_end,
            "surface": sentence[char_start:char_end],
        }

    def _close_story(self, record_id: str) -> dict:
        pending = self._open_stories.pop(record_id)
        return self._element(record_id, "story", pending["index"], pending["sentence"], 0, len(pending["sentence"]))

    def add_sentence(self, *, index: int, sentence: str, tags: list[str], verdict: str) -> list[dict]:
        cited = list(dict.fromkeys(tags)) if verdict == "ok" else []
        completed = [self._close_story(rid) for rid in list(self._open_stories) if rid not in cited]

        spans = quoted_span_positions(sentence)
        for record_id in cited:
            kind = INLINE_CITED_KINDS.get((self._records.get(record_id) or {}).get("record_type"))
            if kind == "story":
                self._open_stories[record_id] = {"index": index, "sentence": sentence}
            elif kind == "quote":
                record = self._records[record_id]
                match = next(((start, end) for start, end, inner in spans if _span_in_records(inner, [record])), None)
                start, end = match if match else (0, len(sentence))
                completed.append(self._element(record_id, "quote", index, sentence, start, end))
        return completed

    def finish(self) -> list[dict]:
        return [self._close_story(rid) for rid in list(self._open_stories)]


def _sentence_spans(text: str, sentences: list[dict]) -> list[dict]:
    spans = []
    cursor = 0
    for index, sentence in enumerate(sentences):
        body = sentence.get("sentence") or ""
        pos = text.find(body, cursor) if body else -1
        if pos < 0:
            spans.append({"index": index, "text_start": None, "text_end": None})
            continue
        spans.append({"index": index, "text_start": pos, "text_end": pos + len(body)})
        cursor = pos + len(body)
    return spans


def _word_elements(word_marks: list[tuple[str, dict]], spans: list[dict], sentences: list[dict], repository_records: dict[str, dict], world_key: str) -> list[dict]:
    elements = []
    for kind, mark in word_marks:
        start = mark.get("text_start")
        if start is None:
            continue
        end = start + len(mark.get("matched_name") or "")
        span = next((s for s in spans if s["text_start"] is not None and s["text_start"] <= start and end <= s["text_end"]), None)
        if span is None:
            continue
        sentence = sentences[span["index"]].get("sentence") or ""
        char_start, char_end = start - span["text_start"], end - span["text_start"]
        record = repository_records.get(mark["id"]) or {}
        elements.append({
            "record_id": mark["id"],
            "record_type": record.get("record_type") or kind,
            "world_key": world_key,
            "confidence": record.get("confidence"),
            "repeat": False,
            "kind": kind,
            "sentence_index": span["index"],
            "char_start": char_start,
            "char_end": char_end,
            "surface": sentence[char_start:char_end],
        })
    return elements


def build_transparency_plan(
    *,
    citations: list[dict],
    net_result: dict,
    repository_records: dict[str, dict],
    world_key: str,
    text: str = "",
    glosses: list[dict] | None = None,
    figures_used: list[dict] | None = None,
) -> dict:
    """citations: engine.m4.turn.apply_net's per-sentence output, already
    carrying resolved `sources`. net_result: apply_net's third return
    value - its `sentences` drive element placement and unverified_claims.
    text: the reply exactly as the participant reads it. glosses /
    figures_used: term_glosses / name_bridge output, each entry carrying
    its own `text_start`. Deterministic: identical input always produces
    identical output."""
    sentences = net_result.get("sentences") or []
    spans = _sentence_spans(text, sentences)

    builder = ElementBuilder(repository_records=repository_records, world_key=world_key)
    elements: list[dict] = []
    for index, sentence in enumerate(sentences):
        elements += builder.add_sentence(
            index=index, sentence=sentence.get("sentence") or "", tags=sentence.get("tags") or [], verdict=sentence.get("verdict"),
        )
    elements += builder.finish()
    word_marks = [("figure", f) for f in figures_used or []] + [("term", g) for g in glosses or []]
    elements += _word_elements(word_marks, spans, sentences, repository_records, world_key)
    elements = [e for e in elements if spans[e["sentence_index"]]["text_start"] is not None]
    elements.sort(key=lambda e: (e["sentence_index"], e["char_end"], e["char_start"]))

    seen_order = list(dict.fromkeys(rid for c in citations for rid in c.get("record_ids") or []))
    references = []
    for record_id in seen_order:
        card = resolve_source_card(record_id, repository_records)
        if card is None:
            continue
        references.append({**card, "world_key": world_key, "confidence": (repository_records.get(record_id) or {}).get("confidence")})
    carded = {card["record_id"] for card in references}
    elements = [e for e in elements if e["kind"] in ("term", "figure") or e["record_id"] in carded]
    elements = _drawn_within_cap(elements, len(sentences))
    inline_ids = {e["record_id"] for e in elements}
    end_references = [card for card in references if card["record_id"] not in inline_ids]

    unverified_sentences = [i for i, s in enumerate(sentences) if s.get("verdict") != "ok"]

    return {
        "world_key": world_key,
        "sentences": spans,
        "elements": elements,
        "references": references,
        "end_references": end_references,
        "unverified_claims": {"count": len(unverified_sentences), "sentence_indexes": unverified_sentences},
    }
