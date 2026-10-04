import pytest

from engine.deeper.door import OPEN, DoorSettings, Stage, ceiling_usd, compute

STAGES = (
    Stage(at=0.66, table_free_rounds=1),
    Stage(at=0.75, free_share=0.5, solo_free_rounds=2),
    Stage(at=0.90, table_free_rounds=0),
    Stage(at=0.95, free_voice=False),
    Stage(at=1.00, paid_voice=False),
)
SETTINGS = DoorSettings(base_usd=150.0, gift_share=0.8, purchase_share=0.5, invoice_factor=1.0, stages=STAGES)
NO_FUNDS = {"gift": 0, "purchase": 0, "adjustment": 0}


def stage_at(ratio, funds=NO_FUNDS, settings=SETTINGS):
    return compute(settings, ratio * settings.base_usd, funds)


def test_the_ceiling_is_the_base_plus_a_share_of_the_weeks_money():
    assert ceiling_usd(SETTINGS, NO_FUNDS) == 150.0
    funds = {"gift": 10_000, "purchase": 20_000, "adjustment": 5_000}
    assert ceiling_usd(SETTINGS, funds) == pytest.approx(150 + 0.8 * 150 + 0.5 * 200)


def test_money_never_lowers_the_ceiling_below_the_base():
    assert ceiling_usd(SETTINGS, {"gift": 0, "purchase": 0, "adjustment": -50_000}) == 150.0


def test_no_spend_leaves_the_door_open():
    state = stage_at(0.0)
    assert state.stage == 0 and state.free_voice and state.paid_voice
    assert state.table_free_rounds is None and state.solo_free_rounds is None and state.free_share == 1.0


@pytest.mark.parametrize(
    "ratio, stage, table, solo, share, free, paid",
    [
        (0.65, 0, None, None, 1.0, True, True),
        (0.66, 1, 1, None, 1.0, True, True),
        (0.75, 2, 1, 2, 0.5, True, True),
        (0.89, 2, 1, 2, 0.5, True, True),
        (0.90, 3, 0, 2, 0.5, True, True),
        (0.95, 4, 0, 2, 0.5, False, True),
        (1.00, 5, 0, 2, 0.5, False, False),
        (3.00, 5, 0, 2, 0.5, False, False),
    ],
)
def test_each_stage_narrows_in_order_and_keeps_what_an_earlier_one_closed(ratio, stage, table, solo, share, free, paid):
    state = stage_at(ratio)
    assert (state.stage, state.table_free_rounds, state.solo_free_rounds, state.free_share, state.free_voice, state.paid_voice) == (
        stage, table, solo, share, free, paid,
    )


def test_a_higher_ratio_never_opens_what_a_lower_one_closed():
    states = [stage_at(r / 100) for r in range(0, 160)]
    for earlier, later in zip(states, states[1:]):
        assert later.stage >= earlier.stage
        assert not (later.free_voice and not earlier.free_voice)
        assert not (later.paid_voice and not earlier.paid_voice)
        assert (later.table_free_rounds if later.table_free_rounds is not None else 99) <= (earlier.table_free_rounds if earlier.table_free_rounds is not None else 99)
        assert later.free_share <= earlier.free_share


def test_gifts_reopen_the_door():
    closed = stage_at(0.96)
    assert not closed.free_voice
    reopened = compute(SETTINGS, 0.96 * 150, {"gift": 20_000, "purchase": 0, "adjustment": 0})
    assert reopened.free_voice and reopened.ceiling_usd > 150


def test_the_invoice_factor_makes_the_door_count_what_the_bill_will_say():
    plain = compute(SETTINGS, 100.0, NO_FUNDS)
    billed = compute(DoorSettings(150.0, 0.8, 0.5, 1.35, STAGES), 100.0, NO_FUNDS)
    assert billed.ratio == pytest.approx(plain.ratio * 1.35)
    assert billed.stage > plain.stage


def test_the_open_state_closes_nothing():
    assert OPEN.free_voice and OPEN.paid_voice and OPEN.stage == 0
