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
    res = cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[{"series": "s", "line": 3, "quote": "SERMO 1l",
                                                  "reason": {"leaf_missing": {"between": [1, 3]}}}]),
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


STEPS = ["SERMO 1", "t", "SERMO 3", "t", "SERMO 3", "t", "SERMO 2", "t", "SERMO 4"]


def step(line, quote, **reason):
    return {"series": "s", "line": line, "quote": quote, "reason": reason}


def explained_steps():
    return [step(3, "SERMO 3", leaf_missing={"between": [1, 3]}),
            step(5, "SERMO 3", as_printed={"line": 3, "quote": "SERMO 3"}),
            step(7, "SERMO 2", as_printed={"line": 5, "quote": "SERMO 3"}),
            step(9, "SERMO 4", leaf_missing={"between": [7, 9]})]


def test_unexplained_series_steps_fail_and_expected_gaps_explain_them(tmp_path):
    problems = unexplained(cu.resolve(make(tmp_path, rules=[SERMO]), STEPS))
    assert len(problems) == 1 and "series 's' has 4" in problems[0] and "lines 3, 5, 7, 9" in problems[0]
    gaps = explained_steps()
    assert unexplained(cu.resolve(make(tmp_path, rules=[SERMO], expected_gaps=gaps), STEPS)) == []
    wrong = [dict(gaps[0], quote="the edition prints no II")] + gaps[1:]
    assert any("not on the line" in p for p in unexplained(cu.resolve(make(tmp_path, rules=[SERMO], expected_gaps=wrong), STEPS)))
    extra = gaps + [step(1, "SERMO 1", counterpart={"line": 3})]
    assert any("matches no gap" in p for p in unexplained(cu.resolve(make(tmp_path, rules=[SERMO], expected_gaps=extra), STEPS)))
    assert any("no rule or entry numbers" in p for p in unexplained(cu.resolve(
        make(tmp_path, rules=[SERMO], expected_gaps=gaps + [dict(gaps[0], series="zz")]), STEPS)))


def gap_problems(tmp_path, entry, lines=STEPS[:3], **doc):
    cur = make(tmp_path, rules=[SERMO], expected_gaps=[entry], **doc)
    return unexplained(cu.resolve(cur, lines))


def test_an_expected_gap_without_a_reason_fails_and_names_the_entry(tmp_path):
    entry = {"series": "s", "line": 3, "quote": "SERMO 3"}
    problems = gap_problems(tmp_path, entry)
    assert len(problems) == 1
    assert "series 's' at line 3 has no reason" in problems[0]
    assert gap_problems(tmp_path, dict(entry, reason=None)) == problems


@pytest.mark.parametrize("reason", [
    "the edition skips II", {"leaf_missing": {"between": [1]}}, {"leaf_missing": {"between": [3, 1]}},
    {"leaf_missing": {}}, {"counterpart": {"line": "3"}}, {"edition_unnumbered": {"line": 2}},
    {"edition_unnumbered": {"line": 2, "quote": ""}}, {"nonsense": {"line": 2}},
    {"counterpart": {"line": 2}, "leaf_missing": {"between": [1, 3]}}, {"counterpart": {"line": 2, "extra": 1}}])
def test_a_malformed_reason_is_rejected_at_load(tmp_path, reason):
    with pytest.raises(cu.CurationError, match="expected_gaps\\[0\\]"):
        make(tmp_path, rules=[SERMO], expected_gaps=[{"series": "s", "line": 3, "quote": "SERMO 3", "reason": reason}])


def test_leaf_missing_must_name_the_series_neighbours_around_the_gap(tmp_path):
    ok = step(3, "SERMO 3", leaf_missing={"between": [1, 3]})
    assert gap_problems(tmp_path, ok) == []
    for between in ([1, 2], [2, 3], [1, 9]):
        problems = gap_problems(tmp_path, step(3, "SERMO 3", leaf_missing={"between": between}))
        assert len(problems) == 1 and "series 's' at line 3" in problems[0]
        assert "neighbours" in problems[0] or "outside the file" in problems[0]
    repeat = step(5, "SERMO 3", leaf_missing={"between": [3, 5]})
    assert "does not explain a repeated step" in gap_problems(tmp_path, repeat, lines=STEPS[:5])[0]


