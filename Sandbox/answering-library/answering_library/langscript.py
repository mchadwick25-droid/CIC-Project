"""Language from the filename code, script from the letters themselves."""
from __future__ import annotations

import re

LANGUAGE_CODES = frozenset({
    "lat", "grc", "eng", "fra", "deu", "ita", "rus", "enm", "spa", "ces", "gmh",
    "chu", "pol", "ara", "syr", "nld", "cym", "por", "swe", "hrv", "gez", "tgl",
    "heb", "hye", "dan", "nor", "fin", "hun", "ukr", "bel", "ron", "cop",
})

CODE_SCRIPT = {
    "grc": "Grek", "rus": "Cyrl", "chu": "Cyrl", "ukr": "Cyrl", "bel": "Cyrl",
    "ara": "Arab", "syr": "Syrc", "heb": "Hebr", "hye": "Armn", "gez": "Ethi", "cop": "Copt",
}

_SCRIPT_RANGES = (
    ("Grek", re.compile("[Ͱ-Ͽἀ-῿]")),
    ("Cyrl", re.compile("[Ѐ-ԯᲀ-᲏ⷠ-ⷿꙀ-ꚟ]")),
    ("Arab", re.compile("[؀-ۿݐ-ݿࢠ-ࣿ]")),
    ("Hebr", re.compile("[֐-׿]")),
    ("Syrc", re.compile("[܀-ݏ]")),
    ("Armn", re.compile("[԰-֏]")),
    ("Ethi", re.compile("[ሀ-᎟]")),
    ("Latn", re.compile("[A-Za-zÀ-ɏḀ-ỿ]")),
)

_STOPWORDS = {
    "eng": "the and of to that in is was he for it with as his not be by this which from are but have they".split(),
    "lat": "et in est non ad cum quod ut qui quae sed ab ex de per sunt esse enim autem nec quo".split(),
    "fra": "le la les de des et en un une du que qui dans est pour par sur au ne pas se ce il".split(),
    "deu": "der die das und den von zu mit sich des ist nicht ein eine auf im dem als auch es".split(),
    "ita": "il lo la le di che e un una del della per con non si da in sono come".split(),
    "spa": "el la los las de que y en un una del por con no se su es como para".split(),
    "swe": "och att det som en i av är för på med till den har de inte ett".split(),
    "nld": "de het een van en in is dat op te zijn voor met niet aan er".split(),
    "enm": "the and of to that in is was he for it with as his not be by this which from".split(),
    "ces": "a se na je v ze to že s do o jest ale jak by byl".split(),
    "pol": "i w na z do nie się że to jest od po jak".split(),
    "por": "o a os as de que e do da em um uma para com não se por".split(),
    "gmh": "und der die das daz er si ist mit von ze in ein".split(),
    "cym": "y yr a ac i o yn ei ar ei".split(),
    "hrv": "i u je da se na za su od to".split(),
    "tgl": "ang ng sa na at ay mga ito".split(),
    "dan": "og at det som en i af for på med til den har de ikke".split(),
    "nor": "og at det som en i av for på med til den har de ikke".split(),
    "fin": "ja on ei että se oli hän mutta kun".split(),
    "hun": "a az és hogy nem is egy van".split(),
    "ron": "și de în la cu pe care nu este un o".split(),
}
_STOPWORDS = {k: frozenset(v) for k, v in _STOPWORDS.items()}
_WORD = re.compile(r"[^\W\d_]+", re.UNICODE)


def filename_codes(filename: str) -> list[str]:
    stem = filename.rsplit(".", 1)[0]
    codes = []
    for token in re.split(r"[-_]", stem):
        if token in LANGUAGE_CODES and token not in codes:
            codes.append(token)
    return codes


def script_of(text: str) -> str:
    best, best_n = "Zyyy", 0
    for name, pattern in _SCRIPT_RANGES:
        n = len(pattern.findall(text))
        if n > best_n:
            best, best_n = name, n
    return best


def _latin_choice(text: str, candidates: list[str]) -> str:
    if len(candidates) == 1:
        return candidates[0]
    words = [w.lower() for w in _WORD.findall(text[:4000])]
    scores = {c: sum(1 for w in words if w in _STOPWORDS.get(c, ())) for c in candidates}
    best = max(candidates, key=lambda c: (scores[c], -candidates.index(c)))
    return best


def language_of(text: str, script: str, codes: list[str]) -> str:
    if script == "Latn":
        latin = [c for c in codes if CODE_SCRIPT.get(c, "Latn") == "Latn"]
        if not latin:
            latin = ["eng"]
        return _latin_choice(text, latin)
    same = [c for c in codes if CODE_SCRIPT.get(c) == script]
    if same:
        return same[0]
    return {"Grek": "grc", "Cyrl": "rus"}.get(script, "und")


INFERENCE_CANDIDATES = ("eng", "lat", "fra", "deu", "ita", "spa", "swe", "nld")
INFERENCE_MARGIN = 1.5


def infer_default_language(text: str) -> str | None:
    """For a file whose name carries no language code: the Latin-script
    language whose stopwords dominate, or None when English (the default)
    holds or nothing clearly wins."""
    words = [w.lower() for w in _WORD.findall(text[:60000])]
    if len(words) < 200:
        return None
    scores = {c: sum(1 for w in words if w in _STOPWORDS[c]) for c in INFERENCE_CANDIDATES}
    best = max((c for c in INFERENCE_CANDIDATES if c != "eng"), key=lambda c: scores[c])
    if scores[best] >= INFERENCE_MARGIN * scores["eng"] and scores[best] >= len(words) * 0.05:
        return best
    return None
