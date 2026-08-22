"""The set of valid canon cells is derived from the fleet's own
canon_question records - never hardcoded (law 4: one registry; everything
derived). At stage 0.6 this is the 8-cell fixture-scope subset; stage 3
grows it to the full 28 without any code here changing.

classify_cell() is the single implementation of the coverage rule (Artifact-1
SS6: "for every canon cell, every open world has >=1 doctrinal_witness/term/
story/quote OR exactly one honest_limit - never neither, never blank"). Both
the M1 canon-coverage gate and the M2 coverage.json builder call this one
function rather than each re-deriving the rule (a landmine this project has
already named: "duplicated logic fixed in one copy").

cell_keywords() is the same discipline applied to the M4 Live-Generation
Design's Stage A (LIVE-GENERATION-DESIGN.md §3.2): engine.m4.evidence
scores a live turn's asks against it at turn time, and engine.m2.builders'
compiled/indexes/canon-map.json caches its output at compile time - one
derivation, owned once, so a live Stage A match and the compiled cache can
never silently diverge.
"""
from engine.m1.gates_experimental import _content_words


def valid_cells(fleet_records: dict[str, dict]) -> set[str]:
    return {
        r["cell"]
        for r in fleet_records.values()
        if r.get("record_type") == "canon_question" and r.get("cell")
    }


def cell_keywords(fleet_records: dict[str, dict]) -> dict[str, set[str]]:
    """Per-cell content-word corpus, built from every canon_question
    record's own `text` field - the small per-cell keyword list §3.2
    names as what Stage A scores an ask against."""
    words: dict[str, set[str]] = {}
    for record in fleet_records.values():
        if record.get("record_type") != "canon_question" or not record.get("cell"):
            continue
        words.setdefault(record["cell"], set()).update(_content_words(record.get("text") or ""))
    return words


def substantive_types() -> set[str]:
    return {"doctrinal_witness", "term", "story", "quote"}


def classify_cell(cell: str, records: dict[str, dict]) -> dict:
    """Returns {"status": ..., "substantive": [ids], "honest_limit": [ids]}.
    status is one of: "substantive", "honest_limit", "multiple_honest_limit"
    (a gate defect - more than one honest_limit claims the same cell), or
    "empty" (a gate defect - neither route covers the cell)."""
    substantive = sorted(
        rid
        for rid, r in records.items()
        if r.get("record_type") in substantive_types() and cell in (r.get("canon_cells") or [])
    )
    honest_limit = sorted(
        rid
        for rid, r in records.items()
        if r.get("record_type") == "honest_limit" and cell in (r.get("canon_cells") or [])
    )
    if substantive:
        status = "substantive"
    elif len(honest_limit) == 1:
        status = "honest_limit"
    elif len(honest_limit) > 1:
        status = "multiple_honest_limit"
    else:
        status = "empty"
    return {"status": status, "substantive": substantive, "honest_limit": honest_limit}
