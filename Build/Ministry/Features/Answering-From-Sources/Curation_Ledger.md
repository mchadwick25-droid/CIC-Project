# Curation ledger (lpc Stage 2)

State at 2026-10-29, after the first run of the checker rules from PR #1329 over every committed curation. Companion to `Stage1_Ledger.md` and `Stage2_Change_Orders.md`. Plain facts; the sampling reviews and redo reports hold the line-level detail. Word counts are the Stage 2 run's measured words per file (`Stage2_Segmentation_Report.md`, section 5).

## Counts on main

- 237 partial or unmarked plain-text files in the union; 66 belong to lpc's shelf: 52 curated, 14 not curated.
- 52 curation files on main: 2 pilots, wave 1a (37: group A 4, group B 8, group C 25), wave 1b (13).
- Status in the yaml: 24 `drafted`, 18 `needs-redo`, 10 `sampled-ok`. (Before this triage: 24, 17, 11. Hefele-Leclercq moves from `sampled-ok` to `needs-redo`; see the triage below.)
- Of the 24 `drafted` files, 10 are on the `needs-redo-suspect` list below. Their yaml status stays `drafted` until a redo or an `expected_gaps` ruling; changing those 10 status lines is a separate step.
- `curate check` with the PR #1329 rules: 25 pass, 27 fail.
- Sampled: 29 of 52 (groups A and B in full, group C 16 of 25). Not sampled: 9 of group C, the 13 wave-1b files, the 2 pilots.

A green check does not mean `sampled-ok`. The checker sees unexplained numbering steps and false `allow_oversize` sentences. It does not see missed headings that leave no gap, wrong loci, running heads taken as entries, or text addressed at the wrong level.

## Checker result by file

### Pass (25)

| File | Status | Words |
|---|---|---|
| `augustine_civitate-dei-1-13-lat_hoffmann-csel40-1` | drafted | 220,201 |
| `augustine_civitate-dei-14-22-lat_hoffmann-csel40-2` | drafted | 244,160 |
| `augustine_confessiones-lat_knoll-csel33` | drafted | 169,301 |
| `augustine_de-catechizandis-rudibus-lat-eng_christopher1926` | sampled-ok | 143,334 |
| `augustine_de-catechizandis-rudibus-lat_krueger1893` | drafted | 27,543 |
| `augustine_sermones-post-maurinos-reperti-lat_morin1930` | needs-redo | 366,874 |
| `bardenhewer_geschichte-altkirchlichen-literatur-band2-cyprian-slice-deu_2e-aufl1914` | sampled-ok | 32,963 |
| `codex-theodosianus_latinlibrary` | needs-redo | 240,192 |
| `delehaye_passions-martyrs-genres-litteraires-fra_1921` | sampled-ok | 127,288 |
| `duchesne_histoire-ancienne-de-leglise-tome1-fra_3e-ed1907` | sampled-ok | 149,429 |
| `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902` | needs-redo | 64,574 |
| `harnack_vita-cypriani-commentary-lat-deu_1913` | sampled-ok | 46,322 |
| `koch_cyprian-und-der-roemische-primat-deu_1910` | drafted | 63,750 |
| `mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912` | needs-redo | 192,982 |
| `mesnage_afrique-chretienne-eveches-ruines-fra_1912` | needs-redo | 191,310 |
| `monceaux_histoire-litteraire-afrique-chretienne-tome1_1901` | sampled-ok | 238,916 |
| `monceaux_histoire-litteraire-afrique-chretienne-tome2_1902` | needs-redo | 166,307 |
| `monceaux_histoire-litteraire-afrique-chretienne-tomes6-7-fra_1922-1923` | sampled-ok | 297,793 |
| `perpetua-scillitan-martyrs-lat-grc_robinson1891` | needs-redo | 52,358 |
| `poschmann_abendlaendische-kirchenbusse-deu_1928` | drafted | 109,665 |
| `toulotte_geographie-afrique-chretienne-numidie-fra_1894` | drafted | 85,435 |
| `vonsoden_cyprianische-briefsammlung-deu_1904` | drafted | 104,123 |
| `vonsoden_ketzertaufstreit-rom-karthago-deu_1909` | drafted | 15,901 |
| `vonsoden_prosopographie-afrikanischer-episkopat-deu_1909` | drafted | 8,987 |
| `vonsoden_streit-rom-karthago-ketzertaufe-deu_1909` | drafted | 15,874 |

Seven `needs-redo` files pass the checker: Morin, Codex Theodosianus, the second Gebhardt scan, both Mesnage scans, Monceaux tome 2 and Robinson. Their defects are of the kinds the checker does not see.

### Fail (27)

