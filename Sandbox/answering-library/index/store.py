import hashlib
import json
import os
import sqlite3
from pathlib import Path
from typing import Mapping, Sequence

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


def index_version(passages: Sequence[Passage], contexts: Mapping[str, str], model_id: str, code_hash: str) -> str:
    digest = hashlib.sha256()
    for passage in sorted(passages, key=lambda p: p.passage_id):
        digest.update(f"{passage.passage_id}\t{text_hash(passage.text)}\t{contexts.get(passage.passage_id, '')}\n".encode())
    digest.update(f"{model_id}\t{code_hash}".encode())
    return digest.hexdigest()


def usable_contexts(records: Mapping[str, dict], passages: Sequence[Passage]) -> dict[str, str]:
    usable = {}
    for passage in passages:
        record = records.get(passage.passage_id)
        if record and record["status"] == CONTEXT_OK and record["text_hash"] == text_hash(passage.text):
            usable[passage.passage_id] = record["context"]
    return usable


def _roles(passage: Passage, entry: FileEntry | None) -> list[tuple[str, str, str]]:
    if entry is None:
        return []
    worlds = set(passage.worlds) or entry.worlds
    wanted = set(passage.row_ids)
    rows = [r for r in entry.rows if r["world"] in worlds and (not wanted or r["row_id"] in wanted)]
    return [(r["world"], r["row_id"] or "(unaddressable)", r["role"] or "unstated") for r in rows]


def build_index(
    db_path: Path,
    passages: Sequence[Passage],
    contexts: Mapping[str, str],
    entries: Mapping[str, FileEntry],
    model_id: str,
) -> str:
    code_hash = pipeline_code_hash()
    version = index_version(passages, contexts, model_id, code_hash)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = db_path.with_name(db_path.name + ".building")
    if temporary.exists():
        temporary.unlink()
    connection = sqlite3.connect(temporary)
    try:
        connection.executescript(SCHEMA)
        for passage in passages:
            context = contexts.get(passage.passage_id, "")
            entry = entries.get(passage.file)
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
            for world, row_id, role in _roles(passage, entry):
                connection.execute("INSERT INTO passage_rows VALUES (?,?,?,?)", (passage.passage_id, world, row_id, role))
            connection.execute("INSERT INTO keys VALUES (?,?,?)", (passage.passage_id, "work_locus", work_locus))
        for key, value in (("version", version), ("model_id", model_id), ("pipeline_code_hash", code_hash),
                           ("passages", str(len(passages))), ("contexts", str(len(contexts)))):
            connection.execute("INSERT INTO meta VALUES (?,?)", (key, value))
        connection.commit()
    finally:
        connection.close()
    os.replace(temporary, db_path)
    return version


def read_meta(db_path: Path) -> dict[str, str]:
    connection = sqlite3.connect(db_path)
    try:
        return dict(connection.execute("SELECT key, value FROM meta"))
    finally:
        connection.close()
