"""SS5.1 segment 2 - the world's own ground: the deployed prompt's
proven prose (craft paras 3,4,5,6,18,19 - horizon, gravities
Primary-first, organizing vocabulary, telos, living-tradition caution)
plus today's capsule depth folded in (the world's-own-words listing -
every remaining term's voice_surface, line per term)."""
from ._common import voice
from .craft import DESERT_CRAFT

_PARAS = (3, 4, 5, 6, 18, 19)
# the five ORGANIZING terms already carried in prose by para 6
ORGANIZING_TERMS = ["desertlex001", "desertlex002", "desertlex003",
                    "desertlex004", "desertlex005"]


def render(ctx) -> str:
    blocks = {b["para"]: b["text"] for b in DESERT_CRAFT
              if b["segment"] == "world_ground"}
    parts = [blocks[p] for p in _PARAS if p in blocks]
    words = [f"- {t['term']}: {voice(t['voice_surface'])}"
             for tid, t in sorted(ctx["terms"].items())
             if tid not in ORGANIZING_TERMS and t.get("voice_surface")]
    parts.insert(4, "The rest of the world's own words, as we speak them:\n"
                 + "\n".join(words))
    return "\n\n".join(parts)


SEGMENT = {"name": "world_ground", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "world_core + gravity records via craft paras 3-6,18,19 (coverage-mapped); remaining terms' voice_surface listed at capsule depth"}
