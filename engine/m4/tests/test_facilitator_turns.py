"""SYSTEM_NATURE's own words are participant-facing honesty text, ruled
directly by Mark (R18, Decision-Log.md Entry 29, corrected wording ruled
2026-09-22) - not free for a future edit to drift back toward
overclaiming ("checked against the record it came from") without
noticing. Pins the ruled middle sentences exactly; PR #383 shipped an
earlier reword with no such pin, which is how the wording needed a
second correction the same week."""
from engine.m4.facilitator_turns import SYSTEM_NATURE


def test_system_nature_states_the_ruled_verification_sentences():
    assert (
        "Before you see an answer, each claim in it is checked to make sure "
        "its words come from the record it names."
    ) in SYSTEM_NATURE.text
    assert "The record itself was checked against the sources when the world was built." in SYSTEM_NATURE.text
    assert (
        "Where the record is silent, the voice is built to say so, not to fill the gap."
    ) in SYSTEM_NATURE.text


def test_system_nature_does_not_overclaim_truth_verification():
    """The R18 defect PR #383 first fixed: wording that reads as verifying
    the underlying history, not just the record's own wording."""
    assert "checked against the record it came from" not in SYSTEM_NATURE.text
    assert "every specific claim in it is checked against the record" not in SYSTEM_NATURE.text
