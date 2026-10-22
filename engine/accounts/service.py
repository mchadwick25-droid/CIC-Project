"""Sign-in, sessions, recovery, address change and deletion.

A person proves they control an address by typing a six-digit code sent to it.
The code is stored only as a keyed value bound to the address hash, works once,
dies after ten minutes, and is burned after five wrong tries. Nothing here logs
an address or a code. A reply never says whether an account exists until the
person has proved the address is theirs.

Everything time-based reads one injected clock, so tests set the time.
"""
import hmac
import ipaddress
import logging
import secrets
import time
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from hashlib import sha256
from typing import Callable, Protocol

from engine.accounts.keys import KeyRing, normalise_address
from engine.accounts.store import Account, AccountStore, Pending, SessionRow

logger = logging.getLogger("cic.accounts")

RECOVERY_ALPHABET = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
RECOVERY_LENGTH = 20
PURPOSES = ("sign_in", "step_up", "change", "recover")


class Mailer(Protocol):
    def send_code(self, address: str, code: str) -> None:
        """Sends one sign-in code. The address is used for this send and nowhere else."""


@dataclass(frozen=True)
class Limits:
    code_ttl_seconds: int = 600
    code_tries: int = 5
    session_idle_seconds: int = 14 * 86400
    session_absolute_seconds: int = 60 * 86400
    step_up_seconds: int = 600
    recovery_wait_days: int = 7
    ledger_days: int = 16
    minimum_age: int = 16
    sends_per_address_15min: int = 3
    sends_per_address_day: int = 10
    sends_per_network_15min: int = 30
    sends_global_hour: int = 300
    sends_global_hour_other: int = 100
    sends_per_coarse_network_15min: int = 120
    account_actions_15min: int = 20
    finishes_per_network_15min: int = 30
    recoveries_per_network_hour: int = 5
    new_accounts_per_network_day: int = 5


@dataclass
class Result:
    status: str
    cookie: str | None = None
    new_account: bool = False
    effective_on: str | None = None
    recovery_code: str | None = None
    data: dict = field(default_factory=dict)


@dataclass(frozen=True)
class Session:
    account_id: str
    token_hash: str
    stepped_up: bool
    pending_recovery: bool


def _epoch_day(epoch: int) -> date:
    return datetime.fromtimestamp(epoch, timezone.utc).date()


def _week(day: date) -> str:
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


def normalise_recovery_code(raw) -> str | None:
    if not isinstance(raw, str):
        return None
    code = "".join(ch for ch in raw.upper() if ch not in " -\t")
    if len(code) != RECOVERY_LENGTH or not set(code) <= set(RECOVERY_ALPHABET):
        return None
    return code


def ledger_hash(account_id: str) -> str:
    return sha256(b"cic-accounts-ledger-v1|" + account_id.encode()).hexdigest()


