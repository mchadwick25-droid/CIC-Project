#!/usr/bin/env python3
"""coverage_search.py - read-only topic-coverage probe for the CiC repo.

For a list of search terms, report per world what the records already hold
and what the vendored texts mapped to that world hold, classified as the
earlier hand-run probe did:

  QUOTE       a quote record matched on text / modern_rendering /
              retrieval.retrieve_when
  WITNESS     a doctrinal_witness, term, gravity, force, story or
              demonstration record matched
  ABSENCE     an honest_limit, contested_claim, or source(kind: absence)
              record matched
  SOURCE_ONLY no record matched, but vendored texts mapped to the world did
  NOTHING     no record and no vendored-text match

Class strength: QUOTE > WITNESS > ABSENCE > SOURCE_ONLY > NOTHING.
Standard library + PyYAML. No network, no model calls, nothing written
except the optional --json file. canon/sealed_probes/ is never read.
"""
import argparse
import json
import os
import re
import sys
import time

import yaml

CLASS_ORDER = ["QUOTE", "WITNESS", "ABSENCE", "SOURCE_ONLY", "NOTHING"]
CLASS_RANK = {c: i for i, c in enumerate(CLASS_ORDER)}

# record_type -> (class, fields searched). Dotted paths descend into dicts;
# lists are searched element-wise; demonstration.exchange is a list of
# {speaker, text} and is handled by the generic walker as well.
TYPE_FIELDS = {
    "quote": ("QUOTE", ["text", "modern_rendering", "retrieval.retrieve_when"]),
    "doctrinal_witness": ("WITNESS", ["text", "positions", "tensions",
                                      "retrieval.retrieve_when", "use_note.means"]),
    "term": ("WITNESS", ["plain_meaning", "world_word", "quick_meaning", "senses",
                         "false_friend", "retrieval.retrieve_when", "use_note.means"]),
    "gravity": ("WITNESS", ["name", "description", "manifestations",
                            "retrieval.retrieve_when", "use_note.means"]),
    "force": ("WITNESS", ["name", "description", "manifestations",
                          "retrieval.retrieve_when", "use_note.means"]),
    "story": ("WITNESS", ["tellable_as", "text", "telling", "absent_detail",
                          "retrieval.retrieve_when", "use_note.means"]),
    "demonstration": ("WITNESS", ["exchange", "tags", "canon_question_id",
                                  "retrieval.retrieve_when", "use_note.means"]),
    "honest_limit": ("ABSENCE", ["statement", "why_sources_cannot_answer",
                                 "retrieval.retrieve_when", "use_note.means"]),
    "contested_claim": ("ABSENCE", ["claim", "concedes", "held_against",
                                    "retrieval.retrieve_when", "use_note.means"]),
    # source records count only when kind == absence (checked in classify_record)
    "source": ("ABSENCE", ["work", "citation", "absence_probes"]),
}
WITNESS_TYPES = [t for t, (c, _) in TYPE_FIELDS.items() if c == "WITNESS"]
ABSENCE_TYPES = [t for t, (c, _) in TYPE_FIELDS.items() if c == "ABSENCE"]

FRONT_RE = re.compile(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.S)


# ----------------------------------------------------------------- helpers

def build_pattern(terms, use_regex, whole_words):
    parts = []
    for t in terms:
        t = t.strip()
        if not t:
            continue
        p = t if use_regex else re.escape(t)
        if whole_words:
            p = r"\b(?:%s)\b" % p
        parts.append("(?:%s)" % p)
    if not parts:
        sys.exit("no search terms given")
    return re.compile("|".join(parts), re.I)


def get_path(d, dotted):
    cur = d
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur


