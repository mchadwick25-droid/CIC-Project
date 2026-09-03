#!/usr/bin/env python3
"""Discovery helper — D2 from the source-infrastructure blueprint (2026-09-02).

WHAT THIS IS. A candidate finder, not an acquirer. Give it a want (author,
title, an optional year window) and it queries the discovery surfaces the
blueprint's research verified — Internet Archive, Google Books, Open
Library, and (offline, from a local dump) Hathifiles and Project
Gutenberg's own catalog — and prints what each one has, with that host's
own public-domain signal. It never fetches a text body and never writes
`download-queue-seed.yaml` for you: it prints a ready-to-paste stub with
`rights_basis` and `verified_by` left blank, because a discovery hit is a
lead, not a verification. Filling those two fields is a human confirming
the specific URL actually carries the specific edition, the same standard
`download-queue-seed.yaml`'s own header sets for every other row.

WHERE THIS RUNS. Build threads never run this — same rule as everything
else in `world-build-docs/_cross-world/` that reaches outside `records/`.
Most of the hosts below are blocked from an agent sandbox but not from
Mark's machine or a research thread with real network; each network call
below fails soft (prints "unreachable here", keeps going) specifically so
the script is honest about *why* a source came back empty rather than
pretending a blocked host means "nothing found."

OFFLINE SOURCES NEED A LOCAL DUMP. Hathifiles (a monthly TSV, no header
row, ~30M rows) and Gutenberg's `pg_catalog.csv` are bulk downloads, not
per-query APIs — see the blueprint §3.1 for both URLs. Point `--hathifiles`
/ `--gutenberg-csv` at a local copy; omitted, those two sources are simply
skipped (not an error — a want with no offline dump yet still gets the
three live sources).

Usage:
  python world-build-docs/_cross-world/discovery_helper.py \\
      --title "Vita Antonii" --author "Athanasius" --year-to 1930 \\
      --world desert --hathifiles ~/data/hathi_full_20260901.txt

  python world-build-docs/_cross-world/discovery_helper.py \\
      --title "Ammianus Marcellinus" --author Ammianus --limit 3
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

# Hathifiles ship as a headerless TSV; this is the field order HathiTrust
# documents for the monthly full dump (see the blueprint's own citation).
# If a real dump's columns don't line up with these labels, the row still
# prints - just mislabeled - so the mismatch is visible immediately rather
# than silently misreading rights codes.
_HATHI_FIELDS = [
    "htid", "access", "rights", "ht_bib_key", "description", "source",
    "source_bib_num", "oclc_num", "isbn", "issn", "lccn", "title",
    "imprint", "rights_reason_code", "rights_timestamp", "us_gov_doc_flag",
    "rights_date_used", "pub_place", "lang", "bib_fmt", "collection_code",
    "content_provider_code", "responsible_entity_code",
    "digitization_agent_code", "access_profile_code", "author",
]

_TIMEOUT = 15
_USER_AGENT = "cic-discovery-helper/1 (church-in-conversation project; discovery only, no bulk fetch)"


@dataclass
class Candidate:
    source: str
    title: str
    author: str
    year: str
    pd_flag: str
    url: str
    note: str = ""


@dataclass
class SourceResult:
    source: str
    hits: list[Candidate] = field(default_factory=list)
    problem: str = ""   # non-empty means "didn't run" - unreachable, no dump given, etc.


def _get_json(url: str) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _contains(haystack: str, needle: str) -> bool:
    return needle.lower().strip() in (haystack or "").lower()


# --- Live sources ------------------------------------------------------

def search_internet_archive(author: str, title: str, year_from: int | None,
                              year_to: int | None, limit: int) -> SourceResult:
    q_parts = []
    if title:
        q_parts.append(f'title:("{title}")')
    if author:
        q_parts.append(f'creator:("{author}")')
    if year_from or year_to:
        q_parts.append(f"year:[{year_from or 1000} TO {year_to or 2100}]")
    query = " AND ".join(q_parts) or "*"
    params = {
        "q": query,
        "fl[]": ["identifier", "title", "creator", "date", "possible-copyright-status"],
        "rows": str(limit),
        "output": "json",
    }
    url = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(params, doseq=True)
    try:
        data = _get_json(url)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return SourceResult("Internet Archive", problem=f"unreachable here ({exc})")
    docs = ((data or {}).get("response") or {}).get("docs") or []
    hits = [
        Candidate(
            source="Internet Archive",
            title=str(d.get("title", "")),
            author=str(d.get("creator", "")),
            year=str(d.get("date", ""))[:4],
            pd_flag=str(d.get("possible-copyright-status", "unstated")),
            url=f"https://archive.org/details/{d.get('identifier')}",
        )
        for d in docs
    ]
    return SourceResult("Internet Archive", hits=hits)


def search_google_books(author: str, title: str, limit: int) -> SourceResult:
    q_parts = []
    if title:
        q_parts.append(f"intitle:{title}")
    if author:
        q_parts.append(f"inauthor:{author}")
    params = {"q": " ".join(q_parts) or title or author, "maxResults": str(limit)}
    url = "https://www.googleapis.com/books/v1/volumes?" + urllib.parse.urlencode(params)
    try:
        data = _get_json(url)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return SourceResult("Google Books", problem=f"unreachable here ({exc})")
    if not data or "error" in data:
        msg = (data or {}).get("error", {}).get("message", "unknown error")
        return SourceResult("Google Books", problem=f"API error: {msg}")
    hits = []
    for item in data.get("items") or []:
        info = item.get("volumeInfo", {})
        access = item.get("accessInfo", {})
        pd = access.get("publicDomain")
        hits.append(Candidate(
            source="Google Books",
            title=str(info.get("title", "")),
            author=", ".join(info.get("authors") or []),
            year=str(info.get("publishedDate", ""))[:4],
            pd_flag=("public domain (US)" if pd else "not flagged public domain (US)")
                    + f", viewability={access.get('viewability', '?')}",
            url=info.get("infoLink") or item.get("selfLink", ""),
        ))
    return SourceResult("Google Books", hits=hits)


def search_open_library(author: str, title: str, limit: int) -> SourceResult:
    q = " ".join(p for p in (title, author) if p)
    params = {"q": q, "limit": str(limit)}
    url = "https://openlibrary.org/search.json?" + urllib.parse.urlencode(params)
    try:
        data = _get_json(url)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return SourceResult("Open Library", problem=f"unreachable here ({exc})")
    hits = []
    for d in (data or {}).get("docs") or []:
        hits.append(Candidate(
            source="Open Library",
            title=str(d.get("title", "")),
            author=", ".join(d.get("author_name") or []),
            year=str(d.get("first_publish_year", "")),
            pd_flag=f"has_fulltext={d.get('has_fulltext')}, public_scan={d.get('public_scan_b')}",
            url=f"https://openlibrary.org{d.get('key', '')}",
        ))
    return SourceResult("Open Library", hits=hits)


# --- Offline sources (need a local dump) --------------------------------

def search_hathifiles(path: str | None, author: str, title: str, limit: int) -> SourceResult:
    if not path:
        return SourceResult("Hathifiles", problem="no --hathifiles dump given, skipped")
    hits: list[Candidate] = []
    try:
        with open(path, encoding="utf-8", errors="replace", newline="") as fh:
            reader = csv.reader(fh, delimiter="\t")
            for row in reader:
                if len(row) < len(_HATHI_FIELDS):
                    continue
                rec = dict(zip(_HATHI_FIELDS, row))
                if title and not _contains(rec["title"], title):
                    continue
                if author and not _contains(rec["author"], author):
                    continue
                hits.append(Candidate(
                    source="Hathifiles",
                    title=rec["title"],
                    author=rec["author"],
                    year=rec["rights_date_used"],
                    pd_flag=f"rights={rec['rights']} ({rec['rights_reason_code']}), pub_place={rec['pub_place']}",
                    url=f"https://babel.hathitrust.org/cgi/pt?id={rec['htid']}",
                ))
                if len(hits) >= limit:
                    break
    except OSError as exc:
        return SourceResult("Hathifiles", problem=f"couldn't read {path}: {exc}")
    return SourceResult("Hathifiles", hits=hits)


def search_gutenberg_csv(path: str | None, author: str, title: str, limit: int) -> SourceResult:
    if not path:
        return SourceResult("Project Gutenberg", problem="no --gutenberg-csv dump given, skipped")
    hits: list[Candidate] = []
    try:
        with open(path, encoding="utf-8", errors="replace", newline="") as fh:
            for rec in csv.DictReader(fh):
                if rec.get("Type") != "Text":
                    continue
                if title and not _contains(rec.get("Title", ""), title):
                    continue
                if author and not _contains(rec.get("Authors", ""), author):
                    continue
                hits.append(Candidate(
                    source="Project Gutenberg",
                    title=rec.get("Title", ""),
                    author=rec.get("Authors", ""),
                    year=rec.get("Issued", ""),
                    pd_flag="cleared for US redistribution by PG's own process",
                    url=f"https://www.gutenberg.org/ebooks/{rec.get('Text#', '')}",
                ))
                if len(hits) >= limit:
                    break
    except OSError as exc:
        return SourceResult("Project Gutenberg", problem=f"couldn't read {path}: {exc}")
    return SourceResult("Project Gutenberg", hits=hits)


# --- Output --------------------------------------------------------------

def render(results: list[SourceResult], author: str, title: str, world: str) -> str:
    out = [f"# Discovery: {title!r} / {author!r}" + (f"  (world: {world})" if world else "")]
    total_hits = 0
    top: Candidate | None = None
    for r in results:
        out.append(f"\n## {r.source}")
        if r.problem:
            out.append(f"  ({r.problem})")
            continue
        if not r.hits:
            out.append("  no hits")
            continue
        for c in r.hits:
            total_hits += 1
            if top is None:
                top = c
            out.append(f"  - {c.title}  —  {c.author} ({c.year})")
            out.append(f"      pd flag : {c.pd_flag}")
            out.append(f"      url     : {c.url}")

    out.append(f"\n{total_hits} hit(s) across {len(results)} source(s).")

    if top:
        out.append(
            "\n--- paste-ready stub for download-queue-seed.yaml -----------------\n"
            "# UNVERIFIED - a discovery hit, not a verification. Confirm the url\n"
            "# actually carries this edition and settle rights_basis against\n"
            "# texts_registry.py's rights_clears() categories before adding this\n"
            "# for real; leave rights_basis/verified_by blank until you have.\n"
            f'  - title: "{title or top.title}"\n'
            f'    author: "{author or top.author}"\n'
            "    translator: null\n"
            f'    year: {top.year or "null"}\n'
            f'    world: {world or "TODO"}\n'
            f"    why: >\n      Found via discovery_helper.py ({top.source}), {top.pd_flag}.\n"
            f'      TODO: what gap this closes and for which record(s).\n'
            f'    url: "{top.url}"\n'
            "    rights_basis: null   # TODO - verify against the host, don't guess\n"
            "    verified_by: null    # TODO - who checked it, and when\n"
            "    status: not-yet-downloaded\n"
            "---------------------------------------------------------------------"
        )
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python world-build-docs/_cross-world/discovery_helper.py")
    parser.add_argument("--title", default="", help="work title (or fragment)")
    parser.add_argument("--author", default="", help="author name (or fragment)")
    parser.add_argument("--year-from", type=int, default=None)
    parser.add_argument("--year-to", type=int, default=None)
    parser.add_argument("--world", default="", help="which world's want this is (informational only)")
    parser.add_argument("--limit", type=int, default=5, help="max hits per source")
    parser.add_argument("--hathifiles", default=None, help="path to a local Hathifiles TSV dump")
    parser.add_argument("--gutenberg-csv", default=None, help="path to a local pg_catalog.csv")
    parser.add_argument("--sources", default="ia,google,ol,hathi,gutenberg",
                        help="comma-separated subset to run: ia,google,ol,hathi,gutenberg")
    args = parser.parse_args(argv)

    if not args.title and not args.author:
        parser.error("give at least --title or --author - an unbounded query helps no one")

    wanted = set(args.sources.split(","))
    results: list[SourceResult] = []
    if "ia" in wanted:
        results.append(search_internet_archive(args.author, args.title, args.year_from, args.year_to, args.limit))
    if "google" in wanted:
        results.append(search_google_books(args.author, args.title, args.limit))
    if "ol" in wanted:
        results.append(search_open_library(args.author, args.title, args.limit))
    if "hathi" in wanted:
        results.append(search_hathifiles(args.hathifiles, args.author, args.title, args.limit))
    if "gutenberg" in wanted:
        results.append(search_gutenberg_csv(args.gutenberg_csv, args.author, args.title, args.limit))

    print(render(results, args.author, args.title, args.world))
    return 0


if __name__ == "__main__":
    sys.exit(main())
