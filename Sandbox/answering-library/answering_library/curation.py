"""Hand curation of one source file's division scheme.

A curation file at curation/<file-stem>.yaml names the edition's own citation
scheme and says how to find its divisions: ordered rules (a regular expression
per division start, with named groups that build the locus and title), an
explicit list of divisions for files where no rule works, patterns for page
furniture, apparatus ranges, and language or speaker overrides per range. This
module loads and validates the file, resolves it against the file's lines and
measures the result. It never changes the vendored text.

Line numbers in curation files are 1-based. Patterns are matched against each
line with its whitespace collapsed to single spaces and both ends trimmed.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from functools import lru_cache
from re import _constants as _sre_c
from re import _parser as _sre_parse
from bisect import bisect_right
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from . import langscript
from . import markers as mk
from . import plain

CURATION_DIR = Path(__file__).resolve().parents[1] / "curation"
STATUSES = ("drafted", "sampled-ok", "needs-redo")
CURATED_MIN_COVER = 0.95
CURATED_MAX_DIVISION_WORDS = plain.OVERSIZE_WORDS
ALLOW_OVERSIZE_MAX_SUBHEADINGS = 10
_FOOTNOTE = re.compile(r"^\d{1,3}\)")
_SUBHEADING_FAMILIES = ("kw:", "bare:roman", "numtitle", "section", "numpara")
SPEAKER_STATES = ("known", "mixed", "unknown")

_TOP_KEYS = {"file", "scheme", "curator", "status", "language", "rules", "divisions", "ignore", "apparatus",
             "languages", "speakers", "evidence", "page_splits", "expected_gaps", "not_subheadings"}
_NOT_SUB_KEYS = {"lines", "kind", "quote"}
NOT_SUBHEADING_KINDS = ("footnote", "running-head", "ocr-debris", "quoted-list")
_EXPECTED_KEYS = {"series", "line", "quote", "reason"}
REASON_FORMS = {"leaf_missing": {"between"}, "counterpart": {"line"}, "edition_unnumbered": {"line", "quote"},
                "as_printed": {"line", "quote"},
                "head_unprinted": {"between", "line", "quote"}}
REASON_STEPS = {"leaf_missing": ("gaps",), "edition_unnumbered": ("gaps",), "head_unprinted": ("gaps",), "as_printed": ("repeated", "backward"),
                "counterpart": ("gaps", "repeated", "backward")}
_UPPER_NUMERAL = "IVXLCDM\u0399\u03a7\u039d\u0406\u0474"
_NUMERAL_STROKES = "0123456789|!\\^'[]()*TUHYWF\u03a4\u0397\u03a5\u0475"
_LOWER_STROKES = "ijlnry"
LOOKALIKE_MARGIN = "a margin number comes first"
LOOKALIKE_NUMERAL = "numeral in a form the pattern does not read"
LOOKALIKE_UNREAD = "a reading of the series whose numeral could not be read"
_RULE_KEYS = {"id", "pattern", "flags", "lines", "parent", "locus", "title", "division", "skip_repeat", "number",
              "ocr_map", "fixes", "allow_oversize", "context", "language"}
_CONTEXT_KEYS = {"prev_blank", "next_blank", "prev_short"}
_SHORT_KEYS = {"lines", "words"}
_DIVISION_KEYS = {"start_line", "locus", "title", "allow_oversize", "id", "parent", "number", "series", "takes_context"}
_PAGE_SPLIT_KEYS = {"pattern", "flags", "lines", "number", "locus", "only_oversize", "skip_repeat", "ocr_map"}
_IGNORE_KEYS = {"pattern", "kind", "lines"}
_APPARATUS_KEYS = {"lines", "kind", "locus"}
_LANGUAGE_KEYS = {"lines", "language", "evidence"}
_SPEAKER_KEYS = {"lines", "state", "voice", "evidence"}
_EVIDENCE_KEYS = {"line", "quote"}
_FIX_KEYS = {"line", "set", "quote"}
_FIELD = re.compile(r"\{(\w+)((?:\|[\w:]+)*)\}")
_LOCUS = re.compile(r"[^\s#]+")


class CurationError(ValueError):
    """A curation file that is malformed, or that cannot be applied to its text."""


@dataclass
class Rule:
    id: str
    rx: re.Pattern
    lines: list | None
    parent: str | None
    locus: str
    title: str
    division: bool
    skip_repeat: bool
    number: str | None
    ocr_map: dict
    fixes: dict
    allow_oversize: str
    context: dict
    language: frozenset | None


@dataclass
class PageSplit:
    rx: re.Pattern
    lines: list | None
    number: str
    locus: str
    only_oversize: bool
    skip_repeat: bool
    ocr_map: dict


@dataclass
class Curation:
    path: Path
    file: str
    scheme: str
    curator: str
    status: str
    language: str | None
    rules: list[Rule]
    divisions: list[dict]
    ignore: list[dict]
    apparatus: list[dict]
    languages: list[dict]
    speakers: list[dict]
    evidence: list[dict]
    sha256: str
    page_splits: list[PageSplit] = field(default_factory=list)
    expected_gaps: list[dict] = field(default_factory=list)
    not_subheadings: list[dict] = field(default_factory=list)

    @property
    def stem(self) -> str:
        return self.path.stem


@dataclass
class CDiv:
    start: int
    end: int
    locus: str
    title: str
    apparatus: bool
    origin: str
    allow_oversize: str = ""
    words: int = 0


@dataclass
class Resolved:
    divisions: list[CDiv]
    furniture: set[int]
    furniture_kinds: dict[str, int]
    line_offsets: list[int]
    rule_hits: dict[str, int]
    skipped_repeats: dict[str, int]
    sequences: dict[str, list[tuple[int, int | None]]]
    problems: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    sequence_groups: dict = field(default_factory=dict)
    header_end: int = 0
    furniture_words: int = 0
    total_words: int = 0
    header_words: int = 0


def _fail(path, message):
    raise CurationError(f"{path}: {message}")


def _ranges(value, where, allow_none=False):
    if value is None:
        if allow_none:
            return None
        raise CurationError(f"{where}: lines is required")
    pairs = [value] if value and not isinstance(value[0], (list, tuple)) else value
    out = []
    for pair in pairs:
        if (not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(isinstance(x, int) for x in pair)
                or pair[0] < 1 or pair[1] < pair[0]):
            raise CurationError(f"{where}: lines must be [first, last] with 1 <= first <= last")
        out.append((pair[0], pair[1]))
    return out


def _check_keys(entry, allowed, where):
    if not isinstance(entry, dict):
        raise CurationError(f"{where}: expected a mapping")
    extra = set(entry) - allowed
    if extra:
        raise CurationError(f"{where}: unknown field(s) {sorted(extra)}")


def _is_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _reason(value, where):
    """A normalised expected_gaps reason, or None when the entry has none. Free text is an error."""
    if value is None:
        return None
    forms = ", ".join(REASON_FORMS)
    if not isinstance(value, dict) or len(value) != 1:
        raise CurationError(f"{where}: reason must be a mapping with exactly one of {forms}; free text is not accepted")
    (form, body), = value.items()
    if form not in REASON_FORMS:
        raise CurationError(f"{where}: unknown reason '{form}'; the forms are {forms}")
    here = f"{where} reason {form}"
    _check_keys(body, REASON_FORMS[form], here)
    if set(body) != REASON_FORMS[form]:
        raise CurationError(f"{here}: needs {sorted(REASON_FORMS[form])}")
    out = {"form": form}
    if "between" in body:
        pair = body["between"]
        if (not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(_is_int(x) for x in pair)
                or not 1 <= pair[0] < pair[1]):
            raise CurationError(f"{here}: between must be [first, last] with 1 <= first < last")
        out["between"] = (pair[0], pair[1])
    if "line" in body:
        if not _is_int(body["line"]) or body["line"] < 1:
            raise CurationError(f"{here}: line must be a positive integer")
        out["line"] = body["line"]
    if "quote" in body:
        quote = " ".join(str(body["quote"] or "").split())
        if not quote:
            raise CurationError(f"{here}: quote may not be empty")
        out["quote"] = quote
    return out


def _template_fields(template, allowed, where):
    for m in _FIELD.finditer(template):
        if m.group(1) not in allowed:
            raise CurationError(f"{where}: template field '{m.group(1)}' is not a group of the pattern "
                                f"(available: {sorted(allowed)})")
    if _FIELD.sub("", template).count("{") or _FIELD.sub("", template).count("}"):
        raise CurationError(f"{where}: unbalanced braces in template '{template}'")


def _context(value, where):
    if value is None:
        return {}
    _check_keys(value, _CONTEXT_KEYS, f"{where} context")
    out = {}
    for key in ("prev_blank", "next_blank"):
        if key in value:
            if not isinstance(value[key], bool):
                raise CurationError(f"{where} context: {key} must be true or false")
            out[key] = value[key]
    if "prev_short" in value:
        short = value["prev_short"]
        _check_keys(short, _SHORT_KEYS, f"{where} context prev_short")
        if not all(isinstance(short.get(k), int) and short[k] >= 1 for k in _SHORT_KEYS):
            raise CurationError(f"{where} context: prev_short needs integer lines and words, each at least 1")
        out["prev_short"] = (short["lines"], short["words"])
    if not out:
        raise CurationError(f"{where}: context names no condition")
    return out


def _language_guard(value, where):
    if value is None:
        return None
    codes = frozenset([value] if isinstance(value, str) else value or [])
    bad = codes - langscript.LANGUAGE_CODES
    if not codes or bad:
        raise CurationError(f"{where}: language must name language codes {sorted(langscript.LANGUAGE_CODES)}; "
                            f"got {sorted(bad) or 'none'}")
    return codes


def _page_split(ps, where):
    _check_keys(ps, _PAGE_SPLIT_KEYS, where)
    for key in ("pattern", "number"):
        if not ps.get(key):
            raise CurationError(f"{where}: '{key}' is required")
    if ps.get("flags") not in (None, "i"):
        raise CurationError(f"{where}: flags may only be 'i'")
    try:
        rx = re.compile(ps["pattern"], re.I if ps.get("flags") == "i" else 0)
    except re.error as exc:
        raise CurationError(f"{where}: bad pattern: {exc}") from exc
    if ps["number"] not in rx.groupindex:
        raise CurationError(f"{where}: number names '{ps['number']}', which is not a group of the pattern")
    locus = ps.get("locus") or "p{%s|int}" % ps["number"]
    _template_fields(locus, set(rx.groupindex) | {"line", "enclosing"}, f"{where} locus")
    return PageSplit(rx=rx, lines=_ranges(ps.get("lines"), where, allow_none=True), number=ps["number"], locus=locus,
                     only_oversize=bool(ps.get("only_oversize", False)), skip_repeat=bool(ps.get("skip_repeat", False)),
                     ocr_map={str(a): str(b) for a, b in (ps.get("ocr_map") or {}).items()})


def _check_levels(name, rules, divisions):
    """Rule ids and explicit-division ids are the levels a parent may name; parents may not loop."""
    rule_ids = {r.id for r in rules}
    parents: dict[str, str | None] = {r.id: r.parent for r in rules}
    for d in divisions:
        if not d["id"]:
            continue
        if d["id"] in rule_ids or (d["id"] in parents and parents[d["id"]] != d["parent"]):
            raise CurationError(f"{name}: division id '{d['id']}' is also a rule id or has a different parent")
        parents[d["id"]] = d["parent"]
    for d in divisions:
        if d["parent"] and d["parent"] not in parents:
            raise CurationError(f"{name}: division at line {d['start'] + 1} names parent '{d['parent']}', "
                                "which is not a rule or division id")
        if d["series"] and d["series"] not in {r.id for r in rules if r.number}:
            raise CurationError(f"{name}: division at line {d['start'] + 1} names series '{d['series']}', "
                                "which is not a rule with a number group")
    for rid, parent in parents.items():
        if parent and parent not in parents:
            raise CurationError(f"{name}: '{rid}' names parent '{parent}', which is not a rule or division id")
        chain, cur = {rid}, parent
        while cur:
            if cur in chain:
                raise CurationError(f"{name}: parents form a loop at '{rid}'")
            chain.add(cur)
            cur = parents[cur]


def load(path: Path) -> Curation:
    path = Path(path)
    raw = path.read_bytes()
    try:
        data = yaml.safe_load(raw.decode("utf-8"))
    except yaml.YAMLError as exc:
        raise CurationError(f"{path.name}: not valid YAML: {exc}") from exc
    name = path.name
    _check_keys(data, _TOP_KEYS, name)
    for key in ("file", "scheme", "curator", "status", "evidence"):
        if not data.get(key):
            raise CurationError(f"{name}: '{key}' is required")
    if Path(data["file"]).stem != path.stem:
        raise CurationError(f"{name}: file '{data['file']}' does not match the curation file name")
    if data["status"] not in STATUSES:
        raise CurationError(f"{name}: status must be one of {STATUSES}")
    if not isinstance(data["scheme"], str) or "\n" in data["scheme"].strip():
        raise CurationError(f"{name}: scheme must be one line")
    if not data.get("rules") and not data.get("divisions"):
        raise CurationError(f"{name}: needs rules or divisions")

    rules, seen = [], set()
    for k, r in enumerate(data.get("rules") or []):
        where = f"{name} rules[{k}]"
        _check_keys(r, _RULE_KEYS, where)
        for key in ("id", "pattern", "locus"):
            if not r.get(key):
                raise CurationError(f"{where}: '{key}' is required")
        if r["id"] in seen:
            raise CurationError(f"{where}: duplicate rule id '{r['id']}'")
        seen.add(r["id"])
        flags = re.I if r.get("flags") == "i" else 0
        if r.get("flags") not in (None, "i"):
            raise CurationError(f"{where}: flags may only be 'i'")
        try:
            rx = re.compile(r["pattern"], flags)
        except re.error as exc:
            raise CurationError(f"{where}: bad pattern: {exc}") from exc
        allowed = set(rx.groupindex) | {"line", "next", "parent"}
        _template_fields(r["locus"], allowed, f"{where} locus")
        _template_fields(r.get("title", ""), allowed, f"{where} title")
        if r.get("number") and r["number"] not in rx.groupindex:
            raise CurationError(f"{where}: number names '{r['number']}', which is not a group of the pattern")
        fixes = {}
        for f in r.get("fixes") or []:
            _check_keys(f, _FIX_KEYS, f"{where} fixes")
            bad = set(f.get("set") or {}) - set(rx.groupindex)
            if not isinstance(f.get("line"), int) or not f.get("set") or bad:
                raise CurationError(f"{where}: a fix needs an integer line and groups of the pattern to set")
            quote = " ".join(str(f["quote"]).split()) if f.get("quote") is not None else None
            if f.get("quote") is not None and not quote:
                raise CurationError(f"{where}: a fix quote may not be empty")
            fixes[f["line"] - 1] = {"set": {g: str(v) for g, v in f["set"].items()}, "quote": quote}
        context = _context(r.get("context"), where)
        language = _language_guard(r.get("language"), where)
        rules.append(Rule(
            id=r["id"], rx=rx, lines=_ranges(r.get("lines"), where, allow_none=True), parent=r.get("parent"),
            locus=r["locus"], title=r.get("title", ""), division=r.get("division", True),
            skip_repeat=bool(r.get("skip_repeat", False)), number=r.get("number"),
            ocr_map={str(a): str(b) for a, b in (r.get("ocr_map") or {}).items()}, fixes=fixes,
            allow_oversize=(r.get("allow_oversize") or "").strip(), context=context, language=language))

    divisions = []
    for k, d in enumerate(data.get("divisions") or []):
        where = f"{name} divisions[{k}]"
        _check_keys(d, _DIVISION_KEYS, where)
        if not isinstance(d.get("start_line"), int) or d["start_line"] < 1 or not d.get("locus"):
            raise CurationError(f"{where}: needs start_line and locus")
        if not _LOCUS.fullmatch(str(d["locus"])):
            raise CurationError(f"{where}: locus may not contain spaces or '#'")
        number = d.get("number")
        if number is not None:
            number = number if isinstance(number, int) and not isinstance(number, bool) else mk.number_value(str(number))
            if number is None:
                raise CurationError(f"{where}: number '{d['number']}' cannot be read as a number")
        if d.get("series") and number is None:
            raise CurationError(f"{where}: series needs a number")
        divisions.append({"start": d["start_line"] - 1, "locus": str(d["locus"]),
                          "title": " ".join(str(d.get("title") or "").split()),
                          "allow_oversize": (d.get("allow_oversize") or "").strip(), "id": d.get("id"),
                          "parent": d.get("parent"), "number": number, "series": d.get("series"),
                          "takes_context": bool(d.get("takes_context", False))})
    _check_levels(name, rules, divisions)

    ignore = []
    for k, ig in enumerate(data.get("ignore") or []):
        where = f"{name} ignore[{k}]"
        ig = {"pattern": ig} if isinstance(ig, str) else ig
        _check_keys(ig, _IGNORE_KEYS, where)
        try:
            rx = re.compile(ig["pattern"])
        except (re.error, KeyError, TypeError) as exc:
            raise CurationError(f"{where}: bad or missing pattern: {exc}") from exc
        ignore.append({"rx": rx, "kind": ig.get("kind", "furniture"), "lines": _ranges(ig.get("lines"), where, True)})

    apparatus = []
    for k, a in enumerate(data.get("apparatus") or []):
        where = f"{name} apparatus[{k}]"
        _check_keys(a, _APPARATUS_KEYS, where)
        if not a.get("kind"):
            raise CurationError(f"{where}: kind is required")
        (first, last), = _ranges(a.get("lines"), where)
        if a.get("locus") and not _LOCUS.fullmatch(str(a["locus"])):
            raise CurationError(f"{where}: locus may not contain spaces or '#'")
        apparatus.append({"first": first - 1, "last": last - 1, "kind": a["kind"], "locus": a.get("locus")})

    page_splits = [_page_split(ps, f"{name} page_splits[{k}]") for k, ps in enumerate(data.get("page_splits") or [])]

    expected_gaps = []
    for k, e in enumerate(data.get("expected_gaps") or []):
        where = f"{name} expected_gaps[{k}]"
        _check_keys(e, _EXPECTED_KEYS, where)
        if not e.get("series") or not _is_int(e.get("line")) or not " ".join(str(e.get("quote") or "").split()):
            raise CurationError(f"{where}: needs series, an integer line and a quote")
        expected_gaps.append({"series": e["series"], "line": e["line"], "quote": " ".join(str(e["quote"]).split()),
                              "reason": _reason(e.get("reason"), where)})

    not_subheadings = []
    for k, e in enumerate(data.get("not_subheadings") or []):
        where = f"{name} not_subheadings[{k}]"
        _check_keys(e, _NOT_SUB_KEYS, where)
        if e.get("kind") not in NOT_SUBHEADING_KINDS:
            raise CurationError(f"{where}: kind must be one of {NOT_SUBHEADING_KINDS}")
        quote = " ".join(str(e.get("quote") or "").split())
        spans = []
        for item in e.get("lines") or []:
            pair = [item, item] if isinstance(item, int) else item
            if (not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(isinstance(x, int) for x in pair)
                    or pair[0] < 1 or pair[1] < pair[0]):
                raise CurationError(f"{where}: lines must be line numbers or [first, last] ranges")
            spans.append((pair[0], pair[1]))
        if not spans or not quote:
            raise CurationError(f"{where}: needs lines and a quote from the first listed line")
        not_subheadings.append({"spans": spans, "kind": e["kind"], "quote": quote})

    languages = []
    for k, a in enumerate(data.get("languages") or []):
        where = f"{name} languages[{k}]"
        _check_keys(a, _LANGUAGE_KEYS, where)
        (first, last), = _ranges(a.get("lines"), where)
        if not a.get("language") or not (a.get("evidence") or "").strip():
            raise CurationError(f"{where}: language and evidence are required")
        languages.append({"first": first - 1, "last": last - 1, "language": a["language"], "evidence": a["evidence"]})

    speakers = []
    for k, a in enumerate(data.get("speakers") or []):
        where = f"{name} speakers[{k}]"
        _check_keys(a, _SPEAKER_KEYS, where)
        (first, last), = _ranges(a.get("lines"), where)
        if a.get("state") not in SPEAKER_STATES or not (a.get("evidence") or "").strip():
            raise CurationError(f"{where}: state must be one of {SPEAKER_STATES} and evidence is required")
        if (a["state"] == "known") != bool(a.get("voice")):
            raise CurationError(f"{where}: voice is given exactly when state is 'known'")
        speakers.append({"first": first - 1, "last": last - 1, "state": a["state"], "voice": a.get("voice"),
                         "evidence": a["evidence"]})

    evidence = []
    for k, e in enumerate(data["evidence"]):
        where = f"{name} evidence[{k}]"
        _check_keys(e, _EVIDENCE_KEYS, where)
        if not isinstance(e.get("line"), int) or not (e.get("quote") or "").strip():
            raise CurationError(f"{where}: needs an integer line and a quote")
        evidence.append({"line": e["line"], "quote": " ".join(e["quote"].split())})

    return Curation(path=path, file=data["file"], scheme=data["scheme"].strip(), curator=str(data["curator"]),
                    status=data["status"], language=data.get("language"), rules=rules, divisions=divisions,
                    ignore=ignore, apparatus=apparatus, languages=languages, speakers=speakers, evidence=evidence,
                    sha256=hashlib.sha256(raw).hexdigest(), page_splits=page_splits,
                    expected_gaps=expected_gaps, not_subheadings=not_subheadings)


def for_file(filename: str, directory: Path | None = None, applied_only: bool = True) -> Curation | None:
    """The curation for a vendored file, or None. A curation marked needs-redo
    is not applied unless applied_only is False."""
    path = Path(directory or CURATION_DIR) / (Path(filename).stem + ".yaml")
    if not path.exists():
        return None
    cur = load(path)
    if cur.file != filename:
        raise CurationError(f"{path.name}: names file '{cur.file}', not '{filename}'")
    if applied_only and cur.status == "needs-redo":
        return None
    return cur


def load_all(filenames, directory: Path | None = None) -> list[Curation]:
    """Every curation file in the directory, each checked against the union's file names."""
    directory = Path(directory or CURATION_DIR)
    if not directory.exists():
        return []
    by_stem = {Path(f).stem: f for f in filenames}
    out = []
    for path in sorted(directory.glob("*.yaml")):
        cur = load(path)
        if by_stem.get(path.stem) != cur.file:
            raise CurationError(f"{path.name}: no file '{cur.file}' in the union of shelves")
        out.append(cur)
    return out


