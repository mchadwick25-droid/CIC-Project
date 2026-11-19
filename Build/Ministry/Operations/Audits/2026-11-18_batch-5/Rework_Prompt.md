# Batch 5 rework prompt: Barsauma (Mark's cap ruling, 2026-11-19)

You rework the Church Family Tree story about **Barsauma of Nisibis** in `Build/Ministry/Operations/Audits/2026-11-18_batch-5/barsauma-of-nisibis/`. You did not write or review it.

## Read
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Parts 1 and 2.
- The Decision-Log entries "Batch 5 hearts: church words explained, and Luther's job re-set" (2026-11-18) and "Batch 5: Barsauma reworked, a sixth reader, then record and go live" (2026-11-19), in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`.
- Barsauma's heart in `Build/Ministry/Operations/Audits/2026-11-18_batch-5/Hearts_Plain.md`.
- In the folder: `Outline.md`, `barsauma-of-nisibis.brief.txt` (the released story), `Reshape_Review.md`.
- What the listeners said about Barsauma in `Build/Ministry/Operations/Audits/2026-11-19_batch-5-read/`: `Pastor.md`, `General.md`, `Skeptic.md`, `Scholar.md`, `AI_Skeptic.md`.
Read nothing else, except a file in `cic/texts/` to check a line the outline cites. Use no shared, scratch or temporary file of any kind.

## The fault
Listeners lose it after one hearing. It tells the record, not the person: five witnesses credited in turn, three versions of his marriage, dates from 424 to 605, no sense of what he stood for or why, and it ends on a synod.

## Do
1. Copy the brief to `barsauma-of-nisibis.brief.v3.txt` before changing anything.
2. Rewrite `barsauma-of-nisibis.brief.txt` from the outline only. Keep the approved heart, and keep the record's force and every hard part (Babowai's death and the charges, the taking back, the amputation letter, the hostile massacre story told as the rivals' claim). Follow one line: the frontier bishop, what he fought for (married clergy, Theodore as guide), the quarrel and Beth Lapat, the taking back, and his church keeping his rules anyway, while its neighbors blamed him for the split. State the marriage conflict once, briefly, with each claim kept to its own witness. Credit a witness where the claim is told, but only the few the line needs. Hold to two or three dates the listener must keep. Let the listener hear what he stood for early. End on the person, not a synod.
3. Kit rules hold: the essence complete by about word 150; the life told once, in order; every name earns its place; quotes only the outline's, word for word, with any cut marked; every listed church word given its plain sense the first time it is heard (never gloss a common word, never chain glosses); no sentence past about 30 words; American spelling outside quotes. Aim near three minutes (about 450 to 520 words); take what the line needs.
4. Run `python -m engine.m1.profile_readability <brief>`. It must pass. Check your work for the four faults: one witness told as fact, an editor's view given to the source, a detail moved onto the wrong event, force softened.
5. Write `Rework.md`: what you changed and why; every sentence that is neither the outline's wording nor the old brief's, with its outline line; every quote with its outline line, and whether it is new to the story or its wording changed; the word at which the essence is complete; the word count and minutes.

Edit nothing else; do not commit. Reply in under 120 words: word count, scorer line, essence word, and any quote added, dropped or changed.
