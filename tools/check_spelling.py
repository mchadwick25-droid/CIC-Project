#!/usr/bin/env python3
"""American spelling for everything the project writes in modern English.

The rule (Answering-From-Sources Decision-Log 77): modern renderings, notes,
voice records, Facilitator text, the site's own prose and the construction
documents' own prose use American spelling. Verbatim quotations from editions,
quoted titles and proper names keep their own spelling.

This check finds British forms from an explicit list (below). It never guesses
from a pattern alone: every ending is paired with the stems it applies to, so
"advise", "exercise" and "promise" are never flagged. Text it does not check:

- quoted spans: "...", “...”, «...», ‘...’ and `...`;
- fenced code, indented code, and Markdown blockquote lines;
- URLs and path-like tokens (anything with a slash or an underscore);
- in a record's frontmatter, the fields that hold an edition's own words or a
  name: `text` on a quote record, `edition`, `work`, `title`, `translator`,
  `author`, `names`, `locus` and the identifiers.

Usage:
  check_spelling.py                       report every finding in the checked trees
  check_spelling.py --base REF            only files changed since the merge-base with REF
  check_spelling.py --base REF --enforce  exit 1 on a finding in an enforced tree
  check_spelling.py FILE...               check the named files

A tree is enforced once its fleet pass has landed (ENFORCED below); until then
its findings are reported and never fail a pull request.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]

# Trees whose files are checked at all, and the subset whose findings fail a
# pull request. A tree moves into ENFORCED when its fleet pass lands.
CHECKED = ("records/", "engine/shape/records/", "cic-website/")
ENFORCED: tuple[str, ...] = ()

# ---------------------------------------------------------------- word list
#
# Every flagged form is spelled out here (generated from a stem and an ending,
# never matched by a bare suffix), so a word that is spelled the same in both
# varieties - advise, exercise, promise, rigorous, glamour - can never be hit.

TABLE: dict[str, str] = {}


def _family(stems, british_end: str, american_end: str, endings) -> None:
    for stem in stems:
        for end in endings:
            TABLE[f"{stem}{british_end}{end}"] = f"{stem}{american_end}{end}"


# -our -> -or
_family(
    ("colo", "hono", "favo", "behavio", "neighbo", "labo", "harbo", "rumo", "humo", "vigo", "rigo", "valo", "savo",
     "flavo", "endeavo", "fervo", "armo", "cando", "clamo", "splendo", "odo", "parlo", "vapo", "tumo", "demeano"),
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
     "galvan", "mesmer", "agon", "item", "equal"),
    "is", "iz", ("e", "es", "ed", "ing", "ation", "ations", "er", "ers"),
)

# -yse -> -yze
for _stem in ("anal", "paral", "catal"):
    for _b, _a in (("yse", "yze"), ("ysed", "yzed"), ("ysing", "yzing"), ("yser", "yzer"), ("ysers", "yzers")):
        TABLE[_stem + _b] = _stem + _a

# -re -> -er
_family(("cent", "epicent"), "re", "er", ("", "s", "d"))
TABLE["centring"] = "centering"
_family(("theat", "met", "lit", "fib", "calib", "somb", "lust", "meag", "spect", "sab", "kilomet", "millimet", "centimet"),
        "re", "er", ("", "s"))
TABLE["manoeuvre"], TABLE["manoeuvres"], TABLE["manoeuvred"] = "maneuver", "maneuvers", "maneuvered"

# doubled l before a suffix: travelled -> traveled
for _stem in ("travel", "label", "cancel", "counsel", "model", "level", "fuel", "signal", "marshal", "quarrel", "channel",
              "tunnel", "funnel", "equal", "total", "dial", "pencil", "shovel", "gravel", "revel", "rival", "duel", "libel",
              "panel", "carol", "initial", "refuel", "unravel"):
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
    "kerb": "curb", "tyre": "tire", "tyres": "tires", "gaol": "jail", "mould": "mold", "moulds": "molds",
    "moulded": "molded", "smoulder": "smolder", "smouldering": "smoldering", "sulphur": "sulfur",
    "pyjamas": "pajamas", "draught": "draft", "draughts": "drafts", "cosy": "cozy", "moustache": "mustache",
    "enquire": "inquire", "enquired": "inquired", "enquiry": "inquiry", "enquiries": "inquiries",
    "connexion": "connection", "learnt": "learned", "dreamt": "dreamed", "fulfil": "fulfill",
    "fulfilment": "fulfillment", "enrol": "enroll", "enrolment": "enrollment", "instil": "instill",
    "skilful": "skillful", "skilfully": "skillfully", "wilful": "willful", "wilfully": "willfully",
    "jewellery": "jewelry", "instalment": "installment", "practise": "practice", "practised": "practiced",
    "practising": "practicing", "distil": "distill", "appal": "appall",
})

_WORD_RE = re.compile(
    r"(?<![\w/_.-])(?:" + "|".join(sorted(map(re.escape, TABLE), key=len, reverse=True)) + r")(?![\w/_-])",
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


# ------------------------------------------------------------ text scanning

_QUOTED = re.compile(
    r"\"[^\"\n]*\"|\u201c[^\u201d\n]*\u201d|\u00ab[^\u00bb\n]*\u00bb|\u2018[^\u2019\n]*\u2019|`[^`\n]*`"
    # 'single-quoted phrase': an opening quote after a non-word character, a closing one before a non-word
    # character, so apostrophes inside words (Cyprian's, don't) are never taken for quote marks.
    r"|(?<!\w)'(?=\S)[^'\n]*?(?<=\S)'(?!\w)"
)
_URL = re.compile(r"https?://\S+")
_PATHLIKE = re.compile(r"\S*[/_]\S*")
# Spellings that are also surnames or other names when capitalized: matched in lower case only.
_LOWER_ONLY = {"grey", "greying", "mould", "moulds", "moulded"}


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    word: str
    suggestion: str


def _blank(match: re.Match[str]) -> str:
    return " " * (match.end() - match.start())


def _find(text: str, markdown: bool = True) -> list[tuple[int, str]]:
    """(offset, word) of each British form in a block of prose. Quoted spans, code,
    blockquotes, URLs and path-like tokens are skipped."""
    out: list[tuple[int, str]] = []
    in_fence = False
    pos = 0
    for raw in text.split("\n"):
        start = pos
        pos += len(raw) + 1
        stripped = raw.lstrip()
        if markdown:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                continue
            if in_fence or stripped.startswith(">") or raw.startswith("    "):
                continue
        line = _URL.sub(_blank, raw)
        line = _PATHLIKE.sub(_blank, line)
        line = _QUOTED.sub(_blank, line)
        for m in _WORD_RE.finditer(line):
            word = m.group(0)
            if word.lower() in _LOWER_ONLY and not word.islower():
                continue
            out.append((start + m.start(), word))
    return out


def _line_of(text: str, offset: int, first_line: int = 1) -> int:
    return first_line + text.count("\n", 0, offset)


def scan_text(text: str, path: str = "", first_line: int = 1) -> list[Finding]:
    return [Finding(path, _line_of(text, off, first_line), w, american(w)) for off, w in _find(text)]


def fix_text(text: str) -> str:
    for off, word in reversed(_find(text)):
        text = text[:off] + american(word) + text[off + len(word):]
    return text


# Frontmatter fields that hold an edition's own words, a title or a name.
_SKIP_KEYS = {
    "id", "world_id", "record_type", "schema_version", "status", "register", "canon_cells", "locus", "edition",
    "work", "title", "translator", "translators", "author", "names", "source_id", "source", "sources_cited",
    "license", "tier", "kind", "voice_of", "census_id", "shelf_row", "speaker", "name",
}


def _scalars(node, key: str | None, record_type: str | None):
    """Each prose scalar node of a frontmatter tree."""
    if isinstance(node, yaml.ScalarNode):
        if key in _SKIP_KEYS or (key == "text" and record_type == "quote"):
            return
        yield node
    elif isinstance(node, yaml.MappingNode):
        for k, v in node.value:
            yield from _scalars(v, k.value if isinstance(k, yaml.ScalarNode) else None, record_type)
    elif isinstance(node, yaml.SequenceNode):
        for v in node.value:
            yield from _scalars(v, key, record_type)


def _record_edits(text: str) -> tuple[list[tuple[int, int, str]], int]:
    """(start, end, replacement) for every flagged word in a record file, and the offset
    where its body begins. Frontmatter words are located through the YAML node that holds them."""
    if not text.startswith("---"):
        return [(o, o + len(w), american(w)) for o, w in _find(text)], 0
    end = text.find("\n---", 3)
    if end == -1:
        return [(o, o + len(w), american(w)) for o, w in _find(text)], 0
    front = text[3:end]
    body_start = end + 4
    edits: list[tuple[int, int, str]] = []
    try:
        root = yaml.compose(front, Loader=yaml.SafeLoader)
    except yaml.YAMLError:
        root = None
    if isinstance(root, yaml.MappingNode):
        rt = next((v.value for k, v in root.value if getattr(k, "value", None) == "record_type" and isinstance(v, yaml.ScalarNode)), None)
        for node in _scalars(root, None, rt):
            raw_start, raw_end = node.start_mark.index, node.end_mark.index
            raw = front[raw_start:raw_end]
            seen: dict[str, int] = {}
            for off, word in _find(node.value):
                k = node.value.count(word, 0, off)
                # the k-th occurrence of this exact word in the raw scalar
                at = -1
                for _ in range(k + 1):
                    at = raw.find(word, at + 1)
                if at == -1:
                    continue
                abs_start = 3 + raw_start + at
                edits.append((abs_start, abs_start + len(word), american(word)))
    else:
        edits.extend((3 + o, 3 + o + len(w), american(w)) for o, w in _find(front))
    edits.extend((body_start + o, body_start + o + len(w), american(w)) for o, w in _find(text[body_start:]))
    return edits, body_start


def scan_record(text: str, path: str) -> list[Finding]:
    edits, _ = _record_edits(text)
    return [Finding(path, _line_of(text, a, 1), text[a:b], new) for a, b, new in sorted(edits)]


def fix_record(text: str) -> str:
    for a, b, new in sorted(_record_edits(text)[0], reverse=True):
        text = text[:a] + new + text[b:]
    return text


_TAG = re.compile(r"<(script|style)\b.*?</\1>|<!--.*?-->|<[^>]+>", re.DOTALL | re.IGNORECASE)


def _html_blanked(text: str) -> str:
    return _TAG.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


def scan_html(text: str, path: str) -> list[Finding]:
    """A page: the text between tags. Script and style blocks and attribute values are not prose."""
    blanked = _html_blanked(text)
    return [Finding(path, _line_of(blanked, off), w, american(w)) for off, w in _find(blanked, markdown=False)]


def fix_html(text: str) -> str:
    for off, word in reversed(_find(_html_blanked(text), markdown=False)):
        text = text[:off] + american(word) + text[off + len(word):]
    return text


def _kind(path: Path) -> str | None:
    rel = str(path.relative_to(REPO)) if REPO in path.parents else str(path)
    suffix = path.suffix.lower()
    if rel.startswith("records/") and suffix == ".md":
        return "record"
    if suffix in (".html", ".htm"):
        return "html"
    if suffix == ".md":
        return "text"
    return None


def scan_file(path: Path) -> list[Finding]:
    kind = _kind(path)
    rel = str(path.relative_to(REPO)) if REPO in path.parents else str(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    if kind == "record":
        return scan_record(text, rel)
    if kind == "html":
        return scan_html(text, rel)
    if kind == "text":
        return scan_text(text, rel)
    return []


def fix_file(path: Path) -> int:
    """Rewrite one file in place; returns how many words changed."""
    kind = _kind(path)
    text = path.read_text(encoding="utf-8")
    new = {"record": fix_record, "html": fix_html, "text": fix_text}.get(kind or "", lambda t: t)(text)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return len(scan_file_text(kind, text))


def scan_file_text(kind: str | None, text: str) -> list[Finding]:
    if kind == "record":
        return scan_record(text, "")
    if kind == "html":
        return scan_html(text, "")
    if kind == "text":
        return scan_text(text, "")
    return []


# ------------------------------------------------------------------ driver


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, check=True, capture_output=True, text=True).stdout


def changed_files(base: str) -> list[Path]:
    merge_base = _git("merge-base", base, "HEAD").strip()
    names = _git("diff", "--name-only", "--diff-filter=AM", merge_base, "HEAD").split("\n")
    return [REPO / n for n in names if n and (REPO / n).is_file()]


def all_files() -> list[Path]:
    names = _git("ls-files", "-z", "--", *CHECKED).split("\0")
    return [REPO / n for n in names if n]


def in_checked(rel: str) -> bool:
    return rel.startswith(CHECKED)


def is_enforced(rel: str) -> bool:
    return bool(ENFORCED) and rel.startswith(ENFORCED)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*")
    parser.add_argument("--base")
    parser.add_argument("--enforce", action="store_true")
    parser.add_argument("--fix", action="store_true", help="rewrite the flagged words in place")
    args = parser.parse_args(argv)
    if args.enforce and not args.base:
        parser.error("--enforce needs --base")

    if args.files:
        paths = [Path(f).resolve() for f in args.files]
    elif args.base:
        paths = changed_files(args.base)
    else:
        paths = all_files()
    paths = [p for p in paths if args.files or in_checked(str(p.relative_to(REPO)))]

    if args.fix:
        changed = [(p, fix_file(p)) for p in paths]
        for p, n in changed:
            if n:
                print(f"{p.relative_to(REPO)}: {n}")
        print(f"\n{sum(n for _, n in changed)} word(s) changed in {sum(1 for _, n in changed if n)} file(s)", file=sys.stderr)
        return 0

    findings: list[Finding] = []
    for path in paths:
        findings.extend(scan_file(path))
    blocking = [f for f in findings if is_enforced(f.path)] if args.enforce else []
    for f in findings:
        print(f"{f.path}:{f.line}: {f.word} -> {f.suggestion}")
    print(f"\n{len(findings)} British spelling(s) found in {len({f.path for f in findings})} file(s); "
          f"{len(blocking)} in enforced trees", file=sys.stderr)
    if blocking:
        print("Use the American spelling (Decision-Log 77); quotations from editions keep their own.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
