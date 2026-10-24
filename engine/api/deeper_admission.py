"""Turns the code on a request into the numbers the engine reads.

The engine is handed a TurnGrant (a cap and the words for a pause) and never
learns why. What a turn draws comes from the round it is and the seats at the
table (engine.deeper.tokens). The free allowance, a window of tokens a visitor
draws from over thirty days, together with the network it connects from, covers a conversation's first rounds;
a valid code buys what it would refuse: a round past the free rounds, or any turn once the free
allowance is spent. The Facilitator is outside all of it: every refusal here is a grant the engine answers with the Facilitator.
Admission reserves a turn's amount before the turn and settles it after it, so
nothing is spent for a turn that was answered by the Facilitator alone, and
nothing is left held when a turn fails.

MessageBoundCheck is the monthly bound on messages that get a safety check and
no Representative reply. Past it a message is answered with a fixed line and no
model call; a code with tokens left is outside it.

A signed-in person draws the free allowance from their account's window instead of the
browser's (and still within the network's), and a code the account holds pays like a code on
the request; free is drawn before any code. Signed out, nothing changes.

Any fault here leaves the free grant. Admission never closes the free path.
"""
import logging
from typing import Callable

from fastapi import Request, Response

from engine.api.account_admission import AccountContext, account_context
from engine.api.deeper_routes import DeeperRuntime
from engine.api.ratelimit import bound_network_of, client_ip, network_of
from engine.deeper import codes, tokens
from engine.m4.grants import TurnGrant, free_grant

logger = logging.getLogger("cic.deeper")

CODE_HEADER = "x-cic-code"
REMAINING_HEADER = "X-Cic-Remaining"
LOW_HEADER = "X-Cic-Low"
FREE_LEFT_HEADER = "X-Cic-Free-Left"


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


def visitor_key(request: Request) -> str:
    """The key the free allowance and the monthly bound count a visitor under: the
    visitor cookie's id, or the address when the request carries none."""
    return getattr(request.state, "visitor_id", None) or f"ip:{network_of(client_ip(request))}"


def install_free_read(app, runtime: DeeperRuntime) -> None:
    """GET /api/deeper/free: what a visitor with no code may still draw from the free
    window, the number a reply reports in X-Cic-Free-Left. Read only; no model call."""

    @app.get("/api/deeper/free")
    def free_left(request: Request, response: Response):
        response.headers["Cache-Control"] = "no-store"
        left = runtime.free.left(visitor_key(request), bound_network_of(client_ip(request)))
        return {"free_left": left}


def code_holds_tokens(runtime: DeeperRuntime, request: Request) -> bool:
    """Whether the code on the request is live with tokens left and codes are not paused.
    Such a request is bounded by its own tokens and is outside the monthly bound."""
    info = _status(runtime, request)
    try:
        if runtime.meter.is_paused():
            return False
        if info is not None and info.status == "live" and info.remaining > 0:
            return True
        context = account_context(request, runtime)
        for code_hash in context.code_hashes if context is not None else ():
            held = runtime.meter.status_of_hash(code_hash)
            if held is not None and held.status == "live" and held.remaining > 0:
                return True
        return False
    except Exception:  # noqa: BLE001
        return False


