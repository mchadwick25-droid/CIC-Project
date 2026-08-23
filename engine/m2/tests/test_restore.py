"""Compiled packages are derived and no longer in git. The property that
makes that safe: a checkout holding only records/, worlds.yaml and each
package's manifest.json can rebuild the exact package it is pinned to."""
import json
import pathlib

import yaml

from engine.m1.registry import load_registry
from engine.m2.checks import restore_package, staleness_sweep


def _strip_to_manifest(location: pathlib.Path) -> int:
    removed = 0
    for p in sorted(location.rglob("*"), reverse=True):
        if p.is_file() and p.name != "manifest.json":
            p.unlink(); removed += 1
        elif p.is_dir() and not any(p.iterdir()):
            p.rmdir()
    return removed


def test_a_checkout_with_only_manifests_can_rebuild_the_pinned_package(tmp_path):
    reg = load_registry()
    entry = reg["fix"]
    location = pathlib.Path(entry["package"]["location"])
    manifest = json.loads((location / "manifest.json").read_text())

    removed = _strip_to_manifest(location)
    assert removed > 0
    assert sorted(p.name for p in location.rglob("*")) == ["manifest.json"]

    result = restore_package("fix", registry=reg)
    assert result["restored"] is True
    # every file is back, and every hash matches the committed contract
    for rel, digest in manifest["files"].items():
        import hashlib
        assert "sha256:" + hashlib.sha256((location / rel).read_bytes()).hexdigest() == digest


def test_the_staleness_guard_needs_no_package_bytes():
    """It compares a recompile against the committed manifest, so it still
    fires on a checkout that has never restored anything."""
    location = pathlib.Path(load_registry()["fix"]["package"]["location"])
    _strip_to_manifest(location)
    results = staleness_sweep()
    assert results["fix"]["stale"] is False
    restore_package("fix")  # leave the tree as we found it


def test_only_manifests_are_tracked_under_packages():
    """The whole point: 10,150 files became 7."""
    ignore = pathlib.Path(".gitignore").read_text()
    assert "packages/*/*/**" in ignore
    assert "!packages/*/*/manifest.json" in ignore