| File | Status | Reason | Words |
|---|---|---|---|
| `acta-martyrum-selecta_gebhardt1902` | needs-redo | unexplained steps: `perpetua-greek` (3), `pionius` (3) | 65,693 |
| `augustine_de-fide-et-symbolo-de-opere-monachorum-et-al-lat_zycha-csel41` | drafted, suspect | unexplained steps in several section series (`s1`, `s5`, others) | 257,080 |
| `augustine_doctrina-christiana-enchiridion-lat_bruder1838` | needs-redo | unexplained steps: `doctrina1` (9), `doctrina2` (3), others | 78,519 |
| `augustine_epistulae-1-123-lat_goldbacher-csel34` | drafted, suspect | unexplained steps: `ep` (1) and page-split series | 315,334 |
| `augustine_epistulae-124-184a-lat_goldbacher-csel44` | drafted, suspect | unexplained steps in page-split series (`pg2111` 5, others) | 280,128 |
| `augustine_epistulae-critical_goldbacher-csel57-pars4` | drafted, suspect | unexplained steps: `ep` (12), `pg2382` (3), others | 229,912 |
| `augustine_epistulae-maurist-order-lat_migne-pl33` | drafted, suspect | unexplained steps: `letter` (13), `chapter` (20), others | 587,627 |
| `augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869` | needs-redo | unexplained steps: `p0`, `p3`, others | 105,595 |
| `augustine_opera-sect-v-pars-iii-lat_zycha1900-csel41` | drafted, suspect | unexplained steps in section series (`s0`, `s1`, others) | 252,695 |
| `augustine_retractationes-lat_knoll-csel36` | drafted, suspect | unexplained steps: `caput` (8) | 87,757 |
| `augustine_sermones-1-340-lat_migne-pl38` | needs-redo | `allow_oversize` on `sermo004` fails: 41 sub-heading lines (CAPUT heads) | 745,026 |
| `augustine_sermones-341-396-et-appendix-lat_migne-pl39` | needs-redo | `allow_oversize` on `sermo351` fails: 11 sub-heading lines (CAPUT heads) | 547,712 |
| `augustine_sermones-ad-populum-lat_migne-gaume1841-t5` | drafted, suspect | unexplained steps: `sermon` (27) | 1,280,238 |
| `augustine_sermones-inediti-lat_caillau1842` | drafted, suspect | unexplained steps: `sermon` (40) | 497,625 |
| `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910` | drafted, suspect | unexplained steps: `s1` (1), `s2` (2), `s4` (1), `s5` (1), others | 570,866 |
| `benson_cyprian-his-life-his-times-his-work_1897` | needs-redo | `allow_oversize` on `chapter4/section3` fails: 14 sub-heading lines | 267,697 |
| `dales_theologie-de-saint-cyprien-fra_1922` | sampled-ok | `allow_oversize` scan on 6 divisions; triaged (B), see below | 156,659 |
| `duchesne_histoire-ancienne-de-leglise-tome3-fra_2e-ed1910` | sampled-ok | `allow_oversize` scan on `chapter14`; triaged (B), see below | 182,417 |
| `harnack_mission-und-ausbreitung-des-christentums-band2-deu_2e-aufl1906` | needs-redo | unexplained step: `zeugnis` (1, at 533) | 138,459 |
| `hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907` | needs-redo | `allow_oversize` on `section6` fails; triaged (A), see below | 12,369 |
| `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929` | needs-redo | unexplained step: `pionius-chapter` (1, at 3835) | 62,214 |
| `koch_cathedra-petri-deu_1930` | drafted | `allow_oversize` on `II/1` fails: 12 sub-heading lines; not sampled | 81,403 |
| `koch_cyprianische-untersuchungen-deu_1926` | drafted | `allow_oversize` on `ch1` fails: 17 sub-heading lines (`Cap. 1.`, `Cap. 2.` ...); not sampled | 153,719 |
| `monceaux_histoire-litteraire-afrique-chretienne-tome3_1905` | sampled-ok | `allow_oversize` scan on 3 divisions; triaged (B), see below | 246,968 |
| `optatus_against-the-donatists` | needs-redo | unexplained step: `chapter` (1, at 1307) | 123,097 |
| `possidius_vita-augustini_weiskotten1919` | needs-redo | unexplained steps: `letter-eng`, `letter-lat` | 54,959 |
| `ribbeck_donatus-und-augustinus-erste-haelfte-deu_1857` | drafted | `allow_oversize` on `T1/c1/a3` fails: 11 sub-heading lines (`1. Die Montanisten ...`); not sampled | 227,009 |

The full list of lines for each failure is in the output of `curate check <stem>`.

## Triage of the four `sampled-ok` files that fail the oversize scan

Each line the checker lists was read in the vendored file. Ruling (A): the sampler missed real printed sub-divisions. Ruling (B): the lines are not divisions.

| File | Ruling | Evidence |
|---|---|---|
| `hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907` | (A), status now `needs-redo` | 57 of the 58 lines are footnotes ("397: 1. S. Cyprien, Kpist., i.xviii, P. L., t. m, col. 1057 sq."). Line 746 is not. It is body text: "1.  On  se  demande  avant  tout  lequel  des  deux  avait  l'antiquité / chrétienne  de  son  côté.", after the sentence "Il nous reste ... à exposer avec plus de précision les opinions et les assertions de Cyprien et d'Etienne." (743-745). It is the printed sub-number 1 of § 6, followed by sub 2 at 1059 and sub 3 at 1251. The `allow_oversize` sentence ("sub-number 1 is not printed in the scan") and the sampler's note ("No line in the slice prints a "1." sub-number") are both untrue. Defect for the redo: add `section6/sub1` at line 746 and remove the `allow_oversize` sentence. The split gives 382-745 (3,155 words) and 746-1058 (2,513 words), both under 5,000. |
| `dales_theologie-de-saint-cyprien-fra_1922` | (B) | 270 lines in 6 divisions (`livre1/chapter3`, `livre1/chapter4`, `livre2/chapter2/section2`, `livre2/chapter3/section2`, `livre2/chapter3/section4`, `livre3/chapter3/section1`). They are footnotes in the form "N. citation" (1869 "4. Ep., uxxiv, 7, p. 804, 17-18."; 9627 "1. H. Kocu, Cyprian und der rémische Primat, p. 74"), running heads with a page number (2047 "24. THEOLOGIE DE SAINT CYPRIEN."; 10755 "174. THEOLOGIE DE SAINT CYPRIEN."), and Cyprian's own capitula quoted as a list inside chapter IV (4002 "AD QUIRINUM TESTIMONIORUM LIBER III", then 4005 "1. De bono operis et misericordiae", 4015 "2. In opere et eleemosynis ...", 4737 "3. Quae comminatio Dei sit adversus eos qui idolis sacrificant."). The Table des matières (25945-26087) prints no level below these chapters and sections (Livre I chapter IV: "L'Ecriture. — Inspiration. — Canon. — Bible latine. — Testimonia ad Quirinum. — ...", unnumbered topics). |
| `duchesne_histoire-ancienne-de-leglise-tome3-fra_2e-ed1910` | (B) | 13 lines in `chapter14` (21450-23863), each a lone "I" three lines above a running head: 21737 "I", then 21740 "l'occident  au  v""  siècle  589"; 21816 "I", then "I/OCCIDENT   AU    y"  SIÈCLE  591"; 22999 "I", then "l'occii)î;xt  au  v''  siècle  623". They are OCR debris at the page break, not headings. The Table des matières (25198 onward) lists chapters only, each with an unnumbered summary ("Chapitre III. — Chrysostome et Théophile 69"). |
| `monceaux_histoire-litteraire-afrique-chretienne-tome3_1905` | (B) | 98 lines in `l5/c3/s1` (11684), `l5/c3/s2` (16254) and `l7/c1/s2` (34841). Line 11692 "I" is the division's own section numeral (11684 "CHAPITRE III", then "I", then the summary "Inscriptions relatives à la persécution. — ..."). The rest are OCR debris from the inscription pages: lone letters (12605 "X", 17631 "CM", 18042 "CD", 15002 "(D"), fragments ("12093: 5. s", "13244: IV)", "13376: § 5", each among lines such as "U T3", "CO CO", "+* d"), a footnote ("15951: I) C I. L., VIII, 20302."), and a stray "III." inside a quoted footnote at 35070 ("lais compositio non mctrica ralionc, sed / III. / numcrosa scansione"). Section II of chapter III begins at 16254 with its numeral ("Il") and summary, as the rule finds. |

