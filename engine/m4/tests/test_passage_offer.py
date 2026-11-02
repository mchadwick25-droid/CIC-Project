"""The passage offer: leaf passages offered beside records, bound and read like records."""
from engine.m4 import bound_draft, passage_offer as po, verify_step
from engine.m4.evidence import assemble_evidence, render_evidence_block
from engine.m4.tests.test_evidence import CANON_QUESTIONS, COVERAGE, REPOSITORY


def _passage(pid, *, voiceable=True, ocr=0.9, words=100, author="Cyprian", work="Letter 73", rank=None):
    return {
        "passage_id": f"cic:f.xml:{pid}#01", "tag": pid, "file": "f.xml", "text": f"Text of {pid}. It is a sentence.", "word_count": words, "locus": "73",
        "speaker_state": "known" if voiceable else "mixed", "speaker": "cyprian" if voiceable else None, "ocr_score": ocr,
        "role": "tradition" if voiceable else "context", "row_id": "r", "work": work, "author_name": author, "date": "256",
        "voiceable": voiceable, "fit": "direct", "rank": rank, "byte_start": 0, "byte_end": 10,
    }


OFFER = {"world": "fix", "subquestions": {"C1.S1": [_passage("p.a", voiceable=False, rank=4), _passage("p.b", rank=1), _passage("p.c", rank=3), _passage("p.d", words=900, rank=2)]}}


def test_passages_come_in_the_seeds_reviewed_rank_order():
    assert [p["tag"] for p in po.select(OFFER, "C1.S1", po.Budget(10, 5000))] == ["p.b", "p.d", "p.c", "p.a"]


def test_the_budget_caps_passages_and_words_and_skips_one_that_does_not_fit():
    assert [p["tag"] for p in po.select(OFFER, "C1.S1", po.Budget(2, 5000))] == ["p.b", "p.d"]
    assert [p["tag"] for p in po.select(OFFER, "C1.S1", po.Budget(10, 250))] == ["p.b", "p.c"]
    assert [p["tag"] for p in po.select(OFFER, "C1.S1", po.Budget(10, 50))] == []
    assert po.select(OFFER, "C9.S9", po.Budget()) == [] and po.select(OFFER, None, po.Budget()) == []


def test_a_passage_is_a_record_a_sentence_can_bind_to():
    passages = po.select(OFFER, "C1.S1", po.Budget(1, 5000))
    records = po.records_by_id(passages)
    assert verify_step.valid_bindings(["p.b", "p.zzz"], records) == ["p.b"]
    assert bound_draft.bindings(["p.b"], records) == ["p.b"]
    assert "Text of p.b" in verify_step.record_pack(records["p.b"], records)


def test_the_offer_line_names_the_author_and_never_lets_an_outside_voice_say_we():
    lines = {c["id"]: po.render_line(c) for c in po.candidates(po.select(OFFER, "C1.S1", po.Budget(10, 5000)), "C1.S1")}
    assert 'say "Cyprian, in Letter 73, writes"' in lines["p.b"] and "VOICEABLE" in lines["p.b"] and "256" in lines["p.b"]
    assert "OUTSIDE OUR VOICE" in lines["p.a"] and 'never "we"' in lines["p.a"]


def test_passages_ride_in_the_evidence_block_after_the_records_and_do_not_change_them():
    kwargs = dict(message="What does your community remember of Jesus?", asks=None, canon_questions=CANON_QUESTIONS, coverage=COVERAGE, repository_records=REPOSITORY)
    base = assemble_evidence(**kwargs)
    passages = po.candidates(po.select(OFFER, "C1.S1", po.Budget(2, 5000)), "C1.S1")
    both = assemble_evidence(**kwargs, passage_candidates=passages)
    assert both["candidates"][: len(base["candidates"])] == base["candidates"]
    assert [c["id"] for c in both["candidates"][len(base["candidates"]):]] == ["p.b", "p.d"]
    assert "[[p.b]] passage" in render_evidence_block(both)


def test_a_passage_is_cited_under_an_id_the_citation_grammar_reads():
    from engine.m4.grounding_net import _TAG
    from engine.m4.reports.passage_offer_build import tag_for
    tag = tag_for("lpc", "cic:npnf102_augustine-city-of-god-christian-doctrine.xml:iv.XXI.17#01")
    assert _TAG.fullmatch(f"[[{tag}]]") and tag.startswith("lpc.passage.")
    assert tag == tag_for("lpc", "cic:npnf102_augustine-city-of-god-christian-doctrine.xml:iv.XXI.17#01")


def test_a_passage_with_no_author_or_work_is_never_offered():
    offer = {"subquestions": {"C1.S1": [_passage("p.x", author=None, work=None), _passage("p.y", author=None)]}}
    assert [p["tag"] for p in po.select(offer, "C1.S1", po.Budget())] == ["p.y"]
    assert po.author_work(_passage("p.x", author=None, work=None)) is None


def test_the_read_is_shown_who_a_passage_is_from_as_the_voice_was():
    records = po.records_by_id([_passage("p.b"), _passage("p.a", voiceable=False)])
    assert verify_step.record_pack(records["p.b"], records).splitlines()[1] == "passage from Cyprian, in Letter 73, 73, 256"
    assert verify_step.record_pack(records["p.a"], records).splitlines()[1].endswith("(outside our voice)")


