"""SS5.1 segment 2 - the world's own ground: the deployed prompt's
proven prose (craft paras 3,4,5,6,18,19 - horizon, gravities
Primary-first, organizing vocabulary, telos, living-tradition caution)
The world's-own-words capsule listing is NOT folded in: the deployed
World Capsule file stays in place at the swap (the runtime concatenation
and the adjudicators' capsule evidence are unchanged - the full fold-in
lands at S6.5's compatibility retirement, declared in the S5.2
artifact)."""
from .craft import DESERT_CRAFT

_PARAS = (3, 4, 5, 6, 18, 19)
# the five ORGANIZING terms already carried in prose by para 6
ORGANIZING_TERMS = ["desertlex001", "desertlex002", "desertlex003",
                    "desertlex004", "desertlex005"]


def render(ctx) -> str:
    blocks = {b["para"]: b["text"] for b in DESERT_CRAFT
              if b["segment"] == "world_ground"}
    return "\n\n".join(blocks[p] for p in _PARAS if p in blocks)


SEGMENT = {"name": "world_ground", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "world_core + gravity records via craft paras 3-6,18,19 (coverage-mapped); capsule listing NOT folded in (capsule file stays deployed until S6.5)"}
