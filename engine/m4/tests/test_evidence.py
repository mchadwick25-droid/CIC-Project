"""Hermetic tests for evidence.py (Live-Generation Design §3, forks signed
off - LIVE-GENERATION-DESIGN.md §9.5). Synthetic records, same shape/
discipline as test_grounding_net.py's fixtures - no compiled package on
disk required.
"""
from engine.m4.evidence import (
    apply_session_exclusion,
    assemble_evidence,
    match_asks_to_cells,
    render_evidence_block,
    select_cell_candidates,
    thin_topic_riders,
)

CANON_QUESTIONS = {
    "fleet.canon.q1": {
        "id": "fleet.canon.q1",
        "record_type": "canon_question",
        "cell": "C-E",
        "text": "What did your community actually have about Jesus - writings, memories, people?",
    },
    "fleet.canon.q2": {
        "id": "fleet.canon.q2",
        "record_type": "canon_question",
        "cell": "C-E",
        "text": "How did the community's memory of Jesus reach you across the generations?",
    },
    "fleet.canon.q3": {
        "id": "fleet.canon.q3",
        "record_type": "canon_question",
        "cell": "F1-E",
        "text": "How does baptism actually work for your community - what does it require?",
    },
}

WITNESS = {"id": "fix.witness.jesus", "record_type": "doctrinal_witness", "canon_cells": ["C-E"], "text": "We received the community's own memory of Jesus, handed down, not seen directly."}
LIMIT = {"id": "fix.limit.jesus", "record_type": "honest_limit", "canon_cells": ["C-E"], "statement": "We cannot give you Jesus in his own words, only what the community's memory kept."}
TERM_A = {"id": "fix.term.eucharistia", "record_type": "term", "canon_cells": ["C-E"], "plain_meaning": "The thanksgiving meal of bread and cup, the community's own memory of Jesus made present."}
TERM_B = {"id": "fix.term.baptisma", "record_type": "term", "canon_cells": ["C-E"], "plain_meaning": "The washing that marks entry into the community, unrelated to the meal."}
STORY_A = {"id": "fix.story.first-meal", "record_type": "story", "canon_cells": ["C-E"], "tellable_as": "The community's memory of Jesus at the first meal, kept and retold."}
QUOTE_A = {"id": "fix.quote.remembered", "record_type": "quote", "canon_cells": ["C-E"], "text": "This is the community's own memory of Jesus, kept whole."}
GRAVITY_SCHOOL = {
    "id": "fix.gravity.school",
    "record_type": "gravity",
    "canon_cells": ["C-E"],
    "description": "The community's memory of Jesus was formed through structured teaching.",
    "relations": [{"type": "tension-with", "target": "fix.gravity.household"}],
}
GRAVITY_HOUSEHOLD = {
    "id": "fix.gravity.household",
    "record_type": "gravity",
    "canon_cells": [],
    "description": "The community's memory of Jesus also lived in ordinary households, unschooled.",
    "relations": [{"type": "tension-with", "target": "fix.gravity.school"}],
}

REPOSITORY = {r["id"]: r for r in (WITNESS, LIMIT, TERM_A, TERM_B, STORY_A, QUOTE_A, GRAVITY_SCHOOL, GRAVITY_HOUSEHOLD)}

COVERAGE = {
    "C-E": {
        "doctrinal_witness": ["fix.witness.jesus"],
        "terms": ["fix.term.eucharistia", "fix.term.baptisma"],
        "stories": ["fix.story.first-meal"],
        "quotes": ["fix.quote.remembered"],
        "honest_limit": ["fix.limit.jesus"],
        "gravities": ["fix.gravity.school"],
        "forces": [],
        "contested_claims": [],
    },
    "F1-E": {
        "doctrinal_witness": [], "terms": [], "stories": [], "quotes": [], "honest_limit": [],
        "gravities": [], "forces": [], "contested_claims": [],
    },
}

THIN_TOPICS = [{"keywords": ["ethnicity", "ethnic background"], "note": "the students' own ethnic background is not named in our record"}]


# ---- Stage A ---------------------------------------------------------------


def test_match_asks_to_cells_finds_the_right_cell():
    matches = match_asks_to_cells(message="What does your community remember of Jesus?", asks=None, canon_questions=CANON_QUESTIONS)
    assert matches
    assert matches[0]["cell"] == "C-E"


def test_match_asks_to_cells_off_canon_message_resolves_to_no_cell():
    matches = match_asks_to_cells(message="What is the weather like today?", asks=None, canon_questions=CANON_QUESTIONS)
    assert matches == []


def test_match_asks_to_cells_respects_top_n():
    asks = [{"text": "What did your community have about Jesus, and how does baptism work?"}]
    matches = match_asks_to_cells(message="", asks=asks, canon_questions=CANON_QUESTIONS, top_n=1)
    assert len(matches) <= 1


# ---- Stage B ---------------------------------------------------------------


def test_select_cell_candidates_always_includes_honest_limit():
    selected = select_cell_candidates(cell="C-E", coverage_entry=COVERAGE["C-E"], repository_records=REPOSITORY, message="Jesus", asks=None)
    ids = [c["id"] for c in selected]
    assert "fix.limit.jesus" in ids


def test_select_cell_candidates_ranks_the_more_relevant_term_first():
    selected = select_cell_candidates(
        cell="C-E", coverage_entry=COVERAGE["C-E"], repository_records=REPOSITORY, message="the community's memory of the thanksgiving meal", asks=None
    )
    term_ids = [c["id"] for c in selected if c["record_type"] == "term"]
    assert term_ids[0] == "fix.term.eucharistia"


