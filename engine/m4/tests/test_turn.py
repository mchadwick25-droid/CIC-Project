"""Hermetic (no live model call) tests for engine.m4.turn.run_turn's
dispatch: does the right routing action reach the right generation path,
and - the one that matters most - does a GENUINELY empty stream (a fake
client returning zero text_stream chunks, not the force_empty_stream test
hook) still produce a crisis-resources append. force_empty_stream exists
for evidence scripts where forcing it is cheaper than trying to provoke a
real model into silence; this file proves the real code path handles a
real empty stream identically, via the fake client's stream_chunks=().
"""
from types import SimpleNamespace

import pytest

from engine.m4.turn import UnhandledRoutingAction, run_turn
from engine.m4.world_loader import LoadedWorld


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


_FAKE_USAGE = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=_FAKE_USAGE))

    def __exit__(self, *exc):
        return False


class _FakeMessages:
    def __init__(self, *, safety_response, reader_response, stream_chunks):
        self._responses = {
            "submit_safety_classification": safety_response,
            "submit_reader_output": reader_response,
        }
        self._stream_chunks = stream_chunks
        self.captured_stream_calls = []  # [(system, messages), ...] - lets a test see what the voice call actually received

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        return SimpleNamespace(content=[_FakeToolUse(name, self._responses[name])], usage=_FAKE_USAGE)

    def stream(self, *, model, max_tokens, system=None, messages):
        self.captured_stream_calls.append((system, messages))
        return _FakeStreamCtx(self._stream_chunks)


class FakeBedrockClient:
    def __init__(self, *, safety_response, reader_response, stream_chunks=()):
        self.messages = _FakeMessages(safety_response=safety_response, reader_response=reader_response, stream_chunks=stream_chunks)


def _reader(**overrides):
    base = {"asks": [{"order": 1, "text": "who was Jesus"}], "register": "informational", "clarity": "clear", "ambiguity_options": [], "out_of_scope": {"class": "none"}, "modern_terms": []}
    base.update(overrides)
    return base


def _safety(signal="NO_SIGNAL"):
    return {"signal": signal, "acute_level": "none", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "high"}


def _world():
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [{"id": "fix.witness.who-is-jesus", "text": "We did not claim to have seen him ourselves."}]},
        quotes={"quotes": [{"id": "fix.quote.private-teaching", "license": "do-not-voice", "text": "not for the voice to speak"}]},
        figures={},
        coverage={},
        frame={},
    )


def test_acute_distress_with_real_stream_text_appends_resources_not_empty():
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=["I hear you. ", "That sounds heavy."])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
    )
    assert result.routing_action == "safety_turn"
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is False
    assert result.voice_event is not None
    assert result.voice_event["text"] == "I hear you. That sounds heavy."


def test_acute_distress_with_genuinely_empty_stream_still_appends_resources():
    """The real code path, not the force_empty_stream hook: the fake
    client's stream yields zero chunks, exactly like a real model call that
    completes but produces no tokens."""
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=[])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
    )
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is True
    assert result.voice_event is None  # nothing worth showing as a voice turn - the append still happened


def test_force_empty_stream_hook_matches_the_real_empty_case():
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=["would never be seen"])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set(), force_empty_stream=True,
    )
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is True
    assert result.voice_event is None


def test_harmful_dynamic_signal_raises_unhandled_not_silently_dropped():
    client = FakeBedrockClient(safety_response=_safety("HARMFUL_DYNAMIC_SIGNAL"), reader_response=_reader())
    with pytest.raises(UnhandledRoutingAction):
        run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())


def test_ambiguous_low_confidence_check_in_turn_raises_unhandled():
    client = FakeBedrockClient(safety_response=_safety("AMBIGUOUS_LOW_CONFIDENCE"), reader_response=_reader())
    with pytest.raises(UnhandledRoutingAction):
        run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())


def test_ordinary_turn_calls_voice_generation_and_checks_inline_citations():
    # M4 step 5: no separate citations call - the single generation call
    # carries its own [[record.id]] tag, checked by grounding_net.check_turn
    # and stripped before the participant ever sees it.
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "voice_with_directive"
    assert result.voice_event["text"] == "We did not claim to have seen him ourselves."  # tag stripped
    assert result.voice_event["citations"] == [{"sentence": "We did not claim to have seen him ourselves.", "record_ids": ["fix.witness.who-is-jesus"]}]
    assert result.voice_event["do_not_voice_violation"] is None
    assert result.voice_event["degraded_by_net"] is False


