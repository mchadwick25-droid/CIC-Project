"""Hermetic (no live model call) tests for engine.m4.turn.run_turn's
dispatch: does the right routing action reach the right generation path,
and - the one that matters most - that the ACUTE_DISTRESS crisis path
never calls the voice at all (portfolio decision 2026-09-08,
CiC_System_Hub_Decision_Log.md), and its crisis-resources append fires
unconditionally regardless of what the fake client is configured to
stream.
"""
import threading
from types import SimpleNamespace


from engine.m4 import turn as turn_module
from engine.m4.turn import run_gate, run_turn, run_voice_turn_for_world
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
    def __init__(self, *, safety_response, reader_response, stream_chunks, stream_scripts=None):
        self._responses = {
            "submit_safety_classification": safety_response,
            "submit_reader_output": reader_response,
        }
        self._stream_chunks = stream_chunks
        # R27 build item 5's own enforcement tests need a DIFFERENT raw
        # answer on the retry than on the raw attempt (a real regeneration
        # call) - stream_scripts is a list of chunk-lists, one per call,
        # popped in order; None (every other test's own default) keeps the
        # original single-script behavior unchanged.
        self._stream_scripts = list(stream_scripts) if stream_scripts is not None else None
        self.captured_stream_calls = []  # [(system, messages), ...] - lets a test see what the voice call actually received

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        return SimpleNamespace(content=[_FakeToolUse(name, self._responses[name])], usage=_FAKE_USAGE)

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        self.captured_stream_calls.append((system, messages))
        chunks = self._stream_scripts.pop(0) if self._stream_scripts is not None else self._stream_chunks
        return _FakeStreamCtx(chunks)


class FakeBedrockClient:
    def __init__(self, *, safety_response, reader_response, stream_chunks=(), stream_scripts=None):
        self.messages = _FakeMessages(
            safety_response=safety_response, reader_response=reader_response,
            stream_chunks=stream_chunks, stream_scripts=stream_scripts,
        )


def _reader(**overrides):
    base = {"asks": [{"order": 1, "text": "who was Jesus"}], "register": "informational", "clarity": "clear", "ambiguity_options": [], "out_of_scope": {"class": "none"}, "modern_terms": []}
    base.update(overrides)
    return base


def _safety(signal="NO_SIGNAL", **overrides):
    base = {"signal": signal, "acute_level": "none", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "high"}
    base.update(overrides)
    return base


def _world():
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [{"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}]},
        quotes={"quotes": [{"id": "fix.quote.private-teaching", "license": "do-not-voice", "text": "not for the voice to speak"}]},
        figures={},
        coverage={},
        frame={"representative": {"name": "Vera", "role_label": "Witness"}},
    )


def test_acute_distress_never_calls_the_voice_even_when_a_stream_is_configured():
    """Portfolio decision 2026-09-08 (CiC_System_Hub_Decision_Log.md):
    the Representative never steps out of its world once ACUTE_DISTRESS
    fires - not "speaks alongside the Facilitator" (the prior behavior),
    strict decoupling, matching engine.m4.round's own table-crisis branch
    (Artifact-7 SS2). The fake client is configured to stream real text
    precisely so this proves the voice is never even called, not merely
    that its output is discarded."""
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS", acute_level="a1"), reader_response=_reader(), stream_chunks=["I hear you. ", "That sounds heavy."])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
    )
    assert result.routing_action == "safety_turn"
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is True
    assert "not Vera" in result.facilitator_events[0]["text"]  # names the Representative from world.frame, not a placeholder
    assert result.voice_event is None
    assert client.messages.captured_stream_calls == []  # no Sonnet call spent on a crisis turn at all


def test_acute_distress_with_genuinely_empty_stream_still_appends_resources():
    """A pre-fix regression guard, kept in its genuinely-empty-stream shape:
    whatever the fake client is configured to produce, the crisis path
    never touches it - the append is unconditioned on the stream, exactly
    as crisis_resources.append_crisis_resources_turn's own docstring
    requires."""
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS", acute_level="a1"), reader_response=_reader(), stream_chunks=[])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
    )
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is True
    assert result.voice_event is None  # nothing worth showing as a voice turn - the append still happened


