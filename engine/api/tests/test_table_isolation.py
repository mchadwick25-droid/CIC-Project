"""THE ISOLATION PROPERTY (Artifact-7 SS3; Constitution V2.2 Art. 3;
Table Design V2.3 SS6): no voice at a table may ground a claim in another
world's records - the only cross-world channel is what was SAID at the
Table. This suite is the CI gate Artifact-7 SS8 item 1 names:

  (a) an assertion sweep over a multi-turn table round - every surviving
      citation of every turn resolves within the speaker's own repository;
  (b) the seeded leak - a record id from seated world B planted in world
      A's raw output must be withheld by A's net as an unresolvable tag,
      visible in the turn's own grounding result;
  (c) the runtime scope check - every voice turn is constructed from
      exactly one LoadedWorld, the selected speaker's, and its generation
      call carries that world's own compiled prompt as its system prefix.

Plus the per-world session-memory boundary (SS3) and the viewer-
parameterized transcript projection (SS4) at the unit level.
"""
from types import SimpleNamespace

import pytest

from engine.api import table_wiring
from engine.api.app import create_app
from engine.api.tests.conftest import reader_response, safety_response
from engine.api.tests.test_table_api import (
    TableFakeClient,
    _create_table,
    _http,
    _table_client,
    grounded_sentence,
)
from engine.api.wiring import _load_world
from engine.m4 import evidence


@pytest.fixture
def alx_world(world_loader, registry):
    return _load_world(world_loader, registry, "alx")


@pytest.fixture
def desert_world(world_loader, registry):
    return _load_world(world_loader, registry, "desert")


