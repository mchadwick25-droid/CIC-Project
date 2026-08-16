"""Confirmed inline-gloss renderings, per world - the bracket-gloss reading
pattern from LEXICON_GLOSS_AUDIT_2026-07-23.md's project-owner review pass.

S4.5 provenance note (Pass 1 §3.11): this list is FACILITATOR-OWNED data
of the same kind as the modern_term records - curated with the same
exact-wording discipline as the whitelist it carries forward. Per §3.11
it lives as a keyed list (this module) rather than as its own
record_type; named here so "record data" points at something specific.
Nothing about its content or consumption changes at S4.5.

Scope: every item the audit document's own tables carried at High confidence
("essentially just the term's own Aliases/Quick Meaning restated plainly")
plus every individually-decided Medium/Flagged item - the full glossary,
project-owner reviewed and confirmed 2026-07-25. Medium-confidence and
flagged (false-friend / no-clean-equivalent) items are reviewed and added
one at a time, per the project owner's own request, rather than shipped in
this bulk pass; excluded/scope-question entries (e.g. Syriac's Catholicos)
are never added at all. Shipping an unconfirmed gloss here would mean
presenting a guess as settled, which is exactly what the audit's own review
process exists to prevent.

A handful of terms the audit flagged "low priority, already plain English"
have no distinct period-term in their own lexicon file's `Term:` line at
all (e.g. Alexandria's bare "Death," "Christ," "Prayer") - there is nothing
to put in brackets for these, so they are correctly absent here rather than
glossed with an invented foreign word.

Two rendering patterns, per the audit's own general rendering rule:
- Category A (vocabulary terms): modern gloss leads, original term follows
  in brackets - "we prepare for the baptism (water)".
- Category B (phrase-level circumlocutions): original phrase leads exactly
  as attested, modern reference follows in brackets - "the day named for
  the sun (Sunday)", not "Sunday (the day named for the sun)".

`original` for Category A entries is the actual period/foreign term a
Representative would plausibly speak - verified against each lexicon
file's own front-matter `Term:` line (not inferred from the audit
document's prose), lowercased for natural mid-sentence use. Where a
lexicon file's Term line pairs an English half with a Greek/Latin half
(e.g. "Knowledge / Gnosis"), the foreign half is what appears in
brackets, since the whole point of Category A is surfacing the
period-specific word - the English half is already what the gloss itself
says in different words.
"""

import functools
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class ConfirmedGloss:
    category: str  # "A" or "B"
    original: str  # Category A: the period term. Category B: the full attested phrase.
    gloss: str  # Category A: the modern-language gloss. Category B: the short modern referent.

    @property
    def rendered(self) -> str:
        if self.category == "A":
            return f"{self.gloss} ({self.original})"
        return f"{self.original} ({self.gloss})"


# Keyed by world_id (matches WORLD_MANIFEST world_id values).
# SS4.3 DATA MOVE (Voice-Governance Addendum, executed at the S6.2 tail,
# 2026-08-01): the authoritative gloss data now lives in
# the engine's confirmed_glosses.yaml (the schema-validated
# keyed list - confirmed_gloss.schema.json; still Facilitator-owned,
# still deliberately not a record type per Pass 1 SS3.11). This module
# LOADS it at import and preserves the exact prior interface -
# CONFIRMED_GLOSSES keyed by world_id, entry order preserved (YAML list
# order == the prior in-code order), so get_gloss_guidance stays
# byte-identical per world (cache stability verified by pre/post-move
# hash comparison at the move). term_id (optional, the backfill's
# field) is accepted and ignored here - Rule C consumes it gate-side.
def _load_confirmed_glosses() -> dict[str, list[ConfirmedGloss]]:
    import yaml
    from pathlib import Path
    from app.engine_bridge import GLOSSES_PATH
    data_path = GLOSSES_PATH
    doc = yaml.safe_load(data_path.read_text(encoding="utf-8"))
    out: dict[str, list[ConfirmedGloss]] = {}
    for e in doc["glosses"]:
        out.setdefault(e["world_id"], []).append(
            ConfirmedGloss(e["category"], e["original"], e["gloss"]))
    return out


CONFIRMED_GLOSSES: dict[str, list[ConfirmedGloss]] = _load_confirmed_glosses()


def get_gloss_guidance(world_id: str) -> str:
    """
    The Representative-facing instruction block for this world's confirmed
    glosses - "" if this world has none. Byte-identical for a given
    world_id on every turn, so callers can mark it as part of the same
    cacheable static prefix as the rest of build_representative_prompt's
    output (see representative_prompts.py).
    """
    glosses = CONFIRMED_GLOSSES.get(world_id)
    if not glosses:
        return ""

    lines = [
        "# When You Use These Specific Words",
        "",
        "A small number of words and phrases in your own vocabulary have a "
        "confirmed modern reading, reviewed and settled specifically so a "
        "participant unfamiliar with your world's own language isn't left "
        "guessing. When you use one of the following in this conversation, "
        "say it exactly in the form given - not a paraphrase, not a "
        "reordering, the exact wording below. This is the only place in "
        "your own speech where an exact form is asked of you rather than "
        "your own formation's natural phrasing; everything else about how "
        "you speak is unchanged. Use these only where they'd naturally "
        "come up - do not force one in. This applies in the turn where "
        "you use the word, as you use it - a word spoken in an earlier "
        "turn is finished business: never open a turn repairing, "
        "re-glossing, or asking about something you already said.",
        "",
    ]
    for g in glosses:
        lines.append(f'- "{g.rendered}"')
    return "\n".join(lines) + "\n"


