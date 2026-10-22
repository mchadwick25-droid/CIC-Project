"""The monthly count of messages that got a safety check and no Representative
reply, per visitor and per network.

A message that is checked and not voiced costs a safety check and earns no
voice, so only a count can bound it. The count is kept as two scrambled values
in the meter's file, each in a rolling window that starts with the first
message counted and is deleted when the window ends, the way the free
allowance is. Nothing here names a session, a conversation or a person.
"""
from engine.deeper.meter import Meter


class MessageBound:
    def __init__(self, meter: Meter, per_visitor: int, per_network: int):
        if per_visitor < 1 or per_network < 1:
            raise ValueError("a limit must be at least 1")
        self._meter = meter
        self.per_visitor = per_visitor
        self.per_network = per_network

    def _keys(self, visitor: str, network: str) -> tuple[str, str]:
        return self._meter.free_key(f"unanswered-visitor:{visitor}"), self._meter.free_key(f"unanswered-network:{network}")

    def reached(self, visitor: str, network: str) -> bool:
        """True once either the visitor or the network has used its count this window."""
        vkey, nkey = self._keys(visitor, network)
        return self._meter.free_window_spent(vkey) >= self.per_visitor or self._meter.free_window_spent(nkey) >= self.per_network

    def count(self, visitor: str, network: str) -> None:
        vkey, nkey = self._keys(visitor, network)
        self._meter.free_window_spend(vkey, 1)
        self._meter.free_window_spend(nkey, 1)
