"""The admission seam: a code buys what the free allowance refuses, the voice
is asked exactly what it would be asked for a free turn, and every limit still
leaves the safety check in front of the participant."""
import copy
import json
import logging
import re
from datetime import date

import anthropic
import httpx
import pytest
from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.deeper_routes import DeeperRuntime
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.deeper import codes
from engine.deeper.claims import ClaimStore
from engine.deeper.meter import Meter

FREE_CAP = 2
ACUTE = safety_response("ACUTE_DISTRESS", acute_level="a1", risk_subject="self")
UNCLEAR = safety_response("AMBIGUOUS_LOW_CONFIDENCE")
CALM = safety_response("NO_SIGNAL")
GROUNDED = ["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."]


class RecordingClient(FakeBedrockClient):
    """Records every voice request in full, and can fail the safety call."""

    def __init__(self, *, safety=CALM, safety_fails=False, voice_fails=False):
        super().__init__(safety_response=safety, reader_response=reader_response(), stream_chunks=GROUNDED)
        self.voice_requests: list[dict] = []
        self.safety_calls = 0
        outer_stream = self.messages.stream
        outer_create = self.messages.create

        def stream(**kwargs):
            if voice_fails:
                raise RuntimeError("voice provider down")
            self.voice_requests.append(copy.deepcopy({k: v for k, v in kwargs.items() if k != "timeout"}))
            return outer_stream(**kwargs)

        def create(**kwargs):
            if kwargs["tool_choice"]["name"] == "submit_safety_classification":
                self.safety_calls += 1
                if safety_fails:
                    raise anthropic.APITimeoutError(request=httpx.Request("POST", "http://bedrock"))
            return outer_create(**kwargs)

        self.messages.stream = stream
        self.messages.create = create


@pytest.fixture
def runtime(tmp_path):
    rt = DeeperRuntime(
        meter=Meter(str(tmp_path / "m.db"), clock=lambda: date(2026, 10, 5)),
        claims=ClaimStore(str(tmp_path / "c.db")),
        webhook_secret="whsec_x",
        products={},
        miss_delay_seconds=0.0,
    )
    yield rt
    rt.meter.close()
    rt.claims.close()


@pytest.fixture(autouse=True)
def small_free_cap(monkeypatch):
    monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", FREE_CAP)
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", 1)


def build(store, usage_store, world_loader, registry, client, *, deeper=None, **kwargs):
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", deeper=deeper, **kwargs,
    )
    return TestClient(app, base_url="https://testserver")


def open_session(http, **headers):
    created = http.post("/api/session", json={"world_key": "fix"}, headers=headers)
    assert created.status_code == 201, created.text
    body = created.json()
    return body["session_id"], {"Authorization": f"Session {body['session_code']}", **headers}


def say(http, session_id, auth, text):
    return http.post(f"/api/session/{session_id}/message", json={"text": text}, headers=auth)


def code_with(runtime, exchanges, kind="single"):
    return runtime.meter.mint(kind, exchanges, f"pi_{codes.generate()}")[0]


# ---- the request-diff test: money buys no change to what the voice is asked --

def run_sitting(http, turns, **headers):
    session_id, auth = open_session(http, **headers)
    last = None
    for i in range(turns):
        last = say(http, session_id, auth, f"question number {i}")
        assert last.status_code == 200, last.text
    return last


def test_the_voice_request_is_identical_off_free_and_paid_at_a_turn_past_the_free_cap(
    store, usage_store, world_loader, registry, runtime, tmp_path, monkeypatch
):
    turns = FREE_CAP + 2
    requests = {}

    monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", 50)
    off = RecordingClient()
    run_sitting(build(store, usage_store, world_loader, registry, off), turns)
    requests["off"] = off.voice_requests[turns - 1]

    free = RecordingClient()
    run_sitting(build(store, usage_store, world_loader, registry, free, deeper=runtime), turns)
    requests["on_free"] = free.voice_requests[turns - 1]

    monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", FREE_CAP)
    paid = RecordingClient()
    code = code_with(runtime, 5)
    last = run_sitting(build(store, usage_store, world_loader, registry, paid, deeper=runtime), turns, **{"X-Cic-Code": code})
    requests["on_paid"] = paid.voice_requests[turns - 1]

    assert last.json()["voice"] is not None
    assert runtime.meter.status(code).remaining == 5 - (turns - FREE_CAP)
    assert len(requests["off"]["messages"]) == 2 * (turns - 1) + 1
    assert requests["off"]["system"] and requests["off"]["model"] == "m"
    assert requests["off"] == requests["on_free"] == requests["on_paid"]
    assert len(paid.voice_requests) == turns


