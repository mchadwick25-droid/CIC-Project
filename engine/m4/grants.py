"""What a sitting is admitted to, as plain numbers.

A TurnGrant says how many completed units (voice turns in an interview,
rounds at a table) the sitting may hold. The default grant is the free
allowance. Nothing here knows why a
grant is larger or smaller than the default.
"""
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class TurnGrant:
    cap: int
    # Words the Facilitator speaks when this grant refuses a turn. When set,
    # the refusal is a pause, not an ending: the sitting stays open and a
    # later turn may be granted. None keeps the default close.
    limit_text: str | None = None


# completed units so far -> the grant
GrantProvider = Callable[[int], TurnGrant]


def free_grant(cap: int, limit_text: str | None = None) -> TurnGrant:
    return TurnGrant(cap=cap, limit_text=limit_text)


def resolve(provider: GrantProvider | None, *, completed: int, free_cap: int) -> TurnGrant:
    """The grant for this turn. A provider that fails leaves the free grant:
    admission never closes the free path."""
    if provider is None:
        return free_grant(free_cap)
    try:
        return provider(completed)
    except Exception:  # noqa: BLE001 - a fault in admission must not stop a conversation
        return free_grant(free_cap)
