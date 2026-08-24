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


def test_harmful_dynamic_signal_names_the_dynamic_and_keeps_the_voice():
    """Track B is a dependency dynamic, not a crisis: no resources, and
    Program-Spec SS8's "explicit continue path back to the voice" means the
    message is NOT withheld the way an acute signal withholds it."""
    client = FakeBedrockClient(
        safety_response=_safety("HARMFUL_DYNAMIC_SIGNAL"), reader_response=_reader(),
        stream_chunks=["We kept the meal together [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "safety_turn"
    facilitator = result.facilitator_events[0]
    assert facilitator["kind"] == "safety"
    assert facilitator["resources_appended"] is False   # Track B never appends
    assert result.voice_event is not None               # the voice still answers


def test_ambiguous_low_confidence_checks_in_and_does_not_answer():
    """Rule 2: softer than the safety turn, and deliberately not an answer -
    the safety call was uncertain, so the message never reaches the voice."""
    client = FakeBedrockClient(safety_response=_safety("AMBIGUOUS_LOW_CONFIDENCE"), reader_response=_reader())
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "check_in_turn"
    facilitator = result.facilitator_events[0]
    assert facilitator["kind"] == "safety"
    assert facilitator["resources_appended"] is False
    assert result.voice_event is None


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


def test_system_nature_is_answered_by_the_facilitator_not_the_world():
    """Rule 3, "plainly, immediately". A question about what the system IS is
    not a question any world can answer, so the voice is never asked - which
    is the failure this route exists to prevent."""
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(out_of_scope={"class": "system_nature"}))
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="are you an AI?", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "system_nature_turn"
    assert result.voice_event is None
    text = result.facilitator_events[0]["text"]
    assert result.facilitator_events[0]["kind"] == "threshold"
    assert "you are talking to an ai" in text.lower()


def test_etic_turn_speaks_for_the_class_that_was_pressed():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(out_of_scope={"class": "later_age"}))
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="what about the Reformation", pressed={"later_age": True}, anachronistic_term_ids=set())
    assert result.routing_action == "etic_turn"
    assert result.voice_event is None
    assert "after this world's own horizon" in result.facilitator_events[0]["text"]


def test_a_bridge_turn_hands_the_voice_the_subject_not_the_modern_word():
    """Program-Spec SS77: the Facilitator speaks the modern sense, the voice
    receives the term-free underlying subject, and the participant's modern
    word never reaches it. Both strings are the fleet record's own."""
    from engine.m1.loader import load_fleet_records

    term_id = "_fleet.modern.trinity"
    fleet = load_fleet_records()
    assert term_id in fleet, "fixture assumes the fleet's own modern_term record"
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(modern_terms=[{"term_id": term_id, "display": "Trinity"}]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="did you believe in the Trinity", pressed={}, anachronistic_term_ids={term_id})
    assert result.routing_action == "bridge_turn"
    facilitator = result.facilitator_events[0]
    assert facilitator["kind"] == "bridge"
    assert fleet[term_id]["modern_sense"] in facilitator["text"]
    assert result.voice_event is not None
    # the voice was asked the underlying subject, not the participant's own
    # sentence. Note the subject itself DOES name the word - the fleet record
    # says "before the word 'Trinity' existed for them to use" - which is the
    # record's own way of explaining the absence, not the modern word
    # reaching the voice as a question to answer.
    sent = client.messages.captured_stream_calls[-1][1][-1]["content"]
    assert fleet[term_id]["underlying_subject"] in sent
    assert "did you believe in the Trinity" not in sent


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


def test_a_turn_the_net_cannot_ground_still_reaches_the_participant_whole():
    """Program-Spec M4 / Artifact-5 SS2: the checks gate decoration, never
    the text. An off-canon message and an untagged answer: the net records
    that nothing substantive was grounded, and the participant still reads
    exactly what the voice wrote. No code-appended floor line - Program-Spec
    M5: "the honest limit is the voice's own testimony, not a system
    apology."
    """
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(asks=[{"order": 1, "text": "what's the weather like"}]), stream_chunks=["We enjoy talking about many things."])
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="what's the weather like today", pressed={}, anachronistic_term_ids=set())
    assert result.voice_event["text"] == "We enjoy talking about many things."
    assert "We don't have grounded material of our own for that." not in result.voice_event["text"]
    # the verdict is still carried, for the SS5 audit
    assert result.voice_event["degraded_by_net"] is True


