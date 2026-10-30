# Curation redo: augustine_doctrina-christiana-enchiridion-lat_bruder1838

Drafter: Sonnet 5.5. Stopped early on a coordinator order. The yaml is unchanged and `status` stays `needs-redo`.

## Time and effort

- Start 2026-10-30T02:39Z, stop about 2026-10-30T02:55Z.
- Check runs: 1 (baseline). Entries added: 0.

## Series state

Done: none. Left: doctrina1, doctrina2, doctrina3, doctrina4, enchiridion. The baseline check output is unchanged: RESULT FAIL, only "rules and evidence" fails, on 9, 3, 6, 4 and 14 unexplained steps in the five series.

## Findings so far

- The check's look-alike warns cover about 41 damaged heads. Another group is not warned about because the pattern misses a missing period or a comma after the C (for example line 2144 `C XI.`, 2157 `C, Xll.`, 2269, 2414, 2454, 2816, 2964, 5499 region, 9460, 11027, 12331). The pattern needs `[.,]?` after the C, and an `<` before it (line 6453 `<C. XXXVI.`).
- Damaged glyphs seen: `\`, `T`, `W`, `F`, `H`, `^`, `V'`, `ij`, `rj`, `Tj`, `[`, `n`, `U`. Some read two ways: `XFil` (line 3536) and `XVH` (3942) could each be more than one numeral. These need a second printed instance before they are set.
- Second instances available in the file:
  - Front-matter argumentum (lines 361 to 1100) lists a topical summary for every Book 1 and Book 2 chapter and for Enchiridion chapters 1 to 122, with clean Arabic numbers. Compare each chapter's opening words with its summary.
  - The summaries for Book 3 chapters 5 to 37 and Book 4 chapters 1 to 6 are missing from the scan (a leaf is lost around line 644). Entries `C. 7` to `C. 31` under the Book 3 heading at lines 651 to 704 are Book 4's summaries. Book 3 and Book 4 chapters 1 to 6 therefore have no argumentum instance.
  - `cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml` (Christian Doctrine) and `npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml` (Enchiridion, from line 19982) are English translations with chapter numbers. Use them for the opening-words comparison, especially for Book 3 and Book 4.
- Running heads print page numbers only, not chapters.

## First thing to do on resume

Widen the shared pattern to accept `[CGO0<][.,]?`, add the glyph entries to `ocr_map` per series (`\`:V, `T`:I and so on, only where the glyph is unambiguous), run the check, then set each remaining damaged head by `fixes` with a quote after comparing its opening words with the argumentum summary or the NPNF chapter. Any head with no second instance is reported and goes in `expected_gaps` only with a reason a reviewer can check.
