"""Turns the code on a request into the numbers the engine reads.

The engine is handed a TurnGrant (a cap and a Facilitator-only flag) and never
learns why. Here a valid code buys what the free allowance would refuse: a
turn past the free cap, or any turn once today's allowance is spent. A turn the
free allowance admits never touches the meter. Admission reserves the
exchanges before the turn and settles them after it, so nothing is spent for a
turn that was answered by the Facilitator alone, and nothing is left held when
a turn fails.

Any fault here leaves the free grant. Admission never closes the free path.
"""
import logging
from typing import Callable

from fastapi import Request

from engine.api.deeper_routes import DeeperRuntime
from engine.deeper import codes
from engine.m4.grants import TurnGrant, free_grant

logger = logging.getLogger("cic.deeper")

CODE_HEADER = "x-cic-code"
REMAINING_HEADER = "X-Cic-Remaining"


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
    sitting past the daily session limit: a live code with exchanges left and
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

    def __init__(self, runtime: DeeperRuntime, code: str | None, *, session_id: str, free_cap: int, unit_cost: int):
        self._runtime = runtime
        self._code = code
        self._free_cap = free_cap
        self._unit_cost = unit_cost
        self._facilitator_only = session_id in runtime.facilitator_only_sessions
        self._paid_sitting = session_id in runtime.paid_sessions
        self._reservation = None
        self._note_key: str | None = None
        self.remaining: int | None = None

    def _limit_text(self) -> str | None:
        return self._runtime.ops.limit_text if self._runtime.ops is not None else None

    def provider(self, completed: int, daily_cap_reached: bool) -> TurnGrant:
        limited = daily_cap_reached or self._facilitator_only or self._paid_sitting
        beyond_free = limited or completed >= self._free_cap
        if self._code and beyond_free:
            admission = self._runtime.meter.reserve(self._code, self._unit_cost)
            if admission.ok:
                self._reservation = admission.reservation
                return TurnGrant(cap=completed + 1, facilitator_only=False)
            self._note_key = _NOTE_FOR_REASON.get(admission.reason, "code_not_accepted")
            return free_grant(self._free_cap, limited, self._limit_text())
        if beyond_free:
            self._note_key = "no_code"
            return free_grant(self._free_cap, limited, self._limit_text())
        return free_grant(self._free_cap, limited)

    def limit_note(self, routing_action: str | None) -> dict | None:
        """The line explaining a refusal, for the response only. It names why
        the code could not carry the turn, in the operations file's words; the
        conversation store holds only the neutral limit text."""
        ops = self._runtime.ops
        if routing_action != "session_cap_turn" or self._note_key is None or ops is None:
            return None
        return {"key": self._note_key, "text": ops.notes[self._note_key]}

    def finish(self, voiced: bool) -> int | None:
        """Spends the held exchanges when the turn was voiced, returns them
        otherwise, and reports what the code has left."""
        meter = self._runtime.meter
        try:
            if self._reservation is not None:
                meter.settle(self._reservation, voiced)
                self._reservation = None
            info = meter.status(self._code) if self._code else None
            self.remaining = info.remaining if info is not None and info.status != "void" else None
        except Exception:  # noqa: BLE001
            logger.exception("deeper settle failed")
        return self.remaining


def new_admission(runtime: DeeperRuntime | None, request: Request, *, session_id: str, free_cap: int, table: bool) -> Admission | None:
    if runtime is None:
        return None
    return Admission(
        runtime, code_from(request), session_id=session_id, free_cap=free_cap,
        unit_cost=runtime.table_round_cost if table else 1,
    )
