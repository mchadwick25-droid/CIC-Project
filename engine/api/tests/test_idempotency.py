"""client_msg_id idempotency, ENFORCED (2026-08-28 foundation audit: the id
was recorded in the payload while the dedupe key was minted fresh per call,
so a retried message ran a second full turn and doubled the spend), plus
the table advance lock (two overlapping advances used to both run a voice
turn against the same open round)."""
import threading

from fastapi.testclient import TestClient

from engine.api import table_wiring
from engine.api.app import create_app
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response


def _client(store, usage_store, world_loader, registry):
    fake = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    app = create_app(
        voice_client=fake, voice_model_id="m", safety_client=fake, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix",
    )
    return TestClient(app), fake


def test_resending_the_same_client_msg_id_is_refused_before_any_model_call(store, usage_store, world_loader, registry):
    http, fake = _client(store, usage_store, world_loader, registry)
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    auth = {"Authorization": f"Session {created['session_code']}"}
    url = f"/api/session/{created['session_id']}/message"

    first = http.post(url, json={"text": "Who was Jesus to you?", "client_msg_id": "msg-1"}, headers=auth)
    assert first.status_code == 200
    calls_after_first = len(fake.messages.stream_calls)

    retry = http.post(url, json={"text": "Who was Jesus to you?", "client_msg_id": "msg-1"}, headers=auth)
    assert retry.status_code == 409
    assert "duplicate" in retry.json()["detail"]
    # The whole point: the retry cost NOTHING - no second voice call ran.
    assert len(fake.messages.stream_calls) == calls_after_first

    # A genuinely new message (new id) still goes through.
    second = http.post(url, json={"text": "And what did following him cost?", "client_msg_id": "msg-2"}, headers=auth)
    assert second.status_code == 200


def test_event_exists_sees_only_real_uuids(store):
    assert not store.event_exists("00000000-0000-0000-0000-000000000000")


def test_table_advance_lock_refuses_overlap():
    """The lock itself, unit-level: a second advance while one is in
    flight raises TableAdvanceInFlight instead of running."""
    entered = threading.Event()
    release = threading.Event()
    results = []

    def hold():
        with table_wiring._advance_lock("s-lock-test"):
            entered.set()
            release.wait(timeout=5)

    t = threading.Thread(target=hold)
    t.start()
    entered.wait(timeout=5)
    try:
        with table_wiring._advance_lock("s-lock-test"):
            results.append("entered")
    except table_wiring.TableAdvanceInFlight:
        results.append("refused")
    release.set()
    t.join(timeout=5)
    assert results == ["refused"]
    # And the lock is reusable once the first advance finishes.
    with table_wiring._advance_lock("s-lock-test"):
        pass
