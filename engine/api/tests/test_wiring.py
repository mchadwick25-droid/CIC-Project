"""Hermetic (no live model call) tests for engine.api.wiring - does it
translate a TurnResult into the right event-log/usage-log writes, in the
right order, including the two branches run_turn() itself doesn't fully
handle content for (crisis, unhandled routing)."""
import pytest

from engine.api import wiring
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response


def test_create_session_opens_exactly_one_session_started(store, world_loader, registry):
    session_id, raw_code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    events = store.read_events(session_id)
    assert len(events) == 1
    assert events[0].event_type == "session_started"
    assert events[0].payload["world_key"] == "fix"

    from engine.m4.session_code import codes_match

    assert codes_match(raw_code, events[0].payload["code_hash"])


def test_create_session_unknown_world_raises(store, world_loader, registry):
    with pytest.raises(wiring.UnknownWorldError):
        wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="does-not-exist")


def test_ordinary_message_appends_events_in_order(store, usage_store, world_loader, registry):
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )

    result = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="who was Jesus", client_msg_id="msg-1",
    )

    assert result.routing_action == "voice_with_directive"
    assert result.voice["text"] == "We did not claim to have seen him ourselves."
    assert result.turn_no == 1

    types = [e.event_type for e in store.read_events(session_id)]
    assert types == ["session_started", "participant_message", "gate_decision", "voice_turn", "turn_committed"]
    assert len(usage_store.read_for_session(session_id)) == 3  # safety_call, reader_call, voice_generation


def test_safety_turn_appends_facilitator_turn_kind_safety(store, usage_store, world_loader, registry):
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("ACUTE_DISTRESS"), reader_response=reader_response(), stream_chunks=["I hear you."]
    )

    result = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="I don't want to be here anymore.",
    )

    assert result.routing_action == "safety_turn"
    assert result.facilitator["kind"] == "safety"
    assert result.facilitator["resources_appended"] is True

    types = [e.event_type for e in store.read_events(session_id)]
    assert "facilitator_turn" in types
    assert types[-1] == "turn_committed"


def test_an_unhandled_routing_action_surfaces_as_itself(store, usage_store, world_loader, registry, monkeypatch):
    """The graceful-degradation path this replaces existed because four
    routing actions genuinely had no content. All seven do now, so it was
    deleted along with the permanently-false unhandled_routing_gap field.

    The guard stays, and must not be swallowed by the provider-failure
    catch: an eighth routing action added without a branch is a programming
    error, and reporting it to an operator as a Bedrock outage would send
    them looking in the wrong place. Nothing commits - the turn never
    happened."""
    from engine.m4.turn import UnhandledRoutingAction

    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())

    def _boom(**kwargs):
        raise UnhandledRoutingAction("forced: an eighth routing action with no branch")

    monkeypatch.setattr(wiring, "run_turn", _boom)

    with pytest.raises(UnhandledRoutingAction):
        wiring.handle_message(
            store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
            voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
            session_id=session_id, text="msg",
        )

    # The participant's message is committed before the turn runs, exactly
    # as it is on a provider failure; no turn is committed on top of it.
    types = [e.event_type for e in store.read_events(session_id)]
    assert types == ["session_started", "participant_message"]


def test_handle_message_unknown_session_raises(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    with pytest.raises(wiring.SessionNotFound):
        wiring.handle_message(
            store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
            voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
            session_id="does-not-exist", text="msg",
        )


def test_provider_failure_commits_the_message_but_not_the_turn(store, usage_store, world_loader, registry):
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")

    class _ExplodingClient:
        class messages:
            @staticmethod
            def create(**kwargs):
                raise RuntimeError("simulated credential failure")

    with pytest.raises(wiring.ProviderCallFailed):
        wiring.handle_message(
            store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
            voice_client=_ExplodingClient(), voice_model_id="m", safety_client=_ExplodingClient(), safety_model_id="m",
            session_id=session_id, text="msg",
        )

    types = [e.event_type for e in store.read_events(session_id)]
    assert types == ["session_started", "participant_message"]  # nothing after the failure point committed


def test_get_transcript_reflects_committed_turns(store, usage_store, world_loader, registry):
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="who was Jesus",
    )

    state = wiring.get_transcript(store, session_id)
    assert state.turn_count == 1
    assert state.transcript[0] == {"speaker": "participant", "text": "who was Jesus"}
    assert state.transcript[1]["speaker"] == "fix"


def test_get_transcript_unknown_session_raises(store):
    with pytest.raises(wiring.SessionNotFound):
        wiring.get_transcript(store, "does-not-exist")


def test_a_pressable_class_asked_twice_reaches_the_etic_turn(store, usage_store, world_loader, registry):
    """The gap this closes was proven live (pahc, 2026-08-24): routing's
    rule 5 reads `pressed` from SessionState, SessionState folds `pressed`
    from escalation_pressed, and nothing in the build ever appended that
    event - so every ask was a first ask and etic_turn was unreachable.
    Two identical later_age asks, and the second one must not be the first
    one again."""
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(out_of_scope={"class": "later_age"}),
        stream_chunks=["We never heard of it [[fix.witness.who-is-jesus]]."],
    )
    call = dict(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id,
    )

    first = wiring.handle_message(**call, text="what did you make of Nicaea", client_msg_id="msg-1")
    assert first.routing_action == "voice_with_directive"
    assert "escalation_pressed" in [e.event_type for e in store.read_events(session_id)]

    second = wiring.handle_message(**call, text="I know, but what did you make of Nicaea", client_msg_id="msg-2")
    assert second.routing_action == "etic_turn"
    assert second.facilitator["kind"] == "threshold"
    assert second.voice is None


