# Recheck: Pliny the Younger (story)

Batch 6, 2026-11-19, per `Recheck_Story_Prompt.md`. Read: `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entries "Batch 6: …" and "Change order: the stories approved before the kit…" (2026-11-19), and in this folder `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `pliny-the-younger.brief.txt`, `pliny-the-younger.brief.v1.txt`. Sources opened: ML 2779–2780, 2811 (`mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`); EU 19540–19546 (`npnf201_eusebius-church-history-life-of-constantine.xml`).

## Verdict: FIX

## 1. Review findings

- **M1 (citizens).** Added as the review gave it. The sentence is held: Outline beat 1, "Roman citizens he sent to Rome (E3)"; Words to explain, "citizens were sent to Rome for trial (E3)"; ML 2780, *quia cives Romani erant, adnotavi in urbem remittendos*. But see the fix below: its place makes the next sentence say more than its source.
- **M2 (Eusebius's "checked").** Fixed. Held by Outline, What came 2 ("says the ruling checked the persecution to a degree … (I2)"), and EU 19543–19544, "was to a certain degree checked". Credited to Eusebius ("wrote that"), as Do not say requires.

Nothing is listed as unfixed.

## 2. New wording

The diff against v1 is exactly the two changes above. The M2 sentence says no more than I2. The M1 sentence is held, but placed before "He does not say what became of them, though later Christians took it that they died", it makes "them" heard first as the citizens. Later Christians' reading that the dead "died" is held only for those "led away" (Source_Sheet E2 note, D1; Outline essence, "that those 'led away' died is the later writers' reading"). What became of the citizens no held source says (D6). Heard once, the story now tells later Christians' reading of the citizens' fate, which nothing holds. This is a detail moved onto the wrong group.

**Fix.** Put the citizens after the sentence about those led away, so "them" is again those who held firm, as in v1. All the words stay.

Replace:

> surely deserved punishment." Roman citizens he sent to Rome for trial. He does not say what became of them, though later Christians took it that they died.

with:

> surely deserved punishment." He does not say what became of them, though later Christians took it that they died. Roman citizens he sent to Rome for trial.

No quote is added; every quote matches the outline, and the Latin is at ML 2777–2779, 2811–2816 and TL 11728–11730.

## 3. The kit lines

- **Hook:** two sentences. Pass.
- **Essence:** complete at "led away." (word 124), before the M1 sentence, and unchanged by the fix. Pass.
- **Also told:** every part present: the trial, the citizens, the list and the statue; the dawn worship told second-hand; the two women; the numbers and the temples; Trajan's rule; what it cannot tell (a page, five sentences, no number); Tertullian, Eusebius, Jerome and the contested reading, now with both sides credited. Pass.
- **Words to explain:** each listed word the story uses has its plain sense the first time it is heard. "Roman citizen" now has it ("sent to Rome for trial"). Pass.
- **Sentences:** the longest is 29 words. Pass.
- **Length:** 626 words, about 4:10. No part the story does not need. Pass.
- **Setting:** date and place share one sentence, and the office comes in the next. It is not stacked. Pass.
- **Ending:** on Pliny, his own closing hope. Pass.

## 4. Score

`python -m engine.m1.profile_readability …/pliny-the-younger/pliny-the-younger.brief.txt`: 626 words, grade 7.9 (names out 7.4), reading ease names out 71.7, 16.5 words a sentence, longest sentence 29 words. Pass, with a note that the grade is under 8. The fix moves one sentence and changes no score.
