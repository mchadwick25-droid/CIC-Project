# Recheck: Tacitus (story)

Batch 6, 2026-11-19, per `Recheck_Story_Prompt.md`. Read: `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entries "Batch 6: …" and "Change order: the stories approved before the kit…" (2026-11-19), and in this folder `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `tacitus.brief.txt`, `tacitus.brief.v1.txt`. Sources checked: TERT-C 4919 (`tertullian_opera-pars1-lat_reifferscheid-wissowa-csel20.txt`, *mendaciorum lo[quacissimus*); the sheet's D3 (SCH 24300–24304, 1922) and I1.

## Verdict: PASS

## 1. Review findings

- **B1.** Fixed. The essence is now complete at word 88 ("Pilate."). The reviser's one wording change, splitting the clause off as "In it he names their founder, Christus, put to death under Pilate.", is held by the outline's essence ("their founder, Christus, was executed … by Pontius Pilate") and beat 1. The split was needed for length and adds nothing.
- **B2.** Fixed, word for word. Held by Outline line 44 ("Historians of a century ago read the verdict this way: the inquiry proved they were Christians, not that they set the fire (D3)") and Words to explain. D3 is Schanz (1922), so "a century ago" is right. It is credited, not the narrator's. The Do not say line was added (line 112).
- **B3.** Fixed, word for word. Held by I1 ("an outside notice of Christus under Pilate") and the Connection ("a Roman's line that Christus was executed under Pilate"). The Do not say line was added (line 113).
- **M1–M5.** Each was made in the review's words. M2 now credits Tertullian ("he wrote"). M3–M5 are splits only.

Nothing is listed as unfixed.

## 2. New wording

The diff against v1 is exactly the eight changes above. Each is held at the lines cited, and none says more than its source. Q1, Q2 and Q3 match the outline's renderings word for word, and their Latin is held (SCH 24312–24318; TERT-L 17915–17916, TERT-C 4919).

## 3. The kit lines

- **Hook:** three sentences, with the name in the third. Pass.
- **Essence:** complete at word 88. Pass.
- **Also told:** every part is present: the chapter in its order, with the rites, the blame, the informers, the verdict, the deaths and his judgement; what it cannot tell; Tertullian; Sulpicius; the victims, the verdict's reading and the 1876 doubt. Pass.
- **Words to explain:** superstition, Judaea, Christus, "hatred of the human race" (now with its plain sense where it is first heard) and "exemplary" (as "as an example to all") are each explained. Pass.
- **Sentences:** the longest is 27 words. Pass.
- **Length:** 526 words, about 3:30, against the review's stated need of about 3:25. No part the story does not need. Pass.
- **Setting:** comes a clause at a time and is not stacked. Pass.
- **Ending:** on Tacitus's own judgement, in the gardens of the opening. Pass.

## 4. Score

`python -m engine.m1.profile_readability …/tacitus/tacitus.brief.txt`: 526 words, grade 8.3 (names out 7.3), reading ease names out 73.2, 17.0 words a sentence, longest sentence 27 words. Pass.