def test_a_sentence_that_fails_verification_loses_its_citation_not_its_existence():
    """The measured cost of deleting instead: 25% of every sentence the
    voice wrote, and an answer to "who was he" that named nobody because
    the naming sentence was struck."""
    world = _world()
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(asks=[{"order": 1, "text": "who is jesus"}]),
        stream_chunks=["We received the community's own memory of Jesus [[fix.witness.who-is-jesus]]. "
                       "Athanasius said it plainly [[fix.nonexistent.record]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=world, participant_message="who is jesus", pressed={}, anachronistic_term_ids=set())
    text = result.voice_event["text"]
    assert "Athanasius said it plainly" in text          # still reaches the reader
    assert "[[" not in text                              # tags never do
    cited = {rid for c in result.voice_event["citations"] for rid in c["record_ids"]}
    assert "fix.nonexistent.record" not in cited         # but it is not decorated as sourced
    verdicts = {s["sentence"][:20]: s["verdict"] for s in result.voice_event["grounding"]["sentences"]}
    assert any(v != "ok" for v in verdicts.values())     # and the audit sees the failure


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


def test_session_memory_rides_in_messages_and_leaves_the_cached_prefix_alone():
    # Program-Spec M4: "one generation call with the participant's own
    # words, the private directive, and full-session memory in cache-
    # conscious layout." Until now the call sent one user message and the
    # voice had never heard the last thing it said.
    world = _world()
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(asks=[{"order": 1, "text": "and what then"}]),
        stream_chunks=["We enjoy talking about many things."],
    )
    history = [
        {"role": "user", "content": "who is jesus"},
        {"role": "assistant", "content": "He was God's own Word, come to us in flesh."},
    ]
    run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
             world=world, participant_message="and what then", pressed={}, anachronistic_term_ids=set(), history=history)

    system, messages = client.messages.captured_stream_calls[0]
    assert [m["role"] for m in messages] == ["user", "assistant", "user"]
    assert messages[0]["content"] == "who is jesus"
    assert messages[1]["content"] == "He was God's own Word, come to us in flesh."
    assert "and what then" in messages[2]["content"]  # this turn's own message, evidence block and all
    # the world prompt is still the sole cached block, untouched by a
    # growing conversation
    assert system[0]["text"] == world.prompt_text
    assert system[0]["cache_control"] == {"type": "ephemeral"}


def test_a_turn_with_no_history_is_unchanged():
    world = _world()
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(asks=[{"order": 1, "text": "hello"}]),
                               stream_chunks=["We enjoy talking about many things."])
    run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
             world=world, participant_message="hello", pressed={}, anachronistic_term_ids=set())
    _, messages = client.messages.captured_stream_calls[0]
    assert [m["role"] for m in messages] == ["user"]


def test_a_bridge_fires_on_the_invented_term_id_the_reader_actually_returns():
    """The seam this closes was measured, not imagined: live on 2026-08-24
    the reader returned term_id "trinity_doctrine" for "How did your
    community understand the Trinity?", routing intersected that against
    fleet record ids, matched nothing, and the turn went to the ordinary
    voice path. The reader is INSTRUCTED to invent that id
    (engine.m5.live_calls' own prompt), so the fix is code resolving it,
    not the model guessing better."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(modern_terms=[{"term_id": "trinity_doctrine", "display": "the Trinity"}]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="How did your community understand the Trinity?", pressed={}, anachronistic_term_ids={"_fleet.modern.trinity"})
    assert result.routing_action == "bridge_turn"
    assert result.facilitator_events[0]["kind"] == "bridge"


def test_a_modern_term_the_fleet_does_not_carry_still_does_not_bridge():
    """Resolution is a lookup, not a permission slip - a term with no fleet
    record keeps the reader's invented id and never intersects."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(modern_terms=[{"term_id": "personal_savior", "display": "personal Lord and Savior"}]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="was he your personal Lord and Savior", pressed={}, anachronistic_term_ids={"_fleet.modern.trinity"})
    assert result.routing_action == "voice_with_directive"


def test_the_readers_out_of_scope_class_reaches_the_caller():
    """engine.api.wiring needs it to append escalation_pressed - without it
    the pressed map stays empty forever and etic_turn is unreachable."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(out_of_scope={"class": "later_age"}),
        stream_chunks=["We never heard of it [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="what did you make of Nicaea", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "voice_with_directive"
    assert result.out_of_scope_class == "later_age"


def test_a_bridge_fires_when_the_reader_flags_nothing_at_all():
    """Run 2 turn 2, 2026-08-24: the reader returned modern_terms: [] for
    "How did your community understand the Trinity?" - the same question it
    had flagged twice earlier the same day - and the bridge did not fire.
    Whether the participant used the word is not a judgement call, so the
    message is read directly."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(modern_terms=[]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="How did your community understand the Trinity?", pressed={}, anachronistic_term_ids={"_fleet.modern.trinity"})
    assert result.routing_action == "bridge_turn"
    assert result.facilitator_events[0]["kind"] == "bridge"


def test_a_message_with_no_modern_term_still_takes_the_ordinary_path():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(modern_terms=[]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="who was Jesus to your people", pressed={}, anachronistic_term_ids={"_fleet.modern.trinity"})
    assert result.routing_action == "voice_with_directive"


def test_the_word_in_the_message_does_not_bridge_a_world_it_is_not_anachronistic_for():
    """The scan finds the word; the world's own time window still decides
    whether it is anachronistic (engine.m5.anachronism.anachronistic_term_ids).
    A world whose horizon closes after the term's origin year gets the
    ordinary path, and the voice answers in its own words."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(modern_terms=[]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="How did your community understand the Trinity?", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "voice_with_directive"
