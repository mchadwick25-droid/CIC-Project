"""The offer with search on: passages found inside the world's lens, one diversity rule over records and passages, the budget
last. The shelf here is a stand-in with the interface of Sandbox/answering-library/search/shelf.py; the two-world test
through the real lens-first search is in Sandbox/answering-library/search/tests/test_offer_assembler.py."""
from engine.m4 import passage_offer as po
from engine.m4.evidence import assemble_evidence, render_evidence_block, select_cell_candidates
from engine.m4.tests.test_evidence import CANON_QUESTIONS, COVERAGE, REPOSITORY

ROWS = {
    "r.aug.cdg": {"row_id": "r.aug.cdg", "author": "augustine", "work": "City of God", "role": "tradition",
                  "date": {"start": 413, "end": 426, "formation_confidence": "Documented"}},
    "r.aug.conf": {"row_id": "r.aug.conf", "author": "augustine", "work": "Confessions", "role": "tradition", "date": None},
    "r.aug.ep": {"row_id": "r.aug.ep", "author": "augustine", "work": "Letters", "role": "tradition", "date": None},
    "r.aug.ser": {"row_id": "r.aug.ser", "author": "augustine", "work": "Sermons", "role": "tradition", "date": None},
    "r.cyp.ep": {"row_id": "r.cyp.ep", "author": "cyprian", "work": "Letters", "role": "tradition", "date": None},
    "r.cyp.unit": {"row_id": "r.cyp.unit", "author": "cyprian", "work": "On the Unity of the Church", "role": "tradition", "date": None},
    "r.opt": {"row_id": "r.opt", "author": "optatus", "work": "Against Parmenian", "role": "context", "date": None},
    "r.anon": {"row_id": "r.anon", "author": None, "work": None, "role": "tradition", "date": None},
}


class FakeShelf:
    """A world's shelf: passages by internal id, the lens, and a fixed ranking for every query."""

    def __init__(self, world, passages, ranking, lens=None):
        self.world = world
        self._passages = passages
        self._ranking = list(ranking)
        self._lens = set(passages) if lens is None else set(lens)
        self.seeds_seen = None
        self.index_version = "ix1"

    def in_lens(self, pid):
        return pid in self._lens

    def internal_id(self, passage_id, byte_start=None, byte_end=None):
        for pid, p in self._passages.items():
            if p["passage_id"] == passage_id and pid in self._lens:
                if byte_start is not None and byte_end is not None and (p["byte_start"], p["byte_end"]) != (byte_start, byte_end):
                    return None
                return pid
        return None

    def ranked(self, query, seeds=()):
        self.seeds_seen = list(seeds)
        return list(self._ranking)

    def passage(self, pid):
        return dict(self._passages[pid])

    def row(self, row_id):
        return ROWS.get(row_id)


def _p(pid, row, words=100, text=None):
    return {"id": pid, "passage_id": f"cic:{row}.xml:{pid}#01", "file": f"{row}.xml", "division_locus": str(pid), "division_title": "",
            "text": text or f"Passage {pid} of {row}.", "word_count": words, "speaker_state": "known", "ocr_score": 0.9,
            "byte_start": pid * 10, "byte_end": pid * 10 + 9, "row": ROWS[row]}


def _shelf(rows_in_rank, words=100, lens=None, world="wa"):
    passages = {n: _p(n, row, words) for n, row in enumerate(rows_in_rank, 1)}
    return FakeShelf(world, passages, list(passages), lens)


def _seed(shelf, pid, **over):
    p = shelf._passages[pid]
    seed = {"tag": po.tag_for(shelf.world, p["passage_id"]), "passage_id": p["passage_id"], "byte_start": p["byte_start"],
            "byte_end": p["byte_end"], "voiceable": True, "author_name": "Augustine", "work": "City of God", "role": "own",
            "fit": "direct", "rank": 1, "window": "inside", "date": "413 to 426, Documented", "word_count": p["word_count"], "text": p["text"]}
    return {**seed, **over}


