"""The Go Deeper operations file: the numbers and participant wording that
change over time, kept in one place and changed by pull request. The module
and the conversation engine hold none of them; the HTTP edge reads the file
at startup, refuses to start on a bad one, and hands each part to whoever
needs it as plain data."""
import os
from dataclasses import dataclass

import yaml

OPS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "deeper", "ops", "go-deeper.yaml")
NOTE_KEYS = ("no_code", "code_not_accepted", "spent", "too_few", "daily_ceiling", "paused", "in_use")
LIMIT_KEYS = ("group_daily_ceiling", "table_round_cost", "group_burst_multiplier")


class OpsFileError(Exception):
    """The operations file is missing, malformed or incomplete."""


@dataclass(frozen=True)
class DeeperOps:
    group_daily_ceiling: int
    table_round_cost: int
    group_burst_multiplier: int
    limit_text: str
    notes: dict


def _section(data: dict, name: str, keys: tuple[str, ...]) -> dict:
    section = data.get(name)
    if not isinstance(section, dict) or set(section) != set(keys):
        raise OpsFileError(f"{name} must hold exactly {sorted(keys)}")
    return section


def load_ops(path: str | None = None) -> DeeperOps:
    path = path or os.environ.get("CIC_DEEPER_OPS_FILE") or OPS_PATH
    try:
        with open(path, encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        raise OpsFileError(f"cannot read {path}: {exc}") from exc
    if not isinstance(data, dict) or set(data) != {"limits", "words"}:
        raise OpsFileError("the file must hold exactly limits and words")
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
    return DeeperOps(
        group_daily_ceiling=limits["group_daily_ceiling"], table_round_cost=limits["table_round_cost"],
        group_burst_multiplier=limits["group_burst_multiplier"], limit_text=words["limit"], notes=dict(notes),
    )
