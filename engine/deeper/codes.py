"""Code generation, normalising, hashing and constant-time comparison.

A code is 20 characters from a 32-character alphabet with no 0, O, 1 or I,
so it carries 100 bits and can be read aloud. It is shown in groups of four.
Only its SHA-256 is stored; with 100 random bits there is nothing to
brute-force, so no pepper is needed.
"""
import hashlib
import hmac
import re
import secrets

ALPHABET = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
CODE_LENGTH = 20
GROUP_SIZE = 4

_SEPARATORS = re.compile(r"[\s\-]+")
_ALPHABET_SET = frozenset(ALPHABET)


def generate() -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


def normalize(raw: str | None) -> str | None:
    """The canonical form of whatever a person typed or pasted, or None if it
    cannot be a code. Case and spacing are forgiven; nothing else is."""
    if not isinstance(raw, str):
        return None
    code = _SEPARATORS.sub("", raw).upper()
    if len(code) != CODE_LENGTH or not _ALPHABET_SET.issuperset(code):
        return None
    return code


def display(code: str) -> str:
    return " ".join(code[i : i + GROUP_SIZE] for i in range(0, len(code), GROUP_SIZE))


def hash_code(code: str) -> str:
    return hashlib.sha256(code.encode("ascii")).hexdigest()


def hashes_match(stored_hash: str, candidate_hash: str) -> bool:
    return hmac.compare_digest(stored_hash.encode("ascii"), candidate_hash.encode("ascii"))


def redact(raw: str | None) -> str:
    """What may appear in a log line: the first four characters at most."""
    code = normalize(raw)
    return f"{code[:GROUP_SIZE]}..." if code else "invalid"
