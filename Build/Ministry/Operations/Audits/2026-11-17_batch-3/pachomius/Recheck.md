# Pachomius: recheck

Rechecker, 2026-11-17. Targeted recheck of `pachomius.brief.txt` (revised) against `Review.md`, `Outline.md`, `Source_Sheet.md`. Diffed against `pachomius.brief.v2.txt`.

## Verdict: FAIL

Both blocking findings are made. The revision fails on length (M5, now worse) and on a new timeline jump at his death that repeats the M1 problem in a new place.

## The three lines, from one hearing

- **Who:** Pachomius, a pagan-born conscript from Upper Egypt in Constantine's time, who became a Christian and gathered monks into a shared life under one rule at Tabennisi, in the fourth century.
- **What happened:** fed by Christians in prison, he vowed to serve people; baptized, trained under Palamon, built Tabennisi with common clothes, food and rules, hid from ordination, housed his sister and other women, survived a hearing and a sword attack at Esneh, and died of plague refusing a better blanket. His fellowship split after him.
- **Why the connection matters:** Jerome put the rules into Latin for Latin-speaking monks and nuns who wanted to live that way, and Benedict of Aniane later set them under Benedict's Rule as one it stood on.

## Findings

- **B1. Made.** Palladius's count now follows the split, says "who visited Egypt about seventy years later" and "monks there under the rule"; no longer heard as the Latin. Outline, What came of them 1; I1.
- **B2. Made.** "After his death his fellowship split, and Theodore, one of its leaders, wrote letters urging the breakaways back." Outline, What came of them 2 (Gennadius, I2); "one of its leaders" fits the outline's Petronius, Horsiesius and Theodore. Not "succeeded him", so the Do not say line is kept.
- **M1. Made in part; new problem.** Esneh now sits in the life, after the sister, and "he was not always welcomed" is gone. But his death is now told after the ninth century ("Pachomius himself had died ... 346 or 348"), so the listener again has to jump back in time, which is the same one-hearing problem in a new place. Fix: tell the death (plague, date, blanket) in the life after Esneh, before "After his death his fellowship split"; or end on the blanket with no pluperfect jump.
- **M2. Made.** "The Coptic Life says an angel..." (Bohairic 6247-6248).
- **M3. Made.** "A priest sent Jerome books that had come from Alexandria." Jerome 4336-4337.
- **M4. Made.** "in his houses and at Metanoia, near Alexandria" separates the Thebaid houses from Metanoia (Jerome 4342-4344; outline Connection).
- **M5. Not made; worse.** 480 words by the scorer (481 by `wc`), up from 474, against about 400 to 450.

## New in the revision

- Palamon's rule loses "hard work" (outline beat 2: "much manual work"), and "at the start he did all their work" loses "at the start" (beat 4: "At first"). Neither is false, but the second now reads as if he always did all their work. Restore "at first".
- "Athanasius of Alexandria visited": supported (outline Links: visited Tabennisi). "His own communities' Coptic Life gives the answer": supported (outline: Bohairic Life from his own communities).
- Every beat still names its Life: Coptic Life (prison, angel), Greek Life (Esneh, blanket), Palladius, Jerome, Benedict of Aniane. The "Lives say" voice and the "rules in a book" beat are unchanged.
- Quotes unchanged from the reviewed version; the review's verbatim checks stand.

## Score

`python -m engine.m1.profile_readability`: 480 words, grade 7.8 (names out 6.6), reading ease names out 78.5, 17.1 words a sentence, longest sentence 31 words. Pass, with the under-8 note; listener read: not flat.
