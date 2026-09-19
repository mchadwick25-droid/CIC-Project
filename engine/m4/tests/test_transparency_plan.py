"""engine.m4.transparency_plan's own tests (Build-Plan.md Stage 3a).

Real compiled repository content for the record lookups (same discipline
as test_citation_cards.py); the `citations` lists themselves are
constructed by hand, since they're this module's actual input shape
(engine.m4.turn.apply_net's per-turn output) and the specific run/repeat
patterns under test need to be pinned down exactly, not hoped for out of
whatever a live turn happens to produce.
"""
import json

from engine.m2.compiler import compile_and_hash
from engine.m4.transparency_plan import build_transparency_plan


def _real_repository(world_key: str) -> dict[str, dict]:
    package, _digest = compile_and_hash(
        world_key=world_key, package_id="TEST", records_commit="TEST", compiler_version="TEST"
    )
    records = json.loads(package["compiled/repository.json"])["records"]
    return {r["id"]: r for r in records}


REPO = _real_repository("alx")

# Two real, distinct record ids this world's own repository actually
# carries (test_citation_cards.py already relies on the first existing).
TERM_ID = "alx.term.allegoria"
_OTHER_CANDIDATES = [rid for rid, r in REPO.items() if r.get("record_type") == "story"]
STORY_ID = _OTHER_CANDIDATES[0]


def _empty_net_result(n_sentences: int) -> dict:
    return {"sentences": [{"verdict": "ok"} for _ in range(n_sentences)]}


def test_completeness_invariant_every_cited_id_reaches_references():
    """The actual fix: every record_id appearing anywhere in citations
    appears in references exactly once, regardless of how many times or
    how non-consecutively it was cited."""
    citations = [
        {"sentence": "First mention.", "record_ids": [TERM_ID]},
        {"sentence": "Unrelated sentence.", "record_ids": [STORY_ID]},
        {"sentence": "Second mention, far later.", "record_ids": [TERM_ID]},
    ]
    plan = build_transparency_plan(
        citations=citations, net_result=_empty_net_result(3), repository_records=REPO, world_key="alx",
    )
    cited_ids = {rid for c in citations for rid in c["record_ids"]}
    reference_ids = {r["record_id"] for r in plan["references"]}
    assert reference_ids == cited_ids
    # Exactly once each - not once per citation.
    assert len(plan["references"]) == len(reference_ids)


def test_contiguous_run_becomes_one_anchor_not_one_per_sentence():
    citations = [
        {"sentence": "Part one.", "record_ids": [STORY_ID]},
        {"sentence": "Part two.", "record_ids": [STORY_ID]},
        {"sentence": "Part three.", "record_ids": [STORY_ID]},
    ]
    plan = build_transparency_plan(
        citations=citations, net_result=_empty_net_result(3), repository_records=REPO, world_key="alx",
    )
    story_anchors = [a for a in plan["anchors"] if a["record_id"] == STORY_ID]
    assert len(story_anchors) == 1
    assert story_anchors[0]["run_start_sentence"] == 0
    assert story_anchors[0]["run_end_sentence"] == 2
    assert story_anchors[0]["repeat"] is False


def test_non_consecutive_recite_becomes_a_second_repeat_anchor():
    citations = [
        {"sentence": "Told here.", "record_ids": [STORY_ID]},
        {"sentence": "Something else entirely.", "record_ids": [TERM_ID]},
        {"sentence": "Told again, later.", "record_ids": [STORY_ID]},
    ]
    plan = build_transparency_plan(
        citations=citations, net_result=_empty_net_result(3), repository_records=REPO, world_key="alx",
    )
    story_anchors = [a for a in plan["anchors"] if a["record_id"] == STORY_ID]
    assert len(story_anchors) == 2
    assert story_anchors[0]["run_start_sentence"] == story_anchors[0]["run_end_sentence"] == 0
    assert story_anchors[0]["repeat"] is False
    assert story_anchors[1]["run_start_sentence"] == story_anchors[1]["run_end_sentence"] == 2
    assert story_anchors[1]["repeat"] is True
    # Still exactly one reference card, not two, for a record cited twice.
    assert sum(1 for r in plan["references"] if r["record_id"] == STORY_ID) == 1


