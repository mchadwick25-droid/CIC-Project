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
        ConfirmedGloss("A", "shrara", "the truth itself"),
        ConfirmedGloss("A", "madrasha", "a teaching-hymn"),
        ConfirmedGloss("A", "Ewangeliyon da-Mhallete", "the harmonized Gospel"),
        ConfirmedGloss("A", "Mar", "my lord, an honorific like \"Saint\""),
        ConfirmedGloss("A", "taḥwîṯâ", "a demonstration"),
        ConfirmedGloss("A", "memra", "a verse composition"),
        ConfirmedGloss("A", "qyama", "a kept vow of celibacy for life"),
    ],
    "desert-monasticism": [
        ConfirmedGloss("A", "Logismoi", "the thoughts that trouble the mind"),
        ConfirmedGloss("A", "Koinōnia", "Pachomius's monastic federation"),
        ConfirmedGloss("A", "Anachōrēsis", "withdrawal"),
        ConfirmedGloss("A", "Apotagē", "renunciation"),
        ConfirmedGloss("A", "Hēsychia", "stillness"),
        ConfirmedGloss("A", "Diakrisis", "discernment"),
        ConfirmedGloss("A", "Abba", "an elder, honored as a father in the faith"),
        ConfirmedGloss("A", "Amma", "an elder, honored as a mother in the faith"),
        ConfirmedGloss("A", "Cheirōnaxia", "manual labor"),
        ConfirmedGloss("A", "Apophthegma", "a teaching-saying"),
    ],
    "hieronymian-ascetic-literary": [
        ConfirmedGloss("A", "Vulgata", "the new Latin translation"),
        ConfirmedGloss("B", "the month named for the harvest", "August"),
        ConfirmedGloss("A", "Hebraica veritas", "the Hebrew truth"),
        ConfirmedGloss("A", "Renuntiatio", "renunciation"),
        ConfirmedGloss("A", "Virginitas", "consecrated virginity"),
        ConfirmedGloss("A", "Vidua", "ascetic widowhood"),
        ConfirmedGloss("A", "Patrocinium", "patronage"),
        ConfirmedGloss("A", "Epistula", "the letter"),
        ConfirmedGloss("A", "Matrona", "a Roman noblewoman of standing"),
        ConfirmedGloss("A", "Grammaticus", "classical schooling"),
        ConfirmedGloss("A", "Praefatio", "the preface"),
        ConfirmedGloss("A", "Nosocomium", "a hospital"),
        ConfirmedGloss("A", "Monachus", "a monk"),
    ],
    "imperial-juridical-christianity": [
        ConfirmedGloss("A", "homoios", "similar to the Father"),
        ConfirmedGloss("A", "primatus", "primacy, Rome's own authority"),
        ConfirmedGloss("A", "presbeia", "a rank of honor"),
        ConfirmedGloss("A", "Imperator intra Ecclesiam", "the emperor is within the Church, not above it"),
        ConfirmedGloss("A", "homoousios", "of one being with the Father"),
        ConfirmedGloss("A", "concilium", "a council"),
        ConfirmedGloss("A", "haeresis", "heresy"),
        ConfirmedGloss("A", "Tomus", "a formal doctrinal letter"),
        ConfirmedGloss("A", "Nea Rhōmē", "New Rome, Constantinople"),
        ConfirmedGloss("A", "basilica", "a church building"),
        ConfirmedGloss("A", "martyrium", "a martyr's shrine"),
    ],
    "post-apostolic-house-church": [
        ConfirmedGloss("B", "the day named for the sun", "Sunday"),
        ConfirmedGloss("B", "the Lord's own day", "Sunday"),
        ConfirmedGloss("B", "the first day of the week", "Sunday"),
        ConfirmedGloss("A", "the water", "baptism"),
        ConfirmedGloss("A", "Two Ways", "the teaching that lays the two paths of life and death before you"),
        ConfirmedGloss("A", "episkopos", "bishop, an overseer"),
        ConfirmedGloss("A", "presbyteros", "an elder"),
        ConfirmedGloss("A", "ekklesia", "the assembly, the church"),
        ConfirmedGloss("A", "eucharistia", "the thanksgiving meal"),
        ConfirmedGloss("A", "diakonos", "a deacon, one who serves"),
        ConfirmedGloss("A", "presbyterion", "the council of elders"),
        ConfirmedGloss("A", "prophetes", "a prophet"),
        ConfirmedGloss("A", "ministrae", "servant-women, per Pliny's own report"),
        ConfirmedGloss("A", "agape", "the love-feast"),
        ConfirmedGloss("A", "pertinacia", "stubbornness, a refusal to recant"),
    ],
    "alexandria-catechetical": [
        ConfirmedGloss("A", "illumination", "baptism"),
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
        ConfirmedGloss("A", "Logos", "the Word"),
        ConfirmedGloss("A", "Divine Pedagogy", "God's ongoing teaching"),
        ConfirmedGloss("A", "Catechesis", "formation before baptism"),
        ConfirmedGloss("A", "photismos", "the opening of sight"),
        ConfirmedGloss("A", "Sophia", "wisdom"),
        ConfirmedGloss("A", "eikon", "the image of God"),
        ConfirmedGloss("A", "Christological Reading", "reading Scripture toward Christ"),
        ConfirmedGloss("A", "Rule of Faith", "the received tradition"),
        ConfirmedGloss("A", "metanoia", "a change of mind, turning back to God"),
        ConfirmedGloss("A", "hamartia", "missing the mark"),
        ConfirmedGloss("A", "episkopos", "the overseer"),
        ConfirmedGloss("A", "didaskalos", "the teacher"),
        ConfirmedGloss("A", "oikos", "the household"),
        ConfirmedGloss("A", "pistis", "trust, the soul's first turn toward God"),
        ConfirmedGloss("A", "agape", "divine love"),
        ConfirmedGloss("A", "elpis", "hope"),
        ConfirmedGloss("A", "ekklesia", "the gathered community"),
        ConfirmedGloss("A", "arete", "excellence"),
        ConfirmedGloss("A", "Pneuma Hagion", "the Spirit of God"),
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
        "come up - do not force one in. Build the rest of the sentence "
        "around the fixed phrase so the whole line still reads naturally: "
        "since the phrase itself cannot change, watch for your own wording "
        "echoing a word already inside it right before or after (e.g. "
        "pairing a phrase ending \"...for life\" with your own \"...his "
        "whole life\" immediately after) - rephrase your own surrounding "
        "words instead, not the fixed phrase.",
        "",
    ]
    for g in glosses:
        lines.append(f'- "{g.rendered}"')
    return "\n".join(lines) + "\n"


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
    return [
        {"category": g.category, "original": g.original, "gloss": g.gloss, "rendered": g.rendered}
        for g in glosses
        if g.rendered.lower() in lowered
    ]
