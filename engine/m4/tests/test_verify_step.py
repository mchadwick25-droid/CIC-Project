"""What the answer check reads a sentence against: bindings, record packs, the confidence cap."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4 import verify_step as vs

LIMIT = "lpc.limit.womens-own-voice"


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


def test_a_context_block_or_unknown_id_is_not_a_binding(records):
    assert vs.valid_bindings([f"ctx.{LIMIT}.1", "no.such.record", LIMIT, LIMIT], records) == [LIMIT]


def test_the_story_pack_is_what_the_voice_was_shown_not_the_source_text(records):
    pack = vs.record_pack(records["lpc.story.numidicus"], records)
    assert records["lpc.story.numidicus"]["tellable_as"].split(".")[0] in pack
    assert "cic/texts" not in pack


def test_the_pack_carries_force_and_years(records):
    pack = vs.record_pack(records[LIMIT], records)
    assert "limited to the years 246 to 430" in pack and "formation confidence: Documented" in pack
    assert "(1) " in pack and "MUST NOT ASSERT: a claim that a woman's own writing survives" in pack
    assert "lpc.source" not in pack and "Doc_09" not in pack


@pytest.mark.parametrize("entry, expected", [
    ({"supported": True, "problem": None, "reason": "ok"}, {"supported": True, "problem": None, "reason": "ok"}),
    ({"supported": False, "problem": "dropped_scope", "reason": "years"}, {"supported": False, "problem": "dropped_scope", "reason": "years"}),
    ({"supported": False, "problem": "nonsense", "reason": "x"}, {"supported": False, "problem": "other", "reason": "x"}),
    ({"supported": "yes"}, None), ({}, None), ("text", None),
])
def test_judgement_from(entry, expected):
    assert vs.judgement_from(entry) == expected


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
    assert vs.apply_confidence_cap(supported, sentence, [WIDELY], records) == supported
    assert vs.apply_confidence_cap(None, sentence, [WIDELY, THIN], records) is None


def test_level_names_count_only_as_names_of_a_level(records):
    for sentence in ("Augustine documented his conversion in a book.", "This is not documented; it is contested.", "It was widely accepted by his hearers."):
        assert not vs.confidence_exceeds(sentence, ["lpc.witness.days-before-the-sun", THIN], records)
    assert vs.confidence_exceeds("We hold it at Widely\n Accepted.", [WIDELY, THIN], records)
    assert vs.confidence_exceeds("It is Documented.", ["lpc.witness.days-before-the-sun", THIN], records)


def test_the_cap_keeps_the_judges_own_finding(records):
    own = {"supported": False, "problem": "added_detail", "reason": "adds a date"}
    assert vs.apply_confidence_cap(own, "We hold it at Widely Accepted.", [WIDELY, THIN], records) == own


def test_the_judge_holds_a_joined_sentence_to_the_narrower_scope_and_the_claim_guard():
    assert "MUST NOT ASSERT" in vs.VERIFY_CRITERIA and "narrower scope" in vs.VERIFY_CRITERIA


def test_the_pack_shows_each_bound_records_claim_guard(records):
    pack = vs.record_pack(records["lpc.term.bishop-of-bishops"], records)
    assert "MUST NOT ASSERT" in pack


def test_the_judge_needs_a_record_to_state_an_exclusive_or_absent_claim():
    assert "exclusivity or absence" in vs.VERIFY_CRITERIA and "merely names the thing" in vs.VERIFY_CRITERIA


def test_the_judge_holds_a_sentence_to_the_sources_hedge_and_date():
    assert "keeps its records' own hedge, concession and date" in vs.VERIFY_CRITERIA
    assert "only allowed, supposed or conceded (stronger_force)" in vs.VERIFY_CRITERIA and "(dropped_scope)" in vs.VERIFY_CRITERIA
    assert "a span of years a record is limited to is not such a tie" in vs.VERIFY_CRITERIA
