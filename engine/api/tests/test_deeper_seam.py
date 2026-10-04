"""The admission seam: a code buys what the free allowance refuses, the voice
is asked exactly what it would be asked for a free turn, and every limit still
leaves the safety check in front of the participant."""
import copy
import dataclasses
import json
import logging
import re
from datetime import date, datetime, timezone

import anthropic
import httpx
import pytest
from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.deeper_ops import load_ops
from engine.api.deeper_routes import DeeperRuntime
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.deeper import codes, tokens
from engine.deeper import door as door_module
from engine.deeper.claims import ClaimStore
from engine.deeper.free import DailyFreeAllowance
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
        ops=load_ops(),
    )
    yield rt
    rt.meter.close()
    rt.claims.close()


from engine.m4 import round as _round_module  # noqa: E402
from engine.m4 import turn as _turn_module  # noqa: E402

SIM_MODEL = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
SHIPPED_SESSION_TURN_CAP = _turn_module.SESSION_TURN_CAP
SHIPPED_TABLE_ROUND_CAP = _round_module.TABLE_SESSION_ROUND_CAP


@pytest.fixture
def shipped_caps(monkeypatch):
    """The engine's own free caps, as shipped, for the tests that prove the free day on top of them."""
    monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", SHIPPED_SESSION_TURN_CAP)
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", SHIPPED_TABLE_ROUND_CAP)


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


def code_with(runtime, amount, kind="single"):
    return runtime.meter.mint(kind, amount, f"pi_{codes.generate()}")[0]


def solo_charge(runtime, first_round, last_round=None):
    """Tokens a solo conversation draws for rounds first_round..last_round."""
    return sum(tokens.charge(runtime.token_rates, n) for n in range(first_round, (last_round or first_round) + 1))


def table_charge(runtime, round_no, seats=2):
    return tokens.charge(runtime.token_rates, round_no, seats)


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
    turns = 2
    requests = {}

    monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", 50)
    off = RecordingClient()
    run_sitting(build(store, usage_store, world_loader, registry, off), turns)
    requests["off"] = off.voice_requests[turns - 1]

    free = RecordingClient()
    run_sitting(build(store, usage_store, world_loader, registry, free, deeper=runtime), turns)
    requests["on_free"] = free.voice_requests[turns - 1]
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_daily - solo_charge(runtime, 1, turns)

    runtime.free = DailyFreeAllowance(runtime.token_rates.free_daily)
    monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", 1)
    paid = RecordingClient()
    spare = 5
    code = code_with(runtime, solo_charge(runtime, 2, turns) + spare)
    last = run_sitting(build(store, usage_store, world_loader, registry, paid, deeper=runtime), turns, **{"X-Cic-Code": code})
    requests["on_paid"] = paid.voice_requests[turns - 1]

    assert last.json()["voice"] is not None
    assert runtime.meter.status(code).remaining == spare
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
    rounds = range(FREE_CAP + 1, FREE_CAP + 4)
    total = solo_charge(runtime, rounds[0], rounds[-1])
    code = code_with(runtime, total)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    free_turns = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP)]
    assert [r.headers["x-cic-remaining"] for r in free_turns] == [str(total)] * FREE_CAP
    paid = [say(http, session_id, auth, f"p{i}") for i in range(3)]
    left = [total - solo_charge(runtime, rounds[0], n) for n in rounds]
    assert left[-1] == 0
    assert [r.headers["x-cic-remaining"] for r in paid] == [str(n) for n in left]
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
    held = solo_charge(runtime, 1)
    code = code_with(runtime, held)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    runtime.facilitator_only_sessions.add(session_id)
    reply = say(http, session_id, auth, "what if someone didn't want to be here")
    assert reply.json()["routing_action"] == "check_in_turn"
    assert runtime.meter.status(code).remaining == held
    assert runtime.meter.reserve(code, held).ok


def test_a_failed_voice_call_gives_the_tokens_back(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient(voice_fails=True)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    held = solo_charge(runtime, 1)
    code = code_with(runtime, held)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    runtime.facilitator_only_sessions.add(session_id)
    reply = say(http, session_id, auth, "tell me more")
    assert reply.status_code == 502
    assert runtime.meter.status(code).remaining == held
    assert runtime.meter.reserve(code, held).ok


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
    session_id, auth = open_session(http, **{"X-Cic-Code": code_with(runtime, solo_charge(runtime, 1))})
    assert say(http, session_id, auth, "hello there").json()["voice"] is not None


def test_a_code_buys_turns_past_the_daily_message_allowance(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_turn_limit=0)
    spare = 30
    code = code_with(runtime, solo_charge(runtime, 1) + spare)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    reply = say(http, session_id, auth, "hello there")
    assert reply.json()["voice"] is not None and reply.headers["x-cic-remaining"] == str(spare)
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
    elif name == "free_day_spent":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        runtime.free.settle(runtime.free.reserve("ip:testclient", runtime.token_rates.free_daily), True)
        session_id, auth = open_session(http)
    elif name == "door_free_closed":
        runtime.door = StubDoor(free_voice=False)
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http)
    elif name == "door_paid_closed":
        runtime.door = StubDoor(free_voice=False, paid_voice=False)
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http, **{"X-Cic-Code": code_with(runtime, 500)})
    elif name == "free_rounds_done":
        runtime.token_rates = dataclasses.replace(runtime.token_rates, free_rounds=1)
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http)
        assert say(http, session_id, auth, "q0").status_code == 200
    else:
        raise AssertionError(name)
    return http, session_id, auth


