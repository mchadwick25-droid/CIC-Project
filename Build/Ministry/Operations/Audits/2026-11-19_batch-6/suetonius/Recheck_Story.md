# Recheck: Suetonius (story)

Batch 6, 2026-11-19, per `Recheck_Story_Prompt.md`. Read: `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entries "Batch 6: …" and "Change order: the stories approved before the kit…" (2026-11-19), and in this folder `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `suetonius.brief.txt`, `suetonius.brief.v1.txt`. Sources opened: ROL 25905–25918, 28456–28461 (`suetonius_lives-of-the-caesars-loeb_rolfe1914.txt`).

## Verdict: FIX

## 1. Review findings

- **B1 (Nero half of the essence).** Fixed: "and one other: under Nero, they were punished." Held by the essence and E3 (ROL 28458–28459, *afflicti suppliciis Christiani*). No kind of punishment is given and no tie is made to the fire. The Do not say line was added to the outline (line 119).
- **M1 (envoys).** Fixed: "he let German envoys sit with the senators". Held by ROL 25909–25916 ("allowed the envoys of the Germans to sit") and by the outline's opening.
- **M2 (the "he" heard as Chrestus).** Fixed: "Suetonius was a close friend…".
- **M3 ("meanwhile").** Fixed: "Long before, Christian writers had complained…". Held by I3, and it is true in time against the 1909 editors.
- **Length cut.** Made as the review gave it.

Nothing is listed as unfixed.

## 2. New wording

The diff against v1 is the four changed sentences above, each in the review's words and each held at the lines cited. None says more than its source. The quotes are unchanged and match the outline word for word.

## 3. The kit lines

- **Hook:** three sentences. Pass.
- **Essence:** the Nero half is at word 85 ("punished."), and the essence is complete at word 111 ("…who Chrestus was."). Pass.
- **Also told:** present: the two lists the lines sit in; "beyond criticism"; the fire never tied to the Christians; Acts and Aquila; the editors on Chrestus; the complaint about the name, with Tertullian. The outline marks Dio and Jerome as the first to cut. Pass.
- **Words to explain:** Chrestus, Chrestianus/chrestos, superstition, old Troy, lives of twelve rulers, and Acts each get their plain sense when first heard. Pass.
- **Sentences: one runs past about 30.** The length cut joined Tertullian's lead-in to Q3 with a colon. That makes "Around 200, Tertullian, defending the Christians, told them so: "And even when … sweetness or kindness."" one sentence of 32 words by the scorer. In v1 the quote stood as its own sentence. The batch's own reviews treat 31 and 32 as past the line (Tacitus, M4 and M5).
- **Length:** 441 words, about 2:57. No part the story does not need. Pass.
- **Setting:** not stacked. Pass.
- **Ending:** on Suetonius's seven words, "from a man not writing about Christians at all". Pass.

**Fix.** Replace:

> told them so: "And even when you wrongly say

with:

> told them so. "And even when you wrongly say

The words are the same. The quote stands as its own sentence of 24 words, and the lead-in becomes a sentence of 9.

## 4. Score

`python -m engine.m1.profile_readability …/suetonius/suetonius.brief.txt`: 441 words, grade 8.8 (names out 7.8), reading ease names out 73.6, 19.2 words a sentence, longest sentence 32 words. Pass on grade and reading ease. The longest sentence is the one the fix splits.
