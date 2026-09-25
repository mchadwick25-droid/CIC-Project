"""Hermetic (no live model call) tests for engine.m4.streaming - Stage 7b's
own engine-side sentence-buffered streaming module. Synthetic records,
same discipline as test_grounding_net.py's own REPOSITORY: not tied to a
compiled package on disk.

FakeStreamingClient below mirrors test_turn.py's own FakeBedrockClient
shape for `client.messages.stream(...)` (a context manager whose
`text_stream` is an iterable of chunks) - the same fake shape, scoped
down to only what this module's own tests need.
"""
from types import SimpleNamespace

import pytest
from anthropic import APIError, APITimeoutError

from engine.m4.grounding_net import build_figure_lexicon, check_turn
from engine.m4.streaming import stream_voice_turn_sentences
from engine.m4.transparency_plan import ElementBuilder

TERM_RECORD = {
    "id": "fix.term.eucharistia",
    "record_type": "term",
    "plain_meaning": "The thanksgiving meal of bread and cup at the heart of the community's worship.",
}
WITNESS_RECORD = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "text": "We did not claim to have seen him ourselves. We claimed only that the ones who told us could not be talked out of what they had seen.",
}
QUOTE_RECORD = {
    "id": "fix.quote.new-song",
    "record_type": "quote",
    "text": "Behold the might of the new song! It has made men out of stones, men out of beasts.",
}
STORY_RECORD = {
    "id": "fix.story.the-gathering",
    "record_type": "story",
    "text": "They gathered in an upper room, broke bread together, and remembered him as he asked.",
}
REPOSITORY = {r["id"]: r for r in (TERM_RECORD, WITNESS_RECORD, QUOTE_RECORD, STORY_RECORD)}


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=None))

    def __exit__(self, *exc):
        return False


class _FakeMessages:
    def __init__(self, stream_scripts):
        # One chunk-list per call, popped in order - the second script
        # is what a corrected regeneration returns.
        self._scripts = list(stream_scripts)
        self.calls = []

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        self.calls.append({"model": model, "system": system, "messages": messages})
        return _FakeStreamCtx(self._scripts.pop(0))


class FakeStreamingClient:
    def __init__(self, *stream_scripts):
        self.messages = _FakeMessages(stream_scripts)


class _RaisingMessages:
    def __init__(self, exc):
        self._exc = exc

    def stream(self, **kwargs):
        raise self._exc


class RaisingClient:
    def __init__(self, exc):
        self.messages = _RaisingMessages(exc)


def _run(client, **kwargs):
    kwargs.setdefault("repository_records", REPOSITORY)
    kwargs.setdefault("world_key", "fix")
    return list(stream_voice_turn_sentences(client, "test-model", **kwargs))


def _sentence_events(events):
    return [e for e in events if e["type"] == "sentence"]


def _done(events):
    return next(e for e in events if e["type"] == "done")


def test_basic_multi_sentence_streaming_no_guard():
    text = "The thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]]. The community's own worship centered on that meal [[fix.term.eucharistia]]."
    client = FakeStreamingClient([text])
    events = _run(client, system_prompt="sys", message="msg")
    sentences = _sentence_events(events)
    assert [s["text"] for s in sentences] == [
        "The thanksgiving meal of bread and cup at the heart of the community's worship.",
        "The community's own worship centered on that meal.",
    ]
    assert all(s["tags"] == ["fix.term.eucharistia"] for s in sentences)
    done = _done(events)
    assert done["citations"] == [
        {"sentence": s["text"], "record_ids": ["fix.term.eucharistia"]} for s in sentences
    ]


def test_streaming_works_when_chunks_split_mid_word_or_mid_tag():
    # The model's own tokens rarely align with sentence or tag
    # boundaries - split the same text into small, arbitrary pieces.
    text = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. We only claimed that those who told us could not be talked out of what they had seen [[fix.witness.who-is-jesus]]."
    chunks = [text[i : i + 7] for i in range(0, len(text), 7)]
    client = FakeStreamingClient(chunks)
    events = _run(client, system_prompt="sys", message="msg")
    sentences = _sentence_events(events)
    assert [s["text"] for s in sentences] == [
        "We did not claim to have seen him ourselves.",
        "We only claimed that those who told us could not be talked out of what they had seen.",
    ]


