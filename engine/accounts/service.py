"""Sign-in, sessions, recovery, address change and deletion.

A person proves they control an address by typing a six-digit code sent to it.
Every proof is a challenge: it has its own random id, belongs to one action and
one account, and is found only by that id, so no other account's action can
touch, replace or stand in for it. The code is stored only as a keyed value
bound to the challenge id, works once, dies after ten minutes, and is burned
after five wrong tries. Nothing here logs an address or a code. A start step
gives the same reply, and counts the same limits, whether or not the address
already has an account; the only difference is that no mail is sent to an
address that has one.

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
from engine.accounts.store import Account, AccountStore, Challenge, Pending, SessionRow

logger = logging.getLogger("cic.accounts")

RECOVERY_ALPHABET = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
RECOVERY_LENGTH = 20
MAX_ID_LENGTH = 64


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
    sends_per_address_open_15min: int = 6
    sends_per_address_open_day: int = 20
    sends_per_network_15min: int = 30
    sends_per_coarse_network_15min: int = 120
    sends_global_hour: int = 300
    sends_global_hour_other: int = 100
    account_actions_15min: int = 20
    finishes_per_network_15min: int = 30
    recoveries_per_network_hour: int = 5
    new_accounts_per_network_day: int = 5


@dataclass
class Result:
    status: str
    challenge: str | None = None
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

    # time and counters -------------------------------------------------------

    def now(self) -> int:
        return int(self._clock())

    def today(self) -> date:
        return _epoch_day(self.now())

    def _allow(self, scope: str, key: str, window_seconds: int, limit: int) -> bool:
        return self.store.hit(scope, key, window_seconds, limit, self.now())

    def purge(self) -> int:
        """Drops expired challenges, sessions, counters and ledger entries."""
        return self.store.purge_ephemeral(self.now()) + self.store.purge_durable(self.today().isoformat())

    def _coarse(self, network: str) -> str:
        """The wider block a network belongs to (an IPv6 /48 or an IPv4 /24), as a keyed value."""
        try:
            ip = ipaddress.ip_address(network.split("/")[0])
        except ValueError:
            return self.keys.network_key(network)
        block = ipaddress.ip_network(f"{ip}/{48 if ip.version == 6 else 24}", strict=False)
        return self.keys.network_key(str(block))

    def _admit(self, kind: str, network: str, *, account_id: str | None = None, address_hash: str | None = None) -> Result | None:
        """Counts a start attempt against every limit that applies and says whether it may go
        on. It runs before anything is learned about the address, so a refusal is the same for
        an address with an account and one without. A sign-in is counted per address because
        anyone may start one. A change or a recovery is counted across all accounts per address:
        an address's own owner never starts one to an address they already hold, so that counter
        carries no signal. Step-up is counted per account only."""
        limits = self.limits
        within = self._allow("send_net", self.keys.network_key(network), 900, limits.sends_per_network_15min)
        within = within and self._allow("send_coarse", self._coarse(network), 900, limits.sends_per_coarse_network_15min)
        if account_id is not None:
            within = within and self._allow("account", account_id, 900, limits.account_actions_15min)
        if address_hash is not None and kind == "sign_in":
            within = (
                within
                and self._allow("send_addr", f"sign_in|{address_hash}", 900, limits.sends_per_address_15min)
                and self._allow("send_addr_day", f"sign_in|{address_hash}", 86400, limits.sends_per_address_day)
            )
        if address_hash is not None and kind in ("change", "recover"):
            within = (
                within
                and self._allow("send_addr", f"{kind}|{address_hash}", 900, limits.sends_per_address_open_15min)
                and self._allow("send_addr_day", f"{kind}|{address_hash}", 86400, limits.sends_per_address_open_day)
            )
        if not within:
            return Result("throttled")
        sign_in = kind == "sign_in"
        if not self._allow(
            "send_global_sign_in" if sign_in else "send_global_other", "all", 3600,
            limits.sends_global_hour if sign_in else limits.sends_global_hour_other,
        ):
            return Result("paused")
        return None

    # challenges ----------------------------------------------------------------

    def _open_challenge(self, kind: str, address_hash: str, account_id: str | None, mail_to: str | None) -> Result:
        """Opens one proof. With no address to mail, the challenge is the same in every
        way except that its code is never sent, so it can never be proved."""
        challenge_id = secrets.token_urlsafe(16)
        code = f"{secrets.randbelow(10**6):06d}"
        self.store.put_challenge(
            Challenge(challenge_id, kind, address_hash, account_id, self.keys.mac("code", challenge_id, code),
                      self.now() + self.limits.code_ttl_seconds, 0),
            replace_same_address=(kind == "sign_in"),
        )
        if mail_to is not None:
            try:
                self.mailer.send_code(mail_to, code)
            except Exception:  # noqa: BLE001 - the address and code must not reach a log
                logger.warning("a sign-in code could not be sent (kind=%s)", kind)
                self.store.burn_challenge(challenge_id)
                return Result("send_failed")
        return Result("sent", challenge=challenge_id)

    def _check(self, challenge_id, kind: str, code, *, account_id: str | None = None, address_hash: str | None = None) -> Challenge | None:
        """Counts one try and returns the challenge if the code is right and the challenge is
        of this kind, for this account and address. The count and the read are one step, so
        concurrent guesses cannot beat the limit. A wrong try that uses the last allowed burns it."""
        if not isinstance(challenge_id, str) or not 0 < len(challenge_id) <= MAX_ID_LENGTH:
            return None
        row = self.store.take_try(challenge_id, self.now(), self.limits.code_tries)
        if row is None or row.kind != kind:
            return None
        if account_id is not None and row.account_id != account_id:
            return None
        if address_hash is not None and row.address_hash != address_hash:
            return None
        given = "".join(ch for ch in str(code) if ch.isdigit()) if isinstance(code, (str, int)) else ""
        if not hmac.compare_digest(self.keys.mac("code", challenge_id, given), row.mac):
            if row.tries >= self.limits.code_tries:
                self.store.burn_challenge_if(challenge_id, row.mac)
            return None
        return row

    def _spend(self, row: Challenge) -> bool:
        """Uses the proved challenge up. Of concurrent requests with the same right code, only one gets True."""
        return self.store.burn_challenge_if(row.challenge_id, row.mac)

    # sign-in ------------------------------------------------------------------

    def start_sign_in(self, address, network: str) -> Result:
        norm = normalise_address(address)
        if norm is None:
            return Result("invalid_address")
        ahash = self.keys.address_hash(norm)
        refused = self._admit("sign_in", network, address_hash=ahash)
        return refused or self._open_challenge("sign_in", ahash, None, norm)

    def finish_sign_in(self, challenge, address, code, network: str, birth_year=None) -> Result:
        norm = normalise_address(address)
        if norm is None:
            return Result("wrong")
        net = self.keys.network_key(network)
        if not self._allow("finish_net", net, 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        ahash = self.keys.address_hash(norm)
        checked = self._check(challenge, "sign_in", code, address_hash=ahash)
        if checked is None:
            return Result("wrong")
        pending = self.store.pending_for_hash(ahash)
        if pending is not None:
            if pending.effective_on > self.today().isoformat():
                return Result("recovery_waiting", effective_on=pending.effective_on)
            if not self._spend(checked):
                return Result("wrong")
            applied = self._apply_pending(pending)
            account = self.store.account_by_hashes(self.keys.candidate_hashes(norm))
            if account is None:
                return Result("wrong")
            issued = self._issue_recovery_code(account.account_id) if applied else None
            return self._sign_in_as(account, ahash, issued)
        account = self.store.account_by_hashes(self.keys.candidate_hashes(norm))
        if account is not None:
            if not self._spend(checked):
                return Result("wrong")
            return self._sign_in_as(account, ahash)
        if birth_year is None:
            return Result("needs_birth_year")
        band = self._age_band(birth_year)
        if band == "invalid":
            return Result("invalid_birth_year")
        if band is None:
            self._spend(checked)
            return Result("under_age")
        if not self._allow("new_account_net", net, 86400, self.limits.new_accounts_per_network_day):
            return Result("throttled")
        if not self._spend(checked):
            return Result("wrong")
        today = self.today()
        account = Account(secrets.token_hex(16), ahash, today.isoformat(), min(today.day, 28), _week(today), band)
        if not self.store.create_account(account):
            account = self.store.account_by_hashes(self.keys.candidate_hashes(norm))
            return self._sign_in_as(account, ahash) if account else Result("wrong")
        return self._sign_in_as(account, ahash, new_account=True)

    def _sign_in_as(self, account: Account, ahash: str, recovery_code: str | None = None, new_account: bool = False) -> Result:
        if not self.keys.is_current(account.address_hash):
            self.store.set_address_hash(account.account_id, ahash)
        self.store.touch(account.account_id, _week(self.today()))
        return Result("ok", cookie=self._open_session(account.account_id), new_account=new_account,
                      recovery_code=recovery_code)

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
        norm = normalise_address(address)
        ahash = self.keys.address_hash(norm) if norm else ""
        refused = self._admit("step_up", network, account_id=session.account_id)
        if refused:
            return refused
        owned = self._owns(session.account_id, address)
        return self._open_challenge("step_up", ahash, session.account_id, owned[0] if owned else None)

    def step_up_finish(self, session: Session, challenge, code, network: str) -> Result:
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        checked = self._check(challenge, "step_up", code, account_id=session.account_id)
        if checked is None or not self._spend(checked):
            return Result("wrong")
        self.store.step_up_session(session.token_hash, self.now() + self.limits.step_up_seconds)
        return Result("ok")

    # recovery code ----------------------------------------------------------------

    def _issue_recovery_code(self, account_id: str) -> str:
        code = "".join(secrets.choice(RECOVERY_ALPHABET) for _ in range(RECOVERY_LENGTH))
        self.store.put_recovery_code(account_id, sha256(code.encode()).hexdigest(), self.today().isoformat())
        return code

    def make_recovery_code(self, session: Session) -> Result:
        """A new recovery code, shown once. It replaces any earlier one, and ends any
        recovery already started with it."""
        if not session.stepped_up:
            return Result("step_up_needed")
        self.store.delete_challenges_of(session.account_id, "recover")
        return Result("ok", recovery_code=self._issue_recovery_code(session.account_id))

    def recover_start(self, recovery_code, new_address, network: str) -> Result:
        """Starts a recovery to a new address. A right recovery code always gets the same reply,
        whether or not the new address already has an account. The recovery code is spent only
        when the new address is proved."""
        if not self._allow("recover_net", self.keys.network_key(network), 3600, self.limits.recoveries_per_network_hour):
            return Result("throttled")
        code = normalise_recovery_code(recovery_code)
        norm = normalise_address(new_address)
        account_id = self.store.account_by_recovery_hash(sha256(code.encode()).hexdigest()) if code else None
        if account_id is None or norm is None:
            return Result("wrong")
        candidates = self.keys.candidate_hashes(norm)
        refused = self._admit("recover", network, account_id=account_id, address_hash=candidates[0])
        if refused:
            return refused
        taken = self.store.account_by_hashes(candidates) is not None or self.store.pending_for_hash(candidates[0]) is not None
        return self._open_challenge("recover", candidates[0], account_id, None if taken else norm)

    def recover_finish(self, challenge, code, network: str) -> Result:
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        checked = self._check(challenge, "recover", code)
        if checked is None or checked.account_id is None or not self._spend(checked):
            return Result("wrong")
        other = self.store.pending_for_hash(checked.address_hash)
        if other is not None and other.account_id != checked.account_id:
            return Result("wrong")
        if not self.store.delete_recovery_code(checked.account_id):  # the recovery code is claimed here, once
            return Result("wrong")
        effective_on = (self.today() + timedelta(days=self.limits.recovery_wait_days)).isoformat()
        if not self.store.put_pending(Pending(checked.account_id, checked.address_hash, effective_on)):
            return Result("wrong")
        return Result("waiting", effective_on=effective_on)

    def cancel_recovery(self, session: Session) -> Result:
        if not session.stepped_up:
            return Result("step_up_needed")
        self.store.delete_pending(session.account_id)
        self.store.delete_challenges_of(session.account_id, "recover")
        return Result("ok")

    def _apply_pending(self, pending: Pending) -> bool:
        """The waiting period is over: the account moves to the new address, every session ends,
        and the old recovery code is gone. False when the address was taken during the wait, in
        which case nothing moves."""
        if self.store.account_by_hashes([pending.new_address_hash]) is not None:
            self.store.delete_pending(pending.account_id)
            return False
        moved = self.store.set_address_hash(pending.account_id, pending.new_address_hash)
        self.store.delete_pending(pending.account_id)
        if not moved:
            return False
        self.store.delete_sessions_of(pending.account_id)
        self.store.delete_recovery_code(pending.account_id)
        return True

    # address change ----------------------------------------------------------------

    def change_address_start(self, session: Session, new_address, network: str) -> Result:
        """Needs a recent step-up, which proved the old address; this sends a code to the new
        one. A new address that already has an account gets the same reply and no code."""
        if not session.stepped_up:
            return Result("step_up_needed")
        norm = normalise_address(new_address)
        if norm is None:
            return Result("invalid_address")
        candidates = self.keys.candidate_hashes(norm)
        refused = self._admit("change", network, account_id=session.account_id, address_hash=candidates[0])
        if refused:
            return refused
        taken = self.store.account_by_hashes(candidates) is not None or self.store.pending_for_hash(candidates[0]) is not None
        return self._open_challenge("change", candidates[0], session.account_id, None if taken else norm)

    def change_address_finish(self, session: Session, challenge, code, network: str) -> Result:
        if not session.stepped_up:
            return Result("step_up_needed")
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        checked = self._check(challenge, "change", code, account_id=session.account_id)
        if checked is None or not self._spend(checked):
            return Result("wrong")
        if not self.store.set_address_hash(session.account_id, checked.address_hash):
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
        """What the account holds today. It grows as the shelf and the token history are
        added; it never includes a live code or the recovery code."""
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
        self.store.delete_challenges_of(session.account_id)
        return Result("ok")

    def reapply_ledger(self) -> int:
        """After a restore from backup: removes any account the ledger says was deleted."""
        gone = self.store.accounts_in_ledger(ledger_hash)
        for account_id in gone:
            self.store.delete_account(account_id, ledger_hash(account_id), self.today().isoformat())
            self.store.delete_sessions_of(account_id)
        return len(gone)
