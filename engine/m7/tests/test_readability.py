"""Readability is a report-only tendency instrument (Artifact-8 §3.3);
these tests pin its honesty rules, not a precision claim - the syllable
counter is a documented heuristic."""
from engine.m7.readability import MIN_SCORABLE_WORDS, measure, syllables


def test_syllables_heuristic():
    assert syllables("cat") == 1
    assert syllables("water") == 2
    assert syllables("beautiful") == 3
    # silent-e adjustment
    assert syllables("grace") == 1
    # -le keeps its syllable
    assert syllables("table") == 2
    # never zero for a real word
    assert syllables("the") == 1


def test_short_text_reports_unscored_never_clean():
    m = measure("A short answer.")
    assert m["scored"] is False
    assert "fk_grade" not in m and "fre" not in m


def test_long_plain_text_scores_and_reads_easy():
    text = ("The man came to the well at noon. He asked her for a drink of water. "
            "She was surprised that he spoke to her at all. They talked for a long "
            "time about her life and her hope. She left her jar and ran to tell the town.")
    m = measure(text)
    assert m["scored"] is True
    assert m["words"] >= MIN_SCORABLE_WORDS
    # plain narrative prose lands in easy territory - the exact number is a
    # heuristic, the band is the claim
    assert m["fre"] > 60
    assert m["fk_grade"] < 10


def test_dense_text_scores_harder_than_plain():
    plain = measure("The man came to the well at noon. He asked her for a drink. " * 5)
    dense = measure(
        "Contemporaneous ecclesiastical historiography demonstrates considerable "
        "interpretive heterogeneity regarding sacramental participation, "
        "necessitating hermeneutical circumspection concerning liturgical "
        "developmental trajectories across geographically distributed communities." * 3
    )
    assert plain["scored"] and dense["scored"]
    assert dense["fk_grade"] > plain["fk_grade"]
    assert dense["fre"] < plain["fre"]
