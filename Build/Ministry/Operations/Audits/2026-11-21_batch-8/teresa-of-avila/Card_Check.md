# Card check: Teresa of Ávila

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. I wrote neither the card nor the brief. Read: `teresa-of-avila.brief.txt` (and `brief.v1.txt`, to see what the final brief dropped), `teresa-of-avila.card.json`, `Card_Edits.md`, and each cited line in its file. New card: there is no census entry or starting card, so every field was checked against its evidence. The validator was not run.

**Verdict: FIX** (one, outside the card: two companion readings for `tools/quote_scan_readings.json`; no change to the card's JSON).

## 1. Each field against its evidence

Re-read at the cited lines, and confirmed:
- `datesNote`: BREV 79186-79193 (28 March 1515, in the Breviary's brackets); LIFE-Z 676-681 (Yepes, the Bollandists, de la Fuente and Lewis on 2 November 1533 and 3 November 1534) and 711-727 (profession 3 November 1536, entry a year and a day earlier, the deeds of 31 October 1536; the deed itself is at 726-727, a few lines past the range `Card_Edits.md` gives); VIDA 19301-19305 and LIFE-L 1891-1893 (24 August 1562); LIFE-Z 1182-1183 and LIFE-L 1907-1911; FOUND 570-573, 700-703; VIDA-ed 6150-6154 (1570 or 1574); LIFE-L 2154; LIFE-L 2383-2385 (6 July) and VIDA-ed 6230-6231 (7 July, from the original); CASTLE-ed 464-467; FOUND-ed 2380-2386 and FOUND 3677-3678; FOUND-ed 2490-2493, 2537-2549, BREV 79312-79313, 79377-79378; LIFE-L 2415-2428; FOUND 3686-3690, JCL 9264-9267, BREV 79325-79327.
- `placeNote`: FOUND 1035-1039 (outside the city), 755-758, 975-978 (Burgos, April 1582), 3790-3794 (Salamanca, 1573, Ripalda); CASTLE 1689-1691 (Toledo).
- `keyWorks`, `role`, `knownFor`: as cited; FOUND 3792-3794 for Ripalda.
- `legacy.traces` and `legacy.remembered`: FOUND 755-772 (seventeen, two plus thirteen); LIFE-L 2189-2196, 2212-2219, 2365-2378, 2389-2398, 2413-2428; CASTLE-ed 751-757; ASS 14101-14108; PASC 15024-15029; LIG 2659, 2687-2689; LIGM 11853; GUY 6780-6782; LOW 10165-10187.
- `uncertain`: FOUND 1040-1072 and 1174 (the 1581 letter, 190 and 180 nuns, prioress 1571 to 6 October 1574); LIFE 16719-16735; VIDA-ed 6156-6200 (Ana de Jesús in the Madrid informations, Gracián); LIFE-Z 1134-1158 and LIFE 18975-18983 (Báñez's deposition, his margin note of May 1575 with nine houses, Salamanca 1591); LIFE-Z 1195-1199; FOUND-ed 2032-2041, 2062-2074; FOUND-ed 2522-2525 (child of the Church).

Nothing in the card is contradicted by a held source or by the brief.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

The final brief dropped the house "like those of the barefoot orders" and "She saw none of that"; no reference names either. The remaining eleven all name what the brief tells, or the source a told claim rests on: [0] Life VIII and the confessors; [1] the Carmelites, the Incarnation, the relaxed rule, St. Joseph's, the thirteen nuns, the city, the Discalced; [2] birth, entry, the convent; [3] the advisers and the Jesuits; [4] the Index and her laughter; [5] 24 August 1562, the council, Báñez; [6] the Life and "burn it at once"; [7] the houses, the Princess, Gracián, Báñez, the censure, the decree; [8] the Castle; [9] 1580, 1588, 1622; [10] Alba de Tormes and her last words. The one quoted span in them, "burn it at once", stands verbatim in the brief. None to remove.

## 4. Census rules

Only allowed keys; no `briefLength`. The brief quotes five spans; the card has five entries, each `modern` word for word as the brief has it, and none for the dropped "like those of the barefoot orders". Every cited file is in `sources`. No audit, review or ruling named. American spelling outside printed wording ("councilors" in a reference without quotation marks, against the brief's "councillors", is allowed). The three spans of six words or more have no `secondReading` yet, as the new-card prompt asks; the two short ones carry "checked at card".

Each `printed`, `original` and `englishPrinted` stands at its lines by the fold rule, except one: the Castle quotation (`quotationOriginals[4]`) does not, as `Card_Edits.md` reports. CASTLE 1759 prints the footnote mark "1" inside the span ("a castle, 1 formed"), which the fold keeps as a word, and lines 1762-1777 hold only footnotes, a page number, a scan stamp and a running head between "there are" and "many mansions". The card's wording is the print's; the fix belongs to the scan-readings file (FIX 1).

**Checked at card.**
- "burn it at once." VIDA 9391 "vuestra merced lo queme luego": queme luego is burn it at once; Lewis prints the same words (LIFE 6335-6336). Right.
- "not a deceiver." LIFE 2371 "she is not a deceiver". Right; English only, as the card says.

## 5. Originals

Spans 1-3 carry Silverio's Spanish, clean at VIDA 8724-8725, 17931-17934 and 9391, with Lewis's English beside it. The Castle, the Foundations and Báñez's censure are not held in Spanish (I found none in `cic/texts/`), so the Castle span and "not a deceiver" rightly carry English alone. Nothing missing.

## 6. Not-found claims, and anything clearly wrong

All upheld: Medina del Campo as the first house after St. Joseph's (the scan's columns do not join names to dates); no year for Liguori's letter; the year of Báñez's deposition rests on Lewis's note (LIFE 18981-18982), and the card says so; the Breviary's thirty-two and Báñez's dozen and nine are each given as that source's count. Nothing clearly wrong was left in.

## FIX

**FIX 1.** No change to the card. Two companion readings for `tools/quote_scan_readings.json` (outside the card; the coordinator adds them), so that `quotationOriginals[4].printed` stands at CASTLE 1759-1778:
- `{"file": "cic/texts/teresa-of-avila_interior-castle_stanbrook1912.txt", "lines": "1759", "scan": "castle, 1 formed", "reads": "castle, formed", "kind": "footnote mark"}`
- `{"file": "cic/texts/teresa-of-avila_interior-castle_stanbrook1912.txt", "lines": "1762-1777", "scan": "CHAP. I.] FIRST MANSIONS. 5", "drop": true, "kind": "footnotes, page number, scan stamp and running head", "lines_held": ["1 Way of Perf. ch. xxviii. 9.", "* In her Life St. Teresa likened God to a diamond (ch. xl.", "14) ; and elsewhere (ch. xi. 10) the soul to a garden wherein", "our Lord takes His delight.", "4", "Digitized by t^.ooQle", "CHAP. I.] FIRST MANSIONS. 5"]}`

With both applied, the printed wording folds into the lines (checked by hand against the validator's fold and drop rules). The "*" after "crystal," folds away and needs no reading.
