"""Authenticated encryption for the contact file.

AES-256-GCM from the `cryptography` library, under a key derived from the
contact secret. Each seal has a fresh random nonce and is bound to the context
it was made for. A blob reads "<key id>:<base64 of nonce and ciphertext>"; the
key id picks which key opens it, so a new key can be introduced while old rows
still open, and each row is re-sealed under the current key the next time its
owner signs in by code.
"""
import base64
import re
import secrets
from dataclasses import dataclass

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

MIN_SECRET_LENGTH = 32
_KEY_ID = re.compile(r"[a-z0-9]{1,8}")


class ContactKeyError(Exception):
    """A contact key that is missing, too short, reused, or badly named."""


@dataclass(frozen=True)
class PreviousContactKey:
    key_id: str
    secret: str


def parse_previous(spec: str | None) -> list[PreviousContactKey]:
    """'id:secret,id:secret' -> keys; empty -> none."""
    keys: list[PreviousContactKey] = []
    for part in (spec or "").split(","):
        part = part.strip()
        if not part:
            continue
        key_id, sep, secret = part.partition(":")
        if not sep:
            raise ContactKeyError("a previous contact key must be id:secret")
        keys.append(PreviousContactKey(key_id, secret))
    return keys


def _derive(secret: str, key_id: str, purpose: str = "contact") -> bytes:
    return HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=f"cic-accounts-{purpose}-v1|{key_id}".encode()).derive(
        secret.encode()
    )


class ContactCipher:
    def __init__(self, secret: str, *, key_id: str = "c1", previous: list[PreviousContactKey] | tuple = (),
                 other_secrets: tuple[str, ...] = (), purpose: str = "contact"):
        secrets_in_use = [secret] + [p.secret for p in previous]
        if any(not isinstance(s, str) or len(s) < MIN_SECRET_LENGTH for s in secrets_in_use):
            raise ContactKeyError(f"each contact key must be at least {MIN_SECRET_LENGTH} characters")
        ids = [key_id] + [p.key_id for p in previous]
        if len(set(ids)) != len(ids) or not all(_KEY_ID.fullmatch(i) for i in ids):
            raise ContactKeyError("contact key ids must be distinct, lower case letters and digits, up to 8 characters")
        if len(set(secrets_in_use)) != len(secrets_in_use) or any(s in other_secrets for s in secrets_in_use):
            raise ContactKeyError("the contact keys must differ from each other and from the address and session keys")
        self.key_id = key_id
        self._keys = {key_id: AESGCM(_derive(secret, key_id, purpose))}
        self._keys.update({p.key_id: AESGCM(_derive(p.secret, p.key_id, purpose)) for p in previous})

    def encrypt(self, plaintext: str, context: str) -> str:
        nonce = secrets.token_bytes(12)
        sealed = self._keys[self.key_id].encrypt(nonce, plaintext.encode(), context.encode())
        return f"{self.key_id}:{base64.urlsafe_b64encode(nonce + sealed).decode()}"

    def decrypt(self, blob: str, context: str) -> str | None:
        key_id, sep, body = blob.partition(":")
        key = self._keys.get(key_id)
        if not sep or key is None:
            return None
        try:
            raw = base64.urlsafe_b64decode(body)
            return key.decrypt(raw[:12], raw[12:], context.encode()).decode()
        except (InvalidTag, ValueError):
            return None
