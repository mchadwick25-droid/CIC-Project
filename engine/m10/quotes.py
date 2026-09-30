"""Re-verification of every quotation in the Step 0-2 documents (handoff check 8)."""
from __future__ import annotations

import itertools
import re
import sys
from pathlib import Path

import yaml

from engine.m1.quote_verbatim import (
    collapse_linewrap_hyphens,
    normalize_archaic_letterforms,
    strip_apparatus,
    strip_edition_apparatus,
    strip_xml_markup,
    iter_source_notes,
    verify_quote_against_notes,
    verify_quote_text,
)

from .common import REPO_ROOT, Finding, read_text, rel, world_dir

MIN_WORDS = 5
FAST_HITS = 20
WINDOW_SHARE = 0.5
_ELLIPSIS = re.compile(r"\.\.\.|…")
_STRAIGHT = re.compile(r'"([^"]+)"')
_CURLY = re.compile(r"“([^”]+)”")
_PATH = re.compile(r"cic/texts/([\w.\-]+\.(?:txt|xml))")
_FILENAME = re.compile(r"\b([\w\-]+_[\w.\-]+\.(?:txt|xml))\b")
_ADDRESS = re.compile(r"cic:(?P<file>[\w.\-]+?\.(?:txt|xml)):(?P<locus>[^\s`'\",;)\]>]+)")
_DIV_OPEN = re.compile(r'<div(?P<level>[1-3])\b(?P<attrs>[^>]*)>')
_ID = re.compile(r'\bid="([^"]*)"')
_TITLE = re.compile(r'\btitle="([^"]*)"')
_REVIEWISH = re.compile(r"review|spotcheck|round|verification|history", re.IGNORECASE)
_NORM = re.compile(r"\s+")


def _squash(text: str) -> str:
    return " ".join(re.sub(r"[\W_]+", " ", text.lower()).split())


def paragraphs(text: str) -> list[str]:
    out, current = [], []
    for line in text.splitlines():
        if not line.strip():
            if current:
                out.append(" ".join(current))
                current = []
            continue
        current.append(re.sub(r"^\s*>\s?", "", line).strip())
    if current:
        out.append(" ".join(current))
    return out


def extract_quotations(paragraph: str) -> tuple[list[str], bool]:
    """Quoted spans of MIN_WORDS words or more, and whether the straight
    quotation marks could be paired."""
    balanced = paragraph.count('"') % 2 == 0
    spans = []
    if balanced:
        spans += _STRAIGHT.findall(paragraph)
    spans += _CURLY.findall(paragraph)
    spans = [re.sub(r"[*`]", "", s).strip().strip(".,;:!?").strip() for s in spans]
    return [s for s in spans if len(s.split()) >= MIN_WORDS], balanced


