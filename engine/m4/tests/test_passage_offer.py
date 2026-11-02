"""The passage offer: leaf passages offered beside records, bound and read like records."""
from engine.m4 import bound_draft, passage_offer as po, verify_step
from engine.m4.evidence import assemble_evidence, render_evidence_block
from engine.m4.reports.passage_offer_build import _line_offset
from engine.m4.tests.test_evidence import CANON_QUESTIONS, COVERAGE, REPOSITORY


def _passage(pid, *, voiceable=True, ocr=0.9, words=100, author="Cyprian", work="Letter 73"):
    return {
        "passage_id": f"cic:f.xml:{pid}#01", "tag": pid, "file": "f.xml", "text": f"Text of {pid}. It is a sentence.", "word_count": words, "locus": "73",
        "speaker_state": "known" if voiceable else "mixed", "speaker": "cyprian" if voiceable else None, "ocr_score": ocr,
        "role": "tradition" if voiceable else "context", "row_id": "r", "work": work, "author_name": author, "date": "256",
        "voiceable": voiceable, "byte_start": 0, "byte_end": 10, "seed_line": 1,
    }


OFFER = {"world": "fix", "subquestions": {"C1.S1": [_passage("p.a", voiceable=False, ocr=0.95), _passage("p.b"), _passage("p.c", ocr=0.5), _passage("p.d", words=900)]}}


def test_voiceable_first_then_cleaner_scan_then_seed_order():
    assert [p["tag"] for p in po.select(OFFER, "C1.S1", po.Budget(10, 5000))] == ["p.b", "p.d", "p.c", "p.a"]


def test_the_budget_caps_passages_and_words_and_skips_one_that_does_not_fit():
    assert [p["tag"] for p in po.select(OFFER, "C1.S1", po.Budget(2, 5000))] == ["p.b", "p.d"]
    assert [p["tag"] for p in po.select(OFFER, "C1.S1", po.Budget(10, 250))] == ["p.b", "p.c"]
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


def test_a_line_number_maps_to_the_byte_offset_of_its_first_byte(tmp_path):
    path = tmp_path / "t.txt"
    path.write_bytes(b"ab\ncde\nf")
    cache: dict = {}
    assert [_line_offset(path, n, cache) for n in (1, 2, 3, 4)] == [0, 3, 7, None]


def test_a_passage_is_cited_under_an_id_the_citation_grammar_reads():
    from engine.m4.grounding_net import _TAG
    from engine.m4.reports.passage_offer_build import tag_for
    tag = tag_for("lpc", "cic:npnf102_augustine-city-of-god-christian-doctrine.xml:iv.XXI.17#01")
    assert _TAG.fullmatch(f"[[{tag}]]") and tag.startswith("lpc.passage.")
    assert tag == tag_for("lpc", "cic:npnf102_augustine-city-of-god-christian-doctrine.xml:iv.XXI.17#01")


def test_a_passage_with_no_author_or_work_is_not_named_by_its_file():
    assert po.author_work({"file": "npnf101_x.xml"}) == "a writing we hold"


def test_the_read_is_shown_who_a_passage_is_from_as_the_voice_was():
    records = po.records_by_id([_passage("p.b"), _passage("p.a", voiceable=False)])
    assert verify_step.record_pack(records["p.b"], records).splitlines()[1] == "passage from Cyprian, in Letter 73, 73"
    assert verify_step.record_pack(records["p.a"], records).splitlines()[1].endswith("(outside our voice)")
