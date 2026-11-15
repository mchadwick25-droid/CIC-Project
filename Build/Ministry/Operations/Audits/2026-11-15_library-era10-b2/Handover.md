# Handover: Library era 10, after batch 2 (2026-11-15)

Written by the era 10 Library thread, batch 2 (session_01JMNsS9o1TTspeWP2qjkoqP), for a fresh session. The coordinator
is session_01JMNsSCBTsM2UVaFpDa3BTF (the Church Family Tree coordinator; the role changed hands twice during this batch). Read
`CLAUDE.md` first, then batch 1's handover and Search_Log
(`Build/Ministry/Operations/Audits/2026-11-15_library-era10/`), then this folder's `Search_Log.md`.

## Where things stand

- Batch 2: 71 files, 4,273,101 words, branch `claude/library-era10-b2`, not yet in a pull request and not merged. Records: `CFT-Wants.md` ("Era 10 ... batch
  2"), `Decision-Log.md` (last entry), this folder's `Search_Log.md` (34 cautions), `Hand_Fetch_List.md` (20 items for
  Mark), `R1_review.md`, `R1_changes.md`, `R2_recheck.md`.
- Batch 1's twelve `needs-ruling` shelf rows are settled by the shelf principle. None is left.
- No further scan of the New York Catholic Worker is on archive.org.

## To finish this batch (first thing for the fresh session)

The coordinator is now session_01JMNsSCBTsM2UVaFpDa3BTF (the second handover in this batch; each was confirmed by the
session standing down). It told this session to stop at a clean point and not to open a pull request.

State of the branch `claude/library-era10-b2` at the stop: everything is committed and pushed; `origin/main` was merged
in at 462e6e35 (the registry and queue conflicts were resolved by keeping both sides; no duplicate entries); review
round 1 (`R1_review.md`, four small blocking findings) is answered in `R1_changes.md`; round 2 (`R2_recheck.md`) is a
PASS. Two review rounds are used of three.

Still to do, in order:

1. Fetch `origin/main` and merge it in again if it has moved. If it has, run `python cic/engine/corpus_map_merge.py`
   and regenerate `cic/texts/README.md` (`python cic/engine/texts_registry.py --write-readme`) and
   `cic-website/data/corpus-coverage.json` (`python cic/engine/corpus_coverage.py`), and commit them.
2. Run every check and read each one's own exit code: `corpus_map_merge.py --check`, `corpus_index.py --build`,
   `works_registry.py --check`, `author_ids.py --check`, `texts_registry.py --check`,
   `tests_corpus_index.py --reuse-index`, `tests_corpus_structure.py`, `tests_passage_index.py`, `tests_corpus_map.py`
   (all under `cic/engine/`), then `python tools/check_live_commentary.py --base origin/main --enforce` and
   `python tools/check_spelling.py --base origin/main --enforce`. At the stop, on the merged state, the README
   regeneration, the coverage file and `corpus_map_merge.py --check` had passed; the index build and the checks after
   it had not finished. Before the merge of main, the commentary check and the spelling check passed.
3. Open one draft pull request, push once, mark it ready. Send the coordinator one line and wait for its go; it gives
   the Open-Gaps number. Add the Open-Gaps entry (what stays unfilled, what is held for Mark, the census gaps below).
4. After merging: send the table, the cautions and the open calls to the coordinator and to the Church in
   Conversation "Answering from Sources" thread (session_01JMNsSD4wzPQYRHkAq6uKE3).

## Two additions, through the coordinator, late in this batch

They came when this session was near its context cap, so they are handed on whole.

1. **Vendor what passes.** Mark said of the Library threads: "each of them are vendering all the sources they find
   into the library". The coordinator's later word is that this was a statement of fact, not a rule. The work it
   points to is the list under "The follow-on" below: sources this batch found and dated and did not take.
2. **The "Texts to fetch, by era" list** on the coordinator's page (https://claude.ai/artifact/DAZgxvjPbCyAjzYadhREMW).
   Mark: "the whole point of the library threads was to build the library so we can do our writing". Its era 10 rows
   are extracted in `Fetch_Rows_Era10.md` here: 408 rows, every one "named from memory, not confirmed". List A (128
   rows) is Africa, Oceania and the Orthodox, Oriental and Assyrian churches; list B (280 rows) is the rest of era
   10, for batch 3. Confirm a title exists before counting it; log what cannot be found with the card it serves.
   About 11 of the 128 name anything dated 1930 or earlier, so most will end as cite and link or hand-fetch.

## The follow-on (batch 2b): what to take

Found by this batch, dated 1930 or earlier by the searchers' reading, and not yet vendored. This session's scratch
downloads are gone, so fetch again by identifier. The identifiers, title-page readings and reasons are in
`searcher-logs/` (`*_SPEC.json` for the recommended items, `*_LOG.md` for everything searched and rejected) and in
`searcher-logs/verify_VERIFY.md` (page-image readings). Each still needs its own title-page check before intake.

- **The Christian East**, the 32 issues to 1930 not yet held (archive.org items `per_christian-east_the-christian-east_<date>_<vol>_<no>`;
  twelve are held). Each issue as its own file, as this batch did.
