"""The facts about a vendored edition that a source card prints: who translated
or edited it and the year the edition's own file states, each with its
confidence and where it was found, or where it was looked for and not found.

The facts live on the source's corpus-map row (the row its `shelf_row` names).
They reach the package as `edition_facts` on that source's entry in
compiled/repository.json, so a card is built from the package alone. A source
whose row carries neither field gets no `edition_facts`; nothing is supplied
for it.
"""
from engine.m9.loader import read_bucket_rows

EDITION_FIELDS = ("translator", "edition_date")


def source_edition_facts(records: dict, census_id: str | None) -> dict[str, dict]:
    """source record id -> {translator?, edition_date?}, copied from the row
    the source's `shelf_row` names in the world's bucket."""
    if not census_id:
        return {}
    rows = {row.get("row_id"): row for row in read_bucket_rows(census_id) if row.get("row_id")}
    out = {}
    for record in records.values():
        if record.get("record_type") != "source":
            continue
        row = rows.get(record.get("shelf_row")) or {}
        facts = {field: row[field] for field in EDITION_FIELDS if isinstance(row.get(field), dict)}
        if facts:
            out[record["id"]] = facts
    return out
