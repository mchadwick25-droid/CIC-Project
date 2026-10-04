"""The Go Deeper operations file: the numbers and participant wording that
change over time, kept in one place and changed by pull request. The module
and the conversation engine hold none of them; the HTTP edge reads the file
at startup, refuses to start on a bad one, and hands each part to whoever
needs it as plain data."""
import os
from dataclasses import dataclass

import yaml

from engine.deeper.door import DoorSettings, Stage
from engine.deeper.tokens import Pack, TokenRates

OPS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "deeper", "ops", "go-deeper.yaml")
DOOR_WORD_KEYS = ("limited", "paused", "code_still_works")
NOTE_KEYS = ("no_code", "code_not_accepted", "spent", "too_few", "daily_ceiling", "paused", "in_use")
SOLO_KEYS = ("open", "round", "round_from_fourth")
TABLE_KEYS = ("open_per_seat", "round_two_seats", "round_three_seats", "round_two_seats_from_fourth", "round_three_seats_from_fourth")
FREE_KEYS = ("window_tokens", "window_days", "rounds_per_conversation")
LATER_ROUNDS_FROM = 4
MINIMUM_PACK_USD = 7
LIMIT_KEYS = ("group_daily_ceiling", "group_burst_multiplier", "low_balance_at")
DOOR_KEYS = ("observe", "base_weekly_usd", "gift_share", "purchase_share", "invoice_factor", "stages")
PAID_KEYS = ("round_cap", "provisional")
ADMIN_KEYS = ("mint_max_tokens_per_request", "mint_max_tokens_per_day")
STAGE_KEYS = {"at", "table_free_rounds", "solo_free_rounds", "free_share", "free_voice", "paid_voice"}


class OpsFileError(Exception):
    """The operations file is missing, malformed or incomplete."""


@dataclass(frozen=True)
class DeeperOps:
    group_daily_ceiling: int
    group_burst_multiplier: int
    low_balance_at: int
    limit_text: str
    notes: dict
    door_words: dict
    rates: TokenRates
    packs: tuple[Pack, ...]
    door: DoorSettings
    door_observe: bool
    paid_round_cap: int
    paid_round_cap_provisional: bool
    admin_mint_max_tokens_per_request: int
    admin_mint_max_tokens_per_day: int


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
        later_rounds_from=LATER_ROUNDS_FROM, free_window=free["window_tokens"], free_window_days=free["window_days"], free_rounds=free["rounds_per_conversation"],
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


def _number(value, name: str, *, low: float, high: float | None = None, inclusive_low: bool = True) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise OpsFileError(f"{name} must be a number")
    if value < low or (not inclusive_low and value == low) or (high is not None and value > high):
        raise OpsFileError(f"{name} is out of range")
    return float(value)


