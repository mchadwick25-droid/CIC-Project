"""Every case here is one the live probe actually produced, or the exact
false positive that would make the check useless."""
import pytest

from engine.m4 import events
from engine.m4.output_check import check_output, find_shipped_defects


def _families(findings):
    return sorted(f["family"] for f in findings)


def test_clean_text_produces_nothing():
    assert check_output("We rose before dawn and wove baskets.", history=[]) == []


def test_catches_the_malformed_tag_strip_tags_cannot():
    """grounding_net.strip_tags matches [a-z0-9_.-]+ only, so a tag with
    uppercase, a colon and spaces survives it. Eight reached a participant
    across three turns of the desert probe."""
    text = "We kept the teaching [[THIN: no material on dying practices]]."
    assert _families(check_output(text, history=[])) == ["display"]


def test_a_claim_of_prior_discourse_on_the_opening_turn_is_false():
    findings = check_output("We already told you how we ate.", history=[])
    assert [f["finding"].startswith("false:") for f in findings] == [True]


def test_names_a_person_no_prior_turn_named():
    """The bug, verbatim: 'the one woman I have named to you so far in this
    conversation' - two turns into a conversation about food."""
    history = [
        {"role": "user", "content": "How did you get food?"},
        {"role": "assistant", "content": "We wove baskets and sold them in the village."},
    ]
    findings = [f for f in check_output("We already named Sarah among us.", history=history) if f["family"] == "conversational"]
    assert len(findings) == 1
    assert findings[0]["finding"].startswith("false:")
    assert "Sarah" in findings[0]["finding"]


def test_a_name_that_was_said_is_not_flagged():
    history = [
        {"role": "user", "content": "Who taught you?"},
        {"role": "assistant", "content": "Sarah was an amma among us."},
    ]
    assert [f for f in check_output("We already named Sarah among us.", history=history) if f["family"] == "conversational"] == []


def test_a_nameless_claim_is_unverified_not_ruled_on():
    """'We told you it is not effort alone' - no name, so whether the topic
    was discussed is a judgment no pattern here can make."""
    history = [
        {"role": "user", "content": "How did you get food?"},
        {"role": "assistant", "content": "We wove baskets."},
    ]
    findings = [f for f in check_output("We told you it is not effort alone.", history=history) if f["family"] == "conversational"]
    assert len(findings) == 1
    assert findings[0]["finding"].startswith("unverified:")


def test_first_person_singular_is_flagged():
    assert "pronoun" in _families(check_output("You are asking me to identify her.", history=[]))


def test_a_quoted_figure_keeps_their_own_first_person():
    """The pronoun rule's own carve-out: a named figure's quoted words keep
    their original wording - that is a citation, not the voice speaking."""
    text = 'She answered them: "It is I who am a man among you, and ye who are women".'
    assert "pronoun" not in _families(check_output(text, history=[]))


def test_the_sanctioned_self_naming_line_is_not_flagged():
    text = "I am a representative of Desert Monasticism, not one of its elders."
    assert "pronoun" not in _families(check_output(text, history=[]))


def test_voice_turn_cannot_be_emitted_without_the_check_having_run():
    payload = {
        "speaker": "desert", "text": "We wove baskets.", "citations": [],
        "glosses": [], "figures_used": [], "quote_offers": [],
        "attempts_meta": {"empty_stream_retries": 0},
    }
    with pytest.raises(events.EventValidationError):
        events.validate("voice_turn", payload)
    events.validate("voice_turn", {**payload, "output_defects": []})


# ---- the participant-message half ------------------------------------------
# The false premise lives in the participant's turn; acceptance is the ABSENCE
# of a correction in the reply. Every case below is one the live probe produced.

_FOOD_HISTORY = [
    {"role": "user", "content": "How did you get food?"},
    {"role": "assistant", "content": "We wove baskets and sold them in the village."},
]


def test_accepting_a_false_premise_by_deixis_is_caught():
    """'That was Sarah' carries no back-reference phrase at all - the
    acceptance is the word 'that', pointing at a mention the participant
    asserted and the transcript refutes. No pattern over the reply reaches
    it."""
    findings = check_output(
        "That was Sarah - Amma Sarah, by the honored address we gave to proven elders.",
        history=_FOOD_HISTORY,
        participant_message="Earlier you mentioned a woman among you by name. Who was she?",
    )
    conversational = [f for f in findings if f["family"] == "conversational"]
    assert len(conversational) == 1
    assert conversational[0]["finding"].startswith("false:")
    assert "Sarah" in conversational[0]["finding"]