def test_ungrounded_sentence_is_silently_dropped_not_emitted():
    # Fabricated claim (Live-Generation Design's own calibration case
    # shape): tagged, but shares no ground with its own record.
    text = "The community held three separate meals under armed guard every week [[fix.term.eucharistia]]. The thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]]."
    client = FakeStreamingClient([text])
    events = _run(client, system_prompt="sys", message="msg")
    sentences = _sentence_events(events)
    # Only the second, grounded sentence streams - the first (verdict
    # "withhold") never reaches a "sentence" event at all, per this
    # module's own stricter-than-whole-turn bar.
    assert len(sentences) == 1
    assert sentences[0]["text"] == "The thanksgiving meal of bread and cup at the heart of the community's worship."
    done = _done(events)
    assert "armed guard" not in done["answer_text"]


def test_quote_verbatim_span_survives_a_mid_quote_chunk_boundary():
    text = 'He wrote, "Behold the might of the new song! It has made men out of stones, men out of beasts." [[fix.quote.new-song]]'
    # Split right in the middle of the quoted exclamation - the naive
    # splitter alone would end a sentence at "song!"; quote_aware_sentences
    # must keep it one sentence, matching grounding_net's own check_turn.
    chunks = [text[:40], text[40:]]
    client = FakeStreamingClient(chunks)
    events = _run(client, system_prompt="sys", message="msg")
    sentences = _sentence_events(events)
    assert len(sentences) == 1
    assert "stones, men out of beasts" in sentences[0]["text"]


def test_story_element_finalizes_on_done_via_trailing_elements():
    text = "They gathered in an upper room [[fix.story.the-gathering]]. They broke bread together [[fix.story.the-gathering]]."
    client = FakeStreamingClient([text])
    events = _run(client, system_prompt="sys", message="msg")
    done = _done(events)
    # A contiguous story run is ONE element, placed at the end of the
    # run - here the run never ends before the stream does, so it can
    # only finalize via ElementBuilder.finish() on "done", never as part
    # of either "sentence" event's own elements list.
    assert all(not s["elements"] for s in _sentence_events(events))
    assert len(done["trailing_elements"]) == 1
    assert done["trailing_elements"][0]["record_id"] == "fix.story.the-gathering"
    assert done["trailing_elements"][0]["kind"] == "story"


def test_opening_guard_violation_triggers_one_retry_then_streams_the_correction():
    labels = ["The Facilitator", "Theon (Desert Monasticism)"]
    bad = "The Facilitator: that is not for me to answer. We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."
    good = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."
    client = FakeStreamingClient([bad], [good])
    events = _run(client, system_prompt="sys", message="msg", guard_labels=labels, opening_sentence_count=1)
    types = [e["type"] for e in events]
    assert types == ["opening_guard_retry", "sentence", "done"]
    sentences = _sentence_events(events)
    assert sentences[0]["text"] == "We did not claim to have seen him ourselves."
    # The retry's own directive names the exact offending prefix, the
    # same correction-channel shape engine.m4.turn's own seat-identity
    # correction uses.
    retry_system = client.messages.calls[1]["system"]
    assert any("The Facilitator:" in block["text"] for block in retry_system)


def test_opening_guard_exhausted_after_two_failures_emits_no_sentence_at_all():
    labels = ["The Facilitator"]
    bad = "The Facilitator: that is not for me to answer."
    client = FakeStreamingClient([bad], [bad])
    events = _run(client, system_prompt="sys", message="msg", guard_labels=labels, opening_sentence_count=1)
    assert [e["type"] for e in events] == ["opening_guard_retry", "opening_guard_exhausted"]
    assert _sentence_events(events) == []