def test_acute_distress_a2_escalation_gets_the_more_direct_script():
    """Artifact-4 SS1: acute_level a2 (plan or intent) routes identically to
    a1 - same safety_turn action - but SS5.1 drafts a more direct register
    for it. First firing this session (no track_a_last), so this is the
    escalation script, not the continuation one."""
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS", acute_level="a2"), reader_response=_reader(), stream_chunks=["I hear you."])
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())
    text = result.facilitator_events[0]["text"]
    assert "I need to stop here and be straightforward with you" in text
    assert "I want to step in for a moment" not in text  # not the a1 opening


def test_acute_distress_second_firing_in_session_gets_the_lighter_continuation():
    """SS4.4/SS4.6's "sustained attention": once Track A has already fired
    once this session (track_a_last is not None), a later firing gets the
    lighter continuation turn - and this outranks acute_level, so even an
    a2 reading on this later turn still gets the continuation, not a second
    full A2 script."""
    prior_track_a = {"track": "A", "level": "a1", "accumulator": {}, "risk_subject": "not_applicable"}
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS", acute_level="a2"), reader_response=_reader(), stream_chunks=["I hear you."])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set(), track_a_last=prior_track_a,
    )
    text = result.facilitator_events[0]["text"]
    assert result.facilitator_events[0]["resources_appended"] is True  # still Track A content, just the lighter script
    assert "I'm still right here with you" in text
    assert "I need to stop here" not in text  # not the a2 script
    assert "I want to step in for a moment" not in text  # not the a1 script


def test_harmful_dynamic_signal_names_the_dynamic_and_silences_the_voice():
    """Track B is a dependency dynamic, not a crisis: no resources - but per
    Program-Spec SS8's 2026-09-20 amendment, the voice is silenced here the
    same way Track A silences it below; no "explicit continue path back to
    the voice" within the same turn any more."""
    client = FakeBedrockClient(
        safety_response=_safety("HARMFUL_DYNAMIC_SIGNAL"), reader_response=_reader(),
        stream_chunks=["We kept the meal together [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "safety_turn"
    facilitator = result.facilitator_events[0]
    assert facilitator["kind"] == "safety"
    assert facilitator["resources_appended"] is False   # Track B never appends
    assert "not Vera" in facilitator["text"]  # names the Representative from world.frame, not a placeholder
    assert result.voice_event is None                   # the voice never runs, same as Track A
    assert len(result.usage_records) == 2                # safety, reader - no voice call at all, same as the crisis path
    assert {r.call_kind for r in result.usage_records} == {"safety_call", "reader_call"}


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
    citations = result.voice_event["citations"]
    assert [{"sentence": c["sentence"], "record_ids": c["record_ids"]} for c in citations] == [
        {"sentence": "We did not claim to have seen him ourselves.", "record_ids": ["fix.witness.who-is-jesus"]}
    ]
    # citation_cards.resolve_citation_sources's own addition - see
    # test_citation_cards.py for the resolution logic itself (including
    # the doctrinal_witness label logic - a real first-sentence label,
    # not the record id, per the cross-world transparency audit); this
    # just proves run_turn actually calls it.
    assert citations[0]["sources"] == [
        {
            "record_id": "fix.witness.who-is-jesus",
            "record_type": "doctrinal_witness",
            "label": "We did not claim to have seen him ourselves",
            "sources": [],
        }
    ]
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
    assert len(result.usage_records) == 2  # safety, reader - no voice call at all on the crisis path
    assert {r.call_kind for r in result.usage_records} == {"safety_call", "reader_call"}
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
    assert "we use ai" in text.lower()


def test_etic_turn_speaks_for_the_class_that_was_pressed():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(out_of_scope={"class": "later_age"}))
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="what about the Reformation", pressed={"later_age": True}, anachronistic_term_ids=set())
    assert result.routing_action == "etic_turn"
    assert result.voice_event is None
    assert "this world's own witnesses stop" in result.facilitator_events[0]["text"]


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


