"""HTTP-shape tests for engine.api.app - TestClient against create_app()
with fakes, never the real env-driven `app` instance (which stays None
unless CIC_API_REGION is set - see app.py's own module docstring)."""
import pytest
from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.api.wiring import history_from_transcript as _history_from


def _client(*, store, usage_store, world_loader, registry, voice_client=None, safety_client=None, default_world_key="fix", r27_enforce=False, **extra):
    client = voice_client or FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    app = create_app(
        voice_client=client,
        voice_model_id="m",
        safety_client=safety_client or client,
        safety_model_id="m",
        store=store,
        usage_store=usage_store,
        world_loader=world_loader,
        registry=registry,
        default_world_key=default_world_key,
        r27_enforce=r27_enforce,
        **extra,
    )
    return TestClient(app)


def test_health(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_list_worlds(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.get("/api/worlds")
    assert resp.status_code == 200
    worlds = resp.json()["worlds"]
    assert "fix" not in {w["world_key"] for w in worlds}
    assert len(worlds) == sum(1 for v in registry.values() if v.get("kind") == "formation" and v.get("package"))
    pahc = next(w for w in worlds if w["world_key"] == "pahc")
    assert pahc["display_name"] == "Post-Apostolic Household-Church Christianity"
    assert pahc["horizon"]
    assert pahc["starters"]
    assert pahc["app"] == registry["pahc"]["app"]
    assert {w["app"]["order"] for w in worlds} == set(range(1, len(worlds) + 1))


def test_create_session_with_no_world_is_refused(store, usage_store, world_loader, registry):
    """POST {} must not seat a session on default_world_key - production
    configures that as the synthetic fixture world the registry says must
    never be participant-reachable. A session names its world or doesn't
    open."""
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.post("/api/session", json={})
    assert resp.status_code == 400
    assert "world_key" in resp.json()["detail"]


def test_create_session_explicit_world(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.post("/api/session", json={"world_key": "fix"})
    assert resp.status_code == 201
    # Stage 0c (Build-Plan.md): no round cap applies to an interview session.
    assert resp.json()["round_cap"] is None


def test_create_session_unknown_world(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.post("/api/session", json={"world_key": "does-not-exist"})
    assert resp.status_code == 400


def test_message_happy_path(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client)
    created = http.post("/api/session", json={"world_key": "fix"}).json()

    resp = http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": "who was Jesus"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["routing_action"] == "voice_with_directive"
    assert body["voice"]["text"] == "We did not claim to have seen him ourselves."


def test_message_over_the_hard_bound_is_refused_before_any_provider_call(store, usage_store, world_loader, registry):
    """The API's hard bound still stops a payload attack before the route
    handler, and so before any provider call."""
    from engine.api.app import _HARD_MAX_MESSAGE_LENGTH

    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client)
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    resp = http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": "x" * (_HARD_MAX_MESSAGE_LENGTH + 1)},
    )
    assert resp.status_code == 422
    assert client.messages.stream_calls == []


def test_an_over_long_message_is_read_by_the_safety_call_then_refused_without_a_voice_call(store, usage_store, world_loader, registry):
    """System Hub decision 35: between 4,000 characters and the hard bound,
    the safety call reads the message first; with no safety route it is
    refused as before, and the voice is never called."""
    from engine.api.wiring import MAX_MESSAGE_LENGTH

    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client)
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    resp = http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": "x" * (MAX_MESSAGE_LENGTH + 1)},
    )
    assert resp.status_code == 422 and "too long" in resp.json()["detail"]
    assert client.messages.stream_calls == []


def test_message_wrong_code_and_missing_session_are_identical_401(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    created = http.post("/api/session", json={"world_key": "fix"}).json()

    wrong_code_resp = http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": "Session 0000-0000-0000-0000-0000-0000-00"},
        json={"text": "hi"},
    )
    missing_session_resp = http.post(
        "/api/session/does-not-exist/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": "hi"},
    )
    assert wrong_code_resp.status_code == 401
    assert missing_session_resp.status_code == 401
    assert wrong_code_resp.json() == missing_session_resp.json() == {"detail": "invalid session"}