def test_counterpart_must_be_a_division_or_matched_head(tmp_path):
    lines = ["SERMO 1", "t", "SERMO 3", "other language head", "SERMO 4"]
    division = {"start_line": 4, "locus": "counter", "title": "t"}
    ok = step(3, "SERMO 3", counterpart={"line": 4})
    assert gap_problems(tmp_path, ok, lines=lines, divisions=[division]) == []
    assert len(gap_problems(tmp_path, ok, lines=lines)) == 1
    assert "is not a division start or matched head" in gap_problems(tmp_path, ok, lines=lines)[0]
    assert "outside the file" in gap_problems(tmp_path, step(3, "SERMO 3", counterpart={"line": 99}), lines=lines)[0]
    own_series = gap_problems(tmp_path, step(3, "SERMO 3", counterpart={"line": 1}), lines=lines)
    assert len(own_series) == 1 and "outside this series" in own_series[0]
    far = ["SERMO 1", "t", "SERMO 3", "t", "SERMO 4", "t", "t", "other head"]
    far_division = [{"start_line": 8, "locus": "counter", "title": "t"}]
    assert "not within or next to the step" in gap_problems(
        tmp_path, step(3, "SERMO 3", counterpart={"line": 8}), lines=far, divisions=far_division)[0]
    own = gap_problems(tmp_path, step(3, "SERMO 3", counterpart={"line": 3}), lines=lines)
    assert len(own) == 1 and "outside this series" in own[0]


def test_edition_unnumbered_needs_its_quote_on_a_line_between_the_neighbours(tmp_path):
    lines = ["SERMO 1", "SERMO without numeral", "t", "SERMO 3"]
    ok = step(4, "SERMO 3", edition_unnumbered={"line": 2, "quote": "without numeral"})
    assert gap_problems(tmp_path, ok, lines=lines) == []
    absent = step(4, "SERMO 3", edition_unnumbered={"line": 3, "quote": "without numeral"})
    assert "quotes text that is not on line 3" in gap_problems(tmp_path, absent, lines=lines)[0]
    outside = step(4, "SERMO 3", edition_unnumbered={"line": 1, "quote": "SERMO 1"})
    assert "not between the neighbours" in gap_problems(tmp_path, outside, lines=lines)[0]


def test_as_printed_must_name_the_previous_reading(tmp_path):
    lines = ["SERMO 1", "t", "SERMO 1", "t"]
    assert gap_problems(tmp_path, step(3, "SERMO 1", as_printed={"line": 1, "quote": "SERMO 1"}), lines=lines) == []
    wrong = gap_problems(tmp_path, step(3, "SERMO 1", as_printed={"line": 2, "quote": "t"}), lines=lines)
    assert len(wrong) == 1 and "not the previous reading" in wrong[0]
    unquoted = gap_problems(tmp_path, step(3, "SERMO 1", as_printed={"line": 1, "quote": "SERMO 9"}), lines=lines)
    assert "quotes text that is not on line 1" in unquoted[0]
    assert "does not explain a gap step" in gap_problems(
        tmp_path, step(3, "SERMO 3", as_printed={"line": 1, "quote": "SERMO 1"}))[0]


def test_an_excusal_cannot_hide_a_printed_but_damaged_numeral(tmp_path):
    lines = ["SERMO I", "t", "SERMO Il", "t", "SERMO III"]
    rule = {"id": "s", "pattern": r"^SERMO (?P<n>[IVX]+)$", "locus": "sermo{n|int}", "number": "n"}
    entry = {"series": "s", "line": 5, "quote": "SERMO III", "reason": {"leaf_missing": {"between": [1, 5]}}}
    cur = make(tmp_path, rules=[rule], expected_gaps=[entry])
    problems = unexplained(cu.resolve(cur, lines))
    assert len(problems) == 1
    assert "series 's' at line 5" in problems[0] and "look-alike" in problems[0]
    assert 'line 3 (numeral in a form the pattern does not read): "SERMO Il"' in problems[0]
    mended = dict(rule, fixes=[{"line": 3, "quote": "SERMO Il", "set": {"n": "II"}}])
    assert unexplained(cu.resolve(make(tmp_path, rules=[mended]), lines)) == []
    plain = rule
    clean = ["SERMO I", "t", "unnumbered head", "t", "SERMO III"]
    assert unexplained(cu.resolve(make(tmp_path, rules=[plain], expected_gaps=[entry]), clean)) == []


