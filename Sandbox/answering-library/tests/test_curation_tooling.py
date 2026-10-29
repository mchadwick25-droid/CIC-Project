import pytest
import yaml

from answering_library import curation as cu


def make(tmp_path, **doc):
    doc = {"file": "x.txt", "scheme": "s", "curator": "t", "status": "drafted",
           "evidence": [{"line": 1, "quote": "x"}], **doc}
    path = tmp_path / "x.yaml"
    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return cu.load(path)


def loci(res):
    return [d.locus for d in res.divisions]


def origins(res):
    return [d.origin for d in res.divisions]


SERMO = {"id": "s", "pattern": r"^SERMO (?P<n>\S+)$", "locus": "sermo{n|int}", "number": "n"}


def test_fix_values_skip_the_ocr_map(tmp_path):
    rule = dict(SERMO, ocr_map={"1": "I", "l": "I"}, fixes=[{"line": 3, "set": {"n": "17"}}])
    res = cu.resolve(make(tmp_path, rules=[rule]), ["SERMO 1", "text", "SERMO 1l", "more"])
    assert loci(res) == ["sermo1", "sermo17"]
    assert res.sequences["s"] == [(1, 1), (3, 17)]
    assert not [p for p in res.problems if not p.startswith("evidence")]


@pytest.mark.parametrize("order", [0, 1])
def test_adjacent_apparatus_ranges_cover_in_any_order(tmp_path, order):
    ranges = [{"lines": [1, 3], "kind": "front", "locus": "front"}, {"lines": [4, 6], "kind": "notes", "locus": "notes"}]
    cur = make(tmp_path, rules=[SERMO], apparatus=ranges[::-1] if order else ranges)
    lines = ["a b", "c d", "e f", "g h", "i j", "k l", "SERMO 1", "body words here"]
    res = cu.resolve(cur, lines)
    assert loci(res) == ["front", "notes", "sermo1"]
    assert origins(res) == ["apparatus", "apparatus", "marker"]
    assert cu.measure(res)["covered_word_share"] == 1.0


def test_a_quoted_fix_targets_a_line_the_pattern_misses(tmp_path):
    rule = {"id": "c", "pattern": r"^(?P<n>[IVX]+)\. ", "locus": "c{n|int}", "number": "n",
            "fixes": [{"line": 3, "quote": "IL II se plaint", "set": {"n": "II"}}]}
    res = cu.resolve(make(tmp_path, rules=[rule]), ["I. first", "text", "IL II se plaint", "text", "III. third"])
    assert loci(res) == ["c1", "c2", "c3"]
    assert not [p for p in res.problems if not p.startswith("evidence")]


def test_a_quoted_fix_must_quote_its_line_and_unquoted_fixes_still_need_a_match(tmp_path):
    rule = {"id": "c", "pattern": r"^(?P<n>[IVX]+)\. ", "locus": "c{n|int}",
            "fixes": [{"line": 3, "quote": "not there", "set": {"n": "II"}},
                      {"line": 4, "set": {"n": "III"}}]}
    res = cu.resolve(make(tmp_path, rules=[rule]), ["I. first", "text", "IL II se plaint", "text"])
    assert any("quotes text that is not on the line" in p for p in res.problems)
    assert any("fix at line 4" in p and "does not land on a match" in p for p in res.problems)


def test_ignore_pattern_hiding_a_rule_match_is_reported(tmp_path):
    cur = make(tmp_path, rules=[SERMO], ignore=[r"^SERMO 2$"])
    res = cu.resolve(cur, ["SERMO 1", "text", "SERMO 2", "text", "SERMO 3"])
    assert loci(res) == ["sermo1", "sermo3"]
    assert any("'^SERMO 2$'" in n and "rule 's' also matches: 3" in n for n in res.notes)


