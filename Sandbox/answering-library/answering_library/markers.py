"""Visible division markers in plain text: keyword-and-number headings, bare
numerals, section signs, numbered paragraphs, all-caps headings; page
furniture to suppress; and the choice of which marker families make up the
division scheme of one file."""
from __future__ import annotations

import re
import statistics
from dataclasses import dataclass, field

from . import ordinals

PAGE_WORDS = (80, 800)
HEADER_KEYS = frozenset({
    "title", "creator", "publisher", "publication date", "rights", "rights basis", "source",
    "provenance note", "content note", "language", "date", "editor", "translator", "note",
    "series", "volume", "host", "retrieved", "license", "licence", "print basis", "text basis",
})

_KEYWORDS = {
    "book": "book liber libri livre buch bok bog libro kniga kn biblion bibl biblos",
    "chapter": "chapter chap ch cap caput capitulum capitulus capit chapitre kapitel kap kapitola capitolo "
               "kephalaion kef glava gl",
    "letter": "letter epistola epistula epistle epistolae lettre brief epistole epistel pismo poslanie",
    "homily": "homily homilia homelie homilie homilies beseda",
    "sermon": "sermon sermo sermones predigt sermon sermao",
    "oration": "oration oratio discourse discours rede logos slovo",
    "treatise": "tractatus tract treatise traite",
    "question": "quaestio question quest demande frage erotesis vopros",
    "canon": "canon can kanon pravilo",
    "article": "article articulus artikel art statia",
    "act": "act actio session sessio sitzung praxis deianie",
    "psalm": "psalm psalmus pseaume psaume psalmos",
    "ode": "ode hymn hymnus hymne",
    "part": "part pars partie teil sectio section sec pt",
    "dialogue": "dialogus dialogue dialog",
    "demonstration": "demonstratio demonstration",
    "document": "document dokument dokumentum akt",
    "number": "no nr numero",
    "tome": "tome tomus tom volume vol",
    "distinction": "distinctio distinction",
    "lecture": "lectio lecture lesson",
    "fragment": "fragment fragmentum fragmenta",
    "paragraph": "paragraphus paragraph",
}
_KEYWORDS["chapter"] += " κεφαλαιον κεφ глава гл"
_KEYWORDS["book"] += " βιβλιον βιβλ книга кн"
_KEYWORDS["letter"] += " επιστολη письмо послание"
_KEYWORDS["homily"] += " ομιλια беседа"
_KEYWORDS["oration"] += " λογος слово"
_KEYWORDS["question"] += " ερωτησις вопрос"
_KEYWORDS["canon"] += " κανων правило"
_KEYWORDS["psalm"] += " ψαλμος псалом"
_KEYWORDS["article"] += " статья"
_KEYWORDS["part"] += " часть μερος"
KEYWORD_CANON: dict[str, str] = {}
for _canon, _variants in _KEYWORDS.items():
    for _v in _variants.split():
        KEYWORD_CANON.setdefault(_v, _canon)

_ROMAN_VALUES = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
ROMAN_MAX_LENGTH = 15  # MMMDCCCLXXXVIII, 3888, the longest numeral under 4000
_ROMAN_ANY = re.compile(r"^[IVXLCDM]{1,%d}$" % ROMAN_MAX_LENGTH)
_ROMAN_SHAPE = re.compile(r"^M{0,3}(?:CM|CD|D?C{0,4})(?:XC|XL|L?X{0,4})(?:IX|IV|V?I{0,4})$", re.I)
_NUM_TOKEN = re.compile(r"^(?:[IVXLCDMivxlcdm]{1,%d}|\d{1,4}[a-z]?|[^\W\d_]{3,10}|[α-ωΑ-Ω]{1,4}[ʹ΄'’′])$"
                        % ROMAN_MAX_LENGTH)