LIMITS = [
    "session_limit", "daily_limit", "free_cap", "zero_balance", "paused", "wrong_code", "module_error", "facilitator_only",
    "free_day_spent", "free_rounds_done", "door_free_closed", "door_paid_closed",
]
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
def test_an_ordinary_message_at_a_limit_gets_a_pause_and_no_voice_call(
    limit, store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient()
    http, session_id, auth = limit_setup(limit, store, usage_store, world_loader, registry, runtime, client)
    before = len(client.voice_requests)
    reply = say(http, session_id, auth, "tell me more")
    assert reply.status_code == 200
    assert reply.json()["routing_action"] == "session_cap_turn"
    assert len(client.voice_requests) == before
    closed = any(e.event_type == "session_closed" for e in store.read_events(session_id))
    if limit == "module_error":
        # a fault in admission leaves the free path exactly as it was
        assert reply.json()["facilitator"]["kind"] == "close" and closed
        return
    assert reply.json()["facilitator"]["kind"] == "limit"
    assert reply.json()["facilitator"]["text"] == runtime.ops.limit_text
    assert not closed


# ---- a limit is a pause: the sitting stays open and a code continues it -----------

def _stored_limit_texts(store, session_id):
    return [e.payload["text"] for e in store.read_events(session_id) if e.event_type == "facilitator_turn" and e.payload.get("kind") == "limit"]


def test_a_code_entered_after_the_pause_continues_the_same_conversation(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    session_id, auth = open_session(http)
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    paused = say(http, session_id, auth, "may I go on?")
    assert paused.json()["facilitator"]["kind"] == "limit"
    assert paused.json()["limit_note"] == {"key": "no_code", "text": runtime.ops.notes["no_code"]}
    assert http.get(f"/api/session/{session_id}/transcript", headers=auth).json()["closed"] is False
    total = 2 * solo_charge(runtime, FREE_CAP + 1)
    code = code_with(runtime, total)
    resumed = say(http, session_id, {**auth, "X-Cic-Code": code}, "now may I?")
    assert resumed.status_code == 200 and resumed.json()["voice"] is not None
    assert resumed.json()["limit_note"] is None
    assert runtime.meter.status(code).remaining == total - solo_charge(runtime, FREE_CAP + 1)
    sent = client.voice_requests[-1]
    assert "q0" in repr(sent), "the voice still sees the conversation from before the pause"


def test_each_reason_a_code_cannot_carry_a_turn_gets_its_own_line_in_the_response(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    spent = code_with(runtime, 1)
    runtime.meter.settle(runtime.meter.reserve(spent).reservation, True)
    group = runtime.meter.mint("group", 50, f"pi_{codes.generate()}", daily_ceiling=1)[0]
    runtime.meter.settle(runtime.meter.reserve(group).reservation, True)
    cases = {"spent": spent, "daily_ceiling": group, "code_not_accepted": codes.generate()}
    for expected, code in cases.items():
        session_id, auth = open_session(http)
        for i in range(FREE_CAP):
            say(http, session_id, auth, f"q{i}")
        reply = say(http, session_id, {**auth, "X-Cic-Code": code}, "more")
        assert reply.json()["limit_note"]["key"] == expected, expected
        assert reply.json()["limit_note"]["text"] == runtime.ops.notes[expected]
    live = code_with(runtime, 5)
    session_id, auth = open_session(http)
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    runtime.meter.pause(True)
    reply = say(http, session_id, {**auth, "X-Cic-Code": live}, "more")
    assert reply.json()["limit_note"]["key"] == "paused"


def test_the_stored_pause_is_the_same_words_for_a_free_sitting_and_a_paid_one_and_the_reason_is_never_stored(
    store, usage_store, world_loader, registry, runtime
):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    free_id, free_auth = open_session(http)
    for i in range(FREE_CAP):
        say(http, free_id, free_auth, f"q{i}")
    say(http, free_id, free_auth, "more")
    code = code_with(runtime, solo_charge(runtime, FREE_CAP + 1))
    paid_id, paid_auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(FREE_CAP + 1):
        say(http, paid_id, paid_auth, f"q{i}")
    runtime.meter.pause(False)
    out = say(http, paid_id, paid_auth, "more")
    assert out.json()["limit_note"]["key"] == "spent"
    assert _stored_limit_texts(store, free_id) == _stored_limit_texts(store, paid_id) == [runtime.ops.limit_text]
    stored = repr([e.payload for e in store.read_events(paid_id)])
    for text in runtime.ops.notes.values():
        assert text not in stored


def test_the_stream_path_carries_the_note_in_its_final_event(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime, streaming_enabled=True)
    session_id, auth = open_session(http)
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    reply = http.post(f"/api/session/{session_id}/message", json={"text": "more"}, headers={**auth, "Accept": "text/event-stream"})
    done = parse_sse(reply.text)[-1]
    assert done[0] == "done" and done[1]["limit_note"]["key"] == "no_code"


def test_a_table_the_code_cannot_cover_pauses_and_stays_open(store, usage_store, world_loader, registry, runtime, alx_world, desert_world):
    client = long_table_client(alx_world, desert_world)
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    code = code_with(runtime, table_charge(runtime, 2) - 1)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers={"X-Cic-Code": code}).json()
    auth = {"Authorization": f"Session {created['session_code']}", "X-Cic-Code": code}
    sid = created["session_id"]
    first = http.post(f"/api/session/{sid}/message", json={"text": "what is prayer?"}, headers=auth)
    while first.json()["round_open"]:
        first = http.post(f"/api/session/{sid}/continue", headers=auth)
    second = http.post(f"/api/session/{sid}/message", json={"text": "and fasting?"}, headers=auth)
    body = second.json()
    assert body["routing_action"] == "session_cap_turn" and body["session_closed"] is False
    assert body["facilitator"][0]["kind"] == "limit" and body["limit_note"]["key"] == "too_few"
    assert not any(e.event_type == "session_closed" for e in store.read_events(sid))


# ---- the low-balance flag ---------------------------------------------------------

def test_the_response_says_when_a_code_is_low_and_only_then(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    low_at = runtime.ops.low_balance_at
    code = code_with(runtime, low_at + solo_charge(runtime, FREE_CAP + 1, FREE_CAP + 2))
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    first = say(http, session_id, auth, "one")
    second = say(http, session_id, auth, "two")
    assert "x-cic-low" not in first.headers
    assert second.headers["x-cic-remaining"] == str(low_at) and second.headers["x-cic-low"] == "1"
    no_code_id, no_code_auth = open_session(http)
    assert "x-cic-low" not in say(http, no_code_id, no_code_auth, "hello").headers


def test_the_stream_says_low_in_its_final_event(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime, streaming_enabled=True)
    code = code_with(runtime, runtime.ops.low_balance_at)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    reply = http.post(f"/api/session/{session_id}/message", json={"text": "more"}, headers={**auth, "Accept": "text/event-stream"})
    done = parse_sse(reply.text)[-1][1]
    assert done["low"] is True and done["remaining"] == runtime.ops.low_balance_at - solo_charge(runtime, FREE_CAP + 1)


# ---- never mid-answer ------------------------------------------------------------

def test_admission_is_decided_before_the_voice_and_never_during_it(store, usage_store, world_loader, registry, runtime, monkeypatch):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    cost = solo_charge(runtime, FREE_CAP + 1)
    code = code_with(runtime, cost)
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
    assert sum(seen["held_during_voice"].values()) == cost
    assert seen["remaining_during_voice"] == cost
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
    cost = solo_charge(runtime, FREE_CAP + 1)
    code = code_with(runtime, 2 * cost)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(FREE_CAP):
        say(http, session_id, auth, f"q{i}")
    reply = http.post(
        f"/api/session/{session_id}/message", json={"text": "streamed"}, headers={**auth, "Accept": "text/event-stream"}
    )
    events = parse_sse(reply.text)
    assert events[-1][0] == "done" and events[-1][1]["voice"] is not None
    assert events[-1][1]["remaining"] == cost
    assert runtime.meter.status(code).remaining == cost
    assert runtime.meter._reserved == {}


def test_a_failed_stream_gives_the_tokens_back(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient(voice_fails=True)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime, streaming_enabled=True)
    held = solo_charge(runtime, 1)
    code = code_with(runtime, held)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    runtime.facilitator_only_sessions.add(session_id)
    reply = http.post(
        f"/api/session/{session_id}/message", json={"text": "streamed"}, headers={**auth, "Accept": "text/event-stream"}
    )
    assert reply.status_code == 502 or parse_sse(reply.text)[-1][0] == "error"
    assert runtime.meter.status(code).remaining == held
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


# ---- the table: a round costs by its number and its seats, paid once, at its opening -----

from engine.api.tests.test_table_api import _create_table, _table_client, alx_world, desert_world, grounded_sentence, pahc_world  # noqa: E402,F401


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
    total = 2 * table_charge(runtime, 2)
    round_price = table_charge(runtime, 2)
    code = code_with(runtime, total)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers={"X-Cic-Code": code}).json()
    auth = {"Authorization": f"Session {created['session_code']}", "X-Cic-Code": code}
    first = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    assert first.status_code == 200 and "x-cic-remaining" in first.headers
    assert first.headers["x-cic-remaining"] == str(total)
    while first.json()["round_open"]:
        first = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
        assert first.status_code == 200
    second = http.post(f"/api/session/{created['session_id']}/message", json={"text": "and fasting?"}, headers=auth)
    assert second.status_code == 200
    assert second.headers["x-cic-remaining"] == str(total - round_price)
    after_open = runtime.meter.status(code).remaining
    while second.json()["round_open"]:
        second = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
        assert second.status_code == 200
    assert runtime.meter.status(code).remaining == after_open == total - round_price
    assert runtime.meter._reserved == {}


@pytest.mark.parametrize("seats, opens, second", [(2, 160, 60), (3, 250, 100)])
def test_a_table_draws_its_opening_and_first_round_then_its_second_by_seats(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world, pahc_world, monkeypatch, seats, opens, second
):
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", 0)
    keys = ["alx", "desert", "pahc"][:seats]
    sentences = [grounded_sentence(w)[0] for w in (alx_world, desert_world, pahc_world)][:seats]
    client = _table_client(
        selector_script=[{"next": keys[i % seats], "reason": "r"} for i in range(60)],
        stream_scripts=[[sentences[i % seats]] for i in range(60)],
    )
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    held = 1000
    code = code_with(runtime, held)
    created = http.post("/api/session", json={"world_keys": keys}, headers={"X-Cic-Code": code}).json()
    auth = {"Authorization": f"Session {created['session_code']}", "X-Cic-Code": code}
    first = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    assert first.status_code == 200 and first.headers["x-cic-remaining"] == str(held - opens)
    while first.json()["round_open"]:
        first = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
    reply = http.post(f"/api/session/{created['session_id']}/message", json={"text": "and fasting?"}, headers=auth)
    assert reply.status_code == 200 and reply.headers["x-cic-remaining"] == str(held - opens - second)


def test_a_table_round_the_balance_cannot_cover_is_not_admitted(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world
):
    client = long_table_client(alx_world, desert_world)
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    short = table_charge(runtime, 2) - 1
    code = code_with(runtime, short)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers={"X-Cic-Code": code}).json()
    auth = {"Authorization": f"Session {created['session_code']}", "X-Cic-Code": code}
    first = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    while first.json()["round_open"]:
        first = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
    second = http.post(f"/api/session/{created['session_id']}/message", json={"text": "and fasting?"}, headers=auth)
    assert second.json()["routing_action"] == "session_cap_turn"
    assert runtime.meter.status(code).remaining == short


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


# ---- review S2-1: Facilitator-only sittings are few ------------------------------

def test_a_visitor_past_the_session_limit_gets_one_facilitator_only_sitting_a_day(
    store, usage_store, world_loader, registry, runtime
):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), anon_daily_session_limit=0)
    first = http.post("/api/session", json={"world_key": "fix"})
    assert first.status_code == 201
    assert http.post("/api/session", json={"world_key": "fix"}).status_code == 429
    http.cookies.clear()
    assert http.post("/api/session", json={"world_key": "fix"}).status_code == 429


