"""§5.1 segment 8 - the turn layer (runtime-supplied): retrieved
voice_surface bodies (deep material only), the pending_guidance queue
head, reactive-turn guidance, the private directive. The only uncached
segment, kept deliberately small."""


def render(ctx):
    return None


SEGMENT = {"name": "turn_layer", "cache_stability": "turn",
           "eviction_priority": 4, "render": render,
           "sources": "runtime: retrieval, guidance queue head, reactive guidance, private directive"}
