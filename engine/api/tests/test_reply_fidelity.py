"""No conversation path regenerates a reply or sets it aside, one to one or
at the Table: every turn makes one voice call. A quotation the voice typed,
or words it put in a named mouth, is cut with what introduces it. A sentence
the net withholds for another reason is shown without its citation. A reply
cut whole is replaced by the world's own answer record, and no Facilitator
line stands in for it. The safety path is unchanged."""
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


def test_one_to_one_a_withheld_sentence_is_shown_without_its_citation_in_one_call(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[f"{CLEAN} {WITHHELD}"]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["text"] == f"{CLEAN_SHOWN} {WITHHELD}"
    assert result.facilitator is None


def test_one_to_one_a_clean_turn_makes_one_call(store, usage_store, world_loader, registry):
    client = _one_to_one_client([[CLEAN]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["text"] == CLEAN_SHOWN


def test_one_to_one_a_typed_quote_and_a_header_never_reach_the_participant(store, usage_store, world_loader, registry):
    typed = "## Sources\n\n**Cassian, Institutes V.26**\n\n" + 'Athanasius wrote, "a thing found in no record that anyone ever read". ' + CLEAN
    client = _one_to_one_client([[typed]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["text"] == CLEAN_SHOWN
    assert result.facilitator is None


def test_one_to_one_a_header_alone_costs_no_extra_call(store, usage_store, world_loader, registry):
    client = _one_to_one_client([["## Sources\n\n**Cassian, Institutes V.26**\n\n" + CLEAN]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["text"] == CLEAN_SHOWN


def test_one_to_one_untagged_attribution_forms_are_cut_in_one_call(store, usage_store, world_loader, registry):
    for attributed in (
        "Athanasius says, the elders never saw him with their own eyes.",
        "The elders never saw him with their own eyes \u2014 Saint Athanasius.",
        "Athanasius wrote: the elders never saw him. They only heard.",
        "Athanasius put it this way. The elders never saw him.",
    ):
        client = _one_to_one_client([[f"{CLEAN}\n\n{attributed}"]])
        result = _send(store, usage_store, world_loader, registry, client)
        assert len(client.messages.stream_calls) == 1, attributed
        assert result.voice["text"] == CLEAN_SHOWN, attributed
        assert result.facilitator is None, attributed


def test_one_to_one_a_reply_cut_whole_is_the_worlds_answer_record_with_no_facilitator_line(
    store, usage_store, world_loader, registry,
):
    typed = 'Athanasius wrote, "a thing found in no record that anyone ever read" [[fix.witness.who-is-jesus]].'
    client = _one_to_one_client([[typed]])
    result = _send(store, usage_store, world_loader, registry, client)
    assert len(client.messages.stream_calls) == 1
    assert result.voice["answer_record_fallback"] == "fix.witness.who-is-jesus"
    assert result.voice["text"] and "Athanasius" not in result.voice["text"]
    assert result.facilitator is None


def test_the_table_a_withheld_sentence_is_shown_without_its_citation_in_one_call(
    store, usage_store, world_loader, registry, alx_world, desert_world,
):
    sentence, _rid = grounded_sentence(alx_world)
    shown = sentence.split(" [[")[0] + "."
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "most directly positioned"}],
        stream_scripts=[[f"{sentence} {WITHHELD}"]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    body = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert len(client.messages.stream_calls) == 1
    assert body["voice"]["text"] == f"{shown} {WITHHELD}"
    assert all(f["kind"] != facilitator_turns.TABLE_SEAT_CORRECTION.kind for f in body.get("facilitator") or [])


def test_the_table_a_clean_turn_makes_one_call(store, usage_store, world_loader, registry, alx_world, desert_world):
    sentence, _rid = grounded_sentence(alx_world)
    client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[sentence]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    body = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert len(client.messages.stream_calls) == 1
    assert body["voice"]["text"] == sentence.split(" [[")[0] + "."


def test_the_table_a_seat_cut_whole_is_its_worlds_answer_record_with_no_correction_line(
    store, usage_store, world_loader, registry, alx_world, desert_world,
):
    typed = 'Athanasius wrote, "a thing found in no record that anyone ever read".'
    client = _table_client(selector_script=[{"next": "alx", "reason": "r"}], stream_scripts=[[typed]])
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    body = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    assert len(client.messages.stream_calls) == 1
    assert body["voice"]["answer_record_fallback"]
    assert body["voice"]["text"] and "Athanasius" not in body["voice"]["text"]
    assert all(f["kind"] != facilitator_turns.TABLE_SEAT_CORRECTION.kind for f in body.get("facilitator") or [])
