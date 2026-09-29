from engine.m10.quotes import TextStore, check_quotes, extract_quotations, paragraphs

from .fixture_world import CODE, QUOTE, SLUG, TEXT_FILE, build_world, write


def _doc(root, body):
    return write(root, f"Build/worlds/{CODE}/Doc_01_World_Identification.md", body)


def _run(root, body, **kw):
    return check_quotes(CODE, [_doc(root, body)], root, slug=SLUG, **kw)


def test_extracts_straight_curly_and_blockquote_spans_of_five_words_or_more():
    text = 'He wrote "one two three four five" and “alpha beta gamma delta epsilon” and "too short".\n\n> "quoted line one two three four"\n'
    spans = [s for p in paragraphs(text) for s in extract_quotations(p)[0]]
    assert spans == ["one two three four five", "alpha beta gamma delta epsilon", "quoted line one two three four"]


def test_emphasis_marks_inside_a_quotation_are_not_text():
    assert extract_quotations('"one **two** three four five"')[0] == ["one two three four five"]


def test_unbalanced_marks_are_reported_not_skipped_silently(tmp_path):
    root = build_world(tmp_path)
    findings, _ = _run(root, 'A stray " mark and "one two three four five" here.\n')
    assert [f.check for f in findings] == ["quotes-unbalanced"]


def test_verbatim_quotation_passes_with_case_and_punctuation_differences(tmp_path):
    root = build_world(tmp_path)
    findings, notes = _run(root, f'See `cic/texts/{TEXT_FILE}`: "{QUOTE.capitalize()}."\n')
    assert findings == [] and "1 quotation" in notes[0]


def test_altered_quotation_fails(tmp_path):
    root = build_world(tmp_path)
    altered = QUOTE.replace("gathered", "summoned")
    findings, _ = _run(root, f'See `cic/texts/{TEXT_FILE}`: "{altered}"\n')
    assert [f.check for f in findings] == ["quotes-unverified"]


def test_quotation_is_found_in_the_worlds_bucket_files_when_no_file_is_cited(tmp_path):
    root = build_world(tmp_path)
    findings, _ = _run(root, f'The letter says "{QUOTE}".\n')
    assert findings == []


def test_file_can_be_cited_by_volume_prefix(tmp_path):
    root = build_world(tmp_path)
    (root / f"cic/corpus-map/{SLUG}.yaml").unlink()
    findings, _ = _run(root, f'In fxvol01 the letter says "{QUOTE}".\n')
    assert findings == []


def test_quotation_of_a_project_document_is_exempt_and_always_reported(tmp_path):
    root = build_world(tmp_path)
    body = 'The dossier asks "whether the northern collection belongs to a sibling world" openly.\n'
    findings, notes = _run(root, body)
    assert findings == []
    assert any("project document" in n for n in notes)


def test_ellipsis_quotation_verifies_each_segment_in_order(tmp_path):
    root = build_world(tmp_path)
    ok, _ = _run(root, 'It says "the bishop gathered his monks ... read them the whole letter aloud".\n')
    bad, _ = _run(root, 'It says "read them the whole letter aloud ... the bishop gathered his monks".\n')
    assert ok == [] and [f.check for f in bad] == ["quotes-unverified"]


def test_mixed_voice_file_needs_the_speaker_named(tmp_path):
    root = build_world(tmp_path)
    write(
        root,
        f"cic/corpus-map/{SLUG}.yaml",
        f"atlas_id: {SLUG}\nworks:\n- work: Test Volume Letters\n  author: test_author\n  role: context\n  confidence: assigned\n  voice_of: rival_party\n  source_file: {TEXT_FILE}\n",
    )
    unnamed, _ = _run(root, f'The text says "{QUOTE}".\n')
    named, _ = _run(root, f'The rival party says "{QUOTE}".\n')
    assert [f.check for f in unnamed] == ["quotes-speaker"] and named == []


