# Curation redo: augustine_doctrina-christiana-enchiridion-lat_bruder1838

Drafter: Sonnet 5.5. File: `Sandbox/answering-library/curation/augustine_doctrina-christiana-enchiridion-lat_bruder1838.yaml` (78,524 words). Status set to `drafted`.

## Time and effort

- First session 2026-10-30T02:39Z to about 02:55Z (baseline, stopped on order). Resumed 2026-10-30T20:28Z, passing check and PR at about 20:35Z. About 7 minutes on resume.
- Check runs: 5 in total (baseline, then 4 on resume; the first resume run only reported an unreadable numeral).
- Entries added: 27 `fixes` (plus 6 existing), 5 `ocr_map` lists changed, 5 patterns changed, 1 explicit division removed (line 9521, now a fix), 61 evidence entries added. 0 `expected_gaps`.

## What was wrong

Chapter heads are OCR-damaged roman numerals. The old pattern read only `C.` plus clean letters, so about 40 heads were not divisions at all and every series showed gaps (9, 3, 6, 4 and 14).

- Pattern: now accepts `C` with a period or comma, a missing period (`C XI.`), a leading `<` (`<C. XXXVI.`), and damaged numeral glyphs. `Caput L` at 1860 still lands.
- `ocr_map` (per series, only glyphs that occur): `l 1 i` as I everywhere. Doctrina 2: `T`=I, `H`=II, `F`=I. Doctrina 3: `T`=I, `U`=II, `H`=II. Doctrina 4: `Y`=V, `T`=I. Enchiridion: `H`=II, `U`=II, `n`=II, `[`=I.
- `fixes` with a quote, for heads whose glyphs are beyond a map: doctrina1 1991, 2547, 2724, 2882; doctrina3 5197, 5310, 5622, 5893, 6399; doctrina4 8770; enchiridion 9521, 10460, 10511, 10606, 10905, 11047, 11545, 11649, 11658, 11716. The six earlier fixes (4363, 4372, 6255, 8541, 9431, 11470) stay.
- Line 11545 prints `V . LXXIX.`: the numeral is clean, the `C.` is damaged. Line 2547 prints `i\ XX\ I.`.

## Second instance for each damaged numeral

- Doctrina 1, 2, 4 (chapters 7 to 31) and the Enchiridion: the front-matter argumentum prints a clean Arabic number with a summary. Each damaged head's opening words match the summary of the number set. The argumentum line is in `evidence` beside the head line.
- Doctrina 3 and doctrina 4 chapters 1 to 6: the argumentum is missing (a leaf is lost near line 644), so no in-file instance exists. The second instance is the English chapter in `npnf102_augustine-city-of-god-christian-doctrine.xml` (same chapter numbers; Shaw's numbering), compared by opening words. The evidence list holds only the head lines for these, since evidence can quote only this file. Affected heads: doctrina3 5197, 5310, 5499, 5622, 5893, 5960, 5975, 6006, 6255, 6399; doctrina4 6720, 6831.
- Enchiridion heads were also compared with `npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml`.
- Running heads print page numbers only, not chapters. No cross-reference was needed.

## Final check output

class after: curated. divisions 279 (278 body, 1 apparatus). Rule hits doctrina1 40, doctrina2 42, doctrina3 37, doctrina4 31, enchiridion 122.
All checks PASS (uniqueness, coverage 100.0% of 78102 body words, oversize 0, rules and evidence, word completeness 78524 = 78524, 357 of 357 byte ranges exact).
Per series: doctrina1 40 readings, first 1, last 40, gaps 0; doctrina2 42, first 1, last 42, gaps 0; doctrina3 37, first 1, last 37, gaps 0; doctrina4 31, first 1, last 31, gaps 0; enchiridion 122, first 1, last 122, gaps 0. No repeats, backward steps or unreadable numerals. RESULT: PASS.

The 43 `warn` lines left are lines beginning `C`, `Cal.`, `Christ-` and the like, picked up by the wider pattern. They are not headings.

## Remaining defects

None open. No `expected_gaps`; the edition prints every chapter 1 to 40, 1 to 42, 1 to 37, 1 to 31 and 1 to 122.

## Judgment calls for the Opus reader

- 2724 `C. XWI.` set to XXXI and 2882 `C. XXWI.` set to XXXVI. W stands for a merged pair (XX in the first, XV in the second). The reading rests on the glyphs, the argumentum summaries for 31 and 36, and the neighbours 2578 (27) and 2751 (32).
- 2547 `i\ XX\ I.` set to XXVI: `\` is V here, the C is lost. Argumentum 26 matches.
- 1991 `C. \T.` (VI), 5310 `C. \T1.` (VII): `\` is V and `T` is I. In 5622 `XV\` and 5893 `XXV^` the last mark is debris, not a letter.
- 4363, 4372, 8541 and 9431 end in `L` (`XXVIL`, `XXVIIL`, `XXIL`, `XVL`): read as the numeral with a damaged full stop. The earlier fixes stay; argumentum and NPNF support 27, 28, 22, 16.
- 9521 `C. XV''!!!.` set to XVIII; 11716 `C. LXXX^'!!.` set to LXXXVII; the apostrophes and bangs are damaged letters. Argumentum 18 matches; NPNF 87 matches (argumentum 87 is lost).
- `Ij`, `Tj`, `rj` before X are L (10460, 10606, 10905, 11047, 11649, 11658); `\L` at 10511 is XL.
- The `ocr_map` entries `H`, `U`, `n` as II and `Y` as V are claims about this scan, each backed by the heads above. A reader should check that none of these letters stands for a different numeral elsewhere in the series.
- The checker was not changed. It reports no gap now; the sequence was not used to set any numeral without a content match (argumentum or NPNF).
