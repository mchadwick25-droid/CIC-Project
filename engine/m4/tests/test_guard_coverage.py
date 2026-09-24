"""Per-world guard coverage (engine/m4/reports/grounding_fooling_measure.py
--world). Runs against the fix fixture world's own records - compiled in
memory, so no package on disk is needed - plus one synthetic claim_guards
entry where the fixture world carries none.
"""
import copy
import json

import pytest

from engine.m1 import loader
from engine.m4.reports import grounding_fooling_measure as gfm

STORY_ID = "fix.story.the-long-road"
STORY_GUARD = "participant is asking which family paid the cost - the scroll does not say, and the Representative must not supply it"


@pytest.fixture(autouse=True)
def _fresh_repo_cache():
    gfm._REPO_CACHE.clear()
    yield
    gfm._REPO_CACHE.clear()


@pytest.fixture
def guarded_fix(monkeypatch):
    """The fix world with one claim_guards entry added to its story."""
    real = loader.load_world_records

    def load(world_key, *args, **kwargs):
        records = copy.deepcopy(real(world_key, *args, **kwargs))
        if world_key == "fix":
            records[STORY_ID]["claim_guards"] = [STORY_GUARD]
        return records

    monkeypatch.setattr(loader, "load_world_records", load)


def _write(tmp_path, payload):
    path = tmp_path / gfm.WORLD_FLAT_ASSERTIONS_NAME
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_unphrased_fields_are_listed_not_skipped(tmp_path):
    report = gfm.run_guard_coverage("fix", world_file=tmp_path / "absent.json")
    assert [r["source"] for r in report["rows"]] == ["contested_claim"]
    assert report["rows"][0]["assertion_origin"] == "verbatim"
    unphrased = {(u["source"], u["id"]) for u in report["unphrased"]}
    assert unphrased == {
        ("honest_limit", "fix.limit.outsiders-fate"),
        ("honest_limit", "fix.limit.scholarly-scrutiny"),
        ("honest_limit", "fix.limit.trinity-language"),
        ("honest_limit", "fix.limit.unbuilt-appendix-a-cells"),
        ("absent_detail", STORY_ID),
    }
    assert report["complete"] is False
    assert all(u["field_text"] for u in report["unphrased"])


def test_world_file_supplies_phrasings(tmp_path):
    records = loader.load_world_records("fix")
    limits = [rid for rid, r in records.items() if r["record_type"] == "honest_limit"]
    world_file = _write(tmp_path, {
        "honest_limit": {rid: "We hold the full answer to this in our own sources." for rid in limits},
        "absent_detail": {STORY_ID: "The scroll names the family and says the cost lasted seven years."},
    })
    report = gfm.run_guard_coverage("fix", world_file=world_file)
    assert report["complete"] is True
    assert report["n"] == 1 + len(limits) + 1
    assert {r["assertion_origin"] for r in report["rows"] if r["source"] != "contested_claim"} == {"world_authored"}
    for row in report["rows"]:
        assert row["verdict"] in ("ok", "withhold") and row["why"]
        assert row["id"] in records


def test_needs_decision_is_passing_and_uncovered(tmp_path):
    report = gfm.run_guard_coverage("fix", world_file=tmp_path / "absent.json")
    assert report["needs_decision"] == [r for r in report["rows"] if r["verdict"] == "ok" and not r["covered"]]
    assert report["needs_decision_count"] == len(report["needs_decision"])


def test_guard_entry_without_phrasing_is_unphrased(guarded_fix, tmp_path):
    report = gfm.run_guard_coverage("fix", world_file=tmp_path / "absent.json")
    assert ("guard", STORY_ID, STORY_GUARD) in {(u["source"], u["id"], u["field_text"]) for u in report["unphrased"]}


def test_own_guard_covers_its_barred_claim(guarded_fix, tmp_path):
    world_file = _write(tmp_path, {
        "guard": {STORY_ID: ["The scroll tells us exactly which family paid the cost."]},
        "absent_detail": {STORY_ID: "The scroll names the family who paid the cost of the long road."},
    })
    report = gfm.run_guard_coverage("fix", world_file=world_file)
    by_source = {r["source"]: r for r in report["rows"] if r["id"] == STORY_ID}
    assert by_source["guard"]["covered"] is True
    assert by_source["guard"]["guard_proximity"]
    # the story's absent_detail assertion names the same barred claim, so the
    # same guard covers it too - it drops out of needs_decision
    assert by_source["absent_detail"]["covered"] is True
    assert all(r["id"] != STORY_ID for r in report["needs_decision"])


def test_covers_is_the_runtime_guard_proximity_rule():
    guarded = {"id": "x.story.a", "record_type": "story", "text": "A story.", "claim_guards": [STORY_GUARD]}
    other = {"id": "x.story.b", "record_type": "story", "text": "Another story."}
    recs = {guarded["id"]: guarded, other["id"]: other}
    barred = "The scroll tells us exactly which family paid the cost."
    assert gfm.guard_proximity_on(barred, "x.story.a", recs)
    # a guard on a different record never covers
    assert gfm.guard_proximity_on(barred, "x.story.b", recs) == []
    # one shared word is below the runtime floor
    assert gfm.guard_proximity_on("The family walked the long road.", "x.story.a", recs) == []


def test_unknown_world_refuses():
    with pytest.raises(SystemExit):
        gfm.run_guard_coverage("no-such-world")


def test_fleet_guard_rows_read_claim_guards():
    """R11 moved every guard line into claim_guards; the fleet Corpus B must
    read that field, and every fleet guard line must have its hand-authored
    assertion - an unmatched one would drop out of the fleet run silently."""
    hits = gfm.collect_guard_lines()
    assert hits
    assert {h["id"] for h in hits} == set(gfm.GUARD_FLAT_ASSERTIONS)