def digest(curations: list[Curation]) -> str:
    h = hashlib.sha256()
    for c in sorted(curations, key=lambda c: (c.stem, c.sha256)):
        h.update(f"{c.stem}\t{c.status}\t{c.sha256}\n".encode())
    return h.hexdigest()


def to_int(token: str, ocr_map: dict | None = None) -> int | None:
    text = "".join((ocr_map or {}).get(ch, ch) for ch in token)
    return mk.number_value(text)


def render(template: str, values: dict, ocr_map: dict, where: str, exact=frozenset()) -> str:
    """Fill a template. Groups named in exact (values a fix set by hand) skip the OCR map."""
    def sub(m):
        value = values.get(m.group(1))
        value = "" if value is None else str(value)
        for flt in [f for f in m.group(2).split("|") if f]:
            name, _, arg = flt.partition(":")
            if name == "int":
                number = to_int(value, None if m.group(1) in exact else ocr_map)
                if number is None:
                    raise CurationError(f"{where}: cannot read '{value}' as a number")
                value = str(number).zfill(int(arg)) if arg else str(number)
            elif name == "slug":
                value = re.sub(r"[^\w]+", "-", value.lower()).strip("-")
            elif name == "lower":
                value = value.lower()
            elif name == "upper":
                value = value.upper()
            else:
                raise CurationError(f"{where}: unknown filter '{name}'")
        return value

    return _FIELD.sub(sub, template)


