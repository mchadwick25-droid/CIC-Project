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
    dedicated = _hits_for(text, tmp_path, "worlds/alx/Review-Artifacts/Doc02_Round1_Review.md")
    loose = _hits_for(text, tmp_path, "worlds/gallic/gallic_Doc02_Review_Round1.md")
    assert dedicated[0].category == "PROTECTED"
    assert loose[0].category == "PROTECTED"


def test_construction_doc_under_worlds_not_protected(tmp_path):
    text = "Per Mark's ruling, R26, this section covers gravity discovery.\n"
    hits = _hits_for(text, tmp_path, "worlds/alx/Doc_04_Gravity_Discovery.md")
    assert hits[0].category != "PROTECTED"


def test_world_build_dir_protected(tmp_path):
    text = "RULED 2026-09-01 per Mark\n"
    hits = _hits_for(text, tmp_path, "worlds/rzg/build/bar-screen-2026-09-19.json")
    assert hits[0].category == "PROTECTED"


def test_gaps_ledger_protected(tmp_path):
    text = "Entry 42 (subject: X, 2026-09-01): per Mark's ruling R26\n"
    hits = _hits_for(text, tmp_path, "worlds/don/Open_Gaps_Tracking.md")
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
    hits = _hits_for("**Date drafted:** 2026-07-20\n", tmp_path, "worlds/alx/Doc_01_World_Identification.md")
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
    ("cic/corpus-map/marcion-marcionism.yaml", 82, "REWRITE"),
    ("cic/corpus-map/homoian-arian-christianity.yaml", 237, "REWRITE"),
    ("cic/corpus-map/latin-pastoral-congregational-christianity.yaml", 162, "REWRITE"),
    # Hand label ROUTE ("a reviewer may prefer... once one exists" names an
    # open, unresolved placement question); the tool currently reads this
    # as REWRITE (a false 4-class miss inside the same "needs action"
    # bucket - see the PR body's ROUTE_CUES limitation note).
    ("cic/corpus-map/imperial-juridical-christianity.yaml", 241, "ROUTE"),
    ("cic/corpus-map/_staging/macarius_fifty-spiritual-homilies_mason1921.yaml", 1, "REWRITE"),
    ("cic/corpus-map/_staging/npnf105_augustine-anti-pelagian-writings.yaml", 204, "REWRITE"),
    ("cic/engine/texts_registry.py", 74, "REWRITE"),
    ("cic/engine/texts_registry.py", 220, "REWRITE"),
    ("cic/engine/corpus_authors.py", 88, "REWRITE"),
    ("cic/engine/tests_corpus_map.py", 52, "REWRITE"),
    ("cic/engine/corpus_map.py", 75, "REWRITE"),
    ("cic/engine/texts_registry.py", 11, "REWRITE"),
    ("cic-poc/frontend/src/components/FigureBridgeMark.tsx", 3, "REWRITE"),
    ("cic-poc/frontend/src/components/VoiceTurnBody.test.tsx", 170, "REWRITE"),
    ("cic-poc/frontend/src/components/Arrival.test.tsx", 2, "REWRITE"),
    ("cic-poc/frontend/src/components/StoryMark.tsx", 15, "REWRITE"),
    ("cic-poc/frontend/src/components/StoryMark.tsx", 16, "REWRITE"),
    ("cic-poc/frontend/src/components/Arrival.tsx", 14, "REWRITE"),
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
    ("cic/corpus-map/_staging/anf01_apostolic-fathers-justin-irenaeus.yaml", 145, "REWRITE"),
    ("cic/corpus-map/_staging/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.yaml", 60, "REWRITE"),
    ("cic/corpus-map/_staging/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.yaml", 297, "REWRITE"),
    ("cic/corpus-map/roman-church-third-century.yaml", 16, "REWRITE"),
    ("cic/corpus-map/README.md", 43, "REWRITE"),
    ("engine/m4/reports/live-table-battery-seat-identity-guard-2026-09-22.json", 5817, "PROTECTED"),
    ("engine/m9/enforce.py", 111, "KEEP"),
    ("engine/m4/tests/test_turn.py", 1268, "REWRITE"),
    ("engine/m4/reports/live-table-battery-monologue-fix-2026-09-05.json", 300, "PROTECTED"),
    ("engine/m9/enforce.py", 139, "REWRITE"),
    ("engine/m4/reports/live-table-battery-seat-identity-guard-2026-09-22.json", 4464, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 243, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 154, "PROTECTED"),
    ("fixtures/README.md", 25, "REWRITE"),
    ("fixtures/seeded_defects.yaml", 251, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 213, "PROTECTED"),
    ("fixtures/seeded_defects.yaml", 191, "PROTECTED"),
    ("records/don/source/don.source.npnf104-prolegomena-analysis.md", 26, "PROTECTED"),
    ("records/cappadocian/voice_craft/cappadocian.voice.craft.md", 106, "REWRITE"),
    ("records/fix/voice_craft/fix.craft.vera-voice.md", 29, "REWRITE"),
    ("records/alx/source/alx.source.origen-comm-matthew.md", 22, "PROTECTED"),
    ("records/hal/force/hal.force.clerical-precarity.md", 52, "REWRITE"),
    ("records/alx/figure/alx.figure.didymus.md", 48, "REWRITE"),
    ("reference/method/Pass2-decisions/S6.2_length_ceiling_retry_cost_investigation_2026-07-31.md", 14, "REWRITE"),
    # Hand label KEEP: "reviewer" here is generic instructional/methodology
    # prose (what a hypothetical reviewer of OTHER content would miss),
    # not a leaked note about this document's own review history - the
    # tool cannot currently tell the two uses of "reviewer" apart. See the
    # PR body's precision limitation note (reference/Project-Reference/
    # CiC_Cleaning_Pattern_Log.md and reference/L4-Templates/*).
    ("reference/Project-Reference/CiC_Cleaning_Pattern_Log.md", 151, "KEEP"),
    ("reference/Redesign-Spec/World-Cards.md", 139, "REWRITE"),
    ("reference/Project-Reference/CiC_Cleaning_Pattern_Log.md", 35, "KEEP"),
    ("reference/Redesign-Spec/PHASE-1-LAUNCH.md", 443, "REWRITE"),
    ("reference/L4-Templates/Representative_Construction_Notes_Template.md", 366, "KEEP"),
    ("worlds/ijc/Doc_07_Integrated_Ecology_Analysis.md", 5, "KEEP"),
    ("worlds/cappadocian/Review-Artifacts/UnusedSourceFinding_Round3_Review.md", 20, "PROTECTED"),
    ("worlds/don/Open_Gaps_Tracking.md", 357, "PROTECTED"),
    ("worlds/witt/witt_Doc03_Review_Round11.md", 64, "PROTECTED"),
    # Hand label KEEP: the "Added" column of a per-world Source Registry is
    # exactly the schema-defined field reference/L3B-World-Build-
    # Methodology/Source_Registry_Template.md names ("Added | Date and
    # who/what added it") - structured provenance, not narration. The
    # tool does not currently parse Source Registry table columns; see the
    # PR body's precision limitation note.
    ("worlds/lpc/Source_Registry.md", 142, "KEEP"),
    ("worlds/gallic/gallic_Doc02_Review_Round1.md", 562, "PROTECTED"),
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
