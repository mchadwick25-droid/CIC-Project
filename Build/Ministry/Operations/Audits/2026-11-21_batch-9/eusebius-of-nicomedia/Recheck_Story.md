# Recheck: Eusebius of Nicomedia (`eusebius-of-nicomedia`)

Brief rechecked: `eusebius-of-nicomedia.brief.txt` against `eusebius-of-nicomedia.brief.v1.txt`, `Review.md`, `Revision.md`, `Outline.md` and `Source_Sheet.md`.

## Verdict: PASS

## 1. Findings in Review.md

- **B1 (Ulfila's setting): fixed.** Paragraph 9 now gives both settings: Philostorgius's "sent by the Goths to Constantine's court" and the modern historian's "under Constantius instead". This matches the Do not say line (Outline 97-98).
- **B2 (Alexander's answer): fixed.** "Alexander told the bishops to ignore his letters." is back in paragraph 3, as cut-first item 4 requires (Outline 17).
- **M1 (held-back reveal): fixed.** The hook names Arius and Eusebius from the start.
- **M2 (letters to bishops) and M3 (grain ships): listed in Revision.md as not made, for length.** I judge this acceptable. Both are minor compressions the outline itself carries (beat 1, Outline 35; beat 4, Outline 38). Neither tells a witness's claim as fact; the grain charge is still Socrates's, and he still calls it slander.
- **M4 (Paul): fixed** by role only, as the outline's Names line gives him (Outline 52).

## 2. Changed sentences, traced

- "Arius, a priest driven out of Alexandria, wrote to Eusebius, bishop of Nicomedia, and greeted him as a fellow pupil of Lucian, a teacher at Antioch who died a martyr." Outline Openings 1 (Outline 32) and Lucian's gloss (Outline 26); THD 6062-6066 ("my fellow-Lucianist", paraphrased, not quoted, per Outline 94).
- "He told him why he was being hounded: [Q1]." Q1 is unchanged and is the slate's lifted wording; THD 6045-6046 confirms the sense ("We are persecuted, because we say that the Son has a beginning, but that God is without beginning").
- "Eusebius answered by taking up his cause." THD 6127-6130 ("When Eusebius received the epistle ... wrote to Paulinus"); Outline 32.
- "Alexander told the bishops to ignore his letters." SOC 2168-2169: "pay no attention to anything that Eusebius should write to you." Credited to Alexander. Says no more than the source.
- "Jerome, writing about forty years later, names Eusebius of Nicomedia." Only "in Latin" removed; Outline 39, JER 45287-45293.
- "...removed the bishop of Constantinople, and moved Eusebius to the emperor's new city." Only "Paul" removed; SOC 5885-5890.
- "Philostorgius says Ulfila, sent by the Goths to Constantine's court, was made their bishop by a bishop named Eusebius." PHI 120: "sent by the then king of the Goths on an embassy to the court of the emperor Constantine ... ordained ... by Eusebius and the other prelates that were with him." Credited to Philostorgius.
- "A modern historian takes this to be Eusebius of Nicomedia, and sets it under Constantius instead." DUC 20993-20995: "une ambassade à la cour de Constance. Eusèbe de Nicomédie le vit ... le consacra". Credited to the modern historian.

No new quote. All checked in `cic/texts/` at the lines above.

## 3. Shape

- **Hook:** paragraph 1 leads straight into the essence. Pass.
- **Essence:** complete by word 118 ("...written by his enemies."); the acts are complete by word 107. Under 150. Pass.
- **Also told:** the letter, the three accounts of Nicaea, the exile and return, the campaign against Athanasius, the baptism in Jerome's account, the party, and Ulfila are all present. Pass.
- **Words to explain:** "the condemnation", "the tyrant", Lucian and "of one being" are each glossed where first heard. Pass.
- **Sentence length:** longest is 30 words (the new hook's first sentence), within about 30. Pass.
- **Length:** 673 words, under 675. Pass.
- **Ending:** on the person, with the two witnesses' names for him. Pass.

## 4. Score

`python -m engine.m1.profile_readability .../eusebius-of-nicomedia.brief.txt`: 673 words, grade 9.2 (names out 6.6), reading ease names out 73.6, 14.6 words a sentence, longest sentence 30 words: pass.
