"""A finished turn writes one anonymous quality-control row (engine.m7.qc_store)."""
import json
import sqlite3

from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.qc_recorder import QCRecorder, text_free
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.m7.qc_store import QCStore


def _http(tmp_path, *, store, usage_store, world_loader, registry, client):
    qc = QCStore(tmp_path / "qc.db")
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", qc_recorder=QCRecorder(qc, registry),
    )
    return TestClient(app), qc


def _message(http, text):
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    auth = {"Authorization": f"Session {created['session_code']}"}
    resp = http.post(f"/api/session/{created['session_id']}/message", headers=auth, json={"text": text})
    assert resp.status_code == 200
    return created, auth


def test_an_interview_turn_writes_one_scrubbed_row_whose_token_never_reaches_the_event_log(tmp_path, store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(),
                               stream_scripts=[["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."]])
    http, qc = _http(tmp_path, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    created, auth = _message(http, "My friend Maria asked: who was Jesus?")
    rows = qc.rows()
    assert len(rows) == 1
    row = rows[0]
    assert row["world"] == "fix" and row["round"] == 1 and row["week"].count("-W") == 1
    assert "Maria" not in row["question_text"] and "[name]" in row["question_text"]
    assert row["answer_text"] == "We did not claim to have seen him ourselves."
    with sqlite3.connect(store.db_path) as conn:
        log = " ".join(p for (p,) in conn.execute("SELECT payload FROM session_events"))
    assert row["conversation_token"] not in log
    assert created["session_id"] not in json.dumps(row)


def test_a_second_turn_in_the_same_conversation_shares_its_token(tmp_path, store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(),
                               stream_scripts=[["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."]] * 2)
    http, qc = _http(tmp_path, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    created, auth = _message(http, "who was Jesus")
    http.post(f"/api/session/{created['session_id']}/message", headers=auth, json={"text": "and then?"})
    rows = qc.rows()
    assert [r["round"] for r in rows] == [1, 2] and rows[0]["conversation_token"] == rows[1]["conversation_token"]


def test_a_flagged_turn_keeps_routing_flags_and_no_text(tmp_path, store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("ACUTE_DISTRESS", acute_level="a1", risk_subject="self"),
                               reader_response=reader_response())
    http, qc = _http(tmp_path, store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    _message(http, "I don't want to be here any more")
    row = qc.rows()[0]
    assert row["question_text"] is None and row["answer_text"] is None
    assert json.loads(row["flags"])["text_free"] is True


def test_text_free_rule():
    assert text_free(None) is True
    assert text_free({"signal": "NO_SIGNAL", "dynamic_tags": []}) is False
    assert text_free({"signal": "HISTORICAL_OTHERNESS_DISORIENTATION", "dynamic_tags": []}) is False
    assert text_free({"signal": "NO_SIGNAL", "dynamic_tags": ["CONFIDANT_LANGUAGE"]}) is True
    assert text_free({"signal": "AMBIGUOUS_LOW_CONFIDENCE", "dynamic_tags": []}) is True
