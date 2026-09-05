"""Table sessions end to end against create_app() with fakes (Artifact-7
SS6, contract-test items of SS8): creation shapes, the turn-at-a-time round
lifecycle (floor/cap/selector close), governed rounds, the 409 sequencing
contract, selector fallback, the session cap at the table unit, and M8's
per-world attribution. The isolation property has its own suite
(test_table_isolation.py)."""
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from engine.api.app import create_app
from engine.api.tests.conftest import reader_response, safety_response
from engine.api.wiring import _load_world
from engine.m4.grounding_net import all_text, content_words
from engine.m4 import evidence

_FAKE_USAGE = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=_FAKE_USAGE))

    def __exit__(self, *exc):
        return False


class _TableMessages:
    """Like conftest's _FakeMessages plus a scripted turn selector and
    per-call stream scripts: each voice turn pops the next script, so a
    multi-turn round can put different words in different voices' mouths."""

    def __init__(self, *, safety, reader, selector_script, stream_scripts):
        self._responses = {"submit_safety_classification": safety, "submit_reader_output": reader}
        self.selector_script = list(selector_script)
        self.stream_scripts = list(stream_scripts)
        self.selector_enums_seen = []
        self.stream_calls = []

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        if name == "submit_turn_selection":
            self.selector_enums_seen.append(list(tools[0]["input_schema"]["properties"]["next"]["enum"]))
            return SimpleNamespace(content=[_FakeToolUse(name, self.selector_script.pop(0))], usage=_FAKE_USAGE)
        return SimpleNamespace(content=[_FakeToolUse(name, self._responses[name])], usage=_FAKE_USAGE)

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        self.stream_calls.append({"system": system, "messages": messages})
        return _FakeStreamCtx(self.stream_scripts.pop(0))


class TableFakeClient:
    def __init__(self, **kwargs):
        self.messages = _TableMessages(**kwargs)


def grounded_sentence(world) -> tuple[str, str]:
    """A sentence guaranteed to pass the speaker's own grounding net: the
    record's own content words, tagged with the record's own id (100%
    overlap with its tagged record by construction)."""
    repo = evidence.repository_records_by_id(world.repository)
    for rid, rec in sorted(repo.items()):
        # Purely alphabetic words only: a token carrying an apostrophe reads
        # to the net as a quoted span and fails its verbatim check.
        words = sorted(w for w in content_words(all_text(rec)) if w.isalpha())
        if len(words) >= 10:
            return f"{' '.join(words[:10])} [[{rid}]].", rid
    raise AssertionError("no repository record with enough content words")


def _http(*, store, usage_store, world_loader, registry, client):
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix",
    )
    return TestClient(app)


def _table_client(*, selector_script, stream_scripts, safety=None, reader=None):
    return TableFakeClient(
        safety=safety or safety_response("NO_SIGNAL"),
        reader=reader or reader_response(),
        selector_script=selector_script,
        stream_scripts=stream_scripts,
    )


def _create_table(http, world_keys=("alx", "desert")):
    resp = http.post("/api/session", json={"world_keys": list(world_keys)})
    assert resp.status_code == 201, resp.text
    body = resp.json()
    return body["session_id"], {"Authorization": f"Session {body['session_code']}"}


@pytest.fixture
def alx_world(world_loader, registry):
    return _load_world(world_loader, registry, "alx")


@pytest.fixture
def desert_world(world_loader, registry):
    return _load_world(world_loader, registry, "desert")


@pytest.fixture
def pahc_world(world_loader, registry):
    return _load_world(world_loader, registry, "pahc")


# --- creation ---


def test_create_table_session_and_door(store, usage_store, world_loader, registry, alx_world, desert_world):
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
                 client=_table_client(selector_script=[], stream_scripts=[]))
    session_id, auth = _create_table(http)
    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()
    assert transcript["mode"] == "table"
    assert transcript["world_keys"] == ["alx", "desert"]
    assert transcript["world_key"] is None
    assert not transcript["round_open"]
    door = transcript["transcript"][0]
    assert door["speaker"] == "facilitator"
    assert alx_world.frame["representative"]["name"] in door["text"]
    assert desert_world.frame["representative"]["name"] in door["text"]


