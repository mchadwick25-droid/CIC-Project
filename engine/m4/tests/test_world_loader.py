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
