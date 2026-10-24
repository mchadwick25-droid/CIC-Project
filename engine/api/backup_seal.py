"""Encryption of the accounts files before they leave the disk.

Backups are uploaded to object storage. The accounts file and the contact file
are sealed first, under a key of their own (CIC_ACCOUNTS_BACKUP_KEY, with a key
id) that is held apart from the address, session, contact and shelf keys, so a
copy of the bucket alone reads nothing. A sealed backup reads
"CICB1", the key id's length and the key id, a 12 byte nonce, then AES-256-GCM
ciphertext bound to the label of the file it holds, so one file cannot be
passed off as another. A previous key stays listed until the last backup made
under it has aged out of the bucket.
"""
import re
import secrets
from dataclasses import dataclass

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from engine.api.contact_cipher import _derive

MAGIC = b"CICB1"
MIN_SECRET_LENGTH = 32
MAX_BYTES = 512 * 1024 * 1024
_KEY_ID = re.compile(r"[a-z0-9]{1,8}")
_LABEL = re.compile(r"[a-z0-9_-]{1,32}")


class BackupKeyError(Exception):
    """A backup key that is missing, too short, reused, or badly named."""


class BackupOpenError(Exception):
    """A sealed backup that cannot be opened: wrong key, wrong label, damaged or not sealed."""


@dataclass(frozen=True)
class PreviousBackupKey:
    key_id: str
    secret: str


def parse_previous(spec: str | None) -> list[PreviousBackupKey]:
    """'id:secret,id:secret' -> keys; empty -> none."""
    keys: list[PreviousBackupKey] = []
    for part in (spec or "").split(","):
        part = part.strip()
        if not part:
            continue
        key_id, sep, secret = part.partition(":")
        if not sep:
            raise BackupKeyError("a previous backup key must be id:secret")
        keys.append(PreviousBackupKey(key_id, secret))
    return keys


class BackupSealer:
    def __init__(self, secret: str, *, key_id: str = "b1", previous: list[PreviousBackupKey] | tuple = (),
                 other_secrets: tuple[str, ...] = ()):
        secrets_in_use = [secret] + [p.secret for p in previous]
        if any(not isinstance(s, str) or len(s) < MIN_SECRET_LENGTH for s in secrets_in_use):
            raise BackupKeyError(f"each backup key must be at least {MIN_SECRET_LENGTH} characters")
        ids = [key_id] + [p.key_id for p in previous]
        if len(set(ids)) != len(ids) or not all(_KEY_ID.fullmatch(i) for i in ids):
            raise BackupKeyError("backup key ids must be distinct, lower case letters and digits, up to 8 characters")
        if len(set(secrets_in_use)) != len(secrets_in_use) or any(s in other_secrets for s in secrets_in_use):
            raise BackupKeyError("the backup keys must differ from each other and from every other accounts key")
        self.key_id = key_id
        self._keys = {key_id: AESGCM(_derive(secret, key_id, "backup"))}
        self._keys.update({p.key_id: AESGCM(_derive(p.secret, p.key_id, "backup")) for p in previous})

    @staticmethod
    def _context(label: str) -> bytes:
        if not _LABEL.fullmatch(label):
            raise ValueError("a backup label is lower case letters, digits, hyphens and underscores")
        return b"cic-backup|" + label.encode()

    def seal(self, data: bytes, label: str) -> bytes:
        if len(data) > MAX_BYTES:
            raise ValueError("this file is too large to seal in memory")
        nonce = secrets.token_bytes(12)
        key_id = self.key_id.encode()
        return MAGIC + bytes([len(key_id)]) + key_id + nonce + self._keys[self.key_id].encrypt(nonce, data, self._context(label))

    def open(self, blob: bytes, label: str) -> bytes:
        if not blob.startswith(MAGIC) or len(blob) < len(MAGIC) + 1:
            raise BackupOpenError("not a sealed backup")
        size = blob[len(MAGIC)]
        start = len(MAGIC) + 1
        key = self._keys.get(blob[start:start + size].decode("ascii", "replace"))
        body = blob[start + size:]
        if key is None or len(body) < 12 + 16:
            raise BackupOpenError("this backup was sealed under a key that is not listed")
        try:
            return key.decrypt(body[:12], body[12:], self._context(label))
        except InvalidTag:
            raise BackupOpenError("this backup does not open under that key and label") from None


def from_env(env: dict, other_secrets: tuple[str, ...] = ()) -> BackupSealer:
    """The sealer for the keys in the environment. A missing or unusable key raises BackupKeyError."""
    return BackupSealer(
        env.get("CIC_ACCOUNTS_BACKUP_KEY", ""), key_id=env.get("CIC_ACCOUNTS_BACKUP_KEY_ID", "b1"),
        previous=parse_previous(env.get("CIC_ACCOUNTS_BACKUP_KEYS_PREVIOUS")), other_secrets=other_secrets,
    )
