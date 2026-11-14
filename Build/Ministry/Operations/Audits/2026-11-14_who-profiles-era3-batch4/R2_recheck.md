# R2 targeted recheck: era 3 batch 4


Reviewer: independent (Opus), did not draft these profiles and did not write R1. Review only: no repo file edited, no paid or model-API call, no web.

Scope: targeted, not a full re-review. Every R1 finding (A-B1 to A-M21, B-B1 to B-M25, C-B1 to C-M17) checked against the current files. Then the text R1 changed checked for new faults: false absences, editor's views told as settled, witness swaps, contested points told one way, unmarked partisans, unplaced common names, "X, not Y", colon-reveals, tails, narrator sentences past about 25 words, and the process word "held".

Method. I diffed the drafts commit (`a209487d`) against HEAD for every brief, card, audio script and `records.json`, so each R1 change was seen in place. I re-read every quotation added or changed in R1 against its vendored file by line number. Before accepting each new or reworded absence I searched every held file naming the person, and the Acta Sanctorum for 1 March around David's chronology. A script checked that each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed, and where the tags sit. It also checked narrator sentences past 25 words and every "held" in a brief or card. Readability is `engine.m1.gates.grade_text`, run from the repo root. The one brief fix proposed below was applied to a scratch copy and re-scored.

Line numbers: briefs and cards as they stand at HEAD; other files under `cic/texts/`.

## R1 findings

| Finding | Verdict | Note |
|---|---|---|
| A-B1 | resolved | All four witnesses marked; the order of ordination given both ways in l.3. |
| A-B2 | resolved | Card `uncertain` 5, sources and records as worded; "in banishment and otherwise" matches Evetts l.39586 (OCR "hanislnncnt"). See R2-M1 for a knock-on in `knownFor`. |
| A-B3 | resolved | |
| A-M1 | resolved | |
| A-M2 | resolved | l.1 and l.3 split. The new l.3 Zachariah sentence is 26 words, within "about 25". |
| A-M3 | resolved | |
| A-M4 | resolved | |
| A-M5 | resolved | Sophronius l.29642-29643 and Mansi 10 l.114428-114430 re-read. |
| A-M6 | resolved | |
| A-M7 | resolved | |
| A-M8 | resolved | |
| A-M9 | resolved | Garnier l.81419-81428 and Mansi 10 l.111238, 111607-111618 re-read. |
| A-M10 | resolved | |
| A-M11 | resolved | |
| A-M12 | resolved | |
| A-M13 | resolved | |
| A-M14 | resolved | |
| A-M15 | resolved | |
| A-M16 | resolved | Bar Hebraeus l.13365-13367 and the spurious Life PO19 l.15640-15648 re-read. |
| A-M17 | resolved | |
| A-M18 | resolved | |
| A-M19 | resolved | |
| A-M20 | resolved | |
| A-M21 | resolved | |
| B-B1 | resolved | See R2-M5 on the quotation marks in the new sentence. |
| B-M1 | resolved | |
| B-M2 | resolved | |
| B-M3 | resolved | On John's card. The Jacob card still gives Brooks's side alone (R2-M2). |
| B-M4 | resolved | |
| B-M5 | resolved | |
| B-M6 | resolved | |
| B-M7 | resolved | |
| B-M8 | resolved | |
| B-M9 | resolved | |
| B-M10 | resolved | |
| B-M11 | partly | The sides are added, but Hodgkin gives 569 flat, and his and Kugener's files are not in the card's sources (R2-M6). |
| B-M12 | resolved | |
| B-M13 | resolved | |
| B-M14 | resolved | |
| B-M15 | resolved | |
| B-M16 | resolved | |
| B-M17 | resolved | |
| B-M18 | resolved | |
| B-M19 | resolved | Strauch's file is not in the card's sources (R2-M7). |
| B-M20 | resolved | |
| B-M21 | resolved | |
| B-M22 | resolved | |
| B-M23 | resolved | |
| B-M24 | resolved | Niebuhr l.94037-94038 re-read ("epigrammata... recentiorum, nondum edita"). |
| B-M25 | resolved | |
| C-B1 | resolved | "the forty-fourth year, with one month now elapsed" matches Williams l.3951-3952. |
| C-B2 | resolved | The false absence is gone. See R2-M4 on the new wording. |
| C-M1 | resolved | |
| C-M2 | resolved | |
| C-M3 | resolved | |
| C-M4 | resolved | |
| C-M5 | resolved | The Bollandists' file is cited but not listed in the card's sources (R2-M3). |
| C-M6 | resolved | |
| C-M7 | resolved | Rees l.398-406 re-read, "perhaps exaggerating". |
| C-M8 | resolved | |
| C-M9 | partly | The card is right. The brief puts Rice Rees's place for Paulinus inside the Lives' scene (R2-M8). |
| C-M10 | resolved | |
| C-M11 | resolved | |
| C-M12 | partly | "Held" is gone, but the reworded absence on the synod of Brefi is false (R2-B1). |
| C-M13 | resolved | |
| C-M14 | resolved | |
| C-M15 | resolved | |
| C-M16 | resolved | |
| C-M17 | resolved | |

