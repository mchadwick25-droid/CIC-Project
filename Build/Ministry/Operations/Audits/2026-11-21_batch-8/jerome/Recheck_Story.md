# Recheck: Jerome

Batch 8, 2026-11-21. The one recheck, on `Recheck_Story_Prompt.md`. Independent checker; did not write, review or revise this story.

## Verdict: FIX

## The fix

**B2's clause names the wrong man on one hearing.** The sentence has three "he"s. The first two ("he marked", "he differed") are Jerome. The third ("which he held") follows them, so a listener takes it as Jerome too. The source is Augustine's own esteem for the Septuagint ("whose authority is worthy of highest esteem", AUG 25155–25157). The outline's Also told (line 8) and beat 4 (line 44) both say "which Augustine held".

Replace:

> unless he marked where he differed from the old Greek, which he held in the highest esteem.

with:

> unless he marked where he differed from the old Greek, which Augustine held in the highest esteem.

The fix adds no words.

## 1. Review findings

- **B1.** Fixed in the outline (Q3, line 58) and in the story, word for word. The Do not say line is added.
- **B2.** The clause is restored, but it needs the fix above.
- **M1 to M4, M7 and M8** are applied. M6 is cleared by M8.
- **M5** is withdrawn for length. I judge that acceptable. With "many of his Bible prefaces" the story would be 677 words, over the cap. The paragraph is about his Bible work at Bethlehem, so "many prefaces" does not mislead. The Also told part on the prefaces is still present.

## 2. New wording: Q3, checked clause by clause against AUGL 20546–20556

- *factus est tantus tumultus in plebe … ut* → "Such an uproar broke out in the congregation that". Faithful. "Tantus … ut" is kept as "Such … that".
- *maxime Graecis arguentibus* → "The Greeks above all found fault with the reading". Faithful. *Arguere* means to charge with error. "The reading" supplies the object the Latin leaves implied, as Cunningham does ("correcting what had been read", AUG 32546–32548).
- *et inflammantibus calumniam falsitatis* → "and fanned the charge that it was false". Faithful. "Fanned" keeps *inflammare*, and nothing is added.
- *cogeretur episcopus … Iudaeorum testimonium flagitare* → "the bishop was forced to demand the Jews' testimony". Faithful. *Flagitare* means to demand.
- *Oea quippe ciuitas erat* → "The town was Oea." Faithful.

The Latin ablative absolute is made its own sentence and set first. "Such" then ties the uproar back to the Greeks' outcry, so the chief accusers and the cause stay in the order Augustine gives them. Every clause is kept, nothing is added, and the longest sentence is 18 words. The quote in the story matches the outline's Q3 exactly.

The rest of the new wording is held:
- "a brother": the review's fallback cut.
- "Years later he wrote of what it cost…": M1.
- "Jerome wrote that there were almost as many forms…": M2, from the Gospels preface (JW 46631–46635).
- "he wrote", at the funeral crowd: M3, JW 8109–8117.
- The gloss on the Greeks: M4, and the outline's Words to explain.
- "a bishop at Oea": M8.

## 3. The kit lines

- **Hook:** four sentences. M1 split one long sentence in two, so it is still about three.
- **Essence:** complete at "copies", about word 151 by the scorer.
- **Also told:** the Roman women, Paula and Palladius, the prefaces, Rufinus, Augustine, Oea, the reconciliation and the force are all present.
- **Words to explain:** each one the story uses gets its plain sense the first time it is heard. The gloss on the Greeks now comes before Q3.
- **Sentences:** the longest is 31 words (the B2 sentence), within about 30.
- **Length:** 674 by the scorer, under about 675.
- **Setting:** not stacked in one sentence.
- **Ending:** on Jerome's own words.

## 4. Score

`python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-21_batch-8/jerome/jerome.brief.txt`: 674 words, grade 7.6 (names out 6.6), reading ease names out 76.7, 16.4 words a sentence, 0.3 joining words per 100, 17% short sentences, longest sentence 31 words. Pass, with the note that grade 7.6 is under 8. On the listener read it is not flat.
