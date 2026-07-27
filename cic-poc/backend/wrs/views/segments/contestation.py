"""§5.1 segment 3 - contestation (contested_claim renders): what we hold
when pushed, what we concede, how we characteristically respond. New as
always-present material - the voice ENACTS its character under
disagreement instead of stating it (doc 10's headline finding)."""
from ._common import voice


def render(ctx) -> str:
    parts = []
    for cid in sorted(ctx["claims"]):
        c = ctx["claims"][cid]
        parts.append(
            f"What we hold: {voice(c['claim'])} When pushed: "
            f"{voice(c['pressure_response'])} What we concede: "
            f"{voice(c['concedes'])}")
    return "\n\n".join(parts)


SEGMENT = {"name": "contestation", "cache_stability": "static",
           "eviction_priority": 2, "render": render,
           "sources": "contested_claim records (claim, pressure_response, concedes)"}
