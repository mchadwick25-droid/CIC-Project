"""One test per allowed difference class (must pass) and per disallowed
one (must fail) - the ruling's own boundary, pinned. Plus an XML-markup
test and an integration check against a real vendored file already in
`cic/texts/`, so the whole path-resolution + matching pipeline is proven
against real data, not only synthetic strings."""
from pathlib import Path

from engine.m1.quote_verbatim import (
    TEXTS_DIR,
    collapse_linewrap_hyphens,
    resolve_vendored_paths,
    strip_xml_markup,
    verify_quote_record,
    verify_quote_text,
)


def _verify(quote: str, source: str, *, xml: bool = False):
    return verify_quote_text(quote, source, source_is_xml=xml)


# --- allowed classes: each must pass ---------------------------------


def test_exact_match_passes():
    r = _verify("the quick brown fox", "the quick brown fox jumps")
    assert r.verified is True
    assert r.classes_used == set()


def test_whitespace_difference_passes():
    r = _verify("the quick brown fox", "the quick   brown\nfox jumps")
    assert r.verified is True
    assert "whitespace" in r.classes_used


def test_case_difference_passes():
    r = _verify("The Quick Brown Fox", "the quick brown fox jumps")
    assert r.verified is True
    assert "case" in r.classes_used


def test_punctuation_variant_passes_curly_quotes_and_dashes():
    r = _verify('the fox’s leap—swift', "the fox's leap-swift and true")
    assert r.verified is True
    assert "punctuation" in r.classes_used


def test_ellipsis_marks_a_real_elision_and_passes():
    r = _verify(
        "the fox ran ... and the dog slept",
        "the fox ran quickly through the tall grass and the dog slept soundly",
    )
    assert r.verified is True
    assert "ellipsis" in r.classes_used


def test_bracket_wrapped_ellipsis_is_one_marker_not_a_bracket_around_nothing():
    """Mark's third ruling (2026-09-22, after the #403 triage):
    cappadocian.quote.basil-against-eunomius-ant marks its own elision as
    "[...]" - splitting on bare "..." alone leaves an orphaned literal
    "[" at the end of one segment and "]" at the start of the next."""
    r = _verify(
        "the fox ran [...] and the dog slept",
        "the fox ran quickly through the tall grass and the dog slept soundly",
    )
    assert r.verified is True
    assert "ellipsis" in r.classes_used
    assert "bracket" not in r.classes_used  # the brackets ARE the ellipsis marker, not a separate insertion


def test_line_wrap_hyphenation_in_source_passes():
    """Mark's third ruling: a source hyphenating a word across a line
    break ("eter-\\nnity") is ordinary print typesetting, not a content
    difference - collapsed before matching."""
    r = _verify(
        "he spoke of eternity and grace",
        "he spoke of eter-\nnity and grace",
    )
    assert r.verified is True


def test_line_wrap_hyphenation_collapse_does_not_manufacture_a_false_match():
    """The collapse only joins a hyphen-broken word back into itself - it
    must not make unrelated text on either side of it start matching
    something the quote didn't actually say."""
    r = _verify(
        "he spoke of eternity",
        "he spoke of grace, not eter-\nnity",
    )
    assert r.verified is False  # "eternity" is real, but not adjacent to "of" - still a genuine mismatch
    r2 = _verify(
        "he spoke of graceful things",
        "he spoke of eter-\nnity",
    )
    assert r2.verified is False


def test_collapse_linewrap_hyphens_joins_across_two_consecutive_wraps():
    assert collapse_linewrap_hyphens("com-\nmu-\nnity") == "community"
    assert collapse_linewrap_hyphens("well-being") == "well-being"  # no line break, no collapse


def test_bracketed_insertion_not_required_in_source():
    r = _verify("he told [Peter] to wait", "he told him to wait by the gate")
    assert r.verified is True
    assert "bracket" in r.classes_used


def test_bracketed_span_that_is_also_literally_in_source_still_passes():
    r = _verify("he was truly [born]", "he was truly [born], and did eat and drink")
    assert r.verified is True


def test_inline_verse_number_at_a_sentence_boundary_passes():
    """Mark's second ruling (2026-09-22): class six. A real shape, seen
    across six ANF/NPNF-sourced quotes: 'thus give thanks. 2. First,'
    in the source, 'thus give thanks. First,' in the record."""
    r = _verify(
        "Now concerning the Thanksgiving, thus give thanks. First, concerning the cup",
        "1. Now concerning the Thanksgiving, thus give thanks. 2. First, concerning the cup: We thank thee",
    )
    assert r.verified is True
    assert "verse_number" in r.classes_used


def test_verse_number_gap_does_not_license_a_wider_skip():
    """The allowance is a bare 1-4 digit number plus a period - not an
    arbitrary gap. Real prose standing where a verse number would still
    fails, same as any other unmarked omission."""
    r = _verify(
        "the fox ran and the dog slept",
        "the fox ran quickly through the tall grass and the dog slept",
    )
    assert r.verified is False


