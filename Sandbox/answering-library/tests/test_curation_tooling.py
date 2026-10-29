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
    res = cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[{"series": "s", "line": 3, "quote": "SERMO 1l"}]),
                     ["SERMO 1", "text", "SERMO 1l", "more"])
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


def unexplained(res):
    return [p for p in res.problems if not p.startswith("evidence")]


def test_unexplained_series_steps_fail_and_expected_gaps_explain_them(tmp_path):
    lines = ["SERMO 1", "t", "SERMO 3", "t", "SERMO 3", "t", "SERMO 2", "t", "SERMO 4"]
    problems = unexplained(cu.resolve(make(tmp_path, rules=[SERMO]), lines))
    assert len(problems) == 1 and "series 's' has 4" in problems[0] and "lines 3, 5, 7, 9" in problems[0]
    gaps = [{"series": "s", "line": n, "quote": q} for n, q in
            [(3, "SERMO 3"), (5, "SERMO 3"), (7, "SERMO 2"), (9, "SERMO 4")]]
    assert unexplained(cu.resolve(make(tmp_path, rules=[SERMO], expected_gaps=gaps), lines)) == []
    wrong = [dict(gaps[0], quote="the edition prints no II")] + gaps[1:]
    assert any("not on the line" in p for p in unexplained(cu.resolve(make(tmp_path, rules=[SERMO], expected_gaps=wrong), lines)))
    extra = gaps + [{"series": "s", "line": 1, "quote": "SERMO 1"}]
    assert any("matches no gap" in p for p in unexplained(cu.resolve(make(tmp_path, rules=[SERMO], expected_gaps=extra), lines)))
    assert any("no rule or entry numbers" in p for p in unexplained(cu.resolve(
        make(tmp_path, rules=[SERMO], expected_gaps=gaps + [{"series": "zz", "line": 1, "quote": "SERMO 1"}]), lines)))


def test_numbers_restart_under_a_new_parent(tmp_path):
    book = {"id": "book", "pattern": r"^BOOK (?P<b>\d)$", "locus": "book{b}", "division": False}
    chap = {"id": "ch", "parent": "book", "pattern": r"^CH (?P<c>\d)$", "locus": "ch{c}", "number": "c"}
    lines = ["BOOK 1", "CH 1", "t", "CH 2", "t", "BOOK 2", "CH 1", "t", "CH 2", "t"]
    assert unexplained(cu.resolve(make(tmp_path, rules=[book, chap]), lines)) == []


def test_series_notes_list_every_step(tmp_path):
    lines = [x for n in range(1, 40, 2) for x in (f"SERMO {n}", "t")]
    notes = cu.sequence_notes(cu.resolve(make(tmp_path, rules=[SERMO]), lines))["s"]
    assert len(notes["gaps"]) == 19


def test_allow_oversize_is_checked_against_the_files_own_sub_headings(tmp_path):
    body = ["HEAD", ""]
    for n in range(1, 13):
        body += [f"CAPUT {n}.", "", " ".join(["word"] * 700), ""]
    rule = {"id": "h", "pattern": "^HEAD$", "locus": "head", "allow_oversize": "one undivided work"}
    problems = unexplained(cu.resolve(make(tmp_path, rules=[rule]), body))
    assert len(problems) == 1 and "does not hold" in problems[0] and '"CAPUT 1."' in problems[0]
    flat = ["HEAD", "", " ".join(["word"] * 5600)]
    assert unexplained(cu.resolve(make(tmp_path, rules=[rule]), flat)) == []


def test_hand_listed_lines_report_headings_the_pattern_missed(tmp_path):
    rule = {"id": "c", "pattern": r"^CAPUT (?P<n>[IVX]+)$", "locus": "c{n|int}", "number": "n", "lines": [[1, 12]]}
    lines = ["CAPUT I", "t", "12 CAPUT II", "t", "CAPUT ΙΙΙ", "t", "CAPUT V", "t", "CAPUT Il", "t", "prose line", "CAPUT IV"]
    notes = [n for n in cu.resolve(make(tmp_path, rules=[rule]), lines).notes if "hand-listed" in n]
    assert len(notes) == 1
    for needle in ("line 3 (a margin number", "line 5 (its numeral", "line 9 (its numeral"):
        assert needle in notes[0]
    assert "line 11" not in notes[0]
    assert not [n for n in cu.resolve(make(tmp_path, rules=[dict(rule, lines=None)]), lines).notes if "hand-listed" in n]


def capita_text(count=12):
    body = ["HEAD", ""]
    for n in range(1, count + 1):
        body += [f"CAPUT {n}.", "", " ".join(["word"] * 700), ""]
    return body


OVERSIZE_RULE = {"id": "h", "pattern": "^HEAD$", "locus": "head", "allow_oversize": "one undivided work"}


def test_not_subheadings_lets_listed_lines_stand_out_of_the_count(tmp_path):
    lines = capita_text()
    listed = [3 + 4 * k for k in range(12)]
    entry = {"lines": listed[1:], "kind": "quoted-list", "quote": "CAPUT 2."}
    assert any("does not hold" in p for p in unexplained(cu.resolve(make(tmp_path, rules=[OVERSIZE_RULE]), lines)))
    ok = cu.resolve(make(tmp_path, rules=[OVERSIZE_RULE], not_subheadings=[entry]), lines)
    assert unexplained(ok) == []
    partial = dict(entry, lines=listed[8:9], quote="CAPUT 9.")
    res = cu.resolve(make(tmp_path, rules=[OVERSIZE_RULE], not_subheadings=[partial]), lines)
    assert any("does not hold" in p for p in unexplained(res))


def test_not_subheadings_ranges_and_checks(tmp_path):
    lines = capita_text()
    ranged = {"lines": [[7, 47]], "kind": "footnote", "quote": "CAPUT 2."}
    res = cu.resolve(make(tmp_path, rules=[OVERSIZE_RULE], not_subheadings=[ranged]), lines)
    assert not any("does not hold" in p for p in res.problems)
    assert any("lists" in p and "does not flag" in p for p in res.problems)
    wrong = dict(ranged, lines=[7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47], quote="CAPUT 99.")
    res = cu.resolve(make(tmp_path, rules=[OVERSIZE_RULE], not_subheadings=[wrong]), lines)
    assert any("quotes text that is not on the line" in p for p in res.problems)
    outside = {"lines": [2], "kind": "ocr-debris", "quote": "HEAD"}
    res = cu.resolve(make(tmp_path, rules=[OVERSIZE_RULE], not_subheadings=[outside]), lines)
    assert any("does not flag" in p for p in res.problems)


@pytest.mark.parametrize("entry,message", [
    ({"lines": [3], "kind": "heading", "quote": "x"}, "kind must be one of"),
    ({"lines": [], "kind": "footnote", "quote": "x"}, "needs lines"),
    ({"lines": [3], "kind": "footnote", "quote": ""}, "needs lines"),
    ({"lines": ["a"], "kind": "footnote", "quote": "x"}, "line numbers"),
    ({"lines": [3], "kind": "footnote", "quote": "x", "pattern": "^x"}, "unknown field"),
])
def test_not_subheadings_entries_are_validated(tmp_path, entry, message):
    with pytest.raises(cu.CurationError, match=message):
        make(tmp_path, rules=[OVERSIZE_RULE], not_subheadings=[entry])
