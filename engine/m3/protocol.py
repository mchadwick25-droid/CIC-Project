"""The battery protocol (spec M3: "the full battery protocol - probe counts
per cell, masking, grading rubric - is stage 4's deliverable-with-spec").

Battery composition, this stage: exactly the 28 sealed probes
(canon/sealed_probes/seals.yaml), one per cell - the fixture-scale battery.
A real world's admission (stage 7, Alexandria) may need more than one probe
per cell to be a serious battery; that grows `canon/sealed_probes/` with
more sealed entries per cell later, not a change to this module's shape.

Draw order: center cells first (canon maintenance rule 5: "the center's
questions are tested first at every admission"), then F1..F6 in spec order,
each family's four registers in I/E/P/T order - both for determinism and so
a masked grader/human reader always sees the same, predictable shape.
"""
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SEALS_PATH = REPO_ROOT / "canon" / "sealed_probes" / "seals.yaml"

_FAMILY_ORDER = ["C", "F1", "F2", "F3", "F4", "F5", "F6"]
_REGISTER_ORDER = ["I", "E", "P", "T"]


def _cell_sort_key(cell: str) -> tuple[int, int]:
    family, register = cell.split("-")
    return _FAMILY_ORDER.index(family), _REGISTER_ORDER.index(register)


def load_seals(seals_path: Path = SEALS_PATH) -> list[dict]:
    return yaml.safe_load(seals_path.read_text())["seals"]


def battery(seals_path: Path = SEALS_PATH) -> list[dict]:
    """Ordered list of {cell, probe_id, sha256, sealed_at, status} - center
    first, then family/register order. One entry per sealed cell; a cell
    with no sealed probe yet is simply absent (never silently skipped
    without being named - callers that need "every cell" should assert
    coverage against engine.m1.canon.valid_cells separately)."""
    seals = load_seals(seals_path)
    return sorted(seals, key=lambda s: _cell_sort_key(s["cell"]))