Of the 69 R1 findings, 66 are resolved and 3 are partly resolved (B-M11, C-M9, C-M12). None is not resolved.

## New findings

### R2-B1 BLOCKING (items 1, 7; false absence). David of Wales card, `uncertain` 6 (l.32); `records.json` `absent_details`

Card l.32: "The synod of Brefi. None of these sources gives a year for it." Records `absent_details`: "A year for the synod of Brefi — No held source gives one." This line was reworded under C-M12. The card's own new source, the Bollandists' commentary in the Acta Sanctorum for 1 March, gives a year that others assign: `acta-sanctorum_martii-tomus-1-lat_1735.txt` l.15583-15584 (OCR), "in Brtvienfi Synodo (ejnam Spelmann/tt, Vf- … fa-ins , aUitfmt anno dxix. habit am tradnnt)", that is, "in the synod of Brefi (which Spelman, Ussher and others say was held in the year 519)". No other held file I searched gives a year: Rees's Lives (l.656, 729, 2522, 14828, 18353-18434, 19597), Williams's Gildas, and the Annales Cambriae, whose "Synodus Victoriae" (l.2487) is the later synod.

Fix, card l.32: "The synod of Brefi. The Bollandists report that Spelman, Ussher and others put it in 519. The miracle of the rising ground is told by both Lives." In `records.json`, delete that `absent_details` entry and add a claim: `{"claim": "The synod of Brefi was held in 519, as Spelman, Ussher and others say", "witness": "Bollandists, Acta Sanctorum, 1 March (acta-sanctorum_martii-tomus-1-lat_1735.txt l.15583-15584, OCR-damaged)", "formation_confidence": "Inferential-Thin"}`. No brief change is needed.

### R2-M1 MINOR (item 7). Theodosius I of Alexandria card, `knownFor` (l.7) and `place` (l.9)

`knownFor`: "lived most of his patriarchate in exile near Constantinople". After A-B2, `uncertain` 5 in the same card gives the other side: "The Ethiopic Synaxarium gives twenty-eight years of exile in Upper Egypt" (budge1928 l.37624-37626, "remained in exile in Upper Egypt for eight and twenty years"). `place` also gives John's Dercus with no owner. The brief says only "in exile", which is right. Fix, `knownFor`: "...who refused the council of Chalcedon, lived most of his patriarchate in exile, and gave his name to the Theodosians of Egypt." `place`: "...; Constantinople and the fortress of Dercus in Thrace in his long exile, by John of Ephesus".

### R2-M2 MINOR (item 7). Jacob Baradaeus card, `uncertain` 1 (l.26)

"Brooks calls Jacob John's hero, and notes that in the quarrel of 575 John stood on the other side." "Notes" tells Brooks's reading as fact. B-M3 showed that Michael the Syrian says the opposite, and John's card now gives both sides: Michael l.25322-25325, "il ne se sépara point d'eux; mais il avertit et blâma les deux partis". Fix: "Brooks calls Jacob John's hero, and places John on the other side in the quarrel of 575. Michael the Syrian says John did not break with Jacob's party but rebuked both sides."

