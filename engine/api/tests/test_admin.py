"""/api/admin/pilot-summary: the one aggregate, participant-content-free
view into the whole session log - "how many real pilot sessions exist"
and "is the table round cap firing where it should" have no answer from
any other endpoint, which is either per-session (gated by that session's
own auth code) or doesn't exist. Auth is its own concern here, not the
per-session code _authenticate checks elsewhere in this test tree."""
import uuid

import pytest
from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.test_table_api import _create_table, _table_client, grounded_sentence
from engine.api.wiring import _load_world, create_session


@pytest.fixture
def alx_world(world_loader, registry):
    return _load_world(world_loader, registry, "alx")


@pytest.fixture
def desert_world(world_loader, registry):
    return _load_world(world_loader, registry, "desert")


def _http(*, store, usage_store, world_loader, registry, client, admin_token=None, **extra):
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", admin_token=admin_token, **extra,
    )
    return TestClient(app)


def test_pilot_summary_404s_when_admin_token_unconfigured(store, usage_store, world_loader, registry):
    client = _table_client(selector_script=[], stream_scripts=[])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    resp = http.get("/api/admin/pilot-summary", headers={"Authorization": "Bearer anything"})
    assert resp.status_code == 404


def test_pilot_summary_404s_with_wrong_or_missing_token(store, usage_store, world_loader, registry):
    client = _table_client(selector_script=[], stream_scripts=[])
    http = _http(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client,
        admin_token="the-real-token",
    )
    assert http.get("/api/admin/pilot-summary", headers={"Authorization": "Bearer wrong"}).status_code == 404
    assert http.get("/api/admin/pilot-summary").status_code == 404


def test_pilot_summary_counts_sessions_and_flags_the_cap_round(
    store, usage_store, world_loader, registry, monkeypatch, alx_world, desert_world
):
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", 1)
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "r1"}, {"next": "close", "reason": "done"}],
        stream_scripts=[[alx_sentence], [desert_sentence], [alx_sentence]],
    )
    http = _http(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client,
        admin_token="the-real-token", deeper=None,
    )
    admin_headers = {"Authorization": "Bearer the-real-token"}

    # Session 1: drive one round to close, then the session's own round
    # cap (patched to 1) fires on the next message.
    capped_id, capped_auth = _create_table(http)
    result = http.post(f"/api/session/{capped_id}/message", json={"text": "one"}, headers=capped_auth).json()
    while result["round_open"]:
        result = http.post(f"/api/session/{capped_id}/continue", headers=capped_auth).json()
    capped = http.post(f"/api/session/{capped_id}/message", json={"text": "two"}, headers=capped_auth).json()
    assert capped["session_closed"]

    # Session 2: created, never closed.
    _create_table(http)

    resp = http.get("/api/admin/pilot-summary", headers=admin_headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["total_sessions"] == 2
    assert body["by_mode"] == {"table": 2}
    assert body["open_sessions"] == 1
    assert body["closed_by_reason"] == {"cap": 1}
    assert body["table_round_counts_on_cap"] == {"1": 1}
    assert body["earliest_session_at"] is not None
    assert body["latest_session_at"] is not None


def test_pilot_summary_reads_a_resumed_idle_session_as_open(store, usage_store, world_loader, registry):
    """engine.m4.idle_close's reporting-only contract, from the admin
    summary's own reader (engine.m7.session_reader, a separate fold from
    the one the API's SessionClosed gate uses - both must agree)."""
    client = _table_client(selector_script=[], stream_scripts=[])
    http = _http(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client,
        admin_token="the-real-token",
    )
    admin_headers = {"Authorization": "Bearer the-real-token"}

    session_id, _code = create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    store.append(session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="session_closed", payload={"reason": "idle"})
    store.append(
        session_id=session_id, event_uuid=str(uuid.uuid4()), event_type="participant_message",
        payload={"text": "still there?", "client_msg_id": "m2"},
    )

    body = http.get("/api/admin/pilot-summary", headers=admin_headers).json()
    assert body["total_sessions"] == 1
    assert body["open_sessions"] == 1
    assert body["closed_by_reason"] == {}
