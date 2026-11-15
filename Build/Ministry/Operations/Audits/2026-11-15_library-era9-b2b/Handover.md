# Handover: Library thread, era 9, after batch 2b

Written 2026-11-15 by the era 9 Library thread, batch 2b, so that the follow-on batch starts in a fresh session.
The coordinator (Church Family Tree) is now session `session_01JMNsSADg2CkWvhgudEDKFw`; each batch's report
goes also to the "Answering from Sources" thread, `session_01JMNsSD4wzPQYRHkAq6uKE3`.

## Where batch 2b stands

- Branch `claude/library-era9-b2b`: 61 files for rows 227-245, 249-262, 267-278, 323 and 327-330 of the wanted
  list, and the Kaiserswerth date check. Two review rounds done; origin/main merged in.
- The record: `Search_Log.md`, `R1_review.md`, `R1_changes.md`, `R2_recheck.md` in this folder; `CFT-Wants.md`
  ("Era 9 (1815-1906), batch 2b"); the Library's `Decision-Log.md`.
- Merging is sequenced by the coordinator: one line when the pull request is ready, then wait for its go and
  take the Open-Gaps number from it.
- `cic-website/data/corpus-coverage.json` is left as on main. When PR #1691 lands (it rewords the Hadewijch
  header and makes CI test coverage drift): merge main, run `python cic/engine/corpus_coverage.py`, commit.

## The follow-on batch: texts the cards rest on (added by Mark, 15 November)

Mark, through the coordinator: "the whole point of the library threads was to build the library so we can do
our writing". A check of the story, tradition and council cards found many resting on texts the Library does
not hold. The era 9 rows are copied in `Texts_To_Fetch_Era9.md` in this folder (211 rows, each "named from
memory, not confirmed"), with a region column added by a helper: Britain 29, Europe 58, North America 47,
other 69, unsure 8.

This thread's share is Britain, Europe and North America: 134 rows, plus whichever of the 8 unsure rows fall
there. Check the region column before trusting it. For each row: confirm the title exists, grep
`cic/texts/REGISTRY.yaml` before downloading, search, rights-check, vendor under the usual rules, and log what
cannot be found with the card it serves. Many rows will be held already after batches 1, 2a and 2b.

## First in the follow-on batch: everything located goes in (the coordinator's instruction, 15 November)

The coordinator passed on a remark of Mark's: "each of them are vendering all the sources they find into the
library". It was a statement of fact about the Library threads, not a rule, so what follows is the coordinator's
instruction. Every source found that passes the rights rules is vendored, with its header, registry entry and shelf rows. Only
texts that fail on rights (logged, with the reason) and the hand-fetch sites stay out. So the items under
"Located, not yet taken" in this folder's `Search_Log.md` are vendored first: the further volumes and the other
witnesses. Mott's history of the Student Volunteer Movement prints no year and needs the date check. Later
printings of a text already held are not taken again. Whether batch 1's "Located, not yet taken" list is this
thread's or batch 2a's is the coordinator's call: ask before starting on it.

## What changed in how the batch runs (keep)

- `tools/build2.py` makes the spec and the staged files; `tools/mkov.py` writes `overrides.json` (titles,
  creators, publishers, date bases); `tools/vendor2.py` copies staged files in and appends the registry and
  queue rows. Paths inside them point at the batch 2b scratch folder and need changing.
- Google's preamble is stripped by `build2.py`, so header line numbers are the vendored file's own lines.
  Checkers read the staged files and never see raw OCR line numbers.
- Regenerate, do not patch: before a second vendor run, remove every file the batch added (tracked and
  untracked) and restore the registry, the queue file, the README and the shelf files from the merge base, not
  from a freshly fetched origin/main. A half-run of `vendor2.py` leaves files without registry rows.
- After the vendor run: `corpus_map_merge.py --assign-ids`, then `corpus_map_merge.py`, then
  `texts_registry.py --write-readme`.
- Merge conflicts with sibling Library threads: keep both sides in `Decision-Log.md`, `REGISTRY.yaml` and the
  queue file; take main's side of the shelf files and the README, then run the merge and the README again.

## What the reviews caught (watch for these)

- An undated later printing under the first edition's copyright notice or preface (the Life of John Smith,
  Cartwright). Compare the publisher on the title page with the name in the copyright notice.
- A publisher line taken from the host record and not from the title page (Cabot).
- A year the OCR prints differently from the page image (Christendom Astray).
- Black-letter German OCR that cannot be read (Lohe's Neuendettelsau history).

## Calls made by the coordinator in this batch

- A printed "First published" line under the imprint, with a signed and dated introduction and the catalogue's
  date agreeing, counts like a dated leaf (Marchant, 1924).
- Where every candidate date is well before 1931, a reader's upload record in place of a library catalogue
  does not block the text; the header gives both dates (Christendom Astray).