@functools.lru_cache(maxsize=1)
def _common_words() -> frozenset:
    """The bundled top-5000 general-English list, used only to suppress a
    plain-side pill on an everyday single word. Fails toward the EMPTY set,
    which suppresses every single-word plain-side match - i.e. toward the
    state that existed before this tier, never toward more pills."""
    try:
        from app.engine_bridge import _alias_freq_table
        return frozenset(_alias_freq_table())
    except Exception:  # noqa: BLE001
        return frozenset()


def _plain_side_eligible(gloss: str) -> bool:
    words = gloss.lower().split()
    if len(words) > 1:
        return True
    common = _common_words()
    return bool(common) and words[0] not in common


def find_glosses_used(world_id: str, response_text: str) -> list[dict]:
    """
    Real-detection pass, run after generation: which of this world's
    confirmed glosses actually appear in the response text, verbatim.
    Simple substring containment against a small known set (well under 30
    entries per world) - deliberately not a fuzzy/regex match, since the
    Representative was instructed to use the exact wording, so an exact
    match is the correct check, not a heuristic one.

    Case-insensitive: `rendered` is written lowercase-first for natural
    mid-sentence use, but a Representative opening a sentence with it
    capitalizes that first letter ("A transformative knowing of God
    (gnosis) is...") - a real response caught exactly this in production
    verification, silently going undetected under a case-sensitive check.
    """
    glosses = CONFIRMED_GLOSSES.get(world_id)
    if not glosses:
        return []
    lowered = response_text.lower()
    # Two-tier detection (gloss-firing fix, 2026-08-09). Tier 1, unchanged:
    # the full rendered form appeared - the voice glossed inline. Tier 2,
    # new: the ORIGINAL phrase appeared without its rendered form. Chloe's
    # diagnosis showed why tier 2 must exist: her rebuilt plain register
    # naturally says "the water" or "Two Ways" mid-sentence and correctly
    # refuses the clunky exact-wording form - so detection reported 0/8 all
    # day while her transparency-worthy vocabulary was on screen. When only
    # the original fires, inline=False tells the UI to supply the modern
    # reading itself (Three-Level Transparency doing its job) instead of
    # the voice being forced to lecture. Voice stays natural; the bridge
    # still reaches the participant.
    #
    # Tier 3, the PLAIN SIDE (2026-08-09). Papnoute fired 0 of 8 across two
    # full checkpoints, and the diagnosis was not a matching bug: he never
    # says his Greek at all. He says "stillness", "the cell", "the elder",
    # "the gathering" - plain English, start to finish - where his lexicon
    # holds hesychia, kellion, geron, synaxis. That is his register doing
    # exactly what 1A asks of it, and it should not cost the reader the
    # scholarship underneath. So when a voice uses the confirmed gloss's own
    # modern phrase and never reaches for the period term, the pill still
    # fires; the UI supplies the word this world had for it, and the road to
    # the record. Voice stays plain; depth stays reachable.
    #
    # Bounded to glosses of at most 4 words, matched on word boundaries: a
    # long gloss ("an elder, honored as a father in the faith") is a
    # definition no one speaks, and matching it would only ever misfire.
    #
    # And a SINGLE-word gloss must be out of the general top-5000 to fire.
    # The first run of this tier put a pill on "hope" (Alexandria's elpis) -
    # an everyday word a reader does not stumble on, marked on every use.
    # That is precisely the noise this whole area is supposed to avoid: a
    # Representative who lectures, relocated into the interface. Distinctive
    # single words ("stillness", "renunciation", "discernment") still fire.
    out = []
    for g in glosses:
        if g.rendered.lower() in lowered:
            out.append({"category": g.category, "original": g.original,
                        "gloss": g.gloss, "rendered": g.rendered,
                        "inline": True, "plain_side": False})
        elif g.original.lower() in lowered:
            out.append({"category": g.category, "original": g.original,
                        "gloss": g.gloss, "rendered": g.rendered,
                        "inline": False, "plain_side": False})
        elif (len(g.gloss.split()) <= 4
                and _plain_side_eligible(g.gloss)
                and re.search(rf"\b{re.escape(g.gloss.lower())}\b", lowered)):
            out.append({"category": g.category, "original": g.original,
                        "gloss": g.gloss, "rendered": g.rendered,
                        "inline": False, "plain_side": True})
    return out
