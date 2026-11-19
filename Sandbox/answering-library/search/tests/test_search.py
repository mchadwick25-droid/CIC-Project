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
    ids = lens.lens_ids(db, ROWS["wa"])
    assert len(ids) == 3
    sqlite = __import__("sqlite3").connect(db)
    got = {r[0] for r in sqlite.execute(f"SELECT passage_id FROM passages WHERE id IN ({','.join(map(str, ids))})")}
    assert got == {"a_file.txt:1", "a_file.txt:2", "e_file.txt:1"}
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
    b = _search(tmp_path, "wb")
    outside = b.lens[0]
    assert outside not in a.lens
    assert a.fused("catechumens baptism", seeds=[outside]) == a.fused("catechumens baptism")
    assert outside not in a.fused("catechumens baptism", seeds=[outside])
    seed = a.lens[-1]
    plain = a.fused("catechumens baptism")
    assert plain.index(seed) > 0
    assert a.fused("catechumens baptism", seeds=[seed]).index(seed) < plain.index(seed)


def test_windows_cover_a_long_passage_without_cutting_it():
    text = " ".join(f"w{i}" for i in range(500))
    parts = windows(text)
    assert len(parts) == 3 and " ".join(parts).split() == text.split()


def test_rrf_rewards_agreement_and_rerank_ties_prefer_seeds():
    assert set(fuse.reciprocal_rank_fusion([[1, 2, 3], [3, 2, 9]])[:2]) == {2, 3}
    assert fuse.reciprocal_rank_fusion([[1, 2], [2, 1]]) == [1, 2]
    assert fuse.reciprocal_rank_fusion([[5], [], [9]], seeds={9}) == [9, 5]
    assert fuse.reciprocal_rank_fusion([[5], [], [9]]) == [5, 9]
    assert fuse.rerank([5, 6, 7], lambda ids: [1.0, 1.0, 0.5], 3, seeds={6}) == [6, 5, 7]
    assert fuse.rerank([5, 6, 7, 8], lambda ids: [0.1, 0.9], 2) == [6, 5, 7, 8]


def test_sign_test_matches_the_binomial():
    assert sign_test_p(0, 0) == 1.0
    assert math.isclose(sign_test_p(10, 0), 2 / 1024)
    assert sign_test_p(30, 10) < 0.01 and sign_test_p(12, 8) > 0.5


class LengthReranker:
    """A test reranker that prefers the passage holding a marker word, whatever its length."""

    def count_tokens(self, text):
        return len(text.split())

    def score(self, query, texts):
        return [1.0 if "feast" in t else 0.0 for t in texts]


def test_fused_with_a_reranker_orders_by_its_score_and_a_seed_wins_an_equal_score(tmp_path):
    a = _search(tmp_path, "wa")
    a.reranker = LengthReranker()
    ranking = a.fused("bishop catechumens baptism feast martyrs")
    feast = a.texts(ranking).index(SHARED)
    assert feast == 0
    unscored = [i for i in a.lens if a.texts([i])[0] != SHARED]
    first, second = unscored[0], unscored[1]
    out = a.fused("bishop catechumens baptism feast martyrs", seeds=[second])
    assert out.index(second) < out.index(first)


def test_windows_never_exceed_the_token_limit_and_keep_every_word():
    text = " ".join(f"w{i}" for i in range(500))
    parts = windows(text, count_tokens=lambda t: len(t.split()) * 3, limit=90)
    assert all(len(p.split()) * 3 <= 90 for p in parts)
    assert " ".join(parts).split() == text.split()


def test_vectors_are_kept_apart_for_different_lenses(tmp_path):
    db = _fixture(tmp_path)
    one = VectorStore.folder_for(tmp_path, db, "wa", "m", [1, 2])
    two = VectorStore.folder_for(tmp_path, db, "wa", "m", [1, 2, 3])
    assert one != two and one == VectorStore.folder_for(tmp_path, db, "wa", "m", [1, 2])


def test_query_level_pairing_counts_one_query_once():
    from search.benchrun import summarise
    ranks = lambda kw, me: {"keyword_unlensed": None, "keyword": kw, "meaning": me, "fused": me, "fused_seeds": me}
    cases = [{"cell": "c", "wording_id": "q", "gold_in_lens": True, "rank": ranks(None, 3)} for _ in range(3)]
    result = summarise(cases)
    assert result["total_cases"] == 3 and result["total_queries"] == 1
    assert result["hits"]["meaning"][5] == 3 and result["query_hits"]["meaning"][5] == 1
    assert result["paired_at_query_level"]["meaning vs keyword @5"]["wins"] == 1
