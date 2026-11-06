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


def test_forms_found_by_the_final_sweep_are_flagged():
    for old, new in (
        ("reorganised", "reorganized"), ("reorganisation", "reorganization"), ("rebaptised", "rebaptized"),
        ("unbaptised", "unbaptized"), ("anathematised", "anathematized"), ("anathematising", "anathematizing"),
        ("regularised", "regularized"), ("regularisation", "regularization"), ("unauthorised", "unauthorized"),
        ("synthesised", "synthesized"), ("synthesises", "synthesizes"), ("dramatising", "dramatizing"),
        ("apostatised", "apostatized"), ("judaisers", "judaizers"), ("legitimise", "legitimize"),
        ("institutionalisation", "institutionalization"), ("scandalised", "scandalized"), ("stylised", "stylized"),
        ("marginalised", "marginalized"), ("capitalised", "capitalized"), ("marvelled", "marveled"),
        ("jewelled", "jeweled"), ("unfavourable", "unfavorable"), ("tricolour", "tricolor"),
        ("ardour", "ardor"), ("succour", "succor"), ("uncatalogued", "uncataloged"),
    ):
        assert words(f"a {old} thing") == [(old, new)], old


def test_words_that_are_spelled_the_same_in_both_varieties_stay_unflagged_in_the_sweep():
    assert words("advertising unwilling improvised appalled annulled rebelled sunrise surmise tortoise") == []


def test_json_string_values_are_scanned_and_names_and_titles_are_skipped():
    import json
    doc = {
        "name": "The Labour Church",
        "why": "They travelled to the centre of the city.",
        "sources": [{"work": "Civilisation and Its Discontents", "note": "A defence of the plan."}],
        "documentedStories": [{"title": "Against the Judaisers", "text": "He praised the \"honour of the realm\" and its labour."}],
    }
    text = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    found = sorted(f.word for f in cs.scan_json(text, "x.json"))
    assert found == ["centre", "defence", "labour", "travelled"]
    fixed = json.loads(cs.fix_json(text))
    assert fixed["name"] == doc["name"]
    assert fixed["sources"][0]["work"] == doc["sources"][0]["work"]
    assert fixed["documentedStories"][0]["title"] == doc["documentedStories"][0]["title"]
    assert fixed["why"] == "They traveled to the center of the city."
    assert fixed["documentedStories"][0]["text"] == 'He praised the "honour of the realm" and its labor.'


def test_json_layout_is_never_changed():
    text = '{"why":"the centre",\n  "list": ["a defence",\n "b"],\n"name":"The Centre"}'
    assert cs.fix_json(text) == '{"why":"the center",\n  "list": ["a defense",\n "b"],\n"name":"The Centre"}'


def test_json_embedded_in_a_script_block_is_fixed_in_place():
    page = '<script>\nconst DATA = {\n "movements": [\n  {"why": "a labour", "name": "Labour"}\n ]\n};\nconst x = "centre";\n</script>'
    fixed = cs.fix_embedded_json(page, "const DATA = ")
    assert '"why": "a labor"' in fixed and '"name": "Labour"' in fixed and 'const x = "centre";' in fixed


def test_a_plain_yaml_file_is_scanned_and_fixed_in_place():
    text = "id: rzg\ndisplay_name: The Reformed Centre\nentry:\n  topics:\n  - word: Baptism\n    note: They baptised infants.\n  - word: x\n    note: 'a labour of love'\n"
    assert sorted(f.word for f in cs.scan_yaml(text, "x.yaml")) == ["baptised", "labour"]
    fixed = cs.fix_yaml(text)
    assert fixed == text.replace("baptised", "baptized").replace("a labour", "a labor")


def test_titles_cited_on_the_site_are_left_alone():
    for line in (
        "Munro-Hay, Aksum: An African Civilisation of Late Antiquity (1991)",
        "Foundations of an African Civilisation: Aksum and the Northern Horn",
        "Carey&#039;s Enquiry (1792)",
        "An Enquiry into the Obligations of Christians to Use Means",
        "Le Theatre sacre des Cevennes (London, 1707)",
        "the Hutterian Brethren, Plough, Rifton, 1987",
    ):
        assert words(line) == [], line
    assert words("a plough and a theatre") == [("plough", "plow"), ("theatre", "theater")]


