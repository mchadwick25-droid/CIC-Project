"""The British-to-American word table.

One table for the two programs that need it: `tools/check_spelling.py` finds British forms in modern-English
prose, and `engine/m10/regate.py` compares a field with its base after both are put through `normalize`, so
that a change of spelling alone is not counted as an edit.

Every flagged form is spelled out here (generated from a stem and an ending, never matched by a bare suffix),
so a word that is spelled the same in both varieties - advise, exercise, promise, rigorous, glamour - can
never be hit.
"""
from __future__ import annotations

import re

TABLE: dict[str, str] = {}


def _family(stems, british_end: str, american_end: str, endings) -> None:
    for stem in stems:
        for end in endings:
            TABLE[f"{stem}{british_end}{end}"] = f"{stem}{american_end}{end}"


# -our -> -or
_family(
    ("colo", "hono", "favo", "behavio", "neighbo", "labo", "harbo", "rumo", "humo", "vigo", "rigo", "valo", "savo",
     "flavo", "endeavo", "fervo", "armo", "cando", "clamo", "splendo", "odo", "parlo", "vapo", "tumo", "demeano",
     "unfavo", "tricolo", "ardo", "succo"),
    "ur", "r", ("", "s", "ed", "ing", "ful", "fully", "less", "able", "ably", "ite", "ites", "ist", "ists", "er", "ers", "y", "hood", "hoods"),
)
TABLE["saviour"], TABLE["saviours"] = "savior", "saviors"

# -ise -> -ize, -isation -> -ization
_family(
    ("organ", "recogn", "real", "emphas", "character", "author", "critic", "summar", "apolog", "civil", "special",
     "memor", "central", "normal", "minim", "maxim", "categor", "final", "legal", "patron", "sanit", "standard",
     "symbol", "systemat", "theor", "util", "visual", "bapt", "canon", "evangel", "catech", "demon", "christian",
     "latin", "hellen", "roman", "secular", "spiritual", "idol", "memorial", "general", "individual", "fertil",
     "harmon", "immortal", "mobil", "modern", "monopol", "neutral", "optim", "popular", "rational", "sympath",
     "local", "national", "material", "mechan", "cauter", "colon", "fratern", "jeopard", "penal", "subsid",
     "synchron", "steril", "pasteur", "formal", "human", "ideal", "industrial", "internation", "liber", "magnet",
     "moral", "natural", "personal", "polar", "social", "stabil", "vandal", "vulgar", "tyrann", "fantas", "hospital",
     "galvan", "mesmer", "agon", "item", "equal", "reorgan", "rebapt", "unbapt", "anathemat", "regular", "unauthor",
     "synthes", "dramat", "apostat", "juda", "legitim", "arab", "recatholic", "institutional", "sexual", "scandal",
     "styl", "marginal", "theolog", "indigen", "polemic", "schemat", "capital", "digit"),
    "is", "iz", ("e", "es", "ed", "ing", "ation", "ations", "er", "ers", "able", "ational", "ationally"),
)

# -yse -> -yze
for _stem in ("anal", "paral", "catal"):
    for _b, _a in (("yse", "yze"), ("ysed", "yzed"), ("ysing", "yzing"), ("yser", "yzer"), ("ysers", "yzers")):
        TABLE[_stem + _b] = _stem + _a

# -re -> -er
_family(("cent", "epicent"), "re", "er", ("", "s"))
TABLE["centred"] = "centered"
TABLE["epicentred"] = "epicentered"
TABLE["centring"] = "centering"
_family(("theat", "met", "lit", "fib", "calib", "somb", "lust", "meag", "spect", "sab", "kilomet", "millimet", "centimet"),
        "re", "er", ("", "s"))
TABLE["manoeuvre"], TABLE["manoeuvres"], TABLE["manoeuvred"] = "maneuver", "maneuvers", "maneuvered"

# doubled l before a suffix: travelled -> traveled
for _stem in ("travel", "label", "cancel", "counsel", "model", "level", "fuel", "signal", "marshal", "quarrel", "channel",
              "tunnel", "funnel", "equal", "total", "dial", "pencil", "shovel", "gravel", "revel", "rival", "duel", "libel",
              "panel", "carol", "initial", "refuel", "unravel", "marvel", "jewel", "dishevel"):
    for _end in ("ed", "ing", "er", "ers", "or", "ors"):
        TABLE[f"{_stem}l{_end}"] = f"{_stem}{_end}"