# ---- a code buys what the free allowance refuses -----------------------------

def test_a_code_pays_only_for_turns_past_the_free_cap_and_the_balance_is_reported(
    store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    code = code_with(runtime, 3)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    free_turns = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP)]
    assert [r.headers["x-cic-remaining"] for r in free_turns] == ["3"] * FREE_CAP
    paid = [say(http, session_id, auth, f"p{i}") for i in range(3)]
    assert [r.headers["x-cic-remaining"] for r in paid] == ["2", "1", "0"]
    assert all(r.json()["voice"] is not None for r in paid)
    out = say(http, session_id, auth, "one more")
    assert out.json()["routing_action"] == "session_cap_turn"
    assert out.headers["x-cic-remaining"] == "0"
    assert len(client.voice_requests) == FREE_CAP + 3


def test_no_code_means_no_header_and_the_free_cap_holds(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    session_id, auth = open_session(http)
    replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP + 1)]
    assert all("x-cic-remaining" not in r.headers for r in replies)
    assert replies[-1].json()["routing_action"] == "session_cap_turn"


def test_the_flag_off_sends_no_balance_and_ignores_a_code_header(store, usage_store, world_loader, registry):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client)
    assert http.app.state.deeper is None
    session_id, auth = open_session(http, **{"X-Cic-Code": codes.generate()})
    replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP + 1)]
    assert all("x-cic-remaining" not in r.headers for r in replies)
    assert replies[-1].json()["routing_action"] == "session_cap_turn"
    assert len(client.voice_requests) == FREE_CAP


def test_a_turn_the_facilitator_answers_alone_spends_nothing(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient(safety=UNCLEAR)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    code = code_with(runtime, 3)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    runtime.facilitator_only_sessions.add(session_id)
    reply = say(http, session_id, auth, "what if someone didn't want to be here")
    assert reply.json()["routing_action"] == "check_in_turn"
    assert runtime.meter.status(code).remaining == 3
    assert runtime.meter.reserve(code, 3).ok


def test_a_failed_voice_call_gives_the_exchange_back(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient(voice_fails=True)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    code = code_with(runtime, 2)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    runtime.facilitator_only_sessions.add(session_id)
    reply = say(http, session_id, auth, "tell me more")
    assert reply.status_code == 502
    assert runtime.meter.status(code).remaining == 2
    assert runtime.meter.reserve(code, 2).ok


def test_a_paused_or_unknown_code_leaves_the_free_path_alone(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    code = code_with(runtime, 5)
    runtime.meter.pause(True)
    for header in (code, codes.generate(), "garbage"):
        session_id, auth = open_session(http, **{"X-Cic-Code": header})
        replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP + 1)]
        assert replies[0].json()["voice"] is not None
        assert replies[-1].json()["routing_action"] == "session_cap_turn"
    assert runtime.meter.status(code).remaining == 5


def test_an_admission_fault_leaves_the_free_grant(store, usage_store, world_loader, registry, runtime, monkeypatch):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    code = code_with(runtime, 5)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})

    def broken(*a, **k):
        raise RuntimeError("meter unavailable")

    monkeypatch.setattr(runtime.meter, "reserve", broken)
    replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP + 1)]
    assert replies[0].json()["voice"] is not None
    assert replies[-1].json()["routing_action"] == "session_cap_turn"


# ---- the daily allowance --------------------------------------------------------

def capped_app(store, usage_store, world_loader, registry, runtime, client, **kwargs):
    return build(
        store, usage_store, world_loader, registry, client, deeper=runtime,
        anon_cap_enabled=True, anon_visitor_secret="s" * 32, **kwargs,
    )


