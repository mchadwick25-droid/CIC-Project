# Card edits: Pliny the Younger

2026-11-19. The existing card is the census card for `pliny-the-younger` (`cic-website/data/world-census.json`), identical to `Card.existing.json`. Every field not named below is kept word for word. Library files, all in `cic/texts/`: **ML** = `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`, **EU** = `npnf201_eusebius-church-history-life-of-constantine.xml`, **TE** = `anf03_tertullian.xml`, **TL** = `tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt`, **JC** = `jerome_eusebii-chronici-canones-lat_fotheringham1923.txt`. Every line cited below was re-read in its file.

Keys used: only those `tools/validate-census.mjs` allows (CARD_KEYS). No `briefLength`, and no connections.

## Clearly wrong

1. **uncertain[1].**
   - Old: "The Library holds no edition of Pliny."
   - New: "The Library holds no edition of Pliny's other letters; the Latin of these two is in Carl Mirbt's source book."
   - Evidence: ML 2758–2819 prints *Letters* 10.96 and 10.97 in Latin, "ed. C F W Müller" (ML 2760). Source_Sheet, ML entry and D6: no held text of his other letters. The rest of the item is unchanged.

## New

2. **sources.ownWords.** Added: Letters 10.96 and 10.97 in Latin, ed. C. F. W. Müller, in Mirbt, documents 14 and 15 (ML 2766, 2807). The brief's renderings of Quotes 1 and 2 and "our age" are made from this Latin (Outline, Quotes).
3. **sources.about.** Added: Tertullian, Apology, chapter 2, Latin, ed. Oehler (TL; Quote 3 is rendered from TL 11728–11730). Added: Eusebius's Chronicle in Jerome's Latin, ed. Fotheringham (JC 42246–42260; the brief's "had killed very many Christians").
4. **briefReferences.** New, one line for each of the brief's paragraphs 1–9 (the last paragraph draws on the same letter as paragraph 6). Grounds: ML 2768–2772 and EU 19459–19463 (opening); EU 19451–19459 and ML 2758 (setting); ML 2776–2780, TL 11655, EU 19449–19451 (the trials); ML 2780–2785 (list and test); ML 2786–2797 (worship, the two women); ML 2797–2805 (why he wrote); ML 2809–2819, EU 19523–19533 (reply); TL 11034, 11653–11658, 11724–11731, TE 1566–1587 (Tertullian); EU 19446–19451, 19541–19556, JC 42246–42260, EU 19561–19576 (Eusebius, Jerome, McGiffert). No quotation marks.
5. **quotationOriginals.** New, one entry for each of the brief's seven quoted spans. Each `modern` is the brief's span exactly; each `printed` and `original` stands verbatim at its lines. Tertullian's two spans, broken in the brief by the narrator's sentence, are two entries.
   - The Latin of Quotes 1 and 2 is not given as `original`: ML 2777 carries the margin number "15" inside the span, and Trajan's sentence runs across a page head (ML 2813–2815) with the OCR "argiiantur" (ML 2816). The Latin of "What a ruling, confused by necessity!" is not given either: the OCR reads "0" for "O" at TL 11728. These need a reading in `tools/quote_scan_readings.json` before the Latin can be cited; the entries cite McGiffert's and Thelwall's English instead.

## Quoted spans, awaiting second reading

The existing card had no `quotationOriginals`, so no `secondReading` could be copied; none is given.

| # | Modern (the brief) | Printed | Original |
|---|---|---|---|
| 1 | Those who confessed, I asked a second and a third time ... surely deserved punishment. | EU 19471–19476 (McGiffert) | — (ML 2777–2779) |
| 2 | They are not to be hunted out. If they are reported and proved guilty, they are to be punished. | EU 19526–19527 (McGiffert) | — (ML 2811, 2816) |
| 3 | our age | EU 19533 (McGiffert) | ML 2819 |
| 4 | What a ruling, confused by necessity! | TE 1583–1585 (Thelwall) | — (TL 11728) |
| 5 | It forbids a search for them ... it looks away and it punishes. | TE 1585–1587 (Thelwall) | TL 11728–11730 |
| 6 | disturbed by the great number of martyrs | EU 19449 (McGiffert's Eusebius) | — |
| 7 | had killed very many Christians | JC 42247–42248 (Jerome's Latin) | — |

## Not found

None. Every existing claim was found in its held source.
