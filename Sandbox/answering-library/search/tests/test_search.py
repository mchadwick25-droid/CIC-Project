import hashlib
import math

import numpy as np

from index import store
from index.catalog import FileEntry
from index.contract import Passage
from search import fuse, lens
from search.benchrun import sign_test_p
from search.engine import Search
from search.meaning import VectorStore, windows

SHARED = "the church keeps the feast of the martyrs each year"


def _passage(file, n, text, *, worlds, rows, language="eng", apparatus=False):
    return Passage(passage_id=f"{file}:{n}", file=file, division_locus=str(n), division_title="", ordinal=n, text=text,
                   word_count=len(text.split()), language=language, script="latin", apparatus=apparatus, speaker_state="known",
                   speaker_voice="X", ocr_score=0.95, byte_start=n * 1000, byte_end=n * 1000 + 500, row_ids=tuple(rows), worlds=tuple(worlds))


class HashEmbedder:
    """A deterministic bag-of-words embedder for tests: shared words, shared direction."""
    model_id = "test-hash"

    def _vec(self, text):
        v = np.zeros(64)
        for w in text.lower().split():
            v[int(hashlib.md5(w.encode()).hexdigest(), 16) % 64] += 1
        return (v / (np.linalg.norm(v) or 1)).tolist()

    def embed_passages(self, texts):
        return [self._vec(t) for t in texts]

    def embed_query(self, text):
        return self._vec(text)


ROWS = {
    "wa": {"a_file.txt": [{"row_id": "wa.1", "locus_ids": None}],
           "d_file.txt": [{"row_id": "wa.3", "locus_ids": ["1"]}, {"row_id": "wa.4", "locus_ids": ["1"]}],
           "e_file.txt": [{"row_id": "wa.5", "locus_ids": ["1"]}, {"row_id": "wa.6", "locus_ids": ["2"]}],
           "c_file.txt": [{"row_id": "wa.7", "locus_ids": ["8"]}, {"row_id": "wa.8", "locus_ids": ["9"]}]},
    "wb": {"b_file.txt": [{"row_id": "wb.1", "locus_ids": None}],
           "c_file.txt": [{"row_id": "wb.2", "locus_ids": ["1"]}]},
}


def _fixture(tmp_path):
    entries = {n: FileEntry(n, 1, set(), []) for n in ("a_file.txt", "b_file.txt", "c_file.txt", "d_file.txt", "e_file.txt")}
    passages = [
        _passage("a_file.txt", 1, "the bishop teaches the catechumens about baptism and the creed", worlds=["wa"], rows=[]),
        _passage("a_file.txt", 2, SHARED, worlds=["wa"], rows=[]),
        _passage("a_file.txt", 3, "the bishop teaches latin words here", worlds=["wa"], rows=[], language="lat"),
        _passage("a_file.txt", 4, "the bishop teaches printed by the editor", worlds=["wa"], rows=[], apparatus=True),
        _passage("b_file.txt", 1, "a zeppelin crossed the harbour while the monks prayed", worlds=["wb"], rows=[]),
        _passage("c_file.txt", 1, "the bishop teaches the zeppelin people", worlds=["wa", "wb"], rows=[]),
        _passage("d_file.txt", 1, "a passage that two rows of the same world both claim", worlds=["wa"], rows=[]),
        _passage("e_file.txt", 1, "a passage that exactly one of two rows claims", worlds=["wa"], rows=[]),
    ]
    db = tmp_path / "ix.sqlite"
    store.build_index(db, passages, {}, entries, "test")
    return db


def _search(tmp_path, world):
    db = _fixture(tmp_path)
    s = Search(db, world, rows=ROWS[world], embedder=HashEmbedder())
    s.store = VectorStore.build(tmp_path / "v" / world, db, s.lens, s.embedder)
    return s


def test_lens_is_the_division_test_over_the_worlds_own_rows(tmp_path):
    db = _fixture(tmp_path)
    # wa: a_file passages 1 and 2 (one row), e_file passage 1 (one of two rows claims it); not Latin, apparatus, d_file (two claim), c_file (none claims)
    assert len(lens.lens_ids(db, ROWS["wa"])) == 3
    assert len(lens.lens_ids(db, ROWS["wb"])) == 2
    assert len(lens.lens_ids(db, ROWS["wa"], window_rows=["wa.1"])) == 2
    assert lens.lens_ids(db, ROWS["wa"], window_rows=["wa.9"]) == []
    assert lens.lens_ids(db, {}) == []


def test_a_query_matching_only_world_b_returns_nothing_for_world_a_by_every_method(tmp_path):
    a = _search(tmp_path, "wa")
    q = "zeppelin harbour monks"
    assert a.keyword(q) == []
    own = set(a.lens)
    for ranking in (a.keyword(q), a.meaning(q), a.fused(q), a.fused(q, seeds=[999999])):
        assert set(ranking) <= own
    b = _search(tmp_path, "wb")
    assert len(b.keyword(q)) == 2 and b.meaning(q)[0] == b.keyword(q)[0]
    assert set(a.meaning(q)).isdisjoint(b.lens)


def test_a_seed_outside_the_lens_is_dropped_and_a_seed_inside_is_rank_help(tmp_path):
    a = _search(tmp_path, "wa")
    inside = a.lens[0]
    assert a.fused("catechumens baptism", seeds=[10_000]) == a.fused("catechumens baptism")
    assert inside in a.fused("feast martyrs", seeds=[inside])


def test_windows_cover_a_long_passage_without_cutting_it():
    text = " ".join(f"w{i}" for i in range(500))
    parts = windows(text)
    assert len(parts) == 3 and " ".join(parts).split() == text.split()


def test_rrf_rewards_agreement_and_rerank_ties_prefer_seeds():
    assert set(fuse.reciprocal_rank_fusion([[1, 2, 3], [3, 2, 9]])[:2]) == {2, 3}
    assert fuse.reciprocal_rank_fusion([[1, 2], [2, 1]]) == [1, 2]
    assert fuse.rerank([5, 6, 7], lambda ids: [1.0, 1.0, 0.5], 3, seeds={6}) == [6, 5, 7]
    assert fuse.rerank([5, 6, 7, 8], lambda ids: [0.1, 0.9], 2) == [6, 5, 7, 8]


def test_sign_test_matches_the_binomial():
    assert sign_test_p(0, 0) == 1.0
    assert math.isclose(sign_test_p(10, 0), 2 / 1024)
    assert sign_test_p(30, 10) < 0.01 and sign_test_p(12, 8) > 0.5
