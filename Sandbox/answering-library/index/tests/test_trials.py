import numpy as np
import pytest

from index import contextwork, dense
from index.check import check_context_line


def test_reciprocal_rank_fusion_prefers_agreement():
    fused = dense.reciprocal_rank_fusion([["a", "b", "c"], ["c", "b", "d"]], depth=3)
    assert fused[0] == "c"


def test_length_batches_group_similar_lengths():
    batches = dense.length_batches([5, 100, 6, 99], 2)
    assert sorted(batches[0]) == [0, 2]
    assert sorted(batches[1]) == [1, 3]


def test_dense_ranking_orders_by_cosine():
    vectors = np.array([[1.0, 0.0], [0.0, 1.0], [0.7, 0.7]], dtype=np.float32)
    ranking = dense.dense_ranking(np.array([1.0, 0.0], dtype=np.float32), vectors, ["x", "y", "z"], 2)
    assert ranking == ["x", "z"]


def test_shards_round_trip(tmp_path):
    class Fixed:
        max_tokens = 8

        def embed_passages(self, texts):
            return np.tile(np.eye(dense.DIMENSION, dtype=np.float32)[0], (len(texts), 1))

    items = [(f"p{i}", "word " * (i + 1)) for i in range(5)]
    dense.embed_to_shards(Fixed(), items, tmp_path, shard_size=2, log=lambda *_: None)
    ids, vectors = dense.load_shards(tmp_path)
    assert ids == [pid for pid, _ in items]
    assert vectors.shape == (5, dense.DIMENSION)
    again = dense.embed_to_shards(Fixed(), items, tmp_path, shard_size=2, log=lambda *_: None)
    assert again.passages == 0


def test_excerpt_keeps_short_text_and_trims_long():
    assert contextwork.excerpt("a b c") == "a b c"
    long = " ".join(str(i) for i in range(500))
    shown = contextwork.excerpt(long).split()
    assert shown[0] == "0" and shown[-1] == "499" and "[...]" in shown


def test_numbered_answers_parse_and_refuse_repeats():
    parsed = contextwork.parse_numbered_answers("## f/0001\n1. First line.\n2. Second line.\n")
    assert parsed == {"f/0001": {1: "First line.", 2: "Second line."}}
    with pytest.raises(contextwork.RefusedBatch):
        contextwork.parse_numbered_answers("## f/0001\n1. A.\n1. B.\n")


def test_check_treats_curly_and_straight_apostrophes_alike():
    result = check_context_line("Cyprian writes about God's mercy.", "Cyprian on God’s mercy to the lapsed")
    assert result.ok
