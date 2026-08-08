"""SS5.1 segment 3 - contestation, NEW as always-present material: what
we hold when pushed, what we concede, how we characteristically respond.
Voice-register craft renders per contested_claim record. R-reviewed
against the records at the S5.2 checkpoint; a claim record change
re-opens its render.

Voice Rebuild Phase 0.3 (2026-08-08): generalized from a Desert-only
module (which hardcoded its six desertclaim renders directly) to read
ctx["claim_renders"] - each world's assembler supplies its own claim-id
-> prose dict via build_context(). Desert's own six renders moved to
craft.py's DESERT_CLAIM_RENDERS so Desert's own render is unchanged."""


def render(ctx) -> str:
    renders = ctx.get("claim_renders", {})
    parts = ["Where the world is pressed, this is how it stands:"]
    for cid in sorted(ctx["claims"]):
        if cid in renders:
            parts.append(renders[cid])
    return "\n\n".join(parts) if len(parts) > 1 else ""


SEGMENT = {"name": "contestation", "cache_stability": "static",
           "eviction_priority": 2, "render": render,
           "sources": "contested_claim records (claim, pressure_response, concedes) via this world's claim_renders - voice craft renders, R-reviewed"}
