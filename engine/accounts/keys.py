"""The address, hashed under a server secret, and the other keyed values.

A sign-in address is normalised, then hashed with HMAC-SHA256 under
CIC_ACCOUNTS_KEY. The stored value carries the id of the key that made it
("k1:..."), so a new key can be introduced while the old one still verifies
until its retirement date; a value is re-written under the current key the next
time the person signs in and types the address. A second, different secret
signs cookies and binds sign-in codes. The address itself is never stored.
"""
import hashlib
import hmac
import re
import unicodedata
from dataclasses import dataclass
from datetime import date
from typing import Callable

MIN_KEY_LENGTH = 32
_KEY_ID = re.compile(r"[a-z0-9]{1,8}")
_DOMAIN = re.compile(r"[^\s@]+")


class AccountsKeyError(Exception):
    """A key that is missing, too short, reused, or badly named."""


@dataclass(frozen=True)
class PreviousKey:
    key_id: str
    secret: str
    retire_on: date


def parse_previous(spec: str | None) -> list[PreviousKey]:
    """'id:secret:retire-date,id:secret:retire-date' -> keys; empty -> none."""
    keys: list[PreviousKey] = []
    for part in (spec or "").split(","):
        part = part.strip()
        if not part:
            continue
        pieces = part.split(":")
        if len(pieces) != 3:
            raise AccountsKeyError("a previous key must be id:secret:retire-date")
        try:
            retire_on = date.fromisoformat(pieces[2])
        except ValueError as exc:
            raise AccountsKeyError("a previous key's retirement date must be YYYY-MM-DD") from exc
        keys.append(PreviousKey(pieces[0], pieces[1], retire_on))
    return keys


def normalise_address(raw) -> str | None:
    """The one form an address is hashed in: Unicode NFKC, trimmed, lower case.
    A plus tag is kept as typed. None when it cannot be an address."""
    if not isinstance(raw, str):
        return None
    text = unicodedata.normalize("NFKC", raw).strip().lower()
    if not text or len(text) > 254:
        return None
    if any(ch.isspace() or unicodedata.category(ch).startswith("C") for ch in text):
        return None
    local, sep, domain = text.rpartition("@")
    if not sep or not local or len(local) > 64 or "@" in local:
        return None
    if not _DOMAIN.fullmatch(domain) or "." not in domain:
        return None
    if domain.startswith(".") or domain.endswith(".") or ".." in domain:
        return None
    return text


class KeyRing:
    def __init__(
        self,
        address_key: str,
        session_key: str,
        *,
        key_id: str = "k1",
        previous: list[PreviousKey] | tuple = (),
        today: Callable[[], date] = date.today,
    ):
        for name, secret in (("address key", address_key), ("session key", session_key)):
            if not isinstance(secret, str) or len(secret) < MIN_KEY_LENGTH:
                raise AccountsKeyError(f"the {name} must be at least {MIN_KEY_LENGTH} characters")
        if address_key == session_key:
            raise AccountsKeyError("the address key and the session key must differ")
        ids = [key_id] + [p.key_id for p in previous]
        if len(set(ids)) != len(ids) or not all(_KEY_ID.fullmatch(i) for i in ids):
            raise AccountsKeyError("key ids must be distinct, lower case letters and digits, up to 8 characters")
        if any(p.secret == address_key or p.secret == session_key for p in previous):
            raise AccountsKeyError("a previous key must not repeat a current key")
        if any(len(p.secret) < MIN_KEY_LENGTH for p in previous) or len({p.secret for p in previous}) != len(previous):
            raise AccountsKeyError("previous keys must each be at least the minimum length and distinct")
        self._address_key = address_key
        self._session_key = session_key
        self.key_id = key_id
        self._previous = tuple(previous)
        self._today = today

    def _hash_with(self, key_id: str, secret: str, normalised: str) -> str:
        digest = hmac.new(secret.encode(), b"cic-accounts-address-v1|" + normalised.encode(), hashlib.sha256).hexdigest()
        return f"{key_id}:{digest}"

    def address_hash(self, address: str) -> str | None:
        """The hash under the current key, or None if it is not an address."""
        normalised = normalise_address(address)
        return None if normalised is None else self._hash_with(self.key_id, self._address_key, normalised)

    def candidate_hashes(self, address: str) -> list[str]:
        """The current hash first, then one per previous key not yet retired."""
        normalised = normalise_address(address)
        if normalised is None:
            return []
        out = [self._hash_with(self.key_id, self._address_key, normalised)]
        today = self._today()
        out += [self._hash_with(p.key_id, p.secret, normalised) for p in self._previous if today <= p.retire_on]
        return out

    def _provider_hash_with(self, key_id: str, secret: str, provider: str, issuer: str, subject: str) -> str:
        message = b"cic-accounts-provider-v1|" + "|".join((provider, issuer, subject)).encode()
        return f"{key_id}:{hmac.new(secret.encode(), message, hashlib.sha256).hexdigest()}"

    def provider_hash(self, provider: str, issuer: str, subject: str) -> str:
        """A provider's stable account id (issuer and subject) as a keyed value, so a
        stolen account file does not name anyone's Google or Apple account."""
        return self._provider_hash_with(self.key_id, self._address_key, provider, issuer, subject)

    def provider_candidates(self, provider: str, issuer: str, subject: str) -> list[str]:
        """The current hash first, then one per previous key not yet retired."""
        today = self._today()
        out = [self.provider_hash(provider, issuer, subject)]
        out += [self._provider_hash_with(p.key_id, p.secret, provider, issuer, subject) for p in self._previous if today <= p.retire_on]
        return out

    def is_current(self, stored_hash: str) -> bool:
        return stored_hash.startswith(self.key_id + ":")

    def mac(self, *parts: str) -> str:
        """A keyed value under the session key, for sign-in codes and cookies."""
        message = b"cic-accounts-mac-v1|" + b"|".join(p.encode() for p in parts)
        return hmac.new(self._session_key.encode(), message, hashlib.sha256).hexdigest()

    def network_key(self, network: str) -> str:
        """A network address as a keyed value, so a counter never holds the address."""
        return self.mac("network", network)[:32]

    def sign_cookie(self, token: str) -> str:
        return f"{token}.{self.mac('cookie', token)[:22]}"

    def open_cookie(self, cookie: str) -> str | None:
        """The token inside a cookie value, or None if the signature is wrong."""
        token, sep, tag = (cookie or "").rpartition(".")
        if not sep or not token or not hmac.compare_digest(tag, self.mac("cookie", token)[:22]):
            return None
        return token
