"""The free allowance: what a visitor may draw without a code.

A visitor's first draw starts a window (30 days in the operations file), and
the window holds a fixed number of tokens in the unit the meter counts. When
the window ends the next draw starts a new one: the refill rolls from a
visitor's own first use, not the calendar. What a visitor has drawn is kept in
the meter's file, so a restart or a deploy does not refill it. The row is keyed
by a salted hash of the visitor key, holds a day and a number, and is deleted
when its window ends.

Admission reserves a turn's amount before the turn and settles it after, as it
does against a code, so a turn the Facilitator answers alone, a failed voice
call and a failed stream draw nothing. A reservation in flight is held in
memory only; it is never spent until it settles.
"""
import threading

from engine.deeper.meter import Meter


class FreeReservation:
    __slots__ = ("key", "amount", "done")

    def __init__(self, key: str, amount: int):
        self.key = key
        self.amount = amount
        self.done = False


class FreeAllowance:
    def __init__(self, meter: Meter, window_amount: int):
        if window_amount < 1:
            raise ValueError("the free allowance must be at least 1")
        self.window_amount = window_amount
        self._meter = meter
        self._held: dict[str, int] = {}
        self._lock = threading.Lock()

    def remaining(self, visitor: str) -> int:
        key = self._meter.free_key(visitor)
        with self._lock:
            return max(0, self.window_amount - self._meter.free_window_spent(key) - self._held.get(key, 0))

    def reserve(self, visitor: str, amount: int, share: float = 1.0) -> FreeReservation | None:
        """Holds amount against the visitor's window, or None when it does not fit.
        share narrows the window: 0.5 lets a visitor draw half of it."""
        if amount < 1:
            raise ValueError("amount must be at least 1")
        if not 0 < share <= 1:
            raise ValueError("share must be above 0 and at most 1")
        key = self._meter.free_key(visitor)
        with self._lock:
            if self._meter.free_window_spent(key) + self._held.get(key, 0) + amount > int(self.window_amount * share):
                return None
            self._held[key] = self._held.get(key, 0) + amount
            return FreeReservation(key, amount)

    def settle(self, reservation: FreeReservation, ok: bool) -> None:
        """Spends the held amount when ok, gives it back when not."""
        with self._lock:
            if reservation.done:
                return
            reservation.done = True
            held = self._held.get(reservation.key, 0) - reservation.amount
            if held > 0:
                self._held[reservation.key] = held
            else:
                self._held.pop(reservation.key, None)
            if ok:
                self._meter.free_window_spend(reservation.key, reservation.amount)
