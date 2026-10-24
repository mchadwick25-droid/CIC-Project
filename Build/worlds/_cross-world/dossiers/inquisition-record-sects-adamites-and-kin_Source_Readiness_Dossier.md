# Source Readiness Dossier — Inquisition-Record "Sects" (Adamites and Kin)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.13
**Corpus-map slug:** `inquisition-record-sects-adamites-and-kin`
**Time window:** fourteenth and fifteenth centuries (the census gives "14th–15th c."; the Adamites of 1421 and the depositions of the 1330s to 1390s)
**Region(s):** Central Europe (Bohemia, Silesia, the German lands)
**Dossier author / date:** Era VI library session, latinwest batch, October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. Before this pass no bucket file existed for this entry. This pass vendored four files and staged them here. Registry entries, seed rows and cross-link rows sit in the lead's snippet files until merged.

**Evidential status.** The census status is "Contested – Evidentiary". Every source for this entry is a hostile record: a chronicle by the people who destroyed the Adamites, an inquisitor's deposition, a papal list of errors that circulated as a template. No voice from inside any of these groups survives. The records say what the questioners expected to find. This dossier says so in each row.

## 1. Already assigned

Every row is a file vendored this pass. Scale is the vendored file size in characters, header included.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Wattenbach, Über die Secte der Brüder vom freien Geiste (1887), with the deposition of John of Brünn (whole academy volume) | wattenbach | context | assigned | ~1.97M chars | `wattenbach_secte-der-brueder-vom-freien-geiste-sitzungsberichte-berlin-deu_1887.txt` |
| Haupt, Beiträge zur Geschichte der Sekte vom freien Geiste und des Beghardentums (Zeitschrift für Kirchengeschichte VII, 1885; whole journal volume) | haupt | context | provisional | ~1.59M chars | `haupt_beitraege-sekte-vom-freien-geiste-zeitschrift-kirchengeschichte-bd7-deu_1885.txt` |
| Tractatus de origine Hussitarum, with a passage on the Adamites (Höfler II, 1865) | hofler | context | provisional | ~2.22M chars | `hofler_geschichtschreiber-husitischen-bewegung-v2-lat_1865.txt` |
| Articuli sacerdotum hereticorum et Pikharditarum, and the Anonymus de origine Taboritarum (Höfler I, 1856) | hofler | context | provisional | ~1.89M chars | `hofler_geschichtschreiber-husitischen-bewegung-v1-lat_1856.txt` |

**What each shows.**