def _ids(shelf, passages):
    by_pid = {p["passage_id"]: n for n, p in shelf._passages.items()}
    return [by_pid[p["passage_id"]] for p in passages]


# Spec 2: the assembler.

def test_a_passage_the_shelf_ranks_outside_the_lens_is_never_offered():
    shelf = _shelf(["r.aug.cdg", "r.cyp.ep", "r.opt"], lens={1, 3})
    assert _ids(shelf, po.search_passages(shelf, "q", [], po.Budget())) == [1, 3]


def test_a_seed_outside_the_lens_or_off_its_byte_span_is_not_rank_help_and_not_offered():
    shelf = _shelf(["r.aug.cdg", "r.cyp.ep"], lens={1})
    outside = _seed(shelf, 2)
    shifted = _seed(shelf, 1, byte_end=999)
    found = po.search_passages(shelf, "q", [outside, shifted], po.Budget())
    assert shelf.seeds_seen == [] and _ids(shelf, found) == [1] and found[0]["voiceable"] is False


def test_the_seeds_go_to_the_ranking_as_rank_help_in_their_reviewed_order():
    shelf = _shelf(["r.aug.cdg", "r.cyp.ep", "r.opt"])
    po.search_passages(shelf, "q", [_seed(shelf, 3, rank=2), _seed(shelf, 2, rank=1)], po.Budget())
    assert shelf.seeds_seen == [2, 3]


def test_a_searched_passage_with_no_seed_is_outside_the_voice_and_cited_by_author_and_work():
    shelf = _shelf(["r.aug.cdg", "r.cyp.ep"])
    found = po.search_passages(shelf, "q", [_seed(shelf, 1)], po.Budget())
    assert [p["voiceable"] for p in found] == [True, False]
    assert found[1]["author_name"] == "Cyprian" and found[1]["work"] == "Letters" and found[1]["fit"] is None
    assert found[0]["date"] == "413 to 426, Documented"
    lines = [po.render_line(c) for c in po.candidates(found, "C1.S1")]
    assert "VOICEABLE" in lines[0] and 'say "Augustine, in City of God, writes"' in lines[0]
    assert "OUTSIDE OUR VOICE" in lines[1] and 'say "Cyprian, in Letters, writes"' in lines[1] and 'never "we"' in lines[1]


def test_a_seed_marked_outside_the_voice_stays_outside_the_voice():
    shelf = _shelf(["r.aug.cdg"])
    assert po.search_passages(shelf, "q", [_seed(shelf, 1, voiceable=False)], po.Budget())[0]["voiceable"] is False


def test_a_passage_is_cited_under_the_world_prefixed_tag():
    shelf = _shelf(["r.cyp.ep"], world="lpc")
    found = po.search_passages(shelf, "q", [], po.Budget())
    assert found[0]["tag"] == po.tag_for("lpc", found[0]["passage_id"]) and found[0]["tag"].startswith("lpc.passage.")


def test_a_passage_with_no_named_author_or_work_is_never_offered():
    shelf = _shelf(["r.anon", "r.cyp.ep"])
    assert _ids(shelf, po.search_passages(shelf, "q", [], po.Budget())) == [2]


def test_a_seed_names_the_author_when_its_row_does_not():
    shelf = _shelf(["r.anon"])
    found = po.search_passages(shelf, "q", [_seed(shelf, 1, author_name="Optatus", work=None)], po.Budget())
    assert found[0]["author_name"] == "Optatus" and po.author_work(found[0]) == "Optatus"


