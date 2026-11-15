# Handover: Library thread, era 9 (1815-1906), after batch 1

Written 2026-11-15 by the era 9 Library thread at the end of batch 1, so that batch 2 starts in a fresh
session. The brief and the coordinator's additions are in the first message of the batch 1 session; the
coordinator (Church Family Tree) is session `session_01JMNsSAmN1HUCBWPQWS4gro`, and each batch's report goes
also to the "Answering from Sources" thread, `session_01JMNsSD4wzPQYRHkAq6uKE3`.

## Where batch 1 stands

- Branch `claude/library-era9-majors`: 99 files for the 63 major person rows (163-225) of
  `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`.
- The record: `Search_Log.md`, `R1_review.md`, `R1_changes.md` in this folder; `CFT-Wants.md` ("Era 9, batch
  1"); the Library's `Decision-Log.md` (last entry).
- Merging is sequenced by the coordinator: send it one line and wait for its go; take the Open-Gaps number
  from it at go time. No Open-Gaps entry has been written for this batch yet.

## Rules that changed during batch 1 (all from Mark, through the coordinator, 15 November)

1. **Undated title pages:** "Copyright notice yes, preface with a check". A copyright notice of 1930 or earlier
   counts; a dated preface counts only when the library catalogue's date agrees. Name the date used and its
   place in the rights line. In `cic/texts/INTAKE.md`, section 2.
2. **Wider rights:** an American book printed 1931 to 1963 whose copyright was never renewed counts as free;
   record the renewal search in the rights line; take one only where it is the best source for a want, and log
   each in the search log. United States government works are free whatever their date. A printed court or
   government record counts by its imprint. Unprinted archive records are cite only. Owner-stated free texts
   are taken with the owner's words in the header: the Dictionary of African Christian Biography (CC BY 4.0;
   skip entries reprinted "with permission"), the Catholic Worker paper, the Cape Town Commitment (verbatim
   only). Non-commercial-only permissions are not taken.
3. **Host additions:** at intake only, the host's own additions (Google's preamble, archive.org notices, OCR
   debris) may be stripped, with exactly what was stripped recorded in the Provenance note. Batch 1 did not
   strip anything; its headers say the text is the host's, whole.

## How batch 1 ran, and what to keep

The tools are in `tools/` in this folder:

- `ia.py`: search, metadata, fetch with byte-count check, page image.
- `verify2.py`: one line per pick with flags (size, year in the OCR head, host rights, reprint signs).
- `crops.py`: the imprint half of named page-image leaves, side by side, for reading years the OCR drops.
- `table.txt` and `overrides.json`: one line per file (archive id, filename, shelf, role, confidence, date,
  want) and the hand corrections. `build.py` makes the spec from these and the searchers' picks; `vendor.py`
  writes the file, the shelf file, the registry entry and the queue row. Paths inside them point at the batch
  1 scratch folder and need changing.

What worked: seven Sonnet searchers in parallel, each held to `ia.py`, `grep` and `sed`, handing back a
`picks.json`. Then the Library thread checked every pick again. None stalled on a permission prompt.

What went wrong, and the fix to keep:

- **Searchers' content notes are not fit to print.** They carried outside knowledge, praise words, wrong line
  numbers and search narration, and the first review caught it. Fix: take only title-page facts, line numbers
  and downloads from searchers. Have fresh Fable checkers write each content note and locus from the text
  (the brief is `tools/NOTES_BRIEF.md`; the searchers' brief is `tools/BRIEF.md`).
- **A year "found in the OCR" may be a copyright line or a catalogue card.** Read the title page itself.
- **Bound-with volumes:** one scan may hold several works (the Friends' pamphlets, Pastor Hsi, two years of a
  periodical). The checkers found these; ask searchers to look for a second title page.
- **Regenerate, do not patch.** A header change after vendoring means removing the files and generating all
  of them again from the spec; the registry and the queue file are restored from main first.
- `tests_corpus_index.py --reuse-index` takes more than ten minutes on this corpus. Run it in the background.

## Batch 2, in order

1. The texts of batch 1 still owed a date check under rule 1: Kuyper's Stone Lectures (three scans), Hudson
   Taylor's A Retrospect, Walsh on the Uganda martyrs (a chapter on Charles Lwanga), Catherine Booth's
   Aggressive Christianity, the Kaiserswerth account "by a lady".
2. Batch 1's not-found rows by the new routes: Tile, Mokone and Sadrach in the Dictionary of African Christian
   Biography; Sadrach and de Cock on dbnl.org; Darby's four smaller books (located); Der Lutheraner, the
   fourth year, for the 1847 constitution; the further volumes listed under "Located, not yet taken".
3. The person rows not marked major, 226-330 (the Who scan's era 9 rows), again by region, with Africa, Asia,
   Oceania, Latin America and the Eastern churches searched on purpose.
4. The era 9 outside-witness rows and council rows of the wanted list.
5. The held eras 8-9 items in `CFT-Wants.md` (batch 2 table) and the sweep's section 8.

Held for Mark, to bring at merge time: Os Sertoes, third edition, 1905 (`004518-completo`: Public Domain Mark
on the record, a non-commercial notice from Brasiliana USP inside the file).
