"""R38 build round-1 review fix (reviewer thread, 2026-09-23): the first
version of REVISION_INSTRUCTION hardcoded "the participant's question
about the Donatists" - the measurement probe's own text, carried
verbatim into production, where the question can be about any
tradition. These pin the fix directly on the module, not only through
the full turn pipeline test_turn.py's own self-revision tests already
cover."""
import re

from engine.m4.self_revision import REVISION_INSTRUCTION, build_revision_message


def test_revision_instruction_names_no_tradition():
    # A hardcoded tradition name in the constant would repeat this
    # defect for every turn, regardless of what the participant actually
    # asked about - the instruction must stay tradition-neutral.
    assert "donatist" not in REVISION_INSTRUCTION.lower()
    assert "manichean" not in REVISION_INSTRUCTION.lower()
    assert not re.search(r"\bquestion about\b", REVISION_INSTRUCTION.lower())


def test_build_revision_message_carries_the_participants_own_question():
    message = build_revision_message(
        participant_message="What did your community believe about the Manicheans?",
        draft_text="A draft [[some.record]].",
        tagged_record_ids=["some.record"],
        repository_records={"some.record": {"text": "The record's own real text."}},
    )
    assert "What did your community believe about the Manicheans?" in message
