import json
from types import SimpleNamespace

import pytest
import yaml

from answering_library import curate, segment
from answering_library import curation as cu
from answering_library.textio import Source

CONTRACT_FIELDS = [
    "passage_id", "file", "division_locus", "division_title", "ordinal", "text", "word_count", "language",
    "script", "apparatus", "speaker", "ocr_score", "byte_start", "byte_end", "row_ids", "worlds",
]
NAME = "sermons_eng_1900.txt"


def prose(tag, sentences=30):
    return " ".join(f"Sentence {i} of {tag} speaks of the grain and the harvest in the valley." for i in range(sentences))


def book_text():
    parts = ["TITLE PAGE AND PREFACE", "", prose("the preface", 5), ""]
    for book in ("I", "II"):
        parts += [f"BOOK {book}", ""]
        for ch in (1, 2, 3):
            parts += [f"Chapter {ch}", "", f"On matters of {book} {ch}", "", prose(f"book {book} chapter {ch}"), "",
                      "Running Head of the Edition 12", ""]
    parts += ["INDEX", "", prose("the index", 4), ""]
    return "\n".join(parts)


def entry_in(tmp_path, content=None, name=NAME, authors=("author-one",)):
    path = tmp_path / name
    path.write_bytes((content if content is not None else book_text()).encode("utf-8"))
    return SimpleNamespace(filename=name, path=path, suffix=path.suffix, authors=list(authors),
                           row_ids=["row-a"], worlds=["lpc"], size=path.stat().st_size)


def line_of(content, needle, nth=1):
    hits = [i + 1 for i, ln in enumerate(content.split("\n")) if ln.strip() == needle]
    return hits[nth - 1]


def base_doc(content, **extra):
    doc = {
        "file": NAME,
        "scheme": "Book and chapter, as printed",
        "curator": "test",
        "status": "drafted",
        "rules": [
            {"id": "book", "pattern": r"^BOOK (?P<b>[IVX]+)$", "locus": "book{b|int}", "division": False},
            {"id": "chapter", "parent": "book", "pattern": r"^Chapter (?P<c>\d+)$", "locus": "ch{c}",
             "title": "{next}"},
        ],
        "ignore": [{"pattern": r"^Running Head of the Edition \d+$", "kind": "running-head"}],
        "apparatus": [
            {"lines": [1, line_of(content, "BOOK I") - 1], "kind": "front", "locus": "front"},
            {"lines": [line_of(content, "INDEX"), len(content.split("\n"))], "kind": "index", "locus": "index"},
        ],
        "evidence": [{"line": line_of(content, "BOOK II"), "quote": "BOOK II"},
                     {"line": line_of(content, "Chapter 2"), "quote": "Chapter 2"}],
    }
    doc.update(extra)
    return doc


def write_curation(directory, doc, stem=None):
    directory.mkdir(exist_ok=True)
    path = directory / f"{stem or NAME.rsplit('.', 1)[0]}.yaml"
    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return path


def _load_doc(tmp_path, doc):
    return cu.load(write_curation(tmp_path / "c", doc, stem=doc["file"].rsplit(".", 1)[0]))


@pytest.fixture
def curated(tmp_path, monkeypatch):
    content = book_text()
    entry = entry_in(tmp_path, content)
    directory = tmp_path / "curation"
    monkeypatch.setattr(cu, "CURATION_DIR", directory)
    path = write_curation(directory, base_doc(content))
    return entry, content, directory, path


def test_rules_compose_with_parent_and_titles(curated):
    entry, content, _, _ = curated
    records, summary = segment.segment(entry)
    loci = [r["division_locus"] for r in records if r["ordinal"] == 1 and not r["apparatus"]]
    assert loci == [f"book{b}/ch{c}" for b in (1, 2) for c in (1, 2, 3)]
    titles = {r["division_locus"]: r["division_title"] for r in records if r["ordinal"] == 1}
    assert titles["book1/ch1"] == "On matters of I 1"
    assert summary["class"] == "curated"
    assert summary["evidence"]["not_clean_because"] == []


