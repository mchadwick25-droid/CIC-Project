"""check_paths.resolves: a citation inside a compiled package resolves via the committed manifest."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_paths


def _package(root: Path, files: dict) -> None:
    pkg = root / "packages" / "w" / "2026-01-01T00-00-00Z"
    pkg.mkdir(parents=True)
    (pkg / "manifest.json").write_text(json.dumps({"files": files}), encoding="utf-8")


def test_listed_package_file_resolves_without_the_derived_file(tmp_path, monkeypatch):
    _package(tmp_path, {"compiled/prompt.txt": "sha256:x"})
    monkeypatch.setattr(check_paths, "REPO", tmp_path)
    assert check_paths.resolves("packages/w/2026-01-01T00-00-00Z/compiled/prompt.txt")


def test_unlisted_package_file_does_not_resolve(tmp_path, monkeypatch):
    _package(tmp_path, {"compiled/prompt.txt": "sha256:x"})
    monkeypatch.setattr(check_paths, "REPO", tmp_path)
    assert not check_paths.resolves("packages/w/2026-01-01T00-00-00Z/compiled/other.txt")


def test_package_without_a_manifest_does_not_resolve(tmp_path, monkeypatch):
    monkeypatch.setattr(check_paths, "REPO", tmp_path)
    assert not check_paths.resolves("packages/w/2026-01-01T00-00-00Z/compiled/prompt.txt")
