import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .catalog import REPO_ROOT

_TOKEN = re.compile(r"[^\W_]+", re.UNICODE)
BM25_WEIGHTS = (1.0, 1.0)


@dataclass(frozen=True)
class Hit:
    passage_id: str
    score: float
    text: str
    context: str
    source: dict


def fts_query(query: str) -> str:
    tokens = [t for t in _TOKEN.findall(query) if t]
    return " OR ".join(f'"{t}"' for t in tokens)


def _source(row: sqlite3.Row, roles: list[dict]) -> dict:
    return {
        "file": row["file"], "path": row["source_path"], "byte_start": row["byte_start"], "byte_end": row["byte_end"],
        "division_locus": row["division_locus"], "division_title": row["division_title"], "ordinal": row["ordinal"],
        "language": row["language"], "script": row["script"], "apparatus": bool(row["apparatus"]),
        "speaker": {"state": row["speaker_state"], "voice": row["speaker_voice"]}, "ocr_score": row["ocr_score"],
        "row_ids": json.loads(row["row_ids"]), "worlds": json.loads(row["worlds"]), "rows": roles,
    }


def search(
    db_path: Path,
    query: str,
    *,
    world: str | None = None,
    roles: Iterable[str] | None = None,
    speakers: Iterable[str] | None = None,
    min_ocr: float | None = None,
    limit: int = 10,
) -> list[Hit]:
    match = fts_query(query)
    if not match:
        return []
    clauses = ["passage_fts MATCH ?"]
    params: list = [match]
    if world is not None or roles is not None:
        sub = "SELECT 1 FROM shelf_files r WHERE r.file = p.file"
        if world is not None:
            sub += " AND r.world = ?"
            params.append(world)
        if roles is not None:
            role_list = list(roles)
            sub += f" AND r.role IN ({','.join('?' * len(role_list))})"
            params.extend(role_list)
        clauses.append(f"EXISTS ({sub})")
    if speakers is not None:
        speaker_list = list(speakers)
        clauses.append(f"p.speaker_state IN ({','.join('?' * len(speaker_list))})")
        params.extend(speaker_list)
    if min_ocr is not None:
        clauses.append("p.ocr_score >= ?")
        params.append(min_ocr)
    sql = (
        "SELECT p.*, bm25(passage_fts, ?, ?) AS score FROM passage_fts JOIN passages p ON p.id = passage_fts.rowid "
        f"WHERE {' AND '.join(clauses)} ORDER BY score LIMIT ?"
    )
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        hits = []
        for row in connection.execute(sql, [*BM25_WEIGHTS, *params, limit]):
            role_rows = [
                dict(r) for r in connection.execute(
                    "SELECT world, row_id, role FROM passage_rows WHERE passage_id = ?", (row["passage_id"],))
            ] or [
                dict(r) for r in connection.execute(
                    "SELECT world, row_id, role FROM shelf_files WHERE file = ?", (row["file"],))
            ]
            hits.append(Hit(row["passage_id"], row["score"], row["text"], row["context"], _source(row, role_rows)))
        return hits
    finally:
        connection.close()


def by_work_locus(db_path: Path, work_locus: str) -> list[str]:
    connection = sqlite3.connect(db_path)
    try:
        return [r[0] for r in connection.execute(
            "SELECT passage_id FROM keys WHERE kind = 'work_locus' AND value = ? ORDER BY rowid", (work_locus,))]
    finally:
        connection.close()


def verify_sources(db_path: Path, texts_dir: Path | None = None, limit: int | None = None) -> list[dict]:
    texts_dir = texts_dir or REPO_ROOT / "cic" / "texts"
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    problems = []
    try:
        sql = "SELECT passage_id, file, byte_start, byte_end, text FROM passages ORDER BY file, byte_start"
        if limit:
            sql += f" LIMIT {int(limit)}"
        handles: dict[str, bytes] = {}
        for row in connection.execute(sql):
            path = texts_dir / row["file"]
            if not path.is_file():
                problems.append({"passage_id": row["passage_id"], "problem": "vendored file missing"})
                continue
            if row["file"] not in handles:
                handles = {row["file"]: path.read_bytes()}
            span = handles[row["file"]][row["byte_start"]:row["byte_end"]].decode("utf-8", errors="replace")
            if " ".join(span.split()) != " ".join(row["text"].split()):
                problems.append({"passage_id": row["passage_id"], "problem": "text differs from the vendored file's byte span"})
        return problems
    finally:
        connection.close()
