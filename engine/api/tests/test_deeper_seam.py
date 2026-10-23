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
from engine.api.deeper_ops import load_ops
from engine.api.deeper_routes import DeeperRuntime
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.deeper import codes, tokens
from engine.deeper.bound import MessageBound
from engine.deeper.claims import ClaimStore
from engine.deeper.free import FreeAllowance
from engine.deeper.meter import Meter
from engine.m4 import facilitator_turns

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
    """The engine's own free caps, as shipped, for the tests that prove the free window on top of them."""
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


def spend_free_allowance(runtime, visitor="ip:testclient"):
    """Draws the visitor's whole free window, so the next turn is carried by a code or refused."""
    runtime.free.settle(runtime.free.reserve(visitor, runtime.free.remaining(visitor)), True)


def code_with(runtime, amount, kind="single"):
    return runtime.meter.mint(kind, amount, f"pi_{codes.generate()}")[0]


def expired_tester_code(runtime, tokens=20000, made=date(2026, 9, 1), days=30):
    """A tester code made on an earlier day whose last day has passed by the runtime's today."""
    today = runtime.meter._clock
    runtime.meter._clock = lambda: made
    try:
        (code,) = runtime.meter.mint("single", tokens, f"tester_{codes.generate()}", source="tester", expires_in_days=days)
    finally:
        runtime.meter._clock = today
    return code


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
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_window - solo_charge(runtime, 1, turns)

    runtime.free = FreeAllowance(runtime.meter, runtime.token_rates.free_window)
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
    spend_free_allowance(runtime)
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
    spend_free_allowance(runtime)
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


# ---- no daily count ----------------------------------------------------------------

def capped_app(store, usage_store, world_loader, registry, runtime, client, **kwargs):
    return build(
        store, usage_store, world_loader, registry, client, deeper=runtime,
        anon_cap_enabled=True, anon_visitor_secret="s" * 32, **kwargs,
    )


def test_a_visitor_with_free_tokens_left_is_never_closed_by_how_many_conversations_they_opened(
    store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient()
    http = capped_app(store, usage_store, world_loader, registry, runtime, client)
    for n in range(6):
        session_id, auth = open_session(http)
        reply = say(http, session_id, auth, f"question {n}")
        assert reply.status_code == 200 and reply.json()["voice"] is not None, n
    assert len(client.voice_requests) == 6


def test_a_conversation_whose_first_voice_reply_fails_uses_nothing_up(store, usage_store, world_loader, registry, runtime):
    failing = build(store, usage_store, world_loader, registry, RecordingClient(voice_fails=True), deeper=runtime)
    window = runtime.token_rates.free_window
    for n in range(8):
        session_id, auth = open_session(failing)
        assert say(failing, session_id, auth, f"question {n}").status_code == 502
    assert runtime.free.remaining("ip:testclient") == window
    working = RecordingClient()
    http = build(store, usage_store, world_loader, registry, working, deeper=runtime)
    session_id, auth = open_session(http)
    assert say(http, session_id, auth, "now it works").json()["voice"] is not None


# ---- safety: the check-in and the crisis turn at every limit ------------------

def limit_setup(name, store, usage_store, world_loader, registry, runtime, client):
    """Builds an app and returns (http, session_id, auth) standing at the named limit."""
    if name == "free_cap":
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
    elif name == "expired_tester":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http, **{"X-Cic-Code": expired_tester_code(runtime)})
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
    elif name == "free_allowance_spent":
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        runtime.free.settle(runtime.free.reserve("ip:testclient", runtime.token_rates.free_window), True)
        session_id, auth = open_session(http)
    elif name == "paid_round_cap":
        runtime.paid_round_cap = FREE_CAP
        http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
        session_id, auth = open_session(http, **{"X-Cic-Code": code_with(runtime, 5000)})
        for i in range(FREE_CAP):
            assert say(http, session_id, auth, f"q{i}").status_code == 200
    else:
        raise AssertionError(name)
    return http, session_id, auth