def test_a_script_opening_sittings_in_a_loop_is_stopped_after_the_first(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), anon_daily_session_limit=0)
    results = []
    for _ in range(30):
        http.cookies.clear()
        results.append(http.post("/api/session", json={"world_key": "fix"}).status_code)
    assert results.count(201) <= 2
    assert len(store.list_session_ids()) <= 2


def test_the_facilitator_only_sitting_answers_a_crisis_on_its_fifth_message(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_session_limit=0)
    session_id, auth = open_session(http)
    first = say(http, session_id, auth, "hello there")
    assert first.json()["routing_action"] == "session_cap_turn"
    for _ in range(3):
        again = say(http, session_id, auth, "anyone there?")
        assert again.status_code == 200 and again.json()["routing_action"] == "session_cap_turn"
    client.messages._responses["submit_safety_classification"] = copy.deepcopy(ACUTE)
    fifth = say(http, session_id, auth, "I do not want to be here")
    assert fifth.status_code == 200
    assert fifth.json()["routing_action"] == "safety_turn" and fifth.json()["facilitator"]["resources_appended"]
    assert client.voice_requests == []


# ---- only a live code with tokens left lifts the limit -------------

def test_a_spent_code_does_not_lift_the_session_limit(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_session_limit=0)
    code = code_with(runtime, 1)
    runtime.meter.settle(runtime.meter.reserve(code).reservation, True)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    reply = say(http, session_id, auth, "hello there")
    assert reply.json()["routing_action"] == "session_cap_turn" and reply.json()["voice"] is None
    assert client.voice_requests == []


