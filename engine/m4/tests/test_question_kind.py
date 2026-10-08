"""The question kind: evidence floors by kind, the directive's per-kind line,
the oblique who-line, and a follow-up inheriting the previous kind."""
import uuid

import pytest

from engine.m4.evidence import QUESTION_KINDS, floors_for_kind, resolve_kind, select_cell_candidates
from engine.m4.entrance import open_session
from engine.m4.projection import project_fresh
from engine.m4.store import Store
from engine.m4.turn_prep import (
    CONCISION_DIRECTIVE,
    KIND_DIRECTIVES,
    OBLIQUE_WHO_DIRECTIVE,
    prepare_voice_turn_inputs,
)
from engine.m4.world_loader import LoadedWorld
from engine.m5.routing import Directive, assemble_directive

BUDGET = 9000
TYPES = ("doctrinal_witness", "term", "story", "quote", "gravity", "force", "contested_claim")
COVERAGE_KEYS = {
    "doctrinal_witness": "doctrinal_witness", "term": "terms", "story": "stories", "quote": "quotes",
    "gravity": "gravities", "force": "forces", "contested_claim": "contested_claims",
}
EXPECTED = {
    "who": (2, 2, 1, 2, 1, 0, 1),
    "what_is": (2, 2, 1, 2, 1, 0, 1),
    "what_did": (1, 1, 3, 2, 0, 1, 1),
    "what_happened": (1, 1, 3, 2, 0, 1, 1),
    "what_means": (1, 3, 1, 2, 1, 0, 1),
    "why": (2, 1, 1, 2, 2, 1, 1),
    "how": (1, 2, 2, 1, 1, 2, 0),
    "did_it_happen": (1, 3, 2, 2, 2, 1, 1),
    "other": (1, 3, 2, 2, 2, 1, 1),
}
BODY = "The community kept this memory of Jesus whole, handed down and told again at the meal. " * 7


def _world_records():
    records = {}
    coverage = {key: [] for key in COVERAGE_KEYS.values()}
    coverage["honest_limit"] = []
    for record_type in TYPES:
        for i in range(4):
            rid = f"fix.{record_type}.{i}"
            body = {"text": BODY}
            if record_type == "quote":
                body = {"text": BODY, "modern_rendering": BODY}
            elif record_type == "term":
                body = {"plain_meaning": BODY}
            elif record_type == "story":
                body = {"tellable_as": BODY}
            elif record_type in ("gravity", "force"):
                body = {"description": BODY}
            elif record_type == "contested_claim":
                body = {"claim": BODY}
            records[rid] = {
                "id": rid, "record_type": record_type, "canon_cells": ["C-E"],
                "sources": [{"source_id": f"fix.source.{record_type}{i}"}], **body,
            }
            coverage[COVERAGE_KEYS[record_type]].append(rid)
    return records, coverage


def _counts(selected):
    return tuple(sum(1 for c in selected if c["record_type"] == t) for t in TYPES)


def test_every_kind_has_a_floor_table_and_the_values_are_the_ruled_ones():
    assert set(EXPECTED) == set(QUESTION_KINDS)
    for kind, floors in EXPECTED.items():
        assert tuple(floors_for_kind(kind).values()) == floors
    assert floors_for_kind(None) == floors_for_kind("other") == floors_for_kind("not-a-kind")


@pytest.mark.parametrize("kind", QUESTION_KINDS)
def test_the_evidence_block_meets_each_kinds_floors_inside_the_budget(kind):
    records, coverage = _world_records()
    selected = select_cell_candidates(
        cell="C-E", coverage_entry=coverage, repository_records=records,
        message="Who was Jesus to your community", asks=None, budget_chars=BUDGET, kind=kind,
    )
    assert _counts(selected) == EXPECTED[kind]
    assert sum(len(c["head"]) for c in selected) <= BUDGET


def test_the_diversity_pick_and_the_already_told_demotion_still_apply_under_a_kind():
    records, coverage = _world_records()
    told = {"fix.quote.0"}
    selected = select_cell_candidates(
        cell="C-E", coverage_entry=coverage, repository_records=records,
        message="Who was Jesus to your community", asks=None, already_told_ids=told, kind="who",
    )
    quotes = [c["id"] for c in selected if c["record_type"] == "quote"]
    assert len(quotes) == 2 and len(set(quotes)) == 2
    assert quotes[0] != "fix.quote.0"


