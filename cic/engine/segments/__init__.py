"""S5.2 - the §5.1 segment registry (Pass 1 §5.1's table, made literal).

Each module exports SEGMENT = {name, cache_stability, eviction_priority,
render(ctx) -> str | None}. Static segments render assembled prose from
records; the session and turn layers are runtime-supplied and render
None here - their entries exist so the manifest carries the WHOLE
specified assembly, not just its static half. Order in ASSEMBLY_ORDER is
§5.1's own: change frequency (static -> session -> turn), the cache-
correct and quality-correct ordering. The quick-reach segment is S5.3's
(R7, gated on the B-PARROT tolerance per F3) and is deliberately absent.
"""
from . import (identity, world_ground, contestation, grounding_anchor,
               quick_reach, demonstrations, guards, session_layer, turn_layer)

ASSEMBLY_ORDER = [
    identity.SEGMENT,
    world_ground.SEGMENT,
    contestation.SEGMENT,
    grounding_anchor.SEGMENT,
    quick_reach.SEGMENT,
    demonstrations.SEGMENT,
    guards.SEGMENT,
    session_layer.SEGMENT,
    turn_layer.SEGMENT,
]
