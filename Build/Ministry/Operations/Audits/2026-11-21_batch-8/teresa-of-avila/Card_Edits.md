# Card edits: Teresa of Ávila

Batch 8, 2026-11-21. The card is new, so every field is listed with its evidence. Files are under `cic/texts/` except where marked. Names: VIDA her Life in Spanish (Silverio, 1915; his notes VIDA-ed); LIFE the Life in Lewis's English, with Zimmerman's introduction (LIFE-Z, to about line 1240) and Lewis's preface (LIFE-L, about 1240-2640); FOUND the Foundations with Zimmerman's introduction and annals (FOUND-ed); CASTLE the Interior Castle (Stanbrook) with Zimmerman's notes (CASTLE-ed); WAY the Way of Perfection; BREV the Roman Breviary; JCL the Life of John of the Cross; ASS Acta Sanctorum; PASC Pascal; LIG and LIGM Liguori; GUY Guyon; LOW Lowndes. Every cited line was re-read in its file. The researcher's line numbers were mostly right to within a few lines; the numbers below are the ones read.

## Fields

| Field | Evidence |
|---|---|
| `otherNames` | "Teresa of Jesus": LIFE 2212; "Theresa": BREV 79186. |
| `knownFor` | The brief, paragraphs 1-2, 5-9; VIDA 19301-19305, 17655-17656; LIFE 16719-16735; CASTLE 1753-1761, 1842-1846, 2017-2018; LIFE-L 2214-2219. |
| `datesNote` | Birth: BREV 79186-79193. Entry: LIFE-Z 676-722, BREV 79223-79225. St. Joseph's: VIDA 19301-19305, LIFE-L 1891-1893. Life: LIFE-Z 1182-1183, LIFE-L 1907-1911. First commission: FOUND 570-573. Duruelo: FOUND 700-703. Denunciation: VIDA-ed 6150-6154; Pastrana LIFE-L 2154. Censure: LIFE-L 2383-2385, VIDA-ed 6230-6231. Castle: CASTLE-ed 464-467. 1580 and 1593: FOUND-ed 2380-2386, FOUND 3677-3678. Death: FOUND-ed 2490-2493, 2537-2549, BREV 79312-79313, 79377-79378. 1588: LIFE-L 2415-2428. 1614 and 1622: FOUND 3686-3690, JCL 9264-9267, BREV 79325-79327. |
| `placeNote` | BREV 79190-79192; FOUND 1035-1039; FOUND 700-703, 757-758; CASTLE 1689-1691; FOUND 3792-3794; FOUND 977; FOUND 2493. |
| `role` | The brief; FOUND 766-769; LIFE-L 1885-1893. |
| `keyWorks` 1-3 | Life: VIDA 9387-9392, LIFE-Z 1182-1183; Castle: CASTLE 1644, 1689-1693, 1753-1761, 2017-2018, VIDA-ed 1320; Foundations: FOUND 3790-3796. |
| `legacy.traces` 1-6 | FOUND 2380-2386, 3677-3678, tree's `legacy`; FOUND 766-772, 760-763, 977; LIFE-L 2415-2428, LIFE-Z 1191-1199, VIDA-ed 4196-4219; CASTLE-ed 751-757; BREV 79252-79253, 79325-79327, tree's `legacy` (Doctor, 1970); ASS 14101-14108. |
| `legacy.remembered` 1-5 | LIFE-L 2214-2219, 2370-2375; LIFE-L 1916-1931, 1952-1954, 2095; LIFE-L 2389-2398; PASC 15024-15029, LIG 2659, 2687-2689, LIGM 11853, GUY 6781; LOW 10174-10187. |
| `uncertain` 1 | LIFE-Z 676-722; BREV 79223-79225. |
| `uncertain` 2-4 | BREV 79226-79227; FOUND 1040-1050, 1060-1072; LIFE 16719-16735, FOUND 1046-1048. |
| `uncertain` 5 | LIFE-Z 1182-1183, 1218-1224; LIFE-L 1885-1891, 1895-1911. |
| `uncertain` 6-8 | VIDA-ed 6191-6200; LIFE-Z 1135-1158; LIFE-L 2102-2111, 2154-2161, 2189-2196; LIFE-L 2214-2248, 2365-2386; LIFE-ed 18975-18983. |
| `uncertain` 9-10 | LIFE-L 2389-2398; VIDA-ed 6185-6190; LIFE-Z 1197-1199, LIFE-L 2424-2426; FOUND 760-772, BREV 79252-79253. |
| `uncertain` 11-13 | FOUND-ed 2034-2040, 2064-2073; LIFE 16747-16750, 16765-16770, LIFE-ed 16771-16772; WAY 1354-1357, 1366-1372; LIFE-L 1836-1855, LIFE-ed 12427-12428, VIDA-ed 4196-4205. |
| `uncertain` 14-19 | FOUND-ed 15384-15414, VIDA-ed 17947-17949; FOUND 2524-2549, BREV 79312-79313, 79377-79378; CASTLE-ed 613-621, 664-671, 738-741; CASTLE-ed 503-523; the tree's entry (`documentedStories`); the tree's `legacy`. |
| `sources` | One entry for each file the card cites. |
| `briefReferences` | One line for each paragraph of the brief. |