For the three (B) files there is no per-file allowance to add. The checker has no per-file threshold or exemption field; its only levers are the global `ALLOW_OVERSIZE_MAX_SUBHEADINGS = 10` and the furniture set (`ignore`). Their status stays `sampled-ok` and they keep failing the check until one of these is decided:

- Proposed smallest field (not implemented): `not_subheadings` on the division entry or rule that carries `allow_oversize`: a list of `{lines, kind, quote}`, where `lines` is a line or a `[first, last]` range, `kind` is one of `footnote`, `running-head`, `ocr-debris`, `quoted-list`, and `quote` is text on the first listed line. The scan skips only those lines; they stay in passage text. Every listed line must be one the scan flags, or the check fails. It takes line numbers, not patterns, because a footnote-shaped pattern (`^\d+\. `) would also have hidden Hefele-Leclercq's printed "1." at line 746.
- Existing alternative, a curation edit rather than an allowance: declare the Duchesne "I" lines, the Dales running heads and the Monceaux debris as `ignore` furniture, which is true of them. This does not fit the Dales footnotes and quoted capitula, which are printed text and belong in passages.

## `needs-redo` (18)

Defects are in `Curation_Sample_Review_Wave1a_A.md`, `_B.md` and `_C.md`, and in the triage above.

| File | Group | Check | Defect | Words |
|---|---|---|---|---|
| `augustine_doctrina-christiana-enchiridion-lat_bruder1838` | A | fail | about 54 printed chapter heads missed | 78,519 |
| `augustine_sermones-1-340-lat_migne-pl38` | A | fail | false oversize justification; sermons print CAPUT heads | 745,026 |
| `augustine_sermones-341-396-et-appendix-lat_migne-pl39` | A | fail | one numeral fixed from sequence alone; false oversize justification | 547,712 |
| `augustine_sermones-post-maurinos-reperti-lat_morin1930` | A | pass | Casinenses sermons not divided | 366,874 |
| `optatus_against-the-donatists` | B | fail | printed editor's heading hidden as furniture (2294); unexplained gap | 123,097 |
| `codex-theodosianus_latinlibrary` | B | pass | paragraph text addressed as `pr`; duplicate law 16.7.3 | 240,192 |
| `acta-martyrum-selecta_gebhardt1902` | B | fail | missed Pionius chapter heads; one Greek chapter mis-addressed (dropped I at 4128) | 65,693 |
| `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902` | B | pass | Pionius split at a running head (5619), not at its chapters | 64,574 |
| `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929` | B | fail | missed Pionius chapters II to IV (3624, 3668, 3688); wrong scheme statement | 62,214 |
| `perpetua-scillitan-martyrs-lat-grc_robinson1891` | B | pass | three address labels the edition does not print | 52,358 |
| `possidius_vita-augustini_weiskotten1919` | B | fail | missed section numbers of the letter in chapter 30 (4229, 4563, 4611) | 54,959 |
| `augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869` | C | fail | four printed headings missed by OCR damage (6510, 8028, 10933, 12790); other gaps to confirm; running heads not declared | 105,595 |
| `benson_cyprian-his-life-his-times-his-work_1897` | C | fail | false oversize justification on chapter X sections 1 and 2; chapter VIII section 4 not split at its printed parts | 267,697 |
| `harnack_mission-und-ausbreitung-des-christentums-band2-deu_2e-aufl1906` | C | fail | testimonies 27 and 28 folded into 26 (500, 529) | 138,459 |
| `mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912` | C | pass | three divisions are a running head or a map reference (2863, 7868, 8767) | 192,982 |
| `mesnage_afrique-chretienne-eveches-ruines-fra_1912` | C | pass | three divisions are OCR debris or a map reference (2436, 2440, 5671) | 191,310 |
| `monceaux_histoire-litteraire-afrique-chretienne-tome2_1902` | C | pass | Livre III ch. VI section V (10244) missing; false oversize justification on s4 | 166,307 |
| `hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907` | C | fail | printed sub-number 1 of § 6 at 746 missed; false oversize justification | 12,369 |

## `needs-redo-suspect` (10)

Wave-1b files, not sampled, that fail the checker on unexplained numbering steps. Their yaml status is unchanged `drafted` until a redo or an `expected_gaps` ruling. Each listed step is either a missed heading (redo) or a step the edition really prints (an `expected_gaps` entry with its line and quote).