def test_context_rule_notes(tmp_path):
    book = {"id": "book", "pattern": r"^BOOK (?P<b>\d)$", "locus": "book{b}", "division": False}
    chap = {"id": "ch", "parent": "book", "pattern": r"^CH (?P<c>\d)$", "locus": "ch{c}"}
    lines = ["BOOK 1", "CH 1", "text", "BOOK 1", "stray words here", "CH 2", "text"]
    res = cu.resolve(make(tmp_path, rules=[book, chap]), lines)
    assert any("matched again with an unchanged address at lines 4" in n for n in res.notes)
    assert any("3 words between it and the division heading at line 6" in n for n in res.notes)


def test_rule_context_conditions(tmp_path):
    lines = ["intro", "", "ALPHA", "", "text", "ALPHA", "text", "", "a b c d e f g", "ALPHA", "x"]
    rule = {"id": "h", "pattern": r"^ALPHA$", "locus": "h{line}", "context": {"prev_blank": True, "next_blank": True}}
    assert loci(cu.resolve(make(tmp_path, rules=[rule]), lines))[-1:] == ["h3"]
    rule["context"] = {"prev_blank": False}
    assert [d.locus for d in cu.resolve(make(tmp_path, rules=[rule]), lines).divisions if d.locus.startswith("h")] \
        == ["h6", "h10"]
    rule["context"] = {"prev_short": {"lines": 1, "words": 3}}
    got = [d.locus for d in cu.resolve(make(tmp_path, rules=[rule]), lines).divisions if d.locus.startswith("h")]
    assert got == ["h3", "h6"]


def test_context_condition_must_name_something(tmp_path):
    rule = {"id": "h", "pattern": "^A$", "locus": "h", "context": {}}
    with pytest.raises(cu.CurationError, match="context"):
        make(tmp_path, rules=[rule])


def page_text(pages=6, words=1200):
    out = ["START", "intro words"]
    for p in range(10, 10 + pages):
        out += [f"{p} RUNNING HEAD", " ".join(["word"] * words)]
    return out


def test_page_split_gives_page_addresses_and_counts_the_numbers(tmp_path):
    lines = page_text()
    cur = make(tmp_path, divisions=[{"start_line": 1, "locus": "work"}],
               page_splits=[{"pattern": r"^(?P<p>\d+) RUNNING HEAD$", "number": "p"}], ignore=[r"RUNNING HEAD$"])
    res = cu.resolve(cur, lines)
    assert loci(res) == ["work", "p10", "p11", "p12", "p13", "p14", "p15"]
    assert cu.sequence_notes(res)["page_splits[0]"]["gaps"] == []
    assert all(d.words <= 1200 + 3 for d in res.divisions)
    assert any("6 page heads start new divisions" in n for n in res.notes)
    assert cu.measure(res)["oversize_divisions"] == []


def test_page_split_reports_when_it_divides_more_than_the_oversize(tmp_path):
    lines = ["START", " ".join(["w"] * 6000)] + page_text(pages=3, words=100)[2:]
    lines.append("SMALL")
    cur = make(tmp_path, divisions=[{"start_line": 1, "locus": "big"}],
               page_splits=[{"pattern": r"^(?P<p>\d+) RUNNING HEAD$", "number": "p", "locus": "{enclosing}/p{p}"}])
    res = cu.resolve(cur, lines)
    assert loci(res)[:2] == ["big", "big/p10"]
    only = make(tmp_path, divisions=[{"start_line": 1, "locus": "big"}, {"start_line": 5, "locus": "small"}],
                page_splits=[{"pattern": r"^(?P<p>\d+) RUNNING HEAD$", "number": "p", "only_oversize": True}])
    assert "small" in loci(cu.resolve(only, lines))


def test_page_split_with_no_match_is_a_problem(tmp_path):
    cur = make(tmp_path, divisions=[{"start_line": 1, "locus": "w"}],
               page_splits=[{"pattern": r"^(?P<p>\d+) NOPE$", "number": "p"}])
    assert any("page split 1 matched no line" in p for p in cu.resolve(cur, ["a b", "c d"]).problems)


