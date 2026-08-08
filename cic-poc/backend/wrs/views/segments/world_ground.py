"""SS5.1 segment 2 - the world's own ground: the deployed prompt's
proven prose (horizon, gravities Primary-first, organizing vocabulary,
telos, living-tradition caution). The world's-own-words capsule listing
is NOT folded in: the deployed World Capsule file stays in place at the
swap (the runtime concatenation and the adjudicators' capsule evidence
are unchanged - the full fold-in lands at S6.5's compatibility
retirement, declared in the S5.2 artifact).

Voice Rebuild Phase 0.3 (2026-08-08): generalized from a Desert-only
module (which imported DESERT_CRAFT directly, and carried an unused
Desert-specific ORGANIZING_TERMS literal, removed - dead code, verified
unreferenced elsewhere) to read ctx["craft"]. Behavior-neutral for
Desert: DESERT_CRAFT's world_ground paragraphs were already exactly
(3,4,5,6,18,19) in that list order."""


def render(ctx) -> str:
    blocks = [b["text"] for b in ctx["craft"] if b["segment"] == "world_ground"]
    return "\n\n".join(blocks)


SEGMENT = {"name": "world_ground", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "world_core + gravity records via this world's craft table, world_ground-tagged blocks, in table order; capsule listing NOT folded in (capsule file stays deployed until S6.5)"}
