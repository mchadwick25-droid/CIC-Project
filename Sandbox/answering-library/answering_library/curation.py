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
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from . import markers as mk
from . import plain

CURATION_DIR = Path(__file__).resolve().parents[1] / "curation"
STATUSES = ("drafted", "sampled-ok", "needs-redo")
CURATED_MIN_COVER = 0.95
CURATED_MAX_DIVISION_WORDS = plain.OVERSIZE_WORDS
SPEAKER_STATES = ("known", "mixed", "unknown")

_TOP_KEYS = {"file", "scheme", "curator", "status", "language", "rules", "divisions", "ignore", "apparatus",
             "languages", "speakers", "evidence"}
_RULE_KEYS = {"id", "pattern", "flags", "lines", "parent", "locus", "title", "division", "skip_repeat", "number",
              "ocr_map", "fixes", "allow_oversize"}
_DIVISION_KEYS = {"start_line", "locus", "title", "allow_oversize"}
_IGNORE_KEYS = {"pattern", "kind", "lines"}
_APPARATUS_KEYS = {"lines", "kind", "locus"}
_LANGUAGE_KEYS = {"lines", "language", "evidence"}
_SPEAKER_KEYS = {"lines", "state", "voice", "evidence"}
_EVIDENCE_KEYS = {"line", "quote"}
_FIX_KEYS = {"line", "set"}
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


def _template_fields(template, allowed, where):
    for m in _FIELD.finditer(template):
        if m.group(1) not in allowed:
            raise CurationError(f"{where}: template field '{m.group(1)}' is not a group of the pattern "
                                f"(available: {sorted(allowed)})")
    if _FIELD.sub("", template).count("{") or _FIELD.sub("", template).count("}"):
        raise CurationError(f"{where}: unbalanced braces in template '{template}'")


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
            fixes[f["line"] - 1] = {g: str(v) for g, v in f["set"].items()}
        rules.append(Rule(
            id=r["id"], rx=rx, lines=_ranges(r.get("lines"), where, allow_none=True), parent=r.get("parent"),
            locus=r["locus"], title=r.get("title", ""), division=r.get("division", True),
            skip_repeat=bool(r.get("skip_repeat", False)), number=r.get("number"),
            ocr_map={str(a): str(b) for a, b in (r.get("ocr_map") or {}).items()}, fixes=fixes,
            allow_oversize=(r.get("allow_oversize") or "").strip()))
    ids = {r.id for r in rules}
    for r in rules:
        if r.parent and r.parent not in ids:
            raise CurationError(f"{name}: rule '{r.id}' names parent '{r.parent}', which is not a rule id")
    for r in rules:
        chain, cur = set(), r
        while cur.parent:
            if cur.parent in chain:
                raise CurationError(f"{name}: rule parents form a loop at '{r.id}'")
            chain.add(cur.parent)
            cur = next(x for x in rules if x.id == cur.parent)

    divisions = []
    for k, d in enumerate(data.get("divisions") or []):
        where = f"{name} divisions[{k}]"
        _check_keys(d, _DIVISION_KEYS, where)
        if not isinstance(d.get("start_line"), int) or d["start_line"] < 1 or not d.get("locus"):
            raise CurationError(f"{where}: needs start_line and locus")
        if not _LOCUS.fullmatch(str(d["locus"])):
            raise CurationError(f"{where}: locus may not contain spaces or '#'")
        divisions.append({"start": d["start_line"] - 1, "locus": str(d["locus"]),
                          "title": " ".join(str(d.get("title") or "").split()),
                          "allow_oversize": (d.get("allow_oversize") or "").strip()})

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
                    sha256=hashlib.sha256(raw).hexdigest())


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


def render(template: str, values: dict, ocr_map: dict, where: str) -> str:
    def sub(m):
        value = values.get(m.group(1))
        value = "" if value is None else str(value)
        for flt in [f for f in m.group(2).split("|") if f]:
            name, _, arg = flt.partition(":")
            if name == "int":
                number = to_int(value, ocr_map)
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


