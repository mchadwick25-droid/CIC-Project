# Searcher brief: era 9 Library batch (read all of this first)

You are a searcher for a source library. For each wanted row you are given, find a scan on archive.org of the
named text (or the best match), download its OCR text, verify it, and write a spec. You vendor nothing and you
edit nothing inside /home/user/CIC-Project. You write only inside your own scratch folder (named in your task).

S = /tmp/claude-0/-home-user-CIC-Project/39e3938f-160e-5665-9646-ae4332ae3602/scratchpad

## Commands: use ONLY these (anything else can stall on a permission prompt for an hour)

- `python3 $S/tools/ia.py search '<lucene query>' [rows]` (write the full path out, not $S)
- `python3 .../tools/ia.py meta <id>`
- `python3 .../tools/ia.py marc <id>` (the library catalogue record of the item: edition, place, publisher, date)
- `python3 .../tools/ia.py fetch <id> <your scratch>/dl`
- `python3 .../tools/ia.py page <id> <leaf number> <your scratch>/img/<name>.jpg` (then the Read tool shows the image)
- `grep`, `sed -n 'A,Bp'`, `head`, `wc`, `ls` on files; and the Read, Grep and Write tools.
- No curl, wget, pip, cd chains with other tools, python one-liners, or any other command. No web search.
- Never print a whole source file. Read title pages and passages by line range only (40 lines at a time).

archive.org has no full-text search here: search by title, creator and year, e.g.
`title:(memoirs finney) AND creator:(finney)`, `title:(apologia pro vita sua) AND year:[1864 TO 1930]`.
Try spelling variants and the original-language title.

## The wanted rows

/home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md
Each row starts `| <number> | <person> |`. Grep for your row numbers (`grep -n '^| 163 |'`) and read them. Titles
marked "[suggested; to confirm]" are guesses: confirm the real title and year from a scan, or find what really
exists. The need is in the "Why it is needed" column: usually the person's own writing, or a Life told by another.

## Before searching: is it held already?

Grep /home/user/CIC-Project/cic/texts/REGISTRY.yaml (case-insensitive) for the author's name and the title's main
words. If held, say so in your report with the filename and skip the download.

## Hard rules for a pick

1. **Imprint 1930 or earlier, read on the title page itself**: in the OCR text (give the line number) or, if the
   OCR year is missing or doubtful, on the page image (give the leaf number). The host's "date" field alone is
   NOT enough. A modern reprint or facsimile counts by its own date: check the first 150 lines and the last 60
   for a reprint notice (e.g. "Reprinted 1968", "Kessinger", "Forgotten Books", "Nabu", "BiblioLife", "University
   Microfilms", "Classic Reprint"). A library accession stamp or a Google/Internet Archive scan notice is fine.
   If the title page prints no year, a pick is still allowed in two cases only, and you must say which:
   (a) a copyright notice in the volume dated 1930 or earlier (give its OCR line and its words); or
   (b) a dated preface, licence or approbation leaf (give its OCR line and its words) AND the library catalogue
   record (`ia.py marc <id>`, field 260/264 or 008) gives the same year. Record the marc output line.
   Otherwise do not pick; report it under NOT TAKEN.
   **Bound-with volumes:** grep for a second title page (a second imprint line, a second "BY", a new pagination).
   If the scan holds more than one work, say so, with the OCR line where each begins.
2. **Host rights**: record `possible-copyright-status`, `licenseurl`, `rights`, `access-restricted-item` exactly
   as `meta` prints them (or "absent"). If the item has a Creative Commons NC or ND licence, a permission notice,
   or access-restricted-item true: do not pick; report it as HELD FOR MARK with the reason.
3. **Complete download**: `fetch` must print `match=True`. If it prints False, fetch once more; if still False,
   say so.
4. **Readable OCR**: sample three places (start, middle, end). If it is garbled beyond reading, look for another
   scan of the same edition or another edition. Say plainly how good it is.
5. **It is the edition claimed**: title-page words, author, place, publisher, year all read from the scan. Never
   write a name, date, place, office or role from memory: only what the title page or the host record gives.
6. **Prefer** the first or an early edition; one work per file. Take the text in the tradition's own language
   wherever a readable scan of 1930 or earlier exists (Russian, Greek, Arabic, Armenian, Amharic, Spanish,
   Portuguese, French, Tagalog, Japanese, Chinese, Malagasy, Xhosa, Sesotho, Dutch ...), AND an English print of
   1930 or earlier where one exists. Record the language. Search in the original script and in transliteration.
   Black letter or non-Latin OCR that is garbled beyond reading is NOT TAKEN (list it as LOCATED, with the id).
7. **Size**: at most 3 files per row unless the row names a multi-volume work a profile needs whole (then say so
   and pick the volumes that matter, and list the others with their ids as "located"). Never take a whole run of
   a periodical: one volume or year at most, the one nearest the event the row names.
8. Do not give up on a row after one query: try at least four (title words, author, year window, other
   spellings, other language). If nothing: report NOT FOUND with the queries tried.

## What to hand back

Write `<your scratch>/picks.json`: a JSON list, one object per picked file:

```
{"row": 165, "person": "Charles G. Finney", "serves": "his own lectures",
 "ia_id": "...", "local": "<your scratch>/dl/<id>_djvu.txt",
 "title_page_words": "title as printed on the title page",
 "author_as_printed": "...", "editor_translator_as_printed": "... or null",
 "place_publisher_as_printed": "...", "imprint_year": 1835,
 "imprint_read_at": "OCR line 23" or "page image leaf n7",
 "first_published": "1835 (from the preface line N / title page) or unknown",
 "host_rights": {"possible-copyright-status": "...", "licenseurl": "absent", "rights": "absent", "access-restricted-item": "absent"},
 "language": "eng", "bytes": 123, "listed": 123, "match": true, "words": 12345 (from wc -w),
 "ocr_quality": "clean / fair / poor, with a sentence",
 "divisions": "how the text is divided (lectures, chapters, letters), with the OCR line of the contents page if any",
 "text_start_line": 120, "text_end_line": 20000, "editorial_matter": "preface by X lines a-b; index from line c",
 "mixed_voices": "e.g. letters to him printed at ...; or none seen",
 "wanted_passages": [{"what": "...", "ocr_lines": "1200-1290"}],
 "front_and_back": "what stands before the title page and after the text ends in the OCR (a Google preamble, library notices, publisher's lists), with OCR line ranges",
 "undated_basis": "null, or for an undated title page: the copyright notice or dated preface (OCR line, words) and the marc date line",
 "cautions": "anything a profile writer must know (author not named on title page, translation only, abridged, vol. 1 of 2...)",
 "library_stamps_or_reprint_signs": "what you saw at front and back"}
```

And `<your scratch>/report.md`: per row, FILLED (ids) / HELD ALREADY (file) / NOT FOUND (queries tried) /
NOT TAKEN (id, why) / HELD FOR MARK (id, why) / LOCATED (ids of further volumes not downloaded). Keep it short.

Your final message back: one line per row with the outcome, nothing else. If a permission prompt blocks you or a
command is refused, stop that step and say so in the final message; do not wait.

Extra rules for this batch: the Dictionary of African Christian Biography, HathiTrust, Papers Past, Google Books
and gallica are not to be used. You do not write content notes: only title-page facts, line numbers and what you
saw. Where a row names a person and not a book, the best pick is that person's own writing, then a Life or
account of 1930 or earlier that tells the life at length (give the OCR lines of the chapter that does).