def test_screen_never_accepts_what_the_matcher_rejects(tmp_path):
    write(tmp_path, "cic/texts/a_x.txt", "Rights: Public domain\n\nalpha beta gamma delta epsilon zeta eta theta\n")
    store = TextStore(tmp_path / "cic/texts")
    assert store.may_contain("alpha beta gamma delta epsilon zeta", "a_x.txt")
    assert store.verify("alpha beta gamma delta epsilon zeta", "a_x.txt").verified
    result = store.verify("alpha beta gamma theta eta epsilon", "a_x.txt")
    assert result is None or not result.verified


INVENTED = "the presbyters of the northern hills burned every copy of the letter in the square"


def test_an_invented_quotation_repeated_in_a_second_step_document_is_not_exempt(tmp_path):
    root = build_world(tmp_path)
    body = f'They record that "{INVENTED}" without a source.\n'
    doc1 = _doc(root, body)
    doc2 = write(root, f"Build/worlds/{CODE}/Doc_02_Source_Ecology.md", body)
    findings, _ = check_quotes(CODE, [doc1, doc2], root, slug=SLUG)
    assert [f.check for f in findings] == ["quotes-unverified", "quotes-unverified"]


def test_an_invented_quotation_copied_into_the_source_registry_or_the_dossier_is_not_exempt(tmp_path):
    root = build_world(tmp_path)
    write(root, f"Build/worlds/{CODE}/Source_Registry.md", f'# Source Registry\n\nNote: "{INVENTED}".\n')
    write(root, f"Build/worlds/_cross-world/dossiers/{SLUG}_Source_Readiness_Dossier.md", f'# Dossier\n\n"{INVENTED}".\n')
    findings, _ = _run(root, f'They record that "{INVENTED}".\n')
    assert [f.check for f in findings] == ["quotes-unverified"]


LETTERS = "fxvol02_letters.xml"
FIRST = "the bishop gathered his monks at dawn and read them the whole letter aloud"
SECOND = "the abbot sent the brothers away before the winter came down on the road"


def _letters_world(tmp_path):
    root = build_world(tmp_path)
    write(root, f"cic/texts/{LETTERS}", f'<div1 id="i" title="Letter I"><p>{FIRST}.</p></div1>\n<div1 id="ii" title="Letter II"><p>{SECOND}.</p><div2 id="ii.a" title="Letter II, part a"><p>a later paragraph here.</p></div2></div1>\n')
    write(root, "cic/texts/REGISTRY.yaml", f"- filename: {TEXT_FILE}\n  supplied_by: Mark\n  date_added: '2026-09-01'\n- filename: {LETTERS}\n  supplied_by: Mark\n  date_added: '2026-09-01'\n")
    return root


def _cite(root, locus, quote=SECOND):
    return _run(root, f'The letter at `cic:{LETTERS}:{locus}` says "{quote}".\n')


def test_a_quotation_inside_the_division_its_address_names_is_confirmed(tmp_path):
    root = _letters_world(tmp_path)
    findings, notes = _cite(root, "ii")
    assert findings == [] and "1 confirmed inside a cited" in notes[1]


def test_a_division_holds_the_text_of_its_children(tmp_path):
    root = _letters_world(tmp_path)
    assert _cite(root, "ii", quote="a later paragraph here")[0] == []
    assert _cite(root, "ii.a", quote="a later paragraph here")[0] == []
    assert [f.check for f in _cite(root, "ii.a")[0]] == ["quotes-locus"]


def test_a_quotation_found_in_the_file_but_outside_the_cited_division_fails(tmp_path):
    root = _letters_world(tmp_path)
    findings, _ = _cite(root, "i")
    assert [f.check for f in findings] == ["quotes-locus"]


def test_an_address_naming_no_division_of_the_file_fails(tmp_path):
    root = _letters_world(tmp_path)
    findings, _ = _cite(root, "iii")
    assert [f.check for f in findings] == ["quotes-locus-unknown"]


def test_a_quotation_with_no_address_cited_is_counted_not_failed(tmp_path):
    root = _letters_world(tmp_path)
    findings, notes = _run(root, f'See `cic/texts/{LETTERS}`: "{SECOND}"\n')
    assert findings == [] and "1 found in a file with no address" in notes[1]