### R2-M3 MINOR (items 1, 12). David of Wales card, `sources.about` (l.35-71)

`uncertain` 1, 2 and 5 (l.27, 28, 30) now cite the Bollandists, but the Acta Sanctorum file is not among the card's sources. This is the same gap as A-M6. Fix: add `{"title": "Acta Sanctorum, March, tome 1: commentary and Life of David from a Utrecht manuscript", "author": "The Bollandists", "date": null, "language": "Latin", "file": "cic/texts/acta-sanctorum_martii-tomus-1-lat_1735.txt"}`.

### R2-M4 MINOR (items 1, 4). David of Wales card, `uncertain` 5 (l.30)

"...reckon his birth from the same story of Patrick; the scan of their numbers is too damaged to read." "The scan" is a Library status line in participant text, the same class as "held". The clause also overstates the damage. The starting point is legible: Patrick's stay comes eighteen years before the mission of 432, "ab anno igitur ccccxiv", with the margin "An. 414". Only the result is garbled: "ad annum CCCCXIV. pervenitur" (l.15507-15528). Fix: "The Bollandists, in the Acta Sanctorum for the first of March, count his birth thirty years after Patrick's stay in the valley of Rosina, which they put in 414." Records claim: add "start 414 (l.15519, margin)" and keep the result unsettled.

### R2-M5 MINOR (item 2). John of Ephesus card, `uncertain` 6 (l.40)

"...Michael the Syrian, who tells of \"the bishop John\" held a year in prison at Chalcedon". The quotation marks hold English words that are not in the vendored file, which reads "l'évèque Jean" (Michael l.26288). B-M23 found the same fault in the Agathias card. Fix: "His source is Michael the Syrian, who tells of a bishop named only as John, held a year in prison at Chalcedon, who died on the day he had foretold."

### R2-M6 MINOR (items 1, 12). Victor of Tunnuna card, `uncertain` 6 (l.36) and `sources.about` (l.51)