def test_contract_fields_and_ids_unchanged(curated):
    entry, _, _, _ = curated
    records, _ = segment.segment(entry)
    for r in records:
        assert list(r) == CONTRACT_FIELDS
        assert r["passage_id"].startswith(f"cic:{NAME}:{r['division_locus']}#")
        assert 1 <= r["word_count"] <= 400


def test_parent_heading_text_stays_with_the_next_division(curated):
    entry, content, _, _ = curated
    records, _ = segment.segment(entry)
    first = next(r for r in records if r["division_locus"] == "book2/ch1" and r["ordinal"] == 1)
    assert first["text"].startswith("BOOK II Chapter 1")


def test_furniture_is_declared_not_dropped_and_words_balance(curated):
    entry, content, _, _ = curated
    records, summary = segment.segment(entry)
    assert all("Running Head" not in r["text"] for r in records)
    furniture = summary["furniture"]
    assert furniture["lines"] == 6 and furniture["kinds"] == {"running-head": 6}
    check = summary["evidence"]["completeness"]
    assert check["passage_words"] + check["furniture_words"] == len(content.split()) == check["file_words"]
    assert check["verbatim_mismatch"] == 0
    data = entry.path.read_bytes()
    for r in records:
        assert set(data[r["byte_start"]:r["byte_end"]].decode().split()) >= set(r["text"].split())


def test_apparatus_ranges_flag_front_and_index(curated):
    entry, _, _, _ = curated
    records, _ = segment.segment(entry)
    flagged = {r["division_locus"] for r in records if r["apparatus"]}
    assert flagged == {"front", "index"}


def test_manifest_fields_record_hash_and_status(curated):
    entry, _, _, path = curated
    _, summary = segment.segment(entry)
    info = summary["curation"]
    assert info["sha256"] == cu.load(path).sha256 and info["status"] == "drafted" and info["curator"] == "test"


def test_changing_the_curation_changes_the_hash_and_the_output(curated):
    entry, content, directory, _ = curated
    records_a, summary_a = segment.segment(entry)
    doc = base_doc(content)
    doc["rules"][1]["locus"] = "chapter{c}"
    write_curation(directory, doc)
    records_b, summary_b = segment.segment(entry)
    assert summary_a["curation"]["sha256"] != summary_b["curation"]["sha256"]
    assert records_a[3]["passage_id"] != records_b[3]["passage_id"]


def test_segmenting_twice_gives_identical_output(curated):
    entry, _, _, _ = curated
    a = json.dumps(segment.segment(entry), sort_keys=True)
    b = json.dumps(segment.segment(entry), sort_keys=True)
    assert a == b


def test_needs_redo_curation_is_not_applied(curated):
    entry, content, directory, _ = curated
    write_curation(directory, base_doc(content, status="needs-redo"))
    _, summary = segment.segment(entry)
    assert "curation" not in summary
    assert summary["class"] != "curated"


def test_heuristic_is_used_when_no_curation_exists(tmp_path, monkeypatch):
    monkeypatch.setattr(cu, "CURATION_DIR", tmp_path / "none")
    _, summary = segment.segment(entry_in(tmp_path))
    assert "curation" not in summary and summary["class"] in ("clean", "partial", "none")


def test_repeated_addresses_fail_the_class_but_stay_unique_in_ids(tmp_path, monkeypatch):
    content = book_text()
    entry = entry_in(tmp_path, content)
    directory = tmp_path / "curation"
    monkeypatch.setattr(cu, "CURATION_DIR", directory)
    doc = base_doc(content)
    del doc["rules"][0]["division"]
    doc["rules"][1].pop("parent")
    doc["rules"][1]["locus"] = "ch{c}"
    write_curation(directory, doc)
    records, summary = segment.segment(entry)
    assert summary["class"] == "partial"
    assert any("addresses repeat" in r for r in summary["evidence"]["not_clean_because"])
    ids = [r["passage_id"] for r in records]
    assert len(ids) == len(set(ids))


