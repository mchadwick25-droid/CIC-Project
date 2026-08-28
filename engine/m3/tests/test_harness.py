from engine.m1.loader import load_world_records
from engine.m3.generation import AnswerResult
from engine.m3.harness import _transitive_source_ids, run_battery


def test_direct_source_citation_resolves():
    records = {
        "w.source.a": {"id": "w.source.a", "record_type": "source", "sources": []},
    }
    assert "w.source.a" in _transitive_source_ids(records)


def test_quote_citing_a_source_resolves_transitively():
    """The alx/hal/syr/ijc convention: a demonstration cites the quote
    record, not the source directly - the quote record's own sources[]
    carries the real source."""
    records = {
        "w.source.a": {"id": "w.source.a", "record_type": "source", "sources": []},
        "w.quote.b": {
            "id": "w.quote.b",
            "record_type": "quote",
            "sources": [{"source_id": "w.source.a"}],
        },
    }
    resolved = _transitive_source_ids(records)
    assert "w.source.a" in resolved
    assert "w.quote.b" in resolved


def test_two_hop_chain_resolves():
    """Not just one hop - a term citing a gravity citing a source should
    still resolve, since the fix is transitive to arbitrary depth, not
    hardcoded to exactly one intermediate hop."""
    records = {
        "w.source.a": {"id": "w.source.a", "record_type": "source", "sources": []},
        "w.gravity.b": {
            "id": "w.gravity.b",
            "record_type": "gravity",
            "sources": [{"source_id": "w.source.a"}],
        },
        "w.term.c": {
            "id": "w.term.c",
            "record_type": "term",
            "sources": [{"source_id": "w.gravity.b"}],
        },
    }
    assert "w.term.c" in _transitive_source_ids(records)


def test_a_citation_with_no_real_source_anywhere_still_fails():
    """The check must not be weakened into "cites something, anything" -
    a record whose sources[] is empty, or whose sources[] only points at
    other records that themselves never bottom out in a real `source`
    record, must NOT resolve. This is the property that keeps
    source_boundedness meaningful as a fabrication check."""
    records = {
        "w.quote.orphan": {"id": "w.quote.orphan", "record_type": "quote", "sources": []},
        "w.term.circular_a": {
            "id": "w.term.circular_a",
            "record_type": "term",
            "sources": [{"source_id": "w.term.circular_b"}],
        },
        "w.term.circular_b": {
            "id": "w.term.circular_b",
            "record_type": "term",
            "sources": [{"source_id": "w.term.circular_a"}],
        },
        "w.term.dangling": {
            "id": "w.term.dangling",
            "record_type": "term",
            "sources": [{"source_id": "w.term.does-not-exist"}],
        },
    }
    resolved = _transitive_source_ids(records)
    assert "w.quote.orphan" not in resolved
    assert "w.term.circular_a" not in resolved
    assert "w.term.circular_b" not in resolved
    assert "w.term.dangling" not in resolved


def test_a_record_that_resolves_only_through_one_of_several_sources_still_resolves():
    """sources[] can carry more than one entry - only one of them needs to
    bottom out in a real source for the citing record to be bounded."""
    records = {
        "w.source.a": {"id": "w.source.a", "record_type": "source", "sources": []},
        "w.quote.b": {
            "id": "w.quote.b",
            "record_type": "quote",
            "sources": [{"source_id": "w.term.nowhere"}, {"source_id": "w.source.a"}],
        },
    }
    assert "w.quote.b" in _transitive_source_ids(records)


def test_fixture_world_battery_still_passes_after_the_fix():
    """The clean fixture world (schema convention: cites sources directly)
    must keep passing exactly as before - this fix only widens what
    resolves, it must never narrow it."""
    records = load_world_records("fix")
    results = run_battery("fix", records)
    assert results
    assert all(r.passed for r in results), [r for r in results if not r.passed]


class _AlwaysVoiceScaffoldAnswerer:
    """Every probe answered by citing the world's own sourceless voice_craft
    record - the shape a real LiveModelAnswerer produces when it draws on
    Identity/Guard/Characteristic-concerns/Flavor-notes content, per the
    compiled prompt's own "(cite as [[id]])" instruction
    (engine/m2/builders.py)."""

    def answer(self, cell, probe_text):
        return AnswerResult(text="A plain answer in the voice's own framing.", citations=["w.voice.craft"],
                             source_record_id="w.voice.craft", source_record_type="voice_craft")


def test_run_battery_wires_voice_scaffold_ids_through_end_to_end():
    """Not just a unit-level grading.py fact - run_battery itself must
    build voice_scaffold_ids from the records it was actually given and
    hand it to source_boundedness_check, the same way it already does for
    known_source_ids. A world whose ONLY citation surface is a sourceless
    voice_craft record must clear the full battery, exactly the case a
    live desert/alx/... run hits whenever the model answers from its own
    identity framing rather than retrieved source-backed content."""
    records = {
        "w.voice.craft": {"id": "w.voice.craft", "record_type": "voice_craft", "sources": []},
    }
    results = run_battery("w", records, answerer=_AlwaysVoiceScaffoldAnswerer())
    assert results
    assert all(r.passed for r in results), [r for r in results if not r.passed]
