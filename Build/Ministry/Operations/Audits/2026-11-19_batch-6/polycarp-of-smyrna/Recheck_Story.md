# Recheck: Polycarp of Smyrna (story)

The independent recheck, batch 6, 2026-11-19, per `Recheck_Story_Prompt.md` and the change order of 2026-11-19. I did not write, review or revise this story. It was approved by Mark before the kit, so I checked only that the revision applied the review's fixes exactly and changed nothing else, plus the kit lines. Read: `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entries of 2026-11-19 "Batch 6: era 1 first …" and "Change order: the stories approved before the kit …", `Review.md`, `Revision.md`, `polycarp-of-smyrna.brief.txt`, `polycarp-of-smyrna.brief.v1.txt`, and the research in `Audits/2026-11-16_polycarp-clean-write/` (`Source_Sheet.md`). There is no outline.

## Verdict: FIX (one passage)

## 1. Review findings, and nothing else changed

`polycarp-of-smyrna.brief.v1.txt` is byte-identical to `Polycarp_approved.brief.txt`. A diff of the brief against v1 shows exactly B1, B2, M1, M2 and M3 as the review words them, and no other change. In B1 all five quoted sentences moved (the review said "four" but quoted five); that is right. M4 needed no change and M5 was optional. The added glosses hold: "meaning the Christians, who would not worship their gods" (ANF 3830–3835, "godly race of Christians"; 4055–4058, "not to sacrifice, or to worship the gods"); "the martyrs before him" (ANF 4226–4228 and note 471, "been athletes"); "Earlier" and "Decades after that visit" (Source_Sheet M9; source check S22, S28).

## 2. Kit lines

- **Hook:** the two-sentence answer. Within "about three".
- **Essence:** complete at word **85** by whitespace count ("...who had seen Jesus.").
- **Also told:** the letter, the Anicetus peace and its use against Victor, and the yearly gathering are all present.
- **Church words:** there is no outline list. The two words the review found unexplained (atheists, competed) now get their plain sense.
- **Sentences:** longest 24.
- **Length:** 478 words, about 3:10; M5's lion clause is the only part it does not need.
- **Ending:** on his own letter's words.
- **Setting: fails.** "Polycarp, an old man, gave that answer in a stadium in Smyrna, a city in the Roman province of Asia, in the second century." Four setting phrases (stadium, city, province, century) are stacked at the end of one sentence, which Part 1 bars. The fix below moves the province into the sentence that names his church, so the place and the time come in a clause at a time. No fact is added or lost.

### FIX

Replace

> "Polycarp, an old man, gave that answer in a stadium in Smyrna, a city in the Roman province of Asia, in the second century. The Roman governor had offered to free him if he would curse Christ. He was the bishop of the church there."

with

> "Polycarp, an old man, gave that answer in a stadium in Smyrna, in the second century. The Roman governor had offered to free him if he would curse Christ. Smyrna was a city in the Roman province of Asia, and he was the bishop of its church."

## 3. Score

`python -m engine.m1.profile_readability`: 478 words, grade 5.9 (names out 5.1), reading ease names out 83.1, 13.7 words a sentence, longest 24. Pass, with the under-8 note for the listener read.