class TextStore:
    def __init__(self, texts_dir: Path):
        self.texts_dir = texts_dir
        self._raw: dict[str, str | None] = {}
        self._plain: dict[str, str] = {}
        self._search: dict[str, str] = {}
        self._unstripped: dict[str, str] = {}
        self._processed: dict[str, str] = {}
        self._unit_cache: dict[str, list[dict]] = {}
        self.prefixes: dict[str, list[str]] = {}
        if texts_dir.is_dir():
            for p in sorted(texts_dir.iterdir()):
                if p.suffix in (".txt", ".xml"):
                    self.prefixes.setdefault(p.stem.split("_")[0], []).append(p.name)

    def exists(self, name: str) -> bool:
        return (self.texts_dir / name).is_file()

    def _load(self, name: str) -> tuple[str, str] | None:
        if name not in self._raw:
            path = self.texts_dir / name
            if not path.is_file():
                self._raw[name] = None
            else:
                whole = path.read_text(encoding="utf-8", errors="replace")
                self._unstripped[name] = whole
                raw = strip_edition_apparatus(whole, name)
                self._raw[name] = raw
                self._plain[name] = strip_xml_markup(raw) if path.suffix == ".xml" else raw
        raw = self._raw[name]
        return None if raw is None else (raw, self._plain[name])

    def _proc(self, name: str) -> str:
        if name not in self._processed:
            plain = self._plain[name]
            self._processed[name] = normalize_archaic_letterforms(strip_apparatus(collapse_linewrap_hyphens(plain)))[0]
        return self._processed[name]

    def may_contain(self, span: str, name: str) -> bool:
        """Cheap screen before the exact matcher: at least WINDOW_SHARE of the
        quotation's three-word runs must occur in the file once case and
        punctuation are set aside. It only ever rules a file out; the exact
        matcher alone accepts a quotation."""
        if self._load(name) is None:
            return False
        if name not in self._search:
            notes = " ".join(text for _, text in iter_source_notes(self._unstripped[name]))
            self._search[name] = _squash(self._proc(name) + " " + normalize_archaic_letterforms(strip_apparatus(notes))[0])
        words = _squash(normalize_archaic_letterforms(span)[0]).split()
        if len(words) < 4:
            return True
        windows = [" ".join(words[i : i + 3]) for i in range(len(words) - 2)]
        found = sum(1 for w in windows if w in self._search[name])
        return found / len(windows) >= WINDOW_SHARE

    def _fast(self, span: str, name: str):
        """The exact matcher, run on a slice of the file around each place the
        quotation's first three words occur. A match inside a slice is a match
        in the file; a miss here settles nothing, and the full pass follows."""
        if _ELLIPSIS.search(span):
            return None
        normalized = normalize_archaic_letterforms(span)[0]
        opening = re.findall(r"\w+", normalized)[:3]
        if len(opening) < 3:
            return None
        text = self._proc(name)
        anchor = re.compile(r"\W+".join(re.escape(t) for t in opening), re.IGNORECASE)
        for hit in itertools.islice(anchor.finditer(text), FAST_HITS):
            piece = text[max(0, hit.start() - 200) : hit.start() + 3 * len(normalized) + 400]
            result = verify_quote_text(normalized, piece, source_is_xml=False, apply_letterform_normalization=False)
            if result.verified:
                return result
        return None

    def verify(self, span: str, name: str):
        loaded = self._load(name)
        if loaded is None or not self.may_contain(span, name):
            return None
        fast = self._fast(span, name)
        if fast is not None:
            return fast
        raw, plain = loaded
        result = verify_quote_text(span, plain, source_is_xml=False)
        if result.verified:
            return result
        return verify_quote_against_notes(span, self._unstripped[name]) or result

    def _units(self, name: str) -> list[dict]:
        if name not in self._unit_cache:
            engine_dir = str(REPO_ROOT / "cic" / "engine")
            sys.path.insert(0, engine_dir)
            try:
                from corpus_index import passage_units

                self._unit_cache[name] = passage_units(self.texts_dir / name)
            finally:
                sys.path.remove(engine_dir)
        return self._unit_cache[name]

    def locus_text(self, name: str, locus: str) -> str | None:
        """The text of the division `locus` names in file `name`: a div whose
        id or title is `locus`, with everything beneath it, or, in a plain-text
        file, the passage unit at that address. None when the file has no such
        division."""
        loaded = self._load(name)
        if loaded is None:
            return None
        raw = loaded[0]
        wanted = " ".join(locus.lower().split())
        marks = [(m.start(), m.end(), int(m.group("level")), m.group("attrs")) for m in _DIV_OPEN.finditer(raw)]
        if marks:
            pieces = []
            for index, (start, end, level, attrs) in enumerate(marks):
                ident = _ID.search(attrs)
                title = _TITLE.search(attrs)
                if (ident and ident.group(1) == locus) or (title and " ".join(title.group(1).lower().split()) == wanted):
                    stop = next((m[0] for m in marks[index + 1 :] if m[2] <= level), len(raw))
                    pieces.append(strip_xml_markup(raw[end:stop]))
            return "\n".join(pieces) if pieces else None
        pieces = [u["text"] for u in self._units(name) if u["locus"] == locus or " ".join(u.get("title", "").lower().split()) == wanted]
        return "\n".join(pieces) if pieces else None

    def valid_loci(self, name: str) -> tuple[list[str], bool]:
        """(loci, plain_text): every locus of file `name` that `locus_text`
        accepts, in file order, and whether the file is plain text, where a
        locus is `line<N>`."""
        loaded = self._load(name)
        if loaded is None:
            return [], False
        marks = [m.group("attrs") for m in _DIV_OPEN.finditer(loaded[0])]
        if marks:
            found = []
            for attrs in marks:
                ident, title = _ID.search(attrs), _TITLE.search(attrs)
                found.append(ident.group(1) if ident else title.group(1) if title else "")
            return list(dict.fromkeys(x for x in found if x)), False
        return list(dict.fromkeys(u["locus"] for u in self._units(name))), True

    def verify_in(self, span: str, text: str) -> bool:
        """Whether the quotation is found word for word inside `text`, a
        division's own text."""
        if verify_quote_text(span, text, source_is_xml=False).verified:
            return True
        cleaned = normalize_archaic_letterforms(strip_apparatus(collapse_linewrap_hyphens(text)))[0]
        return verify_quote_text(normalize_archaic_letterforms(span)[0], cleaned, source_is_xml=False, apply_letterform_normalization=False).verified

    def cited_in(self, text: str) -> list[str]:
        names = list(_PATH.findall(text)) + list(_FILENAME.findall(text))
        for token in set(re.findall(r"\b[a-z]+\d+[a-z]?\b", text)):
            names += self.prefixes.get(token, [])
        return [n for n in dict.fromkeys(names) if self.exists(n)]


