"""Hermetic tests for demonstration citation tagging (M4 step 4 follow-up,
engine/m2/builders.py: _demonstration_candidates/_candidate_head_text/
_tag_representative_text) - LIVE-GENERATION-DESIGN.md §5.3's own recommended
direct-scoring alternative to a `sources`-field-driven approach that real
records don't support. Synthetic fixture records, same discipline as
engine/m4/tests/test_evidence.py's own fixtures.
"""
from engine.m2.builders import (
    _candidate_head_text,
    _demonstration_candidates,
    _tag_representative_text,
    build_prompt,
)

WITNESS = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "canon_cells": ["C-I"],
    "text": "We did not claim to have seen him ourselves.",
}
# A record whose HEAD (compiled-facing) text is short and unrelated to
# "death" or "cost", but whose trailing body (never compiled) happens to
# discuss torture and cost at length - the exact real-data shape that
# produced a false tag before this module scored against head text only.
TERM_WITH_MISLEADING_BODY = {
    "id": "fix.term.ministrae",
    "record_type": "term",
    "canon_cells": ["C-I"],
    "plain_meaning": "A word for two women in a recognized service role.",
    "quick_meaning": "Two women, a recognized role.",
    "_body": "A Roman magistrate's letter records the cost of an interrogation naming these women; the name for their office is otherwise unattested in this world's own record, and its own history is unrecorded.",
}
DEMO = {
    "id": "fix.demo.center-who-is-jesus",
    "record_type": "demonstration",
    "canon_cells": ["C-I"],
    "exchange": [
        {"speaker": "participant", "text": "Who was Jesus to your people?"},
        {
            "speaker": "representative",
            "text": (
                "We did not claim to have seen him ourselves. "
                "What we can tell you is what a death for the name cost some of us."
            ),
        },
    ],
}
REPOSITORY = {r["id"]: r for r in (WITNESS, TERM_WITH_MISLEADING_BODY, DEMO)}


def test_demonstration_candidates_scoped_to_the_demos_own_cell():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    assert {c["id"] for c in candidates} == {"fix.witness.who-is-jesus", "fix.term.ministrae"}


def test_demonstration_candidates_empty_when_demo_has_no_canon_cells():
    assert _demonstration_candidates(REPOSITORY, {"canon_cells": []}) == []


def test_candidate_head_text_uses_compiler_facing_fields_only():
    head = _candidate_head_text(TERM_WITH_MISLEADING_BODY)
    assert "cost" not in head.lower()
    assert "interrogation" not in head.lower()
    assert "recognized service role" in head or "recognized role" in head


def test_tag_representative_text_tags_a_grounded_sentence():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text("We did not claim to have seen him ourselves.", candidates)
    assert "[[fix.witness.who-is-jesus]]" in tagged


def test_tag_representative_text_never_tags_from_a_records_trailing_body():
    """The regression case found against real data: a short sentence that
    shares 2 common words with a candidate's TRAILING BODY (never
    compiled, never seen by a model) must not get tagged to that
    candidate - only the record's own compiled-facing head text counts."""
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text("What we can tell you is what a death for the name cost some of us.", candidates)
    assert "[[fix.term.ministrae]]" not in tagged
    assert "[[" not in tagged  # nothing else clears the floor either - correctly left untagged


def test_tag_representative_text_leaves_ungrounded_sentences_untagged():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text("We are glad you asked us that question today.", candidates)
    assert "[[" not in tagged


def test_tag_representative_text_empty_candidates_is_a_no_op():
    text = "We did not claim to have seen him ourselves."
    assert _tag_representative_text(text, []) == text


def test_build_prompt_tags_only_representative_turns_not_participant_turns():
    prompt = build_prompt(REPOSITORY, {}, {"display_name": "Fixture World"}).decode("utf-8")
    idx = prompt.find("## Demonstration ")
    section = prompt[idx:]
    participant_line = next(line for line in section.splitlines() if line.startswith("participant:"))
    representative_line = next(line for line in section.splitlines() if line.startswith("representative:"))
    assert "[[" not in participant_line
    assert "[[fix.witness.who-is-jesus]]" in representative_line
    assert "[[fix.term.ministrae]]" not in representative_line
