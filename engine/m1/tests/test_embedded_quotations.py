"""Hermetic (no live model call) tests for engine.m1.embedded_quotations:
field-scoping (spoken fields only, never sources[].locus), the word-count
floor, the quote record exclusion, family-aware quote pairing, the
build-document self-quote tag, and survey_world's aggregation - plus a
real-record regression pinning OG-10's own worked instance
(worlds/pahc/Open_Gaps_Tracking.md)."""
from engine.m1.embedded_quotations import (
    MIN_QUOTED_WORDS,
    find_embedded_quotations,
    quoted_spans_by_family,
    survey_world,
)


def test_a_short_quoted_span_under_the_word_floor_is_not_flagged():
    record = {"record_type": "story", "text": 'She said, "hello there," and left.'}
    assert find_embedded_quotations(record) == []


def test_a_long_quoted_span_at_or_above_the_word_floor_is_flagged():
    record = {
        "record_type": "story",
        "text": 'He writes, "Take ye heed, then, to have but one Eucharist, for there is one flesh."',
    }
    hits = find_embedded_quotations(record)
    assert len(hits) == 1
    assert hits[0]["words"] >= MIN_QUOTED_WORDS
    assert hits[0]["field"] == "text"


def test_a_quote_record_is_never_surveyed_even_with_a_long_embedded_span():
    """quote records own this question through their own modern_rendering
    field and engine.m1.gates's existing quote-specific check - excluded
    by the caller (survey_world), not by find_embedded_quotations itself,
    which only looks at the fields it is handed."""
    records = {
        "w.quote.x": {
            "id": "w.quote.x",
            "record_type": "quote",
            "text": '"Take ye heed, then, to have but one Eucharist, for there is one flesh."',
        }
    }
    result = survey_world("w", load=lambda _world: records)
    assert result["findings"] == []
    assert result["non_quote_records"] == 0


def test_a_citation_apparatus_field_is_never_scanned():
    """sources[].locus is never compiled into what the voice sees or
    says - a long quoted-looking span there is not this check's concern,
    since fields_with_role only returns declared voice-diet/evidence-head
    fields for the record's own record_type."""
    record = {
        "record_type": "story",
        "text": "A short telling.",
        "sources": [{"source_id": "w.source.x", "locus": '"a very long quoted locus description spanning many words here"'}],
    }
    assert find_embedded_quotations(record) == []


def test_survey_world_counts_records_not_spans_and_skips_quote_records():
    records = {
        "w.story.a": {
            "id": "w.story.a",
            "record_type": "story",
            "text": 'He writes, "Take ye heed, then, to have but one Eucharist, for there is one flesh."',
        },
        "w.quote.b": {
            "id": "w.quote.b",
            "record_type": "quote",
            "text": '"Take ye heed, then, to have but one Eucharist, for there is one flesh."',
        },
        "w.story.c": {"id": "w.story.c", "record_type": "story", "text": "Nothing quoted here."},
    }
    result = survey_world("w", load=lambda _world: records)
    assert result["non_quote_records"] == 2
    assert result["records_with_embedded_quotation"] == 1
    assert [f["id"] for f in result["findings"]] == ["w.story.a"]


def test_real_pahc_regression_one_eucharist_under_bishop_og10():
    """worlds/pahc/Open_Gaps_Tracking.md OG-10's own worked instance:
    pahc.story.one-eucharist-under-bishop carries the ANF translation's
    archaic wording (brackets and all) with no modern-English rendering -
    a real content gap, not a synthetic fixture."""
    from engine.m1.loader import load_world_records

    records = load_world_records("pahc")
    record = records["pahc.story.one-eucharist-under-bishop"]
    hits = find_embedded_quotations(record)
    assert hits, "OG-10's own worked instance should still be caught"
    assert any("Eucharist" in h["span"] for h in hits)


def test_fleet_survey_world_counts_match_the_og10_baseline():
    """Pinned against worlds/pahc/Open_Gaps_Tracking.md OG-10's own table:
    record counts per world (not span counts, which move independently as
    pairing/self-quote fixes land)."""
    baseline = {
        "pahc": 14, "syr": 2, "desert": 5, "hal": 5, "alx": 9, "ijc": 7,
        "cappadocian": 3, "don": 5, "rzg": 11, "witt": 48, "gallic": 63,
    }
    for world, expected in baseline.items():
        result = survey_world(world)
        assert result["records_with_embedded_quotation"] == expected, world