| File | Unexplained steps | Words |
|---|---|---|
| `augustine_de-fide-et-symbolo-de-opere-monachorum-et-al-lat_zycha-csel41` | section series `s1`, `s5` and others | 257,080 |
| `augustine_opera-sect-v-pars-iii-lat_zycha1900-csel41` | section series `s0`, `s1` and others | 252,695 |
| `augustine_epistulae-1-123-lat_goldbacher-csel34` | `ep` (1) and page-split series | 315,334 |
| `augustine_epistulae-124-184a-lat_goldbacher-csel44` | page-split series (`pg2111` 5, others) | 280,128 |
| `augustine_epistulae-critical_goldbacher-csel57-pars4` | `ep` (12), `pg2382` (3) and others | 229,912 |
| `augustine_epistulae-maurist-order-lat_migne-pl33` | `letter` (13), `chapter` (20) and others | 587,627 |
| `augustine_retractationes-lat_knoll-csel36` | `caput` (8) | 87,757 |
| `augustine_sermones-ad-populum-lat_migne-gaume1841-t5` | `sermon` (27) | 1,280,238 |
| `augustine_sermones-inediti-lat_caillau1842` | `sermon` (40) | 497,625 |
| `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910` | `s1` (1), `s2` (2), `s4` (1), `s5` (1) and others | 570,866 |

Three more `drafted` files fail the check on the oversize scan and are not sampled: `koch_cathedra-petri-deu_1930`, `koch_cyprianische-untersuchungen-deu_1926`, `ribbeck_donatus-und-augustinus-erste-haelfte-deu_1857`. They are not triaged here.

## Not curated (12 hard files, plus the two Cyprian CSEL volumes)

| File | Words |
|---|---|
| `lauchert_kanones-altkirchlichen-concilien-lat-grc_1896` | 81,673 |
| `prosper_chronica-minora-1-lat_mommsen1892` | 345,654 |
| `turner_ecclesiae-occidentalis-monumenta-iuris-antiquissima-tom1-fasc1-lat_1899` | 204,540 |
| `mansi_sacrorum-conciliorum-collectio-tomus-3-347-409-lat_welter-facsimile1901` | 594,481 |
| `pl11-zeno-optatus-collatio-carthaginiensis_migne` | 702,434 |
| `codex-canonum-ecclesiae-africanae_bruns-pars1-1839` | 174,002 |
| `cyprian_ausgewaehlte-schriften-band1-deu_uhl-bkv1869` | 101,149 |
| `augustine_erorterungen-zum-johannis-evangelium-teil2-deu_hayd-bkv1878` | 195,187 |
| `cyprian_oeuvres-completes-tome1-traites-fra_guillon1837` | 155,448 |
| `cyprian_oeuvres-completes-tome2-lettres-fra_guillon1837` | 125,921 |
| `gsell_inscriptions-latines-de-lalgerie-tome1-proconsulaire-fra-lat_1922` | 388,979 |
| `augustine_augustinus-postille-auswahl-reden-kirchenjahr-deu_1861` | 206,457 |
| `cyprian_opera-omnia-critical_hartel-csel3-pars1-2` | 301,236 |
| `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3` | 221,295 |

Reasons are in the wave reports: OCR-damaged or doubled numerals that cannot be read without guessing, or missing title leaves.

## Not yet sampled (24 `drafted` files)

- Group C, 9 files (802,116 words): `koch_cathedra-petri-deu_1930` (fails check), `koch_cyprianische-untersuchungen-deu_1926` (fails check), `poschmann_abendlaendische-kirchenbusse-deu_1928`, `ribbeck_donatus-und-augustinus-erste-haelfte-deu_1857` (fails check), `toulotte_geographie-afrique-chretienne-numidie-fra_1894`, `vonsoden_cyprianische-briefsammlung-deu_1904`, `vonsoden_ketzertaufstreit-rom-karthago-deu_1909`, `vonsoden_prosopographie-afrikanischer-episkopat-deu_1909`, `vonsoden_streit-rom-karthago-ketzertaufe-deu_1909`.
- Wave 1b, 13 files: the 10 on the suspect list, and three that pass the check, `augustine_civitate-dei-1-13-lat_hoffmann-csel40-1`, `augustine_civitate-dei-14-22-lat_hoffmann-csel40-2`, `augustine_confessiones-lat_knoll-csel33` (633,662 words).
- Pilots, 2 files that pass the check: `augustine_de-catechizandis-rudibus-lat_krueger1893`, `koch_cyprian-und-der-roemische-primat-deu_1910` (91,293 words).

## Remaining redo workload

| Group | Files | Words |
|---|---|---|
| `needs-redo` | 18 | 3,475,937 |
| `needs-redo-suspect` | 10 | 4,359,262 |
| Not curated (hard) | 14 | 3,798,456 |
| Total to curate or redo | 42 | 11,633,655 |
| Not yet sampled, outside the suspect list | 14 | 1,527,071 |

Word counts are whole files. A redo touches only the defective divisions, but each file must be read against its print to close the defects and confirm nothing else is missed.

### Suggested worker batches, by edition family

| Batch | Files | Words | Kind |
|---|---|---|---|
| 1. Migne Augustine sermons | PL38, PL39, Morin | 1,659,612 | needs-redo: CAPUT levels, Casinenses |
| 2. Gaume and Caillau sermons, Migne PL33 letters | Gaume t5, Caillau, PL33 | 2,365,490 | suspect: series steps to explain or fix |
| 3. CSEL Augustine | Goldbacher csel34, csel44, csel57 pars 4; Zycha CSEL 41 (both); Knoll Retractationes; Petschenig | 1,993,772 | suspect: series steps to explain or fix |
| 4. Augustine hand editions and German translations | Bruder, Raulx, Hayd, Postille | 585,758 | Bruder and Raulx needs-redo; Hayd and Postille hard OCR |
| 5. Cyprian editions | Hartel CSEL 3 pars 1-2 and pars 3, Guillon (2), Uhl | 905,049 | hard OCR, not curated |
| 6. Councils and law | Lauchert, Turner, Mansi vol. 3, Bruns African Codex, Codex Theodosianus | 1,294,888 | hard OCR (Codex Theodosianus is a needs-redo) |
| 7. Donatist sources, chronicle, inscriptions | Zeno-Optatus PL11, Optatus (English), Prosper, Gsell | 1,560,164 | hard OCR (Optatus is a needs-redo) |
| 8. Martyr acts and modern monographs | Gebhardt (2), Knopf, Robinson, Possidius, Benson, Harnack Mission, Monceaux tome 2, Mesnage (2), Hefele-Leclercq | 1,268,922 | needs-redo |

