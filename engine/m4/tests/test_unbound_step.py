"""The unbound-sentence step: classify what the voice shipped without a binding,
and check a denial of what the sources hold against the shelf."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4 import unbound_step as us

LIMIT = "lpc.limit.womens-own-voice"


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


def _entry(sentence, tags=(), verdict="ok", **extra):
    return {"sentence": sentence, "tags": list(tags), "verdict": verdict, **extra}


def test_shipped_items_mark_bound_unbound_and_withheld_and_skip_placed(records):
    answer = {"net_sentences": [
        _entry("Bound.", [LIMIT]), _entry("Untagged."), _entry("Context only.", ["ctx.x.1"]),
        _entry("Withheld with a tag.", [LIMIT], verdict="withhold"), _entry("Placed lead-in.", [LIMIT], placed_quote=True),
        _entry("A story sentence.", [], placed_story=True),
    ]}
    items = us.shipped_items(answer, records)
    assert [(i["n"], i["bound"], i["withheld"]) for i in items] == [(0, True, False), (1, False, False), (2, False, False), (3, False, True)]


@pytest.mark.parametrize("reply, expected", [
    ('{"kind": "connective", "denies": null}', {"kind": "connective", "denies": None}),
    ('Here: {"kind": "limit", "denies": "how the Maximinus conference ended"}', {"kind": "limit", "denies": "how the Maximinus conference ended"}),
    ('{"kind": "limit", "denies": ""}', {"kind": "limit", "denies": None}),
    ('{"kind": "opinion", "denies": null}', None), ("nothing", None), ('{"kind": "limit", "denies": 3}', None),
])
def test_parse_classify(reply, expected):
    assert us.parse_classify(reply) == expected


def test_decide_classified():
    limit = {"kind": "limit", "denies": "the rite"}
    assert us.decide_classified({"kind": "connective", "denies": None}, False) == "keep"
    assert us.decide_classified({"kind": "conversation", "denies": None}, False) == "keep"
    assert us.decide_classified({"kind": "world_claim", "denies": None}, False) == "withhold"
    assert us.decide_classified({"kind": "world_claim", "denies": None}, True) == "keep"
    assert us.decide_classified(limit, False) == us.decide_classified(limit, True) == "shelf_check"
    assert us.decide_classified({"kind": "limit", "denies": None}, False) == "shelf_check"
    assert us.decide_classified(None, False) == "keep"


@pytest.mark.parametrize("reply, expected", [
    ('{"covered": true, "where": "a.txt 3-9", "reason": "x"}', {"covered": True, "where": "a.txt 3-9", "reason": "x"}),
    ('{"covered": false}', {"covered": False, "where": "", "reason": ""}), ('{"covered": "yes"}', None), ("", None),
])
def test_parse_shelf_and_decide(reply, expected):
    judgement = us.parse_shelf(reply)
    assert judgement == expected
    assert us.decide_shelf(judgement) == ("withhold" if expected and expected["covered"] else "keep")


def test_query_terms_rank_suggested_then_denied_then_sentence_then_question():
    terms = us.query_terms("What happened at the meeting with Maximinus?", "Our record does not say how it ended.",
                           "how the Maximinus conference ended", ["disputation", "Arian"])
    assert terms["disputation"] == terms["arian"] == us.SUGGESTED_WEIGHT
    assert terms["conference"] == us.DENIED_WEIGHT and terms[us._normalise("maximinus")] == us.DENIED_WEIGHT
    assert terms["ended"] == us.DENIED_WEIGHT and terms["meeting"] == us.QUESTION_WEIGHT


@pytest.mark.parametrize("reply, expected", [
    ('{"terms": ["Maximinus", " Arian ", ""]}', ["Maximinus", "Arian"]), ('{"terms": "x"}', None), ('{"terms": [1]}', None), ("no", None),
])
def test_parse_terms(reply, expected):
    assert us.parse_terms(reply) == expected


def test_the_shelf_search_finds_the_window_that_holds_the_terms_and_shows_where(tmp_path):
    (tmp_path / "a.txt").write_text("\n".join(["filler line"] * 30 + ["Maximinus came to the conference at Hippo", "and used the day with a long speech", "then went to Carthage"] + ["filler line"] * 30))
    (tmp_path / "b.txt").write_text("Maximinus alone.\n" * 3)
    index = us.ShelfIndex(tmp_path, ["a.txt", "b.txt"], {"maximinus", "conference", "hippo", "speech"})
    found = index.search({"maximinus": 2.0, "conference": 2.0, "hippo": 1.0, "speech": 1.0})
    assert found and found[0]["file"] == "a.txt" and "long speech" in found[0]["text"]
    lo, hi = (int(x) for x in found[0]["lines"].split("-"))
    assert lo <= 31 <= hi
    assert all(p["file"] != "b.txt" for p in found)


def test_the_shelf_request_names_the_denial_and_the_places(tmp_path):
    request = us.shelf_request("Q?", "Our record is silent.", "how it ended", [{"file": "a.txt", "lines": "1-5", "text": "It ended badly."}])
    assert "THE SENTENCE DENIES\nhow it ended" in request["user"] and "[a.txt lines 1-5]" in request["user"]
    assert "(no passage on the shelf matched)" in us.shelf_request("Q?", "S.", "x", [])["user"]


def test_the_passage_shown_holds_the_matching_lines_and_is_labelled_by_what_is_shown(tmp_path):
    long = "x" * 450
    lines = [long] * 4 + ["Marcellinus presided over the conference"] + [long] * 12
    (tmp_path / "a.txt").write_text("\n".join(lines))
    index = us.ShelfIndex(tmp_path, ["a.txt"], {"marcellinu", "conference", "presided"})
    found = index.search({"marcellinu": 2.0, "conference": 2.0, "presided": 1.0})
    assert found and "Marcellinus presided over the conference" in found[0]["text"]
    assert len(found[0]["text"]) <= us.PASSAGE_CHARS + 20
    lo, hi = (int(x) for x in found[0]["lines"].split("-"))
    assert lo <= 5 <= hi


def test_a_missing_shelf_file_is_recorded(tmp_path):
    (tmp_path / "a.txt").write_text("Maximinus")
    index = us.ShelfIndex(tmp_path, ["a.txt", "gone.txt"], {"maximinu"})
    assert index.missing_files == ["gone.txt"]


def test_the_budget_goes_to_matching_lines_before_context_and_long_lines_are_cut_around_the_hit(tmp_path):
    filler = "word " * 150
    lines = [filler] * 6 + [filler + "Primian spoke at the conference " + filler] + [filler] * 8
    (tmp_path / "a.txt").write_text("\n".join(lines))
    index = us.ShelfIndex(tmp_path, ["a.txt"], {"primian", "conference"})
    text = index.search({"primian": 2.0, "conference": 2.0})[0]["text"]
    assert "Primian spoke at the conference" in text
    assert len(text) <= us.PASSAGE_CHARS + 20
