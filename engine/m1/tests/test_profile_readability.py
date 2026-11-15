from pathlib import Path

import pytest

from engine.m1 import gates
from engine.m1 import profile_readability as pr

FIXTURES = Path(__file__).parent / "fixtures" / "profile_bar"
BAR = pr.REPO / "Build/Ministry/Features/Church-Family-Tree/Who-Profiles/bar"

EXPECTED = {
    "origen": (9.2, 74.6),
    "methodius-of-olympus": (9.1, 72.3),
    "constantine-the-great": (8.9, 78.8),
    "athanasius-of-alexandria": (9.1, 72.7),
    "ephrem-the-syrian": (9.2, 76.7),
    "gregory-of-nazianzus": (9.5, 72.0),
    "gregory-of-nyssa": (10.0, 68.6),
    "john-chrysostom": (8.8, 72.1),
}

FLAT = (
    "The story is told in a late Life. An editor printed it from two copies. It is a late telling. "
    "He thought the Lives were made much later. The few other accounts are late as well. "
    "He built a church by the sea. He taught there for many years. Then he died."
)


def _text(name: str) -> str:
    return (FIXTURES / f"{name}.brief.txt").read_text(encoding="utf-8")


def test_thresholds_are_the_record_gate_numbers():
    assert pr.PROFILE_FK_FLOOR == gates.FK_FLOOR
    assert pr.PROFILE_FK_CEILING == gates.FK_CEILING
    assert pr.PROFILE_FRE_FLOOR == gates.FRE_FLOOR
    assert pr.MIN_WORDS == gates.MIN_WORDS_FOR_READABILITY_CHECK


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_each_bar_brief_passes_both_checks(name):
    score = pr.grade_profile_text(_text(name))
    assert score.passed, score.failures
    assert (round(score.fk, 1), round(score.fre_names_out, 1)) == EXPECTED[name]


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_grade_is_the_full_text_grade(name):
    text = pr.normalize(_text(name))
    assert pr.grade_profile_text(text).fk == gates.grade_text(text)["fk"]


def test_fixtures_match_the_bar_when_it_is_present():
    if not BAR.is_dir():
        pytest.skip("the bar folder is not in this checkout")
    for name in EXPECTED:
        assert (BAR / f"{name}.brief.txt").read_text(encoding="utf-8") == _text(name)


def test_flat_prose_fails_the_floor_only():
    score = pr.grade_profile_text(FLAT)
    assert score.fk < pr.PROFILE_FK_FLOOR
    assert score.fre_names_out >= pr.PROFILE_FRE_FLOOR
    assert pr.profile_readability_failures(FLAT) == [
        f"grade {score.fk:.1f} on the full text, below the floor of 8"
    ]


def test_dense_prose_fails_the_ceiling_and_reading_ease():
    dense = (
        "Notwithstanding considerable historiographical disagreement concerning ecclesiastical "
        "administration, contemporary investigators nevertheless characteristically emphasize "
        "institutional continuity throughout successive generations of episcopal administration."
    )
    failures = pr.profile_readability_failures(dense)
    assert any("above the ceiling of 10" in f for f in failures)
    assert any("below the floor of 60" in f for f in failures)


def test_short_text_is_not_scored():
    assert pr.grade_profile_text("Little else is certain.") is None
    assert pr.profile_readability_failures("Little else is certain.") == []


def test_names_are_found_inside_sentences_and_carried_to_openings():
    text = "Origen taught at Alexandria. Later Eusebius wrote that Origen's father died there."
    assert pr.proper_name_forms(text) == {"Origen", "Origen's", "Alexandria", "Eusebius"}


def test_a_capital_after_an_opening_quote_is_not_a_name():
    text = 'He began a sermon: "In praising him I praise virtue." In time the sermon was copied.'
    assert pr.proper_name_forms(text) == set()


def test_a_form_also_used_in_lower_case_is_not_a_name():
    text = 'They wrote: "For He was made man." Then he left, and He was praised.'
    assert "He" not in pr.proper_name_forms(text)


def test_curly_apostrophe_reads_as_straight():
    straight = "Later the people kept Origen's books, and Jerome's friends read Origen aloud to them."
    curly = straight.replace("'", "’")
    assert pr.grade_profile_text(curly) == pr.grade_profile_text(straight)
    assert pr.proper_name_forms(curly) == {"Origen's", "Origen", "Jerome's"}