def test_declining_a_false_premise_produces_nothing():
    findings = check_output(
        "We have not named anyone yet. Sarah was an amma among us, and here is what we kept of her.",
        history=_FOOD_HISTORY,
        participant_message="Earlier you mentioned a woman among you by name. Who was she?",
    )
    assert [f for f in findings if f["family"] == "conversational"] == []


def test_a_supported_follow_up_is_not_flagged():
    """The common case, and the one that would make this check unusable if it
    fired: the participant refers back to something really said."""
    history = [
        {"role": "user", "content": "What did you believe about the end of the world?"},
        {"role": "assistant", "content": "We held that judgment was coming and the dead would rise."},
    ]
    findings = check_output(
        "We did not keep an account of how we sat with the dying.",
        history=history,
        participant_message="You just answered about the end. Did that shape how you treated the dying?",
    )
    assert [f for f in findings if f["family"] == "conversational"] == []


def test_a_traditions_phrasing_is_not_a_claim_about_this_conversation():
    """'as we put it' attributes WORDING to the tradition. An earlier version
    flagged it, which is a false positive on ordinary voice."""
    findings = check_output(
        "We took that from experience - led, as we put it, not by chattering words but by experience.",
        history=_FOOD_HISTORY,
        participant_message="How were you saved?",
    )
    assert [f for f in findings if f["family"] == "conversational"] == []


# find_shipped_defects: H-3 (witt go-live adversarial review, 2026-09-19).
# A defect check_output() already caught reached engine.m4.live_turn_run's
# own report with `degraded: false` on the same turn - nothing read
# output_defects back before this. These cases are the report shapes
# themselves, not the text-level check already covered above.

def _defect(finding="false: claims something was already said, on a turn with no prior turns"):
    return {"family": "conversational", "finding": finding, "sentence": "We have named it plainly, more than once."}


def test_clean_turn_run_report_has_no_shipped_defects():
    report = {"results": [{"id": "message-1", "message": "hi", "result": {"voice_event": {"output_defects": []}}}]}
    assert find_shipped_defects(report) == []


def test_turn_run_report_surfaces_a_shipped_defect():
    report = {"results": [{"id": "message-3", "message": "What did your founder write?",
                            "result": {"voice_event": {"output_defects": [_defect()]}}}]}
    found = find_shipped_defects(report)
    assert len(found) == 1
    assert found[0]["id"] == "message-3"
    assert found[0]["family"] == "conversational"


def test_turn_run_report_with_no_voice_event_is_clean():
    """A facilitator-only turn (e.g. safety_turn) has voice_event: None."""
    report = {"results": [{"id": "message-1", "message": "hi", "result": {"voice_event": None}}]}
    assert find_shipped_defects(report) == []


def test_table_run_report_surfaces_a_shipped_defect():
    report = {"rounds": [{"message": "hi", "turns": [
        {"round_no": 2, "position": 1, "turn_selected": {"world_key": "witt"}, "voice": {"output_defects": [_defect()]}},
    ]}]}
    found = find_shipped_defects(report)
    assert len(found) == 1
    assert found[0]["round_no"] == 2
    assert found[0]["position"] == 1


def test_table_run_report_with_no_voice_this_position_is_clean():
    """A closed/facilitator-only table turn has no 'voice' key at all."""
    report = {"rounds": [{"message": "hi", "turns": [{"round_no": 1, "position": 0, "turn_selected": None}]}]}
    assert find_shipped_defects(report) == []


def test_multiple_defects_across_both_report_shapes_all_surface():
    report = {
        "results": [{"id": "message-1", "message": "a", "result": {"voice_event": {"output_defects": [_defect(), _defect("false: second")]}}}],
        "rounds": [{"message": "b", "turns": [{"round_no": 1, "position": 0, "voice": {"output_defects": [_defect("false: third")]}}]}],
    }
    assert len(find_shipped_defects(report)) == 3