LIMITS = [
    "free_cap", "zero_balance", "expired_tester", "paused", "wrong_code", "module_error",
    "free_allowance_spent", "paid_round_cap",
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
    cases = [("spent", spent), ("spent", expired_tester_code(runtime)), ("daily_ceiling", group), ("code_not_accepted", codes.generate())]
    for expected, code in cases:
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


def test_a_tester_code_carries_turns_through_its_last_day_and_after_it_is_refused_as_spent_with_its_safety_check_first(
    store, usage_store, world_loader, registry, runtime
):
    day = [date(2026, 10, 5)]
    runtime.meter._clock = lambda: day[0]
    (code,) = runtime.meter.mint("single", 20000, "tester_seam", source="tester", expires_in_days=1)
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    day[0] = date(2026, 10, 6)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    for i in range(FREE_CAP + 1):
        assert say(http, session_id, auth, f"q{i}").json()["routing_action"] != "session_cap_turn"
    spent = runtime.meter.status(code).tokens_used
    assert spent == solo_charge(runtime, FREE_CAP + 1)
    day[0] = date(2026, 10, 7)
    voice_before, safety_before = len(client.voice_requests), client.safety_calls
    reply = say(http, session_id, auth, "more")
    assert reply.json()["routing_action"] == "session_cap_turn"
    assert reply.json()["limit_note"] == {"key": "spent", "text": runtime.ops.notes["spent"]}
    assert client.safety_calls == safety_before + 1 and len(client.voice_requests) == voice_before
    assert runtime.meter.status(code).tokens_used == spent and runtime.meter.status(code).remaining == 0


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


# ---- the free count ----------------------------------------------------------------

def test_a_free_visitor_is_told_their_free_tokens_left_and_a_code_holder_is_not(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    window = runtime.free.window_amount
    session_id, auth = open_session(http)
    first = say(http, session_id, auth, "hello")
    assert first.headers["x-cic-free-left"] == str(window - solo_charge(runtime, 1))
    assert "x-cic-remaining" not in first.headers
    second = say(http, session_id, auth, "again")
    assert second.headers["x-cic-free-left"] == str(window - solo_charge(runtime, 1) - solo_charge(runtime, 2))
    code = code_with(runtime, 1000)
    held_id, held_auth = open_session(http, **{"X-Cic-Code": code})
    reply = say(http, held_id, held_auth, "hello")
    assert "x-cic-free-left" not in reply.headers and "x-cic-remaining" in reply.headers


def test_the_stream_gives_the_free_count_in_its_final_event(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime, streaming_enabled=True)
    session_id, auth = open_session(http)
    reply = http.post(f"/api/session/{session_id}/message", json={"text": "hello"}, headers={**auth, "Accept": "text/event-stream"})
    done = parse_sse(reply.text)[-1][1]
    assert done["free_left"] == runtime.free.window_amount - solo_charge(runtime, 1)
    assert "remaining" not in done


def test_the_free_count_excludes_a_reservation_in_flight_and_gives_it_back(store, usage_store, world_loader, registry, runtime):
    held = runtime.free.reserve("visitor-a", 25)
    assert held is not None
    assert runtime.free.left("visitor-a") == runtime.free.window_amount - 25
    runtime.free.settle(held, False)
    assert runtime.free.left("visitor-a") == runtime.free.window_amount
    spent = runtime.free.reserve("visitor-a", 25)
    runtime.free.settle(spent, True)
    assert runtime.free.left("visitor-a") == runtime.free.window_amount - 25


def test_a_module_that_is_off_reports_no_free_count(store, usage_store, world_loader, registry):
    http = build(store, usage_store, world_loader, registry, RecordingClient())
    session_id, auth = open_session(http)
    assert "x-cic-free-left" not in say(http, session_id, auth, "hello").headers


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
    spend_free_allowance(runtime)
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

# ---- only a live code with tokens left lifts the limit -------------

def test_a_code_keeps_a_conversations_first_turns_free(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient())
    total = 100
    code = code_with(runtime, total)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP)]
    assert [r.headers["x-cic-remaining"] for r in replies] == [str(total)] * FREE_CAP


