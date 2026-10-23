# Source Readiness Dossier — The Bosnian Church (Krstjani)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.20
**Corpus-map slug:** `the-bosnian-church`
**Time window:** c. 1230s–1463
**Region(s):** Bosnia, with Ragusa (Dubrovnik) and the Hungarian and Roman courts as the outside record
**Dossier author / date:** Library thread, Era VI session (east batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. No bucket file `cic/corpus-map/the-bosnian-church.yaml` existed before this pass. Eight files were vendored for this world, each with a staging file that passes `corpus_map_merge.py --check`. Their registry entries, seed rows and cross-link rows sit in the lead's fragment files until merged.

Census inputs (checked October 2026 in `world-census.json`): status Pre-Survey Candidate. Sourcing line: "Largely external (papal condemnations, Ragusan records); Gost Radin's 1466 testament is the one great inside document - and it reads orthodox, a cross drawn down its margin." The floor note says the old identification of the krstjani as Bogomil dualists has been rejected by most scholars since the 1970s, and that the world is "a Slavonic-rite church standing between Rome and Orthodoxy, with the ambiguity acknowledged rather than resolved". The census has no `sources` list for this world.

## 1. Already assigned

Nothing was assigned to this world before this pass. The eight files below were vendored this pass. Scale is characters in the vendored file, counted. The three Rački files and the Truhelka file are partial extracts (the article only).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Acta Bosnae potissimum ecclesiastica ... 925–1752 (Latin regests, Fermendžin, Zagreb 1892) | fermendzin | context | assigned | 1,230,157 characters | `fermendzin_acta-bosnae-potissimum-ecclesiastica-lat_fermendzin1892.txt` |
| Vetera monumenta Slavorum meridionalium, vol. 1 (Theiner 1863): papal documents 1198–1549; row 1, the 1203 instrument of the Bosnian priors | theiner | tradition | assigned | 3,923,440 characters in the file; the instrument is about 45 lines | `theiner_vetera-monumenta-slavorum-meridionalium-v1-lat_1863.txt` |
| Vetera monumenta, vol. 1: row 2, the papal documents on Bosnia and the south Slavs | theiner | context | assigned | the same file | same |
| Testamenat gosta Radina (Truhelka, Glasnik zemaljskog muzeja XXIII, 1911, pp. 355–376), extract | truhelka | tradition | assigned | 82,564 characters | `truhelka_testamenat-gosta-radina-hrv_glasnik-zemaljskog-muzeja1911.txt` |
| Bogomili i Patareni (Rački), Rad Jugoslavenske akademije knjiga VII, pp. 84–179, extract | racki | context | assigned | 274,868 characters | `racki_bogomili-i-patareni-rad-vii-hrv_jazu1869.txt` |
| Bogomili i Patareni (Rački), Rad knjiga VIII, pp. 121–187, extract | racki | context | assigned | 171,771 characters | `racki_bogomili-i-patareni-rad-viii-hrv_jazu1869.txt` |
| Bogomili i Patareni (Rački), Rad knjiga X, from p. 160, extract | racki | context | assigned | 297,288 characters | `racki_bogomili-i-patareni-rad-x-hrv_jazu1870.txt` |
| Monumenta Serbica (Miklosich, Vienna 1858): charters of Serbia, Bosnia and Ragusa | miklosich | context | provisional | 1,173,308 characters | `miklosich_monumenta-serbica-chu_miklosich1858.txt` |
| Through Bosnia and the Herzegovina on foot (Evans 1877), with the Historical Review of Bosnia | evans | context | assigned | 1,172,124 characters | `evans_through-bosnia-and-the-herzegovina-on-foot_1877.txt` |

What kind of witness each is:

- **The church's own words.** Three places, none of them quotable from the OCR yet. (1) The 1203 instrument in Theiner: "Nos Priores illorum hominum, qui hactenus singulariter Christiani nominis prerogativa vocati sumus in territorio Bosne" promise Rome obedience at Ban Kulin's court. It is the papal register's Latin, made under Roman pressure, and the Latin is readable second witness. (2) Gost Radin's testament of 1466, first printed in 1911 by Truhelka. His Croatian commentary reads well. The testament's own text is in Bosnian Cyrillic and the OCR of it is noise, so the wording must come from the plates or page images. (3) The charters in Miklosich, where the church's djeds and gosts witness royal grants. That OCR is the best of four scans and still poor.
- **The outside record.** Fermendžin's Latin regests and Theiner's registers: papal letters against the heretics, the Franciscan mission, the court of the last rulers. Hostile or protective, never the church speaking.
- **The old scholarship.** Rački (1869–70) and Evans (1877) argue the Bogomil identification that the census says most scholars have rejected. They are kept as the origin of that reading and as guides to the sources, not as evidence for it.

## 2. Cross-link opportunities

Checked by searching the headers and bodies of every `cic/texts/*.txt` for Bosnia, Bosna, krstjan, Patarin, Patarene, Bogomil, Kulin and Radin, then opening the hits. Proposed rows are in the lead's `crosslinks.yaml`.

- **Ecthesis chronica, with the Chronicon Athenarum (Lambros 1902), `ecthesis-chronica_with-chronicon-athenarum-grc_lambros1902.txt`** (bucket: the Orthodoxy-under-the-Ottomans worlds). Tier: same time, different region. Its index points to the conquest of Bosnia and the killing of the king ("Bosniam occupat, cralem occidit", line 6588; "cum Mehemete Bosniam invadit", line 5841), which is the 1463 end of the window. Proposed row: context / provisional; the text pages were not read.
- **Lützow, Life and Times of Master John Hus (1909), `lutzow_life-and-times-of-hus_1909.txt`** (bucket: the Hussites). Tier: same time, different region. Lützow quotes Richental's account of Sigismund's arrival at Constance on Christmas Day 1414, in which Elizabeth, queen of Bosnia, wife of Tvrtko, comes with the king (lines 9832–9847). Noted, no row: a passing link to the Hussite world, not to the church.
- **Sphrantzes (Bekker 1838) and Doukas (Bekker 1834), `sphrantzes-cananus-anagnostes_chronicles-grc-lat_bekker1838.txt`, `doukas_historia-byzantina-grc-lat_bekker1834.txt`.** Tier: same time, different region. Bosnia appears as an Ottoman dependency (Sphrantzes line 5207 and the index at 31161; Doukas once). Noted, no row: no mention of the church.
- **Polanco, Lainez, Ignatius (Jesuit letters), `polanco_chronicon-v4-lat_1896.txt`, `lainez_epistolae-et-acta-v2-lat_1912.txt` and others.** Tier: out-of-window. Bosnia is named dozens of times after the Ottoman conquest; not opened for the krstjani. Noted, no row.
- **Martyrs Mirror (Sohm 1886), `van-braght_martyrs-mirror_sohm1886.txt`.** Tier: out-of-window. Uses "Patarins" and "Patarini" as a general term for medieval dissenters (lines 38519, 41447). Noted, no row: no mention of Bosnia in the lines opened.
- **The Cathars bucket and the Serbian and Bulgarian monasticism world.** The Cathars (IV.12) have a bucket with one work, and it does not mention Bosnia. The Serbian and Bulgarian monasticism world (IV.16) has no bucket yet. No shelf file is staged to either that names the Bosnian Church; see §5.

## 3. Verified acquisition leads

Each lead was checked on its host. Item records were read for date, `possible-copyright-status`, licence and the text file. Texts fetched were sampled at opening, middle and end. All are public domain by date unless a row says otherwise.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Acta Bosnae potissimum ecclesiastica | Eusebius Fermendžin | none (Latin) | 1892 | archive.org `actabosnaepotis00fermgoog` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata and title page read; 1.2 MB fetched; Latin with doubled spaces, about 0.50 matched against a clean Latin word list; October 2026. **Vendored.** |
| Vetera monumenta Slavorum meridionalium, tomus primus | Augustin Theiner | none (Latin) | 1863 | archive.org `bub_gb_ahptjBz6wEAC` | pd-us-by-date; Public Domain Mark 1.0 | metadata and title page read; 3.9 MB fetched; readable papal Latin, about 0.61 matched; October 2026. **Vendored.** |
| Testamenat gosta Radina, Glasnik zemaljskog muzeja XXIII | Ćiro Truhelka | none (Croatian) | 1911 | archive.org `glasnikzemaljsk2319zema_2` | pd-us-by-date on the printed 1911; the host date 1948 is not relied on | metadata and title page read; 1.8 MB fetched; commentary readable, testament text unusable; October 2026. **Vendored as an extract.** |
| Bogomili i Patareni, Rad knjige VII, VIII, X | Franjo Rački | none (Croatian) | 1869–1870 | archive.org `rad_jugoslavenske_akademije_znanosti_knjiga_vi_vii_1869`, `..._8_1869`, `..._9_10_1869-1870` | pd-us-by-date; no rights field | metadata read; 1.4, 0.56 and 1.5 MB fetched; readable Croatian; October 2026. **Vendored as three extracts.** |
| Monumenta Serbica | Franz Miklosich | none (Serbian Church Slavonic) | 1858 | archive.org `monumenta-serbica-spectantia-historiam-serbiae-bosnae-ragusii-ed-f-miklosich-viennae-1858` | pd-us-by-date on the OCR title-page year; no host metadata | four scans fetched; this one is the best and still poor; October 2026. **Vendored as second witness only.** |
| Through Bosnia and the Herzegovina on foot | Arthur J. Evans | none (English) | 1877 | archive.org `throughbosniaher00evanrich` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata and title page read; 1.2 MB fetched; clean, about 0.74 matched; October 2026. **Vendored.** |
| Vetera monumenta Slavorum meridionalium (second Google scan) | Augustin Theiner | none (Latin) | 1863 | archive.org `bub_gb_XXtcAAAAcAAJ` | Public Domain Mark 1.0 | metadata read; text not fetched; October 2026. Duplicate edition; not vendored. |
| Acta Bosnae, Michigan scan (bound with a second Monumenta volume) | Eusebius Fermendžin | none (Latin) | 1892 | archive.org `monumentaspecta00umjegoog` | NOT_IN_COPYRIGHT | metadata read; 2.9 MB fetched; the Acta Bosnae part reads better (about 0.60 matched); October 2026. Not vendored as a second scan of a vendored edition; use it if the Harvard scan proves too poor. |
| Poviest Bosne do propasti kraljevstva | Vjekoslav Klaić | none (Croatian) | 1882 | archive.org `poviestbosnedop00klaigoog` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata read; 0.89 MB fetched; clean; October 2026. Scholarship; not vendored. |
| Geschichte der Serben, I | Konstantin Jireček | none (German) | 1911 | archive.org `geschichtederser00jire` | pd-us-by-date on the host date; no rights field | metadata read; 1.2 MB fetched; clean; October 2026. Scholarship; not vendored. |
| Essays on the Latin Orient | William Miller | none (English) | 1921 | archive.org `cu31924028255861` | pd-us-by-date; no rights field | metadata read; 1.9 MB fetched; clean; October 2026. A passage on the Bogomils of Bosnia at about line 23100 (43 Bogomil hits in the book); Evans covers the same ground; not vendored. |
| Bullarium Franciscanum, tomus V (1319–1378) | Konrad Eubel (ed.) | none (Latin) | the host says 1798, which cannot be right | archive.org `bullariumfranciscanum_v` | Public Domain Mark 1.0; title-page year not read | metadata read; 3.9 MB fetched and opened at the front only; October 2026. About 36 mentions of Bosnia; not vendored. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Gost Radin's testament as a stand-alone text (Truhelka 1911) | Named in the task as the one inside document | Found only inside Truhelka's article, now vendored as an extract. No stand-alone transcription or clean image was found. The wording cannot be quoted from the OCR (Bosnian Cyrillic read as noise). |
| Miklosich, other scans (`monumentaserbica00mikluoft`, `monumentaserbic00miklgoog`, `MonumentaSerbica`) | The standard edition of the Bosnian charters | Fetched and sampled. The Toronto scan reads Cyrillic as Latin noise (0.09 matched); the Michigan scan gives wrong letters; the 2018 upload is noise. Only the untitled upload (vendored) is partly usable. |
| Evans, other scans (`throughbosniaan01evangoog` and five others) | Same book | Duplicates of a vendored edition. |
| Fermendžin Acta Bosnae, Harvard scan completeness | The vendored scan | Checked: it runs to the last regest (1752) and ends in the index at the letter S. The index is cut short; the body is complete. |
| Wadding, Annales minorum (`bub_gb_vEGB9UpkE9UC` and six other volumes) | The Franciscan mission to Bosnia | Listed on the host but not opened; the volumes are large Latin folios and Fermendžin already regests the Bosnian entries. |
| Thalloczy, Studien zur Geschichte Bosniens; Ćorović, Historija Bosne | Standard scholarship | Not found on the host by title or creator search. |
| Kniewald 1949 (`kniewald-dragutin-vjerodostojnost-latinskih-izvora-o-bosanskim-krstjanima-1949`); Mužić, Vjera Crkve bosanske (2008); Džaja and Lovrenović (2007); Wenzel, Ukrasni motivi na stećcima (1965); Beslagić, Stećci (2016) | The scholarship that overturned the Bogomil reading | In copyright (published 1931 or later, foreign). Not downloaded. |
| Fine, Šanjek, Lambert | Named in the task | In copyright; closed. |
| Truhelka, Hrvatska Bosna (1907, `TRUHELKA190757`) | An earlier work by the editor of the testament | Listed on the host but not opened. |
| Truhelka, Studije o podrijetlu (1941) | Same author | 1941 Zagreb publication; assumed in copyright. |
| Stećci and grave inscriptions | The census names them as the church's surviving monument | Not texts in the library's sense; the census says the claim that stećci are specifically a Bosnian Church monument is no longer accepted. |

## 5. Open cross-world questions

- **The Bogomil and Cathar boundary.** Rački and Evans treat the krstjani as Bogomil and link them to the Cathars of western Europe. The census puts the Cathars (IV.12) on the register as a floor question. Where this world stops and that one starts is a Step 0 question for both. The historiography is part of this world's story, not its evidence.
- **The Serbian and Bulgarian line.** Serbian and Bulgarian medieval monasticism (IV.16) shares the Slavonic liturgy and the region. The charters in Miklosich cover both. How much of the Slavonic-rite church belongs to which world is open.
- **The window's end.** The window ends in 1463, with the Ottoman conquest. Gost Radin's testament is dated 1466 and is the world's key document. A Doc_01 must say how the world treats a source from three years after its close.
- **Partial extracts.** The Rački and Truhelka files are extracts cut at article boundaries from larger volumes. If the lead prefers whole volumes, the host files are named in each header.
- **The Latin papal church.** The papal and Franciscan record is also the Latin papal church's business (V.14). The proposed rows put Fermendžin and Theiner on this world only.
- **The Hussite link.** The Constance accounts name the queen of Bosnia in Sigismund's party (see §2). Whether that belongs anywhere is for the Hussite world's builder.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says the church was not a dualist body and that its beliefs are still debated. Nothing found settles it. The 1203 instrument has the priors promise to keep oratories, altars, crosses and the Old and New Testament, and Truhelka reports a large cross at the head of Radin's will with the opening "Va ime oca i sina i svetago duha. Amen." (host line 20887, here line 820). That fits the census. Neither is a creed. Innocent IV wrote in 1247 that the diocese had "lapsa ... in perfidiam hereticae pravitatis" (here line 1086). Read the floor as open.

**Sourcing (B1).** The census says "largely external", and that holds. Three inside voices exist, each with a limit: a chancery Latin instrument, a will whose wording is on a page image, and charters whose OCR is poor. There is no public-domain English apart from Evans, who argues the reading the census calls rejected.

**Ecology (B2).** One outside side is hostile (Rome, the Franciscans), one protective (Bosnia's own kings), and one is a Ragusan record of trade and politics. The church appears in all three and speaks in none of them at length.

**Uniqueness (B3).** Against the Cathars the overlap is the old Bogomil identification. Against the Serbian and Bulgarian world it is the Slavonic rite and the charters. Against the Latin papal church it is the mission and the condemnations. Each is a boundary to state.

**Audiences (B4).** No church continues. The argument about the church is part of Bosnian national self-understanding, and the stećci are a visible monument. The audience is real but not a congregation.

**Scale (B5).** About 9.3 MB vendored in eight files, of which the Theiner volume is 3.9 MB. Nine placements in the staged rows, no secondary placements on other worlds, one cross-link row proposed. The next acquisition is a clean image or transcription of Radin's will.

**Recommendation: open question.** The sources can describe this church. They cannot yet let it speak. Its own words are one oath, one will and a set of witness lists, each needing page-image work before a line is quotable, and no public-domain English for any of them. The census itself asks for the ambiguity to be acknowledged, not resolved. If the design accepts a Representative whose own words are a will and an oath, a build could run after the will's plates are in hand. If not, the entry should stay atlas only. This is a recommendation for Mark to weigh, not a decision.
