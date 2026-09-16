"""Hermetic (no live model call) tests for the lazy world loader, run
against the REAL committed fixture package (whichever package_dir/manifest_hash
records/worlds/fix.yaml currently registers) - not a synthetic fixture of
its own, since the whole point is proving the loader against a real,
previously-compiled package."""
from pathlib import Path

import pytest

from engine.m1.registry import load_registry
from engine.m4.world_loader import LazyWorldLoader, PackageRefused

REPO_ROOT = Path(__file__).resolve().parents[3]


def _fix_world_registry_entry() -> dict:
    return load_registry()["fix"]


def test_cold_load_reads_and_verifies_real_package():
    entry = _fix_world_registry_entry()
    loader = LazyWorldLoader()
    assert not loader.is_resident("fix")

    world, timing = loader.load(
        "fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    assert timing.cache_hit is False
    assert timing.seconds >= 0
    assert loader.is_resident("fix")
    assert world.world_key == "fix"
    assert "Vera" in world.prompt_text
    assert len(world.repository["records"]) > 0


def test_second_load_is_a_cache_hit_not_a_second_read():
    entry = _fix_world_registry_entry()
    loader = LazyWorldLoader()
    world1, timing1 = loader.load(
        "fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    world2, timing2 = loader.load(
        "fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    assert timing1.cache_hit is False
    assert timing2.cache_hit is True
    assert world1 is world2  # same object - not re-parsed


def test_unload_evicts_and_a_later_load_is_cold_again():
    entry = _fix_world_registry_entry()
    loader = LazyWorldLoader()
    loader.load("fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
    assert loader.is_resident("fix")

    unload_timing = loader.unload("fix")
    assert unload_timing.cache_hit is False
    assert not loader.is_resident("fix")

    _world, reload_timing = loader.load(
        "fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    assert reload_timing.cache_hit is False  # cold again - unload actually evicted, wasn't a no-op


def test_unload_of_never_loaded_world_is_a_harmless_no_op():
    loader = LazyWorldLoader()
    timing = loader.unload("never-loaded")
    assert timing.cache_hit is False


def test_wrong_manifest_hash_refuses_to_serve():
    entry = _fix_world_registry_entry()
    loader = LazyWorldLoader()
    with pytest.raises(PackageRefused):
        loader.load("fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash="sha256:0000000000000000000000000000000000000000000000000000000000000000")


def test_no_idle_eviction_by_default():
    """max_idle_seconds=None (the default) never evicts, however old a
    resident world gets - the long-standing behavior this class always
    had, unchanged unless a deploy opts in (WO-2)."""
    entry = _fix_world_registry_entry()
    loader = LazyWorldLoader()
    loader.load("fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
    loader._last_accessed[("fix", entry["package"]["manifest_hash"])] -= 10_000_000
    _world, timing = loader.load(
        "fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    assert timing.cache_hit is True  # still resident - no policy configured, no eviction


def test_idle_world_evicted_on_next_load_call():
    """With a policy configured, a world idle past the threshold is gone
    by the time anything next calls load() - eviction is opportunistic,
    not on a timer, per this class's own docstring."""
    entry = _fix_world_registry_entry()
    loader = LazyWorldLoader(max_idle_seconds=1.0)
    loader.load("fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])
    assert loader.is_resident("fix")

    loader._last_accessed[("fix", entry["package"]["manifest_hash"])] -= 2.0  # backdate past the threshold
    _world, timing = loader.load(
        "fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    assert timing.cache_hit is False  # evicted, then reloaded cold


def test_fresh_world_survives_while_a_stale_one_is_evicted():
    """Eviction is per-pin, not all-or-nothing - a world well within its
    idle budget is untouched by another one going stale."""
    entry = _fix_world_registry_entry()
    loader = LazyWorldLoader(max_idle_seconds=100.0)
    cache_key = ("fix", entry["package"]["manifest_hash"])
    loader.load("fix", package_dir=REPO_ROOT / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"])

    other_key = ("also-fix", entry["package"]["manifest_hash"])
    loader._resident[other_key] = loader._resident[cache_key]
    loader._last_accessed[other_key] = loader._last_accessed[cache_key] - 200.0  # already stale

    evicted = loader._evict_idle()
    assert evicted == ["also-fix"]
    assert loader.is_resident("fix")
    assert not loader.is_resident("also-fix")
