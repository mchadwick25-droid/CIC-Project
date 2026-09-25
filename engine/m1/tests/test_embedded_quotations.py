"""Hermetic (no live model call) tests for engine.m1.embedded_quotations:
field-scoping (spoken fields only, never sources[].locus), the word-count
floor, the quote record exclusion, and survey_world's aggregation - plus a
real-record regression pinning OG-10's own worked instance
(worlds/pahc/Open_Gaps_Tracking.md)."""
from engine.m1.embedded_quotations import (
    MIN_QUOTED_WORDS,
    find_embedded_quotations,
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
    """Pinned against worlds/pahc/Open_Gaps_Tracking.md OG-10's own table
    (PR #480's fleet-wide measurement, reproduced here at record-id
    granularity): record counts per world, not span counts (PR #480's own
    span totals used a slightly different counting convention). gallic's
    own count (83) is one below PR #480's original 84 - a known, already
    investigated one-record discrepancy (a hand-read at the time found a
    few of PR #480's raw hits were the project's own analytic prose, not a
    real source quotation), not a regression of this module. don's own
    count dropped from 11 to 6 on 2026-09-25 (worlds/don/Open_Gaps_
    Tracking.md OG-17's re-voicing fix): five records - two `gravity`
    (`martyr-cult-identity`, `parallel-institutional-hierarchy`) and two
    `force` (`transmission-hostile-manuscript-tradition`,
    `vandal-capture-of-carthage`), plus one `gravity` record
    (`rebaptism-boundary-marking`) whose surviving quoted phrase fell
    under the 8-word floor after rewording - lost the quotation marks
    this check was counting because those quoted spans were never a real
    source quotation: OG-17's own pre-fix text quoted internal citations
    to this project's own build documents (e.g. Doc_01 SS2/SS3, Doc_08
    SS8) and one cross-program comparison ("...among the nine confirmed
    worlds"), scare-quoted inside otherwise-plain prose. Removing that
    internal apparatus - OG-17's own fix - correctly took the quote marks
    with it. Confirmed by diffing each of the five records against their
    pre-OG-17 text (git rev faba7b3c): every dropped span is internal-
    apparatus or cross-program text, not source material: no genuine
    historical quotation lost its quotation marks. Not a regression."""
    baseline = {
        "pahc": 14, "syr": 2, "desert": 5, "hal": 5, "alx": 9, "ijc": 7,
        "cappadocian": 3, "don": 6, "rzg": 11, "witt": 48, "gallic": 83,
    }
    for world, expected in baseline.items():
        result = survey_world(world)
        assert result["records_with_embedded_quotation"] == expected, world
