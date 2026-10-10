"""The event-stream form of POST /api/session/{id}/message: each sentence with
its marks while the reply is written, then the finished turn, identical to
the plain response. Fakes only - no provider call."""
import json

from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response

STREAM = {"Accept": "text/event-stream"}
CHUNKS = [
    "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. ",
    "We told what we had been told [[fix.witness.who-is-jesus]]. ",
    "That is all we can say.",
]
FINISHED = "We did not claim to have seen him ourselves. We told what we had been told. That is all we can say."


def _http(store, usage_store, world_loader, registry, *, client=None, streaming_enabled=True, r27_enforce=False):
    client = client or FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(), stream_chunks=CHUNKS)
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", streaming_enabled=streaming_enabled, r27_enforce=r27_enforce,
    )
    return TestClient(app)


def _session(http):
    created = http.post("/api/session", json={"world_key": "fix"}).json()
    return created["session_id"], {"Authorization": f"Session {created['session_code']}"}


def _events(response):
    out = []
    for block in response.text.strip().split("\n\n"):
        name, data = block.split("\n", 1)
        out.append((name.removeprefix("event: "), json.loads(data.removeprefix("data: "))))
    return out


def test_a_streamed_message_sends_sentences_then_the_finished_turn(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry)
    session_id, auth = _session(http)

    resp = http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json={"text": "who was Jesus"})

    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/event-stream")
    events = _events(resp)
    names = [name for name, _ in events]
    assert names[-1] == "done" and names.count("done") == 1
    sentences = [data for name, data in events if name == "sentence"]
    shown = "".join(s["lead"] + s["text"] for s in sentences)
    finished = events[-1][1]["voice"]["text"]
    assert finished == FINISHED
    assert shown and finished.startswith(shown)
    assert "[[" not in shown
    plan = events[-1][1]["voice"]["transparency"]
    for s in sentences:
        assert plan["sentences"][s["index"]] == {"index": s["index"], "text_start": s["text_start"], "text_end": s["text_end"]}


def test_the_finished_turn_is_the_same_as_the_plain_response(store, usage_store, world_loader, registry):
    streamed = _http(store, usage_store, world_loader, registry)
    sid, auth = _session(streamed)
    done = _events(streamed.post(f"/api/session/{sid}/message", headers={**auth, **STREAM}, json={"text": "who was Jesus"}))[-1][1]

    plain = _http(store, usage_store, world_loader, registry, streaming_enabled=False)
    sid2, auth2 = _session(plain)
    body = plain.post(f"/api/session/{sid2}/message", headers=auth2, json={"text": "who was Jesus"}).json()

    assert done["voice"]["text"] == body["voice"]["text"]
    assert done["voice"]["citations"] == body["voice"]["citations"]
    assert done["voice"]["transparency"] == body["voice"]["transparency"]
    assert done["routing_action"] == body["routing_action"]


def test_the_streamed_turn_is_recorded_once_and_matches_the_transcript(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry)
    session_id, auth = _session(http)
    done = _events(http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json={"text": "who was Jesus"}))[-1][1]

    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()
    voices = [t for t in transcript["transcript"] if "citations" in t]
    assert [v["text"] for v in voices] == [done["voice"]["text"]]
    assert transcript["turn_count"] == 1


def test_without_the_flag_an_event_stream_request_gets_the_plain_response(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry, streaming_enabled=False)
    session_id, auth = _session(http)
    resp = http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json={"text": "who was Jesus"})
    assert resp.headers["content-type"].startswith("application/json")
    assert resp.json()["voice"]["text"] == FINISHED


def test_with_the_flag_a_request_that_does_not_ask_for_a_stream_gets_the_plain_response(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry)
    session_id, auth = _session(http)
    resp = http.post(f"/api/session/{session_id}/message", headers=auth, json={"text": "who was Jesus"})
    assert resp.headers["content-type"].startswith("application/json")


def test_a_refusal_before_any_sentence_is_an_http_status_not_a_stream(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry)
    session_id, _auth = _session(http)
    resp = http.post(
        f"/api/session/{session_id}/message", headers={"Authorization": "Session wrong", **STREAM}, json={"text": "who was Jesus"},
    )
    assert resp.status_code == 401


def test_a_duplicate_message_is_a_409_before_any_stream(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry)
    session_id, auth = _session(http)
    body = {"text": "who was Jesus", "client_msg_id": "m-1"}
    assert http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json=body).status_code == 200
    again = http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json=body)
    assert again.status_code == 409


def test_a_turn_the_facilitator_answers_streams_no_sentence(store, usage_store, world_loader, registry):
    client = FakeBedrockClient(
        safety_response=safety_response("ACUTE_DISTRESS", acute_level="a2", risk_subject="self"),
        reader_response=reader_response(), stream_chunks=CHUNKS,
    )
    http = _http(store, usage_store, world_loader, registry, client=client)
    session_id, auth = _session(http)
    events = _events(http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json={"text": "I can't go on"}))
    assert [name for name, _ in events] == ["done"]
    assert events[0][1]["voice"] is None
    assert events[0][1]["facilitator"]


def test_a_turn_that_may_be_regenerated_streams_no_sentence(store, usage_store, world_loader, registry):
    http = _http(store, usage_store, world_loader, registry, r27_enforce=True)
    session_id, auth = _session(http)
    events = _events(http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json={"text": "who was Jesus"}))
    assert [name for name, _ in events] == ["done"]


def test_a_failure_after_the_stream_began_is_an_error_event_with_a_stable_code(store, usage_store, world_loader, registry, monkeypatch):
    import engine.api.app as app_module

    def handle(**kwargs):
        kwargs["on_sentence"]({"index": 0, "lead": "", "text": "We spoke.", "text_start": 0, "text_end": 9, "elements": [], "cards": []})
        raise app_module.wiring.ProviderCallFailed(RuntimeError("throttled"))

    http = _http(store, usage_store, world_loader, registry)
    session_id, auth = _session(http)
    monkeypatch.setattr(app_module.wiring, "handle_message", handle)
    events = _events(http.post(f"/api/session/{session_id}/message", headers={**auth, **STREAM}, json={"text": "who was Jesus"}))
    assert [name for name, _ in events] == ["sentence", "error"]
    assert events[1][1] == {"code": "provider_failed", "status": 502, "detail": "provider call failed"}