def _in(ranges, i):
    return ranges is None or any(a - 1 <= i <= b - 1 for a, b in ranges)


def _valid_locus(locus, where):
    if not _LOCUS.fullmatch(locus):
        raise CurationError(f"{where}: locus '{locus}' is empty or contains spaces or '#'")


def _loosened(rule):
    """The rule's pattern with its numeral group widened to any run of non-space characters, or None."""
    if not rule.number:
        return None
    src = rule.rx.pattern
    start = src.find(f"(?P<{rule.number}>")
    if start < 0:
        return None
    depth, k, in_class = 0, start, False
    while k < len(src):
        ch = src[k]
        if ch == "\\":
            k += 2
            continue
        if in_class:
            in_class = ch != "]"
        elif ch == "[":
            in_class = True
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                break
        k += 1
    wide = src[:start] + f"(?P<{rule.number}>\\S{{1,15}})" + src[k + 1:]
    try:
        return re.compile(wide, rule.rx.flags)
    except re.error:
        return None


def _numeral_shaped(token: str, rule) -> bool:
    """Whether a token could be a numeral the scan has mangled. It is short and made of numeral letters,
    digits, the strokes OCR puts in their place and the characters the rule's ocr_map names. The lowercase
    strokes i j l n r y count only in a token that also holds an uppercase numeral letter, so a lowercase body
    word such as xxi is not a numeral unless the rule ignores case or its ocr_map names the letters."""
    token = "".join(ch for ch in unicodedata.normalize("NFD", token.strip(".,;:'\u2019\u1fbf"))
                    if not unicodedata.combining(ch))
    mapped = set(rule.ocr_map) | set(rule.ocr_map.values())
    allowed = set(_UPPER_NUMERAL) | set(_NUMERAL_STROKES) | mapped
    if rule.rx.flags & re.IGNORECASE:
        allowed |= set("vxcdm")
    if any(ch in _UPPER_NUMERAL for ch in token):
        allowed |= set(_LOWER_STROKES)
    return 0 < len(token) <= 12 and all(ch in allowed for ch in token)


