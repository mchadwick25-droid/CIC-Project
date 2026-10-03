"""Hermetic tests for engine.m4.draft_stream.DraftStream: a draft is always a
true prefix of the finished reply, tags never show, and the open sentence is
held back."""
import pytest

from engine.m4.draft_stream import DraftStream
from engine.m4.grounding_net import strip_tags
from engine.m4.turn import _draft_is_final_text

RAW = (
    "We kept the bread together [[alx.dw.bread]]. He taught that grace comes first [[alx.dw.grace]]!\n\n"
    "Some of us disagreed [[alx.limit.dissent]]. That is what we remember."
)


def _chunked(text, size):
    return [text[i : i + size] for i in range(0, len(text), size)]


def _drafted(chunks):
    stream = DraftStream()
    return "".join(stream.feed(c) for c in chunks)


@pytest.mark.parametrize("size", [1, 2, 3, 5, 7, 11, 1000])
def test_a_draft_is_a_prefix_of_the_finished_reply_whatever_the_chunking(size):
    drafted = _drafted(_chunked(RAW, size))
    finished = strip_tags(RAW)
    assert finished.startswith(drafted)
    assert "[[" not in drafted


@pytest.mark.parametrize("size", [1, 4, 9])
def test_the_open_last_sentence_is_never_shown(size):
    drafted = _drafted(_chunked(RAW, size))
    assert "That is what we remember" not in drafted
    assert "Some of us disagreed" in drafted


def test_a_sentence_is_shown_once_the_next_one_begins():
    stream = DraftStream()
    assert stream.feed("We kept the bread together [[alx.dw.bread]].") == ""
    assert stream.feed(" He") == "We kept the bread together. "


def test_a_half_written_tag_is_never_shown():
    stream = DraftStream()
    stream.feed("We kept the bread together [[alx.dw.bre")
    assert "[[" not in stream.feed("ad]]. He taught")


def test_paragraph_breaks_survive_into_the_draft():
    drafted = _drafted(_chunked(RAW, 6))
    assert "\n\n" in drafted


def test_a_quotation_is_not_cut_at_a_full_stop_inside_it():
    raw = 'He said: "Behold the new song! It has made men new [[alx.q.song]]." Then he sat. And more.'
    drafted = _drafted(_chunked(raw, 4))
    assert strip_tags(raw).startswith(drafted)
    assert "It has made men new" in drafted


def test_nothing_is_shown_before_a_sentence_completes():
    assert DraftStream().feed("Grace comes") == ""


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
def test_a_draft_is_offered_only_when_the_first_attempt_is_the_reply(kwargs, expected):
    base = dict(guard_labels=None, is_other_tradition_first_ask=False, self_revision_enabled=True, r27_enforce=False, sentence_enforce=False)
    base.update(kwargs)
    assert _draft_is_final_text(**base) is expected
