# Fresh read, gathered: John Chrysostom (`john-chrysostom`)

Copied from `Fresh_Trust.md` and `Fresh_FirstTime.md`, not reworded.

## Counts

### Fresh_Trust.md

| Mark | Count |
|---|---|
| HELD | 26 |
| SUMMARY HOLDS | 11 |
| SOFTENED OR CHANGED | 0 |
| ASSUMPTION ADDED | 0 |
| MODERN ONLY | 0 |
| NOT FOUND | 0 |

### Fresh_FirstTime.md

1. Test lines unfilled: 0. Who: a preacher at Antioch, then bishop of Constantinople. What happened: preaching, bishop, rebukes, two councils, exile, death on the way, body brought home. What it was about: plain words on the poor and to the powerful. Why on the tree: "His sermons were read for centuries", and his followers' return.
2. Opening, after three sentences: who, where, when (399) and why there all present. Nothing missing.
3. Sentences failing on one hearing: 0 that lose the thread. Small losses under 7.
4. Bare statements: 1 (BLOCKING, below).
5. Citations read aloud not called for: 1 ("In a sermon on Matthew"). Socrates, Palladius and the later bishop are called for: the sources differ, a motive, one partisan witness.
6. Tells Part 1 names: 0. No dash, no "not X but Y", no stock word, no moral close.
7. Unexplained words: 4 ("chief chamberlain", "Matthew", "minutes", "Comana" unplaced). Runs of short one-act sentences: 0. Talking down: none.
8. Opening pulls me in: yes, strongly. Attention first drifts at "Socrates, a church historian of the city writing a generation later, says Theophilus also held a grudge…": the narrator turns to who-wrote-what, and the Oak paragraph keeps that up with two witnesses. It holds, because the charges are concrete. I would listen to the end.

Tools: readability 756 words, grade 8.9, reading ease 69.2, pass. Craft check, 5 lines: s5 "John said" is a person in the story, fine; s9 is not bare, the next sentences explain it; s21 "historian" is an ancient one and the motive needs its witness, fine; s25 the sources differ, credit called for, fine.

## Verdicts

- Fresh_Trust.md: **Verdict: PASS.** Nothing BLOCKING. One MINOR, optional.
- Fresh_FirstTime.md: Verdict: REVISE (1 BLOCKING, 7 MINOR)

## Findings

### BLOCKING

Fresh_FirstTime.md:

**B1. BLOCKING — bare statement.** "He rebuked many others in office too, and those rebukes made him powerful enemies." Rebukes of whom, for what, is never said (Part 1, Explain it). Change: cut the sentence. The next sentence ("Theophilus also held a grudge") still reads.

### MINOR

Fresh_Trust.md:

**MINOR 1 (optional; apply word for word or note).** "They honored the bread of Communion, which Christians call Christ's body, on the altar with gold cups and silk." The homily puts the gold cup and the gold cloths on the table ("offer for this table a gold and jewelled cup", N110 29908-29909; "furnish His table with cloths bespangled with gold", 29960-29961), not on the bread itself. Exact change: "They decked the altar, where the bread of Communion lies, which Christians call Christ's body, with gold cups and silk." Not blocking: the meaning and force hold, and the quote that follows says "honor him here with silk clothes".

Fresh_FirstTime.md:

**M1. MINOR — citation and unexplained name.** "In a sermon on Matthew he told them" → "In one sermon he told them". A listener with no church background does not know who Matthew is.

**M2. MINOR — unexplained word.** "The emperor's chief chamberlain, Eutropius," → "Eutropius, the emperor's chief chamberlain, who ran his household,". Note: the trust reader checks "ran his household" against the source; if it is not supported, keep the line as it is.

**M3. MINOR — unexplained word.** "summed up the meeting's own minutes" → "summed up the meeting's own written record".

**M4. MINOR — unclear referent.** "They honored the bread of Communion" → "The rich honored the bread of Communion".

**M5. MINOR — unclear phrase.** "seeing the church of Antioch still turning to John" → "seeing the church of Antioch still looking to John". Left as is, the listener can still follow.

**M6. MINOR — place unplaced, death on the road unclear.** "Near Comana he asked for white clothes" does not tell me he had not reached Pityus. Noted only: if the outline holds that he died on the way, "On the road, near Comana," says it. The trust reader decides.

**M7. MINOR — length, noted.** The brief has 756 words. The outline's provisional figure is about 650, and the kind kit's ceiling is about 675. The bar does not block on length. The cut of B1 saves 14 words. The rest is left to Mark's ruling on length.

## Applied

Applied to `john-chrysostom.brief.txt` (backup before this batch: `john-chrysostom.brief.v2.txt`):

1. Fresh_FirstTime B1 (cut the sentence)
   - Before: "He rebuked many others in office too, and those rebukes made him powerful enemies."
   - After: (cut)
2. Fresh_Trust MINOR 1
   - Before: "They honored the bread of Communion, which Christians call Christ's body, on the altar with gold cups and silk."
   - After: "They decked the altar, where the bread of Communion lies, which Christians call Christ's body, with gold cups and silk."
3. Fresh_FirstTime M1
   - Before: "In a sermon on Matthew he told them"
   - After: "In one sermon he told them"
4. Fresh_FirstTime M3
   - Before: "summed up the meeting's own minutes"
   - After: "summed up the meeting's own written record"
5. Fresh_FirstTime M5
   - Before: "seeing the church of Antioch still turning to John"
   - After: "seeing the church of Antioch still looking to John"

### Noted, not applied

- Fresh_FirstTime M2: "The emperor's chief chamberlain, Eutropius," to "Eutropius, the emperor's chief chamberlain, who ran his household,". The finding says to keep the line as it is if the trust reader does not support "ran his household". `Fresh_Trust.md` does not check that phrase. Not applied.
- Fresh_FirstTime M6: "Near Comana he asked for white clothes" (no exact wording given; the read says "On the road, near Comana," only if the outline holds that he died on the way, and leaves it to the trust reader).
- Fresh_FirstTime M7: length (756 words against about 650 and about 675), left to Mark's ruling.
- Do not say lines: neither read gives a new line. `Fresh_Trust.md` only lists the existing Do not say list as honored. Nothing added to `Outline.md`.

### Could not apply

- Fresh_FirstTime M4: "They honored the bread of Communion" to "The rich honored the bread of Communion". After Fresh_Trust MINOR 1 replaced the whole sentence, the old text is found 0 times (it had been found once before). Both findings rewrite the same sentence and no wording of my own is allowed, so the two cannot be joined.

### Scorer

`python -m engine.m1.profile_readability john-chrysostom.brief.txt`:

Build/Ministry/Operations/Audits/2026-11-24_references/john-chrysostom/john-chrysostom.brief.txt: 742 words, grade 8.8 (names out 8.2), reading ease names out 69.9, 19.0 words a sentence, 0.4 joining words per 100, 13% short sentences, longest sentence 35 words - pass

