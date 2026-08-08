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


# Phase 2, per-world post-history guard exports (Design SS2 Layer 4; Blueprint
# SS3 step 1). Each world's Phase 2 pass adds its own entry, assembled from
# that world's records; worlds without an entry keep the shared constant
# unchanged, so behaviour for un-passed worlds is byte-identical to before.
# The IJC-scoped extension stays hardcoded at the nodes.py wiring site until
# Marius's own pass carries it into his export (the Blueprint's own note).
#
# hieronymian-ascetic-literary (Albina), assembled from halvoice001:
# - record-only discipline + naming: the grounding-anchor blocks and the
#   no-manufactured-name rule (norms).
# - the letter's measure, with its under-pressure intensity spelled out:
#   the letter's-measure-economy trait's own second intensity ("the
#   discipline NOT suspended - the measure holds"), which checkpoint 1
#   measured failing under sustained pushback while ordinary conversation
#   held. The constraint that must survive attention decay is exactly this
#   one, which is why it rides here, closest to generation (doc 09).
# - anti-fabrication absolute + honest thinness: avoid_traits
#   "manufactured specifics" and the formation-internal thinness trait.
POST_HISTORY_GUARDS = {
    "hieronymian-ascetic-literary": (
        "Hold, before you speak: only what this household's own record "
        "carries, under the right name, and at the letter's measure - one "
        "matter, argued closely, closed. The measure does not lift because "
        "you are pressed: a challenge is answered at the same length as a "
        "question, and more words are not more ground held. Never an "
        "invented scene, saying, source, or attribution - where the record "
        "thins, say the thinness plainly and stop."),
}


def post_history_guard_for(world_id: str) -> str:
    """This world's own post-history guard export, or the shared fleet
    constant for worlds whose Phase 2 pass has not yet written one."""
    return POST_HISTORY_GUARDS.get(world_id, POST_HISTORY_GUARD)


SEGMENT = {"name": "categorical_guards", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "story/figure/force records + world_core cautions via this world's craft table, categorical_guards-tagged blocks, in table order (incl. the absolute anti-fabrication form)",
           "post_history": POST_HISTORY_GUARD}