def test_quoted_spans_by_family_never_pairs_a_double_open_with_a_single_close():
    """A single-quoted sentence with a nested double-quoted phrase inside
    it (the real shape found in gallic.force.power-displayed-disowned's
    own description field) must not let the inner double-quote's own
    close swallow the outer single quote's real close - the outer
    single-quoted span must still reach its own real end. The inner
    double-quoted phrase is also, correctly, its own separate span (each
    family is scanned independently) - not a bug, just a nested quote."""
    text = "before 'it never became an argument, which is Doc_04's own \"strongest case\" and is not resolved.' after"
    inners = [s[2] for s in quoted_spans_by_family(text)]
    assert 'it never became an argument, which is Doc_04\'s own "strongest case" and is not resolved.' in inners


def test_quoted_spans_by_family_pairs_double_and_single_independently():
    text = 'He said "a real double quote here" and also \'a real single quote here\'.'
    spans = quoted_spans_by_family(text)
    inners = [s[2] for s in spans]
    assert "a real double quote here" in inners
    assert "a real single quote here" in inners


def test_a_real_close_ending_in_s_is_not_mistaken_for_a_possessive():
    """An earlier version of this module tried to guess "possessive, not a
    close" from local context alone (a word ending in s, an apostrophe,
    then a lowercase word) and rejected real closes that happen to fit
    that shape - "within us'" (not even a possessive - "us" just ends in
    s) followed by "and he meant it", and "'nourishes'" (a one-word
    quotation) followed by "the poor man's prayer". Both must still close
    at the first single-quote mark after their own open, exactly like any
    other close."""
    text = "'the kingdom of God is within us' and he meant it plainly, not as a riddle."
    spans = quoted_spans_by_family(text)
    assert len(spans) == 1
    assert spans[0][2] == "the kingdom of God is within us"


def test_nourishes_closes_immediately_not_at_a_later_apostrophe():
    """The real pahc.witness.marriage-and-wealth shape (positions field):
    two short single-word/short-phrase quotations close-by, separated by
    plain prose carrying its own unrelated possessive apostrophes
    ("man's"). Each quote must close at its own very next single-quote
    mark, not skip past it looking for a "better" close."""
    text = "the rich man's wealth 'nourishes' the poor man's prayer, and the poor man's prayer, 'rich in intercession,' in turn benefits the rich man before God."
    spans = quoted_spans_by_family(text)
    inners = [s[2] for s in spans]
    assert "nourishes" in inners
    assert "rich in intercession," in inners


def test_a_leading_tis_contraction_never_opens_a_span():
    text = "'Tis a small thing, he said, and left it there without another word about it at all."
    assert quoted_spans_by_family(text) == []


def test_a_close_immediately_before_an_em_dash_is_still_detected():
    text = "before 'a real quotation of some real length here, spoken plainly'—and the sentence continues after it."
    spans = quoted_spans_by_family(text)
    assert len(spans) == 1
    assert spans[0][2] == "a real quotation of some real length here, spoken plainly"


def test_a_span_naming_the_build_apparatus_is_tagged_not_counted_as_an_old_translation():
    record = {
        "record_type": "force",
        "description": 'The finding stands: \'this connects directly to Doc_04\'s own G6 cell and the CLASSIFICATION layer above it, tying formation to structure\'.',
    }
    hits = find_embedded_quotations(record)
    assert len(hits) == 1
    assert hits[0]["self_quote_of_build_document"] is True


def test_survey_world_counts_a_build_document_self_quote_separately_from_old_translations():
    records = {
        "w.force.a": {
            "id": "w.force.a",
            "record_type": "force",
            "description": "'this connects to Doc_04 and the CLASSIFICATION layer, tying formation to structure directly'.",
        },
        "w.story.b": {
            "id": "w.story.b",
            "record_type": "story",
            "text": 'He writes, "Take ye heed, then, to have but one Eucharist, for there is one flesh."',
        },
    }
    result = survey_world("w", load=lambda _world: records)
    assert [f["id"] for f in result["findings"]] == ["w.story.b"]
    assert result["records_with_embedded_quotation"] == 1
    assert [f["id"] for f in result["self_quote_findings"]] == ["w.force.a"]
    assert result["records_with_build_document_self_quote"] == 1