def test_create_table_session_bad_shapes(store, usage_store, world_loader, registry):
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
                 client=_table_client(selector_script=[], stream_scripts=[]))
    assert http.post("/api/session", json={"world_keys": ["alx"]}).status_code == 400
    assert http.post("/api/session", json={"world_keys": ["alx", "desert", "pahc", "syr"]}).status_code == 400
    assert http.post("/api/session", json={"world_keys": ["alx", "alx"]}).status_code == 400
    assert http.post("/api/session", json={"world_key": "alx", "world_keys": ["alx", "desert"]}).status_code == 400
    assert http.post("/api/session", json={"world_keys": ["alx", "nope"]}).status_code == 400


# --- the round lifecycle ---


def test_round_turn_at_a_time_to_selector_close(store, usage_store, world_loader, registry, alx_world, desert_world):
    alx_sentence, alx_rid = grounded_sentence(alx_world)
    desert_sentence, desert_rid = grounded_sentence(desert_world)
    # Positions 2 and 3 are forced moves at a two-seat table (one eligible
    # voice, floor unmet) - the selector model is consulted only at the
    # genuine choices: the opening pick and the close decision.
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "most directly positioned"},
            {"next": "close", "reason": "genuinely answered"},
        ],
        stream_scripts=[[alx_sentence], [desert_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)

    first = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert first["round_no"] == 1 and first["position"] == 1 and first["round_open"]
    assert first["voice"]["speaker"] == "alx"
    assert first["turn_selected"]["world_key"] == "alx"
    assert first["turn_no"] is None
    # Below the floor, close was not even in the selector's enum.
    assert "close" not in client.messages.selector_enums_seen[0]

    second = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert second["position"] == 2 and second["voice"]["speaker"] == "desert" and second["round_open"]

    third = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert third["position"] == 3 and third["voice"]["speaker"] == "alx" and third["round_open"]
    assert "forced move" in third["turn_selected"]["reason"]

    close = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert not close["round_open"] and close["voice"] is None and close["turn_no"] == 1
    # At the floor, close became a legal move (second real consult - the
    # forced positions never reached the model).
    assert "close" in client.messages.selector_enums_seen[1]
    assert len(client.messages.selector_enums_seen) == 2

    # The round is committed - the next participant message opens round 2.
    assert http.post(f"/api/session/{session_id}/continue", headers=auth).status_code == 409
    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()
    assert transcript["turn_count"] == 1
    speakers = [t["speaker"] for t in transcript["transcript"]]
    assert speakers == ["facilitator", "participant", "alx", "desert", "alx"]


def test_round_cap_closes_at_five_for_two_seats(store, usage_store, world_loader, registry, alx_world, desert_world):
    """Mark's ruling, 2026-09-05: 'for 2 voices and a participant, the max
    turns should be 5' (RoundConfig.cap_for(2) == 5, superseding the old
    flat cap of 4 this test used to pin)."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "r1"},
            {"next": "desert", "reason": "still adding"},
            {"next": "alx", "reason": "still adding more"},
        ],
        stream_scripts=[[alx_sentence], [desert_sentence], [alx_sentence], [desert_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)

    result = http.post(f"/api/session/{session_id}/message", json={"text": "what do each of you think of fasting?"}, headers=auth).json()
    for _ in range(4):
        assert result["round_open"]
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    # The fifth voice turn is the cap: closed in the same response, with
    # the voice turn still delivered.
    assert result["position"] == 5 and result["voice"] is not None
    assert not result["round_open"] and result["turn_no"] == 1


def test_round_cap_closes_at_six_for_three_seats(
    store, usage_store, world_loader, registry, alx_world, desert_world, pahc_world
):
    """Mark's ruling, 2026-09-05: 'for 3 voices the cap is 6'
    (RoundConfig.cap_for(3) == 6). At three seats there is never a forced
    move (two voices are always eligible, excluding only the last
    speaker), so all six turns are real selector picks; the floor (3,
    unconditional, unchanged) makes close legal from position 4's decision
    onward, but this round's own selector keeps finding something worth
    adding until the cap forces it closed at position 6."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    pahc_sentence, _ = grounded_sentence(pahc_world)
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "opening"},
            {"next": "desert", "reason": "unheard voice"},
            {"next": "pahc", "reason": "last unheard voice"},
            {"next": "alx", "reason": "still adding - a real second-pass reply"},
            {"next": "desert", "reason": "still adding"},
            {"next": "pahc", "reason": "still adding"},
        ],
        stream_scripts=[
            [alx_sentence], [desert_sentence], [pahc_sentence], [alx_sentence], [desert_sentence], [pahc_sentence],
        ],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert", "pahc"))

    result = http.post(
        f"/api/session/{session_id}/message", json={"text": "who is Jesus, and how did you understand Him?"}, headers=auth
    ).json()
    assert result["position"] == 1 and result["voice"]["speaker"] == "alx"
    assert "close" not in client.messages.selector_enums_seen[0]  # below the floor

    for expected_position in (2, 3):
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
        assert result["position"] == expected_position and result["round_open"]

    # Position 4's decision is the first point "close" is legal (floor met),
    # but this round's own script keeps choosing a real voice instead.
    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["position"] == 4 and result["round_open"]
    assert "close" in client.messages.selector_enums_seen[-1]

    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["position"] == 5 and result["round_open"] and result["turn_no"] is None

    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    # The sixth voice turn is the cap: closed in the same response.
    assert result["position"] == 6 and result["voice"] is not None
    assert not result["round_open"] and result["turn_no"] == 1

    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()
    speakers = [t["speaker"] for t in transcript["transcript"]]
    assert speakers == ["facilitator", "participant", "alx", "desert", "pahc", "alx", "desert", "pahc"]


