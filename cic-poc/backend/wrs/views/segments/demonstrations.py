"""§5.1 segment 5 - demonstrations (demonstration records selected
against the rubric). Pruned FIRST under token pressure (lowest eviction
rank), per the universal permanent-vs-evicted split. Selection: the
records whose trait_scores carry no 'weak' - the rubric doing the
selecting, not taste; capped at 3 (token pressure is the standing
reality this segment is first to yield to)."""
from ._common import voice


def _selected(demos: dict, cap: int = 3) -> list:
    keep = []
    for did in sorted(demos):
        d = demos[did]
        scores = [t.get("score") for t in d.get("trait_scores", [])]
        if scores and "weak" not in scores:
            keep.append(d)
    return keep[:cap]


def render(ctx) -> str:
    chosen = _selected(ctx.get("demonstrations", {}))
    if not chosen:
        return ""
    parts = ["How this voice actually moves, shown not described:"]
    for d in chosen:
        dialogue = voice(d.get("dialogue", ""))
        if dialogue:
            parts.append(dialogue)
    return "\n\n".join(parts) if len(parts) > 1 else ""


SEGMENT = {"name": "demonstrations", "cache_stability": "static",
           "eviction_priority": 5, "render": render,
           "sources": "demonstration records (rubric-selected: no weak trait scores; cap 3)"}