def test_every_real_call_this_turn_makes_is_attributed_to_the_session():
    """M8's stage-6 gate item, exercised end to end: an ordinary turn makes
    THREE real calls now (safety, reader, voice generation) - the citations
    call is gone (M4 step 5, LIVE-GENERATION-DESIGN.md Fork 1) - every one
    must land in usage_records tagged with the caller's session_id, zero
    unattributed."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="participant-session-42", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set())
    assert len(result.usage_records) == 3
    assert {r.call_kind for r in result.usage_records} == {"safety_call", "reader_call", "voice_generation"}
    assert all(r.session_id == "participant-session-42" for r in result.usage_records)
    assert all(r.is_attributed for r in result.usage_records)


def test_crisis_turn_usage_records_are_also_attributed():
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=["I hear you."])
    result = run_turn(session_id="crisis-session-1", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set())
    assert len(result.usage_records) == 3  # safety, reader, voice_generation_crisis - no citations call on the crisis path
    assert all(r.session_id == "crisis-session-1" for r in result.usage_records)


def test_do_not_voice_quote_verbatim_is_flagged_on_a_real_turn():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["I should not have said this: not for the voice to speak."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="tell me the secret", pressed={}, anachronistic_term_ids=set())
    assert result.voice_event["do_not_voice_violation"] == "fix.quote.private-teaching"


def test_system_nature_out_of_scope_raises_unhandled():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(out_of_scope={"class": "system_nature"}))
    with pytest.raises(UnhandledRoutingAction):
        run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="are you an AI?", pressed={}, anachronistic_term_ids=set())


# ---- M4 step 5: evidence assembly wiring + the deterministic net's own
# degradation path (LIVE-GENERATION-DESIGN.md §9.5 Fork 2) -------------------


def test_ordinary_turn_wires_a_real_evidence_block_into_the_user_message():
    """Not a synthetic fixture - Stage A runs against the REAL fleet canon
    (engine.m1.loader.load_fleet_records, same call _run_ordinary_voice_turn
    makes), so this proves the wiring against the same data a live turn
    would see, not a hand-picked cell id that happens to agree with the
    test's own assumptions."""
    from engine.m1.loader import load_fleet_records
    from engine.m4.evidence import match_asks_to_cells

    ask_text = "who was Jesus, to you and your people"
    canon_questions = load_fleet_records()
    matches = match_asks_to_cells(message="", asks=[{"text": ask_text}], canon_questions=canon_questions, top_n=1)
    assert matches, "the real fleet canon should match at least one cell for this ask - if not, the fixture ask needs updating, not this test"
    cell = matches[0]["cell"]

    world = LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [{"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}]},
        quotes={"quotes": []},
        figures={},
        coverage={cell: {"doctrinal_witness": ["fix.witness.who-is-jesus"], "terms": [], "stories": [], "quotes": [], "honest_limit": [], "gravities": [], "forces": [], "contested_claims": []}},
        frame={},
    )
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(asks=[{"order": 1, "text": ask_text}]),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=world, participant_message=ask_text, pressed={}, anachronistic_term_ids=set())

    system, messages = client.messages.captured_stream_calls[0]
    user_message = messages[0]["content"]
    assert "## Ground for this turn" in user_message
    assert "[[fix.witness.who-is-jesus]]" in user_message
    assert ask_text in user_message  # the participant's own message still rides alongside the evidence block


def test_turn_with_no_cell_match_and_no_grounded_claim_degrades_to_the_fleet_floor_line():
    # An off-canon message and an untagged, unclaimable answer: Stage A
    # resolves to no cell (engine.m4.evidence's own "no cell" case), so
    # _degradation_statement has no honest_limit candidate to reach for and
    # falls back to the fleet floor line.
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(asks=[{"order": 1, "text": "what's the weather like"}]), stream_chunks=["We enjoy talking about many things."])
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="what's the weather like today", pressed={}, anachronistic_term_ids=set())
    assert result.voice_event["degraded_by_net"] is True
    assert "We don't have grounded material of our own for that." in result.voice_event["text"]


def test_already_told_ids_reaches_evidence_assembly_without_error():
    # Stage E is a pure annotate-not-drop pass with no candidates in this
    # fixture world's coverage - this just proves the parameter threads all
    # the way through run_turn -> _run_ordinary_voice_turn -> assemble_evidence
    # without blowing up, the plumbing test the fuller wiring test above
    # doesn't cover (that one exercises a real cell match, not this kwarg).
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set(),
        already_told_ids={"fix.story.the-long-road"},
    )
    assert result.voice_event["degraded_by_net"] is False


def test_the_per_turn_directive_sits_after_the_cache_breakpoint_not_inside_it():
    # The whole point of the split: the world's compiled prompt is the only
    # block carrying cache_control, and it is byte-identical to what was
    # compiled - so the prefix is reusable across every turn of a session.
    # The directive, which differs every turn, rides in a second block
    # AFTER that breakpoint. Concatenating the two (the shape this replaced)
    # made every turn a cache write and never a cache read.
    world = _world()
    ask_text = "who is jesus"
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(asks=[{"order": 1, "text": ask_text}]),
        stream_chunks=["We enjoy talking about many things."],
    )
    run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=world, participant_message=ask_text, pressed={}, anachronistic_term_ids=set())

    system, _ = client.messages.captured_stream_calls[0]
    assert len(system) == 2
    assert system[0]["text"] == world.prompt_text  # untouched, so the prefix holds
    assert system[0]["cache_control"] == {"type": "ephemeral"}
    assert "cache_control" not in system[1]  # the volatile half is never cached
    assert "This turn's private directive" in system[1]["text"]
    assert "This turn's private directive" not in system[0]["text"]
    # And the model still sees the same bytes in the same order as before.
    assert "".join(b["text"] for b in system) == world.prompt_text + system[1]["text"]
