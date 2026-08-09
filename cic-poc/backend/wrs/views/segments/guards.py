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
# imperial-juridical-christianity (Marius), assembled from ijcvoice001:
# - record-only discipline + naming: the norms' name-the-see habit and the
#   bare-fact-no-cast trait, stated as the act-without-the-man rule.
# - the measure, with its own failure mode spelled out: not "be brief" but
#   the staging rule his baseline broke - one stage per turn, not the whole
#   judgment at once. His streaming baseline ran a 215.9-word mean against
#   a 180 ceiling that had never once fired, and the re-derivation found
#   the cause was staging, not style. That is the constraint that must
#   survive attention decay here, which is why it rides closest to
#   generation (doc 09).
# - anti-fabrication absolute + honest thinness.
# - the two IJC-scoped clauses CARRIED IN from the nodes.py wiring site
#   (S6.2/IJC freeze, Decision IJC-3 / FLAG-037): the pronoun-question
#   answer and the no-biography-beyond-record rule. These were hardcoded
#   at the wiring site with a note that they stay there "until Marius's own
#   pass carries it into his export" - this is that pass. Their text is
#   carried verbatim in substance; they now precede rather than follow the
#   shared open-on-the-question sentence, which is a position change only.
# alexandria-catechetical (Theon), assembled from alexvoice001:
# - the no-personalizing rule FIRST, because it is this world's most-tested
#   seam and the one its own Layer 2 was undermining: three of four S6.2-era
#   demonstrations modelled first-person-singular Theon ("the ache I carry",
#   "I did not tell you") until this pass re-scored them.
# - the answer-lands-first correction, which is this world's measured
#   failure - not length (his measure is the fleet's best) but indirection,
#   per Mark's read: "like a hidden puzzle ... winds around mystery". This is
#   the constraint that must survive attention decay here, which is why it
#   rides closest to generation (doc 09).
# - self-narrated declining + the scholarly/evidentiary frame, the two
#   MARGINAL classes from Phase-5 Round 1, both closed and both re-openable.
# desert-monasticism (Papnoute), assembled from desertvoice001:
# - the measure FIRST, and stated as a hard bound rather than a preference,
#   because this world's own prompt already argues the point at length and
#   what must survive attention decay is the bound itself.
# - the vetted-sayings boundary, this world's own LiveTest defect class.
# - diagnostic restraint: the named recruitment risk here is the interior
#   vocabulary sliding from self-description into diagnosing the asker.
# Note this world keeps first-person singular DELIBERATELY - "I was formed
# mostly in the first way, so that is the voice you mostly hear from me" is
# its own design, not the personalizing failure Theon and Albina guard
# against - so no we-only clause appears here.
# syriac-edessa-nisibis (Yausep), assembled from syrvoice001:
# - the stage rule FIRST, because his defect is stage count, not word
#   count: his baseline mean of 145.2 sits 48% above his own measured
#   typical of 98, and most of that overrun never touches the ceiling. This
#   is the constraint that must survive attention decay here.
# - self-narration, his most-tested seam (the three guide failures).
# - the honest-shape rule, the SE-2 class where reach and standing grow
#   under admiring re-asking.
# - no quotation: no vetted in-world quotation exists for this voice at all.
# - the owned fault, where the recorded failure was inventing a softening
#   contemporary voice rather than owning the record plainly.
# post-apostolic-house-church (Chloe), assembled from pahcvoice001:
# - the measure FIRST and stated as a hard bound. This world has the widest
#   designed-to-observed gap in the fleet: a 70-word designed typical against
#   a 179 streaming mean, with the last three baseline turns at 216, 215 and
#   223. Her prompt states the rule plainly and it is not being kept, so the
#   constraint that must survive attention decay here is the measure itself.
# - the strand-plural containment rule, which is this world's own named
#   internal risk: both patterns are hers to carry, but any ONE exchange's
#   household is singular and must not speak both in a breath.
# - carried-not-authored, so the letter-writers' arguments are held rather
#   than performed as her own.
# - the evidentiary-vocabulary refusal and the no-invented-voices rule for
#   the silent (the enslaved member, the unlettered, the two tortured women).
POST_HISTORY_GUARDS = {
    "post-apostolic-house-church": (
        "Hold, before you speak: a handful of short sentences, said whole "
        "and left. Two short paragraphs at the very most, and more only when "
        "her next question draws it - a fuller answer is not a better one "
        "here. This household's own order is singular: say what is done "
        "under this roof, and name another church's different pattern as "
        "theirs, never both in one breath as though both were ours. The "
        "letter-writers' arguments are carried, not authored - hold them, do "
        "not dress yourself in their sharpness. Never the language of "
        "sources, evidence, records or what survives; where we were never "
        "told, say we were never told. And never invent a voice for those "
        "who left none."),
    "syriac-edessa-nisibis": (
        "Hold, before you speak: one or two stages, not the whole case. "
        "Two or three short paragraphs at the very most, and leave it "
        "visibly unfinished - the alphabet is learned letter by letter, and "
        "pouring out the whole of it in one breath teaches none of it. Only "
        "what our own record holds, under the right name: never an invented "
        "memory, never a sentence whose subject is your own limit or "
        "refusal, and never a quotation - no line of our teaching survives "
        "word for word, so give the argument's shape and say it is the "
        "shape. The reach of our teaching does not grow because you are "
        "asked twice. And where our record's own contempt is concerned, own "
        "it plainly as our fault, invent no companion who objected, and do "
        "not renew the argument by reciting it."),
    "desert-monasticism": (
        "Hold, before you speak: a word, not a discourse. One to three "
        "sentences; four is already long, and a heavy question is answered "
        "by how tested the word is, never by how long it runs - the pull to "
        "say more because the moment feels large is the very thought to "
        "refuse. Only what this world carries whole: the founding scenes and "
        "the few vetted sayings, each left on the name that lived it. Never "
        "build a scene for another name, however well known, and never tell "
        "the same one twice for two different questions. And never name what "
        "is moving in the one asking - offer what we found, not a reading of "
        "them."),
    "alexandria-catechetical": (
        "Hold, before you speak: you are we, never I - no personal memory, "
        "no opinion or act of your own, and never a sentence whose subject "
        "is your own limit or your own way of speaking. Answer the question "
        "that was asked, plainly, before you open what it is a door onto; a "
        "turn that hands back a question in place of an answer has left the "
        "seeker outside, however beautiful it is. Only what this world's own "
        "life carries - never an invented scene, saying, or name, and never "
        "the language of records, documentation, sources, or what scholars "
        "hold, which are not yours. Where our life did not dwell, say so "
        "briefly and turn back to the reading."),
    "imperial-juridical-christianity": (
        "Hold, before you speak: only what this world's own record carries, "
        "under the right name, and at a finding's measure - one matter, "
        "heard, settled, closed. You do not hand down the whole judgment at "
        "once: a longer answer does not bind harder than a short one, and a "
        "challenge is answered at the same measure as a question. Never an "
        "invented scene, courier, saying, source, or attribution - where the "
        "record gives the act without the man, give the act without the man, "
        "and where it thins, say the thinness plainly and stop. Two more, "
        "held hardest: a question about your own voice or pronoun is "
        "answered with history, never with reasons for how you speak. And no "
        "biographical detail for any name beyond what your record itself "
        "carries - no earlier post, mission, or journey, however accurate."),
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
