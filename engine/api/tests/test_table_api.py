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
from engine.m4.round import TABLE_SESSION_ROUND_CAP
from engine.m4.turn import R26_HONEST_LIMIT_SENTENCE

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


def _http(*, store, usage_store, world_loader, registry, client, **extra):
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", **extra,
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


@pytest.fixture
def ijc_world(world_loader, registry):
    return _load_world(world_loader, registry, "ijc")


@pytest.fixture
def don_world(world_loader, registry):
    return _load_world(world_loader, registry, "don")


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


def test_table_session_round_cap_is_surfaced_from_the_root(store, usage_store, world_loader, registry, alx_world, desert_world):
    """Stage 0c (Build-Plan.md): the frontend used to hardcode a literal
    round count in participant-facing copy. Both the session-create
    response and the transcript now carry the real
    engine.m4.round.TABLE_SESSION_ROUND_CAP value instead."""
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
                 client=_table_client(selector_script=[], stream_scripts=[]))
    resp = http.post("/api/session", json={"world_keys": ["alx", "desert"]})
    assert resp.json()["round_cap"] == TABLE_SESSION_ROUND_CAP
    session_id, auth = _create_table(http)
    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()
    assert transcript["round_cap"] == TABLE_SESSION_ROUND_CAP


def test_create_table_session_bad_shapes(store, usage_store, world_loader, registry):
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
                 client=_table_client(selector_script=[], stream_scripts=[]))
    assert http.post("/api/session", json={"world_keys": ["alx"]}).status_code == 400
    assert http.post("/api/session", json={"world_keys": ["alx", "desert", "pahc", "syr"]}).status_code == 400
    assert http.post("/api/session", json={"world_keys": ["alx", "alx"]}).status_code == 400
    assert http.post("/api/session", json={"world_key": "alx", "world_keys": ["alx", "desert"]}).status_code == 400
    assert http.post("/api/session", json={"world_keys": ["alx", "nope"]}).status_code == 400


def test_create_table_session_rejects_bad_seat_count_directly(store, world_loader, registry):
    """The HTTP layer's own 2-3-distinct-
    seats check (engine.api.app) isn't the only caller -
    engine.m4.live_table_run and engine.m4.live_table_battery call
    create_table_session directly with an unvalidated --worlds split, and
    used to fail only well into a real, billed round (a single key spent
    turn 1 before crashing at position 2; a fourth key ran with a seat
    that could never speak). The invariant now lives at the function
    itself, not only the one caller that happened to validate first."""
    from engine.api.table_wiring import create_table_session

    with pytest.raises(ValueError):
        create_table_session(store=store, world_loader=world_loader, registry=registry, world_keys=["alx"])
    with pytest.raises(ValueError):
        create_table_session(store=store, world_loader=world_loader, registry=registry, world_keys=["alx", "alx"])
    with pytest.raises(ValueError):
        create_table_session(
            store=store, world_loader=world_loader, registry=registry, world_keys=["alx", "desert", "pahc", "syr"]
        )


