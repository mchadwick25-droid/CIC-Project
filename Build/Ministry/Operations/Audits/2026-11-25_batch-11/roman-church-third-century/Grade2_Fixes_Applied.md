# Grade 2 fixes applied: roman-church-third-century

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `roman-church-third-century/Fixes_Grade2.md`
- `roman-church-third-century/Recheck_Grade2.md`

## Backup

- `roman-church-third-century.brief.v5.txt` (copy of the live brief before any change)

## Changes and status

| Change | File | Status |
|---|---|---|
| Brief 1 (Natalius reason) | roman-church-third-century.brief.txt | applied |
| Brief 2 + cut g (confessors deceived) | roman-church-third-century.brief.txt | applied |
| Cut a | roman-church-third-century.brief.txt | applied |
| Cut b | roman-church-third-century.brief.txt | applied |
| Cut c | roman-church-third-century.brief.txt | applied |
| Cut d | roman-church-third-century.brief.txt | applied |
| Cut e | roman-church-third-century.brief.txt | applied |
| Cut f | roman-church-third-century.brief.txt | applied |
| Sheet Z3 cell 1 | Source_Sheet.md | applied |
| Sheet Z3 quote cell | Source_Sheet.md | applied |
| Sheet new row N7a (recheck: CyL 6748) | Source_Sheet.md | applied |
| Outline line 120 (Ending 1) | Outline.md | applied |
| Outline Cut first 24 | Outline.md | applied |
| Outline Cut first 27 | Outline.md | applied |
| Outline Cut first 33 (new) | Outline.md | applied |

## Counts and checks

- `wc -w roman-church-third-century.brief.txt`: **675** (recheck expects 675)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/roman-church-third-century/roman-church-third-century.brief.txt: 673 words, grade 8.3 (names out 7.3), reading ease names out 75.7, 18.7 words a sentence, 0.6 joining words per 100, 6% short sentences, longest sentence 35 words - pass
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/roman-church-third-century/roman-church-third-century.brief.txt: 3 to look at
  s 12  names a source           Hippolytus says Callistus did it because he feared Hippolytus, and to clear himself of the charge that he shared Sabellius's view.
  s 15  names a source           Hippolytus says Callistus let people off for sins of the body, saying he forgave them all.
  s 20  modern-scholar word      Some years after Callistus, as a later historian tells it, all the brothers and sisters met to choose a bishop by vote, and set Fabian on the bishop's seat.
```