class AccountsService:
    def __init__(
        self,
        store: AccountStore,
        keys: KeyRing,
        mailer: Mailer,
        *,
        clock: Callable[[], float] = time.time,
        limits: Limits = Limits(),
    ):
        self.store = store
        self.keys = keys
        self.mailer = mailer
        self.limits = limits
        self._clock = clock

    # time -------------------------------------------------------------------

    def now(self) -> int:
        return int(self._clock())

    def today(self) -> date:
        return _epoch_day(self.now())

    # counters ---------------------------------------------------------------

    def _allow(self, scope: str, key: str, window_seconds: int, limit: int) -> bool:
        return self.store.hit(scope, key, window_seconds, limit, self.now())

    def purge(self) -> int:
        """Drops expired codes, sessions, counters and ledger entries."""
        return self.store.purge_ephemeral(self.now()) + self.store.purge_durable(self.today().isoformat())

    # codes -------------------------------------------------------------------

    def _coarse(self, network: str) -> str:
        """The wider block a network belongs to (an IPv6 /48 or an IPv4 /24), as a keyed value."""
        try:
            ip = ipaddress.ip_address(network.split("/")[0])
        except ValueError:
            return self.keys.network_key(network)
        prefix = 48 if ip.version == 6 else 24
        block = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)
        return self.keys.network_key(str(block))

    def _count_start(self, network: str) -> bool:
        """Counts a start attempt against the network and its wider block, whatever follows."""
        limits = self.limits
        net = self.keys.network_key(network)
        return (
            self._allow("send_net", net, 900, limits.sends_per_network_15min)
            and self._allow("send_coarse", self._coarse(network), 900, limits.sends_per_coarse_network_15min)
        )

    def _admit_send(self, address_hash: str, purpose: str, network: str, scope: str = "") -> Result | None:
        """Counts a send attempt against every limit that applies and says whether it
        may go on. It runs before anything is learned about the address, so a refusal
        is the same for an address with an account and one without. The per-address
        counters are kept per purpose and, for step-up, address change and recovery,
        per account, so what the address's own owner did never changes what a
        stranger's attempts meet."""
        limits = self.limits
        key = f"{purpose}|{scope}|{address_hash}"
        within = (
            self._count_start(network)
            and self._allow("send_addr", key, 900, limits.sends_per_address_15min)
            and self._allow("send_addr_day", key, 86400, limits.sends_per_address_day)
        )
        if not within:
            return Result("throttled")
        sign_in = purpose == "sign_in"
        if not self._allow(
            "send_global_sign_in" if sign_in else "send_global_other", "all", 3600,
            limits.sends_global_hour if sign_in else limits.sends_global_hour_other,
        ):
            return Result("paused")
        return None

    def _deliver(self, norm: str, address_hash: str, purpose: str, account_id: str | None) -> Result:
        code = f"{secrets.randbelow(10**6):06d}"
        self.store.put_code(
            address_hash, purpose, self.keys.mac("code", purpose, address_hash, code),
            self.now() + self.limits.code_ttl_seconds, account_id,
        )
        try:
            self.mailer.send_code(norm, code)
        except Exception:  # noqa: BLE001 - the address and code must not reach a log
            logger.warning("a sign-in code could not be sent (purpose=%s)", purpose)
            self.store.burn_code(address_hash, purpose)
            return Result("send_failed")
        return Result("sent")

    def _send_code(self, norm: str, address_hash: str, purpose: str, network: str, account_id: str | None) -> Result:
        refused = self._admit_send(address_hash, purpose, network, account_id or "")
        return refused or self._deliver(norm, address_hash, purpose, account_id)

    def _check_code(self, address_hash: str, purpose: str, code) -> "CodeCheck | None":
        """Counts one try and says whether the code is right. The count and the
        read are one step, so concurrent guesses cannot beat the limit. A wrong
        try that uses the last allowed burns the code."""
        row = self.store.take_try(address_hash, purpose, self.now(), self.limits.code_tries)
        if row is None:
            return None
        given = "".join(ch for ch in str(code) if ch.isdigit()) if isinstance(code, (str, int)) else ""
        expected = self.keys.mac("code", purpose, address_hash, given)
        if not hmac.compare_digest(expected, row.mac):
            if row.tries >= self.limits.code_tries:
                self.store.burn_code_if(address_hash, purpose, row.mac)
            return None
        return CodeCheck(row.account_id, row.mac)

    def _spend_code(self, address_hash: str, purpose: str, check: "CodeCheck") -> bool:
        """Uses the proved code up. Of concurrent requests with the same right
        code, only one gets True."""
        return self.store.burn_code_if(address_hash, purpose, check.mac)

    # sign-in ------------------------------------------------------------------

    def start_sign_in(self, address, network: str) -> Result:
        norm = normalise_address(address)
        if norm is None:
            return Result("invalid_address")
        return self._send_code(norm, self.keys.address_hash(norm), "sign_in", network, None)

    def finish_sign_in(self, address, code, network: str, birth_year=None) -> Result:
        norm = normalise_address(address)
        if norm is None:
            return Result("wrong")
        net = self.keys.network_key(network)
        if not self._allow("finish_net", net, 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        ahash = self.keys.address_hash(norm)
        checked = self._check_code(ahash, "sign_in", code)
        if checked is None:
            return Result("wrong")
        pending = self.store.verified_pending_for_hash(ahash)
        if pending is not None:
            if pending.effective_on > self.today().isoformat():
                return Result("recovery_waiting", effective_on=pending.effective_on)
            if not self._spend_code(ahash, "sign_in", checked):
                return Result("wrong")
            applied = self._apply_pending(pending)
            account = self.store.account_by_hashes(self.keys.candidate_hashes(norm))
            if account is None:
                return Result("wrong")
            issued = self._issue_recovery_code(account.account_id) if applied else None
            return self._sign_in_as(account, ahash, issued)
        account = self.store.account_by_hashes(self.keys.candidate_hashes(norm))
        if account is not None:
            if not self._spend_code(ahash, "sign_in", checked):
                return Result("wrong")
            return self._sign_in_as(account, ahash)
        if birth_year is None:
            return Result("needs_birth_year")
        band = self._age_band(birth_year)
        if band == "invalid":
            return Result("invalid_birth_year")
        if band is None:
            self._spend_code(ahash, "sign_in", checked)
            return Result("under_age")
        if not self._allow("new_account_net", net, 86400, self.limits.new_accounts_per_network_day):
            return Result("throttled")
        if not self._spend_code(ahash, "sign_in", checked):
            return Result("wrong")
        today = self.today()
        account = Account(secrets.token_hex(16), ahash, today.isoformat(), min(today.day, 28), _week(today), band)
        if not self.store.create_account(account):
            account = self.store.account_by_hashes(self.keys.candidate_hashes(norm))
            if account is None:
                return Result("wrong")
            return self._sign_in_as(account, ahash)
        return self._sign_in_as(account, ahash, new_account=True)

    def _sign_in_as(self, account: Account, ahash: str, recovery_code: str | None = None, new_account: bool = False) -> Result:
        if not self.keys.is_current(account.address_hash):
            self.store.set_address_hash(account.account_id, ahash)
        self.store.touch(account.account_id, _week(self.today()))
        return Result("ok", cookie=self._open_session(account.account_id), new_account=new_account,
                      recovery_code=recovery_code)

    def _issue_recovery_code(self, account_id: str) -> str:
        code = "".join(secrets.choice(RECOVERY_ALPHABET) for _ in range(RECOVERY_LENGTH))
        self.store.put_recovery_code(account_id, sha256(code.encode()).hexdigest(), self.today().isoformat())
        return code

    def _age_band(self, birth_year) -> str | None:
        year = self.today().year
        if isinstance(birth_year, bool) or not isinstance(birth_year, int) or not 1900 <= birth_year <= year:
            return "invalid"
        age = year - birth_year
        if age < self.limits.minimum_age:
            return None
        return "16-17" if age <= 17 else "18+"

    # sessions -------------------------------------------------------------------

    def _open_session(self, account_id: str) -> str:
        token = secrets.token_urlsafe(32)
        now = self.now()
        self.store.put_session(SessionRow(
            sha256(token.encode()).hexdigest(), account_id,
            now + self.limits.session_idle_seconds, now + self.limits.session_absolute_seconds, 0,
        ))
        return self.keys.sign_cookie(token)

    def session(self, cookie) -> Session | None:
        token = self.keys.open_cookie(cookie) if isinstance(cookie, str) else None
        if token is None:
            return None
        token_hash = sha256(token.encode()).hexdigest()
        row = self.store.get_session(token_hash)
        now = self.now()
        if row is None:
            return None
        if row.idle_expires_at <= now or row.abs_expires_at <= now:
            self.store.delete_session(token_hash)
            return None
        if self.store.account(row.account_id) is None:
            self.store.delete_session(token_hash)
            return None
        self.store.slide_session(token_hash, min(now + self.limits.session_idle_seconds, row.abs_expires_at))
        return Session(
            row.account_id, token_hash, row.stepped_up_until > now,
            self.store.pending_for_account(row.account_id) is not None,
        )

    def sign_out(self, session: Session) -> None:
        self.store.delete_session(session.token_hash)

    def sign_out_everywhere(self, session: Session) -> None:
        self.store.delete_sessions_of(session.account_id)

    # step-up --------------------------------------------------------------------

    def _owns(self, account_id: str, address) -> tuple[str, str] | None:
        """(normalised address, current-key hash) when the typed address is this account's."""
        norm = normalise_address(address)
        account = self.store.account(account_id)
        if norm is None or account is None:
            return None
        if account.address_hash not in self.keys.candidate_hashes(norm):
            return None
        return norm, self.keys.address_hash(norm)

    def step_up_start(self, session: Session, address, network: str) -> Result:
        if not self._allow("account", session.account_id, 900, self.limits.account_actions_15min):
            return Result("throttled")
        norm = normalise_address(address)
        if norm is None:
            return Result("sent") if self._count_start(network) else Result("throttled")
        typed = self.keys.address_hash(norm)
        refused = self._admit_send(typed, "step_up", network, session.account_id)
        if refused:
            return refused
        owned = self._owns(session.account_id, address)
        if owned is None:
            return Result("sent")
        return self._deliver(owned[0], owned[1], "step_up", session.account_id)

    def step_up_finish(self, session: Session, address, code, network: str) -> Result:
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        owned = self._owns(session.account_id, address)
        checked = self._check_code(owned[1], "step_up", code) if owned else None
        if checked is None or not self._spend_code(owned[1], "step_up", checked):
            return Result("wrong")
        self.store.step_up_session(session.token_hash, self.now() + self.limits.step_up_seconds)
        return Result("ok")

    # recovery code ----------------------------------------------------------------

    def make_recovery_code(self, session: Session) -> Result:
        """A new recovery code, shown once. It replaces any earlier one."""
        if not session.stepped_up:
            return Result("step_up_needed")
        return Result("ok", recovery_code=self._issue_recovery_code(session.account_id))

    def recover_start(self, recovery_code, new_address, network: str) -> Result:
        """Starts a recovery for a new address. A recovery code that is right always
        gets the same reply, whether or not the new address already has an account, and
        every limit is counted before that is looked at. The code is spent only when the
        new address is proved, at recover_finish."""
        if not self._allow("recover_net", self.keys.network_key(network), 3600, self.limits.recoveries_per_network_hour):
            return Result("throttled")
        code = normalise_recovery_code(recovery_code)
        norm = normalise_address(new_address)
        account_id = self.store.account_by_recovery_hash(sha256(code.encode()).hexdigest()) if code else None
        if account_id is None or norm is None:
            return Result("wrong")
        candidates = self.keys.candidate_hashes(norm)
        refused = self._admit_send(candidates[0], "recover", network, account_id)
        if refused:
            return refused
        taken = self.store.account_by_hashes(candidates) is not None
        if taken or self.store.verified_pending_for_hash(candidates[0]) is not None:
            return Result("sent")
        today = self.today()
        effective_on = (today + timedelta(days=self.limits.recovery_wait_days)).isoformat()
        if not self.store.put_pending(Pending(account_id, candidates[0], effective_on, False, today.isoformat())):
            return Result("sent")
        sent = self._deliver(norm, candidates[0], "recover", account_id)
        if sent.status != "sent":
            self.store.delete_pending(account_id)
            return sent
        return Result("sent")

    def recover_finish(self, new_address, code, network: str) -> Result:
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        norm = normalise_address(new_address)
        if norm is None:
            return Result("wrong")
        ahash = self.keys.address_hash(norm)
        checked = self._check_code(ahash, "recover", code)
        pending = self.store.pending_of(checked.account_id, ahash) if checked and checked.account_id else None
        if pending is None or not self._spend_code(ahash, "recover", checked):
            return Result("wrong")
        if not self.store.verify_pending(pending.account_id, ahash):
            return Result("wrong")
        self.store.delete_recovery_code(pending.account_id)
        return Result("waiting", effective_on=pending.effective_on)

    def cancel_recovery(self, session: Session) -> Result:
        if not session.stepped_up:
            return Result("step_up_needed")
        self.store.delete_pending(session.account_id)
        return Result("ok")

    def _apply_pending(self, pending: Pending) -> bool:
        """The waiting period is over: the account moves to the new address, every
        session ends, and the old recovery code is gone. False when the address was
        taken during the wait, in which case nothing moves."""
        if self.store.account_by_hashes([pending.new_address_hash]) is not None:
            self.store.delete_pending(pending.account_id)
            return False
        self.store.set_address_hash(pending.account_id, pending.new_address_hash)
        self.store.delete_sessions_of(pending.account_id)
        self.store.delete_recovery_code(pending.account_id)
        self.store.delete_pending(pending.account_id)
        return True

    # address change ----------------------------------------------------------------

    def change_address_start(self, session: Session, new_address, network: str) -> Result:
        """Needs a recent step-up, which proved the old address; this sends a code to
        the new one. A new address that already has an account gets the same reply and
        no code, so the reply never says whether an account exists."""
        if not session.stepped_up:
            return Result("step_up_needed")
        norm = normalise_address(new_address)
        if norm is None:
            return Result("invalid_address")
        if not self._allow("account", session.account_id, 900, self.limits.account_actions_15min):
            return Result("throttled")
        candidates = self.keys.candidate_hashes(norm)
        refused = self._admit_send(candidates[0], "change", network, session.account_id)
        if refused:
            return refused
        if self.store.account_by_hashes(candidates) is not None or self.store.verified_pending_for_hash(candidates[0]) is not None:
            return Result("sent")
        return self._deliver(norm, candidates[0], "change", session.account_id)

    def change_address_finish(self, session: Session, new_address, code, network: str) -> Result:
        if not session.stepped_up:
            return Result("step_up_needed")
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        ahash = self.keys.address_hash(new_address)
        checked = self._check_code(ahash, "change", code) if ahash else None
        if checked is None or checked.account_id != session.account_id or not self._spend_code(ahash, "change", checked):
            return Result("wrong")
        if not self.store.set_address_hash(session.account_id, ahash):
            return Result("wrong")
        self.store.delete_sessions_of(session.account_id, except_token_hash=session.token_hash)
        self.store.delete_pending(session.account_id)
        return Result("ok")

    # what an account holds, and deletion ------------------------------------------------

    def me(self, session: Session) -> dict:
        account = self.store.account(session.account_id)
        return {
            "signed_in": True,
            "refill_day": account.refill_day,
            "age_band": account.age_band,
            "pending_recovery": session.pending_recovery,
            "has_recovery_code": self.store.has_recovery_code(session.account_id),
        }

    def export(self, session: Session) -> Result:
        """What the account holds today. It grows as the shelf and the token
        history are added; it never includes a live code or the recovery code."""
        if not session.stepped_up:
            return Result("step_up_needed")
        account = self.store.account(session.account_id)
        return Result("ok", data={
            "day_created": account.day_created,
            "refill_day": account.refill_day,
            "week_last_used": account.week_last_used,
            "age_band": account.age_band,
        })

    def delete_account(self, session: Session) -> Result:
        if not session.stepped_up:
            return Result("step_up_needed")
        expires = (self.today() + timedelta(days=self.limits.ledger_days)).isoformat()
        account = self.store.account(session.account_id)
        self.store.delete_account(session.account_id, ledger_hash(session.account_id), expires)
        if account is not None:
            self.store.forget_address(account.address_hash)
        self.store.delete_sessions_of(session.account_id)
        self.store.delete_codes_of(session.account_id)
        return Result("ok")

    def reapply_ledger(self) -> int:
        """After a restore from backup: removes any account the ledger says was deleted."""
        gone = self.store.accounts_in_ledger(ledger_hash)
        for account_id in gone:
            self.store.delete_account(account_id, ledger_hash(account_id), self.today().isoformat())
            self.store.delete_sessions_of(account_id)
        return len(gone)


@dataclass(frozen=True)
class CodeCheck:
    account_id: str | None
    mac: str
