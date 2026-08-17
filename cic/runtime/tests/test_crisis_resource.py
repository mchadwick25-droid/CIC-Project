"""A person in acute distress must be given a real number to call.

California SB 243 requires an operator whose system detects suicidal
ideation or self-harm to refer the user to crisis services. Until
2026-08-17 these templates forbade naming any resource - the shipped
Option A of the 2026-08-05 resource-redirect decision, which explicitly
reserved Option C (a concrete named resource) to the project lead.

The referral is APPENDED by stream_relational_safety_response, not asked
of the model, and that is the thing these tests protect. A prompt asking
a model for a phone number is asking it to recall one; the same day this
landed, a generation audit caught a representative inventing a saying and
hanging it on a named person against four explicit prohibitions in its
own prompt. A wrong number in a crisis turn is worse than no number.

So: the model may write anything at all, including nothing, and the
referral still reaches the participant.

Pure string and generator handling - no LLM, no key, no network.
"""
import pytest

from app.prompts.facilitator_prompts import (
    CRISIS_RESOURCE_LINE,
    FACILITATOR_ACUTE_DISTRESS_A1_PROMPT,
    FACILITATOR_ACUTE_DISTRESS_A2_PROMPT,
)


def test_the_number_is_dialable_and_carries_a_non_us_path():
    """988 for the US, and something for everyone else.

    The decision document's objection to Option B was that a
    wrong-jurisdiction number is actively unhelpful at exactly the wrong
    moment, so the non-US sentence is not decoration - it is the reason
    naming a US number is defensible at all.
    """
    assert "988" in CRISIS_RESOURCE_LINE
    assert "Outside the US" in CRISIS_RESOURCE_LINE
    lowered = CRISIS_RESOURCE_LINE.lower()
    assert "call or text" in lowered
    assert "crisis line" in lowered or "lifeline" in lowered


@pytest.mark.parametrize("template", [
    FACILITATOR_ACUTE_DISTRESS_A1_PROMPT,
    FACILITATOR_ACUTE_DISTRESS_A2_PROMPT,
])
def test_the_model_is_told_not_to_write_the_number_itself(template):
    """The prohibition survives, with its meaning inverted.

    It used to mean "no resource is given at all". It now means "the
    system gives it, so do not duplicate or misremember it". If a future
    edit drops this line, the model starts producing numbers from memory
    alongside the appended one.
    """
    assert "appended" in template
    assert "988" not in template


def test_a1_still_carries_the_general_redirect_floor():
    """Option A stays exactly as it was, underneath.

    The concrete resource is added to the general language, not
    substituted for it - that is what makes this Option C rather than a
    reversal of the 2026-08-05 decision.
    """
    assert "a person they trust, a crisis line, or emergency services" \
        in FACILITATOR_ACUTE_DISTRESS_A1_PROMPT


def _drain(events):
    """The text a participant actually receives, tokens plus final."""
    streamed = "".join(e["text"] for e in events if e["type"] == "token")
    final = next(e for e in events if e["type"] == "complete")
    return streamed, final["message"].content


def test_referral_survives_a_model_that_ignores_every_instruction(safety_events):
    """The whole point: the model's output is not trusted to contain it."""
    events = safety_events(model_text="I would rather not answer that.")
    streamed, final = _drain(events)
    assert "988" in streamed
    assert "988" in final


def test_referral_survives_an_empty_stream(safety_events):
    events = safety_events(model_text="")
    streamed, final = _drain(events)
    assert CRISIS_RESOURCE_LINE.strip() in streamed
    assert CRISIS_RESOURCE_LINE.strip() in final


def test_no_referral_on_a_harmful_dynamic_turn(safety_events):
    """Track B is over-attachment, not a crisis disclosure.

    Appending a hotline to it would be the system misreading someone's
    enthusiasm as an emergency.
    """
    events = safety_events(model_text="Something warm.",
                                 category="HARMFUL_DYNAMIC_SIGNAL")
    streamed, _ = _drain(events)
    assert "988" not in streamed


def test_no_referral_on_a_continuation_turn(safety_events):
    """Light-touch by design - repeating the hotline every message reads
    as a script being recited at someone rather than staying with them."""
    events = safety_events(model_text="I'm still here.",
                                 fresh_fire=False)
    streamed, _ = _drain(events)
    assert "988" not in streamed
