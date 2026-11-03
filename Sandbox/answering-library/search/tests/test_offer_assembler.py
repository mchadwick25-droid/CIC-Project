"""The offer assembler (engine.m4.passage_offer.search_passages) over a real two-world index, the lens-first search and the
shelf loader."""
import hashlib

import numpy as np
import pytest

from engine.m4 import passage_offer as po
from index import store
from index.catalog import FileEntry
from index.contract import Passage
from search import shelf as shelf_mod
from search.meaning import VectorStore


class HashEmbedder:
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


class EqualReranker:
    """Every passage scores the same, so only a seed can break the tie."""

    def score(self, query, texts):
        return [0.5] * len(texts)


def _row(row_id, file, author, work, locus_ids=None, role="tradition"):
    return {"row_id": row_id, "source_file": file, "author": author, "work": work, "locus_ids": locus_ids, "role": role,
            "date": {"start": 413, "end": 426, "formation_confidence": "Documented"}}


ROWS = {
    "wa": [_row("wa.cdg", "a_file.txt", "augustine", "City of God"),
           _row("wa.ep", "c_file.txt", "cyprian", "Letters", ["1"]),
           _row("wa.unit", "c_file.txt", "cyprian", "On the Unity", ["2"])],
    "wb": [_row("wb.z", "b_file.txt", "zosimus", "New History")],
}


def _passage(file, n, text, worlds, language="eng", apparatus=False):
    return Passage(passage_id=f"{file}:{n}", file=file, division_locus=str(n), division_title="", ordinal=n, text=text,
                   word_count=len(text.split()), language=language, script="latin", apparatus=apparatus, speaker_state="known",
                   speaker_voice="X", ocr_score=0.95, byte_start=n * 1000, byte_end=n * 1000 + 500, row_ids=(), worlds=tuple(worlds))


def _db(tmp_path):
    entries = {n: FileEntry(n, 1, set(), []) for n in ("a_file.txt", "b_file.txt", "c_file.txt")}
    passages = [
        _passage("a_file.txt", 1, "the martyrs feast is kept by the church each year", ["wa"]),
        _passage("a_file.txt", 2, "the bishop keeps the martyrs feast with the people", ["wa"]),
        _passage("a_file.txt", 3, "the martyrs feast in latin", ["wa"], language="lat"),
        _passage("a_file.txt", 4, "the martyrs feast printed by the editor", ["wa"], apparatus=True),
        _passage("b_file.txt", 1, "a zeppelin crossed the harbour while the monks prayed", ["wb"]),
        _passage("c_file.txt", 1, "the martyrs feast and the letters of the bishop", ["wa"]),
        _passage("c_file.txt", 2, "the unity of the church and the martyrs feast", ["wa"]),
        _passage("c_file.txt", 3, "the martyrs feast that no row of the world claims", ["wa"]),
    ]
    db = tmp_path / "ix.sqlite"
    store.build_index(db, passages, {}, entries, "test")
    return db


def _shelf(tmp_path, db, world, reranker=None):
    rows = shelf_mod.rows_by_file(ROWS[world])
    embedder = HashEmbedder()
    probe = shelf_mod.Search(db, world, rows=rows)
    VectorStore.build(VectorStore.folder_for(tmp_path / "v", db, world, embedder.model_id, probe.lens), db, probe.lens, embedder)
    return shelf_mod.load(world, db_path=db, rows=rows, vectors_root=tmp_path / "v", embedder=embedder,
                          reranker=reranker or EqualReranker())


def _lens_passage_ids(shelf):
    return {shelf.passage(pid)["passage_id"] for pid in shelf.search.lens}


def test_a_query_matching_only_world_b_offers_nothing_for_world_a(tmp_path):
    db = _db(tmp_path)
    a, b = _shelf(tmp_path, db, "wa"), _shelf(tmp_path, db, "wb")
    query = "zeppelin harbour monks"
    assert [p["passage_id"] for p in po.search_passages(b, query, [], po.Budget())] == ["b_file.txt:1"]
    offered = po.search_passages(a, query, [], po.Budget())
    assert "b_file.txt:1" not in {p["passage_id"] for p in offered}
    assert {p["passage_id"] for p in offered} <= _lens_passage_ids(a)
    assert a.search.keyword(query) == []