def iter_strings(value):
    """Yield every string nested inside value (str / list / dict)."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for v in value:
            yield from iter_strings(v)
    elif isinstance(value, dict):
        for v in value.values():
            yield from iter_strings(v)


def snippet(text, m, width):
    """A window of `width` chars around match m, whitespace collapsed."""
    text = text.replace("\n", " ")
    start, end = m.start(), m.end()
    half = max(0, (width - (end - start)) // 2)
    a = max(0, start - half)
    b = min(len(text), a + width)
    a = max(0, b - width)
    s = text[a:b]
    s = re.sub(r"\s+", " ", s).strip()
    if a > 0:
        s = "..." + s
    if b < len(text):
        s = s + "..."
    return s


def load_yaml_file(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


# ------------------------------------------------------------------ worlds

def load_worlds(repo, only_codes):
    wdir = os.path.join(repo, "records", "worlds")
    worlds = []
    for fn in sorted(os.listdir(wdir)):
        if not fn.endswith(".yaml"):
            continue
        code = fn[:-5]
        if only_codes and code not in only_codes:
            continue
        data = load_yaml_file(os.path.join(wdir, fn)) or {}
        worlds.append({
            "code": code,
            "display_name": data.get("display_name", code),
            "world_id": data.get("world_id"),
            "census_id": data.get("census_id"),
            "state": data.get("state"),
        })
    if only_codes:
        missing = sorted(set(only_codes) - {w["code"] for w in worlds})
        if missing:
            print("warning: unknown world code(s): %s" % ", ".join(missing), file=sys.stderr)
    return worlds


def corpus_map_path(repo, world):
    """records/worlds/<code>.yaml joins cic/corpus-map/ by world_id, else census_id."""
    for key in ("world_id", "census_id"):
        wid = world.get(key)
        if wid:
            p = os.path.join(repo, "cic", "corpus-map", wid + ".yaml")
            if os.path.exists(p):
                return p, key
    return None, None


def mapped_source_files(repo, world):
    path, via = corpus_map_path(repo, world)
    if not path:
        return None, None, []
    data = load_yaml_file(path) or {}
    files = []
    seen = set()
    for row in data.get("works", []) or []:
        sf = row.get("source_file")
        if sf and sf not in seen:
            seen.add(sf)
            files.append(sf)
    return os.path.relpath(path, repo), via, files


# ----------------------------------------------------------------- records

def classify_record(front, pattern, snip_width):
    """Return (class, [hits]) or (None, []) for a parsed front matter dict."""
    rtype = front.get("record_type")
    if rtype not in TYPE_FIELDS:
        return None, []
    cls, fields = TYPE_FIELDS[rtype]
    if rtype == "source" and front.get("kind") != "absence":
        return None, []
    hits = []
    for field in fields:
        value = get_path(front, field)
        if value is None:
            continue
        for s in iter_strings(value):
            m = pattern.search(s)
            if m:
                hits.append({"field": field, "term": m.group(0),
                             "snippet": snippet(s, m, snip_width)})
                break  # one hit per field is enough
    if not hits:
        return None, []
    return cls, hits


def scan_records(repo, code, pattern, snip_width):
    base = os.path.join(repo, "records", code)
    results = {"QUOTE": [], "WITNESS": [], "ABSENCE": []}
    parse_errors = []
    if not os.path.isdir(base):
        return results, parse_errors, 0
    n_files = 0
    for rtype in sorted(os.listdir(base)):
        tdir = os.path.join(base, rtype)
        if not os.path.isdir(tdir):
            continue
        for fn in sorted(os.listdir(tdir)):
            if not fn.endswith(".md"):
                continue
            n_files += 1
            path = os.path.join(tdir, fn)
            with open(path, encoding="utf-8", errors="replace") as fh:
                raw = fh.read()
            m = FRONT_RE.match(raw)
            if not m:
                parse_errors.append({"path": os.path.relpath(path, repo), "error": "no front matter"})
                continue
            try:
                front = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError as e:
                parse_errors.append({"path": os.path.relpath(path, repo),
                                     "error": str(e).splitlines()[0][:120]})
                continue
            if not isinstance(front, dict):
                continue
            cls, hits = classify_record(front, pattern, snip_width)
            if cls is None:
                continue
            results[cls].append({
                "id": front.get("id", fn[:-3]),
                "record_type": front.get("record_type"),
                "status": front.get("status"),
                "formation_confidence": (front.get("confidence") or {}).get("formation_confidence"),
                "hits": hits,
            })
    return results, parse_errors, n_files


# ----------------------------------------------------------------- sources

class SourceScanner:
    """Scans each vendored file once (files are shared across worlds)."""

    def __init__(self, repo, pattern, line_width):
        self.repo = repo
        self.pattern = pattern
        self.line_width = line_width
        self.cache = {}
        self.bytes_read = 0

    def scan(self, source_file):
        if source_file in self.cache:
            return self.cache[source_file]
        path = os.path.join(self.repo, "cic", "texts", source_file)
        res = {"file": source_file, "n_hits": 0, "n_lines": 0, "first": None,
               "terms": {}}
        if not os.path.isfile(path):
            res["error"] = "missing"
            self.cache[source_file] = res
            return res
        with open(path, encoding="utf-8", errors="replace", newline="") as fh:
            text = fh.read()
        self.bytes_read += len(text)
        line_no = 1
        pos = 0
        last_line = -1
        for m in self.pattern.finditer(text):
            line_no += text.count("\n", pos, m.start())
            pos = m.start()
            res["n_hits"] += 1
            term = m.group(0).lower()
            res["terms"][term] = res["terms"].get(term, 0) + 1
            if line_no != last_line:
                res["n_lines"] += 1
                last_line = line_no
            if res["first"] is None:
                ls = text.rfind("\n", 0, m.start()) + 1
                le = text.find("\n", m.end())
                if le == -1:
                    le = len(text)
                line = text[ls:le].rstrip("\r")
                # re-anchor the match inside the line for the window
                lm = self.pattern.search(line)
                res["first"] = {"line": line_no,
                                "text": snippet(line, lm, self.line_width) if lm else line[:self.line_width]}
        self.cache[source_file] = res
        return res


# -------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True, help="path to the CIC-Project checkout")
    ap.add_argument("--terms", required=True,
                    help="comma-separated search terms (quote the whole list)")
    ap.add_argument("--regex", action="store_true", help="treat each term as a regular expression")
    ap.add_argument("--whole-words", action="store_true",
                    help="wrap each term in word boundaries (hell will not match shell/Hellenic)")
    ap.add_argument("--worlds", default="", help="comma-separated world codes (default: all)")
    ap.add_argument("--max-source-hits", type=int, default=3, help="top N vendored files per world")
    ap.add_argument("--max-records", type=int, default=0,
                    help="cap record lines printed per type per world (0 = all)")
    ap.add_argument("--json", dest="json_out", default="", help="write full results to this JSON file")
    ap.add_argument("--no-sources", action="store_true", help="skip the vendored-text scan")
    args = ap.parse_args()

    repo = os.path.abspath(args.repo)
    terms = [t.strip() for t in args.terms.split(",") if t.strip()]
    pattern = build_pattern(terms, args.regex, args.whole_words)
    only = {c.strip() for c in args.worlds.split(",") if c.strip()} or None

    t0 = time.time()
    worlds = load_worlds(repo, only)
    scanner = SourceScanner(repo, pattern, 160)
    report = []

    for w in worlds:
        code = w["code"]
        recs, perr, n_rec_files = scan_records(repo, code, pattern, 120)
        map_path, via, files = mapped_source_files(repo, w)
        src_hits = []
        if not args.no_sources:
            for sf in files:
                r = scanner.scan(sf)
                if r["n_hits"]:
                    src_hits.append(r)
            src_hits.sort(key=lambda r: (-r["n_hits"], r["file"]))

        if recs["QUOTE"]:
            cls = "QUOTE"
        elif recs["WITNESS"]:
            cls = "WITNESS"
        elif recs["ABSENCE"]:
            cls = "ABSENCE"
        elif src_hits:
            cls = "SOURCE_ONLY"
        else:
            cls = "NOTHING"
        secondary = [c for c in ("QUOTE", "WITNESS", "ABSENCE") if recs[c] and c != cls]
        if src_hits and cls != "SOURCE_ONLY":
            secondary.append("SOURCE")

        entry = {
            "code": code,
            "display_name": w["display_name"],
            "state": w["state"],
            "class": cls,
            "also": secondary,
            "n_record_files": n_rec_files,
            "corpus_map": map_path,
            "corpus_map_join": via,
            "n_mapped_files": len(files),
            "n_source_files_hit": len(src_hits),
            "records": recs,
            "sources": src_hits[: args.max_source_hits] if args.max_source_hits else src_hits,
            "sources_all": [{"file": r["file"], "n_hits": r["n_hits"], "n_lines": r["n_lines"]} for r in src_hits],
            "record_parse_errors": perr,
        }
        report.append(entry)
        print_world(entry, args.max_records)

    elapsed = time.time() - t0
    print_summary(report)
    print("\nterms: %s%s%s" % (", ".join(terms), " [regex]" if args.regex else "",
                               " [whole words]" if args.whole_words else ""))
    print("worlds: %d   vendored files scanned: %d (%.0f MB)   time: %.1fs" % (
        len(report), len(scanner.cache), scanner.bytes_read / 1e6, elapsed))

    if args.json_out:
        out = {
            "repo": repo,
            "terms": terms,
            "regex": args.regex,
            "whole_words": args.whole_words,
            "elapsed_seconds": round(elapsed, 2),
            "class_order": CLASS_ORDER,
            "worlds": report,
        }
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=1, ensure_ascii=False)
        print("json: %s" % args.json_out)


def print_world(e, max_records):
    print("=" * 78)
    also = ("  (also: %s)" % ", ".join(e["also"])) if e["also"] else ""
    print("%s  %s  ->  %s%s" % (e["code"], e["display_name"], e["class"], also))
    print("  records: %d files; corpus map: %s (%d files)" % (
        e["n_record_files"], e["corpus_map"] or "none", e["n_mapped_files"]))
    for cls in ("QUOTE", "WITNESS", "ABSENCE"):
        rows = e["records"][cls]
        if not rows:
            continue
        print("  [%s] %d record(s)" % (cls, len(rows)))
        by_type = {}
        for r in rows:
            by_type.setdefault(r["record_type"], []).append(r)
        for rtype in sorted(by_type):
            print("    %s:" % rtype)
            shown = by_type[rtype][:max_records] if max_records else by_type[rtype]
            for r in shown:
                h = r["hits"][0]
                print("      %s  [%s]" % (r["id"], r["formation_confidence"] or "-"))
                print("        %s: %s" % (h["field"], h["snippet"]))
                for extra in r["hits"][1:]:
                    print("        %s: %s" % (extra["field"], extra["snippet"]))
            if max_records and len(by_type[rtype]) > max_records:
                print("      ... %d more" % (len(by_type[rtype]) - max_records))
    if e["sources"]:
        print("  [SOURCES] %d of %d mapped files hit; top %d:" % (
            e["n_source_files_hit"], e["n_mapped_files"], len(e["sources"])))
        for s in e["sources"]:
            print("    %s  (%d hits, %d lines)" % (s["file"], s["n_hits"], s["n_lines"]))
            if s["first"]:
                print("      L%d: %s" % (s["first"]["line"], s["first"]["text"]))
    elif e["n_mapped_files"]:
        print("  [SOURCES] no hits in %d mapped files" % e["n_mapped_files"])
    if e["record_parse_errors"]:
        print("  [WARN] %d record(s) failed to parse" % len(e["record_parse_errors"]))


def print_summary(report):
    print("\n" + "=" * 78)
    hdr = "%-13s | %-11s | %7s | %9s | %9s | %14s" % (
        "world", "class", "n_quote", "n_witness", "n_absence", "n_source_files")
    print(hdr)
    print("-" * len(hdr))
    for e in report:
        print("%-13s | %-11s | %7d | %9d | %9d | %14d" % (
            e["code"], e["class"], len(e["records"]["QUOTE"]), len(e["records"]["WITNESS"]),
            len(e["records"]["ABSENCE"]), e["n_source_files_hit"]))


if __name__ == "__main__":
    main()
