# Grade 2 fixes applied: marcion-marcionism

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `marcion-marcionism/Fixes_Grade2.md`
- `marcion-marcionism/Recheck_Grade2.md`

## Backup

- `marcion-marcionism.brief.v5.txt` (copy of the live brief before any change)

## Changes and status

| Change | File | Status |
|---|---|---|
| Fix 1 (paragraph 4) | marcion-marcionism.brief.txt | applied |
| Sheet line 87 (recheck correction, range 16289) | Source_Sheet.md | applied |

## Counts and checks

- `wc -w marcion-marcionism.brief.txt`: **656** (recheck expects 656)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/marcion-marcionism/marcion-marcionism.brief.txt: 657 words, grade 9.6 (names out 8.6), reading ease names out 67.5, 19.3 words a sentence, 0.2 joining words per 100, 9% short sentences, longest sentence 33 words - pass
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/marcion-marcionism/marcion-marcionism.brief.txt: 6 to look at
  s 10  names a source           Tertullian, a writer at Carthage, in North Africa, says Marcion was cast out for his restless curiosity, which spread to others.
  s 11  names a source           Irenaeus, a bishop writing within a generation, says Marcion cut from both books every passage that called the maker of the world the Father of Jesus.
  s 21  names a source           He was said to be, Eusebius writes, a bishop of the Marcionites, eager for religion as he understood it, but without true knowledge.
  s 22  possible bare statement  When the persecutions ended, the emperor Constantine issued an edict, a law addressed by name to the Marcionites and other heretics, those who, their enemies said, chose error.
  s 23  possible bare statement  Their teaching, it said, made the healthy soul sick.
  s 30  not X but Y              Theodoret worked to bring them to his own faith, that Christ was, as he wrote, not only good but just.
```
