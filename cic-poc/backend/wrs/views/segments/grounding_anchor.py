"""SS5.1 segment 4 - the grounding anchor: a short-sentence-register
wrapper (Desert's own craft prose) around a DERIVED list (CO-016's
mechanism) from source records where attribution_status = genuine.

Voice Rebuild Phase 0.3 (2026-08-08): generalized from a Desert-only
module (which hardcoded its wrapper sentences directly - confirmed
present verbatim in Papnoute's deployed prompt at line 45, and
confirmed ABSENT from Chloe's/PAHC's deployed prompt entirely, so
reusing it unconditionally for every world would have injected
Desert-authored prose into worlds that don't have this content today)
to read ctx["craft"]'s grounding_anchor-tagged blocks for the wrapper
text. A world whose craft table has no such block renders NOTHING AT
ALL for this segment - confirmed by testing against PAHC's real source
records, not assumed: rendering the derived list without its wrapper
produced an orphaned fragment ("The genuinely attributed core of that
record is small and known to us: ...") with no framing sentence, which
is worse than omitting the segment. A wrapper is required for any
content to render."""
from ._common import voice  # noqa: F401  (kept: shared strip helper for future per-world use)


def render(ctx) -> str:
    blocks = {b.get("role"): b["text"] for b in ctx.get("craft", [])
             if b["segment"] == "grounding_anchor"}
    if "open" not in blocks:
        return ""

    genuine = []
    for sid in sorted(ctx["sources"]):
        s = ctx["sources"][sid]
        if s.get("attribution_status") != "genuine":
            continue
        author = s.get("work_author") or ""
        title = s.get("work_title") or s.get("title") or ""
        if author or title:
            genuine.append(f"{author}{' - ' if author and title else ''}{title}")

    parts = [blocks["open"]]
    if genuine:
        parts.append("The genuinely attributed core of that record is small "
                     "and known to us: " + "; ".join(genuine[:8]) + ".")
    if "close" in blocks:
        parts.append(blocks["close"])
    return " ".join(parts)


SEGMENT = {"name": "grounding_anchor", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "this world's craft table (grounding_anchor-tagged wrapper text) + source records (attribution_status = genuine), derived list"}
