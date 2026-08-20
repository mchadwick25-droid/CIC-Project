"""Session codes (Artifact-3 SS3): 128-bit CSPRNG, Crockford base32 (26
chars, grouped for humans), stored hashed (SHA-256 - codes are high-entropy
so no slow hash is needed), constant-time compared. Possession = resume +
transcript + deletion.
"""
import hashlib
import hmac
import secrets

_ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"  # Crockford base32 - excludes I, L, O, U
_SYMBOL_COUNT = 26  # ceil(128 bits / 5 bits-per-symbol)
_GROUP_SIZES = [4, 4, 4, 4, 4, 4, 2]  # 26 chars, human-groupable


def _crockford_encode(data: bytes, length: int) -> str:
    n = int.from_bytes(data, "big")
    chars = []
    for _ in range(length):
        n, remainder = divmod(n, 32)
        chars.append(_ALPHABET[remainder])
    return "".join(reversed(chars))


def generate_code() -> str:
    raw = secrets.token_bytes(16)  # 128 bits
    symbols = _crockford_encode(raw, _SYMBOL_COUNT)
    groups, i = [], 0
    for size in _GROUP_SIZES:
        groups.append(symbols[i : i + size])
        i += size
    return "-".join(groups)


def hash_code(code: str) -> str:
    normalized = code.replace("-", "").upper()
    return hashlib.sha256(normalized.encode("ascii")).hexdigest()


def codes_match(candidate: str, code_hash: str) -> bool:
    """Constant-time: a wrong code and an unknown session must be
    indistinguishable in timing (Artifact-6 threat model)."""
    return hmac.compare_digest(hash_code(candidate), code_hash)
