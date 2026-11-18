"""The held-out half is read by the trial's final scoring only. Any other
code that names the held-out file fails here."""
from pathlib import Path

from goldset.common import REPO_ROOT

ALLOWED = {"goldset/split.py", "goldset/trial.py", "goldset/tests/test_isolation.py"}
SCANNED = ("engine", "Sandbox", "tools", "cic/engine")
NEEDLE = "heldout" + ".jsonl"


def test_only_the_trial_reads_the_heldout_half():
    offenders = []
    for top in SCANNED:
        for path in sorted((REPO_ROOT / top).rglob("*.py")):
            rel = path.relative_to(REPO_ROOT / "Sandbox" / "Answering-From-Sources").as_posix() if "Answering-From-Sources" in path.parts else None
            if rel in ALLOWED:
                continue
            if NEEDLE in path.read_text(encoding="utf-8", errors="replace"):
                offenders.append(str(path.relative_to(REPO_ROOT)))
    assert offenders == []
