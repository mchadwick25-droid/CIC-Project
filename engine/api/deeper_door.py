"""Works out the door's state from what the week really cost.

The week's cost comes from the usage log (the approved price tables, per model
and call kind) and the money that came in comes from the meter's funds. The
door's own arithmetic, in engine.deeper.door, takes only the two numbers.

A call that ran on a model with no approved price is counted at the dearest
approved price rather than left out, so an unpriced model can only make the
door narrower. If the state cannot be worked out, the last good state stands:
a fault never opens what had closed. Before the first good state the door is
open; the Console spending ceiling is the backstop for that moment.
"""
import logging
import time
from datetime import datetime, timedelta, timezone
from typing import Callable

from engine.deeper import door as door_module
from engine.deeper.door import DoorSettings, DoorState
from engine.m8 import price_tables
from engine.m8.cost import PriceTable, estimate_cost
from engine.m8.log_store import UsageLogStore
from engine.m8.usage import SYSTEM_SESSION_ID

logger = logging.getLogger("cic.deeper")

WINDOW_DAYS = 7
REFRESH_SECONDS = 60.0

_APPROVED = (
    price_tables.SONNET_4_5_PRICE_TABLE,
    price_tables.SONNET_5_5_PRICE_TABLE,
    price_tables.OPUS_5_5_PRICE_TABLE,
    price_tables.HAIKU_4_5_PRICE_TABLE,
)
DEAREST = PriceTable(
    input_per_token=max(t.input_per_token for t in _APPROVED),
    output_per_token=max(t.output_per_token for t in _APPROVED),
    cache_write_per_token=max(t.cache_write_per_token for t in _APPROVED),
    cache_read_per_token=max(t.cache_read_per_token for t in _APPROVED),
    source="the dearest approved price in each category, for a call whose model has no approved row",
)


def week_spend_usd(usage_store: UsageLogStore, now: datetime) -> float:
    """List-price cost of every participant call in the last seven days."""
    since = (now - timedelta(days=WINDOW_DAYS)).isoformat()
    total = 0.0
    for record in usage_store.read_since(since):
        if record.session_id == SYSTEM_SESSION_ID:
            continue
        table = price_tables.price_for_call(record.call_kind, record.model_id) or DEAREST
        estimate = estimate_cost(record.usage, table)
        total += estimate.dollars or 0.0
    return total


class DoorMonitor:
    """The door's current state, refreshed at most once a minute."""

    def __init__(
        self,
        settings: DoorSettings,
        usage_store: UsageLogStore,
        funds: Callable[[], dict[str, int]],
        *,
        clock: Callable[[], datetime] | None = None,
        monotonic: Callable[[], float] = time.monotonic,
        refresh_seconds: float = REFRESH_SECONDS,
    ):
        self._settings = settings
        self._usage_store = usage_store
        self._funds = funds
        self._clock = clock or (lambda: datetime.now(timezone.utc))
        self._monotonic = monotonic
        self._refresh = refresh_seconds
        self._state: DoorState = door_module.OPEN
        self._computed_at: float | None = None

    def state(self) -> DoorState:
        now = self._monotonic()
        if self._computed_at is not None and now - self._computed_at < self._refresh:
            return self._state
        try:
            spend = week_spend_usd(self._usage_store, self._clock())
            fresh = door_module.compute(self._settings, spend, self._funds())
        except Exception:  # noqa: BLE001 - a fault keeps the last state, never opens it
            logger.exception("door could not be worked out; the last state stands")
            self._computed_at = now
            return self._state
        if fresh.stage != self._state.stage:
            logger.warning("door moved from stage %d to stage %d (ratio %.2f)", self._state.stage, fresh.stage, fresh.ratio)
        self._state = fresh
        self._computed_at = now
        return fresh
