import json
from types import SimpleNamespace

from answering_library import markers, ocr, passages, segment, speaker
from answering_library.langscript import filename_codes, language_of, script_of
from answering_library.markup import parse
from answering_library.textio import Source

CONTRACT_FIELDS = [
    "passage_id", "file", "division_locus", "division_title", "ordinal", "text", "word_count", "language",
    "script", "apparatus", "speaker", "ocr_score", "byte_start", "byte_end", "row_ids", "worlds",
]


def entry_for(tmp_path, name, content, authors=("author-one",)):
    path = tmp_path / name
    path.write_bytes(content.encode("utf-8"))
    return SimpleNamespace(
        filename=name, path=path, suffix=path.suffix, authors=list(authors),
        row_ids=["row-a", "row-b"], worlds=["lpc"], size=path.stat().st_size,
    )


def english_body(chapter, sentences=40):
    return " ".join(
        f"Sentence {i} of chapter {chapter} speaks of the grain and the harvest in the valley." for i in range(sentences)
    )


def run(entry):
    return segment.segment(entry)


def test_english_chapters_are_clean_and_cut_at_sentences(tmp_path):
    body = "\n\n".join(f"CHAPTER {roman}.\n\n{english_body(n)}" for n, roman in enumerate(["I", "II", "III", "IV"], 1))
    records, summary = run(entry_for(tmp_path, "treatise_eng_1900.txt", body))
    assert summary["class"] == "clean"
    assert [r["division_locus"] for r in records if r["ordinal"] == 1] == [
        "chapter1", "chapter2", "chapter3", "chapter4"]
    for r in records:
        assert list(r) == CONTRACT_FIELDS
        assert 150 <= r["word_count"] <= 400
        assert r["text"].rstrip().endswith(".")
        assert r["script"] == "Latn" and r["language"] == "eng"
    assert records[0]["passage_id"] == "cic:treatise_eng_1900.txt:chapter1#01"


def test_passages_never_cross_a_division(tmp_path):
    body = "\n\n".join(f"CHAPTER {roman}.\n\n{english_body(n, 25)}" for n, roman in enumerate(["I", "II", "III"], 1))
    records, _ = run(entry_for(tmp_path, "treatise_eng_1900.txt", body))
    for r in records:
        assert f"chapter {r['division_locus'][-1]} " in r["text"] or r["text"].count("chapter") >= 1
        others = {str(n) for n in (1, 2, 3)} - {r["division_locus"][-1]}
        assert not any(f"of chapter {o} " in r["text"] for o in others)


def test_byte_range_recovers_the_passage_text(tmp_path):
    content = "CHAPTER I.\n\n" + english_body(1) + "\n\nCHAPTER II.\n\n" + english_body(2) + "\n\nCHAPTER III.\n\n" + english_body(3)
    e = entry_for(tmp_path, "treatise_eng_1900.txt", content)
    records, _ = run(e)
    data = e.path.read_bytes()
    for r in records:
        assert data[r["byte_start"]:r["byte_end"]].decode("utf-8").split() == r["text"].split()


def test_latin_caput_headings(tmp_path):
    body = "\n\n".join(
        f"CAPUT {n}.\n\n" + " ".join(f"Sententia {i} capitis {n} de pane et vino in ecclesia sancta nostra." for i in range(40))
        for n in (1, 2, 3, 4)
    )
    records, summary = run(entry_for(tmp_path, "tractatus-lat_edition1880.txt", body))
    assert summary["class"] == "clean"
    assert {r["language"] for r in records} == {"lat"}
    assert records[0]["division_locus"] == "chapter1"


def test_greek_chapters_and_script(tmp_path):
    sentence = "Ὁ λόγος τοῦ θεοῦ ἐστιν ἀληθής καὶ ἡ πίστις ἡμῶν ἐν τῷ κυρίῳ μένει."
    body = "\n\n".join(f"ΚΕΦΑΛΑΙΟΝ {g}.\n\n" + " ".join([sentence] * 40) for g in ("α'", "β'", "γ'", "δ'"))
    records, summary = run(entry_for(tmp_path, "homiliae-grc_edition1880.txt", body))
    assert summary["class"] == "clean"
    assert {r["script"] for r in records} == {"Grek"}
    assert {r["language"] for r in records} == {"grc"}
    assert [r["division_locus"] for r in records if r["ordinal"] == 1][:2] == ["chapter1", "chapter2"]


