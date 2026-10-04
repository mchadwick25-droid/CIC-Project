"""The door: a weekly spend limit that narrows the free path in stages.

Pure arithmetic over numbers handed in: the week's priced spend, and the money
that came in. It knows no model, no price table, no world and no conversation.
The ceiling is the base number plus a share of the week's gifts and
adjustments and a share of its purchases. As spend rises against the ceiling,
each stage whose threshold has been passed narrows what the free path may do;
stages only ever narrow, so a higher ratio never opens anything a lower one
closed. The Facilitator is never part of this: nothing here can close it.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    at: float
    table_free_rounds: int | None = None
    solo_free_rounds: int | None = None
    free_share: float | None = None
    free_voice: bool | None = None
    paid_voice: bool | None = None


@dataclass(frozen=True)
class DoorSettings:
    base_usd: float
    gift_share: float
    purchase_share: float
    invoice_factor: float
    stages: tuple[Stage, ...]


@dataclass(frozen=True)
class DoorState:
    """What the door allows right now. None means the free path's own number stands."""

    stage: int
    ratio: float
    ceiling_usd: float
    table_free_rounds: int | None = None
    solo_free_rounds: int | None = None
    free_share: float = 1.0
    free_voice: bool = True
    paid_voice: bool = True


OPEN = DoorState(stage=0, ratio=0.0, ceiling_usd=0.0)


def ceiling_usd(settings: DoorSettings, funds_cents: dict[str, int]) -> float:
    """The base number plus what the week's money adds to it. Money never lowers it below the base."""
    gifts = funds_cents.get("gift", 0) + funds_cents.get("adjustment", 0)
    purchases = funds_cents.get("purchase", 0)
    raised = (settings.gift_share * gifts + settings.purchase_share * purchases) / 100
    return settings.base_usd + max(0.0, raised)


def compute(settings: DoorSettings, list_price_spend_usd: float, funds_cents: dict[str, int]) -> DoorState:
    """The state for a week's list-price spend against its ceiling. The spend is
    multiplied by the invoice factor here, so the door counts what the bill will say."""
    ceiling = ceiling_usd(settings, funds_cents)
    ratio = (list_price_spend_usd * settings.invoice_factor) / ceiling
    state = DoorState(stage=0, ratio=ratio, ceiling_usd=ceiling)
    for index, stage in enumerate(settings.stages, start=1):
        if ratio < stage.at:
            break
        state = DoorState(
            stage=index,
            ratio=ratio,
            ceiling_usd=ceiling,
            table_free_rounds=state.table_free_rounds if stage.table_free_rounds is None else stage.table_free_rounds,
            solo_free_rounds=state.solo_free_rounds if stage.solo_free_rounds is None else stage.solo_free_rounds,
            free_share=state.free_share if stage.free_share is None else stage.free_share,
            free_voice=state.free_voice if stage.free_voice is None else stage.free_voice,
            paid_voice=state.paid_voice if stage.paid_voice is None else stage.paid_voice,
        )
    return state