def test_a_paused_code_does_not_lift_the_session_limit(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_session_limit=0)
    code = code_with(runtime, 5)
    runtime.meter.pause(True)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    assert say(http, session_id, auth, "hello there").json()["voice"] is None
    assert runtime.meter.status(code).remaining == 5


def test_an_extra_sitting_opened_by_a_live_code_draws_down_from_its_first_turn(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_session_limit=0)
    first_cost, second_cost = solo_charge(runtime, 1), solo_charge(runtime, 2)
    code = code_with(runtime, first_cost + second_cost)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    first = say(http, session_id, auth, "one")
    second = say(http, session_id, auth, "two")
    third = say(http, session_id, auth, "three")
    assert first.json()["voice"] is not None and first.headers["x-cic-remaining"] == str(second_cost)
    assert second.json()["voice"] is not None and second.headers["x-cic-remaining"] == "0"
    assert third.json()["routing_action"] == "session_cap_turn"
    assert len(client.voice_requests) == 2


def test_a_code_under_the_session_limit_keeps_its_first_turns_free(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient())
    total = 100
    code = code_with(runtime, total)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP)]
    assert [r.headers["x-cic-remaining"] for r in replies] == [str(total)] * FREE_CAP


def test_a_round_the_code_just_paid_to_zero_can_still_be_continued_past_the_daily_count(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world, monkeypatch
):
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", 0)
    client = long_table_client(alx_world, desert_world)
    http = capped_app(store, usage_store, world_loader, registry, runtime, client, anon_daily_turn_limit=1)
    code = code_with(runtime, table_charge(runtime, 1))
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers={"X-Cic-Code": code}).json()
    auth = {"Authorization": f"Session {created['session_code']}", "X-Cic-Code": code}
    opened = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    assert opened.status_code == 200 and opened.headers["x-cic-remaining"] == "0"
    while opened.json()["round_open"]:
        opened = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
        assert opened.status_code == 200


