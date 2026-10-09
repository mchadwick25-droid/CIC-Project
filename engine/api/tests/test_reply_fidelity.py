"""Sentence enforcement is on for every conversation path: a sentence the
grounding net withholds is rewritten out of the reply once, and a rewrite
still holding one is set aside for the Facilitator's line rather than shown
with sentences cut out of it, in a one-to-one conversation and at the
Table. A clean turn costs no extra call. The safety path is unchanged."""
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


def test_one_to_one_a_withheld_sentence_rewritten_out_ships_the_rewrite(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[f"{CLEAN} {WITHHELD}"], [CLEAN]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 2
    assert result.voice["text"] == CLEAN_SHOWN
    assert result.voice["sentence_enforcement"]["still_flagged"] == []
    assert result.facilitator is None


def test_one_to_one_a_sentence_still_withheld_after_the_rewrite_sets_the_reply_aside(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[f"{CLEAN} {WITHHELD}"], [f"{CLEAN} {WITHHELD}"]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 2
    assert result.voice["text"] == ""
    assert result.voice["sentence_enforcement"]["still_flagged"] == [WITHHELD]
    assert result.facilitator["kind"] == facilitator_turns.VOICE_REJECTED.kind


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
    header = "## Sources\n\n**Cassian, Institutes V.26**\n\n"
    typed = header + 'Athanasius wrote, "a thing found in no record that anyone ever read". ' + CLEAN
    client = _one_to_one_client([[typed], [header + CLEAN]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 2
    assert result.voice["text"] == CLEAN_SHOWN
    repeated = _one_to_one_client([[typed], [typed]])
    result = _send(store, usage_store, world_loader, registry, repeated)
    assert len(repeated.messages.stream_calls) == 2
    assert result.voice["text"] == ""
    assert result.facilitator["kind"] == facilitator_turns.VOICE_REJECTED.kind


def test_one_to_one_a_header_alone_costs_no_extra_call(store, usage_store, world_loader, registry):
    client = _one_to_one_client([["## Sources\n\n**Cassian, Institutes V.26**\n\n" + CLEAN]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["text"] == CLEAN_SHOWN


def test_one_to_one_untagged_attribution_forms_are_regenerated_once_then_set_aside(store, usage_store, world_loader, registry):
    for attributed in (
        "Athanasius says, the elders never saw him with their own eyes.",
        "The elders never saw him with their own eyes \u2014 Saint Athanasius.",
        "Athanasius wrote: the elders never saw him. They only heard.",
        "Athanasius put it this way. The elders never saw him.",
    ):
        reply = f"{CLEAN}\n\n{attributed}"
        client = _one_to_one_client([[reply], [reply]])
        result = _send(store, usage_store, world_loader, registry, client)
        assert len(client.messages.stream_calls) == 2, attributed
        assert result.voice["text"] == "", attributed
        assert result.voice["sentence_enforcement"]["still_flagged"], attributed
        assert result.facilitator["kind"] == facilitator_turns.VOICE_REJECTED.kind, attributed


def test_the_table_a_withheld_sentence_still_there_after_the_rewrite_sets_the_seat_aside(
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
    assert shown not in body["voice"]["text"]
    assert body["voice"]["text"] == ""
    assert body["voice"]["sentence_enforcement"]["still_flagged"] == [WITHHELD]
    assert body["facilitator"][-1]["kind"] == facilitator_turns.TABLE_SEAT_CORRECTION.kind


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
