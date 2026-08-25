"""Hermetic tests for evidence.py (Live-Generation Design §3, forks signed
off - LIVE-GENERATION-DESIGN.md §9.5). Synthetic records, same shape/
discipline as test_grounding_net.py's fixtures - no compiled package on
disk required.
"""
from engine.m4.evidence import (
    _fallback_search_text,
    _fulltext_fallback_candidates,
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


# A record whose own retrieval hints name words no canon_question uses -
# the shape that made "What was it like when the plague came?" reach no
# cell at all on a live run while the plague story sat in its coverage.
HINTED = {
    "id": "fix.story.sickness",
    "record_type": "story",
    "canon_cells": ["F1-E"],
    "tellable_as": "The community nursed the dying through the great sickness and many died with them.",
    "retrieval": {"tier": 1, "retrieve_when": ["sickness, death, plague, care for the dying"], "do_not_retrieve_when": []},
}


def test_retrieval_hints_reach_a_cell_the_canon_vocabulary_cannot():
    # Two shared words, because _MIN_ASK_MATCH_WORDS is an absolute floor:
    # a hint contributing one word to a cell the canon vocabulary does not
    # otherwise touch still cannot carry that cell on its own. In the live
    # case the union did the work - the hint supplied "plague" and the
    # cell's own canon text already had "like".
    q = "What was the sickness and the plague like?"
    assert match_asks_to_cells(message=q, asks=None, canon_questions=CANON_QUESTIONS) == []

    matches = match_asks_to_cells(message=q, asks=None, canon_questions=CANON_QUESTIONS, repository_records={"fix.story.sickness": HINTED})
    assert [m["cell"] for m in matches] == ["F1-E"]
    assert matches[0]["from_retrieval_hint"] is True
    assert matches[0]["shared_words"] == ["plague", "sickness"]  # both words came from the record's own hint


def test_retrieval_hints_never_displace_a_cell_the_canon_vocabulary_matched():
    # Scoring both corpora together was the shape that displaced honest
    # canon matches; hints may only fill slots the canon ranking left open.
    q = "What did your community remember of Jesus?"
    before = match_asks_to_cells(message=q, asks=None, canon_questions=CANON_QUESTIONS, top_n=1)
    after = match_asks_to_cells(message=q, asks=None, canon_questions=CANON_QUESTIONS, repository_records={"fix.story.sickness": HINTED}, top_n=1)
    assert before == after
    assert after[0]["cell"] == "C-E"


def test_retrieval_hints_cannot_invent_a_cell_the_fleet_does_not_define():
    stale = {**HINTED, "canon_cells": ["Z9-Q"]}
    matches = match_asks_to_cells(message="What was the sickness and the plague like?", asks=None, canon_questions=CANON_QUESTIONS, repository_records={"x": stale})
    assert matches == []


def test_records_without_retrieval_hints_change_nothing():
    q = "What does your community remember of Jesus?"
    plain = {"fix.witness.jesus": WITNESS, "fix.limit.jesus": LIMIT}
    assert match_asks_to_cells(message=q, asks=None, canon_questions=CANON_QUESTIONS) == match_asks_to_cells(
        message=q, asks=None, canon_questions=CANON_QUESTIONS, repository_records=plain
    )


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


def test_a_morphological_variant_reaches_the_cell_its_root_defines():
    """Measured failure: "persecuted" against a corpus holding
    "persecution" 28 times; "belong" against a hint reading "belonging".
    Stemming is applied to both sides, so it can only add a match."""
    canon = {**CANON_QUESTIONS, "fleet.canon.q4": {
        "id": "fleet.canon.q4", "record_type": "canon_question", "cell": "F1-E",
        "text": "How did the community handle disputes and disagreements about baptism?"}}
    m = match_asks_to_cells(message="Did they dispute and disagree over baptisms?", asks=None, canon_questions=canon)
    assert [x["cell"] for x in m] == ["F1-E"]
    assert m[0]["matched_by"] == "stem"


def test_stemming_never_displaces_a_literal_match():
    before = match_asks_to_cells(message="What does your community remember of Jesus?", asks=None, canon_questions=CANON_QUESTIONS, top_n=1)
    assert before[0]["cell"] == "C-E"
    assert "matched_by" not in before[0]  # the literal tier answered, untouched


def test_the_stemmer_will_not_collapse_short_words():
    from engine.m4.evidence import _stem
    assert _stem("mass") == "mass"      # 4-char floor - never "mas"
    assert _stem("its") == "its"
    assert _stem("persecuted") == "persecut"
    assert _stem("persecution") == "persecut"
    assert _stem("belonging") == "belong"


# ---- Stage A2: full-text fallback (added 2026-08-25) -----------------------
# Fires only when Stage A finds no cell at all - the gap this closes is real
# and was found on a live turn (pahc/Chloe, "what was the kingdom of God"):
# the fleet's own canon vocabulary and every world's own retrieval hints can
# together define a cell vocabulary that a perfectly answerable question
# just never touches, even though a record in the world's own repository
# answers it directly.

_COMMON_WORD_RECORDS = {
    f"fix.common.r{i}": {"id": f"fix.common.r{i}", "record_type": "term", "canon_cells": [], "plain_meaning": f"Record {i} about the everyday word widespread, repeated across this whole fixture set."}
    for i in range(8)
}

FALLBACK_REPOSITORY = {
    "fix.quote.narrow-word": {
        "id": "fix.quote.narrow-word",
        "record_type": "quote",
        "canon_cells": [],
        "text": "The elders spoke often of paradise restored, a word this community used nowhere else in what survives.",
    },
    "fix.term.editorial-only": {
        "id": "fix.term.editorial-only",
        "record_type": "term",
        "canon_cells": [],
        "plain_meaning": "A term about an unrelated household custom.",
        "divergence_note": "Modern scholars call this custom's survival important, though the community itself never said so.",
    },
    **_COMMON_WORD_RECORDS,
}


def test_fulltext_fallback_finds_a_record_no_cell_reaches():
    candidates = _fulltext_fallback_candidates(query_words={"paradise"}, repository_records=FALLBACK_REPOSITORY)
    assert [c["id"] for c in candidates] == ["fix.quote.narrow-word"]
    assert candidates[0]["fulltext_fallback"] is True


def test_fulltext_fallback_drops_a_word_too_common_to_discriminate():
    # "widespread" appears in all 8 _COMMON_WORD_RECORDS entries - well past
    # _FULLTEXT_FALLBACK_MAX_POOL (6). A word that common can't tell one
    # record from another, so it contributes nothing, same as a genuinely
    # off-canon question resolves to no cell today.
    candidates = _fulltext_fallback_candidates(query_words={"widespread"}, repository_records=FALLBACK_REPOSITORY)
    assert candidates == []


def test_fulltext_fallback_mixed_query_drops_only_the_common_word():
    # The exact shape of the live bug: one rare word (finds the record) and
    # one word common enough that alone it would swamp the pool.
    candidates = _fulltext_fallback_candidates(query_words={"paradise", "widespread"}, repository_records=FALLBACK_REPOSITORY)
    assert [c["id"] for c in candidates] == ["fix.quote.narrow-word"]


def test_fulltext_fallback_ignores_editorial_commentary_fields():
    # "important" only appears inside divergence_note - a build-team
    # caveat about the record, not the record's own substance. Matching on
    # it would surface an unrelated household-custom term for a question
    # about importance in general - the exact false positive measured on
    # pahc.term.ministrae before this exclusion existed.
    candidates = _fulltext_fallback_candidates(query_words={"important"}, repository_records=FALLBACK_REPOSITORY)
    assert candidates == []


def test_fallback_search_text_excludes_editorial_keys_all_text_keeps():
    record = FALLBACK_REPOSITORY["fix.term.editorial-only"]
    assert "important" not in _fallback_search_text(record)
    assert "household" in _fallback_search_text(record)  # plain_meaning itself is still searched


def test_assemble_evidence_uses_fallback_only_when_no_cell_matches_at_all():
    evidence = assemble_evidence(
        message="What did they say of paradise?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=FALLBACK_REPOSITORY,
    )
    assert evidence["cells"] == []
    ids = {c["id"] for c in evidence["candidates"]}
    assert "fix.quote.narrow-word" in ids


def test_assemble_evidence_fallback_never_fires_once_a_cell_matches():
    # A real cell match (however thin) must never be topped up by the
    # fallback - Stage A2 is a net under total silence, not an addition to
    # a working match.
    evidence = assemble_evidence(
        message="What does your community remember of Jesus?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
    )
    assert evidence["cells"] != []
    assert all(not c.get("fulltext_fallback") for c in evidence["candidates"])
