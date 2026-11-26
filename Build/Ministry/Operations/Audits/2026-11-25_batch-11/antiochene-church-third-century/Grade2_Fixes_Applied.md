# Grade 2 fixes applied: antiochene-church-third-century

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `antiochene-church-third-century/Fixes_Grade2.md`
- `antiochene-church-third-century/Recheck_Grade2.md`

## Backup

- `antiochene-church-third-century.brief.v4.txt` (copy of the live brief before any change)

## Changes and status

| Change | File | Status |
|---|---|---|
| Fix 1 (recheck wording) | antiochene-church-third-century.brief.txt | applied |
| Fix 3 (Malchion cut) | antiochene-church-third-century.brief.txt | applied |
| Outline line 71 tag | Outline.md | applied |
| Outline line 72 (recheck version) | Outline.md | applied |
| Outline line 73 (recheck version) | Outline.md | applied |
| Outline line 135 (Who tells it) | Outline.md | applied |
| Sheet new row L4-ANF | Source_Sheet.md | applied |
| Sheet line 123 (recheck version) | Source_Sheet.md | applied |
| Fixes_Grade2: Fix 2 (Lucian "but his letter does not say why"), brief | (see text) | Withdrawn by recheck (BLOCKING 1); live sentence stands |
| Fixes_Grade2: Outline line 73 change | (see text) | Replaced by the recheck guard text (applied above) |
| Fixes_Grade2: Fix 1 wording, Outline line 72, Source_Sheet line 123 texts | (see text) | Replaced by the recheck texts (applied above) |
| Card edit for the Malchion judgment (`antiochene-church-third-century.card.json`) | (see text) | NOT APPLIED: the recheck says the card pass needs to add it but gives no card text, and no text was supplied to apply word for word |

## Counts and checks

- `wc -w antiochene-church-third-century.brief.txt`: **665** (recheck expects 665)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/antiochene-church-third-century/antiochene-church-third-century.brief.txt: 665 words, grade 8.0 (names out 7.2), reading ease names out 74.5, 17.5 words a sentence, 0.9 joining words per 100, 21% short sentences, longest sentence 37 words - pass
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/antiochene-church-third-century/antiochene-church-third-century.brief.txt: 6 to look at
  s  7  well past 30 words (37)  When their own bishop was charged with refusing to confess that the Son of God came down from heaven, the bishops of the East met again and again over him, until at last they put him out.
  s  9  names a source           They wrote that Paul said Jesus Christ was from below, and Eusebius says he held that Christ was by nature an ordinary man.
  s 10  names a source           Bishops hurried to Antioch from every side, Eusebius says, as against a man ravaging Christ's flock, and they met there often while Paul's side hid what he taught.
  s 28  run of 3 short sentences I am a Christian.
  s 31  names a source           Later, in Alexandria, a presbyter named Arius said that the Son of God had a beginning, and God had none.
  s 34  modern-scholar word      A church historian of the next century, on Arius's side, says that some of Lucian's pupils became bishops.
```
