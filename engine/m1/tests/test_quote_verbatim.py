"""One test per allowed difference class (must pass) and per disallowed
one (must fail) - the ruling's own boundary, pinned. Plus an XML-markup
test and an integration check against a real vendored file already in
`cic/texts/`, so the whole path-resolution + matching pipeline is proven
against real data, not only synthetic strings."""
from pathlib import Path

from engine.m1.quote_verbatim import (
    TEXTS_DIR,
    collapse_linewrap_hyphens,
    iter_source_notes,
    resolve_vendored_paths,
    strip_apparatus,
    strip_edition_apparatus,
    strip_xml_markup,
    verify_quote_against_notes,
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


def test_polycrates_to_victor_omission_is_now_marked_and_verifies():
    """Until the 2026-09-22 quote-fidelity record-fix pass, this record
    silently dropped ~15 words of real source text ('when He cometh with
    glory from heaven and shall raise again all the saints') with no
    ellipsis - a genuine unmarked-omission defect, not a verse-number
    gap, and this test originally asserted the new verse_number tolerance
    did not paper over it (`verified is False`). The record-fix pass
    corrected the defect the right way: a real ellipsis mark at the
    dropped span, matching the record's own already-disclosed elision.
    That means it now verifies, and the general principle this test
    guarded - that the verse_number allowance never licenses a wider,
    unmarked skip - is covered independently, without depending on any
    one record's mutable content, by
    test_verse_number_gap_does_not_license_a_wider_skip above."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("pahc")
    fleet = load_fleet_records()
    rec = records["pahc.quote.polycrates-to-victor"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True
    assert "ellipsis" in result.classes_used


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


# --- apparatus (fourth round, 2026-09-23) -------------------------------


def test_soft_hyphen_in_source_passes():
    r = _verify("he did not suppose it", "he did not sup\xadpose it possible")
    assert r.verified is True


def test_tilde_wrapped_digit_with_no_surrounding_space_passes():
    r = _verify("the covenant of God before baptism", "the covenant of God~1~before baptism, and")
    assert r.verified is True


def test_pipe_digit_page_marker_passes():
    r = _verify("he renounced the world in the days", "he renounced the world |146 in the days of Julian")
    assert r.verified is True


def test_bracketed_migne_column_locator_passes():
    r = _verify("linked to her by her parents", "linked to her by her [964D] parents' arrangement")
    assert r.verified is True


def test_bracketed_page_reference_passes():
    r = _verify("darkness like a hyena", "darkness [p. 687] like a hyena")
    assert r.verified is True


def test_bracketed_author_page_line_citation_passes():
    r = _verify("goes a little from the way", "goes [Ov. p. 53, l. 2.] a little from the way")
    assert r.verified is True


def test_short_bracketed_digit_is_not_treated_as_apparatus():
    """The 3-4 digit floor is deliberate: a record's own `[1]`, `[2]`...
    section numbering (desert.quote.the-noonday-demon's own convention)
    is real quoted content already tolerated by the `bracket` class, not
    apparatus - stripping it out of the SOURCE broke the word-adjacency
    that tolerance depends on (a real regression caught before this PR
    shipped). A 1-2 digit bracket must stay untouched by strip_apparatus,
    so a genuinely dropped one-digit bracket still fails as an omission."""
    assert strip_apparatus("it [1] still here") == "it [1] still here"
    assert strip_apparatus("it [12] still here") == "it [12] still here"
    assert strip_apparatus("it [964] gone") == "it gone"


def test_bare_unwrapped_footnote_digit_is_not_silently_tolerated():
    """Deliberately NOT part of `apparatus`: a bare digit with no pipe,
    bracket, or tilde marker of its own (cappadocian.quote.basil-on-
    common-life's real failure: " 1 is more useful" for a footnote
    reference with no wrapper) still fails - the fourth-round docstring
    note explains why a safe, narrow rule for this shape wasn't found."""
    r = _verify(
        "the life of a number lived in common is more useful",
        "the life of a number lived in common 1 is more useful in many ways",
    )
    assert r.verified is False


def test_alx_soft_hyphen_record_now_verifies():
    """alx.quote.no-sun-no-moon-no-sky: 334 literal U+00AD characters in
    its vendored file, the #413-triage's own soft-hyphen finding."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("alx")
    fleet = load_fleet_records()
    rec = records["alx.quote.no-sun-no-moon-no-sky"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)


def test_syr_apparatus_records_now_verify():
    """syr.quote.warned-before-baptism (tilde-digit) and syr.quote.the-
    blasphemy-of-madmen (bracketed author/page/line citation)."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("syr")
    fleet = load_fleet_records()
    for rid in ["syr.quote.warned-before-baptism", "syr.quote.the-blasphemy-of-madmen"]:
        result = verify_quote_record(records[rid], records, fleet)
        assert result.verified is True, (rid, result.failed_segment, result.nearest_context)


def test_desert_pipe_page_marker_records_now_verify():
    """desert.quote.for-thirty-two-years-i-touched-no-fruit,
    desert.quote.pachomius-angel-tablet, and desert.quote.monks-like-
    hyenas all cleared the pipe-plus-digits page marker; desert.quote.
    the-noonday-demon (its own [1]-[6] section numbering) must stay
    verified throughout - the regression this round caught and fixed.
    desert.quote.good-good-i-dont-mind's own bare-digit footnotes
    (" 163 ", " 164 ") are cleared separately, by item 2's per-edition
    apparatus (Palladius) - see test_palladius_bare_digit_footnotes_
    verify_via_edition_apparatus below."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("desert")
    fleet = load_fleet_records()
    for rid in [
        "desert.quote.for-thirty-two-years-i-touched-no-fruit",
        "desert.quote.pachomius-angel-tablet",
        "desert.quote.monks-like-hyenas",
        "desert.quote.the-noonday-demon",
    ]:
        result = verify_quote_record(records[rid], records, fleet)
        assert result.verified is True, (rid, result.failed_segment, result.nearest_context)


def test_cappadocian_macrina_pipe_and_bracket_locator_record_now_verifies():
    """cappadocian.quote.macrina-refuses-remarriage hits both a pipe-page
    marker ("|25") and a bracketed Migne column locator ("[964D]") in the
    same quote - both must clear."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("cappadocian")
    fleet = load_fleet_records()
    rec = records["cappadocian.quote.macrina-refuses-remarriage"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)


# --- note-body fallback (R33, 2026-09-23) -------------------------------
#
# Supersedes R28/#423's per-record `source_note_id` field (never merged):
# the gate itself falls back to every <note> body in the source file once
# the running text fails, so no record carries a pointer to a note.


def test_iter_source_notes_yields_id_and_plain_text_in_order():
    raw = (
        "<p>Running text</p>"
        '<note place="end" n="1" id="my-note-id">'
        "<p>Pliny wrote to Trajan: <i>ministræ</i>, he called them.</p>"
        "</note>"
        '<note place="end" n="2">A note with no id attribute at all.</note>'
    )
    notes = list(iter_source_notes(raw))
    assert [n[0] for n in notes] == ["my-note-id", "#1"]
    assert "Pliny wrote to Trajan" in notes[0][1]
    assert "ministræ" in notes[0][1]
    assert "<i>" not in notes[0][1]
    assert "A note with no id attribute at all." in notes[1][1]


def test_verify_quote_against_notes_finds_a_match_in_the_second_note():
    raw = (
        '<note id="unrelated">Nothing relevant here.</note>'
        '<note id="quoted-note">The governor wrote: I found nothing except a superstition.</note>'
    )
    result = verify_quote_against_notes("I found nothing except a superstition", raw)
    assert result is not None
    assert result.verified is True
    assert result.verified_in == "note"
    assert result.note_id == "quoted-note"


def test_verify_quote_against_notes_returns_none_when_no_note_matches():
    raw = '<note id="unrelated">Nothing relevant here at all.</note>'
    assert verify_quote_against_notes("words that appear nowhere in this file", raw) is None


def test_running_text_match_never_falls_through_to_a_note():
    """A quote present in the running text verifies as running_text, even
    when the same source file also has a note whose text would match -
    the running text is always tried first and wins."""
    raw = (
        "<p>The quick brown fox jumps over the lazy dog.</p>"
        '<note id="decoy">The quick brown fox jumps over the lazy dog.</note>'
    )
    result = verify_quote_text("The quick brown fox jumps over the lazy dog.", raw, source_is_xml=True)
    assert result.verified is True
    assert result.verified_in == "running_text"


def test_a_quote_matching_only_note_commentary_is_reported_as_note_verified_not_hidden():
    """The whole point of `verified_in`/`note_id`: a record verified only
    via a note must be visibly distinguishable from an ordinary
    running-text pass, never silently folded into the same bucket."""
    raw = (
        "<p>The primary narrative says nothing about this at all.</p>"
        '<note id="translator-comment">Here the translator quotes the original at length: '
        "a superstition depraved and immoderate.</note>"
    )
    running_text_result = verify_quote_text("a superstition depraved and immoderate", raw, source_is_xml=True)
    assert running_text_result.verified is False
    note_result = verify_quote_against_notes("a superstition depraved and immoderate", raw)
    assert note_result is not None
    assert note_result.verified is True
    assert note_result.verified_in == "note"
    assert note_result.note_id == "translator-comment"


def test_pahc_deaconesses_record_verifies_via_the_note_fallback_with_no_record_field():
    """pahc.quote.two-female-slaves-who-were-called-deaconesses: R33's own
    real case. Pliny's letter to Trajan is quoted in full inside
    Eusebius's translator's endnote id iii.viii.xxxiii-p2.2, not in the
    running text. No `source_note_id` field on the record - the gate's
    own fallback finds it, restoring verified-direct."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("pahc")
    fleet = load_fleet_records()
    rec = records["pahc.quote.two-female-slaves-who-were-called-deaconesses"]
    assert "source_note_id" not in rec
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)
    assert result.verified_in == "note"
    assert result.note_id == "iii.viii.xxxiii-p2.2"
    assert rec["confidence"]["verification_state"] == "verified-direct"


def test_ordinary_running_text_records_are_unaffected_by_the_note_fallback():
    """A representative sample of already-verified running-text records
    across worlds must still verify the same way (verified_in stays
    "running_text") now that the note fallback exists alongside them."""
    from engine.m1.loader import load_fleet_records, load_world_records

    fleet = load_fleet_records()
    cases = [
        ("pahc", "pahc.quote.tacitus-hatred-against-mankind"),
        ("cappadocian", "cappadocian.quote.macrina-refuses-remarriage"),
        ("rzg", "rzg.quote.christ-the-mirror-of-election"),
    ]
    for world_key, rid in cases:
        records = load_world_records(world_key)
        result = verify_quote_record(records[rid], records, fleet)
        assert result.verified is True, (rid, result.failed_segment, result.nearest_context)
        assert result.verified_in == "running_text"
# --- bracket-locator orphaned-space fix (item 2, fleet-wide, not per-edition) ---


def test_bracket_locator_before_punctuation_no_longer_leaves_orphaned_space():
    """npnf205's own "Him Who is [2002] , nor can there" - stripping
    "[2002] " alone used to leave "is , nor" (a stray space before the
    comma) where the quote's own clean text has "is, nor". The fix
    collapses that leftover space the same way line-wrap hyphenation
    collapses its own typesetting artifact."""
    assert strip_apparatus("Him Who is [2002] , nor can there") == "Him Who is, nor can there"


def test_cappadocian_gregory_nyssa_becoming_god_record_now_verifies():
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("cappadocian")
    fleet = load_fleet_records()
    rec = records["cappadocian.quote.gregory-nyssa-on-becoming-god"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)


# --- edition-level apparatus (item 2, R33: gate/edition-level, never a record field) ---


def test_edition_with_no_apparatus_entry_behaves_exactly_as_today():
    text = "some text with a 300 in it and a [964D] locator too"
    assert strip_edition_apparatus(text, "some-edition-with-no-registry-entry.txt") == text


def test_edition_apparatus_does_not_swallow_a_real_number_construct_the_case():
    """The exact risk item 2 names: a blanket digit rule would swallow
    "5000 monks" if it were real quoted content. Palladius's own
    apparatus entries are anchored to their real evidenced context
    ("from work ... and found", "her lover ... behaving", "Paula, ...
    mother") and must leave an unrelated digit phrase completely alone,
    even inside the very same file."""
    text = "the abbot counted 5000 monks in that valley, then went from work 163 and found peace"
    stripped = strip_edition_apparatus(text, "palladius_lausiac-history_clarke1918.txt")
    assert "5000 monks" in stripped
    assert "163" not in stripped


def test_palladius_bare_digit_footnotes_verify_via_edition_apparatus():
    """desert.quote.good-good-i-dont-mind: two bare endnote numbers
    ("163", "164") glued into the running text with no wrapper of their
    own, cleared only because this edition (and only this edition) has a
    closed apparatus entry for them."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("desert")
    fleet = load_fleet_records()
    rec = records["desert.quote.good-good-i-dont-mind"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)


def test_palladius_paula_comma_footnote_verifies_via_edition_apparatus():
    """hal.quote.hindered-by-jerome: "Paula,276 mother" - the endnote
    number glued directly to the comma, no space at all."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("hal")
    fleet = load_fleet_records()
    rec = records["hal.quote.hindered-by-jerome"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)


def test_ammianus_bare_digit_footnote_verifies_via_edition_apparatus():
    """ijc.quote.ammianus-sicininus-massacre: "Christian church.1" - the
    endnote number glued to the sentence-ending period."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("ijc")
    fleet = load_fleet_records()
    rec = records["ijc.quote.ammianus-sicininus-massacre"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)


def test_basil_common_life_endnote_digit_pattern_clears_but_record_still_fails():
    """cappadocian.quote.basil-on-common-life's own "in common 1 is more"
    endnote number is cleared by endnote-num-after-in-common (checked in
    isolation below) - but the record still does not verify, because the
    same span has a SEPARATE, newly-discovered defect this PR does not
    fix: this edition's own scan reads "Tor just as the foot" where the
    real word is "For" (a genuine OCR misread, not a footnote marker),
    plus a stray inserted curly quote before "To begin" and two more bare
    footnote glyphs ("?", "®") later in the same span. Recorded honestly
    as a new Rulings-Pending entry rather than papered over by stretching
    the apparatus mechanism to hide a real word-level corruption - see
    this PR's own Decision-Log entry."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("cappadocian")
    fleet = load_fleet_records()
    rec = records["cappadocian.quote.basil-on-common-life"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is False
    assert "endnote-num-after-in-common" in [p.name for p in _apparatus_entries_for_basil()]


def _apparatus_entries_for_basil():
    from cic.engine.texts_registry import apparatus_for

    return apparatus_for("basil_ascetic-works-longer-shorter-rules_clarke1925.txt")


def test_basil_common_life_endnote_digit_pattern_isolated():
    text = "the life of a number lived in common 1 is more useful in many ways"
    stripped = strip_edition_apparatus(text, "basil_ascetic-works-longer-shorter-rules_clarke1925.txt")
    assert stripped == "the life of a number lived in common  is more useful in many ways"


def test_basil_work_and_prayer_verifies_via_four_edition_apparatus_patterns():
    """cappadocian.quote.basil-on-work-and-prayer: the registered-mark and
    guillemet footnote glyphs, the stray column-continuation letter "E",
    and an unbracketed Migne column locator ("383A") - all four in one
    record's own span."""
    from engine.m1.loader import load_fleet_records, load_world_records

    records = load_world_records("cappadocian")
    fleet = load_fleet_records()
    rec = records["cappadocian.quote.basil-on-work-and-prayer"]
    result = verify_quote_record(rec, records, fleet)
    assert result.verified is True, (result.failed_segment, result.nearest_context)


def test_basil_registered_mark_glyph_pattern_isolated():
    text = 'Ecclesiastes says: "There is a time for everything." ® But for prayer'
    stripped = strip_edition_apparatus(text, "basil_ascetic-works-longer-shorter-rules_clarke1925.txt")
    assert "®" not in stripped
    assert "everything." in stripped and "But for prayer" in stripped


def test_basil_guillemet_glyph_pattern_isolated():
    text = "as for many other things, » every time is suitable"
    stripped = strip_edition_apparatus(text, "basil_ascetic-works-longer-shorter-rules_clarke1925.txt")
    assert "»" not in stripped
    assert "many other things" in stripped and "every time is suitable" in stripped


def test_basil_stray_column_letter_pattern_isolated():
    text = "in work with \n\nE the tongue if it is possible"
    stripped = strip_edition_apparatus(text, "basil_ascetic-works-longer-shorter-rules_clarke1925.txt")
    assert stripped == "in work with \n\n the tongue if it is possible"


def test_basil_stray_column_letter_pattern_never_strips_a_real_one_letter_word():
    """"I" and "A" are real English words and must never be stripped by
    the column-letter marker, which is anchored to "in work with ...
    the tongue" specifically and to nothing else."""
    text = "in work with I the tongue if it is possible, and A great work it was"
    stripped = strip_edition_apparatus(text, "basil_ascetic-works-longer-shorter-rules_clarke1925.txt")
    assert " I the tongue" in stripped
    assert " A great work" in stripped


def test_basil_unbracketed_column_locator_pattern_isolated():
    text = "commands us to labour and work with our hands that which is 382A written"
    stripped = strip_edition_apparatus(text, "basil_ascetic-works-longer-shorter-rules_clarke1925.txt")
    assert "382A" not in stripped
    assert "that which is" in stripped and "written" in stripped
