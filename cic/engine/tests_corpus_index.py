"""Tests for corpus_index.search()'s scoping fix. Run:
python cic/engine/tests_corpus_index.py

Same check()/results/sys.exit() convention as tests_corpus_map.py and
tests_corpus_structure.py in this same directory. Builds a real, throwaway
INDEX.sqlite from the real corpus (cheap - a couple of seconds, ~220
files) rather than a synthetic fixture DB, so the regression case is
reproduced against the real bug, not an invented shape.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_index as ci


def check(label, ok):
    print(f"  {'OK ' if ok else '***'} {label}")
    return ok


results = []

with tempfile.TemporaryDirectory() as tmp:
    db_path = Path(tmp) / "test-index.sqlite"
    ci.build(db_path=db_path)

    # --- the real regression: "chalice" --entry <hussite bucket> ----------
    # Scoping must happen inside the query: this entry's own texts rank
    # below other worlds' texts for "chalice", so a fleet-wide capped fetch
    # filtered afterwards would return nothing at the default limit.
    entry = "the-hussite-and-bohemian-brethren-movement"
    default_limit_hits = ci.search("chalice", entry=entry, limit=10, db_path=db_path)
    results.append(check(
        "\"chalice\" --entry hussite returns real hits at the DEFAULT limit (10), not \"no matches\"",
        len(default_limit_hits) > 0))
    results.append(check(
        "lutzow_hussite-wars_1914.txt (13 real occurrences) is among those default-limit hits",
        any(h["file"] == "lutzow_hussite-wars_1914.txt" for h in default_limit_hits)))
    results.append(check(
        "every returned hit is actually inside the requested entry's own file set",
        {h["file"] for h in default_limit_hits} <= ci.files_for_entry(entry)))

    # --- scoping never returns MORE than the real corpus-map bucket holds --
    huge_limit_hits = ci.search("chalice", entry=entry, limit=200, db_path=db_path)
    results.append(check(
        "raising --limit doesn't surface files outside the entry's own bucket either",
        {h["file"] for h in huge_limit_hits} <= ci.files_for_entry(entry)))

    # --- unscoped search is unchanged: no entry filter, plain fleet-wide ---
    unscoped_hits = ci.search("chalice", entry=None, limit=10, db_path=db_path)
    results.append(check(
        "unscoped search still returns hits (fleet-wide, not entry-narrowed)",
        len(unscoped_hits) > 0))
    results.append(check(
        "unscoped search can surface files OUTSIDE the hussite bucket (proves no scope leaked in)",
        not ({h["file"] for h in unscoped_hits} <= ci.files_for_entry(entry))))
    results.append(check(
        "unscoped search never returns more than the requested limit",
        len(unscoped_hits) <= 10))

    # --- a bucket that exists but has nothing assigned: no matches, no crash
    real_map_dir = ci.MAP_DIR
    empty_map_dir = Path(tmp) / "empty-map"
    empty_map_dir.mkdir()
    (empty_map_dir / "empty-entry.yaml").write_text("works: []\n", encoding="utf-8")
    ci.MAP_DIR = empty_map_dir
    try:
        empty_scope_hits = ci.search("chalice", entry="empty-entry", limit=10, db_path=db_path)
    finally:
        ci.MAP_DIR = real_map_dir
    results.append(check("a real bucket with nothing assigned yet returns [] with no exception",
                         empty_scope_hits == []))

    # --- an entry with no corpus-map bucket at all still raises cleanly ---
    raised = False
    try:
        ci.search("chalice", entry="not-a-real-entry-id", limit=10, db_path=db_path)
    except SystemExit:
        raised = True
    results.append(check("an unknown --entry still raises SystemExit, not a silent empty result",
                         raised))

print("\nall passed" if all(results) else "\nFAILURES")
sys.exit(0 if all(results) else 1)
