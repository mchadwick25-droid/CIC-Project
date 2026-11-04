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
ENFORCED: tuple[str, ...] = ("records/gallic/", "records/witt/", "records/cappadocian/")

# ---------------------------------------------------------------- word list
# The table lives in engine/m1/spelling_table.py, shared with the readability regate.
sys.path.insert(0, str(REPO))
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
    r"|Programme to Combat Racism",
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


def _find(text: str, markdown: bool = True) -> list[tuple[int, str]]:
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
    for m in _WORD_RE.finditer(body):
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
    "license", "tier", "kind", "voice_of", "census_id", "shelf_row", "speaker", "speaker_or_author", "name", "citation",
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