def test_no_markers_falls_back_to_paragraph_blocks(tmp_path):
    paragraphs = "\n\n".join(
        " ".join(f"Paragraph {p} sentence {i} tells of the road and the river." for i in range(8)) for p in range(30)
    )
    records, summary = run(entry_for(tmp_path, "plain_eng_1900.txt", paragraphs))
    assert summary["class"] == "none"
    assert all(r["division_locus"].startswith("line") for r in records)
    assert sum(r["word_count"] for r in records) == len(paragraphs.split())


def test_thml_xml_uses_div_ids_and_separates_notes(tmp_path):
    xml = (
        '<ThML><ThML.head><DC.Title>Sample</DC.Title></ThML.head>'
        '<div1 id="i" title="Title Page."><p>Sample volume title.</p></div1>'
        '<div1 id="ii" title="Chapter I."><p>' + english_body(1, 20)
        + '<note><p>Editor remark on the grain.</p></note></p></div1>'
        '<div1 id="iii" title="Chapter II."><p>' + english_body(2, 20) + '</p></div1>'
        '<div1 id="iv" title="Chapter III."><p>' + english_body(3, 20) + '</p></div1></ThML>'
    )
    records, summary = run(entry_for(tmp_path, "vol01_sample.xml", xml))
    assert summary["mode"] == "markup" and summary["class"] == "clean"
    loci = {r["division_locus"] for r in records}
    assert {"i", "ii", "iii", "iv", "ii/notes"} <= loci
    title_page = [r for r in records if r["division_locus"] == "i"]
    assert title_page and all(r["apparatus"] for r in title_page)
    notes = [r for r in records if r["division_locus"] == "ii/notes"]
    assert notes and all(r["apparatus"] for r in notes)
    assert all("Editor remark" not in r["text"] for r in records if r["division_locus"] == "ii")


def test_xml_without_markers_is_none(tmp_path):
    xml = "<doc><p>" + english_body(1, 30) + "</p></doc>"
    _, summary = run(entry_for(tmp_path, "flat.xml", xml))
    assert summary["class"] == "none"


def test_running_heads_and_page_numbers_are_suppressed_not_lost(tmp_path):
    pages = []
    for p in range(12):
        lines = [f"Page {p} line {i} of the story goes on." for i in range(30)]
        pages.append(f"THE LIFE OF SAINT TEST\n\n{p + 40}\n\n" + "\n".join(lines))
    body = "CHAPTER I.\n\n" + "\n\n".join(pages)
    e = entry_for(tmp_path, "life_eng_1900.txt", body)
    records, summary = run(e)
    text = " ".join(r["text"] for r in records)
    assert "THE LIFE OF SAINT TEST" not in text
    assert summary["furniture"]["words"] > 0
    assert sum(r["word_count"] for r in records) + summary["furniture_words"] == len(body.split())


def test_header_block_is_apparatus(tmp_path):
    header = "Title: A Test\nCreator: Someone\nPublisher: Nowhere\nRights: Public Domain\n---\n"
    body = header + "CHAPTER I.\n\n" + english_body(1) + "\n\nCHAPTER II.\n\n" + english_body(2) + "\n\nCHAPTER III.\n\n" + english_body(3)
    records, _ = run(entry_for(tmp_path, "headed_eng_1900.txt", body))
    head = [r for r in records if r["division_locus"] == "header"]
    assert head and all(r["apparatus"] for r in head)


def test_locus_collisions_are_made_unique(tmp_path):
    body = "\n\n".join(f"CHAPTER I.\n\n{english_body(n, 20)}" for n in range(4))
    records, _ = run(entry_for(tmp_path, "twice_eng_1900.txt", body))
    loci = [r["division_locus"] for r in records if r["ordinal"] == 1]
    assert len(loci) == len(set(loci)) == 4