## Quoted spans

| Span in the brief | Entry | Status |
|---|---|---|
| "I crossed this stormy sea ... fall once more." | VIDA 8724-8725 (Spanish); LIFE 5439-5441 (English) | awaiting second reading |
| "People came to me in great fear. ... never afraid." | VIDA 17931-17934; LIFE 17113-17117 | awaiting second reading |
| "burn it at once." | VIDA 9391; LIFE 6335-6336 | checked at card |
| "not a deceiver." | LIFE 2371 (English only) | checked at card |
| "I thought of the soul as like a castle ... dwelling places." | CASTLE 1759-1778 (English only) | awaiting second reading |

Each `modern` is the brief's wording exactly (taken from the brief file by pattern, including the period inside the short spans). Each `printed` and `englishPrinted` is taken from its lines. The Spanish is printed as the original, with Lewis's English beside it as `englishPrinted`; the validator's companion keys are used. No `secondReading` is written for the three long ones.

## Conflicts and claims to check

1. **The castle quotation cannot pass the line check as it stands.** The print breaks the sentence after "just as in heaven there are": footnotes and a page heading stand in CASTLE 1762-1777, and footnote marks ("1" after "castle", "*" after "crystal") stand in the sentence. The `printed` text omits them. The validator needs a `drop` reading in `tools/quote_scan_readings.json` for those lines and marks; I did not edit that file.
2. **The tree's entry for the Carmelite reform** (the starting list for a new person) differs from the held sources on three points, all in `uncertain` 7 and 18: its documented story has the Inquisition of Toledo take the manuscript (Lewis has Madrid, LIFE-L 2189, 2192-2193); it dates Báñez's report 7 July 1575 (6 July in de la Fuente's printing, 7 July in Silverio's note from the autograph); and it says the book was to be shown to no one (the censure says not to every one, but only to men of learning). The tree's own record marks that story as taken from reference summaries, with the primary text not yet read. The tree's Doctor of the Church line (1970) is not in a held text.
3. **Spanish originals.** VIDA is clean at the passages used. LIFE is fair, with stray errors, and every printed English span read as written. The Castle, the Way and the Foundations are not held in Spanish, so no original is printed for the Castle quotation. Báñez's Spanish is not held, so "not a deceiver" has English alone.
4. **Claims not found:** that Medina del Campo was the first house after St. Joseph's (the dates in FOUND 929-930 and the names beside them are in separate columns of the scan, so the card gives only the first commission of 27 April 1567 and Duruelo of 1568); the year of Liguori's letter calling her his patroness (the lines do not give it, so the card gives none); the year of Báñez's deposition rests on Lewis's note at LIFE 18982-18983 (testimony given at Salamanca in 1591 in the Saint's process) and on Zimmerman's reference to the same deposition (LIFE-Z 1134-1135), which does not state the year itself; the Breviary's thirty-two houses and Báñez's "a dozen" and "nine" are given as each source's own count.
5. **Not used, left to the card's `uncertain` or left out:** the Breviary's wonders (the flight to the Moors, her death), the "living book" voice of 1559 (VIDA 14820), the vision of hell, the governor's threat to break the doors and the novices' answer (VIDA-ed 19600-19604, a later witness through an editor), the Lutherans in France as a second reason (kept only in `uncertain` 12), and John of the Cross's prison, which is the home entry's story.