def test_the_scan_reaches_lines_a_hand_listed_rule_does_not_cover_and_skips_ordinary_words(tmp_path):
    rule = {"id": "s", "pattern": r"^(?:\d{1,2} )?(?P<n>[IVX]+)[.,]? ", "locus": "sermo{n|int}", "number": "n",
            "lines": [[1, 1], [7, 7]]}
    lines = ["I. first", "Kai the text", "25 VIL Kai damaged head", "Rom. cites a verse", "t", "more", "IV. fourth"]
    entry = {"series": "s", "line": 7, "quote": "IV. fourth", "reason": {"leaf_missing": {"between": [1, 7]}}}
    problems = unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), lines))
    assert len(problems) == 1 and "line 3 (numeral in a form" in problems[0]
    assert "line 2" not in problems[0] and "line 4" not in problems[0]
    mended = dict(rule, fixes=[{"line": 3, "quote": "VIL Kai", "set": {"n": "III"}}])
    assert not [p for p in unexplained(cu.resolve(make(tmp_path, rules=[mended], expected_gaps=[entry]), lines))
                if "look-alike" in p]


def test_a_look_alike_with_a_margin_number_is_also_found(tmp_path):
    lines = ["SERMO 1", "t", "12 SERMO 2", "t", "SERMO 3"]
    entry = step(5, "SERMO 3", leaf_missing={"between": [1, 5]})
    problems = gap_problems(tmp_path, entry, lines=lines)
    assert len(problems) == 1 and "(a margin number comes first)" in problems[0]


def test_an_unnumbered_head_the_scan_does_not_report_may_be_named(tmp_path):
    lines = ["SERMO 1", "De pace", "t", "SERMO 4"]
    rule = {"id": "s", "pattern": r"^SERMO (?P<n>\d+)$", "locus": "sermo{n}", "number": "n"}
    entry = step(4, "SERMO 4", edition_unnumbered={"line": 2, "quote": "De pace"})
    assert unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), lines)) == []
    flagged = ["SERMO 1", "SERMO x", "t", "SERMO 4"]
    entry = step(4, "SERMO 4", edition_unnumbered={"line": 2, "quote": "SERMO x"})
    problems = unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), flagged))
    assert any("reason edition_unnumbered names line 2" in p for p in problems)
    assert any("look-alike" in p and "line 2" in p for p in problems)


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
    for needle in ("line 3 (a margin number", "line 5 (numeral in a form", "line 9 (numeral in a form"):
        assert needle in notes[0]
    assert "line 11" not in notes[0]
    assert not [n for n in cu.resolve(make(tmp_path, rules=[dict(rule, lines=None)]), lines).notes if "hand-listed" in n]


def hand_listed_notes(tmp_path, rule, lines):
    return [n for n in cu.resolve(make(tmp_path, rules=[rule]), lines).notes if "hand-listed" in n]


def test_hand_listed_warn_skips_lines_a_fix_already_covers(tmp_path):
    rule = {"id": "c", "pattern": r"^CAPUT (?P<n>[IVX]+)$", "locus": "c{n|int}", "number": "n", "lines": [[1, 12]]}
    lines = ["CAPUT I", "t", "CAPUT Il", "t", "CAPUT III", "t", "CAPUT IV"]
    assert "line 3 (numeral" in hand_listed_notes(tmp_path, rule, lines)[0]
    fixed = dict(rule, fixes=[{"line": 3, "quote": "CAPUT Il", "set": {"n": "II"}}])
    assert hand_listed_notes(tmp_path, fixed, lines) == []
    other_line = dict(rule, fixes=[{"line": 5, "quote": "CAPUT III", "set": {"n": "III"}}])
    assert "line 3 (numeral" in hand_listed_notes(tmp_path, other_line, lines)[0]


def test_hand_listed_warn_counts_each_kind_and_lists_each_line_beneath(tmp_path):
    rule = {"id": "c", "pattern": r"^CAPUT (?P<n>[IVX]+)$", "locus": "c{n|int}", "number": "n", "lines": [[1, 40]]}
    lines = []
    for k in range(5):
        lines += [f"CAPUT I{k}", f"{k + 10} CAPUT V"]
    lines += ["CAPUT I"]
    note = hand_listed_notes(tmp_path, rule, lines)[0]
    head, *detail = note.split("\n")
    assert "10 line(s)" in head
    assert head.endswith("5 numeral in a form the pattern does not read; 5 a margin number comes first")
    assert len(detail) == 10 and all(d.startswith("      line ") for d in detail)
    assert detail[0].startswith('      line 1 (numeral in a form the pattern does not read): "CAPUT I0"')


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


