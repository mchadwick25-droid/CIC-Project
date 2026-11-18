# R2 recheck: Library era 10, batch 1 (94 files), 2026-11-15

Rechecker: one fresh Fable subagent, read and grep only, at lower effort. A targeted recheck of the round 1 findings
and of what `R1_changes.md` says changed. Filed by the Library thread; what was done about its four small points is at
the end.

**Verdict: clear to proceed.** All five blocking findings are fixed in every place they lived. Nothing new is
blocking.

## Blocking findings still open or new

None.

## Non-blocking

1. **"Twenty files rest on it" is now nineteen.** Niebuhr 1927 was one of round 1's twenty and now rests on the
   title-page year.
2. **Two citations point at text that is not on this branch.** "R1 to R11 in `Decision-Log.md`, 'Era 10 rights
   rulings'", and "`INTAKE.md` section 2 names the Owner-declared free class", live on
   `origin/claude/library-era10-rights-rulings`, which is in neither `main` nor this branch. They hold once that
   branch lands first. Both branches append to `Decision-Log.md` and edit `INTAKE.md` section 2, so expect a merge
   conflict.
3. **Dyer's life of 1900: two wordings.** "Cut off at the end of chapter XII" in the Search_Log; "cut off in chapter
   XII" in the wants table. The raw scan breaks mid-sentence inside chapter XII, so the table's wording is right.
4. **Cape Town shelf note.** It says the 2011 notice falls "at the very end of the entry's window"; the window ends in
   2010, so 2011 is after it. The row is `needs-ruling` and gives both dates.

Observations, no change needed: Emhardt's header says the Sergius letter is "printed in full"; the book does not use
those words, the range carries no omission mark, and one page-foot note sits inside it. In God Hath Spoken the 11
removed lines include two lines of OCR noise from the Internet Archive's own inserted leaf, no book text.
Removed-line counts differ from the Provenance notes by one blank line in two files (Dyer; Loisy's Simples
réflexions). The R12 line in `INTAKE.md` says "dated inside the rule" where the logs say "1930 or earlier".

## Confirmed fixed

- **1. Cape Town notice.** The whole notice is in the header, the registry note and the queue row, and matches the
  file's own line.
- **2. R12.** Recorded in the `Decision-Log.md` batch entry with Mark's words and in `INTAKE.md` section 2; the
  Search_Log and `CFT-Wants.md` cite it to the entry for this batch; the rule reads the same in all three.
- **3. The Fundamentals.** "1910 to 1915" and "gathers the essays" are gone everywhere; the new wording matches the
  preface in volume 1.
- **4. Spinka.** Every place says he "says he cites it in full" and that one omission is marked; lines 5288, 5437 and
  5381 are right.
- **5. Four split rows.** Each has a tradition row on the home shelf and a context row on the other; role, confidence
  and note agree. All 117 placements in the 94 staging files equal the merged shelf rows field for field. No leftover
  row from the first vendoring is in any shelf file.
- **Host marks, compared with the raw host files.** Acta Sanctae Sedis 40: 40 preamble lines and 854 marks removed,
  none left, no book line removed. Niebuhr 1927: the Internet Archive notice and its tail. Loisy (English), Mott 1900,
  Ramabai 1888: only the Cornell scanning notice and its address. Five more files and one with nothing removed
  (Emhardt, byte-equal to the raw file): removed lines are host notices only.
- **Loisy 1902 (French).** Absent from every record; logged "held for Mark" in the wants table, the Search_Log and the
  Decision-Log. The raw scan carries "MICROFILMED 1993" and the permission line.
- **Line numbers after the second strip pass.** Acta Sanctae Sedis 40 (all three texts, first and last lines);
  Niebuhr 1927 (nine chapters); Mott 1900 (thirteen parts); Ramabai (twelve); Loisy English (seven); Emhardt (the
  letter, the epistle, sixteen part lines); the Korea Mission Field (postcard and signature); Faith and Order (both
  ranges); and three citations each in fourteen files not checked in depth in round 1. All right.
- **Other items.** Caution 14 quotes the print. Niebuhr's other 1932 title is named in the header, the registry, the
  queue and the Search_Log. Niebuhr 1927's saved page image shows the title page printing 1927. Beauduin's misreading
  is named. Macnicol's note says it is after the window. Each wants-table item round 1 listed is now in the Search_Log
  or attributed. Registry notes match the header Content notes for all 94 files. "94 files, 10,208,969 words" matches
  the wants table.

## Not checkable by this recheck

Page-image and host claims other than Niebuhr 1927 leaf 6; the quoted terms of the three websites and the renewal
results; that Mark said the words quoted for R12 and for the two calls (they are recorded as coming through the briefs
and the coordinator); the census windows the shelf notes cite; Search_Log finds for scans not saved; the bodies of the
83 files outside the eleven compared.

## What the Library thread did about the four points

1. "Nineteen" in both places.
2. `origin/main` is merged in before the pull request; the citations are checked again after the merge.
3. The Search_Log now says "cut off in chapter XII".
4. The Cape Town shelf note now says the 2011 notice is "the year after the entry's window closes (c. 2010)".

After the recheck the live-commentary check asked for process references to leave the vendored headers and the queue
rows. The headers now state each rights basis plainly, without naming a ruling or a call; the rulings and calls are in
`Decision-Log.md` and the Search_Log. Each header and registry note was then compared with the regenerated spec: all
94 equal.
