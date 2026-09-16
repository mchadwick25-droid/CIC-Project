#!/usr/bin/env python3
"""Work-granularity coverage diff: assigned corpus vs. records that actually opened it.

WHY THIS EXISTS
---------------
The existing discovery sweep (e.g. `alx.search.unopened-volume-sweep`) asks a
VOLUME-level question: "which vendored volumes does this world name an author of,
while never opening that author's works?" That instrument is blind to a whole class
of gap — an *assigned work sitting inside a volume the world has already opened*.

Alexandria is the worked example (OG-6, 2026-09-09): it opens `anf06` for two works
(Gregory's Address, Dionysius's Extant Fragments), so anf06 was never an "unopened
volume" — while twelve further anf06 works assigned to it, including Peter of
Alexandria's Canonical Epistle and the Theognostus and Pierus fragments, had zero
records. The sweep's own note reads its short result as a sign of health; that
inference is backwards for this failure mode, because the more volumes a world opens,
the more of its assigned works hide inside opened volumes.

The corpus map is already work-granular data (`work`, `author`, `locus`,
`confidence`, `source_file`). Nothing diffs it against the records. This does.

WHAT IT REPORTS — three classes per assigned work:

  AUTHOR-ABSENT     the assigned author's name appears NOWHERE in this world's records
                    <-- THE HARD FINDING. This is Peter of Alexandria's class.
  WORK-UNCONFIRMED  the author is present, but nothing evidences THIS work - e.g. a
                    second work by an author the world already opened. Needs a human.
  VOLUME-UNOPENED   no record cites this source_file at all (the class the existing
                    volume-level sweep already catches)
  OPENED            author present, volume cited, and the work's own title corroborates
  INDETERMINATE     the author's name is too common in this world to test with

HONEST LIMITS — read before acting on output:
  * This is TRIAGE, not adjudication. Token matching produces both false positives
    (a token appearing only inside a *filename* in an `edition:` field — a real trap:
    grepping `peter` in records/alx matches `anf09_gospel-of-peter-...xml` twice and
    neither line mentions any Peter) and false negatives (a record covering a work
    under a different name). Filename-only matches are detected and reported
    separately rather than counted as coverage.
  * An AUTHOR-ABSENT row is a QUESTION for a human, not a defect. A world may have
    deliberately declined a work; several of Alexandria's are correctly declined.
  * INDETERMINATE is common and expected: a world's own principal authors (Athanasius,
    Origen) appear in so many records that their names cannot discriminate between
    their individual works. This instrument does not resolve those; only reading does.
  * It cannot tell "assigned but deliberately not drawn on" from "assigned and
    overlooked". Only reading the records can.

USAGE
-----
    python3 cic/corpus-map/work_coverage_diff.py                 # all mapped worlds
    python3 cic/corpus-map/work_coverage_diff.py --world alx     # one world
    python3 cic/corpus-map/work_coverage_diff.py --assigned-only # skip provisional
    python3 cic/corpus-map/work_coverage_diff.py --json report.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
CORPUS_MAP = REPO / "cic" / "corpus-map"
RECORDS = REPO / "records"

# corpus-map file stem -> records/<key>/ directory.
# Only worlds with BOTH a corpus map and a record store are diffable.
WORLD_MAP = {
    "alexandria-catechetical": "alx",
    "desert-monasticism": "desert",
    "post-apostolic-house-church": "pahc",
    "hieronymian-ascetic-literary": "hal",
    "syriac-edessa-nisibis": "syr",
    "imperial-juridical-christianity": "ijc",
    "cappadocian-nicene-pastoral-monastic-tradition": "cappadocian",
}

# A token appearing in more than this fraction of a world's records is treated as
# world-wide vocabulary, not evidence that a particular work was opened.
DF_CEILING = 0.25

STOPWORDS = {
    "the", "of", "and", "on", "to", "in", "a", "an", "from", "with", "his", "her",
    "for", "by", "at", "or", "as", "is", "it", "be", "fragments", "fragment",
    "works", "work", "book", "books", "letter", "letters", "epistle", "epistles",
    "homily", "homilies", "treatise", "sermon", "sermons", "discourse", "discourses",
    "commentary", "extant", "selected", "select", "against", "concerning", "life",
    "acts", "canons", "canon", "volume", "part", "text", "texts", "writings",
    "introduction", "notes", "other", "some", "two", "three", "four", "five", "six",
}


def load_rows(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [r for r in data if isinstance(r, dict)]
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list) and value and isinstance(value[0], dict):
                return [r for r in value if isinstance(r, dict)]
    return []


def load_records(world_dir: Path) -> list[tuple[Path, str]]:
    return [
        (p, p.read_text(encoding="utf-8", errors="replace"))
        for p in sorted(world_dir.rglob("*.md"))
    ]


def author_tokens(row: dict) -> list[str]:
    """Tokens naming the AUTHOR - the only reliable work-identity signal available.

    Title words alone are far too noisy: Peter of Alexandria's `On the Godhead` and
    `Canonical Epistle` yield `godhead`, `paschal` and `canonical`, every one of which
    occurs in Alexandria's records for unrelated reasons (Athanasius's paschal letters,
    the Alexandrian canonical answers). Matching on those reported Peter as OPENED when
    he has no record at all. The author's own name does not have that problem.
    """
    out: set[str] = set()
    for part in re.split(r"[_\-\s]+", str(row.get("author") or "")):
        p = part.lower()
        if len(p) > 3 and p not in STOPWORDS:
            out.add(p)
    return sorted(out)


def title_tokens(row: dict) -> list[str]:
    """Distinctive title words - corroborating only, never sufficient on their own."""
    out: set[str] = set()
    for word in re.findall(r"[A-Za-z][A-Za-z'’]+", str(row.get("work") or "")):
        w = word.lower()
        if len(w) > 4 and w not in STOPWORDS:
            out.add(w)
    return sorted(out)


def doc_frequency(records: list[tuple[Path, str]]) -> dict[str, float]:
    """Fraction of this world's record files each lowercase word appears in.

    A token the whole world shares is not evidence that a particular work was
    opened. On Alexandria, the author slug `peter_alexandria` yields the token
    `alexandria`, which appears in every one of 192 records - so without this
    filter every assigned work matched and the diff reported a perfect score for
    a world with a dozen genuinely unopened works. Tokens above DF_CEILING are
    discarded as non-distinctive.
    """
    n = max(len(records), 1)
    counts: dict[str, int] = {}
    for _, text in records:
        for w in set(re.findall(r"[a-z][a-z'\u2019]+", text.lower())):
            counts[w] = counts.get(w, 0) + 1
    return {w: c / n for w, c in counts.items()}


def filename_only(text: str, token: str, source_file: str) -> bool:
    """True if every occurrence of `token` sits inside a vendored-filename string.

    Guards the exact false positive that fooled a human reviewer on Alexandria:
    `peter` matching `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml`
    inside an `edition:` field, on lines that mention no Peter at all.
    """
    filenames = set(re.findall(r"[A-Za-z0-9_.\-]+\.(?:xml|txt)", text))
    filenames.add(source_file)
    for line in text.splitlines():
        low = line.lower()
        if token not in low:
            continue
        stripped = low
        for fn in filenames:
            stripped = stripped.replace(fn.lower(), " ")
        if token in stripped:
            return False  # a real, non-filename mention exists
    return True


def diff_world(stem: str, key: str, assigned_only: bool) -> dict | None:
    map_path = CORPUS_MAP / f"{stem}.yaml"
    world_dir = RECORDS / key
    if not map_path.exists() or not world_dir.is_dir():
        return None

    rows = load_rows(map_path)
    records = load_records(world_dir)
    blob = "\n".join(text for _, text in records).lower()
    freq = doc_frequency(records)

    cited_files = set(re.findall(r"[A-Za-z0-9_.\-]+\.(?:xml|txt)", blob))

    findings: list[dict] = []
    for row in rows:
        conf = str(row.get("confidence") or "").strip().lower()
        if assigned_only and conf != "assigned":
            continue
        source_file = str(row.get("source_file") or "").strip()
        if not source_file:
            continue

        volume_opened = source_file.lower() in cited_files
        # AUTHOR is the load-bearing signal; title words only corroborate.
        auth = [t for t in author_tokens(row) if freq.get(t, 0.0) <= DF_CEILING]
        auth_common = [t for t in author_tokens(row) if t not in auth]
        auth_hits = [t for t in auth if t in blob]
        strong = [t for t in auth_hits if not filename_only(blob, t, source_file)]

        tit = [t for t in title_tokens(row) if freq.get(t, 0.0) <= DF_CEILING]
        tit_strong = [t for t in tit if t in blob and not filename_only(blob, t, source_file)]

        if not auth:
            status = "INDETERMINATE"      # author name too common to test with
        elif not strong:
            status = "AUTHOR-ABSENT"      # <-- the hard finding: nobody wrote this author down
        elif not volume_opened:
            status = "VOLUME-UNOPENED"    # author present via some other volume
        elif tit_strong:
            status = "OPENED"
        else:
            status = "WORK-UNCONFIRMED"   # right author present; this work not evidenced

        findings.append({
            "work": str(row.get("work") or "")[:100],
            "author": row.get("author"),
            "locus": row.get("locus"),
            "confidence": conf,
            "source_file": source_file,
            "status": status,
            "author_tokens_matched": strong,
            "author_tokens_filename_only": [t for t in auth_hits if t not in strong],
            "title_tokens_matched": tit_strong,
            "ignored_common_tokens": auth_common,
        })

    counts: dict[str, int] = {}
    for f in findings:
        counts[f["status"]] = counts.get(f["status"], 0) + 1
    return {
        "world": key,
        "corpus_map": f"{stem}.yaml",
        "records_dir": f"records/{key}",
        "record_files": len(records),
        "rows_examined": len(findings),
        "counts": counts,
        "findings": findings,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--world", help="records key, e.g. alx. Default: every mapped world.")
    ap.add_argument("--assigned-only", action="store_true",
                    help="Only rows at confidence: assigned (skip provisional).")
    ap.add_argument("--json", metavar="PATH", help="Also write the full report as JSON.")
    args = ap.parse_args()

    targets = {s: k for s, k in WORLD_MAP.items() if not args.world or k == args.world}
    if not targets:
        print(f"No mapped world for {args.world!r}. Known: {sorted(WORLD_MAP.values())}", file=sys.stderr)
        return 2

    reports = []
    for stem, key in sorted(targets.items(), key=lambda kv: kv[1]):
        rep = diff_world(stem, key, args.assigned_only)
        if rep:
            reports.append(rep)

    scope = "assigned only" if args.assigned_only else "assigned + provisional"
    print("=" * 78)
    print(f"WORK-GRANULARITY COVERAGE DIFF  ({scope})")
    print("Triage, not adjudication - an AUTHOR-ABSENT row is a question, not a defect.")
    print("=" * 78)

    for rep in reports:
        c = rep["counts"]
        print(f"\n### {rep['world']}  ({rep['corpus_map']} -> {rep['records_dir']}, "
              f"{rep['record_files']} records)")
        print(f"    rows examined: {rep['rows_examined']}   "
              + "   ".join(f"{k}: {v}" for k, v in sorted(c.items())))
        for status in ("AUTHOR-ABSENT", "VOLUME-UNOPENED", "WORK-UNCONFIRMED", "INDETERMINATE"):
            rows = [f for f in rep["findings"] if f["status"] == status]
            if not rows:
                continue
            print(f"\n    -- {status} ({len(rows)}) " + "-" * (50 - len(status)))
            for f in rows:
                flag = "!" if f["confidence"] == "assigned" else " "
                print(f"    {flag} [{f['confidence']:<11}] {f['author'] or '?':<24} {f['work']}")
                print(f"        {f['source_file']}  locus: {str(f['locus'])[:60]}")
                if f["author_tokens_filename_only"]:
                    print(f"        (author token(s) {f['author_tokens_filename_only']} appear ONLY inside filenames)")

    print("\n" + "=" * 78)
    print("FLEET TOTALS")
    for rep in reports:
        c = rep["counts"]
        absent_assigned = sum(
            1 for f in rep["findings"]
            if f["status"] == "AUTHOR-ABSENT" and f["confidence"] == "assigned"
        )
        print(f"  {rep['world']:<12} opened {c.get('OPENED', 0):>3}   "
              f"AUTHOR-ABSENT {c.get('AUTHOR-ABSENT', 0):>3} (assigned: {absent_assigned:>2})   "
              f"work-unconfirmed {c.get('WORK-UNCONFIRMED', 0):>3}   "
              f"vol-unopened {c.get('VOLUME-UNOPENED', 0):>3}")
    print("=" * 78)
    print("'!' marks confidence: assigned - the world's own map says it belongs here.")

    if args.json:
        Path(args.json).write_text(json.dumps(reports, indent=2), encoding="utf-8")
        print(f"\nFull report written to {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
