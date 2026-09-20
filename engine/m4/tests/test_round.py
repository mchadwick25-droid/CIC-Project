"""Table round resolution (Artifact-7 SS2): governed vs. bridged vs.
ordinary rounds, the session cap's placement (yields only to a real
crisis), the round config's floor/cap rules, and the continue
re-derivation contract - voice_message_for_round must produce the same
answer-target from the logged gate payload that the round open produced,
because a turn-at-a-time continue has nothing else to go on."""
from types import SimpleNamespace

import pytest

from engine.m4.round import (
    TABLE_SESSION_ROUND_CAP,
    RoundConfig,
    directive_from_payload,
    open_table_round,
    voice_message_for_round,
)
from engine.m4.turn import GateRun
from engine.m5.failure import CallOutcome
from engine.m5.routing import Directive

NAMES = ["Clement", "Papnoute"]


def _gate_run(
    *,
    action="voice_pass_through",
    reason="ordinary",
    safety_value=None,
    reader_value=None,
    directive=None,
    gate_overrides=None,
):
    safety_value = safety_value if safety_value is not None else {"signal": "NO_SIGNAL", "acute_level": "none"}
    reader_value = reader_value if reader_value is not None else {"asks": [], "out_of_scope": {"class": "none"}, "modern_terms": []}
    gate = {
        "asks": reader_value.get("asks", []),
        "register": None,
        "out_of_scope": reader_value.get("out_of_scope"),
        "modern_terms": reader_value.get("modern_terms", []),
        "safety": safety_value,
        "route": action,
        "directive": None,
        "degraded": False,
    }
    gate.update(gate_overrides or {})
    return GateRun(
        gate=gate,
        gate_result=SimpleNamespace(routing=SimpleNamespace(action=action, reason=reason, directive=directive), degraded=False),
        safety_outcome=CallOutcome(status="ok", value=safety_value),
        reader_outcome=CallOutcome(status="ok", value=reader_value),
        safety_state_events=[],
        usage_records=[],
    )


def _open(gate_run, *, rounds_completed=0, track_a_last=None, anachronistic_term_ids=frozenset()):
    return open_table_round(
        gate_run=gate_run,
        representative_names=NAMES,
        track_a_last=track_a_last,
        rounds_completed=rounds_completed,
        anachronistic_term_ids=set(anachronistic_term_ids),
    )


# --- round config (C3) ---


def test_round_config_defaults_and_bounds():
    config = RoundConfig()
    assert config.floor_for(2) == 3 and config.floor_for(3) == 5
    assert not config.close_allowed(2, num_seats=2)
    assert config.close_allowed(3, num_seats=2)
    assert not config.close_allowed(4, num_seats=3)
    assert config.close_allowed(5, num_seats=3)
    RoundConfig(cap_by_seats=((2, 5), (3, 6)))  # the re-tested ceiling is legal
    with pytest.raises(ValueError):
        RoundConfig(cap_by_seats=((2, 5), (3, 7)))  # beyond the re-tested ceiling
    with pytest.raises(ValueError):
        RoundConfig(floor_by_seats=((2, 6),), cap_by_seats=((2, 5),))  # floor above a configured cap
    with pytest.raises(ValueError):
        RoundConfig(default_cap=7)  # the fallback is bound by the same ceiling


def test_round_config_is_genuinely_immutable():
    """Independent review, 2026-09-05: a mutable dict field on a frozen
    dataclass used to defeat `frozen` twice over - unhashable, and mutable
    out from under it with no error. cap_by_seats is a tuple now."""
    config = RoundConfig()
    hash(config)  # does not raise
    with pytest.raises(AttributeError):
        config.cap_by_seats = ((2, 99),)


def test_round_config_seat_scaled_cap():
    """Mark's ruling, 2026-09-05: 'for 2 voices and a participant, the max
    turns should be 5... for 3 voices the cap is 6' - applied to every
    round, not gated behind any 'is this broad' judgment (his own explicit
    scoping, superseding this thread's first pass at a broad-only 5/6
    minimum)."""
    config = RoundConfig()
    assert config.cap_for(2) == 5
    assert config.cap_for(3) == 6
    assert not config.cap_reached(4, num_seats=2)
    assert config.cap_reached(5, num_seats=2)
    assert not config.cap_reached(5, num_seats=3)
    assert config.cap_reached(6, num_seats=3)
    # a table this project never seats (Artifact-7 SS1: world_keys 2-3)
    # falls back to the pre-existing default rather than raising
    assert config.cap_for(1) == config.default_cap == 4


def test_round_config_seat_scaled_floor():
    """Mark's ruling, 2026-09-05, later the same day, reversing the "soft
    target only" call for the floor specifically: investigated (root-
    caused from real selector_reason data, not guessed) why 3-seat rounds
    consistently closed right after the first pass while 2-seat rounds
    reliably reached a real second pass. The mechanism: the OLD flat floor
    of 3 happens to land past first-pass completion at 2 seats (forcing
    one bridging turn) but exactly at first-pass completion at 3 seats (no
    forced bridge). The first fix, "raise the floor to 4", restored that
    bridge - but a live round then closed AT that new floor too, on a
    full-table synthesis, and a structural fix for the synthesis itself
    (engine.m4.turn_selector.Selection.engages,
    engine.api.table_wiring._scoped_pending) proved on a live re-run that
    content quality and round length are independent: the returning turn
    engaged one voice genuinely, and the round still closed at 4 anyway.
    Only then, on that isolated evidence, did Mark rule "raise the floor
    to 5" - his own original "ultimate zone" target for a 3-seat table.
    The 2-seat floor (3) is untouched - it was never observed closing
    early relative to its own cap."""
    config = RoundConfig()
    assert config.floor_for(2) == 3
    assert config.floor_for(3) == 5
    # 3 seats: close is not legal until turn 5 - the round's only possible
    # close points are now 5 or 6, matching "5-6 interactions."
    assert not config.close_allowed(4, num_seats=3)
    assert config.close_allowed(5, num_seats=3)
    # 2 seats: unchanged - already forces a bridging turn past first pass
    # (turn 2) because the floor (3) was always one more than that.
    assert not config.close_allowed(2, num_seats=2)
    assert config.close_allowed(3, num_seats=2)


