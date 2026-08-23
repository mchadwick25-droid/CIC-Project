"""HTTP-shape tests for engine.api.app - TestClient against create_app()
with fakes, never the real env-driven `app` instance (which stays None
unless CIC_API_REGION is set - see app.py's own module docstring)."""
from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.api.wiring import history_from_transcript as _history_from


def _client(*, store, usage_store, world_loader, registry, voice_client=None, safety_client=None, default_world_key="fix"):
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
    )
    return TestClient(app)


def test_health(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_create_session_default_world(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.post("/api/session", json={})
    assert resp.status_code == 201
    body = resp.json()
    assert "session_id" in body and "session_code" in body


def test_create_session_explicit_world(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    resp = http.post("/api/session", json={"world_key": "fix"})
    assert resp.status_code == 201


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
    created = http.post("/api/session", json={}).json()

    resp = http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": "who was Jesus"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["routing_action"] == "voice_with_directive"
    assert body["unhandled_routing_gap"] is False
    assert body["voice"]["text"] == "We did not claim to have seen him ourselves."


def test_message_wrong_code_and_missing_session_are_identical_401(store, usage_store, world_loader, registry):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    created = http.post("/api/session", json={}).json()

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


def test_message_unhandled_routing_returns_200_not_500(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("HARMFUL_DYNAMIC_SIGNAL"), reader_response=reader_response())
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client)
    created = http.post("/api/session", json={}).json()

    resp = http.post(
        f"/api/session/{created['session_id']}/message",
        headers={"Authorization": f"Session {created['session_code']}"},
        json={"text": "msg"},
    )
    assert resp.status_code == 200
    assert resp.json()["unhandled_routing_gap"] is True


def test_transcript_reflects_committed_turns(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, voice_client=client)
    created = http.post("/api/session", json={}).json()
    headers = {"Authorization": f"Session {created['session_code']}"}
    http.post(f"/api/session/{created['session_id']}/message", headers=headers, json={"text": "who was Jesus"})

    resp = http.get(f"/api/session/{created['session_id']}/transcript", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["turn_count"] == 1
    assert body["transcript"][0] == {"speaker": "participant", "text": "who was Jesus"}


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