def test_a_generated_report_is_exempt():
    assert cs.is_exempt("cic-website/data/corpus-coverage.json")
    assert not cs.is_exempt("cic-website/data/world-census.json")


def test_surface_records_under_build_worlds_are_records_and_enforced():
    assert cs.in_checked("Build/worlds/lpc/surface/world_front/x.md")
    assert cs.is_enforced("Build/worlds/lpc/surface/world_front/x.md")
    assert not cs.in_checked("Build/worlds/lpc/Doc_01_World_Identification.md")
    assert cs._kind(cs.REPO / "Build/worlds/lpc/surface/world_front/x.md") == "record"


def html_words(page):
    return [f.word for f in cs.scan_html(page, "x.html")]


def test_html_entity_quotation_marks_open_a_quotation():
    page = "<p>He wrote &quot;by the judgment of God and the favour of the people.&quot; His favour grew.</p>"
    assert html_words(page) == ["favour"]
    assert cs.fix_html(page).count("favor") == 1 and "the favour of the people" in cs.fix_html(page)


def test_hyphen_compounds_count_in_site_prose_but_not_in_slugs():
    assert html_words("<p>a scripture-centred view and hat-honour</p>") == ["centred", "honour"]
    assert html_words('<a href="/tree/the-centre-of-it">go</a>') == []
    assert sorted(f.word for f in cs.scan_json('{"why": "re-baptised and child-labour"}')) == ["baptised", "labour"]
    assert words("see arch-drawn-from-the-centre") == []


def test_attribute_text_a_reader_meets_is_scanned():
    page = '<img src="a.png" alt="a grey portrait" class="grey"><a title="the centre" href="x">y</a>'
    assert html_words(page) == ["grey", "centre"]
    assert cs.fix_html(page) == '<img src="a.png" alt="a gray portrait" class="grey"><a title="the center" href="x">y</a>'


def test_party_and_organisation_names_are_left_alone():
    for line in (
        "The Labour Party had won government",
        "the church's people voted Labour, and Labour carried Maori grievances",
        "stood as Labour candidates",
        "before the new Labour prime minister: a potato",
        "the Labour leader whose 1936 meeting",
        "the Friendly Society of Agricultural Labourers",
        "the Church of the Saviour at Berestove",
        "the All Saviour's monastery",
    ):
        assert words(line) == [], line
    assert words("Our Saviour came. Hard labour.") == [("Saviour", "Savior"), ("labour", "labor")]


def test_forms_found_by_the_site_recheck_are_flagged():
    for old, new in (
        ("outmanoeuvred", "outmaneuvered"), ("arbours", "arbors"), ("amphitheatre", "amphitheater"),
        ("ploughman", "plowman"), ("metred", "metered"), ("enquirers", "inquirers"),
    ):
        assert words(f"a {old} thing") == [(old, new)], old
    assert words("Bedford gaol") == []


def test_json_verbatim_quote_field_is_skipped():
    import json
    doc = {"edges": [{"note": "Zwingli travelled to Marburg.",
                      "sources": [{"work": "x", "quote": "nor would they re-baptise the Faithful"}]}]}
    text = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    assert sorted(f.word for f in cs.scan_json(text, "x.json")) == ["travelled"]
    fixed = json.loads(cs.fix_json(text))
    assert fixed["edges"][0]["sources"][0]["quote"] == "nor would they re-baptise the Faithful"
    assert fixed["edges"][0]["note"] == "Zwingli traveled to Marburg."


def test_html_single_quoted_title_written_with_entities_is_skipped():
    page = "<p>Mills, &#039;The naturalisation of Andean Christianities&#039; and the colour of it.</p>\n"
    assert [f.word for f in cs.scan_html(page, "x.html")] == ["colour"]
    assert "naturalisation" in cs.fix_html(page)
