"""An absence sentence stays only when a cited record states it, with its scope."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4.absence_rule import (
    REASON_ABSENCE_SCOPE, REASON_ABSENCE_UNSUPPORTED, check_absence, content_words, spoken_text,
)
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import apply_net

LIMIT = "lpc.limit.womens-own-voice"


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


def _check(sentence, records, *ids):
    return check_absence(sentence, [records[i] for i in ids])


def test_scope_dropped_is_withheld(records):
    assert _check("No text a woman wrote survives from our two cities.", records, LIMIT) == REASON_ABSENCE_SCOPE


@pytest.mark.parametrize("sentence", [
    "From our two cities, in all our years, no text a woman wrote herself survives.",
    "In our years from 246 to 430, no text a woman wrote survives.",
])
def test_scope_kept_passes(records, sentence):
    assert _check(sentence, records, LIMIT) is None


def test_year_outside_the_record_window_is_withheld(records):
    assert _check("In 150 no text a woman wrote survives.", records, LIMIT) == REASON_ABSENCE_SCOPE


def test_absence_no_record_states_is_withheld(records):
    sentence = "We have no sermon of our own on those opening lines to give you."
    assert _check(sentence, records, LIMIT) == REASON_ABSENCE_UNSUPPORTED
    assert check_absence(sentence, []) == REASON_ABSENCE_UNSUPPORTED


def test_a_sentence_with_no_absence_is_untouched(records):
    assert _check("Women come to us in men's words.", records, LIMIT) is None


def test_self_stance_with_no_topic_passes(records):
    assert check_absence("We cannot say more.", []) is None


def test_fixed_other_tradition_sentence_passes():
    assert check_absence("Our record doesn't mention that Christian tradition.", []) is None


def test_prohibition_field_is_not_support(records):
    assert "writing survives" not in spoken_text(records[LIMIT]) or "a claim that" not in spoken_text(records[LIMIT])
    assert "a claim that a woman's own writing survives" not in spoken_text(records[LIMIT])


def test_content_words_match_whole_words_only():
    assert "prefer" not in content_words("We have no prefect of ours.")
    assert "prefect" in content_words("We have no prefect of ours.")


def _ship(draft, records):
    return apply_net(draft, repository_records=records, thin_topics=None, placement=PlacementContext())


def test_net_removes_the_widened_sentence_and_keeps_the_scoped_one(records):
    draft = (
        f"Women reach us in men's words [[{LIMIT}]]. "
        f"No text a woman wrote survives from our two cities [[{LIMIT}]]."
    )
    text, _citations, net = _ship(draft, records)
    assert "survives" not in text and "Women reach us" in text
    assert any(s["why"] == REASON_ABSENCE_SCOPE for s in net["reply_shape"]["removed"])
    kept = _ship(
        f"In all our years, no text a woman wrote survives from our two cities [[{LIMIT}]].", records,
    )[0]
    assert "survives" in kept


@pytest.mark.parametrize("sentence", [
    "In all our years, no text a woman wrote survives anywhere in the Christian world.",
    "In our years from 246 to 430, no text a woman wrote survives in Rome or Alexandria or Antioch.",
])
def test_a_claim_that_inverts_or_widens_the_record_is_withheld(records, sentence):
    assert _check(sentence, records, LIMIT) is not None


def test_the_fixed_sentence_with_more_after_it_is_checked():
    assert check_absence("Our record doesn't mention that Christian tradition, and no text a man wrote survives either.", []) is not None


def test_a_possessive_is_matched_as_its_word():
    assert "woman" in content_words("No woman's writing survives.")


def test_check_limit_holds_a_limit_the_cue_phrases_miss_to_the_same_test():
    from engine.m4 import absence_rule

    records = load_world_records("lpc")
    limit = records["lpc.limit.womens-own-voice"]
    assert absence_rule.check_absence("We know only that for one country town Augustine looked for a bishop who knew Punic.", [limit]) is None
    assert absence_rule.check_limit("We know only that for one country town Augustine looked for a bishop who knew Punic.", [limit])
    stated = "From our own two cities, in our years from 246 to 430, no text a woman wrote herself survives."
    assert absence_rule.check_limit(stated, [limit]) is None


def test_check_limit_passes_nothing_with_no_word_that_says_what_it_is_about():
    records = load_world_records("lpc")
    from engine.m4 import absence_rule
    for record in (records["lpc.limit.womens-own-voice"], records["lpc.gravity.collegial-communion-preserved"]):
        for sentence in ("That is not known.", "Nothing of that is known to us.", "We cannot say.", "We have nothing on that."):
            assert absence_rule.check_limit(sentence, [record])


def test_check_limit_does_not_match_two_limits_that_only_share_their_way_of_speaking():
    from engine.m4 import absence_rule
    record = {"id": "x.limit.a", "record_type": "honest_limit", "statement": "Our sources do not tell us when the council met."}
    assert absence_rule.check_limit("Our sources do not tell us how the bishop died.", [record])
    assert absence_rule.check_limit("Our sources never tell us what the bishop ate.", [record])
