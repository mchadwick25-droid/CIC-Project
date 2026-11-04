import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_spelling as cs  # noqa: E402


def words(text):
    return [(f.word, f.suggestion) for f in cs.scan_text(text)]


def test_british_forms_are_flagged_with_the_american_form():
    assert words("The colour of honour; they organised and travelled.") == [
        ("colour", "color"), ("honour", "honor"), ("organised", "organized"), ("travelled", "traveled"),
    ]


def test_capitalization_is_kept():
    assert words("Centre. DEFENCE.") == [("Centre", "Center"), ("DEFENCE", "DEFENSE")]


def test_words_spelled_the_same_in_both_varieties_are_never_flagged():
    text = "advise exercise promise rigorous vigorous glamour analyses surprise revise comprise otherwise"
    assert words(text) == []


def test_quoted_spans_are_skipped_in_every_quote_style():
    text = ("He said \"the colour\" and “the honour” and 'the favour' and ‘the labour’ "
            "and `the centre` but not the harbour.")
    assert words(text) == [("harbour", "harbor")]


def test_apostrophes_inside_words_are_not_quote_marks():
    assert words("Cyprian's neighbours' colour is don't-care") == [("neighbours", "neighbors"), ("colour", "color")]


def test_paths_urls_code_and_blockquotes_are_skipped():
    text = "See cic/texts/colour_x.txt and https://example.org/colour here.\n> a colour quoted\n```\ncolour\n```\n    colour\n"
    assert words(text) == []


def test_names_spelled_like_british_words_keep_their_capital():
    assert words("Lady Jane Grey wore grey.") == [("grey", "gray")]


RECORD = '''---
id: x.quote.y
record_type: quote
text: "The colour of the harbour, as printed."
edition: "The Honour of Kings"
use_note:
  means: "Pontius says the neighbours fled, and honour was lost; 'their own favour' stays."
notes: >-
  A long note that wraps
  across lines and mentions the
  neighbour twice: neighbour.
---
Body prose: the centre held, and "the centre" stays.
'''


def test_a_quote_records_text_edition_and_title_fields_are_not_checked():
    found = [(f.word, f.line) for f in cs.scan_record(RECORD, "r.md")]
    assert found == [("neighbours", 7), ("honour", 7), ("neighbour", 11), ("neighbour", 11), ("centre", 13)]


def test_a_text_field_on_another_record_type_is_prose_and_is_checked():
    rec = "---\nid: a.story.b\nrecord_type: story\ntext: the colour of it\n---\n"
    assert [f.word for f in cs.scan_record(rec, "r.md")] == ["colour"]


def test_fix_changes_only_the_flagged_words_and_nothing_else():
    fixed = cs.fix_record(RECORD)
    assert 'text: "The colour of the harbour, as printed."' in fixed
    assert "the neighbors fled, and honor was lost; 'their own favour' stays." in fixed
    assert "neighbor twice: neighbor." in fixed
    assert "the center held, and \"the centre\" stays." in fixed
    assert fixed.replace("neighbors", "neighbours").replace("honor", "honour").replace("neighbor", "neighbour").replace(
        "the center held", "the centre held") == RECORD


def test_fix_is_idempotent_and_leaves_a_clean_file_alone():
    once = cs.fix_record(RECORD)
    assert cs.fix_record(once) == once
    assert cs.scan_record(once, "r.md") == []


def test_html_checks_the_text_between_tags_only():
    page = '<p class="colour">The colour</p><script>var colour = 1;</script><!-- colour --><a href="/colour">centre</a>'
    assert [f.word for f in cs.scan_html(page, "p.html")] == ["colour", "centre"]
    fixed = cs.fix_html(page)
    assert 'class="colour"' in fixed and "var colour = 1;" in fixed and "<!-- colour -->" in fixed and ">The color<" in fixed


def test_only_the_enforced_trees_can_fail_a_pull_request():
    assert cs.is_enforced("records/lpc/quote/x.md") == any("records/lpc/quote/x.md".startswith(t) for t in cs.ENFORCED)
    assert not cs.is_enforced("Build/reference/x.md")


def test_a_quotation_that_wraps_across_lines_is_skipped_but_not_across_a_blank_line():
    text = 'Cassian: "fastened within the barriers of the\ncell in some secure harbour" and the harbour here.\n\nA stray " quote\n\nthe labour after a blank line.'
    assert [f.word for f in cs.scan_text(text)] == ["harbour", "labour"]


def test_a_wrapped_quotation_inside_a_record_field_is_skipped():
    rec = ('---\nid: a.demo.b\nrecord_type: demonstration\nnote: |\n'
           '  psalms by heart, "fastened within the barriers\n  of the cell in a secure harbour" and the harbour of prayer\n---\n')
    assert [f.word for f in cs.scan_record(rec, "r.md")] == ["harbour"]
    assert 'secure harbour" and the harbor of prayer' in cs.fix_record(rec)


def test_a_citation_line_names_works_and_keeps_their_titles():
    rec = ('---\nid: a.source.b\nrecord_type: source\nwork: Encyclopaedia Britannica\n'
           'citation: Encyclopaedia Britannica (online), a Reply in Defence of the Doctrines of Men\n'
           'note: the colour of the page\n---\n')
    assert [f.word for f in cs.scan_record(rec, "r.md")] == ["colour"]


def _words(text):
    return [f.word for f in cs.scan_text(text)]


def test_a_place_name_that_is_also_a_british_word_is_left_alone():
    assert _words("Origen died at Tyre.") == []
    assert _words("The old tyre split.") == ["tyre"]


def test_institution_and_work_names_are_left_alone():
    assert _words("Pontifical Institute of Mediaeval Studies at Toronto.") == []
    assert _words("See the Encyclopaedia Iranica entry.") == []
    assert _words("The Labour Party won.") == []
    assert _words("the International Christian Centre in London") == []
    assert _words("Augustine wrote On the Catechising of the Uninstructed.") == []
    assert _words("Athanasius, Defence Against the Arians, is long.") == []
    assert _words("Mediaeval scholars read it.") == ["Mediaeval"]
    assert _words("The centre of the city.") == ["centre"]


def test_a_text_that_names_both_spellings_is_left_alone():
    assert _words("Whether you baptise or baptize babies.") == []
    assert _words("They baptise babies.") == ["baptise"]


def test_new_forms_are_flagged():
    for old in ("recognisable", "organisational", "cataloguers", "councillor", "catalogued"):
        assert _words(f"a {old} case") == [old], old
    assert _words("a gaol") == []


def test_speaker_or_author_is_not_rewritten():
    text = "---\nrecord_type: quote\nspeaker_or_author: Summarising monk\nnote: summarising it\n---\n"
    assert [f.word for f in cs.scan_record(text, "x.md")] == ["summarising"]