def test_a_visitor_at_the_session_limit_gets_a_facilitator_only_sitting_not_a_429(
    store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_session_limit=0)
    session_id, auth = open_session(http)
    reply = say(http, session_id, auth, "hello there")
    assert reply.status_code == 200
    assert reply.json()["routing_action"] == "session_cap_turn" and reply.json()["voice"] is None
    assert client.voice_requests == []
    assert client.safety_calls >= 1


def test_without_the_module_the_session_limit_still_answers_429(store, usage_store, world_loader, registry):
    http = build(
        store, usage_store, world_loader, registry, RecordingClient(),
        anon_cap_enabled=True, anon_visitor_secret="s" * 32, anon_daily_session_limit=0,
    )
    assert http.post("/api/session", json={"world_key": "fix"}).status_code == 429


def test_a_valid_code_lifts_the_daily_session_limit(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_session_limit=0)
    session_id, auth = open_session(http, **{"X-Cic-Code": code_with(runtime, 5)})
    assert say(http, session_id, auth, "hello there").json()["voice"] is not None


def test_a_code_buys_turns_past_the_daily_message_allowance(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_turn_limit=0)
    code = code_with(runtime, 2)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    reply = say(http, session_id, auth, "hello there")
    assert reply.json()["voice"] is not None and reply.headers["x-cic-remaining"] == "1"
    other_id, other_auth = open_session(http)
    assert say(http, other_id, other_auth, "hello there").json()["routing_action"] == "session_cap_turn"


# ---- safety: the check-in and the crisis turn at every limit ------------------

def limit_setup(name, store, usage_store, world_loader, registry, runtime, client):
    """Builds an app and returns (http, session_id, auth) standing at the named limit."""
    if name == "session_limit":
        http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_session_limit=0)
        session_id, auth = open_session(http)
    elif name == "daily_limit":
        http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_turn_limit=0)
        session_id, auth = open_session(http)
    elif name == "free_cap":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http)
        for i in range(FREE_CAP):
            assert say(http, session_id, auth, f"q{i}").status_code == 200
    elif name == "zero_balance":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        code = code_with(runtime, 1)
        session_id, auth = open_session(http, **{"X-Cic-Code": code})
        runtime.meter.settle(runtime.meter.reserve(code).reservation, True)
        for i in range(FREE_CAP):
            assert say(http, session_id, auth, f"q{i}").status_code == 200
    elif name == "paused":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        code = code_with(runtime, 5)
        session_id, auth = open_session(http, **{"X-Cic-Code": code})
        runtime.meter.pause(True)
        for i in range(FREE_CAP):
            assert say(http, session_id, auth, f"q{i}").status_code == 200
    elif name == "wrong_code":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http, **{"X-Cic-Code": codes.generate()})
        for i in range(FREE_CAP):
            assert say(http, session_id, auth, f"q{i}").status_code == 200
    elif name == "module_error":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http, **{"X-Cic-Code": code_with(runtime, 5)})
        runtime.meter.reserve = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("down"))
        for i in range(FREE_CAP):
            assert say(http, session_id, auth, f"q{i}").status_code == 200
    elif name == "facilitator_only":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http)
        runtime.facilitator_only_sessions.add(session_id)
    else:
        raise AssertionError(name)
    return http, session_id, auth


LIMITS = ["session_limit", "daily_limit", "free_cap", "zero_balance", "paused", "wrong_code", "module_error", "facilitator_only"]
SAFETY = [
    ("acute", dict(safety=ACUTE), "safety_turn"),
    ("unclear", dict(safety=UNCLEAR), "check_in_turn"),
    ("failed", dict(safety_fails=True), "check_in_turn"),
]


