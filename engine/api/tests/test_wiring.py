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
    assert result.unhandled_routing_gap is False
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


def test_unhandled_routing_action_degrades_gracefully_and_stays_usable(store, usage_store, world_loader, registry, monkeypatch):
    """Every routing action the gate can take now has content behind it, so
    this forces the seam rather than reaching it through a real route. The
    net is still worth keeping: it is what stops a future action - or a bug
    in one of the seven - reaching a participant as a 500."""
    from engine.m4.turn import UnhandledRoutingAction

    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())

    def _boom(**kwargs):
        raise UnhandledRoutingAction("forced: a routing action with no content wired up")

    monkeypatch.setattr(wiring, "run_turn", _boom)

    result = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="msg",
    )

    assert result.unhandled_routing_gap is True
    assert result.degraded is True
    assert result.facilitator["kind"] == "threshold"
    assert result.turn_no == 1

    types = [e.event_type for e in store.read_events(session_id)]
    assert types == ["session_started", "participant_message", "facilitator_turn", "turn_committed"]

    # A second, ordinary message on the same session still works - turn
    # numbering and state stayed consistent through the gap.
    monkeypatch.undo()
    client2 = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    result2 = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client2, voice_model_id="m", safety_client=client2, safety_model_id="m",
        session_id=session_id, text="who was Jesus",
    )
    assert result2.turn_no == 2
    assert result2.unhandled_routing_gap is False


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
