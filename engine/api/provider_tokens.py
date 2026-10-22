"""Checks a Google or Apple sign-in token.

The page signs in with the provider's own button and sends back a signed ID
token. This module proves the provider made it for this app and for the nonce
the server issued: the signature against the provider's published keys, the
issuer, the audience, the expiry and the nonce. Only RS256 is accepted. The
token's email is never read; the only value kept is the provider's own stable
account id (the subject). Public keys are fetched over HTTPS and cached.
"""
import base64
import json
import logging
import threading
import time
import urllib.request
from typing import Callable

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers

logger = logging.getLogger("cic.accounts")

KEYS_URL = {
    "google": "https://www.googleapis.com/oauth2/v3/certs",
    "apple": "https://appleid.apple.com/auth/keys",
}
ISSUERS = {
    "google": ("https://accounts.google.com", "accounts.google.com"),
    "apple": ("https://appleid.apple.com",),
}
CANONICAL_ISSUER = {"google": "https://accounts.google.com", "apple": "https://appleid.apple.com"}

KEYS_TTL_SECONDS = 3600
REFETCH_FLOOR_SECONDS = 300
CLOCK_SKEW_SECONDS = 60
MAX_KEYS_BYTES = 200_000
MAX_SUBJECT_LENGTH = 255


def fetch_keys(url: str) -> dict:
    """The provider's published key set, over HTTPS, small and with a short timeout."""
    if not url.startswith("https://"):
        raise ValueError("provider keys are fetched over https only")
    with urllib.request.urlopen(url, timeout=5) as response:  # noqa: S310 - fixed https urls above
        body = response.read(MAX_KEYS_BYTES + 1)
    if len(body) > MAX_KEYS_BYTES:
        raise ValueError("provider key set too large")
    return json.loads(body)


def _b64(part: str) -> bytes:
    return base64.urlsafe_b64decode(part + "=" * (-len(part) % 4))


class ProviderVerifier:
    """client_ids maps a provider name to the id of our app at that provider; a provider
    with none is not available."""

    def __init__(
        self,
        client_ids: dict[str, str],
        *,
        fetch: Callable[[str], dict] = fetch_keys,
        clock: Callable[[], float] = time.time,
    ):
        self._client_ids = {p: c for p, c in client_ids.items() if p in KEYS_URL and c}
        self._fetch = fetch
        self._clock = clock
        self._lock = threading.Lock()
        self._cache: dict[str, tuple[float, dict[str, dict]]] = {}

    def available(self, provider: str) -> bool:
        return provider in self._client_ids

    def _key_for(self, provider: str, kid: str):
        now = self._clock()
        with self._lock:
            fetched_at, keys = self._cache.get(provider, (0.0, {}))
            stale = now - fetched_at > KEYS_TTL_SECONDS
            unknown = kid not in keys and now - fetched_at > REFETCH_FLOOR_SECONDS
            if stale or unknown:
                try:
                    listed = self._fetch(KEYS_URL[provider]).get("keys", [])
                except Exception:  # noqa: BLE001 - keep serving the keys already held
                    logger.warning("provider keys could not be fetched (provider=%s)", provider)
                    listed = None
                if listed is not None:
                    keys = {k["kid"]: k for k in listed if isinstance(k, dict) and isinstance(k.get("kid"), str)}
                    self._cache[provider] = (now, keys)
                elif stale:
                    keys = {}
            jwk = keys.get(kid)
        if not jwk or jwk.get("kty") != "RSA":
            return None
        return RSAPublicNumbers(int.from_bytes(_b64(jwk["e"]), "big"), int.from_bytes(_b64(jwk["n"]), "big")).public_key()

    def verify(self, provider: str, id_token: str, nonce: str) -> tuple[str, str] | None:
        if not self.available(provider) or not isinstance(nonce, str) or not nonce:
            return None
        try:
            head_b64, body_b64, sig_b64 = id_token.split(".")
            header = json.loads(_b64(head_b64))
            claims = json.loads(_b64(body_b64))
            signature = _b64(sig_b64)
        except (ValueError, TypeError):
            return None
        if not isinstance(header, dict) or not isinstance(claims, dict):
            return None
        if header.get("alg") != "RS256" or not isinstance(header.get("kid"), str):
            return None
        key = self._key_for(provider, header["kid"])
        if key is None:
            return None
        try:
            key.verify(signature, f"{head_b64}.{body_b64}".encode(), padding.PKCS1v15(), hashes.SHA256())
        except InvalidSignature:
            return None
        now = self._clock()
        exp, iat, subject = claims.get("exp"), claims.get("iat"), claims.get("sub")
        valid = (
            claims.get("iss") in ISSUERS[provider]
            and claims.get("aud") == self._client_ids[provider]
            and isinstance(exp, (int, float)) and not isinstance(exp, bool) and exp > now - CLOCK_SKEW_SECONDS
            and (iat is None or (isinstance(iat, (int, float)) and not isinstance(iat, bool) and iat <= now + CLOCK_SKEW_SECONDS))
            and claims.get("nonce") == nonce
            and isinstance(subject, str) and 0 < len(subject) <= MAX_SUBJECT_LENGTH
        )
        return (CANONICAL_ISSUER[provider], subject) if valid else None
