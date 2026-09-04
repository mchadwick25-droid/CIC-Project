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
    assert [e.event_type for e in events] == ["session_started", "facilitator_turn"]
    assert events[0].payload["world_key"] == "fix"
    assert events[1].payload["kind"] == "door"

    from engine.m4.session_code import codes_match

    assert codes_match(raw_code, events[0].payload["code_hash"])


def test_create_session_unknown_world_raises(store, world_loader, registry):
    with pytest.raises(wiring.UnknownWorldError):
        wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="does-not-exist")


def test_a_repin_mid_session_does_not_refuse_the_in_flight_session(store, usage_store, world_loader, registry):
    """Regression, 2026-09-04: a live bug Mark hit on turn 3 of a real
    conversation, root-caused to _load_world() always resolving the package
    DIRECTORY through the registry's CURRENT pointer rather than the one a
    session actually verified against at open. A repin between session-open
    and a later turn (exactly what happened live - a routine records/
    worlds.yaml commit landing mid-conversation) made every later turn
    refuse with PackageRefused -> 503, permanently, for that session.

    Uses two of fix's own real, already-compiled historical packages
    (never deleted - packages/fix/*) rather than a synthetic fixture, so
    this proves the fix against real package bytes, not an idealization.
    Picked from packages actually holding full compiled bytes locally, not
    just the manifest.json committed history keeps (packages/README/
    .gitignore: compiled bytes are derived, not source)."""
    old_location, old_hash = (
        "packages/fix/2026-09-03T14-57-38Z",
        "sha256:e27e46abe8e11edf25375e64829d7e4ef9b47812aee8ac5d96a917e27452de0d",
    )
    new_location, new_hash = (
        "packages/fix/2026-09-04T01-37-28Z",
        "sha256:6aeda41fb4471b0066f7781f4660046b070854426c6b9a98bdc6eb10c541a652",
    )
    registry["fix"]["package"]["location"] = old_location
    registry["fix"]["package"]["manifest_hash"] = old_hash

    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    started = store.read_events(session_id)[0]
    assert started.payload["package_manifest_hash"] == old_hash
    assert started.payload["package_location"] == old_location

    # The repin: only the registry's pointer moves, same as a real
    # records/worlds.yaml commit - old_location's bytes are untouched.
    registry["fix"]["package"]["location"] = new_location
    registry["fix"]["package"]["manifest_hash"] = new_hash

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
    assert result.turn_no == 1  # did not raise PackageRefused

    # And a brand-new session opened AFTER the repin correctly pins the NEW
    # package - both stay independently correct in the same process/loader.
    session_id_2, _code_2 = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    started_2 = store.read_events(session_id_2)[0]
    assert started_2.payload["package_manifest_hash"] == new_hash
    assert started_2.payload["package_location"] == new_location


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
    assert types == ["session_started", "facilitator_turn", "participant_message", "gate_decision", "voice_turn", "turn_committed"]
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
    assert types == ["session_started", "facilitator_turn", "participant_message"]


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
    assert types == ["session_started", "facilitator_turn", "participant_message"]  # nothing after the failure point committed


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
    assert state.transcript[0]["kind"] == "door"
    assert state.transcript[1] == {"speaker": "participant", "text": "who was Jesus"}
    assert state.transcript[2]["speaker"] == "fix"


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
        "session_started", "facilitator_turn", "participant_message", "gate_decision", "voice_turn", "turn_committed",
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


def test_figures_used_flows_through_and_a_second_mention_this_session_does_not_re_fire(store, usage_store, world_loader, registry):
    """End to end against the REAL fix world's real figure record
    (records/fix/figure/fix.figure.the-elder.md, compiled unchanged) - not
    a synthetic fixture. First turn names "the Elder" and the bridge
    fires; second turn names him again and it does not, because
    handle_message derives already_bridged_figure_ids from the first
    turn's own figures_used, same as it already does for already_told_ids."""
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["The Elder spoke for us, and we remembered it [[fix.witness.who-is-jesus]]."],
    )

    first = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="who led you", client_msg_id="msg-1",
    )
    assert [f["id"] for f in first.voice["figures_used"]] == ["fix.figure.the-elder"]
    assert first.voice["figures_used"][0]["bridge_line"] == "an elder of this gathering, remembered for what he said about the ones who came after"

    second = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="tell me more about him", client_msg_id="msg-2",
    )
    assert second.voice["figures_used"] == []


def test_the_tenth_completed_turn_still_answers_and_the_eleventh_closes(store, usage_store, world_loader, registry):
    """Ten real turns through the actual handle_message path (not a faked
    history list) - the same real transcript-folding
    (history_from_transcript) engine.m4.turn.SESSION_TURN_CAP is measured
    against. The eleventh message gets the graceful redirect instead of an
    answer, and the session_closed event lands with reason="cap"."""
    from engine.m4 import turn as turn_module

    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )

    for i in range(turn_module.SESSION_TURN_CAP):
        result = wiring.handle_message(
            store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
            voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
            session_id=session_id, text=f"question {i}", client_msg_id=f"msg-{i}",
        )
        assert result.routing_action != "session_cap_turn", f"capped early, on turn {i}"

    capped = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text="one more question", client_msg_id="msg-cap",
    )
    assert capped.routing_action == "session_cap_turn"
    assert capped.facilitator["kind"] == "close"
    assert capped.voice is None

    types = [e.event_type for e in store.read_events(session_id)]
    assert types[-2:] == ["session_closed", "turn_committed"]
    closed_events = [e for e in store.read_events(session_id) if e.event_type == "session_closed"]
    assert closed_events[0].payload["reason"] == "cap"

    state = wiring.get_transcript(store, session_id)
    assert state.closed is True

    with pytest.raises(wiring.SessionClosed):
        wiring.handle_message(
            store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
            voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
            session_id=session_id, text="are you still there", client_msg_id="msg-after-close",
        )


def test_list_worlds_excludes_the_fixture_and_carries_the_doorway_fields(world_loader, registry):
    worlds = wiring.list_worlds(world_loader=world_loader, registry=registry)

    assert "fix" not in {w["world_key"] for w in worlds}
    assert {w["world_key"] for w in worlds} == {k for k, v in registry.items() if v.get("kind") == "formation"}

    pahc = next(w for w in worlds if w["world_key"] == "pahc")
    assert pahc["display_name"] == "Post-Apostolic House-Church Christianity"
    assert pahc["representative"] == {"name": "Chloe", "role_label": "Household Leader"}
    assert pahc["census_id"] == "post-apostolic-house-church"
    assert pahc["horizon"] and "Antioch" in pahc["horizon"]
    assert pahc["thinness_statement"]
    assert pahc["starters"] and all({"cell", "text"} <= s.keys() for s in pahc["starters"])
    assert "_generated_by" not in pahc