"Thomas Hodgkin and M.-A. Kugener give about 569." Hodgkin gives a flat year: `cassiodorus_variae-letters-hodgkin1886.txt` l.25465, "Victor Tunnunensis, chronicler (died in 569)". Kugener hedges: `zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.26977, "Victor mourut vers l'an 569". Neither file is in the card's sources. Fix: "Gallandi thinks shortly after 566; Thomas Hodgkin gives 569, and M.-A. Kugener about 569." Add both files to `sources.about` ("Index to The Letters of Cassiodorus", Thomas Hodgkin, English; "Notes to the Life of Severus", M.-A. Kugener, French).

### R2-M7 MINOR (items 1, 12). Cassiodorus card, `uncertain` 1 (l.40) and `sources.about` (l.65)

The new "Philipp Strauch as 563" (B-M19) and the existing "Hugh Williams gives his death as 570" cite files the card does not list: `langmann_offenbarungen-gmh_strauch1878.txt` l.22202, "Cassiodori Senatoris (f 563)", and `gildas_de-excidio-britanniae-lorica-penitential-lat-eng_williams1899.txt` l.286. Fix: add both to `sources.about` (Strauch, notes to Die Offenbarungen der Adelheid Langmann, German; Williams, notes to Gildas, English).

### R2-M8 MINOR (items 1, 7; a modern identifier inside the source's scene). David of Wales brief l.1, and the audio script

"Paulinus, his old teacher from the White House on the Tave, told them to send for David." The paragraph is told as "the Lives of David say". The White House on the Tave is Rice Rees's, as W. J. Rees quotes him (Rees l.18001, "afterwards in the school of Paulinus, in White House on Tave"), and the records tag it Contested. The Latin Life puts Paulinus "in a certain island" (Rees l.18905-18907). The scene's own Welsh Life gives an identifier: "Saint Paulinus, who was an old holy bishop" (l.18377), and "a master who was called Paulinus... and he taught David" (l.18117-18119). The phrase "his old teacher" also comes before David is named. Fix, brief l.1 and audio: "Paulinus, an old bishop who had once taught David, told them to send for him." The card's attributed form (l.31) stays. Brief then 323 words, FK 6.4, Flesch 74.3.

### Checked and not findings

- Audio: each of the ten scripts equals its brief once `[calmly] ` and `[warmly] ` are removed. Each opens with `[calmly]` and has one `[warmly]`, at the start of the last paragraph. There are no tags in any brief or card.
- "Held": every remaining use in a brief or card is ordinary English (held back, held at Dercus, held in the city's monasteries, held the see, held the office, held a year in prison). None is the Library sense.
- Quotations added or changed in R1, re-read against the vendored files. Gildas: Williams l.3951-3952. Theodosius: Evetts l.39586; Garnier l.81419-81428. Jacob: Michael l.24984-24987; Bar Hebraeus l.13365-13367; PO18 l.39674; PO19 l.15640-15648. David: Williams l.23071-23074. Victor (records): Mommsen l.17577-17578; Noris, PL68 l.73057-73058. Cassiodorus (records): Hodgkin l.3141-3147 and l.3757-3770; PL70 l.84039-84060. All are verbatim, allowing for OCR, except R2-M5.
- New absences: Longinus "The sources give nothing of his origin, his age or his death", Jacob "The sources give no year of birth" and Radegund "None of these sources gives a year of birth or of her capture" stand on R1's searches, and nothing I read contradicts them. The Brefi absence is R2-B1.
- Narrator sentences past 25 words in changed text: only Theodosius l.3, at 26. The others past 25 (Theodosius l.5 and l.9, Longinus l.1 and l.5, John l.7, David l.11, Cassiodorus l.5, Gildas l.1) carry quotations or were cleared in R1.
- I found no new "X, not Y", colon-reveal, tail or unplaced common name in the changed text. Victor's "a later copyist" for Noris's "corruptoris cujuspiam" is a fair gloss. Victor's "who died in 565 by Mommsen's introduction" follows Mommsen's "narratio perveniat ad a. 565" with Justinian's death at its end; it is R1's wording and holds.
- Card order: all follow Mark's order except the Jacob card, whose `sources` lists `about` before `ownWords` (l.36, l.87). The pattern orders "Their own words" first, and the nine other cards do. This is a one-line reorder and is noted here, not counted.

## Length and readability (current files)

| Profile | Words | Time @162 | FK | Flesch | Cap | Pass |
|---|---|---|---|---|---|---|
| Theodosius I of Alexandria (major) | 401 | 2:28 | 7.2 | 66.1 | 405 | yes |
| Jacob Baradaeus (major) | 402 | 2:28 | 6.0 | 75.6 | 405 | yes |
| Cassiodorus (major) | 405 | 2:30 | 6.3 | 75.8 | 405 | yes, at the cap |
| Gildas (major) | 403 | 2:29 | 6.2 | 75.8 | 405 | yes |
| Longinus, bishop of the Nobadae | 320 | 1:58 | 7.1 | 70.2 | 325 | yes |
| John of Ephesus | 320 | 1:58 | 6.2 | 74.2 | 325 | yes |
| Victor of Tunnuna | 321 | 1:58 | 8.0 | 60.6 | 325 | yes, near the Flesch floor |
| Agathias of Myrina | 323 | 1:59 | 6.2 | 73.6 | 325 | yes |
| David of Wales | 325 (323 with R2-M8) | 2:00 | 6.4 (6.4) | 74.4 (74.3) | 325 | yes |
| Radegund | 326 | 2:00 | 5.7 | 76.6 | about 325 | yes |

Every `briefLength` matches its word count. R2-B1 and R2-M1 to R2-M7 touch only cards and records, so no other brief changes.

Totals: R1 findings 66 resolved, 3 partly, 0 not. New in R2: 1 blocking (R2-B1) and 8 minor (R2-M1 to R2-M8).
