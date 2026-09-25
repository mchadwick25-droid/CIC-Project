"""engine.m2.site_cli.site_staleness_sweep - the CI-shaped check for the
Website V2 world_front compiler stage. Uses the real fixture world's
records (records/fix/**, which already carries a real, minimal
world_front record - fix.front.fixture-synthetic) against a throwaway
site-data directory, so this never touches the real cic-website/data/
worlds/ tree.
"""
import json

from engine.m1 import cross_world
from engine.m1.registry import load_registry

from engine.m2.site_cli import compile_site_json_for_world, site_staleness_sweep

REGISTRY = load_registry()


def test_a_not_yet_admitted_world_with_no_committed_site_json_stays_silent(tmp_path):
    """Not a pass, not a fail - simply nothing to check yet for a world
    that hasn't reached admitted/open, so participants cannot reach it
    regardless."""
    registry = {"w": {"census_id": "w-census", "state": "built"}}
    results = site_staleness_sweep(registry=registry, site_data_dir=tmp_path)
    assert results == {}


def test_an_admitted_world_with_no_committed_site_json_is_reported_stale(tmp_path):
    """An admitted/open world is participant-reachable, so a missing
    compiled site JSON needs a visible signal, not silence."""
    registry = {"w": {"census_id": "w-census", "state": "admitted"}}
    results = site_staleness_sweep(registry=registry, site_data_dir=tmp_path)
    assert results["w"]["stale"] is True
    assert "admitted" in results["w"]["reason"]


def test_a_waived_missing_site_json_is_reported_not_stale(tmp_path, monkeypatch):
    """engine.m1.cross_world's own required-site-json/<world> waiver is
    the ONE place this exception is recorded - site_staleness_sweep reads
    it rather than keeping a second copy, so a live waiver there reports
    stale: False with the waiver text attached, not a second silent
    exception this sweep would have to remember on its own."""
    monkeypatch.setitem(cross_world.ACCEPTED_OPEN, "required-site-json/w", "test waiver text")
    registry = {"w": {"census_id": "w-census", "state": "admitted"}}
    results = site_staleness_sweep(registry=registry, site_data_dir=tmp_path)
    assert results["w"]["stale"] is False
    assert results["w"]["waived"] == "test waiver text"


def test_removing_the_waiver_makes_the_sweep_fail_again(tmp_path, monkeypatch):
    """The waiver is read live from ACCEPTED_OPEN, not cached or baked in
    - deleting it restores the unwaived stale: True result immediately."""
    monkeypatch.setitem(cross_world.ACCEPTED_OPEN, "required-site-json/w", "test waiver text")
    registry = {"w": {"census_id": "w-census", "state": "admitted"}}
    waived = site_staleness_sweep(registry=registry, site_data_dir=tmp_path)
    assert waived["w"]["stale"] is False

    monkeypatch.delitem(cross_world.ACCEPTED_OPEN, "required-site-json/w")
    unwaived = site_staleness_sweep(registry=registry, site_data_dir=tmp_path)
    assert unwaived["w"]["stale"] is True
    assert "waived" not in unwaived["w"]


def test_a_matching_committed_site_json_is_reported_not_stale(tmp_path):
    compiled = compile_site_json_for_world(
        "fix", compiler_version="test-version", records_commit="test-commit"
    )
    assert compiled is not None  # the fixture world DOES have a world_front record
    (tmp_path / "fixture-synthetic.json").write_bytes(compiled)

    results = site_staleness_sweep(registry=REGISTRY, site_data_dir=tmp_path)
    assert results["fix"] == {"stale": False, "diff": []}


def test_a_committed_site_json_that_no_longer_matches_a_recompile_is_stale(tmp_path):
    compiled = json.loads(
        compile_site_json_for_world("fix", compiler_version="test-version", records_commit="test-commit")
    )
    compiled["skim"]["tile"]["text"] = "this no longer matches the real fixture record"
    (tmp_path / "fixture-synthetic.json").write_bytes(json.dumps(compiled).encode("utf-8"))

    results = site_staleness_sweep(registry=REGISTRY, site_data_dir=tmp_path)
    assert results["fix"]["stale"] is True
    assert "skim" in results["fix"]["diff"]


def test_a_missing_generated_by_header_is_reported_stale(tmp_path):
    (tmp_path / "fixture-synthetic.json").write_text(json.dumps({"no": "header"}), encoding="utf-8")
    results = site_staleness_sweep(registry=REGISTRY, site_data_dir=tmp_path)
    assert results["fix"]["stale"] is True
    assert "_generated_by" in results["fix"]["reason"]


def test_a_nonexistent_site_data_dir_returns_an_empty_sweep(tmp_path):
    results = site_staleness_sweep(registry=REGISTRY, site_data_dir=tmp_path / "does-not-exist")
    assert results == {}
