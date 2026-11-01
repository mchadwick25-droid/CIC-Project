"""The facts about a vendored edition reach the package on the source's own entry, from its corpus-map row."""
import json

from engine.m2 import edition_facts
from engine.m2.builders import build_repository_json
from engine.m2.compiler import compile_and_hash

ROWS = [
    {"row_id": "r1", "translator": {"name": "A. Translator", "source": "file line 3", "formation_confidence": "Documented"},
     "edition_date": {"formation_confidence": "unknown", "checked": "title page"}},
    {"row_id": "r2", "work": "no facts on this row"},
    {"row_id": "r3", "translator": "not a mapping"},
]
RECORDS = {
    "w.source.a": {"id": "w.source.a", "record_type": "source", "shelf_row": "r1"},
    "w.source.b": {"id": "w.source.b", "record_type": "source", "shelf_row": "r2"},
    "w.source.c": {"id": "w.source.c", "record_type": "source", "shelf_row": "r3"},
    "w.source.d": {"id": "w.source.d", "record_type": "source"},
    "w.term.x": {"id": "w.term.x", "record_type": "term", "shelf_row": "r1"},
}


def test_only_a_source_whose_row_holds_a_fact_mapping_gets_facts(monkeypatch):
    monkeypatch.setattr(edition_facts, "read_bucket_rows", lambda census_id: ROWS)
    assert edition_facts.source_edition_facts(RECORDS, "w") == {"w.source.a": {"translator": ROWS[0]["translator"], "edition_date": ROWS[0]["edition_date"]}}


def test_a_world_with_no_census_id_gets_nothing():
    assert edition_facts.source_edition_facts(RECORDS, None) == {}


def test_the_repository_entry_carries_the_facts_only_where_given():
    facts = {"w.source.a": {"translator": {"name": "A", "formation_confidence": "Documented"}}}
    records = {k: {**v, "status": "ready"} for k, v in RECORDS.items() if k in ("w.source.a", "w.source.b")}
    entries = {r["id"]: r for r in json.loads(build_repository_json(records, facts))["records"]}
    assert entries["w.source.a"]["edition_facts"] == facts["w.source.a"]
    assert "edition_facts" not in entries["w.source.b"]
    assert json.loads(build_repository_json(records))["records"] == json.loads(build_repository_json(records, {}))["records"]


def test_lpc_sources_carry_their_row_facts_and_a_world_without_them_is_unchanged():
    def sources(world):
        package, _ = compile_and_hash(world_key=world, package_id="TEST", records_commit="TEST", compiler_version="TEST")
        return [r for r in json.loads(package["compiled/repository.json"])["records"] if r["record_type"] == "source"]
    lpc = [r for r in sources("lpc") if "edition_facts" in r]
    assert lpc and all(set(r["edition_facts"]) <= {"translator", "edition_date"} for r in lpc)
    assert not [r for r in sources("alx") if "edition_facts" in r]
