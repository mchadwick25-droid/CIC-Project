"""The free local models: a sentence embedder behind the Embedder interface, and a cross-encoder reranker. No network at run time."""
from pathlib import Path
from typing import Sequence

import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
MAX_TOKENS = 512


def _session(path: Path) -> ort.InferenceSession:
    options = ort.SessionOptions()
    options.log_severity_level = 3
    return ort.InferenceSession(str(path), options, providers=["CPUExecutionProvider"])


def _feed(session: ort.InferenceSession, encodings) -> dict:
    ids = np.array([e.ids for e in encodings], dtype=np.int64)
    feed = {"input_ids": ids, "attention_mask": np.array([e.attention_mask for e in encodings], dtype=np.int64)}
    if any(i.name == "token_type_ids" for i in session.get_inputs()):
        feed["token_type_ids"] = np.array([e.type_ids for e in encodings], dtype=np.int64)
    return feed


class BgeSmallEmbedder:
    """BAAI/bge-small-en-v1.5 (MIT licence), run locally. Vectors are unit length, so a dot product is the cosine."""

    model_id = "bge-small-en-v1.5"
    batch = 32

    def __init__(self, model: Path, tokenizer: Path):
        self._session = _session(model)
        self._tok = Tokenizer.from_file(str(tokenizer))
        self._tok.enable_truncation(MAX_TOKENS)
        self._tok.enable_padding()

    def _embed(self, texts: Sequence[str]) -> list[list[float]]:
        out: list[np.ndarray] = []
        order = sorted(range(len(texts)), key=lambda i: len(texts[i]))
        for start in range(0, len(order), self.batch):
            chunk = [texts[i] for i in order[start:start + self.batch]]
            encodings = self._tok.encode_batch(chunk)
            hidden = self._session.run(None, _feed(self._session, encodings))[0][:, 0, :]
            out.append(hidden / np.linalg.norm(hidden, axis=1, keepdims=True))
        matrix = np.concatenate(out) if out else np.zeros((0, 384), dtype=np.float32)
        result = np.empty_like(matrix)
        result[order] = matrix
        return result.tolist()

    def count_tokens(self, text: str) -> int:
        return len(self._tok.encode(text, add_special_tokens=True).ids)

    def embed_passages(self, texts: Sequence[str]) -> list[list[float]]:
        return self._embed(list(texts))

    def embed_query(self, text: str) -> list[float]:
        return self._embed([QUERY_PREFIX + text])[0]


class MiniLMReranker:
    """cross-encoder/ms-marco-MiniLM-L-6-v2 (Apache-2.0 licence), run locally: one relevance score per (query, passage)."""

    model_id = "ms-marco-MiniLM-L-6-v2"
    batch = 16

    def __init__(self, model: Path, tokenizer: Path):
        self._session = _session(model)
        self._tok = Tokenizer.from_file(str(tokenizer))
        self._tok.enable_truncation(MAX_TOKENS)
        self._tok.enable_padding()

    def count_tokens(self, text: str) -> int:
        return len(self._tok.encode(text, add_special_tokens=True).ids)

    def score(self, query: str, texts: Sequence[str]) -> list[float]:
        """One relevance score per text: the best score over the text's windows, each short enough for the model's input
        together with the query, so no part of a passage goes unread."""
        from .meaning import windows

        room = MAX_TOKENS - self.count_tokens(query) - 4
        pairs: list[tuple[int, str]] = []
        for index, text in enumerate(texts):
            pairs += [(index, part) for part in windows(text, self.count_tokens, room)]
        scores = [-1e9] * len(texts)
        for start in range(0, len(pairs), self.batch):
            chunk = pairs[start:start + self.batch]
            encodings = self._tok.encode_batch([(query, part) for _, part in chunk])
            for (index, _), value in zip(chunk, self._session.run(None, _feed(self._session, encodings))[0][:, 0].tolist()):
                scores[index] = max(scores[index], value)
        return scores