def _norm(text: str) -> str:
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return _NORM.sub(" ", text).lower().strip()


def _project_texts(code: str, root: Path, slug: str | None = None) -> dict[str, str]:
    """Documents a quotation may legitimately quote instead of a source: the
    fleet-level documents and method library. Nothing from the world under
    check is included (its Step 0-2 documents, Source Registry and later build
    documents all come from the same drafter, so one invented quotation
    repeated across them would exempt itself), nor is its dossier."""
    own = world_dir(code, root).resolve()
    dossier = (root / "Build" / "worlds" / "_cross-world" / "dossiers" / f"{slug}_Source_Readiness_Dossier.md").resolve() if slug else None
    files: list[Path] = []
    for directory in (root / "Build" / "worlds" / "_cross-world", root / "Build" / "reference"):
        if directory.is_dir():
            files += [p for p in sorted(directory.rglob("*.md")) if not _REVIEWISH.search(p.name) and "Review-Artifacts" not in p.parts]
    files += [p for p in (root / "CLAUDE.md", root / "cic-website" / "data" / "world-census.json") if p.is_file()]
    out = {}
    for p in files:
        resolved = p.resolve()
        if own in resolved.parents or resolved == dossier:
            continue
        out[rel(p, root)] = _norm(read_text(p))
    return out


def _bucket_rows(slug: str | None, root: Path) -> list[dict]:
    if not slug:
        return []
    path = root / "cic" / "corpus-map" / f"{slug}.yaml"
    if not path.is_file():
        return []
    return list((yaml.safe_load(read_text(path)) or {}).get("works") or [])


def _speaker_tokens(value: str) -> set[str]:
    return {t for t in re.split(r"[^a-z]+", str(value).lower()) if len(t) > 3}


LOCI_SHOWN = 10


def _loci_hint(store: TextStore, name: str) -> str:
    loci, plain = store.valid_loci(name)
    if not loci:
        return ""
    shown = ", ".join(loci[:LOCI_SHOWN])
    more = f", first {LOCI_SHOWN} shown" if len(loci) > LOCI_SHOWN else ""
    kind = "; plain-text loci are line<N>, the line number corpus_index prints for the passage" if plain else ""
    return f"{kind}; valid loci: {shown} ({len(loci)} in all{more})"