# --- disallowed: each must fail ---------------------------------------


def test_word_substitution_fails():
    r = _verify("the quick brown wolf", "the quick brown fox jumps")
    assert r.verified is False


def test_silent_omission_without_ellipsis_fails():
    r = _verify("the fox ran and the dog slept", "the fox ran through the grass and the dog slept")
    assert r.verified is False


def test_addition_outside_brackets_fails():
    r = _verify("he told Peter clearly to wait", "he told him to wait by the gate")
    assert r.verified is False


def test_colon_read_as_dash_fails_not_a_punctuation_variant():
    """The real defect this project already caught by hand (Melito quote,
    2026-09): a colon and a dash are different marks, never equivalent."""
    r = _verify("two natures—of his deity", "he gave us sure indications of his two natures: of his deity")
    assert r.verified is False


def test_empty_quote_text_fails():
    r = _verify("", "anything at all")
    assert r.verified is False


# --- XML markup stripping ----------------------------------------------


def test_strip_xml_markup_drops_note_content_and_pb_but_keeps_scripref_text():
    raw = (
        "Stop your ears, therefore, when any one speaks to you at variance with"
        '<note anchored="yes"><p class="endnote">Literally, "apart from."</p></note> '
        '<pb href="/x/Page_70.html"/> Jesus Christ, who <scripRef>was truly born</scripRef>.'
    )
    stripped = strip_xml_markup(raw)
    assert "apart from" not in stripped
    assert "Page_70" not in stripped
    assert "was truly born" in stripped
    assert "Jesus Christ" in stripped


def test_verify_against_xml_source_ignores_stripped_note():
    source = (
        "Stop your ears, therefore, when any one speaks to you at variance with"
        '<note anchored="yes"><p class="endnote">a footnote that is not part of the reading text</p></note> '
        "Jesus Christ, who was truly born."
    )
    r = _verify("Stop your ears, therefore, when any one speaks to you at variance with Jesus Christ", source, xml=True)
    assert r.verified is True


# --- integration against a real vendored file ---------------------------


def test_resolve_and_verify_a_real_pahc_record():
    """pahc.quote.ignatius-truly-born's own body cites anf01 directly and
    its text is known (project's own re-diff) to match verbatim,
    including the source's own `[truly]` translator bracket."""
    from engine.m1.loader import REPO_ROOT, parse_record_file

    record_path = REPO_ROOT / "records" / "pahc" / "quote" / "pahc.quote.ignatius-truly-born.md"
    if not record_path.exists():
        import pytest

        pytest.skip("fixture record not present in this checkout")
    rec = parse_record_file(record_path)
    result = verify_quote_record(rec, {rec["id"]: rec}, {})
    assert result.verified is True, result.nearest_context


def test_verse_number_ruling_fixes_a_real_previously_failing_record():
    """pahc.quote.first-concerning-the-cup failed the first fleet sweep
    (2026-09-22) on exactly the inline-verse-number pattern the second
    ruling was made to cover ('thus give thanks. 2. First,' in
    anf07's Didache text). Must pass now."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("pahc")
    fleet = load_fleet_records()
    rec = records["pahc.quote.first-concerning-the-cup"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)
    assert "verse_number" in result.classes_used


def test_real_unmarked_omission_still_fails_after_the_verse_number_ruling():
    """pahc.quote.polycrates-to-victor silently drops ~15 words of real
    source text ('when He cometh with glory from heaven and shall raise
    again all the saints') with no ellipsis - a genuine defect, not a
    verse-number gap. The new tolerance must not paper over it."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("pahc")
    fleet = load_fleet_records()
    rec = records["pahc.quote.polycrates-to-victor"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is False


def test_texts_dir_points_at_the_real_vendored_library():
    assert TEXTS_DIR.name == "texts"
    assert TEXTS_DIR.exists()


def test_rzg_line_wrap_hyphenation_records_now_verify():
    """rzg.quote.christ-the-mirror-of-election and rzg.quote.mass-not-a-
    sacrifice were the #403 triage's own "other" cases: 100% verbatim,
    failing only because the vendored .txt hyphenates across line breaks
    ("predes-\\ntination", "eter-\\nnity", "where-\\nfrom",
    "remem-\\nbrance"). Both must verify now."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("rzg")
    fleet = load_fleet_records()
    for rid in ["rzg.quote.christ-the-mirror-of-election", "rzg.quote.mass-not-a-sacrifice"]:
        result = verify_quote_record(records[rid], records, fleet)
        assert result.verified is True, (rid, result.failed_segment, result.nearest_context)


def test_cappadocian_bracket_wrapped_ellipsis_record_now_verifies():
    """cappadocian.quote.basil-against-eunomius-ant marks its own elision
    as "[...]" - the #403 triage's own third flagged pattern."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("cappadocian")
    fleet = load_fleet_records()
    rec = records["cappadocian.quote.basil-against-eunomius-ant"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)
    assert "ellipsis" in result.classes_used