def test_selector_presentation_order_is_shuffled_not_the_session_seating(
    monkeypatch, store, usage_store, world_loader, registry, alx_world, desert_world, pahc_world
):
    """Presentation order is freshly shuffled per selector call.
    The session's own canonical seating (state.world_keys - what worlds,
    labels, and direct-address detection all read) is untouched; only the
    COPY shown to the turn selector each call is freshly shuffled, so a
    genuinely open question doesn't quietly always open with whichever
    voice happens to be listed first."""
    import engine.api.table_wiring as table_wiring_module

    monkeypatch.setattr(table_wiring_module.random, "shuffle", lambda seq: seq.reverse())

    pahc_sentence, _ = grounded_sentence(pahc_world)
    client = _table_client(
        selector_script=[{"next": "pahc", "reason": "reversed presentation puts the last-seated voice first"}],
        stream_scripts=[[pahc_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert", "pahc"))

    http.post(f"/api/session/{session_id}/message", json={"text": "who is Jesus?"}, headers=auth)

    # The enum the selector actually saw is the reverse of session seating
    # order (alx, desert, pahc) - proof the presentation order really is a
    # freshly shuffled copy, not the canonical order passed straight through.
    assert client.messages.selector_enums_seen[0] == ["pahc", "desert", "alx"]
    # The session's own canonical seating is untouched by the shuffle.
    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()
    assert transcript["world_keys"] == ["alx", "desert", "pahc"]


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

    # The real selector's own stated reason for closing used to
    # be discarded entirely - round_closed.reason is only the fixed ENUM
    # category ("selector_closed"), never the model's actual free-text
    # justification. It's logged now, in the raw event.
    closed_events = [e for e in store.read_events(session_id) if e.event_type == "round_closed"]
    assert closed_events[0].payload["selector_reason"] == "genuinely answered"


def test_round_close_reasons_endpoint_surfaces_selector_reason(store, usage_store, world_loader, registry, alx_world, desert_world):
    """The diagnostic endpoint built for the same question above: readable
    over HTTP, gated the same way the transcript endpoint is, without a
    direct read against the store."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "most directly positioned"},
            {"next": "close", "reason": "genuinely answered"},
        ],
        stream_scripts=[[alx_sentence], [desert_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)

    # No round closed yet: an empty list, not an error.
    assert http.get(f"/api/session/{session_id}/round-close-reasons", headers=auth).json()["rounds"] == []

    http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)  # the closing turn

    body = http.get(f"/api/session/{session_id}/round-close-reasons", headers=auth).json()
    assert body["session_id"] == session_id
    assert len(body["rounds"]) == 1
    closed = body["rounds"][0]
    assert closed["round_no"] == 1
    assert closed["reason"] == "selector_closed"
    assert closed["turns"] == 3
    assert closed["selector_reason"] == "genuinely answered"

    # Gated exactly like the transcript endpoint: no code, wrong code, both 401.
    assert http.get(f"/api/session/{session_id}/round-close-reasons").status_code == 401
    assert http.get(
        f"/api/session/{session_id}/round-close-reasons", headers={"Authorization": "Session wrong-code"}
    ).status_code == 401


def test_round_cap_closes_at_five_for_two_seats(store, usage_store, world_loader, registry, alx_world, desert_world):
    """For 2 voices and a participant, the max
    turns is 5 (RoundConfig.cap_for(2) == 5, replacing the old
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
    """For 3 voices the cap is 6
    (RoundConfig.cap_for(3) == 6). At three seats there is never a forced
    move (two voices are always eligible, excluding only the last
    speaker), so all six turns are real selector picks; the 3-seat floor
    (5 - raised on live evidence that the
    engagement-scoping fix genuinely worked but round length was an
    independent problem it didn't touch) makes close legal only from
    position 6's decision onward - the same decision the cap forces
    closed regardless, so 5 or 6 is now this table's only possible close
    point. This round's own selector keeps finding something worth adding
    at every decision until the cap forces it closed at position 6."""
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

    for expected_position in (2, 3, 4, 5):
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
        assert result["position"] == expected_position and result["round_open"]
        # Below the 3-seat floor (5) - close is not yet offered, including
        # at position 5's own decision (round_turns=4 < floor_for(3)=5).
        assert "close" not in client.messages.selector_enums_seen[-1]

    # Position 6's decision is the first point "close" is legal (floor
    # met) - but it is also the cap position, so the turn happens and the
    # round closes in the same response regardless of what the selector
    # would have chosen.
    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert "close" in client.messages.selector_enums_seen[-1]
    assert result["position"] == 6 and result["voice"] is not None
    assert not result["round_open"] and result["turn_no"] == 1

    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()
    speakers = [t["speaker"] for t in transcript["transcript"]]
    assert speakers == ["facilitator", "participant", "alx", "desert", "pahc", "alx", "desert", "pahc"]


def test_second_pass_turn_only_sees_its_engaged_voice_not_every_prior_answer(
    store, usage_store, world_loader, registry, alx_world, desert_world, pahc_world
):
    """The finding that actually mattered:
    naming one voice in the directive is not structural scoping if the
    turn's own context still hands it every other voice's full answer
    regardless of what one sentence asks it not to do with it. alx's
    first return (position 4) gets no explicit `engages` from the
    selector script, so _resolve_engages falls back to round_speakers[-1]
    = pahc - desert's own first-pass answer must be genuinely absent from
    what alx is shown this turn, not merely unaddressed in the
    instructions."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    pahc_sentence, _ = grounded_sentence(pahc_world)
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "opening"},
            {"next": "desert", "reason": "unheard voice"},
            {"next": "pahc", "reason": "last unheard voice"},
            {"next": "alx", "reason": "still adding - a real second-pass reply"},
        ],
        stream_scripts=[[alx_sentence], [desert_sentence], [pahc_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert", "pahc"))

    http.post(f"/api/session/{session_id}/message", json={"text": "who is Jesus?"}, headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)
    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["position"] == 4 and result["voice"]["speaker"] == "alx"

    fourth_call = client.messages.stream_calls[-1]
    rendered_system = str(fourth_call["system"]) + str(fourth_call["messages"][-1]["content"])
    rendered_messages = str(fourth_call["messages"])
    # The directive names pahc specifically - the resolved engagement target.
    assert pahc_world.frame["representative"]["name"] in rendered_system
    # desert's own first-pass answer is genuinely gone from this turn's
    # context, not merely unaddressed in the instructions; pahc's stays -
    # its own words, not the citation tag (cross-voice replay strips an
    # unverifiable tag; the point here is the ATTRIBUTION, not the mark).
    assert desert_sentence.split(" [[")[0] not in rendered_messages
    assert pahc_sentence.split(" [[")[0] in rendered_messages


def test_a_first_time_speaker_landing_on_the_cap_turn_gets_the_final_turn_framing(
    store, usage_store, world_loader, registry, alx_world, desert_world, pahc_world
):
    """The exact scenario a live
    probe demonstrated as broken: at 3 seats, alx/desert alternate through
    positions 1-5 (both legal - no immediate self-repeat only excludes the
    LAST speaker, not every prior one) and pahc speaks for the first time
    only at position 6, the cap. pahc's is_second_pass is False, but it is
    unambiguously the round's actual final turn - it must get the settle/
    hand-to-the-participant framing despite never having spoken before,
    never the ordinary "leave room for the other voices; you can always be
    drawn back in" (which would be a real promise this turn cannot keep)."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    pahc_sentence, _ = grounded_sentence(pahc_world)
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "opening"},
            {"next": "desert", "reason": "responding"},
            {"next": "alx", "reason": "still adding"},
            {"next": "desert", "reason": "still adding"},
            {"next": "alx", "reason": "still adding"},
            {"next": "pahc", "reason": "pahc's first word, and the table's last"},
        ],
        stream_scripts=[
            [alx_sentence], [desert_sentence], [alx_sentence], [desert_sentence], [alx_sentence], [pahc_sentence],
        ],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert", "pahc"))

    result = http.post(f"/api/session/{session_id}/message", json={"text": "hi"}, headers=auth).json()
    for _ in range(5):
        assert result["round_open"]
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["position"] == 6 and result["voice"]["speaker"] == "pahc"
    assert not result["round_open"] and result["turn_no"] == 1

    final_call = client.messages.stream_calls[-1]
    rendered = str(final_call["system"]) + str(final_call["messages"][-1]["content"])
    assert "last turn before the participant speaks again" in rendered
    assert "leave the floor open for the participant" in rendered
    # A pre-existing vacuous assertion here
    # checked for a substring with a semicolon the code never produces.
    # "drawn back in every time" is the non-final ending's own phrase -
    # genuinely absent from a final turn.
    assert "drawn back in every time" not in rendered
    # still a real, full first answer for pahc - point 6 holds even on the
    # round's last turn.
    assert "Answer the participant first" in rendered


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
    # The close-for-good at the cap is the module-off contract; with the module on, a limit pauses.
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client, deeper=None)
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


def test_cap_closed_round_governance_includes_the_cap_turn_itself(
    store, usage_store, world_loader, registry, alx_world, desert_world
):
    """PRE-EXISTING BUG (not introduced by this session's round-length
    work). A cap-forced close built its governance_summary from the `state`
    projected at the TOP of _advance_open_round, before the cap-triggering
    voice_turn was written - the round_closed payload's own `turns` count
    and its `governance` block silently disagreed by exactly one turn on
    every cap-forced close, undercounting whichever voice closes it."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[
            {"next": "alx", "reason": "r1"}, {"next": "desert", "reason": "still adding"}, {"next": "alx", "reason": "still adding more"},
        ],
        stream_scripts=[[alx_sentence], [desert_sentence], [alx_sentence], [desert_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    result = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    while result["round_open"]:
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["turn_no"] == 1  # this round closed via the cap, not the selector

    closed = [e for e in store.read_events(session_id) if e.event_type == "round_closed"]
    governance = closed[0].payload["governance"]
    # 5 voice turns total (the cap for 2 seats): alx at 1/3/5, desert at 2/4.
    assert closed[0].payload["turns"] == 5
    assert governance["turns"] == {"alx": 3, "desert": 2}
    assert sum(governance["turns"].values()) == 5


def test_table_voice_payload_matches_interview_shape(store, usage_store, world_loader, registry, alx_world):
    """The three-level transparency program (citation cards with
    participant-readable labels, per-sentence citations, glosses, figure
    bridges - engine/m4/citation_cards.py and the shipped VoiceTurnBody
    UI) consumes the interview's voice payload. A table voice turn must
    hand it the identical shape, so the same rendering carries the same
    apparatus at a table with zero UI changes - the transparency program
    needs to be part of the conversation at the Table too."""
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


# --- seat-identity guard ---


def test_seat_identity_guard_regenerates_once_then_ships_the_clean_retry(store, usage_store, world_loader, registry, alx_world, desert_world):
    clean_sentence, rid = grounded_sentence(alx_world)
    violating = "The Facilitator: I will speak for both of us now."
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "opening"}],
        stream_scripts=[[violating], [clean_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))

    result = http.post(f"/api/session/{session_id}/message", json={"text": "who is jesus"}, headers=auth).json()
    assert result["voice"]["speaker"] == "alx"
    # The clean regenerated text ships, not the caught first attempt.
    assert "Facilitator" not in result["voice"]["text"]
    assert rid in [c["record_ids"][0] for c in result["voice"]["citations"]]

    violations = [e for e in store.read_events(session_id) if e.event_type == "seat_identity_violation"]
    assert len(violations) == 1
    assert violations[0].payload["attempt"] == "first"
    assert violations[0].payload["offending_prefix"] == "The Facilitator:"
    assert violations[0].payload["world_key"] == "alx"
    assert violations[0].payload["round_no"] == 1 and violations[0].payload["position"] == 1

    # Two real stream calls were made for this one turn - the guard's one
    # regeneration actually happened, not silently skipped.
    assert len(client.messages.stream_calls) == 2

    # No facilitator fallback fired - the retry succeeded.
    assert not any(f["kind"] == "seat_correction" for f in result["facilitator"])


def test_seat_identity_guard_exhausted_hands_the_turn_to_the_facilitator(store, usage_store, world_loader, registry, alx_world, desert_world):
    desert_label = f"{desert_world.frame['representative']['name']} ({desert_world.frame['display_name']})"
    violating_1 = "The Facilitator: I will speak for both of us now."
    violating_2 = f"{desert_label}: I agree with what was just said."
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "opening"}],
        stream_scripts=[[violating_1], [violating_2]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))

    result = http.post(f"/api/session/{session_id}/message", json={"text": "who is jesus"}, headers=auth).json()
    assert result["voice"]["speaker"] == "alx"
    # The voice's text is not shown.
    assert result["voice"]["text"] == ""
    # The round still advanced (position/turn bookkeeping intact) rather than stalling.
    assert result["position"] == 1 and result["round_open"]

    fallback = [f for f in result["facilitator"] if f["kind"] == "seat_correction"]
    assert len(fallback) == 1
    assert alx_world.frame["representative"]["name"] in fallback[0]["text"]

    violations = [e for e in store.read_events(session_id) if e.event_type == "seat_identity_violation"]
    assert [v.payload["attempt"] for v in violations] == ["first", "regenerated"]
    assert [v.payload["offending_prefix"] for v in violations] == ["The Facilitator:", f"{desert_label}:"]

    stored_facilitator_events = [
        e for e in store.read_events(session_id) if e.event_type == "facilitator_turn" and e.payload["kind"] == "seat_correction"
    ]
    assert len(stored_facilitator_events) == 1

    # Round bookkeeping stayed intact: alx counts as having spoken this
    # round (the voice_turn event was still written, empty text and all),
    # which is what keeps the next selection from immediately re-picking
    # the same seat that just failed (turn_selector's own no-immediate-
    # self-repeat rule, engine.m4.turn_selector.eligible_worlds).
    projected = [e for e in store.read_events(session_id) if e.event_type == "voice_turn"]
    assert len(projected) == 1 and projected[0].payload["speaker"] == "alx"


# --- other-tradition parity with interview ---
# table_wiring.py never threaded is_other_tradition_first_ask into a
# selected seat's own directive, so the honest-limit/evidence directive
# and self-revision never fired at the Table even when the gate
# classified a message other_tradition - a seated voice answering about
# an absent tradition got only the seat-to-seat clause. These pin the fix
# directly against a real, currently-classified-other_tradition round.


def _other_tradition_directive_text(client, call_index=0):
    system = client.messages.stream_calls[call_index]["system"]
    return "".join(block["text"] for block in system[2:])


def test_a_table_turn_classified_other_tradition_gets_the_directive(store, usage_store, world_loader, registry, alx_world, desert_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    theon = alx_world.frame["representative"]["name"]
    client = _table_client(
        selector_script=[],
        # Two scripts: alx_sentence carries a tag, so self-revision fires
        # on this other_tradition turn too - the draft is call 0
        # regardless, which is all this test checks.
        stream_scripts=[[alx_sentence], ["(revision, no change needed)"]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{theon}, what did you make of the Donatists?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "alx"
    directive_text = _other_tradition_directive_text(client)
    assert "another Christian tradition" in directive_text


def test_a_seat_whose_own_records_mention_the_named_tradition_gets_the_records_branch(
    store, usage_store, world_loader, registry, ijc_world, desert_world
):
    # ijc's own real records (ijc.quote.compelled-to-come-in, ijc.story.
    # emperor-builds-another-basilica) genuinely name Donatism - the same
    # real pair #440's own interview-level fix used.
    ijc_sentence, _ = grounded_sentence(ijc_world)
    john = ijc_world.frame["representative"]["name"]
    client = _table_client(
        selector_script=[],
        # Second script: the tagged draft also triggers self-revision on
        # this other_tradition turn - see the "gets the directive" test's
        # own note. The draft (call 0) is what this test checks.
        stream_scripts=[[ijc_sentence], ["(revision, no change needed)"]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("ijc", "desert"))
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{john}, what did you make of the Donatists?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "ijc"
    directive_text = _other_tradition_directive_text(client)
    assert "your own records already speak to it" in directive_text
    assert "[[ijc.quote.compelled-to-come-in]]" in directive_text
    assert R26_HONEST_LIMIT_SENTENCE not in directive_text


def test_a_seat_whose_own_records_do_not_mention_it_gets_the_fixed_sentence(store, usage_store, world_loader, registry, alx_world, desert_world):
    # alx's own real records never mention Donatism - the honest-limit
    # branch.
    alx_sentence, _ = grounded_sentence(alx_world)
    theon = alx_world.frame["representative"]["name"]
    client = _table_client(
        selector_script=[],
        # Second script: same self-revision note as the sibling tests above.
        stream_scripts=[[alx_sentence], ["(revision, no change needed)"]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{theon}, what did you make of the Donatists?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "alx"
    directive_text = _other_tradition_directive_text(client)
    assert R26_HONEST_LIMIT_SENTENCE in directive_text


def test_self_revision_runs_on_an_other_tradition_table_turn_and_not_on_an_ordinary_one(
    store, usage_store, world_loader, registry, ijc_world, desert_world
):
    ijc_sentence, ijc_rid = grounded_sentence(ijc_world)
    john = ijc_world.frame["representative"]["name"]
    revised = " ".join(ijc_sentence.split(" [[")[0].split()[:6]) + f" [[{ijc_rid}]]."
    client = _table_client(
        selector_script=[],
        stream_scripts=[[ijc_sentence], [revised]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("ijc", "desert"))
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{john}, what did you make of the Donatists?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "ijc"
    # Two stream calls: the draft, then the self-revision pass - the exact
    # same shape engine/m4/tests/test_turn.py already pins at the unit
    # level, now proven wired at the Table too.
    assert len(client.messages.stream_calls) == 2
    assert result["voice"]["text"] == " ".join(ijc_sentence.split(" [[")[0].split()[:6]) + "."


def test_self_revision_does_not_run_on_an_ordinary_table_turn(store, usage_store, world_loader, registry, alx_world, desert_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    client = _table_client(selector_script=[], stream_scripts=[[alx_sentence]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    theon = alx_world.frame["representative"]["name"]
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{theon}, who was Jesus?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "alx"
    assert len(client.messages.stream_calls) == 1


def test_seat_to_seat_engagement_clause_is_unchanged_by_the_other_tradition_directive(
    store, usage_store, world_loader, registry, alx_world, ijc_world
):
    # Two turns, same round (one gate classification governs the whole
    # round, exactly as engine.api.table_wiring._continue_table_round_
    # unlocked re-reads the round's own opening out_of_scope_class rather
    # than re-classifying per turn): alx opens, ijc returns second and
    # gets BOTH directive parts in the same system block - the Table's own
    # seat-to-seat clause never suppressed by, and never suppressing, the
    # other_tradition directive _build_turn_directive composes them into.
    alx_sentence, _ = grounded_sentence(alx_world)
    ijc_sentence, _ = grounded_sentence(ijc_world)
    client = _table_client(
        selector_script=[{"next": "ijc", "reason": "r1"}],
        # Both drafts carry a tag on an other_tradition round, so each
        # turn's own self-revision pass consumes a script too: call 0 =
        # alx draft, call 1 = alx self-revision, call 2 = ijc draft (what
        # this test checks), call 3 = ijc self-revision.
        stream_scripts=[
            [alx_sentence], ["(revision, no change needed)"],
            [ijc_sentence], ["(revision, no change needed)"],
        ],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "ijc"))
    theon = alx_world.frame["representative"]["name"]
    http.post(f"/api/session/{session_id}/message", json={"text": f"{theon}, what did you make of the Donatists?"}, headers=auth).json()
    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["voice"]["speaker"] == "ijc"
    directive_text = _other_tradition_directive_text(client, call_index=2)
    assert "You are being brought into a Table round, not answering alone" in directive_text
    assert "your own records already speak to it" in directive_text


# --- other-tradition directive fixes, second pass ---


def test_a_seat_drawn_back_in_the_same_round_does_not_repeat_the_fixed_sentence(
    store, usage_store, world_loader, registry, alx_world, desert_world
):
    # turn_selector may draw a seat back into the same round (its own
    # no-immediate-self-repeat rule only blocks the VERY NEXT pick, not
    # a later one) - alx speaks turn 1, desert turn 2, alx turn 3. The
    # fixed honest-limit sentence is true and said once; repeating it
    # verbatim on the return turn is not what interview's own single-ask
    # shape ever produces.
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    theon = alx_world.frame["representative"]["name"]
    client = _table_client(
        selector_script=[{"next": "desert", "reason": "r1"}, {"next": "alx", "reason": "r2"}],
        stream_scripts=[
            [alx_sentence], ["(revision, no change needed)"],
            [desert_sentence], ["(revision, no change needed)"],
            [alx_sentence], ["(revision, no change needed)"],
        ],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    http.post(f"/api/session/{session_id}/message", json={"text": f"{theon}, what did you make of the Donatists?"}, headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)  # desert's turn
    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()  # alx, again
    assert result["voice"]["speaker"] == "alx"
    first_turn_directive = _other_tradition_directive_text(client, call_index=0)
    second_turn_directive = _other_tradition_directive_text(client, call_index=4)
    assert R26_HONEST_LIMIT_SENTENCE in first_turn_directive
    assert R26_HONEST_LIMIT_SENTENCE not in second_turn_directive
    assert "Answer only from what your own world's records actually hold about it" in second_turn_directive


def test_a_seated_tradition_with_no_evidence_gets_its_own_directive_not_silence(
    store, usage_store, world_loader, registry, alx_world, don_world
):
    # don is the OTHER seat at this table - the fixed sentence would be
    # false (that tradition's own Representative sits right there), and
    # alx's own records never mention Donatism, so there is no evidence
    # branch either. This is the round's opening turn (the very message
    # naming don), and table_engagement is never built on an opening turn
    # (only when other_voice_has_spoken), so the Table's own seat-to-seat
    # clause does not govern here either. A real seated-tradition
    # directive fires instead, naming don's own card_name and limiting
    # this seat to what that chair has actually said - never the fixed
    # honest-limit sentence, which would be false.
    alx_sentence, _ = grounded_sentence(alx_world)
    theon = alx_world.frame["representative"]["name"]
    don_card_name = registry["don"]["card_name"]
    client = _table_client(
        selector_script=[],
        stream_scripts=[[alx_sentence], ["(revision, no change needed)"]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "don"))
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{theon}, what was your relationship with {don_card_name}?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "alx"
    directive_text = _other_tradition_directive_text(client)
    assert R26_HONEST_LIMIT_SENTENCE not in directive_text
    assert don_card_name in directive_text
    assert "seated at this table" in directive_text
    assert "Never speak for that tradition" in directive_text
    assert "what that chair has actually said in this conversation" in directive_text


def test_a_seated_tradition_with_evidence_still_gets_the_records_branch(
    store, usage_store, world_loader, registry, ijc_world, don_world
):
    # don is seated AND ijc's own records genuinely mention it (#440's
    # own fix) - the evidence branch still applies; being seated only
    # ever suppresses the FIXED sentence, never the evidence branch.
    ijc_sentence, _ = grounded_sentence(ijc_world)
    john = ijc_world.frame["representative"]["name"]
    don_card_name = registry["don"]["card_name"]
    client = _table_client(
        selector_script=[],
        stream_scripts=[[ijc_sentence], ["(revision, no change needed)"]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("ijc", "don"))
    result = http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{john}, what was your relationship with {don_card_name}?"}, headers=auth,
    ).json()
    assert result["voice"]["speaker"] == "ijc"
    directive_text = _other_tradition_directive_text(client)
    assert "your own records already speak to it" in directive_text
    assert "[[ijc.quote.compelled-to-come-in]]" in directive_text


# --- the pivot's own licence, per seat ---
# Condition (a) from THIS seat's own window against the named tradition's;
# condition (b) from what the Facilitator, the participant, and every
# other seat actually said. The round's own opening question is never
# quoted back.


def test_a_seat_that_could_have_known_the_tradition_is_licensed_under_condition_a(
    store, usage_store, world_loader, registry, alx_world, desert_world
):
    # alx (150-400) on the Donatists (from 311): a worked example of the
    # pivot licensed under condition (a).
    alx_sentence, _ = grounded_sentence(alx_world)
    theon = alx_world.frame["representative"]["name"]
    client = _table_client(
        selector_script=[],
        stream_scripts=[[alx_sentence], ["(revision, no change needed)"]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    http.post(f"/api/session/{session_id}/message", json={"text": f"{theon}, what did you make of the Donatists?"}, headers=auth)
    directive_text = _other_tradition_directive_text(client)
    assert "could have known of that tradition in its own time" in directive_text
    assert "word for word" not in directive_text


def test_a_seat_asked_about_a_later_tradition_is_limited_to_the_question(
    store, usage_store, world_loader, registry, alx_world, desert_world
):
    alx_sentence, _ = grounded_sentence(alx_world)
    theon = alx_world.frame["representative"]["name"]
    client = _table_client(
        selector_script=[],
        stream_scripts=[[alx_sentence], ["(revision, no change needed)"]],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    http.post(
        f"/api/session/{session_id}/message",
        json={"text": f"{theon}, what would you say to {registry['rzg']['card_name']}?"}, headers=auth,
    )
    directive_text = _other_tradition_directive_text(client)
    assert "arose after your own world's time" in directive_text
    assert "using only the question's own words - never outside knowledge" in directive_text


def test_what_another_representative_said_reaches_the_next_seat_r37_b(
    store, usage_store, world_loader, registry, alx_world, desert_world
):
    # Condition (b): alx names the Donatists in its own turn; desert,
    # drawn in second, is given that exact sentence, attributed to alx's
    # own label.
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    theon = alx_world.frame["representative"]["name"]
    alx_turn = alx_sentence
    alx_shown = alx_sentence.split(" [[")[0] + "."
    client = _table_client(
        selector_script=[{"next": "desert", "reason": "r1"}],
        stream_scripts=[
            [alx_turn], [alx_turn],
            [desert_sentence], ["(revision, no change needed)"],
        ],
        reader=reader_response(out_of_scope={"class": "other_tradition"}),
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    http.post(f"/api/session/{session_id}/message", json={"text": f"{theon}, what did you make of the Donatists?"}, headers=auth)
    result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert result["voice"]["speaker"] == "desert"
    directive_text = _other_tradition_directive_text(client, call_index=2)
    assert f': "{alx_shown}"' in directive_text
    assert f"- {theon}" in directive_text
    # The round's own question is still never quoted back.
    assert "what did you make of the Donatists?" not in directive_text


def test_continue_forwards_the_turn_switches(store, usage_store, world_loader, registry, monkeypatch):
    seen = {}

    def fake_continue(**kwargs):
        seen.update(kwargs)
        raise table_wiring.TableRoundNotOpen()

    from engine.api import table_wiring
    monkeypatch.setattr(table_wiring, "continue_table_round", fake_continue)
    client = _table_client(selector_script=[], stream_scripts=[])
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", r27_enforce=True, self_revision_enabled=False, citation_attach_enabled=True,
    )
    http = TestClient(app)
    resp = http.post("/api/session", json={"world_key": "fix"})
    auth = {"Authorization": f"Session {resp.json()['session_code']}"}
    http.post(f"/api/session/{resp.json()['session_id']}/continue", headers=auth)
    assert (seen["r27_enforce"], seen["self_revision_enabled"], seen["citation_attach_enabled"]) == (True, False, True)


def test_table_voice_turns_write_qc_rows_including_continues(tmp_path, store, usage_store, world_loader, registry, alx_world, desert_world):
    from engine.api.qc_recorder import QCRecorder
    from engine.m7.qc_store import QCStore

    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "most directly positioned"}],
        stream_scripts=[[alx_sentence], [desert_sentence]],
    )
    qc = QCStore(tmp_path / "qc.db")
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", qc_recorder=QCRecorder(qc, registry),
    )
    http = TestClient(app)
    session_id, auth = _create_table(http)
    http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)
    rows = qc.rows()
    assert [(r["world"], r["round"]) for r in rows] == [("alx", 1), ("desert", 2)]
    assert len({r["conversation_token"] for r in rows}) == 1
    assert all(r["question_text"] == "what is prayer?" for r in rows)


# --- streamed seats (System Hub decision 38) ---

STREAM = {"Accept": "text/event-stream"}


def _events(response):
    import json
    out = []
    for block in response.text.strip().split("\n\n"):
        name, data = block.split("\n", 1)
        out.append((name.removeprefix("event: "), json.loads(data.removeprefix("data: "))))
    return out


def test_a_streamed_table_seat_sends_its_sentences_then_the_turn(store, usage_store, world_loader, registry, alx_world, desert_world):
    clean_sentence, rid = grounded_sentence(alx_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "opening"}],
        stream_scripts=[[clean_sentence + " ", clean_sentence + " ", clean_sentence + " ", "That is what we hold."]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client,
                 streaming_enabled=True, sentence_enforce=False)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    events = _events(http.post(f"/api/session/{session_id}/message", json={"text": "who is jesus"}, headers={**auth, **STREAM}))
    names = [name for name, _ in events]
    assert names[-1] == "done" and names.count("sentence") == 2
    done = events[-1][1]
    assert done["voice"]["speaker"] == "alx" and done["round_open"]
    shown = "".join(d["lead"] + d["text"] for name, d in events if name == "sentence")
    assert done["voice"]["text"].startswith(shown)


def test_a_seat_caught_mid_reply_ends_at_its_last_shown_sentence_and_the_facilitator_says_so(
    store, usage_store, world_loader, registry, alx_world, desert_world,
):
    clean_sentence, rid = grounded_sentence(alx_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "opening"}],
        stream_scripts=[[clean_sentence + " ", clean_sentence + "\n\n", "The Facilitator: I will speak for both of us now. ", "And more."]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client,
                 streaming_enabled=True, sentence_enforce=False)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    events = _events(http.post(f"/api/session/{session_id}/message", json={"text": "who is jesus"}, headers={**auth, **STREAM}))
    shown = [d["text"] for name, d in events if name == "sentence"]
    assert len(shown) == 2 and not any("Facilitator" in t for t in shown)
    done = events[-1][1]
    assert "Facilitator" not in done["voice"]["text"] and done["voice"]["text"].count(".") == 2
    cut = [f for f in done["facilitator"] if f["kind"] == "seat_correction"]
    assert len(cut) == 1 and "What came before that point stands." in cut[0]["text"]
    assert alx_world.frame["representative"]["name"] in cut[0]["text"]
    assert len(client.messages.stream_calls) == 1
    violations = [e.payload for e in store.read_events(session_id) if e.event_type == "seat_identity_violation"]
    assert [v["attempt"] for v in violations] == ["streamed"] and violations[0]["offending_prefix"] == "The Facilitator:"


def test_a_seat_caught_in_its_first_sentence_shows_nothing_and_regenerates(store, usage_store, world_loader, registry, alx_world, desert_world):
    clean_sentence, rid = grounded_sentence(alx_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "opening"}],
        stream_scripts=[["The Facilitator: I will speak for both of us now. ", "Then more."], [clean_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client,
                 streaming_enabled=True, sentence_enforce=False)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    events = _events(http.post(f"/api/session/{session_id}/message", json={"text": "who is jesus"}, headers={**auth, **STREAM}))
    assert [name for name, _ in events] == ["done"]
    done = events[-1][1]
    assert "Facilitator" not in done["voice"]["text"]
    assert rid in [c["record_ids"][0] for c in done["voice"]["citations"]]
    assert len(client.messages.stream_calls) == 2
    assert not any(f["kind"] == "seat_correction" for f in done["facilitator"])


def test_continue_streams_the_next_seat(store, usage_store, world_loader, registry, alx_world, desert_world):
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "opening"}, {"next": "desert", "reason": "second"}],
        stream_scripts=[[alx_sentence], [desert_sentence + " ", desert_sentence + " ", desert_sentence + " ", "So we held."]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client,
                 streaming_enabled=True, sentence_enforce=False)
    session_id, auth = _create_table(http, world_keys=("alx", "desert"))
    http.post(f"/api/session/{session_id}/message", json={"text": "who is jesus"}, headers=auth)
    events = _events(http.post(f"/api/session/{session_id}/continue", headers={**auth, **STREAM}))
    assert [name for name, _ in events].count("sentence") == 2
    assert events[-1][0] == "done" and events[-1][1]["voice"]["speaker"] == "desert"
