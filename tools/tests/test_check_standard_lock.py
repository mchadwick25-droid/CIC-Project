import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_standard_lock as lock  # noqa: E402

PATTERN = lock.FOLDER + "Brief-Kit/Standard.md"


def run(repo, *args):
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


def write(repo, rel, text):
    path = Path(repo, rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_repo(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    run(repo, "init", "-q", "-b", "main")
    run(repo, "config", "user.email", "t@example.invalid")
    run(repo, "config", "user.name", "t")
    write(repo, PATTERN, "The standard.\n")
    write(repo, lock.DECISION_LOG, "# Decision Log\n\n## 2026-11-01 — An old entry (Mark)\n")
    run(repo, "add", "-A")
    run(repo, "commit", "-q", "-m", "base")
    run(repo, "checkout", "-q", "-b", "pr")
    write(repo, PATTERN, "The standard, changed.\n")
    return repo


def check_in(repo):
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        return lock.check("main")
    finally:
        os.chdir(cwd)


def test_passes_with_a_new_entry_quoting_mark(tmp_path):
    repo = make_repo(tmp_path)
    log = Path(repo, lock.DECISION_LOG).read_text(encoding="utf-8")
    write(repo, lock.DECISION_LOG, log + "\n## 2026-11-16 — The standard changes\n\n"
          "**Decided (Mark, 2026-11-16).** He answered: “yes, change it”.\n")
    run(repo, "commit", "-qam", "pr")
    assert check_in(repo) == 0


def test_fails_without_a_new_entry_quoting_mark(tmp_path):
    repo = make_repo(tmp_path)
    log = Path(repo, lock.DECISION_LOG).read_text(encoding="utf-8")
    write(repo, lock.DECISION_LOG, log + "\n## 2026-11-16 — The standard changes (coordinator)\n\n"
          "**Decided (coordinator).** The standard is tightened.\n")
    run(repo, "commit", "-qam", "pr")
    assert check_in(repo) == 1
