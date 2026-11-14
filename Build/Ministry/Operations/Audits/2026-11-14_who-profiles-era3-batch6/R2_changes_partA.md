# R2 changes, part A: era 3 batch 6

Each R2 finding, what was done, and where. Files are under `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`, and line numbers point to files under `cic/texts/`. Every cited line was opened in its vendored file before the change was made. No brief changed, so the audio scripts stand as rebuilt after R1. `records.json` was re-loaded just before the write, and only the `isidore-of-seville` entry changed (indent=1, ensure_ascii=False). R2-A-M4, the README and the `"date": null` keys, is left to the lead. No date key was added or removed, except the one carried in R2-A-M3's new source entry.

| Finding | Done |
|---|---|
| R2-A-M1 (Columbanus `keyWorks` 3: 35-word sentence) | Taken as worded. The longest sentence is now 23 words. |
| R2-A-M2 (Isidore `uncertain` 5: Pagi's condition dropped) | Taken as worded. Confirmed mansi10 l.59531-59534: "haec synodus ad an. 618 retrahenda, si tamen mense Novembri aut Decembri celebrata sit, qua de re non satis liquet" (OCR "Horum crium", "648", "fity"). The card now reads: "That sets it in 618, he says, if it met in November or December, which is not clear." |
| R2-A-M3 (Isidore: the Breviarium preface is Lorenzana's, and two sources were missing) | Taken. Confirmed PL 86 l.385-390 ("FRANCISCUS ANTONIUS LORENZANA, ARCHIEPISCOPUS TOLETANUS … LECTORI SALUTEM") and l.474. Card `uncertain` 4 is changed as worded. Both `sources.about` entries were added as worded: Lorenzana's, with "date": "1775" from the Library file header, and Pagi's, with no date key. Records: the claim now names Lorenzana, and its witness cites l.385-390 and 474. The presiding `contested_claim` side names Lorenzana, with "reprinted in PL 86". |

None was declined.

### Length and readability

No brief changed. The figures are as after R1:

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| Columbanus (major) | 403 | 2:29 | 7.6 | 67.1 |
| Isidore of Seville (major) | 405 | 2:30 | 7.8 | 64.0 |
| John of Biclaro (recorder) | 325 | 2:00 | 7.9 | 64.6 |
