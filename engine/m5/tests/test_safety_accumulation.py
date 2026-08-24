"""The writer, and the things the spec forbids it to do."""
from engine.m5.safety_accumulation import (
    TRACK_B_LEVEL_UNEVALUATED,
    safety_state_events,
    tags_for,
    track_a_state,
    track_b_state,
)


def _safety(signal, tags=(), acute_level="none", risk_subject="not_applicable", confidence="high"):
    return {"signal": signal, "acute_level": acute_level, "risk_subject": risk_subject,
            "dynamic_tags": list(tags), "confidence": confidence}


# ---- what banks, and what must never bank -------------------------------


def test_a_harmful_dynamic_signal_banks_its_tags():
    state = track_b_state(None, _safety("HARMFUL_DYNAMIC_SIGNAL", ["CONFIDANT_LANGUAGE"]))
    assert state["accumulator"] == {"CONFIDANT_LANGUAGE": 1}
    assert state["track"] == "B"


def test_counts_add_across_turns():
    first = track_b_state(None, _safety("HARMFUL_DYNAMIC_SIGNAL", ["CONFIDANT_LANGUAGE"]))
    second = track_b_state(first["accumulator"], _safety("HARMFUL_DYNAMIC_SIGNAL", ["CONFIDANT_LANGUAGE", "RETURN_COMPULSION"]))
    assert second["accumulator"] == {"CONFIDANT_LANGUAGE": 2, "RETURN_COMPULSION": 1}


def test_a_tag_counts_once_per_turn_not_once_per_mention():
    """SS4.3's threshold is written in turns - "two CONFIDANT_LANGUAGE tags
    within a session" - so counting mentions inside one message would
    inflate it against its own wording."""
    state = track_b_state(None, _safety("HARMFUL_DYNAMIC_SIGNAL", ["CONFIDANT_LANGUAGE", "CONFIDANT_LANGUAGE"]))
    assert state["accumulator"] == {"CONFIDANT_LANGUAGE": 1}


def test_historical_otherness_disorientation_never_banks_anything():
    """"The encounter working as designed, never harm" - Program-Spec SS72.
    Tags arriving alongside it are discarded, not banked."""
    assert tags_for(_safety("HISTORICAL_OTHERNESS_DISORIENTATION", ["CONFIDANT_LANGUAGE"])) == []
    assert track_b_state({"CONFIDANT_LANGUAGE": 1}, _safety("HISTORICAL_OTHERNESS_DISORIENTATION", ["CONFIDANT_LANGUAGE"])) is None


def test_no_signal_banks_nothing():
    assert track_b_state({"CONFIDANT_LANGUAGE": 1}, _safety("NO_SIGNAL")) is None


def test_acute_distress_does_not_accumulate():
    """Track A "acts on the single message"; Track B is the one that
    accumulates (Program-Spec SS210)."""
    assert track_b_state(None, _safety("ACUTE_DISTRESS", acute_level="a2", risk_subject="self")) is None


# ---- the ambiguous case, which is why this module exists ----------------


def test_an_ambiguous_signal_leaves_a_trace_even_with_no_tags_returned():
    """Measured live 2026-08-24: both AMBIGUOUS_LOW_CONFIDENCE messages came
    back with an empty tag list. SS4.2 says the weak signal is logged, so code
    names it or it is not recorded at all - and the check-in turn asks the
    participant a question whose answer would otherwise reach a gate with no
    memory of having asked."""
    state = track_b_state(None, _safety("AMBIGUOUS_LOW_CONFIDENCE"))
    assert state["accumulator"] == {"DISTRESS_ADJACENT": 1}


def test_the_weak_tag_is_not_doubled_when_the_classifier_returns_it_too():
    state = track_b_state(None, _safety("AMBIGUOUS_LOW_CONFIDENCE", ["DISTRESS_ADJACENT"]))
    assert state["accumulator"] == {"DISTRESS_ADJACENT": 1}


# ---- Track A's audit record ---------------------------------------------


def test_track_a_records_the_level_that_was_recorded_nowhere():
    """"The level recorded for audit priority" (Program-Spec SS210) - a1 and
    a2 were indistinguishable in every log this build had written."""
    state = track_a_state(_safety("ACUTE_DISTRESS", acute_level="a2", risk_subject="third_party"))
    assert state == {"track": "A", "level": "a2", "accumulator": {}, "risk_subject": "third_party"}


def test_track_a_is_silent_for_every_other_signal():
    assert track_a_state(_safety("HARMFUL_DYNAMIC_SIGNAL", ["CONFIDANT_LANGUAGE"])) is None


# ---- what gets written, and what deliberately does not ------------------


def test_nothing_is_written_when_nothing_changed():
    """The fold takes the latest event per track and each event carries its
    own full value, so a turn that banks nothing has nothing to say. One row
    per turn forever is how a log stops being readable."""
    assert safety_state_events({"CONFIDANT_LANGUAGE": 1}, _safety("NO_SIGNAL")) == []


def test_nothing_is_written_when_the_safety_call_failed():
    """Inventing a neutral classification would put a claim in the log that
    no classifier ever made."""
    assert safety_state_events(None, None) == []


def test_an_acute_turn_writes_track_a_only():
    events = safety_state_events(None, _safety("ACUTE_DISTRESS", acute_level="a1", risk_subject="self"))
    assert [e["track"] for e in events] == ["A"]


def test_track_b_level_says_it_was_not_evaluated():
    """Writing "none" would read as "evaluated, below threshold". No
    threshold is computed in this build, and the log must not imply one."""
    state = track_b_state(None, _safety("HARMFUL_DYNAMIC_SIGNAL", ["RETURN_COMPULSION"]))
    assert state["level"] == TRACK_B_LEVEL_UNEVALUATED


def test_the_previous_accumulator_is_not_mutated():
    previous = {"CONFIDANT_LANGUAGE": 1}
    track_b_state(previous, _safety("HARMFUL_DYNAMIC_SIGNAL", ["CONFIDANT_LANGUAGE"]))
    assert previous == {"CONFIDANT_LANGUAGE": 1}
