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


def _moved(root: Path) -> None:
    (root / "tools").mkdir(exist_ok=True)
    (root / "tools" / "moved_paths.txt").write_text(
        "records/<code>/world_front  Build/worlds/<code>/surface/world_front\n", encoding="utf-8")


def test_an_old_path_resolves_while_the_file_exists_at_its_new_home(tmp_path, monkeypatch):
    _moved(tmp_path)
    home = tmp_path / "Build" / "worlds" / "alx" / "surface" / "world_front"
    home.mkdir(parents=True)
    (home / "alx.front.a.md").write_text("x", encoding="utf-8")
    monkeypatch.setattr(check_paths, "REPO", tmp_path)
    assert check_paths.resolves("records/alx/world_front/alx.front.a.md")
    assert check_paths.resolves("records/alx/world_front")


def test_an_old_path_whose_file_is_gone_from_the_new_home_does_not_resolve(tmp_path, monkeypatch):
    _moved(tmp_path)
    (tmp_path / "Build" / "worlds" / "alx" / "surface" / "world_front").mkdir(parents=True)
    monkeypatch.setattr(check_paths, "REPO", tmp_path)
    assert not check_paths.resolves("records/alx/world_front/alx.front.missing.md")


def test_a_path_that_only_shares_the_moved_prefix_is_not_mapped(tmp_path, monkeypatch):
    _moved(tmp_path)
    (tmp_path / "Build" / "worlds" / "alx" / "surface" / "world_front_extra").mkdir(parents=True)
    monkeypatch.setattr(check_paths, "REPO", tmp_path)
    assert not check_paths.resolves("records/alx/world_front_extra")
