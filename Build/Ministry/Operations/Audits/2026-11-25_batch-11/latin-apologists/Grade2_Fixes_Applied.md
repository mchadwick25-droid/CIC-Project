# Grade 2 fixes applied: latin-apologists

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `latin-apologists/Fixes_Grade2.md`
- `latin-apologists/Recheck_Grade2.md`

## Backup

- `latin-apologists.brief.v4.txt` (copy of the live brief before any change)

## Changes and status

| Change | File | Status |
|---|---|---|
| B1 (split essence sentence) | latin-apologists.brief.txt | applied |
| B2 (Octavius sentence, with "sometimes") | latin-apologists.brief.txt | applied |
| Outline beat 2 | Outline.md | applied |
| Outline Cut first note | Outline.md | applied |
| Sheet line 59 | Source_Sheet.md | applied |
| Fixes_Grade2: brief change 1 (new first sentence) and 1a | (see text) | Withdrawn by recheck (BLOCKING 1) |
| Fixes_Grade2: brief change 2 | (see text) | Replaced by recheck B2 (applied above) |
| Fixes_Grade2: Outline Openings 1 change | (see text) | Withdrawn by recheck; stands as it was |
| Fixes_Grade2: Outline beat 2 and Cut first note | (see text) | Replaced by the recheck versions (applied above) |
| Fixes_Grade2: Source_Sheet "no change" | (see text) | Replaced by the recheck sheet line 59 change (applied above) |

## Counts and checks

- `wc -w latin-apologists.brief.txt`: **673** (recheck expects 673)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/latin-apologists/latin-apologists.brief.txt: 671 words, grade 9.1 (names out 7.8), reading ease names out 72.7, 18.6 words a sentence, 0.1 joining words per 100, 8% short sentences, longest sentence 37 words - pass
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/latin-apologists/latin-apologists.brief.txt: 5 to look at
  s 11  names a source           He and others like him, Octavius says, once believed them too.
  s 20  modern-scholar word      Jerome, a Christian scholar writing later, says the Roman clergy's envy and insults drove Tertullian to the New Prophecy.
  s 30  names a source           Arnobius's pupil, Jerome says, was Lactantius, called to teach rhetoric at Nicomedia, a Greek city in Bithynia.
  s 31  names a source           He was teaching there when, Lactantius says, the emperor's officers burned the Christians' Scriptures and leveled their church, on a day picked to end Christianity.
  s 36  well past 30 words (37)  Of the writers known to him, Lactantius wrote, Minucius Felix had stood well among the pleaders, and his Octavius showed how fit a champion of truth he might have been, had he given himself wholly to it.
```
