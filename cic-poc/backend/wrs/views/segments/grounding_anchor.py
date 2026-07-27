"""SS5.1 segment 4 - the grounding anchor, DERIVED (CO-016's mechanism)
from source records where attribution_status = genuine; short-sentence
voice register (the S5.2 G gate's second catch: the listing sentence
ran FK 15.4 as one clause)."""
from ._common import voice


def render(ctx) -> str:
    genuine = []
    for sid in sorted(ctx["sources"]):
        s = ctx["sources"][sid]
        if s.get("attribution_status") != "genuine":
            continue
        author = s.get("work_author") or ""
        title = s.get("work_title") or s.get("title") or ""
        if author or title:
            genuine.append(f"{author}{' - ' if author and title else ''}{title}")
    parts = [
        "You draw only on this world's own vetted record. The sayings and "
        "lives as our own documents carry them. Never another world's more "
        "famous words.",
    ]
    if genuine:
        parts.append("The genuinely attributed core of that record is small "
                     "and known to us: " + "; ".join(genuine[:8]) + ".")
    parts.append("Where the record is thin, we say the thinness. We do not "
                 "fill it.")
    return " ".join(parts)


SEGMENT = {"name": "grounding_anchor", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "source records (attribution_status = genuine), derived"}
