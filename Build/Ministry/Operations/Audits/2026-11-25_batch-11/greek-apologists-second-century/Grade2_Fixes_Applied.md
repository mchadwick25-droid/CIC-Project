# Grade 2 fixes applied: greek-apologists-second-century

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `greek-apologists-second-century/Fixes_Grade2.md`
- `greek-apologists-second-century/Recheck_Grade2.md`

## Backup

- None. The recheck leaves the brief unchanged, so no backup was made and the brief was not touched.

## Changes and status

| Change | File | Status |
|---|---|---|
| Outline Do not say (two lines, recheck version) | Outline.md | applied |
| Sheet row after line 41 (recheck version) | Source_Sheet.md | applied |
| Sheet row after line 69 (recheck version) | Source_Sheet.md | applied |
| Sheet line 176 (Library sweep, Used) | Source_Sheet.md | applied |
| Fixes_Grade2: brief rows 1, 2, 2a, 3-8 | (see text) | Withdrawn by recheck; brief untouched, no backup made |
| Fixes_Grade2: Outline lines 63, 64, 65, 66, 68 and Cut first item 25 | (see text) | Withdrawn by recheck |

## Counts and checks

- `wc -w greek-apologists-second-century.brief.txt`: **675** (recheck expects 675)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/greek-apologists-second-century/greek-apologists-second-century.brief.txt: 675 words, grade 8.4 (names out 7.5), reading ease names out 72.2, 17.3 words a sentence, 0.7 joining words per 100, 8% short sentences, longest sentence 38 words - pass
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/greek-apologists-second-century/greek-apologists-second-century.brief.txt: 5 to look at
  s  4  well past 30 words (38)  Accused of being godless, of eating human flesh and of incest, they answered that they worshipped the one God who made all things and prayed for the emperors, and they asked to be judged by how they lived.
  s  8  modern-scholar word      Eusebius, a church historian, still had the book in the early 300s.
  s 14  possible bare statement  Under Marcus Aurelius, Justin was condemned and put to death for refusing to sacrifice to the gods and obey the emperor's command.
  s 20  names a source           If the charges were true, Athenagoras said, let the emperors destroy the Christians root and branch.
  s 30  possible bare statement  But the friend believed the rumors, and thought Christian books were new and their teaching nonsense.
```
