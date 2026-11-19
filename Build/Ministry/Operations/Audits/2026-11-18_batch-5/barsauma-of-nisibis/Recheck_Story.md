# Recheck: Barsauma of Nisibis (story)

Independent checker, batch 5, 2026-11-18. I did not write, review or revise this story. Checked against `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `barsauma-of-nisibis.brief.txt` and `barsauma-of-nisibis.brief.v1.txt`.

**Verdict: PASS**

## 1. Review findings

- **B1** (486 told as marriage only): fixed. Paragraph 7 now gives the confession of Christ, the order on the wandering men in black, and the marriage rule. Outline Do not say line 128 is honoured.
- **B2** (hostile charge dropped): fixed. The charge is credited to "a hostile chronicle of the 1100s" alone (Do not say line 129).
- **B3** (424 point missing): fixed. The 424 sentence follows the essence (Do not say line 130).
- **M1, M2a, M2b, M3:** done as the review gave them. M5 is resolved by M2a. M6 needed no change.
- **M4:** not changed. The review marked it optional. The reviser's reason holds: the outline fixes 605 as the close, and the legend's letter is later than both 506 and 605, so the move would not give time order either.

## 2. New wording

Every sentence that differs from v1 is held at the lines cited:

- "The Persian church had run its own affairs since 424; what his synods set apart was its teaching and its rules." Held by Outline 7, 12 and 80, and by S4 (Source_Sheet 44).
- "In April 484 came the break." Held by Outline 10 and 46. "The break" is the quarrel itself, which the next sentence names.
- "A hostile chronicle of the 1100s, built on old men's memories, says he made the marriage rule so he would not be blamed for her." Held by Outline 46 and 100 and Source_Sheet 85. I re-read it at MS 33594–33596: "Il définit qu'aucun prêtre, diacre ou évoque ne serait sans femme, afin de n'être pas blâmé lui-même à cause de la courtisane". The right witness is credited, and the sentence says no more than the source. Michael places this rule at Beth Edrai. The story names no place, so nothing is moved.
- The 486 confession and the wandering men. Held by Outline 6, 23 and 49 and by E11. I re-read them at SO 19739–19746 ("deux natures ... mélange ... confusion") and SO 19752–19760 ("fourbes ... vêtements noirs"). The story says less than the canon, never more.
- "It quoted Beth Lapat's ruling on Theodore." Held by Outline 46 (E6, "known only as quoted by a synod of 605"), 55 and 80. This also honours Do not say line 113.
- "That historian, writing in the 1100s", "in an unknown year", "And it barred bishops ..." and "It called the synod left out of the book ...": these are cuts or re-joins of v1's wording. Nothing in them is new.

No quote is new. The existing quotes are unchanged from v1, and the review re-read each one in `cic/texts/`.

## 3. Kit lines

- **Hook:** three sentences (paragraph 1). PASS.
- **Essence:** its own sentences end at word 140, "set the Persian church apart." The 424 sentence, which B3 requires, completes it at **word 161**, "its rules." **Judgment: this is within "about 150".** The overrun is 11 words, about 4 seconds heard. The added clause is part of the essence's meaning: it stops the listener hearing "set apart" as "made independent", which Do not say bars. Cutting it to reach 150 would bring that misreading back. PASS.
- **Also told:** all parts are present. That covers the frontier letters, the plea with the king's threat, Beth Lapat's charges, and Babowai's death in all three credited versions. It also covers 486 with all three rulings, Narsai in one clause, 491, and the marriage in all three credited versions. PASS.
- **Church words:** synod, catholicos, clergy, deacon (as "assistant ministers"), canons (as "rules"), excommunication, marzban (as "the Persian governor"), nun, cell, concubine, Mar and Syriac Orthodox (as "the rival Syriac church") each get their plain sense where first heard. The new wording uses no listed word. "Two natures" is given only as its plain sense. PASS.
- **Sentence length:** the longest is 30 words. PASS.
- **Length (ruling 8):** 748 words, about 5 minutes. The new material is what B1 to B3 and M1 require. I find no part the story does not need.
- **Setting:** brought in a clause at a time, not stacked. PASS.
- **Ending:** it closes on the opening's image and on "the blessed Mar Barsauma". PASS.

## 4. Score

`python -m engine.m1.profile_readability`: 748 words, grade 8.8 (names out 7.8), reading ease (names out) 70.5, 17.8 words a sentence, 10% short sentences, longest sentence 30 words. Pass.