def test_secondary_context_reaches_evidence_assembly_and_fills_a_gap_cell():
    """Stage 4f (Build-Plan.md): run_voice_turn_for_world's own
    secondary_context param (the table's additions - None on every
    interview call) threads through to evidence.assemble_evidence and can
    find ground an off-canon participant_message alone would not. Same
    real-fleet-canon discipline as the evidence-block wiring test above,
    not a synthetic cell id."""
    from engine.m1.loader import load_fleet_records
    from engine.m4.evidence import match_asks_to_cells

    secondary_text = "who was Jesus, to you and your people"
    canon_questions = load_fleet_records()
    matches = match_asks_to_cells(message="", asks=[{"text": secondary_text}], canon_questions=canon_questions, top_n=1)
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
        reader_response=_reader(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=world,
        participant_message="What is the weather like today?", directive=None, session_id="test-session",
        secondary_context=secondary_text,
    )

    system, messages = client.messages.captured_stream_calls[0]
    user_message = messages[0]["content"]
    assert "[[fix.witness.who-is-jesus]]" in user_message


def test_secondary_context_defaults_to_none_and_changes_nothing():
    """Every interview call omits secondary_context - confirms the default
    keeps run_voice_turn_for_world byte-identical to before this stage."""
    from engine.m1.loader import load_fleet_records
    from engine.m4.evidence import match_asks_to_cells

    ask_text = "who was Jesus, to you and your people"
    canon_questions = load_fleet_records()
    matches = match_asks_to_cells(message="", asks=[{"text": ask_text}], canon_questions=canon_questions, top_n=1)
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
    run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=world,
        participant_message=ask_text, directive=None, session_id="test-session",
    )
    system, messages = client.messages.captured_stream_calls[0]
    assert "[[fix.witness.who-is-jesus]]" in messages[0]["content"]


def test_already_bridged_figures_reach_the_voice_as_an_already_introduced_line():
    """A pilot read found both Chloe turns opened "One of us,
    Ignatius" - already_bridged_figure_ids kept the second UI mark from
    firing but never reached the voice. The set now also resolves to
    spoken names and rides in the evidence block, so the voice knows the
    participant has met the name. Without the kwarg, no line - a first
    turn's prompt is unchanged."""
    ask_text = "who was Jesus, to you and your people"
    world = LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [{"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}]},
        quotes={"quotes": []},
        figures={"figures": [
            {"id": "fix.figure.the-elder", "names": [{"tag": "in-world", "name": "the Elder"}]},
            {"id": "fix.figure.unmet", "names": [{"tag": "in-world", "name": "Rhoda"}]},
        ]},
        coverage={"C-I": {"doctrinal_witness": ["fix.witness.who-is-jesus"], "terms": [], "stories": [], "quotes": [], "honest_limit": [], "gravities": [], "forces": [], "contested_claims": []}},
        frame={},
    )
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(asks=[{"order": 1, "text": ask_text}]),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=world, participant_message=ask_text, pressed={}, anachronistic_term_ids=set(),
        already_bridged_figure_ids={"fix.figure.the-elder"},
    )
    system, messages = client.messages.captured_stream_calls[0]
    user_message = messages[0]["content"]
    assert "## Already introduced: the Elder." in user_message
    assert "Rhoda" not in user_message  # never introduced, so never listed
    # The per-turn directive (the channel measured to win - see
    # _build_turn_directive) carries the same state.
    directive_text = system if isinstance(system, str) else str(system)
    assert "Already introduced in this conversation: the Elder." in directive_text
    assert "Rhoda" not in directive_text


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


def test_the_gate_payload_reaches_the_caller_whole():
    """Two things at once, and neither used to arrive. engine.api.wiring
    needs out_of_scope to append escalation_pressed (without it the pressed
    map stays empty forever and etic_turn is unreachable), and it needs the
    rest to write a gate_decision that says anything at all - every one this
    build logged before 2026-08-24 had every key but route and degraded
    hardcoded blank."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(out_of_scope={"class": "later_age"}),
        stream_chunks=["We never heard of it [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="what did you make of Nicaea", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "voice_with_directive"
    assert result.gate["out_of_scope"] == {"class": "later_age"}
    assert result.gate["register"] == "informational"
    assert result.gate["asks"] == [{"order": 1, "text": "who was Jesus"}]
    assert result.gate["safety"]["signal"] == "NO_SIGNAL"
    assert result.gate["route"] == "voice_with_directive"
    assert result.gate["degraded"] is False
    assert result.gate["directive"]["asks"] == [{"order": 1, "text": "who was Jesus"}]


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


def test_the_gate_payload_shows_which_path_found_a_modern_term():
    """The resolved list goes in the event, not the raw one: reader_term_id
    and source are how an auditor sees which path found a term and what the
    model called it before code renamed it."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(modern_terms=[{"term_id": "trinity_doctrine", "display": "the Trinity"}]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="How did your community understand the Trinity?", pressed={}, anachronistic_term_ids=set())
    terms = result.gate["modern_terms"]
    assert [t["term_id"] for t in terms] == ["_fleet.modern.trinity"]
    assert terms[0]["reader_term_id"] == "trinity_doctrine"