# ---- review S2 notes: the request diff on the stream path and the table ------------

def test_the_voice_request_is_identical_on_the_stream_path_past_the_free_cap(
    store, usage_store, world_loader, registry, runtime, monkeypatch
):
    turns = FREE_CAP + 1

    def run(deeper, code, cap):
        monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", cap)
        client = RecordingClient()
        http = build(store, usage_store, world_loader, registry, client, deeper=deeper, streaming_enabled=True)
        headers = {"X-Cic-Code": code} if code else {}
        session_id, auth = open_session(http, **headers)
        for i in range(turns):
            reply = http.post(
                f"/api/session/{session_id}/message", json={"text": f"question number {i}"},
                headers={**auth, "Accept": "text/event-stream"},
            )
            assert parse_sse(reply.text)[-1][0] == "done"
        return client.voice_requests[turns - 1]

    off = run(None, None, 50)
    free = run(runtime, None, 50)
    paid = run(runtime, code_with(runtime, 2 * solo_charge(runtime, FREE_CAP + 1)), FREE_CAP)
    assert off == free == paid


def test_the_voice_requests_are_identical_for_a_table_round_past_the_free_rounds(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world, monkeypatch
):
    def run(deeper, code, cap):
        monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", cap)
        client = long_table_client(alx_world, desert_world)
        http = build(store, usage_store, world_loader, registry, client, deeper=deeper)
        headers = {"X-Cic-Code": code} if code else {}
        created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers=headers).json()
        auth = {"Authorization": f"Session {created['session_code']}", **headers}
        marks = []
        for text in ("what is prayer?", "and fasting?"):
            reply = http.post(f"/api/session/{created['session_id']}/message", json={"text": text}, headers=auth)
            assert reply.status_code == 200
            marks.append(len(client.messages.stream_calls))
            while reply.json()["round_open"]:
                reply = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
        return client.messages.stream_calls[marks[0] :]

    off = run(None, None, 5)
    free = run(runtime, None, 5)
    runtime.free = DailyFreeAllowance(runtime.token_rates.free_daily)
    paid = run(runtime, code_with(runtime, 2 * table_charge(runtime, 2)), 1)
    assert off and off == free == paid


def test_a_reply_with_no_words_is_not_charged_and_a_reply_with_words_is():
    from types import SimpleNamespace

    from engine.api.app import _spoke

    assert not _spoke(None)
    assert not _spoke(SimpleNamespace(text=""))
    assert not _spoke(SimpleNamespace(text="  \n"))
    assert not _spoke({"text": ""})
    assert _spoke({"text": "Words."})
    assert _spoke(SimpleNamespace(text="We did not claim to have seen him ourselves."))