def test_select_cell_candidates_empty_coverage_entry_returns_only_nothing():
    selected = select_cell_candidates(cell="F1-E", coverage_entry=COVERAGE["F1-E"], repository_records=REPOSITORY, message="baptism", asks=None)
    assert selected == []


def test_select_cell_candidates_head_text_uses_compiler_facing_fields():
    selected = select_cell_candidates(cell="C-E", coverage_entry=COVERAGE["C-E"], repository_records=REPOSITORY, message="Jesus meal", asks=None)
    by_id = {c["id"]: c for c in selected}
    assert by_id["fix.term.eucharistia"]["head"] == TERM_A["plain_meaning"]
    assert by_id["fix.limit.jesus"]["head"] == LIMIT["statement"]


# ---- Stage D ---------------------------------------------------------------


def test_thin_topic_riders_fires_on_message_keyword():
    riders = thin_topic_riders(message="What was the ethnicity of the students?", asks=None, selected=[], thin_topics=THIN_TOPICS)
    assert len(riders) == 1
    assert "ethnicity" in riders[0]["keywords"]


def test_thin_topic_riders_fires_on_selected_candidate_head_text():
    selected = [{"head": "a note about ethnic background left unstated", "id": "x"}]
    riders = thin_topic_riders(message="unrelated", asks=None, selected=selected, thin_topics=THIN_TOPICS)
    assert len(riders) == 1


def test_thin_topic_riders_no_hit_returns_empty():
    riders = thin_topic_riders(message="What is baptism?", asks=None, selected=[], thin_topics=THIN_TOPICS)
    assert riders == []


def test_thin_topic_riders_dedupes_by_note():
    selected = [{"head": "ethnicity mentioned here", "id": "x"}]
    riders = thin_topic_riders(message="ethnicity again", asks=None, selected=selected, thin_topics=THIN_TOPICS)
    assert len(riders) == 1


# ---- Stage E ---------------------------------------------------------------


def test_session_exclusion_annotates_not_drops():
    selected = [{"id": "fix.story.first-meal", "record_type": "story"}, {"id": "fix.term.eucharistia", "record_type": "term"}]
    out = apply_session_exclusion(selected=selected, already_told_ids={"fix.story.first-meal"})
    by_id = {c["id"]: c for c in out}
    assert by_id["fix.story.first-meal"]["already_told_this_session"] is True
    assert "already_told_this_session" not in by_id["fix.term.eucharistia"]
    assert len(out) == 2  # never dropped


def test_session_exclusion_no_told_ids_is_a_no_op():
    selected = [{"id": "fix.story.first-meal", "record_type": "story"}]
    assert apply_session_exclusion(selected=selected, already_told_ids=None) == selected


# ---- Full pipeline / Stage C integration -----------------------------------


def test_assemble_evidence_pulls_in_tension_partner_via_scope_completion():
    evidence = assemble_evidence(
        message="What does your community remember of Jesus through its teaching?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
    )
    ids = {c["id"] for c in evidence["candidates"]}
    assert "fix.gravity.school" in ids
    # the untensioned household side is never selected by Stage B (it has
    # no canon_cells membership) - only scope_completion's tension walk
    # can pull it in, which is the whole point of this test.
    household = next(c for c in evidence["candidates"] if c["id"] == "fix.gravity.household")
    assert household["scope_completion"] is True


def test_assemble_evidence_no_cell_still_returns_empty_but_valid_shape():
    evidence = assemble_evidence(
        message="What's the weather like?", asks=None, canon_questions=CANON_QUESTIONS, coverage=COVERAGE, repository_records=REPOSITORY
    )
    assert evidence == {"cells": [], "candidates": [], "thin_ground": []}


def test_assemble_evidence_wires_thin_ground_end_to_end():
    evidence = assemble_evidence(
        message="What was the ethnicity of the community?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
        thin_topics=THIN_TOPICS,
    )
    assert len(evidence["thin_ground"]) == 1


def test_assemble_evidence_deduplicates_ids_across_cells():
    # A pathological coverage map where two matched cells share a record -
    # assemble_evidence must never emit the same id twice.
    shared_coverage = {
        "C-E": COVERAGE["C-E"],
        "F1-E": {**COVERAGE["F1-E"], "terms": ["fix.term.eucharistia"]},
    }
    asks = [{"text": "What did your community have about Jesus, and how does baptism work?"}]
    evidence = assemble_evidence(message="", asks=asks, canon_questions=CANON_QUESTIONS, coverage=shared_coverage, repository_records=REPOSITORY, top_n_cells=2)
    ids = [c["id"] for c in evidence["candidates"]]
    assert len(ids) == len(set(ids))


# ---- Rendering --------------------------------------------------------------


def test_render_evidence_block_uses_citation_ready_ids():
    evidence = assemble_evidence(
        message="What does your community remember of Jesus?", asks=None, canon_questions=CANON_QUESTIONS, coverage=COVERAGE, repository_records=REPOSITORY
    )
    block = render_evidence_block(evidence)
    assert "[[fix.witness.jesus]]" in block or "[[fix.limit.jesus]]" in block
    assert block.startswith("## Ground for this turn")


def test_render_evidence_block_marks_already_told_and_scope_completion():
    evidence = assemble_evidence(
        message="What does your community remember of Jesus through its teaching?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
        already_told_ids={"fix.story.first-meal"},
    )
    block = render_evidence_block(evidence)
    assert "already told this session" in block
    assert "scope completion" in block


def test_render_evidence_block_includes_thin_ground_line():
    evidence = {"candidates": [], "cells": [], "thin_ground": THIN_TOPICS}
    block = render_evidence_block(evidence)
    assert "THIN GROUND" in block
    assert "ethnicity" in block