class MessageBoundCheck:
    """One request's place in the monthly bound on messages that get a safety check
    and no Representative reply. Build it before the message is handled. .reached
    says the message is past the bound and gets the fixed line with no model call;
    .count records a message that was checked and not voiced. A fault in either
    leaves the safety check running and counts nothing."""

    def __init__(self, runtime: DeeperRuntime | None, request: Request):
        self._bound = runtime.bound if runtime is not None else None
        self._visitor = visitor_key(request)
        self._network = bound_network_of(client_ip(request))
        self.exempt = False
        if self._bound is not None:
            try:
                self.exempt = code_holds_tokens(runtime, request)
            except Exception:  # noqa: BLE001
                logger.exception("deeper bound could not read the code")

    @property
    def active(self) -> bool:
        return self._bound is not None and not self.exempt

    @property
    def reached(self) -> bool:
        if not self.active:
            return False
        try:
            return self._bound.reached(self._visitor, self._network)
        except Exception:  # noqa: BLE001 - a fault leaves the safety check running
            logger.exception("deeper bound could not be read")
            return False

    def count(self) -> None:
        if not self.active:
            return
        try:
            self._bound.count(self._visitor, self._network)
        except Exception:  # noqa: BLE001
            logger.exception("deeper bound could not count a message")


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

    def __init__(self, runtime: DeeperRuntime, code: str | None, *, free_cap: int, seats: int, visitor: str,
                 network: str | None = None, account: AccountContext | None = None):
        self._runtime = runtime
        self._code = code
        self._account = account
        self._free_cap = free_cap
        self._seats = seats
        self._visitor = visitor
        self._network = network
        self._free_reservation = None
        self._reservation = None
        self._note_key: str | None = None
        self._refusal: str | None = None
        self.remaining: int | None = None
        self.free_left: int | None = None

    def _limit_text(self) -> str | None:
        return self._runtime.ops.limit_text if self._runtime.ops is not None else None

    def provider(self, completed: int) -> TurnGrant:
        try:
            return self._decide(completed)
        except Exception:  # noqa: BLE001 - a fault leaves the free grant
            logger.exception("deeper admission faulted; the free grant stands")
            return free_grant(self._free_cap)

    def _holds_codes(self) -> bool:
        return self._account is not None and bool(self._account.code_hashes)

    def _reserve_paid(self, cost: int):
        """A code on the request pays as it always has. With none, the account's own codes are
        tried in turn and the first that can carry the turn does; if none can, the reason
        given is the one nearest to success, so the participant is told the most useful thing."""
        meter = self._runtime.meter
        if self._code:
            return meter.reserve(self._code, cost)
        order = ("paused", "daily_ceiling", "in_use", "insufficient", "spent", "void", "unknown")
        failures = []
        for code_hash in self._account.code_hashes:
            admission = meter.reserve_hash(code_hash, cost)
            if admission.ok:
                return admission
            failures.append(admission)
        return min(failures, key=lambda a: order.index(a.reason) if a.reason in order else len(order))

    def _account_remaining(self) -> int | None:
        """What the account's codes hold together, or None when it holds none."""
        if not self._holds_codes():
            return None
        meter = self._runtime.meter
        total = 0
        for code_hash in self._account.code_hashes:
            info = meter.status_of_hash(code_hash)
            if info is not None and info.status != "void":
                total += info.remaining
        return total

    def _decide(self, completed: int) -> TurnGrant:
        rates = self._runtime.token_rates
        cost = tokens.charge(rates, completed + 1, self._seats)
        free_rounds = self._free_cap
        free_open = completed < free_rounds
        if free_open:
            if self._account is not None:
                held = self._runtime.free.account_reserve(
                    self._account.account_id, self._account.refill_day, cost, self._network
                )
            else:
                held = self._runtime.free.reserve(self._visitor, cost, self._network)
            if held is not None:
                self._free_reservation = held
                return TurnGrant(cap=completed + 1)
        # Past the free rounds, or the free allowance cannot cover this turn: the grant
        # that refuses has a cap no higher than the turns already done.
        refusal_cap = min(self._free_cap, completed)
        cap = self._runtime.paid_round_cap
        has_paid = bool(self._code) or self._holds_codes()
        if has_paid and cap is not None and completed >= cap:
            self._refusal = "paid_round_cap"
            return free_grant(refusal_cap, self._limit_text())
        if has_paid:
            admission = self._reserve_paid(cost)
            if admission.ok:
                self._reservation = admission.reservation
                return TurnGrant(cap=completed + 1)
            self._note_key = _NOTE_FOR_REASON.get(admission.reason, "code_not_accepted")
            self._refusal = self._note_key
            return free_grant(refusal_cap, self._limit_text())
        self._note_key = "no_code"
        if completed >= free_rounds:
            self._refusal = "free_rounds_done"
        else:
            self._refusal = "free_allowance_spent"
        return free_grant(refusal_cap, self._limit_text())

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
            if self._code is None and self._account is not None:
                self.remaining = self._account_remaining()
            if self._code is None:
                if self._account is not None:
                    self.free_left = self._runtime.free.account_left(
                        self._account.account_id, self._account.refill_day, self._network
                    )
                else:
                    self.free_left = self._runtime.free.left(self._visitor, self._network)
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


def new_admission(runtime: DeeperRuntime | None, request: Request, *, free_cap: int, seats: int = 1) -> Admission | None:
    if runtime is None:
        return None
    return Admission(
        runtime, code_from(request), free_cap=free_cap,
        seats=seats, visitor=visitor_key(request),
        network=bound_network_of(client_ip(request)),
        account=account_context(request, runtime),
    )
