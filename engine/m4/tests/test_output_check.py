"""Every case here is one the live probe actually produced, or the exact
false positive that would make the check useless."""
import pytest

from engine.m4 import events
from engine.m4.output_check import check_output


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
