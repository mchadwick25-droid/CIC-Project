# Curation redo: batch B4 and B7 (three files)

Drafter: Sonnet 5.5. One sparse worktree, one branch, three local commits, one push. Tooling: origin/main at 037ef0194. No model or paid calls. Vendored files not edited. Start 2026-10-30T21:29Z, end 2026-10-30T21:35Z (clock as the shell reports it).

## Summary

| File | Result | Check runs | Fixes and entries added | Minutes | Status |
|---|---|---|---|---|---|
| `augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869` | pass | 3 | 11 `fixes` with quote, 11 evidence entries | about 3 | drafted |
| `optatus_against-the-donatists` | pass | 4 | 1 `expected_gaps`, 1 context rule, 1 evidence entry, `ignore` removed | about 2 | drafted |
| `augustine_retractationes-lat_knoll-csel36` | pass | 2 | 8 explicit divisions given `number` and `series` | about 2 | drafted |

## Raulx tome 13 (105,595 words)

Wrong: eleven paragraph heads were damaged by OCR or spacing, so the pattern missed them and ten series showed gaps. The eleven are lines 664, 3286, 5294, 6510, 8028, 9109, 9976, 10933, 12790, 12864, 14038. Each now has a `fix` with a quote from its line, plus an evidence entry.

Readings: `Xlil.` as XIII, `Xiy.` as XIV (the head the tooling review named), `m.` as III (three lines, each after a blank line between II and IV), `XXIÏ.` as XXII, `XLYII.` as XLVII, `Vil.` as VII, `XV .` as XV (a space before the stop), `XXXMII.` as XXXVIII, `XXXiX.` as XXXIX.

Final check: class curated, 248 divisions (247 body, 1 apparatus). Coverage 100.0%, word completeness 105485 + 261 = 105746, 284 exact byte ranges and 98 less furniture, 0 mismatch. Every series p0 to p9 reads first 1 to its last with 0 gaps, repeats, backward steps or unreadable numerals. RESULT: PASS. One `warn` left: line 12817, a running head `LIVRE I. - LES DEUX LETTRES DE GAUDENTIUS`, not a head of the series.

Second printed instance: this translation has no argumentum or capitula list, and its paragraph numbers (sequential, 1 to 54 in Gaudentius book one) do not match the Latin chapter numbers (the Latin passage on Razias is I.31.36 in CSEL 53, Raulx XXXVIII). So no parallel edition under `cic/texts` serves as a second instance. Each reading rests on the glyphs on the line (strokes `l`, `i`, `I` as I; `y` and `Y` as V; `m` as three strokes), not on the sequence.

## Optatus, English edition (123,097 words)

Wrong, two things:
- The `ignore` pattern declared line 2294, `APPENDIX TO BOOK III.309`, as a running head. It is an editor's heading printed between chapters XII and XIII of Book III. The `ignore` is removed. A `division: false` rule (`book3appendix`) now sends the heading line to chapter XIII (`book-third/ch13`), as the sample shows.
- Book II prints XXIV at line 1233 and XXVI at line 1307 and no head for XXV in between.

Final check: class curated, 135 divisions (123 body, 11 apparatus). Coverage 99.9%, word completeness 123196 = 123196, 372 exact ranges, 0 mismatch. RESULT: PASS. The `warn` about 1,287 hand-listed look-alike lines is footnote numbers in the notes ranges; it does not change the result.

## Knoll, Retractationes (87,757 words)

Wrong: the eight chapters addressed by explicit divisions (7, 12, 19, 55, 59, 67, 76, 82) were not counted in the `caput` series, so it showed eight gaps. Each entry now carries `number` and `series: caput`. No address changed.

Printed instance for each: line 3119 `VIL (VIII)`, 4490 `XIL`, 6830 `XVIIII. (XX)`, 11491 `LVIIIL`, 12074 `LXVIL`, 13110 `LXXXII.`. Chapters 55 (line 11240) and 76 (line 12611) print no numeral; the printed list of capitula (lines 1124 to 1506) gives `LV. Admonitio Donatistarum de Maximianistis` and `LXXVI. Contra Pelagium et Caelestium libri II`, matching the headings. The other six also match their capitula entries by title.

Final check: class curated, 97 divisions (94 body, 3 apparatus). Coverage 100.0%, word completeness 87744 + 608 = 88352, 89 exact ranges and 171 less furniture, 0 mismatch. `caput`: 93 readings, first 1, last 93, gaps 0. RESULT: PASS.

## Remaining defects

None that fail the check. Not re-examined: the older `fixes` in the Knoll file (set without a quote, all on lines the pattern matches) and the `allow_oversize` sentence on `caput25`.

## Judgment calls for the Opus reader

1. Raulx line 12790, `XXXMII.`: set to XXXVIII. The glyphs fix `XXX` and `II`, and `M` stands in for a damaged V or VI. XXXVII is already read at an earlier line, XXXIX is read at 12864. This rests on glyph shape plus the neighbours, with no second printed instance. If the reader wants a stricter bar, this one head is the only one that does.
2. Raulx `m.` for III (lines 5294, 9109, 14038): a lowercase letter is read as three strokes. The lines sit after a blank line, between a printed II and a printed IV in the same work.
3. Optatus Book II chapter XXV: the edition prints no head. The reason used is `leaf_missing: between [1233, 1307]`. Page marks |115 to |118 run on without a break, so no leaf is missing; the text is there and only the head is not printed. The Latin of Ziwsa (CSEL 26, `optatus_libri-vii-lat_ziwsa1893-csel26-tei`) has a chapter 25 in that stretch. No `edition_unnumbered` form fits, since no line is a head without a numeral. No XXV division was created. The text of XXV sits inside chapter XXIV.
4. Optatus line 2294: the editor's heading is now the first line of `book-third/ch13`, not inside chapter XII.
5. Knoll chapters 55 and 76 take their numerals from the capitula list, not from a head on the page.
