"""Hermetic tests for engine.m4.sentence_stream.SentenceStream: each streamed
sentence carries the index, offsets and quote and story marks the finished
plan gives it, tags never show, and the open sentence is held back."""
import pytest

from engine.m4.grounding_net import strip_tags
from engine.m4.sentence_stream import SentenceStream
from engine.m4.transparency_plan import build_transparency_plan
from engine.m4.turn import _draft_is_final_text, apply_net

RECORDS = {
    "w.dw.bread": {"id": "w.dw.bread", "record_type": "doctrinal_witness", "text": "We kept the bread together each week."},
    "w.story.road": {"id": "w.story.road", "record_type": "story", "tellable_as": "Two walked the road to Emmaus and knew him in the bread."},
    "w.quote.song": {"id": "w.quote.song", "record_type": "quote", "text": "Behold the new song", "modern_rendering": "Look, the new song"},
}
RAW = (
    "We kept the bread together each week [[w.dw.bread]]. Two walked the road to Emmaus [[w.story.road]]. "
    "They knew him in the bread [[w.story.road]]!\n\n"
    'Our teacher sang of "the new song" [[w.quote.song]]. That is what we remember. We hold it still.'
)


def _chunked(text, size):
    return [text[i : i + size] for i in range(0, len(text), size)]


def _streamed(chunks):
    stream = SentenceStream(repository_records=RECORDS, world_key="w")
    return [event for chunk in chunks for event in stream.feed(chunk)]


def _plan(raw):
    text, citations, net = apply_net(raw, repository_records=RECORDS, thin_topics=None)
    return text, build_transparency_plan(citations=citations, net_result=net, repository_records=RECORDS, world_key="w", text=text)


@pytest.mark.parametrize("size", [1, 2, 3, 5, 7, 11, 1000])
def test_streamed_sentences_match_the_finished_plan_whatever_the_chunking(size):
    events = _streamed(_chunked(RAW, size))
    text, plan = _plan(RAW)
    assert [e["index"] for e in events] == list(range(len(events)))
    for e in events:
        assert plan["sentences"][e["index"]] == {"index": e["index"], "text_start": e["text_start"], "text_end": e["text_end"]}
        assert text[e["text_start"]:e["text_end"]] == e["text"]
    streamed_elements = [el for e in events for el in e["elements"]]
    assert streamed_elements == [el for el in plan["elements"] if el["sentence_index"] < len(events)]


@pytest.mark.parametrize("size", [1, 4, 9])
def test_leads_and_texts_rebuild_a_prefix_of_the_reply_with_its_paragraph_breaks(size):
    shown = "".join(e["lead"] + e["text"] for e in _streamed(_chunked(RAW, size)))
    assert strip_tags(RAW).startswith(shown)
    assert "\n\n" in shown and "[[" not in shown


def test_the_open_last_sentence_and_the_one_before_it_are_never_released():
    texts = [e["text"] for e in _streamed(_chunked(RAW, 4))]
    assert "We hold it still." not in texts
    assert "That is what we remember." not in texts
    assert 'Our teacher sang of "the new song".' in texts


def test_a_story_mark_arrives_when_its_telling_ends():
    events = _streamed(_chunked(RAW, 3))
    story = [(e["index"], el) for e in events for el in e["elements"] if el["kind"] == "story"]
    assert [(at, el["sentence_index"]) for at, el in story] == [(3, 2)]
    assert any(c["record_id"] == "w.story.road" for c in events[3]["cards"])


def test_a_quote_mark_arrives_with_its_own_sentence_and_its_card():
    events = _streamed(_chunked(RAW, 5))
    quote = next(e for e in events if any(el["kind"] == "quote" for el in e["elements"]))
    assert quote["index"] == 3 and [c["record_id"] for c in quote["cards"]] == ["w.story.road", "w.quote.song"]


def test_a_half_written_tag_is_never_released():
    stream = SentenceStream(repository_records=RECORDS, world_key="w")
    assert stream.feed("We kept the bread together each week [[w.dw.bre") == []
    assert stream.feed("ad]]. Two walked") == []
    events = stream.feed(" the road to Emmaus [[w.story.road]]. They")
    assert [e["text"] for e in events] == ["We kept the bread together each week."]


def test_nothing_is_released_before_a_sentence_completes():
    assert SentenceStream(repository_records=RECORDS, world_key="w").feed("Grace comes") == []


@pytest.mark.parametrize(
    "kwargs, expected",
    [
        ({}, True),
        ({"is_other_tradition_first_ask": True}, False),
        ({"is_other_tradition_first_ask": True, "self_revision_enabled": False}, True),
        ({"r27_enforce": True}, False),
        ({"sentence_enforce": True}, False),
    ],
)
def test_sentences_are_streamed_only_when_the_first_attempt_is_the_reply(kwargs, expected):
    base = dict(is_other_tradition_first_ask=False, self_revision_enabled=True, r27_enforce=False, sentence_enforce=False)
    base.update(kwargs)
    assert _draft_is_final_text(**base) is expected


