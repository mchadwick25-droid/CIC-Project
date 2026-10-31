"""Context blocks and the fit judge's request, reply and decision. Context
supports no sentence: a sentence tagged to a context block is withheld."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4 import fit_step
from engine.m4.evidence import render_evidence_block
from engine.m4.grounding_net import REASON_CONTEXT_BINDING
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import apply_net

RECORD = {
    "id": "t.quote.one", "record_type": "quote",
    "sources": [{"source_id": "t.source.one", "locus": "Sermon 1; English at cic/texts/sample.txt, lines 100-101"}],
}


@pytest.fixture()
def texts(tmp_path):
    (tmp_path / "cic" / "texts").mkdir(parents=True)
    (tmp_path / "cic" / "texts" / "sample.txt").write_text("\n".join(f"<p>line {n} of the sermon</p>" for n in range(1, 201)), encoding="utf-8")
    return tmp_path


def test_a_block_is_the_text_around_the_cited_lines_with_markup_off(texts):
    blocks = fit_step.context_blocks(RECORD, texts)
    assert [b["id"] for b in blocks] == ["ctx.t.quote.one.1"] and blocks[0]["lines"] == "100-101"
    text = blocks[0]["text"]
    assert "line 100 of the sermon" in text and "line 101 of the sermon" in text and "<p>" not in text
    assert "line 70 of the sermon" in text and "line 131 of the sermon" in text
    assert "line 69 of" not in text and "line 132 of" not in text


def test_a_block_is_at_most_the_word_ceiling(texts):
    assert len(fit_step.context_blocks(RECORD, texts)[0]["text"].split()) <= fit_step.CONTEXT_MAX_WORDS


def test_a_record_with_no_file_and_line_locus_has_no_context(texts):
    bare = {**RECORD, "sources": [{"source_id": "t.source.one", "locus": "Sermon 1"}]}
    missing = {**RECORD, "sources": [{"source_id": "x", "locus": "cic/texts/absent.txt, line 3"}]}
    assert fit_step.context_blocks(bare, texts) == [] and fit_step.context_blocks(missing, texts) == []


def test_only_quotes_and_stories_get_context(texts):
    evidence = {"candidates": [{**RECORD}, {"id": "t.term.one", "record_type": "term", "sources": RECORD["sources"]}]}
    out = fit_step.with_context(evidence, {"t.quote.one": RECORD, "t.term.one": {"id": "t.term.one"}}, texts)
    assert out["candidates"][0]["context"] and "context" not in out["candidates"][1]


def test_the_evidence_block_marks_context_as_supporting_nothing(texts):
    candidate = {"id": "t.quote.one", "record_type": "quote", "head": "head", "context": fit_step.context_blocks(RECORD, texts)}
    block = render_evidence_block({"candidates": [candidate], "thin_ground": [], "figures_already_named": []})
    context = [line for line in block.splitlines() if "CONTEXT ctx.t.quote.one.1" in line]
    assert context and "supports no sentence" in context[0] and "line 100 of the sermon" in context[0]


def test_a_sentence_tagged_to_a_context_block_is_withheld_whatever_it_says():
    records = load_world_records("desert")
    draft = "Abba Moses was once a robber in the desert [[ctx.desert.quote.one.1]]."
    _t, _c, net = apply_net(draft, repository_records=records, thin_topics=None, placement=PlacementContext())
    flagged = [s for s in net["sentences"] if "ctx.desert.quote.one.1" in s["tags"]]
    assert flagged and all(s["verdict"] == "withhold" and s["why"] == REASON_CONTEXT_BINDING for s in flagged)


def test_the_fit_request_carries_question_guards_passage_and_context(texts):
    record = {
        **RECORD, "modern_rendering": "Love, and do what you will.",
        "use_note": {"means": "The root decides the deed.", "not_for": ["a warrant for striking a child"]},
    }
    request = fit_step.fit_request("Is it right to hit a child?", record, fit_step.context_blocks(record, texts))
    assert request["system"] == fit_step.FIT_SYSTEM
    user = request["user"]
    for part in ("Is it right to hit a child?", "The root decides the deed.", "a warrant for striking a child", "Love, and do what you will.", "line 100 of the sermon"):
        assert part in user


def test_a_story_is_passed_at_the_length_told():
    story = {"id": "t.story.one", "record_type": "story", "telling": "The full telling.", "telling_short": "Short.", "telling_medium": "Medium."}
    assert fit_step.passage(story) == "The full telling." and fit_step.passage(story, "short") == "Short."
    assert fit_step.passage({"id": "t.story.two", "record_type": "story", "telling": "Only full."}, "medium") == "Only full."


@pytest.mark.parametrize("reply,expected", [
    ('{"fit": "fits", "reason": "ok", "limit_stated": false}', {"fit": "fits", "reason": "ok", "limit_stated": False}),
    ('Here: {"fit": "off_point", "reason": "x", "limit_stated": true}', {"fit": "off_point", "reason": "x", "limit_stated": True}),
    ('{"fit": "maybe", "reason": "x", "limit_stated": false}', None),
    ('{"fit": "fits", "reason": "x"}', None),
    ("not json", None),
    ("", None),
])
def test_a_reply_is_read_or_refused(reply, expected):
    assert fit_step.parse_fit(reply) == expected


@pytest.mark.parametrize("fit,limit,expected", [
    ("fits", False, "keep"), ("fits", True, "keep"), ("partly", True, "keep"), ("partly", False, "drop"),
    ("off_point", True, "drop"), ("off_point", False, "drop"),
])
def test_the_decision(fit, limit, expected):
    assert fit_step.decide({"fit": fit, "reason": "", "limit_stated": limit}) == expected


def test_an_unreadable_reply_keeps_the_placement():
    assert fit_step.decide(None) == "keep"
