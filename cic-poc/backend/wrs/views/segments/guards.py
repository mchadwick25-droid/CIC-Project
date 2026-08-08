"""SS5.1 segment 6 - categorical guards: the deployed prompt's proven
guard prose (story ownership + vetted sayings, another's-table
discipline, the late-dispute closure guard, thin domains, the
anti-fabrication ABSOLUTE form). POST_HISTORY_GUARD rides closest to
generation (doc 09), wired by the runtime.

Voice Rebuild Phase 0.3 (2026-08-08): generalized from a Desert-only
module (which imported DESERT_CRAFT directly and hardcoded two
Desert-specific prose blocks - the fabrication-guard and
quotable-line-guard sentences, confirmed present verbatim in Papnoute's
own deployed prompt, not fleet-neutral text) to read ctx["craft"]
entirely - all categorical_guards-tagged blocks, in table order, no
prose left hardcoded in this shared module. Those two blocks moved into
DESERT_CRAFT itself (craft.py paras 20-21) so Desert's own render is
unchanged. The other five worlds' Phase 2 passes write their own
fabrication/quotable-line wording into their own craft tables - per
Design's own finding, this wording is NOT identical across worlds today
(Yausep/Marius carry near-verbatim "museum guide" wording, Theon a
reworded version, Papnoute its own).

POST_HISTORY_GUARD stays a single shared constant, unchanged - it
genuinely IS fleet-wide today (app/graph/nodes.py imports this exact
name and applies it to every migrated world). Moving to six per-world
guard exports is named Design work (§2 Layer 4), not this phase's."""


def render(ctx) -> str:
    blocks = [b["text"] for b in ctx["craft"] if b["segment"] == "categorical_guards"]
    return "\n\n".join(blocks)


POST_HISTORY_GUARD = (
    "Hold, before you speak: only what your own record carries, under the "
    "right name, at your own measure. Never an invented scene, saying, "
    "source, or attribution - honest thinness over invented depth, "
    "absolutely.")


SEGMENT = {"name": "categorical_guards", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "story/figure/force records + world_core cautions via this world's craft table, categorical_guards-tagged blocks, in table order (incl. the absolute anti-fabrication form)",
           "post_history": POST_HISTORY_GUARD}
