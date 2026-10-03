"""A participant's deletion request removes the conversation from the event
log and from the M7 audit files."""
import json
from datetime import date

from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.m7 import erase


def _http(tmp_path, store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(),
                               stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."])
    return TestClient(create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", m7_audit_root=tmp_path / "m7-audits",
    ))


def _audit_run(root, stamp, session_ids):
    run = root / stamp
    (run / "sessions").mkdir(parents=True)
    for sid in session_ids:
        (run / "sessions" / f"{sid}.json").write_text(json.dumps({"session_id": sid, "text": "participant words"}))
    (run / "fleet-rollup.json").write_text(json.dumps({
        "lineage_session_ids": session_ids,
        "findings": [{"session_id": s, "detail": "x"} for s in session_ids],
        "sessions": [{"session_id": s} for s in session_ids],
    }))
    (run / "canon-candidates.json").write_text(json.dumps({
        "lineage_session_ids": session_ids,
        "candidates": [{"ask": "who was Jesus", "count": len(session_ids), "session_ids": session_ids},
                       {"ask": "only theirs", "count": 2, "session_ids": [session_ids[0]]}],
    }))
    (run / "fleet-digest.md").write_text("\n".join(
        [f"- **info** (x, session {s}): detail" for s in session_ids] + [f"Computed from session_ids: {', '.join(session_ids)}"]))
    return run


def test_delete_removes_the_conversation_and_its_audit_traces(tmp_path, store, usage_store, world_loader, registry):
    http = _http(tmp_path, store, usage_store, world_loader, registry)
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    sid = created["session_id"]
    auth = {"Authorization": f"Session {created['session_code']}"}
    http.post(f"/api/session/{sid}/message", headers=auth, json={"text": "who was Jesus"})
    run = _audit_run(tmp_path / "m7-audits", "2026-10-03T03-17-00Z", [sid, "other-session"])

    resp = http.delete(f"/api/session/{sid}", headers=auth)
    assert resp.status_code == 204
    assert store.read_events(sid) == []
    assert not (run / "sessions" / f"{sid}.json").exists() and (run / "sessions" / "other-session.json").exists()
    every_file = "".join(p.read_text() for p in run.rglob("*") if p.is_file())
    assert sid not in every_file and "other-session" in every_file
    candidates = json.loads((run / "canon-candidates.json").read_text())["candidates"]
    assert [c["ask"] for c in candidates] == ["who was Jesus"]
    assert http.get(f"/api/session/{sid}/transcript", headers=auth).status_code == 401


def test_delete_needs_the_sessions_own_code(tmp_path, store, usage_store, world_loader, registry):
    http = _http(tmp_path, store, usage_store, world_loader, registry)
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    resp = http.delete(f"/api/session/{created['session_id']}", headers={"Authorization": "Session wrong"})
    assert resp.status_code == 401
    assert store.read_events(created["session_id"]) != []


def test_prune_removes_runs_past_the_window_only(tmp_path):
    root = tmp_path / "m7-audits"
    _audit_run(root, "2026-06-01T03-17-00Z", ["a"])
    _audit_run(root, "2026-09-30T03-17-00Z", ["b"])
    (root / "last_run.json").write_text("{}")
    assert erase.prune_older_than(root, date(2026, 10, 3), 90) == 1
    assert sorted(p.name for p in root.iterdir()) == ["2026-09-30T03-17-00Z", "last_run.json"]
