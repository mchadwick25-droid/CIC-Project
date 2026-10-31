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


def test_a_bound_exclusive_claim_is_left_to_the_verify_step_not_the_limit_test(records):
    gravity = "lpc.term.bishop-of-bishops"
    assert us.decide_classified({"kind": "world_claim"}, _item("Only Christ judges him.", [gravity]), records) == "keep"
    assert us.decide_classified({"kind": "connective"}, _item("None of us stood apart.", []), records) == "keep"


@pytest.mark.parametrize("sentence, expected", [
    ("We hold it at Widely Accepted.", True), ("We call it Inferential-Thin.", True), ("The formation confidence is high.", True),
    ("We hold it as Documented.", True), ("Documented in his letters, the rule stands.", False), ("It is widely accepted that he wrote.", False),
])
def test_talks_of_tags(sentence, expected):
    assert us.talks_of_tags(sentence) is expected


OFFERED = ["lpc.limit.womens-own-voice", "lpc.witness.days-before-the-sun"]


def test_the_bind_request_shows_the_offered_records_and_the_sentence(records):
    request = us.bind_request("Q?", "We kept it so.", OFFERED, records)
    assert "lpc.limit.womens-own-voice" in request["user"] and request["user"].endswith("SENTENCE\nWe kept it so.")
    assert "bind" in us.BIND_SYSTEM and "repair" in us.BIND_SYSTEM and "none" in us.BIND_SYSTEM


@pytest.mark.parametrize("reply, expected", [
    ('{"action": "bind", "record": "lpc.limit.womens-own-voice", "sentence": null}', {"action": "bind", "record": "lpc.limit.womens-own-voice", "sentence": "S."}),
    ('{"action": "none", "record": null, "sentence": null}', None),
    ('{"action": "bind", "record": "lpc.limit.not-offered", "sentence": null}', None),
    ('{"action": "repair", "record": "lpc.limit.womens-own-voice", "sentence": "We keep to what is written. And more."}', None),
    ('{"action": "repair", "record": "lpc.limit.womens-own-voice", "sentence": "We keep what is written [[x]]."}', None),
    ("not json", None),
])
def test_parse_bind(reply, expected, records):
    assert us.parse_bind(reply, "S.", OFFERED, records) == expected


def test_a_repair_that_is_one_plain_sentence_stands(records):
    reply = '{"action": "repair", "record": "lpc.witness.days-before-the-sun", "sentence": "Augustine wrote that the days came before the sun."}'
    assert us.parse_bind(reply, "S.", OFFERED, records) == {
        "action": "repair", "record": "lpc.witness.days-before-the-sun", "sentence": "Augustine wrote that the days came before the sun."}


def test_a_limit_bound_to_a_record_must_still_be_stated_by_it(records):
    stated = "From our own two cities, in our years from 246 to 430, no text a woman wrote herself survives."
    assert us.bound_limit_stands(stated, "lpc.limit.womens-own-voice", True, records)
    assert not us.bound_limit_stands("Nothing we carry speaks of him.", "lpc.limit.womens-own-voice", True, records)
    assert us.bound_limit_stands("Nothing we carry speaks of him.", "lpc.limit.womens-own-voice", False, records)


def test_a_repair_that_names_a_confidence_level_is_refused(records):
    reply = '{"action": "repair", "record": "lpc.witness.days-before-the-sun", "sentence": "We hold it as Documented that the days came before the sun."}'
    assert us.parse_bind(reply, "S.", OFFERED, records) is None


def test_bind_reply_readable():
    assert us.bind_reply_readable('{"action": "none", "record": null, "sentence": null}')
    assert not us.bind_reply_readable("garbage") and not us.bind_reply_readable('{"action": "maybe"}')


def test_shipped_items_carry_the_sentence_before_that_stays_in_the_answer(records):
    answer = {"net_sentences": [_entry("First one."), _entry("Held out.", ["not.a.record"]), _entry("Then he spoke.", [LIMIT])]}
    items = us.shipped_items(answer, records)
    assert items[-1]["before"] == "First one." and items[0]["before"] == ""


def test_a_repair_that_names_a_confidence_level_is_refused(records):
    reply = '{"action": "repair", "record": "lpc.witness.days-before-the-sun", "sentence": "We hold it as Documented that the days came before the sun."}'
    assert us.parse_bind(reply, "S.", OFFERED, records) is None


def test_bind_reply_readable():
    assert us.bind_reply_readable('{"action": "none", "record": null, "sentence": null}')
    assert not us.bind_reply_readable("garbage") and not us.bind_reply_readable('{"action": "maybe"}')


def test_shipped_items_carry_the_sentence_before_that_stays_in_the_answer(records):
    answer = {"net_sentences": [_entry("First one."), _entry("Held out.", ["not.a.record"]), _entry("Then he spoke.", [LIMIT])]}
    items = us.shipped_items(answer, records)
    assert items[-1]["before"] == "First one." and items[0]["before"] == ""
