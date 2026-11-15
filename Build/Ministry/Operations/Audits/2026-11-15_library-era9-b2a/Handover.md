# Handover: Library thread, era 9 (1815-1906), after batch 2a

Written 2026-11-15 by the era 9 batch 2a thread, for batch 2b (Britain, Europe, North America) and batch 3
(outside witnesses, council records, held items). The coordinator (Church Family Tree) is session
`session_01JMNsSAmN1HUCBWPQWS4gro`; each batch's report goes also to the "Answering from Sources" thread,
`session_01JMNsSD4wzPQYRHkAq6uKE3`. Read batch 1's `Handover.md` in
`Build/Ministry/Operations/Audits/2026-11-15_library-era9/` first; this file only adds to it.

## Where batch 2a stands

- Branch `claude/library-era9-b2a`: 74 files for rows 226, 246-248, 263-266, 279-322 and 324-326, and for
  batch 1's retried rows (181, 185, 186, 191, 197, 207, 210, 213).
- The record: `Search_Log.md` and the review files in this folder; `CFT-Wants.md` ("Era 9, batch 2a"); the
  Library's `Decision-Log.md` (last entry).
- Batch 1's eighteen `needs-ruling` shelf rows are decided. No row of batch 2a is at `needs-ruling`.

## What is left, by batch

**Batch 2b:** rows 227-245, 249-262, 267-278, 323 and 327-330 of the wanted list; the date check on the
Kaiserswerth account "by a lady" (`kaiserswerthdea00deacgoog`); batch 1's European and American rows still
open (John Thomas, Noyes, Bourne, de Cock, Walther's constitution in `DerLutheraner04`, Wichern, Dollinger,
Waldenstrom, White's Spiritual Gifts, Lipscomb); the further volumes batch 1 lists under "Located, not yet
taken".

**Batch 3:** the era 9 outside-witness rows and council rows; the held eras 8-9 items in `CFT-Wants.md`
(batch 2 table) and the sweep's section 8.

**Still open from batch 2a's rows** (all in the search log): Tile, Netsvetov, the Optina elders' letters,
Theophan's letters, the Maronite synod of 1818, Hoyek, Varzhapetian, the acts of 1872, Binh, Liang Fa's tract,
Ta'unga's own narrative, Bokwe's Ntsikana, the Iglesia Filipina Independiente's first books, Kuyper's Stone
Lectures, A Retrospect, Os Sertoes. The search log's "Located, not yet taken" list gives archive.org ids for
about thirty further volumes.

## What changed in how the batch runs

The tools in `tools/` are batch 1's, changed as follows. Paths inside them point at the batch 2a scratch
folder and need changing.

- `ia.py marc <id>` prints the item's library catalogue record (edition, place, publisher, date). The undated
  rule needs it: the `meta` date field is not the catalogue.
- `build_strip.py` removes Google's preamble and the lines that hold only a scanner's page mark, and returns
  the words that go in the Provenance note. The preamble's last line is often misread by the OCR ("qooqle");
  the pattern allows for it. A preamble the OCR turned into another script needs a line range in
  `overrides.json` (`pre_upto`).
- Line numbers in headers and shelf rows are now the vendored file's own line numbers. Checkers read the
  vendored first pass, so the first pass must already be stripped the way the final one will be. If the strip
  changes between passes, `build.py` shifts the checkers' line numbers by the difference; it reads the
  first-pass file on disk to do so, so build the final spec before removing the first pass.
- `overrides.json` carries the date basis for undated title pages (`basis_re`, `basis_tpl`), a cut for a host
  file that holds a second volume (`cut_at`), shelf notes (`note_add`) and last corrections to a title or
  creator (`final_sub`).
- `NOTES_BRIEF.md`: the checkers now write the title, creator and publisher from the title page as well as the
  content note and locus, and report flags. The searchers write no content notes.

What went wrong, and the fix to keep:

- **A searcher's "held already" check misses files named differently.** Ormanian's Church of Armenia was
  picked though it was held. Check every pick's archive.org id against `REGISTRY.yaml` and the queue file
  before building.
- **Lending-library scans.** An id of the form `title0000auth` is usually one. `verify2.py` flags the
  collection; do not take them.
- **A second-pass searcher is worth its cost.** Nine files came from one searcher sent back with exact leads
  after the first reports were read.
- **Searchers' OCR-quality phrases carry narration.** `build.py` now keeps only the grade.
- **Sub-agents cannot write a file named `report.md`** in the scratch folder (a tool rule refuses it). Ask for
  the report in the final message.

## Hosts

archive.org only. dbnl.org's robots file disallows automated clients, and a search request was answered 429:
treat it like HathiTrust, Papers Past and prlib.ru, and put what is needed from it on the hand-fetch list (the
search log has the list).

## Generated files

`corpus-coverage.json`'s generator output already differs from main (flagged by PR #1688). This batch did not
run that generator. Look at it before running it; do not fix it blind.