def _index(tmp_path, name="i"):
    import sqlite3
    path = tmp_path / f"{name}.sqlite"
    c = sqlite3.connect(path)
    c.executescript("""
    CREATE TABLE meta (key TEXT, value TEXT);
    CREATE TABLE passages (passage_id TEXT, file TEXT, division_locus TEXT, division_title TEXT, language TEXT, apparatus INTEGER,
      speaker_state TEXT, speaker_voice TEXT, ocr_score REAL, byte_start INTEGER, byte_end INTEGER, word_count INTEGER, text TEXT);
    CREATE TABLE passage_rows (passage_id TEXT, world TEXT, row_id TEXT, role TEXT);
    INSERT INTO meta VALUES ('version', 'v1');
    INSERT INTO passages VALUES ('cic:f.xml:a#01', 'f.xml', 'a', '', 'eng', 0, 'known', 'cyprian', 0.9, 0, 10, 100, 'Text of a.');
    INSERT INTO passages VALUES ('cic:f.xml:b#01', 'f.xml', 'b', '', 'eng', 0, 'known', 'cyprian', 0.9, 10, 20, 100, 'Text of b.');
    INSERT INTO passage_rows VALUES ('cic:f.xml:a#01', 'w', 'r1', 'tradition');
    INSERT INTO passage_rows VALUES ('cic:f.xml:b#01', 'w', 'r1', 'tradition');
    """)
    c.commit()
    c.close()
    return path


NARROWED = "row narrowed by locus_ids to r1"
FILE_LEVEL = "file level only: the file is on the world shelf, this work may not be"


def _hit(pid, start, end, **kw):
    hit = {"passage_id": f"cic:f.xml:{pid}#01", "byte_start": start, "byte_end": end, "voice": "voiceable", "role": "own", "rank": 1,
           "shelf_binding": NARROWED, "window": "inside the window", "author": "cyprian", "speaker": {"state": "known", "name": "cyprian"},
           "work": "Letter 73", "fit": "direct", "work_date": {"start": 256, "end": 256, "formation_confidence": "Widely Accepted"}}
    return {**hit, **kw}


def _seed(*hits, index="v1"):
    return {"header": {"world": "w", "index_version": index, "phase": 2}, "subquestions": {"C1.S1": {"seeds": list(hits)}}}


def _offered(tmp_path, *hits, name="i"):
    from engine.m4.reports.passage_offer_build import build_offer
    offer, report = build_offer(_seed(*hits), _index(tmp_path, name))
    return offer["subquestions"].get("C1.S1", []), report


def test_only_a_seed_in_the_worlds_lens_is_offered_and_a_missing_binding_is_not_in_it(tmp_path):
    got, report = _offered(tmp_path, _hit("a", 0, 10), _hit("b", 10, 20, shelf_binding=FILE_LEVEL))
    assert [p["passage_id"] for p in got] == ["cic:f.xml:a#01"] and report["not_in_lens"] == 1
    missing = _hit("b", 10, 20)
    del missing["shelf_binding"]
    assert _offered(tmp_path, missing, name="j")[1]["not_in_lens"] == 1


def test_a_passage_is_voiceable_only_when_seed_role_index_role_speaker_and_window_all_agree(tmp_path):
    assert _offered(tmp_path, _hit("a", 0, 10))[0][0]["voiceable"] is True
    for n, change in enumerate(({"voice": "etic"}, {"role": "outside"}, {"window": "outside the window"}, {"window": None})):
        assert _offered(tmp_path, _hit("a", 0, 10, **change), name=f"k{n}")[0][0]["voiceable"] is False


def test_the_offer_carries_the_works_date_with_its_confidence_and_names_the_author(tmp_path):
    got, _ = _offered(tmp_path, _hit("a", 0, 10), _hit("b", 10, 20, work_date="unresolved: 2 rows disagree", author="gregory-of-nyssa", speaker={"state": "mixed", "name": None}))
    assert got[0]["date"] == "256, Widely Accepted" and got[0]["author_name"] == "Cyprian"
    assert got[1]["date"] is None and got[1]["author_name"] == "Gregory of Nyssa"


def test_a_seed_with_no_author_and_no_work_is_left_out_and_counted(tmp_path):
    got, report = _offered(tmp_path, _hit("a", 0, 10, author="unset: several", speaker={"state": "mixed", "name": None}, work="unset: several"))
    assert got == [] and report["no_source_label"] == 1


def test_an_offer_is_not_built_from_a_seed_made_against_another_index(tmp_path):
    import pytest
    from engine.m4.reports.passage_offer_build import build_offer
    with pytest.raises(SystemExit):
        build_offer(_seed(_hit("a", 0, 10), index="other"), _index(tmp_path))


def test_a_passage_whose_span_differs_from_the_index_is_not_offered(tmp_path):
    got, report = _offered(tmp_path, _hit("a", 0, 11))
    assert got == [] and len(report["unresolved"]) == 1