def test_the_budget_caps_passages_and_words():
    many = ["r.aug.cdg", "r.aug.conf", "r.cyp.ep", "r.cyp.unit", "r.opt", "r.aug.ep", "r.aug.ser", "r.cyp.ep"]
    shelf = _shelf(many)
    assert len(po.search_passages(shelf, "q", [], po.Budget())) == 6
    shelf = _shelf(many, words=500)
    found = po.search_passages(shelf, "q", [], po.Budget())
    assert len(found) == 3 and sum(p["word_count"] for p in found) <= 1800
    passages = {1: _p(1, "r.aug.cdg", 1500), 2: _p(2, "r.cyp.ep", 400), 3: _p(3, "r.opt", 300)}
    shelf = FakeShelf("wa", passages, [1, 2, 3])
    assert _ids(shelf, po.search_passages(shelf, "q", [], po.Budget())) == [1, 3]


# Spec 4: the diversity rule.

def _row_ranking(rows):
    """Passages of the given rows in rank order, each row its own work unless the row repeats."""
    return _shelf(rows)


def test_six_of_eight_from_one_author_are_cut_to_three_and_the_rest_keep_rank_order():
    rows = ["r.aug.cdg", "r.aug.conf", "r.cyp.ep", "r.aug.ep", "r.aug.ser", "r.aug.cdg", "r.opt", "r.aug.conf"]
    shelf = _row_ranking(rows)
    found = po.search_passages(shelf, "q", [], po.Budget())
    assert _ids(shelf, found) == [1, 2, 3, 4, 7]
    assert sum(p["author_name"] == "Augustine" for p in found) == 3


def test_no_more_than_two_from_one_work():
    shelf = _row_ranking(["r.aug.cdg", "r.aug.cdg", "r.aug.cdg", "r.cyp.ep", "r.opt", "r.cyp.unit"])
    assert _ids(shelf, po.search_passages(shelf, "q", [], po.Budget())) == [1, 2, 4, 5, 6]


def test_with_one_author_in_the_lens_the_offer_takes_up_to_the_budget_from_that_author():
    shelf = _row_ranking(["r.aug.cdg", "r.aug.conf", "r.aug.ep", "r.aug.ser", "r.aug.cdg", "r.aug.conf", "r.aug.ep"])
    assert len(po.search_passages(shelf, "q", [], po.Budget())) == 6


def test_with_one_work_in_the_lens_the_offer_takes_up_to_the_budget_from_that_work():
    shelf = _row_ranking(["r.aug.cdg"] * 8)
    assert len(po.search_passages(shelf, "q", [], po.Budget())) == 6


def test_with_two_works_in_the_lens_each_work_may_hold_three():
    shelf = _row_ranking(["r.cyp.ep", "r.cyp.ep", "r.cyp.ep", "r.cyp.ep", "r.opt", "r.opt", "r.opt", "r.opt"])
    found = po.search_passages(shelf, "q", [], po.Budget())
    assert _ids(shelf, found) == [1, 2, 3, 5, 6, 7]


def test_a_seed_ranked_first_stays_first_when_the_cap_binds_on_its_author():
    shelf = _row_ranking(["r.aug.cdg", "r.aug.conf", "r.aug.ep", "r.aug.ser", "r.cyp.ep"])
    found = po.search_passages(shelf, "q", [_seed(shelf, 1)], po.Budget())
    assert _ids(shelf, found) == [1, 2, 3, 5] and found[0]["voiceable"] is True


def test_the_word_budget_still_applies_after_the_cap():
    shelf = _shelf(["r.aug.cdg", "r.cyp.ep", "r.opt", "r.aug.conf", "r.cyp.unit"], words=700)
    found = po.search_passages(shelf, "q", [], po.Budget())
    assert _ids(shelf, found) == [1, 2] and sum(p["word_count"] for p in found) <= 1800


def test_a_passage_with_no_author_or_work_is_dropped_before_the_cap_and_takes_no_slot():
    shelf = _row_ranking(["r.anon", "r.anon", "r.aug.cdg", "r.aug.conf", "r.aug.ep", "r.aug.ser", "r.cyp.ep"])
    assert _ids(shelf, po.search_passages(shelf, "q", [], po.Budget())) == [3, 4, 5, 7]


