# Grade 2 fixes applied: syriac-edessa-nisibis

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `syriac-edessa-nisibis/Fixes_Grade2.md`
- `syriac-edessa-nisibis/Recheck_Grade2.md`

## Backup

- `syriac-edessa-nisibis.brief.v4.txt` (copy of the live brief before any change)

## Changes and status

| Change | File | Status |
|---|---|---|
| Cut: November of the year 201 | syriac-edessa-nisibis.brief.txt | applied |
| Cut: and it destroyed | syriac-edessa-nisibis.brief.txt | applied |
| Cut: Aphrahat letters for the church | syriac-edessa-nisibis.brief.txt | applied |
| Cut: hoping that want would | syriac-edessa-nisibis.brief.txt | withdrawn by recheck |
| Cut: In his prose writings | syriac-edessa-nisibis.brief.txt | applied |
| Fix 1 (paragraph 9, recheck version) | syriac-edessa-nisibis.brief.txt | applied |
| Recheck: so that lust | syriac-edessa-nisibis.brief.txt | applied |
| Recheck: broke through the wall | syriac-edessa-nisibis.brief.txt | applied |
| Sheet after line 129 (two lines, 16236-16237) | Source_Sheet.md | applied |
| Sheet line 176 | Source_Sheet.md | applied |
| Outline line 61 (beat 6) | Outline.md | applied |
| Outline line 186 (Cut first 15) | Outline.md | applied |
| Outline Cut first item 31 (recheck version) | Outline.md | applied |
| Fixes_Grade2: brief cut "hoping that want would" to "hoping want would" | (see text) | Withdrawn by recheck (MINOR 2); not applied |
| Fixes_Grade2: brief paragraph 9 new text ("A bishop came to Persia as a Roman envoy ...") | (see text) | Replaced by the recheck text (applied above) |

## Counts and checks

- `wc -w syriac-edessa-nisibis.brief.txt`: **654** (recheck expects 654)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/syriac-edessa-nisibis/syriac-edessa-nisibis.brief.txt: 647 words, grade 7.5 (names out 6.6), reading ease names out 80.0, 18.0 words a sentence, 0.3 joining words per 100, 3% short sentences, longest sentence 38 words - pass (note: grade 7.5 is under 8: the listener read checks it is not flat)
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/syriac-edessa-nisibis/syriac-edessa-nisibis.brief.txt: 3 to look at
  s  5  possible bare statement  In the 300s they sang their teaching in hymns and counted among them men and women vowed to God for life.
  s 10  well past 30 words (38)  One of his letters asks them to keep watch at night, to sing psalms and pray, to give their goods to the poor, and not to live with the other sex, so lust will not draw them back.
  s 27  names a source           Marcion taught a Stranger God, apart from the Maker of the world; Mani taught two first Roots, Light and Darkness; and Bardaisan said the world was made from five first beings.
```
