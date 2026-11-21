# Card edits: Tatian

Card writer, batch 6 (2026-11-19), under `roles/card.md` and `Card_Prompt.md`. Base: `Card.existing.json` (the census card for `tatian`). Output: `tatian.card.json`. Every other field is kept word for word and in order.

## Clearly wrong

1. **legacy.remembered[2].** Old: "Theodoret of Cyrus replaced more than two hundred copies…". New: "Theodoret of Cyrrhus replaced more than two hundred copies…". Evidence: the brief, paragraph 7, "Theodoret of Cyrrhus, in northern Syria"; the census name of `theodoret-of-cyrrhus` (Source_Sheet §4, which notes the old card's "Cyrus"). The spelling only; the claim is held (TH 14984–14987).

## New

2. **sources.about**, two entries added after the existing four:
   - Epiphanius of Salamis, *Panarion* 46, Greek of Karl Holl, `cic/texts/epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt`. Evidence: the brief's "A later writer says Tatian went east… and only that writer puts him there" (EP 15995–16008; Holl, EP-ed 16018).
   - Theodoret of Cyrrhus, *Compendium of Heretical Fables* I.20, as quoted in Maran's prolegomena, `cic/texts/apologists-fragmentary_reliquiae-corpus-apologetarum-vol9-grc-lat_otto1872.txt`. Evidence: Q3 and the brief's Theodoret sentences (TH 14972–14987). The quotation entry cites this file, so the card must list it.
3. **briefReferences**, 16 lines, one per part of the brief, each with its work and chapter (Address 1, 2, 19, 29, 31–42 in Ryland, AG 5682–7471; Otto's Greek of 1851; Irenaeus I.28.1, IR 33642–33675; McGiffert's notes, EU-ed 26218–26234; Eusebius IV.28–29; Jerome 29; Epiphanius 46.1; Hogg's introduction, DI-ed 1715–1726, 1764–1768, 1790–1794, 1822–1828, 1845–1851, 1914–1931; Theodoret via Maran, TH 14972–14987). No quotation marks.
4. **quotationOriginals**, four entries, one for each quoted span in the brief. Each printed and original wording was re-read in its file at the cited lines and copied as printed, OCR faults kept.
   - Q1, "So I said goodbye… my own." Printed: Ryland, AG 7258–7260. Original: Otto's Greek, AG-G 12199–12201.
   - "the self-controlled". Printed: "Encratites (self-controlled)", Irenaeus I.28.1, IR 33656–33657.
   - Q3, "I myself found… the four evangelists." Printed: Theodoret's Greek as Maran quotes it, TH 14984–14987 (OCR reads "Evgov" for Εὗρον; kept as printed).
   - Q2, "Now that I know… I will not deny it." Printed: Ryland, AG 7464–7471 (an editor's note sits inside the lines). Original: Otto's Greek, AG-G 14236–14241 (the marginal letters "Δ" and "δ" are in the file and kept).

## Awaiting second reading

The census card has no `quotationOriginals`, so all four spans are new and carry no `secondReading`:
- "So I said goodbye to the boasting of the Romans… I made our barbarian philosophy my own."
- "the self-controlled"
- "I myself found more than two hundred such books… the Gospels of the four evangelists."
- "Now that I know who God is… and I will not deny it."

## Not changed

No `briefLength` (the census check does not allow it): the brief runs 626 words, about 4 minutes 10 seconds. Every existing claim was found in a held source: Hogg's "very widely if not universally read" (DI-ed 1929–1930); McGiffert's "seem fully to establish his main positions" (EU-ed 26233–26234); "I know not how" (EU 26424–26479). None contradicts the brief.

## Not found

None.
