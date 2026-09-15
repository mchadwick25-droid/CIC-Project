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

ENTRIES carries only what CANNOT be recovered by reading the file or
scanning the records: when it arrived, who supplied it, and free-form notes
(the editorial content that used to live only in the hand-maintained
README - e.g. "this volume's own Julius is Africanus, not Rome" - preserved
here so it survives being folded into a generated document instead of a
hand-edited one). Moved out of this module 2026-09-02 (Mark's sign-off) to
cic/texts/REGISTRY.yaml - same fields, same discipline, same "only what a
file can't say about itself" rule - see that file's own header for the
schema. This module still reads it, still validates it against what's
actually sitting in cic/texts/, still generates README.md from it; only
where the data itself lives changed, the same split works_registry.py/
WORKS.yaml and author_ids.py/AUTHOR-IDS.yaml already use. `ENTRIES` below
is now a loader, not a literal - every check and gate downstream is
unchanged, since they only ever consumed the tuple, never the syntax that
built it.

THE DATE RULE IS ROLLING, NOT FIXED AT 1929. US copyright duration is
published-work-plus-95-years; a work enters the public domain on January 1
of the year 95 years after its publication, every year, on a rolling basis.
As of 2026-01-01, that means works published through 1930 are public
domain, not just through 1929 - last year's line, not a permanent one.
Individual REGISTRY.yaml notes that cite "pre-1929" or "to ~1929" are
historical records of the rule as it stood when that specific file was
vendored and are correct as written; they are deliberately NOT rewritten
here to say 1930, per this registry's own no-rewrite-history practice
(the same discipline that keeps a superseded file's old note rather than
deleting it). Anyone applying the date rule to a NEW candidate should use
the current year-95 threshold, not copy the "1929" figure out of an old
note. This threshold needs restating again next January, and the January
after that, indefinitely - it is not a one-time fix.

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
REPO_ROOT = ROOT.parent  # PORT NOTE (2026-08-21, world/alexandria handoff): this script
# originated on claude/table-voice-reset-nufsm4, where records lived at cic/records/ -
# this redesign moved the records tree to <repo_root>/records/ (Artifact-1), one level
# above cic/, while cic/texts/ itself did not move. RECORDS_DIR below is the one line
# that changed for the port; citing_records()'s logic (grep every *.md under RECORDS_DIR
# for the literal "cic/texts/<filename>" path string) needed no change at all - it was
# already schema-agnostic, a dumb full-text scan, not a YAML-aware records reader.
TEXTS_DIR = ROOT / "texts"
RECORDS_DIR = REPO_ROOT / "records"

# Planning triggers for the store's total size, not a gate - see
# worlds/_cross-world/PLAN-texts-store-scaling.md for the reasoning
# (git-lfs vs a separate cic-texts repository vs doing nothing) and why these
# two numbers specifically. 700 MB is "go re-read the plan"; 1 GB is the
# blueprint's own original "act on it" threshold. Printed by report() below,
# never enforced - crossing either is not a defect.
_SIZE_TRIGGER_BYTES = 700 * 1024 * 1024
_SIZE_URGENT_BYTES = 1024 * 1024 * 1024

# Two conventions seen across what's actually been vendored, both CCEL's
# own: the plain-text export's "Rights: Public Domain" line, and ThML XML's
# own <DC.Rights>Public Domain</DC.Rights> Dublin-Core element - found only
# by reading the real anf01 XML header, not assumed from the .txt
# convention. Order matters (first alternative wins the same group number
# either way, since only one can match a given header).
_RIGHTS_LINE = re.compile(r"Rights:\s*(.+)|<DC\.Rights>\s*([^<]+)")
_TITLE_LINE = re.compile(r"Title:\s*(.+)|<DC\.Title>\s*([^<]+)")
# Added 2026-09-02, for original-language witnesses (see cic/texts/INTAKE.md):
# every file vendored before this line was English by construction, so this
# reads as None for all 64 of them - report() below treats that as English,
# not as UNVERIFIED. A file whose text is NOT the language a reader would
# assume from its title/context should say so explicitly with this line, an
# ISO 639-3 code (grc, lat, syr, ...) rather than a free-text name, the same
# "a real, checkable code, not a project-invented label" discipline
# rights_basis and AUTHOR-IDS.yaml's own identifiers already follow.
_LANGUAGE_LINE = re.compile(r"Language:\s*(.+)|<DC\.Language>\s*([^<]+)")


@dataclass(frozen=True)
class TextEntry:
    filename: str
    supplied_by: str
    date_added: str
    notes: str = ""


REGISTRY_FILE = TEXTS_DIR / "REGISTRY.yaml"


def _load_entries() -> tuple[TextEntry, ...]:
    """Reads cic/texts/REGISTRY.yaml - what CANNOT be read off a vendored
    file itself or computed by scanning records/ (see that file's own
    header for the schema and the discipline behind it). Called once, at
    import time, so ENTRIES stays what it always was: a plain tuple every
    function below already expects."""
    import yaml
    data = yaml.safe_load(REGISTRY_FILE.read_text(encoding="utf-8")) or []
    return tuple(
        TextEntry(filename=d["filename"], supplied_by=d["supplied_by"],
                  date_added=d["date_added"], notes=d.get("notes", ""))
        for d in data
    )


ENTRIES: tuple[TextEntry, ...] = _load_entries()


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


def rights_clears(rights: str | None) -> bool:
    """Whether a declared rights basis is one this registry accepts as
    verified, not just present. Two categories, not one: public domain (the
    original and still the overwhelming majority - out of copyright by age
    or an accepted transcriber declaration), and an explicit open licence
    (evagrius_praktikos_dysinger.txt, added 2026-09-02, the first file in
    this corpus that is not public domain - CC BY 4.0, which is lawful to
    vendor but carries an attribution obligation the PD files do not).
    Anything else - blank, a bare 'copyright', an in-copyright notice - is
    correctly NOT cleared here; this function widens what counts as
    verified, it does not loosen the verification itself."""
    if not rights:
        return False
    r = rights.lower()
    return "public domain" in r or "cc by" in r


def title_declared(header: str) -> str | None:
    m = _TITLE_LINE.search(header)
    if not m:
        return None
    return (m.group(1) or m.group(2)).strip()


def language_declared(header: str) -> str:
    """The file's own stated language, read fresh - same discipline as
    rights/title. Undeclared means English: every file vendored before
    2026-09-02 predates this field and is English by construction, so
    absence is the documented default, not an UNVERIFIED state the way
    a missing rights line is."""
    m = _LANGUAGE_LINE.search(header)
    if not m:
        return "en"
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
    language: str = "en"
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
        if not rights_clears(r):
            problems.append(f"{name}: no verifiable rights line found in its own header "
                            f"({r!r}) - not public domain and no recognized open licence, "
                            f"do not treat as cleared for use")
    return problems


def total_bytes() -> int:
    """Live, not cached - the sum of what's actually sitting in cic/texts/
    right now. Small enough a directory to just stat every run."""
    return sum((TEXTS_DIR / name).stat().st_size for name in discovered_files())


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
            language=language_declared(header) if exists else "en",
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
        ok = rights_clears(r.rights)
        rights_mark = r.rights if ok else f"UNVERIFIED ({r.rights!r})"
        print(f"{r.filename:<{namecol}}{rights_mark:<16}{len(r.citing):<10}")

    uncited = [r.filename for r in rows if r.exists and not r.citing]
    print(f"\n{len(rows)} vendored file(s), {len(uncited)} with zero citing record(s):")
    for name in uncited:
        print(f"  - {name}")

    non_english = [(r.filename, r.language) for r in rows if r.exists and r.language != "en"]
    if non_english:
        print(f"\n{len(non_english)} non-English source(s) - original-language witness, "
              "not primary evidence (see cic/texts/INTAKE.md):")
        for name, lang in non_english:
            print(f"  - {name}  [{lang}]")

    total = total_bytes()
    mb = total / (1024 * 1024)
    if total >= _SIZE_URGENT_BYTES:
        print(f"\ncic/texts/ is {mb:.0f} MB - at or past the ~1GB threshold in "
              "worlds/_cross-world/PLAN-texts-store-scaling.md. Time to act on "
              "that plan, not just re-read it.")
    elif total >= _SIZE_TRIGGER_BYTES:
        print(f"\ncic/texts/ is {mb:.0f} MB - past the 700MB planning trigger in "
              "worlds/_cross-world/PLAN-texts-store-scaling.md. Worth a look "
              "before it becomes urgent.")
    else:
        print(f"\ncic/texts/ is {mb:.0f} MB ({total / _SIZE_TRIGGER_BYTES:.0%} of the "
              "700MB planning trigger).")

    problems = registry_problems_live()
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("\nOK: every vendored file has a header-verified rights line (public domain, or a "
          "recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file.")
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
        "file or adding an entry to cic/texts/REGISTRY.yaml. Editing this table directly",
        "will be overwritten the next time it runs. See `cic/texts/INTAKE.md` for the",
        "full procedure, from an attached file to a vendored, registered, findable text.",
        "",
        "PUBLIC DOMAIN ONLY. Every file here must be out of copyright, and its own",
        "provenance header must say so -- the `rights` column below is read fresh",
        "from each file's own header every time this report runs, not trusted from",
        "a claim made when the file was added. In-copyright editions (Holmes 2007,",
        "Ward 1975) are referenced by `source` record and never vendored --",
        "committing them would be redistribution.",
        "",
        "`lang` is blank for English (the default when a file has no `Language:` line -",
        "true for every file vendored before 2026-09-02) and an ISO 639-3 code otherwise",
        "-- an original-language witness, not a translation; see `cic/texts/INTAKE.md`.",
        "",
        "| file | title (from the file's own header) | lang | rights | supplied | added | cited by |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        if not r.exists:
            continue
        e = r.entry
        cited = ", ".join(f"`{c}`" for c in r.citing) if r.citing else "-"
        supplied = e.supplied_by if e else "?"
        added = e.date_added if e else "?"
        lang = "" if r.language == "en" else r.language
        lines.append(f"| `{r.filename}` | {r.title or ''} | {lang} | {r.rights or 'UNVERIFIED'} "
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