def _guarded():
    from engine.m4.seat_identity_guard import find_seat_identity_violation
    return SentenceStream(repository_records=RECORDS, world_key="w",
                          guard=lambda raw: find_seat_identity_violation(raw, ["Hilary", "Facilitator"]))


def test_a_guarded_stream_never_releases_the_caught_sentence_or_anything_after():
    raw = "We kept the bread together each week [[w.dw.bread]]. Hilary: and I would add more. Then we sat down."
    stream = _guarded()
    events = [e for chunk in _chunked(raw, 4) for e in stream.feed(chunk)]
    assert [e["text"] for e in events] == ["We kept the bread together each week."]
    assert stream.cut(raw) == "We kept the bread together each week [[w.dw.bread]]."


def test_a_catch_in_the_first_sentence_releases_nothing_and_leaves_regeneration_to_the_turn():
    raw = "Hilary: we would say otherwise. Then we sat down. And more."
    stream = _guarded()
    assert [e for chunk in _chunked(raw, 5) for e in stream.feed(chunk)] == []
    assert stream.released == 0 and stream.cut(raw) is None


def test_a_catch_in_the_last_sentence_is_found_when_the_reply_ends():
    raw = "We kept the bread together each week [[w.dw.bread]]. Two walked the road to Emmaus [[w.story.road]]. Facilitator: that is all."
    stream = _guarded()
    events = [e for chunk in _chunked(raw, 6) for e in stream.feed(chunk)]
    assert len(events) == 1
    assert stream.cut(raw).endswith("Two walked the road to Emmaus [[w.story.road]].")


def test_a_clean_guarded_reply_is_not_cut():
    stream = _guarded()
    for chunk in _chunked(RAW, 7):
        stream.feed(chunk)
    assert stream.cut(RAW) is None


UNQUOTED_RAW = (
    "We kept the bread together each week [[w.dw.bread]]. "
    'Our teacher sang of "nobody\'s song" [[w.quote.song]]. '
    'He also sang of "the new song" [[w.quote.song]]. That is what we remember.'
)


@pytest.mark.parametrize("size", [1, 3, 8, 1000])
def test_a_sentence_whose_marks_came_off_streams_with_them_off_and_the_offsets_of_the_finished_reply(size):
    events = _streamed(_chunked(UNQUOTED_RAW, size))
    text, plan = _plan(UNQUOTED_RAW)
    assert '"nobody' not in text and "nobody's song" in text
    assert [e["text"] for e in events][1] == "Our teacher sang of nobody's song."
    for e in events:
        assert plan["sentences"][e["index"]] == {"index": e["index"], "text_start": e["text_start"], "text_end": e["text_end"]}
        assert text[e["text_start"]:e["text_end"]] == e["text"]


def test_apply_net_withholds_a_sentence_whose_marks_came_off_and_gives_it_no_citation():
    text, citations, net = apply_net(UNQUOTED_RAW, repository_records=RECORDS, thin_topics=None)
    assert text.startswith('We kept the bread together each week. Our teacher sang of nobody\'s song. He also sang of "the new song"')
    assert [c["sentence"] for c in citations] == [
        "We kept the bread together each week.",
        'He also sang of "the new song".',
    ]
    assert [s["why"] for s in net["sentences"]][1] == "quotation not in records"


@pytest.mark.parametrize("later", [
    "Our teacher put it plainly [[quote:w.quote.song]].",
    'Our teacher wrote, "a line that no record of ours carries".',
    "Ephrem wrote: the bread was never only bread.",
    "## Sources",
])
def test_the_stream_stops_before_a_sentence_the_finished_reply_may_reshape_and_holds_the_one_before_it(later):
    raw = (
        "We kept the bread together each week [[w.dw.bread]]. Two walked the road to Emmaus [[w.story.road]]. "
        f"{later} That is what we remember. We hold it still."
    )
    texts = [e["text"] for e in _streamed(_chunked(raw, 5))]
    assert texts == ["We kept the bread together each week."]


def test_a_retold_story_stops_the_stream():
    stream = SentenceStream(repository_records=RECORDS, world_key="w", told_stories=frozenset({"w.story.road"}))
    raw = "We kept the bread together each week [[w.dw.bread]]. Two walked the road to Emmaus [[w.story.road]]. Then more. And more."
    assert [e["text"] for chunk in _chunked(raw, 5) for e in stream.feed(chunk)] == []