def test_a_round_the_code_just_paid_to_zero_can_still_be_continued(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world, monkeypatch
):
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", 0)
    client = long_table_client(alx_world, desert_world)
    http = capped_app(store, usage_store, world_loader, registry, runtime, client)
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
    runtime.free = FreeAllowance(runtime.meter, runtime.token_rates.free_window)
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


# ---- the free window: three rounds a conversation, a day's worth of tokens -------------

def run_free_conversation(http, rounds, **headers):
    session_id, auth = open_session(http, **headers)
    replies = [say(http, session_id, auth, f"question {i}") for i in range(rounds)]
    return session_id, auth, replies


def test_a_free_solo_conversation_runs_to_the_engines_round_cap_and_says_why(store, usage_store, world_loader, registry, runtime, shipped_caps):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    rounds = SHIPPED_SESSION_TURN_CAP
    _, _, replies = run_free_conversation(http, rounds + 1)
    assert [r.json()["voice"] is not None for r in replies] == [True] * rounds + [False]
    assert replies[rounds].json()["routing_action"] == "session_cap_turn"
    assert replies[rounds].json()["limit_note"]["key"] == "no_code"
    assert len(client.voice_requests) == rounds
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_window - solo_charge(runtime, 1, rounds)


def test_only_the_free_tokens_end_a_free_conversation_before_the_engines_cap(store, usage_store, world_loader, registry, runtime, shipped_caps):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    runtime.free = FreeAllowance(runtime.meter, solo_charge(runtime, 1, 6))
    _, _, replies = run_free_conversation(http, 8)
    assert [r.json()["voice"] is not None for r in replies] == [True] * 6 + [False] * 2
    assert replies[6].json()["limit_note"]["key"] == "no_code"


def test_with_the_module_off_a_conversation_still_runs_to_the_engines_own_cap(store, usage_store, world_loader, registry, shipped_caps):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client)
    _, _, replies = run_free_conversation(http, 4)
    assert all(r.json()["voice"] is not None for r in replies)


