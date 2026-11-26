# Grade 2 fixes applied: alexandria-catechetical

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `alexandria-catechetical/Fixes_Grade2.md`
- `alexandria-catechetical/Recheck_Grade2.md`

## Backup

- `alexandria-catechetical.brief.v3.txt` (copy of the live brief before any change)

## Changes and status

| Change | File | Status |
|---|---|---|
| Brief 1 (Origen counted her death as her baptism) | alexandria-catechetical.brief.txt | applied |
| Brief 2 (cut 1a) | alexandria-catechetical.brief.txt | applied |
| Brief 3 (cut 1e) | alexandria-catechetical.brief.txt | applied |
| Sheet line 72 (recheck version) | Source_Sheet.md | applied |
| Outline line 86 (Quote 1) | Outline.md | applied |
| Outline Cut first items 13-14 (recheck version) | Outline.md | applied |
| Fixes_Grade2: brief new sentence 2 ("The words suggest she was burned to death ...") | (see text) | Withdrawn by recheck (BLOCKING 1) |
| Fixes_Grade2: brief cuts 1b, 1c, 1d | (see text) | Withdrawn by recheck (MINOR 2) |
| Fixes_Grade2: Outline line 140 (Do not say) | (see text) | Withdrawn by recheck; line stands as it was |
| Fixes_Grade2: Outline Cut first items 15-16 and the "These four pay for the 21 words" line | (see text) | Withdrawn by recheck; replaced by items 13-14 as listed above |
| Fixes_Grade2: Source_Sheet line 72 and Outline line 86 versions | (see text) | Replaced by the recheck versions (applied above) |

## Counts and checks

- `wc -w alexandria-catechetical.brief.txt`: **628** (recheck expects 628)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/alexandria-catechetical/alexandria-catechetical.brief.txt: 625 words, grade 9.7 (names out 8.6), reading ease names out 70.7, 20.8 words a sentence, 0.3 joining words per 100, 3% short sentences, longest sentence 37 words - pass
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/alexandria-catechetical/alexandria-catechetical.brief.txt: 2 to look at
  s  3  well past 30 words (37)  Nearly all we know of these classrooms comes from Eusebius of Caesarea, writing about a century later from letters and from people who had known Origen, and he tells of the pupils who were put to death.
  s 24  possible bare statement  In the district of Arsinoe, in the Egyptian countryside, his teaching had held for a long time, and whole churches had broken away and fallen away.
```