def test_message_while_round_open_is_409(store, usage_store, world_loader, registry, alx_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[alx_sentence]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    assert http.post(f"/api/session/{session_id}/message", json={"text": "hi"}, headers=auth).json()["round_open"]
    resp = http.post(f"/api/session/{session_id}/message", json={"text": "another"}, headers=auth)
    assert resp.status_code == 409


def test_continue_on_interview_session_is_409(store, usage_store, world_loader, registry):
    client = _table_client(selector_script=[], stream_scripts=[])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    resp = http.post("/api/session", json={"world_key": "fix"})
    session_id = resp.json()["session_id"]
    auth = {"Authorization": f"Session {resp.json()['session_code']}"}
    assert http.post(f"/api/session/{session_id}/continue", headers=auth).status_code == 409


def test_governed_round_acute_crisis(store, usage_store, world_loader, registry, alx_world, desert_world):
    client = _table_client(
        selector_script=[], stream_scripts=[],
        safety=safety_response("ACUTE_DISTRESS", acute_level="a1", risk_subject="self"),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    result = http.post(f"/api/session/{session_id}/message", json={"text": "..."}, headers=auth).json()
    assert not result["round_open"] and result["voice"] is None and result["turn_no"] == 1
    event = result["facilitator"][0]
    assert event["resources_appended"]
    names = f"{alx_world.frame['representative']['name']} or {desert_world.frame['representative']['name']}"
    assert names in event["text"]
    # A governed round still commits - the next message opens round 2.
    assert http.post(f"/api/session/{session_id}/continue", headers=auth).status_code == 409


def test_selector_fallback_degrades_not_fails(store, usage_store, world_loader, registry, alx_world, desert_world):
    desert_sentence, _ = grounded_sentence(desert_world)
    alx_sentence, _ = grounded_sentence(alx_world)
    # Three seats so position 2 is a genuine choice (two eligible voices) -
    # the scripted selector insists on alx twice (illegal self-repeat) and
    # the fallback speaks desert with degraded=true rather than failing.
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "r1"},
            {"next": "alx", "reason": "again"},
            {"next": "alx", "reason": "insisting"},
        ],
        stream_scripts=[[alx_sentence], [desert_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert", "pahc"))
    http.post(f"/api/session/{session_id}/message", json={"text": "hi"}, headers=auth)
    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["voice"]["speaker"] == "desert"
    assert result["turn_selected"]["degraded"] is True
    assert "fallback" in result["turn_selected"]["reason"]


def test_session_cap_at_table_unit(store, usage_store, world_loader, registry, monkeypatch, alx_world, desert_world):
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", 1)
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "r1"},
            {"next": "close", "reason": "done"},
        ],
        stream_scripts=[[alx_sentence], [desert_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    result = http.post(f"/api/session/{session_id}/message", json={"text": "one"}, headers=auth).json()
    while result["round_open"]:
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    capped = http.post(f"/api/session/{session_id}/message", json={"text": "two"}, headers=auth).json()
    assert capped["session_closed"] and not capped["round_open"] and capped["voice"] is None
    assert capped["facilitator"][0]["kind"] == "close"
    # The session is closed for good.
    assert http.post(f"/api/session/{session_id}/message", json={"text": "three"}, headers=auth).status_code == 409


def test_direct_address_routes_without_selector(store, usage_store, world_loader, registry, alx_world, desert_world):
    """FG SS8 end to end: naming Papnoute routes desert at position 1 with
    no selector call at all (an empty selector script proves it - any call
    would pop-from-empty and fail)."""
    desert_sentence, _ = grounded_sentence(desert_world)
    papnoute = desert_world.frame["representative"]["name"]
    client = _table_client(selector_script=[], stream_scripts=[[desert_sentence]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{papnoute}, what do you do with a restless mind?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "desert"
    assert "direct address" in result["turn_selected"]["reason"]
    assert client.messages.selector_enums_seen == []
    # And no turn_selector usage record exists - the routing cost nothing.
    assert all(r.call_kind != "turn_selector" for r in usage_store.read_for_session(session_id))


def test_round_closed_carries_governance_summary(store, usage_store, world_loader, registry, alx_world, desert_world):
    """Every round_closed event carries the deterministic governance
    summary (C5) - visible here through a full round driven over HTTP,
    read back from the raw store."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "r1"}, {"next": "close", "reason": "done"}],
        stream_scripts=[[alx_sentence], [desert_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    result = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    while result["round_open"]:
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    closed = [e for e in store.read_events(session_id) if e.event_type == "round_closed"]
    assert len(closed) == 1
    governance = closed[0].payload["governance"]
    assert set(governance["word_share"]) == {"alx", "desert"}
    assert governance["turns"] == {"alx": 2, "desert": 1}
    assert isinstance(governance["dominance_signals"], list)


def test_table_voice_payload_matches_interview_shape(store, usage_store, world_loader, registry, alx_world):
    """The three-level transparency program (citation cards with
    participant-readable labels, per-sentence citations, glosses, figure
    bridges - engine/m4/citation_cards.py and the shipped VoiceTurnBody
    UI) consumes the interview's voice payload. A table voice turn must
    hand it the identical shape, so the same rendering carries the same
    apparatus at a table with zero UI changes - Mark's requirement,
    2026-08-28: the transparency program 'will need to be part of the
    conversation' at the Table."""
    from engine.api.tests.conftest import FakeBedrockClient

    alx_sentence, _ = grounded_sentence(alx_world)
    # Interview turn on fix (the existing proven fixture path).
    interview_client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=interview_client)
    resp = http.post("/api/session", json={"world_key": "fix"})
    auth = {"Authorization": f"Session {resp.json()['session_code']}"}
    interview_voice = http.post(
        f"/api/session/{resp.json()['session_id']}/message", json={"text": "who was Jesus?"}, headers=auth
    ).json()["voice"]

    # Table turn on alx.
    table_client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[alx_sentence]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=table_client)
    session_id, auth = _create_table(http)
    table_voice = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()["voice"]

    assert set(interview_voice) <= set(table_voice), (
        f"table voice payload missing interview keys: {set(interview_voice) - set(table_voice)}"
    )
    # And the cards resolve: every citation carries the resolved sources
    # list the transparency UI's level three reads.
    assert table_voice["citations"], "the table turn should carry a surviving citation"
    assert all("sources" in c for c in table_voice["citations"])


def test_usage_records_carry_world_attribution(store, usage_store, world_loader, registry, alx_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[alx_sentence]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    http.post(f"/api/session/{session_id}/message", json={"text": "hi"}, headers=auth)
    records = usage_store.read_for_session(session_id)
    by_kind = {}
    for r in records:
        by_kind.setdefault(r.call_kind, []).append(r)
    # Gate calls belong to no single world; selector and voice belong to alx.
    assert {r.world_key for r in by_kind["safety_call"]} == {None}
    assert {r.world_key for r in by_kind["reader_call"]} == {None}
    assert {r.world_key for r in by_kind["turn_selector"]} == {"alx"}
    assert {r.world_key for r in by_kind["voice_generation"]} == {"alx"}
