# Curation redo report: knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929

Drafter: Sonnet 5.5. File: `Sandbox/answering-library/curation/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.yaml` (62,214 words by the brief; 62,548 by the checker's count).

## Time and effort

- Start 2026-10-30T00:11:49Z, end about 2026-10-30T00:17Z. About 5 minutes.
- Check runs: 2 (baseline, after the edit).
- Entries added or changed: 1 new `fixes` entry (line 3668), 1 pattern widened, 1 `ocr_map` entry, 4 evidence entries, 0 explicit divisions, 0 `expected_gaps`. Status set to `drafted`.

## What was wrong

Series `pionius-chapter` (act 10) read 1, 5, 6 and so on. Chapters II, III and IV were never divisions, so their text sat inside chapter I:

- II, line 3624, printed `Il.`: OCR read lower-case l for I. Pattern class widened to `[IVXLl]`, `ocr_map` `{'l': 'I'}`.
- IV, line 3688, printed `; . IV.`: stray marks before the numeral. Pattern now accepts a prefix of `; ` or `. ` marks, or a margin line number.
- III, line 3668, printed `HI.` after OCR debris on the same line: set by a `fix` with quote `HI. LMeocev`.

The existing fix at 3906 (printed `VII.`, set to VIII) is unchanged.

## Final check output

class after: curated (was partial). Divisions 58 (56 body, 2 apparatus). Rule hits: act 33, pionius-chapter 23.
All checks PASS: uniqueness, coverage 100.0%, oversize 0, rules and evidence, word completeness 62548 = 62548, 190 of 190 byte ranges exact. Series pionius-chapter: 23 readings, first 1, last 23, no repeats, backward steps or gaps. Series act: 33 readings, no defects. RESULT: PASS.

## Remaining defects

None in the numbering. One `warn` line remains, listing 71 hand-listed lines inside the Pionius range that the look-alike scan takes for headings. They are not chapter heads: they are the editors' verse numbers inside the Greek text (for example `3. adxotw ...`), apparatus footnote lines, and running heads. The only roman-numeral heads in the range are the 23 now read. The warn does not change the result and the checker was not changed.

## Judgment calls for the Opus reader

- Chapter III (line 3668) is set although Knopf prints `HI.` only. The second printed instance is the vendored Gebhardt edition (`gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt`, the text Knopf says it follows): it prints `III. Προσευξαμένων` (OCR: `III. MNooosvsausvav de avıav`) with the same opening words, and its running head on page 97 reads `Martyrium S. Pionii III. IV.`. Sequence alone was not the basis.
- Chapter IV and chapter V are likewise printed in Gebhardt (`IV. Eotnoav`, running head, and `V. Tovrav`). Chapter II: Knopf `Il.` is read through the one `ocr_map` entry; Gebhardt's own II head is OCR-damaged to `I.`, so it adds no support beyond the sequence and the matching text.
- Line 3906 (VIII): Knopf prints `VII.` a second time; Gebhardt prints `VIII. Πάλιν δὲ Πιονίῳ εἶπεν Πολέμων` (running head page 102 for VII and VIII). This was the earlier fix and is now backed by that counterpart.
- The `ocr_map` entry `l` to `I` applies only to lines in the hand-listed range 3607 to 4442.
