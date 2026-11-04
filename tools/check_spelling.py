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
  `author`, `names`, `citation`, `locus` and the identifiers.

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
import json
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
ENFORCED: tuple[str, ...] = ("records/", "engine/shape/records/", "cic-website/")

# ---------------------------------------------------------------- word list
# The table lives in engine/m1/spelling_table.py, shared with the readability regate.
sys.path.insert(0, str(REPO))
from engine.m1.spelling_table import COMPARE_RE as _HYPHEN_RE
from engine.m1.spelling_table import LOWER_ONLY as _LOWER_ONLY  # noqa: E402
from engine.m1.spelling_table import TABLE, WORD_RE as _WORD_RE, american  # noqa: E402

# ------------------------------------------------------------ text scanning

_PARA = r"(?:[^{q}\n]|\n(?!\s*\n))*"  # runs across a wrapped line, never across a blank line
_QUOTED = re.compile(
    "|".join([
        '"' + _PARA.format(q='"') + '"',
        "\u201c" + _PARA.format(q="\u201d") + "\u201d",
        "\u00ab" + _PARA.format(q="\u00bb") + "\u00bb",
        "\u2018" + _PARA.format(q="\u2019") + "\u2019",
        "`" + _PARA.format(q="`") + "`",
        # 'single-quoted phrase': an opening quote after a non-word character, a closing one before a
        # non-word character, so apostrophes inside words (Cyprian's, don't) are never taken for quote marks.
        r"(?<!\w)'(?=\S)(?:[^'\n]|\n(?!\s*\n))*?(?<=\S)'(?!\w)",
    ])
)
# Names and titles that carry a British spelling as part of the name: an institution, a periodical, a
# work cited in running prose. They are written down here, never inferred.
_NAMES = re.compile(
    r"Pontifical Institute of Mediaeval Studies|Mediaeval Academy|Encyclopaedia (?:Iranica|Britannica|of Islam)"
    r"|On the Catechising of the Uninstructed"
    r"|(?:In )?Defence (?:of|Against|before) (?:the |his |His |Himself|Dionysius|Origen|Ries|English)[\w' ]*[A-Z]\w*"
    r"|Programme to Combat Racism"
    r"|African Civilisation|Carey\S{1,7}s Enquiry|An Enquiry into the Obligations|Le Theatre sacre des Cevennes"
    r"|Plough, Rifton"
    r"|Labour Party|(?:voted|stood as|and) Labour\b|Labour (?:carried|prime minister|leader|government)|Agricultural Labourers|Dorchester Labourers"
    r"|Church of the Saviour|All Saviour\S{1,7}s monastery",
)
# A capitalized word of this kind next to another capitalized word is part of a name (Labour Party,
# International Christian Centre, Mediaeval Studies), not prose.
_NAME_PRONE = {"centre", "labour", "mediaeval", "encyclopaedia", "programme"}
_URL = re.compile(r"https?://\S+")
_PATHLIKE = re.compile(r"\S*[/_]\S*")


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    word: str
    suggestion: str


def _blank(match: re.Match[str]) -> str:
    """Spaces of the same length, keeping line breaks so offsets stay put."""
    return re.sub(r"[^\n]", " ", match.group(0))


def _find(text: str, markdown: bool = True, hyphen: bool = False) -> list[tuple[int, str]]:
    """(offset, word) of each British form in a block of prose. Quoted spans, code,
    blockquotes, URLs and path-like tokens are skipped."""
    masked: list[str] = []
    in_fence = False
    for raw in text.split("\n"):
        stripped = raw.lstrip()
        if markdown:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                masked.append(" " * len(raw))
                continue
            if in_fence or stripped.startswith(">") or raw.startswith("    "):
                masked.append(" " * len(raw))
                continue
        line = _URL.sub(_blank, raw)
        masked.append(_PATHLIKE.sub(_blank, line))
    body = "\n".join(masked)
    body = _QUOTED.sub(_blank, body)
    body = _NAMES.sub(_blank, body)
    out: list[tuple[int, str]] = []
    for m in (_HYPHEN_RE if hyphen else _WORD_RE).finditer(body):
        word = m.group(0)
        if word.lower() in _LOWER_ONLY and not word.islower():
            continue
        near = text[max(0, m.start() - 120):m.end() + 120]
        if american(word).lower() in {w.lower() for w in re.findall(r"[^\W\d_]+", near)}:
            continue
        if word.lower() in _NAME_PRONE and word[:1].isupper() and _in_name(body, m):
            continue
        out.append((m.start(), word))
    return out


def _in_name(body: str, m: re.Match[str]) -> bool:
    after = re.match(r"[ \t]+[A-Z][a-z]", body[m.end():])
    before = re.search(r"[A-Z][\w'’-]*[ \t]+$", body[:m.start()])
    return bool(after or before)


def _line_of(text: str, offset: int, first_line: int = 1) -> int:
    return first_line + text.count("\n", 0, offset)


def scan_text(text: str, path: str = "", first_line: int = 1, hyphen: bool = False) -> list[Finding]:
    return [Finding(path, _line_of(text, off, first_line), w, american(w)) for off, w in _find(text, hyphen=hyphen)]