def test_an_unhandled_routing_action_is_not_reported_as_a_provider_failure(store, usage_store, world_loader, registry, monkeypatch):
    """This used to assert a 200 with unhandled_routing_gap: true, because
    four routing actions genuinely had no content and a participant meeting
    one deserved a graceful turn rather than an error. All seven have
    content now; that field is gone from the response schema with the state
    it described.

    What is left to protect is the operator's diagnosis. An eighth routing
    action added without a branch must not come back as 502 provider-call-
    failed, which would send someone hunting a Bedrock outage that is not
    happening."""
    from engine.api import wiring
    from engine.m4.turn import UnhandledRoutingAction

    def _boom(**kwargs):
        raise UnhandledRoutingAction("forced: an eighth routing action with no branch")

    monkeypatch.setattr(wiring, "run_turn", _boom)
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client)
    created = http.post("/api/session", json={"world_key": "fix"}).json()

    with pytest.raises(UnhandledRoutingAction):
        http.post(
            f"/api/session/{created['session_id']}/message",
            headers={"Authorization": f"Session {created['session_code']}"},
            json={"text": "msg"},
        )


def test_transcript_reflects_committed_turns(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client)
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    headers = {"Authorization": f"Session {created['session_code']}"}
    http.post(f"/api/session/{created['session_id']}/message", headers=headers, json={"text": "who was Jesus"})

    resp = http.get(f"/api/session/{created['session_id']}/transcript", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["turn_count"] == 1
    assert body["transcript"][0]["kind"] == "door"
    assert body["transcript"][1] == {"speaker": "participant", "text": "who was Jesus"}
    # Stage 0c (Build-Plan.md): no round cap applies to an interview session.
    assert body["round_cap"] is None


def test_transcript_missing_session_401(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.get("/api/session/does-not-exist/transcript", headers={"Authorization": "Session x"})
    assert resp.status_code == 401


def test_history_replays_shown_text_skips_the_facilitator_and_stays_alternating():
    transcript = [
        {"speaker": "participant", "text": "who is jesus"},
        {"speaker": "alx", "text": "He was God's own Word."},
        {"speaker": "participant", "text": "are you an ai"},
        {"speaker": "facilitator", "kind": "threshold", "text": "We use AI, and here is how."},
        {"speaker": "participant", "text": "what did that cost"},
        {"speaker": "alx", "text": "It cost blood, first."},
    ]
    h = _history_from(transcript)
    assert [m["role"] for m in h] == ["user", "assistant", "user", "assistant"]
    # the facilitator's answer is not put in the Representative's mouth,
    # and the participant turn it answered does not dangle
    assert all("We use AI" not in m["content"] for m in h)
    assert [m["content"] for m in h if m["role"] == "user"] == ["who is jesus", "what did that cost"]


def test_history_replays_the_citations_that_verified():
    """The measured failure this exists to stop: over six live turns on
    desert the voice cited 9 sentences, then 6, then 0, 0, 0, 0 - it read
    its own untagged history and copied it. Session memory was teaching it
    to stop citing."""
    transcript = [
        {"speaker": "participant", "text": "who is jesus"},
        {
            "speaker": "alx",
            "text": "He was God's own Word. We argued about it for a century.",
            "citations": [{"sentence": "He was God's own Word.", "record_ids": ["alx.dw.jesus"]}],
        },
    ]
    said = _history_from(transcript)[1]["content"]
    # the tag goes back on, BEFORE the stop, so a sentence split cannot
    # carry it onto the next sentence
    assert said == "He was God's own Word [[alx.dw.jesus]]. We argued about it for a century."


def test_a_sentence_the_net_withheld_keeps_its_text_and_loses_its_tag():
    """The net gates decoration, not text - a withheld sentence WAS shown
    to the participant, so the model has to hear itself say it. It just
    does not come back carrying a citation the net rejected."""
    transcript = [
        {"speaker": "participant", "text": "who taught you"},
        {
            "speaker": "alx",
            "text": "Clement taught here. Some four hundred of us studied under him.",
            # only the first sentence verified; the figure was withheld
            "citations": [{"sentence": "Clement taught here.", "record_ids": ["alx.figure.clement"]}],
        },
    ]
    said = _history_from(transcript)[1]["content"]
    assert "Some four hundred of us studied under him." in said
    assert said.count("[[") == 1


def test_a_fabricated_record_id_is_never_replayed():
    """Turn 1 of the same live run tagged three sentences to
    desert.dw.f6-e-struggle-interior and
    desert.dw.f1-i-discernment-contemplation. Neither record exists. The
    net caught both, so neither reaches `citations` - and a fabricated id
    must never come back as an example of how to cite."""
    transcript = [
        {"speaker": "participant", "text": "why the desert"},
        {
            "speaker": "desert",
            "text": "A path to give everything had closed. We went looking for another one.",
            "citations": [],  # both tags were unresolvable, so nothing verified
        },
    ]
    said = _history_from(transcript)[1]["content"]
    assert "[[" not in said
    assert said.startswith("A path to give everything had closed.")


def test_a_sentence_with_two_tags_replays_both():
    transcript = [
        {"speaker": "participant", "text": "tell me"},
        {
            "speaker": "alx",
            "text": "We taught and we argued.",
            "citations": [{"sentence": "We taught and we argued.", "record_ids": ["alx.a.one", "alx.b.two"]}],
        },
    ]
    said = _history_from(transcript)[1]["content"]
    assert said == "We taught and we argued [[alx.a.one]] [[alx.b.two]]."


def test_a_turn_with_no_citations_replays_unchanged():
    transcript = [
        {"speaker": "participant", "text": "who is jesus"},
        {"speaker": "alx", "text": "We will not invent what we do not have."},
    ]
    assert _history_from(transcript)[1]["content"] == "We will not invent what we do not have."


def test_a_voice_turn_the_net_emptied_leaves_no_dangling_role():
    transcript = [
        {"speaker": "participant", "text": "who is jesus"},
        {"speaker": "alx", "text": "   "},
        {"speaker": "participant", "text": "what did that cost"},
        {"speaker": "alx", "text": "It cost blood, first."},
    ]
    h = _history_from(transcript)
    assert [m["role"] for m in h] == ["user", "assistant"]
    assert h[0]["content"] == "what did that cost"


def test_the_eleventh_message_closes_gracefully_and_a_twelfth_is_refused(store, usage_store, world_loader, registry):
    from engine.m4.turn import SESSION_TURN_CAP

    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    # The close-for-good at the cap is the module-off contract; with the module on, a limit pauses.
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client, deeper=None)
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    headers = {"Authorization": f"Session {created['session_code']}"}

    for i in range(SESSION_TURN_CAP):
        resp = http.post(f"/api/session/{created['session_id']}/message", headers=headers, json={"text": f"question {i}"})
        assert resp.status_code == 200

    capped = http.post(f"/api/session/{created['session_id']}/message", headers=headers, json={"text": "one more"})
    assert capped.status_code == 200
    assert capped.json()["routing_action"] == "session_cap_turn"
    assert capped.json()["facilitator"]["kind"] == "close"

    transcript = http.get(f"/api/session/{created['session_id']}/transcript", headers=headers).json()
    assert transcript["closed"] is True

    refused = http.post(f"/api/session/{created['session_id']}/message", headers=headers, json={"text": "are you there"})
    assert refused.status_code == 409


def test_r27_enforce_hands_a_twice_rejected_turn_to_the_facilitator_end_to_end(store, usage_store, world_loader, registry):
    """Full wiring: create_app with uncited-claim enforcement on, through
    wiring.handle_message, not the unit-level engine.m4.turn test - the
    voice's raw answer hard-fails (a real wholly_uncited_paragraph
    offense - "Even a broken priest could not block his grace." carries
    no proper noun, so it reaches verdict "ok" with no tag), the one
    allowed regeneration fails the same way, and the Facilitator's own
    interview-mode line (voice_rejected_turn) is what the response
    actually carries."""
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(),
        stream_scripts=[
            ["Even a broken priest could not block his grace."],
            ["Even a broken priest could not block his grace."],
        ],
    )
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client, r27_enforce=True)
    created = http.post("/api/session", json={"world_key": "fix"}).json()

    resp = http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": "who was Jesus"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert len(client.messages.stream_calls) == 2  # the one allowed regeneration, no more
    assert body["voice"]["text"] == ""
    assert body["voice"]["r27_enforcement_exhausted"] is True
    assert body["facilitator"]["kind"] == "grounding_correction"
    assert "Vera" in body["facilitator"]["text"]