def test_cut_points_respect_bounds():
    flags = [2 if i % 17 == 16 else 0 for i in range(1300)]
    cuts = passages.cut_points(1300, flags)
    sizes = [b - a for a, b in zip([0] + cuts, cuts)]
    assert sum(sizes) == 1300
    assert all(150 <= s <= 400 for s in sizes)
    assert passages.cut_points(120, [0] * 120) == [120]


def test_sentence_strengths_skip_abbreviations():
    words = "See St. Paul and Rom. 5 for this. Then he left.".split()
    flags = passages.strengths(words, "Latn")
    assert flags[words.index("St.")] == 0
    assert flags[words.index("Rom.")] == 0
    assert flags[words.index("this.")] == 2


def test_filename_language_codes_and_script():
    assert filename_codes("origen_homiliae-grc-lat_migne1857.txt") == ["grc", "lat"]
    assert filename_codes("plain_work_smith1900.txt") == []
    assert script_of("λόγος καὶ θεός") == "Grek"
    assert script_of("Слово о законе") == "Cyrl"
    assert language_of("the word and the work of the church", "Latn", []) == "eng"
    assert language_of("et in nomine patris et filii", "Latn", ["grc", "lat"]) == "lat"


def test_ocr_score_orders_clean_above_noisy():
    clean = "The word of God endures forever and the church keeps it faithfully."
    noisy = "Tbe w0rd o£ G~d en|dures f0rev|er an^d tl1e chu^rch k~eeps i| faithf|ully."
    a = ocr.score(ocr.components(clean, "eng", "Latn", None))
    b = ocr.score(ocr.components(noisy, "eng", "Latn", None))
    assert 0.0 <= b < a <= 1.0


def test_speaker_states():
    plain_text = "Therefore the soul turns to the good and rests."
    assert speaker.classify("treatise-lat.txt", ["augustine"], "Chapter 1", plain_text, 120, False) == {
        "state": "known", "voice": "augustine"}
    assert speaker.classify("treatise-lat.txt", ["a", "b"], "Chapter 1", plain_text, 120, False)["state"] == "unknown"
    assert speaker.classify("letters-lat.txt", ["augustine"], "Letter 4", plain_text, 120, False)["state"] == "mixed"
    assert speaker.classify("treatise-lat.txt", ["augustine"], "Preface", plain_text, 120, True)["state"] == "unknown"
    quoted = 'He said “' + "the quoted words of another speaker go here at length " * 4 + '” and then went on.'
    assert speaker.classify("treatise-lat.txt", ["augustine"], "Chapter 1", quoted, 60, False)["state"] == "mixed"


def test_markup_stream_maps_back_to_raw():
    raw = '<div1 id="a" title="T"><p>Alpha &amp; beta<i>gamma</i> delta.</p></div1>'
    doc = parse(raw)
    text = doc.main.text
    start = text.index("Alpha")
    end = text.index("delta.") + len("delta.")
    rs, re_ = doc.main.raw_pos_start(start), doc.main.raw_pos_end(end)
    assert raw[rs] == "A" and raw[re_ - 1] == "."


def test_sequentiality_and_number_values():
    assert markers.number_value("XIV") == 14
    assert markers.number_value("ιβ'") == 12
    assert markers.number_value("Third") == 3
    hs = [markers.Heading(i, "f", n, "x", "x") for i, n in enumerate([1, 2, 3, 5, 1, 2])]
    assert markers.sequentiality(hs) == 1.0


def test_source_byte_offsets_with_multibyte_text():
    s = Source("αβγ δ\nλόγος".encode("utf-8"))
    i = s.text.index("λ")
    assert s.byte_of(i) == len("αβγ δ\n".encode("utf-8"))


def test_records_are_json_serialisable(tmp_path):
    records, _ = run(entry_for(tmp_path, "x_eng_1900.txt", "CHAPTER I.\n\n" + english_body(1) + "\n\nCHAPTER II.\n\n" + english_body(2)))
    for r in records:
        json.dumps(r, ensure_ascii=False)


def test_roman_value_ignores_non_ascii_lookalikes():
    from answering_library import markers

    assert markers.roman_value("ı") is None
    assert markers.roman_value("XIV") == 14
