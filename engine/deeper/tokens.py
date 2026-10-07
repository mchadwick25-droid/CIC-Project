"""What a conversation draws, in tokens. Pure arithmetic over the rates in the
operations file: no storage, no clock, nothing about worlds or voices.

A conversation draws its opening amount with its first admitted round, on top
of that round's own amount, so a solo conversation of three rounds draws
50 + 3 * 20 = 110 tokens. A Table's opening amount is per seat. From a set
round onward each round draws its higher amount, because the history it
carries has grown.
"""
from dataclasses import dataclass

MAX_SEATS = 3


@dataclass(frozen=True)
class TokenRates:
    solo_open: int
    solo_round: int
    solo_round_later: int
    table_open_per_seat: int
    table_round_two: int
    table_round_three: int
    table_round_two_later: int
    table_round_three_later: int
    later_rounds_from: int
    free_window: int
    free_window_days: int
    free_rounds: int


@dataclass(frozen=True)
class Pack:
    price_usd: int
    tokens: int


def opening_cost(rates: TokenRates, seats: int = 1) -> int:
    """Drawn once, with a conversation's first admitted round. seats is 1 for a solo conversation."""
    _check_seats(seats)
    return rates.solo_open if seats == 1 else rates.table_open_per_seat * seats


def round_cost(rates: TokenRates, round_no: int, seats: int = 1) -> int:
    """The round's own amount: round_no counts from 1."""
    _check_seats(seats)
    if round_no < 1:
        raise ValueError("rounds count from 1")
    later = round_no >= rates.later_rounds_from
    if seats == 1:
        return rates.solo_round_later if later else rates.solo_round
    if seats == 2:
        return rates.table_round_two_later if later else rates.table_round_two
    return rates.table_round_three_later if later else rates.table_round_three


def charge(rates: TokenRates, round_no: int, seats: int = 1) -> int:
    """What admitting this round draws: its own amount, plus the opening amount if it is the first."""
    return round_cost(rates, round_no, seats) + (opening_cost(rates, seats) if round_no == 1 else 0)


def conversation_cost(rates: TokenRates, rounds: int, seats: int = 1) -> int:
    return sum(charge(rates, n, seats) for n in range(1, rounds + 1))


def _check_seats(seats: int) -> None:
    if not 1 <= seats <= MAX_SEATS:
        raise ValueError(f"a conversation has one to {MAX_SEATS} seats")
