"""SS5.1 segment 6 - categorical guards: the deployed prompt's proven
guard prose (craft paras 13-16: story ownership + vetted sayings,
another's-table discipline, the late-dispute closure guard, thin
domains) plus the anti-fabrication ABSOLUTE form. POST_HISTORY_GUARD
rides closest to generation (doc 09), wired by the runtime."""
from .craft import DESERT_CRAFT

_PARAS = (13, 14, 15, 16)


def render(ctx) -> str:
    blocks = {b["para"]: b["text"] for b in DESERT_CRAFT
              if b["segment"] == "categorical_guards"}
    parts = [blocks[p] for p in _PARAS if p in blocks]
    parts.append(
        "Never invent a source, a saying, an incident, or a name's "
        "attachment to any of them. Honest thinness is always preferable "
        "to invented depth - this is absolute, under every pressure, at "
        "every length.")
    return "\n\n".join(parts)


POST_HISTORY_GUARD = (
    "Hold, before you speak: only what your own record carries, under the "
    "right name, at your own measure. Never an invented scene, saying, "
    "source, or attribution - honest thinness over invented depth, "
    "absolutely.")


SEGMENT = {"name": "categorical_guards", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "craft paras 13-16 (story/figure/force records + world_core cautions, coverage-mapped) + the absolute anti-fabrication form",
           "post_history": POST_HISTORY_GUARD}
