"""Turns the code on a request into the numbers the engine reads.

The engine is handed a TurnGrant (a cap and a Facilitator-only flag) and never
learns why. What a turn draws comes from the round it is and the seats at the
table (engine.deeper.tokens). The free allowance covers a conversation's first
rounds while the visitor's free day lasts, narrowed by the door's stage when
the week's real spend nears its ceiling; a valid code buys what it would
refuse: a round past the free rounds, or any turn once the free day is spent.
At the door's last stage a code is refused too. The Facilitator is outside all
of it: every refusal here is a grant the engine answers with the Facilitator.
Admission reserves a turn's amount before the turn and settles it after it, so
nothing is spent for a turn that was answered by the Facilitator alone, and
nothing is left held when a turn fails.

Any fault here leaves the free grant. Admission never closes the free path.
"""
import logging
from typing import Callable

from fastapi import Request

from engine.api.deeper_routes import DeeperRuntime
from engine.api.ratelimit import client_ip
from engine.deeper import codes, tokens
from engine.deeper import door as door_module
from engine.m4.grants import TurnGrant, free_grant

logger = logging.getLogger("cic.deeper")

CODE_HEADER = "x-cic-code"
REMAINING_HEADER = "X-Cic-Remaining"
LOW_HEADER = "X-Cic-Low"


def code_from(request: Request) -> str | None:
    return request.headers.get(CODE_HEADER)


def _status(runtime: DeeperRuntime, request: Request):
    """The request's code status, looked up once per request."""
    cached = getattr(request.state, "deeper_status", _UNSET)
    if cached is not _UNSET:
        return cached
    try:
        info = runtime.meter.status(code_from(request))
    except Exception:  # noqa: BLE001 - admission must not break the free path
        info = None
    request.state.deeper_status = info
    return info


_UNSET = object()


def code_is_usable(runtime: DeeperRuntime, request: Request, *, strict: bool = True) -> bool:
    """Whether the code on the request vouches for it. Strict, for opening a
    sitting past the daily session limit: a live code with tokens left and
    codes not paused. Loose, for continuing a round already admitted: any code
    that is not void."""
    info = _status(runtime, request)
    if info is None or info.status == "void":
        return False
    if not strict:
        return True
    try:
        paused = runtime.meter.is_paused()
    except Exception:  # noqa: BLE001
        return False
    return info.status == "live" and info.remaining > 0 and not paused


def burst_key(runtime: DeeperRuntime, request: Request) -> tuple[str, int] | None:
    """The rate-limit bucket for a request carrying a usable code: its own
    bucket, larger for a pooled group code. None leaves the address bucket."""
    raw = code_from(request)
    if not raw:
        return None
    info = _status(runtime, request)
    if info is None or info.status == "void":
        return None
    normal = codes.normalize(raw)
    scale = runtime.group_burst_multiplier if info.kind == "group" else 1
    return f"code:{codes.hash_code(normal)[:16]}", scale


# why a held code could not carry the turn -> which line of the operations
# file the participant is shown (in the response only, never stored)
_NOTE_FOR_REASON = {
    "spent": "spent",
    "insufficient": "too_few",
    "daily_ceiling": "daily_ceiling",
    "in_use": "in_use",
    "paused": "paused",
}


