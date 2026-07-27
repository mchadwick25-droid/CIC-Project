"""§5.1 segment 7 - the session layer (runtime-supplied): Priority-Layer
view, table composition, other seated worlds' term lists (for
divergence, §6.5). Loaded once, held all session. Rendered by the
runtime, not this view - the entry exists so the manifest specifies the
WHOLE assembly."""


def render(ctx):
    return None


SEGMENT = {"name": "session_layer", "cache_stability": "session",
           "eviction_priority": 3, "render": render,
           "sources": "runtime: table composition; priority layer; other seated worlds' term lists"}
