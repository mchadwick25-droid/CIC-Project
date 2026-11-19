# Card check: Bardaisan of Edessa

Card checker, batch 6 (2026-11-19), under `Card_Check_Prompt.md`. Read: `bardaisan-of-edessa.brief.txt`, `bardaisan-of-edessa.card.json`, `Card_Edits.md`, `Card.existing.json` (identical to the census card for `bardaisan-of-edessa`), and each cited line in its file.

**Verdict: FIX** (one change below).

## 1. Each edit is justified

- **datesNote, "about 223" to "about 222".** Justified. Barhebraeus gives "obiit anno 533" (BHE 4221). Holl converts that to 221/2 (EPI 26427). The 223 comes from Hort, as McGiffert reports him (EU 26586–26588). The brief says "He died about 222", so the old card contradicted it.
- **uncertain[2], sentence added.** Justified. McGiffert's claim that Ephrem "knows him only through his followers" (EU 26574–26577) is contradicted by Ephrem's own held words. Ephrem says "I have chanced upon a book of Bardaisan" (Gwynn, npnf213 11200), and he writes of "the book (called) 'Of Domnus'" (EPH-P 1372). McGiffert's view stays on the card, attributed to him. One correction to the evidence, not the card: `Card_Edits.md` cites the heading at EPH-P 1350–1352. Burkitt calls the collection's title "Of Domnus" a scribe's choice (EPH-P 2592). Ephrem's own naming of the book is at EPH-P 1372.
- **sources.about, six entries added.** Justified. Each supports a sentence of the brief: Gwynn (11200–11202, 11241–11247, 11261–11270), Jerome in English and Latin (npnf203 40139–40151; PL 23 53437–53442), Thomas Smith on the Recognitions, the Chronicle of Edessa (line 49), and Barhebraeus (4220–4221).
- **briefReferences, 16 lines.** Each was checked against the brief. One part names something the brief no longer tells (FIX 1).
- **quotationOriginals, three entries.** Each modern span is word for word in the brief. Each printed wording stands at its lines in anf08, which is in `sources.ownWords`.

## 2. Nothing else moved

A field-by-field diff against `Card.existing.json` shows only the listed changes: datesNote, uncertain[2], six entries added at the end of sources.about, and the new briefReferences and quotationOriginals. Every other field is word for word and in order.

## 3. References

One part names something the brief no longer tells. The brief says only that a Latin scholar "called it the strongest of his books". It does not tell "most famous", or Jerome's point about its force in translation.

**FIX 1.** `briefReferences[11]`
- Old: "Jerome, Lives of Illustrious Men 33, in Latin and English: On Fate the most famous and strongest of his books, and its force even in translation."
- New: "Jerome, Lives of Illustrious Men 33, in Latin and English: On Fate the strongest of his books."

Every other reference names only what the brief tells, or the source a told claim comes from.

## 4. Census rules

The card uses only allowed keys and has no `briefLength`. There are three entries for the brief's three quoted spans, and none extra. Every cited file is in `sources`. No briefReferences entry has quotation marks. No audit, review or ruling is named. Spelling is American. No entry has a `secondReading` yet: all three spans are new and wait for step 7.

## 5. Originals

All three quotes are rendered from Pratten's English. Cureton's Syriac is not held, and the outline cites no original. Nothing is missing.

## 6. Not found, and anything clearly wrong left in

- **"Ephrem attacked Bardaisan as one of the worst of heretics in his Prose Refutations."** Ruling: keep it. The words "one of the worst" are not found as such. But the substance stands. The Prose Refutations are written against Mani, Marcion and Bardaisan as the chief false teachers, under the heading "Mani, the last of the great heretics" (EPH-P 957). They attack Bardaisan throughout. No held source contradicts the line.
- Nothing else in the card is clearly wrong.
