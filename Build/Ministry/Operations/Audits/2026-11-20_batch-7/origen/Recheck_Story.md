# Recheck: Origen (story)

The independent recheck, batch 7, 2026-11-20, per `Recheck_Story_Prompt.md` and the change order of 2026-11-19. I did not write, review or revise this story. It was approved before the kit, so there is no `Outline.md` or `Source_Sheet.md`. New wording was traced to `Audits/2026-11-16_eight-standard-v1/drafts/origen.refs.md` and to `cic/texts/`. Read: `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entries named in the prompt, `Review.md`, `Revision.md`, `origen.brief.txt` and `origen.brief.v1.txt`.

## Verdict: PASS

## 1. Review findings, and nothing else changed

`origen.brief.v1.txt` is identical to the live census text (`world-census.json`, `origen` longDescription). A diff against v1 shows only B1 (", and Jerome says he died at Tyre" cut from paragraph 2) and B2 (the new Decius paragraph, the review's wording word for word). Every other sentence is unchanged from v1. M1 is for the card; M2 asked for no change.

## 2. New wording

- "Late in life, under the emperor Decius, Eusebius says he was chained and tortured, his feet stretched in the stocks for many days." Eusebius VI.39.5, `npnf201_eusebius-church-history-life-of-constantine.xml` 37484–37490 ("bonds and bodily tortures and torments under the iron collar … for many days with his feet stretched four spaces in the stocks"); Decius from the chapter title (37378); refs, "card-only" list. It says no more than Eusebius: not that he died of it (the judge strove "not to end his life", 37493; McGiffert's note 37510).
- "Jerome says he died at Tyre." Moved, not new: Jerome, Lives 54, `npnf203_theodoret-jerome-gennadius-rufinus.xml` 40589–40591. "Late in life" rests on the same lines ("until his sixty-ninth year").

## 3. Kit lines

- **Hook:** four sentences (paragraph 1). It is one scene, and it leads straight into the essence. Within "about three".
- **Essence:** complete at word **139** ("…where the old Greek fell short.").
- **Also told:** the Hexapla and Jerome's Job, the three senses and the Philocalia, Athanasius, Gregory and Athenodorus, the souls-before-birth dispute with Methodius, Pamphilus and Eusebius, 553, and now the Decius torture and the death at Tyre. All present.
- **Church words:** no outline list. Hexapla and Philocalia are glossed in the sentence.
- **Sentences:** longest 31 (M2), within "about 30".
- **Length:** 337 words, about 2:15. Nothing it does not need.
- **Setting:** a clause at a time.
- **Order and ending:** the death now comes after Caesarea, then the attacks and 553. The close on the acts of 553 is the story's point, "argued over for centuries".

## 4. Score

`python -m engine.m1.profile_readability`: 337 words, grade 8.7 (names out 6.6), reading ease names out 75.0, 15.3 words a sentence, longest 31. Pass.