def test_skip_repeat_ocr_numerals_and_fixes(tmp_path):
    text = "\n".join([
        "SERMO I.", "", "alpha beta gamma", "", "SERMO I.", "", "delta epsilon", "", "SERMO Il.", "", "zeta eta",
        "SERMO 111.", "theta", "SERMO XXX.", "iota kappa"])
    doc = {
        "file": "x.txt", "scheme": "Sermon numbers", "curator": "t", "status": "drafted",
        "rules": [{"id": "s", "pattern": r"^SERMO (?P<n>\S+?)\.$", "locus": "sermo{n|int}", "skip_repeat": True,
                   "number": "n", "ocr_map": {"l": "I", "1": "I"},
                   "fixes": [{"line": 14, "set": {"n": "IV"}}]}],
        "evidence": [{"line": 1, "quote": "SERMO I."}],
    }
    cur = _load_doc(tmp_path, doc)
    res = cu.resolve(cur, text.split("\n"))
    assert [d.locus for d in res.divisions] == ["sermo1", "sermo2", "sermo3", "sermo4"]
    assert res.skipped_repeats == {"s": 1}
    assert res.problems == []
    notes = cu.sequence_notes(res)["s"]
    assert notes["readings"] == 4 and notes["gaps"] == [] and notes["backward"] == []


def test_unreadable_numeral_is_an_error_for_the_locus(tmp_path):
    doc = {"file": "x.txt", "scheme": "s", "curator": "t", "status": "drafted",
           "rules": [{"id": "s", "pattern": r"^SERMO (?P<n>\S+)$", "locus": "sermo{n|int}"}],
           "evidence": [{"line": 1, "quote": "SERMO"}]}
    cur = _load_doc(tmp_path, doc)
    with pytest.raises(cu.CurationError, match="cannot read"):
        cu.resolve(cur, ["SERMO ???", "text"])


def test_a_fix_that_misses_a_match_is_a_problem(tmp_path):
    doc = {"file": "x.txt", "scheme": "s", "curator": "t", "status": "drafted",
           "rules": [{"id": "s", "pattern": r"^SERMO (?P<n>\d+)$", "locus": "sermo{n}",
                      "fixes": [{"line": 3, "set": {"n": "9"}}]}],
           "evidence": [{"line": 1, "quote": "SERMO 1"}]}
    res = cu.resolve(_load_doc(tmp_path, doc), ["SERMO 1", "text", "more", "SERMO 2", "text"])
    assert any("fix at line 3" in p for p in res.problems)


def test_explicit_divisions_replace_rules(tmp_path, monkeypatch):
    content = "\n".join(["alpha " * 40, "", "beta " * 40, "", "gamma " * 40])
    entry = entry_in(tmp_path, content)
    directory = tmp_path / "curation"
    monkeypatch.setattr(cu, "CURATION_DIR", directory)
    doc = {"file": NAME, "scheme": "No numbering printed: heading text plus line", "curator": "t",
           "status": "drafted",
           "divisions": [{"start_line": 1, "locus": "alpha@1", "title": "Alpha"},
                         {"start_line": 3, "locus": "beta@3", "title": "Beta"},
                         {"start_line": 5, "locus": "gamma@5", "title": "Gamma"}],
           "evidence": [{"line": 3, "quote": "beta beta"}]}
    write_curation(directory, doc)
    records, summary = segment.segment(entry)
    assert [r["division_locus"] for r in records] == ["alpha@1", "beta@3", "gamma@5"]
    assert summary["class"] == "curated"


def test_text_outside_divisions_lowers_coverage(tmp_path, monkeypatch):
    content = "\n".join(["lead " * 400, "", "BOOK", "body " * 100])
    entry = entry_in(tmp_path, content)
    directory = tmp_path / "curation"
    monkeypatch.setattr(cu, "CURATION_DIR", directory)
    doc = {"file": NAME, "scheme": "s", "curator": "t", "status": "drafted",
           "rules": [{"id": "b", "pattern": "^BOOK$", "locus": "book"}],
           "evidence": [{"line": 3, "quote": "BOOK"}]}
    write_curation(directory, doc)
    _, summary = segment.segment(entry)
    assert summary["class"] == "none"
    assert any("cover" in r for r in summary["evidence"]["not_clean_because"])


