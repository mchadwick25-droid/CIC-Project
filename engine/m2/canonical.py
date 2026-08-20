"""Canonical JSON + hashing, shared by every compiled artifact and the
manifest itself. One serialization rule, used everywhere, so "byte-identical
on a second compile" (Artifact-2 SS3) is a property of this module alone."""
import hashlib
import json


def canonical_json(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_prefixed(data: bytes) -> str:
    return f"sha256:{sha256_hex(data)}"
