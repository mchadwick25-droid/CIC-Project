"""System Hub decision 35: a message the service would refuse unread is read
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


# ---- a safety call that cannot run: an unread message is refused as it would have been, never answered "send it again" ----


def _cannot_run_safety(client):
    """The client's safety call fails as a missing credential does; every other call works."""
    from botocore.exceptions import NoCredentialsError

    real = client.messages.create

    def create(**kwargs):
        if kwargs["tool_choice"]["name"] == "submit_safety_classification" and not getattr(client, "safety_recovered", False):
            raise NoCredentialsError()
        return real(**kwargs)

    client.messages.create = create
    return client


def test_an_unread_message_to_a_closed_session_is_refused_not_told_to_send_it_again(store, usage_store, world_loader, registry):
    client = _cannot_run_safety(FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response()))
    http = _http(client, store, usage_store, world_loader, registry)
    created, auth = _interview(http)
    _close_by_cap(store, created["session_id"])
    resp = http.post(f"/api/session/{created['session_id']}/message", headers=auth, json={"text": "I can't go on"})
    assert resp.status_code == 409 and resp.json()["detail"] == "session already closed"


def test_an_unread_over_long_message_is_refused_not_told_to_send_it_again(store, usage_store, world_loader, registry):
    client = _cannot_run_safety(FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response()))
    http = _http(client, store, usage_store, world_loader, registry)
    created, auth = _interview(http)
    resp = http.post(f"/api/session/{created['session_id']}/message", headers=auth,
                     json={"text": "I need to say this. " * (MAX_MESSAGE_LENGTH // 10)})
    assert resp.status_code != 200


def test_an_unread_message_while_a_table_round_is_open_is_refused_and_the_round_stays_open(store, usage_store, world_loader, registry, alx_world, desert_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    client = _cannot_run_safety(_table_client(selector_script=[{"next": "alx", "reason": "most directly positioned"}], stream_scripts=[[alx_sentence]]))
    client.safety_recovered = True
    http = _http(client, store, usage_store, world_loader, registry)
    session_id, auth = _create_table(http)
    first = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert first["round_open"]
    client.safety_recovered = False
    resp = http.post(f"/api/session/{session_id}/message", json={"text": "and fasting?"}, headers=auth)
    assert resp.status_code == 409 and "round still open" in resp.json()["detail"]
    reasons = [e.payload["reason"] for e in store.read_events(session_id) if e.event_type == "round_closed"]
    assert "safety" not in reasons


def test_unread_messages_at_a_table_do_not_use_up_its_rounds(store, usage_store, world_loader, registry, alx_world, desert_world):
    from engine.m4.round import TABLE_SESSION_ROUND_CAP

    alx_sentence, _ = grounded_sentence(alx_world)
    client = _cannot_run_safety(_table_client(selector_script=[{"next": "alx", "reason": "most directly positioned"}], stream_scripts=[[alx_sentence]]))
    http = _http(client, store, usage_store, world_loader, registry)
    session_id, auth = _create_table(http)
    for attempt in range(TABLE_SESSION_ROUND_CAP + 2):
        resp = http.post(f"/api/session/{session_id}/message", json={"text": f"hello {attempt}"}, headers=auth)
        assert resp.status_code == 200, resp.text
        body = resp.json()
        assert body["routing_action"] == "safety_unread_turn" and not body["round_open"] and body["voice"] is None
        assert body["turn_no"] == 0
    client.safety_recovered = True
    answered = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert answered["routing_action"] != "session_cap_turn" and not answered.get("session_closed")
    assert answered["round_open"]
    assert not any(e.event_type == "session_closed" for e in store.read_events(session_id))