def test_oversize_needs_a_justification(tmp_path, monkeypatch):
    content = "\n".join(["HEAD", " ".join(["word"] * 5200), "HEAD", "short text here"])
    entry = entry_in(tmp_path, content)
    directory = tmp_path / "curation"
    monkeypatch.setattr(cu, "CURATION_DIR", directory)
    doc = {"file": NAME, "scheme": "s", "curator": "t", "status": "drafted",
           "rules": [{"id": "h", "pattern": "^HEAD$", "locus": "head{line}"}],
           "evidence": [{"line": 1, "quote": "HEAD"}]}
    write_curation(directory, doc)
    assert segment.segment(entry)[1]["class"] == "partial"
    doc["rules"][0]["allow_oversize"] = "one undivided work; no printed sections"
    write_curation(directory, doc)
    assert segment.segment(entry)[1]["class"] == "curated"


def test_evidence_that_does_not_quote_the_file_blocks_curated(curated):
    entry, content, directory, _ = curated
    doc = base_doc(content)
    doc["evidence"] = [{"line": 1, "quote": "A heading the edition never printed"}]
    write_curation(directory, doc)
    _, summary = segment.segment(entry)
    assert summary["class"] != "curated"
    assert any("evidence" in r for r in summary["evidence"]["not_clean_because"])


def test_language_and_speaker_overrides_apply_to_their_lines(tmp_path, monkeypatch):
    content = book_text()
    entry = entry_in(tmp_path, content)
    directory = tmp_path / "curation"
    monkeypatch.setattr(cu, "CURATION_DIR", directory)
    ch = line_of(content, "Chapter 2", 2)
    doc = base_doc(content,
                   languages=[{"lines": [ch, ch + 5], "language": "lat", "evidence": "quoted in Latin at these lines"}],
                   speakers=[{"lines": [ch, ch + 5], "state": "known", "voice": "author-one",
                              "evidence": "the edition prints the author's name at the head of the chapter"}])
    write_curation(directory, doc)
    records, _ = segment.segment(entry)
    hit = next(r for r in records if r["division_locus"] == "book2/ch2" and r["ordinal"] == 1)
    other = next(r for r in records if r["division_locus"] == "book1/ch1" and r["ordinal"] == 1)
    assert hit["language"] == "lat" and other["language"] == "eng"
    assert hit["speaker"] == {"state": "known", "voice": "author-one"}


def test_speaker_voice_must_be_an_author_of_the_file(tmp_path, monkeypatch):
    content = book_text()
    entry = entry_in(tmp_path, content)
    directory = tmp_path / "curation"
    monkeypatch.setattr(cu, "CURATION_DIR", directory)
    doc = base_doc(content, speakers=[{"lines": [1, 5], "state": "known", "voice": "someone-else", "evidence": "x"}])
    write_curation(directory, doc)
    with pytest.raises(cu.CurationError, match="not an author"):
        segment.segment(entry)


@pytest.mark.parametrize("change,message", [
    (lambda d: d.pop("scheme"), "'scheme' is required"),
    (lambda d: d.update(status="finished"), "status must be one of"),
    (lambda d: d.update(bogus=1), "unknown field"),
    (lambda d: d["rules"][0].update(pattern="("), "bad pattern"),
    (lambda d: d["rules"][1].update(parent="missing"), "not a rule id"),
    (lambda d: d["rules"][1].update(locus="ch{nope}"), "not a group of the pattern"),
    (lambda d: d["rules"][1].update(id="book"), "duplicate rule id"),
    (lambda d: d["rules"][0].update(parent="chapter"), "loop"),
    (lambda d: d.update(evidence=[]), "'evidence' is required"),
    (lambda d: d["apparatus"][0].update(lines=[5, 2]), "first <= last"),
    (lambda d: d.update(file="other.txt"), "does not match"),
])
def test_invalid_curation_files_are_rejected(tmp_path, change, message):
    doc = base_doc(book_text())
    change(doc)
    path = write_curation(tmp_path / "c", doc)
    with pytest.raises(cu.CurationError, match=message):
        cu.load(path)


def test_curation_names_must_match_the_union(tmp_path):
    path = write_curation(tmp_path / "c", base_doc(book_text()))
    assert [c.stem for c in cu.load_all([NAME], tmp_path / "c")] == [path.stem]
    with pytest.raises(cu.CurationError, match="no file"):
        cu.load_all(["different.txt"], tmp_path / "c")