# --- round-level routing ---


def test_ordinary_round_lets_voices_speak():
    opening = _open(_gate_run())
    assert opening.voices_speak
    assert opening.facilitator_events == []
    assert not opening.session_capped


def test_governed_routes_close_with_no_voices():
    for action in ("check_in_turn", "system_nature_turn"):
        opening = _open(_gate_run(action=action))
        assert not opening.voices_speak
        assert len(opening.facilitator_events) == 1

    opening = _open(
        _gate_run(action="etic_turn", reader_value={"asks": [], "out_of_scope": {"class": "later_age"}, "modern_terms": []})
    )
    assert not opening.voices_speak
    assert "witnesses stop" in opening.facilitator_events[0]["text"]


def test_acute_crisis_is_governed_and_appends_resources():
    opening = _open(
        _gate_run(action="safety_turn", safety_value={"signal": "ACUTE_DISTRESS", "acute_level": "a1"})
    )
    assert not opening.voices_speak
    event = opening.facilitator_events[0]
    assert event["resources_appended"]
    # The Mark-approved slot filled with the or-joined names, text otherwise
    # untouched.
    assert "Clement or Papnoute" in event["text"]


def test_track_b_checks_and_silences_the_voices():
    opening = _open(
        _gate_run(action="safety_turn", safety_value={"signal": "HARMFUL_DYNAMIC_SIGNAL", "acute_level": "none"})
    )
    assert not opening.voices_speak  # amendment 2026-09-20: silenced, same as Track A above
    assert opening.facilitator_events[0]["resources_appended"] is False
    assert "Clement or Papnoute" in opening.facilitator_events[0]["text"]


def test_session_cap_fires_at_table_unit():
    opening = _open(_gate_run(), rounds_completed=TABLE_SESSION_ROUND_CAP)
    assert opening.session_capped
    assert not opening.voices_speak
    assert opening.routing_action == "session_cap_turn"


def test_acute_crisis_overrides_session_cap():
    opening = _open(
        _gate_run(action="safety_turn", safety_value={"signal": "ACUTE_DISTRESS", "acute_level": "a2"}),
        rounds_completed=TABLE_SESSION_ROUND_CAP,
    )
    assert not opening.session_capped
    assert opening.facilitator_events[0]["resources_appended"]


# --- bridge and continue re-derivation ---

_TERM_ID = None


def _find_fleet_bridge_term():
    """A real fleet modern_term record with an underlying_subject, so the
    bridge path is tested against authored data rather than a synthetic
    record shape."""
    global _TERM_ID
    if _TERM_ID is None:
        from engine.m1.loader import load_fleet_records

        fleet = load_fleet_records()
        _TERM_ID = next(
            tid for tid, rec in sorted(fleet.items())
            if rec.get("underlying_subject") and rec.get("modern_sense") and rec.get("display_terms")
        )
    return _TERM_ID


def test_bridge_round_speaks_sense_and_updates_gate_directive():
    term_id = _find_fleet_bridge_term()
    reader_value = {
        "asks": [{"order": 1, "text": "tell me about it"}],
        "register": "translational",
        "out_of_scope": {"class": "none"},
        "modern_terms": [{"term_id": term_id, "display": "the term"}],
        "ambiguity_options": [],
    }
    gate_run = _gate_run(
        action="bridge_turn",
        reader_value=reader_value,
        gate_overrides={"modern_terms": reader_value["modern_terms"], "route": "bridge_turn"},
    )
    opening = _open(gate_run, anachronistic_term_ids={term_id})
    assert opening.voices_speak
    assert opening.facilitator_events[0]["kind"] == "bridge"
    # The gate payload's directive was updated in place, so the caller logs
    # what the voices were actually handed - and the continue derivation
    # below reads it back.
    message, directive = voice_message_for_round(gate_run.gate, "original with the term", {term_id})
    from engine.m1.loader import load_fleet_records

    assert message == load_fleet_records()[term_id]["underlying_subject"].strip()
    assert message != "original with the term"


def test_ordinary_continue_rederives_message_and_directive():
    directive = Directive(asks=[{"order": 1, "text": "what is prayer"}], register_note=None)
    gate_payload = {
        "route": "voice_with_directive",
        "directive": {"asks": [{"order": 1, "text": "what is prayer"}], "register_note": None, "suspend_register_statement_1": False, "ambiguity_options": []},
        "modern_terms": [],
    }
    message, rebuilt = voice_message_for_round(gate_payload, "what is prayer?", set())
    assert message == "what is prayer?"
    assert rebuilt == directive


def test_directive_roundtrip_matches_turn_payload_shape():
    # round._directive_payload is a deliberate reproduction of
    # engine.m4.turn's - this pin fails if either side drifts.
    from engine.m4.round import _directive_payload as round_payload
    from engine.m4.turn import _directive_payload as turn_payload

    directive = Directive(
        asks=[{"order": 1, "text": "a"}], register_note="witness-before-answer licensed",
        suspend_register_statement_1=True, ambiguity_options=["x", "y"],
    )
    assert round_payload(directive) == turn_payload(directive)
    assert directive_from_payload(round_payload(directive)) == directive
    assert directive_from_payload(None) is None
    assert round_payload(None) is None