def test_short_single_sentence_answer_still_gets_opening_checked():
    # Regression: a stream short enough that _split_ready never finalizes
    # ANY sentence mid-stream (the whole answer sits in the trailing
    # buffer until the stream itself ends) must still be guard-checked -
    # the opening hold cannot depend on a second sentence existing.
    labels = ["The Facilitator"]
    bad = "The Facilitator: not for me to answer."
    client = FakeStreamingClient([bad], ["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."])
    events = _run(client, system_prompt="sys", message="msg", guard_labels=labels, opening_sentence_count=1)
    assert events[0]["type"] == "opening_guard_retry"
    sentences = _sentence_events(events)
    assert len(sentences) == 1
    assert sentences[0]["text"] == "We did not claim to have seen him ourselves."


def test_guard_labels_none_skips_the_opening_hold_entirely():
    # Every interview call passes no guard_labels - the first sentence
    # streams as soon as it clears grounding, no hold, no retry ever
    # possible (there is nothing to check against).
    text = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."
    client = FakeStreamingClient([text])
    events = _run(client, system_prompt="sys", message="msg", guard_labels=None)
    assert events[0]["type"] == "sentence"
    assert len(client.messages.calls) == 1


def test_timeout_yields_error_event_not_an_exception():
    client = RaisingClient(APITimeoutError("timed out"))
    events = _run(client, system_prompt="sys", message="msg")
    assert events == [{"type": "error", "status": "timeout"}]


def test_api_error_yields_error_event_not_an_exception():
    client = RaisingClient(APIError("boom", request=SimpleNamespace(), body=None))
    events = _run(client, system_prompt="sys", message="msg")
    assert events[0]["type"] == "error"
    assert events[0]["status"] == "error"


# ---- stream/turn parity - the pre-7b guarantee (Decision-Log.md) --------


@pytest.mark.parametrize(
    "text",
    [
        "The thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]]. Nothing else mattered as much [[fix.term.eucharistia]].",
        "The community held three separate meals under armed guard every week [[fix.term.eucharistia]]. The thanksgiving meal of bread and cup at the heart of the community's worship [[fix.term.eucharistia]].",
        'He wrote, "Behold the might of the new song! It has made men out of stones, men out of beasts." [[fix.quote.new-song]] We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]].',
        "They gathered in an upper room [[fix.story.the-gathering]]. They broke bread together [[fix.story.the-gathering]]. We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]].",
    ],
)
def test_stream_turn_parity_same_text_same_elements_and_citations(text):
    """The whole-turn path (check_turn + a single, whole-answer
    ElementBuilder pass, exactly as build_transparency_plan does) and
    this module's own sentence-by-sentence streaming must produce the
    same participant-facing sentences, the same citations, and the same
    inline elements for identical input text - engine.m4.transparency_
    plan.ElementBuilder's own docstring names this as the whole point of
    its add-only, one-sentence-at-a-time API."""
    # Whole-turn side: check_turn's own verdicts, fed sentence by
    # sentence into a fresh ElementBuilder exactly as
    # build_transparency_plan does.
    whole_turn_result = check_turn(text, REPOSITORY)
    whole_builder = ElementBuilder(repository_records=REPOSITORY, world_key="fix")
    whole_elements = []
    whole_sentences = []
    for i, sent in enumerate(whole_turn_result["sentences"]):
        whole_elements += whole_builder.add_sentence(index=i, sentence=sent["sentence"], tags=sent["tags"], verdict=sent["verdict"])
        if sent["verdict"] == "ok":
            whole_sentences.append(sent["sentence"])
    whole_elements += whole_builder.finish()
    whole_citations = [
        {"sentence": s["sentence"], "record_ids": s["tags"]}
        for s in whole_turn_result["sentences"] if s["verdict"] == "ok" and s["tags"]
    ]

    # Streaming side: the same text, fed through the model-stream fake
    # as one single chunk (chunking granularity is proven not to matter
    # by the other tests above).
    client = FakeStreamingClient([text])
    events = _run(client, system_prompt="sys", message="msg")
    streamed_sentences = [s["text"] for s in _sentence_events(events)]
    streamed_elements = [el for s in _sentence_events(events) for el in s["elements"]] + _done(events)["trailing_elements"]

    assert streamed_sentences == whole_sentences
    assert _done(events)["citations"] == whole_citations
    assert streamed_elements == whole_elements
