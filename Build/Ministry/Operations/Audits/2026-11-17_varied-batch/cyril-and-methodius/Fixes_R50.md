# Fixes R50: Cyril and Methodius

Ruling: Mark, 2026-11-17 ("yes no softening, we are a witness not a judge … for this round 1 but also the should fixes too"). Not yet released; the current text is kept as `cyril-and-methodius.r50.brief.txt` before any change.

## Fix-list items

1. **MUST: restore the 879 ban and the 880 condition, so Rome does not read as a steady ally.**
   - Old: "Yet in 880 Pope John wrote that "he who made the three chief languages, Hebrew, Greek and Latin, also himself created all the others, for his praise and glory.""
   - New: "In 879 Pope John the Eighth repeated an earlier ban on singing Mass in Slavic, though Methodius could still preach in it. In 880, John questioned him before his own bishops and found him sound. He allowed Mass in Slavic, with the Gospel read first in Latin. And he wrote that "he who made the three chief languages, Hebrew, Greek and Latin, also himself created all the others, for his praise and glory.""
   - Source: Outline beat 7; sheet M16 and M17. Held text opened: Ginzel, `cic/texts/ginzel_geschichte-der-slawenapostel-cyrill-und-method-deu-lat_1861.txt` lines 13799–13805 (the ban, "per Paulum episcopum Anconitanum … prohibuimus, ne in ea lingua sacra missarum solempnia celebrares"; "Predicare vero … tibi licet"), 13902–13916 (questioned "coram positis fratribus nostris episcopis", found "orthodoxum"), 13970–13980 (Slavonic Mass allowed; "evangelium latine legatur et postmodum sclavinica lingua translatum … adnuncietur"). Q3 unchanged.

2. **Say the letters were the Glagolitic script, not Cyrillic.**
   - Old: "Because the Slavs had no letters, Constantine made them, and so began the mission of Cyril and Methodius."
   - New: "Because the Slavs had no letters, Constantine made them: most likely the script now called Glagolitic, not the Cyrillic alphabet later named after him."
   - Source: sheet D6 — Cross, `cic/texts/russian-primary-chronicle_cross1930.txt` lines 5667–5672 ("This was not the so-called Cyrillic alphabet … but the more curious and difficult Glagolica", opened); census CEN 42689, 42695 (Cyrillic "named for one brother, though their followers gave it its shape"). **Note:** the sheet and outline mark the alphabet Contested (Lützow, LUT 1337–1340, says Cyrillic) and the outline said "Slavic letters". To make the fix without presenting a contested point as settled, "most likely" carries the uncertainty in the sentence itself; the card already gives both views. This is the piece's one uncertainty marker.

3. **"In the ninth century, in the 860s" → "In the 860s". Cut "and so began the mission of Cyril and Methodius".** Both done (the cut is in item 2). Source: S4.

4. **Keep the two Clements apart.**
   - Kept: "relics of Clement, an early bishop of Rome" (M10).
   - Old: "Two of them, Clement and Naum, carried the letters … There, a later Life of Clement says,"
   - New: "Two of them, Naum and a man also named Clement, carried the letters … There, a later Life of this Clement says,"
   - Source: I1 (PG 98738–98739; LCl).

## Across-the-set items

- **Setting stack:** "to Moravia, in central Europe, in what is now the Czech Republic" → "to Moravia, in what is now the Czech Republic" (one "in what is now"; no stack). Source: S3.
- **Witness line varied:** "Most of what we know comes from two Lives by their followers, which survive only in copies made centuries later." → "Two Lives written by their followers tell most of their story, and they survive only in copies made centuries later." Source: Outline, Who tells it; D1.
- **"Yet":** the "Yet" before Pope John's letter is gone (item 1).
- **No softening:** item 1 restores Rome's ban; the Frankish bishops' two and a half years' hold and the Salzburg complaint (with "partly") stay as released.

## Readability

`python -m engine.m1.profile_readability …/cyril-and-methodius.brief.txt`: 494 words (was 450; +9.8%, inside the 10% allowance, the growth is the restored 879–880 material), grade 8.1 (names out 7.0), reading ease (names out) 75.0, 17.0 words a sentence, longest sentence 27 words — pass.

## Quotations added or changed

None. Opening phrases (M4), Q1, Q2, Q3, the Salzburg phrases and "the first bishop of the Bulgarian tongue" are unchanged. Q3 now follows "And he wrote that" in its own sentence; its words are unchanged.
