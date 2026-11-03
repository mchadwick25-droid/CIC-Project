"""A world's searchable shelf for the passage offer: the built index, the world's corpus-map rows and the world's saved
vectors, each loaded from a path or value the caller gives. Nothing here names a location.

The shelf is what engine.m4.passage_offer.search_passages reads; its index_version is what a seed file must match. It answers only for passages in the world's lens
(search.lens): a passage outside the lens has no internal id here, no ranking place and no text.

  shelf = load(world, db_path=..., rows=rows_by_file(corpus_map_rows), vectors_root=..., embedder=..., reranker=...)

Both the embedder and the reranker are required, so the meaning step and the rerank step cannot drop out unseen; the
vectors must already be built for this index, model and lens (meaning.VectorStore.build), or loading is refused.
"""
import sqlite3
from pathlib import Path
from typing import Collection, Iterable, Mapping, Sequence

from . import lens
from .engine import Search
from .meaning import VectorStore

_FIELDS = ("id", "passage_id", "file", "division_locus", "division_title", "text", "word_count", "speaker_state",
           "ocr_score", "byte_start", "byte_end")


class ShelfError(Exception):
    pass


def rows_by_file(rows: Iterable[dict]) -> dict[str, list[dict]]:
    """Corpus-map rows grouped by their vendored file, each row kept whole (row_id, locus_ids, author, work, role, date)."""
    out: dict[str, list[dict]] = {}
    for row in rows:
        if row.get("source_file"):
            out.setdefault(row["source_file"], []).append(row)
    return out


class Shelf:
    def __init__(self, world: str, search: Search, rows: Mapping[str, Sequence[dict]]):
        self.world = world
        self.search = search
        self._rows = rows
        self._lens = frozenset(search.lens)
        self._by_row_id = {r["row_id"]: r for file_rows in rows.values() for r in file_rows if r.get("row_id")}
        self._passages: dict[int, dict] = {}
        connection = sqlite3.connect(search.db_path)
        try:
            self.index_version = connection.execute("SELECT value FROM meta WHERE key = 'version'").fetchone()[0]
        finally:
            connection.close()

    def in_lens(self, pid: int) -> bool:
        return pid in self._lens

    def internal_id(self, passage_id: str, byte_start: int | None = None, byte_end: int | None = None) -> int | None:
        """The internal id of an index passage in the lens; None when it is not in the index, its byte span differs from
        the one given, or it is outside the lens."""
        connection = sqlite3.connect(self.search.db_path)
        try:
            found = connection.execute("SELECT id, byte_start, byte_end FROM passages WHERE passage_id = ?", (passage_id,)).fetchone()
        finally:
            connection.close()
        if found is None or found[0] not in self._lens:
            return None
        if byte_start is not None and byte_end is not None and (found[1], found[2]) != (byte_start, byte_end):
            return None
        return found[0]

    def ranked(self, query: str, seeds: Sequence[int] = ()) -> list[int]:
        """Lens passages for the query, best first: keyword and meaning inside the lens, fused, reranked; seeds are rank help."""
        return [pid for pid in self.search.fused(query, seeds) if pid in self._lens]

    def passage(self, pid: int) -> dict:
        """The index fields of a lens passage and the one corpus-map row it is bound to (`row`)."""
        if pid not in self._lens:
            raise ShelfError(f"passage {pid} is outside the {self.world} lens")
        if pid not in self._passages:
            connection = sqlite3.connect(self.search.db_path)
            try:
                values = connection.execute(f"SELECT {', '.join(_FIELDS)} FROM passages WHERE id = ?", (pid,)).fetchone()
            finally:
                connection.close()
            passage = dict(zip(_FIELDS, values))
            row_id = lens.bound_row(self._rows[passage["file"]], passage["division_locus"])
            passage["row"] = self._by_row_id.get(row_id) if row_id else None
            self._passages[pid] = passage
        return dict(self._passages[pid])

    def row(self, row_id: str | None) -> dict | None:
        """The world's corpus-map row by its id, or None when the world has no such row."""
        return self._by_row_id.get(row_id) if row_id else None


def load(world: str, *, db_path: Path, rows: Mapping[str, Sequence[dict]], vectors_root: Path, embedder, reranker,
         window_rows: Collection[str] | None = None) -> Shelf:
    """The world's shelf, with the vectors saved under `vectors_root` for this index, embedder and lens."""
    if embedder is None or reranker is None:
        raise ShelfError("the shelf needs both an embedder and a reranker")
    search = Search(Path(db_path), world, embedder=embedder, reranker=reranker, rows=rows, window_rows=window_rows)
    folder = VectorStore.folder_for(Path(vectors_root), Path(db_path), world, embedder.model_id, search.lens)
    store = VectorStore.load(folder)
    if store is None:
        raise ShelfError(f"no vectors for {world} at {folder}; build them for this index, model and lens first")
    search.store = store
    return Shelf(world, search, rows)
