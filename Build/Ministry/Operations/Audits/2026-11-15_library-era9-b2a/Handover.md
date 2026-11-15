# Handover: Library thread, era 9 (1815-1906), after batch 2a

Written 2026-11-15 by the era 9 batch 2a thread, for batch 2b (Britain, Europe, North America) and batch 3
(outside witnesses, council records, held items). The coordinator (Church Family Tree) is session
`session_01JMNsSAmN1HUCBWPQWS4gro`; each batch's report goes also to the "Answering from Sources" thread,
`session_01JMNsSD4wzPQYRHkAq6uKE3`. Read batch 1's `Handover.md` in
`Build/Ministry/Operations/Audits/2026-11-15_library-era9/` first; this file only adds to it.

## Where batch 2a stands

- Branch `claude/library-era9-b2a`: 73 files for rows 226, 246-248, 263-266, 279-322 and 324-326, and for
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

- **Another Library thread may vendor the same item while a batch runs.** Aglipay's Catequesis was vendored
  here and by the era 10 batch under the same name; it surfaced only as a merge conflict. Check the picks'
  archive.org ids against main's registry again just before the merge.
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

## The finish, handed on (the thread stopped at its context limit)

The batch is complete on the branch: 73 files, two review rounds (round 2 clears), origin/main merged in with
no conflict markers. What is left is only the finish.

1. **Checks on the merged branch.** The nine Library validators passed before the merge. They were run again
   after it, with `tools/check_live_commentary.py --base origin/main --enforce`,
   `tools/check_spelling.py --base origin/main --enforce` and `tools/check_paths.py`; the result is in the last
   section of this file. If main has moved again, merge it and run them again.
2. **`cic-website/data/corpus-coverage.json` was not committed.** The coordinator's new rule (PR #1691, not on
   main when this was written) is to run `python cic/engine/corpus_coverage.py` after the last map change and
   after merging main, and to commit the file. Run here, the generator's output differs from main far beyond
   this batch: 307 entries become 619, because the committed copy predates the census's growth. That is the
   drift PR #1688 flagged. It was left as main has it, and the question was put to the coordinator. Once
   #1691 is on main, merge main, run the generator and commit its output.
3. **One draft pull request** from `claude/library-era9-b2a` into `main`, marked ready when CI is green. No
   pull request has been opened yet. Earlier pushes ran no CI (the workflow runs on pull requests only).
4. **Before merging,** send the coordinator (`session_01JMNsSADg2CkWvhgudEDKFw`, confirmed by the former
   coordinator) one line and wait for its go; it gives the Open-Gaps number then. Write the Open-Gaps entry in
   `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` on the pattern of batch 1's entry 287: what stays
   unfilled (the search log's "Not found" and hand-fetch lists).
5. **After merging,** send the wants table, the cautions and what is left at `needs-ruling` (nothing) to the
   coordinator and to the "Answering from Sources" thread, `session_01JMNsSD4wzPQYRHkAq6uKE3`.

To regenerate the files (only if a header must change): the spec is built by `tools/build.py` from
`tools/table.txt`, `tools/overrides.json`, the searchers' picks (`tools/data/picks_*.json`) and the checkers'
notes (`tools/data/notes_out_*.json`). `build.py` expects them in a scratch folder as `g<letter>/picks.json` and
`notes_out_<n>.json`, with each scan's `djvu.txt` fetched again by `ia.py fetch` into `g<letter>/dl/`. For one
small change it is less work to change `overrides.json` and edit by hand the one file's header line, its
staging row, its registry entry and its queue row, all four together.
