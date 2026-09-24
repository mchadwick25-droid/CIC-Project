"""engine.m2.site_cli.site_staleness_sweep - the CI-shaped check for the
Website V2 world_front compiler stage. Uses the real fixture world's
records (records/fix/**, which already carries a real, minimal
world_front record - fix.front.fixture-synthetic) against a throwaway
site-data directory, so this never touches the real cic-website/data/
worlds/ tree.
"""
import json

from engine.m1.registry import load_registry

from engine.m2.site_cli import compile_site_json_for_world, site_staleness_sweep

REGISTRY = load_registry()


def test_a_world_with_no_committed_site_json_is_absent_from_the_sweep(tmp_path):
    """Not a pass, not a fail - simply nothing to check yet. Every real
    world today has no cic-website/data/worlds/<census_id>.json at all
    (content migration is a separate, later stage), so the sweep must
    stay silent about all of them, not report them clean."""
    results = site_staleness_sweep(registry=REGISTRY, site_data_dir=tmp_path)
    assert results == {}


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
