"""Tests for engine.m2.builders.build_retrieval_json / _retrieval_words
(Build-Plan.md Stage 4c). Synthetic fixture records, same discipline as
test_demo_tagging.py's own - these are pinned edge cases (a real leak found
and fixed while building this module), which a hand-built fixture makes
exact and reproducible rather than dependent on whichever real record
happens to still exhibit the shape.
"""
import json

from engine.m2.builders import _retrieval_words, build_retrieval_json
from engine.m2.compiler import compile_and_hash


def test_voice_diet_field_is_indexed():
    term = {"id": "fix.term.logos", "record_type": "term", "plain_meaning": "The Word, God's own reason made speech."}
    assert "reason" in _retrieval_words(term)
    assert "speech" in _retrieval_words(term)


def test_instruction_role_field_is_never_indexed():
    """voice_craft declares only "instruction"-role fields - never itself
    retrievable ground, so it must produce an empty word set regardless of
    how much text it carries."""
    craft = {"id": "fix.voice.craft", "record_type": "voice_craft", "identity": "Speak always as a monk of the desert."}
    assert _retrieval_words(craft) == []


def test_a_field_not_declared_for_this_record_type_is_ignored():
    """world_word is a participant-label field for term, not for story -
    a story carrying a stray world_word (or any field its own type never
    declares) must not leak it in."""
    story = {"id": "fix.story.one", "record_type": "story", "tellable_as": "A monk left everything.", "world_word": "should never appear"}
    words = _retrieval_words(story)
    assert "never" not in words and "appear" not in words


def test_dotted_source_id_never_leaks_into_a_quotes_own_words():
    """The real bug found while building this module: quote.sources is
    itself a spoken (participant-label) field, but its own list items
    carry source_id, which tokenizes into ordinary-looking words purely
    because it's a dotted identifier (alx.source.origen-contra-celsum ->
    {alx, source, origen, contra, celsum})."""
    quote = {
        "id": "fix.quote.one",
        "record_type": "quote",
        "text": "A real spoken sentence.",
        "sources": [{"source_id": "alx.source.origen-contra-celsum", "locus": "Book II"}],
    }
    words = _retrieval_words(quote)
    assert "alx" not in words
    assert "celsum" not in words


def test_locus_and_work_are_truncated_before_their_scholarly_apparatus():
    """The other real bug found while building this module: a locus/work
    string's own trailing apparatus (here, a vendored filename in
    parentheses) is exactly what engine.m4.citation_cards.short_head
    already knows not to show a participant - a retrieval ranking must not
    search on more than that same headline."""
    quote = {
        "id": "fix.quote.two",
        "record_type": "quote",
        "text": "Another real spoken sentence.",
        "sources": [{"source_id": "fix.source.one", "locus": "Answering the charge (anf04_obscure-filename-fragment.xml)"}],
    }
    words = _retrieval_words(quote)
    assert "answering" in words and "charge" in words
    assert "anf04_obscure" not in " ".join(words)
    assert "filename" not in words

    source = {"id": "fix.source.two", "record_type": "source", "work": "The Real Title; a scholarly apparatus nobody types"}
    words = _retrieval_words(source)
    assert "real" in words and "title" in words
    assert "scholarly" not in words and "apparatus" not in words


def test_build_retrieval_json_is_one_entry_per_record_sorted_by_id():
    records = {
        "b": {"id": "fix.term.b", "record_type": "term", "plain_meaning": "second"},
        "a": {"id": "fix.term.a", "record_type": "term", "plain_meaning": "first"},
    }
    decoded = json.loads(build_retrieval_json(records))
    assert list(decoded.keys()) == ["fix.term.a", "fix.term.b"]
    assert decoded["fix.term.a"] == ["first"]


def test_a_record_with_no_declared_spoken_fields_present_is_an_empty_list_not_an_error():
    honest = {"id": "fix.honest.one", "record_type": "honest_limit"}
    assert _retrieval_words(honest) == []


def test_deterministic_and_every_real_record_type_reaches_at_least_one_word_on_alx():
    """Real compiled repository content (compile_and_hash, same discipline
    as test_citation_cards.py) - a fleet-sanity check that every genuine
    content record type in a real world is actually retrievable, not just
    the hand-built fixtures above."""
    package, _digest = compile_and_hash(world_key="alx", package_id="TEST", records_commit="TEST", compiler_version="TEST")
    package2, _digest2 = compile_and_hash(world_key="alx", package_id="TEST", records_commit="TEST", compiler_version="TEST")
    assert package["compiled/retrieval.json"] == package2["compiled/retrieval.json"]

    index = json.loads(package["compiled/retrieval.json"])
    records = {r["id"]: r for r in json.loads(package["compiled/repository.json"])["records"]}
    expected_empty = {"voice_craft"}
    for record_id, record in records.items():
        if record.get("record_type") in expected_empty:
            continue
        assert index.get(record_id), f"{record_id} ({record.get('record_type')}) has no retrieval words at all"
