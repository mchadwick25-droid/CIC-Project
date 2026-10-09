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
tag may be half written at the end of the buffer. On a Table turn a guard
(the seat-identity check) reads each sentence before it is released; the
first sentence it catches is never released, and nothing after it either. Term and figure marks, the
mark cap, and anything citation attachment adds arrive with the finished
plan, which is authoritative; a mark the cap demotes moves to the reference
line. A sentence whose quotation marks the net took off is released with
them off, and offsets count the text as the finished reply has it.

apply_net may change or remove a sentence after the fact: it places a quote
marker (taking the sentence before a marker that stands alone as its
lead-in), scrubs markdown, drops a retold story, and drops words attributed
without a placed quote, with the sentence that introduced them or the
sentences after them. So the last finished sentence is always held back
until the next one finishes, and the first sentence any of that could touch
(_reshaped) stops the stream: neither it, nor the sentence before it, nor
anything after it is released; they arrive with the finished reply. A sentence that touches a run of demonstration words
(engine.m4.recitation) is held back while the run may still grow into a
recitation, so a recited reply can be regenerated before any of it is shown;
with demonstrations in play nothing is released before the finished
sentences reach the recitation length, so a recitation that begins in the
reply's first words is caught before any of it shows.
No streamed sentence is ever taken back.
"""
from engine.m4.citation_cards import resolve_source_card
from engine.m4.grounding_net import (
    QUOTATION_DROP_REASONS,
    QUOTE_MARKER,
    WITHHOLD_FLOOR,
    QuotationIndex,
    build_figure_lexicon,
    parse_tagged,
    split_into_paragraphs,
    strip_markdown,
    strip_tags,
    verdict_for_sentence,
)
from engine.m4.recitation import RECITATION_WORDS, DemonstrationIndex, reply_words
from engine.m4.transparency_plan import ElementBuilder


def _sentences(raw: str) -> list[dict]:
    return [s for paragraph in split_into_paragraphs(raw) for s in parse_tagged(paragraph)]


class SentenceStream:
    def __init__(self, *, repository_records: dict[str, dict], world_key: str, thin_topics: list[dict] | None = None,
                 guard=None, demonstrations: DemonstrationIndex | None = None,
                 quotable_texts: list[str] | None = None, told_stories: frozenset[str] = frozenset(),
                 voiced_quotes: frozenset[str] = frozenset()):
        self._guard = guard
        self._told_stories = told_stories
        self._demonstrations = demonstrations or DemonstrationIndex(repository_records)
        self._quotation_index = QuotationIndex(repository_records, quotable_texts, voiced=voiced_quotes)
        self._shift = 0
        self._stopped = False
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
        that completed: {index, speaker, lead, text, text_start, text_end,
        elements, cards}. `speaker` is the world key of the voice speaking;
        `lead` is the display text between the previous sentence and this
        one (a space, or a paragraph break); text_start and text_end are
        offsets in the finished reply, or None when the sentence cannot be
        placed, as the plan would give it."""
        self._buffer += chunk
        if self._stopped:
            return []
        finished = _sentences(self._buffer)[:-1]
        complete = finished[:-1]
        if len(complete) <= self._released:
            return []
        shown = strip_tags(self._buffer)
        hold_from = self._hold_from(finished)
        events = []
        for index in range(self._released, len(complete)):
            if hold_from is not None and index >= hold_from:
                break
            sentence = complete[index]
            if self._guard is not None and self._guard(sentence["raw"]):
                self._stopped = True
                break
            verdict = verdict_for_sentence(
                sentence["text"], sentence["tags"], repository_records=self._records, figure_names=self._figures,
                thin_topics=self._thin_topics, grounding_floor=WITHHOLD_FLOOR, quotation_index=self._quotation_index,
            )
            if self._reshaped(sentence, verdict) or self._reshaped(finished[index + 1], None):
                self._stopped = True
                break
            source = sentence["text"]
            text = verdict["sentence"] if "source_sentence" in verdict else source
            position = shown.find(source, self._cursor) if source else -1
            if position < 0:
                lead, text_start, text_end = "", None, None
            else:
                text_start = position - self._shift
                lead, text_end = shown[self._cursor:position], text_start + len(text)
                self._cursor = position + len(source)
                self._shift += len(source) - len(text)
                self._placed.add(index)
            completed = self._builder.add_sentence(
                index=index, sentence=text, tags=sentence["tags"], verdict=verdict["verdict"],
            )
            elements = [e for e in completed if e["sentence_index"] in self._placed]
            cards = [c for c in (self._card(rid) for rid in dict.fromkeys(e["record_id"] for e in elements)) if c]
            events.append({"index": index, "speaker": self._world_key, "lead": lead, "text": text, "text_start": text_start,
                           "text_end": text_end, "elements": elements, "cards": cards})
            self._released = index + 1
        return events

    def _reshaped(self, sentence: dict, verdict: dict | None) -> bool:
        """apply_net could change or remove this sentence, or (for the one
        after a sentence about to be released) the sentence before it."""
        raw = sentence["raw"]
        if QUOTE_MARKER.search(raw) or strip_markdown(raw) != raw.strip():
            return True
        if any(tag in self._told_stories for tag in sentence["tags"]):
            return True
        if verdict is None:
            verdict = verdict_for_sentence(
                sentence["text"], sentence["tags"], repository_records=self._records, figure_names=self._figures,
                thin_topics=self._thin_topics, grounding_floor=WITHHOLD_FLOOR, quotation_index=self._quotation_index,
            )
        return bool(verdict.get("opens_quote") or verdict.get("stands_alone") or verdict.get("why") in QUOTATION_DROP_REASONS)

    def _hold_from(self, complete: list[dict]) -> int | None:
        """The index of the first sentence to keep back: the one holding the
        first word of a run of demonstration words that is, or may still
        become, a recitation."""
        counts = [len(reply_words(sentence["text"])) for sentence in complete]
        words = [w for sentence in complete for w in reply_words(sentence["text"])]
        if not self._demonstrations.empty and len(words) < RECITATION_WORDS:
            return 0
        start = self._demonstrations.hold_start(words)
        if start is None:
            return None
        total = 0
        for index, count in enumerate(counts):
            total += count
            if start < total:
                return index
        return None

    @property
    def released(self) -> int:
        return self._released

    def cut(self, raw_text: str) -> str | None:
        """When sentences have been released and the guard catches a later
        sentence of the finished raw text (including the last one, never
        released while open), the raw text up to that sentence; otherwise
        None. Everything kept has already been shown."""
        if not self._released or self._guard is None:
            return None
        sentences = _sentences(raw_text)
        caught = next((i for i in range(self._released, len(sentences)) if self._guard(sentences[i]["raw"])), None)
        if caught is None:
            return None
        cursor = 0
        for sentence in sentences[:caught + 1]:
            start = raw_text.find(sentence["raw"], cursor)
            cursor = start + len(sentence["raw"])
        return raw_text[:start].rstrip()