def _prefix_items(items, group):
    """The parsed pattern items before the numeral group, flattened through enclosing groups, or None."""
    for k, (op, av) in enumerate(items):
        if op is _sre_c.SUBPATTERN:
            if av[0] == group:
                return list(items[:k])
            inner = _prefix_items(av[3], group)
            if inner is not None:
                return list(items[:k]) + inner
    return None


def _requires_word(items) -> bool:
    for op, av in items:
        if op is _sre_c.LITERAL and chr(av).isalpha():
            return True
        if op is _sre_c.IN and av and all(o is _sre_c.LITERAL for o, _ in av) and any(chr(a).isalpha() for _, a in av):
            return True
        if op is _sre_c.SUBPATTERN and _requires_word(av[3]):
            return True
        if op is _sre_c.BRANCH and all(_requires_word(list(b)) for b in av[1]):
            return True
        if op in (_sre_c.MAX_REPEAT, _sre_c.MIN_REPEAT) and av[0] >= 1 and _requires_word(list(av[2])):
            return True
    return False


@lru_cache(maxsize=None)
def _pattern_requires_word(pattern: str, flags: int, group: int) -> bool:
    prefix = _prefix_items(_sre_parse.parse(pattern, flags), group)
    return bool(prefix) and _requires_word(prefix)


def requires_head_word(rule) -> bool:
    """Whether the rule's pattern demands a literal word (Caput, C., SERMO) before the numeral group. A prefix of
    optional groups or free-token classes does not."""
    group = rule.rx.groupindex.get(rule.number)
    return bool(group) and _pattern_requires_word(rule.rx.pattern, rule.rx.flags, group)


def _lookalike(rule, loose, text):
    """Why a line that the rule's pattern does not match is still a head of the series, or None. It is one when a
    margin number comes first, or when the numeral position holds a token that looks like a mangled numeral. A
    pattern that requires a literal head word before the numeral (Caput, C., SERMO) makes any token there a
    numeral, because the head word already makes the line a heading."""
    if rule.rx.search(text):
        return None
    stripped = re.sub(r"^\d{1,5}\s+", "", text)
    if stripped != text and rule.rx.search(stripped):
        return LOOKALIKE_MARGIN
    m = loose.search(text) if loose is not None else None
    if m is None:
        return None
    if requires_head_word(rule) or _numeral_shaped(m.group(rule.number) or "", rule):
        return LOOKALIKE_NUMERAL
    return None


