# Card check: Clement of Alexandria

Checker, 2026-11-18. Starting card: the census `card` for `clement-of-alexandria` in `cic-website/data/world-census.json`.

**Verdict: FIX** (three `briefReferences` parts).

## 1. Edits justified

Edits 1–18 confirmed. Re-read: ANF2 27489-27492, 27891-27893 (note 1853, Gal. iii. 24), 28146-28148, 28315; JER 16628-16629, 16634-16636. The two unchanged spans keep their census `secondReading`; the four new or changed spans correctly have none.

## 2. Nothing else moved

Diff against the census card: only `briefReferences` and `quotationOriginals` changed, each change listed. Key order kept.

## 3. References that remain

1. Stromata I.1: the search for teachers, "found rest". 2. Eusebius V.11: Pantaenus. 3. Stromata IV.2: the Miscellanies patched together (**FIX**). 4. Jerome, Lives 38, and Alexander: a presbyter. 5. VI.10 and I.9: masks, "bare faith alone", the vine. 6. I.5: the guide, the pædagogus. 7. I.7: "whatever has been well said". 8. II.20: martyrs burnt (**FIX**), impaled, beheaded. 9. Eusebius VI.11, VI.14: Alexander's letters. 10. Jerome, Letter 70: the critic, "the most learned of men", Origen's Miscellanies. 11. Eusebius VI.6, Jerome, Lives 38: Origen his pupil. 12. I.21 and Eusebius VI.6: around 200, after the death of Commodus (**FIX**). 13. I.5 note: Paul, Galatians 3:24. 14. I.7: what men falsified. 15. IV.10: not handing oneself over. 16. Eusebius V.11, VI.6–14: most of his life, a century later.

## 4. Census rules

Allowed keys only; no `briefLength`. Six quoted spans in the brief, six entries, each `printed` verbatim at its lines. All cited files in `sources`. Remaining quotation marks in `briefReferences` ("found rest", "bare faith alone", "whatever has been well said", "the most learned of men") are verbatim in the brief. No audit named. Spelling: "burnt" (FIX 2) now stands outside quotation marks, so it is no longer printed wording.

## 5. Not found

- Valentinus's letters: found at ANF2 32722 and 34289; the claim stands.
- McGiffert, "long honored as a saint": a fair paraphrase of "in ancient times commemorated as a saint"; it stands.
Nothing clearly wrong left in beyond the FIXes.

## FIX

1. `briefReferences[2]`. The brief says only "which he called Miscellanies".
   - Old: `Stromata IV.2: the Miscellanies patched together.`
   - New: `Stromata IV.2: the Miscellanies.`
2. `briefReferences[7]`. American spelling, as in the brief ("burned").
   - Old: `Stromata II.20: martyrs burnt, impaled, beheaded every day.`
   - New: `Stromata II.20: martyrs burned, impaled, beheaded every day.`
3. `briefReferences[11]`. The brief names no Commodus.
   - Old: `Stromata I.21, and Eusebius, Church History VI.6: written around the year 200, after the death of Commodus.`
   - New: `Stromata I.21, and Eusebius, Church History VI.6: written around the year 200.`