def test_a_failed_reader_is_visible_in_the_gate_payload():
    """The case the blank payload hid completely: a gate that returned and
    a gate that fell over used to log identically."""
    from engine.m5.failure import CallOutcome

    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    real_reader = turn_module.live_calls.call_reader
    turn_module.live_calls.call_reader = lambda *a, **k: CallOutcome(status="timeout")
    try:
        result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set())
    finally:
        turn_module.live_calls.call_reader = real_reader

    assert result.routing_action == "voice_pass_through"
    assert result.gate["degraded"] is True
    assert result.gate["register"] is None
    assert result.gate["out_of_scope"] is None
    assert result.gate["asks"] == []
    assert result.gate["directive"] is None
    # safety still returned, and the record still says so
    assert result.gate["safety"]["signal"] == "NO_SIGNAL"


def test_a_bridged_compound_question_keeps_its_other_ask():
    """Two asks in one sentence, one carrying the modern word. The word is
    barred; the other ask is not, and used to be lost with it because the
    bridge route carries no directive."""
    import json as _json

    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(asks=[
            {"order": 1, "text": "did you argue about the Trinity"},
            {"order": 2, "text": "did you argue about who should lead"},
        ]),
        stream_chunks=["We argued about who should lead [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="did you argue about the Trinity, and about who should lead?", pressed={}, anachronistic_term_ids={"_fleet.modern.trinity"})

    assert result.routing_action == "bridge_turn"
    system, messages = client.messages.captured_stream_calls[-1]
    sent = _json.dumps([system, messages])
    assert "did you argue about who should lead" in sent
    # The barred ask never reaches the voice. Asserting on the ask's own
    # wording rather than on the bare word: the fleet record's underlying
    # subject names "Trinity" itself, to explain the absence, and the fix
    # world's own honest-limit record carries it too.
    assert "did you argue about the Trinity" not in sent
    # and the event log says what the voice was actually handed
    assert [a["order"] for a in result.gate["directive"]["asks"]] == [2]


def test_an_ordinary_bridge_still_hands_the_voice_the_subject_alone():
    """No regression on the single-ask bridge: no directive, exactly as
    before."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(asks=[{"order": 1, "text": "did you believe in the Trinity"}]),
        stream_chunks=["We spoke of the Father and the Son [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="did you believe in the Trinity", pressed={}, anachronistic_term_ids={"_fleet.modern.trinity"})
    assert result.routing_action == "bridge_turn"
    assert result.gate["directive"] is None


def _world_with_figure():
    """_world() with one real-shaped figure record added - compiled/
    figures.json's own {id, names, bridge_line, dates} shape
    (engine.m2.builders.build_figures_json), not a synthetic one, so these
    tests exercise engine.m4.name_bridge against the shape it actually gets
    handed at runtime."""
    from dataclasses import replace

    return replace(
        _world(),
        figures={
            "figures": [
                {
                    "id": "fix.figure.the-elder",
                    "names": [
                        {"name": "the Elder", "tag": "in-world"},
                        {"name": "the presiding elder (unnamed, the source's own term)", "tag": "scholarly"},
                    ],
                    "bridge_line": "the presiding elder whose name the record itself never gives",
                    "dates": {},
                    "narratable": False,
                }
            ]
        },
    )


def test_figures_used_is_populated_from_a_name_in_the_finished_answer():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        stream_chunks=["We were led by the Elder, who spoke for us [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world_with_figure(), participant_message="who led you", pressed={}, anachronistic_term_ids=set(),
    )
    from engine.m4 import events

    events.validate("voice_turn", result.voice_event)  # the schema floor, not just this test's own expectations
    figures_used = result.voice_event["figures_used"]
    assert [f["id"] for f in figures_used] == ["fix.figure.the-elder"]
    assert figures_used[0]["matched_name"] == "the Elder"
    assert figures_used[0]["bridge_line"].startswith("the presiding elder")


def test_already_bridged_figure_ids_suppresses_a_repeat_within_run_turn():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        stream_chunks=["The Elder spoke for us again [[fix.witness.who-is-jesus]]."],
    )
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world_with_figure(), participant_message="who led you", pressed={}, anachronistic_term_ids=set(),
        already_bridged_figure_ids={"fix.figure.the-elder"},
    )
    assert result.voice_event["figures_used"] == []


def test_crisis_path_never_produces_a_voice_event_even_with_a_figure_in_scope():
    """Superseded by the portfolio decision (2026-09-08): the crisis path
    used to hand-build a voice_event and this test guarded its shape
    (figures_used present but empty, since find_figures_used never runs on
    that path). Now there is no voice_event on the crisis path at all."""
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS", acute_level="a1"), reader_response=_reader(), stream_chunks=["I hear you. ", "That sounds heavy."])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world_with_figure(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
    )
    assert result.voice_event is None


def _world_with_term():
    """_world() with one real-shaped term record added to the repository -
    the {plain_meaning, world_word, senses, false_friend, sources} shape
    Artifact-1's own schema defines, so these tests exercise
    engine.m4.term_glosses against the real thing, not a synthetic guess."""
    from dataclasses import replace

    return replace(
        _world(),
        repository={
            "records": [
                {"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."},
                {
                    "id": "fix.term.koinonia",
                    "record_type": "term",
                    "world_word": "koinonia (shared life)",
                    "plain_meaning": "The shared life and goods of the gathered community.",
                    "quick_meaning": "Life held in common.",
                    "senses": {"translational": "\"Was it just a potluck?\" - no: koinonia bound property, meals, and care together."},
                    "false_friend": ["a modern support group"],
                    "sources": [{"source_id": "fix.source.witness-scroll", "locus": "2.1", "license": "public-domain"}],
                },
            ]
        },
    )


def test_glosses_is_populated_when_a_cited_term_is_actually_said():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        stream_chunks=["We held koinonia, sharing what we had [[fix.term.koinonia]]."],
    )
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world_with_term(), participant_message="how did you live", pressed={}, anachronistic_term_ids=set(),
    )
    from engine.m4 import events

    events.validate("voice_turn", result.voice_event)
    glosses = result.voice_event["glosses"]
    assert [g["id"] for g in glosses] == ["fix.term.koinonia"]
    assert glosses[0]["matched_name"] == "koinonia"
    assert glosses[0]["plain_meaning"].startswith("The shared life")
    assert glosses[0]["sourced_by"][0]["source_id"] == "fix.source.witness-scroll"


def test_already_bridged_gloss_ids_suppresses_a_repeat_within_run_turn():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        stream_chunks=["We held koinonia again [[fix.term.koinonia]]."],
    )
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world_with_term(), participant_message="how did you live", pressed={}, anachronistic_term_ids=set(),
        already_bridged_gloss_ids={"fix.term.koinonia"},
    )
    assert result.voice_event["glosses"] == []


def _history_of(n_turns):
    """n_turns completed user/assistant pairs - the same shape
    engine.api.wiring.history_from_transcript builds."""
    history = []
    for i in range(n_turns):
        history.append({"role": "user", "content": f"question {i}"})
        history.append({"role": "assistant", "content": f"answer {i}"})
    return history


def test_the_cap_fires_at_ten_completed_turns_and_spends_no_voice_call():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["should never be reached"])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="one more question", pressed={}, anachronistic_term_ids=set(),
        history=_history_of(turn_module.SESSION_TURN_CAP),
    )
    assert result.routing_action == "session_cap_turn"
    assert result.voice_event is None
    assert client.messages.captured_stream_calls == []  # no Sonnet call spent once capped
    assert result.facilitator_events[0]["kind"] == "close"
    from engine.m4 import events

    events.validate("facilitator_turn", result.facilitator_events[0])


def test_the_cap_does_not_fire_one_turn_early():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["still answering"])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="a question", pressed={}, anachronistic_term_ids=set(),
        history=_history_of(turn_module.SESSION_TURN_CAP - 1),
    )
    assert result.routing_action != "session_cap_turn"
    assert result.voice_event is not None


def test_acute_distress_is_never_capped_away():
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS", acute_level="a1"), reader_response=_reader(), stream_chunks=["I hear you."])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
        history=_history_of(turn_module.SESSION_TURN_CAP + 5),  # well past the cap
    )
    assert result.routing_action == "safety_turn"
    assert result.facilitator_events[0]["resources_appended"] is True


def test_a_non_acute_signal_is_capped_like_any_other_ordinary_turn():
    client = FakeBedrockClient(safety_response=_safety("HARMFUL_DYNAMIC", dynamic_tags=["dependency"]), reader_response=_reader(), stream_chunks=["should never be reached"])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I feel like you're the only one who understands me.", pressed={}, anachronistic_term_ids=set(),
        history=_history_of(turn_module.SESSION_TURN_CAP),
    )
    assert result.routing_action == "session_cap_turn"
    assert result.voice_event is None


def test_the_cap_names_the_representative_from_world_frame():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=[])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="one more", pressed={}, anachronistic_term_ids=set(),
        history=_history_of(turn_module.SESSION_TURN_CAP),
    )
    assert "Vera" in result.facilitator_events[0]["text"]


def test_a_capped_turn_still_attributes_its_gate_calls():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=[])
    result = run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="one more", pressed={}, anachronistic_term_ids=set(),
        history=_history_of(turn_module.SESSION_TURN_CAP),
    )
    assert {r.call_kind for r in result.usage_records} == {"safety_call", "reader_call"}
    assert all(r.session_id == "test-session" for r in result.usage_records)


def test_gate_calls_run_concurrently_not_sequentially():
    """Stage 0a (Build-Plan.md): call_safety and call_reader used to run
    strictly sequentially inside run_gate. A two-party barrier blocks each
    fake call until both have actually started - if the two calls were
    still sequential, the first would block forever waiting for a second
    call that cannot start until the first returns, and the barrier would
    time out with BrokenBarrierError. Concurrent execution clears it
    immediately, proving both calls are genuinely in flight at once, not
    merely that both eventually happen."""
    barrier = threading.Barrier(2, timeout=2.0)

    class _BarrierMessages:
        def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
            barrier.wait()
            name = tool_choice["name"]
            responses = {"submit_safety_classification": _safety("NO_SIGNAL"), "submit_reader_output": _reader()}
            return SimpleNamespace(content=[_FakeToolUse(name, responses[name])], usage=_FAKE_USAGE)

    client = SimpleNamespace(messages=_BarrierMessages())
    gate_run = run_gate(
        session_id="test-session", safety_client=client, safety_model_id="m",
        participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set(),
    )
    assert gate_run.safety_outcome.status == "ok"
    assert gate_run.reader_outcome.status == "ok"
    # Fixed append order regardless of which future actually completed first.
    assert [r.call_kind for r in gate_run.usage_records] == ["safety_call", "reader_call"]


def test_gate_carries_an_other_tradition_reader_classification_through_to_routing():
    """R27 F4 (reviewer thread fix list, 2026-09-22): a mocked-reader
    routing test to complement engine.m5.tests.test_routing's own pure-
    function coverage of route() - this proves the layer ABOVE it,
    run_gate's own real dispatch through resolve_gate, correctly carries
    a reader classification of "other_tradition" into
    gate_result.routing.out_of_scope_class end to end. The reader's own
    classification decision (does the real model actually read "What was
    your relationship with the Donatists?" as other_tradition) is a live
    model behavior no mock can test - engine.m5.live_calls.READER_SYSTEM_
    PROMPT's own rubric text is what changed for that, verified live,
    separately, not here. This test pins the deterministic half: once the
    reader SAYS other_tradition, nothing downstream loses it."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(out_of_scope={"class": "other_tradition"}),
    )
    gate_run = run_gate(
        session_id="test-session", safety_client=client, safety_model_id="m",
        participant_message="What was your relationship with the Donatists?",
        pressed={}, anachronistic_term_ids=set(),
    )
    assert gate_run.gate_result.routing.action == "voice_with_directive"
    assert gate_run.gate_result.routing.out_of_scope_class == "other_tradition"


def test_correction_is_appended_to_the_turn_directive_the_model_actually_sees():
    """R27 fix list F3 (reviewer thread, 2026-09-22):
    engine.m4.live_uncited_claims_battery's own opt-in regeneration
    channel - unset on every real interview/table caller (byte-identical
    behavior preserved; no assertion needed for the None case, since
    every other test in this file already exercises it without passing
    correction). This is the one hermetic proof that the text actually
    reaches the model, in the same uncached, per-turn system block
    turn_directive itself rides in - not silently dropped."""
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["An answer."])
    run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(),
        participant_message="who was Jesus", directive=None, session_id="test-session",
        correction="\n## Correction\nCite everything, or say plainly your record is silent.",
    )
    system_blocks = client.messages.captured_stream_calls[0][0]
    directive_text = "".join(b["text"] for b in system_blocks[1:])
    assert "Cite everything, or say plainly your record is silent." in directive_text


