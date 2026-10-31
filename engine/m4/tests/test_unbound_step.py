"""The unbound-sentence step: classify what the voice shipped without a binding;
a limit stays only when a record it is bound to states it."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4 import unbound_step as us

LIMIT = "lpc.limit.womens-own-voice"
STATED = "From our own two cities, in our years from 246 to 430, no text a woman wrote herself survives."


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


def _entry(sentence, tags=(), verdict="ok", **extra):
    return {"sentence": sentence, "tags": list(tags), "verdict": verdict, **extra}


def _item(sentence, bound=(), withheld=False):
    return {"sentence": sentence, "bound": bool(bound), "records": list(bound), "withheld": withheld}


def test_shipped_items_mark_bound_unbound_and_withheld_and_skip_placed(records):
    answer = {"net_sentences": [
        _entry("Bound.", [LIMIT]), _entry("Untagged."), _entry("Context only.", ["ctx.x.1"]),
        _entry("Withheld with a tag.", [LIMIT], verdict="withhold"), _entry("Placed lead-in.", [LIMIT], placed_quote=True),
        _entry("A story sentence.", [], placed_story=True),
    ]}
    items = us.shipped_items(answer, records)
    assert [(i["n"], i["bound"], i["withheld"]) for i in items] == [(0, True, False), (1, False, False), (2, False, False), (3, False, True)]
    assert items[0]["records"] == [LIMIT] and items[1]["records"] == []


@pytest.mark.parametrize("reply, expected", [
    ('{"kind": "connective"}', {"kind": "connective"}),
    ('Here: {"kind": "limit", "denies": "anything"}', {"kind": "limit"}),
    ('{"kind": "opinion"}', None), ("nothing", None),
])
def test_parse_classify(reply, expected):
    assert us.parse_classify(reply) == expected


def test_an_unbound_world_claim_is_withheld_and_a_bound_one_is_left_to_the_verify_step(records):
    claim = {"kind": "world_claim"}
    assert us.decide_classified(claim, _item("x."), records) == "withhold"
    assert us.decide_classified(claim, _item("x.", [LIMIT]), records) == "keep"
    for kind in ("connective", "conversation"):
        assert us.decide_classified({"kind": kind}, _item("x."), records) == "keep"
    assert us.decide_classified(None, _item("x."), records) == "keep"


def test_a_limit_with_no_binding_is_always_withheld(records):
    limit = {"kind": "limit"}
    assert us.decide_classified(limit, _item(STATED), records) == "withhold_limit"
    assert us.decide_classified(limit, _item("That is as far as his words take us."), records) == "withhold_limit"


def test_a_limit_bound_to_a_record_that_states_it_with_its_scope_is_kept(records):
    assert us.decide_classified({"kind": "limit"}, _item(STATED, [LIMIT]), records) == "keep"


def test_a_limit_bound_to_a_record_that_does_not_state_it_is_withheld(records):
    force = "lpc.force.inherited-latin-theological-vocabulary"
    sentence = "We know only that for one country town Augustine looked for a bishop who knew Punic."
    assert us.decide_classified({"kind": "limit"}, _item(sentence, [force]), records) == "withhold_limit"


def test_a_limit_wider_than_the_record_it_cites_is_withheld(records):
    assert us.decide_classified({"kind": "limit"}, _item("No text a woman wrote herself survives.", [LIMIT]), records) == "withhold_limit"


def test_a_bound_sentence_worded_as_a_limit_gets_the_limit_test_whatever_the_reader_said(records):
    force = "lpc.force.inherited-latin-theological-vocabulary"
    sentence = "We know only that for one country town Augustine looked for a bishop who knew Punic."
    assert us.decide_classified({"kind": "world_claim"}, _item(sentence, [force]), records) == "withhold_limit"
    assert us.decide_classified({"kind": "connective"}, _item("It never came up.", [force]), records) == "withhold_limit"
    assert us.decide_classified({"kind": "world_claim"}, _item("Augustine looked for a bishop who knew Punic.", [force]), records) == "keep"


@pytest.mark.parametrize("sentence, expected", [
    ("We know only that it was so.", True), ("Nothing survives of it.", True), ("The record does not say how it ended.", True),
    ("No text from them survives but one.", True), ("He wrote to the council.", False), ("They met once.", False),
])
def test_says_limit(sentence, expected):
    assert us.says_limit(sentence) is expected


@pytest.mark.parametrize("sentence, expected", [
    ("We hold it at Widely Accepted.", True), ("We call it Inferential-Thin.", True), ("The formation confidence is high.", True),
    ("We hold it as Documented.", True), ("Documented in his letters, the rule stands.", False), ("It is widely accepted that he wrote.", False),
])
def test_talks_of_tags(sentence, expected):
    assert us.talks_of_tags(sentence) is expected