class Admission:
    """One request's admission. Build it, hand .provider to the engine, and
    call .finish(voiced) exactly once when the turn is over."""

    def __init__(self, runtime: DeeperRuntime, code: str | None, *, session_id: str, free_cap: int, seats: int, visitor: str):
        self._runtime = runtime
        self._code = code
        self._free_cap = free_cap
        self._seats = seats
        self._visitor = visitor
        self._free_reservation = None
        self._facilitator_only = session_id in runtime.facilitator_only_sessions
        self._paid_sitting = session_id in runtime.paid_sessions
        self._reservation = None
        self._note_key: str | None = None
        self._refusal: str | None = None
        self.remaining: int | None = None

    def _limit_text(self) -> str | None:
        return self._runtime.ops.limit_text if self._runtime.ops is not None else None

    def provider(self, completed: int, daily_cap_reached: bool) -> TurnGrant:
        limited = daily_cap_reached or self._facilitator_only or self._paid_sitting
        door = self._runtime.door.state() if self._runtime.door is not None else door_module.OPEN
        try:
            return self._decide(completed, limited, door)
        except Exception:  # noqa: BLE001 - a fault must never open what the door has closed
            logger.exception("deeper admission faulted; the grant keeps to the door")
            return self._grant_in_a_fault(completed, limited, door)

    def _door_rounds(self, door: door_module.DoorState) -> int | None:
        return door.table_free_rounds if self._seats > 1 else door.solo_free_rounds

    def _grant_in_a_fault(self, completed: int, limited: bool, door: door_module.DoorState) -> TurnGrant:
        """What the engine is handed when admission itself fails. With the door
        closed to free voice (paid voice never closes first) it is a refusal; with
        it open the free grant, no longer than the door lets a free conversation run."""
        if not door.free_voice:
            return free_grant(min(self._free_cap, completed), limited, self._limit_text())
        door_rounds = self._door_rounds(door)
        cap = min(self._free_cap, self._runtime.token_rates.free_rounds)
        if door_rounds is not None:
            cap = min(cap, door_rounds)
        return free_grant(cap, limited)

    def _decide(self, completed: int, limited: bool, door: door_module.DoorState) -> TurnGrant:
        rates = self._runtime.token_rates
        cost = tokens.charge(rates, completed + 1, self._seats)
        free_rounds = min(self._free_cap, rates.free_rounds)
        door_rounds = self._door_rounds(door)
        if door_rounds is not None:
            free_rounds = min(free_rounds, door_rounds)
        free_open = not limited and door.free_voice and completed < free_rounds
        if free_open:
            held = self._runtime.free.reserve(self._visitor, cost, door.free_day_share)
            if held is not None:
                self._free_reservation = held
                return TurnGrant(cap=completed + 1, facilitator_only=False)
        # Past the free rounds, or the free day cannot cover this turn: the grant
        # that refuses has a cap no higher than the turns already done.
        refusal_cap = min(self._free_cap, completed)
        if self._code and not door.paid_voice:
            self._note_key = "paused"
            self._refusal = "door_paid_closed"
            return free_grant(refusal_cap, limited, self._limit_text())
        if self._code:
            admission = self._runtime.meter.reserve(self._code, cost)
            if admission.ok:
                self._reservation = admission.reservation
                return TurnGrant(cap=completed + 1, facilitator_only=False)
            self._note_key = _NOTE_FOR_REASON.get(admission.reason, "code_not_accepted")
            self._refusal = self._note_key
            return free_grant(refusal_cap, limited, self._limit_text())
        self._note_key = "no_code"
        if limited:
            self._refusal = "no_code"
        elif not door.free_voice:
            self._refusal = "door_free_closed"
        elif completed >= free_rounds:
            self._refusal = "free_rounds_done"
        else:
            self._refusal = "free_day_spent"
        return free_grant(refusal_cap, limited, self._limit_text())

    @property
    def low(self) -> bool:
        """True when the code in use is down to the operations file's low-balance
        number or less, so the app can offer more before it runs out."""
        ops = self._runtime.ops
        return ops is not None and self.remaining is not None and self.remaining <= ops.low_balance_at

    def limit_note(self, routing_action: str | None) -> dict | None:
        """The line explaining a refusal, for the response only. It names why
        the code could not carry the turn, in the operations file's words; the
        conversation store holds only the neutral limit text."""
        ops = self._runtime.ops
        if routing_action != "session_cap_turn" or self._note_key is None or ops is None:
            return None
        return {"key": self._note_key, "text": ops.notes[self._note_key]}

    def finish(self, voiced: bool) -> int | None:
        """Spends the held tokens when the turn was voiced, returns them
        otherwise, and reports what the code has left."""
        meter = self._runtime.meter
        try:
            if self._free_reservation is not None:
                self._runtime.free.settle(self._free_reservation, voiced)
                self._free_reservation = None
            if self._reservation is not None:
                meter.settle(self._reservation, voiced)
                self._reservation = None
            info = meter.status(self._code) if self._code else None
            self.remaining = info.remaining if info is not None and info.status != "void" else None
        except Exception:  # noqa: BLE001
            logger.exception("deeper settle failed")
        self._count_refusal()
        return self.remaining

    def _count_refusal(self) -> None:
        """Counts a refused turn once, after everything else has settled; a count that fails changes nothing."""
        reason, self._refusal = self._refusal, None
        if reason is None:
            return
        try:
            self._runtime.meter.measure(f"refused_{reason}")
        except Exception:  # noqa: BLE001
            logger.exception("deeper refusal could not be counted")


def new_admission(runtime: DeeperRuntime | None, request: Request, *, session_id: str, free_cap: int, seats: int = 1) -> Admission | None:
    if runtime is None:
        return None
    return Admission(
        runtime, code_from(request), session_id=session_id, free_cap=free_cap,
        seats=seats, visitor=getattr(request.state, "visitor_id", None) or f"ip:{client_ip(request)}",
    )
