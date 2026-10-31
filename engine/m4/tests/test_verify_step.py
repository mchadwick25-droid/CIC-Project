"""The verify and rewrite step reads each cited sentence against its bound records."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4 import verify_step as vs

LIMIT = "lpc.limit.womens-own-voice"


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


def _answer(*entries, placed=()):
    return {"net_sentences": list(entries), "reply_shape": {"placed": list(placed)}}


def _entry(sentence, tags, verdict="ok", **extra):
    return {"sentence": sentence, "tags": tags, "verdict": verdict, **extra}


def test_a_context_block_or_unknown_id_is_not_a_binding(records):
    assert vs.valid_bindings([f"ctx.{LIMIT}.1", "no.such.record", LIMIT, LIMIT], records) == [LIMIT]


def test_a_sentence_with_no_valid_binding_is_held_out(records):
    items = vs.sentence_items(_answer(_entry("A claim.", ["ctx.x.1"]), _entry("Another.", [LIMIT])), records)
    assert [(i["n"], i["held_out"]) for i in items] == [(0, True), (1, False)]


def test_uncited_withheld_and_placed_sentences_are_not_read(records):
    answer = _answer(
        _entry("Uncited framing.", []), _entry("Withheld.", [LIMIT], verdict="withhold"),
        _entry("Quote lead-in.", [LIMIT], placed_quote=True), _entry("Story.", ["lpc.story.numidicus"]),
        placed=["lpc.story.numidicus"],
    )
    assert vs.sentence_items(answer, records) == []


def test_the_pack_carries_force_and_years(records):
    pack = vs.record_pack(records[LIMIT])
    assert "limited to the years 246 to 430" in pack and "formation confidence: Documented" in pack
    assert "(1) " in pack and "a claim that a woman's own writing survives" not in pack


def test_the_request_names_the_sentence_and_its_records(records):
    request = vs.verify_request("We wrote it.", [LIMIT], records)
    assert LIMIT in request["user"] and request["user"].endswith("SENTENCE\nWe wrote it.")


@pytest.mark.parametrize("reply, expected", [
    ('{"supported": true, "problem": null, "reason": "ok"}', {"supported": True, "problem": None, "reason": "ok"}),
    ('Sure: {"supported": false, "problem": "dropped_scope", "reason": "years"}', {"supported": False, "problem": "dropped_scope", "reason": "years"}),
    ('{"supported": false, "problem": "nonsense", "reason": "x"}', {"supported": False, "problem": "other", "reason": "x"}),
    ("not json", None), ('{"supported": "yes"}', None), ("", None),
])
def test_parse_verify(reply, expected):
    assert vs.parse_verify(reply) == expected


def test_decide_keeps_supported_and_unreadable_and_rewrites_unsupported():
    assert vs.decide({"supported": True, "problem": None, "reason": ""}) == "keep"
    assert vs.decide(None) == "keep"
    assert vs.decide({"supported": False, "problem": "other", "reason": ""}) == "rewrite"


@pytest.mark.parametrize("reply, expected", [
    ("Women reach us in men's words.", "Women reach us in men's words."),
    ("DROP", None), ("drop.", None), ("", None),
    ("Women [[x]] reach us.", None), ('He said "no".', None), ("One line.\nTwo lines.", None),
])
def test_parse_rewrite(reply, expected):
    assert vs.parse_rewrite(reply) == expected


def test_splice_replaces_or_removes_one_sentence():
    text = "First one. Second one.\n\nThird one."
    assert vs.splice(text, "Second one.", "Changed.") == "First one. Changed.\n\nThird one."
    assert vs.splice(text, "Third one.", None) == "First one. Second one."
    assert vs.splice(text, "Absent.", "x") == text