def test_digest_depends_on_every_curation(tmp_path):
    a = cu.load(write_curation(tmp_path / "c", base_doc(book_text())))
    other = base_doc(book_text(), status="sampled-ok")
    b = cu.load(write_curation(tmp_path / "d", other))
    assert cu.digest([a]) != cu.digest([b])
    assert cu.digest([a, b]) == cu.digest([b, a])


def test_curation_refuses_markup_files(tmp_path, monkeypatch):
    xml = "<TEI><text><body><div type='chapter' n='1'><p>one two three</p></div></body></text></TEI>"
    entry = entry_in(tmp_path, xml, name="work_eng_1900.xml")
    doc = base_doc(book_text())
    doc["file"] = "work_eng_1900.xml"
    path = write_curation(tmp_path / "c", doc, stem="work_eng_1900")
    with pytest.raises(cu.CurationError, match="plain-text"):
        segment.segment(entry, curation=cu.load(path))


def test_checker_exit_codes_and_report(curated, monkeypatch, capsys):
    entry, content, directory, _ = curated
    monkeypatch.setattr(curate, "TEXTS_DIR", entry.path.parent)
    assert curate.main(["check", NAME.rsplit(".", 1)[0], "--curation-dir", str(directory)]) == 0
    out = capsys.readouterr().out
    for needle in ("class before:", "class after:  curated", "PASS  address uniqueness", "PASS  coverage",
                   "PASS  oversize", "PASS  word completeness", "PASS  verbatim byte ranges", "sample: 6 divisions",
                   "RESULT: PASS"):
        assert needle in out
    doc = base_doc(content)
    doc["rules"][1]["locus"] = "same"
    doc["rules"][1].pop("parent")
    del doc["rules"][0]["division"]
    write_curation(directory, doc)
    assert curate.main(["check", NAME.rsplit(".", 1)[0], "--curation-dir", str(directory)]) == 1
    assert "FAIL  address uniqueness" in capsys.readouterr().out
    (directory / f"{NAME.rsplit('.', 1)[0]}.yaml").write_text("file: [", encoding="utf-8")
    assert curate.main(["check", NAME.rsplit(".", 1)[0], "--curation-dir", str(directory)]) == 2


def test_sample_helper_picks_evenly_spaced_divisions():
    assert curate.sample_indices(5, 12) == [0, 1, 2, 3, 4]
    assert curate.sample_indices(100, 12) == sorted({round(k * 99 / 11) for k in range(12)})
    assert curate.sample_indices(100, 1) == [0]


def test_sample_writes_a_review_packet(curated, monkeypatch, tmp_path, capsys):
    entry, _, directory, _ = curated
    monkeypatch.setattr(curate, "TEXTS_DIR", entry.path.parent)
    out = tmp_path / "review" / "packet.md"
    code = curate.main(["sample", NAME.rsplit(".", 1)[0], "--n", "3", "--curation-dir", str(directory),
                        "--out", str(out)])
    assert code == 0
    text = out.read_text(encoding="utf-8")
    for needle in ("## Scheme", "## Evidence the scheme is the edition's own", "## Checker", "## Sampled divisions",
                   "### 3.", "book2/ch3", "## Smallest and largest body divisions", "## Apparatus ranges",
                   "## Questions for the reader"):
        assert needle in text
    assert "### 4." not in text


def test_char_of_inverts_byte_of_on_multibyte_text():
    text = ("αβγ δεζ  naïve café — " * 900)
    src = Source(text.encode("utf-8"))
    for char in (0, 1, 5, 4095, 4096, 4097, 9000, len(text)):
        assert src.char_of(src.byte_of(char)) == char
    with pytest.raises(ValueError):
        src.char_of(1)


def test_committed_curations_load_and_their_evidence_holds():
    names = sorted(cu.CURATION_DIR.glob("*.yaml"))
    assert names, "the pilot curations are committed"
    for path in names:
        cur = cu.load(path)
        raw = (curate.TEXTS_DIR / cur.file).read_bytes().decode("utf-8", errors="surrogateescape")
        res = cu.resolve(cur, raw.split("\n"))
        assert cu.failures(cu.measure(res)) == [], path.name
