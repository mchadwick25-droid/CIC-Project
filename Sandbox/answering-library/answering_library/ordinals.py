"""Ordinal words in headings ("Erstes", "Deuxieme", "Tertia") and their values.

Each language is an explicit table built from a fixed list of stems and endings.
Keys are compared after norm_key, which drops diacritics, so a scan that lost
its umlauts or accents ("Deuxieme" for "Deuxième") reads the same. A word that
is not in a table has no value."""
from __future__ import annotations

import unicodedata


def fold(s: str) -> str:
    """Lower case, no diacritics, one spelling for u/v, i/j, long s and sharp s."""
    s = unicodedata.normalize("NFD", s.lower().replace("ß", "ss").replace("ſ", "s"))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.replace("v", "u").replace("j", "i").replace("’", "").replace("'", "").replace("ς", "σ")


_TRANSLIT = {"ä": "ae", "ö": "oe", "ü": "ue"}


def _spellings(word: str) -> set[str]:
    """The word as written, without its diacritics, and with umlauts spelled out (ü as ue)."""
    out = {fold(word)}
    spelled = "".join(_TRANSLIT.get(c, c) for c in word.lower())
    out.add(fold(spelled))
    return out


def _add(table: dict[str, int], words, value: int) -> None:
    for w in words:
        for key in _spellings(w):
            if table.setdefault(key, value) != value:
                raise ValueError(f"ordinal '{w}' reads as both {table[key]} and {value}")


ENGLISH = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8,
           "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12}

_LATIN_STEMS = ["prim", "secund", "terti", "quart", "quint", "sext", "septim", "octav", "non", "decim"]

_ITALIAN_STEMS = ["prim", "second", "terz", "quart", "quint", "sest", "settim", "ottav", "non", "decim"]

_GERMAN_ORDINAL_STEMS = {
    1: ["erst"], 2: ["zweit"], 3: ["dritt"], 4: ["viert"], 5: ["fünft"], 6: ["sechst"], 7: ["siebt", "siebent"],
    8: ["acht"], 9: ["neunt"], 10: ["zehnt"], 11: ["elft"], 12: ["zwölft"], 13: ["dreizehnt"], 14: ["vierzehnt"],
    15: ["fünfzehnt"], 16: ["sechzehnt"], 17: ["siebzehnt"], 18: ["achtzehnt"], 19: ["neunzehnt"],
}
_GERMAN_UNITS = {1: "ein", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs", 7: "sieben", 8: "acht",
                 9: "neun"}
_GERMAN_TENS = {20: "zwanzig", 30: "dreißig", 40: "vierzig", 50: "fünfzig", 60: "sechzig", 70: "siebzig",
                80: "achtzig", 90: "neunzig"}
_GERMAN_ENDINGS = ("e", "er", "es", "en", "em")

_FRENCH_CARDINALS = {1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                     9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13: "treize", 14: "quatorze", 15: "quinze",
                     16: "seize"}
_FRENCH_TENS = {20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 60: "soixante"}


def _german_ordinal_stems(n: int) -> list[str]:
    """Stems of the German ordinal of n (1 to 999), before the case ending."""
    if n < 20:
        return list(_GERMAN_ORDINAL_STEMS[n])
    if n < 100:
        tens, unit = n - n % 10, n % 10
        if not unit:
            return [_GERMAN_TENS[tens] + "st"]
        return [_GERMAN_UNITS[unit] + "und" + _GERMAN_TENS[tens] + "st"]
    hundreds, rest = divmod(n, 100)
    heads = ["hundert", "einhundert"] if hundreds == 1 else [_GERMAN_UNITS[hundreds] + "hundert"]
    if not rest:
        return [h + "st" for h in heads]
    return [h + s for h in heads for s in _german_ordinal_stems(rest)]


def _french_cardinal(n: int) -> str:
    """The French cardinal of n (1 to 99) as hyphenated words."""
    if n <= 16:
        return _FRENCH_CARDINALS[n]
    if n < 20:
        return "dix-" + _FRENCH_CARDINALS[n - 10]
    tens, unit = n - n % 10, n % 10
    if tens in _FRENCH_TENS:
        if not unit:
            return _FRENCH_TENS[tens]
        return f"{_FRENCH_TENS[tens]}-et-un" if unit == 1 else f"{_FRENCH_TENS[tens]}-{_FRENCH_CARDINALS[unit]}"
    if tens == 70:
        return "soixante-et-onze" if n == 71 else "soixante-" + _french_cardinal(n - 60)
    if n == 80:
        return "quatre-vingts"
    return f"quatre-vingt-{_french_cardinal(n - 80)}"


def _french_ordinal(cardinal: str) -> str:
    head, _, last = cardinal.rpartition("-")
    if last == "vingts":
        last = "vingt"
    if last == "cinq":
        last = "cinqu"
    elif last == "neuf":
        last = "neuv"
    elif last.endswith("e") and last not in ("un",):
        last = last[:-1]
    return (head + "-" if head else "") + last + "ième"


def _build() -> dict[str, int]:
    table: dict[str, int] = {}
    for word, value in ENGLISH.items():
        _add(table, [word], value)
    for value, stem in enumerate(_LATIN_STEMS, start=1):
        _add(table, [stem + e for e in ("us", "a", "um")], value)
    for value, stem in enumerate(_ITALIAN_STEMS, start=1):
        _add(table, [stem + e for e in ("o", "a", "i", "e")], value)
    for n in range(1, 1000):
        _add(table, [s + e for s in _german_ordinal_stems(n) for e in _GERMAN_ENDINGS], n)
    _add(table, ["premier", "première"], 1)
    _add(table, ["second", "seconde"], 2)
    for n in range(2, 100):
        _add(table, [_french_ordinal(_french_cardinal(n)).replace("-", "")], n)
    _add(table, ["centième"], 100)
    return table


TABLE: dict[str, int] = _build()


def ordinal_value(token: str) -> int | None:
    """The value of an ordinal word in English, Latin, Italian, German or French, or None."""
    key = fold(token.strip())
    key = key.replace("-", "")
    return TABLE.get(key)
