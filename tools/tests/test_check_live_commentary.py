"""Unit tests for tools/check_live_commentary.py's classification rules,
plus the precision/recall measurement over a 60-hit hand-labelled sample
(Step 1 PR A's own requirement) drawn from the real repo.

The hand-labelled sample (TestHandLabelledSample) pins (path, line,
expected_category) against the actual files on disk. If one of those
lines moves or its surrounding text changes enough to flip a real
classification, this test is the thing that is supposed to notice -
failing it means re-checking the sample against the file at that path,
not loosening the assertion.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools import check_live_commentary as clc

REPO = Path(__file__).resolve().parents[2]


def _hits_for(text: str, tmp_path: Path, rel: str) -> list[clc.Hit]:
    path = tmp_path / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    # scan_file needs `path.relative_to(repo)`, so treat tmp_path as the repo root.
    return clc.scan_file(tmp_path, path, "engine")


# ---------------------------------------------------------------------------
# PROTECTED
# ---------------------------------------------------------------------------

def test_vendored_texts_fully_excluded():
    # cic/texts/ isn't one of SURFACES' scanned roots at all (only
    # cic/engine and cic/corpus-map are) - a real scan never walks into
    # it. is_protected still marks it PROTECTED as defense in depth, for
    # any path reaching scan_file() directly (as this test does).
    assert not any(root.startswith("cic/texts") for roots in clc.SURFACES.values() for root in roots)
    hit = clc.Hit("engine", "cic/texts/foo.txt", 1, "", [], "")
    assert clc.is_protected(Path(hit.path), hit.line, set())


def test_seeded_defects_file_fully_protected(tmp_path):
    text = 'note: "per Mark\'s standing quote ruling, RULED 2026-08-21, R26"\n'
    hits = _hits_for(text, tmp_path, "fixtures/seeded_defects.yaml")
    assert len(hits) == 1
    assert hits[0].category == "PROTECTED"


def test_review_doc_under_worlds_protected_both_conventions(tmp_path):
    text = "Round 1 review Finding S5: per Mark, R26\n"
    dedicated = _hits_for(text, tmp_path, "Build/worlds/alx/Review-Artifacts/Doc02_Round1_Review.md")
    loose = _hits_for(text, tmp_path, "Build/worlds/gallic/gallic_Doc02_Review_Round1.md")
    assert dedicated[0].category == "PROTECTED"
    assert loose[0].category == "PROTECTED"


def test_construction_doc_under_worlds_not_protected(tmp_path):
    text = "Per Mark's ruling, R26, this section covers gravity discovery.\n"
    hits = _hits_for(text, tmp_path, "Build/worlds/alx/Doc_04_Gravity_Discovery.md")
    assert hits[0].category != "PROTECTED"


# ---------------------------------------------------------------------------
# Doc_0[1-9] construction-doc review-status exemption
# (_doc_construction_protected_lines / _is_doc_construction_file)
# ---------------------------------------------------------------------------

def test_doc_construction_header_field_protected(tmp_path):
    text = (
        "# Doc_07 -- Integrated Ecology Analysis\n"
        "## Some World\n"
        "\n"
        "**Status:** Round 1 review complete; Round 2 bounded spot-check complete\n"
        "**Produced at:** Construction Step 7, per Mark, 2026-07-27\n"
        "\n"
        "---\n"
        "\n"
        "## 1. Body\n"
        "Per Mark's ruling, R26, this is ordinary body text.\n"
    )
    hits = _hits_for(text, tmp_path, "Build/worlds/alx/Doc_07_Integrated_Ecology_Analysis.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line[4] == "PROTECTED"  # **Status:**
    assert by_line[5] == "PROTECTED"  # **Produced at:**
    assert by_line[10] != "PROTECTED"  # ordinary body text, well past the header


def test_doc_construction_header_narrative_lead_not_protected(tmp_path):
    # A bold lead that reads as a full sentence (an apostrophe, in this
    # case) rather than a short field name is real header disclosure
    # prose, not metadata - it must stay flagged like any other narrative,
    # even though it sits in the same header block as genuine fields.
    text = (
        "# Doc_04 -- Gravity Discovery\n"
        "## Some World\n"
        "\n"
        "**Status:** Approved to proceed, per Mark, R26\n"
        "**Per Mark's own ruling, R26, this candidate is Supporting:** decided directly.\n"
        "\n"
        "---\n"
    )
    hits = _hits_for(text, tmp_path, "Build/worlds/don/Doc_04_Gravity_Discovery.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line[4] == "PROTECTED"
    assert by_line[5] != "PROTECTED"


def test_doc_construction_open_items_and_handoff_variants_protected(tmp_path):
    # Two of the real, surveyed heading variants - "Handoff and Open
    # Items" (don) and a separate "Document Log" immediately after it
    # (the actual gallic Doc_07 shape) - each start their own run.
    text = (
        "# Doc_03 -- Lexicon Candidate List\n"
        "## Some World\n"
        "\n"
        "**Status:** Approved to proceed\n"
        "\n"
        "---\n"
        "\n"
        "## 1. Candidates\n"
        "Per Mark's ruling, R26, candidate X is included.\n"
        "\n"
        "## 6. Handoff and Open Items\n"
        "Per Mark's ruling, R26, this is carried to Doc_04.\n"
        "\n"
        "## 7. Document Log\n"
        "Round 1 review (Opus, 2026-07-20): per Mark, R26.\n"
        "\n"
        "## 8. Appendix\n"
        "Per Mark's ruling, R26, an appendix note outside the tail block.\n"
    )
    hits = _hits_for(text, tmp_path, "Build/worlds/rzg/Doc_03_Lexicon_Candidate_List.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line[9] != "PROTECTED"  # "## 1. Candidates" body - ordinary
    assert by_line[12] == "PROTECTED"  # inside "Handoff and Open Items"
    assert by_line[15] == "PROTECTED"  # inside "Document Log"
    assert by_line[18] != "PROTECTED"  # past both, back to ordinary body


def test_doc_construction_no_tail_heading_leaves_nothing_protected(tmp_path):
    # lpc's Doc_08 and syr's Doc_09 shape: no "Open Items"/"Handoff"/
    # "Document Log"/"Disposition" heading anywhere - nothing to protect,
    # and nothing should be swept.
    text = (
        "# Doc_08 -- Forces Document\n"
        "## Some World\n"
        "\n"
        "**Status:** Approved to proceed, per Mark, R26\n"
        "\n"
        "---\n"
        "\n"
        "## 1. Forces\n"
        "Per Mark's ruling, R26, this is a force finding.\n"
    )
    hits = _hits_for(text, tmp_path, "Build/worlds/lpc/Doc_08_Forces_Document.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line[4] == "PROTECTED"  # the header field is still protected
    assert by_line[9] != "PROTECTED"  # no tail heading exists to protect this


def test_doc_construction_world_prefixed_filename_not_covered(tmp_path):
    # A real, surveyed exception: a world-prefixed filename
    # (hal_Doc_01_..., gallic_Doc07_..., witt_Doc_01_...,
    # cappadocian_Doc_01_...) is not the bare Doc_0[1-9]_*.md convention
    # this exemption matches, and is deliberately left uncovered rather
    # than guessed at.
    text = "**Status:** Approved to proceed, per Mark, R26\n"
    hits = _hits_for(text, tmp_path, "Build/worlds/hal/hal_Doc_01_World_Identification_Boundaries_Orientation.md")
    assert hits[0].category != "PROTECTED"


def test_world_build_dir_protected(tmp_path):
    text = "RULED 2026-09-01 per Mark\n"
    hits = _hits_for(text, tmp_path, "Build/worlds/rzg/build/bar-screen-2026-09-19.json")
    assert hits[0].category == "PROTECTED"


def test_gaps_ledger_protected(tmp_path):
    text = "Entry 42 (subject: X, 2026-09-01): per Mark's ruling R26\n"
    hits = _hits_for(text, tmp_path, "Build/worlds/don/Open_Gaps_Tracking.md")
    assert hits[0].category == "PROTECTED"


def test_worlds_registry_log_protected(tmp_path):
    text = "Mark's ruling, R26, RULED 2026-09-01: take it back to when it was working\n"
    hits = _hits_for(text, tmp_path, "records/WORLDS_REGISTRY_LOG.md")
    assert hits[0].category == "PROTECTED"


def test_engine_reports_protected(tmp_path):
    text = '"rights_status": "public domain, per Mark, 2026-08-27, R26"\n'
    hits = _hits_for(text, tmp_path, "engine/m4/reports/live-table-battery-2026-09-22.json")
    assert hits[0].category == "PROTECTED"


def test_donatism_historical_pages_protected(tmp_path):
    text = "The verdict went against them at Carthage in 411.\n"
    for rel in ("cic-website/tree/donatism.html", "cic-website/traditions/donatism.html"):
        hits = _hits_for("RULED 2026-09-01 per Mark\n" + text, tmp_path, rel)
        assert hits[0].category == "PROTECTED"


def test_record_provenance_fields_protected(tmp_path):
    record = (
        "---\n"
        "id: alx.source.example\n"
        "record_type: source\n"
        "discovery_channel: \"requested 2026-08-20, per Mark's own ruling R26\"\n"
        "author: Origen\n"
        "status: draft\n"
        "---\n"
        "body text, not protected: per Mark's ruling R26\n"
    )
    hits = _hits_for(record, tmp_path, "records/alx/source/alx.source.example.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line[4] == "PROTECTED"  # discovery_channel
    assert 8 in by_line and by_line[8] != "PROTECTED"  # free body text


def test_quote_text_field_protected_but_modern_rendering_field_always_is(tmp_path):
    quote = (
        "---\n"
        "id: alx.quote.example\n"
        "record_type: quote\n"
        "text: \"archaic wording per Mark 2026-08-20\"\n"
        "modern_rendering: \"plain wording per Mark 2026-08-20\"\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(quote, tmp_path, "records/alx/quote/alx.quote.example.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line[4] == "PROTECTED"
    assert by_line[5] == "PROTECTED"


def test_modern_rendering_protected_outside_quote_records_too(tmp_path):
    record = (
        "---\n"
        "id: alx.term.example\n"
        "record_type: term\n"
        "modern_rendering: \"per Mark 2026-08-20\"\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(record, tmp_path, "records/alx/term/alx.term.example.md")
    assert hits[0].category == "PROTECTED"


# ---------------------------------------------------------------------------
# ROUTE / REWRITE / KEEP
# ---------------------------------------------------------------------------

def test_open_gap_cue_routes(tmp_path):
    text = "TODO: this citation is not yet resolved, per Mark\n"
    hits = _hits_for(text, tmp_path, "engine/m1/gates.py")
    assert hits[0].category == "ROUTE"


def test_ruling_wrapped_reason_rewrites(tmp_path):
    text = "# Skip retry above 3 attempts (R26, per Mark's ruling, RULED 2026-08-21)\n"
    hits = _hits_for(text, tmp_path, "engine/m4/turn.py")
    assert hits[0].category == "REWRITE"


def test_bare_yaml_date_scalar_keeps(tmp_path):
    hits = _hits_for("sealed_at: '2026-08-20'\n", tmp_path, "canon/sealed_probes/seals.yaml")
    assert hits[0].category == "KEEP"


def test_bare_markdown_header_date_keeps(tmp_path):
    # Path deliberately does NOT match Doc_0[1-9]_*.md (see
    # test_doc_construction_header_field_protected below for that case) -
    # this test isolates the plain _BARE_DATE_HEADER_LINE KEEP rule on its
    # own, on a worlds/ file the new construction-doc exemption ignores.
    hits = _hits_for("**Date drafted:** 2026-07-20\n", tmp_path, "Build/worlds/alx/World_Profile.md")
    assert hits[0].category == "KEEP"


def test_structured_waiver_deadline_kwarg_keeps(tmp_path):
    text = '    "m9:shelf-row/desert": Waiver(count=1, deadline="2026-12-14", owner="desert thread"),\n'
    hits = _hits_for(text, tmp_path, "engine/m9/enforce.py")
    assert hits[0].category == "KEEP"


def test_non_review_round_keeps(tmp_path):
    hits = _hits_for("Retries use a round-trip budget of three attempts.\n", tmp_path, "engine/m4/turn.py")
    assert hits == [] or hits[0].category == "KEEP"


def test_iso_date_inside_prose_rewrites(tmp_path):
    text = "This behavior changed in the 2026-08-21 handoff; the new script reads REPO_ROOT directly.\n"
    hits = _hits_for(text, tmp_path, "cic/engine/texts_registry.py")
    assert hits[0].category == "REWRITE"


# ---------------------------------------------------------------------------
# Checker refinements (2026-09-24, checker-refinements PR)
# ---------------------------------------------------------------------------

def test_plain_prose_open_item_routes_with_no_other_pattern(tmp_path):
    # Real failure mode: cic/corpus-map entries naming an open item in plain
    # prose, with no ruling number, date, or other PATTERNS hit on the line
    # at all - before the ROUTE_CUES root-cause fix, scan_file's own
    # `if not matched: continue` meant these were silently skipped rather
    # than routed.
    text = "Whether this source counts as native is worth reconsidering.\n"
    hits = _hits_for(text, tmp_path, "cic/corpus-map/witt.map.md")
    assert len(hits) == 1
    assert hits[0].category == "ROUTE"


def test_flagged_for_mark_and_needing_a_ruling_route(tmp_path):
    for text in (
        "This attribution is flagged for Mark.\n",
        "The tradition boundary here is needing a ruling.\n",
        "This cross-check has not yet been done for the second edition.\n",
    ):
        hits = _hits_for(text, tmp_path, "cic/corpus-map/witt.map.md")
        assert hits and hits[0].category == "ROUTE", text


def test_era_gate_freeze_narration_rewrites(tmp_path):
    # cic-website/data/world-census.json's own "at the Freeze"/"at the gate"
    # construction - previously invisible (no ruling number, no date, no
    # other PATTERNS hit).
    text = '"statusDescription": "Its start was corrected at the gate from 330 to 451."\n'
    hits = _hits_for(text, tmp_path, "cic-website/data/world-census.json")
    assert hits[0].category == "REWRITE"
    assert "era-gate" in hits[0].patterns


def test_era_frozen_status_phrase_not_flagged_as_era_gate(tmp_path):
    # The legitimate current-status phrasing the era-gate pattern must not
    # catch: "era frozen" is not "at the ... Freeze/gate".
    text = '"stepStatus": "Step 0 run complete - era frozen"\n'
    hits = _hits_for(text, tmp_path, "cic-website/data/world-census.json")
    assert not any("era-gate" in h.patterns for h in hits)


def test_generic_reviewer_keeps(tmp_path):
    # cic-website/support.html:127 and Build/reference/Project-Reference/
    # CiC_Cleaning_Pattern_Log.md's own real KEEP examples: a generic or
    # hypothetical third-party reviewer, not this project's own review
    # process.
    for text in (
        "If you know a scholar who might serve as an external reviewer, introduce us.\n",
        "A reviewer checking only for names would still miss this.\n",
    ):
        hits = _hits_for(text, tmp_path, "cic-website/support.html")
        assert hits == [] or hits[0].category == "KEEP", text


def test_named_project_reviewer_still_rewrites(tmp_path):
    # The carve-out must not blanket-suppress a genuine provenance mention.
    text = "Per Mark's ruling, the reviewer's own note (R26, 2026-08-21) still applies.\n"
    hits = _hits_for(text, tmp_path, "engine/m4/turn.py")
    assert hits[0].category == "REWRITE"


def test_source_registry_row_id_keeps(tmp_path):
    for text in (
        "Doc_09 witt-S07; Source Registry R45.\n",
        "Named absence; vol. IV carries R48 and R61. (Source Registry row 62; Confidence B.)\n",
        "the Iserloh row (R76) is cited but not read.\n",
    ):
        hits = _hits_for(text, tmp_path, "records/witt/story/witt.story.example.md")
        assert hits == [] or hits[0].category == "KEEP", text


def test_source_registry_row_id_inside_source_record_body_keeps(tmp_path):
    record = (
        "---\n"
        "id: witt.source.example\n"
        "record_type: source\n"
        "status: ready\n"
        "---\n"
        "Named absence; vol. IV carries R48 and R61.\n"
    )
    hits = _hits_for(record, tmp_path, "records/witt/source/witt.source.example.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line.get(6, "KEEP") == "KEEP"


def test_ruling_number_outside_source_registry_context_still_rewrites(tmp_path):
    # The carve-out is scoped to Source Registry/row context and source
    # record bodies - a bare ruling number elsewhere in a story record's
    # body still rewrites.
    text = "Per Mark's ruling R26, this scene stays as narrated.\n"
    hits = _hits_for(text, tmp_path, "records/witt/story/witt.story.example.md")
    assert hits[0].category == "REWRITE"


def test_change_history_cue_widens_to_whole_paragraph(tmp_path):
    # records/witt/voice_craft/witt.voice.craft.md's own real shape: a
    # CORRECTION paragraph whose other sentences cite process artifacts in
    # shapes no PATTERNS entry catches on its own (a bare "OG-15" gap ID,
    # a "Doc_10" single-digit citation).
    text = (
        "CORRECTION (go-live adversarial review, Round 1 re-confirmation pass):\n"
        "the first fix gave the guard field a real instruction, but that\n"
        "instruction was itself factually inaccurate (Doc_10; OG-15).\n"
        "The library is not silent on 1525; it holds real content.\n"
        "\n"
        "A fully unrelated paragraph after a blank line.\n"
    )
    hits = _hits_for(text, tmp_path, "records/witt/voice_craft/witt.voice.craft.md")
    by_line = {h.line: h.category for h in hits}
    assert by_line.get(1) == "REWRITE"
    assert by_line.get(2) == "REWRITE"  # no PATTERNS hit of its own
    assert by_line.get(3) == "REWRITE"  # "OG-15"/"Doc_10" match nothing on their own
    assert by_line.get(4) == "REWRITE"
    assert 6 not in by_line  # the next paragraph is untouched


def test_change_history_cue_in_yaml_frontmatter_does_not_flood_siblings(tmp_path):
    # Real bug (records/lpc/source/lpc.source.hartel-cyprian-opera-omnia-
    # csel3-standing-reference.md): front matter has no blank lines between
    # sibling top-level keys at all, so the ordinary paragraph-based
    # widening used to sweep every unrelated field (id, world_id,
    # schema_version, sources, ...) into the same flagged block. A cue
    # inside one field's own value must widen only to that field's own
    # lines, never past the next top-level key.
    text = (
        "---\n"
        "id: fix.source.example\n"
        "world_id: fixture-world\n"
        "record_type: source\n"
        "schema_version: 2\n"
        "status: draft\n"
        "note: >-\n"
        "  CORRECTION (cold adversarial review, 2026-08-31): this note\n"
        "  previously said the wrong edition was vendored.\n"
        "sources: []\n"
        "relations: []\n"
        "---\n"
        "Body text after front matter.\n"
    )
    hits = _hits_for(text, tmp_path, "records/fix/source/fix.source.example.md")
    by_line = {h.line: h for h in hits}
    # Only the `note:` field's own lines (its key line, 7, plus its two
    # continuation lines, 8-9) carry the flood tag - every sibling key
    # (id, world_id, record_type, schema_version, status, sources,
    # relations) stays untouched.
    assert set(by_line) == {7, 8, 9}
    assert by_line[7].category == "REWRITE"
    assert by_line[8].category == "REWRITE"
    assert by_line[9].category == "REWRITE"
    assert "change-history-cue" in by_line[8].patterns
    assert "change-history-block" in by_line[7].patterns
    assert "change-history-block" in by_line[9].patterns


def test_change_history_cue_yaml_multiline_scalar_stays_widened_together(tmp_path):
    # A genuine multi-line scalar value (its continuation lines are
    # indented, never matching the top-level-key shape, so they never act
    # as a sibling-key boundary) must still widen as one unit - the cue on
    # one line pulls in the rest of the same field's prose, not just its
    # own line.
    text = (
        "---\n"
        "id: fix.dw.example\n"
        "record_type: doctrinal_witness\n"
        "divergence_note: >-\n"
        "  The record originally misdated this event by a year.\n"
        "  CORRECTION (cold adversarial review, 2026-08-31): the correct\n"
        "  year, verified directly against the source, is given below.\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(text, tmp_path, "records/fix/doctrinal_witness/fix.dw.example.md")
    by_line = {h.line: h for h in hits}
    # Lines 4-7 (the `divergence_note:` key line plus its three
    # continuation lines) all get swept together as one scalar block; the
    # sibling `id`/`record_type`/`status` lines (2, 3, 8) do not.
    assert set(by_line) == {4, 5, 6, 7}
    assert by_line[6].category == "REWRITE"
    assert "change-history-cue" in by_line[6].patterns
    assert "change-history-block" in by_line[4].patterns
    assert "change-history-block" in by_line[5].patterns
    assert "change-history-block" in by_line[7].patterns


def test_change_history_cue_case_sensitivity(tmp_path):
    # CORRECTION/BLOCKING stay case-sensitive (all-caps only), same
    # reasoning as the existing "ruled" pattern - ordinary lowercase
    # engineering prose must not be swept in.
    text = "A correction to one's wording is exactly the kind of change that can happen.\n"
    hits = _hits_for(text, tmp_path, "engine/m1/gates.py")
    assert hits == [] or hits[0].category == "KEEP"


# ---------------------------------------------------------------------------
# Spoken-field grading/provenance vocabulary (SPOKEN_VOCAB_PATTERNS)
# ---------------------------------------------------------------------------

def _world_core_record(thinness: str) -> str:
    return (
        "---\n"
        "id: rzg.core.example\n"
        "record_type: world_core\n"
        f"thinness: '{thinness}'\n"
        "status: draft\n"
        "---\n"
    )


def test_spoken_field_grading_vocab_rewrites(tmp_path):
    # The real rzg.core.the-reformed-cities-zurich-and-geneva.md sentence
    # this pattern set was written to catch.
    text = _world_core_record(
        "rests on Confidence D/E, unacquired evidence (Source_Registry.md row 13) "
        "- the general doctrine is Documented, but the vivid detail is not."
    )
    hits = _hits_for(text, tmp_path, "records/rzg/world_core/rzg.core.example.md")
    by_line = {h.line: h for h in hits}
    hit = by_line[4]
    assert hit.category == "REWRITE"
    assert {"confidence-grade", "source-registry-ref", "confidence-predicate"} <= set(hit.patterns)


def test_doc_and_section_ref_in_spoken_field_rewrites(tmp_path):
    text = _world_core_record("as Doc_04 SS3.4 and Doc_08 SS2C both note, evidence is thin here.")
    hits = _hits_for(text, tmp_path, "records/rzg/world_core/rzg.core.example.md")
    assert hits[0].category == "REWRITE"
    assert "doc-ref" in hits[0].patterns
    assert "section-ref" in hits[0].patterns


def test_grading_vocab_outside_a_spoken_field_not_flagged_by_new_patterns(tmp_path):
    # `sources` isn't a declared SPOKEN_FIELDS entry for world_core - a
    # Doc_04/Confidence mention there is untouched by SPOKEN_VOCAB_PATTERNS
    # (it may still be flagged by the ordinary global PATTERNS, which is a
    # separate, pre-existing concern this test doesn't assert on).
    text = (
        "---\n"
        "id: rzg.core.example\n"
        "record_type: world_core\n"
        "sources: []\n"
        "notes_field_not_declared_spoken: 'Confidence B per Doc_04 SS2'\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(text, tmp_path, "records/rzg/world_core/rzg.core.example.md")
    # Not a declared spoken field, and none of these words trip the global
    # PATTERNS on their own - no hit at all, not just an unflagged one.
    assert hits == []


def test_honest_limit_and_contested_claim_excluded_from_spoken_vocab_patterns(tmp_path):
    text = (
        "---\n"
        "id: rzg.limit.example\n"
        "record_type: honest_limit\n"
        "statement: 'Doc_02 SS6 states this directly (Source_Registry.md row 17); "
        "the general claim is Documented at Confidence B.'\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(text, tmp_path, "records/rzg/honest_limit/rzg.limit.example.md")
    # honest_limit is excluded from SPOKEN_VOCAB_PATTERNS entirely, and
    # none of these words trip the global PATTERNS on their own.
    assert hits == []


def test_formation_confidence_field_itself_stays_protected(tmp_path):
    record = (
        "---\n"
        "id: rzg.core.example\n"
        "record_type: world_core\n"
        "confidence:\n"
        "  citation_specificity: B\n"
        "  formation_confidence: Documented\n"
        "thinness: 'plain statement, no leaked vocabulary here'\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(record, tmp_path, "records/rzg/world_core/rzg.core.example.md")
    # formation_confidence's own value never matches "is Documented" (no
    # "is" word present) or any other SPOKEN_VOCAB_PATTERNS - confirms the
    # field needs no special-case matching, only stays out of the way.
    assert hits == []


# ---------------------------------------------------------------------------
# Widened SPOKEN_VOCAB_PATTERNS (2026-09-25, Mark's ruling: "yes, widen the
# fleet checks" - see the owning Decision-Log). True positives are drawn
# from real, still-unfixed fleet text (git-visible on main at the time this
# test was written); true negatives are drawn from real clean fields on
# main, chosen specifically because they use the same everyday words
# ("formation", "primary", "supporting") the new patterns must not trip on.
# ---------------------------------------------------------------------------

_NEW_SPOKEN_VOCAB_KEYS = {
    "six-test-vocabulary", "cross-check-label", "gravity-classification-label",
    "all-caps-section-header", "matrix-cell-code", "build-history-language",
}


def _new_pattern_hits(path: str):
    surface = next((s for s, roots in clc.SURFACES.items() if any(path.startswith(r + "/") for r in roots)), "records")
    hits = clc.scan_file(REPO, REPO / path, surface)
    return [h for h in hits if set(h.patterns) & _NEW_SPOKEN_VOCAB_KEYS]


def _gravity_record(name: str, description: str) -> str:
    return (
        "---\n"
        "id: fix.gravity.example\n"
        "record_type: gravity\n"
        f"name: {name}\n"
        f"description: '{description}'\n"
        "status: draft\n"
        "---\n"
    )


def test_six_test_name_with_colon_rewrites(tmp_path):
    # Real shape from don.gravity.rebaptism-boundary-marking.md: each of
    # the six tests named as its own labelled clause.
    text = _gravity_record(
        "Rebaptism as Boundary-Marking Practice",
        "Repetition: attested across multiple independent sources. Dependency: membership "
        "status depends on it directly.",
    )
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    by_line = {h.line: h for h in hits}
    assert "six-test-vocabulary" in by_line[5].patterns
    assert by_line[5].category == "REWRITE"


def test_six_test_name_lowercase_with_test_word_rewrites(tmp_path):
    # Real shape from desert.gravity.koinonia.md: lowercase test names in a
    # list, but "the Persistence test" (capitalised, literal word "test"
    # right after) is what actually trips the pattern.
    text = _gravity_record(
        "Koinonia",
        "Strong within the corpus on every test - repetition, dependency, formation, "
        "explanatory power - but fails the Persistence test outright.",
    )
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "six-test-vocabulary" in hits[0].patterns
    assert hits[0].category == "REWRITE"


def test_pass_fail_grading_rewrites(tmp_path):
    text = _gravity_record(
        "Example Gravity",
        "Doc_04 SS3.2: PRIMARY, 6/6 tests PASS (strong). Repetition PASS; Interaction PASS.",
    )
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "six-test-vocabulary" in hits[0].patterns


def test_author_gravity_risk_rewrites(tmp_path):
    # Real phrase from don.gravity.church-of-the-martyrs.md.
    text = _gravity_record(
        "Church of the Martyrs",
        "the least Author-Gravity-encumbered Primary in this world. AUTHOR-GRAVITY RISK "
        "FLAGGED AT GENERATION: Low.",
    )
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "six-test-vocabulary" in hits[0].patterns


def test_cross_check_label_rewrites(tmp_path):
    text = _gravity_record("Example", "No Confidence/Gravity Cross-Check divergence - agrees throughout.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "cross-check-label" in hits[0].patterns


def test_bracketed_classification_tag_in_name_field_rewrites(tmp_path):
    # Real, fleet-wide shape (confirmed live on alx/hal, the fleet's own
    # exemplar worlds, not just un-re-voiced ones): engine/m4/
    # citation_cards.py's own _short_name already strips this tag before a
    # citation card shows it, but engine/m2/builders.py build_prompt()'s
    # own Gravities-list line (`g.get('name')`) does not - the raw tag
    # reaches the model's own prompt context unstripped every turn.
    text = _gravity_record("Divine Pedagogy [SUPPORTING - explanatory framework]", "plain description text here.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    by_line = {h.line: h for h in hits}
    assert "gravity-classification-label" in by_line[4].patterns


def test_confirmed_primary_classification_rewrites(tmp_path):
    text = _gravity_record("Example", "Confirmed PRIMARY (Doc_04 SS3.3, SS4), the strongest candidate.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "gravity-classification-label" in hits[0].patterns


def test_supporting_rather_than_primary_rewrites(tmp_path):
    text = _gravity_record("Example", "Dependency revealing Supporting rather than Primary status.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "gravity-classification-label" in hits[0].patterns


def test_tier_number_rewrites(tmp_path):
    text = _gravity_record("Example", "Built from Doc_06 entry 23 (Tier 2), a later hagiographic source.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "gravity-classification-label" in hits[0].patterns


def test_layer_headers_rewrite(tmp_path):
    # Real shape from don.force.sustained-purity-rebaptism-practice.md.
    text = (
        "---\n"
        "id: fix.force.example\n"
        "record_type: force\n"
        "name: Example Force\n"
        "description: >-\n"
        "  LAYER 1 -- HISTORICAL EVENT: the purity doctrine operated as follows.\n"
        "  LAYER 2 -- THE WORLD'S OWN EXPERIENCE: to belong here was to have been washed again.\n"
        "  LAYER 3 -- FORMATION IMPACT: this is central to the world's own life.\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(text, tmp_path, "records/fix/force/fix.force.example.md")
    layer_lines = [h for h in hits if "all-caps-section-header" in h.patterns]
    assert len(layer_lines) == 3


def test_cross_cell_connection_rewrites(tmp_path):
    text = (
        "---\n"
        "id: fix.force.example\n"
        "record_type: force\n"
        "name: Example Force\n"
        "description: >-\n"
        "  CROSS-CELL CONNECTION (Doc_08 Section 4, Connection 2): reinforces the parallel force.\n"
        "status: draft\n"
        "---\n"
    )
    hits = _hits_for(text, tmp_path, "records/fix/force/fix.force.example.md")
    assert any("all-caps-section-header" in h.patterns for h in hits)


def test_matrix_cell_code_rewrites(tmp_path):
    # Real shape from don.force.sustained-purity-rebaptism-practice.md and
    # don.force.caecilianist-victory-selects-survivors.md.
    for text_body in ("Doc_08 Cell 2B, Force 2B-1.", "Doc_08 Cell 3B, Force 3B-2, the transmission dimension."):
        text = _gravity_record("Example Gravity", text_body).replace("record_type: gravity", "record_type: force")
        hits = _hits_for(text, tmp_path, "records/fix/force/fix.force.example.md")
        assert any("matrix-cell-code" in h.patterns for h in hits), text_body


def test_bracketed_matrix_cell_code_rewrites(tmp_path):
    text = _gravity_record("Example Force", "operates as [2B - ongoing/internal] throughout the window.").replace(
        "record_type: gravity", "record_type: force"
    )
    hits = _hits_for(text, tmp_path, "records/fix/force/fix.force.example.md")
    assert any("matrix-cell-code" in h.patterns for h in hits)


def test_build_history_language_rewrites(tmp_path):
    text = _gravity_record(
        "Example", "Finding S4 from this build's own review process revised the original assessment."
    )
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "build-history-language" in hits[0].patterns


# --- Recall additions (2026-09-25, review round 2) ----------------------

def test_six_of_six_and_all_six_tests_rewrite(tmp_path):
    for body in ("Six of six PASS (strong to very strong), the clergy dying in office.",
                 "Strong on all six tests, this candidate clears the bar easily."):
        text = _gravity_record("Example", body)
        hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
        assert "six-test-vocabulary" in hits[0].patterns, body


def test_grading_adjective_before_name_without_on_rewrites(tmp_path):
    # Real shape reported in review: an adjective directly before the test
    # name, no "on"/"for" between them.
    text = _gravity_record("Example", "the link is moderate Dependency; indirect Formation is also present.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "six-test-vocabulary" in hits[0].patterns


def test_is_with_relational_phrase_rewrites(tmp_path):
    text = _gravity_record("Example", "its Interaction is with the household-catechism gravity, reinforcing it.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "six-test-vocabulary" in hits[0].patterns


def test_all_caps_test_name_with_dash_pass_rewrites(tmp_path):
    # Real shape from don.gravity.church-of-the-martyrs.md: "REPETITION -
    # PASS (very strong): ...".
    text = _gravity_record("Example", "REPETITION - PASS (very strong): the sources name it directly.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "six-test-vocabulary" in hits[0].patterns


def test_explanatory_alone_without_power_rewrites(tmp_path):
    # Real shape from cappadocian.gravity.martyrs-land.md: "Explanatory"
    # used bare, the "Power" half dropped.
    text = _gravity_record("Example", "strong on Repetition; MODERATE on Dependency and Explanatory.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "six-test-vocabulary" in hits[0].patterns


def test_parenthetical_gravity_number_rewrites(tmp_path):
    # Real shape from desert.gravity.koinonia.md: "(gravity 3)".
    text = _gravity_record(
        "Example", "Stands as one pole of the authority-tension gravity (10) against the elder-mediated model (gravity 3)."
    )
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "gravity-classification-label" in hits[0].patterns


def test_strand_label_rewrites(tmp_path):
    # Real shape from desert.gravity.koinonia.md / pahc's own force
    # descriptions: "Strand A", "Strand A-B" as a source-pool label.
    text = _gravity_record("Example", "no equivalent exists in Strand A or C, though Strand A-B shows overlap.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "matrix-cell-code" in hits[0].patterns


# --- Precision fixes (2026-09-25, review round 2) ------------------------

def test_formation_tests_the_soul_ordinary_verb_not_flagged(tmp_path):
    # Real false positive named in review: "tests" as an ordinary plural
    # verb (Formation is the subject), not the singular noun "test"
    # following a label.
    text = _gravity_record("Example", "Formation tests the soul and shapes the will over a lifetime.")
    hits = _new_pattern_hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert hits == []


def test_lowercase_interaction_test_not_flagged(tmp_path):
    # Real false positive named in review: an unrelated, lowercase
    # "interaction test" (e.g. a statistics term), not a capitalised
    # Doc_04 label.
    text = _gravity_record("Example", "A statistician ran the interaction test on the dataset twice.")
    hits = _new_pattern_hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert hits == []


def test_earlier_version_of_a_historical_text_not_flagged(tmp_path):
    # Real false positive named in review: source-critical talk about a
    # historical text's own earlier version is legitimate emic content,
    # not build-history narration about this record.
    text = _gravity_record("Example", "An earlier version of the story says the well ran dry that summer.")
    hits = _new_pattern_hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert hits == []


def test_earlier_version_of_this_record_still_rewrites(tmp_path):
    # The narrowed pattern must still catch the genuine build-history
    # shape it was written for: self-reference to THIS record/field.
    text = _gravity_record("Example", "An earlier version of this record scored FK grade 14, since fixed.")
    hits = _hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert "build-history-language" in hits[0].patterns


# --- True negatives: ordinary English on the same vocabulary -----------

def test_ordinary_formation_usage_not_flagged(tmp_path):
    # Real sentence from pahc's own (clean) world_core.formation_logic:
    # "Formation" capitalised only because it is sentence-initial, not a
    # test-battery label.
    text = (
        "---\n"
        "id: fix.core.example\n"
        "record_type: world_core\n"
        "formation_logic: 'Household- and correspondence-based pastoral formation. Formation "
        "here never resolves into one settled office.'\n"
        "status: draft\n"
        "---\n"
    )
    hits = _new_pattern_hits_for(text, tmp_path, "records/fix/world_core/fix.core.example.md")
    assert hits == []


def test_ordinary_primary_and_supporting_prose_not_flagged(tmp_path):
    text = _gravity_record(
        "Example",
        "This was the primary reason households stayed connected, and letters were written in "
        "support of that claim.",
    )
    hits = _new_pattern_hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert hits == []


def test_numbered_editorial_caution_labels_not_flagged(tmp_path):
    # Real shape from pahc.core.house-church.md's own `cautions` field -
    # this world's own invented organizing labels, not a copied
    # build-template header. The generic "2+ capitalised words" rule this
    # test guards against was tried and dropped for exactly this false
    # positive.
    text = (
        "---\n"
        "id: fix.core.example\n"
        "record_type: world_core\n"
        "cautions: '1) THE IGNATIUS CONCENTRATION governs every use here. 2) STRAND DISCIPLINE: "
        "both patterns held, neither wrong.'\n"
        "status: draft\n"
        "---\n"
    )
    hits = _new_pattern_hits_for(text, tmp_path, "records/fix/world_core/fix.core.example.md")
    assert hits == []


def test_ordinary_cross_check_verb_not_flagged(tmp_path):
    text = _gravity_record("Example", "A reader should cross check this claim against the primary sources.")
    hits = _new_pattern_hits_for(text, tmp_path, "records/fix/gravity/fix.gravity.example.md")
    assert hits == []


def _new_pattern_hits_for(text: str, tmp_path: Path, rel: str):
    hits = _hits_for(text, tmp_path, rel)
    return [h for h in hits if set(h.patterns) & _NEW_SPOKEN_VOCAB_KEYS]


def test_real_fleet_true_positives_still_match_on_main():
    # Confirms the patterns fire against real, currently-unfixed files on
    # disk (not just synthetic examples). don.force.sustained-purity-
    # rebaptism-practice.md's own hit (the original third example here)
    # was cleared by don's #551 re-voicing PR after this test was written -
    # exactly the intended outcome, not a false positive - so it was
    # swapped for cappadocian's own matrix-cell-code example, a fleet-wide
    # leak (the bracketed build-taxonomy tag on every gravity/force `name`)
    # not yet remediated in any world.
    assert _new_pattern_hits("records/don/gravity/don.gravity.rebaptism-boundary-marking.md")
    assert _new_pattern_hits("records/desert/gravity/desert.gravity.koinonia.md")
    assert _new_pattern_hits("records/cappadocian/force/cappadocian.force.ascetic-ferment.md")


def test_real_editorial_numbered_labels_not_flagged_as_headers():
    # pahc.core.house-church.md's own `cautions` field numbers its points
    # with invented editorial labels ("1) THE IGNATIUS CONCENTRATION
    # governs...", "3) DATING HUMILITY: ...") - never a copied
    # build-template header, so all-caps-section-header must stay clean
    # on it specifically (the same field is legitimately flagged by
    # matrix-cell-code, on this world's own real "Strand A" usage
    # elsewhere in the same field - a different, correct finding, not
    # this test's concern).
    hits = _new_pattern_hits("records/pahc/world_core/pahc.core.house-church.md")
    assert not any("all-caps-section-header" in h.patterns for h in hits)


# ---------------------------------------------------------------------------
# Hand-labelled sample: precision/recall (PR A's own required measurement)
# ---------------------------------------------------------------------------

# (surface, path, line, expected_category) - 60 hits, stratified across
# every scanned surface, drawn from a fixed random sample (seed 20260924)
# of the real repo's flagged lines at the time this test was written, then
# hand-read and labelled against their actual context (see the PR body for
# the file this table backs and its measured precision/recall).
HAND_LABELS: list[tuple[str, int, str]] = [
    ("canon/sealed_probes/seals.yaml", 136, "KEEP"),
    ("canon/sealed_probes/seals.yaml", 41, "KEEP"),
    ("canon/sealed_probes/seals.yaml", 86, "KEEP"),
    ("canon/sealed_probes/seals.yaml", 106, "KEEP"),
    ("canon/sealed_probes/seals.yaml", 21, "KEEP"),
    ("canon/sealed_probes/seals.yaml", 146, "KEEP"),
    # Refreshed 2026-09-24 (Live-Surface-Cleanup Step 2, PR #506): the
    # cic/corpus-map samples below were cleaned by that PR's own full
    # surface pass and stopped matching. Moved to fresh worlds/ examples,
    # not yet touched by the cleanup program (item 4), to keep this table
    # at >=60 real, currently-matching lines.
    ("Build/worlds/rzg/CiC_Reformed_Zurich_Geneva_Doc01_Scope_Confirmations_2026-09-15.md", 1, "REWRITE"),
    ("Build/worlds/ijc/Post_Admission_Source_Finding_Philostorgius_OpusImperfectum_2026-09-09.md", 279, "REWRITE"),
    ("Build/worlds/pahc/CiC_W1_World_Profile.md", 562, "REWRITE"),
    ("Build/worlds/_cross-world/DOWNLOAD-QUEUE.md", 17, "REWRITE"),
    ("Build/worlds/ijc/Source_Registry.md", 25, "REWRITE"),
    ("Build/worlds/rzg/Doc_05_Ecological_Reconstruction.md", 177, "REWRITE"),
    # Refreshed 2026-09-26 (per-world decision-log exemption): this line
    # sits inside CiC_W7_Decision_Log.md, a per-world decision log
    # (matching lpc_Decision_Log.md's own header purpose), now correctly
    # PROTECTED rather than REWRITE under the new _is_decision_log rule.
    ("Build/worlds/syr/CiC_W7_Decision_Log.md", 16, "PROTECTED"),
    # Refreshed 2026-09-26 (Doc_0X construction-doc review-status
    # exemption): this line sits in Doc_04's own "## Disposition" section
    # ("Carried open, and not resolved by this approval") - exactly the
    # load-bearing pipeline-state content that section now protects, so
    # it moved from a hand-labelled ROUTE (a genuinely open placement
    # question the tool used to read as REWRITE) to PROTECTED, the
    # correct category under the new rule.
    ("Build/worlds/lpc/Doc_04_Gravity_Discovery.md", 259, "PROTECTED"),
    ("Build/worlds/witt/witt_Doc_06_Full_Lexicon_Development.md", 1754, "REWRITE"),
    # Refreshed 2026-09-26 (Phase 3b: cic/engine/ + cic-poc/frontend
    # cleanup, commits 11ee5a81 and the earlier f1e1e093): all 7 samples
    # below (6 cic/engine, 1 cic-poc/frontend) were cleaned and stopped
    # matching. Moved to fresh records/ examples, not yet touched by the
    # cleanup program, to keep this table at >=60 real, currently-matching
    # lines.
    # Refreshed 2026-09-26 (Phase 3b records/ cleanup, commits
    # 0cbe76d5..30b1cb93): all 7 samples below were cleaned by that
    # effort and stopped matching. Moved to fresh Build/reference/
    # examples, a surface not part of any active or near-term cleanup
    # pass, to keep this table stable and at >=60 real, currently-
    # matching lines.
    ("Build/reference/method/CiC_Voice_Style_Guide_and_Scaling_Plan.md", 1301, "REWRITE"),
    ("Build/reference/method/CiC_Representative_Naming_Role_Discipline_2026-09-08.md", 6, "REWRITE"),
    ("Build/reference/L2C-System-Status/CiC_Pipeline_Decision_Log.md", 174, "REWRITE"),
    ("Build/reference/Project-Reference/CiC_Cleaning_Pattern_Log.md", 137, "REWRITE"),
    ("Build/reference/method/Pass2-decisions/2026-08-01_M_lean_validation_interview_spend.md", 54, "REWRITE"),
    ("Build/reference/method/CiC_Record_Native_World_Build_Process_V1.9.md", 627, "REWRITE"),
    ("Build/reference/Redesign-Spec/PHASE-1-LAUNCH.md", 200, "REWRITE"),
    # Refreshed 2026-09-24 (Live-Surface-Cleanup Step 2, PR #501): the
    # original 6 cic-website samples here were cleaned by that PR and
    # stopped matching. cic-website is now clean apart from one known
    # false positive (below); the other 5 slots move to cic/corpus-map,
    # not yet touched by the cleanup program, to keep this table at >=60
    # real, currently-matching examples.
    # Hand label KEEP: "external reviewer" here is real body copy about
    # wanting an academic reviewer for the project's own scholarship, not
    # narration of this project's internal review process - the same
    # `reviewer`-pattern gap already hand-labelled for reference/ above.
    ("cic-website/support.html", 127, "KEEP"),
    ("Build/worlds/cappadocian/CAPPADOCIAN_BUILD_LEDGER.md", 463, "REWRITE"),
    ("Build/worlds/_cross-world/CiC_Cross_System_Consistency_Audit_2026-08-26.md", 666, "REWRITE"),
    ("Build/worlds/gallic/gallic_Doc03_Lexicon_Candidates.md", 802, "REWRITE"),
    ("Build/worlds/pahc/CiC_W1_World_Profile.md", 81, "REWRITE"),
    ("Build/worlds/witt/witt_Doc_06_Full_Lexicon_Development.md", 1524, "REWRITE"),
    # Refreshed 2026-09-24 (Live-Surface-Cleanup Step 2, PR #506): all 10
    # cic/corpus-map samples in this block were cleaned by that PR's own
    # full surface pass and stopped matching. Moved to 10 more worlds/
    # examples, distinct from the 8 above, to keep this table at >=60
    # real, currently-matching lines.
    ("Build/worlds/witt/witt_Doc_04_Historical_Gravity.md", 569, "REWRITE"),
    # Refreshed 2026-09-26 (per-world decision-log exemption): this line
    # sits inside hal_Decision_Log.md, a per-world decision log, now
    # correctly PROTECTED rather than REWRITE under the new
    # _is_decision_log rule.
    ("Build/worlds/hal/hal_Decision_Log.md", 88, "PROTECTED"),
    ("Build/worlds/don/scripts/wb_don_s21.py", 450, "REWRITE"),
    ("Build/worlds/alx/Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md", 13, "REWRITE"),
    ("Build/worlds/rzg/Doc_01_World_Identification_Boundaries_Orientation.md", 80, "REWRITE"),
    ("engine/m4/reports/live-table-battery-seat-identity-guard-2026-09-22.json", 5817, "PROTECTED"),
    # Refreshed 2026-09-25 (fleet-checks-widening PR round 2: review
    # findings applied): line 109 shifted to 120 once the eleven
    # m1:readability waivers were added above it in the file.
    ("engine/m9/enforce.py", 120, "KEEP"),
    # Refreshed 2026-09-25: main's own sentence_enforce PR shifted this
    # file's lines by +7 above this point; re-pinned to the same
    # r27_regenerated assertion, now at 1131.
    ("engine/m4/tests/test_turn.py", 1131, "REWRITE"),
    ("engine/m4/reports/live-table-battery-monologue-fix-2026-09-05.json", 300, "PROTECTED"),
    # Refreshed 2026-09-25 (fleet-checks-widening PR round 2: review
    # findings applied): the comment block this entry pinned ("the five
    # m1:readability waivers... removed the same day") was itself pure
    # change-history narration with no independent design reason once its
    # provenance was stripped, so it was deleted outright rather than
    # reworded - enforce.py now carries zero REWRITE hits. Re-pinned to a
    # fresh REWRITE example elsewhere.
    ("records/cappadocian/gravity/cappadocian.gravity.athens-fishermen.md", 43, "REWRITE"),
    ("engine/m4/reports/live-table-battery-seat-identity-guard-2026-09-22.json", 4464, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 243, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 154, "PROTECTED"),
    ("fixtures/README.md", 25, "REWRITE"),
    ("fixtures/seeded_defects.yaml", 251, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 213, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 191, "PROTECTED"),
    ("records/don/source/don.source.npnf104-prolegomena-analysis.md", 26, "PROTECTED"),
    # Refreshed 2026-09-26 (Phase 3b records/ cleanup, commits
    # 0cbe76d5..30b1cb93): the original cappadocian.voice.craft.md:106 line
    # was cleaned as part of that effort. Re-pinned to a stable
    # Build/reference/ example.
    ("Build/reference/method/CiC_Adversarial_Review_Standard_Practice.md", 25, "REWRITE"),
    # Refreshed 2026-09-25 (fleet-checks-widening PR): the original
    # fix.craft.vera-voice.md:29 "REVISED 2026-09-19" line was itself
    # cleaned as part of that PR (the file's `guard` field was rewritten
    # for FK/FRE, which obligated removing the file's own pre-existing
    # commentary too, per CLAUDE.md's "any PR that edits a live file also
    # removes the commentary already in it"). Re-pinned to a fresh
    # gravity-classification-label hit, not yet touched by any re-voicing
    # PR.
    ("records/alx/force/alx.force.scripture-ongoing.md", 29, "REWRITE"),
    ("records/alx/source/alx.source.origen-comm-matthew.md", 22, "PROTECTED"),
    # Refreshed 2026-09-26 (Phase 3b records/ cleanup, commits
    # 0cbe76d5..30b1cb93): the original hal.force.clerical-precarity.md:52
    # line was cleaned as part of that effort. Re-pinned to a stable
    # Build/reference/ example.
    ("Build/reference/fleet-voice/EXEMPLAR-TRANSCRIPT.md", 146, "REWRITE"),
    # Refreshed 2026-09-25 (Live-Surface-Cleanup Step 4/Item A prep): the
    # original alx.figure.didymus.md:48 line was cleaned by PR #509 and
    # stopped matching.
    # Refreshed again 2026-09-26 (Phase 3b records/ cleanup, commits
    # 0cbe76d5..30b1cb93): the re-pinned
    # cappadocian.contested.agennetos-transmission.md:27 line was itself
    # cleaned by that effort. Re-pinned to a stable Build/reference/
    # example.
    ("Build/reference/Project-Reference/CiC_V7_Upgrade_Reference.md", 134, "REWRITE"),
    ("Build/reference/method/Pass2-decisions/S6.2_length_ceiling_retry_cost_investigation_2026-07-31.md", 14, "REWRITE"),
    # Hand label KEEP: "reviewer" here is generic instructional/methodology
    # prose (what a hypothetical reviewer of OTHER content would miss),
    # not a leaked note about this document's own review history - the
    # tool cannot currently tell the two uses of "reviewer" apart. See the
    # PR body's precision limitation note (Build/reference/Project-Reference/
    # CiC_Cleaning_Pattern_Log.md and Build/reference/L4-Templates/*).
    ("Build/reference/Project-Reference/CiC_Cleaning_Pattern_Log.md", 151, "KEEP"),
    ("Build/reference/Redesign-Spec/World-Cards.md", 139, "REWRITE"),
    ("Build/reference/Project-Reference/CiC_Cleaning_Pattern_Log.md", 35, "KEEP"),
    ("Build/reference/Redesign-Spec/PHASE-1-LAUNCH.md", 443, "REWRITE"),
    ("Build/reference/L4-Templates/Representative_Construction_Notes_Template.md", 366, "KEEP"),
    # Refreshed 2026-09-26 (Doc_0X construction-doc review-status
    # exemption): this "Date drafted:" header line was hand-labelled KEEP
    # under the old bare-date rule alone; it is now PROTECTED, the more
    # specific and correct category, by the new
    # _doc_construction_protected_lines header-field-line rule.
    ("Build/worlds/ijc/Doc_07_Integrated_Ecology_Analysis.md", 5, "PROTECTED"),
    ("Build/worlds/cappadocian/Review-Artifacts/UnusedSourceFinding_Round3_Review.md", 20, "PROTECTED"),
    ("Build/worlds/don/Open_Gaps_Tracking.md", 357, "PROTECTED"),
    ("Build/worlds/witt/witt_Doc03_Review_Round11.md", 64, "PROTECTED"),
    # Hand label KEEP: the "Added" column of a per-world Source Registry is
    # exactly the schema-defined field reference/L3B-World-Build-
    # Methodology/Source_Registry_Template.md names ("Added | Date and
    # who/what added it") - structured provenance, not narration. The
    # tool does not currently parse Source Registry table columns; see the
    # PR body's precision limitation note.
    ("Build/worlds/lpc/Source_Registry.md", 142, "KEEP"),
    ("Build/worlds/gallic/gallic_Doc02_Review_Round1.md", 562, "PROTECTED"),
]

ACTIONABLE = {"REWRITE", "ROUTE"}


def _actual_category(path: str, line: int) -> str | None:
    full = REPO / path
    surface = next((s for s, roots in clc.SURFACES.items() if any(path.startswith(r + "/") for r in roots)), "engine")
    hits = clc.scan_file(REPO, full, surface)
    for hit in hits:
        if hit.line == line:
            return hit.category
    return None


@pytest.mark.parametrize("path,line,expected", HAND_LABELS)
def test_hand_label_present(path, line, expected):
    """Every hand-labelled line still exists and the tool still flags it
    (as SOME category) - a line moving or stopping matching means the
    sample table above needs updating, not that the rule broke."""
    assert (REPO / path).exists(), f"{path} no longer exists on disk"
    assert _actual_category(path, line) is not None, f"{path}:{line} no longer flagged by any pattern"


def test_precision_and_recall_on_hand_labelled_sample():
    assert len(HAND_LABELS) >= 60
    tp = fp = fn = tn = 0
    for path, line, expected in HAND_LABELS:
        actual = _actual_category(path, line)
        assert actual is not None, f"{path}:{line} not flagged"
        actual_positive = actual in ACTIONABLE
        expected_positive = expected in ACTIONABLE
        if actual_positive and expected_positive:
            tp += 1
        elif actual_positive and not expected_positive:
            fp += 1
        elif not actual_positive and expected_positive:
            fn += 1
        else:
            tn += 1

    precision = tp / (tp + fp) if (tp + fp) else 1.0
    recall = tp / (tp + fn) if (tp + fn) else 1.0
    exact_matches = sum(
        1 for path, line, expected in HAND_LABELS if _actual_category(path, line) == expected
    )
    print(
        f"\nHand-labelled sample (n={len(HAND_LABELS)}): "
        f"binary precision={precision:.3f} recall={recall:.3f} "
        f"(TP={tp} FP={fp} FN={fn} TN={tn}); "
        f"4-class exact-category accuracy={exact_matches}/{len(HAND_LABELS)}"
    )
    # Measured at write time: precision 0.895 (34 TP / 38 flagged-positive),
    # recall 1.000 (34/34 - no actionable line was missed). Thresholds set
    # a bit under that so a small, honest regression doesn't need a hair-
    # trigger fix, while still catching a real drop.
    assert recall >= 0.95
    assert precision >= 0.85
