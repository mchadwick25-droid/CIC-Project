"""Hermetic tests for engine.m4.turn_prep.prepare_voice_turn_inputs - the
setup engine.m4.turn._run_ordinary_voice_turn needs before a generation
call: the evidence-assembled user message and the per-turn private directive.
_build_turn_directive/_other_tradition_directive's own extensive coverage
stays in engine/m4/tests/test_turn.py (moved here unchanged, still
importable as turn_module._build_turn_directive/_other_tradition_directive
- see that file) - these tests exercise the new composition point itself,
not the directive-building logic it wraps."""
from engine.m4.turn_prep import prepare_voice_turn_inputs
from engine.m4.world_loader import LoadedWorld
from engine.m5.routing import Directive


def _world(**frame):
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={
            "records": [
                {"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."},
                {"id": "fix.core", "record_type": "world_core", "thin_topics": [{"topic": "resurrection"}]},
            ]
        },
        quotes={"quotes": []},
        figures={"figures": [{"id": "fix.figure.paul", "names": [{"name": "Paul"}]}]},
        coverage={},
        frame={"representative": {"name": "Vera"}, **frame},
    )


def _directive(**overrides):
    base = {"asks": [{"order": 1, "text": "who was Jesus"}], "register_note": None, "suspend_register_statement_1": False, "ambiguity_options": []}
    base.update(overrides)
    return Directive(**base)


def test_repository_records_and_thin_topics_are_derived_from_the_world():
    prepared = prepare_voice_turn_inputs(world=_world(), participant_message="Who was Jesus?", directive=None)
    assert "fix.witness.who-is-jesus" in prepared.repository_records
    assert prepared.thin_topics == [{"topic": "resurrection"}]


def test_user_message_carries_the_participant_message_with_no_evidence_candidates():
    prepared = prepare_voice_turn_inputs(world=_world(), participant_message="Who was Jesus?", directive=None)
    assert "Who was Jesus?" in prepared.user_message


def test_context_prefix_rides_ahead_of_the_user_message():
    prepared = prepare_voice_turn_inputs(
        world=_world(), participant_message="Who was Jesus?", directive=None,
        context_prefix="Another seat just said: 'We remember him as a teacher.'",
    )
    assert prepared.user_message.startswith("Another seat just said: 'We remember him as a teacher.'")
    assert prepared.user_message.endswith("Who was Jesus?")


def test_turn_directive_is_none_with_no_directive_and_no_table_engagement():
    prepared = prepare_voice_turn_inputs(world=_world(), participant_message="Who was Jesus?", directive=None)
    assert prepared.turn_directive is None


def test_turn_directive_carries_the_directive_s_asks():
    prepared = prepare_voice_turn_inputs(world=_world(), participant_message="Who was Jesus?", directive=_directive())
    assert "who was Jesus" in prepared.turn_directive


def test_correction_is_appended_onto_whatever_the_directive_already_produced():
    prepared = prepare_voice_turn_inputs(
        world=_world(), participant_message="Who was Jesus?", directive=_directive(),
        correction="\n## Correction\nDo not do that again.",
    )
    assert prepared.turn_directive.endswith("\n## Correction\nDo not do that again.")


def test_correction_alone_still_produces_a_turn_directive_with_no_other_directive():
    """The append-not-replace channel _append_seat_identity_correction and
    _append_r27_correction already use for a regeneration's own retry
    directive: correction must still land even when nothing else would
    have produced a turn_directive at all."""
    prepared = prepare_voice_turn_inputs(
        world=_world(), participant_message="Who was Jesus?", directive=None,
        correction="\n## Correction\nDo not do that again.",
    )
    assert prepared.turn_directive == "\n## Correction\nDo not do that again."


def test_figures_already_named_resolves_bridged_figure_ids_to_spoken_names():
    prepared = prepare_voice_turn_inputs(
        world=_world(), participant_message="Who was Jesus?", directive=None,
        already_bridged_figure_ids={"fix.figure.paul"},
    )
    assert prepared.figures_already_named == ["Paul"]


def test_other_tradition_first_ask_always_produces_a_real_directive():
    prepared = prepare_voice_turn_inputs(
        world=_world(), participant_message="What about the Donatists?", directive=None,
        is_other_tradition_first_ask=True,
    )
    assert prepared.turn_directive is not None
    assert "another Christian tradition" in prepared.turn_directive


def test_offered_passages_reach_the_voice_and_the_bound_records_but_not_the_records_search():
    from engine.m4 import passage_offer
    passage = {
        "tag": "fix.passage.abc", "passage_id": "cic:f.xml:a#01", "file": "f.xml", "text": "Concerning the lapsed, the bishop writes of mercy after penance.",
        "word_count": 10, "locus": "73", "role": "own", "work": "Letter 73", "author_name": "Cyprian", "date": None, "voiceable": False,
        "fit": "direct", "rank": 1, "byte_start": 0, "byte_end": 10,
    }
    world = _world(passage_offer={"offer": {"subquestions": {"C1.S1": [passage]}}, "budget": passage_offer.Budget()}, subquestion_routing=True)
    prepared = prepare_voice_turn_inputs(world=world, participant_message="Lapsed penance mercy?", directive=_directive(sub_question="C1.S1"))
    assert "fix.passage.abc" in prepared.repository_records and prepared.repository_records["fix.passage.abc"]["passage_id"] == "cic:f.xml:a#01"
    assert "[[fix.passage.abc]] passage (OUTSIDE OUR VOICE" in prepared.user_message
    assert prepared.offered_ids["passage"] == ["fix.passage.abc"]
    assert "fix.witness.who-is-jesus" in prepared.repository_records


def test_the_length_line_asks_for_succinctness_with_no_word_range():
    from engine.m4.turn_prep import CONCISION_DIRECTIVE
    assert "succinct" in CONCISION_DIRECTIVE
    assert "120" not in CONCISION_DIRECTIVE and "220" not in CONCISION_DIRECTIVE
    assert "fewest sentences" not in CONCISION_DIRECTIVE
    assert "every sentence earns its place" in CONCISION_DIRECTIVE


def test_the_limit_line_states_a_lack_plainly_and_succinctly():
    from engine.m4.turn_prep import LIMIT_LINE
    assert "plainly and succinctly" in LIMIT_LINE and "briefly" not in LIMIT_LINE


def test_the_no_new_figure_line_yields_to_a_person_the_question_or_the_offered_sources_name():
    from engine.m4.turn_prep import NO_NEW_FIGURE_LINE
    assert "visitor's question" in NO_NEW_FIGURE_LINE and "sources offered" in NO_NEW_FIGURE_LINE
