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
        _entry("Quote lead-in.", [LIMIT], placed_quote=True), _entry("Story.", ["lpc.story.numidicus"], placed_story=True),
        _entry("Answer record.", [LIMIT], placed_answer=True),
    )
    assert vs.sentence_items(answer, records) == []


def test_a_voice_sentence_citing_a_story_code_placed_is_still_read(records):
    answer = _answer(_entry("The story.", ["lpc.story.numidicus"], placed_story=True),
                     _entry("That is why we keep the vigil.", ["lpc.story.numidicus"]), placed=["lpc.story.numidicus"])
    assert [i["n"] for i in vs.sentence_items(answer, records)] == [1]


def test_the_story_pack_is_what_the_voice_was_shown_not_the_source_text(records):
    pack = vs.record_pack(records["lpc.story.numidicus"], records)
    assert records["lpc.story.numidicus"]["tellable_as"].split(".")[0] in pack
    assert "cic/texts" not in pack


def test_the_pack_carries_force_and_years(records):
    pack = vs.record_pack(records[LIMIT], records)
    assert "limited to the years 246 to 430" in pack and "formation confidence: Documented" in pack
    assert "(1) " in pack and "MUST NOT ASSERT: a claim that a woman's own writing survives" in pack
    assert "lpc.source" not in pack and "Doc_09" not in pack


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
    ("He said ‘no’ to them.", None), ("He said «no».", None), ("One sentence. Another one.", None),
    ("Cyprian's letter reached us.", "Cyprian's letter reached us."),
    ("We don’t hold that.", "We don’t hold that."), ("The apostles’ letters reached us.", "The apostles’ letters reached us."),
    ("Ignatius called it 'the medicine of immortality'.", None),
])
def test_parse_rewrite(reply, expected):
    assert vs.parse_rewrite(reply) == expected


def test_a_rewrite_that_states_an_unsupported_absence_is_refused(records):
    assert vs.parse_rewrite("We have no sermon of our own on those opening lines.", [LIMIT], records) is None
    assert vs.parse_rewrite("In all our years, no text a woman wrote survives from our two cities.", [LIMIT], records)


def test_splice_replaces_or_removes_one_sentence():
    text = "First one. Second one.\n\nThird one."
    assert vs.splice(text, "Second one.", "Changed.") == ("First one. Changed.\n\nThird one.", True)
    assert vs.splice(text, "Third one.", None) == ("First one. Second one.", True)
    assert vs.splice(text, "Absent.", "x") == (text, False)
    assert vs.splice("A long sentence. Long.", "Long.", "Short.")[0] == "A long sentence. Short."


def test_the_quote_pack_names_the_speaker(records):
    pack = vs.record_pack(records["lpc.quote.a-dreadful-plague-broke-out"], records)
    assert "quote from" in pack and "Pontius" in pack


WIDELY = "lpc.gravity.collegial-communion-preserved"
THIN = "lpc.witness.answerability-as-ground"


def test_the_request_shows_the_sentence_before_it_for_words_that_refer_back(records):
    request = vs.verify_request("What light made them, he wrote, is beyond our senses.", ["lpc.witness.days-before-the-sun"], records,
                                "The older books speak of days before the sun.")
    assert "SENTENCE BEFORE IT" in request["user"] and "The older books speak" in request["user"]
    assert request["user"].endswith("SENTENCE\nWhat light made them, he wrote, is beyond our senses.")
    assert "SENTENCE BEFORE IT" not in vs.verify_request("We wrote it.", [LIMIT], records)["user"]


def test_sentence_items_carry_the_sentence_before(records):
    items = vs.sentence_items(_answer(_entry("First.", []), _entry("Then them.", [LIMIT])), records)
    assert items[0]["before"] == "First."


def test_the_judge_instructions_cover_referents_and_the_lowest_confidence():
    assert "unresolved_referent" in vs.VERIFY_SYSTEM and "lowest level" in vs.VERIFY_SYSTEM


def test_a_rewrite_names_the_thing_instead_of_a_pronoun():
    assert "instead of using a pronoun" in vs.REWRITE_SYSTEM


def test_records_of_different_confidence_cap_a_sentence_at_the_lowest(records):
    held = "We hold the link at Widely Accepted, and no source states it."
    assert vs.confidence_exceeds(held, [WIDELY, THIN], records)
    assert not vs.confidence_exceeds("We call the link Inferential-Thin.", [WIDELY, THIN], records)
    assert not vs.confidence_exceeds(held, [WIDELY], records)
    assert not vs.confidence_exceeds("We say nothing of levels.", [WIDELY, THIN], records)
    assert not vs.confidence_exceeds(held, [], records)


def test_the_cap_turns_a_supported_reading_into_stronger_force(records):
    supported = {"supported": True, "problem": None, "reason": "ok"}
    sentence = "We hold the link at Widely Accepted."
    capped = vs.apply_confidence_cap(supported, sentence, [WIDELY, THIN], records)
    assert capped["supported"] is False and capped["problem"] == "stronger_force"
    assert vs.decide(capped) == "rewrite"
    assert vs.apply_confidence_cap(supported, sentence, [WIDELY], records) == supported
    assert vs.apply_confidence_cap(None, sentence, [WIDELY, THIN], records) is None
    reply = '{"supported": true, "problem": null, "reason": "ok"}'
    assert vs.read_reply(reply, sentence, [WIDELY, THIN], records)["supported"] is False


def test_the_sentence_before_skips_one_that_does_not_stay_in_the_answer(records):
    answer = _answer(_entry("Kept first.", []), _entry("Held out.", ["not.a.record"]), _entry("Withheld.", [], verdict="withhold"), _entry("Then he.", [LIMIT]))
    items = vs.sentence_items(answer, records)
    assert items[-1]["sentence"] == "Then he." and items[-1]["before"] == "Kept first."
    assert vs.sentence_items(_answer(_entry("Only.", [LIMIT])), records)[0]["before"] == ""


def test_level_names_count_only_as_names_of_a_level(records):
    for sentence in ("Augustine documented his conversion in a book.", "This is not documented; it is contested.", "It was widely accepted by his hearers."):
        assert not vs.confidence_exceeds(sentence, ["lpc.witness.days-before-the-sun", THIN], records)
    assert vs.confidence_exceeds("We hold it at Widely\n Accepted.", [WIDELY, THIN], records)
    assert vs.confidence_exceeds("It is Documented.", ["lpc.witness.days-before-the-sun", THIN], records)


def test_the_cap_keeps_the_judges_own_finding(records):
    own = {"supported": False, "problem": "added_detail", "reason": "adds a date"}
    assert vs.apply_confidence_cap(own, "We hold it at Widely Accepted.", [WIDELY, THIN], records) == own


def test_the_judge_holds_a_joined_sentence_to_the_narrower_scope_and_the_claim_guard():
    assert "MUST NOT ASSERT" in vs.VERIFY_SYSTEM and "narrower scope" in vs.VERIFY_SYSTEM


def test_the_pack_shows_each_bound_records_claim_guard(records):
    pack = vs.record_pack(records["lpc.term.bishop-of-bishops"], records)
    assert "MUST NOT ASSERT" in pack


def test_the_judge_needs_a_record_to_state_an_exclusive_or_absent_claim():
    assert "exclusivity or absence" in vs.VERIFY_SYSTEM and "merely names the thing" in vs.VERIFY_SYSTEM