def fix_text(text: str, hyphen: bool = False) -> str:
    for off, word in reversed(_find(text, hyphen=hyphen)):
        text = text[:off] + american(word) + text[off + len(word):]
    return text


# Frontmatter fields that hold an edition's own words, a title or a name.
_SKIP_KEYS = {
    "id", "world_id", "record_type", "schema_version", "status", "register", "canon_cells", "locus", "edition",
    "work", "title", "translator", "translators", "author", "names", "source_id", "source", "sources_cited",
    "license", "tier", "kind", "voice_of", "census_id", "shelf_row", "speaker", "speaker_or_author", "name", "citation", "display_name", "census_id", "location", "manifest_hash",
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
        edits.extend(_yaml_scalar_edits(front, root, 3))
    else:
        edits.extend((3 + o, 3 + o + len(w), american(w)) for o, w in _find(front))
    edits.extend((body_start + o, body_start + o + len(w), american(w)) for o, w in _find(text[body_start:]))
    return edits, body_start


def _yaml_scalar_edits(front: str, root, offset: int) -> list[tuple[int, int, str]]:
    """(start, end, replacement) for each flagged word in the prose scalars of a composed YAML mapping,
    located through the node that holds it; `offset` is where `front` begins in the whole file."""
    edits: list[tuple[int, int, str]] = []
    rt = next((v.value for k, v in root.value if getattr(k, "value", None) == "record_type" and isinstance(v, yaml.ScalarNode)), None)
    for node in _scalars(root, None, rt):
        raw_start, raw_end = node.start_mark.index, node.end_mark.index
        raw = front[raw_start:raw_end]
        for off, word in _find(node.value):
            k = node.value.count(word, 0, off)
            # the k-th occurrence of this exact word in the raw scalar
            at = -1
            for _ in range(k + 1):
                at = raw.find(word, at + 1)
            if at == -1:
                continue
            abs_start = offset + raw_start + at
            edits.append((abs_start, abs_start + len(word), american(word)))
    return edits


def scan_yaml(text: str, path: str = "") -> list[Finding]:
    try:
        root = yaml.compose(text, Loader=yaml.SafeLoader)
    except yaml.YAMLError:
        return []
    if not isinstance(root, yaml.MappingNode):
        return []
    return [Finding(path, _line_of(text, a), text[a:b], new) for a, b, new in sorted(_yaml_scalar_edits(text, root, 0))]


def fix_yaml(text: str) -> str:
    try:
        root = yaml.compose(text, Loader=yaml.SafeLoader)
    except yaml.YAMLError:
        return text
    if not isinstance(root, yaml.MappingNode):
        return text
    for a, b, new in sorted(_yaml_scalar_edits(text, root, 0), reverse=True):
        text = text[:a] + new + text[b:]
    return text


def scan_record(text: str, path: str) -> list[Finding]:
    edits, _ = _record_edits(text)
    return [Finding(path, _line_of(text, a, 1), text[a:b], new) for a, b, new in sorted(edits)]


def fix_record(text: str) -> str:
    for a, b, new in sorted(_record_edits(text)[0], reverse=True):
        text = text[:a] + new + text[b:]
    return text


_TAG = re.compile(r"<(script|style)\b.*?</\1>|<!--.*?-->|<[^>]+>", re.DOTALL | re.IGNORECASE)


_ENTITY_QUOTES = re.compile(r"&quot;|&#34;|&#x22;|&ldquo;|&rdquo;", re.IGNORECASE)
_ATTRS = re.compile(r'\b(alt|title|aria-label|content)="([^"]*)"')


def _html_blanked(text: str) -> str:
    """The page with tags blanked and entity quotation marks turned into real ones of the same length."""
    blanked = _TAG.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    return _ENTITY_QUOTES.sub(lambda m: ("\u201c" if m.group(0).lower() == "&ldquo;" else "\u201d" if m.group(0).lower() == "&rdquo;" else '"') + " " * (len(m.group(0)) - 1), blanked)


def _html_edits(text: str) -> list[tuple[int, str]]:
    """(offset, word) for the prose between tags and for the attribute text a reader meets
    (alt, title, aria-label, and a meta tag's content). Script and style blocks are not prose."""
    out = list(_find(_html_blanked(text), markdown=False, hyphen=True))
    for tag in _TAG.finditer(text):
        t = tag.group(0)
        if not t.startswith("<") or t[1:2] in "!/" or re.match(r"<(script|style)\b", t, re.IGNORECASE):
            continue
        for attr in _ATTRS.finditer(t):
            if attr.group(1) == "content" and not t.lower().startswith("<meta"):
                continue
            start = tag.start() + attr.start(2)
            out.extend((start + off, w) for off, w in _find(attr.group(2), markdown=False, hyphen=True))
    return sorted(out)


def scan_html(text: str, path: str) -> list[Finding]:
    return [Finding(path, _line_of(text, off), w, american(w)) for off, w in _html_edits(text)]


def fix_html(text: str) -> str:
    for off, word in reversed(_html_edits(text)):
        text = text[:off] + american(word) + text[off + len(word):]
    return text


_JSON_SKIP_KEYS = _SKIP_KEYS | {"shortName", "informalName", "atlasId", "url", "href", "slug", "glyph", "chip"}
_JSON_TOKEN = re.compile(r'"(?:[^"\\]|\\.)*"|[{}\[\],:]')


def _json_encode_like(original: str, value: str) -> str:
    """Encode value the way original (a JSON string token) was written; refuse when that cannot be told."""
    old = json.loads(original)
    for ascii_only in (False, True):
        if json.dumps(old, ensure_ascii=ascii_only) == original:
            return json.dumps(value, ensure_ascii=ascii_only)
    raise ValueError(f"JSON string escaping is not reproducible: {original[:60]}")


def _json_edits(text: str, start: int = 0):
    """(start, end, old value, new value) for every prose string of the JSON value that begins at `start`,
    found token by token so that nothing else in the text is touched. Returns the edits and the offset
    where the value ends."""
    stack: list[list] = []
    edits = []
    for m in _JSON_TOKEN.finditer(text, start):
        tok = m.group(0)
        if tok in "{[":
            parent_key = None
            if stack:
                parent_key = stack[-1][1] if stack[-1][0] == "obj" else stack[-1][2]
            stack.append(["obj", None, None, True] if tok == "{" else ["arr", None, parent_key])
        elif tok in "}]":
            stack.pop()
            if not stack:
                return edits, m.end()
        elif tok == ",":
            if stack and stack[-1][0] == "obj":
                stack[-1][3] = True
        elif tok == ":":
            if stack and stack[-1][0] == "obj":
                stack[-1][3] = False
        else:
            if not stack:
                continue
            top = stack[-1]
            if top[0] == "obj" and top[3]:
                top[1] = json.loads(tok)
                continue
            key = top[1] if top[0] == "obj" else top[2]
            if key in _JSON_SKIP_KEYS:
                continue
            old = json.loads(tok)
            fixed = fix_text(old, hyphen=True)
            if fixed != old:
                edits.append((m.start(), m.end(), tok, _json_encode_like(tok, fixed), old))
    return edits, len(text)


def scan_json(text: str, path: str = "") -> list[Finding]:
    edits, _ = _json_edits(text)
    out: list[Finding] = []
    for a, _, _, _, old in edits:
        out.extend(Finding(path, _line_of(text, a), f.word, f.suggestion) for f in scan_text(old, hyphen=True))
    return out


def _apply_edits(text: str, edits) -> str:
    for a, b, _, new, _ in sorted(edits, reverse=True):
        text = text[:a] + new + text[b:]
    return text


def fix_json(text: str) -> str:
    """Rewrite the prose strings of a JSON file; every other byte stays as it was."""
    edits, _ = _json_edits(text)
    return _apply_edits(text, edits)


def fix_embedded_json(page: str, marker: str) -> str:
    """The same, for the JSON value that follows `marker` inside a page (atlas-v3.html's `const DATA = `)."""
    at = page.index(marker) + len(marker)
    edits, _ = _json_edits(page, at)
    return _apply_edits(page, edits)


_SURFACE = re.compile(r"Build/worlds/[^/]+/surface/")


def _is_surface(rel: str) -> bool:
    return bool(_SURFACE.match(rel))


def _kind(path: Path) -> str | None:
    rel = str(path.relative_to(REPO)) if REPO in path.parents else str(path)
    suffix = path.suffix.lower()
    if (rel.startswith("records/") or _is_surface(rel)) and suffix == ".md":
        return "record"
    if suffix in (".html", ".htm"):
        return "html"
    if suffix == ".json":
        return "json"
    if suffix in (".yaml", ".yml") and rel.startswith("records/"):
        return "yaml"
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
    if kind == "json":
        return scan_json(text, rel)
    if kind == "yaml":
        return scan_yaml(text, rel)
    if kind == "text":
        return scan_text(text, rel)
    return []


def fix_file(path: Path) -> int:
    """Rewrite one file in place; returns how many words changed."""
    kind = _kind(path)
    text = path.read_text(encoding="utf-8")
    new = {"record": fix_record, "html": fix_html, "json": fix_json, "yaml": fix_yaml, "text": fix_text}.get(kind or "", lambda t: t)(text)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return len(scan_file_text(kind, text))


def scan_file_text(kind: str | None, text: str) -> list[Finding]:
    if kind == "record":
        return scan_record(text, "")
    if kind == "html":
        return scan_html(text, "")
    if kind == "json":
        return scan_json(text, "")
    if kind == "yaml":
        return scan_yaml(text, "")
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


# Generated from the Library's own rights wording, which quotes the host sites' terms.
EXEMPT = ("cic-website/data/corpus-coverage.json",)


def is_exempt(rel: str) -> bool:
    return rel.startswith(EXEMPT)


def in_checked(rel: str) -> bool:
    return (rel.startswith(CHECKED) or _is_surface(rel)) and not is_exempt(rel)


def is_enforced(rel: str) -> bool:
    return bool(ENFORCED) and (rel.startswith(ENFORCED) or _is_surface(rel))


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
