# Fixes from the batch grade: roman-church-third-century

Source of the finding: `Grades/listener.md` (roman-church-third-century: "Opening: missing when"). Ruling: Mark, "yes to all" (Decision-Log, "Batch 11: the eight briefs, Manichaeism's length and the grade fixes"). This pass fixes that one finding only. The listener's bare statement (the weeds parable) and the two `Grades/Held_Findings.json` entries (S003, S004) are outside this pass's brief and are not touched. The brief is not edited here; these are the exact replacements to apply to `roman-church-third-century.brief.txt`.

Count: the live brief is 678 words (`wc -w`). With the fix and its cuts applied it is 675 words (`wc -w` on a scratch copy). `python3 -m engine.m1.profile_readability --report` on that copy: 673 words by its count, grade 8.5 (names out 7.5), reading ease 75.3, 19.2 words a sentence, longest sentence 36 words, pass (live brief: 676 by its count, grade 8.5, 75.7, 19.3, pass).

## 1. Opening is missing when (applied)

The when goes into sentence 2, so it covers the whole Natalius episode, not only Zephyrinus's start. "Early in the 200s" is used, not "around 200", because no source dates Natalius's fall itself: it is placed only "in the time of Zephyrinus", whose time runs from about 199 to about 217.

Old (paragraph 1, sentence 2):
> Yet he let a group that taught that Christ was only a man make him their paid bishop.

New:
> Yet, early in the 200s, he let a group teaching that Christ was only a man make him their paid bishop.

Content behind it (already held; nothing added to the outline or sheet):
- `Outline.md` line 11 (When and where: "Rome, from Zephyrinus, bishop from about 200") and line 32 (Century and years: "Zephyrinus became bishop about the ninth year of Severus (S1): say 'around 200'"; his death "around 217").
- `Source_Sheet.md` S1 (line 28): Eusebius, `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` 32210-32211, "Zephyrinus was appointed his successor about the ninth year of the reign of Severus". Later witness (about 100 years); Documented; "about 200" Widely Accepted.
- Same file 32213-32214, checked at the lines: the Little Labyrinth's author "narrates another event which occurred in the time of Zephyrinus". The writer himself, a contemporary, puts it "not long ago, but in our own day" (32223-32224; `Source_Sheet.md` Z2, line 44). Documented that it fell in Zephyrinus's time.
- `Source_Sheet.md` S2 (line 29): the Liberian list, `cic/texts/liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt` 66792-66796, dates Zephyrinus from the consuls of 198 to those of 217 (Duchesne's bracketed years). S3 (line 30): Eusebius 35480-35482, he died after eighteen years. Later list; Documented that it says so.
- Confidence of the wording "early in the 200s": Widely Accepted, a plain span for 198/199 to 217.

Words: +4 ("early in the 200s").

## Cuts that pay for it (all Leave out)

The when adds 4 words. Seven come out, so the brief ends 3 under its current count and at 675. Each is a joining word or a framing phrase. None is from the heart, the record's force, a credit, a quote, or an explanation Part 1 requires. Each listed below is **Leave out** (wording only; nothing moves to the card).

1. Paragraph 1, the same sentence: "a group that taught that Christ" becomes "a group teaching that Christ" (−1, shown in the new text above).
2. Paragraph 4: "saying that he forgave them all" becomes "saying he forgave them all" (−1; the outline's own wording, beat 3, C7).
3. Paragraph 5: "Hippolytus charged that such women then took drugs" becomes "Hippolytus charged that such women took drugs" (−1).
4. Paragraph 6: "Fabian died a martyr, and Rome went without a bishop." becomes "Fabian died a martyr, leaving Rome without a bishop." (−1; the church without a bishop stays, D7).
5. Paragraph 7: "Cornelius was made bishop in 251, and counted his church:" becomes "Cornelius, made bishop in 251, counted his church:" (−2; the count stays as Cut first 31 leaves it).
6. Paragraph 8: "Cornelius wrote of how the people met them:" becomes "Cornelius wrote how the people met them:" (−1; the credit stays).

Net: +4 − 7 = −3. 678 becomes 675.

Considered and not taken: cutting "to the gods" after "sacrifice". Outline Cut first 30 lists it, but the fresh listener asked for it as an explanation (`Fresh_Listen.md` line 51; applied in `Fresh_Read_Applied.md`), so it stays. "One and the same" (Sabellius's teaching) stays as the outline's gloss (`Outline.md` line 44). "Threw himself down" stays as the opening's force.

## Totals

Applied: 1, with 6 cut edits (7 words) to pay for it. Not applied: none. No new content goes into `Outline.md` or `Source_Sheet.md`; every line cited was already there and was re-read in its file.
