"""Sign-in, sessions, step-up, address change and deletion.

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

from engine.accounts.contacts import ContactStore
from engine.accounts.keys import KeyRing, normalise_address
from engine.accounts.store import Account, AccountStore, Challenge, SessionRow

logger = logging.getLogger("cic.accounts")

MAX_ID_LENGTH = 64


PROVIDERS = ("google", "apple")


class ProviderVerifier(Protocol):
    def available(self, provider: str) -> bool:
        """Whether this way of signing in is set up."""

    def verify(self, provider: str, id_token: str, nonce: str) -> tuple[str, str] | None:
        """(issuer, subject) when the provider signed this token for our app and this nonce, else None."""


class Mailer(Protocol):
    def send_code(self, address: str, code: str) -> None:
        """Sends one sign-in code. The address is used for this send and nowhere else."""

    def send_notice(self, address: str, kind: str, fields: dict) -> None:
        """Sends one notice to an account's own address, such as that a recovery was started."""


@dataclass(frozen=True)
class Limits:
    code_ttl_seconds: int = 600
    code_tries: int = 5
    session_idle_seconds: int = 14 * 86400
    session_absolute_seconds: int = 60 * 86400
    step_up_seconds: int = 600
    ledger_days: int = 16
    sends_per_address_15min: int = 3
    sends_per_address_day: int = 10
    sends_per_address_open_15min: int = 4
    sends_per_address_open_day: int = 10
    sends_per_network_15min: int = 30
    sends_per_coarse_network_15min: int = 120
    sends_global_hour: int = 300
    sends_global_hour_other: int = 100
    account_actions_15min: int = 20
    account_actions_day: int = 60
    finishes_per_network_15min: int = 30
    new_accounts_per_network_day: int = 5
    provider_starts_per_network_15min: int = 30
    provider_starts_per_coarse_network_15min: int = 120
    nonce_ttl_seconds: int = 600
    recovery_wait_days: int = 7


@dataclass
class Result:
    status: str
    challenge: str | None = None
    cookie: str | None = None
    new_account: bool = False
    data: dict = field(default_factory=dict)


@dataclass(frozen=True)
class Session:
    account_id: str
    token_hash: str
    stepped_up: bool


def _epoch_day(epoch: int) -> date:
    return datetime.fromtimestamp(epoch, timezone.utc).date()