- **The International Review of Missions**, volumes for 1914-1921, 1924-1927, 1929 and 1930
  (`sim_international-review-of-mission_<year>_<vol>`; 1922, 1923 and 1928 are held).
- **Proceedings of the Church Missionary Society**, 1910-1921 (`per_proceedings-church-missionary-soc-for-africa-a_<year>`).
- Africa: Tucker of Uganda (`tuckerofugandaar0000shep`, 1929); the Uganda pageant book (`uganda18771927pa00chur`, 1927);
  Tucker's volume I (not searched for; volume II is held); and the items the Africa searcher downloaded and did not
  recommend, each to be dated first: `bantupastpresent00mole`, `churchinugandach00will`, `twentyfiveyears00roscuoft`,
  `howugandawassave00stoc`, `unitedwestafrica00hayf`, `congomissionaryc00cong_0`, `congomissionfiel00gene`,
  `monkanamomosemon00bill`; a Sesotho communion service of 1926 (`mokhoa-oa-ho-etsa-komunione-e-halalelang`).
- Oceania: Te Karere for 1926 and 1928 (the searcher found no Rātana matter in them); Latter-day Saint prints in
  Tahitian (`ebukahimeneifaaa00chur`, 1921) and Hawaiian (`kealakaioiahoihe00dina`, 1907); `ngahimenemongahu00unse_0`
  (1918 by a dated preface; confirm on the page image).
- Orthodox: Hapgood's Service Book (`servicebookofhol00orth_0`, 1906); Douglas (`relationsofangli00dougiala`, 1921);
  Gavin (`someaspectsofcon00gavi`, 1923); the Orthodox Catholic Review (`orthodoxcatholic1361unse`, 1927); Velimirović,
  The New Ideal in Education (`newidealineducat00veliiala`, 1916); Lototsky (`cerkovne-pravo-lotockyj-1923`) and
  Евразийский временник (`evraziskivremenn53unse`), neither yet examined.
- Oriental: Leeder (1918), Mercer's Ethiopic Liturgy (1915), Connolly (1913), an Armenian Synaxaire (1910), Armenian
  pamphlets of 1908, and Mizo and Khasi church prints of 1912-1930: identifiers in `searcher-logs/oriental_LOG.md`.

Not to take, with the reason, is in the Search_Log (no printed year; reprints; a host's copyright claim; an
uploader's non-commercial license; lending-only; incomplete text; unusable OCR).

## What bit in this batch

- A searcher's claim about what a book contains is a lead, not a finding. Naayem's book was said to carry Surma; a
  mapper found she is not named in it. Map every file on the assembled text before writing its header.
- The row author in a staging file must be the file's own author prefix, or the merge rejects it.
- Host marks come in more shapes than batch 1 met: a digitizing library's page-foot stamp (Руниверс, 3,332 lines), an
  Internet Archive notice whose URL the OCR garbles, and one whose whole text came out as Cyrillic noise. Grep every
  assembled file for "digitized", "google", "archive.org" below the header before mapping.
- A file name can promise more than the scan holds: one volume of two (Tucker), numbers out of order (Te Karere), a
  number cut short (Путь 5), a document missing its last page (The Christian East, May 1923).
- A pack of many issues may not offer page images for each; a garbled masthead year then rests on the numbers on
  either side.
- `texts_registry.py --write-readme` and the corpus index build each take several minutes. Run them in the
  background, and read each check's own output: a shell pipe hides its exit code.
- American spelling in our own text ("catalog", "license").

## Batch 3, as batch 1 proposed, with list B

American books of 1931-1963 under R7 (Adventist, Churches of Christ, Oneness, the Black church), the remaining
non-major people and council leads, and the 280 rows of list B in `Fetch_Rows_Era10.md`.

## Open with the coordinator

- The calls this thread made, which the coordinator or Mark may overrule (Search_Log, "Calls"): the Malayalam
  calendar-leaf year; Jabavu's second edition; the leaf of 1915 in Wanger's catechism; a tradition's own writer after
  its entry's window placed as tradition on the entry that closes in 1906.
- Census gaps met: Sundar Singh; the mission churches of southern Africa after 1906; the Coptic church from 1906 to
  1940; the Serbian church between 1906 and 1920; the Māori and Pacific mission churches after 1906.
- Batch 1's open items still stand (the eleven year-in-title files; the living marks after 2010; second renderings
  under R11 for the Latin held with no old English).

## The finish, by the closing session (2026-11-15)

Main was merged in three more times (the coverage check of PR #1691, era 9 batch 2b, data release 46). No archive.org
identifier of this batch is held under another file name on main. After the merge of era 9 batch 2b, every check of
"To finish this batch" step 2 passed with exit code 0, with `tools/check_paths.py` added; the index build covered the
merged shelf. After the last merge, which touched no Library text, the map check, the registry check, the coverage
generator, the commentary check, the spelling check and the path check were run again and passed. The Open-Gaps entry
is "Library, era 10 batch 2" (2026-11-15). The 408 card-text rows of `Fetch_Rows_Era10.md` are dropped: they came from
the legend check, and the coordinator passed on Mark's direction of 2026-11-15 that they are not wanted.
