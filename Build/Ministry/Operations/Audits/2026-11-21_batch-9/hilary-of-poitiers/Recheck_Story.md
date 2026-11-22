# Recheck: Hilary of Poitiers (`hilary-of-poitiers`)

Reviewer, batch 9, 2026-11-22. Read `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `hilary-of-poitiers.brief.txt` and `hilary-of-poitiers.brief.v1.txt`. Changed lines were checked against `cic/texts/`.

## Verdict: FIX (length only)

Every finding is fixed and every new sentence is held. The story is 698 words by the scorer, 23 over the 675 cap. That is BLOCKING under the batch header. All six Cut first items are already gone. The heart and the record's force (Milan, the excommunications, Lucifer's dissent) must not be cut for length (Outline.md line 136). The fix below takes out only spare words and keeps every fact and credit. Applied together, the story is **674 words** by the scorer (grade 7.7, names-out reading ease 75.6, longest sentence 25 words, pass). Mark rules on the length either way.

## 1. Findings in `Review.md`

- B1, no age: fixed. "Martin, fresh from the army" (CSEL1 6382-6384).
- B2, Martin in the essence: fixed. The essence now ends at word 160 by the scorer.
- B3, Milan: restored as its own paragraph, with "the new emperor" (Outline.md lines 58, 130).
- B4, the excommunications: restored ("They cut off Auxentius and other Arian leaders from communion"). CSEL65 6918-6920 names Auxentius, Ursacius, Valens and others.
- B5, Lucifer: restored by role. NPNF211 11434-11440: he "separated himself from the communion of those who had received them", and Sulpicius "will not take upon me to say".
- M1, "only": removed.
- M2: not restored. `Revision.md` says it goes to the card. I agree: it is not part of the heart.
- M3 and M4: no story change, as the review said.

## 2. Changed sentences, by source

- "bishop of Poitiers in Gaul": PL23 60464-60465.
- "Before the exile, Martin, later bishop of Tours, had already sought him out.": Outline.md line 5; CSEL1 6382-6384.
- "Saturninus then deceived the emperor, Hilary says, and a faction had him exiled on false reports.": NPNF209 7773-7775; CSEL65 15364-15368. Both are Hilary's words, so "Hilary says" covers both. Cut first item 5 is honored.
- "In it he also wrote, as to brothers, ...": NPNF209 9850-9861; Outline.md line 126.
- "They cut off Auxentius and other Arian leaders from communion.": CSEL65 6918-6920. Holds. MINOR: Auxentius is first heard here with no role, and he only gets one in the Milan paragraph. The fix below gives him "bishop of Milan" on first hearing.
- Lucifer by role: NPNF211 11434-11440. "Exiled" is held by Outline.md line 98 ("fellow exile").
- Milan: PL10 49250-49260, 49277-49280. Hilary reports that Auxentius had "scripsisse" (written) that Christ is true God, of one godhead and substance with the Father, and that the emperor ("rex") then took communion with him. Hilary said "fingi omnia" (it was all a pretense) and was ordered "de Mediolano proficisci" (to leave Milan). "Signed" follows the outline's beat 7, but Hilary's word is "wrote". MINOR: the fix below says "wrote".
- "Only Hilary tells it.": Outline.md line 58.
- "Sulpicius wrote:" with quote 3 moved: Sulpicius was already credited as openly on Hilary's side. The quote matches CSEL1 5656-5658 and NPNF211 11433-11434.
- "Hilary died at Poitiers, in the sixth year after his return, about 367.": NPNF211 11441-11442; PL23 60530-60531; Outline.md line 132.
- Quotes 1 and 2 are unchanged and verbatim against PL10 43844-43848 and CSEL65 6815-6820.

## 3. Shape

- Hook: Hilary's own admission (quote 1). Holds.
- Essence: complete at word 160 by the scorer ("...had already sought him out."), a little past 150. Not a failure on its own, and the fix brings it to word 156.
- Also told: all five parts are present with their weight (the plea; On the Councils at the bishops' request; Seleucia and the refused hearing; the letter, the excommunications, pardon over shunning, and Saturninus; Milan).
- Words to explain: Nicaea, the two "substance" terms, Arian, exorcist, communion, Phrygia and Ariminum each get their plain sense when first heard. "Orthodox" (Milan) is unglossed. It is common enough at B2: MINOR, no change.
- No sentence runs past 30 words. The longest is 26.
- Length: 698, past the outline's 675. BLOCKING, fixed below.
- Ending: on the person's death, as in the outline's Ending 1. Holds.

## 4. Score

`python -m engine.m1.profile_readability .../hilary-of-poitiers.brief.txt`: 698 words, grade 7.9 (names out 6.6), names-out reading ease 75.7, 15.5 words a sentence, longest sentence 26 words. Pass. Grade 7.9 is under 8, but on the listener read it is not flat.

## FIX: exact replacements (−24 words by the scorer, 698 to 674)

Each line below keeps every fact and credit. Apply all of them.

1. "There he learned how the Eastern bishops were quarreling over the Son." → "There he learned the Eastern bishops' quarrel over the Son."
2. "who held that the Son was less than the Father" → "who held the Son was less than the Father"
3. "Before the exile, Martin, later bishop of Tours, had already sought him out." → "Before the exile, Martin, later bishop of Tours, had sought him out."
4. "rests on his own letters and on Sulpicius Severus" → "rests on his own letters and Sulpicius Severus"
5. "Sulpicius says that Martin, fresh from the army, stayed with him for a time." → "Sulpicius says Martin, fresh from the army, stayed with him a while."
6. "Martin refused, crying that he was unworthy." → "Martin refused, crying he was unworthy."
7. "So Hilary made him an exorcist, one who prayed over people" → "So Hilary made him an exorcist, who prayed over people"
8. "The office was so lowly that Martin could not refuse it" → "The office was so lowly Martin could not refuse it"
9. "communion, the sharing of the sacrament that shows churches belong together" → "communion, the shared sacrament that shows churches belong together"
10. "Hilary denounced the leaders of that side at a council in Béziers." → "At a council in Béziers he denounced that side's leaders."
11. "which we know as On the Trinity." → "now called On the Trinity."
12. "Then the bishops of Gaul asked him to tell them what the Eastern bishops had confessed" → "The bishops of Gaul asked him what the Eastern bishops had confessed"
13. "a faith that matched Nicaea" → "a faith matching Nicaea"
14. "In Gaul many wanted nothing to do with those who had signed." → "In Gaul many wanted nothing to do with the signers."
15. "They cut off Auxentius and other Arian leaders from communion." → "They cut off Auxentius, bishop of Milan, and other Arian leaders from communion." (+3; gives him his role on first hearing)
16. "Hilary accused Auxentius, the bishop there, who then signed a confession that sounded orthodox." → "Hilary accused Auxentius, who then wrote a confession that sounded orthodox." (Hilary's "scripsisse", PL10 49253)
17. "The new emperor took communion with him, and Hilary, calling it all a pretense, was ordered out of the city." → "The new emperor took communion with him. Hilary called it all a pretense and was ordered out of Milan."

Checked by applying all 17 to a scratch copy and running the scorer: 674 words, grade 7.7, names-out reading ease 75.6, longest sentence 25 words, pass. The essence then ends at word 156.

## Applied (coordinator, 2026-11-22)
All 17 replacements above applied word for word to the brief.
