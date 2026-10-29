"""The admission harness answers a sealed probe through the same run_turn call,
with the same inputs, as the conversation path does for a fresh session's
first message, and the participant reads the text the harness grades."""
import pytest

from engine.api import wiring
from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.m3 import generation
from engine.m3.generation import LiveModelAnswerer, LivePathSettings
from engine.m4 import turn as turn_module

_NOT_COMPARED = {"session_id", "voice_client", "safety_client", "on_sentence"}
_DRAFT = ["We hold this [[fix.witness.who-is-jesus]]."]


def _capturing(captured):
    def run(**kwargs):
        captured.update(kwargs)
        return turn_module.run_turn(**kwargs)

    return run


@pytest.mark.parametrize("self_revision", [True, False])
@pytest.mark.parametrize("other_tradition", [False, True])
def test_a_probe_reaches_run_turn_as_a_first_message_does(
    store, usage_store, world_loader, registry, loaded_fix_world, monkeypatch, self_revision, other_tradition
):
    message = "What did the Alexandrian Christianity believe?" if other_tradition else "Who was Jesus, to you and your people?"
    reader = reader_response(out_of_scope={"class": "other_tradition"}) if other_tradition else reader_response()
    client = FakeBedrockClient(safety_response=safety_response(), reader_response=reader, stream_chunks=_DRAFT)
    voice, gate = "voice-model", "gate-model"

    from_wiring: dict = {}
    monkeypatch.setattr(wiring, "run_turn", _capturing(from_wiring))
    session_id, _code = wiring.create_session(store=store, world_loader=world_loader, registry=registry, world_key="fix")
    read = wiring.handle_message(
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        voice_client=client, voice_model_id=voice, safety_client=client, safety_model_id=gate,
        session_id=session_id, text=message, self_revision_enabled=self_revision,
    )

    from_harness: dict = {}
    monkeypatch.setattr(generation, "run_turn", _capturing(from_harness))
    settings = LivePathSettings(
        voice_model_id=voice, safety_model_id=gate, r27_enforce=False, self_revision_enabled=self_revision,
        citation_attach_enabled=False,
    )
    graded = LiveModelAnswerer(world=loaded_fix_world, registry=registry, client=client, settings=settings).answer("C-I", message)

    assert set(from_harness) == set(from_wiring)
    for key in set(from_harness) - _NOT_COMPARED:
        assert from_harness[key] == from_wiring[key], key
    assert from_harness["on_sentence"] is None and from_wiring["on_sentence"] is None
    if other_tradition:
        assert from_wiring["other_tradition_known_in_window"] is not None
    assert graded.text == read.voice["text"]
    assert graded.live_turn.routing_action == read.routing_action
