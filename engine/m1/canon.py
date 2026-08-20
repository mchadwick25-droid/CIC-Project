"""The set of valid canon cells is derived from the fleet's own
canon_question records - never hardcoded (law 4: one registry; everything
derived). At stage 0.6 this is the 8-cell fixture-scope subset; stage 3
grows it to the full 28 without any code here changing.
"""


def valid_cells(fleet_records: dict[str, dict]) -> set[str]:
    return {
        r["cell"]
        for r in fleet_records.values()
        if r.get("record_type") == "canon_question" and r.get("cell")
    }


def substantive_types() -> set[str]:
    return {"doctrinal_witness", "term", "story", "quote"}
