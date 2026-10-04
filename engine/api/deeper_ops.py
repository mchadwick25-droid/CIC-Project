"""The Go Deeper operations file: the numbers and participant wording that
change over time, kept in one place and changed by pull request. The module
and the conversation engine hold none of them; the HTTP edge reads the file
at startup, refuses to start on a bad one, and hands each part to whoever
needs it as plain data."""
import os
from dataclasses import dataclass

import yaml

from engine.deeper.tokens import Pack, TokenRates

OPS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "deeper", "ops", "go-deeper.yaml")
NOTE_KEYS = ("no_code", "code_not_accepted", "spent", "too_few", "daily_ceiling", "paused", "in_use")
SOLO_KEYS = ("open", "round", "round_from_fourth")
TABLE_KEYS = ("open_per_seat", "round_two_seats", "round_three_seats", "round_two_seats_from_fourth", "round_three_seats_from_fourth")
FREE_KEYS = ("daily", "rounds_per_conversation")
LATER_ROUNDS_FROM = 4
MINIMUM_PACK_USD = 7
LIMIT_KEYS = ("group_daily_ceiling", "group_burst_multiplier", "low_balance_at")


class OpsFileError(Exception):
    """The operations file is missing, malformed or incomplete."""


@dataclass(frozen=True)
class DeeperOps:
    group_daily_ceiling: int
    group_burst_multiplier: int
    low_balance_at: int
    limit_text: str
    notes: dict
    rates: TokenRates
    packs: tuple[Pack, ...]


def _section(data: dict, name: str, keys: tuple[str, ...]) -> dict:
    section = data.get(name)
    if not isinstance(section, dict) or set(section) != set(keys):
        raise OpsFileError(f"{name} must hold exactly {sorted(keys)}")
    return section


def _whole(value, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise OpsFileError(f"{name} must be a positive whole number")
    return value


def _tokens(section) -> tuple[TokenRates, tuple[Pack, ...]]:
    if not isinstance(section, dict) or set(section) != {"solo", "table", "free", "packs"}:
        raise OpsFileError("tokens must hold exactly solo, table, free and packs")
    solo, table, free = (_section(section, name, keys) for name, keys in (("solo", SOLO_KEYS), ("table", TABLE_KEYS), ("free", FREE_KEYS)))
    for group, values in (("solo", solo), ("table", table), ("free", free)):
        for key, value in values.items():
            _whole(value, f"tokens.{group}.{key}")
    if solo["round_from_fourth"] < solo["round"]:
        raise OpsFileError("a solo round from the fourth cannot cost less than before")
    if table["round_two_seats_from_fourth"] < table["round_two_seats"] or table["round_three_seats_from_fourth"] < table["round_three_seats"]:
        raise OpsFileError("a Table round from the fourth cannot cost less than before")
    if table["round_three_seats"] < table["round_two_seats"]:
        raise OpsFileError("a round at three seats cannot cost less than at two")
    rates = TokenRates(
        solo_open=solo["open"], solo_round=solo["round"], solo_round_later=solo["round_from_fourth"],
        table_open_per_seat=table["open_per_seat"], table_round_two=table["round_two_seats"], table_round_three=table["round_three_seats"],
        table_round_two_later=table["round_two_seats_from_fourth"], table_round_three_later=table["round_three_seats_from_fourth"],
        later_rounds_from=LATER_ROUNDS_FROM, free_daily=free["daily"], free_rounds=free["rounds_per_conversation"],
    )
    raw = section["packs"]
    if not isinstance(raw, list) or not raw:
        raise OpsFileError("tokens.packs must list at least one pack")
    packs = []
    for item in raw:
        if not isinstance(item, dict) or set(item) != {"price_usd", "tokens"}:
            raise OpsFileError("each pack holds exactly price_usd and tokens")
        price, amount = _whole(item["price_usd"], "pack price_usd"), _whole(item["tokens"], "pack tokens")
        if price < MINIMUM_PACK_USD:
            raise OpsFileError(f"no pack is priced under ${MINIMUM_PACK_USD}")
        packs.append(Pack(price_usd=price, tokens=amount))
    prices = [p.price_usd for p in packs]
    if prices != sorted(set(prices)) or [p.tokens for p in packs] != sorted(p.tokens for p in packs):
        raise OpsFileError("packs must rise in price, one of each price, and in tokens")
    return rates, tuple(packs)


def load_ops(path: str | None = None) -> DeeperOps:
    path = path or os.environ.get("CIC_DEEPER_OPS_FILE") or OPS_PATH
    try:
        with open(path, encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        raise OpsFileError(f"cannot read {path}: {exc}") from exc
    if not isinstance(data, dict) or set(data) != {"limits", "tokens", "words"}:
        raise OpsFileError("the file must hold exactly limits, tokens and words")
    limits = _section(data, "limits", LIMIT_KEYS)
    for key, value in limits.items():
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise OpsFileError(f"limits.{key} must be a positive whole number")
    words = data["words"]
    if not isinstance(words, dict) or set(words) != {"limit", "notes"}:
        raise OpsFileError("words must hold exactly limit and notes")
    notes = _section(words, "notes", NOTE_KEYS)
    for text in (words["limit"], *notes.values()):
        if not isinstance(text, str) or not text.strip():
            raise OpsFileError("every piece of wording must be a non-empty string")
    rates, packs = _tokens(data["tokens"])
    return DeeperOps(
        group_daily_ceiling=limits["group_daily_ceiling"],
        group_burst_multiplier=limits["group_burst_multiplier"], low_balance_at=limits["low_balance_at"], limit_text=words["limit"], notes=dict(notes), rates=rates, packs=packs,
    )
