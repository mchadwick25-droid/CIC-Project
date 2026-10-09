"""Sentence enforcement is on for every conversation path: a sentence the
grounding net withholds is regenerated once and dropped if still withheld,
in a one-to-one conversation and at the Table, and a clean turn costs no
extra call. The safety path is unchanged."""
from engine.api import wiring
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.api.tests.test_table_api import (  # noqa: F401  (fixtures)
    _create_table,
    _http,
    _table_client,
    alx_world,
    desert_world,
    grounded_sentence,
)
from engine.m4 import facilitator_turns

CLEAN = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."
CLEAN_SHOWN = "We did not claim to have seen him ourselves."
WITHHELD = "Athanasius of Alexandria opposed the council."


def _send(store, usage_store, world_loader, registry, client, text="who was Jesus"):
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    return wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        session_id=session_id, text=text, client_msg_id="msg-1",
    )


def _one_to_one_client(scripts):
    return FakeBedrockClient(
        safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response(), stream_scripts=scripts,
    )


def test_one_to_one_a_withheld_sentence_is_regenerated_once_then_dropped(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[f"{CLEAN} {WITHHELD}"], [f"{CLEAN} {WITHHELD}"]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 2
    assert result.voice["text"] == CLEAN_SHOWN
    assert result.voice["sentence_enforcement"]["sentences_dropped"] == [WITHHELD]


def test_one_to_one_a_clean_turn_makes_no_extra_call(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[CLEAN]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["text"] == CLEAN_SHOWN
    assert result.voice["sentence_enforcement"]["regenerated"] is False


def test_one_to_one_a_reply_with_nothing_left_is_set_aside_for_the_facilitators_line(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[WITHHELD], [WITHHELD]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 2
    assert result.voice["text"] == ""
    assert result.facilitator["kind"] == facilitator_turns.VOICE_REJECTED.kind


def test_one_to_one_a_typed_quote_and_a_header_never_reach_the_participant(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[
        '## Sources\n\n**Cassian, Institutes V.26**\n\nAthanasius wrote, "a thing found in no record that anyone ever read". ' + CLEAN
    ]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["text"] == CLEAN_SHOWN


def test_the_table_a_withheld_sentence_is_regenerated_once_then_dropped(
    store, usage_store, world_loader, registry, alx_world, desert_world,
):
    sentence, _rid = grounded_sentence(alx_world)
    shown = sentence.split(" [[")[0] + "."
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "most directly positioned"}],
        stream_scripts=[[f"{sentence} {WITHHELD}"], [f"{sentence} {WITHHELD}"]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    body = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert len(client.messages.stream_calls) == 2
    assert body["voice"]["text"] == shown
    assert body["voice"]["sentence_enforcement"]["sentences_dropped"] == [WITHHELD]


def test_the_table_a_clean_turn_makes_no_extra_call(store, usage_store, world_loader, registry, alx_world, desert_world):
    sentence, _rid = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[sentence]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    body = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert len(client.messages.stream_calls) == 1
    assert body["voice"]["sentence_enforcement"]["regenerated"] is False


def test_the_table_a_seat_with_nothing_left_is_set_aside_for_the_table_correction(
    store, usage_store, world_loader, registry, alx_world, desert_world,
):
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[WITHHELD], [WITHHELD]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    body = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert len(client.messages.stream_calls) == 2
    assert body["voice"]["text"] == ""
    assert body["facilitator"][-1]["kind"] == facilitator_turns.TABLE_SEAT_CORRECTION.kind
