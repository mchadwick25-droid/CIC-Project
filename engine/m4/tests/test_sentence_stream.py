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
    'Our teacher said: "Look, the new song" [[w.quote.song]]. That is what we remember.'
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


def test_the_open_last_sentence_is_never_released():
    texts = [e["text"] for e in _streamed(_chunked(RAW, 4))]
    assert "That is what we remember." not in texts
    assert 'Our teacher said: "Look, the new song".' in texts


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
    events = stream.feed("ad]]. Two walked")
    assert [e["text"] for e in events] == ["We kept the bread together each week."]


def test_nothing_is_released_before_a_sentence_completes():
    assert SentenceStream(repository_records=RECORDS, world_key="w").feed("Grace comes") == []


@pytest.mark.parametrize(
    "kwargs, expected",
    [
        ({}, True),
        ({"guard_labels": ["Facilitator"]}, False),
        ({"is_other_tradition_first_ask": True}, False),
        ({"is_other_tradition_first_ask": True, "self_revision_enabled": False}, True),
        ({"r27_enforce": True}, False),
        ({"sentence_enforce": True}, False),
    ],
)
def test_sentences_are_streamed_only_when_the_first_attempt_is_the_reply(kwargs, expected):
    base = dict(guard_labels=None, is_other_tradition_first_ask=False, self_revision_enabled=True, r27_enforce=False, sentence_enforce=False)
    base.update(kwargs)
    assert _draft_is_final_text(**base) is expected
