"""A reply's sentences, each with its own marks, as the voice finishes
writing them.

The voice writes tagged text ("... [[world.type.slug]]." with the tag before
the sentence's full stop). The reply a participant keeps is
`grounding_net.strip_tags` of that raw text, and its marks come from
`apply_net`'s per-sentence verdicts and the transparency plan's
`ElementBuilder`. This module runs those same steps on each sentence the
moment the next one begins: the same paragraph-then-sentence split
`check_turn_with_paragraph_coverage` uses, the same `verdict_for_sentence`,
the same `ElementBuilder`, and the same offset search as the plan's
`_sentence_spans`. A streamed sentence's index, text, offsets and quote and
story marks are therefore the ones the finished plan gives it.

The last, still-open sentence is held back: more text may extend it, and a
tag may be half written at the end of the buffer. Term and figure marks, the
mark cap, and anything citation attachment adds arrive with the finished
plan, which is authoritative; a mark the cap demotes moves to the reference
line. Nothing here changes the text, and no streamed sentence is ever taken
back.
"""
from engine.m4.citation_cards import resolve_source_card
from engine.m4.grounding_net import (
    WITHHOLD_FLOOR,
    build_figure_lexicon,
    parse_tagged,
    split_into_paragraphs,
    strip_tags,
    verdict_for_sentence,
)
from engine.m4.transparency_plan import ElementBuilder


class SentenceStream:
    def __init__(self, *, repository_records: dict[str, dict], world_key: str, thin_topics: list[dict] | None = None):
        self._records = repository_records
        self._world_key = world_key
        self._thin_topics = thin_topics
        self._figures = build_figure_lexicon(repository_records)
        self._builder = ElementBuilder(repository_records=repository_records, world_key=world_key)
        self._buffer = ""
        self._released = 0
        self._cursor = 0
        self._placed: set[int] = set()

    def _card(self, record_id: str) -> dict | None:
        card = resolve_source_card(record_id, self._records)
        if card is None:
            return None
        return {**card, "world_key": self._world_key, "confidence": (self._records.get(record_id) or {}).get("confidence")}

    def feed(self, chunk: str) -> list[dict]:
        """Add one chunk of raw model text. Returns one event per sentence
        that completed: {index, lead, text, text_start, text_end, elements,
        cards}. `lead` is the display text between the previous sentence and
        this one (a space, or a paragraph break); text_start and text_end are
        offsets in the finished reply, or None when the sentence cannot be
        placed, as the plan would give it."""
        self._buffer += chunk
        sentences = [s for paragraph in split_into_paragraphs(self._buffer) for s in parse_tagged(paragraph)]
        complete = sentences[:-1]
        if len(complete) <= self._released:
            return []
        shown = strip_tags(self._buffer)
        events = []
        for index in range(self._released, len(complete)):
            sentence = complete[index]
            verdict = verdict_for_sentence(
                sentence["text"], sentence["tags"], repository_records=self._records, figure_names=self._figures,
                thin_topics=self._thin_topics, grounding_floor=WITHHOLD_FLOOR,
            )
            position = shown.find(sentence["text"], self._cursor) if sentence["text"] else -1
            if position < 0:
                lead, text_start, text_end = "", None, None
            else:
                lead, text_start, text_end = shown[self._cursor:position], position, position + len(sentence["text"])
                self._cursor = text_end
                self._placed.add(index)
            completed = self._builder.add_sentence(
                index=index, sentence=sentence["text"], tags=sentence["tags"], verdict=verdict["verdict"],
            )
            elements = [e for e in completed if e["sentence_index"] in self._placed]
            cards = [c for c in (self._card(rid) for rid in dict.fromkeys(e["record_id"] for e in elements)) if c]
            events.append({"index": index, "lead": lead, "text": sentence["text"], "text_start": text_start,
                           "text_end": text_end, "elements": elements, "cards": cards})
        self._released = len(complete)
        return events