def test_records_in_the_offer_take_no_passage_slot_and_a_one_author_lens_is_not_starved():
    shelf = _row_ranking(["r.aug.cdg"] * 8)
    many_records = [{"id": f"w.quote.{n}"} for n in range(8)]
    request = po.SearchRequest(shelf=shelf, query="q", seeds=(), budget=po.Budget())
    offered = [c for c in po.offer_contents(many_records, [], request) if c.get("record_type") == po.PASSAGE_TYPE]
    assert len(offered) == 6


def test_a_reviewed_seed_of_an_author_the_records_hold_stays_first():
    shelf = _row_ranking(["r.aug.cdg", "r.cyp.ep", "r.opt", "r.aug.conf"])
    request = po.SearchRequest(shelf=shelf, query="q", seeds=(_seed(shelf, 1),), budget=po.Budget())
    offered = [c for c in po.offer_contents([{"id": f"w.quote.aug{n}"} for n in range(5)], [], request) if c.get("record_type") == po.PASSAGE_TYPE]
    assert offered[0]["passage"]["voiceable"] is True and offered[0]["passage"]["passage_id"] == shelf._passages[1]["passage_id"]


def test_the_cap_counts_a_passage_under_the_author_and_work_it_is_cited_as():
    shelf = _row_ranking(["r.anon", "r.anon", "r.anon", "r.anon", "r.cyp.ep"])
    seeds = [_seed(shelf, n, author_name="Optatus", work="Against Parmenian", rank=n) for n in (1, 2, 3, 4)]
    found = po.search_passages(shelf, "q", seeds, po.Budget())
    assert _ids(shelf, found) == [1, 2, 3, 5]
    assert po.passage_keys(found[0]) == ("optatus", ("optatus", "against parmenian"))


def test_seeds_count_only_when_the_offer_file_matches_the_shelf_index():
    shelf = _shelf(["r.aug.cdg"])
    offer = {"index_version": "ix1", "subquestions": {"C1.S1": [_seed(shelf, 1)]}}
    assert len(po.seeds_on_shelf(offer, shelf, "C1.S1")) == 1
    assert po.seeds_on_shelf({**offer, "index_version": "ix0"}, shelf, "C1.S1") == []
    assert po.seeds_on_shelf({**offer, "index_version": None}, shelf, "C1.S1") == []
    assert po.seeds_on_shelf(None, shelf, "C1.S1") == []


def test_diversify_keeps_rank_order_and_only_cuts():
    items = [(a, (a, w)) for a, w in [("x", "1"), ("x", "2"), ("y", "1"), ("x", "3"), ("x", "4"), ("z", "1")]]
    kept = po.diversify(items, 6, lambda item: item)
    assert kept == [items[0], items[1], items[2], items[3], items[5]]


# The seam and the record-side spread.

KWARGS = dict(message="What does your community remember of Jesus?", asks=None, canon_questions=CANON_QUESTIONS, coverage=COVERAGE,
              repository_records=REPOSITORY)


def test_search_off_leaves_the_offer_exactly_as_it_was():
    base = assemble_evidence(**KWARGS)
    assert assemble_evidence(**KWARGS, passage_search=None) == base
    assert po.offer_contents(base["candidates"], []) == base["candidates"]


def test_search_on_places_the_searched_passages_among_the_records_by_rank():
    shelf = _shelf(["r.aug.cdg", "r.cyp.ep"])
    base = assemble_evidence(**KWARGS)
    request = po.SearchRequest(shelf=shelf, query=KWARGS["message"], seeds=(), budget=po.Budget(), sub_question=None)
    found = assemble_evidence(**KWARGS, passage_search=request)
    ids = [c["id"] for c in found["candidates"]]
    tags = [po.tag_for("wa", shelf._passages[n]["passage_id"]) for n in (1, 2)]
    assert [i for i in ids if i not in tags] == [c["id"] for c in base["candidates"]]
    assert ids[:4] == [base["candidates"][0]["id"], tags[0], base["candidates"][1]["id"], tags[1]]
    block = render_evidence_block(found)
    assert f"[[{tags[1]}]] passage (OUTSIDE OUR VOICE" in block
    assert {r["id"] for r in po.offered_records(found["candidates"]).values()} == set(tags)