DAMAGED = ["SERMO I", "t", "SERMO Il", "t", "SERMO III"]
STROKE_RULE = {"id": "s", "pattern": r"^SERMO (?P<n>[IVX]+)$", "locus": "sermo{n|int}", "number": "n"}


def test_edition_unnumbered_cannot_name_a_head_that_carries_a_damaged_numeral(tmp_path):
    entry = step(5, "SERMO III", edition_unnumbered={"line": 3, "quote": "SERMO Il"})
    cur = make(tmp_path, rules=[STROKE_RULE], expected_gaps=[entry])
    problems = unexplained(cu.resolve(cur, DAMAGED))
    assert any("reason edition_unnumbered names line 3" in p for p in problems)
    assert any("look-alike" in p and "line 3" in p for p in problems)
    rule = {"id": "s", "pattern": r"^(?:\d{1,2} )?(?P<n>[IVX]+)[.,]? ", "locus": "sermo{n|int}", "number": "n"}
    lines = ["I. a", "25 VIL Kai b", "t", "IV. d"]
    entry = step(4, "IV. d", edition_unnumbered={"line": 2, "quote": "25 VIL"})
    problems = unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), lines))
    assert any("numeral position" in p and "edition_unnumbered" in p for p in problems)
    assert any("look-alike" in p and "line 2" in p for p in problems)


def test_counterpart_cannot_name_a_head_that_carries_a_damaged_numeral(tmp_path):
    division = {"start_line": 3, "locus": "damaged", "title": "t"}
    entry = step(5, "SERMO III", counterpart={"line": 3})
    cur = make(tmp_path, rules=[STROKE_RULE], expected_gaps=[entry], divisions=[division])
    problems = unexplained(cu.resolve(cur, DAMAGED))
    assert any("numeral position" in p for p in problems) and any("look-alike" in p for p in problems)


def test_an_unreadable_reading_between_the_neighbours_fails_the_entry(tmp_path):
    rule = {"id": "s", "pattern": r"^SERMO (?P<n>[IVXLCl1]+)\.", "locus": "sermo{n}", "number": "n"}
    lines = ["SERMO I. a", "t", "SERMO IlX. b", "t", "SERMO III. c"]
    entry = step(5, "SERMO III. c", leaf_missing={"between": [1, 5]})
    cur = make(tmp_path, rules=[rule], expected_gaps=[entry])
    assert cu.resolve(cur, lines).sequences["s"] == [(1, 1), (3, None), (5, 3)]
    problems = unexplained(cu.resolve(cur, lines))
    assert problems and all("series 's' at line 5" in p for p in problems)
    named = step(5, "SERMO III. c", leaf_missing={"between": [3, 5]})
    problems = unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[named]), lines))
    assert any("could not be read" in p and "line 3" in p for p in problems)


BRUDER = [
    "C. \\T. Diximusnc aliquid", "C. Vil. Nam quum ille", "C. XWI. (^uapropter adhuc", "C. XFil. Sed quoniam",
    "C. XVH. Non enim audiendi", "C. XXVT. Adumbrata enim", "C. IV^. Non solum autem", "C. XU. Quae autem quasi",
    "C. XV\\ Sic eversa tyrannide", "C. XXV^ Quod (|uum adparuerit", "C. XXVTI. Quando autem",
    "C. XXXV'. (iuintam Tichonius", "C. iV. Debet igiturdi", "C. XY. Agit itaque", "C. XV''!!!. Verum hic",
    "C. XXU. Porro autem omne", "C. XIjV. Quamvis et in illo", "C. IjII. De qua per", "C. IjXI. Haec ergo",
    "C. LXXX[. Hoc nunc dicam", "C. LXXXn. Xam et ipsa", "C. rjXXXni. Qui vero", "C. LXXX^'!!. Neqiie enini",
    "C. CVUI. Nam neijue", "C. ill. Sed quaecumque"]


def test_every_damaged_head_of_the_bruder_edition_is_reported(tmp_path):
    rule = {"id": "s", "pattern": r"^(?:Caput|[CGO0]\.) ?(?P<c>[IVXLCl1]+)[.,]?\s", "locus": "c{c|int}", "number": "c"}
    lines = ["C. I. first"]
    for head in BRUDER:
        lines += ["text", head]
    lines += ["text", "C. XL. last"]
    entry = step(len(lines), "C. XL. last", leaf_missing={"between": [1, len(lines)]})
    problems = unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), lines))
    assert len(problems) == 1
    shown = problems[0].count(" (numeral in a form the pattern does not read)")
    assert shown == 6
    listed = [i + 1 for i, line in enumerate(lines) if line in BRUDER]
    for start in range(0, len(listed), 5):
        part = lines[:1] + [x for i in listed[start:start + 5] for x in ("text", lines[i - 1])] + ["text", "C. XL. last"]
        entry = step(len(part), "C. XL. last", leaf_missing={"between": [1, len(part)]})
        found = unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), part))
        assert len(found) == 1
        for i, line in enumerate(part):
            if line in BRUDER:
                assert f"line {i + 1} (" in found[0] or f"line {i + 1}:" in found[0]


