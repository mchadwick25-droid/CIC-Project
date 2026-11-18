# Coordinator fix check, batch 4 (2026-11-18)

An independent check of the four coordinator-worded changes (commits aeac522af6 and a14ea4f594). Each was checked against the vendored source in `cic/texts/`.

## 1. dhuoda: "written", not "carved". FIX

Source: DH 11963–11975 (`dhuoda_liber-manualis_bondurand1887.txt`). The heading says "De epitaphio sepulchri tui ut scribas rogo". The text says "in loco in quo fuerim sepulta, super ipso tecto sepulchri quod meum operuerit corpus, hos versiculos jube transcribere firmatim, ut cernentes ipsum epitaphium sepulchri, pro me indigna dignas ad Deum jubeant fundere preces". She asks him to have these verses written firmly over the covering of the tomb, so that those who see them will pray for her. Witness: Dhuoda's own words, the right witness.

- Brief: PASS. "asks William to have it written on her grave, so that passers-by will pray for her" says no more and no less than the Latin.
- Source_Sheet.md E17 heading and the "whether the epitaph was written there" gap line: PASS.
- Outline.md Do not say entry and the E17 gloss: FIX. Saying "not to carve it" claims more than the source. *Transcribere* means to write or copy. It does not rule out cutting the letters, and *firmatim* ("firmly") points toward a lasting inscription. The source is silent on the method, so the gloss must be silent too.
- Outline.md beat 5 (line 17): FIX. It still reads "asks him to have it carved on her grave", which contradicts the brief and the corrected Do not say entry.

Replacements:

- Outline.md, Do not say entry. Replace `(her Latin is *transcribere*, to write it there, not to carve it)` with `(her Latin is *transcribere*, to write it there; she does not say carved)`.
- Source_Sheet.md E17. Replace `(*transcribere*: to write it on the tomb's covering, not to carve it.)` with `(*transcribere ... firmatim*: to write it firmly on the tomb's covering; she does not say how, and does not say carved.)`.
- Outline.md beat 5. Replace `She writes her own epitaph and asks him to have it carved on her grave, so that passers-by will pray for her (E17).` with `She writes her own epitaph and asks him to have it written on her grave, so that passers-by will pray for her (E17).`.

## 2. cyril-and-methodius: "ploughing" to "plowing". PASS

The diff in a14ea4f594 changes exactly one word in the brief and one word in the card's `quotationOriginals[3].modern`. Nothing else moved. The Latin "unum sulcum imprimentes" (VM 12251–12255) is unaffected. Outline.md Q2 still reads "ploughing". It is not participant-facing and was not in scope, so it is noted here only.

## 3. hild-of-whitby: Source_Sheet.md B1. PASS

- III.21, Diuma: Giles 7426–7431 has "the scarcity of priests was the occasion that one prelate was set over two nations". Plummer 20711–20714 has "Paucitas enim sacerdotum cogebat unum antistitem duobus populis praefici". Both are correct. (Plummer's running header on that page reads Cap. XXII, but the passage falls inside XXI, which begins at 20642.)
- IV.12, Bosa: Giles 9874–9880 and Plummer 23690–23696 have "Bosa, to preside over the nation of the Deiri" and "Bosa ... qui Deirorum ... prouinciam gubernaret". Both are correct. Bosa is first among Hild's five bishops (Giles 10973–10976, IV.23).
- IV.5, Hertford canon IX: Giles 9358–9360 and Plummer 23031–23033 have "more bishops should be made, as the number of believers increased; but this matter for the present was passed over". Both are correct.
- Label: "LATER (Bede). Widely Accepted as a summary; the narrator's gloss, not Bede's words" is apt. The entry does not present the general rule as Bede's own statement, and the three passages carry it.

## 4. Essences.md, Columba: "Bede says he turned the northern Picts to the faith". FIX (wording only)

The claim: PASS. Giles III.4 (5815–5820, 5836–5839) says Columba came "to preach the word of God to the provinces of the northern Picts" and "converted that nation to the faith of Christ, by his preaching and example". The subject is Columba ("he"), not Iona.

The new wording left a defect behind it. In "and through Aidan it sent the faith to the English", the pronoun "it" was meant for Iona. After the change to "he", the sentence offers no antecedent for "it". Aidan as "a monk of the island called Hii" is in Giles III.3 (5794–5795).

Replacement. Replace `Bede says he turned the northern Picts to the faith, and through Aidan it sent the faith to the English.` with `Bede says he turned the northern Picts to the faith. Through Aidan, Iona sent the faith to the English.`.
