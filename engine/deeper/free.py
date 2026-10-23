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

A signed-in person draws from an account window instead: the same number of
tokens, refilling on the account's own day of the month, never accumulating, and
begun with what the person's browser had already drawn so signing up is not a
second allowance. The account's row is keyed by a salted hash of the account id
under the meter's own secret, never by the id. A signed-in draw must also fit
the network's window, so many accounts behind one network share it. The
browser's own window is not drawn from.

Admission reserves a turn's amount before the turn and settles it after, as it
does against a code, so a turn the Facilitator answers alone, a failed voice
call and a failed stream draw nothing. A reservation in flight is held in
memory only; it is never spent until it settles.
"""
import threading

from engine.deeper.meter import Meter


class FreeReservation:
    __slots__ = ("key", "amount", "done", "network_key", "refill_day", "window_start")

    def __init__(self, key: str, amount: int, network_key: str | None = None, refill_day: int | None = None,
                 window_start=None):
        self.key = key
        self.amount = amount
        self.network_key = network_key
        self.refill_day = refill_day
        self.window_start = window_start
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

    def _room(self, key: str, size: int) -> int:
        """Caller holds the lock."""
        return max(0, size - self._meter.free_window_spent(key) - self._held.get(key, 0))

    def account_key(self, account_id: str) -> str:
        return self._meter.free_key(f"account:{account_id}")

    def _account_room(self, key: str, refill_day: int) -> int:
        """Caller holds the lock."""
        spent = self._meter.account_window_spent(key, refill_day)
        return max(0, self.window_amount - spent - self._held.get(key, 0))

    def account_left(self, account_id: str, refill_day: int, network: str | None = None) -> int:
        """What the account may still draw this window, and no more than the network window has left."""
        key = self.account_key(account_id)
        nkey = self._network_key(network)
        with self._lock:
            room = self._account_room(key, refill_day)
            return room if nkey is None else min(room, self._room(nkey, self.network_window_amount))

    def account_reserve(self, account_id: str, refill_day: int, amount: int,
                        network: str | None = None) -> FreeReservation | None:
        """Holds amount against the account's window and the network's, or None when it does not fit either."""
        if amount < 1:
            raise ValueError("amount must be at least 1")
        key = self.account_key(account_id)
        nkey = self._network_key(network)
        with self._lock:
            if self._account_room(key, refill_day) < amount:
                return None
            if nkey is not None and self._room(nkey, self.network_window_amount) < amount:
                return None
            self._held[key] = self._held.get(key, 0) + amount
            if nkey is not None:
                self._held[nkey] = self._held.get(nkey, 0) + amount
            return FreeReservation(key, amount, nkey, refill_day, self._meter.account_window_start(refill_day))

    def seed_account(self, account_id: str, refill_day: int, visitor: str) -> None:
        """A new account starts with what is left of its browser's window: what the browser
        had drawn is entered as spent in the account's first window."""
        drawn = min(self.window_amount, self._meter.free_window_spent(self._meter.free_key(visitor)))
        self._meter.account_window_seed(self.account_key(account_id), refill_day, drawn)

    def remaining(self, visitor: str, network: str | None = None) -> int:
        key = self._meter.free_key(visitor)
        nkey = self._network_key(network)
        with self._lock:
            room = self._room(key, self.window_amount)
            return room if nkey is None else min(room, self._room(nkey, self.network_window_amount))

    def left(self, visitor: str, network: str | None = None) -> int:
        """What the visitor may still draw: the window less what is spent and held, and no more
        than the network window has left. Never below zero."""
        key = self._meter.free_key(visitor)
        nkey = self._network_key(network)
        with self._lock:
            room = self._room(key, self.window_amount)
            return room if nkey is None else min(room, self._room(nkey, self.network_window_amount))

    def reserve(self, visitor: str, amount: int, network: str | None = None) -> FreeReservation | None:
        """Holds amount against the visitor's window and the network's, or None when it does not fit either."""
        if amount < 1:
            raise ValueError("amount must be at least 1")
        key = self._meter.free_key(visitor)
        nkey = self._network_key(network)
        with self._lock:
            if self._room(key, self.window_amount) < amount:
                return None
            if nkey is not None and self._room(nkey, self.network_window_amount) < amount:
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
                    if key == reservation.key and reservation.refill_day is not None:
                        self._meter.account_window_spend(key, reservation.refill_day, reservation.amount, reservation.window_start)
                    else:
                        self._meter.free_window_spend(key, reservation.amount)
