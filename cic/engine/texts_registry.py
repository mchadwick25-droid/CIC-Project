#!/usr/bin/env python3
"""The vendored-text registry - what's sitting in cic/texts/, verified, not asserted.

WHY. Vendoring CCEL's public-domain volumes solved a real, total blocker this
session hit repeatedly: every patristic text host (ccel.org, newadvent.org,
wikisource, archive.org, gutenberg.org, tertullian.org) is blocked by this
sandbox's egress policy, so without a local copy no quote could be verified
at all - Check B's whole grounding claim (`verified-direct`) had nothing to
stand on. Vendoring fixed that. But by the time this registry was built,
10 volumes (38MB) were already sitting in cic/texts/ with only 3 ever linked
to a record that cites them - a real, measured fact (found 2026-08-15 by
hand-grepping, the trigger for building this) with no earlier structure that
would have surfaced it on its own. That is the SAME shape of problem
mechanism_dependencies.py (T3-A) and gate_mechanism_coverage (T3-B) exist to
catch at the record layer - a resource sitting present with no declared
need - just one layer up, at the reference-text layer instead.

WHAT THIS VERIFIES, NOT ASSERTS. Two facts about a vendored file are
worth checking every run rather than trusting a claim written when the file
arrived: (1) does its OWN header actually state a public-domain rights
basis - checked by reading the file, not by re-trusting whatever note
accompanied it when vendored, and (2) which records actually cite it -
computed by scanning cic/records/ for the literal file path, not read off a
static "covers" field that could drift out of date the moment a new quote
record is authored. A registry that just repeated hand-typed claims would
be exactly the kind of self-certified report this build's own review
discipline (CO-020/CO-022) already distrusts.

ENTRIES below carries only what CANNOT be recovered by reading the file or
scanning the records: when it arrived, who supplied it, and free-form notes
(the editorial content that used to live only in the hand-maintained
README - e.g. "this volume's own Julius is Africanus, not Rome" - preserved
here so it survives being folded into a generated document instead of a
hand-edited one).

Usage:
  python cic/engine/texts_registry.py                 # report
  python cic/engine/texts_registry.py --write-readme   # regenerate cic/texts/README.md
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
TEXTS_DIR = ROOT / "texts"
RECORDS_DIR = ROOT / "records"

# Two conventions seen across what's actually been vendored, both CCEL's
# own: the plain-text export's "Rights: Public Domain" line, and ThML XML's
# own <DC.Rights>Public Domain</DC.Rights> Dublin-Core element - found only
# by reading the real anf01 XML header, not assumed from the .txt
# convention. Order matters (first alternative wins the same group number
# either way, since only one can match a given header).
_RIGHTS_LINE = re.compile(r"Rights:\s*(.+)|<DC\.Rights>\s*([^<]+)")
_TITLE_LINE = re.compile(r"Title:\s*(.+)|<DC\.Title>\s*([^<]+)")


@dataclass(frozen=True)
class TextEntry:
    filename: str
    supplied_by: str
    date_added: str
    notes: str = ""


# What CANNOT be read off the file itself or computed from the records.
ENTRIES: tuple[TextEntry, ...] = (
    TextEntry("anf01_apostolic-fathers-justin-irenaeus.xml", "Mark", "2026-08-15",
              "CCEL's native ThML source, SWAPPED IN 2026-08-15 for the plain-text rendering that "
              "originally carried this id - same volume, same rights basis, verified byte-identical "
              "on all four passages already committed as quote records (pahcq001-004) before the "
              "swap. Structurally better for this build's own purposes: shorter/longer/Syriac "
              "recensions are addressable by id (e.g. v.v.iv-p1 vs v.v.iv-p4 for Romans 4), and "
              "footnotes are their own <note> elements rather than interleaved apparatus text - both "
              "real friction points hand-transcribing the plain text had already hit. Extracting text "
              "correctly requires walking element trees properly, not naive regex: a lazy `<p>...</p>` "
              "match truncates early against nested <note><p class=\"endnote\">...</p></note> "
              "structures, and a node's own skip-tag status must not be applied to its `tail` text - "
              "both mistakes were made and caught live during this swap, on the Smyrnaeans and "
              "Martyrdom-of-Polycarp passages respectively, before anything was recommitted."),
    TextEntry("anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml", "Mark", "2026-08-15",
              "Shepherd of Hermas, Tatian, Athenagoras, Theophilus, Clement of Alexandria. Swapped from "
              "the plain-text rendering the same day, as anf01 was - no record cited the old .txt file "
              "(this volume's own zero-citation status, unchanged), so this swap needed no "
              "re-verification of any existing quote."),
    TextEntry("anf03_tertullian.xml", "Mark", "2026-08-15",
              "Carries Tertullian's Apologeticus, the primary text srcPAHCP15 already cites in pahc "
              "('Tertullian, Apology 39'). No quote record was in this session's worklist, so none "
              "was written, but the translation edition is available if one is ever wanted. Swapped "
              "from the plain-text rendering the same day, as anf01/anf02 were - zero citations before "
              "the swap, so nothing needed re-verification."),
    TextEntry("anf04_tertullian4-minucius-felix-commodian-origen1-2.txt", "Mark", "2026-08-15",
              "Tertullian Pt. 4, Minucius Felix, Commodian, Origen Pts. 1-2."),
    TextEntry("anf05_hippolytus-cyprian-caius-novatian.xml", "Mark", "2026-08-15",
              "Hippolytus, Cyprian, Caius, Novatian. Carries ~82 of Cyprian's own letters plus On the "
              "Lapsed, On the Mortality, and Pontius's Life of Cyprian - primary-source material for "
              "the not-yet-built Latin Pastoral-Congregational Christianity world (census: "
              "'Selected - Not Yet Built'). Swapped from the plain-text rendering the same day, as "
              "anf01/02/03 were - zero citations before the swap, so nothing needed re-verification. "
              "Structured letter/chapter ids here would matter directly once that world is built: "
              "Cyprian's ~82 letters are individually addressable rather than needing to be located "
              "by reading forward through flowing prose."),
    TextEntry("anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml", "Mark",
              "2026-08-15",
              "This volume's own 'Julius' is Julius Africanus the chronographer, a named author here - "
              "NOT Julius I of Rome (srcIJC04/srcIJC42). Swapped from the plain-text rendering the same "
              "day, as anf01/02/03/05 were - zero citations before the swap, so nothing needed "
              "re-verification."),
    TextEntry("anf07_lactantius-apostolic-constitutions-didache-liturgies.xml", "Mark", "2026-08-15",
              "Carries the Didache, published too late for ANF vol. 1 - closed the deferred gap "
              "srcPAHCS62 named. Translator for the Didache specifically: Isaac H. Hall and John T. "
              "Napier (Sunday-School Times, 1884), not the volume's general editors. Swapped from the "
              "plain-text rendering the same day, as anf01/02/03/05/06 were - unlike those, this one "
              "had an existing quote (pahcq005) and source (srcPAHCS63) citing it, so both were "
              "re-verified against the XML with the tail-aware element walker before the swap, not "
              "just before it was trusted: the committed wording matched exactly."),
    TextEntry("anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.txt", "Mark", "2026-08-15",
              "Carries Abgar/Edessa correspondence material, relevant to syriac world (syrfig005, "
              "Addai) - not drawn on so far; that figure's own record already treats him as legend, "
              "not history."),
    TextEntry("anf09_gospel-of-peter-diatessaron-origen-commentaries.txt", "Mark", "2026-08-15",
              "Origen's Commentaries on John and Matthew, among others."),
    TextEntry("npnf204_athanasius-select-works-letters.txt", "Mark", "2026-08-15",
              "The volume srcIJC42 was scoped for from the start. Closed the last inert Check B cell "
              "in the fleet (ijcq001, Julius I's letter of 341)."),
)


def read_header(path: Path, lines: int = 100) -> str:
    """The file's own first N lines - generous on purpose, and widened twice
    now for two different real reasons. Two of the ten plain-text files have
    titles that wrap across 4-6 lines before the Rights: line appears; an
    8-line window (this module's first draft) missed both and would have
    false-flagged two genuinely public-domain files as unverified. Then the
    anf01 XML swap: ThML's own <DC.Rights> Dublin-Core element sits at line
    68 in that file's real header, well past the 30-line window that had
    covered every plain-text file fine - widened to 100 with margin for
    other ThML files' own varying metadata-block length.
    """
    out = []
    with path.open(encoding="utf-8", errors="replace") as f:
        for _ in range(lines):
            line = f.readline()
            if not line:
                break
            out.append(line)
    return "".join(out)


def rights_declared(header: str) -> str | None:
    """The file's own stated rights basis, or None if it cannot be found -
    checked fresh every run, not trusted from whatever note accompanied the
    file when it was vendored."""
    m = _RIGHTS_LINE.search(header)
    if not m:
        return None
    return (m.group(1) or m.group(2)).strip()  # exactly one alternative matches


def title_declared(header: str) -> str | None:
    m = _TITLE_LINE.search(header)
    if not m:
        return None
    return (m.group(1) or m.group(2)).strip()


def discovered_files() -> list[str]:
    """What is ACTUALLY sitting in cic/texts/ right now, not what ENTRIES
    claims - the two are cross-checked in report(), not assumed to agree."""
    # Both plain-text renderings and CCEL's native ThML XML source live here
    # now (the anf01 swap, 2026-08-15) - a *.txt-only glob went blind to the
    # first .xml file added and silently reported it as a missing file, a
    # real bug caught live while doing that swap, not a hypothetical one.
    return sorted(p.name for p in TEXTS_DIR.iterdir()
                  if p.is_file() and p.suffix in (".txt", ".xml"))


def citing_records(filename: str) -> list[str]:
    """Every record under cic/records/ whose own text mentions this vendored
    file by path - source records typically for the translation-edition
    claim, quote records typically for the transcription itself. Computed by
    scanning the records, not read off a static field: a citation this
    session actually has to catch lives in the QUOTE record's body prose for
    anf01, not in its source record at all (srcPAHCS62 never repeats the
    path; pahcq001-004 do) - a coverage-only source-record scan would have
    silently under-counted a real, already-verified citation.
    """
    needle = f"cic/texts/{filename}"
    hits = []
    for p in sorted(RECORDS_DIR.rglob("*.md")):
        try:
            if needle in p.read_text(encoding="utf-8"):
                hits.append(p.stem)
        except Exception:  # noqa: BLE001
            continue
    return hits


@dataclass
class Row:
    entry: TextEntry | None
    filename: str
    exists: bool
    rights: str | None
    title: str | None
    citing: list[str] = field(default_factory=list)


def registry_problems(entries: tuple, discovered: list, headers: dict) -> list:
    """PURE - no file I/O, no import of anything that touches disk. entries:
    TextEntry tuples (what's declared). discovered: filenames actually found
    under cic/texts/ (what's real). headers: {filename: its own header text},
    already read by the caller. Returns violation strings.

    Split out from report()/the live gate deliberately, for T3-G's own
    reason: "a gate that never fails checks nothing" only means something if
    the gate can be handed a KNOWN-BROKEN case and shown to catch it. A
    version of this logic that always reads the real cic/texts/ directory
    can only ever be fixture-tested against whatever that directory's real
    state happens to be right now (today, genuinely clean) - which proves
    nothing about whether the CHECK is correct, only that nobody has broken
    anything yet. This function takes plain data instead, so gate_fixtures.py
    can hand it a literal broken case with no real file on disk at all.

    THREE integrity checks, deliberately not four. Missing rights line,
    undeclared file, orphaned ENTRIES row are real mistakes with a knowable
    right answer - today's baseline is genuinely zero, so any of the three
    appearing is new, current-moment state worth catching immediately, not
    legacy debt to grandfather (the reasoning that made mechanism_coverage
    advisory does not apply here). Whether a vendored file has been CITED
    YET is deliberately NOT a fourth check here: an unexploited volume is
    not a mistake, and turning it into a violation would be inventing a
    threshold nobody asked for - exactly the "assume the floor" move
    mechanism_coverage's own docstring already refuses for the same reason.
    Citation counts stay in report()'s informational output only.
    """
    problems = []
    declared = {e.filename for e in entries}
    found = set(discovered)
    for name in sorted(declared - found):
        problems.append(f"{name}: declared in ENTRIES but no file present in cic/texts/")
    for name in sorted(found - declared):
        problems.append(f"{name}: file present in cic/texts/ but no ENTRIES row - "
                        f"undeclared vendoring")
    for name in sorted(declared & found):
        r = rights_declared(headers.get(name, ""))
        if not (r and "public domain" in r.lower()):
            problems.append(f"{name}: no verifiable public-domain rights line found in its "
                            f"own header ({r!r}) - do not treat as cleared for use")
    return problems


def registry_problems_live() -> list:
    """The real check: ENTRIES against whatever is actually sitting in
    cic/texts/ right now, headers read fresh. This is what gate_texts_registry
    (gates.py) and report() below both call - one place this logic lives,
    so the CLI report and the gate's verdict can never quietly disagree."""
    discovered = discovered_files()
    headers = {name: read_header(TEXTS_DIR / name) for name in discovered}
    return registry_problems(ENTRIES, discovered, headers)


def build_rows() -> list[Row]:
    by_name = {e.filename: e for e in ENTRIES}
    names = sorted(set(by_name) | set(discovered_files()))
    rows = []
    for name in names:
        path = TEXTS_DIR / name
        exists = path.exists()
        header = read_header(path) if exists else ""
        rows.append(Row(
            entry=by_name.get(name),
            filename=name,
            exists=exists,
            rights=rights_declared(header) if exists else None,
            title=title_declared(header) if exists else None,
            citing=citing_records(name) if exists else [],
        ))
    return rows


def report() -> int:
    rows = build_rows()
    namecol = max(len(r.filename) for r in rows) + 2
    print(f"{'file':<{namecol}}{'rights':<16}{'cited by':<10}")
    print("-" * (namecol + 26))
    for r in rows:
        if not r.exists:
            print(f"{r.filename:<{namecol}}{'MISSING FILE':<16}")
            continue
        ok = bool(r.rights and "public domain" in r.rights.lower())
        rights_mark = r.rights if ok else f"UNVERIFIED ({r.rights!r})"
        print(f"{r.filename:<{namecol}}{rights_mark:<16}{len(r.citing):<10}")

    uncited = [r.filename for r in rows if r.exists and not r.citing]
    print(f"\n{len(rows)} vendored file(s), {len(uncited)} with zero citing record(s):")
    for name in uncited:
        print(f"  - {name}")

    problems = registry_problems_live()
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("\nOK: every vendored file has a header-verified public-domain rights line, "
          "an ENTRIES row, and no ENTRIES row points at a missing file.")
    return 0


def write_readme() -> int:
    rows = build_rows()
    lines = [
        "# Vendored public-domain source texts",
        "",
        "Full text of editions this build's quote records cite, committed so that",
        "wording can be verified *reproducibly* -- by any session, at any time,",
        "without network access. That matters here for a specific reason: the",
        "sandbox this project's agents run in blocks every patristic text host",
        "(ccel.org, newadvent.org, wikisource, archive.org, gutenberg, tertullian.org),",
        "so before these files existed a quote record could not be verified at all",
        "and `gate_quote_fidelity_recording` had nothing honest to record.",
        "",
        "**This file is GENERATED, not hand-edited** -- run",
        "`python cic/engine/texts_registry.py --write-readme` after vendoring a new",
        "file or adding an ENTRIES row in that module. Editing this table directly",
        "will be overwritten the next time it runs.",
        "",
        "PUBLIC DOMAIN ONLY. Every file here must be out of copyright, and its own",
        "provenance header must say so -- the `rights` column below is read fresh",
        "from each file's own header every time this report runs, not trusted from",
        "a claim made when the file was added. In-copyright editions (Holmes 2007,",
        "Ward 1975) are referenced by `source` record and never vendored --",
        "committing them would be redistribution.",
        "",
        "| file | title (from the file's own header) | rights | supplied | added | cited by |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        if not r.exists:
            continue
        e = r.entry
        cited = ", ".join(f"`{c}`" for c in r.citing) if r.citing else "-"
        supplied = e.supplied_by if e else "?"
        added = e.date_added if e else "?"
        lines.append(f"| `{r.filename}` | {r.title or ''} | {r.rights or 'UNVERIFIED'} "
                     f"| {supplied} | {added} | {cited} |")

    lines.append("")
    lines.append("Notes carried over per file:")
    lines.append("")
    for r in rows:
        if r.entry and r.entry.notes:
            lines.append(f"- **`{r.filename}`** -- {r.entry.notes}")
    lines.append("")
    lines.append(
        "Not records: nothing here is schema-validated or read by the runtime. These "
        "are reference copies for verification, cited by the `source`/`quote` records "
        "that carry the bibliographic and wording claims."
    )
    lines.append("")

    (TEXTS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {TEXTS_DIR / 'README.md'}: {sum(1 for r in rows if r.exists)} file(s) listed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-readme", action="store_true")
    args = ap.parse_args()
    if args.write_readme:
        return write_readme()
    return report()


if __name__ == "__main__":
    sys.exit(main())