def test_five_free_conversations_use_the_free_window_and_a_sixth_is_refused_until_a_code_carries_it(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    for _ in range(5):
        run_free_conversation(http, 3)
    assert runtime.free.remaining("ip:testclient") == 0
    session_id, auth = open_session(http)
    refused = say(http, session_id, auth, "a sixth conversation")
    assert refused.json()["voice"] is None and refused.json()["limit_note"]["key"] == "no_code"
    code = code_with(runtime, solo_charge(runtime, 1))
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    carried = say(http, session_id, auth, "a sixth conversation")
    assert carried.json()["voice"] is not None
    assert carried.headers["x-cic-remaining"] == "0"


def test_a_code_carries_a_conversation_past_the_engines_free_cap_at_the_later_price(
    store, usage_store, world_loader, registry, runtime, shipped_caps
):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    free_rounds = SHIPPED_SESSION_TURN_CAP
    spare = 7
    code = code_with(runtime, solo_charge(runtime, free_rounds + 1, free_rounds + 2) + spare)
    _, _, replies = run_free_conversation(http, free_rounds + 2, **{"X-Cic-Code": code})
    assert all(r.json()["voice"] is not None for r in replies)
    assert runtime.meter.status(code).remaining == spare
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_window - solo_charge(runtime, 1, free_rounds)


def test_a_failed_voice_call_gives_the_free_tokens_back(store, usage_store, world_loader, registry, runtime, shipped_caps):
    http = build(store, usage_store, world_loader, registry, RecordingClient(voice_fails=True), deeper=runtime)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    assert runtime.free.remaining("ip:testclient") == runtime.token_rates.free_window
    assert runtime.free._held == {}


@pytest.mark.parametrize("seats", [2, 3])
def test_a_free_table_draws_the_free_window_by_its_seats_and_stops_after_three_rounds(
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
        drawn.append(runtime.token_rates.free_window - runtime.free.remaining("ip:testclient"))
        while reply.json()["round_open"]:
            reply = http.post(f"/api/session/{created['session_id']}/continue", headers=auth)
    assert reply.json()["routing_action"] == "session_cap_turn"
    first = tokens.charge(runtime.token_rates, 1, seats)
    second = tokens.charge(runtime.token_rates, 2, seats)
    third = tokens.charge(runtime.token_rates, 3, seats)
    expected = [first, first + second, first + second + third]
    # a Table at three seats is 250 + 100 + 100, more than the day holds: its later rounds are refused
    admitted = [d for d in expected if d <= runtime.token_rates.free_window]
    assert drawn[: len(admitted)] == admitted


# ---- a fault in admission leaves the free grant -----------------------

def _grant_for(runtime, *, code, completed, seats=1, free_cap=SHIPPED_SESSION_TURN_CAP):
    from engine.api.deeper_admission import Admission

    admission = Admission(runtime, code, free_cap=free_cap, seats=seats, visitor="v")
    return admission.provider(completed)


def test_a_fault_in_the_free_window_leaves_the_free_grant_as_it_was(runtime, monkeypatch):
    def down(*_a, **_k):
        raise RuntimeError("free day down")

    monkeypatch.setattr(runtime.free, "reserve", down)
    assert _grant_for(runtime, code=None, completed=1).cap == SHIPPED_SESSION_TURN_CAP


# ---- the standing measure counts each refused turn once, by its reason ----------------------

def _turn(runtime, *, code, completed, seats=1):
    from engine.api.deeper_admission import Admission

    admission = Admission(runtime, code, free_cap=SHIPPED_SESSION_TURN_CAP, seats=seats, visitor="v")
    grant = admission.provider(completed)
    admission.finish(False)
    return grant


def _refusals(runtime) -> dict:
    rows = runtime.meter.measures(1)
    return {k[len("refused_"):]: v for k, v in rows[0].items() if k.startswith("refused_") and v} if rows else {}


def test_a_turn_with_no_code_past_the_free_rounds_counts_once(runtime):
    _turn(runtime, code=None, completed=SHIPPED_SESSION_TURN_CAP)
    assert _refusals(runtime) == {"free_rounds_done": 1}


def test_a_turn_the_free_window_cannot_cover_counts_as_the_free_allowance_spent(runtime):
    runtime.free.settle(runtime.free.reserve("v", runtime.token_rates.free_window), True)
    _turn(runtime, code=None, completed=0)
    assert _refusals(runtime) == {"free_allowance_spent": 1}


def test_a_code_without_enough_tokens_counts_as_too_few_or_spent(runtime):
    _turn(runtime, code=code_with(runtime, 5), completed=SHIPPED_SESSION_TURN_CAP)
    assert sum(_refusals(runtime).values()) == 1 and set(_refusals(runtime)) <= {"too_few", "spent"}


def test_an_admitted_turn_counts_no_refusal(runtime):
    _turn(runtime, code=None, completed=0)
    assert _refusals(runtime) == {}


def test_a_turn_is_counted_when_it_ends_not_when_it_is_decided(runtime):
    from engine.api.deeper_admission import Admission

    admission = Admission(runtime, None, free_cap=SHIPPED_SESSION_TURN_CAP, seats=1, visitor="v")
    admission.provider(SHIPPED_SESSION_TURN_CAP)
    assert _refusals(runtime) == {}
    admission.finish(False)
    admission.finish(False)
    assert _refusals(runtime) == {"free_rounds_done": 1}


def test_a_refusal_that_cannot_be_counted_still_reports_what_the_code_has_left(runtime, monkeypatch):
    from engine.api.deeper_admission import Admission

    def down(*_a, **_k):
        raise RuntimeError("daily table down")

    monkeypatch.setattr(runtime.meter, "measure", down)
    code = code_with(runtime, 5)
    admission = Admission(runtime, code, free_cap=SHIPPED_SESSION_TURN_CAP, seats=1, visitor="v")
    admission.provider(SHIPPED_SESSION_TURN_CAP)
    assert admission.finish(False) == 5


# ---- the paid conversation's round cap -----------------------------------------------------

def test_a_paid_conversation_stops_at_its_round_cap_and_spends_nothing(runtime):
    cap = SHIPPED_SESSION_TURN_CAP + 2
    runtime.paid_round_cap = cap
    code = code_with(runtime, 5000)
    before = runtime.meter.status(code).remaining
    grant = _turn(runtime, code=code, completed=cap)
    assert grant.cap <= cap and grant.limit_text is not None
    assert runtime.meter.status(code).remaining == before
    assert _refusals(runtime) == {"paid_round_cap": 1}


def test_a_paid_conversation_below_its_cap_is_carried(runtime):
    cap = SHIPPED_SESSION_TURN_CAP + 2
    runtime.paid_round_cap = cap
    code = code_with(runtime, 5000)
    assert _turn(runtime, code=code, completed=cap - 1).cap == cap
    assert _refusals(runtime) == {}


def test_no_cap_leaves_a_long_paid_conversation_alone(runtime):
    runtime.paid_round_cap = None
    code = code_with(runtime, 5000)
    assert _turn(runtime, code=code, completed=60).cap == 61


def test_the_shipped_cap_is_provisional_and_above_the_engines_free_cap():
    ops = load_ops()
    assert ops.paid_round_cap_provisional is True
    assert ops.paid_round_cap > SHIPPED_SESSION_TURN_CAP


def test_the_round_cap_refusal_gets_the_facilitator_and_no_new_words(runtime):
    runtime.paid_round_cap = SHIPPED_SESSION_TURN_CAP + 2
    from engine.api.deeper_admission import Admission

    admission = Admission(runtime, code_with(runtime, 5000), free_cap=SHIPPED_SESSION_TURN_CAP, seats=1, visitor="v")
    grant = admission.provider(SHIPPED_SESSION_TURN_CAP + 2)
    assert grant.limit_text == runtime.ops.limit_text
    assert admission.limit_note("session_cap_turn") is None


def test_a_turn_with_no_code_past_the_cap_is_not_counted_as_the_paid_cap(runtime):
    runtime.paid_round_cap = 3
    _turn(runtime, code=None, completed=SHIPPED_SESSION_TURN_CAP + 5)
    assert "paid_round_cap" not in _refusals(runtime)
    assert sum(_refusals(runtime).values()) == 1


def test_what_a_visitor_has_drawn_survives_a_deploy_so_the_window_is_not_refilled(tmp_path, store, usage_store, world_loader, registry, shipped_caps):
    path = str(tmp_path / "persist.db")
    first = DeeperRuntime(
        meter=Meter(path, clock=lambda: date(2026, 10, 5), free_key=b"k" * 32), claims=ClaimStore(str(tmp_path / "c1.db")),
        webhook_secret="whsec_x", products={}, miss_delay_seconds=0.0, ops=load_ops(),
    )
    try:
        http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=first)
        for _ in range(5):
            run_free_conversation(http, 3)
        assert first.free.remaining("ip:testclient") == 0
    finally:
        first.meter.close()
        first.claims.close()
    second = DeeperRuntime(
        meter=Meter(path, clock=lambda: date(2026, 10, 5), free_key=b"k" * 32), claims=ClaimStore(str(tmp_path / "c2.db")),
        webhook_secret="whsec_x", products={}, miss_delay_seconds=0.0, ops=load_ops(),
    )
    try:
        http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=second)
        session_id, auth = open_session(http)
        refused = say(http, session_id, auth, "after the deploy")
        assert refused.json()["voice"] is None and refused.json()["limit_note"]["key"] == "no_code"
    finally:
        second.meter.close()
        second.claims.close()


