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


def test_a_worlds_build_scripts_are_not_a_live_surface():
    assert clc.surface_of(Path("Build/worlds/lpc/scripts/wb_lpc_s21.py")) is None
    assert clc.surface_of(Path("Build/worlds/lpc/Doc_01_x.md")) == "worlds"
    assert clc.is_world_build_tool(Path("Build/worlds/syr/scripts/gen.py"))
    assert not clc.is_world_build_tool(Path("Build/worlds/_cross-world/scripts-note.md"))


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


def test_verbatim_copies_of_source_documents_are_not_a_live_surface():
    assert clc.surface_of(Path("Build/reference/text-renderings/CiC_L1_Constitution_V2_2.md")) is None
    assert clc.is_verbatim_copy(Path("Build/reference/text-renderings/x.md"))
    assert not clc.is_verbatim_copy(Path("Build/reference/method/x.md"))