@pytest.mark.parametrize("limit", LIMITS)
@pytest.mark.parametrize("label,client_kwargs,expected", SAFETY, ids=[s[0] for s in SAFETY])
def test_a_safety_route_is_answered_at_every_limit(
    limit, label, client_kwargs, expected, store, usage_store, world_loader, registry, runtime
):
    calm = RecordingClient()
    http, session_id, auth = limit_setup(limit, store, usage_store, world_loader, registry, runtime, calm)
    before = len(calm.voice_requests)
    calm.messages._responses["submit_safety_classification"] = copy.deepcopy(client_kwargs.get("safety", CALM))
    if client_kwargs.get("safety_fails"):
        failing = RecordingClient(safety_fails=True)
        http.app.state.deps.safety_client = failing
    reply = say(http, session_id, auth, "I do not know how to say this")
    assert reply.status_code == 200, reply.text
    body = reply.json()
    assert body["routing_action"] == expected
    assert body["voice"] is None
    assert len(calm.voice_requests) == before
    if expected == "safety_turn":
        assert body["facilitator"]["resources_appended"]


@pytest.mark.parametrize("limit", LIMITS)
def test_an_ordinary_message_at_a_limit_gets_a_close_and_no_voice_call(
    limit, store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient()
    http, session_id, auth = limit_setup(limit, store, usage_store, world_loader, registry, runtime, client)
    before = len(client.voice_requests)
    reply = say(http, session_id, auth, "tell me more")
    assert reply.status_code == 200
    assert reply.json()["routing_action"] == "session_cap_turn"
    assert reply.json()["facilitator"]["kind"] == "close"
    assert len(client.voice_requests) == before


# ---- never mid-answer ------------------------------------------------------------

def test_admission_is_decided_before_the_voice_and_never_during_it(store, usage_store, world_loader, registry, runtime, monkeypatch):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    code = code_with(runtime, 1)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    seen = {}
    original_stream = client.messages.stream

    def watching(**kwargs):
        seen["held_during_voice"] = runtime.meter._reserved.copy()
        seen["remaining_during_voice"] = runtime.meter.status(code).remaining
        return original_stream(**kwargs)

    client.messages.stream = watching
    reply = say(http, session_id, auth, "the paid one")
    assert reply.json()["voice"] is not None
    assert sum(seen["held_during_voice"].values()) == 1
    assert seen["remaining_during_voice"] == 1
    assert runtime.meter.status(code).remaining == 0
    assert runtime.meter._reserved == {}


# ---- streaming and the table -----------------------------------------------------

def parse_sse(text):
    events = []
    for block in text.strip().split("\n\n"):
        name = next(l[7:] for l in block.splitlines() if l.startswith("event: "))
        data = next(l[6:] for l in block.splitlines() if l.startswith("data: "))
        events.append((name, json.loads(data)))
    return events


def test_the_stream_path_admits_settles_and_reports_the_balance(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime, streaming_enabled=True)
    code = code_with(runtime, 2)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    reply = http.post(
        f"/api/session/{session_id}/message", json={"text": "streamed"}, headers={**auth, "Accept": "text/event-stream"}
    )
    events = parse_sse(reply.text)
    assert events[-1][0] == "done" and events[-1][1]["voice"] is not None
    assert events[-1][1]["remaining"] == 1
    assert runtime.meter.status(code).remaining == 1
    assert runtime.meter._reserved == {}


def test_a_failed_stream_gives_the_exchange_back(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient(voice_fails=True)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime, streaming_enabled=True)
    code = code_with(runtime, 2)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    runtime.facilitator_only_sessions.add(session_id)
    reply = http.post(
        f"/api/session/{session_id}/message", json={"text": "streamed"}, headers={**auth, "Accept": "text/event-stream"}
    )
    assert reply.status_code == 502 or parse_sse(reply.text)[-1][0] == "error"
    assert runtime.meter.status(code).remaining == 2
    assert runtime.meter._reserved == {}


# ---- logs ------------------------------------------------------------------------

def test_a_handled_message_logs_no_session_id_and_no_turn_number(store, usage_store, world_loader, registry, runtime, caplog):
    caplog.set_level(logging.INFO, logger="cic.api")
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime, streaming_enabled=True)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    http.post(f"/api/session/{session_id}/message", json={"text": "again"}, headers={**auth, "Accept": "text/event-stream"})
    handled = [r.getMessage() for r in caplog.records if "handled" in r.getMessage()]
    assert len(handled) == 2
    for line in handled:
        assert session_id not in line and "turn=" not in line and "session=" not in line


