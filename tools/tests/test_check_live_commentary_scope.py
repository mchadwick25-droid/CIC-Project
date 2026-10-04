"""tools/check_live_commentary.py's changed-files scope and its blocking
mode: a change that edits a live file must leave no REWRITE or ROUTE line
in it, and files the change does not touch never fail the run.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools import check_live_commentary as clc

CLEAN = "def add(a, b):\n    return a + b\n"
DIRTY = "# TODO: still an open gap here\ndef add(a, b):\n    return a + b\n"


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *args], cwd=repo, check=True, capture_output=True)


@pytest.fixture
def repo(tmp_path, monkeypatch):
    _git(tmp_path, "init", "-q", "-b", "main")
    (tmp_path / "engine").mkdir()
    (tmp_path / "engine" / "untouched.py").write_text(DIRTY, encoding="utf-8")
    (tmp_path / "engine" / "edited.py").write_text(CLEAN, encoding="utf-8")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "base")
    monkeypatch.setattr(clc, "REPO", tmp_path)
    return tmp_path


def test_surface_of_maps_a_path_to_its_surface():
    assert clc.surface_of(Path("engine/m1/gates.py")) == "engine"
    assert clc.surface_of(Path("Build/worlds/syr/x.md")) == "worlds"
    assert clc.surface_of(Path("README.md")) is None


def test_only_added_and_modified_files_are_in_scope(repo):
    (repo / "engine" / "edited.py").write_text(CLEAN + "\n", encoding="utf-8")
    (repo / "engine" / "new.py").write_text(CLEAN, encoding="utf-8")
    names = {p.name for p in clc.changed_files(repo, "main")}
    assert names == {"edited.py", "new.py"}


def test_a_legacy_hit_in_an_untouched_file_does_not_fail_the_run(repo):
    (repo / "engine" / "edited.py").write_text(CLEAN + "\n", encoding="utf-8")
    assert clc.main(["--base", "main", "--enforce"]) == 0


def test_a_hit_in_an_edited_file_fails_the_run(repo):
    (repo / "engine" / "edited.py").write_text(DIRTY, encoding="utf-8")
    assert clc.main(["--base", "main", "--enforce"]) == 1


def test_editing_a_file_that_already_carried_commentary_fails_until_it_is_removed(repo):
    path = repo / "engine" / "untouched.py"
    path.write_text(DIRTY + "\n", encoding="utf-8")
    assert clc.main(["--base", "main", "--enforce"]) == 1
    path.write_text(CLEAN, encoding="utf-8")
    assert clc.main(["--base", "main", "--enforce"]) == 0


def test_without_enforce_the_scan_is_a_report_and_exits_zero(repo):
    (repo / "engine" / "edited.py").write_text(DIRTY, encoding="utf-8")
    assert clc.main(["--base", "main"]) == 0


def test_enforce_without_a_base_is_refused(repo):
    with pytest.raises(SystemExit):
        clc.main(["--enforce"])


def test_a_file_moved_unchanged_between_live_surfaces_is_not_an_edit(repo):
    _git(repo, "checkout", "-q", "-b", "work")
    (repo / "records").mkdir()
    _git(repo, "mv", "engine/untouched.py", "records/untouched.py")
    _git(repo, "commit", "-q", "-m", "move")
    assert clc.changed_files(repo, "main") == []
    assert clc.main(["--base", "main", "--enforce"]) == 0


def test_a_file_moved_and_edited_is_in_scope(repo):
    _git(repo, "checkout", "-q", "-b", "work")
    (repo / "records").mkdir()
    _git(repo, "mv", "engine/untouched.py", "records/untouched.py")
    (repo / "records" / "untouched.py").write_text(DIRTY + "x = 1\n", encoding="utf-8")
    _git(repo, "commit", "-q", "-am", "move and edit")
    assert {p.as_posix() for p in clc.changed_files(repo, "main")} == {(repo / "records" / "untouched.py").as_posix()}
    assert clc.main(["--base", "main", "--enforce"]) == 1


def test_a_file_moved_onto_a_live_surface_from_outside_is_in_scope(repo):
    (repo / "notes").mkdir()
    (repo / "notes" / "draft.py").write_text(DIRTY, encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "draft")
    _git(repo, "checkout", "-q", "-b", "work")
    _git(repo, "mv", "notes/draft.py", "engine/draft.py")
    _git(repo, "commit", "-q", "-m", "promote")
    assert {p.name for p in clc.changed_files(repo, "main")} == {"draft.py"}
