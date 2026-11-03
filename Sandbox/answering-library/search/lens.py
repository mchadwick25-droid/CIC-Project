"""The lens: the passages a world's search may reach. A hard filter, applied before any ranking.

A passage is in a world's lens when the world's own corpus-map rows bind it to exactly one row (the division test the
the corpus-map rows use), it has an English reading, and it is not apparatus:

  a file with one row of the world         every passage of the file is bound to that row;
  a file with several rows of the world    a passage is bound to the one row whose `locus_ids` hold its division locus
                                           (or `whole-file`); a passage that no row, or more than one row, claims is only
                                           on the shelf at file level, the work is not known, and it is outside.

The rows are read from the corpus map, not from the index's own row tie, which ties every passage of a multi-row file to all
of the file's rows. A caller that knows the rows whose dated window sits inside the world's window passes them as
`window_rows`; neither the index nor the rows give a dated window here.
"""
import sqlite3
from pathlib import Path
from typing import Collection, Mapping, Sequence

WHOLE_FILE = "whole-file"


def world_rows(world: str) -> dict[str, list[dict]]:
    """The world's corpus-map rows by vendored file: row_id and locus_ids of each."""
    from index.catalog import TEXTS_DIR, _engine_imports

    load_registry, read_bucket_rows = _engine_imports()
    by_file: dict[str, list[dict]] = {}
    for row in read_bucket_rows(load_registry()[world]["census_id"]):
        name = row.get("source_file")
        if name and (TEXTS_DIR / name).is_file():
            by_file.setdefault(name, []).append({"row_id": row.get("row_id"), "locus_ids": row.get("locus_ids")})
    return by_file


def bound_row(rows: Sequence[dict], division_locus: str) -> str | None:
    """The one row of the file that claims the division, or None when no row or several rows do."""
    if len(rows) == 1:
        return rows[0]["row_id"] or ""
    claimed = [r for r in rows if r.get("locus_ids") and (WHOLE_FILE in r["locus_ids"] or division_locus in r["locus_ids"])]
    return (claimed[0]["row_id"] or "") if len(claimed) == 1 else None


def lens_ids(db_path: Path, rows: Mapping[str, Sequence[dict]], window_rows: Collection[str] | None = None) -> list[int]:
    """The index's internal ids of the passages in the lens, ascending. `rows` is the world's rows by file (world_rows)."""
    if not rows:
        return []
    allowed = None if window_rows is None else set(window_rows)
    names = sorted(rows)
    out: list[int] = []
    connection = sqlite3.connect(db_path)
    try:
        for start in range(0, len(names), 500):
            chunk = names[start:start + 500]
            sql = (f"SELECT id, file, division_locus FROM passages WHERE language = 'eng' AND apparatus = 0 "
                   f"AND file IN ({','.join('?' * len(chunk))})")
            for pid, file, locus in connection.execute(sql, chunk):
                row = bound_row(rows[file], locus)
                if row is not None and (allowed is None or row in allowed):
                    out.append(pid)
    finally:
        connection.close()
    return sorted(out)
