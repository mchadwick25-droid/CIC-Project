"""A personal check-in (loss to suicide, coercion by a person) is shown once
per conversation; the same reason on a later turn goes on to the voice. The
general check-in is shown every time. A participant's own risk is always the
crisis turn."""
from engine.api.app import create_app
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.api.tests.test_deeper_seam import GROUNDED
from engine.api.tests.test_table_api import _create_table, _http, _table_client, alx_world, desert_world, grounded_sentence  # noqa: F401
from engine.m4 import facilitator_turns
from fastapi.testclient import TestClient

LOSS = safety_response("AMBIGUOUS_LOW_CONFIDENCE", check_in_reason="loss_to_suicide")
COERCION = safety_response("AMBIGUOUS_LOW_CONFIDENCE", check_in_reason="coercion_by_person")
GENERAL = safety_response("AMBIGUOUS_LOW_CONFIDENCE", check_in_reason="general")
OWN_RISK = safety_response("ACUTE_DISTRESS", acute_level="a1", risk_subject="self")


def _interview(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=LOSS, reader_response=reader_response(), stream_chunks=GROUNDED)
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
    )
    http = TestClient(app, base_url="https://testserver")
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    auth = {"Authorization": f"Session {created['session_code']}"}
    return client, http, created["session_id"], auth


def _say(http, session_id, auth, text="msg"):
    reply = http.post(f"/api/session/{session_id}/message", json={"text": text}, headers=auth)
    assert reply.status_code == 200, reply.text
    return reply.json()


def _classify(client, safety):
    client.messages._responses["submit_safety_classification"] = safety


def test_interview_loss_check_in_is_shown_once_then_the_voice_answers(store, usage_store, world_loader, registry):
    client, http, session_id, auth = _interview(store, usage_store, world_loader, registry)
    first = _say(http, session_id, auth)
    assert first["routing_action"] == "check_in_turn"
    assert first["facilitator"]["text"] == facilitator_turns.CHECK_IN_LOSS.text
    assert first["facilitator"]["check_in_reason"] == "loss_to_suicide"
    second = _say(http, session_id, auth)
    assert second["routing_action"] != "check_in_turn"
    assert second["voice"] is not None


def test_interview_coercion_check_in_is_shown_once_then_the_voice_answers(store, usage_store, world_loader, registry):
    client, http, session_id, auth = _interview(store, usage_store, world_loader, registry)
    _classify(client, COERCION)
    assert _say(http, session_id, auth)["facilitator"]["text"] == facilitator_turns.CHECK_IN_COERCION.text
    second = _say(http, session_id, auth)
    assert second["routing_action"] != "check_in_turn"
    assert second["voice"] is not None


def test_interview_a_different_reason_still_gets_its_own_check_in(store, usage_store, world_loader, registry):
    client, http, session_id, auth = _interview(store, usage_store, world_loader, registry)
    assert _say(http, session_id, auth)["routing_action"] == "check_in_turn"
    _classify(client, COERCION)
    assert _say(http, session_id, auth)["facilitator"]["text"] == facilitator_turns.CHECK_IN_COERCION.text


def test_interview_general_check_in_is_shown_every_time(store, usage_store, world_loader, registry):
    client, http, session_id, auth = _interview(store, usage_store, world_loader, registry)
    _classify(client, GENERAL)
    for _ in range(3):
        reply = _say(http, session_id, auth)
        assert reply["routing_action"] == "check_in_turn"
        assert reply["facilitator"]["text"] == facilitator_turns.CHECK_IN.text
        assert reply["facilitator"]["check_in_reason"] == "general"


def test_interview_own_risk_is_still_the_crisis_turn_after_a_loss_check_in(store, usage_store, world_loader, registry):
    client, http, session_id, auth = _interview(store, usage_store, world_loader, registry)
    assert _say(http, session_id, auth)["routing_action"] == "check_in_turn"
    _classify(client, OWN_RISK)
    reply = _say(http, session_id, auth)
    assert reply["routing_action"] == "safety_turn"
    assert reply["facilitator"]["resources_appended"] is True


def test_table_loss_check_in_is_shown_once_then_the_round_goes_on(store, usage_store, world_loader, registry, alx_world, desert_world):
    sentence, _ = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[sentence]], safety=LOSS)
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    first = http.post(f"/api/session/{session_id}/message", json={"text": "msg"}, headers=auth).json()
    assert first["routing_action"] == "check_in_turn"
    assert first["facilitator"][0]["text"] == facilitator_turns.CHECK_IN_LOSS.text
    assert first["voice"] is None
    second = http.post(f"/api/session/{session_id}/message", json={"text": "msg"}, headers=auth).json()
    assert second["routing_action"] != "check_in_turn"
    assert second["voice"]["speaker"] == "alx"


def test_table_coercion_check_in_is_shown_once_and_general_every_time(store, usage_store, world_loader, registry, alx_world, desert_world):
    sentence, _ = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[sentence]], safety=COERCION)
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    first = http.post(f"/api/session/{session_id}/message", json={"text": "msg"}, headers=auth).json()
    assert first["facilitator"][0]["text"] == facilitator_turns.CHECK_IN_COERCION.text
    assert http.post(f"/api/session/{session_id}/message", json={"text": "msg"}, headers=auth).json()["voice"] is not None

    general = _table_client(selector_script=[], stream_scripts=[], safety=GENERAL)
    other = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=general)
    other_id, other_auth = _create_table(other)
    for _ in range(2):
        reply = other.post(f"/api/session/{other_id}/message", json={"text": "msg"}, headers=other_auth).json()
        assert reply["routing_action"] == "check_in_turn"
