import hashlib
import json
import os
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from .catalog import FileEntry
from .contract import Passage
from .generate import text_hash

SCHEMA = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE passages (
    id INTEGER PRIMARY KEY,
    passage_id TEXT NOT NULL UNIQUE,
    file TEXT NOT NULL,
    source_path TEXT NOT NULL,
    division_locus TEXT NOT NULL,
    division_title TEXT NOT NULL,
    ordinal INTEGER NOT NULL,
    language TEXT NOT NULL,
    script TEXT NOT NULL,
    apparatus INTEGER NOT NULL,
    speaker_state TEXT NOT NULL,
    speaker_voice TEXT,
    ocr_score REAL,
    byte_start INTEGER NOT NULL,
    byte_end INTEGER NOT NULL,
    word_count INTEGER NOT NULL,
    text_hash TEXT NOT NULL,
    row_ids TEXT NOT NULL,
    worlds TEXT NOT NULL,
    work_locus TEXT NOT NULL,
    context TEXT NOT NULL,
    context_status TEXT NOT NULL,
    text TEXT NOT NULL
);
CREATE VIRTUAL TABLE passage_fts USING fts5(context, text, tokenize='unicode61 remove_diacritics 2');
CREATE TABLE passage_rows (passage_id TEXT NOT NULL, world TEXT NOT NULL, row_id TEXT NOT NULL, role TEXT NOT NULL);
CREATE TABLE shelf_files (file TEXT NOT NULL, world TEXT NOT NULL, row_id TEXT NOT NULL, role TEXT NOT NULL);
CREATE INDEX shelf_files_lookup ON shelf_files (world, role, file);
CREATE TABLE keys (passage_id TEXT NOT NULL, kind TEXT NOT NULL, value TEXT NOT NULL);
CREATE INDEX keys_lookup ON keys (kind, value);
CREATE INDEX passage_rows_lookup ON passage_rows (world, role);
CREATE INDEX passages_work_locus ON passages (work_locus);
"""

KEY_KINDS = ("sub_question", "scripture_ref", "work_locus")
CONTEXT_OK = "ok"
CONTEXT_NONE = "none"


def pipeline_code_hash() -> str:
    digest = hashlib.sha256()
    for path in sorted(Path(__file__).resolve().parent.glob("*.py")):
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def usable_contexts(records: Mapping[str, dict], passages: Sequence[Passage]) -> dict[str, str]:
    usable = {}
    for passage in passages:
        record = records.get(passage.passage_id)
        if record and record["status"] == CONTEXT_OK and record["text_hash"] == text_hash(passage.text):
            usable[passage.passage_id] = record["context"]
    return usable


@dataclass(frozen=True)
class BuildStats:
    version: str
    files: int
    passages: int
    contexts: int
    seconds: float


def _explicit_rows(passage: Passage, entry: FileEntry | None) -> list[tuple[str, str, str]]:
    if entry is None or not passage.row_ids:
        return []
    wanted = set(passage.row_ids)
    return [(r["world"], r["row_id"], r["role"] or "unstated") for r in entry.rows if r["row_id"] in wanted]


def build_index_stream(
    db_path: Path,
    groups: Iterable[tuple[str, Sequence[Passage], Mapping[str, str]]],
    entries: Mapping[str, FileEntry],
    model_id: str,
) -> BuildStats:
    started = time.monotonic()
    code_hash = pipeline_code_hash()
    digest = hashlib.sha256()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = db_path.with_name(db_path.name + ".building")
    if temporary.exists():
        temporary.unlink()
    connection = sqlite3.connect(temporary)
    files = passages_total = contexts_total = 0
    try:
        connection.executescript(SCHEMA)
        for file_name, passages, contexts in groups:
            files += 1
            entry = entries.get(file_name)
            for row in (entry.rows if entry else []):
                connection.execute("INSERT INTO shelf_files VALUES (?,?,?,?)",
                                   (file_name, row["world"], row["row_id"] or "(unaddressable)", row["role"] or "unstated"))
            for passage in passages:
                context = contexts.get(passage.passage_id, "")
                digest.update(f"{passage.passage_id}\t{text_hash(passage.text)}\t{context}\n".encode())
                work_locus = f"{passage.file}#{passage.division_locus}"
                cursor = connection.execute(
                    "INSERT INTO passages (passage_id, file, source_path, division_locus, division_title, ordinal, language, script, "
                    "apparatus, speaker_state, speaker_voice, ocr_score, byte_start, byte_end, word_count, text_hash, row_ids, worlds, "
                    "work_locus, context, context_status, text) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        passage.passage_id, passage.file, f"cic/texts/{passage.file}", passage.division_locus, passage.division_title,
                        passage.ordinal, passage.language, passage.script, int(passage.apparatus), passage.speaker_state,
                        passage.speaker_voice, passage.ocr_score, passage.byte_start, passage.byte_end, passage.word_count,
                        text_hash(passage.text), json.dumps(list(passage.row_ids)), json.dumps(list(passage.worlds)), work_locus,
                        context, CONTEXT_OK if context else CONTEXT_NONE, passage.text,
                    ),
                )
                connection.execute("INSERT INTO passage_fts (rowid, context, text) VALUES (?,?,?)", (cursor.lastrowid, context, passage.text))
                for world, row_id, role in _explicit_rows(passage, entry):
                    connection.execute("INSERT INTO passage_rows VALUES (?,?,?,?)", (passage.passage_id, world, row_id, role))
                connection.execute("INSERT INTO keys VALUES (?,?,?)", (passage.passage_id, "work_locus", work_locus))
                passages_total += 1
                contexts_total += 1 if context else 0
            connection.commit()
        digest.update(f"{model_id}\t{code_hash}".encode())
        version = digest.hexdigest()
        for key, value in (("version", version), ("model_id", model_id), ("pipeline_code_hash", code_hash),
                           ("passages", str(passages_total)), ("contexts", str(contexts_total)), ("files", str(files))):
            connection.execute("INSERT INTO meta VALUES (?,?)", (key, value))
        connection.commit()
    finally:
        connection.close()
    os.replace(temporary, db_path)
    return BuildStats(version, files, passages_total, contexts_total, time.monotonic() - started)


def build_index(
    db_path: Path,
    passages: Sequence[Passage],
    contexts: Mapping[str, str],
    entries: Mapping[str, FileEntry],
    model_id: str,
) -> str:
    by_file: dict[str, list[Passage]] = {}
    for passage in sorted(passages, key=lambda p: (p.file, p.byte_start, p.ordinal)):
        by_file.setdefault(passage.file, []).append(passage)
    groups = ((name, ps, {p.passage_id: contexts[p.passage_id] for p in ps if p.passage_id in contexts}) for name, ps in by_file.items())
    return build_index_stream(db_path, groups, entries, model_id).version


def read_meta(db_path: Path) -> dict[str, str]:
    connection = sqlite3.connect(db_path)
    try:
        return dict(connection.execute("SELECT key, value FROM meta"))
    finally:
        connection.close()
