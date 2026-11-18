# Baudonivia — Card Edits

Card written to `baudonivia.card.json` from `baudonivia.original.card.json`. Every field of the original card is kept word for word, in its order. SRM2 = `cic/texts/fredegar-liber-historiae-francorum-vitae-mgh-srm-2-lat_krusch1888.txt`; AA4 = `cic/texts/venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt`.

## New

1. **`briefLength` added** after `role`. Old: none. New: "about 2 minutes 10 seconds". Evidence: `baudonivia.brief.txt` is 346 words (`wc -w`; the Recheck's scorer gives 345). The batch-2 cards give about 2.7 words a second for briefs of 316–404 words, which puts 346 words at about 2 minutes 10 seconds. That is within the Outline's "2 minutes" and the Recheck's "within the two minutes".

2. **`briefReferences` added** (ten entries). Old: none. Evidence for each, re-read in its file:
   - Book II prologue: SRM2 29433–29441 (Dedimia and the community; "digito caelum tangere"), 29492–29499 ("minus docta, plus devota"; "non polito, sed rustico"; "Non ea quae ... Fortunatus episcopus ... iteramus, sed ea quae prolixitate praetermisit").
   - Fortunatus's Hilary prologue: AA4 43014–43015 ("pene mibi videatur aequale tam istud posse dicere quam digito caelum tangere").
   - Ch. 2: SRM2 29663–29675 (chapter number at 29663).
   - Ch. 5: SRM2 29743–29745 ("per ordinationem praecelsi regis Chlotarii construxit").
   - Ch. 10: SRM2 29987–29995 (chapter begins 29977).
   - Ch. 16: SRM2 30238–30261, 30302–30312 (chapter runs 30198–30327).
   - Ch. 21: SRM2 30521–30522 (chapter title list, 29589).
   - Ch. 24: SRM2 30581–30584.
   - Krusch's introduction: SRM2 28170–28197, 28219–28233.
   - Krusch's proemium: AA4 41898–41899, 41918–41919; date 1885 at AA4 4 and 42990.

3. **`quotationOriginals` added** (three entries). Old: none. The modern renderings are copied exactly from the brief; the printed wording is the OCR text of the file, verbatim, re-read at the lines given:
   - "I ask your prayer to help me. I am less learned, more devoted." = SRM2 29492–29493: "vestrn* rae oratione iuvari'* peto, quae sum / minus docta, plus devota." [vestra me oratione iuvari]
   - "What she did in the land of the East, blessed Radegund did in Gaul." = SRM2 30245: "Quod fecit illa in orientali patria, hoc fecit beata\"i Kadegundis in GalHa." [Radegundis in Gallia]
   - "Her eyes were closed, and ours were darkened." = SRM2 30522: "clausi sunt eius\" ocuU, et obscurati sunt nostri." [oculi]
   The brief's other borrowed phrases ("touching the sky with a finger"; "pardon good Baudonivia, who confesses her weakness") are not in quotation marks in the brief, so they are listed under `briefReferences`, not as quotations.

## Clearly wrong

None. Every statement on the card was checked against its held source and none is contradicted, nor does any contradict the brief.

- **The Patrologia Latina 72 entry under `sources.ownWords`** was left in place. The batch's Library check says her text should be cited from Krusch's MGH edition, and the card already lists Krusch first. The PL72 entry says only that Book II is printed in PL72, and it is: PL72 50643–50654 ("LIBER SECUNDUS, AUCTORE BAUDONIVIA ...", "Baudonivia [Al., Bandonivia, Bandomina] humilis omnium"). No held source contradicts the entry, so card.md's rule does not allow a correction. The brief's quotations and references cite Krusch (SRM2) only.

## Not found

None. Each claim on the card was found in a held source. The checks: Dedimia known only from her, SRM2 29481; the Migne note on Fortunatus, PL72 50773–50777; Hildebert, SRM2 28227–28233; Krusch's verdict, SRM2 28219–28225; the cradle phrase, SRM2 29449–29450, SRM2 29483–29485, AA4 43008–43009, 41118–41122; Gregory's bishop and country estate, Dalton 19603–19611; Krusch's notes on Justin and Maroveus, SRM2 30295–30297; Dalton's Maroveus reading, Dalton 29584–29591; the 13 August and 587, SRM2 30521–30522, Dalton 17574–17577, SRM2 28171; the date after 600, SRM2 28186–28197; Krusch on the Life of Caesarius, SRM2 28222–28223; Dalton on Domolenus, Dalton 28164–28168, with the vision in Fortunatus's Book I, SRM2 29380–29384; the unnamed manuscript title, SRM2 29465–29467; Dalton's "contemporary" and "in the monastery during Radegund's life", Dalton 24356–24358, 29584.
