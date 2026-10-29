"""Deterministic OCR-quality score per passage, 0 (unusable) to 1 (clean).

score = 1 - min(1, W_UNKNOWN*unknown + W_SYMBOL*symbol + W_SHORT*short
                   + W_MIXED*mixed + W_HYPHEN*hyphen)

unknown  share of alphabetic tokens of three or more letters that are not
         plausible words of the passage language, where plausible means the
         token occurs at least KNOWN_MIN_COUNT times, in at least
         min(KNOWN_MIN_FILES, files of that language) files, of the union
         corpus (a vocabulary built from the texts themselves).
symbol   share of non-space characters that are neither letters, digits nor
         ordinary punctuation, plus long-s and typographic ligatures.
short    share of Latin-script tokens that are one stray letter.
mixed    share of tokens that fuse digits and letters, put an uppercase
         letter inside a lowercase word, or are vowelless runs of five or
         more letters.
hyphen   share of line breaks in the source passage that fall inside a
         hyphenated word.
"""
from __future__ import annotations

import re
from collections import Counter

W_UNKNOWN = 1.2
W_SYMBOL = 4.0
W_SHORT = 3.0
W_MIXED = 3.0
W_HYPHEN = 0.4
KNOWN_MIN_COUNT = 3
KNOWN_MIN_FILES = 3
RECOMMENDED_FLOOR = 0.60

_WORD = re.compile(r"[^\W\d_]+", re.UNICODE)
_ALLOWED = re.compile(
    r"[\w\s.,;:!?'\"()\[\]\-‐-―‘-‟«»‹›/&%*+=§¶·…†‡·;´`]"
)
_NOISE_CHARS = re.compile("[ſﬀ-ﬆ�]")
_FUSED = re.compile(r"[^\W\d_]\d|\d[^\W\d_]")
_INNER_CAP = re.compile(r"[a-zß-ÿά-ώ][A-ZÀ-ÞΑ-Ω]")
_VOWELLESS = re.compile(r"^[^aeiouyàáâãäåæèéêëìíîïòóôõöøùúûüœΑ-ωἀ-῿Ѐ-ӿ]+$", re.I)
_ROMAN = re.compile(r"^[ivxlcdm]+$", re.I)
_HYPHEN_BREAK = re.compile(r"[^\W\d_]-[ \t]*\n[ \t]*[^\W\d_]")
_VOWELS = frozenset("aeiouy")
_SINGLE_OK = frozenset("aeiouyàéòôi")


class Vocabulary:
    def __init__(self):
        self.counts: dict[str, Counter] = {}
        self.files: dict[str, Counter] = {}
        self.file_totals: Counter = Counter()
        self.known: dict[str, frozenset] = {}

    def add(self, lang: str, counts: Counter):
        self.counts.setdefault(lang, Counter()).update(counts)
        self.files.setdefault(lang, Counter()).update(counts.keys())
        self.file_totals[lang] += 1

    def freeze(self):
        for lang, counts in self.counts.items():
            min_files = min(KNOWN_MIN_FILES, self.file_totals[lang])
            files = self.files[lang]
            self.known[lang] = frozenset(
                w for w, c in counts.items() if c >= KNOWN_MIN_COUNT and files[w] >= min_files
            )
        self.counts = {}
        self.files = {}

    def unknown_share(self, lang: str, tokens: list[str]) -> float | None:
        known = self.known.get(lang)
        if known is None or not tokens:
            return None
        return sum(1 for t in tokens if t not in known) / len(tokens)


def token_counts(text: str) -> Counter:
    return Counter(w.lower() for w in _WORD.findall(text) if len(w) >= 3)


def components(text: str, lang: str, script: str, vocab: Vocabulary | None, source_text: str | None = None) -> dict:
    words_all = _WORD.findall(text)
    n_words = max(len(words_all), 1)
    compact = re.sub(r"\s+", "", text)
    n_chars = max(len(compact), 1)
    noise = len(_NOISE_CHARS.findall(compact))
    other = sum(1 for c in compact if not _ALLOWED.match(c))
    symbol = (noise + other) / n_chars
    short = 0.0
    if script == "Latn":
        short = sum(1 for w in words_all if len(w) == 1 and w.lower() not in _SINGLE_OK) / n_words
    tokens = text.split()
    n_tok = max(len(tokens), 1)
    mixed_hits = 0
    for tok in tokens:
        if _FUSED.search(tok) or _INNER_CAP.search(tok):
            mixed_hits += 1
            continue
        core = "".join(_WORD.findall(tok))
        if script == "Latn" and len(core) >= 5 and _VOWELLESS.match(core) and not _ROMAN.match(core):
            mixed_hits += 1
    mixed = mixed_hits / n_tok
    hyphen = 0.0
    if source_text is not None:
        breaks = source_text.count("\n")
        if breaks:
            hyphen = len(_HYPHEN_BREAK.findall(source_text)) / breaks
    unknown = None
    if vocab is not None:
        lows = [w.lower() for w in words_all if len(w) >= 3]
        unknown = vocab.unknown_share(lang, lows)
    return {"unknown": unknown, "symbol": symbol, "short": short, "mixed": mixed, "hyphen": hyphen}


def score(parts: dict) -> float:
    penalty = (
        W_UNKNOWN * (parts["unknown"] or 0.0)
        + W_SYMBOL * parts["symbol"]
        + W_SHORT * parts["short"]
        + W_MIXED * parts["mixed"]
        + W_HYPHEN * parts["hyphen"]
    )
    return round(1.0 - min(1.0, penalty), 4)
