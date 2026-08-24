"""The literal stage-5 gate item, proven hermetically: "crisis append
asserted including the empty-stream case." append_crisis_resources_turn
takes no client and makes no call - these are pure assertions against its
return value for every shape a real voice-companion generation call could
have produced (real text, empty text, whitespace-only text, an outright
call failure)."""
from engine.m4.crisis_resources import append_crisis_resources_turn


def test_acute_distress_appends_with_real_stream_text():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="I hear how much pain you're carrying.", stream_failed=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is False
    assert "reach out to someone real" in turn["text"]


def test_acute_distress_appends_on_empty_string_stream():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="", stream_failed=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True
    assert "reach out to someone real" in turn["text"]


def test_acute_distress_appends_on_whitespace_only_stream():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="   \n  ", stream_failed=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True


def test_acute_distress_appends_on_none_stream_text():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text=None, stream_failed=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True


def test_acute_distress_appends_even_when_stream_call_failed_outright():
    """The call itself erroring (timeout/APIError) is functionally the same
    as an empty stream for append purposes - resources still go out."""
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text=None, stream_failed=True)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True


def test_acute_distress_appends_even_when_call_failed_but_somehow_carried_text():
    """stream_failed=True dominates regardless of stream_text - a failed
    call's text (if any leaked through) is never trusted as 'not empty'."""
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="some text", stream_failed=True)
    assert turn["empty_stream"] is True


def test_harmful_dynamic_signal_does_not_append_crisis_resources():
    """Track B (dependency dynamics) is not a crisis - resources are
    Track A's alone (Program-Spec SS8)."""
    turn = append_crisis_resources_turn(signal="HARMFUL_DYNAMIC_SIGNAL", stream_text="anything", stream_failed=False)
    assert turn["resources_appended"] is False
    assert turn["text"] is None
