"""SS77 applied to session memory (found and fixed 2026-08-28, the Table
thread): the bridge turn hands the voice the term-free underlying subject,
and until this fix the NEXT turn's history replayed the participant's raw
message - the barred modern word reached the voice one turn late. Both
modes are fixed through one function (engine.api.wiring.replay_transcript),
and both are pinned here.

What "term-free" asserts: the participant's own sentence (their modern
framing) never replays to a voice. The substitute is the fleet record's own
underlying_subject verbatim - authored data that may mention the word
meta-textually ("before the word 'Trinity' existed for them to use"), which
is the record doing exactly its authored job, not a leak."""
import pytest

from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.api.tests.test_table_api import _create_table, _http, _table_client, grounded_sentence
from engine.api.wiring import _load_world
from engine.m1.loader import load_fleet_records

TRINITY_QUESTION = "What is the Trinity?"


@pytest.fixture
def underlying_subject():
    return load_fleet_records()["_fleet.modern.trinity"]["underlying_subject"].strip()


def test_interview_history_replays_underlying_subject(store, usage_store, world_loader, registry, underlying_subject):
    # No reader flag needed: terms_in_message finds "Trinity" against the
    # fleet record's own display_terms, and the term postdates fix's window,
    # so routing bridges (the same path the live 2026-08-24 fix proved).
    client = FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"),
        reader_response=reader_response(),
        stream_chunks=["We remember the Father, the Son, and the Spirit together."],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    resp = http.post("/api/session", json={"world_key": "fix"})
    session_id = resp.json()["session_id"]
    auth = {"Authorization": f"Session {resp.json()['session_code']}"}

    first = http.post(f"/api/session/{session_id}/message", json={"text": TRINITY_QUESTION}, headers=auth).json()
    assert first["routing_action"] == "bridge_turn"
    # The live turn already honored SS77: the voice's call carries the
    # underlying subject, not the participant's sentence.
    first_call = client.messages.stream_calls[0]
    assert TRINITY_QUESTION not in str(first_call["messages"])
    assert underlying_subject in str(first_call["messages"])

    second = http.post(f"/api/session/{session_id}/message", json={"text": "Say more about that."}, headers=auth).json()
    assert second["routing_action"] in ("voice_with_directive", "voice_pass_through")
    # THE FIX: the second turn's replayed history carries what the voice was
    # actually handed on turn one - never the participant's modern framing.
    second_call = client.messages.stream_calls[1]
    history_user_turns = [m["content"] for m in second_call["messages"] if m["role"] == "user"]
    assert all(TRINITY_QUESTION not in content for content in history_user_turns)
    assert any(underlying_subject in content for content in history_user_turns)


def test_table_round_replays_underlying_subject_to_every_voice(store, usage_store, world_loader, registry, underlying_subject):
    # pahc + fix: the one seating where the trinity term is anachronistic
    # for EVERY seated world, so the round bridges (Artifact-7 SS2's
    # intersection rule). fix is the synthetic fixture world - never
    # participant-reachable, exactly what it exists for in tests.
    pahc_world = _load_world(world_loader, registry, "pahc")
    fix_world = _load_world(world_loader, registry, "fix")
    pahc_sentence, _ = grounded_sentence(pahc_world)
    fix_sentence, _ = grounded_sentence(fix_world)
    client = _table_client(
        selector_script=[{"next": "pahc", "reason": "r1"}],  # position 2 is a forced move
        stream_scripts=[[pahc_sentence], [fix_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http, world_keys=("pahc", "fix"))

    first = http.post(f"/api/session/{session_id}/message", json={"text": TRINITY_QUESTION}, headers=auth).json()
    assert first["routing_action"] == "bridge_turn"
    assert first["facilitator"] and first["facilitator"][0]["kind"] == "bridge"
    assert first["voice"]["speaker"] == "pahc"
    second = http.post(f"/api/session/{session_id}/continue", headers=auth).json()
    assert second["voice"]["speaker"] == "fix"

    # Every voice's call this round - the first speaker's context and the
    # second speaker's context (which also replays the round so far) - sees
    # the underlying subject where the participant's sentence was.
    assert len(client.messages.stream_calls) == 2
    for call in client.messages.stream_calls:
        rendered = str(call["messages"])
        assert TRINITY_QUESTION not in rendered
        assert underlying_subject in rendered
