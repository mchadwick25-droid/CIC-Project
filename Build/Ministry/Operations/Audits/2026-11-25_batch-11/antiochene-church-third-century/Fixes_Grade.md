# Fixes from the batch grade: antiochene-church-third-century

Source of the findings: `Grades/listener.md` (antiochene-church-third-century: opening missing when; one thread-losing sentence; one bare statement) and `Grades/Held_Findings.json`. Ruling: Mark, "yes to all" (Decision-Log, "Batch 11: the eight briefs, Manichaeism's length and the grade fixes"). The brief is not edited here; these are the exact replacements to apply to `antiochene-church-third-century.brief.txt`.

Count: the live brief is 670 words (`wc -w`). With fixes 1 and 2 applied it is 670 words (`wc -w` on a scratch copy). `engine/m1/profile_readability.py --report` on that copy: grade 8.1, reading ease 74.0, 17.6 words a sentence, pass (live brief: grade 8.2, 73.9, pass).

## 1. Opening is missing when (applied)

The when is moved up, not added: the brief already says "Paul became bishop around 260" in its third paragraph. It now opens the story, and the third paragraph drops it.

Old (paragraph 1, sentence 1):
> The bishops who judged Paul of Samosata, bishop of Antioch, wrote that he had changed the psalms, the sacred songs, sung in his own church.

New:
> Paul of Samosata became bishop of Antioch around 260. The bishops who judged him wrote that he had changed the psalms, the sacred songs, sung in his own church.

Old (paragraph 3, start):
> Paul became bishop around 260. Almost all we know of him comes from the letter his judges sent out,

New:
> Almost all we know of him comes from the letter his judges sent out,

Content behind it (already held; nothing added to the outline or sheet):
- `Outline.md` line 30 ("Say 'around 260'") and beat 1, line 68 ("Paul becomes bishop, around 260").
- `Source_Sheet.md` S1 (line 33): Eusebius, `E-Eng 41784-41785, 41836`, later witness (a generation or two), Documented: Paul became bishop when Demetrianus died. S2 (line 35): Jerome's Chronicle, `JerChr 44213-44215`, later (c. 380), puts it in Gallienus's seventh year; "around 260" Widely Accepted.

Words: +3 in sentence 1, -5 in paragraph 3; net -2. No cut needed.

## 2. Thread-losing sentence (applied)

Old (last paragraph):
> Arius had sent that letter to one of them, a different Eusebius, bishop of Nicomedia, and ended the letter with their own name for the pupils of Lucian.

New:
> One was Eusebius, bishop of Nicomedia, not the historian. Arius had written to him about being driven out, and ended that letter with the name Lucian's pupils gave themselves.

What it fixes: "one of them" becomes a sentence of its own, saying this Eusebius was one of Lucian's pupils who became a bishop, and "not the historian" sets him apart from Eusebius of Caesarea. "That letter" now names the letter by what the listener heard of it in the paragraph before (Arius driven out of the city).

Content behind it (already held):
- `Source_Sheet.md` L6 (line 141): Philostorgius, `Philost 138`, later (c. 425), friendly to Arius's side, Documented as his report: Lucian's disciples include "Eusebius, bishop of Nicomedia".
- L5 (line 136): Arius's letter to Eusebius of Nicomedia, own words, Documented, `Thdt 6063-6064`, Greek `Epiph-Gk 45744-45746`; written when Alexander had driven him out (`Thdt 6005-6026`). Ar2 (line 138), `Thdt 6025-6027`: "He has driven us out of the city as atheists". Rechecked in `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` at those lines: the chapter is headed "The Letter of Arius to Eusebius, Bishop of Nicomedia", and the driving-out lines stand in that letter.

Words: +1 net. Paid by fix 1's -2, so no cut is taken.

## 3. Missing why: Lucian out of communion (not applied; no held source gives a reason)

Sentence, left as it is:
> Lucian, he wrote, kept out of communion with the bishops for many years,

No held source says why Lucian broke with the bishops. Alexander's letter, the only old witness (`Source_Sheet.md` L4, line 134; `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` 5757-5762, Alexander as Arius's enemy, c. 320s, Documented as his charge), gives the act only: "Lucianus, his successor, withdrew himself from communion with these bishops during a period of many years." The editor's note 295 (same file, 5760-5768) says whom he refused communion with (Domnus, Timaeus, Cyril) but gives no reason either, and it is a modern claim (L4-note: not usable). No other entry in the Source Sheet holds a reason.

Noted, not applied: in Alexander's text, "these bishops" points back to "a council of all the bishops" that put Paul out (5757-5759). That says with whom, not why, so it does not answer the listener's question, and adding it would invite the listener to infer a motive the source never states.

## Totals

Applied: 2. Not applied: 1 (no held source). Brief stays at 670 words. No word added needs a cut to the card or Leave out; nothing from the heart, the record's force or a Part 1 explanation is touched.
