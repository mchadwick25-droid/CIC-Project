"""The free allowance: what a visitor may draw without a code.

A visitor's first draw starts a window (30 days in the operations file), and
the window holds a fixed number of tokens in the unit the meter counts. When
the window ends the next draw starts a new one: the refill rolls from a
visitor's own first use, not the calendar. What a visitor has drawn is kept in
the meter's file, so a restart or a deploy does not refill it. The row is keyed
by a salted hash of the visitor key, holds a day and a number, and is deleted
when its window ends.

A network has a window of its own, a few allowances wide, that every visitor
behind it draws from as well, so dropping the cookie does not draw a fresh
allowance. Its row is keyed the same way and deleted the same way.

Admission reserves a turn's amount before the turn and settles it after, as it
does against a code, so a turn the Facilitator answers alone, a failed voice
call and a failed stream draw nothing. A reservation in flight is held in
memory only; it is never spent until it settles.
"""
import threading

from engine.deeper.meter import Meter


class FreeReservation:
    __slots__ = ("key", "amount", "done", "network_key")

    def __init__(self, key: str, amount: int, network_key: str | None = None):
        self.key = key
        self.amount = amount
        self.network_key = network_key
        self.done = False


class FreeAllowance:
    """A visitor draws from its own window and, when the allowance has a
    network window, also from the window of the network it connects from. A
    draw must fit both. The network window is how many tokens all the
    visitors behind one network may draw together, so a script that drops its
    cookie draws from the same pool each time."""

    def __init__(self, meter: Meter, window_amount: int, network_window_amount: int | None = None):
        if window_amount < 1:
            raise ValueError("the free allowance must be at least 1")
        if network_window_amount is not None and network_window_amount < window_amount:
            raise ValueError("the network window cannot be smaller than one visitor's window")
        self.window_amount = window_amount
        self.network_window_amount = network_window_amount
        self._meter = meter
        self._held: dict[str, int] = {}
        self._lock = threading.Lock()

    def _network_key(self, network: str | None) -> str | None:
        if network is None or self.network_window_amount is None:
            return None
        return self._meter.free_key(f"network:{network}")

    def _room(self, key: str, size: int, share: float) -> int:
        """Caller holds the lock."""
        return max(0, int(size * share) - self._meter.free_window_spent(key) - self._held.get(key, 0))

    def remaining(self, visitor: str, network: str | None = None) -> int:
        key = self._meter.free_key(visitor)
        nkey = self._network_key(network)
        with self._lock:
            room = self._room(key, self.window_amount, 1.0)
            return room if nkey is None else min(room, self._room(nkey, self.network_window_amount, 1.0))

    def left(self, visitor: str, share: float = 1.0, network: str | None = None) -> int:
        """What the visitor may still draw under the share in force: the narrowed
        window less what is spent and held, and no more than the network window
        has left. Never below zero."""
        key = self._meter.free_key(visitor)
        nkey = self._network_key(network)
        with self._lock:
            room = self._room(key, self.window_amount, share)
            return room if nkey is None else min(room, self._room(nkey, self.network_window_amount, share))

    def reserve(self, visitor: str, amount: int, share: float = 1.0, network: str | None = None) -> FreeReservation | None:
        """Holds amount against the visitor's window and the network's, or None when it does not fit either.
        share narrows both windows: 0.5 lets a visitor draw half of each."""
        if amount < 1:
            raise ValueError("amount must be at least 1")
        if not 0 < share <= 1:
            raise ValueError("share must be above 0 and at most 1")
        key = self._meter.free_key(visitor)
        nkey = self._network_key(network)
        with self._lock:
            if self._room(key, self.window_amount, share) < amount:
                return None
            if nkey is not None and self._room(nkey, self.network_window_amount, share) < amount:
                return None
            self._held[key] = self._held.get(key, 0) + amount
            if nkey is not None:
                self._held[nkey] = self._held.get(nkey, 0) + amount
            return FreeReservation(key, amount, nkey)

    def settle(self, reservation: FreeReservation, ok: bool) -> None:
        """Spends the held amount when ok, gives it back when not."""
        with self._lock:
            if reservation.done:
                return
            reservation.done = True
            for key in (reservation.key, reservation.network_key):
                if key is None:
                    continue
                held = self._held.get(key, 0) - reservation.amount
                if held > 0:
                    self._held[key] = held
                else:
                    self._held.pop(key, None)
                if ok:
                    self._meter.free_window_spend(key, reservation.amount)
