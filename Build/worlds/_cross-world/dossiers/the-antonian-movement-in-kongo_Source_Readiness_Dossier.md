# Source Readiness Dossier — The Antonian Movement in Kongo

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.11
**Corpus-map slug:** `the-antonian-movement-in-kongo`
**Time window:** 1704-1706
**Region(s):** Kongo; census `regions`: Africa
**Dossier author / date:** Claude, Library thread, Era VIII source-research pass, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-viii-2026-10`, this pass.

## 1. Already assigned

10 works across 7 vendored files in `cic/corpus-map/the-antonian-movement-in-kongo.yaml`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Letters, charters and inquests of D. Afonso I (Mvemba a Nzinga), king of Kongo, 1512-1540s, in Portuguese | afonso-i-of-kongo | antecedent | provisional | the documents in Afonso's name, file line 441 onward (see the first row) | `paiva-manso_historia-do-congo-documentos-por_1877.txt` |
| A Curious and Exact Account of a Voyage to Congo, by Angelo and Carli (English of 1704, in Pinkerton XVI) | carli | context | assigned | 'Voyage to Congo by Angelo and Carli', from the contents entry and its running heads | `pinkerton_general-collection-voyages-and-travels-v16_1814.txt` |
| Viaggio nel regno del Congo (1671), Carli's narrative | carli | context | assigned | Carli's narrative after Guattini's death | `carli_viaggio-nel-regno-del-congo-ita_guattini1671.txt` |
| Istorica descrizione de' tre' regni Congo, Matamba, et Angola (1687) | cavazzi | context | assigned | books one to seven; the passages on Kongo, the Capuchin missions and Kongo religion | `cavazzi_istorica-descrizione-tre-regni-congo-matamba-angola-ita_alamandini1687.txt` |
| Viaggio nel regno del Congo (1671), the joint part of the narrative | guattini | context | assigned | the opening part of the narrative, before Carli writes alone | `carli_viaggio-nel-regno-del-congo-ita_guattini1671.txt` |
| A Report of the Kingdom of Congo (1591), English of 1881 | lopes | antecedent | provisional | Books one and two; the chapters on the kings and the coming of Christianity | `lopes_report-of-the-kingdom-of-congo_hutchinson1881.txt` |
| A Voyage to Congo and several other countries chiefly in Southern Africk, by Merolla (English of 1704, in Pinkerton XVI) | merolla | context | assigned | 'Merolla's Voyage to Congo', under its own running heads | `pinkerton_general-collection-voyages-and-travels-v16_1814.txt` |
| Breve, e succinta relatione del viaggio nel regno di Congo (1692) | merolla | context | assigned | both parts | `merolla_breve-e-succinta-relatione-viaggio-congo-ita_piccardo1692.txt` |
| History of Loango, Kakongo, and other Kingdoms in Africa, by Proyart (English, in Pinkerton XVI) | proyart | context | provisional | 'History of Loango, Kakongo' and its chapters | `pinkerton_general-collection-voyages-and-travels-v16_1814.txt` |
| Missions- und Reise-Beschreibung nach Congo (German 1715; Italian 1712) | zucchelli | context | assigned | the twenty relations; especially the later relations on Soyo, the war for the kingdom and Pedro IV | `zucchelli_missions-und-reise-beschreibung-nach-congo-deu_1715.txt` |

## 2. Cross-link opportunities

| file | locus | why | suggested role / confidence |
|---|---|---|---|
| paiva-manso_historia-do-congo-documentos-por_1877.txt | documents CC to CCVIII, from the royal letter of 5 March 1700 (file line about 16099) to Pedro Mendes's letter on the state of Kongo, 2 January 1710 (heading at about 16560) | The only vendored documents inside the movement's own years: the Count of Soyo's Latin letters to the Capuchin general (4 October 1701; 28 August 1708), the governor of Angola on the Kongo mission (29 July 1703), the Overseas Council on letters of Soyo and fr. André de Pavia (30 August 1709), and Mendes's narrative of the civil war, including Pedro IV's taking of São Salvador and the death of Pedro Constantinho 'Quibango' on 15 February 1709 (about line 16790). A grep found no mention of Beatriz or the Antonians in these documents. The bucket today holds only the Afonso I row (antecedent). | context / provisional (a reader should confirm what Mendes says of the restoration) |
| paiva-manso_historia-do-congo-documentos-por_1877.txt | the seventeenth-century documents (D. Alvaro II onward) | The two-century Kongo-Christian matrix the census asks for: the court's correspondence with Lisbon and Rome. | antecedent / provisional |

No other vendored file carries Kongo matter of weight: Telles and Ludolf mention Congo three times each in passing; the Propaganda Fide Collectanea mentions Angola once (about line 45482) and was not read for Kongo.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Istorica descrizione de' tre' regni Congo, Matamba et Angola (second scan, Ghent) | Cavazzi | none | 1687 | https://archive.org/details/bub_gb_7MpQAAAAcAAJ | PD by date | metadata API, djvu 3.27 MB, 23 October 2026 |
| Istorica descrittione de' tre regni (Milan reissue) | Cavazzi | none | 1690 | https://archive.org/details/istoricadescritt00cava | PD by date | metadata API, djvu 3.35 MB, 23 October 2026 |
| Historische Beschreibung der drey Königreichen Congo, Matamba und Angola | Cavazzi | unnamed (German) | 1694 | https://archive.org/details/b3327521x | PD by date | metadata API, djvu 2.79 MB, 23 October 2026 |
| Relation historique de l'Ethiopie occidentale, vols 1-5 | Cavazzi, adapted by Jean-Baptiste Labat | Labat | 1732 | https://archive.org/details/relationhistoriq01cava (and ...02, ...03, ...04 cava; vol. 5 b33014759_0005) | PD by date | metadata API, djvu about 0.5-0.65 MB each, OCR 0.70-0.82, 23 October 2026 |
| Breve, e succinta relatione (Naples and Rome copies; Naples reprint) | Merolla | none | 1692; 1726 | https://archive.org/details/bub_gb_psuQriUlOSwC ; https://archive.org/details/gri_33125011120454 | PD by date | metadata API, djvu 0.63-0.73 MB, 23 October 2026 |
| A Voyage to Congo (English, separate scan; host date 1682 is wrong, it is the English of 1704) | Merolla | unnamed | 1704 | https://archive.org/details/voyagetocongosev00mero | PD by date | metadata API, djvu 0.58 MB, 23 October 2026 |
| Viaggio nel regno del Congo (Bologna edition) | Guattini and Carli | none | 1679 | https://archive.org/details/bub_gb_i2sLzjITfecC | PD by date | metadata API, djvu 0.39 MB, 23 October 2026 |
| A New General Collection of Voyages and Travels, vol. III (carries Carli and Merolla in English) | Thomas Astley (publisher) | unnamed | 1745 | https://archive.org/details/b30414283_0003 | PD by date | metadata API, djvu 3.31 MB, OCR 0.80, 23 October 2026 |
| A Report of the Kingdom of Congo (other scans) | Lopes and Pigafetta | Hutchinson | 1881 | https://archive.org/details/areportkingdomc00hutcgoog | PD by date | metadata API, djvu 0.38 MB, 23 October 2026 |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Bernardo da Gallo's and Lorenzo da Lucca's relations | The only contemporary record of Beatriz, her trial and burning | No public-domain print found. Archive manuscripts; modern editions (Cuvelier, Relations sur le Congo du père Laurent de Lucques, 1953; Brásio, Monumenta Missionaria Africana, 1952 onward; Thornton) are in copyright or 1931-1963 renewal-check territory. |
| Monumenta Missionaria Africana (Brásio) | The census names it for the court's correspondence | Vol. I is 1952 and later volumes later still; the IA copies (dli.ernet.535459 and others, monumentamission01bras) are a lead for rights review only, never a download. |
| Cardoso's Kikongo Doutrina Christãa (1624) | The census names the 1624 catechism | No scan found on the Internet Archive under title or author searches. |
| Gentilis Angollae fidei mysteriis (1661), Kimbundu catechism | A seventeenth-century African-language catechism | Kimbundu (Angola), not Kikongo; and the OCR is garbled (0.14). |
| Zucchelli, Relazioni del viaggio e missione di Congo (Venice 1712), Italian original | The original of the nearest witness | Not found on the Internet Archive by title or author; the German of 1715 is vendored instead. |
| Pigafetta, Regnum Congo (Latin, De Bry 1624) | Latin of Lopes | Garbled small djvu (0.29 MB); the 1881 English is clean. |
| Angel de Valencia, Copia fielmente sacada de una relacion (1646) | The first Capuchin report from Kongo | Djvu is 0.02 MB, effectively no text. |
| Van Wing, De geheime sekte van 't Kimpasi (1921) | A Kongo initiation society | Twentieth-century ethnography, not the movement; djvu 0.23 MB. Not pursued. |
| Labat, Relation historique (1732) | French reworking of Cavazzi in five volumes | A translation-adaptation of the vendored Italian; no Antonian matter found by grep. Listed as a lead only. |

## 5. Open cross-world questions

- Should Cavazzi and Lopes also stand in `mission-born-christianities-kirishitan-japan-kon` (VI.13, Kongo to 1650)? Rows are placed there as provisional.
- Proyart's History of Loango (1776) is placed provisionally as a later outside witness; whether coastal Loango and Kakongo belong to this world at all is unnamed so far.
- The census's second floor question (how far the teaching departed from the Christianity it grew out of) cannot be tested from these files, because none records the teaching.

## 6. Recommendation (portfolio decision for the project lead; does not block library work)

**Atlas only, unless the lead accepts a build without the movement's own record.** The public domain gives this world a good Capuchin and Portuguese matrix: the church Beatriz was raised in, the divided kingdom, and Pedro IV's restoration up to 1710. It gives nothing of the movement itself: no da Gallo, no da Lucca, no Salve Antoniana. Every vendored text is an outside, missionary or colonial witness, and most are hostile to Kongo religion. A Representative would have to speak for a movement whose words exist only in modern copyrighted editions, which runs straight into the never-invent rule. The census's own status (deferred, contested on record) fits this; a build becomes possible only if Thornton's translations or the Cuvelier edition can be licensed.

