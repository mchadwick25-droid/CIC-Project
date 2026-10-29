from engine.m3.gate_replay import SavedDraftClient
from engine.m4.generation import stream_voice_turn


def test_the_saved_draft_comes_back_as_the_voice_reply():
    client = SavedDraftClient()
    client.draft = "We held it [[w.dw.a]]."
    outcome = stream_voice_turn(client, "model", system_prompt="s", message="m")
    assert outcome.status == "ok"
    assert outcome.value.text == "We held it [[w.dw.a]]."