def previous_lines(seq: list, groups: list | None = None) -> dict[int, int]:
    """For each reading of a series, the line of the reading before it in the same group."""
    out, prev_line, prev_group = {}, None, None
    for k, (line, _value) in enumerate(seq):
        group = groups[k] if groups else None
        if group != prev_group:
            prev_line = None
        if prev_line is not None:
            out[line] = prev_line
        prev_line, prev_group = line, group
    return out


def _subheadings(part: list[str], furniture: set[int]) -> list[tuple[int, str]]:
    """Lines of a division that look like numbered sub-headings, by the segmenter's own marker families."""
    found = mk.find_headings(part, 0, furniture)
    out = {h.line: h.title for fam, hs in found.items() if fam.startswith(_SUBHEADING_FAMILIES) for h in hs
           if h.line > 0 and not _FOOTNOTE.match(h.title)}
    return sorted(out.items())


def _line_list(lines, limit=8):
    shown = ", ".join(str(x) for x in lines[:limit])
    return shown + (f" and {len(lines) - limit} more" if len(lines) > limit else "")


def resolve(cur: Curation, lines: list[str], codes: list[str] | None = None) -> Resolved:
    """Divisions, furniture and diagnostics of one file under one curation.
    Divisions tile the body (every line after the library header) with no gap.
    codes are the file's language codes, used by a rule's language guard."""
    n = len(lines)
    h_end = mk.header_end(lines)
    norm = [" ".join(ln.split()) for ln in lines]
    offsets, pos = [], 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1
    offsets.append(pos - 1)
    words = [len(ln.split()) for ln in lines]
    codes = list(codes) if codes else ([cur.language] if cur.language else [])

    furniture: set[int] = set()
    kinds: Counter = Counter()
    ignored_by: dict[int, str] = {}
    for i in range(h_end, n):
        if not norm[i]:
            continue
        for ig in cur.ignore:
            if _in(ig["lines"], i) and ig["rx"].search(norm[i]):
                furniture.add(i)
                kinds[ig["kind"]] += 1
                ignored_by[i] = ig["rx"].pattern
                break

    def blankish(j):
        return j < h_end or j >= n or not norm[j] or j in furniture

    languages: dict[int, str] = {}

    def language_at(i):
        if i not in languages:
            languages[i] = langscript.language_of(norm[i], langscript.script_of(norm[i]), codes)
        return languages[i]

    def context_ok(rule, i):
        c = rule.context
        if "prev_blank" in c and blankish(i - 1) != c["prev_blank"]:
            return False
        if "next_blank" in c and blankish(i + 1) != c["next_blank"]:
            return False
        if "prev_short" in c:
            count, most = c["prev_short"]
            return all(blankish(j) or len(norm[j].split()) <= most for j in range(i - count, i))
        return True

    def match(rule, i, allow_forced=True):
        """The pattern's groups when the rule applies to line i, else None. A fix that carries a
        quote found on the line makes the rule apply there whatever the pattern says."""
        m = rule.rx.search(norm[i]) if _in(rule.lines, i) else None
        if m is not None and context_ok(rule, i) and (rule.language is None or language_at(i) in rule.language):
            return m.groupdict()
        fix = rule.fixes.get(i)
        if allow_forced and fix and fix["quote"] and fix["quote"] in norm[i]:
            return {g: None for g in rule.rx.groupindex}
        return None

    parent_of: dict[str, str | None] = {r.id: r.parent for r in cur.rules}
    for d in cur.divisions:
        if d["id"]:
            parent_of[d["id"]] = d["parent"]
    children: dict[str, list[str]] = {k: [] for k in parent_of}
    for k, p in parent_of.items():
        if p:
            children[p].append(k)

    def descendants(rid):
        for c in children[rid]:
            yield c
            yield from descendants(c)

    explicit_at: dict[int, dict] = {}
    for d in cur.divisions:
        if not (h_end <= d["start"] < n):
            raise CurationError(f"{cur.path.name}: division at line {d['start'] + 1} is outside the body "
                                f"(lines {h_end + 1}-{n})")
        if d["start"] in explicit_at:
            raise CurationError(f"{cur.path.name}: two explicit divisions start at line {d['start'] + 1}")
        explicit_at[d["start"]] = d

    starts: dict[int, dict] = {}
    context: dict[str, str] = {}
    last: dict[str, str] = {}
    hits: Counter = Counter()
    repeats: Counter = Counter()
    context_repeats: dict[str, list[int]] = {}
    sequences: dict[str, list] = {r.id: [] for r in cur.rules if r.number}
    seq_groups: dict[str, list] = {r.id: [] for r in cur.rules if r.number}
    used_fixes: set[tuple[str, int]] = set()
    notes: list[str] = []
    claimed: set[int] = set()
    pending: int | None = None
    pending_rule = ""

    def set_context(level, full):
        context[level] = full
        last[level] = full
        for d in descendants(level):
            context.pop(d, None)
            last.pop(d, None)

    def take_pending(start):
        """The line a division starting at `start` really begins on: the context heading waiting
        for it, if there is one."""
        nonlocal pending
        if pending is None:
            return start
        begin = pending
        stray = sum(words[j] for j in range(begin + 1, start) if j not in furniture)
        if stray:
            notes.append(f"context rule '{pending_rule}' at line {begin + 1}: {stray} words between it and the "
                         f"division heading at line {start + 1} belong to that division")
        pending = None
        return begin

    for i in range(h_end, n):
        d = explicit_at.get(i)
        if d is not None:
            where = f"line {i + 1} division"
            if d["parent"] and d["parent"] not in context:
                raise CurationError(f"{where}: starts before its parent '{d['parent']}' ever matched")
            full = f"{context[d['parent']]}/{d['locus']}" if d["parent"] else d["locus"]
            _valid_locus(full, where)
            starts[take_pending(i) if d["takes_context"] else i] = {
                "locus": full, "title": d["title"], "origin": "marker", "allow_oversize": d["allow_oversize"]}
            claimed.add(i)
            if d["id"]:
                set_context(d["id"], full)
            if d["number"] is not None:
                key = d["series"] or "divisions"
                sequences.setdefault(key, []).append((i + 1, d["number"]))
                seq_groups.setdefault(key, []).append(context.get(parent_of.get(d["series"]), "") if d["series"] else "")
        if i in furniture or not norm[i]:
            continue
        forced = [r for r in cur.rules if (r.fixes.get(i) or {}).get("quote")]
        for rule in forced + [r for r in cur.rules if r not in forced]:
            groups = match(rule, i)
            if groups is None:
                continue
            where = f"line {i + 1} rule '{rule.id}'"
            values = dict(groups)
            fix = rule.fixes.get(i)
            exact = frozenset()
            if fix:
                values.update(fix["set"])
                exact = frozenset(fix["set"])
                used_fixes.add((rule.id, i))
            if rule.parent and rule.parent not in context:
                raise CurationError(f"{where}: matched before its parent rule '{rule.parent}' ever matched")
            values["line"] = i + 1
            values["parent"] = context.get(rule.parent, "")
            values["next"] = next((norm[j] for j in range(i + 1, min(n, i + 40)) if norm[j] and j not in furniture), "")
            part = render(rule.locus, values, rule.ocr_map, where, exact)
            full = f"{context[rule.parent]}/{part}" if rule.parent else part
            _valid_locus(full, where)
            if rule.skip_repeat and last.get(rule.id) == full:
                repeats[rule.id] += 1
                break
            if not rule.division and not rule.skip_repeat and last.get(rule.id) == full:
                context_repeats.setdefault(rule.id, []).append(i + 1)
            hits[rule.id] += 1
            set_context(rule.id, full)
            if rule.number:
                reading = values.get(rule.number) or ""
                sequences[rule.id].append((i + 1, to_int(reading, None if rule.number in exact else rule.ocr_map)))
                seq_groups[rule.id].append(values["parent"])
            if i in claimed:
                break
            if rule.division:
                title = " ".join(render(rule.title, values, rule.ocr_map, where, exact).split())
                starts[take_pending(i)] = {"locus": full, "title": title, "origin": "marker",
                                           "allow_oversize": rule.allow_oversize}
            elif pending is None:
                pending, pending_rule = i, rule.id
            break
    if pending is not None:
        starts.setdefault(pending, {"locus": f"text/line{pending + 1}", "title": "", "origin": "gap",
                                    "allow_oversize": ""})

    for rid, at in context_repeats.items():
        notes.append(f"context rule '{rid}' matched again with an unchanged address at lines {_line_list(at)}; "
                     "if these are running heads, add skip_repeat or narrow the rule's lines")
    shadows: dict[tuple[str, str], list[int]] = {}
    for i in sorted(furniture):
        for rule in cur.rules:
            if match(rule, i, allow_forced=False) is not None:
                shadows.setdefault((ignored_by[i], rule.id), []).append(i + 1)
                break
    for (pattern, rid), at in shadows.items():
        notes.append(f"ignore pattern '{pattern}' declares {len(at)} line(s) furniture that rule '{rid}' also "
                     f"matches: {_line_list(at)}")

    for rule in cur.rules:
        if rule.lines is None:
            continue
        loose = _loosened(rule)
        missed = []
        for i in range(h_end, n):
            if not norm[i] or i in furniture or i in rule.fixes or not _in(rule.lines, i):
                continue
            kind = _lookalike(rule, loose, norm[i])
            if kind:
                missed.append((i, kind))
        if missed:
            counts = Counter(kind for _, kind in missed)
            summary = "; ".join(f"{counts[k]} {k}" for k in (LOOKALIKE_NUMERAL, LOOKALIKE_MARGIN) if counts[k])
            detail = "".join(f'\n      line {i + 1} ({kind}): "{norm[i][:70]}"' for i, kind in missed)
            notes.append(f"rule '{rule.id}' has hand-listed lines, and {len(missed)} line(s) in them look like its "
                         f"heading but did not match: {summary}{detail}")

    ranges = []
    for a in cur.apparatus:
        first, last_line = max(a["first"], h_end), min(a["last"], n - 1)
        if first > last_line:
            continue
        ranges.append((first, last_line))
        if first not in starts or starts[first]["origin"] == "gap":
            starts[first] = {"locus": a["locus"] or f"{a['kind']}/line{first + 1}", "title": "",
                             "origin": "apparatus", "allow_oversize": ""}
    for first, last_line in ranges:
        if last_line + 1 < n:
            starts.setdefault(last_line + 1, {"locus": f"text/line{last_line + 2}", "title": "", "origin": "gap",
                                              "allow_oversize": ""})
    if h_end < n and h_end not in starts:
        first_start = min(starts) if starts else n
        if any(words[i] for i in range(h_end, first_start) if i not in furniture):
            starts[h_end] = {"locus": f"text/line{h_end + 1}", "title": "", "origin": "gap", "allow_oversize": ""}

    def tile(table):
        out: list[CDiv] = []
        if h_end:
            out.append(CDiv(0, h_end, "header", "", True, "header"))
        order = sorted(table)
        for k, s in enumerate(order):
            e = order[k + 1] if k + 1 < len(order) else n
            info = table[s]
            in_apparatus = any(a <= s <= b for a, b in ranges)
            div = CDiv(s, e, info["locus"], info["title"], in_apparatus, info["origin"], info["allow_oversize"])
            div.words = sum(words[i] for i in range(s, e) if i not in furniture)
            out.append(div)
        if out and out[0].origin == "header":
            out[0].words = sum(words[:h_end])
        return out

    problems = []
    if cur.page_splits:
        body = [d for d in tile(starts) if d.origin != "header"]
        body_starts = [d.start for d in body]
        page_starts: dict[int, dict] = {}
        for k, ps in enumerate(cur.page_splits):
            key = f"page_splits[{k}]"
            sequences[key] = []
            seq_groups[key] = []
            added, touched, previous = [], {}, None
            for i in range(h_end, n):
                if not norm[i] or not _in(ps.lines, i) or any(a <= i <= b for a, b in ranges):
                    continue
                m = ps.rx.search(norm[i])
                if m is None or i in starts or i in page_starts:
                    continue
                at = bisect_right(body_starts, i) - 1
                if at < 0:
                    continue
                enclosing = body[at]
                oversize = (enclosing.words > CURATED_MAX_DIVISION_WORDS and not enclosing.apparatus
                            and not enclosing.allow_oversize)
                if ps.only_oversize and not oversize:
                    continue
                where = f"line {i + 1} page split {k + 1}"
                values = dict(m.groupdict(), line=i + 1, enclosing=enclosing.locus)
                locus = render(ps.locus, values, ps.ocr_map, where)
                _valid_locus(locus, where)
                sequences[key].append((i + 1, to_int(values.get(ps.number) or "", ps.ocr_map)))
                seq_groups[key].append("")
                if ps.skip_repeat and previous == locus:
                    continue
                previous = locus
                page_starts[i] = {"locus": locus, "title": "", "origin": "marker", "allow_oversize": ""}
                added.append(i + 1)
                touched[at] = (enclosing.words, oversize)
            if not added:
                problems.append(f"page split {k + 1} matched no line")
                continue
            fixed = sum(w for w, o in touched.values() if o)
            other = sum(w for w, o in touched.values() if not o)
            note = (f"page split {k + 1}: {len(added)} page heads start new divisions (lines {_line_list(added, 4)}) "
                    f"inside {len(touched)} existing division(s); {fixed} oversize words divided")
            if other > fixed:
                note += (f"; it also divides {other} words in divisions that were not oversize, more than the "
                         f"{fixed} oversize words it fixes (set only_oversize or narrow lines)")
            notes.append(note)
        starts.update(page_starts)

    divisions = tile(starts)

    for r in cur.rules:
        if not hits[r.id]:
            problems.append(f"rule '{r.id}' matched no line")
        for line in sorted(r.fixes):
            quote = r.fixes[line]["quote"]
            if quote and not (0 <= line < n and quote in norm[line]):
                problems.append(f"fix at line {line + 1} of rule '{r.id}' quotes text that is not on the line: "
                                f"\"{quote}\"")
            elif (r.id, line) not in used_fixes:
                problems.append(f"fix at line {line + 1} of rule '{r.id}' does not land on a match"
                                if not quote else
                                f"fix at line {line + 1} of rule '{r.id}' was not reached: the line is blank "
                                "or declared furniture")
    for e in cur.evidence:
        i = e["line"] - 1
        if not 0 <= i < n or e["quote"] not in norm[i]:
            problems.append(f"evidence at line {e['line']} does not quote the file: \"{e['quote']}\"")

    allowed = {x for e in cur.not_subheadings for a, b in e["spans"] for x in range(a, b + 1)}
    flagged: set[int] = set()
    for d in divisions:
        if d.allow_oversize and not d.apparatus and d.words > CURATED_MAX_DIVISION_WORDS:
            subs = [(d.start + r + 1, t) for r, t in
                    _subheadings(lines[d.start:d.end], {j - d.start for j in furniture if d.start <= j < d.end})]
            flagged.update(line for line, _ in subs)
            counted = [(line, t) for line, t in subs if line not in allowed]
            if len(counted) > ALLOW_OVERSIZE_MAX_SUBHEADINGS:
                shown = "; ".join(f'line {line}: "{t[:50]}"' for line, t in counted)
                problems.append(f"allow_oversize on '{d.locus}' (line {d.start + 1}) does not hold: it contains "
                                f"{len(counted)} sub-heading lines, over {ALLOW_OVERSIZE_MAX_SUBHEADINGS}: {shown}")
    for e in cur.not_subheadings:
        first = e["spans"][0][0]
        if not 0 < first <= n or e["quote"] not in norm[first - 1]:
            problems.append(f"not_subheadings entry at line {first} quotes text that is not on the line: "
                            f"\"{e['quote']}\"")
        stray = [x for a, b in e["spans"] for x in range(a, b + 1) if x not in flagged]
        if stray:
            problems.append(f"not_subheadings ({e['kind']}) lists {len(stray)} line(s) the oversize scan does not "
                            f"flag: {_line_list(stray)}")

    res_groups = seq_groups
    anomalies = {sid: series_anomalies(seq, res_groups.get(sid)) for sid, seq in sequences.items()}
    explained = set()
    previous = {sid: previous_lines(seq, res_groups.get(sid)) for sid, seq in sequences.items()}
    head_lines = {d.start + 1 for d in divisions if d.origin == "marker"}
    head_lines.update(line for seq in sequences.values() for line, _ in seq)
    scan = _GapScan(norm=norm, n=n, furniture=furniture, apparatus=[(a["first"], a["last"]) for a in cur.apparatus],
                    h_end=h_end, language_at=language_at, head_lines=head_lines,
                    readings={sid: {line for line, _ in seq} for sid, seq in sequences.items()})
    for e in cur.expected_gaps:
        sid, at = e["series"], e["line"]
        label = f"expected_gaps for series '{sid}' at line {at}"
        found = {x[0]: kind for kind in ("repeated", "backward", "gaps") for x in anomalies.get(sid, {}).get(kind, [])}
        line_ok = 0 < at <= n and e["quote"] in norm[at - 1]
        if sid not in sequences:
            problems.append(f"expected_gaps names series '{sid}', which no rule or entry numbers")
        elif not line_ok:
            problems.append(f"{label} quotes text that is not on the line: \"{e['quote']}\"")
        elif at not in found:
            problems.append(f"{label} matches no gap, repeat or backward step")
        else:
            explained.add((sid, at))
            before = previous[sid].get(at)
            readings = [line for line, _ in sequences[sid]]
            unread = {line for line, value in sequences[sid] if value is None}
            problems.extend(_reason_problems(cur, e, label, found[at], before, scan, readings))
            hidden = _hidden_heads(cur, e, before, scan, unread)
            if hidden:
                shown = "; ".join(f'line {i + 1} ({kind}): "{norm[i][:60]}"' for i, kind in hidden[:6])
                problems.append(f"{label} excuses a step with a look-alike heading of the series between its "
                                f"neighbours (lines {before} and {at}), which nothing accounts for: {shown}; a "
                                "printed numeral that is damaged is not a gap: read it with a fix or an ocr_map "
                                "entry")
    for sid, found in anomalies.items():
        if sid.startswith("page_splits["):
            continue
        open_lines = sorted({x[0] for kind in ("repeated", "backward", "gaps") for x in found[kind]
                             if (sid, x[0]) not in explained})
        if open_lines:
            problems.append(f"series '{sid}' has {len(open_lines)} gap, repeat or backward step the curation does "
                            f"not explain (lines {_line_list(open_lines)}); list each in expected_gaps with its "
                            "line and a quote from that line, or fix the rule")

    return Resolved(
        divisions=divisions, furniture=furniture, furniture_kinds=dict(kinds), line_offsets=offsets,
        rule_hits=dict(hits), skipped_repeats=dict(repeats), sequences=sequences, problems=problems, notes=notes,
        sequence_groups=seq_groups,
        header_end=h_end, furniture_words=sum(words[i] for i in furniture), total_words=sum(words),
        header_words=sum(words[:h_end]))