def resolve(cur: Curation, lines: list[str]) -> Resolved:
    """Divisions, furniture and diagnostics of one file under one curation.
    Divisions tile the body (every line after the library header) with no gap."""
    n = len(lines)
    h_end = mk.header_end(lines)
    norm = [" ".join(ln.split()) for ln in lines]
    offsets, pos = [], 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1
    offsets.append(pos - 1)
    words = [len(ln.split()) for ln in lines]

    furniture: set[int] = set()
    kinds: Counter = Counter()
    for i in range(h_end, n):
        if not norm[i]:
            continue
        for ig in cur.ignore:
            if _in(ig["lines"], i) and ig["rx"].search(norm[i]):
                furniture.add(i)
                kinds[ig["kind"]] += 1
                break

    children: dict[str, list[str]] = {r.id: [] for r in cur.rules}
    for r in cur.rules:
        if r.parent:
            children[r.parent].append(r.id)

    def descendants(rid):
        for c in children[rid]:
            yield c
            yield from descendants(c)

    starts: dict[int, dict] = {}
    context: dict[str, str] = {}
    last: dict[str, str] = {}
    hits: Counter = Counter()
    repeats: Counter = Counter()
    sequences: dict[str, list] = {r.id: [] for r in cur.rules if r.number}
    used_fixes: set[tuple[str, int]] = set()
    pending: int | None = None
    for i in range(h_end, n):
        if i in furniture or not norm[i]:
            continue
        for rule in cur.rules:
            if not _in(rule.lines, i):
                continue
            m = rule.rx.search(norm[i])
            if not m:
                continue
            where = f"line {i + 1} rule '{rule.id}'"
            values = {k: v for k, v in m.groupdict().items()}
            if i in rule.fixes:
                values.update(rule.fixes[i])
                used_fixes.add((rule.id, i))
            if rule.parent and rule.parent not in context:
                raise CurationError(f"{where}: matched before its parent rule '{rule.parent}' ever matched")
            values["line"] = i + 1
            values["parent"] = context.get(rule.parent, "")
            nxt = next((norm[j] for j in range(i + 1, min(n, i + 40)) if norm[j] and j not in furniture), "")
            values["next"] = nxt
            part = render(rule.locus, values, rule.ocr_map, where)
            full = f"{context[rule.parent]}/{part}" if rule.parent else part
            _valid_locus(full, where)
            if rule.skip_repeat and last.get(rule.id) == full:
                repeats[rule.id] += 1
                break
            hits[rule.id] += 1
            context[rule.id] = full
            last[rule.id] = full
            for d in descendants(rule.id):
                context.pop(d, None)
                last.pop(d, None)
            if rule.number:
                sequences[rule.id].append((i + 1, to_int(values.get(rule.number) or "", rule.ocr_map)))
            if rule.division:
                title = " ".join(render(rule.title, values, rule.ocr_map, where).split())
                starts[pending if pending is not None else i] = {
                    "locus": full, "title": title, "origin": "marker", "allow_oversize": rule.allow_oversize}
                pending = None
            elif pending is None:
                pending = i
            break
    if pending is not None:
        starts.setdefault(pending, {"locus": f"text/line{pending + 1}", "title": "", "origin": "gap",
                                    "allow_oversize": ""})

    explicit: set[int] = set()
    for d in cur.divisions:
        if not (h_end <= d["start"] < n):
            raise CurationError(f"{cur.path.name}: division at line {d['start'] + 1} is outside the body "
                                f"(lines {h_end + 1}-{n})")
        if d["start"] in explicit:
            raise CurationError(f"{cur.path.name}: two explicit divisions start at line {d['start'] + 1}")
        explicit.add(d["start"])
        starts[d["start"]] = {"locus": d["locus"], "title": d["title"], "origin": "marker",
                              "allow_oversize": d["allow_oversize"]}

    ranges = []
    for a in cur.apparatus:
        first, last_line = max(a["first"], h_end), min(a["last"], n - 1)
        if first > last_line:
            continue
        ranges.append((first, last_line))
        starts.setdefault(first, {"locus": a["locus"] or f"{a['kind']}/line{first + 1}", "title": "",
                                  "origin": "apparatus", "allow_oversize": ""})
        if last_line + 1 < n:
            starts.setdefault(last_line + 1, {"locus": f"text/line{last_line + 2}", "title": "", "origin": "gap",
                                              "allow_oversize": ""})
    if h_end < n and h_end not in starts:
        first_start = min(starts) if starts else n
        if any(words[i] for i in range(h_end, first_start) if i not in furniture):
            starts[h_end] = {"locus": f"text/line{h_end + 1}", "title": "", "origin": "gap", "allow_oversize": ""}

    divisions: list[CDiv] = []
    if h_end:
        divisions.append(CDiv(0, h_end, "header", "", True, "header"))
    order = sorted(starts)
    for k, s in enumerate(order):
        e = order[k + 1] if k + 1 < len(order) else n
        info = starts[s]
        in_apparatus = any(a <= s <= b for a, b in ranges)
        div = CDiv(s, e, info["locus"], info["title"], in_apparatus, info["origin"], info["allow_oversize"])
        div.words = sum(words[i] for i in range(s, e) if i not in furniture)
        divisions.append(div)
    if divisions and divisions[0].origin == "header":
        divisions[0].words = sum(words[:h_end])

    problems = []
    for r in cur.rules:
        if not hits[r.id]:
            problems.append(f"rule '{r.id}' matched no line")
        for line in sorted(r.fixes):
            if (r.id, line) not in used_fixes:
                problems.append(f"fix at line {line + 1} of rule '{r.id}' does not land on a match")
    for e in cur.evidence:
        i = e["line"] - 1
        if not 0 <= i < n or e["quote"] not in norm[i]:
            problems.append(f"evidence at line {e['line']} does not quote the file: \"{e['quote']}\"")

    return Resolved(
        divisions=divisions, furniture=furniture, furniture_kinds=dict(kinds), line_offsets=offsets,
        rule_hits=dict(hits), skipped_repeats=dict(repeats), sequences=sequences, problems=problems,
        header_end=h_end, furniture_words=sum(words[i] for i in furniture), total_words=sum(words),
        header_words=sum(words[:h_end]))


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


def sequence_notes(res: Resolved) -> dict[str, dict]:
    """Information on the numbers a rule read: where they repeat, run backwards, skip or cannot be read."""
    out = {}
    for rid, seq in res.sequences.items():
        prev, repeated, backward, gaps, unread = None, [], [], [], []
        for line, value in seq:
            if value is None:
                unread.append(line)
                continue
            if prev is not None:
                if value == prev:
                    repeated.append((line, value))
                elif value < prev:
                    backward.append((line, prev, value))
                elif value > prev + 1:
                    gaps.append((line, prev, value))
            prev = value
        values = [v for _, v in seq if v is not None]
        out[rid] = {"readings": len(seq), "first": values[0] if values else None, "last": values[-1] if values else None,
                    "repeated": repeated, "backward": backward, "gaps": gaps, "unread": unread}
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