def test_explicit_divisions_carry_parent_context_and_numbers(tmp_path):
    book = {"id": "book", "pattern": r"^BOOK (?P<b>\d)$", "locus": "book{b}", "division": False}
    chap = {"id": "ch", "parent": "book", "pattern": r"^CH (?P<c>\d)$", "locus": "ch{c}"}
    lines = ["BOOK 1", "CH 1", "text", "Letter without marker", "CH 1", "more", "BOOK 2", "Next letter", "CH 1", "z"]
    divisions = [{"start_line": 4, "locus": "letter1", "parent": "book", "id": "letter", "number": 1, "series": None},
                 {"start_line": 8, "locus": "letter2", "parent": "book", "id": "letter", "number": "II", "takes_context": True}]
    divisions = [{k: v for k, v in d.items() if v is not None} for d in divisions]
    chap2 = dict(chap, id="lch", parent="letter", pattern=r"^CH (?P<c>\d)$", lines=[[5, 5], [9, 9]])
    chap["lines"] = [[2, 2]]
    res = cu.resolve(make(tmp_path, rules=[book, chap, chap2], divisions=divisions), lines)
    assert loci(res) == ["book1/ch1", "book1/letter1", "book1/letter1/ch1", "book2/letter2", "book2/letter2/ch1"]
    assert res.sequences["divisions"] == [(4, 1), (8, 2)]


def test_explicit_division_joins_a_rule_series_and_takes_context_on_request(tmp_path):
    book = {"id": "book", "pattern": r"^BOOK (?P<b>\d)$", "locus": "book{b}", "division": False, "number": "b"}
    lines = ["BOOK 1", "heading without marker", "text", "BOOK 3", "x"]
    plain = [{"start_line": 2, "locus": "u1", "parent": "book", "number": 2, "series": "book"}]
    res = cu.resolve(make(tmp_path, rules=[book], divisions=plain), lines)
    assert res.sequences["book"] == [(1, 1), (2, 2), (4, 3)]
    assert cu.sequence_notes(res)["book"]["gaps"] == []
    assert res.divisions[0].locus == "text/line1"
    taking = [dict(plain[0], takes_context=True)]
    res = cu.resolve(make(tmp_path, rules=[book], divisions=taking), lines)
    assert res.divisions[0].locus == "book1/u1" and res.divisions[0].start == 0


@pytest.mark.parametrize("change,message", [
    ({"parent": "nope"}, "not a rule or division id"),
    ({"series": "book"}, "series needs a number"),
    ({"number": "???"}, "cannot be read"),
    ({"number": 1, "series": "nope"}, "not a rule with a number group"),
])
def test_explicit_division_fields_are_validated(tmp_path, change, message):
    book = {"id": "book", "pattern": r"^BOOK$", "locus": "book"}
    with pytest.raises(cu.CurationError, match=message):
        make(tmp_path, rules=[book], divisions=[dict({"start_line": 1, "locus": "u"}, **change)])


def test_language_guard_separates_parallel_text(tmp_path):
    latin = {"id": "lat", "pattern": r"^(?:CAPUT|ΚΕΦΑΛΑΙΟΝ) (?P<n>\S+)$", "locus": "lat{n|int}", "language": "lat"}
    greek = {"id": "grc", "pattern": r"^(?:CAPUT|ΚΕΦΑΛΑΙΟΝ) (?P<n>\S+)$", "locus": "grc{n|int}", "language": ["grc"]}
    lines = ["CAPUT 1", "text", "ΚΕΦΑΛΑΙΟΝ 1", "text", "CAPUT 2", "text"]
    res = cu.resolve(make(tmp_path, rules=[latin, greek]), lines, ["lat", "grc"])
    assert loci(res) == ["lat1", "grc1", "lat2"]
    with pytest.raises(cu.CurationError, match="language must name"):
        make(tmp_path, rules=[dict(latin, language="klingon")])
