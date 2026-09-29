"""tools/check_paths.py: a citation into a compiled package resolves against
the package's manifest, and survives the pin timestamp changing on repin."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools import check_paths as cp


@pytest.fixture
def repo(tmp_path, monkeypatch):
    pin = tmp_path / "packages" / "zzz" / "2026-01-02T00-00-00Z"
    pin.mkdir(parents=True)
    manifest = {"files": {"compiled/prompt.txt": "h1", "compiled/chunks/story/a.md": "h2"}}
    (pin / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    (tmp_path / "records" / "worlds").mkdir(parents=True)
    (tmp_path / "records" / "worlds" / "zzz.yaml").write_text(
        'state: admitted\npackage:\n  location: "packages/zzz/2026-01-02T00-00-00Z"\n', encoding="utf-8")
    monkeypatch.setattr(cp, "REPO", tmp_path)
    return tmp_path


def test_a_listed_compiled_file_in_the_live_pin_resolves(repo):
    assert cp.resolves("packages/zzz/2026-01-02T00-00-00Z/compiled/prompt.txt")


def test_a_pin_that_repinning_replaced_resolves_against_the_live_pin(repo):
    assert cp.resolves("packages/zzz/2025-12-31T00-00-00Z/compiled/prompt.txt")


def test_a_folder_the_manifest_lists_files_under_resolves(repo):
    assert cp.resolves("packages/zzz/2025-12-31T00-00-00Z/compiled/chunks/story")


def test_a_file_the_package_never_compiled_does_not_resolve(repo):
    assert not cp.resolves("packages/zzz/2025-12-31T00-00-00Z/compiled/nothing.txt")
    assert not cp.resolves("packages/zzz/2026-01-02T00-00-00Z/compiled/nothing.txt")


def test_a_world_with_no_package_does_not_resolve(repo):
    assert not cp.resolves("packages/nope/2025-12-31T00-00-00Z/compiled/prompt.txt")


def test_a_real_path_still_resolves_and_a_missing_one_does_not(repo):
    assert cp.resolves("records/worlds/zzz.yaml")
    assert not cp.resolves("records/worlds/missing.yaml")
