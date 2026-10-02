# hus handoff gate: residue cleared, 2026-09-30

Run with a temporary registry entry (`records/worlds/hus.yaml`, `records/hus/`), removed afterwards and not committed. The project lead registers the world and sets `safety_adjacent`.

## Changes

- **handoff-02.** `Step0_Review_Round3.md` gains the `Disposition: Approved to proceed` line. Its header still lacks the fields `reviewfile` reads (reviewer and drafter models and agents, round, two truncation checks); they are not supplied here because the file does not record them.
- **handoff-04.** `Source_Registry.md` rows 80 (Camerarius, `Historica narratio`, confidence C) and 81 (cross-link to Lollardy, confidence D, cross-link only, no claim rests on it). The header rule on works assigned only to another world names row 81 as the one exception. `Doc_02_Source_Ecology.md` section 10 points R9 to row 80. Two ISO dates in prose (rows 11 and 48) are written out.
- **handoff-08.** Quotes triaged against the vendored files:
  - Real quotations that the gate did not match, now quoted as the scan prints them: Lützow's "Small" and "Great" party passage, the Waldensian note and the Taborite footnote (nested marks and the scan's " ;" spacing); Schaff, "did a man owe more to mortal teacher..." (the word "Never" sits before a page break); Hus, Letter XVII ("tomb ; but") and Letter XX (the scan breaks "All-" and "powerful" across a line, so the span now starts at "to suffer under Pilate's power"); Luther's 1520 address, split at the ellipsis and given its file name; the Constitution's Article 22 wording, now the contiguous words of the Constitution.
  - Corrected against the file: the Registry row 55 source note "E MS. Miaden. p. 82" is printed "E MS. Mladen. p. 82" at line 7374 of the Palacký file (the "Miaden" misreading is real only at p. 79, line 7487).
  - Marks removed (a heading, a corpus-map note, the project lead's choice-box answer, a Registry-internal label, or the builder's English gloss of Latin): the Atlas title, Article 4's title, `One world, three strands (Recommended)` (recorded in `hus_Round1_Revision_2026-09-30.md`), the Registry section headings named in Doc_02, the Piccolomini corpus-map note, `Articles of the Taborite priests`, `the tract attributed to Hus by Thomson`, and the contents-list gloss on the Satisfactoria (the file's line is Latin).
  - Canisius's "Hus much haue we saide" is in `canisius_summe-of-christian-doctrine_anon1622.txt`, line 31353; the file is now named in the paragraph.
- No `cic:<file>:<locus>` addresses were added. For these plain-text files a locus is a passage unit of 55,000 to 180,000 characters whose title is not the section it opens, so it would confirm nothing about the division.

## Gate state after the changes

Passing: handoff-02, 05, 06, 07, 08, 09, 10, 11, 12; `gaps hus`; live-commentary shows no REWRITE or ROUTE line under `Build/worlds/hus/`. Not passing: handoff-01 (`safety_adjacent`, the project lead's field). Handoff-03 and 04 failed on the round cap until the Round 3 files of Doc_01 and Doc_02 carried a disposition (the Cycle reset in the Round 4 files needs one); another session's uncommitted disposition lines on those two files make `roundcount hus 1` and `2` pass, and the gate was not re-run after them.
