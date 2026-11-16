# Handover: Library, Thread B, after the rendering sample and the year audit (2026-11-16)

Written by Thread B (Library), session_01JMNsS9WRK3s4XStRhyW6qw, which stopped at a clean point on the
coordinator's instruction. The coordinator is session_01JMNsSCBTsM2UVaFpDa3BTF; every report goes there with
send_message. Read `CLAUDE.md` first, then `../2026-11-16_library-era9-located/Handover.md` (the intake
method), then `../2026-11-16_library-era10-b2b-periodicals/Handover.md` (the queue's detail), then this file.

## The next session has two jobs only, in this order, then stops

The coordinator, 2026-11-16: 307 first, then 308, then stop. Everything in "The queue" further down waits
for the eras 1 to 7 milestone.

## Job 1 of 2 for the next session: the Martyrs' Mirror swap (Open-Gaps 307)

Mark, 2026-11-16, as the coordinator passed his words on: first "Retire it, find the 1886 scan
(Recommended)", then, once the census dependency was reported, "Swap now, then retire (Recommended)". Vendor
the clean 1886 scan, re-point the nine census sources and the shelves to the same passages in it, then move
the 2012 file to Archive, in one small pull request. Do this now, not after the milestone.

`van-braght_martyrs-mirror_sohm1886.txt` is held from a 2012 Herald Press printing that carries "Copyright ©
1938 by Mennonite Publishing House". It could not simply be moved: nine sources in the live census cite it,
and `tools/validate-census.mjs` fails a source whose file is not under `cic/texts/`.

- **The clean scan is found:** archive.org item `bloodytheatreorm00brag`. Its title page, read on the image
  (leaf index 10): "ELKHART, INDIANA. / MENNONITE PUBLISHING COMPANY. / 1886.", "Translated ... by Joseph F.
  Sohm", with a Copyright Office stamp of 25 April 1887. A Library of Congress scan. Not vendored. Run the
  full intake checks on it (R15: look for a film notice; the whole title leaf and its verso).
- **Every record that cites the held file** is in `martyrs_mirror_citations.json`: the nine census sources
  with their lines and quotations, the same nine in `cft-website/index.html`, the shelf rows in five
  traditions, the two staging files, the registry entry, `cic/engine/tests_corpus_index.py` line 261, the
  mention in the Dordrecht Confession file's header, and the world documents that name it.
- All nine census sources quote van Braght's own text in Sohm's translation. The only matter later than 1886
  in the held file is the "Publisher's Preface to the Second English Edition", lines 102 to about 130. Cite
  nothing from those lines.
- The swap, in order: vendor the 1886 scan by the intake method of the era 9 handover; find each of the nine
  quotations in it and re-point file and lines in `cic-website/data/world-census.json` (the 1886 print may
  word or spell a line differently from the 2012 resetting: a quotation must match the new file word for
  word, so where it differs, report it to the coordinator and do not edit the quotation yourself); rebuild
  whatever copies the census into `cft-website/index.html`; re-point the shelf rows; move the 2012 file to
  `Archive/Retired-Library-Texts/`; update the registry, the generated indexes and the test list. Nothing is
  deleted. Record it under Open-Gaps 307.

## Job 2 of 2 for the next session: the header corrections (Open-Gaps 308)

The coordinator, 2026-11-16: correct the twelve wrong header years and the Evliya Çelebi part number; no file
renames; these are factual fixes and need no ruling. This session did not do them: each wrong year stands in
three or four header lines, in the registry's notes and reader credit, and in two to seven shelf rows.

- The list, with what each page prints, is in `README.md` here; every read with its host item and leaf is in
  `page_reads_206.json`.
- Change the year wherever the header, `cic/texts/REGISTRY.yaml` and the shelves in `cic/corpus-map/` state it
  for that file. Keep every header's line count the same, so no cited line moves. Leave the file names.
- Two need judgement. Lake's Diognetus: the held file is a transcription that cites 1917 and G. P. Putnam's
  Sons, while the scan the header names prints MCMXIII, Heinemann and Macmillan; say which the file is taken
  from. Cassiodorus, PL 70: the header has no publication date line and its rights basis says 1866; the page
  prints 1865.
- Then the generated indexes, `python cic/engine/texts_registry.py --check`, the corpus tests and
  `corpus_coverage.py`, as in the era 9 handover's recipe. One independent Opus review of the diff.

## Why this session stopped

Mark, 2026-11-16, as the coordinator passed it on: "Writing first, trim the Library (Recommended)". The last
of the free Fable goes to the writing. The Library's remaining work waits until the eras 1 to 7 milestone.
The two jobs at the top of this file are the exception: Mark wants them now. Do not start the queue
further down before the coordinator says the milestone is reached.

## Done by this session

- **The rendering sample, approved and stored.** `cic/renderings/` exists: the finding guide to Groen van
  Prinsterer's Ongeloof en Revolutie in 40 sections, and three passage renderings. Record:
  `../2026-11-16_library-rendering-sample/README.md`. Mark's decision is in the Library Decision-Log, "The
  rendering sample". Pull request #1706.
- **The year audit (Open-Gaps 305), published as a list.** Record: `README.md` in this folder. The page:
  https://claude.ai/artifact/SsidCpJNKaA7JXgLS6kkAK. No file was changed.
- **`CLAUDE.md`** now names `cic/renderings/` among the live surfaces (Mark, 2026-11-16: "Yes, add it to the
  list (Recommended)").

## The queue, for after the eras 1 to 7 milestone

In the coordinator's order. Detail for 302, 301 and 303 is in the batch 2b handover and is not repeated here.

1. **302: the books of era 10 batch 2's follow-on**, with the Pacific Garden Mission's statement of 1916
   under R13, the Путь headers brought to R14, and the three era 8 shelf rows moved from `needs-ruling` to
   `assigned` with Mark's words "Yes, as proposed (Recommended)".
2. **301: era 8 batch 3.**
3. **303: The International Review of Missions for 1912 and 1913.** No CMS volume: R15.
4. **Finding guides for the other non-English texts** (about 65, less the five whose scanned text is too
   garbled), era 8 to 10 first, the tradition's own-voice texts first. On Opus by then, by Mark's direction,
   unless he says otherwise.
5. **Passage renderings** only when a writer asks for a passage.

Hand searches still owed, for a person with a browser: HathiTrust and Google Books, for a scan of the CMS
Proceedings without the microfilm maker's notice.

Run the CORPUS-USE, WANTS-REGISTER and queue check before every search. Never vendor legend-check card rows.
A ruling is only Mark's own words. Make no metered model or API calls.

## How to make a finding guide now

The rule: `cic/renderings/README.md` and `cic/texts/INTAKE.md`. The briefs that worked are in
`../2026-11-16_library-rendering-sample/briefs/`.

1. Split the text into spans of about 2,000 to 3,000 lines that end on chapter boundaries. One writer per
   span reads all of it and writes its sections straight at section level: two or three sections a chapter,
   20 to 40 for the book. Adapt `SECTION_BRIEF.md`, but have the writers read the text itself. (The Groen
   guide was written from 206 small parts first, which the ruling made unnecessary. Do not repeat that.)
2. Names and quoted authors with their lines: have the writers list them per section, then check by script
   that each name is on its line.
3. One reviewer per span reads the whole span and checks every section (`REVIEW_BRIEF.md`). The reviewer
   writes the corrected text. Apply it; split any sentence over 25 words.
4. Store it as `cic/renderings/guides/<text>.yaml` and run `python cic/engine/renderings.py --check`.
5. Cost to expect: about 21 subagent tokens for each word of the source, half writers and half reviewers.

What the reviews caught, to put in every brief: a view the author sets out in order to attack, given as his
own; a limiting word dropped; a main division of a chapter left out; a footnote range that takes in the
neighbouring note; a quotation given to the wrong author.

## How to make a passage rendering now

1. Read the passage on the page image and list every scanning fault. Page images:
   `https://archive.org/download/<item>/page/n<index>.jpg`; the item's `_scandata.xml` maps printed pages to
   leaves, and the index can be one less than the leaf number.
2. Two renderers, separately. Give each the bare passage, the page image and the bar. Nothing that steers a
   word choice: both renderers of the sample were told to keep two Dutch words apart, and both wrote "the
   Upheaval" where the reviewer ruled for "the Revolution".
3. Compare. A difference in meaning is marked uncertain and both readings are kept.
4. A fresh reviewer on Opus checks the final rendering against the original and the bar. Apply the fixes.
5. Store it in `cic/renderings/passages/<text>.yaml`: `original` word for word as the file has it, the scan
   faults, the page image, both renderings, the uncertain readings. No review talk in the record; the check
   for live surfaces covers the folder.

## Tools here

`fetch_meta.py` (host dates for a list of items), `leaves.py` (the leaves a host types as title or cover),
`READ_BRIEF.md` (the brief for reading a printed year on a page image). `crop.py`, `sheet.py` and `stack.py`
are in `../2026-11-16_library-era9-located/tools/`. A host's "Title" leaf type is often wrong for Migne and
Mansi volumes; look at the first twelve leaves.
