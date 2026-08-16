"""SS5.1 segment 1 - Identity & register: the deployed prompt's proven
voice prose (craft blocks - speaking model, register rules, native
measure, witness stance).

Voice Rebuild Phase 0.3 (2026-08-08): generalized from a Desert-only
module (which imported DESERT_CRAFT directly) to read ctx["craft"] -
each world's assembler supplies its own craft table via build_context().
Behavior-neutral for Desert: DESERT_CRAFT's identity_register paragraphs
were already exactly (1,2,7,8,9,10,11,12,17) in that list order, so
filtering by segment in table order (below) reproduces the prior
explicit-tuple selection exactly - verified by direct comparison before
this change shipped."""


def render(ctx) -> str:
    blocks = [b["text"] for b in ctx["craft"] if b["segment"] == "identity_register"]
    return "\n\n".join(blocks)


SEGMENT = {"name": "identity_register", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "voice_profile (speaking_model, identity, native_measure, traits) via this world's craft table, identity_register-tagged blocks, in table order"}
