"""One test per allowed difference class (must pass) and per disallowed
one (must fail) - the ruling's own boundary, pinned. Plus an XML-markup
test and an integration check against a real vendored file already in
`cic/texts/`, so the whole path-resolution + matching pipeline is proven
against real data, not only synthetic strings."""
from pathlib import Path

from engine.m1.quote_verbatim import (
    TEXTS_DIR,
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


def test_bracketed_insertion_not_required_in_source():
    r = _verify("he told [Peter] to wait", "he told him to wait by the gate")
    assert r.verified is True
    assert "bracket" in r.classes_used


def test_bracketed_span_that_is_also_literally_in_source_still_passes():
    r = _verify("he was truly [born]", "he was truly [born], and did eat and drink")
    assert r.verified is True


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


def test_texts_dir_points_at_the_real_vendored_library():
    assert TEXTS_DIR.name == "texts"
    assert TEXTS_DIR.exists()