def _world(oblique):
    witness = {"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}
    if oblique is not None:
        witness["answers_obliquely"] = oblique
        if oblique:
            witness["oblique_reason"] = "Our own sources speak of him through the meal."
    return LoadedWorld(
        world_key="fix", manifest_hash="sha256:test", prompt_text="## Identity\nVera.", capsule_text="capsule",
        repository={"records": [witness]}, quotes={"quotes": []}, figures={"figures": []}, coverage={},
        frame={"representative": {"name": "Vera", "role_label": "Witness"}},
    )


def _directive(kind):
    return Directive(asks=[{"order": 1, "text": "who was Jesus"}], kind=kind)


@pytest.mark.parametrize("kind", QUESTION_KINDS)
def test_the_directive_carries_the_opening_line_for_every_kind_and_the_matching_kind_line(kind):
    prepared = prepare_voice_turn_inputs(world=_world(None), participant_message="Who was Jesus?", directive=_directive(kind))
    assert CONCISION_DIRECTIVE in prepared.turn_directive
    others = {line for k, line in KIND_DIRECTIVES.items() if k != kind}
    if kind in KIND_DIRECTIVES:
        assert KIND_DIRECTIVES[kind] in prepared.turn_directive
    assert not any(line in prepared.turn_directive for line in others - {KIND_DIRECTIVES.get(kind)})


def test_a_who_turn_whose_lead_witness_answers_obliquely_gets_the_oblique_line():
    prepared = prepare_voice_turn_inputs(world=_world(True), participant_message="Who was Jesus?", directive=_directive("who"))
    assert OBLIQUE_WHO_DIRECTIVE in prepared.turn_directive
    assert KIND_DIRECTIVES["who"] not in prepared.turn_directive


@pytest.mark.parametrize("oblique", [None, False])
def test_without_the_flag_a_who_turn_gets_the_plain_who_line(oblique):
    prepared = prepare_voice_turn_inputs(world=_world(oblique), participant_message="Who was Jesus?", directive=_directive("who"))
    assert KIND_DIRECTIVES["who"] in prepared.turn_directive
    assert OBLIQUE_WHO_DIRECTIVE not in prepared.turn_directive


def test_the_oblique_flag_changes_nothing_on_a_turn_that_is_not_a_who_turn():
    prepared = prepare_voice_turn_inputs(world=_world(True), participant_message="Why did they meet?", directive=_directive("why"))
    assert OBLIQUE_WHO_DIRECTIVE not in prepared.turn_directive
    assert KIND_DIRECTIVES["why"] in prepared.turn_directive


def test_the_reader_kind_reaches_the_directive_and_an_unknown_kind_reads_as_other():
    reader = {"asks": [], "register": "informational", "ambiguity_options": []}
    for kind in QUESTION_KINDS:
        assert assemble_directive({**reader, "kind": kind}).kind == kind
    assert assemble_directive({**reader, "kind": "nonsense"}).kind == "other"
    assert assemble_directive(reader).kind == "other"


def _follow_up_inputs():
    from engine.m1.loader import load_fleet_records

    return dict(
        message="Why did that matter?", asks=None,
        history=[{"role": "user", "content": "How does baptism actually work for your community?"}, {"role": "assistant", "content": "We washed."}],
        canon_questions=load_fleet_records(), repository_records={},
    )


def test_a_follow_up_the_reader_leaves_as_other_inherits_the_previous_kind():
    assert resolve_kind("other", previous_kind="how", **_follow_up_inputs()) == "how"


def test_a_follow_up_whose_message_changes_the_kind_keeps_its_own():
    assert resolve_kind("why", previous_kind="how", **_follow_up_inputs()) == "why"


def test_a_first_turn_reads_as_the_reader_kind_and_never_inherits():
    inputs = {**_follow_up_inputs(), "history": []}
    assert resolve_kind("other", previous_kind="how", **inputs) == "other"
    assert resolve_kind("who", previous_kind="how", **inputs) == "who"


def test_a_message_that_is_not_a_follow_up_never_inherits():
    inputs = {**_follow_up_inputs(), "message": "How does baptism actually work for your community?"}
    assert resolve_kind("other", previous_kind="who", **inputs) == "other"


def _voice(store, sid, kind):
    payload = {
        "speaker": "fix", "text": "We washed.", "citations": [], "glosses": [], "figures_used": [],
        "quote_offers": [], "attempts_meta": {}, "output_defects": [],
    }
    if kind:
        payload["kind"] = kind
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type="voice_turn", payload=payload)


def test_the_session_keeps_the_kind_the_previous_voice_turn_answered_under(tmp_path):
    store = Store(tmp_path / "events.db")
    sid = str(uuid.uuid4())
    open_session(
        store, session_id=sid, event_uuid=str(uuid.uuid4()), world_key="fix", mode="interview",
        frame="general_seeker", code_hash="abc123", package_manifest_hash="sha256:xyz",
    )
    assert project_fresh(sid, store).last_kind is None
    _voice(store, sid, "how")
    assert project_fresh(sid, store).last_kind == "how"
    _voice(store, sid, "other")
    assert project_fresh(sid, store).last_kind == "other"
    _voice(store, sid, None)
    assert project_fresh(sid, store).last_kind == "other"


def test_the_voice_turn_records_the_kind_it_answered_under():
    prepared = prepare_voice_turn_inputs(world=_world(None), participant_message="Who was Jesus?", directive=_directive("how"))
    assert prepared.kind == "how"


@pytest.mark.parametrize("kind", ["what_did", "what_happened"])
def test_the_telling_line_makes_the_story_no_quota(kind):
    line = KIND_DIRECTIVES[kind]
    assert "tell it as the record tells it rather than summarising it" in line
    assert "where they do not, do not reach for one" in line


def test_the_prepared_turn_lists_the_offered_record_ids_by_type():
    prepared = prepare_voice_turn_inputs(world=_world(None), participant_message="Who was Jesus?", directive=_directive("who"))
    assert prepared.offered_ids == {"doctrinal_witness": ["fix.witness.who-is-jesus"]}


def test_the_offered_ids_group_every_candidate_by_its_type():
    from engine.m4.turn_prep import _offered_ids

    evidence_block = {"candidates": [
        {"id": "a.story.1", "record_type": "story"}, {"id": "a.quote.1", "record_type": "quote"},
        {"id": "a.story.2", "record_type": "story"},
    ]}
    assert _offered_ids(evidence_block) == {"story": ["a.story.1", "a.story.2"], "quote": ["a.quote.1"]}
