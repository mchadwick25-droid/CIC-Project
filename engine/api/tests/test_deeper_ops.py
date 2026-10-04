"""The Go Deeper operations file: it loads, it is complete, its wording reads at
the target level, and a bad file stops the start rather than reaching a participant."""
import re
from pathlib import Path

import pytest
import yaml

from engine.api.deeper_ops import NOTE_KEYS, OPS_PATH, OpsFileError, load_ops
from engine.m7.turn_readability import score_turn


def _write(tmp_path, data) -> str:
    path = tmp_path / "ops.yaml"
    path.write_text(yaml.safe_dump(data))
    return str(path)


def _good():
    return yaml.safe_load(Path(OPS_PATH).read_text())


def test_the_shipped_file_loads_with_every_note():
    ops = load_ops()
    assert set(ops.notes) == set(NOTE_KEYS)
    assert ops.group_daily_ceiling > 0 and ops.group_burst_multiplier > 0 and ops.low_balance_at > 0


def test_the_token_rates_and_packs_are_the_ruled_ones():
    from engine.deeper.tokens import Pack, TokenRates

    ops = load_ops()
    assert ops.rates == TokenRates(
        solo_open=50, solo_round=20, solo_round_later=25,
        table_open_per_seat=50, table_round_two=60, table_round_three=100,
        table_round_two_later=75, table_round_three_later=125,
        later_rounds_from=4, free_daily=330, free_rounds=3,
    )
    assert ops.packs == (Pack(7, 1100), Pack(15, 2750), Pack(30, 6600))


def test_all_wording_reads_at_the_target_level():
    ops = load_ops()
    for text in (ops.limit_text, *ops.notes.values()):
        assert score_turn(text).passed, text


def test_the_stored_pause_names_no_code_and_no_money():
    assert not re.search(r"\b(codes?|pay|paid|price|balance|exchanges?|stripe)\b", load_ops().limit_text, re.I)


@pytest.mark.parametrize(
    "change",
    [
        lambda d: d.pop("words"),
        lambda d: d["limits"].update(table_round_cost=3),
        lambda d: d["limits"].update(low_balance_at=0),
        lambda d: d["limits"].pop("low_balance_at"),
        lambda d: d["limits"].update(extra=1),
        lambda d: d["words"]["notes"].pop("spent"),
        lambda d: d["words"]["notes"].update(spent="  "),
        lambda d: d["words"].update(limit=""),
    ],
)
def test_a_malformed_file_is_refused(tmp_path, change):
    data = _good()
    change(data)
    with pytest.raises(OpsFileError):
        load_ops(_write(tmp_path, data))


@pytest.mark.parametrize(
    "change",
    [
        lambda d: d.pop("tokens"),
        lambda d: d["tokens"].pop("packs"),
        lambda d: d["tokens"]["solo"].update(open=0),
        lambda d: d["tokens"]["solo"].update(round="20"),
        lambda d: d["tokens"]["solo"].update(round_from_fourth=19),
        lambda d: d["tokens"]["table"].update(round_two_seats_from_fourth=59),
        lambda d: d["tokens"]["table"].update(round_three_seats=59),
        lambda d: d["tokens"]["table"].pop("open_per_seat"),
        lambda d: d["tokens"]["free"].update(daily=-1),
        lambda d: d["tokens"].update(packs=[]),
        lambda d: d["tokens"].update(packs=[{"price_usd": 5, "tokens": 800}]),
        lambda d: d["tokens"].update(packs=[{"price_usd": 15, "tokens": 2750}, {"price_usd": 7, "tokens": 1100}]),
        lambda d: d["tokens"].update(packs=[{"price_usd": 7, "tokens": 1100}, {"price_usd": 7, "tokens": 1200}]),
        lambda d: d["tokens"].update(packs=[{"price_usd": 7, "tokens": 2000}, {"price_usd": 15, "tokens": 1500}]),
        lambda d: d["tokens"].update(packs=[{"price_usd": 7}]),
    ],
)
def test_a_bad_token_section_is_refused(tmp_path, change):
    data = _good()
    change(data)
    with pytest.raises(OpsFileError):
        load_ops(_write(tmp_path, data))


def test_a_missing_or_unreadable_file_is_refused(tmp_path):
    with pytest.raises(OpsFileError):
        load_ops(str(tmp_path / "nothing.yaml"))
    (tmp_path / "bad.yaml").write_text("limits: [unclosed")
    with pytest.raises(OpsFileError):
        load_ops(str(tmp_path / "bad.yaml"))


def test_the_flag_on_refuses_to_start_on_a_bad_file(tmp_path, monkeypatch):
    from engine.api import deeper_routes
    from engine.deeper.config import DeeperConfig

    data = _good()
    data["words"].pop("limit")
    monkeypatch.setenv("CIC_DEEPER_OPS_FILE", _write(tmp_path, data))
    config = DeeperConfig(True, str(tmp_path / "m.db"), str(tmp_path / "c.db"))
    with pytest.raises(OpsFileError):
        deeper_routes.build_runtime(config, {"CIC_DEEPER_WEBHOOK_SECRET": "whsec_x", "CIC_API_ANON_CAP_ENABLED": "1"})