# ---- the monthly bound on messages that get a safety check and no voice ------------


VISITOR = "ip:testclient"
NETWORK = "testclient"


def bounded(runtime, per_visitor=2, per_network=100):
    runtime.bound = MessageBound(runtime.meter, per_visitor, per_network)
    return runtime.bound


def reach(runtime, per_visitor=2):
    bound = bounded(runtime, per_visitor)
    for _ in range(per_visitor):
        bound.count(VISITOR, NETWORK)


def assert_fixed_line(reply):
    body = reply.json()
    assert reply.status_code == 200, reply.text
    assert body["routing_action"] == "visitor_bound_turn" and body["voice"] is None
    assert body["facilitator"]["text"] == facilitator_turns.VISITOR_BOUND.text
    assert body["facilitator"]["resources_appended"]
    assert "reach out to someone real" in body["facilitator"]["text"]


def test_messages_that_get_a_pause_count_and_past_the_count_the_fixed_line_answers(
    store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    bounded(runtime, per_visitor=2)
    session_id, auth = open_session(http)
    voiced = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP)]
    assert all(r.json()["voice"] is not None for r in voiced)
    paused = [say(http, session_id, auth, f"more {i}") for i in range(2)]
    assert all(r.json()["routing_action"] == "session_cap_turn" for r in paused)
    safety_before, voice_before = client.safety_calls, len(client.voice_requests)
    assert_fixed_line(say(http, session_id, auth, "and again"))
    assert (client.safety_calls, len(client.voice_requests)) == (safety_before, voice_before), "no model call past the count"


