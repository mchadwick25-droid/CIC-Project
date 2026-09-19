"""world_front and facilitator_brief must NEVER reach the Representative's
own voice assembly (Website V2 world_front design, approved to proceed
2026-09-19). Proven here, not assumed, against every path that could
possibly carry a record type into a live turn:

  - build_prompt / build_capsule / build_chunks: allowlists
    (CHUNK_DIR_BY_TYPE, and the explicit _one()/_by_type() calls inside
    build_prompt/build_capsule) that simply never name either type - so
    not adding them is sufficient, and this test is the regression proof
    that stays true if anyone ever tries to.
  - build_repository_json: the ONE compiler function that processes every
    OTHER record type by default (a denylist, _PACKAGE_EXCLUDED_RECORD_
    TYPES), so both new types are explicitly added to that set - see its
    own comment for why this matters beyond "build residue": compiled/
    repository.json feeds engine.m4.evidence's _fulltext_fallback_
    candidates(), which has no record-type filter of its own and would
    otherwise surface a world_front/facilitator_brief field as live
    evidence in a real participant turn.
"""
from engine.m2.builders import (
    CHUNK_DIR_BY_TYPE,
    build_capsule,
    build_chunks,
    build_prompt,
    build_repository_json,
)

WORLD_FRONT = {
    "id": "fix.front.fixture-synthetic",
    "world_id": "fixture-synthetic",
    "record_type": "world_front",
    "schema_version": 2,
    "status": "draft",
    "register": "etic",
    "census_id": "fixture-synthetic",
    "skim": {
        "tile": {
            "text": "REPRESENTATIVE_MUST_NEVER_SEE_THIS_WORLD_FRONT_TILE_TEXT",
            "grounded_in": ["fix.term.the-way"],
        }
    },
    "orientation": {
        "relations_summary": {
            "text": "REPRESENTATIVE_MUST_NEVER_SEE_THIS_RELATIONS_SUMMARY",
            "grounded_in": ["fix.term.the-way"],
        }
    },
}

FACILITATOR_BRIEF = {
    "id": "fix.facilitator_brief.fixture-synthetic",
    "world_id": "fixture-synthetic",
    "record_type": "facilitator_brief",
    "schema_version": 2,
    "status": "draft",
    "register": "etic",
    "audience": "facilitator",
    "world_identity": {
        "text": "REPRESENTATIVE_MUST_NEVER_SEE_THIS_FACILITATOR_BRIEF_TEXT",
        "grounded_in": ["fix.term.the-way"],
    },
    "cautions": ["REPRESENTATIVE_MUST_NEVER_SEE_THIS_CAUTION"],
}

CORE = {
    "id": "fix.core.fix",
    "record_type": "world_core",
    "horizon": "A two-source fixture world.",
    "formation_logic": "Formation by reading the two sources it has.",
    "thinness": "Thin on everything except its two sources.",
    "cautions": "Never stand in for a real world.",
}

WITNESS = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "canon_cells": ["C-I"],
    "text": "We did not claim to have seen him ourselves.",
}

RECORDS = {r["id"]: r for r in (WORLD_FRONT, FACILITATOR_BRIEF, CORE, WITNESS)}
REGISTRY_ENTRY = {"display_name": "Fixture World"}
POISON_STRINGS = (
    "REPRESENTATIVE_MUST_NEVER_SEE_THIS_WORLD_FRONT_TILE_TEXT",
    "REPRESENTATIVE_MUST_NEVER_SEE_THIS_RELATIONS_SUMMARY",
    "REPRESENTATIVE_MUST_NEVER_SEE_THIS_FACILITATOR_BRIEF_TEXT",
    "REPRESENTATIVE_MUST_NEVER_SEE_THIS_CAUTION",
)


def test_chunk_dir_by_type_has_no_entry_for_either_type():
    assert "world_front" not in CHUNK_DIR_BY_TYPE
    assert "facilitator_brief" not in CHUNK_DIR_BY_TYPE


def test_build_chunks_emits_no_file_for_either_record():
    chunks = build_chunks(RECORDS)
    for path in chunks:
        assert WORLD_FRONT["id"] not in path
        assert FACILITATOR_BRIEF["id"] not in path


def test_build_prompt_never_contains_world_front_or_facilitator_brief_content():
    prompt = build_prompt(RECORDS, {}, REGISTRY_ENTRY).decode("utf-8")
    for poison in POISON_STRINGS:
        assert poison not in prompt
    assert WORLD_FRONT["id"] not in prompt
    assert FACILITATOR_BRIEF["id"] not in prompt
    # Sanity: an ordinary chunk-feeding/prompt type from the same records
    # dict DOES reach the prompt, so this is a real exclusion, not a bug
    # that would have hidden everything.
    assert CORE["cautions"] in prompt


def test_build_capsule_never_contains_world_front_or_facilitator_brief_content():
    capsule = build_capsule(RECORDS, REGISTRY_ENTRY).decode("utf-8")
    for poison in POISON_STRINGS:
        assert poison not in capsule


def test_build_repository_json_excludes_both_types():
    """The one compiler function with a denylist instead of an allowlist -
    see this module's own docstring for why that makes it the real risk,
    via engine.m4.evidence's fulltext fallback having no type filter of
    its own."""
    repo = build_repository_json(RECORDS)
    import json

    payload = json.loads(repo)
    ids_shipped = {r["id"] for r in payload["records"]}
    assert WORLD_FRONT["id"] not in ids_shipped
    assert FACILITATOR_BRIEF["id"] not in ids_shipped
    # Sanity: an ordinary record from the same dict DOES ship, so this is
    # a real, scoped exclusion.
    assert WITNESS["id"] in ids_shipped