@pytest.mark.parametrize("text", ["", "   ", "\n", "One sentence.", " Padded words. "])
def test_a_reply_counts_as_spoken_exactly_when_it_adds_a_pair_to_the_memory_the_next_turn_counts_from(text):
    from engine.api.app import _spoke
    from engine.api.wiring import history_from_transcript

    voice = {"speaker": "fix", "text": text, "citations": []}
    history = history_from_transcript([{"speaker": "participant", "text": "question"}, voice])
    assert _spoke(voice) == (len(history) // 2 == 1)


# ---- the free day: three rounds a conversation, a day's worth of tokens -------------

def run_free_conversation(http, rounds, **headers):
    session_id, auth = open_session(http, **headers)
    replies = [say(http, session_id, auth, f"question {i}") for i in range(rounds)]
    return session_id, auth, replies


def test_a_free_solo_conversation_stops_after_three_rounds_and_says_why(store, usage_store, world_loader, registry, runtime, shipped_caps):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    _, _, replies = run_free_conversation(http, 4)
    assert [r.json()["voice"] is not None for r in replies] == [True, True, True, False]
    assert replies[3].json()["routing_action"] == "session_cap_turn"
    assert replies[3].json()["limit_note"]["key"] == "no_code"
    assert len(client.voice_requests) == 3


def test_with_the_module_off_a_conversation_still_runs_to_the_engines_own_cap(store, usage_store, world_loader, registry, shipped_caps):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client)
    _, _, replies = run_free_conversation(http, 4)
    assert all(r.json()["voice"] is not None for r in replies)


def test_three_free_conversations_use_the_free_day_and_a_fourth_is_refused_until_a_code_carries_it(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    for _ in range(3):
        run_free_conversation(http, 3)
    assert runtime.free.remaining("ip:testclient") == 0
    session_id, auth = open_session(http)
    refused = say(http, session_id, auth, "a fourth conversation")
    assert refused.json()["voice"] is None and refused.json()["limit_note"]["key"] == "no_code"
    code = code_with(runtime, solo_charge(runtime, 1))
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    carried = say(http, session_id, auth, "a fourth conversation")
    assert carried.json()["voice"] is not None
    assert carried.headers["x-cic-remaining"] == "0"


def test_a_code_carries_a_conversation_past_its_third_free_round_at_the_later_price(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    spare = 7
    code = code_with(runtime, solo_charge(runtime, 4, 5) + spare)
    _, _, replies = run_free_conversation(http, 5, **{"X-Cic-Code": code})
    assert all(r.json()["voice"] is not None for r in replies)
    assert runtime.meter.status(code).remaining == spare
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_daily - solo_charge(runtime, 1, 3)


def test_a_failed_voice_call_gives_the_free_tokens_back(store, usage_store, world_loader, registry, runtime, shipped_caps):
    http = build(store, usage_store, world_loader, registry, RecordingClient(voice_fails=True), deeper=runtime)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_daily
    assert runtime.free._held == {}


@pytest.mark.parametrize("seats", [2, 3])
def test_a_free_table_draws_the_free_day_by_its_seats_and_stops_after_three_rounds(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world, pahc_world, shipped_caps, seats
):
    keys = ["alx", "desert", "pahc"][:seats]
    sentences = [grounded_sentence(w)[0] for w in (alx_world, desert_world, pahc_world)][:seats]
    client = _table_client(
        selector_script=[{"next": keys[i % seats], "reason": "r"} for i in range(80)],
        stream_scripts=[[sentences[i % seats]] for i in range(80)],
    )
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    created = http.post("/api/session", json={"world_keys": keys}).json()
    auth = {"Authorization": f"Session {created['session_code']}"}
    drawn = []
    for text in ("one?", "two?", "three?", "four?"):
        reply = http.post(f"/api/session/{created['session_id']}/message", json={"text": text}, headers=auth)
        assert reply.status_code == 200
        drawn.append(runtime.token_rates.free_daily - runtime.free.remaining("ip:testclient"))
        while reply.json()["round_open"]:
            reply = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
    assert reply.json()["routing_action"] == "session_cap_turn"
    first = tokens.charge(runtime.token_rates, 1, seats)
    second = tokens.charge(runtime.token_rates, 2, seats)
    third = tokens.charge(runtime.token_rates, 3, seats)
    expected = [first, first + second, first + second + third]
    # a Table at three seats is 250 + 100 + 100, more than the day holds: its later rounds are refused
    admitted = [d for d in expected if d <= runtime.token_rates.free_daily]
    assert drawn[: len(admitted)] == admitted


# ---- the door: stages narrow the free path, and the Facilitator stays ------------------

class StubDoor:
    def __init__(self, **fields):
        self._state = door_module.DoorState(stage=1, ratio=0.7, ceiling_usd=150.0, **fields)

    def state(self):
        return self._state


def door_app(store, usage_store, world_loader, registry, runtime, client, **fields):
    runtime.door = StubDoor(**fields)
    return build(store, usage_store, world_loader, registry, client, deeper=runtime)


def test_with_free_voice_closed_a_free_visitor_is_refused_with_no_voice_call_and_a_code_still_carries(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    client = RecordingClient()
    http = door_app(store, usage_store, world_loader, registry, runtime, client, free_voice=False)
    session_id, auth = open_session(http)
    refused = say(http, session_id, auth, "hello")
    assert refused.json()["voice"] is None and refused.json()["limit_note"]["key"] == "no_code"
    assert len(client.voice_requests) == 0
    code = code_with(runtime, solo_charge(runtime, 1, 2))
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    assert say(http, session_id, auth, "hello").json()["voice"] is not None
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_daily


def test_with_paid_voice_closed_a_code_is_refused_as_paused_and_nothing_is_spent(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    client = RecordingClient()
    http = door_app(store, usage_store, world_loader, registry, runtime, client, free_voice=False, paid_voice=False)
    code = code_with(runtime, 500)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    refused = say(http, session_id, auth, "hello")
    assert refused.json()["voice"] is None and refused.json()["limit_note"]["key"] == "paused"
    assert len(client.voice_requests) == 0
    assert runtime.meter.status(code).remaining == 500


def test_the_door_limits_free_solo_rounds_but_never_raises_the_free_paths_own_cap(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    http = door_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), solo_free_rounds=2)
    _, _, replies = run_free_conversation(http, 3)
    assert [r.json()["voice"] is not None for r in replies] == [True, True, False]
    runtime.free = DailyFreeAllowance(runtime.token_rates.free_daily)
    runtime.door = StubDoor(solo_free_rounds=9)
    _, _, replies = run_free_conversation(http, 4)
    assert [r.json()["voice"] is not None for r in replies] == [True, True, True, False]


def test_a_code_carries_a_conversation_the_door_has_stopped_for_free(store, usage_store, world_loader, registry, runtime, shipped_caps):
    http = door_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), solo_free_rounds=1)
    code = code_with(runtime, solo_charge(runtime, 2, 3))
    _, _, replies = run_free_conversation(http, 3, **{"X-Cic-Code": code})
    assert all(r.json()["voice"] is not None for r in replies)
    assert runtime.meter.status(code).remaining == 0


def test_the_door_halves_the_free_day(store, usage_store, world_loader, registry, runtime, shipped_caps):
    http = door_app(store, usage_store, world_loader, registry, runtime, RecordingClient(), free_day_share=0.5)
    run_free_conversation(http, 3)
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_daily - solo_charge(runtime, 1, 3)
    session_id, auth = open_session(http)
    assert say(http, session_id, auth, "a second conversation").json()["voice"] is None


def test_the_door_closes_free_tables_and_leaves_free_solo_open(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world, shipped_caps
):
    client = long_table_client(alx_world, desert_world)
    runtime.door = StubDoor(table_free_rounds=0)
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}).json()
    auth = {"Authorization": f"Session {created['session_code']}"}
    refused = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    assert refused.json()["routing_action"] == "session_cap_turn" and refused.json()["limit_note"]["key"] == "no_code"
    solo = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    session_id, solo_auth = open_session(solo)
    assert say(solo, session_id, solo_auth, "hello").json()["voice"] is not None