# ---- the table: a round costs several exchanges, paid once, at its opening -----

from engine.api.tests.test_table_api import _create_table, _table_client, alx_world, desert_world, grounded_sentence  # noqa: E402,F401


def long_table_client(alx_world, desert_world, turns=40):
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    seats = ["alx", "desert"]
    return _table_client(
        selector_script=[{"next": seats[i % 2], "reason": "r"} for i in range(turns)],
        stream_scripts=[[alx_sentence if i % 2 == 0 else desert_sentence] for i in range(turns)],
    )


def table_app(store, usage_store, world_loader, registry, runtime, client):
    return build(store, usage_store, world_loader, registry, client, deeper=runtime)


def test_a_table_round_past_the_free_rounds_costs_the_round_price_once(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world
):
    client = long_table_client(alx_world, desert_world)
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    code = code_with(runtime, 7)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers={"X-Cic-Code": code}).json()
    auth = {"Authorization": f"Session {created['session_code']}", "X-Cic-Code": code}
    first = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    assert first.status_code == 200 and "x-cic-remaining" in first.headers
    assert first.headers["x-cic-remaining"] == "7"
    while first.json()["round_open"]:
        first = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
        assert first.status_code == 200
    second = http.post(f"/api/session/{created['session_id']}/message", json={"text": "and fasting?"}, headers=auth)
    assert second.status_code == 200
    assert second.headers["x-cic-remaining"] == "4"
    after_open = runtime.meter.status(code).remaining
    while second.json()["round_open"]:
        second = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
        assert second.status_code == 200
    assert runtime.meter.status(code).remaining == after_open == 4
    assert runtime.meter._reserved == {}


def test_a_table_round_the_balance_cannot_cover_is_not_admitted(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world
):
    client = long_table_client(alx_world, desert_world)
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    code = code_with(runtime, 2)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers={"X-Cic-Code": code}).json()
    auth = {"Authorization": f"Session {created['session_code']}", "X-Cic-Code": code}
    first = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    while first.json()["round_open"]:
        first = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
    second = http.post(f"/api/session/{created['session_id']}/message", json={"text": "and fasting?"}, headers=auth)
    assert second.json()["routing_action"] == "session_cap_turn"
    assert runtime.meter.status(code).remaining == 2


# ---- a class on one network ------------------------------------------------------

def test_twenty_five_students_behind_one_address_all_get_through_on_a_group_code(
    store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, rate_limit=True)
    group = code_with(runtime, 400, kind="group")
    statuses = []
    for student in range(25):
        http.cookies.clear()
        created = http.post("/api/session", json={"world_key": "fix"}, headers={"X-Cic-Code": group})
        statuses.append(created.status_code)
        assert created.status_code == 201, (student, created.text)
        body = created.json()
        auth = {"Authorization": f"Session {body['session_code']}", "X-Cic-Code": group}
        for turn in range(2):
            reply = say(http, body["session_id"], auth, f"student {student} question {turn}")
            statuses.append(reply.status_code)
            assert reply.status_code == 200, (student, turn, reply.text)
    assert set(statuses) <= {200, 201}


def test_the_same_class_without_a_code_is_still_limited_by_address(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), rate_limit=True)
    created = []
    for _ in range(25):
        http.cookies.clear()
        created.append(http.post("/api/session", json={"world_key": "fix"}).status_code)
    assert created.count(429) > 0


def test_each_batch_code_has_its_own_burst_bucket(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), rate_limit=True)
    batch = runtime.meter.mint("batch", 10, "pi_class", count=25)
    for code in batch:
        http.cookies.clear()
        assert http.post("/api/session", json={"world_key": "fix"}, headers={"X-Cic-Code": code}).status_code == 201


def test_a_forged_code_gets_no_bucket_of_its_own(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), rate_limit=True)
    results = []
    for _ in range(8):
        http.cookies.clear()
        results.append(http.post("/api/session", json={"world_key": "fix"}, headers={"X-Cic-Code": codes.generate()}).status_code)
    assert 429 in results
