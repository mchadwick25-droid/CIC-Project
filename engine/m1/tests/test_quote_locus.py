"""The locus check: a quote's text must occur at the lines its own locus cites."""
import copy

from engine.m1 import gates
from engine.m1.loader import load_world_records
from engine.m1.quote_locus import cited_spans, gate_quote_locus, unchecked_quotes

QUOTE = "lpc.quote.a-respite-from-their-torments"


def _records():
    return copy.deepcopy(load_world_records("lpc"))


def _run(rec):
    return gate_quote_locus({rec["id"]: rec}, {}, {})


def test_a_quote_at_its_cited_span_passes():
    assert _run(_records()[QUOTE]) == []


def test_a_changed_word_fails_with_the_failed_segment():
    rec = _records()[QUOTE]
    rec["text"] = rec["text"].replace("tender", "stern", 1)
    [finding] = _run(rec)
    assert "does not occur at its cited locus" in finding and "stern" in finding


def test_a_span_that_has_moved_off_the_passage_fails():
    rec = _records()[QUOTE]
    ref = cited_spans(rec)[0]
    first, last = (int(n) for n in ref["lines"].split("-"))
    moved = f"{ref['file']}, lines {first + 400}-{last + 400}"
    rec["sources"] = [{"source_id": rec["sources"][0]["source_id"], "locus": moved}]
    assert len(_run(rec)) == 1


def test_a_span_past_the_end_of_the_file_is_reported_as_unresolved():
    rec = _records()[QUOTE]
    rec["sources"] = [{"source_id": rec["sources"][0]["source_id"], "locus": "cic/texts/no_such_file.xml, lines 1-5"}]
    [finding] = _run(rec)
    assert "fails to resolve" in finding


def test_a_quote_passes_when_any_one_of_its_spans_holds_the_text():
    rec = _records()[QUOTE]
    good = cited_spans(rec)[0]
    rec["sources"] = [{"source_id": rec["sources"][0]["source_id"], "locus": f"English at cic/texts/no_such_file.xml, lines 1-5; English at {good['file']}, lines {good['lines']}"}]
    assert _run(rec) == []


def test_a_quote_citing_no_span_is_not_checked_and_is_counted():
    rec = _records()[QUOTE]
    rec["sources"] = [{"source_id": rec["sources"][0]["source_id"], "locus": "Ep. 5, with no line span"}]
    assert _run(rec) == []
    assert unchecked_quotes({rec["id"]: rec}) == [rec["id"]]


def test_a_paraphrase_only_quote_is_out_of_scope():
    rec = _records()[QUOTE]
    rec["license"] = "paraphrase-only"
    rec["text"] = "words that are nowhere in the file"
    assert _run(rec) == []


def test_the_gate_is_registered():
    assert gates.GATES["quote-locus"] is gate_quote_locus