def test_lowercase_body_text_is_not_a_look_alike_for_an_uppercase_rule(tmp_path):
    rule = {"id": "s", "pattern": r"^(?:\d{1,2} )?(?P<n>[IVX]+)[.,]? ", "locus": "sermo{n|int}", "number": "n"}
    lines = ["I. a", "xxi body text of the page", "ii more text", "t", "IV. d"]
    entry = step(5, "IV. d", leaf_missing={"between": [1, 5]})
    assert unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), lines)) == []


CAPUT_RULE = {"id": "s", "pattern": r"^(?:Caput|[CGO0]\.) ?(?P<n>[IVXLCl1]+)[.,]?\s", "locus": "c{n|int}", "number": "n"}


def test_no_reason_form_can_excuse_a_damaged_head_the_scan_reports(tmp_path):
    gebhardt = {"id": "s", "pattern": r"^(?:\d{1,2} )?(?P<n>[IVX]+)[.,]? ", "locus": "sermo{n|int}", "number": "n"}
    lines = ["I. a", "25 VIL Kai b", "t", "IV. d"]
    division = {"start_line": 2, "locus": "damaged", "title": "t"}
    for reason in ({"leaf_missing": {"between": [1, 4]}}, {"edition_unnumbered": {"line": 2, "quote": "25 VIL"}},
                   {"counterpart": {"line": 2}}):
        entry = step(4, "IV. d", **reason)
        cur = make(tmp_path, rules=[gebhardt], expected_gaps=[entry], divisions=[division])
        problems = unexplained(cu.resolve(cur, lines))
        assert any("look-alike" in p and "line 2" in p for p in problems), reason


def test_a_reading_of_the_series_is_never_excused_by_a_reason(tmp_path):
    rule = {"id": "s", "pattern": r"^SERMO (?P<n>[IVXLCl1]+)\.", "locus": "sermo{n}", "number": "n"}
    lines = ["SERMO I. a", "t", "SERMO IlX. b", "t", "SERMO III. c"]
    for reason in ({"leaf_missing": {"between": [3, 5]}}, {"leaf_missing": {"between": [1, 5]}},
                   {"edition_unnumbered": {"line": 3, "quote": "IlX"}}):
        entry = step(5, "SERMO III. c", **reason)
        assert unexplained(cu.resolve(make(tmp_path, rules=[rule], expected_gaps=[entry]), lines)), reason


def test_a_reason_and_the_scan_use_one_test(tmp_path):
    lines = ["C. I. a", "t", "C. X\u00a7I. b", "t", "C. III. c"]
    division = {"start_line": 3, "locus": "damaged", "title": "t"}
    for reason in ({"edition_unnumbered": {"line": 3, "quote": "X\u00a7I"}}, {"counterpart": {"line": 3}}):
        entry = step(5, "C. III. c", **reason)
        cur = make(tmp_path, rules=[CAPUT_RULE], expected_gaps=[entry], divisions=[division])
        problems = unexplained(cu.resolve(cur, lines))
        assert any("the scan reports as a head of the series" in p for p in problems)
        assert any("look-alike" in p and "line 3" in p for p in problems)


LEAD_RULE = {"id": "s", "pattern": r"^(?:\d{1,2} )?(?P<n>[IVX]+)[.,]? ", "locus": "sermo{n|int}", "number": "n"}
REAL_LEADING = ["Ilil. Contra litteras Petiliani", "Iill. Contra litteras Petiliani", "Illi. DE CONTINENTIA.",
                "15 XXilll. Neque enim dictum est", "CLXXXVIIi.", "Xlil. Qu'il consid\u00e8re", "Vil. On continua",
                "XXXiX. D\u00e8s lors", "iV. Die Ausf\u00fchrung. 49", "Vil. Kai body", "Vill. Sed", "XXiX. wSi", "XIj", "IjXI. Haec"]


