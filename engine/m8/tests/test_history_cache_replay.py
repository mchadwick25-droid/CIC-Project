import pytest

from engine.m8.history_cache_replay import FRAME_TOKENS, replay


def _turn(index, uncached, output=400):
    return {
        "turn_index": index, "voice_call_input_tokens": uncached, "voice_call_output_tokens": output,
        "voice_call_cache_write_tokens": 12000 if index == 0 else 0, "voice_call_cache_read_tokens": 0 if index == 0 else 12000,
    }


def test_turn_zero_has_no_history_so_only_the_directive_frame_is_added():
    rows = replay([_turn(0, 300), _turn(1, 1300)])
    assert rows[0]["history_tokens"] == 0
    assert rows[0]["after"] - rows[0]["before"] == pytest.approx(FRAME_TOKENS * 3.0 / 1_000_000)


def test_later_turns_read_the_prior_history_at_the_cache_rate():
    rows = replay([_turn(i, 300 + 1000 * i) for i in range(6)])
    assert all(r["after"] < r["before"] for r in rows[2:])
    assert [r["history_tokens"] for r in rows] == [0, 1000, 2000, 3000, 4000, 5000]


def test_the_saving_grows_as_the_history_grows():
    rows = replay([_turn(i, 300 + 1000 * i) for i in range(8)])
    saved = [1 - r["after"] / r["before"] for r in rows]
    assert saved[7] > saved[3] > saved[1]
