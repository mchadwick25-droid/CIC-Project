"""What a sitting is admitted to, as plain numbers.

A TurnGrant says how many completed units (voice turns in an interview,
rounds at a table) the sitting may hold, and whether the sitting is
Facilitator-only: the safety check runs and the Facilitator answers, with no
voice call. The default grant is the free allowance. Nothing here knows why a
grant is larger or smaller than the default.
"""
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class TurnGrant:
    cap: int
    facilitator_only: bool = False
    # Which close text a refused turn speaks. None is the default text; any
    # other value is a key into the Facilitator's close variants.
    close_variant: str | None = None


# completed units so far, whether today's allowance is spent -> the grant
GrantProvider = Callable[[int, bool], TurnGrant]


def free_grant(cap: int, daily_cap_reached: bool = False, close_variant: str | None = None) -> TurnGrant:
    return TurnGrant(cap=cap, facilitator_only=daily_cap_reached, close_variant=close_variant)


def resolve(provider: GrantProvider | None, *, completed: int, free_cap: int, daily_cap_reached: bool) -> TurnGrant:
    """The grant for this turn. A provider that fails leaves the free grant:
    admission never closes the free path."""
    if provider is None:
        return free_grant(free_cap, daily_cap_reached)
    try:
        return provider(completed, daily_cap_reached)
    except Exception:  # noqa: BLE001 - a fault in admission must not stop a conversation
        return free_grant(free_cap, daily_cap_reached)