def test_debug_capture_receives_the_exact_raw_tagged_text_apply_net_checks():
    """R27 fix list F6 (reviewer thread, 2026-09-22):
    engine.m4.live_uncited_claims_battery's own opt-in paragraph-coverage
    channel - unset on every real caller, never part of voice_event. This
    is the one hermetic proof the captured text is the real raw stream
    output, tags and all, not a placeholder or a post-apply_net (already
    stripped) copy."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(),
        stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    capture: dict = {}
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(),
        participant_message="who was Jesus", directive=None, session_id="test-session",
        debug_capture=capture,
    )
    assert capture["raw_tagged_text"] == "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."
    assert "[[fix.witness.who-is-jesus]]" not in voice_event["text"]  # apply_net's own strip, unaffected by the capture


# R27 build item 5 (Decision-Log.md Entry 56/Rulings-Pending.md R36,
# 2026-09-23): the flag-gated enforcement's own required test list, per
# the reviewer thread's own item 5 message. r27_enforce=False (every
# existing test above, and every real caller until Mark flips
# CIC_R27_ENFORCE) is already proven byte-identical by the full suite
# passing unchanged; these are the flag-ON cases.
def _donatist_schism_world() -> LoadedWorld:
    """Same world as _world() above, plus a second record whose own text
    genuinely shares ground with "For years they held together." - the
    real alx conflict-turn shape (Decision-Log.md Entry 55's own pinned
    case), needed here so test 5 below is a real pass, not a rigged one."""
    world = _world()
    repo = dict(world.repository)
    repo["records"] = [
        *repo["records"],
        {
            "id": "fix.witness.donatist-schism", "record_type": "doctrinal_witness",
            "text": (
                "The two communities argued for years before the final break came, but for years they "
                "held together despite the strain between them."
            ),
        },
    ]
    return LoadedWorld(**{**world.__dict__, "repository": repo})


def test_r27_enforce_regenerates_a_wholly_uncited_paragraph_and_clears_on_a_clean_retry():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(),
        stream_scripts=[
            ["Even a broken priest could not block his grace."],
            ["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
        ],
    )
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(),
        participant_message="who was Jesus", directive=None, session_id="test-session",
        r27_enforce=True, known_tradition_names=[],
    )
    assert len(client.messages.captured_stream_calls) == 2  # the one allowed regeneration, no more
    assert voice_event["attempts_meta"]["r27_regenerated"] is True
    assert voice_event["r27_enforcement_exhausted"] is False
    assert voice_event["text"] == "We did not claim to have seen him ourselves."
    assert voice_event["paragraph_offenses"] == []
    assert voice_event["uncited_claims"] == []


def test_r27_enforce_hands_the_turn_to_the_facilitator_when_the_regeneration_still_fails():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(),
        stream_scripts=[
            ["Even a broken priest could not block his grace."],
            ["Even a broken priest could not block his grace."],
        ],
    )
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(),
        participant_message="who was Jesus", directive=None, session_id="test-session",
        r27_enforce=True, known_tradition_names=[],
    )
    assert len(client.messages.captured_stream_calls) == 2  # one attempt, one regeneration, never a third
    assert voice_event["attempts_meta"]["r27_regenerated"] is True
    assert voice_event["r27_enforcement_exhausted"] is True
    assert voice_event["text"] == ""  # the voice's text is not shown - the caller substitutes a Facilitator turn
    assert voice_event["paragraph_offenses"] == []
    assert voice_event["uncited_claims"] == []


def test_r27_enforce_never_regenerates_an_inherited_ungrounded_only_turn():
    # R36's own scope decision: inherited_ungrounded stays report-only.
    # "That was not the only one." carries no tag of its own but rides in
    # a cited paragraph whose inherited check fails - a real
    # inherited_ungrounded finding, reported, but not one of the two
    # classes item 5 enforces.
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(),
        stream_scripts=[
            ["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. That was not the only one."],
        ],
    )
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(),
        participant_message="who was Jesus", directive=None, session_id="test-session",
        r27_enforce=True, known_tradition_names=[],
    )
    assert len(client.messages.captured_stream_calls) == 1  # never regenerated
    assert voice_event["attempts_meta"]["r27_regenerated"] is False
    assert voice_event["r27_enforcement_exhausted"] is False
    assert voice_event["paragraph_offenses"] == [{"sentence": "That was not the only one.", "class": "inherited_ungrounded"}]


def test_r27_enforce_still_fails_the_augustinian_pair_inside_an_other_tradition_turn():
    # R26's own motivating sentence (Entry 50/51), routed via
    # other_tradition (is_other_tradition_first_ask=True) - proves the
    # narrowing at item 1 (own_doctrine_in_other_tradition_turn requiring
    # a real paragraph failure) does not somehow exempt a turn from
    # wholly_uncited_paragraph enforcement itself; the routing context is
    # irrelevant to whether this class enforces.
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(),
        stream_scripts=[
            ["Even a broken priest could not block his grace."],
            ["Even a broken priest could not block his grace."],
        ],
    )
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(),
        participant_message="What was your relationship with the Donatists?", directive=None, session_id="test-session",
        r27_enforce=True, known_tradition_names=[], is_other_tradition_first_ask=True,
    )
    assert voice_event["r27_enforcement_exhausted"] is True
    assert voice_event["text"] == ""


def test_r27_enforce_passes_a_grounded_frame_sentence_inside_a_cited_paragraph_without_regenerating():
    # alx's own conflict-turn shape (PR #427's own report:
    # uncited_in_cited_paragraph), same fixture discipline as
    # test_r27a_narrowed_rule_passes_a_grounded_frame_sentence_inside_a_
    # cited_other_tradition_paragraph in test_uncited_claims.py - a real
    # record whose own text grounds the frame sentence, not a rigged pass.
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(),
        stream_scripts=[
            [
                "The two sides argued for years before the break finally came [[fix.witness.donatist-schism]]. "
                "For years they held together."
            ],
        ],
    )
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_donatist_schism_world(),
        participant_message="who was Jesus", directive=None, session_id="test-session",
        r27_enforce=True, known_tradition_names=[],
    )
    assert len(client.messages.captured_stream_calls) == 1  # never regenerated
    assert voice_event["attempts_meta"]["r27_regenerated"] is False
    assert voice_event["r27_enforcement_exhausted"] is False
    assert voice_event["paragraph_offenses"] == []


# R39's own reviewer-ordered fix (relayed 2026-09-23): _other_tradition_
# directive's own honest-limit sentence used to fire unconditionally,
# even for a world (ijc) whose own records already name the tradition
# asked about - provably false in that case. Both branches pinned
# directly, per the reviewer's own explicit "test both branches"
# instruction, so a future edit can't silently reintroduce either defect
# shape (a world with real evidence still forced to deny it, or a world
# with none suddenly handed a fabricated "your records speak to it").
def test_other_tradition_directive_keeps_the_fixed_sentence_when_there_is_no_evidence():
    text = turn_module._other_tradition_directive(None)
    assert turn_module.R26_HONEST_LIMIT_SENTENCE in text
    assert "your records already speak to it" not in text


def test_other_tradition_directive_keeps_the_fixed_sentence_on_an_empty_evidence_list():
    text = turn_module._other_tradition_directive([])
    assert turn_module.R26_HONEST_LIMIT_SENTENCE in text


def test_other_tradition_directive_skips_the_fixed_sentence_when_the_world_own_records_already_name_it():
    text = turn_module._other_tradition_directive(["ijc.quote.compelled-to-come-in", "ijc.story.emperor-builds-another-basilica"])
    assert turn_module.R26_HONEST_LIMIT_SENTENCE not in text
    assert "[[ijc.quote.compelled-to-come-in]]" in text
    assert "[[ijc.story.emperor-builds-another-basilica]]" in text