def test_no_passage_outside_the_lens_is_offered_and_every_one_is_flagged_and_labelled(tmp_path):
    a = _shelf(tmp_path, _db(tmp_path), "wa")
    offered = po.search_passages(a, "martyrs feast", [], po.Budget())
    ids = {p["passage_id"] for p in offered}
    assert ids == _lens_passage_ids(a) == {"a_file.txt:1", "a_file.txt:2", "c_file.txt:1", "c_file.txt:2"}
    for passage in offered:
        assert passage["voiceable"] is False and po.author_work(passage) in (
            "Augustine, in City of God", "Cyprian, in Letters", "Cyprian, in On the Unity")
        assert passage["tag"] == po.tag_for("wa", passage["passage_id"])


def _seed(shelf, passage_id):
    pid = next(p for p in shelf.search.lens if shelf.passage(p)["passage_id"] == passage_id)
    p = shelf.passage(pid)
    return {"tag": po.tag_for("wa", passage_id), "passage_id": passage_id, "byte_start": p["byte_start"], "byte_end": p["byte_end"],
            "voiceable": True, "author_name": "Cyprian", "work": "On the Unity of the Church", "role": "own", "rank": 1,
            "fit": "direct", "window": "inside"}


def test_a_reviewed_seed_outranks_a_searched_passage_of_equal_score(tmp_path):
    a = _shelf(tmp_path, _db(tmp_path), "wa")
    plain = po.search_passages(a, "martyrs feast", [], po.Budget())
    last = plain[-1]["passage_id"]
    seeded = po.search_passages(a, "martyrs feast", [_seed(a, last)], po.Budget())
    assert seeded[0]["passage_id"] == last and seeded[0]["voiceable"] is True
    assert seeded[0]["work"] == "On the Unity of the Church"
    assert all(p["voiceable"] is False for p in seeded[1:])


def test_a_seed_from_another_world_is_neither_rank_help_nor_offered(tmp_path):
    db = _db(tmp_path)
    a = _shelf(tmp_path, db, "wa")
    foreign = {"tag": "wb.passage.x", "passage_id": "b_file.txt:1", "byte_start": 1000, "byte_end": 1500, "voiceable": True,
               "author_name": "Zosimus", "work": "New History", "rank": 1}
    assert po.search_passages(a, "martyrs feast", [foreign], po.Budget()) == po.search_passages(a, "martyrs feast", [], po.Budget())
    assert po.search_passages(a, "zeppelin harbour monks", [foreign], po.Budget()) == po.search_passages(a, "zeppelin harbour monks", [], po.Budget())


def test_the_shelf_refuses_without_vectors_or_without_either_model(tmp_path):
    db = _db(tmp_path)
    rows = shelf_mod.rows_by_file(ROWS["wa"])
    with pytest.raises(shelf_mod.ShelfError, match="no vectors"):
        shelf_mod.load("wa", db_path=db, rows=rows, vectors_root=tmp_path / "none", embedder=HashEmbedder(), reranker=EqualReranker())
    with pytest.raises(shelf_mod.ShelfError, match="embedder and a reranker"):
        shelf_mod.load("wa", db_path=db, rows=rows, vectors_root=tmp_path / "none", embedder=HashEmbedder(), reranker=None)


def test_the_shelf_answers_nothing_outside_its_lens(tmp_path):
    db = _db(tmp_path)
    a, b = _shelf(tmp_path, db, "wa"), _shelf(tmp_path, db, "wb")
    outside = b.search.lens[0]
    assert not a.in_lens(outside) and a.internal_id("b_file.txt:1") is None and a.internal_id("a_file.txt:3") is None
    with pytest.raises(shelf_mod.ShelfError):
        a.passage(outside)
    assert a.row("wa.cdg")["author"] == "augustine" and a.row("wb.z") is None