def test_without_a_door_nothing_narrows(store, usage_store, world_loader, registry, runtime, shipped_caps):
    assert runtime.door is None
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    _, _, replies = run_free_conversation(http, 3)
    assert all(r.json()["voice"] is not None for r in replies)


@pytest.mark.parametrize("label,client_kwargs,expected", SAFETY, ids=[s[0] for s in SAFETY])
def test_a_safety_route_is_answered_at_a_table_the_door_has_closed(
    label, client_kwargs, expected, store, usage_store, world_loader, registry, runtime, alx_world, desert_world, shipped_caps
):
    runtime.door = StubDoor(free_voice=False, paid_voice=False, table_free_rounds=0)
    client = long_table_client(alx_world, desert_world)
    http = table_app(store, usage_store, world_loader, registry, runtime, client)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}, headers={"X-Cic-Code": code_with(runtime, 500)}).json()
    auth = {"Authorization": f"Session {created['session_code']}"}
    if client_kwargs.get("safety_fails"):
        http.app.state.deps.safety_client = RecordingClient(safety_fails=True)
    else:
        client.messages._responses["submit_safety_classification"] = copy.deepcopy(client_kwargs["safety"])
    reply = http.post(f"/api/session/{created['session_id']}/message", json={"text": "I do not know how to say this"}, headers=auth)
    assert reply.status_code == 200, reply.text
    assert reply.json()["routing_action"] == expected
    assert reply.json()["voice"] is None


# ---- bounded spend: real spend stays under the ceiling, and the Facilitator stays at every stage ----

