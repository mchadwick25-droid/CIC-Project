from engine.m5.failure import CallOutcome, resolve_gate, should_page_operator

READER_OK = CallOutcome(
    status="ok",
    value={
        "asks": [{"order": 1, "text": "who was Jesus"}],
        "register": "informational",
        "clarity": "clear",
        "ambiguity_options": [],
        "out_of_scope": {"class": "none"},
        "modern_terms": [],
    },
)
SAFETY_OK = CallOutcome(
    status="ok",
    value={"signal": "NO_SIGNAL", "acute_level": "none", "risk_subject": "not_applicable", "check_in_reason": "not_applicable", "dynamic_tags": [], "confidence": "high"},
)
SAFETY_ACUTE = CallOutcome(
    status="ok",
    value={"signal": "ACUTE_DISTRESS", "acute_level": "a1", "risk_subject": "not_applicable", "check_in_reason": "not_applicable", "dynamic_tags": [], "confidence": "high"},
)
SAFETY_HARMFUL = CallOutcome(
    status="ok",
    value={"signal": "HARMFUL_DYNAMIC_SIGNAL", "acute_level": "none", "risk_subject": "not_applicable", "check_in_reason": "not_applicable", "dynamic_tags": [], "confidence": "high"},
)
SAFETY_AMBIGUOUS = CallOutcome(
    status="ok",
    value={"signal": "AMBIGUOUS_LOW_CONFIDENCE", "acute_level": "none", "risk_subject": "not_applicable", "check_in_reason": "not_applicable", "dynamic_tags": [], "confidence": "low"},
)


def test_both_ok_routes_normally_not_degraded():
    result = resolve_gate(
        safety_outcome=SAFETY_OK, reader_outcome=READER_OK, pressed={}, anachronistic_term_ids=set(), message="who was Jesus"
    )
    assert result.degraded is False
    assert result.routing.action == "voice_with_directive"


def test_reader_timeout_is_pass_through_and_degraded():
    result = resolve_gate(
        safety_outcome=SAFETY_OK, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert result.routing.action == "voice_pass_through"
    assert result.routing.directive is None
    assert result.degraded is True


def test_reader_parse_failure_is_a_failure_not_salvaged():
    result = resolve_gate(
        safety_outcome=SAFETY_OK, reader_outcome=CallOutcome(status="parse_failure"), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert result.routing.action == "voice_pass_through"
    assert result.degraded is True


def test_safety_failure_goes_to_the_fixed_line_with_the_redirect_never_the_voice():
    for status in ("timeout", "error", "parse_failure"):
        result = resolve_gate(
            safety_outcome=CallOutcome(status=status), reader_outcome=READER_OK, pressed={}, anachronistic_term_ids=set(),
            message="who was Jesus",
        )
        assert result.routing.action == "safety_unread_turn"
        assert result.degraded is True


def test_reader_timeout_never_discards_a_successful_acute_classification():
    """Regression: a reader-call failure must not
    silently erase a successful ACUTE_DISTRESS finding from the safety call
    on the same turn. Returning
    voice_pass_through unconditionally whenever the reader failed would let the
    Representative answer a real crisis message directly if the
    unrelated reader call happened to time out."""
    result = resolve_gate(
        safety_outcome=SAFETY_ACUTE, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert result.routing.action == "safety_turn"
    assert result.degraded is True


def test_reader_timeout_never_discards_a_successful_harmful_dynamic_classification():
    result = resolve_gate(
        safety_outcome=SAFETY_HARMFUL, reader_outcome=CallOutcome(status="parse_failure"), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert result.routing.action == "safety_turn"
    assert result.degraded is True


def test_reader_timeout_still_routes_a_successful_ambiguous_classification():
    result = resolve_gate(
        safety_outcome=SAFETY_AMBIGUOUS, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert result.routing.action == "check_in_turn"
    assert result.degraded is True


def test_reader_timeout_with_safety_no_signal_still_falls_to_pass_through():
    """The companion case: when safety succeeds but has nothing decisive to
    say (NO_SIGNAL), a reader failure still correctly falls through to
    pass-through - this is not a blanket "always trust safety" change."""
    result = resolve_gate(
        safety_outcome=SAFETY_OK, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set(),
        message="who was Jesus",
    )
    assert result.routing.action == "voice_pass_through"
    assert result.degraded is True


def test_both_fail_goes_to_the_fixed_line_with_the_redirect():
    result = resolve_gate(
        safety_outcome=CallOutcome(status="error"), reader_outcome=CallOutcome(status="timeout"), pressed={},
        anachronistic_term_ids=set(), message="who was Jesus",
    )
    assert result.routing.action == "safety_unread_turn"
    assert result.degraded is True


def test_should_page_on_two_consecutive_degraded_turns():
    assert should_page_operator([True, True]) is True
    assert should_page_operator([False, True, True]) is True


def test_should_not_page_on_isolated_or_alternating_degraded_turns():
    assert should_page_operator([]) is False
    assert should_page_operator([True]) is False
    assert should_page_operator([True, False]) is False
    assert should_page_operator([True, True, False]) is False


def _loss(signal="AMBIGUOUS_LOW_CONFIDENCE"):
    value = dict(SAFETY_AMBIGUOUS.value, signal=signal, check_in_reason="loss_to_suicide")
    return CallOutcome(status="ok", value=value)


def test_reader_failure_still_routes_a_personal_check_in_and_carries_the_reason():
    from engine.m4.facilitator_turns import check_in_turn
    from engine.m5.routing import check_in_reason_for

    outcome = _loss()
    result = resolve_gate(safety_outcome=outcome, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set(), message="msg")
    assert result.routing.action == "check_in_turn"
    assert check_in_turn(check_in_reason_for(outcome.value))["check_in_reason"] == "loss_to_suicide"


def test_reader_failure_with_a_personal_reason_on_a_non_ambiguous_signal_still_checks_in():
    result = resolve_gate(safety_outcome=_loss("NO_SIGNAL"), reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set(), message="msg")
    assert result.routing.action == "check_in_turn"


def test_reader_failure_after_the_check_in_was_shown_falls_to_pass_through():
    result = resolve_gate(
        safety_outcome=_loss(), reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set(),
        message="msg", check_ins_shown=frozenset({"loss_to_suicide"}),
    )
    assert result.routing.action == "voice_pass_through"