def _week(day: date) -> str:
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


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
        verifier: ProviderVerifier | None = None,
        contacts: ContactStore | None = None,
    ):
        self.store = store
        self.keys = keys
        self.mailer = mailer
        self.limits = limits
        self.verifier = verifier
        self.contacts = contacts
        self._clock = clock

    # time and counters -------------------------------------------------------

    def now(self) -> int:
        return int(self._clock())

    def today(self) -> date:
        return _epoch_day(self.now())

    def _allow(self, scope: str, key: str, window_seconds: int, limit: int) -> bool:
        return self.store.hit(scope, key, window_seconds, limit, self.now())

    def purge(self) -> int:
        """Drops expired challenges, sessions, counters and ledger entries, and carries out any
        recovery whose days are up."""
        self._apply_due_recoveries()
        self._sweep_contacts()
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
        anyone may start one. An address change is counted across all accounts per address: an
        address's own owner never starts one to an address they already hold, so that counter
        carries no signal. Step-up mails only the account's own address and is counted per
        account and per network, never in a budget other parties can fill, so an owner can
        always prove their address."""
        limits = self.limits
        within = self._allow("send_net", self.keys.network_key(network), 900, limits.sends_per_network_15min)
        within = within and self._allow("send_coarse", self._coarse(network), 900, limits.sends_per_coarse_network_15min)
        if account_id is not None:
            within = (
                within
                and self._allow("account", account_id, 900, limits.account_actions_15min)
                and self._allow("account_day", account_id, 86400, limits.account_actions_day)
            )
        if address_hash is not None and kind == "sign_in":
            within = (
                within
                and self._allow("send_addr", f"sign_in|{address_hash}", 900, limits.sends_per_address_15min)
                and self._allow("send_addr_day", f"sign_in|{address_hash}", 86400, limits.sends_per_address_day)
            )
        if address_hash is not None and kind == "change":
            within = (
                within
                and self._allow("send_addr", f"{kind}|{address_hash}", 900, limits.sends_per_address_open_15min)
                and self._allow("send_addr_day", f"{kind}|{address_hash}", 86400, limits.sends_per_address_open_day)
            )
        if not within:
            return Result("throttled")
        if kind == "step_up":
            return None
        sign_in = kind == "sign_in"
        if not self._allow(
            "send_global_sign_in" if sign_in else "send_global_other", "all", 3600,
            limits.sends_global_hour if sign_in else limits.sends_global_hour_other,
        ):
            return Result("paused")
        return None

    # challenges ----------------------------------------------------------------

    def _open_challenge(self, kind: str, address_hash: str, account_id: str | None, mail_to: str | None,
                        bound: str | None = None) -> Result:
        """Opens one proof. With no address to mail, the challenge is the same in every
        way except that its code is never sent, so it can never be proved."""
        challenge_id = secrets.token_urlsafe(16)
        code = f"{secrets.randbelow(10**6):06d}"
        self.store.put_challenge(
            Challenge(challenge_id, kind, address_hash, account_id, self.keys.mac("code", challenge_id, code),
                      self.now() + self.limits.code_ttl_seconds, 0, bound),
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

    def finish_sign_in(self, challenge, address, code, network: str, over_18=None) -> Result:
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
        self._apply_due_recoveries()
        candidates = self.keys.candidate_hashes(norm)
        account = self.store.account_by_hashes(candidates)
        if account is not None:
            if not self._spend(checked):
                return Result("wrong")
            self._keep_contact(account.account_id, norm)
            return self._sign_in_as(account, ahash)
        waiting = self.store.pending_for_address(candidates)
        if waiting is not None:
            # The code just proved this address, so naming the wait tells no stranger anything;
            # opening an account here would make the recovery fail on its seventh day.
            return Result("recovery_waiting", data={"effective_on": waiting})
        if over_18 is None:
            return Result("needs_age_answer")
        if over_18 is not True:
            # A no opens nothing and stores nothing, and leaves the proved code unused.
            return Result("not_adult")
        if not self._allow("new_account_net", net, 86400, self.limits.new_accounts_per_network_day):
            return Result("throttled")
        if not self._spend(checked):
            return Result("wrong")
        today = self.today()
        account = Account(secrets.token_hex(16), ahash, today.isoformat(), min(today.day, 28), _week(today), "18+")
        if not self.store.create_account(account):
            account = self.store.account_by_hashes(self.keys.candidate_hashes(norm))
            if account is None:
                return Result("wrong")
            self._keep_contact(account.account_id, norm)
            return self._sign_in_as(account, ahash)
        self._keep_contact(account.account_id, norm)
        return self._sign_in_as(account, ahash, new_account=True)

    def _keep_contact(self, account_id: str, address: str) -> None:
        """Keeps the typed address, sealed, for sending to its owner. Written when there is none
        yet, cannot be read, differs from the one typed, or is sealed under an older key."""
        if self.contacts is not None and (self.contacts.get(account_id) != address or not self.contacts.is_current(account_id)):
            self.contacts.put(account_id, address)

    def _sign_in_as(self, account: Account, ahash: str, new_account: bool = False) -> Result:
        if not self.keys.is_current(account.address_hash):
            self.store.set_address_hash(account.account_id, ahash)
        self.store.touch(account.account_id, _week(self.today()))
        return Result("ok", cookie=self._open_session(account.account_id), new_account=new_account)

    # Google and Apple ------------------------------------------------------------

    def provider_start(self, network: str) -> Result:
        """A nonce the page hands to Google or Apple, so a token made for another sitting cannot
        be replayed here. It is random, carries its own expiry and is signed under the session
        key, so issuing one writes nothing and no cap on issuing can be filled to lock people
        out. A row is written only when a nonce is used."""
        limits = self.limits
        if not (
            self._allow("provider_net", self.keys.network_key(network), 900, limits.provider_starts_per_network_15min)
            and self._allow("provider_coarse", self._coarse(network), 900, limits.provider_starts_per_coarse_network_15min)
        ):
            return Result("throttled")
        body = f"{secrets.token_urlsafe(18)}.{self.now() + limits.nonce_ttl_seconds}"
        return Result("sent", challenge=f"{body}.{self.keys.mac('nonce', body)[:24]}")

    def _provider_ready(self, provider) -> bool:
        return provider in PROVIDERS and self.verifier is not None and self.verifier.available(provider)

    def _nonce(self, nonce) -> int | None:
        """The expiry of a nonce this server issued and that has not run out, else None."""
        if not isinstance(nonce, str) or not 0 < len(nonce) <= MAX_ID_LENGTH:
            return None
        body, sep, tag = nonce.rpartition(".")
        _, _, expiry = body.rpartition(".")
        if not sep or not expiry.isdigit() or not hmac.compare_digest(self.keys.mac("nonce", body)[:24], tag):
            return None
        return int(expiry) if int(expiry) > self.now() else None

    def _identity(self, provider: str, id_token, nonce: str) -> tuple[str, list[str]] | None:
        """(the current-key hash, every live-key hash) of the provider's account id, when the
        token is genuine, made for this app and carries this nonce."""
        if not isinstance(id_token, str) or not 0 < len(id_token) <= 4096:
            return None
        try:
            who = self.verifier.verify(provider, id_token, nonce)
        except Exception:  # noqa: BLE001 - the token must not reach a log
            logger.warning("a provider token could not be checked (provider=%s)", provider)
            return None
        if who is None:
            return None
        candidates = self.keys.provider_candidates(provider, who[0], who[1])
        return candidates[0], candidates

    def provider_sign_in(self, provider, id_token, nonce, network: str, over_18=None) -> Result:
        """Signs in by a provider's account id. A person the provider does not yet map to an
        account is asked the one-click age line first, as at a first typed-code sign-in. The
        provider's email is never read."""
        if not self._provider_ready(provider):
            return Result("not_available")
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        expiry = self._nonce(nonce)
        who = self._identity(provider, id_token, nonce) if expiry is not None else None
        if who is None:
            return Result("wrong")
        current, candidates = who
        found = self.store.account_by_subjects(candidates)
        if found is not None:
            account, stored, _ = found
            if not self.store.spend_nonce(nonce, expiry):
                return Result("wrong")
            if stored != current:
                self.store.rekey_link(stored, current)
            return self._sign_in_by_provider(account)
        if over_18 is None:
            return Result("needs_age_answer")
        if over_18 is not True:
            return Result("not_adult")
        if not self._allow("new_account_net", self.keys.network_key(network), 86400, self.limits.new_accounts_per_network_day):
            return Result("throttled")
        if not self.store.spend_nonce(nonce, expiry):
            return Result("wrong")
        today = self.today()
        account = Account(secrets.token_hex(16), None, today.isoformat(), min(today.day, 28), _week(today), "18+")
        if not self.store.create_account(account, (current, provider)):
            found = self.store.account_by_subjects(candidates)
            return self._sign_in_by_provider(found[0]) if found else Result("wrong")
        return self._sign_in_by_provider(account, new_account=True)

    def _sign_in_by_provider(self, account: Account, new_account: bool = False) -> Result:
        self.store.touch(account.account_id, _week(self.today()))
        return Result("ok", cookie=self._open_session(account.account_id), new_account=new_account)

    def provider_step_up(self, session: Session, provider, id_token, nonce, network: str) -> Result:
        """A fresh sign-in by a provider the account already has counts as the step-up only for
        an account with no address, which has no address to send a code to. An account that has
        an address steps up by a code to it, so a stolen Google or Apple session cannot change
        the address, link or unlink a method, export or delete."""
        if not self._provider_ready(provider):
            return Result("not_available")
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        expiry = self._nonce(nonce)
        who = self._identity(provider, id_token, nonce) if expiry is not None else None
        found = self.store.account_by_subjects(who[1]) if who is not None else None
        if (
            found is None or found[0].account_id != session.account_id or found[0].address_hash is not None
            or not self.store.spend_nonce(nonce, expiry)
        ):
            return Result("wrong")
        self.store.step_up_session(session.token_hash, self.now() + self.limits.step_up_seconds)
        return Result("ok")

    def provider_link(self, session: Session, provider, id_token, nonce, network: str) -> Result:
        """Adds Google or Apple to the signed-in account. Never by a matching email; only by
        the provider's own account id, after a fresh step-up. Every other session ends."""
        if not session.stepped_up:
            return Result("step_up_needed")
        if not self._provider_ready(provider):
            return Result("not_available")
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        expiry = self._nonce(nonce)
        who = self._identity(provider, id_token, nonce) if expiry is not None else None
        if who is None:
            return Result("wrong")
        if self.store.account_by_subjects(who[1]) is not None or provider in self.store.links_of(session.account_id):
            return Result("provider_cannot_use")
        if not self.store.spend_nonce(nonce, expiry) or not self.store.add_link(session.account_id, who[0], provider):
            return Result("wrong")
        self.store.delete_sessions_of(session.account_id, except_token_hash=session.token_hash)
        return Result("ok")

    def provider_unlink(self, session: Session, provider) -> Result:
        if not session.stepped_up:
            return Result("step_up_needed")
        if provider not in PROVIDERS:
            return Result("wrong")
        outcome = self.store.remove_link(session.account_id, provider)
        if outcome != "ok":
            return Result("last_method" if outcome == "last_method" else "wrong")
        self.store.delete_sessions_of(session.account_id, except_token_hash=session.token_hash)
        return Result("ok")

    def _methods(self, account: Account) -> list[str]:
        methods = set(self.store.links_of(account.account_id))
        if account.address_hash is not None:
            methods.add("address")
        return sorted(methods)

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
        return Session(row.account_id, token_hash, row.stepped_up_until > now)

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

    # address change ----------------------------------------------------------------

    def change_address_start(self, session: Session, new_address, network: str) -> Result:
        """Needs a recent step-up, which proved the old address (or, for an account with no
        address, its provider); this sends a code to the new one. A new address that already has an account gets the same reply and no code."""
        if not session.stepped_up:
            return Result("step_up_needed")
        norm = normalise_address(new_address)
        if norm is None:
            return Result("invalid_address")
        candidates = self.keys.candidate_hashes(norm)
        refused = self._admit("change", network, account_id=session.account_id, address_hash=candidates[0])
        if refused:
            return refused
        taken = self.store.account_by_hashes(candidates) is not None
        return self._open_challenge("change", candidates[0], session.account_id, None if taken else norm)

    def change_address_finish(self, session: Session, challenge, code, network: str, new_address) -> Result:
        """The new address is typed again here, so it can be kept, sealed, for sending; it must
        be the one the code was sent to. A move to a new address also ends any recovery waiting."""
        if not session.stepped_up:
            return Result("step_up_needed")
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        norm = normalise_address(new_address)
        if norm is None:
            return Result("wrong")
        checked = self._check(challenge, "change", code, account_id=session.account_id, address_hash=self.keys.address_hash(norm))
        if checked is None or not self._spend(checked):
            return Result("wrong")
        if not self.store.set_address_hash(session.account_id, checked.address_hash):
            return Result("wrong")
        if self.store.pending_of(session.account_id) is not None:
            self._end_recovery(session.account_id)
        if self.contacts is not None:
            self.contacts.put(session.account_id, norm)
        self.store.delete_sessions_of(session.account_id, except_token_hash=session.token_hash)
        return Result("ok")

    # recovery -----------------------------------------------------------------------

    def recovery_code_make(self, session: Session) -> Result:
        """A new recovery code for the account, shown once; it replaces any earlier one and ends
        any recovery waiting, since the owner is here and has just chosen. It is kept only as a
        keyed hash."""
        if not session.stepped_up:
            return Result("step_up_needed")
        if self.store.pending_of(session.account_id) is not None:
            self._end_recovery(session.account_id)
        code = secrets.token_urlsafe(16)
        self.store.put_recovery_key(session.account_id, self.keys.secret_hash("recovery", code), self.today().isoformat())
        return Result("ok", data={"recovery_code": code})

    def recovery_start(self, recovery_code, new_address, network: str) -> Result:
        """Starts a recovery for a person who lost their address: the recovery code names the
        account, and a code is sent to the new address. The challenge is bound to that recovery
        code, so it can be proved only while that same code is still the account's. The reply is
        the same whether or not the recovery code is right, the new address is free, or the account
        has an address on file to warn, so it tells a stranger nothing."""
        norm = normalise_address(new_address)
        if norm is None:
            return Result("invalid_address")
        candidates = self.keys.candidate_hashes(norm)
        refused = self._admit("change", network, address_hash=candidates[0])
        if refused:
            return refused
        known = isinstance(recovery_code, str) and 0 < len(recovery_code) <= 80
        found = self.store.account_by_recovery_key(self.keys.secret_candidates("recovery", recovery_code)) if known else None
        account_id, used_key = found if found else (None, None)
        usable = (
            account_id is not None and self.contacts is not None and self.contacts.get(account_id) is not None
            and self.store.account_by_hashes(candidates) is None and self.store.pending_of(account_id) is None
        )
        return self._open_challenge("recovery", candidates[0], account_id, norm if usable else None, bound=used_key)

    def recovery_prove(self, challenge, code, new_address, network: str) -> Result:
        """The new address is proved. In one transaction the recovery code is spent, the seven-day
        wait is written and a replacement code is stored; then the old address is told, with a
        cancel code. If the mail provider does not accept that notice the recovery is taken back
        and does not start; the move never takes effect without it. The replacement code is shown once."""
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        norm = normalise_address(new_address)
        if norm is None or self.contacts is None:
            return Result("wrong")
        checked = self._check(challenge, "recovery", code, address_hash=self.keys.address_hash(norm))
        if checked is None or checked.account_id is None or checked.bound is None:
            return Result("wrong")
        account_id = checked.account_id
        old_address = self.contacts.get(account_id)
        if old_address is None or not self.store.has_recovery_key(account_id):
            return Result("wrong")
        cancel_code = secrets.token_urlsafe(16)
        new_code = secrets.token_urlsafe(16)
        cancel_hash = self.keys.secret_hash("cancel", cancel_code)
        new_key = self.keys.secret_hash("recovery", new_code)
        today = self.today().isoformat()
        effective_on = (self.today() + timedelta(days=self.limits.recovery_wait_days + 1)).isoformat()
        # Reserve first: one transaction that checks everything. Only the attempt that wins it
        # goes on to write the waiting address and send the notice, so a losing attempt can never
        # send a notice whose cancel code does not work or touch the winner's rows.
        if not self.store.begin_recovery(
            account_id, checked.bound, new_key, today, self.keys.candidate_hashes(norm), checked.address_hash,
            cancel_hash, effective_on,
        ):
            return Result("wrong")
        self.contacts.put_pending(account_id, norm)
        try:
            self.mailer.send_notice(old_address, "recovery_started", {"cancel_code": cancel_code, "effective_on": effective_on})
        except Exception:  # noqa: BLE001 - the address and codes must not reach a log
            logger.warning("a recovery notice could not be sent")
            if self.store.undo_recovery(account_id, cancel_hash, new_key, checked.bound, today):
                self.contacts.forget_pending(account_id)
            return Result("send_failed")
        # Until the notice is accepted the waiting move never takes effect, even after a crash.
        self.store.mark_notified(account_id, cancel_hash)
        self._spend(checked)
        return Result("ok", data={"recovery_code": new_code, "effective_on": effective_on})

    def recovery_cancel(self, address, cancel_code, network: str) -> Result:
        """The owner stops a recovery with the cancel code from the notice and the old address.
        No mail is sent here, so no sending limit can be used up to stop an owner. The recovery
        code, which the one who started the recovery holds, is ended too."""
        if not self._allow("finish_net", self.keys.network_key(network), 900, self.limits.finishes_per_network_15min):
            return Result("throttled")
        norm = normalise_address(address)
        account = self.store.account_by_hashes(self.keys.candidate_hashes(norm)) if norm else None
        pending = self.store.pending_of(account.account_id) if account else None
        given = cancel_code if isinstance(cancel_code, str) and 0 < len(cancel_code) <= 80 else ""
        held = self.keys.secret_candidates("cancel", given)
        if pending is None or pending[1] not in held:
            return Result("wrong")
        self._end_recovery(account.account_id)
        return Result("ok")

    def recovery_cancel_signed_in(self, session: Session) -> Result:
        """A signed-in owner stops a recovery waiting on their account."""
        if self.store.pending_of(session.account_id) is None:
            return Result("wrong")
        self._end_recovery(session.account_id)
        return Result("ok")

    def _end_recovery(self, account_id: str) -> None:
        """Ends a waiting recovery and the recovery code that was handed out with it."""
        self.store.delete_pending(account_id)
        if self.contacts is not None:
            self.contacts.forget_pending(account_id)
        self.store.delete_recovery_key(account_id)

    def _recovery_banner(self, account_id: str) -> dict | None:
        pending = self.store.pending_of(account_id)
        return {"effective_on": pending[2]} if pending else None

    def _apply_due_recoveries(self) -> None:
        """Carries out each recovery whose day has come: the account moves to the new address,
        every session ends, and the person signs in there. The move is made only if the waiting
        row is still there, so a cancel that got in first wins. Called whenever an address is
        looked up, so neither address finds an account that has already moved."""
        today = self.today().isoformat()
        for account_id, new_hash in self.store.due_pending(today):
            address = self.contacts.pending(account_id) if self.contacts is not None else None
            if self.store.apply_pending(account_id, new_hash, today):
                if address is not None and self.contacts is not None:
                    self.contacts.put(account_id, address)
                self.store.delete_sessions_of(account_id)
                if self.contacts is not None:
                    self.contacts.forget_pending(account_id)

    def _sweep_contacts(self) -> None:
        """Removes any kept address whose account is gone, such as after a crash between the two
        files or a contact file restored apart from the account file."""
        if self.contacts is None:
            return
        for account_id in self.contacts.account_ids():
            if self.store.account(account_id) is None:
                self.contacts.forget(account_id)

    # what an account holds, and deletion ------------------------------------------------

    def me(self, session: Session) -> dict:
        account = self.store.account(session.account_id)
        return {
            "signed_in": True,
            "refill_day": account.refill_day,
            "age_band": account.age_band,
            "sign_in_methods": self._methods(account),
            "has_recovery_code": self.store.has_recovery_key(account.account_id),
            "recovery_pending": self._recovery_banner(account.account_id),
        }

    def export(self, session: Session) -> Result:
        """What the account holds today. It grows as the shelf and the token history are
        added; it never includes a live code."""
        if not session.stepped_up:
            return Result("step_up_needed")
        account = self.store.account(session.account_id)
        return Result("ok", data={
            "day_created": account.day_created,
            "refill_day": account.refill_day,
            "week_last_used": account.week_last_used,
            "age_band": account.age_band,
            "sign_in_methods": self._methods(account),
        })

    def delete_account(self, session: Session) -> Result:
        if not session.stepped_up:
            return Result("step_up_needed")
        expires = (self.today() + timedelta(days=self.limits.ledger_days)).isoformat()
        account = self.store.account(session.account_id)
        if self.contacts is not None:
            self.contacts.forget(session.account_id)
        self.store.delete_account(session.account_id, ledger_hash(session.account_id), expires)
        if account is not None and account.address_hash is not None:
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
        self._sweep_contacts()
        return len(gone)