# -ence -> -ense, and a few single words
TABLE.update({
    "defence": "defense", "defences": "defenses", "defenceless": "defenseless", "offence": "offense",
    "offences": "offenses", "pretence": "pretense", "licence": "license", "licences": "licenses",
    "mediaeval": "medieval", "encyclopaedia": "encyclopedia", "paediatric": "pediatric", "anaemia": "anemia",
    "foetus": "fetus", "oestrogen": "estrogen", "diarrhoea": "diarrhea", "haemorrhage": "hemorrhage",
    "orthopaedic": "orthopedic", "leukaemia": "leukemia", "anaesthetic": "anesthetic",
    "grey": "gray", "greying": "graying", "ageing": "aging", "judgement": "judgment", "judgements": "judgments",
    "acknowledgement": "acknowledgment", "acknowledgements": "acknowledgments", "programme": "program",
    "programmes": "programs", "artefact": "artifact", "artefacts": "artifacts", "sceptic": "skeptic",
    "sceptics": "skeptics", "sceptical": "skeptical", "scepticism": "skepticism", "plough": "plow",
    "ploughed": "plowed", "ploughing": "plowing", "aluminium": "aluminum", "cheque": "check", "cheques": "checks",
    "kerb": "curb", "tyre": "tire", "tyres": "tires", "mould": "mold", "moulds": "molds",
    "moulded": "molded", "smoulder": "smolder", "smouldering": "smoldering", "sulphur": "sulfur",
    "pyjamas": "pajamas", "draught": "draft", "draughts": "drafts", "cosy": "cozy", "moustache": "mustache",
    "enquire": "inquire", "enquired": "inquired", "enquiry": "inquiry", "enquiries": "inquiries",
    "connexion": "connection", "learnt": "learned", "dreamt": "dreamed", "fulfil": "fulfill",
    "fulfilment": "fulfillment", "enrol": "enroll", "enrolment": "enrollment", "instil": "instill",
    "skilful": "skillful", "skilfully": "skillfully", "wilful": "willful", "wilfully": "willfully",
    "jewellery": "jewelry", "instalment": "installment", "practise": "practice", "practised": "practiced",
    "practising": "practicing", "distil": "distill", "appal": "appall",
    "councillor": "councilor", "councillors": "councilors", "uncatalogued": "uncataloged",
    "catalogue": "catalog", "catalogues": "catalogs", "catalogued": "cataloged", "cataloguing": "cataloging",
    "cataloguer": "cataloger", "cataloguers": "catalogers",
})

WORD_RE = re.compile(
    r"(?<![\w/_.-])(?:" + "|".join(sorted(map(re.escape, TABLE), key=len, reverse=True)) + r")(?![\w/_-])",
    re.IGNORECASE,
)

_COMPARE_RE = re.compile(
    r"(?<![\w/_.])(?:" + "|".join(sorted(map(re.escape, TABLE), key=len, reverse=True)) + r")(?![\w/_])",
    re.IGNORECASE,
)


def american(word: str) -> str:
    """The American form of one flagged word, keeping its capitalization."""
    new = TABLE[word.lower()]
    if word.isupper():
        return new.upper()
    if word[:1].isupper():
        return new[:1].upper() + new[1:]
    return new



# Spellings that are also surnames or other names when capitalized: matched in lower case only.
LOWER_ONLY = {"grey", "greying", "mould", "moulds", "moulded", "tyre", "tyres"}


def is_flagged(word: str) -> bool:
    return word.lower() in TABLE and not (word.lower() in LOWER_ONLY and not word.islower())


def normalize(text: str) -> str:
    """The text with every British form replaced by the American one, wherever it stands
    (quotations included, and a form joined to another word by a hyphen): used to compare two texts,
    never to rewrite one."""
    return _COMPARE_RE.sub(lambda m: american(m.group(0)) if is_flagged(m.group(0)) else m.group(0), text)
