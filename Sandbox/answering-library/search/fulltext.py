"""Keyword search inside a lens: the index's own full-text ranking, restricted to the lens before it ranks."""
import re
import sqlite3
from pathlib import Path
from typing import Sequence

from index.retrieve import fts_query

_STOP = frozenset(
    """a about after all also am an and any are as at be been being but by can could did do does for from had has have he her him his
    how i if in into is it its me my no not of on one or our out she so some than that the their them then there these they this
    those to up us was we were what when where which who whom why will with would you your yours""".split())


def query_terms(text: str) -> list[str]:
    return [t for t in re.findall(r"[^\W_]+", text.casefold()) if t not in _STOP and len(t) > 1]


def rank(db_path: Path, query: str, lens: Sequence[int], depth: int = 100) -> list[int]:
    """Internal passage ids in the lens, best first. Nothing outside the lens is ever scored."""
    match = fts_query(" ".join(query_terms(query)))
    if not match or not lens:
        return []
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("CREATE TEMP TABLE lens (id INTEGER PRIMARY KEY)")
        connection.executemany("INSERT INTO lens VALUES (?)", ((i,) for i in lens))
        sql = ("SELECT l.id FROM passage_fts f JOIN lens l ON l.id = f.rowid WHERE passage_fts MATCH ? "
               "ORDER BY bm25(passage_fts) LIMIT ?")
        return [r[0] for r in connection.execute(sql, (match, depth))]
    finally:
        connection.close()