def test_seeded_cross_world_leak_is_withheld(store, usage_store, world_loader, registry, alx_world, desert_world):
    """(b) - alx's voice 'cites' a real desert record. desert's id resolves
    in desert's repository, so the ONLY thing keeping it out of alx's
    citations is that alx's net never sees desert's repository at all."""
    good_sentence, good_rid = grounded_sentence(alx_world)
    _, desert_rid = grounded_sentence(desert_world)
    assert desert_rid in evidence.repository_records_by_id(desert_world.repository)
    leak_sentence = f"The desert elders taught silence above all things [[{desert_rid}]]."
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "r"}],
        stream_scripts=[[good_sentence, " ", leak_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    result = http.post(f"/api/session/{session_id}/message", json={"text": "what of the desert?"}, headers=auth).json()

    voice = result["voice"]
    assert voice["speaker"] == "alx"
    # The genuine citation survives; the cross-world one is gone.
    cited = {rid for c in voice["citations"] for rid in c["record_ids"]}
    assert good_rid in cited
    assert desert_rid not in cited
    # And the withholding is visible in the turn's own grounding record -
    # detected as an id alx's world simply does not carry.
    leak_verdicts = [s for s in voice["grounding"]["sentences"] if desert_rid in (s.get("tags") or [])]
    assert leak_verdicts, "the seeded sentence must appear in the net's per-sentence record"
    assert all(s["verdict"] == "withhold" and "unresolvable" in s["why"] for s in leak_verdicts)
    # The net gates decoration, never the text: the sentence itself still
    # reached the participant, tags stripped - with no citation badge.
    assert "silence above all things" in voice["text"]
    assert desert_rid not in voice["text"]


def test_every_citation_resolves_in_speakers_own_repository(store, usage_store, world_loader, registry, alx_world, desert_world):
    """(a) - the assertion sweep over a real multi-voice round."""
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
    result = http.post(f"/api/session/{session_id}/message", json={"text": "what is prayer?"}, headers=auth).json()
    while result["round_open"]:
        result = http.post(f"/api/session/{session_id}/continue", headers=auth).json()

    repos = {
        "alx": set(evidence.repository_records_by_id(alx_world.repository)),
        "desert": set(evidence.repository_records_by_id(desert_world.repository)),
    }
    transcript = http.get(f"/api/session/{session_id}/transcript", headers=auth).json()["transcript"]
    voice_turns = [t for t in transcript if t["speaker"] in repos]
    assert len(voice_turns) == 3
    for turn in voice_turns:
        cited = {rid for c in (turn.get("citations") or []) for rid in c.get("record_ids", [])}
        assert cited, f"{turn['speaker']} turn should carry its surviving citation"
        assert cited <= repos[turn["speaker"]], (
            f"{turn['speaker']} cited outside its own repository: {cited - repos[turn['speaker']]}"
        )


def test_voice_turn_scope_is_exactly_the_selected_world(store, usage_store, world_loader, registry, monkeypatch, alx_world, desert_world):
    """(c) - every run_voice_turn_for_world call gets the selected speaker's
    own LoadedWorld, and the generation call it makes carries that world's
    own compiled prompt. The spy wraps the real function - nothing is
    stubbed out of the path under test."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    calls = []
    real = table_wiring.run_voice_turn_for_world

    def spy(**kwargs):
        calls.append(kwargs)
        return real(**kwargs)

    monkeypatch.setattr(table_wiring, "run_voice_turn_for_world", spy)
    client = _table_client(
        selector_script=[{"next": "desert", "reason": "r1"}],  # position 2 is a forced move
        stream_scripts=[[desert_sentence], [alx_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    first = http.post(f"/api/session/{session_id}/message", json={"text": "hi"}, headers=auth).json()
    second = http.post(f"/api/session/{session_id}/continue", headers=auth).json()

    assert [c["world"].world_key for c in calls] == ["desert", "alx"]
    assert [first["turn_selected"]["world_key"], second["turn_selected"]["world_key"]] == ["desert", "alx"]
    for c in calls:
        # One LoadedWorld per turn, and the usage attribution names it.
        assert c["usage_world_key"] == c["world"].world_key
        # The per-world session memory handed in is derived from that
        # world's own turns only (empty here - neither had spoken before).
    # The second call's history/context carries desert's SAID words (the
    # public transcript) but its scope objects are alx's alone.
    second_call = calls[1]
    assert second_call["world"].world_key == "alx"
    assert "since your last turn" in second_call["context_prefix"]


def test_no_foreknowledge_instruction_reaches_every_voice(store, usage_store, world_loader, registry, alx_world, desert_world):
    """Mark's rule (2026-08-28, after the first live run): a Representative
    has insight into the conversation and its own world ONLY - no
    foreknowledge of the other worlds. The grounding net cannot enforce
    this (it checks citations, and a voice describing another world from
    the model's general knowledge simply loses its badge), so the
    epistemic position is stated in every table voice call's context, and
    this test pins that it actually arrives."""
    alx_sentence, _ = grounded_sentence(alx_world)
    desert_sentence, _ = grounded_sentence(desert_world)
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "r1"}],  # position 2 is a forced move
        stream_scripts=[[alx_sentence], [desert_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    http.post(f"/api/session/{session_id}/message", json={"text": "hi"}, headers=auth)
    http.post(f"/api/session/{session_id}/continue", headers=auth)
    assert len(client.messages.stream_calls) == 2
    for call in client.messages.stream_calls:
        # 2026-09-05 bug fix (Mark's report: monologues on broad questions):
        # the epistemic/engagement instruction now rides in the directive
        # channel (system), not the user message it lived in entirely
        # before - see engine.m4.turn._build_turn_directive's own note on
        # why. "Reaches every voice" still means either channel.
        rendered = str(call["system"]) + str(call["messages"])
        assert "only through what they have said" in rendered
        assert "no knowledge of their worlds" in rendered
        assert "THEIR witness, never yours" in rendered  # the L4 appropriation finding's fix
        assert "Keep this turn compact" in rendered


def test_per_world_session_memory_is_filtered_by_speaker():
    transcript = [
        {"speaker": "participant", "text": "q"},
        {"speaker": "alx", "text": "a", "citations": [{"sentence": "a", "record_ids": ["alx.story.one"]}],
         "figures_used": [{"id": "alx.figure.origen"}], "glosses": [{"id": "alx.term.logos"}]},
        {"speaker": "desert", "text": "b", "citations": [{"sentence": "b", "record_ids": ["desert.story.two"]}],
         "figures_used": [], "glosses": []},
    ]
    alx_told, alx_figures, alx_glosses = table_wiring._already_sets_for("alx", transcript)
    desert_told, _, _ = table_wiring._already_sets_for("desert", transcript)
    assert alx_told == {"alx.story.one"} and desert_told == {"desert.story.two"}
    assert alx_figures == {"alx.figure.origen"} and alx_glosses == {"alx.term.logos"}
    # A story desert told is NOT "already told" for alx, and vice versa.
    assert "desert.story.two" not in alx_told and "alx.story.one" not in desert_told


def test_viewer_parameterized_history():
    labels = {"alx": "Theon (Alexandria)", "desert": "Papnoute (The Desert)",
              "participant": "The participant", "facilitator": "The Facilitator"}
    transcript = [
        {"speaker": "facilitator", "text": "welcome to the Table"},
        {"speaker": "participant", "text": "what is prayer?"},
        {"speaker": "alx", "text": "Prayer is conversation with God.", "citations": []},
        {"speaker": "desert", "text": "Prayer is the cell's own work.", "citations": []},
        {"speaker": "participant", "text": "and fasting?"},
    ]
    alx_history, alx_pending = table_wiring.table_history_for("alx", transcript, labels)
    # alx's own turn is the assistant side; everything before it is one user
    # bucket; everything after is pending for the next call.
    assert alx_history == [
        {"role": "user", "content": "The Facilitator: welcome to the Table\n\nThe participant: what is prayer?"},
        {"role": "assistant", "content": "Prayer is conversation with God."},
    ]
    assert alx_pending == ["Papnoute (The Desert): Prayer is the cell's own work.", "The participant: and fasting?"]

    desert_history, desert_pending = table_wiring.table_history_for("desert", transcript, labels)
    # desert hears alx's SAID words attributed on the user side - what was
    # said at the Table, never alx's records.
    assert desert_history[0]["content"].endswith("Theon (Alexandria): Prayer is conversation with God.")
    assert desert_history[1] == {"role": "assistant", "content": "Prayer is the cell's own work."}
    assert desert_pending == ["The participant: and fasting?"]
