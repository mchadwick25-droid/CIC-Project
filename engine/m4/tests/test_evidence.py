"""Hermetic tests for evidence.py (Live-Generation Design §3, forks signed
off - LIVE-GENERATION-DESIGN.md §9.5). Synthetic records, same shape/
discipline as test_grounding_net.py's fixtures - no compiled package on
disk required.
"""
from engine.m4.evidence import (
    _fallback_search_text,
    _looks_like_follow_up,
    _word_weights,
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


# ---- Stage B2 (Build-Plan.md Stage 4c, part 2) -----------------------------


def test_retrieval_fill_only_fires_when_the_coverage_list_is_wholly_empty():
    """F1-E's own coverage entry lists zero terms at all - a structural
    absence, not a low score - so Stage B2 widens the search to the whole
    repository and finds fix.term.baptisma by shared words alone, even
    though that record's own canon_cells never names F1-E."""
    selected = select_cell_candidates(
        cell="F1-E", coverage_entry=COVERAGE["F1-E"], repository_records=REPOSITORY,
        message="the washing that marks entry", asks=None,
    )
    by_id = {c["id"]: c for c in selected}
    assert "fix.term.baptisma" in by_id
    assert by_id["fix.term.baptisma"]["retrieval_fill"] is True


def test_retrieval_fill_never_fires_for_a_type_the_coverage_list_already_has():
    """C-E's own coverage entry already lists both terms - Stage B's own
    coverage-seeded ranking is the whole answer for that slot, and Stage B2
    must never widen an already-served slot."""
    selected = select_cell_candidates(
        cell="C-E", coverage_entry=COVERAGE["C-E"], repository_records=REPOSITORY,
        message="the community's memory of the thanksgiving meal", asks=None,
    )
    terms = [c for c in selected if c["record_type"] == "term"]
    assert terms
    assert all("retrieval_fill" not in t for t in terms)


def test_retrieval_fill_never_touches_honest_limit():
    """honest_limit is never a key in _TYPE_FLOORS - a wholly empty
    coverage_entry["honest_limit"] must stay empty, never widened to the
    whole repository the way an ordinary type is (see the module comment
    on why that type is unconditional and cell-scoped only)."""
    selected = select_cell_candidates(
        cell="F1-E", coverage_entry=COVERAGE["F1-E"], repository_records=REPOSITORY,
        message="Jesus", asks=None,
    )
    assert not [c for c in selected if c["record_type"] == "honest_limit"]


def test_retrieval_fill_never_fires_on_an_off_canon_query():
    """A query sharing no words with anything in the repository must not
    force a fill just because the slot is empty - Stage B2 only ever adds
    real, matched evidence, the same "report only what was found"
    discipline as the fulltext fallback one stage up."""
    selected = select_cell_candidates(
        cell="F1-E", coverage_entry=COVERAGE["F1-E"], repository_records=REPOSITORY,
        message="What is the weather like today?", asks=None,
    )
    assert selected == []


_FILL_REPOSITORY = {
    **REPOSITORY,
    **{
        f"fix.term.extra-{i}": {
            "id": f"fix.term.extra-{i}",
            "record_type": "term",
            "canon_cells": ["Z9-Q"],
            "plain_meaning": f"An unrelated washing-themed entry, variant {i}, for the fleet's own washing rite.",
        }
        for i in range(1, 5)
    },
}


def test_retrieval_fill_is_capped_at_the_type_own_floor():
    """Five term records in the repository share the query's words
    (baptisma plus four synthetic extras), but the term floor is 3 - Stage
    B2 fills the identical slot count Stage B itself would, never more."""
    selected = select_cell_candidates(
        cell="F1-E", coverage_entry=COVERAGE["F1-E"], repository_records=_FILL_REPOSITORY,
        message="washing entry", asks=None,
    )
    terms = [c for c in selected if c["record_type"] == "term"]
    assert len(terms) == 3
    assert all(c.get("retrieval_fill") for c in terms)


def test_assemble_evidence_signature_is_unchanged_by_stage_b2():
    """Build-Plan.md Stage 4c's own Done criterion: assemble_evidence's
    signature stays unchanged - Stage B2 is entirely internal to
    select_cell_candidates, reading nothing assemble_evidence's own callers
    don't already pass it (repository_records alone)."""
    evidence = assemble_evidence(
        message="How does baptism actually work for your community, the washing that marks entry?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
    )
    ids = [c["id"] for c in evidence["candidates"]]
    assert "fix.term.baptisma" in ids


# ---- Stage 4d: tier prior (Build-Plan.md) ----------------------------------

# Identical plain_meaning on both records ties their raw overlap score
# exactly - any ordering difference below can only come from the tier
# prior. Ids are deliberately chosen so the LOW-tier record would win the
# tie-break's own alphabetical fallback ("aaa" < "zzz") if the prior did
# nothing - isolating the prior's effect from that incidental fallback.
_TIER_HIGH = {
    "id": "fix.term.zzz-high-tier", "record_type": "term", "canon_cells": ["Z9-Q"],
    "plain_meaning": "The community remembers something old kept safe.",
    "retrieval": {"tier": 1},
}
_TIER_LOW = {
    "id": "fix.term.aaa-low-tier", "record_type": "term", "canon_cells": ["Z9-Q"],
    "plain_meaning": "The community remembers something old kept safe.",
}
_TIER_QUERY = "the community remembers something old kept safe"
_TIER_COVERAGE_ENTRY = {
    "doctrinal_witness": [], "terms": ["fix.term.zzz-high-tier", "fix.term.aaa-low-tier"],
    "stories": [], "quotes": [], "honest_limit": [], "gravities": [], "forces": [], "contested_claims": [],
}
_TIER_REPOSITORY = {r["id"]: r for r in (_TIER_HIGH, _TIER_LOW)}


def test_tier_prior_breaks_a_genuine_tie_toward_the_lower_tier_number():
    selected = select_cell_candidates(
        cell="Z9-Q", coverage_entry=_TIER_COVERAGE_ENTRY, repository_records=_TIER_REPOSITORY,
        message=_TIER_QUERY, asks=None,
    )
    terms = [c["id"] for c in selected if c["record_type"] == "term"]
    assert terms == ["fix.term.zzz-high-tier", "fix.term.aaa-low-tier"]


def test_tier_prior_never_overrides_a_clearly_stronger_content_match():
    """A tier-1 record with weak overlap must not outrank an untiered
    record with strong overlap - the prior is bounded well under any
    meaningful score gap (see _TIER_PRIOR's own comment)."""
    strong_untiered = {
        "id": "fix.term.strong-match", "record_type": "term", "canon_cells": ["Z9-Q"],
        "plain_meaning": "The community remembers something old kept safe.",
    }
    weak_tier_one = {
        "id": "fix.term.weak-but-tier-one", "record_type": "term", "canon_cells": ["Z9-Q"],
        "plain_meaning": "A short note about something else.",
        "retrieval": {"tier": 1},
    }
    repo = {r["id"]: r for r in (strong_untiered, weak_tier_one)}
    coverage_entry = {**_TIER_COVERAGE_ENTRY, "terms": [strong_untiered["id"], weak_tier_one["id"]]}
    selected = select_cell_candidates(
        cell="Z9-Q", coverage_entry=coverage_entry, repository_records=repo,
        message=_TIER_QUERY, asks=None,
    )
    terms = [c["id"] for c in selected if c["record_type"] == "term"]
    assert terms[0] == "fix.term.strong-match"


def test_tier_prior_also_applies_inside_the_stage_b2_fill():
    """The same lean, in the same direction, when Stage B2's whole-world
    scan is what's doing the ranking (an empty coverage slot) - one prior,
    not two independently-tuned copies."""
    empty_coverage = {
        "doctrinal_witness": [], "terms": [], "stories": [], "quotes": [],
        "honest_limit": [], "gravities": [], "forces": [], "contested_claims": [],
    }
    selected = select_cell_candidates(
        cell="Z9-Q", coverage_entry=empty_coverage, repository_records=_TIER_REPOSITORY,
        message=_TIER_QUERY, asks=None,
    )
    terms = [c["id"] for c in selected if c["record_type"] == "term"]
    assert terms[0] == "fix.term.zzz-high-tier"
    assert all(c.get("retrieval_fill") for c in selected if c["record_type"] == "term")


def test_tier_3_and_unset_tier_are_treated_identically():
    tier_three = {**_TIER_LOW, "id": "fix.term.explicit-tier-three", "retrieval": {"tier": 3}}
    repo = {_TIER_LOW["id"]: _TIER_LOW, tier_three["id"]: tier_three}
    coverage_entry = {**_TIER_COVERAGE_ENTRY, "terms": [_TIER_LOW["id"], tier_three["id"]]}
    selected = select_cell_candidates(
        cell="Z9-Q", coverage_entry=coverage_entry, repository_records=repo,
        message=_TIER_QUERY, asks=None,
    )
    scores = {c["id"]: c["score"] for c in selected if c["record_type"] == "term"}
    assert scores["fix.term.aaa-low-tier"] == scores["fix.term.explicit-tier-three"]


# ---- Stage 4f: secondary-weight table context (Build-Plan.md) -------------


def test_secondary_context_fills_an_empty_cell_slot():
    """An off-canon message alone reaches no cell; the table's own recent
    speech (what another voice just said) can still find one, at secondary
    weight - exactly the "conversation-aware" gap this stage closes."""
    evidence_result = assemble_evidence(
        message="What is the weather like today?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
        secondary_context="How does baptism actually work for your community - what does it require?",
    )
    cells = [c["cell"] for c in evidence_result["cells"]]
    assert "F1-E" in cells
    matched = next(c for c in evidence_result["cells"] if c["cell"] == "F1-E")
    assert matched.get("from_secondary_context") is True


def test_secondary_context_never_displaces_a_real_match():
    """A message that already fills every top_n_cells slot on its own is
    left exactly as it was - secondary_context only ever fills a gap, never
    competes for a slot the participant's own words already won."""
    q = "What does your community remember of Jesus?"
    without = match_asks_to_cells(message=q, asks=None, canon_questions=CANON_QUESTIONS, top_n=1)
    evidence_result = assemble_evidence(
        message=q, asks=None, canon_questions=CANON_QUESTIONS, coverage=COVERAGE,
        repository_records=REPOSITORY, top_n_cells=1,
        secondary_context="How does baptism actually work for your community - what does it require?",
    )
    assert evidence_result["cells"] == without
    assert all("from_secondary_context" not in c for c in evidence_result["cells"])


def test_secondary_context_respects_the_top_n_cells_cap():
    evidence_result = assemble_evidence(
        message="What is the weather like today?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
        top_n_cells=2,
        secondary_context="How does baptism actually work for your community, and what does your community remember of Jesus?",
    )
    assert len(evidence_result["cells"]) <= 2


def test_secondary_context_absent_is_byte_identical_to_before_this_stage():
    q = "What does your community remember of Jesus?"
    with_default = assemble_evidence(message=q, asks=None, canon_questions=CANON_QUESTIONS, coverage=COVERAGE, repository_records=REPOSITORY)
    without_param = assemble_evidence(
        message=q, asks=None, canon_questions=CANON_QUESTIONS, coverage=COVERAGE, repository_records=REPOSITORY, secondary_context=None,
    )
    assert with_default == without_param


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
    assert evidence == {"cells": [], "candidates": [], "thin_ground": [], "figures_already_named": []}


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


def test_render_evidence_block_says_its_ground_is_not_already_said():
    """The header frames THIS channel; nothing frames the replayed history
    (engine.api.wiring._replay_text, which re-attaches [[id]] tags to past
    turns on purpose). Without this clause a record read here for the first
    time can be reported to the participant as already given - measured on
    desert, "Sarah, whose words we already gave you", two turns after a
    conversation that had not mentioned her."""
    evidence = {"candidates": [], "cells": [], "thin_ground": []}
    block = render_evidence_block(evidence)
    assert "Available, not already said" in block
    assert "the conversation above" in block


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


def test_render_evidence_block_names_figures_already_introduced():
    """A pilot read found both Chloe turns opened "One of us,
    Ignatius" - the session's already_bridged_figure_ids suppressed the
    UI's second underline but never reached the voice. The evidence block
    is where the voice learns session state (same channel Stage E's
    already-told annotation uses), so the caller-resolved names render
    there; no names, no line."""
    evidence = assemble_evidence(
        message="What does your community remember of Jesus?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
        figures_already_named=["Ignatius", "Justin"],
    )
    assert evidence["figures_already_named"] == ["Ignatius", "Justin"]
    block = render_evidence_block(evidence)
    assert "## Already introduced: Ignatius, Justin." in block

    bare = assemble_evidence(
        message="What does your community remember of Jesus?",
        asks=None,
        canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE,
        repository_records=REPOSITORY,
    )
    assert bare["figures_already_named"] == []
    assert "Already introduced" not in render_evidence_block(bare)


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


# ---- entity routing (Stage A, added 2026-08-27) -------------------------
# Fixture shaped from the measured failure it exists for: a world whose
# figure is named in the question but whose name is in no canon question,
# so every content-word tier is blind to it.
ENTITY_CANON = {
    **CANON_QUESTIONS,
    "fleet.canon.q-f1e-rule": {
        "id": "fleet.canon.q-f1e-rule",
        "record_type": "canon_question",
        "cell": "F1-E",
        "text": "Who held authority among you, and how did anyone come to have it?",
    },
}
ENTITY_FIGURE = {
    "id": "fix.figure.pachomius",
    "record_type": "figure",
    "canon_cells": ["F1-E"],
    "names": [{"name": "Pachomius", "tag": "in-world"}, {"name": "Pachomius of Tabennesi (c. 292-346)", "tag": "scholarly"}],
}
ENTITY_QUOTE = {
    "id": "fix.quote.the-rule",
    "record_type": "quote",
    "canon_cells": ["F1-E"],
    "text": "Suffer each one to eat and to drink, as Pachomius was commanded.",
    "license": "verbatim",
}
ENTITY_REPOSITORY = {r["id"]: r for r in (WITNESS, LIMIT, TERM_A, ENTITY_FIGURE, ENTITY_QUOTE)}
ENTITY_COVERAGE = {**COVERAGE, "F1-E": {"quotes": ["fix.quote.the-rule"], "terms": [], "stories": [], "doctrinal_witness": [], "gravities": [], "forces": [], "contested_claims": []}}


def test_entity_routing_reaches_a_cell_no_content_word_tier_would():
    matches = match_asks_to_cells(
        message="Is there anything Pachomius himself actually put in writing?",
        asks=None,
        canon_questions=ENTITY_CANON,
        repository_records=ENTITY_REPOSITORY,
    )
    entity = [m for m in matches if m.get("from_entity")]
    assert entity, "a named figure must reach the cell its own world discusses it in"
    assert entity[0]["cell"] == "F1-E"
    assert entity[0]["from_entity"] == "pachomius"


def test_entity_routing_adds_a_slot_and_never_displaces_a_content_word_match():
    # The whole safety argument: entity routing widens the ground, so a
    # cell an honest literal match found must still be there afterwards.
    without = match_asks_to_cells(
        message="What did your community actually have about Jesus?",
        asks=None, canon_questions=ENTITY_CANON, repository_records=None,
    )
    with_entity = match_asks_to_cells(
        message="What did your community actually have about Jesus, and about Pachomius?",
        asks=None, canon_questions=ENTITY_CANON, repository_records=ENTITY_REPOSITORY,
    )
    kept = {m["cell"] for m in with_entity if not m.get("from_entity")}
    assert {m["cell"] for m in without} <= kept


def test_entity_routing_ignores_a_name_the_canon_already_carries():
    # A token already in canon vocabulary routes through cell_keywords; a
    # second path for it would only let the entity tier duplicate - and
    # potentially outrank - the honest match it is copying.
    figure = {**ENTITY_FIGURE, "id": "fix.figure.jesus", "names": [{"name": "Jesus", "tag": "in-world"}]}
    repo = {**ENTITY_REPOSITORY, figure["id"]: figure}
    matches = match_asks_to_cells(
        message="Tell me about Jesus.", asks=None, canon_questions=ENTITY_CANON, repository_records=repo,
    )
    assert not [m for m in matches if m.get("from_entity") == "jesus"]


def test_fallback_still_fires_when_the_only_match_is_an_entity_match():
    # Regression guard: an entity match is a weaker signal than a canon or
    # hint match - it knows the question is ABOUT someone, not what is
    # asked - so it must not suppress the Stage A2 net the way a real cell
    # match does. Measured on pahc: "Who was Papias?" fell from three
    # records to one when entity routing first landed.
    repo = {**FALLBACK_REPOSITORY, ENTITY_FIGURE["id"]: ENTITY_FIGURE}
    evidence = assemble_evidence(
        message="What did Pachomius say of paradise?",
        asks=None,
        canon_questions=ENTITY_CANON,
        coverage=ENTITY_COVERAGE,
        repository_records=repo,
    )
    assert all(m.get("from_entity") for m in evidence["cells"])
    assert any(c.get("fulltext_fallback") for c in evidence["candidates"])


def test_retrieve_when_is_not_searched_by_the_fulltext_fallback():
    # Regression guard, from the day 124 quote records were hinted at once.
    # A hint is retrieval vocabulary in the PARTICIPANT'S words - exactly
    # what this fallback matches on - so counting it inflates document
    # frequency until an honestly-discriminating word crosses the pool cap
    # and stops discriminating. Measured on pahc: "believe" matched 4
    # records and reached ground; after hinting it matched 7, went over the
    # cap, and "How did you know what to believe?" returned nothing.
    record = {
        "id": "fix.quote.hinted",
        "record_type": "quote",
        "text": "A saying about bread.",
        "retrieval": {"tier": 2, "retrieve_when": ["participant asks what they believed about anything at all"]},
    }
    searched = _fallback_search_text(record)
    assert "bread" in searched
    assert "believed" not in searched


# ---- short-query single-word tier (added 2026-08-27) --------------------
SHORT_CANON = {
    **CANON_QUESTIONS,
    "fleet.canon.q-marriage": {
        "id": "fleet.canon.q-marriage", "record_type": "canon_question", "cell": "F1-E",
        "text": "What did marriage mean to your people - did you have weddings?",
    },
}


def test_short_query_may_match_on_one_discriminating_canon_word():
    # "What did you think of marriage?" has two content words and shares
    # exactly one with exactly the right cell. Requiring two is requiring
    # the impossible.
    matches = match_asks_to_cells(
        message="What did you think of marriage?", asks=None,
        canon_questions=SHORT_CANON, repository_records=None,
    )
    assert [m["cell"] for m in matches if m.get("matched_by") == "single-word"] == ["F1-E"]


def test_long_query_still_needs_two_shared_words():
    # The relaxation is for short queries only. A lone shared word among
    # many is the noise the two-word floor exists to reject.
    matches = match_asks_to_cells(
        message="I have been wondering lately about weddings and whether anyone here bothered with marriage at all",
        asks=None, canon_questions=SHORT_CANON, repository_records=None,
    )
    assert not [m for m in matches if m.get("matched_by") == "single-word"]


def test_short_query_will_not_match_on_a_word_spread_across_cells():
    # Measured: "Do you like pizza?" reached two cells on `like`, which is
    # in seven of the fleet's 28 canon cells and picks a cell by coin-toss.
    spread = {
        f"fleet.canon.spread{i}": {
            "id": f"fleet.canon.spread{i}", "record_type": "canon_question", "cell": cell,
            "text": "Did you like the way things were done?",
        }
        for i, cell in enumerate(["C-E", "F1-E", "C-I", "F2-I"])
    }
    matches = match_asks_to_cells(
        message="Do you like pizza?", asks=None,
        canon_questions={**CANON_QUESTIONS, **spread}, repository_records=None,
    )
    assert not [m for m in matches if m.get("matched_by") == "single-word"]


def test_single_word_tier_never_displaces_a_stronger_match():
    # Ordering is this tier's whole safety. Measured on ijc: run before the
    # hint tier, a 0.5 single-word canon match took a slot ahead of a 1.0
    # two-word hint match and pushed out the cell that actually answered
    # the question. A turn already reaching cells must be unchanged.
    msg = "What did your community actually have about Jesus - writings, memories, people?"
    before = match_asks_to_cells(message=msg, asks=None, canon_questions=CANON_QUESTIONS, repository_records=None)
    after = match_asks_to_cells(message=msg, asks=None, canon_questions=SHORT_CANON, repository_records=None)
    assert [m["cell"] for m in before] == [m["cell"] for m in after]


def test_one_word_query_may_match_a_hint_word_but_a_two_word_query_may_not():
    # A one-word query's single content word IS the subject - there is no
    # other word for it to be the framing of, and no vocabulary at all can
    # give it a second shared word. A two-word query is the case where the
    # matched word may be the framing verb while the real subject is
    # unknown to every cell ("Can you write me some code?").
    repo = {
        "fix.term.hinted": {
            "id": "fix.term.hinted", "record_type": "term", "canon_cells": ["F1-E"],
            "plain_meaning": "Washing at initiation.",
            "retrieval": {"tier": 2, "retrieve_when": ["participant asks whether you baptise babies"]},
        }
    }
    one = match_asks_to_cells(message="Who could be baptise?", asks=None,
                             canon_questions=CANON_QUESTIONS, repository_records=repo)
    assert [m["cell"] for m in one if m.get("matched_by") == "single-word-hint"] == ["F1-E"]

    two = match_asks_to_cells(message="Discuss baptise please", asks=None,
                              canon_questions=CANON_QUESTIONS, repository_records=repo)
    assert not [m for m in two if m.get("matched_by") == "single-word-hint"]

# --- cell-scorer weighting (the broad-cell defect, 2026-08-27) ---------------

def test_a_word_in_many_cells_is_discounted_but_never_silenced():
    """The taper's shape, pinned. A word in few cells is full evidence; one
    spread across many is worth less but still counts, because silencing it
    would delete the denominator protection that keeps an off-canon message
    at no cell."""
    w = _word_weights(
        {"rare", "borderline", "common", "everywhere", "unknown"},
        {"rare": 1, "borderline": 4, "common": 8, "everywhere": 28, "unknown": 0},
    )
    assert w["rare"] == 1.0
    assert w["borderline"] == 1.0          # at the threshold, still full evidence
    assert 0.25 < w["common"] < 1.0        # discounted
    assert w["everywhere"] == 0.25         # floored, not zero
    assert w["unknown"] == 1.0             # in no cell: cannot be shared, only widens the denominator


def test_a_broad_cell_does_not_shut_out_a_specific_one_on_common_words():
    """The measured defect this weighting exists for. BROAD shares three
    words with the query but two of them sit in every cell; NARROW shares
    two words that occur nowhere else. Under the old flat overlap
    coefficient BROAD won on count alone and NARROW never reached Stage B,
    because only the top-scoring cells survive. FILLER exists to give the
    common words somewhere else to live, which is what makes them common."""
    canon = {
        "q.broad": {"record_type": "canon_question", "cell": "F6-P",
                    "text": "people believe someone happened among community"},
        "q.narrow": {"record_type": "canon_question", "cell": "F1-P",
                     "text": "quintessence perambulation"},
    }
    for i, cell in enumerate(["C-I", "C-E", "C-P", "C-T", "F2-I", "F2-E", "F3-I", "F3-P"]):
        canon[f"q.filler{i}"] = {"record_type": "canon_question", "cell": cell,
                                 "text": "people believe someone happened among community"}
    message = "people believe someone quintessence perambulation"
    cells = [m["cell"] for m in match_asks_to_cells(
        message=message, asks=[{"order": 1, "text": message}], canon_questions=canon)]
    assert "F1-P" in cells, cells


# --- follow-ups inherit the prior subject's cells (2026-08-27) --------------

def test_a_question_that_names_its_own_subject_is_not_a_follow_up():
    """The half of the test that stops this firing on real questions: 33 of
    the 93 canon questions contain `that`, `this` or `it`, and every one of
    them still names what it is asking about."""
    assert not _looks_like_follow_up(
        "What did your community actually have about Jesus - writings, memories, people?",
        None, CANON_QUESTIONS, None)


def test_a_back_reference_with_no_subject_is_a_follow_up():
    assert _looks_like_follow_up("Why did that matter?", None, CANON_QUESTIONS, None)
    assert _looks_like_follow_up("Say more about that.", None, CANON_QUESTIONS, None)


def test_a_bare_request_with_no_back_reference_is_not_a_follow_up():
    """`Tell me more.` is a follow-up to a human and not to this test - it
    carries no marker, so it is deliberately out of scope rather than
    caught by a looser rule that would also catch real questions."""
    assert not _looks_like_follow_up("Tell me more.", None, CANON_QUESTIONS, None)


def test_a_follow_up_inherits_the_prior_turn_cells():
    history = [
        {"role": "user", "content": "What did your community actually have about Jesus - writings, memories, people?"},
        {"role": "assistant", "content": "What we had reached us through people who had known him."},
    ]
    out = assemble_evidence(
        message="Why did that matter?", asks=None, canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE, repository_records=REPOSITORY, history=history)
    assert out["cells"], "a follow-up with history should reach a cell"
    assert all(c.get("inherited_from_prior_turn") for c in out["cells"]), out["cells"]
    assert out["cells"][0]["cell"] == "C-E"


def test_history_never_changes_a_turn_that_names_its_own_subject():
    """The safety property: only follow-ups consult history at all, so every
    ordinary turn is bit-for-bit what it was before this existed."""
    message = "What did your community actually have about Jesus - writings, memories, people?"
    history = [{"role": "user", "content": "How did your people fast?"},
               {"role": "assistant", "content": "We fasted."}]
    kw = dict(message=message, asks=None, canon_questions=CANON_QUESTIONS,
              coverage=COVERAGE, repository_records=REPOSITORY)
    assert assemble_evidence(**kw) == assemble_evidence(**kw, history=history)


def test_a_first_turn_has_no_history_to_inherit_from():
    out = assemble_evidence(
        message="Why did that matter?", asks=None, canon_questions=CANON_QUESTIONS,
        coverage=COVERAGE, repository_records=REPOSITORY, history=[])
    assert not any(c.get("inherited_from_prior_turn") for c in out["cells"])


def test_diverse_take_breadth_first_by_source():
    """Source breadth is a system function of
    selection, never a per-record hand-fix. Same slot count; composition
    prefers one-per-source-family before seconds from the same family."""
    from engine.m4.evidence import _diverse_take, _source_key
    repo = {
        "w.quote.a1": {"id": "w.quote.a1", "sources": [{"source_id": "w.source.ignatius"}]},
        "w.quote.a2": {"id": "w.quote.a2", "sources": [{"source_id": "w.source.ignatius"}]},
        "w.quote.b1": {"id": "w.quote.b1", "sources": [{"source_id": "w.source.pliny"}]},
    }
    scored = [("w.quote.a1", 0.9), ("w.quote.a2", 0.8), ("w.quote.b1", 0.5)]
    # floor 2: best ignatius + best pliny, not two ignatius
    assert _diverse_take(scored, repo, 2) == [("w.quote.a1", 0.9), ("w.quote.b1", 0.5)]
    # floor 3: the second ignatius comes back in the fill pass
    assert _diverse_take(scored, repo, 3) == [("w.quote.a1", 0.9), ("w.quote.b1", 0.5), ("w.quote.a2", 0.8)]
    # single-family cell: identical to plain top-N
    mono = [("w.quote.a1", 0.9), ("w.quote.a2", 0.8)]
    assert _diverse_take(mono, repo, 2) == mono
    # sourceless record is its own family, never crowded out
    assert _source_key({"id": "w.limit.x", "sources": []}) == "w.limit.x"


def test_diverse_take_downgrades_session_used_families():
    """A reference already drawn on this session
    is looked to LAST, never banned - Ignatius yields the first slot to a
    fresh family once he has spoken, and still fills slots nothing else can."""
    from engine.m4.evidence import _diverse_take
    repo = {
        "w.quote.ign1": {"id": "w.quote.ign1", "sources": [{"source_id": "w.source.ignatius"}]},
        "w.quote.ign2": {"id": "w.quote.ign2", "sources": [{"source_id": "w.source.ignatius"}]},
        "w.quote.pliny": {"id": "w.quote.pliny", "sources": [{"source_id": "w.source.pliny"}]},
        "w.quote.justin": {"id": "w.quote.justin", "sources": [{"source_id": "w.source.justin"}]},
    }
    scored = [("w.quote.ign1", 0.9), ("w.quote.pliny", 0.6), ("w.quote.justin", 0.5), ("w.quote.ign2", 0.4)]
    # nothing used yet: breadth-first as before, Ignatius leads on score
    assert _diverse_take(scored, repo, 2) == [("w.quote.ign1", 0.9), ("w.quote.pliny", 0.6)]
    # Ignatius already drawn on this session: fresh families first, Ignatius after
    used = {"w.source.ignatius"}
    assert _diverse_take(scored, repo, 3, used) == [
        ("w.quote.pliny", 0.6), ("w.quote.justin", 0.5), ("w.quote.ign1", 0.9)]
    # when only Ignatius qualifies, he still fills the slots - downgraded, not banned
    only_ign = [("w.quote.ign1", 0.9), ("w.quote.ign2", 0.4)]
    assert _diverse_take(only_ign, repo, 2, used) == only_ign
