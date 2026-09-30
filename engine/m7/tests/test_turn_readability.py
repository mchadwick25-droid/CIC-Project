import pytest

from engine.m1.fk import fk_grade, fre_score
from engine.m1.gates import FK_CEILING, FK_FLOOR, FRE_FLOOR
from engine.m7 import turn_readability as tr

IN_BAND = (
    "Ephrem taught the faith through hymns that families could learn by heart, so the songs carried "
    "his teaching into homes where few people could read. Men and women took a vow to stay single "
    "and serve the poor, and they lived inside the local church and did not go off to a monastery. "
    "Their teachers liked plain words better than long arguments, and we know most of this from "
    "a few old texts that still survive."
)
TOO_SIMPLE = (
    "We sang in the church. The songs were long. The people sat and sang with us. "
    "It was a good day for all of us. We ate bread and we sang some more that night."
)
DENSE = (
    "The christological controversies precipitated by fourth-century pneumatological "
    "disputations necessitated comprehensive institutional reconfigurations of ecclesiastical "
    "jurisdictions throughout Mesopotamian metropolitan territories, notwithstanding "
    "considerable disagreements concerning theological terminology."
)
SHORT_DENSE = "Ecclesiastical reconfigurations necessitated comprehensiveness."


def test_the_turn_scorer_is_the_record_gates_scorer():
    score = tr.score_turn(IN_BAND)
    assert score.fk == pytest.approx(fk_grade(IN_BAND))
    assert score.fre == pytest.approx(fre_score(IN_BAND))


def test_the_ceilings_are_the_record_gates_ceilings():
    assert (FK_CEILING, FRE_FLOOR, FK_FLOOR) == (10, 60, 8)


def test_an_in_band_turn_passes():
    tr.assert_turn_readable(IN_BAND)
    score = tr.score_turn(IN_BAND)
    assert score.passed and not score.below_floor
    assert FK_FLOOR <= score.fk <= FK_CEILING and score.fre >= FRE_FLOOR


def test_a_dense_turn_fails_on_both_measures():
    with pytest.raises(tr.TurnUnreadable) as exc:
        tr.assert_turn_readable(DENSE)
    assert "FK grade" in str(exc.value) and "FRE" in str(exc.value)


def test_a_turn_under_the_band_floor_is_reported_never_failed():
    score = tr.score_turn(TOO_SIMPLE)
    assert score.scored and score.fk < FK_FLOOR
    assert score.below_floor and score.passed
    tr.assert_turn_readable(TOO_SIMPLE)


def test_a_turn_too_short_to_grade_is_unscored_not_failed():
    score = tr.score_turn(SHORT_DENSE)
    assert not score.scored and score.passed
    tr.assert_turn_readable(SHORT_DENSE)
    tr.assert_turn_readable("")


def test_report_lists_every_hard_fail_and_every_below_floor_turn_by_index():
    report = tr.report_turns([IN_BAND, DENSE, TOO_SIMPLE, SHORT_DENSE])
    assert report["turns"] == 4 and report["scored"] == 3 and report["unscored"] == 1
    assert [f["index"] for f in report["failed"]] == [1]
    assert [b["index"] for b in report["below_floor"]] == [2]


def test_one_bad_turn_fails_a_batch_even_when_the_average_is_fine():
    report = tr.report_turns([IN_BAND] * 5 + [DENSE])
    assert len(report["failed"]) == 1 and report["failed"][0]["index"] == 5
