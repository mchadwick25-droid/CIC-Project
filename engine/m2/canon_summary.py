"""coverage_summary and declared_floors both feed manifest.json. Kept as
their own small module (not inlined in manifest.py) because coverage.json
(builders.py) needs the identical per-cell classification - both read
through engine.m1.canon.classify_cell, never re-derive it.
"""
from engine.m1 import canon


def coverage_summary(records: dict, fleet: dict) -> dict:
    counts = {"cells_substantive": 0, "cells_honest_limit": 0, "cells_empty": 0}
    for cell in canon.valid_cells(fleet):
        status = canon.classify_cell(cell, records)["status"]
        if status == "substantive":
            counts["cells_substantive"] += 1
        elif status == "honest_limit":
            counts["cells_honest_limit"] += 1
        else:  # empty or multiple_honest_limit - both are gate defects, never silently counted as covered
            counts["cells_empty"] += 1
    return counts


def declared_floors(records: dict) -> dict:
    """Spec principle 10: thresholds come from baselines, never invented.
    No real fleet coverage-floor policy exists yet (that's set at stage 7,
    Alexandria, from a measured baseline) - so this package reports its own
    actual counts rather than copying Artifact-2's illustrative example
    numbers (term:10/story:6/quote:3) as if they were real policy."""
    return {
        "term": sum(1 for r in records.values() if r.get("record_type") == "term"),
        "story": sum(1 for r in records.values() if r.get("record_type") == "story"),
        "quote": sum(1 for r in records.values() if r.get("record_type") == "quote"),
        "demonstration_cells_required": ["C-*", "tag:identity-collision"],
        "enforced": False,
        "note": (
            "actual counts for this package, not a fleet policy - real per-type coverage "
            "floors are set at stage 7 (Alexandria) from a measured baseline, per spec "
            "principle 10"
        ),
    }