_GREEK_DIGITS = {"α": 1, "β": 2, "γ": 3, "δ": 4, "ε": 5, "ϛ": 6, "ζ": 7, "η": 8, "θ": 9, "ι": 10, "κ": 20,
                 "λ": 30, "μ": 40, "ν": 50, "ξ": 60, "ο": 70, "π": 80, "ϙ": 90, "ρ": 100, "σ": 200,
                 "ς": 200, "τ": 300, "υ": 400, "φ": 500, "χ": 600, "ψ": 700, "ω": 800}
_KW_LINE = re.compile(
    r"^\s{0,24}(?:(?:[IVXLC]{1,6}|\d{1,3})[.)]\s+)?(?P<kw>[^\W\d_]{2,12})\.?\s+(?P<num>\S{1,10}?)(?P<rest>[\s.,:;)\-—–*].*|)$"
)
_BARE_LINE = re.compile(r"^\s{0,32}[\[(]?(?P<num>[IVXLCDM]{1,15}|\d{1,4})[\])]?[.)]?\s*$")
_NUMTITLE_LINE = re.compile(r"^\s{0,16}(?P<num>[IVXLCDM]{1,15}|\d{1,3})[.)]\s+(?P<t>[A-ZÀ-ÞΑ-ΩЀ-Я«“\"'].{2,80})$")
_SECTION_LINE = re.compile(r"^\s{0,8}§\s*(?P<num>\d{1,4})")
_NUMPARA_LINE = re.compile(r"^\s{0,8}(?P<num>\d{1,4})[.)]\s+\S")
_BRACKET_LINE = re.compile(r"^\s{0,8}\[(?P<num>\d{1,4})\]\s*\S")
_PAGE_LINE = re.compile(r"^\s*[\[(]?\s*(?:page|pag|p|pp|seite|s|стр|σελ)\.?\s*\d{1,4}\s*[\])]?\s*$", re.I)
_PAGE_NUMBER = re.compile(r"^\s*\d{1,4}\s*$")
_BOILERPLATE = re.compile(r"^\s*(digitized by|generated for|google|http://www\.archive\.org|https?://|public domain)", re.I)
_NO_ALNUM = re.compile(r"^[^\w]*$")
_TOC_LINE = re.compile(r"(?:\.{3,}|\s{3,}|\s)\s*(?:\d{1,4}|[ivxlc]{1,6})\s*$")
_TRAIL_NUM = re.compile(r"\s*[.,:;(\[\-]*\b(?:[IVXLCDM]+|\d+)$")
_LEAD_NUM = re.compile(r"^(?:[IVXLCDM]+|\d+)\b[.,:;)\]\-]*\s*")

APPARATUS_HEADING = re.compile(
    r"^\W*(title page|preface|praefatio|prooemium|proemium|prologue|prolegomena|introduction|"
    r"introductory|contents|table of contents|table|index|indices|bibliograph|errata|addenda|"
    r"appendix|appendices|translator|editor|avertissement|vorwort|einleitung|inhalt|oglavlenie|"
    r"epilogue|notes?\b|footnotes|glossary|abbreviations|list of)",
    re.I,
)


def norm_key(s: str) -> str:
    return ordinals.fold(s)


def roman_value(tok: str) -> int | None:
    """A Roman numeral, upper or lower case, below 4000. Additive forms (IIII, XXXX)
    count; anything that is not shaped like a numeral (VX, IIX, MIXLCD) does not."""
    if not 1 <= len(tok) <= ROMAN_MAX_LENGTH or not _ROMAN_SHAPE.match(tok):
        return None
    total = 0
    vals = [_ROMAN_VALUES[c.lower()] for c in tok]
    for i, v in enumerate(vals):
        total += -v if i + 1 < len(vals) and vals[i + 1] > v else v
    return total if 0 < total < 4000 else None


def number_value(tok: str) -> int | None:
    t = tok.strip(".,:;)(").strip()
    if t.isdigit():
        return int(t)
    m = re.match(r"^(\d{1,4})[a-z]$", t)
    if m:
        return int(m.group(1))
    ordinal = ordinals.ordinal_value(t)
    if ordinal is not None:
        return ordinal
    g = re.match(r"^([α-ωΑ-Ω]{1,4})[ʹ΄'’′]$", t.strip())
    if g:
        letters = g.group(1).lower()
        if letters.startswith("στ"):
            return 6 + sum(_GREEK_DIGITS.get(c, 0) for c in letters[2:])
        return sum(_GREEK_DIGITS.get(c, 0) for c in letters) or None
    return roman_value(t)