def test_search_on_with_passage_candidates_given_offers_only_the_searched_passages():
    shelf = _shelf(["r.cyp.ep"])
    request = po.SearchRequest(shelf=shelf, query="q", seeds=(), budget=po.Budget(), sub_question=None)
    stale = po.candidates([{**_seed(shelf, 1), "tag": "wa.passage.stale"}], "C1.S1")
    ids = [c["id"] for c in assemble_evidence(**KWARGS, passage_search=request, passage_candidates=stale)["candidates"]]
    assert "wa.passage.stale" not in ids


SPREAD_REPOSITORY = {
    **REPOSITORY,
    "w.quote.i1": {"id": "w.quote.i1", "record_type": "quote", "text": "jesus meal one", "modern_rendering": "jesus meal one", "speaker_or_author": "ignatius", "canon_cells": ["C-E"]},
    "w.quote.i2": {"id": "w.quote.i2", "record_type": "quote", "text": "jesus meal two", "modern_rendering": "jesus meal two", "speaker_or_author": "ignatius", "canon_cells": ["C-E"]},
    "w.quote.p1": {"id": "w.quote.p1", "record_type": "quote", "text": "jesus", "modern_rendering": "jesus", "speaker_or_author": "pliny", "canon_cells": ["C-E"]},
}


def test_the_record_spread_stays_with_search_off_and_the_capped_rule_fills_floors_with_search_on():
    entry = {**COVERAGE["C-E"], "quotes": ["w.quote.i1", "w.quote.i2", "w.quote.p1"]}
    kwargs = dict(cell="C-E", coverage_entry=entry, repository_records=SPREAD_REPOSITORY, message="jesus meal one two", asks=None)
    spread = [c["id"] for c in select_cell_candidates(**kwargs) if c["record_type"] == "quote"]
    ranked = [c["id"] for c in select_cell_candidates(**kwargs, source_spread=False) if c["record_type"] == "quote"]
    assert [c["id"] for c in select_cell_candidates(**kwargs, source_spread=True) if c["record_type"] == "quote"] == spread
    assert "w.quote.p1" in spread and len(set(spread)) == len(spread)
    assert set(ranked) == {"w.quote.i1", "w.quote.i2"} and "w.quote.p1" not in ranked


def test_a_record_floor_is_cut_by_the_same_caps():
    from engine.m4.evidence import _capped_take
    repo = {f"w.q.{n}": {"id": f"w.q.{n}", "speaker_or_author": "ignatius", "sources": [{"source_id": "w.source.eph"}]} for n in range(4)}
    repo["w.q.p"] = {"id": "w.q.p", "speaker_or_author": "pliny", "sources": [{"source_id": "w.source.ep"}]}
    repo["w.q.j"] = {"id": "w.q.j", "speaker_or_author": "justin", "sources": [{"source_id": "w.source.apol"}]}
    scored = [(f"w.q.{n}", 1.0 - n / 10) for n in range(4)] + [("w.q.p", 0.5), ("w.q.j", 0.4)]
    assert [r for r, _ in _capped_take(scored, repo, 4)] == ["w.q.0", "w.q.1", "w.q.p", "w.q.j"]
    only_one = {k: v for k, v in repo.items() if k.startswith("w.q.") and k[-1].isdigit()}
    assert [r for r, _ in _capped_take(scored[:4], only_one, 3)] == ["w.q.0", "w.q.1", "w.q.2"]
