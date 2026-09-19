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
    value={"signal": "NO_SIGNAL", "acute_level": "none", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "high"},
)
SAFETY_ACUTE = CallOutcome(
    status="ok",
    value={"signal": "ACUTE_DISTRESS", "acute_level": "a1", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "high"},
)
SAFETY_HARMFUL = CallOutcome(
    status="ok",
    value={"signal": "HARMFUL_DYNAMIC_SIGNAL", "acute_level": "none", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "high"},
)
SAFETY_AMBIGUOUS = CallOutcome(
    status="ok",
    value={"signal": "AMBIGUOUS_LOW_CONFIDENCE", "acute_level": "none", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "low"},
)


def test_both_ok_routes_normally_not_degraded():
    result = resolve_gate(safety_outcome=SAFETY_OK, reader_outcome=READER_OK, pressed={}, anachronistic_term_ids=set())
    assert result.degraded is False
    assert result.routing.action == "voice_with_directive"
    assert result.needs_async_safety_reclassification is False


def test_reader_timeout_is_pass_through_and_degraded():
    result = resolve_gate(
        safety_outcome=SAFETY_OK, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "voice_pass_through"
    assert result.routing.directive is None
    assert result.degraded is True
    assert result.needs_async_safety_reclassification is False


def test_reader_parse_failure_is_a_failure_not_salvaged():
    result = resolve_gate(
        safety_outcome=SAFETY_OK, reader_outcome=CallOutcome(status="parse_failure"), pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "voice_pass_through"
    assert result.degraded is True


def test_safety_failure_alone_fails_open_but_still_routes():
    result = resolve_gate(
        safety_outcome=CallOutcome(status="timeout"), reader_outcome=READER_OK, pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "voice_with_directive"  # reader-based routing still applies
    assert result.degraded is True
    assert result.needs_async_safety_reclassification is True


def test_reader_timeout_never_discards_a_successful_acute_classification():
    """Regression for the 2026-09-19 fix: a reader-call failure must not
    silently erase a successful ACUTE_DISTRESS finding from the safety call
    on the same turn. Before the fix, resolve_gate returned
    voice_pass_through unconditionally whenever the reader failed, so the
    Representative could answer a real crisis message directly if the
    unrelated reader call happened to time out."""
    result = resolve_gate(
        safety_outcome=SAFETY_ACUTE, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "safety_turn"
    assert result.degraded is True
    assert result.needs_async_safety_reclassification is False


def test_reader_timeout_never_discards_a_successful_harmful_dynamic_classification():
    result = resolve_gate(
        safety_outcome=SAFETY_HARMFUL, reader_outcome=CallOutcome(status="parse_failure"), pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "safety_turn"
    assert result.degraded is True
    assert result.needs_async_safety_reclassification is False


def test_reader_timeout_still_routes_a_successful_ambiguous_classification():
    result = resolve_gate(
        safety_outcome=SAFETY_AMBIGUOUS, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "check_in_turn"
    assert result.degraded is True
    assert result.needs_async_safety_reclassification is False


def test_reader_timeout_with_safety_no_signal_still_falls_to_pass_through():
    """The companion case: when safety succeeds but has nothing decisive to
    say (NO_SIGNAL), a reader failure still correctly falls through to
    pass-through - this is not a blanket "always trust safety" change."""
    result = resolve_gate(
        safety_outcome=SAFETY_OK, reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "voice_pass_through"
    assert result.degraded is True
    assert result.needs_async_safety_reclassification is False


def test_both_fail_collapses_to_pass_through():
    result = resolve_gate(
        safety_outcome=CallOutcome(status="error"), reader_outcome=CallOutcome(status="timeout"), pressed={}, anachronistic_term_ids=set()
    )
    assert result.routing.action == "voice_pass_through"
    assert result.degraded is True
    assert result.needs_async_safety_reclassification is True


def test_should_page_on_two_consecutive_degraded_turns():
    assert should_page_operator([True, True]) is True
    assert should_page_operator([False, True, True]) is True


def test_should_not_page_on_isolated_or_alternating_degraded_turns():
    assert should_page_operator([]) is False
    assert should_page_operator([True]) is False
    assert should_page_operator([True, False]) is False
    assert should_page_operator([True, True, False]) is False
