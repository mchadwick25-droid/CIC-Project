# Card edits: Arius

Card writer, 2026-11-17. Worked from `arius.original.card.json`, `arius.brief.txt`, `Outline.md` and `Source_Sheet.md`. Output: `arius.card.json`. Every original field is kept word for word and in order; the new fields and list entries are added.

## New

| # | Old words | New words | Evidence |
|---|---|---|---|
| N1 | (none) | `"briefLength": "about 3 minutes"`, after `role` | The brief is 458 words. The batch-2 era-3 cards run at about 160 words a minute (403 words = about 2 min 30 s; 378 = about 2 min 20 s), which gives about 2 min 52 s. Recheck.md: "about 3 minutes". |
| N2 | (none) | `sources.ownWords`: Letter to Eusebius of Nicomedia, in Panarion 69.6 (Arius, in Epiphanius of Salamis; Greek, with Latin translation; epiphanius Oehler file) | Q1 is rendered from this Greek: epiphanius_panarion-haer-48-69-...oehler1860.txt 45736-45738. |
| N3 | (none) | `sources.about`: Socrates, Church History 2.10, with the Antioch letter of 341 (Greek, Hussey) | Q3 is rendered from it: socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt 16658-16659. |
| N4 | (none) | `sources.about`: The Creed of Nicaea, in The Seven Ecumenical Councils (npnf214) | Brief: "Its creed ended by cursing anyone who said 'before he was begotten he was not', or that the Son came 'of things that were not'." npnf214 2419-2425. |
| N5 | (none) | `sources.about`: Acts of the Council of Aquileia (381), Mansi vol. 3 | Brief: "at Aquileia, two bishops said they did not know who Arius was". Mansi 3 60273 ("Ego Arium non novi"), 61131-61133 ("Qui fuerit Arius, ignoro"); Palladius deposed 60851-60853, 61005-61008. |
| N6 | (none) | `sources.about`: Kauffmann, Aus der Schule des Wulfila (1899), editor's account of Aquileia | Brief: "the council deposed them both." Kauffmann 1957-1958: "einstimmig wurden Palladius und Secundianus als ketzer ihrer ämter für unwürdig erklärt." |
| N7 | (none) | `briefReferences`, twelve entries | One per beat the brief draws on, each traced in Outline.md and Source_Sheet.md (S1, S4, E6-E9, E13-E15, E17, I2, I4, I6). |
| N8 | (none) | `quotationOriginals` Q1: modern "We are persecuted because we said: the Son has a beginning, but God has no beginning." / printed "Διωκόμεθα δὲ ὅτι εἴπομεν, Ἀρχὴν ἔχει ὁ υἱὸς, ὁ δὲ θεὸς ἄναρχός ἐστι." | Re-read at epiphanius Oehler 45736-45738 (OCR; ϑ, ᾿Δρχὴν and ἀναρχός corrected mechanically, as Source_Sheet's OCR note does). Checked against npnf203 6045-6046. |
| N9 | (none) | Q2: modern "I have walked in their footsteps, ... wisdom and knowledge." / printed "Along their track, have I been walking, with like opinions. I the very famous, the much suffering for God’s glory; And taught of God, I have acquired wisdom and knowledge." | Re-read at npnf204 41472-41479. Greek compared at PG 26 1192, 1221-1225 (OCR second witness). |
| N10 | (none) | Q3: modern "We have not been followers of Arius. For how could we, who are bishops, follow a priest?" / printed "Ἡμεῖς οὔτε ἀκόλουθοι Ἀρείου γεγόναμεν. πῶς γὰρ ἐπίσκοποι ὄντες ἀκολουθήσομεν πρεσβυτέρῳ;" | Re-read at Hussey 16658-16659 (the outline gives 16656-16657 and the source sheet 16656-16658; the Greek stands at 16658-16659). OCR "' Apelov" and "ἀκολουθήσομενν" corrected. Checked against npnf204 57418-57419. |
| N11 | (none) | The brief's four quoted fragments: "as atheists" (npnf203 6026); "enemies of Christ" (npnf204 19018); "before he was begotten he was not" (npnf214 2422); "of things that were not" (npnf214 2422-2423) | Each re-read in its file; the brief's words match the printed English. |

No `secondReading` field is given: no second reading of these quotations is held in this folder.

## Clearly wrong

None. Every statement in the original card was checked against the held sources and the brief:
- Robertson's "obscure" origin, his note on Constantine's letter, and "a native of Libya": npnf204 1672-1676, 1702-1705.
- Socrates's "there was a time when the Son was not": npnf202 2096.
- Photius calling Philostorgius a liar: philostorgius 52.
- Athanasius's account from Macarius and the death the day before his reception: npnf204 70066-70106.
- Sozomen's three views: npnf202 30400-30406.
- Theodoret, Church History 1.4: npnf203 chapter heading "The Letter of Arius to Eusebius".

## Not found

- `legacy.traces[0]`: "The churches later called Arian, which held with him that the Son was not eternal." No held source on the source sheet shows what the later Homoian churches held about the Son's eternity. Left in place.

## After the card check (2026-11-18)

Made by the batch coordinator to `Card_Check.md`'s exact corrections (N8, N10):
- Q1 `printed` now stands as the file has it, OCR and all (Oehler 45736–45738); the true readings are in `uncertain`. Every word was checked by script to stand in those lines.
- Q3 `printed` likewise (Hussey 16658–16659), with the true readings in `uncertain`.
- The not-found claim ("The churches later called Arian, which held with him that the Son was not eternal") stays in place, as the checker ruled, and is registered in Open-Gaps.
