# Recheck: Gregory of Nyssa (batch 9)

Read: `Review.md`, `Revision.md`, `gregory-of-nyssa.brief.txt`, `gregory-of-nyssa.brief.v1.txt`. No `Outline.md` or `Source_Sheet.md` exists, so the changed sentences are traced to the sources `Review.md` cites in `cic/texts/`.

## Verdict: FIX

One change, same word count:

- Replace: "He also wrote the life of his sister Macrina,"
- With: "Gregory also wrote the life of his sister Macrina,"

Why: the sentence before it is "Christ, he writes, frees humanity from evil and heals even the devil, who brought evil in." Its subject is Christ, and the last person named is the devil. "He" at the start of the next sentence attaches to Christ on one hearing, so a listener hears Christ writing the life of "his sister". The reviser's flag is right. This is a misattribution a listener cannot recover. It also stops "He also wrote" being heard twice (paragraph two already has "He also wrote that the Holy Spirit..."). Nothing else needs to change.

## 1. Findings in Review.md

- 1 BLOCKING (Macrina, the soul and the resurrection): fixed with the review's wording. The stock how-we-know sentence is gone.
- 2 MINOR (cleansing): fixed.
- 3 MINOR ("the one who brought evil in"): fixed as "the devil, who brought evil in".
- 4, 5 MINOR: no change was directed, and none was made. Agreed.
- 6 MINOR (card, "Against Eunomius XII" should be "II"): this is a card fix for step 6, so it stays open. Not a story matter. Agreed.

## 2. Changed sentences against the sources

- "restored, after long and painful cleansing, and all creation gives thanks": Great Catechism 26, npnf205 44413-44418 ("after long periods of time ... restoration of those who are now lying in Sin ... a harmony of thanksgiving will arise from all creation ... in the process of the purgation have suffered chastisement"). "Painful" is held at 44405 ("the separation is agonizing") and 44427 ("the chastisement, however painful"). The words are Gregory's own, and the sentence says no more than he does.
- "heals even the devil, who brought evil in": 44425-44426 ("healing even the introducer of evil himself"). The same passage calls him "the adversary" (44406). Held.
- "the life of his sister Macrina": `gregory-nyssa_life-of-macrina_clarke1916.txt`, Creator line (Gregory of Nyssa), and the introduction at line 58 ("Gregory's account of his sister's life"). The sentence does not claim it is "the only" life. Held.
- "a dialogue on the soul and the resurrection in which she, near death, answers his grief": On the Soul and the Resurrection, npnf205 38083-38103 ("she too was lying in a state of prostration even unto death ... she tried to check me by speaking, and to correct ... the disorder of my soul"). Gregory's own witness, credited to him. Held.
- The unchanged quotes still match the text word for word: "received the legacy of Eunomius' controversy" at 2788 (the approved modern rendering), "is above every name" at 8957-8958, and "of the same rank as the Father and the Son" at 27944.

## 3. Shape

- The hook is unchanged. It names him by the third sentence.
- The essence is unchanged. Eunomius comes at about word 102, "above every name" at 130, the Spirit at about 145-155, and the 381 law is complete at about word 184 (by whitespace count). This is just past 150. It is approved wording, the review accepted it, and the revision did not move it.
- What else is also told: the Spirit, endless growth, the restoration, and now Macrina and the dialogue on the soul and the resurrection. All are present.
- No new word needs explaining. "Cleansing", "dialogue" and "devil" are plain.
- The new sentence is 26 words. The 33-word sentences are approved wording (finding 5). No sentence runs well past 30 words.
- Length: there is no outline. The brief is 310 words by the scorer's count, against about 299 approved. The +11 is the net the review set for the blocking fix. Accepted.
- The ending is still on Trullo and his own canons (finding 4). It is not wrong.

## 4. Score

`python -m engine.m1.profile_readability .../gregory-of-nyssa.brief.txt`: 310 words, grade 9.6 (names out 8.2), reading ease (names out) 69.1, 18.2 words a sentence, longest sentence 33 words. **Pass.** The fix above does not change the word count.

## Applied (coordinator, 2026-11-22)
The replacement above applied word for word to `gregory-of-nyssa.brief.txt`.