The hard OCR batches are 5, 6 and 7, and the two hard files in batch 4. Batch 2 is the largest by words, but most of its work is reading the reported steps, not the whole text. Sampling the 14 unsampled files outside the suspect list is a separate review pass, not a redo.

## Tooling

Merged: long Roman numerals (to 3,888) and German, French, Latin and Italian ordinals (PR 1310). PR 1329: unexplained numbering steps fail the check unless listed in `expected_gaps`; every step is printed; `allow_oversize` divisions with more than 10 numbered sub-heading lines fail; missed heading-like lines are reported. Open: `fixes` not passed through `ocr_map`; adjacent apparatus ranges; explicit divisions setting a parent for later rules; page-head splitting; a rule context condition; a per-rule language guard; a way to mark scan lines as not sub-headings (proposal above).

## Post-apparatus divisions now carry the apparatus address (PR 1321)

Five files have a division that starts right after an apparatus range or is itself the first line of the next range: `augustine_sermones-inediti-lat_caillau1842`, `koch_cathedra-petri-deu_1930`, both `mesnage_afrique-chretienne-eveches-ruines` files and `possidius_vita-augustini_weiskotten1919`.

- Before: the division was labelled with a gap address of the form `text/line<N>` and its words were not counted as covered.
- Now: it carries the apparatus address its curation declares, and its words count as covered, so coverage reads 100% in each file.
- Division counts and the body/apparatus split are unchanged.
- Accepted by the coordination thread: no record or index points at those addresses yet.

## First thing on resume

1. Decide the oversize-scan mechanism for the three (B) files: the `not_subheadings` field, `ignore` furniture where true, or neither.
2. Run the redo batches above; re-sample each redo with a different Opus reviewer.
3. Set the 10 suspect files to `needs-redo`, or list their steps in `expected_gaps`, as each is examined.
4. Sample the 14 unsampled files outside the suspect list; treat any numeral read from sequence alone as a defect.

## `not_subheadings` rulings for the three (B) files (2026-10-29)

An Opus reader opened every flagged line of the three files in the vendored text, with its neighbouring lines, and ruled on it. The proposed kinds came from `Curation_NotSubheadings_Candidates.md`. No flagged line in any of the three files is a printed sub-heading or a division numeral, so all three keep `status: sampled-ok` and gain a `not_subheadings` field. `curate check` passes on each file, which now reaches class `curated`.

| File | Flagged | footnote | running-head | ocr-debris | quoted-list | Left unlisted | Unconfirmed |
|---|---|---|---|---|---|---|---|
| `dales_theologie-de-saint-cyprien-fra_1922` | 345 | 312 | 3 | 0 | 28 | 2 | 0 |
| `duchesne_histoire-ancienne-de-leglise-tome3-fra_2e-ed1910` | 13 | 0 | 0 | 13 | 0 | 0 | 0 |
| `monceaux_histoire-litteraire-afrique-chretienne-tome3_1905` | 97 | 1 | 0 | 96 | 0 | 0 | 0 |

- **Dales.** Most proposed `quoted-list` groups were footnotes: numbered references at the foot of the page, such as `1. Ep., ...`, plus one footnote that runs on with `§ 165` at line 20618. These are re-kinded `footnote`. Three lines are running heads with the page number read into a numeral: 2047, 10755 and 12110. The 28 `quoted-list` lines are the numbered capitula of Cyprian's *Ad Quirinum (Testimonia)* II and III and of the *Ad Fortunatum*, which Dales reproduces inside livre1/chapter4 (lines 3651 to 4802). They are Cyprian's titles quoted by Dales, not divisions of Dales's book. Lines 7935 and 11434 are body prose that opens with `M.` (Monsieur), in `M. H. Koch` and `M. Ernst`. None of the four kinds fits them, so they are left unlisted. Each sits well under the limit of 10 in its division.
- **Duchesne.** Every flagged line is a lone `I` at the foot of the page, just before the next running head. This is scan debris.
- **Monceaux.** 95 lines are the scattered cells of rotated tables that the OCR could not read: the inscription lists in l5/c3/s1 and l5/c3/s2, and the metrical-inscription tables in l7/c1/s2. Line 35070 (`III.`) is the volume's signature mark, caught inside footnote 3; it is kinded `ocr-debris`. Line 15951 (`I) C I. L., VIII, 20302.`) is footnote 1, so it is re-kinded `footnote` rather than the proposed `quoted-list`.


## Redo batches, 2026-10-30

Reports: `Curation_Redo_B8_Report.md`, `Curation_Redo_B4B7_Report.md`, `Curation_Pilot_Report.md`. Reviews: `Curation_Sample_Review_B8.md`, `Curation_Sample_Review_Round3_BensonMesnageKnoll.md`, `Curation_Sample_Review_Mesnage_IndexPass.md`, `Curation_Sample_Review_B4B7.md`, `Curation_Tooling_Review_HeadUnprinted.md`.

| File | Outcome |
|---|---|
| `possidius_vita-augustini_weiskotten1919` | `sampled-ok` (pilot) |
| `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929` | `sampled-ok` |
| `acta-martyrum-selecta_gebhardt1902` | `sampled-ok` after a second round |
| `augustine_doctrina-christiana-enchiridion-lat_bruder1838` | `sampled-ok` |
| `hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907` | `sampled-ok` |
| `perpetua-scillitan-martyrs-lat-grc_robinson1891` | `sampled-ok` |
| `harnack_mission-und-ausbreitung-des-christentums-band2-deu_2e-aufl1906` | `sampled-ok` |
| `monceaux_histoire-litteraire-afrique-chretienne-tome2_1902` | `sampled-ok` |
| `benson_cyprian-his-life-his-times-his-work_1897` | `sampled-ok` after the third round |
| `augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869` | `sampled-ok` |
| `augustine_retractationes-lat_knoll-csel36` | `sampled-ok` after the third round |
| `optatus_against-the-donatists` | `sampled-ok`: the one defect was the untrue reason; fixed with `head_unprinted` (Decision-Log 26), form checked against the file by the tooling reviewer |
| both `mesnage_afrique-chretienne-eveches-ruines` scans | `sampled-ok` after a fourth look (Decision-Log 27) |