@dataclass
class Heading:
    line: int
    family: str
    num: int | None
    label: str
    title: str


@dataclass
class Furniture:
    lines: set[int] = field(default_factory=set)
    kinds: dict[str, int] = field(default_factory=dict)


def header_end(lines: list[str]) -> int:
    """Index of the first line after the library's prepended metadata block
    (0 when the file has none)."""
    i = 0
    n = len(lines)
    seen = 0
    while i < n:
        ln = lines[i]
        m = re.match(r"^([A-Za-z][A-Za-z ]{1,24}):\s", ln + " ")
        if m and m.group(1).strip().lower() in HEADER_KEYS:
            seen += 1
            i += 1
            while i < n and lines[i][:1] in (" ", "\t") and lines[i].strip():
                i += 1
            continue
        break
    if seen < 3:
        return 0
    while i < n and not lines[i].strip():
        i += 1
    if i < n and lines[i].strip() == "---":
        i += 1
    return i


def _heading_key(line: str) -> str:
    s = re.sub(r"\s+", " ", line.strip().upper())
    for _ in range(4):
        t = _TRAIL_NUM.sub("", _LEAD_NUM.sub("", s)).strip()
        if t == s:
            break
        s = t
    return s


def find_furniture(lines: list[str], start: int) -> Furniture:
    fur = Furniture()

    def mark(i: int, kind: str):
        fur.lines.add(i)
        fur.kinds[kind] = fur.kinds.get(kind, 0) + 1

    page_candidates: list[int] = []
    repeats: dict[str, list[int]] = {}
    for i in range(start, len(lines)):
        ln = lines[i]
        s = ln.strip()
        if not s:
            continue
        if "\x0c" in ln and not s.strip("\x0c"):
            mark(i, "form-feed")
            continue
        if _NO_ALNUM.match(s):
            mark(i, "symbol-only")
            continue
        if _PAGE_LINE.match(s):
            mark(i, "page-marker")
            continue
        if _BOILERPLATE.match(s) and len(s) < 120:
            mark(i, "boilerplate")
            continue
        if _PAGE_NUMBER.match(s):
            page_candidates.append(i)
            continue
        if 6 <= len(s) <= 70:
            key = re.sub(r"\W+", " ", _heading_key(s).lower()).strip()
            if len(key) >= 6:
                repeats.setdefault(key, []).append(i)

    if len(page_candidates) >= 8:
        vals = [int(lines[i].strip()) for i in page_candidates]
        forward = sum(1 for a, b in zip(vals, vals[1:]) if 0 < b - a <= 2)
        gaps = [sum(len(x.split()) for x in lines[a + 1:b]) for a, b in zip(page_candidates, page_candidates[1:])]
        med = statistics.median(gaps)
        spread = statistics.pstdev(gaps) / med if med else 9.0
        if forward / (len(vals) - 1) >= 0.5 and PAGE_WORDS[0] <= med <= PAGE_WORDS[1] and spread < 0.6:
            for i in page_candidates:
                mark(i, "page-number")
    for key, idxs in repeats.items():
        if len(idxs) < 8:
            continue
        gaps = [b - a for a, b in zip(idxs, idxs[1:])]
        g = statistics.median(gaps)
        if g < 15:
            continue
        regular = sum(1 for x in gaps if 0.5 * g <= x <= 1.5 * g) / len(gaps)
        if regular >= 0.5:
            for i in idxs:
                mark(i, "running-head")
    return fur


