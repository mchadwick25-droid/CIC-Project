import html
import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from answering_library import markup

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


def _visible_streams(span: str) -> tuple[list[str], list[str]]:
    """The words a markup range shows a reader, as (main text, notes), read by the segmenter's own token and tag rules:
    block tags break words, inline tags do not, comments and declarations vanish, style and script bodies are skipped,
    entities are decoded, and note bodies are a second stream. A range that begins inside a note starts in that stream."""
    tokens = list(markup.TOKEN.finditer(span))
    tags = [(m.group("name").lower(), bool(m.group("close"))) for m in tokens if m.group("name")]
    first_note = next(((closing for name, closing in tags if name in markup.NOTE_TAGS)), False)
    note_depth, skip = (1 if first_note else 0), 0
    pieces: dict[bool, list[str]] = {False: [], True: []}
    for match in tokens:
        token, name = match.group(0), match.group("name")
        if name is None:
            if not token.startswith(("<!", "<?")) and not skip:
                pieces[note_depth > 0].append(html.unescape(token) if token[0] == "&" and len(token) > 1 else token)
            continue
        lname, closing = name.lower(), bool(match.group("close"))
        selfclose = match.group("attrs").rstrip().endswith("/")
        if lname in markup.SKIP_TEXT:
            skip = max(skip + (-1 if closing else (0 if selfclose else 1)), 0)
        elif lname in markup.NOTE_TAGS:
            note_depth = max(note_depth - 1, 0) if closing else note_depth + (0 if selfclose else 1)
        elif lname in markup.BLOCK:
            pieces[note_depth > 0].append("\n")
    return "".join(pieces[False]).split(), "".join(pieces[True]).split()


def _in_order(words: list[str], span_words: list[str]) -> bool:
    if not words or not span_words or words[0] != span_words[0] or words[-1] != span_words[-1]:
        return False
    position = 0
    for word in words:
        try:
            position = span_words.index(word, position) + 1
        except ValueError:
            return False
    return True


def span_contains_passage(span: str, text: str) -> bool:
    """The segmenter's contract for a passage's byte range.

    The range runs from the passage's first word to its last word in the vendored file. The passage text is the words
    of that range in order, minus suppressed page furniture (running heads, bare page numbers) and, for a markup file,
    minus tags and the other text stream (notes against main text), with entities decoded. So the passage words are an
    in-order subsequence of the range's words, and the first and last words are the range's own.
    """
    words = text.split()
    return _in_order(words, span.split()) or any(_in_order(words, stream) for stream in _visible_streams(span))


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
            if not span_contains_passage(span, row["text"]):
                problems.append({"passage_id": row["passage_id"], "problem": "text differs from the vendored file's byte span"})
        return problems
    finally:
        connection.close()