def test_overlapping_free_and_paid_sittings_hit_each_stage_in_order_and_spend_stays_under_the_ceiling(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    from engine.api.deeper_door import DEAREST, DoorMonitor, week_spend_usd
    from engine.m8 import price_tables
    from engine.m8.cost import estimate_cost
    from engine.m8.usage import UsageRecord
    from engine.provider.bedrock import NormalizedUsage

    per_turn = 0.050001
    paid_usage = NormalizedUsage(input_tokens=16_667, output_tokens=0, cache_creation_input_tokens=0, cache_read_input_tokens=0)
    base = 1.0
    settings = dataclasses.replace(load_ops().door, base_usd=base, invoice_factor=1.0)
    runtime.door = DoorMonitor(settings, usage_store, lambda: {"gift": 0, "purchase": 0, "adjustment": 0}, refresh_seconds=0.0)
    runtime.free = DailyFreeAllowance(10_000_000)
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    counter = [0]

    def cost_of(reply):
        if reply.json()["voice"] is not None:
            counter[0] += 1
            usage_store.append(UsageRecord(
                trace_id=f"sim{counter[0]}", session_id="sim", call_kind="voice_generation", model_id=SIM_MODEL,
                provider="bedrock", usage=paid_usage,
            ))
            return True
        return False

    stages = []

    def voice_spend():
        """What the voice has cost: the safety checks every message gets, even a refused one, are not the voice."""
        total = 0.0
        for rec in usage_store.read_all():
            if rec.call_kind == "voice_generation":
                total += estimate_cost(rec.usage, price_tables.price_for_call(rec.call_kind, rec.model_id) or DEAREST).dollars
        return total

    def turn(session_id, auth, text):
        stages.append(runtime.door.state().stage)
        return say(http, session_id, auth, text)

    # free sittings, interleaved: one round each, round and round, until nobody is admitted
    sessions = [open_session(http) for _ in range(40)]
    for round_no in range(3):
        for session_id, auth in sessions:
            cost_of(turn(session_id, auth, f"free {round_no}"))
    spent = week_spend_usd(usage_store, datetime.now(timezone.utc))
    assert stages == sorted(stages), "the door only narrows as spend climbs"
    assert 0.9 * base <= spent
    assert voice_spend() <= base + 0.0001, voice_spend()
    assert runtime.door.state().free_voice is False
    # nothing free is admitted now, and the Facilitator still answers distress
    session_id, auth = open_session(http)
    assert not cost_of(turn(session_id, auth, "one more"))
    acute = RecordingClient(safety=ACUTE)
    http.app.state.deps.safety_client = acute
    distress = say(http, session_id, auth, "I do not know how to say this")
    assert distress.json()["routing_action"] == "safety_turn" and distress.json()["voice"] is None
    http.app.state.deps.safety_client = client
    # a code carries on past the free stop until the door's last stage, then is refused too
    code = code_with(runtime, 1_000_000)
    paid_sessions = [open_session(http, **{"X-Cic-Code": code}) for _ in range(40)]
    for round_no in range(3):
        for session_id, auth in paid_sessions:
            cost_of(turn(session_id, auth, f"paid {round_no}"))
    spent = week_spend_usd(usage_store, datetime.now(timezone.utc))
    assert stages == sorted(stages)
    assert base <= spent
    assert voice_spend() <= base + per_turn + 0.0001, voice_spend()
    final = runtime.door.state()
    assert not final.paid_voice and final.stage == len(settings.stages)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    refused = turn(session_id, auth, "after the last stage")
    assert refused.json()["voice"] is None and refused.json()["limit_note"]["key"] == "paused"
    http.app.state.deps.safety_client = acute
    distress = say(http, session_id, auth, "I do not know how to say this")
    assert distress.json()["routing_action"] == "safety_turn"
    assert runtime.meter.status(code).remaining > 0


# ---- a fault in admission never reopens what the door has closed -----------------------

def _grant_for(runtime, *, code, completed, seats=1, free_cap=SHIPPED_SESSION_TURN_CAP):
    from engine.api.deeper_admission import Admission

    admission = Admission(runtime, code, session_id="s", free_cap=free_cap, seats=seats, visitor="v")
    return admission.provider(completed, False)


def test_a_fault_at_a_door_closed_to_free_voice_still_refuses_even_with_a_code(runtime, monkeypatch):
    runtime.door = StubDoor(free_voice=False)

    def down(*_a, **_k):
        raise RuntimeError("meter down")

    monkeypatch.setattr(runtime.meter, "reserve", down)
    grant = _grant_for(runtime, code=code_with(runtime, 500), completed=1)
    assert grant.cap <= 1 and grant.limit_text is not None


def test_a_fault_in_the_free_day_keeps_to_the_rounds_the_door_allows(runtime, monkeypatch):
    runtime.door = StubDoor(solo_free_rounds=1, free_day_share=0.5)

    def down(*_a, **_k):
        raise ValueError("free day down")

    monkeypatch.setattr(runtime.free, "reserve", down)
    assert _grant_for(runtime, code=None, completed=1).cap == 1
    assert _grant_for(runtime, code=None, completed=0).cap == 1


def test_a_fault_with_the_door_open_leaves_the_free_grant_as_it_was(runtime, monkeypatch):
    def down(*_a, **_k):
        raise RuntimeError("free day down")

    monkeypatch.setattr(runtime.free, "reserve", down)
    assert _grant_for(runtime, code=None, completed=1).cap == runtime.token_rates.free_rounds