def _kw_heading(line: str, prev_blank: bool) -> tuple[str, int | None, str] | None:
    m = _KW_LINE.match(line)
    if not m:
        return None
    kw = m.group("kw")
    canon = KEYWORD_CANON.get(norm_key(kw))
    if canon is None:
        return None
    if not kw[0].isupper():
        return None
    num_tok = m.group("num").rstrip(".,:;)")
    if not _NUM_TOKEN.match(num_tok):
        return None
    value = number_value(num_tok)
    if value is None:
        return None
    rest = m.group("rest") or ""
    if len(line.strip()) > 110:
        return None
    sep = rest[:1]
    body = rest.strip(" .,:;)-—–*")
    if body and sep.isspace() and body[:1].islower() and len(body.split()) > 1:
        return None
    if len(kw) <= 4 and not (prev_blank or kw.isupper()):
        return None
    if _TOC_LINE.search(line) and len(body.split()) > 1:
        return None
    return canon, value, kw


def find_headings(lines: list[str], start: int, furniture: set[int]) -> dict[str, list[Heading]]:
    families: dict[str, list[Heading]] = {}

    def add(h: Heading):
        families.setdefault(h.family, []).append(h)

    caps_candidates: list[tuple[int, str]] = []
    blank_before = True
    for i in range(start, len(lines)):
        ln = lines[i]
        s = ln.strip()
        if not s:
            blank_before = True
            continue
        was_blank = blank_before
        blank_before = False
        if i in furniture or len(s) > 110:
            continue
        c0 = s[0]
        if c0.isalpha():
            hit = _kw_heading(ln, was_blank)
            if hit:
                canon, value, kw = hit
                add(Heading(i, f"kw:{canon}", value, f"{canon}{value}", re.sub(r"\s+", " ", s)))
                continue
        m = _BARE_LINE.match(ln)
        if m and was_blank:
            value = number_value(m.group("num"))
            if value is not None:
                fam = "bare:roman" if _ROMAN_ANY.match(m.group("num")) else "bare:arabic"
                add(Heading(i, fam, value, f"n{value}", s))
                continue
        m = _NUMTITLE_LINE.match(ln)
        if m and was_blank:
            value = number_value(m.group("num"))
            if value is not None:
                add(Heading(i, "numtitle", value, f"s{value}", re.sub(r"\s+", " ", s)))
                continue
        m = _SECTION_LINE.match(ln)
        if m:
            add(Heading(i, "section", int(m.group("num")), f"sec{m.group('num')}", re.sub(r"\s+", " ", s)[:100]))
            continue
        m = _BRACKET_LINE.match(ln)
        if m:
            add(Heading(i, "bracket", int(m.group("num")), f"b{m.group('num')}", re.sub(r"\s+", " ", s)[:100]))
            continue
        m = _NUMPARA_LINE.match(ln)
        if m and was_blank:
            add(Heading(i, "numpara", int(m.group("num")), f"p{m.group('num')}", re.sub(r"\s+", " ", s)[:100]))
            continue
        if _is_caps_heading(s):
            caps_candidates.append((i, re.sub(r"\s+", " ", s)))

    counts: dict[str, int] = {}
    for _, text in caps_candidates:
        k = _heading_key(text)
        counts[k] = counts.get(k, 0) + 1
    for i, text in caps_candidates:
        if counts[_heading_key(text)] <= 3:
            add(Heading(i, "caps", None, f"line{i + 1}", text))
    return families


def _is_caps_heading(s: str) -> bool:
    if len(s) > 100 or any(c.islower() for c in s) or not any(c.isalpha() for c in s):
        return False
    words = s.split()
    if len(words) > 12:
        return False
    stripped = [w.strip(".,:;()[]-–—'\"") for w in words]
    return any(len(w) >= 3 and any(c.isalpha() for c in w) and not _ROMAN_ANY.match(w) for w in stripped)


def sequentiality(headings: list[Heading]) -> float:
    nums = [h.num for h in headings if h.num is not None]
    if len(nums) < 2:
        return 0.0
    ok = sum(1 for a, b in zip(nums, nums[1:]) if 0 < b - a <= 3 or b == 1)
    return ok / (len(nums) - 1)
