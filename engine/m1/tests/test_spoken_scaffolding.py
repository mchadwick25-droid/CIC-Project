"""The oblique flag on a witness, and the spoken-scaffolding check."""
import pytest
from jsonschema import Draft202012Validator

from engine.m1.schemas import build_schema
from engine.m1.spoken_scaffolding import scaffolding_hits

CLEAN_WITNESS = {
    "id": "fix.dw.who-is-jesus", "record_type": "doctrinal_witness", "world_id": "fix", "schema_version": 1,
    "text": "We knew him as the one the meal remembers. We did not claim to have seen him ourselves.",
}


def _errors(record):
    validator = Draft202012Validator(build_schema("doctrinal_witness"))
    return [e.message for e in validator.iter_errors(record)]


def test_a_witness_may_carry_the_flag_with_a_reason():
    record = {**CLEAN_WITNESS, "answers_obliquely": True, "oblique_reason": "Our sources speak of him through the meal."}
    assert _errors(record) == []


def test_the_schema_rejects_the_flag_without_a_reason():
    errors = _errors({**CLEAN_WITNESS, "answers_obliquely": True})
    assert any("oblique_reason" in e for e in errors)
    assert _errors({**CLEAN_WITNESS, "answers_obliquely": True, "oblique_reason": ""})


def test_a_false_flag_needs_no_reason_and_no_flag_is_the_default():
    assert _errors({**CLEAN_WITNESS, "answers_obliquely": False}) == []
    assert _errors(CLEAN_WITNESS) == []


def test_no_other_record_type_takes_the_flag():
    validator = Draft202012Validator(build_schema("term"))
    record = {"id": "fix.term.a", "record_type": "term", "world_id": "fix", "schema_version": 1, "answers_obliquely": True}
    assert any("answers_obliquely" in e.message for e in validator.iter_errors(record))


def _witness(text):
    return {"id": "fix.dw.a", "record_type": "doctrinal_witness", "text": text}


def test_the_clean_fixture_passes():
    assert scaffolding_hits({"fix.dw.a": _witness(CLEAN_WITNESS["text"])}) == []


@pytest.mark.parametrize(
    "text, reason",
    [
        ("Was Jesus God? To us it would be strange to hear that asked.", "question mark"),
        ("We knew him by the meal. Your second question is harder.", "your second question"),
        ("Start with the part about the meal. We kept it.", "start with the part"),
        ("As you asked, we held to the old creed.", "as you asked"),
        ("We knew him by the meal. You asked about the creed.", "you asked"),
    ],
)
def test_the_seeded_defect_fires(text, reason):
    hits = scaffolding_hits({"fix.dw.a": _witness(text)})
    assert hits and reason in hits[0][2].lower()


def test_a_question_after_the_first_sentence_is_not_a_defect():
    assert scaffolding_hits({"fix.dw.a": _witness("We knew him by the meal. Who would not?")}) == []


def test_term_and_story_text_is_checked_too_and_other_types_are_not():
    term = {"id": "fix.term.a", "record_type": "term", "plain_meaning": "What does it mean? A washing."}
    story = {"id": "fix.story.a", "record_type": "story", "tellable_as": "A woman came to the well. As you asked, here is the telling."}
    quote = {"id": "fix.quote.a", "record_type": "quote", "text": "Who is this?", "modern_rendering": "Who is this?"}
    found = {rid for rid, _, _ in scaffolding_hits({r["id"]: r for r in (term, story, quote)})}
    assert found == {"fix.term.a", "fix.story.a"}
