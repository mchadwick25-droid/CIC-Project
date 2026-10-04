"""The free day: what a visitor may draw each day without a code.

One in-memory counter per visitor key and UTC day, in the same unit the meter
counts. Admission reserves a turn's amount before the turn and settles it
after, exactly as it does against a code, so a turn the Facilitator answers
alone, a failed voice call and a failed stream draw nothing. A restart resets
every visitor's day: this is a soft allowance, not a ledger, and it keeps no
record of who drew what beyond the day's running number.
"""
import threading
from datetime import date
from typing import Callable

MAX_VISITORS = 50_000


class FreeReservation:
    __slots__ = ("key", "day", "amount", "done")

    def __init__(self, key: str, day: str, amount: int):
        self.key = key
        self.day = day
        self.amount = amount
        self.done = False


class DailyFreeAllowance:
    def __init__(self, daily_amount: int, clock: Callable[[], date] | None = None):
        if daily_amount < 1:
            raise ValueError("the free day must be at least 1")
        self.daily_amount = daily_amount
        self._clock = clock or date.today
        self._used: dict[str, tuple[str, int]] = {}
        self._held: dict[str, int] = {}
        self._lock = threading.Lock()

    def _used_today(self, key: str, today: str) -> int:
        day, used = self._used.get(key, (today, 0))
        return used if day == today else 0

    def remaining(self, key: str) -> int:
        today = self._clock().isoformat()
        with self._lock:
            return max(0, self.daily_amount - self._used_today(key, today) - self._held.get(key, 0))

    def reserve(self, key: str, amount: int) -> FreeReservation | None:
        """Holds amount against today's allowance, or None when it does not fit."""
        if amount < 1:
            raise ValueError("amount must be at least 1")
        today = self._clock().isoformat()
        with self._lock:
            if self._used_today(key, today) + self._held.get(key, 0) + amount > self.daily_amount:
                return None
            self._held[key] = self._held.get(key, 0) + amount
            return FreeReservation(key, today, amount)

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
            if not ok:
                return
            used = self._used_today(reservation.key, reservation.day)
            self._used[reservation.key] = (reservation.day, used + reservation.amount)
            if len(self._used) > MAX_VISITORS:
                stale = [k for k, (day, _) in self._used.items() if day != reservation.day]
                for k in stale:
                    del self._used[k]
