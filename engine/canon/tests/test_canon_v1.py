import re
from pathlib import Path

import yaml

from engine.canon.check_seal_isolation import find_violations
from engine.m1.loader import load_fleet_records

REPO_ROOT = Path(__file__).resolve().parents[3]
ALL_CELLS = {f"{fam}-{reg}" for fam in ["C", "F1", "F2", "F3", "F4", "F5", "F6"] for reg in ["I", "E", "P", "T"]}


def test_every_cell_has_at_least_one_canon_question():
    fleet = load_fleet_records()
    cells = {r["cell"] for r in fleet.values() if r.get("record_type") == "canon_question"}
    assert cells == ALL_CELLS


def test_every_cell_has_exactly_one_sealed_probe():
    seals = yaml.safe_load((REPO_ROOT / "canon" / "sealed_probes" / "seals.yaml").read_text())["seals"]
    cells = [s["cell"] for s in seals]
    assert set(cells) == ALL_CELLS
    assert len(cells) == len(set(cells)), "a cell has more than one sealed probe"


def test_sealed_probes_are_not_verbatim_canon_strings():
    fleet = load_fleet_records()
    canon_texts = {r["id"]: r["text"] for r in fleet.values() if r.get("record_type") == "canon_question"}
    seals = yaml.safe_load((REPO_ROOT / "canon" / "sealed_probes" / "seals.yaml").read_text())["seals"]
    for seal in seals:
        plaintext = (REPO_ROOT / "canon" / "sealed_probes" / "plaintext" / f"{seal['probe_id']}.md").read_text()
        body = plaintext.split("---", 2)[-1].strip()
        cq_id = re.search(r"paraphrase_of: (\S+)", plaintext).group(1)
        assert body != canon_texts[cq_id].strip(), f"{seal['probe_id']} is verbatim, not a paraphrase"


def test_seal_hashes_match_current_plaintext():
    import hashlib

    seals = yaml.safe_load((REPO_ROOT / "canon" / "sealed_probes" / "seals.yaml").read_text())["seals"]
    for seal in seals:
        plaintext = (REPO_ROOT / "canon" / "sealed_probes" / "plaintext" / f"{seal['probe_id']}.md").read_bytes()
        digest = f"sha256:{hashlib.sha256(plaintext).hexdigest()}"
        assert digest == seal["sha256"], f"{seal['probe_id']} plaintext was edited after sealing"


def test_seal_isolation_guard_is_clean():
    assert find_violations() == []
