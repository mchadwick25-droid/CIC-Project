from engine.m9.cli import _complement_verbatim, _perspective_spans, _window_match
from engine.m9.shelf import Shelf


def _shelf() -> Shelf:
    return Shelf(
        world_key="w",
        census_id="w",
        rows={},
        files={"trad.txt": ["trad-row"]},
        units={"trad.txt": "words that live on this world's own shelf and nowhere else"},
        pairs={},
        parties={},
        vendored_files=frozenset({"trad.txt", "elsewhere.txt", "another.txt"}),
    )


def test_perspective_spans_finds_quoted_text_in_scoped_fields():
    records = {
        "s1": {"id": "s1", "record_type": "story", "tellable_as": 'She said, "a phrase worth checking here" to the crowd.'},
        "s2": {"id": "s2", "record_type": "world_core", "body": 'Not scoped: "should never be picked up" at all.'},
    }
    spans = _perspective_spans(records)
    assert ("s1", "tellable_as", "a phrase worth checking here") in spans
    assert not any(rid == "s2" for rid, _field, _span in spans)


def test_perspective_spans_includes_representative_demonstration_turns_only():
    records = {
        "d1": {
            "id": "d1",
            "record_type": "demonstration",
            "exchange": [
                {"speaker": "facilitator", "text": '"never picked up, wrong speaker"'},
                {"speaker": "representative", "text": '"picked up, a quoted representative span"'},
            ],
        }
    }
    spans = _perspective_spans(records)
    assert ("d1", "exchange[1].text", "picked up, a quoted representative span") in spans
    assert not any(field == "exchange[0].text" for _rid, field, _span in spans)


def test_window_match_true_on_substring_six_word_window():
    assert _window_match("the exact hidden words of leakage", ["normalized haystack the exact hidden words of leakage right here"])


def test_window_match_false_when_absent():
    assert not _window_match("words never present anywhere", ["completely unrelated haystack text"])


def test_complement_verbatim_silent_when_span_only_matches_own_shelf():
    records = {
        "s1": {"id": "s1", "record_type": "story", "tellable_as": 'It says, "words that live on this world own shelf" plainly.'},
    }
    complement_units = {"elsewhere.txt": "words that live on this world own shelf and in the complement too"}
    hits = _complement_verbatim(records, _shelf(), complement_units)
    assert hits == []


def test_complement_verbatim_fires_when_span_only_in_complement():
    records = {
        "s1": {"id": "s1", "record_type": "story", "tellable_as": 'It says, "a phrase found only off this shelf" plainly.'},
    }
    complement_units = {"elsewhere.txt": "a phrase found only off this shelf and nowhere on our own"}
    hits = _complement_verbatim(records, _shelf(), complement_units)
    assert len(hits) == 1
    assert hits[0]["record"] == "s1"
    assert hits[0]["field"] == "tellable_as"
    assert hits[0]["span"] == "a phrase found only off this shelf"


def test_complement_verbatim_silent_when_no_complement_files():
    records = {
        "s1": {"id": "s1", "record_type": "story", "tellable_as": 'It says, "anything at all here" plainly.'},
    }
    assert _complement_verbatim(records, _shelf(), {}) == []