@pytest.mark.parametrize("head", REAL_LEADING)
def test_a_damaged_leading_numeral_with_lowercase_strokes_is_found(tmp_path, head):
    lines = ["I. a", "t", head + " x" if " " not in head else head, "t", "IV. d"]
    entry = step(5, "IV. d", leaf_missing={"between": [1, 5]})
    problems = unexplained(cu.resolve(make(tmp_path, rules=[LEAD_RULE], expected_gaps=[entry]), lines))
    assert len(problems) == 1 and "line 3" in problems[0]


@pytest.mark.parametrize("body", ["xxi body text of the page", "ii more text", "in nomine patris", "de pace"])
def test_a_lowercase_body_word_is_not_a_leading_numeral(tmp_path, body):
    lines = ["I. a", "t", body, "t", "IV. d"]
    entry = step(5, "IV. d", leaf_missing={"between": [1, 5]})
    assert unexplained(cu.resolve(make(tmp_path, rules=[LEAD_RULE], expected_gaps=[entry]), lines)) == []


def test_only_a_required_literal_word_skips_the_shape_test(tmp_path):
    free = {"id": "s", "pattern": r"^(?:\S{1,3} ){0,2}(?:[A-Za-z1^.]{1,10}[.,:]? ){0,2}(?P<n>\d{1,3})[.,:] ?",
            "locus": "s{n}", "number": "n"}
    lines = ["1. a", "t", "de baptismo Iohannis, quod solet", "collegii consortio iungerentur", "t", "5. e"]
    entry = step(6, "5. e", leaf_missing={"between": [1, 6]})
    assert unexplained(cu.resolve(make(tmp_path, rules=[free], expected_gaps=[entry]), lines)) == []
    required = {"id": "s", "pattern": r"^(?:SERMO|Sermo) (?P<n>[IVX]+)[.,]? ", "locus": "s{n|int}", "number": "n"}
    lines = ["SERMO I. a", "t", "SERMO de baptismo", "t", "SERMO V. e"]
    entry = step(5, "SERMO V. e", leaf_missing={"between": [1, 5]})
    assert any("line 3" in p for p in unexplained(cu.resolve(make(tmp_path, rules=[required], expected_gaps=[entry]), lines)))
    rules = make(tmp_path, rules=[required, dict(free, id="f")]).rules
    assert [cu.requires_head_word(r) for r in rules] == [True, False]
    assert not cu.requires_head_word(make(tmp_path, rules=[LEAD_RULE]).rules[0])
    assert cu.requires_head_word(make(tmp_path, rules=[CAPUT_RULE]).rules[0])


def test_counterpart_may_name_a_reading_of_another_series(tmp_path):
    s = {"id": "s", "pattern": r"^(?P<n>[IVX]+)\. ", "locus": "s{n|int}", "number": "n", "lines": [[1, 1], [4, 4]]}
    g = {"id": "g", "pattern": r"^(?P<n>[IVX]+)\. ", "locus": "g{n|int}", "number": "n", "lines": [[2, 3], [5, 5]]}
    lines = ["I. a", "I. a", "II. b", "III. c", "III. c"]
    entry = step(4, "III. c", counterpart={"line": 3})
    assert unexplained(cu.resolve(make(tmp_path, rules=[s, g], expected_gaps=[entry]), lines)) == []


def test_a_fix_of_another_rule_does_not_cover_a_damaged_head(tmp_path):
    other = {"id": "p", "pattern": r"^ZZZ (?P<x>\S+)$", "locus": "p{x}",
             "fixes": [{"line": 3, "quote": "SERMO Il", "set": {"x": "1"}}]}
    entry = step(5, "SERMO III", leaf_missing={"between": [1, 5]})
    problems = unexplained(cu.resolve(make(tmp_path, rules=[STROKE_RULE, other], expected_gaps=[entry]), DAMAGED))
    assert any("look-alike" in p and "line 3" in p for p in problems)


def test_yaml_booleans_are_not_line_numbers(tmp_path):
    for entry in (dict(step(3, "SERMO 3", leaf_missing={"between": [1, 3]}), line=True),
                  step(3, "SERMO 3", leaf_missing={"between": [True, 3]}),
                  step(3, "SERMO 3", counterpart={"line": True}),
                  step(3, "SERMO 3", edition_unnumbered={"line": True, "quote": "x"})):
        with pytest.raises(cu.CurationError):
            make(tmp_path, rules=[SERMO], expected_gaps=[entry])
