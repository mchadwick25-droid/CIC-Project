"""The literal stage-5 gate item, proven hermetically: "crisis append
asserted including the empty-stream case." append_crisis_resources_turn
takes no client and makes no call - these are pure assertions against its
return value for every shape a real voice-companion generation call could
have produced (real text, empty text, whitespace-only text, an outright
call failure)."""
from engine.m4.crisis_resources import append_crisis_resources_turn, resources_for_signal


def test_acute_distress_appends_with_real_stream_text():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="I hear how much pain you're carrying.", stream_failed=False, representative_name="Vera", acute_level="a1", already_fired=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is False
    assert "reach out to someone real" in turn["text"]
    assert "not Vera" in turn["text"]  # representative_name is substituted, not left as a template slot


def test_acute_distress_appends_on_empty_string_stream():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="", stream_failed=False, representative_name="Vera", acute_level="a1", already_fired=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True
    assert "reach out to someone real" in turn["text"]


def test_acute_distress_appends_on_whitespace_only_stream():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="   \n  ", stream_failed=False, representative_name="Vera", acute_level="a1", already_fired=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True


def test_acute_distress_appends_on_none_stream_text():
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text=None, stream_failed=False, representative_name="Vera", acute_level="a1", already_fired=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True


def test_acute_distress_appends_even_when_stream_call_failed_outright():
    """The call itself erroring (timeout/APIError) is functionally the same
    as an empty stream for append purposes - resources still go out."""
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text=None, stream_failed=True, representative_name="Vera", acute_level="a1", already_fired=False)
    assert turn["resources_appended"] is True
    assert turn["empty_stream"] is True


def test_acute_distress_appends_even_when_call_failed_but_somehow_carried_text():
    """stream_failed=True dominates regardless of stream_text - a failed
    call's text (if any leaked through) is never trusted as 'not empty'."""
    turn = append_crisis_resources_turn(signal="ACUTE_DISTRESS", stream_text="some text", stream_failed=True, representative_name="Vera", acute_level="a1", already_fired=False)
    assert turn["empty_stream"] is True


def test_harmful_dynamic_signal_does_not_append_crisis_resources():
    """Track B (dependency dynamics) is not a crisis - resources are
    Track A's alone (Program-Spec SS8)."""
    turn = append_crisis_resources_turn(signal="HARMFUL_DYNAMIC_SIGNAL", stream_text="anything", stream_failed=False, representative_name="Vera", acute_level="a1", already_fired=False)
    assert turn["resources_appended"] is False
    assert turn["text"] is None


# ---- resources_for_signal: the A1/A2/continuation selection itself -------


def test_a1_is_the_default_first_firing_script():
    resources = resources_for_signal("ACUTE_DISTRESS", acute_level="a1", already_fired=False)
    assert "I want to step in for a moment" in resources.text


def test_a2_is_the_escalation_script_on_a_first_firing():
    resources = resources_for_signal("ACUTE_DISTRESS", acute_level="a2", already_fired=False)
    assert "I need to stop here and be straightforward with you" in resources.text


def test_already_fired_wins_the_continuation_turn_even_on_an_a2_reading():
    """SS4.4's "sustained attention": already_fired is a property of the
    SESSION, not of this turn's own escalation reading - it outranks
    acute_level. (Whether it should keep doing so is a separate, open
    governance question - not decided by this test.)"""
    resources = resources_for_signal("ACUTE_DISTRESS", acute_level="a2", already_fired=True)
    assert "I'm still right here with you" in resources.text


def test_continuation_still_carries_an_actual_redirect():
    """The continuation turn must always carry the same redirect language
    A1/A2 do, on every Track A turn in a session after the first - a
    warm-sounding continuation with no actual redirect sentence would leave
    a session's later turns without one."""
    resources = resources_for_signal("ACUTE_DISTRESS", acute_level="a1", already_fired=True)
    assert "reach out to someone real" in resources.text
    text = resources.text.format(representative_name="Vera")
    assert "not Vera" not in text  # continuation never claims to be Vera speaking
    assert "Vera" in text  # but still names the Representative in the reopen offer


def test_non_acute_signal_gets_no_resources_regardless_of_level_or_already_fired():
    assert resources_for_signal("HARMFUL_DYNAMIC_SIGNAL", acute_level="a2", already_fired=True) is None
    assert resources_for_signal("NO_SIGNAL", acute_level="none", already_fired=False) is None
