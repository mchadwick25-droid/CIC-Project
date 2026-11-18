# Fixes R50: Antony the Great

Ruling: Mark, 2026-11-17 ("yes no softening, we are a witness not a judge … for this round 1 but also the should fixes too"). Released text kept as `antony-the-great.r50.brief.txt`.

## Fix-list items

1. **Put the Arian episode in the Life's voice.**
   - Old: "Yet when Arians claimed he agreed with them, he came down to Alexandria and taught that the Son of God was not created."
   - New: "The Life says the Arians, who taught that the Son of God was created, lied that he agreed with them. Then, it says, the bishops summoned him, and he came down to Alexandria to teach that the Son was not created."
   - Source: E14 — VA §69, NP4 32924–32932 ("the Arians having lyingly asserted that Antony's opinions were the same as theirs … being summoned by the bishops and all the brethren, he descended from the mountain … taught the people that the Son of God was not a created being"). "Lied" is the Life's own charge, kept in its voice.

2. **Explain "Arians" in a clause.** Done in item 1: "the Arians, who taught that the Son of God was created". Source: E14 gloss (NP4 32935, "there was a time when He was not").

3. **Mention the demons briefly, in the Life's voice.**
   - Added after the witness line: "Demons fill much of it. In a tomb outside the village, it says, they beat him until a friend found him lying as though dead."
   - The next sentence, "It tells how he went further, to a deserted fort…", became "Then he went further, to a deserted fort…" so the tomb comes first, as in the Life.
   - Source: D8 (demons "fill much of the Life", §§5–13, 48–66, 82, 86); E6 — VA §8, NP4 31454–31469 (the tombs; demons beat him; his friend found him "lying on the ground as though dead"). Outline beat 4.

4. **Cut or split the Constantine sentence; give the era concretely.**
   - Old: "That choice led him into the life of Egypt's desert monks, and he lived on into the time of the emperor Constantine and his sons."
   - New: "That choice took him into the desert. He was still there when the emperor Constantine and his sons wrote him letters."
   - Source: E16 — VA §81, NP4 33188–33189 ("Constantine Augustus, and his sons Constantius and Constans the Augusti wrote letters to him"); S4. The emperors are tied to his late life, not his youth, as the outline's Do not say requires.

5. **Keep the length near 462 or shorter; the Augustine quotation may be trimmed.** The quotation is trimmed to drop the Gospel words that repeat the opening (see Quotations). With the quote no longer addressing God as "you", the lead-in "Writing to God in his Confessions, he recalled:" became "In his Confessions, he recalled:". Length 462 → 461.

## Across-the-set items

- **No softening / one-side framing:** the Arian episode, the Life's most partisan scene, is now the Life's account, not the narrator's (item 1).
- **Witness line varied:** "Most of what we know comes from one book, a Life written soon after his death, which the church has long credited to Athanasius, bishop of Alexandria." → "His story is told in one book, a Life written soon after his death, which the church has long credited to Athanasius, bishop of Alexandria." Source: Outline, Who tells it; D1.
- **"Yet":** the "Yet" before the Arian sentence is gone (item 1). The impact does not open with "Yet".
- **Setting / "in what is now" / uncertainty tags:** none needed change.

## Readability

`python -m engine.m1.profile_readability …/antony-the-great.brief.txt`: 461 words (was 462), grade 7.4 (names out 6.6), reading ease (names out) 80.6, 18.4 words a sentence — pass, with the tool's note that grade 7.4 is under 8 and goes to the listener read. The longest sentence (31 words, "After giving the fields to the villagers…") is unchanged from the released text; no fix touched it.

## Quotations added or changed

- **Trimmed:** Augustine, *Confessions* VIII.12.29 (Q3). Now spoken: "For I had heard this of Antony. He had come in by chance during the Gospel reading, and was urged on by it. It was as though the words read were spoken to him." Dropped: the Gospel words and "By such a divine word he was at once turned to you." The kept words are the outline's Q3 rendering unchanged, from the Latin at `cic/texts/augustine_confessiones-lat_knoll-csel33.txt` lines 13470–13476 (English AUG 13117–13124). Needs a second reading.
- Quoted phrase "the desert became a city of monks" unchanged.