def confirm_locus(store: TextStore, span: str, paragraph: str) -> tuple[bool | None, list[Finding]]:
    """(confirmed, problems) for a quotation whose paragraph cites canonical
    addresses (cic:<file>:<locus>). The quotation must sit inside the division
    one of the addresses names, found by its div id or title, and not merely
    somewhere in the file. None when the paragraph cites no address."""
    addresses = [(m.group("file"), m.group("locus").rstrip(".,;:")) for m in _ADDRESS.finditer(paragraph)]
    if not addresses:
        return None, []
    problems: list[Finding] = []
    for name, locus in dict.fromkeys(addresses):
        text = store.locus_text(name, locus)
        if text is None:
            problems.append(Finding("", "quotes-locus-unknown", f"cic:{name}:{locus} does not name a division of {name}{_loci_hint(store, name)}"))
        elif store.verify_in(span, text):
            return True, []
        else:
            problems.append(Finding("", "quotes-locus", f"found in the file but not inside cic:{name}:{locus}: {span[:70]!r}"))
    return False, problems


def check_quotes(code: str, documents: list[Path], root: Path = REPO_ROOT, *, slug: str | None = None) -> tuple[list[Finding], list[str]]:
    store = TextStore(root / "cic" / "texts")
    rows = _bucket_rows(slug, root)
    files_by_name: dict[str, list[dict]] = {}
    for row in rows:
        files_by_name.setdefault(row.get("source_file", ""), []).append(row)
    bucket_files = [n for n in files_by_name if store.exists(n)]

    findings: list[Finding] = []
    notes: list[str] = []
    checked = exempt = located = unlocated = 0
    for doc in documents:
        where = rel(doc, root)
        text = read_text(doc)
        doc_cited = store.cited_in(text)
        project: dict[str, str] | None = None
        for para in paragraphs(text):
            spans, balanced = extract_quotations(para)
            if not balanced:
                findings.append(Finding(where, "quotes-unbalanced", f"cannot pair the quotation marks in this paragraph, so its quotations are unchecked: {para[:70]!r}"))
            para_cited = store.cited_in(para)
            for span in spans:
                checked += 1
                tiers = [para_cited, doc_cited, bucket_files]
                hit = None
                tried: list[str] = []
                for tier in tiers:
                    for name in tier:
                        if name in tried:
                            continue
                        tried.append(name)
                        result = store.verify(span, name)
                        if result is not None and result.verified:
                            hit = name
                            break
                    if hit:
                        break
                if hit is None:
                    if project is None:
                        project = _project_texts(code, root, slug)
                    needle = _norm(span)
                    source = next((p for p, body in project.items() if needle in body), None)
                    if source:
                        exempt += 1
                        notes.append(f"{where}: quotation is from project document {source}: {span[:60]!r}")
                        continue
                    where_tried = f"the {len(tried)} cited or assigned cic/texts file(s)" if tried else "any cic/texts file (none cited or assigned)"
                    findings.append(Finding(where, "quotes-unverified", f"not found word for word in {where_tried}: {span[:90]!r}"))
                    continue
                confirmed, problems = confirm_locus(store, span, para)
                if confirmed:
                    located += 1
                elif confirmed is None:
                    unlocated += 1
                else:
                    findings.extend(Finding(where, p.check, p.reason) for p in problems)
                file_rows = files_by_name.get(hit, [])
                mixed = [r for r in file_rows if r.get("voice_of")]
                if mixed:
                    named: set[str] = set()
                    for r in file_rows:
                        named |= _speaker_tokens(r.get("author", "")) | _speaker_tokens(r.get("voice_of") or "")
                    if not (named & _speaker_tokens(para)):
                        findings.append(Finding(where, "quotes-speaker", f"{hit} mixes voices (voice_of {mixed[0]['voice_of']!r}); the paragraph does not name the speaker of: {span[:70]!r}"))
    notes.insert(0, f"{checked} quotation(s) of {MIN_WORDS}+ words checked, {exempt} taken from project documents")
    notes.insert(1, f"{located} confirmed inside a cited cic:<file>:<locus> division, {unlocated} found in a file with no address cited in their paragraph")
    return findings, notes