@dataclass
class _GapScan:
    """The file facts the checks on an expected_gaps entry read."""
    norm: list
    n: int
    furniture: set
    apparatus: list
    h_end: int
    language_at: object
    head_lines: set
    readings: dict


def _series_rules(cur, sid):
    return [r for r in cur.rules if r.id == sid and r.number] or [r for r in cur.rules if r.number]


def _carries_numeral(rules, text) -> bool:
    """Whether a line is a reading or a look-alike head of any of the rules: the predicate the scan applies."""
    return any(rule.rx.search(text) or _lookalike(rule, _loosened(rule), text) for rule in rules)


def _reason_problems(cur, e, label, kind, before, scan, readings) -> list[str]:
    """What is wrong with the reason an expected_gaps entry gives for its step, as problem lines."""
    reason, n, norm = e["reason"], scan.n, scan.norm
    if reason is None:
        return [f"{label} has no reason: give one of {', '.join(REASON_FORMS)}"]
    form = reason["form"]
    if kind not in REASON_STEPS[form]:
        return [f"{label} gives reason {form}, which does not explain a {'gap' if kind == 'gaps' else kind} step; "
                f"it explains {', '.join(REASON_STEPS[form])}"]
    if form in ("leaf_missing", "head_unprinted"):
        first, last = reason["between"]
        if not (1 <= first <= n and 1 <= last <= n):
            return [f"{label} reason {form} names line(s) outside the file ({n} lines)"]
        if (first, last) != (before, e["line"]):
            return [f"{label} reason {form} between [{first}, {last}] does not name the series' neighbours "
                    f"around the gap, which are [{before}, {e['line']}]"]
        if form == "leaf_missing":
            return []
    line = reason["line"]
    if not 1 <= line <= n:
        return [f"{label} reason {form} names line {line}, outside the file ({n} lines)"]
    if form == "as_printed":
        if reason["quote"] not in norm[line - 1]:
            return [f"{label} reason as_printed quotes text that is not on line {line}: \"{reason['quote']}\""]
        if line != before:
            return [f"{label} reason as_printed line {line} is not the previous reading of the series "
                    f"(line {before})"]
        return []
    if form in ("edition_unnumbered", "head_unprinted"):
        if reason["quote"] not in norm[line - 1]:
            return [f"{label} reason {form} quotes text that is not on line {line}: \"{reason['quote']}\""]
        if before is not None and not before < line < e["line"]:
            return [f"{label} reason {form} line {line} is not between the neighbours "
                    f"(lines {before} and {e['line']})"]
    else:
        after = next((x for x in readings if x > e["line"]), n)
        if line in readings or line not in scan.head_lines:
            return [f"{label} reason counterpart line {line} is not a division start or matched head outside "
                    f"this series"]
        if before is not None and not before <= line <= after:
            return [f"{label} reason counterpart line {line} is not within or next to the step "
                    f"(lines {before} to {after})"]
    if form == "counterpart" and any(line in lines for sid, lines in scan.readings.items() if sid != e["series"]):
        return []
    if _carries_numeral(_series_rules(cur, e["series"]), norm[line - 1]):
        return [f"{label} reason {form} names line {line}, which the scan reports as a head of the series with a "
                "numeral in its numeral position; such a head is neither unnumbered, unprinted nor a counterpart"]
    return []


