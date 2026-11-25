# Grade 2 fixes applied: manichaeism

Applied word for word from `Fixes_Grade2.md` (the fix pass), as corrected by `Recheck_Grade2.md` (the recheck governs). Nothing added, reworded or judged.

## Source files

- `manichaeism/Fixes_Grade2.md`
- `manichaeism/Recheck_Grade2.md`

## Backup

- `manichaeism.brief.v4.txt` (copy of the live brief before any change)

## Changes and status

| Change | File | Status |
|---|---|---|
| Fix 1 (843 reason) | manichaeism.brief.txt | applied |
| Fix 2 (Augustine, recheck wording) | manichaeism.brief.txt | applied |
| Trim a | manichaeism.brief.txt | applied |
| Trim b | manichaeism.brief.txt | applied |
| Trim c | manichaeism.brief.txt | withdrawn by recheck |
| Trim d | manichaeism.brief.txt | applied |
| Trim e | manichaeism.brief.txt | applied |
| Trim f | manichaeism.brief.txt | applied |
| Trim g | manichaeism.brief.txt | applied |
| Trim h | manichaeism.brief.txt | applied |
| Trim i | manichaeism.brief.txt | applied |
| Trim j | manichaeism.brief.txt | applied |
| Trim k | manichaeism.brief.txt | applied |
| Trim l | manichaeism.brief.txt | applied |
| Trim m | manichaeism.brief.txt | applied |
| Sheet line 106 (843 row) | Source_Sheet.md | applied |
| Sheet new row B26a (recheck version) | Source_Sheet.md | applied |
| Sheet line 94 (alms row) | Source_Sheet.md | applied |
| Outline 72 (beat 6) first | Outline.md | applied |
| Outline 72 (beat 6) second | Outline.md | applied |
| Outline 69 (beat 3) | Outline.md | applied |
| Outline 44 (Words to explain, alms) | Outline.md | applied |
| Outline after line 45 (the Uyghurs row) | Outline.md | applied |
| Outline 220 (Cut first 21) | Outline.md | applied |
| Outline 138 (Who tells it, CHI row) | Outline.md | applied |
| Outline new Cut first item 32 (recheck version) | Outline.md | applied |
| Outline recount line (recheck version) | Outline.md | applied |
| Fixes_Grade2: brief trim (c) "owned only a day's food" to "owned a day's food" | (see text) | Withdrawn by recheck (BLOCKING); "only" kept |
| Fixes_Grade2: Fix 2 brief text ("who would set the Hearers free") | (see text) | Replaced by the recheck text "who would free the Hearers" (applied above) |

## Counts and checks

- `wc -w manichaeism.brief.txt`: **840** (recheck expects 840)
- Scorer (`python -m engine.m1.profile_readability`):

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/manichaeism/manichaeism.brief.txt: 833 words, grade 8.6 (names out 7.4), reading ease names out 74.9, 18.5 words a sentence, 0.8 joining words per 100, 7% short sentences, longest sentence 40 words - pass
```

- Craft check (`python tools/check_brief_craft.py`), reported, not acted on:

```
Build/Ministry/Operations/Audits/2026-11-25_batch-11/manichaeism/manichaeism.brief.txt: 11 to look at
  s 10  modern-scholar word      He wrote a book for King Shapur of Persia, and Biruni, a Muslim scholar of about 1000, quotes how it begins.
  s 11  names a source           Mani says God's messengers brought wisdom and deeds to people from age to age: the Buddha to India, Zoroaster to Persia, Jesus to the West.
  s 13  possible bare statement  He said he was the Paraclete, the Helper Jesus had promised, and he wrote his own scriptures.
  s 21  names a source           Biruni says King Bahram had Mani hunted down, and gives the king's reason: "This man has come forward calling people to destroy the world.
  s 24  names a source           A book by one of his pupils, which Biruni reports, says he failed to cure a relative of the king and was chained in prison until he died.
  s 26  names a source           Augustine says he asked why they honored it far above Easter.
  s 28  modern-scholar word      After Mani's death, a Baghdad scholar of the 900s says, the king killed his followers wherever he found them, and they fled east into the lands of the Turks.
  s 30  possible bare statement  Faustus of Milevis, a bishop of theirs, wrote a book answering their opponents' questions on the gospel, and Augustine, a Hearer for nine years, kept his words, quoting each part before answering.
  s 35  possible bare statement  Christians brought Faustus before the governor's court, and, found to be a Manichaean, he was exiled to an island.
  s 37  well past 30 words (41)  In 732 a Chinese emperor's order called Mani's teaching a perverse belief that falsely took the name of Buddhism and deceived the people, and forbade it, though the foreigners from the West, whose own religion it was, might keep it themselves.
  s 38  names a source           A later emperor's letter says China let the faith grow because the Uyghurs, a Turkish people, revered it.
```