- **John of Brünn.** Wattenbach prints the Latin deposition of Brother John of Brünn, a Dominican examined as a member of the sect (it begins "Ego frater Johannes de Brunna"), from the Greifswald manuscript, with a report on the sect's relation to the "willing poor" and further Waldensian protocols. Wattenbach notes that the report on the willing poor describes an ascetic, wholly orthodox life and that its author shows no thought of the Free Spirit doctrine.
- **The error-list.** Haupt prints and compares the lists of errors (the Mainz manuscript and the Passau anonymous's list) that inquisitors used. This is the template. His article is on pp. 503 ff. of the volume.
- **The Adamites.** Höfler II's *Tractatus de origine Hussitarum* (item XIX) names the Adamites ("Adamitis, qui nudi gradiuntur") and, in another passage, Waldensians, Taborites and Adamites together. Höfler I prints the Picard articles. Neither is a record of what the Adamites said.
- **Not vendored: the Schweidnitz interrogations of 1332.** No text was found (§4).

**Scan quality.** Wattenbach 1887 and Haupt read well in German with Latin protocols; both files are whole volumes of a series, and only the named article is relevant. Höfler II reads with scattered letter errors.

## 2. Cross-link opportunities

Checked by searching the bodies of every `cic/texts/*.txt` for Adamites, Free Spirit, the Beguines and Beghards, Ad nostrum and the Council of Vienne, then opening the hits. Proposed rows are in the lead's `crosslinks.yaml`.

- **Lawrence of Březová, *Historia Hussitica*** (Hussite bucket). The chronicle names the Adamites' articles of 1421; Goll's editorial note (file line 1671) says they sit in the text before the inserted Picard and Waldensian articles. Hostile. Tier: same time-place. Proposed row: context / provisional.
- **Piccolomini, *Historia Bohemica*** (1592 and 1524 printings; Hussite bucket). Has a chapter "De Adamitis" (1592, file line 5132) and a heading "De Adamitis Hereticis" (1524, file line 300). A later outside observer. OCR poor. Tier: same time-place. Proposed rows: context / provisional.
- **Lützow, *The Hussite Wars*** (Hussite bucket). Fifteen mentions of the Adamites; file lines 5332–5337 argue they had no connection with Hussitism and cite the first mention of Adamites in Bohemia. Secondary. Tier: same time-place. Proposed row: context / provisional.
- **Van Braght, *Martyrs' Mirror*.** Names Adamites among the names given to dissenters (file line 41446) and mentions the Free Spirit seven times. Tier: same time-different-region. Proposed row: context / provisional.
- **Bernard Gui, *Manuel de l'Inquisiteur*, tome I** (Franciscan pass). "Erreurs des Béguins" (p. 153) and the Beguins' evasive answers (p. 188): the inquisitor's own description in the template's form. Tier: same time-different-region. Proposed row: context / provisional.
- **Limborch, *Liber sententiarum inquisitionis Tholosanae*** (Franciscan pass). The section "Culpe beguinorum" (file line 34571) and the Beguins' recantations. Coerced answers recorded by their judges. Tier: same time-different-region. Proposed row: context / provisional.
- **Ehrle, *Archiv*, Bd 3 and Bd 4** (Franciscan pass). Papal-court papers on the Beghini of Provence (Bd 3, file lines 746 and 931) and the Beguins' confessions from the Toulouse register (Bd 4, file lines 306–503). Tier: same time-different-region. Proposed rows: context / provisional.
- **Lea, *History of the Inquisition*, vol. III** (Franciscan pass). Beghards at file lines 7570, 27403 and 27702. The Free Spirit chapter and the Adamites (index: Adamites ii. 518, Taborites ii. 512–524) are in vol. II, which the shelf does not hold. Secondary. Proposed row: context / provisional. Vol. II is the wanted volume.
- Noted, no row proposed: Groote's Latin letters (`groote_epistolae-xiv-lat_acquoy1857.txt`) and Kempis's *Founders of the New Devotion* (eight and nine mentions of Beghards or Beguines). They are Devotio moderna witnesses of how the Beguine world was read, not records of the sects.

## 3. Verified acquisition leads

Each lead was checked on the host: item record read, text file fetched and sampled. The first two rows are vendored (the two Höfler volumes are listed on the Taborite dossier). Rights basis is public domain by date unless the row says otherwise.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Über die Secte der Brüder vom freien Geiste (Sitzungsberichte der Berliner Akademie, 1887). Vendored as `wattenbach_secte-der-brueder-vom-freien-geiste-sitzungsberichte-berlin-deu_1887.txt`. | Wilhelm Wattenbach | none (German with Latin) | 1887 | https://archive.org/details/sitzungsberichte1887deutsch | pd-us-by-date | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Zeitschrift für Kirchengeschichte, Band VII (1885), with H. Haupt, Beiträge zur Geschichte der Sekte vom freien Geiste. Vendored as `haupt_beitraege-sekte-vom-freien-geiste-zeitschrift-kirchengeschichte-bd7-deu_1885.txt`. | Herman Haupt | none (German with Latin) | 1885 | https://archive.org/details/bub_gb_dyUMAAAAIAAJ | pd-us-by-date; Public Domain Mark 1.0 on the item | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Sacrorum conciliorum collectio (Mansi), tomus 25 (Council of Vienne, 1311-1312). Not vendored: it prints Antoninus of Florence's summary of the eight errors of the Beguines and Beghards, not the decree. The decree is in the Clementines (Friedberg, Corpus iuris canonici II), which is not on the host. | Giovanni Domenico Mansi (editor) | none (Latin) | 1782 | https://archive.org/details/sacrorumconcilio0025joan | pd-us-by-date (1782 edition, Welter reprint) | October 2026: item metadata read; 3.6 MB file fetched and searched for Ad nostrum. |
| Beiträge zur Sektengeschichte des Mittelalters, II: Dokumente vornehmlich zur Geschichte der Waldenser und Katharer. Not vendored: Shared lead: the Franciscan pass had this item in its download folder at the time of the check. Grep the shelf before relying on it. | Ignaz von Döllinger | none (German with Latin) | 1890 | https://archive.org/details/beitrgezursekt02dl | pd-us-by-date (1890) | October 2026: item metadata read; metadata read (1.77 MB; first volume beitrgezursekt01dl 0.58 MB). |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Ad nostrum (Council of Vienne, 1312) in the Clementines, Friedberg, *Corpus iuris canonici* II (1881) | The template document, named in the task | Not on the host. The only Friedberg item found is vol. I (`bub_gb_sfwfAQAAMAAJ`, the Decretum only; fetched, 8.4 MB, no Clementines). The 1955 and 1959 reprints are borrow-only or in copyright. No public-domain English translation was found. Tanner (1990) is in copyright. |
| Mosheim, *De Beghardis et Beguinabus* (1790, `iolavrentiamosh00moshgoog`) | Prints the Vienne decrees and the Beguine documents | Fetched (1.49 MB). OCR poor, word-form coverage 0.25–0.39; "Ad nostrum" is not found by search. Eighteenth-century scholarship in any case. |
| The Schweidnitz beguines' interrogation, 1332 | Named in the task | Not located. The protocol is cited in Erbstösser's *Ketzer im Mittelalter*, in the *Neue Deutsche Biographie* and in a 1902 study of inquisition procedure in Germany. Searches on the host by title, place and date, and two full-text searches, found only citations. Haupt 1890 (Waldensian and inquisition papers, vendored under V.16) mentions the burnings at Schweidnitz but does not print the protocol. |
| Wattenbach 1887, separate offprint | A smaller file than a whole academy volume | None found. Two other Berlin Sitzungsberichte items dated 1887 (`sitzungsbericht24berlgoog`, `sitzungsbericht29unkngoog`) were fetched and searched; each has one line that mentions the sect and neither prints the article. |
| Jundt, *Histoire du panthéisme populaire au moyen âge* (1875, `histoiredupanth00jundgoog`) | French survey of the Free Spirit | Scholarship, not a source. Fetched (876 KB), not vendored. |
| Lerner, *The Heresy of the Free Spirit in the Later Middle Ages* (California, 1972) | The scholarly consensus on the template | In copyright. A reference for Step 0, not a library file. |
| Fudge (2002) and Kaminsky (1967) on the Adamites | The census's route to the Hussite side | In copyright. |
| Preger, *Geschichte der deutschen Mystik* (1874–1893) | Prints the Passau anonymous's error-list | Several scans exist (for example `geschichtederde05preggoog`). Not fetched: scholarship, and the list is in Haupt. |
| Staří letopisové čeští (Czech annals of the Adamites) | A Czech account | Not located (see the Taborite dossier). |

## 5. Open cross-world questions

- **Taborites and Adamites.** Tábor destroyed the Adamites (Lützow and Březová tell it). The Taborite world (V.11, inside the Hussite world) and this entry share Höfler I and II and Březová. Where the Adamites belong, as a Bohemian episode of the Hussite world or as one case of a wider pattern, is for Step 0.
- **Picards and Adamites.** Höfler I prints "articles of the Picards"; Březová prints "articles of the Adamites". Whether they are one group is a scholarly question that this pass does not decide.
- **The Free Spirit and the Franciscan worlds.** The Beguins of Languedoc and Provence belong to the Fraticelli and Spiritual Franciscans as well. Bernard Gui, Limborch, Ehrle and Lea are staged there. The Free Spirit pattern (Brother John of Brünn, the Schweidnitz beguines) is a different strand. State the line in Step 0.
- **The Waldensian entries.** Wattenbach 1886 and Haupt 1890 print German Waldensian protocols and the Brünn deposition sits beside them; the Waldensian entries claim the Waldensian ones.
- **A Representative without a voice.** No inside voice survives, so a conversational Representative would be spoken for by the record. That is a Representative-identity question.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says "cannot be assessed". The dossier agrees: no source states what the Adamites or the Free Spirit communities believed in their own words. The sources state what their examiners recorded.

**Sourcing (B1).** One deposition in Latin (John of Brünn, Wattenbach 1887), one list of errors (Haupt 1885; the decree itself is not on the host), one Hussite chronicle line on the Adamites and one set of Picard articles. Gui, Limborch and Ehrle add the Beguins' answers from Languedoc. No public-domain English translation exists for any of them. Lea vol. II, which treats the Free Spirit and the Adamites at length, is not on the shelf.

**Ecology (B2).** One shape: the questioner's record. A conversation would test whether the project can hold a voice that exists only as a defendant's answer. That is the central fact the sources show.

**Uniqueness (B3).** The entry has no church and no institution; nothing survives, and in some cases there may have been nothing to survive. It is a warning about method.

**Audiences (B4).** Historians of heresy take the template seriously. There is no institutional audience.

**Scale (B5).** About 7.7 million characters in four vendored files, two of them whole volumes of series (an academy year and a journal volume) of which only an article is relevant. The relevant material is a few hundred thousand characters.

**Recommendation: atlas only.** No voice from inside the groups survives, and every source is hostile, coerced or a template (B1, B2). There is no public-domain English leg and the decree that generates the template is not on the host. The entry earns its place on the Atlas as a map of what the records are, and the Hussite world can carry the Adamites as a Bohemian episode. This is a recommendation for Mark to weigh, not a decision.
