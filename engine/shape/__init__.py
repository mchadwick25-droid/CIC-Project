"""The engine's shape segment: how every Representative converses. It is
built from the fleet_voice record, is byte-identical for every world, and is
the first cached system block of every voice call (engine.m4.voice_request).

SHAPE_HASH pins it. Any change to the segment changes its hash, and the
segment refuses to load until SHAPE_HASH is updated with it, so a change to
how every Representative converses is always a deliberate engine change.
Admission results record the hash they ran under (engine.m3.admission_conform).
"""
from functools import lru_cache

from engine.m1.loader import load_fleet_records
from engine.m2.canonical import sha256_prefixed

SHAPE_HASH = "sha256:fc9a453f20737164fab3b1826220e656f38a820ebf886927decd6a7924c23a68"


class ShapeMismatch(RuntimeError):
    pass


def build_shape(fleet: dict) -> str:
    """The segment's text from the fleet records; empty when the fleet has no
    fleet_voice record."""
    record = next((r for _, r in sorted(fleet.items()) if r.get("record_type") == "fleet_voice"), None)
    if record is None:
        return ""
    segments: list[str] = []

    def emit(header: str, body: str | None) -> None:
        if body and body.strip():
            segments.append(f"## {header}\n\n{body.strip()}\n")

    statements = sorted(record.get("register_statements") or [], key=lambda s: s["number"])
    if statements:
        body = "\n".join(f"{s['number']}. {s['statement']}" for s in statements)
        hold = (record.get("register_hold") or "").strip()
        emit("Register", f"{body}\n\n{hold}" if hold else body)
    emit("Pronoun rule", record.get("pronoun_rule"))
    emit("Citation contract", record.get("citation_contract"))
    emit("Stories and quotes", record.get("story_quote_reach"))
    emit("Limit discipline", record.get("limit_discipline"))
    return "\n".join(segments)


def shape_hash(text: str) -> str:
    return sha256_prefixed(text.encode("utf-8"))


@lru_cache(maxsize=1)
def shape_text() -> str:
    """The segment every voice call sends, verified against SHAPE_HASH."""
    text = build_shape(load_fleet_records())
    actual = shape_hash(text)
    if actual != SHAPE_HASH:
        raise ShapeMismatch(f"the shape segment hashes to {actual}, but engine/shape pins {SHAPE_HASH}; "
                            "a change to the segment updates SHAPE_HASH with it")
    return text