def test_a_sentence_citing_two_records_produces_two_single_record_anchors():
    citations = [{"sentence": "Cites both at once.", "record_ids": [TERM_ID, STORY_ID]}]
    plan = build_transparency_plan(
        citations=citations, net_result=_empty_net_result(1), repository_records=REPO, world_key="alx",
    )
    assert len(plan["anchors"]) == 2
    assert {a["record_id"] for a in plan["anchors"]} == {TERM_ID, STORY_ID}
    for anchor in plan["anchors"]:
        assert anchor["run_start_sentence"] == 0
        assert anchor["run_end_sentence"] == 0


def test_world_key_is_stamped_on_the_plan_every_anchor_and_every_reference():
    citations = [{"sentence": "One.", "record_ids": [TERM_ID]}]
    plan = build_transparency_plan(
        citations=citations, net_result=_empty_net_result(1), repository_records=REPO, world_key="alx",
    )
    assert plan["world_key"] == "alx"
    assert all(a["world_key"] == "alx" for a in plan["anchors"])
    assert all(r["world_key"] == "alx" for r in plan["references"])


def test_confidence_is_attached_but_this_module_never_renders_anything():
    citations = [{"sentence": "One.", "record_ids": [TERM_ID]}]
    plan = build_transparency_plan(
        citations=citations, net_result=_empty_net_result(1), repository_records=REPO, world_key="alx",
    )
    anchor = plan["anchors"][0]
    reference = plan["references"][0]
    # Whatever this record's own confidence block is (present or absent),
    # it's the record's own value, verbatim - not invented here.
    assert anchor["confidence"] == REPO[TERM_ID].get("confidence")
    assert reference["confidence"] == REPO[TERM_ID].get("confidence")


def test_unverified_claims_counts_non_ok_sentences_only():
    citations = [{"sentence": "Survived.", "record_ids": [TERM_ID]}]
    net_result = {
        "sentences": [
            {"verdict": "ok"},
            {"verdict": "withheld"},
            {"verdict": "withheld"},
        ]
    }
    plan = build_transparency_plan(
        citations=citations, net_result=net_result, repository_records=REPO, world_key="alx",
    )
    assert plan["unverified_claims"] == {"count": 2, "sentence_indexes": [1, 2]}


def test_a_record_id_absent_from_the_repository_is_skipped_in_references_not_crashed_on():
    citations = [{"sentence": "Cites something gone.", "record_ids": ["alx.term.does-not-exist"]}]
    plan = build_transparency_plan(
        citations=citations, net_result=_empty_net_result(1), repository_records=REPO, world_key="alx",
    )
    assert plan["references"] == []
    # The anchor still exists (record_type is None for an unresolved id) -
    # this module never silently drops an anchor, only a reference card it
    # has no record to build one from.
    assert plan["anchors"][0]["record_id"] == "alx.term.does-not-exist"
    assert plan["anchors"][0]["record_type"] is None


def test_deterministic_for_identical_input():
    citations = [
        {"sentence": "A.", "record_ids": [TERM_ID]},
        {"sentence": "B.", "record_ids": [STORY_ID, TERM_ID]},
    ]
    net_result = _empty_net_result(2)
    first = build_transparency_plan(citations=citations, net_result=net_result, repository_records=REPO, world_key="alx")
    second = build_transparency_plan(citations=citations, net_result=net_result, repository_records=REPO, world_key="alx")
    assert first == second


def test_empty_citations_produce_an_empty_plan_not_an_error():
    plan = build_transparency_plan(
        citations=[], net_result=_empty_net_result(0), repository_records=REPO, world_key="alx",
    )
    assert plan == {
        "world_key": "alx",
        "anchors": [],
        "references": [],
        "unverified_claims": {"count": 0, "sentence_indexes": []},
    }
