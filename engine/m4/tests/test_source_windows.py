"""Context windows resolved through the source record's vendored edition,
for loci that name no `cic/texts/<file>, lines N` span."""
from engine.m4 import fit_step, source_windows

NAME = "xyz01_fixture-volume.xml"
SOURCE = {"id": "w.source.vol", "record_type": "source", "edition": f"Fixture volume, vendored as cic/texts/{NAME} (div i)"}


def _fixture(tmp_path):
    filler = [f"<p>filler {n} alpha beta gamma delta</p>" for n in range(1, 41)]
    lines = (
        ['<div1 id="i" title="Book One">']
        + filler[:20]
        + ['<div2 id="i.ii" title="Chapter Two">', "<p>Before the saying there is talk of the harbour.</p>",
           "<p>The <i>light</i> of the city, he said, is the gathered church at prayer;</p>",
           "<p>and no lamp is lit for itself alone.</p>", "<p>After it the talk turns to bread.</p>", "</div2>"]
        + filler[20:]
        + ["</div1>"]
    )
    path = tmp_path / "cic" / "texts" / NAME
    path.parent.mkdir(parents=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return lines


def _record(record_type="quote", locus="Book One, ch. 2 (xyz01)", text="the light of the city, he said, is the gathered church at prayer; and no lamp is lit"):
    return {"id": "w.quote.light", "record_type": record_type, "text": text,
            "sources": [{"source_id": SOURCE["id"], "locus": locus}]}


def test_a_quote_is_found_by_its_words_and_kept_inside_its_division(tmp_path):
    lines = _fixture(tmp_path)
    (block,) = source_windows.context_blocks(_record(), {SOURCE["id"]: SOURCE}, tmp_path)
    first = lines.index("<p>The <i>light</i> of the city, he said, is the gathered church at prayer;</p>") + 1
    assert block["id"] == f"{fit_step.CONTEXT_PREFIX}w.quote.light.1" and block["file"] == f"cic/texts/{NAME}"
    assert block["lines"] == f"{first}-{first + 1}"
    assert "harbour" in block["text"] and "bread" in block["text"]
    assert "filler" not in block["text"] and "<" not in block["text"]


def test_the_locus_lines_anchor_a_story_and_a_division_id_anchors_one_with_no_lines(tmp_path):
    lines = _fixture(tmp_path)
    story = _record("story", locus="ch. 2 (xyz01 line 24)", text="")
    (block,) = source_windows.context_blocks(story, {SOURCE["id"]: SOURCE}, tmp_path)
    assert block["lines"] == "24-24" and "light" in lines[23] and "bread" in block["text"]
    by_div = _record("story", locus="ch. 2 (xyz01 div i.ii)", text="")
    (block,) = source_windows.context_blocks(by_div, {SOURCE["id"]: SOURCE}, tmp_path)
    opening = next(n for n, line in enumerate(lines, start=1) if line.startswith('<div2 id="i.ii"'))
    assert block["lines"] == f"{opening}-{opening}" and "harbour" in block["text"]


def test_an_unresolvable_record_gets_no_window(tmp_path):
    _fixture(tmp_path)
    assert source_windows.context_blocks(_record("story", locus="the whole text", text=""), {SOURCE["id"]: SOURCE}, tmp_path) == []
    assert source_windows.context_blocks(_record(), {}, tmp_path) == []


HISTORY = "xyz02_fixture-history.xml"
HISTORY_SOURCE = {"id": "w.source.hist", "record_type": "source", "author": "Fixturius of Nowhere",
                  "work": "Church History - a fixture", "edition": f"Fixture, vendored as cic/texts/{HISTORY}"}


def _history(tmp_path, chapter_words=300):
    body = " ".join(["word"] * chapter_words)
    lines = ['<div1 title="Preface." id="i">', '<div2 type="Chapter" n="VI" title="Chapter VI.—A preface chapter" id="i.i">',
             "<p>preface six</p>", "</div2>", "</div1>",
             '<div1 title="The Church History of Fixturius." id="ii">']
    for book in ("V", "VI"):
        lines.append(f'<div2 type="Book" n="{book}" title="Book {book}" id="ii.{book.lower()}">')
        for chapter in ("I", "II", "III"):
            if chapter == "I":
                lines.append(f'<div3 type="Chapter" n="I" title="First of book {book}." id="ii.{book.lower()}.i">')
            else:
                lines.append(f'<div3 type="Chapter" title="Untitled." id="ii.{book.lower()}.{chapter.lower()}">')
            lines += [f"<p>Chapter {chapter}.— Book {book} chapter {chapter} opens.</p>", f"<p>{body}</p>", "</div3>"]
        lines.append("</div2>")
    lines.append("</div1>")
    path = tmp_path / "cic" / "texts" / HISTORY
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _story(locus, source=HISTORY_SOURCE):
    return {"id": "w.story.s", "record_type": "story", "sources": [{"source_id": source["id"], "locus": locus}]}


def test_a_book_and_chapter_reference_resolves_inside_the_work_by_n_or_by_the_division_s_own_heading(tmp_path):
    _history(tmp_path)
    records = {HISTORY_SOURCE["id"]: HISTORY_SOURCE}
    (block,) = source_windows.context_blocks(_story("VI.1-2 (the gloss)"), records, tmp_path)
    assert block["text"].startswith("Chapter I.— Book VI chapter I opens.")
    assert block["trimmed"] is True and len(block["text"].split()) == fit_step.CONTEXT_MAX_WORDS
    (block,) = source_windows.context_blocks(_story("VI.3"), records, tmp_path)
    assert block["text"].startswith("Chapter III.— Book VI chapter III opens.") and block["trimmed"] is False


def test_a_number_the_work_does_not_hold_resolves_nothing(tmp_path):
    _history(tmp_path)
    records = {HISTORY_SOURCE["id"]: HISTORY_SOURCE}
    assert source_windows.context_blocks(_story("VI.96-97"), records, tmp_path) == []
    assert source_windows.context_blocks(_story("the year-513 entry"), records, tmp_path) == []


def test_a_chap_heading_inside_a_division_and_a_named_letter_resolve(tmp_path):
    lines = ['<div1 title="Letters" id="v">', '<div2 title="The Epistle to the Magnesians" id="v.i">',
             '<div3 id="v.i.vi" n="vi" title="Chapter VI.—Preserve harmony.">', "<p>Harmony text.</p>", "</div3>", "</div2>",
             '<div2 title="Vision Second." id="v.ii">', "<h5>Chap. I.</h5>", "<p>first part</p>", "<h5>Chap. II.</h5>",
             "<p>second part</p>", "</div2>", "</div1>"]
    path = tmp_path / "cic" / "texts" / NAME
    path.parent.mkdir(parents=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    source = {**SOURCE, "edition": f"vendored as cic/texts/{NAME} (div1 v)"}
    records = {source["id"]: source}
    (block,) = source_windows.context_blocks(_story("Magnesians 6; Smyrnaeans 8", source), records, tmp_path)
    assert block["text"] == "Harmony text." and block["lines"] == "3-5"
    (block,) = source_windows.context_blocks(_story("Vision 2.2.3", source), records, tmp_path)
    assert block["text"] == "Chap. II. second part"


def test_a_plain_text_chapter_heading_skips_the_table_of_contents(tmp_path):
    name = "xyz03_plain.txt"
    lines = ["CHAPTER XL -- EPHRAIM", "CHAPTER XLI -- WOMEN", ""] + ["filler " * 10] * 3 + [
        "CHAPTER XL. -- EPHRAIM", "You must have heard of Ephraim. " + "word " * 80, "CHAPTER XLI -- WOMEN", "other"]
    path = tmp_path / "cic" / "texts" / name
    path.parent.mkdir(parents=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    source = {"id": "w.source.p", "record_type": "source", "edition": f"vendored as cic/texts/{name}"}
    (block,) = source_windows.context_blocks(_story("ch. XL, the chapter", source), {source["id"]: source}, tmp_path)
    assert block["text"].startswith("CHAPTER XL. -- EPHRAIM You must have heard") and "other" not in block["text"]


def test_numbers_read_as_roman_arabic_and_ordinal():
    assert [source_windows.number(t) for t in ("VI", "lviij", "44", "Second", "XXVI", "x1")] == [6, 58, 44, 2, 26, None]
    assert source_windows.pieces("VI.8, VI.23-26 (HIGH-risk)") == [(None, [6, 8], None), (None, [6, 23], 26)]
    assert source_windows.pieces("1:1-2; 2:1-4:14 (gloss)")[0] == (None, [1], None)
    assert source_windows.pieces("Book I, ch. lviij - the opening")[0] == ("Book", [1, 58], None)


def test_a_cited_range_longer_than_the_ceiling_keeps_its_opening_and_is_marked_trimmed(tmp_path):
    long_text = " ".join(f"w{n}" for n in range(600))
    lines = ['<div1 id="i" title="Book One">', "<p>before</p>", f"<p>{long_text[:1500]}</p>", f"<p>{long_text[1500:]}</p>",
             "<p>after</p>", "</div1>"]
    path = tmp_path / "cic" / "texts" / NAME
    path.parent.mkdir(parents=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    (block,) = source_windows.context_blocks(_record(text=long_text), {SOURCE["id"]: SOURCE}, tmp_path)
    assert block["lines"] == "3-4" and block["trimmed"] is True
    assert block["text"].split() == long_text.split()[:fit_step.CONTEXT_MAX_WORDS]
    (short,) = source_windows.context_blocks(_record(), {SOURCE["id"]: SOURCE},
                                             (_fixture(tmp_path / "other"), tmp_path / "other")[1])
    assert short["trimmed"] is False


CLEMENT = "xyz04_fixture-clement.xml"


def _clement(tmp_path):
    def chapters(work, book):
        return [line for n in ("I", "II", "III") for line in (
            f'<div4 type="Chapter" title="Chapter {n}.—{work} book {book} chapter {n}." id="{work}.{book}.{n}">',
            f"<p>{work} book {book} chapter {n} text.</p>", "</div4>")]
    lines = ['<div1 title="CLEMENT OF ALEXANDRIA" id="vi">', '<div2 title="Exhortation to the Heathen" id="vi.ii">']
    lines += [line for n in ("I", "II", "III") for line in (
        f'<div3 type="Chapter" title="Chapter {n}.—Exhortation chapter {n}." id="vi.ii.{n}">',
        f"<p>Exhortation chapter {n} text.</p>", "</div3>")]
    lines.append("</div2>")
    for work, title in (("instructor", "The Instructor"), ("stromata", "The Stromata, or Miscellanies")):
        lines.append(f'<div2 title="{title}" id="vi.{work}">')
        for book in ("I", "II"):
            lines += [f'<div3 type="Book" n="{book}" title="Book {book}" id="vi.{work}.{book}">'] + chapters(work, book) + ["</div3>"]
        lines.append("</div2>")
    lines.append("</div1>")
    path = tmp_path / "cic" / "texts" / CLEMENT
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _clement_source(work):
    return {"id": "w.source.clement", "record_type": "source", "author": "Clement of Alexandria (c. 150-215 CE)",
            "work": work, "edition": f"Fixture, vendored as cic/texts/{CLEMENT}"}


def test_a_latin_or_greek_work_name_resolves_inside_its_english_titled_work(tmp_path):
    _clement(tmp_path)
    for work, locus, opening in (("Paedagogus", "I", "instructor book I chapter I text."),
                                 ("Paedagogus", "II.3", "instructor book II chapter III text."),
                                 ("Stromateis", "II.2", "stromata book II chapter II text."),
                                 ("Stromateis", "II, V", "stromata book II chapter I text.")):
        source = _clement_source(work)
        (block,) = source_windows.context_blocks(_story(locus, source), {source["id"]: source}, tmp_path)
        assert block["text"].startswith(opening), (work, locus, block["text"])
        assert "Exhortation" not in block["text"]


def test_a_work_the_file_does_not_hold_is_not_located_and_says_why(tmp_path):
    _clement(tmp_path)
    source = _clement_source("Excerpta ex Theodoto")
    record = _story("I.1", source)
    assert source_windows.context_blocks(record, {source["id"]: source}, tmp_path) == []
    assert source_windows.source_block(record, record["sources"][0], {source["id"]: source}, tmp_path) == (
        None, source_windows.WORK_NOT_MATCHED)


def test_a_letter_named_with_a_ligature_resolves_inside_that_letter_and_an_absent_letter_does_not(tmp_path):
    lines = ['<div1 title="IGNATIUS" id="v">', '<div2 title="Epistle to the Ephesians: Shorter and Longer Versions" id="v.ii">',
             "<h4>Chap. VIII.</h4>", "<p>Ephesians eight text.</p>", "</div2>",
             '<div2 title="Epistle to the Smyrnæans: Shorter and Longer Versions" id="v.vii">',
             '<div3 type="Chapter" title="Chapter VIII.—Let nothing be done without the bishop." id="v.vii.viii">',
             "<p>Smyrnaeans eight text.</p>", "</div3>", "</div2>", "</div1>"]
    path = tmp_path / "cic" / "texts" / NAME
    path.parent.mkdir(parents=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    source = {**SOURCE, "edition": f"vendored as cic/texts/{NAME} (div1 v)"}
    records = {source["id"]: source}
    (block,) = source_windows.context_blocks(_story("Smyrnaeans 8", source), records, tmp_path)
    assert block["text"] == "Smyrnaeans eight text." and "Smyrnæans" in block["division_path"][1]
    record = _story("Philippians 8", source)
    assert source_windows.source_block(record, record["sources"][0], records, tmp_path) == (None, source_windows.WORK_NOT_MATCHED)


def test_titles_fold_ligatures_accents_case_and_punctuation():
    keys = source_windows.work_names({"work": "Stromateis (Miscellanies), Books I-II"})
    assert source_windows.names_work("The Stromata, or Miscellanies", keys)
    assert not source_windows.names_work("Exhortation to the Heathen", keys)
    assert source_windows.names_work("THE HEXÆMERON.", source_windows.work_names({"work": "The Hexaemeron, Homily II"}))
    assert source_windows.names_work("Origen Against Celsus.", source_windows.work_names({"work": "Contra Celsum"}))