def _door(section) -> DoorSettings:
    section = _section({"door": section}, "door", DOOR_KEYS)
    if not isinstance(section["observe"], bool):
        raise OpsFileError("door.observe must be true or false")
    base = _number(section["base_weekly_usd"], "door.base_weekly_usd", low=0, inclusive_low=False)
    gift = _number(section["gift_share"], "door.gift_share", low=0, high=1)
    purchase = _number(section["purchase_share"], "door.purchase_share", low=0, high=1)
    factor = _number(section["invoice_factor"], "door.invoice_factor", low=1)
    raw = section["stages"]
    if not isinstance(raw, list) or not raw:
        raise OpsFileError("door.stages must list at least one stage")
    stages = []
    previous_at = 0.0
    narrowest = {"table_free_rounds": None, "solo_free_rounds": None, "free_share": None}
    free_closed = False
    for item in raw:
        if not isinstance(item, dict) or "at" not in item or not set(item) <= STAGE_KEYS:
            raise OpsFileError(f"each door stage holds an 'at' and only {sorted(STAGE_KEYS - {'at'})}")
        at = _number(item["at"], "door stage at", low=0, inclusive_low=False)
        if at <= previous_at:
            raise OpsFileError("door stages must rise strictly")
        previous_at = at
        fields: dict = {"at": at}
        for key in ("table_free_rounds", "solo_free_rounds"):
            if key in item:
                value = item[key]
                if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                    raise OpsFileError(f"door stage {key} must be a whole number, 0 or more")
                if narrowest[key] is not None and value > narrowest[key]:
                    raise OpsFileError(f"door stages may only narrow: {key} cannot rise")
                narrowest[key] = value
                fields[key] = value
        if "free_share" in item:
            share = _number(item["free_share"], "door stage free_share", low=0, high=1, inclusive_low=False)
            if narrowest["free_share"] is not None and share > narrowest["free_share"]:
                raise OpsFileError("door stages may only narrow: free_share cannot rise")
            narrowest["free_share"] = share
            fields["free_share"] = share
        for key in ("free_voice", "paid_voice"):
            if key in item:
                if item[key] is not False:
                    raise OpsFileError(f"door stage {key} may only be false: a stage never opens what an earlier one closed")
                fields[key] = False
        if item.get("free_voice") is False:
            free_closed = True
        if item.get("paid_voice") is False and not free_closed:
            raise OpsFileError("paid voice cannot close before free voice does")
        stages.append(Stage(**fields))
    return DoorSettings(base_usd=base, gift_share=gift, purchase_share=purchase, invoice_factor=factor, stages=tuple(stages))


def load_ops(path: str | None = None) -> DeeperOps:
    path = path or os.environ.get("CIC_DEEPER_OPS_FILE") or OPS_PATH
    try:
        with open(path, encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        raise OpsFileError(f"cannot read {path}: {exc}") from exc
    if not isinstance(data, dict) or set(data) != {"limits", "tokens", "door", "paid", "admin", "words"}:
        raise OpsFileError("the file must hold exactly limits, tokens, door, paid, admin and words")
    limits = _section(data, "limits", LIMIT_KEYS)
    for key, value in limits.items():
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise OpsFileError(f"limits.{key} must be a positive whole number")
    words = data["words"]
    if not isinstance(words, dict) or set(words) != {"limit", "notes", "door"}:
        raise OpsFileError("words must hold exactly limit, notes and door")
    notes = _section(words, "notes", NOTE_KEYS)
    door_words = _section(words, "door", DOOR_WORD_KEYS)
    for text in (words["limit"], *notes.values(), *door_words.values()):
        if not isinstance(text, str) or not text.strip():
            raise OpsFileError("every piece of wording must be a non-empty string")
    rates, packs = _tokens(data["tokens"])
    door = _door(data["door"])
    paid = _section(data, "paid", PAID_KEYS)
    if isinstance(paid["round_cap"], bool) or not isinstance(paid["round_cap"], int) or paid["round_cap"] <= 0:
        raise OpsFileError("paid.round_cap must be a positive whole number")
    if not isinstance(paid["provisional"], bool):
        raise OpsFileError("paid.provisional must be true or false")
    admin = _section(data, "admin", ADMIN_KEYS)
    for key, value in admin.items():
        _whole(value, f"admin.{key}")
    if admin["mint_max_tokens_per_request"] > admin["mint_max_tokens_per_day"]:
        raise OpsFileError("admin.mint_max_tokens_per_request cannot exceed admin.mint_max_tokens_per_day")
    return DeeperOps(
        group_daily_ceiling=limits["group_daily_ceiling"],
        group_burst_multiplier=limits["group_burst_multiplier"], low_balance_at=limits["low_balance_at"], limit_text=words["limit"], notes=dict(notes), door_words=dict(door_words), rates=rates, packs=packs, door=door,
        door_observe=data["door"]["observe"], paid_round_cap=paid["round_cap"], paid_round_cap_provisional=paid["provisional"],
        admin_mint_max_tokens_per_request=admin["mint_max_tokens_per_request"], admin_mint_max_tokens_per_day=admin["mint_max_tokens_per_day"],
    )
