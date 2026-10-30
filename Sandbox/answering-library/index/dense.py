import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

QUERY_PREFIX = "query: "
PASSAGE_PREFIX = "passage: "
DEFAULT_MAX_TOKENS = 256
DEFAULT_BATCH = 32
DIMENSION = 384


@dataclass(frozen=True)
class ModelFiles:
    onnx: Path
    tokenizer: Path

    @classmethod
    def in_directory(cls, directory: Path, onnx_name: str = "model_q.onnx") -> "ModelFiles":
        return cls(directory / onnx_name, directory / "tokenizer.json")


class OnnxEmbedder:
    """multilingual-e5 style embedder: prefix, mean pooling over the attention mask, L2 normalised, onnxruntime on CPU."""

    def __init__(self, files: ModelFiles, model_id: str, max_tokens: int = DEFAULT_MAX_TOKENS, threads: int | None = None):
        import onnxruntime
        from tokenizers import Tokenizer

        options = onnxruntime.SessionOptions()
        if threads:
            options.intra_op_num_threads = threads
        self.session = onnxruntime.InferenceSession(str(files.onnx), options, providers=["CPUExecutionProvider"])
        self.input_names = {i.name for i in self.session.get_inputs()}
        self.tokenizer = Tokenizer.from_file(str(files.tokenizer))
        self.tokenizer.enable_truncation(max_length=max_tokens)
        self.tokenizer.enable_padding(pad_id=self.tokenizer.token_to_id("<pad>") or 0, pad_token="<pad>")
        self.model_id = model_id
        self.max_tokens = max_tokens

    def _encode(self, texts: Sequence[str]) -> np.ndarray:
        encodings = self.tokenizer.encode_batch(list(texts))
        ids = np.array([e.ids for e in encodings], dtype=np.int64)
        mask = np.array([e.attention_mask for e in encodings], dtype=np.int64)
        feed = {"input_ids": ids, "attention_mask": mask}
        if "token_type_ids" in self.input_names:
            feed["token_type_ids"] = np.zeros_like(ids)
        hidden = self.session.run(None, feed)[0]
        weights = mask[:, :, None].astype(np.float32)
        pooled = (hidden * weights).sum(axis=1) / np.maximum(weights.sum(axis=1), 1.0)
        norms = np.linalg.norm(pooled, axis=1, keepdims=True)
        return (pooled / np.maximum(norms, 1e-12)).astype(np.float32)

    def embed_passages(self, texts: Sequence[str]) -> np.ndarray:
        return self._encode([PASSAGE_PREFIX + t for t in texts])

    def embed_queries(self, texts: Sequence[str]) -> np.ndarray:
        return self._encode([QUERY_PREFIX + t for t in texts])


def length_batches(lengths: Sequence[int], batch_size: int) -> list[list[int]]:
    order = sorted(range(len(lengths)), key=lambda i: lengths[i])
    return [order[i:i + batch_size] for i in range(0, len(order), batch_size)]


@dataclass
class EmbedStats:
    passages: int
    seconds: float

    @property
    def per_thousand_seconds(self) -> float:
        return self.seconds / self.passages * 1000 if self.passages else 0.0


def embed_corpus(embedder: OnnxEmbedder, texts: Sequence[str], batch_size: int = DEFAULT_BATCH) -> tuple[np.ndarray, EmbedStats]:
    started = time.monotonic()
    lengths = [min(len(t), embedder.max_tokens * 8) for t in texts]
    vectors = np.zeros((len(texts), DIMENSION), dtype=np.float32)
    for batch in length_batches(lengths, batch_size):
        vectors[batch] = embedder.embed_passages([texts[i] for i in batch])
    return vectors, EmbedStats(len(texts), time.monotonic() - started)


def dense_ranking(query_vector: np.ndarray, vectors: np.ndarray, ids: Sequence[str], depth: int) -> list[str]:
    scores = vectors @ query_vector
    depth = min(depth, len(scores))
    top = np.argpartition(-scores, depth - 1)[:depth]
    return [ids[i] for i in top[np.argsort(-scores[top])]]


def reciprocal_rank_fusion(rankings: Iterable[Sequence[str]], depth: int, constant: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for position, passage_id in enumerate(ranking, 1):
            scores[passage_id] = scores.get(passage_id, 0.0) + 1.0 / (constant + position)
    return [pid for pid, _ in sorted(scores.items(), key=lambda kv: -kv[1])[:depth]]


SHARD_SIZE = 1000


def shard_paths(directory: Path, number: int) -> tuple[Path, Path]:
    return directory / f"shard{number:04d}.npy", directory / f"shard{number:04d}.ids.json"


def embed_to_shards(embedder: OnnxEmbedder, items: Sequence[tuple[str, str]], directory: Path, limit: int | None = None,
                    shard_size: int = SHARD_SIZE, batch_size: int = DEFAULT_BATCH, log=print) -> EmbedStats:
    """Embed (passage_id, text) pairs in the order given, one resumable shard at a time. Stops after `limit` passages."""
    directory.mkdir(parents=True, exist_ok=True)
    wanted = items if limit is None else items[:limit]
    started = time.monotonic()
    done = 0
    for number, begin in enumerate(range(0, len(wanted), shard_size)):
        vectors_path, ids_path = shard_paths(directory, number)
        chunk = wanted[begin:begin + shard_size]
        if vectors_path.is_file() and ids_path.is_file():
            continue
        vectors, stats = embed_corpus(embedder, [text for _, text in chunk], batch_size)
        ids_path.write_text(json.dumps([pid for pid, _ in chunk]), encoding="utf-8")
        np.save(vectors_path, vectors.astype(np.float16))
        done += len(chunk)
        log(f"shard {number}: {len(chunk)} passages, {stats.per_thousand_seconds:.0f} s per 1,000")
    return EmbedStats(done, time.monotonic() - started)


def load_shards(directory: Path, up_to: int | None = None) -> tuple[list[str], np.ndarray]:
    ids: list[str] = []
    parts = []
    number = 0
    while True:
        vectors_path, ids_path = shard_paths(directory, number)
        if not (vectors_path.is_file() and ids_path.is_file()):
            break
        ids += json.loads(ids_path.read_text(encoding="utf-8"))
        parts.append(np.load(vectors_path).astype(np.float32))
        number += 1
    vectors = np.concatenate(parts) if parts else np.zeros((0, DIMENSION), dtype=np.float32)
    if up_to is not None:
        return ids[:up_to], vectors[:up_to]
    return ids, vectors
