"""The Stage 3 still-works check on lpc: the marks, hovers and source references a participant has today are
unchanged on the changed path (a story and a quote now also carry their vendored spans and a story its telling)."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4.term_glosses import find_glosses_used
from engine.m4.transparency_plan import build_transparency_plan

STORY = "lpc.story.celerinus-writes-to-lucian"
QUOTE = "lpc.quote.a-respite-from-their-torments"
TERM = "lpc.term.catechesis"
WITNESS = "lpc.witness.punishment-without-end"
SOURCE_KEYS = {"source_id", "locus", "author", "work", "rights_status", "edition"}


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


@pytest.fixture(scope="module")
def plan(records):
    quoted = records[QUOTE]["modern_rendering"].split(".")[0]
    rows = [
        ("A person is taught the creed before the water, in catechesis.", [TERM], "ok"),
        ("Celerinus, a confessor, asked Lucian to seek peace for his sister.", [STORY], "ok"),
        ("Lucian gave it, if each case went before the bishop.", [STORY], "ok"),
        (f'Augustine wrote: "{quoted}."', [QUOTE], "ok"),
        ("The punishment of the lost has no end.", [WITNESS], "ok"),
    ]
    text = " ".join(s for s, _t, _v in rows)
    net_result = {"sentences": [{"sentence": s, "tags": t, "verdict": v} for s, t, v in rows]}
    citations = [{"sentence": s, "record_ids": t} for s, t, _v in rows]
    glosses = [g for g in find_glosses_used(text, citations, records) if g["id"] == TERM]
    return build_transparency_plan(citations=citations, net_result=net_result, repository_records=records, world_key="lpc", text=text, glosses=glosses)


def _of(plan, record_id):
    return [e for e in plan["elements"] if e["record_id"] == record_id]


def _card(plan, record_id):
    return next(c for c in plan["references"] if c["record_id"] == record_id)


def test_a_story_a_quote_and_a_lexicon_word_each_keep_their_inline_mark(plan, records):
    [story] = _of(plan, STORY)
    assert story["kind"] == "story" and story["sentence_index"] == 2 and story["repeat"] is False
    [quote] = _of(plan, QUOTE)
    assert quote["kind"] == "quote"
    [term] = _of(plan, TERM)
    assert term["kind"] == "term" and term["surface"].lower() == "catechesis"
    for element in (story, quote, term):
        assert _card(plan, element["record_id"])["confidence"] == records[element["record_id"]]["confidence"]


def test_every_card_keeps_the_fields_it_had_and_only_adds(plan):
    for card in plan["references"]:
        assert {"record_id", "record_type", "label", "sources", "world_key", "confidence"} <= set(card) and card["label"]
        for source in card["sources"]:
            assert SOURCE_KEYS <= set(source)
    quote = _card(plan, QUOTE)
    assert quote["spoken_rendering"] and quote["speaker"]


def test_the_story_and_quote_cards_now_carry_what_the_click_needs(plan):
    story = _card(plan, STORY)
    assert story["means"] and story["narrative_tier"] == 1 and story["heart"]
    assert story["sources"][0]["vendored"][0]["file"].startswith("cic/texts/")
    quote = _card(plan, QUOTE)
    assert all(ref["file"].startswith("cic/texts/") for ref in quote["sources"][0]["vendored"])


def test_a_plain_citation_still_resolves_to_its_sourcing_links(plan):
    card = _card(plan, WITNESS)
    assert card["sources"] and all(SOURCE_KEYS <= set(s) for s in card["sources"])
    assert all("vendored" not in s for s in card["sources"])