def _hidden_heads(cur, e, before, scan, unread) -> list[tuple[int, str]]:
    """Look-alike headings of the series between the step's neighbours that nothing accounts for, as
    (0-based line, kind), plus readings of the series in that stretch whose numeral could not be read."""
    if before is None:
        return []
    rules = _series_rules(cur, e["series"])
    accounted = set().union(*(set(r.fixes) for r in rules))
    hidden: dict[int, str] = {}
    for line in sorted(x for x in unread if before <= x < e["line"]):
        hidden[line - 1] = LOOKALIKE_UNREAD
    for rule in rules:
        loose = _loosened(rule)
        for i in range(max(before, scan.h_end), e["line"] - 1):
            if (not scan.norm[i] or i in scan.furniture or i in accounted or i in hidden
                    or any(a <= i <= b for a, b in scan.apparatus)
                    or (rule.language is not None and scan.language_at(i) not in rule.language)):
                continue
            kind = _lookalike(rule, loose, scan.norm[i])
            if kind:
                hidden[i] = kind
    return sorted(hidden.items())


def measure(res: Resolved) -> dict:
    """The numbers the curated thresholds are judged on."""
    body = [d for d in res.divisions if d.origin != "header" and d.words > 0]
    body_words = res.total_words - res.header_words - res.furniture_words
    covered = sum(d.words for d in body if d.origin in ("marker", "apparatus"))
    loci = Counter(d.locus for d in body)
    oversize = [d for d in body if d.words > CURATED_MAX_DIVISION_WORDS and not d.apparatus
                and not d.allow_oversize]
    return {
        "divisions": len(body),
        "marker_divisions": sum(1 for d in body if d.origin == "marker" and not d.apparatus),
        "apparatus_divisions": sum(1 for d in body if d.apparatus),
        "repeated_loci": sorted(k for k, v in loci.items() if v > 1),
        "body_words": body_words,
        "covered_words": covered,
        "covered_word_share": round(covered / body_words, 4) if body_words else 0.0,
        "oversize_divisions": [(d.locus, d.words) for d in oversize],
        "justified_oversize": [(d.locus, d.words) for d in body if d.words > CURATED_MAX_DIVISION_WORDS
                               and not d.apparatus and d.allow_oversize],
        "problems": list(res.problems),
    }


