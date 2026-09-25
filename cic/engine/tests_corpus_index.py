"""Tests for corpus_index.search()'s scoping fix, and for passage_units()'s
plain-text heading/paragraph split. Run:
python cic/engine/tests_corpus_index.py

Same check()/results/sys.exit() convention as tests_corpus_map.py and
tests_corpus_structure.py in this same directory. Builds a real, throwaway
INDEX.sqlite from the real corpus (cheap - a couple of seconds, ~220
files) rather than a synthetic fixture DB, so the regression case is
reproduced against the real bug, not an invented shape.
"""
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_index as ci
import corpus_structure as cs


def check(label, ok):
    print(f"  {'OK ' if ok else '***'} {label}")
    return ok


def _no_text_lost(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = cs._strip_tags_if_markup(path, raw)
    units = ci.passage_units(path)
    reassembled = re.sub(r"\s+", " ", " ".join(u["text"] for u in units)).strip()
    return reassembled == re.sub(r"\s+", " ", text).strip()


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

# ============================================================================
# passage_units() plain-text heading/paragraph split (Mark's ruling "a",
# 2026-09-25: split on headings, fall back to paragraphs). Synthetic
# fixtures for shape and correctness; the real-corpus block below proves it
# on the volumes the ruling named plus a no-text-lost sweep of the whole
# library.
# ============================================================================

with tempfile.TemporaryDirectory() as tmp:
    tmp_dir = Path(tmp)

    # --- heading split: real division lines become their own units --------
    heading_fixture = tmp_dir / "heading-fixture.txt"
    heading_fixture.write_text(
        "Title: A Fixture Book\n"
        "Creator: Nobody\n"
        "\n"
        "LETTER I.    TO THE FIRST RECIPIENT\n"
        "\n"
        "The first letter's own body text, several words long.\n"
        "\n"
        "LETTER II.    TO THE SECOND RECIPIENT\n"
        "\n"
        "The second letter's own body text, on its own line.\n",
        encoding="utf-8",
    )
    heading_units = ci.passage_units(heading_fixture)
    results.append(check("a heading-structured fixture splits into one preamble unit plus one per heading",
                         len(heading_units) == 3))
    results.append(check("the preamble unit (before the first heading) is untitled and carries the header block",
                         heading_units[0]["title"] == "" and "A Fixture Book" in heading_units[0]["text"]))
    results.append(check("the first heading unit's title is the heading line itself",
                         heading_units[1]["title"] == "LETTER I.    TO THE FIRST RECIPIENT"))
    results.append(check("the first heading unit's own text includes both the heading words and its body",
                         "LETTER I" in heading_units[1]["text"] and "first letter's own body" in heading_units[1]["text"]))
    results.append(check("the second heading unit runs to end of file and doesn't bleed into the first",
                         "second letter's own body" in heading_units[2]["text"]
                         and "first letter's own body" not in heading_units[2]["text"]))
    results.append(check("locus is line<N>, the real 1-based line the unit's own heading (or file start) sits on",
                         heading_units[0]["locus"] == "line1"
                         and heading_units[1]["locus"] == "line4"
                         and heading_units[2]["locus"] == "line8"))
    results.append(check("no text lost against the heading fixture",
                         _no_text_lost(heading_fixture)))

    # --- a file with no headings at all falls back to one unit per paragraph
    paragraph_fixture = tmp_dir / "paragraph-fixture.txt"
    paragraph_fixture.write_text(
        "First paragraph, several\nwords across two lines.\n"
        "\n"
        "Second paragraph, a single line.\n"
        "\n"
        "\n"
        "Third paragraph, after two blank lines in a row.\n",
        encoding="utf-8",
    )
    paragraph_units = ci.passage_units(paragraph_fixture)
    results.append(check("a heading-free fixture falls back to one unit per paragraph, not one whole-file blob",
                         len(paragraph_units) == 3))
    results.append(check("a two-line paragraph is reassembled as one unit, whitespace-normalized",
                         paragraph_units[0]["text"] == "First paragraph, several words across two lines."))
    results.append(check("paragraph units carry no title (a paragraph names nothing the way a heading does)",
                         all(u["title"] == "" for u in paragraph_units)))
    results.append(check("paragraph loci are the real 1-based line each paragraph starts on",
                         [u["locus"] for u in paragraph_units] == ["line1", "line4", "line7"]))
    results.append(check("no text lost against the paragraph fixture",
                         _no_text_lost(paragraph_fixture)))

    # --- a running header/footer is filtered out, not treated as a heading -
    running_header_fixture = tmp_dir / "running-header-fixture.txt"
    page_body = "\n\n".join(f"Body text for page {n}, unique content." for n in range(1, 6))
    running_header_fixture.write_text(
        "REAL CHAPTER HEADING\n\n"
        + "\n\nA RUNNING TITLE\n\n".join(f"Body text for page {n}, unique content." for n in range(1, 6))
        + "\n",
        encoding="utf-8",
    )
    running_units = ci.passage_units(running_header_fixture)
    results.append(check("a short all-caps line repeated across most of a file is filtered as a running header, "
                         "not split into its own unit each time",
                         len(running_units) == 1))
    results.append(check("the filtered running header's own words stay in the surrounding unit's text "
                         "(filtered from being a boundary, not deleted)",
                         "A RUNNING TITLE" in running_units[0]["text"]))
    results.append(check("no text lost against the running-header fixture",
                         _no_text_lost(running_header_fixture)))

    # --- a running header that carries a different page number each time --
    # (verso/recto convention: CCEL/archive.org scans often print a running
    # title with a page number appended or prepended, differing page to
    # page) still collapses to one dedup key and gets filtered the same way.
    numbered_header_fixture = tmp_dir / "numbered-header-fixture.txt"
    body_pieces = []
    for n in range(1, 6):
        body_pieces.append(f"RUNNING TITLE {n}")
        body_pieces.append(f"Body text for page {n}, unique content.")
    numbered_header_fixture.write_text(
        "REAL CHAPTER HEADING\n\n" + "\n\n".join(body_pieces) + "\n",
        encoding="utf-8",
    )
    numbered_units = ci.passage_units(numbered_header_fixture)
    results.append(check("a running header with a different trailing page number each time still "
                         "collapses to one dedup key and gets filtered",
                         len(numbered_units) == 1))
    results.append(check("no text lost against the numbered running-header fixture",
                         _no_text_lost(numbered_header_fixture)))

    # --- an apparatus-classified heading is still flagged apparatus --------
    apparatus_fixture = tmp_dir / "apparatus-fixture.txt"
    apparatus_fixture.write_text(
        "PREFACE\n\nSome prefatory remarks.\n\n"
        "CHAPTER ONE\n\nThe real body text begins here.\n",
        encoding="utf-8",
    )
    apparatus_units = ci.passage_units(apparatus_fixture)
    results.append(check("a heading matching the apparatus vocabulary (PREFACE) is flagged apparatus",
                         apparatus_units[0]["apparatus"] is True))
    results.append(check("a heading that doesn't match the apparatus vocabulary is not flagged",
                         apparatus_units[1]["apparatus"] is False))

# --- the real volumes Mark's ruling named, plus a fleet-wide no-text-lost
# sweep. Confirms the split actually fires (not silently falling back to
# paragraphs) on the named samples and that nothing in the whole library
# loses a character either way.
_named_samples = [
    "van-braght_martyrs-mirror_sohm1886.txt",       # Martyrs Mirror
    "foxe_acts-and-monuments-v3_cattley-townsend1837.txt",  # Foxe
    "council-of-trent_canons-and-decrees_waterworth1848.txt",  # Waterworth's Trent
    "hus_letters_workman-pope1904.txt",             # Hus's Letters
    "pl11-zeno-optatus-collatio-carthaginiensis_migne.txt",  # one noisy OCR file
]
for name in _named_samples:
    p = cs.TEXTS_DIR / name
    if not p.is_file():
        results.append(check(f"{name} is present in this checkout", False))
        continue
    units = ci.passage_units(p)
    results.append(check(f"{name}: heading split actually fires (not the paragraph fallback)",
                         len(units) > 1 and any(u["title"] for u in units)))
    results.append(check(f"{name}: no text lost", _no_text_lost(p)))

_lossy = [p.name for p in cs.volumes() if p.suffix == ".txt" and not _no_text_lost(p)]
results.append(check(f"fleet-wide: every .txt volume's passage units reassemble losslessly ({len(_lossy)} exceptions)",
                     not _lossy))
for _name in _lossy:
    print(f"       text lost in: {_name}")

print("\nall passed" if all(results) else "\nFAILURES")
sys.exit(0 if all(results) else 1)
