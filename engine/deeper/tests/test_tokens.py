"""The token arithmetic, checked against Mark's ruling of 2026-10-03."""
import pytest

from engine.deeper.tokens import TokenRates, charge, conversation_cost, opening_cost, round_cost

RATES = TokenRates(
    solo_open=50, solo_round=20, solo_round_later=25,
    table_open_per_seat=50, table_round_two=60, table_round_three=100,
    table_round_two_later=75, table_round_three_later=125,
    later_rounds_from=4, free_daily=330, free_rounds=3,
)


def test_a_solo_conversation_of_three_rounds_draws_110():
    assert [charge(RATES, n) for n in (1, 2, 3)] == [70, 20, 20]
    assert conversation_cost(RATES, 3) == 110


def test_the_fourth_round_and_on_draw_the_higher_amount():
    assert [round_cost(RATES, n) for n in (3, 4, 5, 9)] == [20, 25, 25, 25]
    assert conversation_cost(RATES, 5) == 110 + 25 + 25


def test_a_table_opens_per_seat_and_a_round_draws_by_seats():
    assert opening_cost(RATES, 2) == 100 and opening_cost(RATES, 3) == 150
    assert [round_cost(RATES, 1, s) for s in (2, 3)] == [60, 100]
    assert [round_cost(RATES, 4, s) for s in (2, 3)] == [75, 125]
    assert conversation_cost(RATES, 3, 2) == 100 + 3 * 60
    assert conversation_cost(RATES, 3, 3) == 150 + 3 * 100


def test_the_opening_is_drawn_once_with_the_first_round_only():
    assert charge(RATES, 1, 3) == 150 + 100 and charge(RATES, 2, 3) == 100


def test_the_free_grant_is_three_solo_conversations_of_three_rounds():
    assert RATES.free_daily == 3 * conversation_cost(RATES, RATES.free_rounds)


def test_the_packs_are_whole_numbers_of_those_conversations():
    per = conversation_cost(RATES, 3)
    assert [1100 // per, 2750 // per, 6600 // per] == [10, 25, 60]
    assert all(t % per == 0 for t in (1100, 2750, 6600))


@pytest.mark.parametrize("seats", [0, 4, -1])
def test_a_conversation_has_one_to_three_seats(seats):
    with pytest.raises(ValueError):
        charge(RATES, 1, seats)


def test_rounds_count_from_one():
    with pytest.raises(ValueError):
        round_cost(RATES, 0)