def failures(m: dict) -> list[str]:
    out = []
    if m["divisions"] < 1:
        out.append("no divisions")
    if m["repeated_loci"]:
        out.append(f"division addresses repeat ({len(m['repeated_loci'])})")
    if m["covered_word_share"] < CURATED_MIN_COVER:
        out.append(f"divisions cover {m['covered_word_share']:.1%} of the text, under {CURATED_MIN_COVER:.0%}")
    if m["oversize_divisions"]:
        out.append(f"{len(m['oversize_divisions'])} division(s) over {CURATED_MAX_DIVISION_WORDS} words "
                   "without allow_oversize")
    out.extend(m["problems"])
    return out


def series_anomalies(seq: list, groups: list | None = None) -> dict:
    """Repeats, backward steps, gaps and unreadable numerals in one numbered series. The count
    starts again whenever the group (the parent address a numeral sits under) changes."""
    prev, prev_group = None, None
    repeated, backward, gaps, unread = [], [], [], []
    for k, (line, value) in enumerate(seq):
        group = groups[k] if groups else None
        if value is None:
            unread.append(line)
            continue
        if group != prev_group:
            prev = None
        if prev is not None:
            if value == prev:
                repeated.append((line, value))
            elif value < prev:
                backward.append((line, prev, value))
            elif value > prev + 1:
                gaps.append((line, prev, value))
        prev, prev_group = value, group
    return {"repeated": repeated, "backward": backward, "gaps": gaps, "unread": unread}


def sequence_notes(res: Resolved) -> dict[str, dict]:
    """Information on the numbers a rule read: where they repeat, run backwards, skip or cannot be read."""
    out = {}
    for rid, seq in res.sequences.items():
        found = series_anomalies(seq, res.sequence_groups.get(rid))
        values = [v for _, v in seq if v is not None]
        out[rid] = {"readings": len(seq), "first": values[0] if values else None,
                    "last": values[-1] if values else None, **found}
    return out


def override_for(entries: list[dict], line: int) -> dict | None:
    for e in entries:
        if e["first"] <= line <= e["last"]:
            return e
    return None


def _subsequence(own: list[str], seg: list[str]) -> bool:
    it = iter(seg)
    return all(tok in it for tok in own)


def verify(records: list[dict], src, work: str, furniture_words: int) -> dict:
    """Completeness and verbatim checks on the passages of one file: every byte range
    re-read from the file gives the passage text (less only declared furniture), and
    passage words plus furniture words are the file's words."""
    exact = suppressed = bad = 0
    for r in records:
        bs, be = r["byte_start"], r["byte_end"]
        try:
            cs, ce = src.char_of(bs), src.char_of(be)
        except ValueError:
            bad += 1
            continue
        seg = src.data[bs:be].decode("utf-8", errors="surrogateescape").split()
        own = r["text"].split()
        if seg == own:
            exact += 1
        elif (len(seg) - len(own) == len(src.text[cs:ce].split()) - len(work[cs:ce].split())
              and _subsequence(own, seg)):
            suppressed += 1
        else:
            bad += 1
    words = sum(r["word_count"] for r in records)
    return {
        "passages": len(records),
        "verbatim_exact": exact,
        "verbatim_with_declared_furniture": suppressed,
        "verbatim_mismatch": bad,
        "passage_words": words,
        "passage_words_resplit": sum(len(r["text"].split()) for r in records),
        "furniture_words": furniture_words,
        "file_words": len(src.text.split()),
    }


def verify_failures(v: dict) -> list[str]:
    out = []
    if v["verbatim_mismatch"]:
        out.append(f"{v['verbatim_mismatch']} byte range(s) do not reproduce the passage text")
    if v["passage_words"] != v["passage_words_resplit"]:
        out.append("word_count fields disagree with the passage texts")
    if v["passage_words"] + v["furniture_words"] != v["file_words"]:
        out.append(f"passage words {v['passage_words']} + furniture {v['furniture_words']} "
                   f"!= file words {v['file_words']}")
    return out
