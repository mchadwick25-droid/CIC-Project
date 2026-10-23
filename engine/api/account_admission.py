"""A signed-in request, as the admission seam reads it.

The account module never learns worlds, records or the meter's codes, and the
meter never learns accounts. This edge module joins them for one purpose: the
account id and refill day that name the account's free window, and the meter
codes the account holds. The account keeps each code only as a keyed scramble
of its hash; here the meter's live codes are scrambled the same way, and an
in-memory index matches them. The index is a cache: a code missing from it is
not used until it is added or the index is rebuilt, never wrongly used.
"""
import logging
import threading
import time
from dataclasses import dataclass, field

from engine.deeper import codes

logger = logging.getLogger("cic.deeper")

REFRESH_SECONDS = 60


@dataclass
class AccountContext:
    account_id: str
    refill_day: int
    code_hashes: list[str] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)  # held links that name no live code


class CodeIndex:
    """Meter code hash by scramble, for every live code under every live address key."""

    def __init__(self, meter, keys, clock=time.monotonic):
        self._meter = meter
        self._keys = keys
        self._clock = clock
        self._lock = threading.Lock()
        self._by_scramble: dict[str, str] = {}
        self._generation = None
        self._built_at = 0.0

    def _rebuild(self) -> None:
        generation = self._meter.code_generation()
        index: dict[str, str] = {}
        for code_hash in self._meter.live_code_hashes():
            for scramble in self._keys.secret_candidates("code", code_hash):
                index[scramble] = code_hash
        self._by_scramble, self._generation, self._built_at = index, generation, self._clock()

    def add(self, code_hash: str) -> None:
        """A code just attached or minted is usable at once."""
        with self._lock:
            for scramble in self._keys.secret_candidates("code", code_hash):
                self._by_scramble[scramble] = code_hash

    def resolve(self, scrambles: list[str]) -> list[tuple[str, str]]:
        """(stored scramble, meter hash) for each held link that names a live code."""
        if not scrambles:
            return []
        with self._lock:
            if self._clock() - self._built_at > REFRESH_SECONDS or self._generation != self._meter.code_generation():
                self._rebuild()
            return [(s, self._by_scramble[s]) for s in scrambles if s in self._by_scramble]


def _move_to_current_key(service, account_id: str, found: list[tuple[str, str]]) -> None:
    """A held code found under an older address key is kept under the current one from now on,
    as an address is re-keyed at its owner's next sign-in. Best effort; a fault changes nothing."""
    try:
        for stored, code_hash in found:
            current = service.keys.secret_hash("code", code_hash)
            if stored != current:
                service.rescramble_code(account_id, stored, current)
    except Exception:  # noqa: BLE001
        logger.exception("a held code could not be moved to the current key")


def real_code_hash(raw, runtime) -> str | None:
    """The meter hash of a typed code that exists and is not void, else None. A code is checked
    here once, at the edge; the account keeps only a keyed scramble of the hash."""
    code = codes.normalize(raw)
    if code is None or runtime is None:
        return None
    code_hash = codes.hash_code(code)
    info = runtime.meter.status_of_hash(code_hash)
    live = info is not None and info.status == "live" and info.remaining > 0 and info.kind != "group"
    return code_hash if live else None


def code_index(request, runtime) -> CodeIndex | None:
    accounts = getattr(request.app.state, "accounts", None)
    if accounts is None or runtime is None:
        return None
    index = getattr(request.app.state, "account_code_index", None)
    if index is None:
        index = CodeIndex(runtime.meter, accounts.service.keys)
        request.app.state.account_code_index = index
    return index


def account_context(request, runtime) -> AccountContext | None:
    """The signed-in account behind a request, or None for a visitor. A fault leaves the
    visitor path, which is the free grant: admission never closes it."""
    cached = getattr(request.state, "account_context", _UNSET)
    if cached is not _UNSET:
        return cached
    context = _read_context(request, runtime)
    request.state.account_context = context
    return context


_UNSET = object()


def _read_context(request, runtime) -> AccountContext | None:
    accounts = getattr(request.app.state, "accounts", None)
    cookie = request.cookies.get(accounts.cookie_name) if accounts is not None else None
    if not cookie:
        return None
    try:
        held = accounts.service.admission_context(cookie)
        if held is None:
            return None
        index = code_index(request, runtime)
        found = index.resolve(held["scrambles"]) if index else []
        context = AccountContext(held["account_id"], held["refill_day"], [h for _, h in found])
        resolved = {s for s, _ in found}
        context.unresolved = [s for s in held["scrambles"] if s not in resolved]
        if index is not None:
            _move_to_current_key(accounts.service, held["account_id"], found)
        return context
    except Exception:  # noqa: BLE001 - admission must not break the free path
        logger.exception("deeper admission could not read the account")
        return None
