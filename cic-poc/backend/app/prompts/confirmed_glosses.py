"""Confirmed inline-gloss renderings, per world - the bracket-gloss reading
pattern from LEXICON_GLOSS_AUDIT_2026-07-23.md's project-owner review pass.

Scope, deliberately narrow: this module holds ONLY the items the audit
document's own "Decisions log" section marks Confirmed - roughly 20 of the
~104+ terms and phrases the audit addressed. Everything else in that
document is still an open recommendation awaiting review; shipping an
unconfirmed gloss here would mean presenting a guess as settled, which is
exactly what the audit's own review process exists to prevent. When more
items are confirmed, add them here - do not promote a recommendation by
inferring it from the doc's prose.

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
CONFIRMED_GLOSSES: dict[str, list[ConfirmedGloss]] = {
    "syriac-edessa-nisibis": [
        ConfirmedGloss("A", "raza", "a sign tied to a hidden truth"),
        ConfirmedGloss("A", "Iḥidaya", "the undivided one"),
    ],
    "desert-monasticism": [
        ConfirmedGloss("A", "Logismoi", "the thoughts that trouble the mind"),
        ConfirmedGloss("A", "Koinōnia", "Pachomius's monastic federation"),
    ],
    "hieronymian-ascetic-literary": [
        ConfirmedGloss("A", "Vulgata", "the new Latin translation"),
        ConfirmedGloss("B", "the month named for the harvest", "August"),
    ],
    "imperial-juridical-christianity": [
        ConfirmedGloss("A", "homoios", "similar to the Father"),
    ],
    "post-apostolic-house-church": [
        ConfirmedGloss("B", "the day named for the sun", "Sunday"),
        ConfirmedGloss("B", "the Lord's own day", "Sunday"),
        ConfirmedGloss("B", "the first day of the week", "Sunday"),
    ],
    "alexandria-catechetical": [
        ConfirmedGloss("A", "gnosis", "a transformative knowing of God"),
        ConfirmedGloss("A", "participation", "a deep sharing in God's life"),
        ConfirmedGloss("A", "theosis", "being drawn into God's life"),
        ConfirmedGloss("A", "psyche", "your whole self, body and heart together"),
        ConfirmedGloss("A", "nous", "the soul's deepest eye"),
        ConfirmedGloss("A", "likeness of God", "growing to reflect God more fully"),
        ConfirmedGloss("A", "autexousia", "the freedom to respond to God"),
        ConfirmedGloss("A", "allegory", "reading for the deeper meaning"),
        ConfirmedGloss("A", "oikonomia", "how God wisely arranges the whole plan of salvation"),
        ConfirmedGloss("A", "mysterion", "a sacred reality known from within"),
    ],
}


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
        "come up - do not force one in.",
        "",
    ]
    for g in glosses:
        lines.append(f'- "{g.rendered}"')
    return "\n".join(lines) + "\n"


def find_glosses_used(world_id: str, response_text: str) -> list[dict]:
    """
    Real-detection pass, run after generation: which of this world's
    confirmed glosses actually appear in the response text, verbatim.
    Simple substring containment against a small known set (at most 10
    entries per world) - deliberately not a fuzzy/regex match, since the
    Representative was instructed to use the exact wording, so an exact
    match is the correct check, not a heuristic one.
    """
    glosses = CONFIRMED_GLOSSES.get(world_id)
    if not glosses:
        return []
    return [
        {"category": g.category, "original": g.original, "gloss": g.gloss, "rendered": g.rendered}
        for g in glosses
        if g.rendered in response_text
    ]
