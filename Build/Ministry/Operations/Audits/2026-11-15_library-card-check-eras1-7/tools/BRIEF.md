# Searcher brief: eras 1-4 card-check Library batch (read all of this first)

You are a searcher for a source library. For each wanted row you are given, find a scan on archive.org of the
named text (or the best match), download its OCR text, verify it, and write a spec. You vendor nothing and you
edit nothing inside /home/user/CIC-Project. You write only inside your own scratch folder (named in your task).

S = /tmp/claude-0/-home-user-CIC-Project/f9c57968-70e1-5279-8761-1e6f86eb7bd3/scratchpad

## Commands: use ONLY these (anything else can stall on a permission prompt for an hour)

- `python3 $S/tools/ia.py search '<lucene query>' [rows]` (write the full path out, not $S)
- `python3 .../tools/ia.py meta <id>`
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
   If no imprint can be read: do not pick; report it under NOT TAKEN.
2. **Host rights**: record `possible-copyright-status`, `licenseurl`, `rights`, `access-restricted-item` exactly
   as `meta` prints them (or "absent"). If the item has a Creative Commons NC or ND licence, a permission notice,
   or access-restricted-item true: do not pick; report it as HELD FOR MARK with the reason.
3. **Complete download**: `fetch` must print `match=True`. If it prints False, fetch once more; if still False,
   say so.
4. **Readable OCR**: sample three places (start, middle, end). If it is garbled beyond reading, look for another
   scan of the same edition or another edition. Say plainly how good it is.
5. **It is the edition claimed**: title-page words, author, place, publisher, year all read from the scan. Never
   write a name, date, place, office or role from memory: only what the title page or the host record gives.
6. **Prefer** the first or an early edition; one work per file; English where an English print of 1930 or earlier
   exists, and the original-language print as well when the person wrote in another language (record the language).
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
 "content_note": "two or three plain sentences on what the file holds, only from what you read",
 "cautions": "anything a profile writer must know (author not named on title page, translation only, abridged, vol. 1 of 2...)",
 "library_stamps_or_reprint_signs": "what you saw at front and back"}
```

And `<your scratch>/report.md`: per row, FILLED (ids) / HELD ALREADY (file) / NOT FOUND (queries tried) /
NOT TAKEN (id, why) / HELD FOR MARK (id, why) / LOCATED (ids of further volumes not downloaded). Keep it short.

Your final message back: one line per row with the outcome, nothing else. If a permission prompt blocks you or a
command is refused, stop that step and say so in the final message; do not wait.

## Addendum for the eras 5-7 searchers (overrides the text above where they differ)

- Your wants are NOT rows of Wanted_Sources.md. They are the rows marked SEARCH in the dedupe table named in your
  task (columns: want, cards, verdict, held file, edition(s) to search for, note). Use the table's row number as
  "row" and the cards as "person". Rows marked HELD or NOT A TEXT: skip, unless the note says "partly held".
- The "edition(s) to search for" were named from memory and are guesses. Confirm from the scan what exists. If the
  named edition is modern (after 1930), look for an older print of the same work (the original-language edition
  in Migne, MGH, Acta Sanctorum, Rolls Series, a national series, the first print; and an English, French or
  German translation by 1930).
- Every find that passes the hard rules and has readable OCR is a pick: do not leave a good find as "located".
  "Located" is only for unreadable OCR, an unreadable imprint (give the leaf you tried), or volumes beyond the
  3-file limit.
- If report.md cannot be written with the Write tool, put the whole report in your final message instead.
- For a multi-work volume (Migne, Mansi, MGH, Acta Sanctorum) always give the OCR line range of the wanted work.
- Before fetching, check the library again: `ls /home/user/CIC-Project/cic/texts | grep -i <word>`.