Tooling merged: PR #1343, #1346, #1359 (single look-alike test, reasons for `expected_gaps`, `y` stroke), #1365 (`head_unprinted`). The merger of #1346 is not identified.

## Migne, Gaume and Caillau redo group, 2026-10-30

Each file was redone by a Sonnet worker and read by an independent Opus reader who opened the vendored lines. No reason form was added and no tooling changed.

| File | Outcome |
|---|---|
| `augustine_sermones-341-396-et-appendix-lat_migne-pl39` | `sampled-ok` after one read |
| `augustine_sermones-post-maurinos-reperti-lat_morin1930` | `sampled-ok` after the third round (the cap) |
| `augustine_sermones-1-340-lat_migne-pl38` | `sampled-ok` after two rounds |
| `augustine_sermones-ad-populum-lat_migne-gaume1841-t5` | `sampled-ok` after two rounds |
| `augustine_epistulae-maurist-order-lat_migne-pl33` | `sampled-ok` after two rounds |
| `augustine_sermones-inediti-lat_caillau1842` | `sampled-ok` after two rounds |

### Rulings applied (coordination level, AI-reviewed)

- A numeral missing from a printed head line may be supplied from the edition's own running head or index for that very head, quoted as evidence. It is never read from the sequence alone. Caillau line 13761 (sermon LVIII) rests on the index alone.
- Where a page is column-interleaved or a head is lost and no reason form fits truthfully, the stretch is read by a rule or explicit divisions without a numeral series. No reason is stated that the page does not show.
- Caillau line 32624 prints `SEHMO XVII.` where its title and the index place it as the sixth Epiphany sermon. It is addressed by its printed head text and line, outside the numbered series.

### Open gaps

- PL38, sermon 294: `CAPUT V.` (line 93939) and `CAPUT VI.` (line 93997) are printed in the middle of a line in a column-merged scan. They have no division; their text sits inside the neighbouring capita.
- PL38, sermon 88: the edition prints one combined head, `CAPITA VII et VIII` (line 37916). It is one division, addressed `caput07-08`.
- PL33, letter 260 (Audax to Augustine): the head is lost from the scan; its text sits inside the `ep259` division (lines 78646 to 78809). The step is explained with `leaf_missing` between lines 78647 and 78810. The Index (lines 87333 and 89231) lists the letter.
- PL33, three letters and the appendix letter 17: stretches read without a numeral series because of column interleave or a lost head or page (letter 108, 148, 169; appendix letter 17).
- Gaume t5, sermon 361: no `CAPUT III` head in the scan (lines 114340 to 115250). The stretch is read without a numeral series.
- Gaume t5: eight chapter stretches in sermons 4, 37, 51, 52, 88, 169 and 277 and the stretch at lines 114349 to 115246 are read without a numeral series.
- Caillau: the edition's numbering skips sermons LXVI and LXXV. The printed index agrees and no text is missing. They are listed with `leaf_missing` (the nearest form the tooling allows).
- Morin: the Part VII introduction and the Appendix are apparatus, as editor's prose.
- Where a head starts mid-line in a two-column page, a few lines of the previous sermon fall into the next division (Caillau, Gaume). A line-based division cannot split a line.

### Open tooling notes

No tooling is built from these now. Coordination batches them into one small tooling PR, with Opus review before merge, if a later file needs it or after the CSEL group.

- The checker does not fail a body division left as a `text/line` gap under a context heading that an apparatus range clips. It was found by reading the resolved divisions in Gaume t5 and PL33.
- `counterpart` is accepted for a bare head with no numeral token even when the file is not a parallel text. No curation uses it for that now.
- There is no reason form for a numeral the edition itself skips with no text missing (Caillau LXVI and LXXV). `leaf_missing` is used and misdescribes it. A form such as `edition_skips`, checked against the edition's own index, is the likeliest to be worth building.

## CSEL group redo, 2026-10-30 and 2026-10-31

Each file was redone by a Sonnet worker and read by independent Opus readers who opened the vendored lines. No reason form was added and no tooling changed.

| File | Outcome |
|---|---|
| `augustine_epistulae-critical_goldbacher-csel57-pars4` | `sampled-ok` after two rounds |
| `augustine_epistulae-1-123-lat_goldbacher-csel34` | `sampled-ok` after two rounds |
| `augustine_epistulae-124-184a-lat_goldbacher-csel44` | `sampled-ok` after two rounds |
| `augustine_de-fide-et-symbolo-de-opere-monachorum-et-al-lat_zycha-csel41` | `sampled-ok` after two rounds |
| `augustine_opera-sect-v-pars-iii-lat_zycha1900-csel41` | `sampled-ok` after two rounds |
| `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910` | `sampled-ok` after the third round (the cap) |

### Open gaps

- Goldbacher CSEL 34: pages 55 (head printed `oo`, unreadable), 384, 468, 554, 622 and 690 (head line absent, text present) are read outside the numbered page series. Pages 62 and 63 are missing from the scan; letter XXIII is read from the running heads.
- Goldbacher CSEL 44: pages 55 (head printed without a number) and 70 (head absent) are read outside the numbered page series. Three damaged odd-page heads are read as 73, 323 and 357 from the two printed leading digits, odd-page position and the neighbouring heads, with no cross-reference to confirm them.
- Goldbacher CSEL 57: page and section sub-series of twelve oversize letters are hand-listed and not checked as a series.
- Zycha CSEL 41 (both scans): Book II of De adulterinis prints chapters IIII and V with no section numeral and no section 4 head; they are addressed `caput4` and `caput5`, outside the section series.
- Petschenig: sections 81 to 103 of De baptismo VII are read outside the numbered series, because the head at line 19797 prints only a Roman chapter numeral and the look-alike test refuses `edition_unnumbered`. Stretches the scan prints twice are read by line address in one copy and numbered in the other. The Epistula ad catholicos prints pages 268 and 269 out of order.
- Petschenig line 39361 (`82.` read as 32) is the weakest accepted numeral reading.