def test_an_ordinary_turn_presses_nothing(store, usage_store, world_loader, registry):
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="who was Jesus", client_msg_id="msg-1",
    )
    assert "escalation_pressed" not in [e.event_type for e in store.read_events(session_id)]


def test_the_gate_decision_event_records_what_the_gate_said(store, usage_store, world_loader, registry):
    """Until 2026-08-24 this payload was hand-built blank in wiring - asks,
    register, out_of_scope, modern_terms, safety and directive hardcoded
    empty on every gate_decision this build ever logged. The event existed;
    the record did not."""
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(register="personal_wound", out_of_scope={"class": "later_age"}),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="who was Jesus", client_msg_id="msg-1",
    )
    gate = next(e for e in store.read_events(session_id) if e.event_type == "gate_decision").payload
    assert gate["register"] == "personal_wound"
    assert gate["out_of_scope"] == {"class": "later_age"}
    assert gate["asks"] == [{"order": 1, "text": "who was Jesus"}]
    assert gate["safety"]["signal"] == "NO_SIGNAL"
    assert gate["route"] == "voice_with_directive"
    assert gate["degraded"] is False
    # the directive the voice was actually given, not a reconstruction
    assert gate["directive"]["suspend_register_statement_1"] is True
    assert gate["directive"]["register_note"] == "witness-before-answer licensed"


def test_the_pressed_class_is_read_from_the_recorded_gate_decision(store, usage_store, world_loader, registry):
    """One source for the class: whatever the event log says is what the
    escalation_pressed append used, so the two can never disagree."""
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(out_of_scope={"class": "other_tradition"}),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="what did the Marcionites teach", client_msg_id="msg-1",
    )
    events = store.read_events(session_id)
    gate = next(e for e in events if e.event_type == "gate_decision").payload
    pressed = next(e for e in events if e.event_type == "escalation_pressed").payload
    assert pressed["class"] == gate["out_of_scope"]["class"] == "other_tradition"


def test_the_accumulator_is_written_and_folds_across_turns(store, usage_store, world_loader, registry):
    """The event was declared in engine.m4.events, folded in
    engine.m4.projection, and appended by nothing - so track_b_accumulator
    was permanently None and Track B's "accumulating across the session"
    (Program-Spec SS210) did not accumulate."""
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("HARMFUL_DYNAMIC_SIGNAL", dynamic_tags=["CONFIDANT_LANGUAGE"]),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    call = dict(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id,
    )
    wiring.handle_message(**call, text="you are the only one who gets me", client_msg_id="msg-1")
    wiring.handle_message(**call, text="you are still the only one who gets me", client_msg_id="msg-2")

    states = [e.payload for e in store.read_events(session_id) if e.event_type == "safety_state"]
    assert [s["accumulator"] for s in states] == [
        {"CONFIDANT_LANGUAGE": 1},
        {"CONFIDANT_LANGUAGE": 2},
    ]
    from engine.m4.projection import project_fresh

    assert project_fresh(session_id, store).safety.track_b_accumulator == {"CONFIDANT_LANGUAGE": 2}


def test_the_accumulator_changes_no_routing(store, usage_store, world_loader, registry):
    """The promise this change makes: it records, it decides nothing. A turn
    with a loaded accumulator behind it routes exactly as the first one did,
    because no threshold reads it."""
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("HARMFUL_DYNAMIC_SIGNAL", dynamic_tags=["CONFIDANT_LANGUAGE"]),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    call = dict(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id,
    )
    first = wiring.handle_message(**call, text="you are the only one who gets me", client_msg_id="msg-1")
    third = None
    for n in (2, 3):
        third = wiring.handle_message(**call, text="still only you", client_msg_id=f"msg-{n}")
    assert first.routing_action == third.routing_action == "safety_turn"


def test_an_ordinary_turn_writes_no_safety_state(store, usage_store, world_loader, registry):
    """Most turns append nothing - an event per turn forever is how a log
    stops being readable."""
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="who was Jesus", client_msg_id="msg-1",
    )
    assert [e.event_type for e in store.read_events(session_id)] == [
        "session_started", "participant_message", "gate_decision", "voice_turn", "turn_committed",
    ]


def test_an_acute_turn_records_the_level_for_audit(store, usage_store, world_loader, registry):
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("ACUTE_DISTRESS", acute_level="a2", risk_subject="self"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="a disclosure", client_msg_id="msg-1",
    )
    from engine.m4.projection import project_fresh

    track_a = project_fresh(session_id, store).safety.track_a_last
    assert track_a["level"] == "a2"
    assert track_a["risk_subject"] == "self"
    assert project_fresh(session_id, store).safety.track_b_accumulator is None