def test_names_out_raises_reading_ease_and_leaves_grade_alone():
    text = _text("john-chrysostom")
    score = pr.grade_profile_text(text)
    assert score.fre_names_out > gates.grade_text(pr.normalize(text))["fre"]
    assert score.fk_names_out < score.fk


def test_is_profile_brief():
    root = "Build/Ministry/Features/Church-Family-Tree"
    assert pr.is_profile_brief(f"{root}/Who-Profiles/era4/batch11/al-tabari.brief.txt")
    assert pr.is_profile_brief(f"{root}/Council-Profiles/era7/council-of-trent.brief.txt")
    assert not pr.is_profile_brief(f"{root}/Who-Profiles/era4/batch11/al-tabari.card.json")
    assert not pr.is_profile_brief("engine/m1/tests/fixtures/profile_bar/origen.brief.txt")


def test_main_exit_status(tmp_path, capsys):
    good = tmp_path / "good.brief.txt"
    good.write_text(_text("origen"), encoding="utf-8")
    bad = tmp_path / "bad.brief.txt"
    bad.write_text(FLAT, encoding="utf-8")
    assert pr.main([str(good)]) == 0
    assert pr.main([str(tmp_path)]) == 1
    assert pr.main(["--report", str(tmp_path)]) == 0
    assert "FAIL" in capsys.readouterr().out


def test_word_count_matches_fk_after_a_closing_curly_quote():
    text = "He said ‘go home.’ Then the people of Edessa went home, and Ephrem stayed in the city with them."
    normal = pr.normalize(text)
    assert len(pr._forms(normal)) == len(pr._WORD.findall(normal))
    assert pr.grade_profile_text(text).words == len(pr._WORD.findall(normal))


def test_a_closing_straight_quote_does_not_make_an_opening_word():
    text = 'They called him "the great" Constantine. Constantine ruled for many years after that day.'
    assert "Constantine" in pr.proper_name_forms(text)


def test_contractions_of_i_are_not_names():
    text = "He wrote that I'm ready and that I'll come, though I'd rather stay here."
    assert pr.proper_name_forms(text) == set()


def test_a_line_break_and_a_bracket_make_opening_words():
    text = "the story goes on\nThen it ends (So they say) and no more is told."
    assert pr.proper_name_forms(text) == set()


def test_a_name_seen_only_at_sentence_starts_is_not_counted():
    text = "Beuno built a church. Beuno taught there. Later the people kept his feast."
    assert pr.proper_name_forms(text) == set()


def test_an_all_capitals_word_inside_a_sentence_counts_as_a_name():
    assert pr.proper_name_forms("They carved SPQR on the stone and left.") == {"SPQR"}


def _git(repo, *args):
    import subprocess

    subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", *args],
        cwd=repo, check=True, capture_output=True, text=True,
    )


def test_changed_brief_names_skips_a_pure_move_and_keeps_a_move_with_an_edit(tmp_path):
    root = tmp_path / "Build/Ministry/Features/Church-Family-Tree/Who-Profiles"
    (root / "era1").mkdir(parents=True)
    for name in ("origen", "john-chrysostom", "ephrem-the-syrian"):
        (root / "era1" / f"{name}.brief.txt").write_text(_text(name), encoding="utf-8")
    (root / "era1" / "origen.card.json").write_text("{}", encoding="utf-8")
    _git(tmp_path, "init", "-q", "-b", "main")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "base")
    _git(tmp_path, "checkout", "-q", "-b", "work")
    (root / "era2").mkdir()
    _git(tmp_path, "mv", str(root / "era1/origen.brief.txt"), str(root / "era2/origen.brief.txt"))
    _git(tmp_path, "mv", str(root / "era1/john-chrysostom.brief.txt"), str(root / "era2/john-chrysostom.brief.txt"))
    moved = root / "era2/john-chrysostom.brief.txt"
    moved.write_text(moved.read_text(encoding="utf-8") + "\nHe was buried there.\n", encoding="utf-8")
    (root / "era2" / "new.brief.txt").write_text(FLAT, encoding="utf-8")
    (root / "era1" / "origen.card.json").write_text('{"a": 1}', encoding="utf-8")
    _git(tmp_path, "rm", "-q", str(root / "era1/ephrem-the-syrian.brief.txt"))
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "work")
    prefix = "Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/"
    assert sorted(pr.changed_brief_names("main", repo=tmp_path)) == [
        prefix + "john-chrysostom.brief.txt",
        prefix + "new.brief.txt",
    ]


def test_main_returns_2_for_a_brief_that_cannot_be_read(tmp_path):
    assert pr.main([str(tmp_path / "missing.brief.txt")]) == 2