### Open tooling notes (added to the three above)

- `edition_unnumbered` is refused by the look-alike test where a head prints a Roman chapter numeral and no Arabic section numeral (Petschenig line 19797).
- Splitting a numbered series, or dropping `number`, turns off the look-alike scan over that stretch. In the CSEL group this hid wrong page and section addresses in two files until a reader opened the lines. A rule that keeps the scan on across an absent head would help.

## Group C and the large Augustine files, 2026-10-31

Each file was read by independent Opus readers who opened the vendored lines. No reason form was added and no tooling changed.

| File | Outcome |
|---|---|
| `augustine_de-catechizandis-rudibus-lat_krueger1893` | `sampled-ok` after one read |
| `augustine_confessiones-lat_knoll-csel33` | `sampled-ok` after one read |
| `augustine_civitate-dei-1-13-lat_hoffmann-csel40-1` | `sampled-ok` after one read |
| `augustine_civitate-dei-14-22-lat_hoffmann-csel40-2` | `sampled-ok` after one read |
| `poschmann_abendlaendische-kirchenbusse-deu_1928` | `sampled-ok` after one read |
| `koch_cyprian-und-der-roemische-primat-deu_1910` | `sampled-ok` after two rounds (the Anhang was folded into chapter XXI) |
| `koch_cathedra-petri-deu_1930` | `sampled-ok` after two rounds |
| `vonsoden_cyprianische-briefsammlung-deu_1904` | `sampled-ok` after two rounds |
| `ribbeck_donatus-und-augustinus-erste-haelfte-deu_1857` | `sampled-ok` after two rounds |
| `toulotte_geographie-afrique-chretienne-numidie-fra_1894` | `sampled-ok` after three rounds (the cap) |
| `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902` | `sampled-ok` on its second review (the first, in the B8 batch, ruled needs-redo) |
| `koch_cyprianische-untersuchungen-deu_1926` | `sampled-ok` after three rounds and Mark's one fourth look (below) |

### Mark's ruling, 2026-10-31

