"""Lens-first search: the lens is fixed before any ranking, then keyword and meaning rank inside it, are fused, and are reranked."""
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from . import fuse, keyword, lens
from .meaning import VectorStore

CANDIDATES = 100
RERANK_KEEP = 30


@dataclass
class Search:
    db_path: Path
    world: str
    store: VectorStore | None = None
    embedder: object | None = None
    reranker: object | None = None
    rows: dict | None = None
    window_rows: Sequence[str] | None = None

    def __post_init__(self):
        self.lens = lens.lens_ids(self.db_path, self.rows if self.rows is not None else lens.world_rows(self.world), self.window_rows)
        self._lens_set = set(self.lens)
        self._text: dict[int, str] = {}
        self._cache: dict[tuple, list[int]] = {}

    def texts(self, ids: Sequence[int]) -> list[str]:
        missing = [i for i in ids if i not in self._text]
        if missing:
            connection = sqlite3.connect(self.db_path)
            try:
                for start in range(0, len(missing), 900):
                    chunk = missing[start:start + 900]
                    for pid, text in connection.execute(f"SELECT id, text FROM passages WHERE id IN ({','.join('?' * len(chunk))})", chunk):
                        self._text[pid] = text
            finally:
                connection.close()
        return [self._text[i] for i in ids]

    def keyword(self, query: str, depth: int = CANDIDATES) -> list[int]:
        key = ("keyword", query, depth)
        if key not in self._cache:
            self._cache[key] = keyword.rank(self.db_path, query, self.lens, depth)
        return self._cache[key]

    def meaning(self, query: str, depth: int = CANDIDATES) -> list[int]:
        if self.store is None or self.embedder is None:
            raise RuntimeError("meaning search needs a vector store and an embedder")
        key = ("meaning", query, depth)
        if key not in self._cache:
            self._cache[key] = self.store.rank(self.embedder.embed_query(query), self.lens, depth)
        return self._cache[key]

    def fused(self, query: str, seeds: Sequence[int] = (), depth: int = CANDIDATES) -> list[int]:
        rankings = [self.keyword(query, depth), self.meaning(query, depth)]
        seeds = [s for s in seeds if s in self._lens_set]
        if seeds:
            rankings.append(seeds)
        merged = fuse.reciprocal_rank_fusion(rankings)
        if self.reranker is None:
            return merged
        return fuse.rerank(merged, lambda ids: self.reranker.score(query, self.texts(ids)), RERANK_KEEP, seeds)
