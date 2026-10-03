"""System Hub decision 29: a message the service would refuse unread is read
by the safety call first, and a safety route gets the Facilitator's safety
turn instead of the refusal."""
import uuid

from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.api.tests.test_anon_cap import _app, _send
from engine.api.tests.test_table_api import _create_table, _table_client, alx_world, desert_world, grounded_sentence  # noqa: F401
from engine.api.wiring import MAX_MESSAGE_LENGTH

ACUTE = safety_response("ACUTE_DISTRESS", acute_level="a1", risk_subject="self")


def _http(client, store, usage_store, world_loader, registry):
    return TestClient(create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
    ))


def _interview(http):
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    return created, {"Authorization": f"Session {created['session_code']}"}


def _close_by_cap(store, session_id):
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="session_closed", payload={"reason": "cap"})


def test_a_crisis_in_a_cap_closed_session_gets_the_safety_turn_and_the_session_stays_closed(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=ACUTE, reader_response=reader_response())
    http = _http(client, store, usage_store, world_loader, registry)
    created, auth = _interview(http)
    _close_by_cap(store, created["session_id"])
    resp = http.post(f"/api/session/{created['session_id']}/message", headers=auth, json={"text": "I can't go on"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["routing_action"] == "safety_turn" and body["facilitator"]["resources_appended"] and body["voice"] is None
    assert client.messages.stream_calls == []
    client.messages._responses["submit_safety_classification"] = safety_response("NO_SIGNAL")
    again = http.post(f"/api/session/{created['session_id']}/message", headers=auth, json={"text": "hello again"})
    assert again.status_code == 409 and again.json()["detail"] == "session already closed"


def test_an_ordinary_message_to_a_closed_session_is_still_refused(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    http = _http(client, store, usage_store, world_loader, registry)
    created, auth = _interview(http)
    _close_by_cap(store, created["session_id"])
    resp = http.post(f"/api/session/{created['session_id']}/message", headers=auth, json={"text": "one more question"})
    assert resp.status_code == 409
    assert client.messages.stream_calls == []


def test_a_crisis_in_an_over_long_message_gets_the_safety_turn(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=ACUTE, reader_response=reader_response())
    http = _http(client, store, usage_store, world_loader, registry)
    created, auth = _interview(http)
    resp = http.post(f"/api/session/{created['session_id']}/message", headers=auth,
                     json={"text": "I need to say this. " * (MAX_MESSAGE_LENGTH // 10)})
    assert resp.status_code == 200 and resp.json()["routing_action"] == "safety_turn"
    assert client.messages.stream_calls == []


def test_an_uncertain_safety_call_over_the_daily_cap_gets_the_check_in_not_the_cap(store, usage_store, world_loader, registry):
    http = _app(
        anon_cap_enabled=True, secret="s" * 32, daily_turn_limit=0, safety_signal="AMBIGUOUS_LOW_CONFIDENCE",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
    )
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    resp = _send(http, created, text="what if someone didn't want to be here")
    assert resp.status_code == 200 and resp.json()["routing_action"] == "check_in_turn"


def test_a_crisis_typed_while_a_table_round_is_open_closes_the_round_and_gets_the_safety_turn(store, usage_store, world_loader, registry, alx_world, desert_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "most directly positioned"}], stream_scripts=[[alx_sentence]])
    http = _http(client, store, usage_store, world_loader, registry)
    session_id, auth = _create_table(http)
    first = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert first["round_open"]
    client.messages._responses["submit_safety_classification"] = ACUTE
    resp = http.post(f"/api/session/{session_id}/message", json={"text": "I want to end it"}, headers=auth)
    assert resp.status_code == 200
    body = resp.json()
    assert not body["round_open"] and body["voice"] is None and body["facilitator"][0]["resources_appended"]
    closes = [e.payload for e in store.read_events(session_id) if e.event_type == "round_closed"]
    assert [c["reason"] for c in closes] == ["safety", "selector_closed"]
    assert closes[0]["turns"] == 1
    assert http.post(f"/api/session/{session_id}/continue", headers=auth).status_code == 409


def test_an_ordinary_message_while_a_table_round_is_open_is_still_refused(store, usage_store, world_loader, registry, alx_world, desert_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "most directly positioned"}], stream_scripts=[[alx_sentence]])
    http = _http(client, store, usage_store, world_loader, registry)
    session_id, auth = _create_table(http)
    http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth)
    resp = http.post(f"/api/session/{session_id}/message", json={"text": "and fasting?"}, headers=auth)
    assert resp.status_code == 409 and "round still open" in resp.json()["detail"]