`koch_cyprianische-untersuchungen-deu_1926` got one fourth look: a fresh independent Opus reader on the one fixed sentence only (the lettered-points clause of the scheme line, now matching Anhang item 4's a) and b)). It is a one-time ruling for this file and does not reopen the cap elsewhere. The fourth reader found the sentence true to both the division list and the page. If it had failed, the file would have stayed `drafted` with no fifth look.

### Open gaps

- Ribbeck, first half: the file holds both halves although its library header says first half only. The scan repeats pages 284 to 285 in II/1 (lines 12265 to 12390), pages 352 to 353 four times in the Parmenian stretch (15212 to 15578), pages 434 to 436 in II/5/a2 (19340 to 19722) and pages 598 to 599 four times in the third-day account (26854 to 27202). Addresses stay correct. Undivided printed sub-heads remain in divisions under 5,000 words.
- Toulotte: nine sees are missing from the scan (XX to XXII, XCIV to XCV, CLVI to CLIX), with the pages 68 to 69, 196 to 197 and 300 to 309 absent. Four runs of repeated pages are read outside the numbered series. The heads printed CLXIII and CLXIV at lines 12764 (Suava) and 12789 (Sulli) are read at 143 and 144 from the edition's own list, for the sequence check only.
- Koch, Cyprianische Untersuchungen: Cap. 6 is printed twice (lines 1152 and 1243); the second is addressed by line outside the numbered series.
- Gebhardt 1902 (second scan): in Perpetua the Latin and Greek alternate on each page, so continued text lands in the neighbouring language's chapter division. The format cannot give one chapter two ranges. This is a question for the Howto owner (a sub-address split by language or page), not a defect of either Gebhardt file.
- Pionius II and XIII in that scan rest on the first scan as a second printed instance of the same head, and Piece XVIII on its printed `XVIH.` alone.

### Open tooling notes (added)

- `clean` does not mean citable addresses. See the caveat in `Stage2_Segmentation_Report.md`, section 2.
- The format cannot give one chapter two ranges, so interleaved parallel texts cannot be addressed by language within a chapter.
- A head that prints a clean numeral contradicting its position (Toulotte 12764 and 12789, Caillau 32624) cannot be taken out of the numbered series without a reason form, because the look-alike test flags it. It is handled by reading the position from the edition's own list for the sequence check only, or by line address.
- Partial markup files (anf05, anf04, npnf101, npnf106, npnf108, and also npnf104 and npnf107): file-level fallback is enough for now (coordination ruling, 2026-10-31). Their share of words in divisions over 5,000 words is 28.7, 15.2, 31.4, 24.0, 49.7, 32.3 and 50.9 per cent. The lpc records cite by work, section number and quote, so the coarse divisions break no cited locus.

## Audit of the clean plain-text files, 2026-10-31

Why: the segmenter's class `clean` means enough markers, sequential numbering and no oversize divisions. It does not mean the addresses are numbers the edition prints for its divisions (caveat in `Stage2_Segmentation_Report.md`, section 2).

Method. A script measured every plain-text file with the segmenter's own heuristics and no curation: the class, the share of divisions addressed by a line number, the share addressed by a bare four-digit number, the share of tiny divisions, and the share whose address numeral appears in the first 200 characters of the division. It found 41 plain-text files of class clean (the Stage 2 report counted 38; the three extra are unexplained and may come from tooling changes since 2026-10-29). Every clean file on the lpc shelf (14) was then read by an independent Opus reader who opened the text.

Result on the lpc shelf: 14 of 14 need curation. None is usable as it stands. 13 need whole-file curation; Bardenhewer needs a light, scoped one.

| File | Measured address match | What the addresses really are | Verdict |
|---|---|---|---|
| `augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2` | 0.958 (94% four-digit) | Migne column numbers; 0 of 134 tractate heads addressable | needs curation (in progress) |
| `augustine_enarrationes-in-psalmos-lat_migne-pl36-37` | 0.666 | `lineN` and `lineN/pM`; 22 of 151 psalm heads open a division | needs curation (curation drafted, under read) |
| `augustine_opera-minora-catechetica-lat_migne-pl40` | 0.216 | chapter and section numbers with no work name; 88 of 122 Enchiridion chapters found | needs curation, whole file |
| `audollent_carthage-romaine-146-av-jc-698-ap-jc-fra_1901` | 0.0 (85% line) | line numbers that hide the printed Livre/Chapitre structure | needs curation, whole file |
| `audollent_carthage-romaine-fra_1901` | 0.877 | page numbers, gathering numbers, misreads; 0 of 41 Livre/Chapitre heads open a division | needs curation, whole file |
| `duchesne_histoire-ancienne-de-leglise-tome2-fra_3e-ed1907` | 0.0 (91% line) | 98% of divisions are page or running-head debris | needs curation, whole file |
| `augustine_oeuvres-completes-tome15-donatistes-slice-fra_raulx1870` | 0.38 | paragraph numbers under running-head parents, no work or book | needs curation, whole file |
| `mansi_sacrorum-conciliorum-collectio-tomus-2-305-346-lat_welter-facsimile1901` | 0.857 | Mansi column numbers; 0 of 27 council heads open a division | needs curation, whole file |
| `mansi_sacrorum-conciliorum-collectio-tomus-3-347-409-lat_welter-facsimile1901` | 0.096 (76% line) | line numbers; 73 of 87 council heads open a division | needs curation, whole file |
| `mansi_sacrorum-conciliorum-collectio-tomus-4-410-431-lat_welter-facsimile1901` | 0.908 | Mansi column numbers; 0 of 34 council heads open a division | needs curation, whole file |
| `augustine_sermones-guelferbytani-lat_morin1917` | 0.83 | page numbers; 9 of 42 tractatus heads open a division | needs curation, whole file |
| `augustine_bekenntnisse-deu_hefele-diederichs1921` | 0.921 | page numbers (n1 to n315); about 22 pages missing from the scan | needs curation, whole file |
| `bardenhewer_geschichte-altkirchlichen-literatur-band4-augustinus-slice-deu_1924` | 0.889 | printed subsection numbers; 24 of 28 addressable; four damaged heads, one false division | needs light curation |
| `hefele-leclercq_histoire-des-conciles-tome2-1-conciles-africains-slice-fra_1908` | 0.978 | page numbers; 22 of 22 section heads present, none addressed by its number | needs curation, whole file |

Reading the table:
- The measured address match cannot clear a file. Of the four lpc files that passed the cheap rule, three (Audollent fra, Bekenntnisse, Hefele-Leclercq) were fooled by page numbers.
- Citing by page works roughly in the page-numbered files; citing by chapter, section, council or canon does not.
- Mansi is cited by column in the literature, so column addresses may stay as a locator, but not as the only address.

Known gaps found by the audit (source defects, not curation defects):
- `augustine_bekenntnisse-deu_hefele-diederichs1921`: about 22 pages are missing between pages 265 and 315 (254 of 278 chapter heads present). The library header says the OCR is clean and all thirteen books are present; it is not.
- `augustine_opera-minora-catechetica-lat_migne-pl40`: the title page and I.1 of De catechizandis rudibus are missing from the scan (jump at line 21143).
- `audollent_carthage-romaine-146-av-jc-698-ap-jc-fra_1901` and `audollent_carthage-romaine-fra_1901` are one book in two scans (the second adds the Additions and Corrections); the corpus map lists them as two works; the corpus map row for 'Les chretiens' points to line 47700, which is the Table entry, not the chapter (line 38751).
- `augustine_sermones-guelferbytani-lat_morin1917` is Morin's first edition of sermons whose 1930 reprint is curated (`augustine_sermones-post-maurinos-reperti-lat_morin1930`); the 1917 file adds the nine appendix tractatus and the praefatio.

Size of the same risk elsewhere (cheap measures only; not read): 27 of the 41 clean plain files are not on the lpc shelf. By the cheap rule 4 pass, 3 are doubtful and 20 raise at least one flag (line, column or low-match addresses, tiny-division clutter). The pass rule failed on the lpc shelf, so these figures are a warning list and not a clearance. By world (files may be on several worlds): alx 2, cappadocian 2, don 4, ijc 8, pahc 3, rzg 8, syr 3, witt 4; desert, gallic and hal have none.

Not audited: the clean XML files (their divisions are the source's own markup, a different risk) and the 30 TEI `.txt` files (a separate class).

## In Ioannis, Migne PL 35 whole volume, 2026-10-31

- File: `augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2`. Status `sampled-ok` after three review rounds (round 1 worker redo and read, round 2 recheck, round 3 wording confirm). 1,334 divisions, coverage 100%, no byte-range mismatches.
- Gospel tractates: 66 divided by printed paragraph numbers, 4 divided by line of the paragraph head, 54 undivided. All 10 Epistle tractates are undivided although they print paragraph numbers.
- Two numerals read from printed glyph damage and quoted as evidence: `iO.` = 10 at line 25420 and `G.` = 6 at line 41311. The same OCR prints 6 as `G.` at 11373, 12017, 13292, 22189, 23186 and 10 as `iO.` at 29988, 31630, 47352.
- Open gap: the 1 John prologue's body sits at lines 46832-46858 inside tractate 1 because of the OCR column order; no contiguous range joins it to its head, so `in-1io/prologus` holds only the head and the last line.
- Open gap: the Benedictine admonition at lines 395-411 counts as body of the tituli division.