def test_voiced_messages_never_count(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    bounded(runtime, per_visitor=1)
    for _ in range(3):
        session_id, auth = open_session(http)
        assert say(http, session_id, auth, "hello").json()["voice"] is not None
    assert not runtime.bound.reached(VISITOR, NETWORK)


def test_a_crisis_message_past_the_count_gets_the_redirect_from_code_and_no_model_call(
    store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient(safety=ACUTE)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    reach(runtime)
    session_id, auth = open_session(http)
    reply = say(http, session_id, auth, "I do not want to be here anymore")
    assert_fixed_line(reply)
    assert client.safety_calls == 0 and client.voice_requests == []


@pytest.mark.parametrize("label,client_kwargs", [("acute", dict(safety=ACUTE)), ("unclear", dict(safety=UNCLEAR)), ("failed", dict(safety_fails=True))])
def test_every_kind_of_message_past_the_count_gets_the_same_fixed_line(
    label, client_kwargs, store, usage_store, world_loader, registry, runtime
):
    client = RecordingClient(**client_kwargs)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    reach(runtime)
    session_id, auth = open_session(http)
    assert_fixed_line(say(http, session_id, auth, "I do not know how to say this"))
    assert client.safety_calls == 0 and client.voice_requests == []


def test_a_code_with_tokens_is_outside_the_count(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    reach(runtime)
    code = code_with(runtime, solo_charge(runtime, 1))
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    assert say(http, session_id, auth, "hello there").json()["voice"] is not None


def test_a_spent_code_is_inside_the_count(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    reach(runtime)
    code = code_with(runtime, 1)
    runtime.meter.settle(runtime.meter.reserve(code).reservation, True)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    assert_fixed_line(say(http, session_id, auth, "hello there"))


def test_paused_codes_leave_a_code_holder_inside_the_count(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    reach(runtime)
    code = code_with(runtime, 500)
    runtime.meter.pause(True)
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    assert_fixed_line(say(http, session_id, auth, "hello there"))


def test_a_network_reaches_its_count_whatever_cookie_each_visitor_holds(store, usage_store, world_loader, registry, runtime):
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient())
    bound = bounded(runtime, per_visitor=100, per_network=2)
    bound.count("someone-else", NETWORK)
    bound.count("another", NETWORK)
    session_id, auth = open_session(http)
    assert_fixed_line(say(http, session_id, auth, "hello there"))
    http.cookies.clear()
    session_id, auth = open_session(http)
    assert_fixed_line(say(http, session_id, auth, "a fresh cookie changes nothing"))


def test_an_ipv6_home_is_one_network_across_its_blocks(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    bound = bounded(runtime, per_visitor=100, per_network=1)
    bound.count("someone", "2001:db8:1::/56")
    session_id, auth = open_session(http)
    reply = http.post(
        f"/api/session/{session_id}/message", json={"text": "hello"}, headers={**auth, "x-forwarded-for": "2001:db8:1:7::9"}
    )
    assert_fixed_line(reply)
    other = http.post(
        f"/api/session/{session_id}/message", json={"text": "hello"}, headers={**auth, "x-forwarded-for": "2001:db8:2:7::9"}
    )
    assert other.json()["routing_action"] != "visitor_bound_turn"


def test_a_message_refused_after_its_safety_check_counts(store, usage_store, world_loader, registry, runtime):
    from engine.api.wiring import MAX_MESSAGE_LENGTH

    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    bounded(runtime, per_visitor=2)
    session_id, auth = open_session(http)
    for _ in range(2):
        say(http, session_id, auth, "x" * (MAX_MESSAGE_LENGTH + 1))
    assert_fixed_line(say(http, session_id, auth, "hello"))


def test_the_fixed_line_is_sent_on_the_stream_path_too(store, usage_store, world_loader, registry, runtime):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime, streaming_enabled=True)
    reach(runtime)
    session_id, auth = open_session(http)
    reply = http.post(f"/api/session/{session_id}/message", json={"text": "hello"}, headers={**auth, "Accept": "text/event-stream"})
    events = parse_sse(reply.text)
    assert [name for name, _ in events] == ["done"]
    body = events[0][1]
    assert body["routing_action"] == "visitor_bound_turn" and body["facilitator"]["resources_appended"]
    assert client.safety_calls == 0 and client.voice_requests == []


def test_the_fixed_line_answers_a_table_with_no_model_call(
    store, usage_store, world_loader, registry, runtime, alx_world, desert_world
):
    client = RecordingClient()
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    reach(runtime)
    created = http.post("/api/session", json={"world_keys": ["alx", "desert"]}).json()
    auth = {"Authorization": f"Session {created['session_code']}"}
    reply = http.post(f"/api/session/{created['session_id']}/message", json={"text": "what is prayer?"}, headers=auth)
    body = reply.json()
    assert reply.status_code == 200 and body["routing_action"] == "visitor_bound_turn"
    assert body["voice"] is None and body["facilitator"][0]["resources_appended"]
    assert client.safety_calls == 0 and client.voice_requests == []


def test_past_the_count_nothing_is_stored_for_the_message(store, usage_store, world_loader, registry, runtime):
    http = build(store, usage_store, world_loader, registry, RecordingClient(), deeper=runtime)
    reach(runtime)
    session_id, auth = open_session(http)
    events_before = len(list(store.read_events(session_id)))
    say(http, session_id, auth, "a private worry")
    assert len(list(store.read_events(session_id))) == events_before


def test_a_fault_in_the_count_leaves_the_safety_check_running(store, usage_store, world_loader, registry, runtime, monkeypatch):
    client = RecordingClient(safety=ACUTE)
    http = build(store, usage_store, world_loader, registry, client, deeper=runtime)
    reach(runtime)

    def down(*_a, **_k):
        raise RuntimeError("meter down")

    monkeypatch.setattr(runtime.bound, "reached", down)
    session_id, auth = open_session(http)
    reply = say(http, session_id, auth, "I do not want to be here anymore")
    assert reply.json()["routing_action"] == "safety_turn"


def test_the_flag_off_has_no_bound(store, usage_store, world_loader, registry):
    http = build(store, usage_store, world_loader, registry, RecordingClient())
    for _ in range(FREE_CAP + 3):
        session_id, auth = open_session(http)
        assert say(http, session_id, auth, "hello").status_code == 200


def test_the_words_past_the_count_read_at_the_target_level_and_name_no_code():
    from engine.m7.turn_readability import score_turn

    assert score_turn(facilitator_turns.VISITOR_BOUND.text).passed
    assert not re.search(r"\b(codes?|pay|paid|price|balance|stripe)\b", facilitator_turns.VISITOR_BOUND.text, re.I)


# ---- the network free window, through admission --------------------------------------

def test_visitors_with_new_cookies_draw_from_the_networks_pool_and_then_are_paused(
    store, usage_store, world_loader, registry, runtime
):
    first_round = solo_charge(runtime, 1)
    runtime.free = FreeAllowance(runtime.meter, 2 * first_round, 2 * first_round + first_round // 2)
    http = capped_app(store, usage_store, world_loader, registry, runtime, RecordingClient())
    results = []
    for _ in range(3):
        http.cookies.clear()
        session_id, auth = open_session(http)
        results.append(say(http, session_id, auth, "hello").json())
    assert [r["voice"] is not None for r in results] == [True, True, False]
    assert results[-1]["routing_action"] == "session_cap_turn"


def test_the_network_pool_is_five_allowances_as_shipped(runtime):
    assert runtime.free.network_window_amount == 5 * runtime.free.window_amount == 2750
