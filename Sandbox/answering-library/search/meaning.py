"""Meaning search inside a lens: passage vectors from an Embedder, cosine ranking over the lens rows only.

A passage longer than WINDOW_WORDS is embedded as several windows and scores as its best window, so no part of a passage
is cut off by the model's input limit. Vectors are kept outside the index file, in a folder named by the index version
and the embedder, so a rebuilt index or another model never reads stale vectors.
"""
import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Sequence

import numpy as np

WINDOW_WORDS = 220
MAX_TOKENS = 500


def _fit(words: list[str], count_tokens, limit: int) -> list[str]:
    chunk = " ".join(words)
    if len(words) <= 1 or count_tokens(chunk) <= limit:
        return [chunk]
    middle = len(words) // 2
    return _fit(words[:middle], count_tokens, limit) + _fit(words[middle:], count_tokens, limit)


def windows(text: str, count_tokens=None, limit: int = MAX_TOKENS, size: int = WINDOW_WORDS) -> list[str]:
    """The text in windows of at most `size` words and, when a token counter is given, at most `limit` tokens, so the model
    never cuts a window short. Every word of the text is in exactly one window."""
    words = text.split()
    chunks = [words[i:i + size] for i in range(0, max(len(words), 1), size)]
    if count_tokens is None:
        return [" ".join(c) for c in chunks]
    return [part for c in chunks for part in _fit(c, count_tokens, limit)]


class VectorStore:
    def __init__(self, folder: Path, vectors: np.ndarray, owners: np.ndarray):
        self.folder, self.vectors, self.owners = folder, vectors, owners

    @classmethod
    def folder_for(cls, root: Path, db_path: Path, world: str, model_id: str, lens: Sequence[int]) -> Path:
        """Named by the index version, the model and the lens: another lens, index or model never reads these vectors."""
        connection = sqlite3.connect(db_path)
        try:
            version = connection.execute("SELECT value FROM meta WHERE key = 'version'").fetchone()[0]
        finally:
            connection.close()
        lens_hash = hashlib.sha256(",".join(map(str, lens)).encode()).hexdigest()[:12]
        return root / world / f"{version[:16]}-{model_id}-{lens_hash}"

    @classmethod
    def build(cls, folder: Path, db_path: Path, lens: Sequence[int], embedder, progress=None) -> "VectorStore":
        connection = sqlite3.connect(db_path)
        texts: list[str] = []
        owners: list[int] = []
        try:
            for start in range(0, len(lens), 900):
                chunk = list(lens[start:start + 900])
                for pid, text in connection.execute(
                        f"SELECT id, text FROM passages WHERE id IN ({','.join('?' * len(chunk))}) ORDER BY id", chunk):
                    for part in windows(text, getattr(embedder, "count_tokens", None)):
                        texts.append(part)
                        owners.append(pid)
        finally:
            connection.close()
        batches = []
        for start in range(0, len(texts), 2048):
            batches.append(np.asarray(embedder.embed_passages(texts[start:start + 2048]), dtype=np.float32))
            if progress:
                progress(min(start + 2048, len(texts)), len(texts))
        vectors = np.concatenate(batches) if batches else np.zeros((0, 384), dtype=np.float32)
        folder.mkdir(parents=True, exist_ok=True)
        np.save(folder / "vectors.npy", vectors)
        np.save(folder / "owners.npy", np.asarray(owners, dtype=np.int64))
        (folder / "meta.json").write_text(json.dumps({"windows": len(texts), "passages": len(set(owners)), "model_id": embedder.model_id}))
        return cls(folder, vectors, np.asarray(owners, dtype=np.int64))

    @classmethod
    def load(cls, folder: Path) -> "VectorStore | None":
        if not (folder / "vectors.npy").is_file():
            return None
        return cls(folder, np.load(folder / "vectors.npy"), np.load(folder / "owners.npy"))

    def rank(self, query_vector: Sequence[float], lens: Sequence[int], depth: int = 100) -> list[int]:
        """Internal passage ids in the lens, best first. Windows of passages outside the lens are never scored."""
        inside = np.isin(self.owners, np.asarray(list(lens), dtype=np.int64))
        scores = self.vectors[inside] @ np.asarray(query_vector, dtype=np.float32)
        owners = self.owners[inside]
        best: dict[int, float] = {}
        for owner, score in zip(owners.tolist(), scores.tolist()):
            if score > best.get(owner, -2.0):
                best[owner] = score
        return [o for o, _ in sorted(best.items(), key=lambda kv: (-kv[1], kv[0]))[:depth]]
