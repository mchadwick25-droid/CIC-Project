# Recheck: Lactantius (story)

The independent recheck, batch 7, 2026-11-20, per `Recheck_Story_Prompt.md`. I did not write, review or revise this story. Read: `CLAUDE.md` ("Trust and source fidelity"), Kit Parts 1 and 2, the Decision-Log entries named in the prompt, `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `lactantius.brief.txt` and `lactantius.brief.v1.txt`.

## Verdict: FIX (one sentence)

## 1. Review findings

A diff against v1 shows B1, B2 and M1 to M6 applied in the review's words, and nothing else changed.

- **B1:** fixed. Crispus is now in the essence (P2) and is not told again (P10).
- **B2:** fixed. "The world will run as it is for six thousand years" matches AN 6648–6650 ("continue in its present state through six ages, that is, six thousand years").

## 2. New wording

- "Late in life, Jerome says, he taught Constantine's son Crispus in Gaul." This is moved, not new. It is held by Outline 5 and 43 (E14).
- "some seventy years later": Outline 77 ("about 70 years later").
- "does not know how it began": Outline 38. EU 43982–43984 reads "I know not how".
- "He wrote:" is a speaker tag. Q1 is verbatim to Outline 52 and DI-L 23206–23210.
- "Of the Latin defenders before him": Outline 7 ("Tertullian had defended the Christians"), Outline 15 (the Latin Apologists) and Source_Sheet E7 (AN 4466–4476, 4569). It says no more than these.
- **M6 fails.** It cut "Both were posted at Nicomedia, and". That leaves "Lactantius copied their text into his book." The sentence before it ends "returned their churches", so on one hearing "their text" now means the Christians' text, not the two edicts. This misleads on one of the things the story must tell (Outline 9, the edicts' texts copied into the book).

### FIX

Replace

> "Lactantius copied their text into his book."

with

> "Lactantius copied the text of both into his book."

This adds one word, for 674 in all. It keeps the Do not say wording ("copied their text into his book", Outline 96) and does not say "in full".

## 3. Kit lines

- **Hook:** three sentences.
- **Essence:** complete at word **135** ("…in Gaul.").
- **Also told:** why and how he wrote, what the *Institutes* argue, what *the Persecutors* holds (the children told as his verdict), and the fire's three causes. All present.
- **Words to explain:** rhetoric, the Great Persecution, edict, *Institutes*, Sibyls, Cicero and Bithynia are each glossed when first heard. Caesar is not used. The Holy Spirit is unglossed, as the outline says.
- **Sentences:** longest 28.
- **Length:** 673 words, about 4:29, under the 4:30 ceiling. Nothing beyond the review's applied cuts (M5, M6).
- **Setting:** not stacked.
- **Ending:** on the person, in Jerome's words.

Outline note (flag only, not part of the brief): the two Do not say lines from B1 and B2 were appended under "For the card, not the story" (Outline 123–124), not under "Do not say". Q3's note (Outline 54) and Ending 1 (Outline 71) still place Crispus in beat 7.

## 4. Score

`python -m engine.m1.profile_readability`: 673 words, grade 8.9 (names out 7.7), reading ease names out 70.0, 16.8 words a sentence, longest 28. Pass.
