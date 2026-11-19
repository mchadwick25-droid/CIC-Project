# Card edits 2: Thomas à Kempis

Card written to `thomas-a-kempis.card.json`, from the census's current `card` object for `thomas-a-kempis` (`cic-website/data/world-census.json`). It overwrites the old batch card. No `briefLength`: the census check does not allow it. Every field other than `quotationOriginals` and `briefReferences` is word for word as in the census. Files are in `cic/texts/`.

## Clearly wrong

None. Nothing on the card is contradicted by the new brief or by a held source.

- The two census claims the outline does not hold are not on the card. "The most copied after the Bible" is in the census teaser, not on the card. The card's `legacy.remembered` already gives Neale's judgment with his "probably" (Neale 4716–4720). "On his desk" is not on the card either. `legacy.traces` gives Manare's report as Manare's: Ignatius usually kept no books on the table of his inner room but the New Testament and Thomas à Kempis (Scripta 24338–24347). That is what the source holds, credited to its later witness, so it stays.

## New: `quotationOriginals`

The new brief has seven quoted spans. The card has one entry for each, in the brief's order.

1. **Removed:** the entry with modern "At Manresa he had first seen the little Gerson. ... He read one chapter a day, in order." The new brief no longer quotes it.
2. **Added:** "Whoever follows me does not walk in darkness". Printed "Vi sequitar me non ambulat in tenebris", Pohl II 677–678, Imitation I.1, the OCR with drop capital lost (read "Qui sequitur"). secondReading same (S3-03).
3. **Kept unchanged:** "I would rather feel sorrow for sin than know how to define it." Pohl II 704–706, minor. Re-read: "Opto" ends line 704; the batch-1 note placing it on 703 does not hold, so the lines stand.
4. **Added:** "Learn to scorn outward things ... come within you." Printed "Disce exteriora contemnere et ad interiora te lo dare : et videbis regnum Dei in te venire.", Pohl II 2831–2833, Imitation II.1. "lo" is the margin number 10, noted in `uncertain`. English: Benham 3550–3553, "Learn to despise outward things and to give thyself to things inward, and thou shalt see the kingdom of God come within thee." secondReading minor (S3-04).
5. **Added:** "royal way". Printed "DE REGIA VIA SANCTAE CRVCIS.", Pohl II 3717, the title of Imitation II.12. English: Benham 4597, "Of the royal way of the Holy Cross." secondReading minor (S3-05); the reader's "royal road" worry goes in `uncertain`.
6. **Added:** "the little Gerson". Printed "el Ger^onzito", Scripta 9403–9404, Câmara's Memoriale no. 97, with the old entry's `work` and `file`. Second_Readings_3 has no item for this span. Its verdict, minor, is the one the removed entry carried for the whole passage that holds these words (Second_Readings.md, thomas-a-kempis Q2). The blind reader also rendered it "the little Gerson" (Second_Readings_Blind.md 192). `uncertain` says the verdict comes from that passage. No new verdict was made.
7. **Added:** "began to see that true religion was seated in the heart". Printed "I began to see that true religion was seated in the heart", Wesley 963–964. That is inside the key's 962–965, narrowed to the lines that hold it. secondReading same (S3-06).
8. **Added:** "a man of a true Christian spirit". Printed Woolman's sentence through "spirit", Woolman 12189–12192. secondReading same (S3-07).

Each printed and English wording was re-read in its file and lines. Each was checked against the folded text the census check uses, and each `modern` against the brief's quoted spans. A dry run of `tools/validate-census.mjs` on a census copy was killed for lack of memory, so this check was done by a script that copies its rules. The sources each entry cites are all in `sources` already.

## New: `briefReferences`

The old seventeen were replaced with sixteen plain-text references to what the new brief draws on. Lines re-read:

- Pohl II 671–684, 699–706, 2827–2833, 3717–3738, 3758–3760, 3764–3769
- Benham 1118–1129, 3540–3553, 4597–4670
- Chronicle 292–300, 810–813, 1100–1106, 1189–1195, 1819–1829, 1892–1896, 1908–1915, 3409–3430
- Founders 2063–2072, 8990–9017
- Busch 5410–5415
- Ingram 1176–1186; Neale 4716–4722
- Scripta 9403–9408, 9431
- Wesley 960–966
- Methodist minutes 2643–2653
- Woolman 12189–12192

The only quotation marks in them are around words the brief also quotes. Dropped, because the new brief no longer uses them:

- the indulgences
- the sandy hill
- the novices' sermons
- the Exercises
- the census tradition line

## Not found

None.
