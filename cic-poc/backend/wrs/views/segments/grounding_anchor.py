"""§5.1 segment 4 - the grounding anchor, DERIVED (CO-016's mechanism):
generated from source records where attribution_status = genuine,
weighted toward the load-bearing evidence base - it can never again
exist for five worlds only as an unwritten convention."""
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
    listed = "; ".join(genuine[:8])
    parts = [
        "You draw only on this world's own vetted record. The sayings and "
        "lives as this world's own documents carry them. Never another "
        "world's more famous words. Never anything you cannot feel the "
        "weight of in your own record.",
    ]
    if listed:
        parts.append(f"The genuinely attributed core of that record: {listed}.")
    parts.append("Where your record is thin, the thinness is spoken, not filled.")
    return " ".join(parts)


SEGMENT = {"name": "grounding_anchor", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "source records (attribution_status = genuine), derived"}
