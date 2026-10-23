# Source Readiness Dossier — Muscovite Monastic Christianity

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.8
**Corpus-map slug:** `muscovite-monastic-christianity`
**Time window:** c. 1340–1517
**Region(s):** The Russian north (the Trinity monastery of Sergius near Moscow, the Beloozero and Solovetsky houses, the Volokolamsk house)
**Dossier author / date:** Library thread, Era VI session (east batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. No bucket file `cic/corpus-map/muscovite-monastic-christianity.yaml` existed before this pass. Three files were vendored for this world, each with a staging file that passes `corpus_map_merge.py --check`. Their registry entries, seed rows and cross-link rows sit in the lead's fragment files until merged.

Census inputs (checked October 2026 in `world-census.json`): status Pre-Survey Candidate, floor note "No question". Sourcing line: "Moderate-to-rich: lives, skete rules, the possessors/non-possessors polemics; peasant voice thin." The census names six voices: Sergius of Radonezh, Epiphanius the Wise, Stephen of Perm, Nil Sorsky, Joseph of Volotsk and Andrei Rublev.

## 1. Already assigned

Nothing was assigned to this world before this pass. The three files below were vendored this pass. Scale is characters in the vendored file, counted; for the Menaion the two Sergius sections are counted separately.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Great Menaion of Metropolitan Macarius, September 25: the Life of Saint Sergius of Radonezh (Pachomius's redaction) and the Praise of Sergius ascribed to Epiphanius, Church Slavonic | macarius-metropolitan | tradition | assigned | 1,775,607 characters in the file; the Life is about 313,000 (file lines 1363–12158) and the Praise about 35,000 (lines 12159–13358) | `macarius-metropolitan_velikie-minei-chetii-september-25-30-chu_arkheograficheskaya-kommissiya1883.txt` |
| Nil Sorsky, the Tradition and the Rule for the skete (Предание и Устав), Slavonic with the editor's Russian introduction, 1912 | nil-sorsky | tradition | assigned | 251,550 characters | `nil-sorsky_predanie-i-ustav-chu_borovkova-maikova1912.txt` |
| A History of the Church of Russia (Mouravieff; Blackmore's English, 1842) | mouravieff | context | assigned | 1,238,051 characters | `mouravieff_history-of-the-church-of-russia_blackmore1842.txt` |

The same pass also staged secondary placements. The Menaion is placed on the Russian church from Stoglav to Nikon (context, provisional). Nil is placed there as an antecedent (provisional). Mouravieff is placed on the Stoglav-to-Nikon world, the Nikon-to-Holy-Synod world and the Old Believers (context, provisional).

What kind of witness each is:

- **The movement's own voice.** Two files. The Menaion carries the Life of Sergius as Pachomius the Serb reworked it, and the Praise that the volume assigns to Epiphanius. The Life names its writer in the first person ("мне недостойному Пахомию", file line 5033). The census says Epiphanius's own Life survives only through Pachomius's redactions, and the Menaion fits that. The Nil file is the non-possessor leader's own rule. Both are Slavonic with systematic OCR substitutions (the letter yat read as Ь, Б or Ф; i read as a digit or an exclamation mark), so they are quotable only after the page image is checked.
- **The outside narrator.** Mouravieff is a Russian official's history in an English chaplain's translation. It covers Sergius (file line 3151), the Solovetsky foundation (3520), Joseph of Volokolamsk (4413) and Nilus of Sor (4648). It speaks about the movement, not for it. It is the only public-domain English leg found.
- **Not here.** Joseph of Volotsk, Stephen of Perm and Rublev have no text in the library from their own hands. The possessors' side appears only through the Stoglav retrospective on the shelf and through Mouravieff.

## 2. Cross-link opportunities

Checked by searching the headers and bodies of every `cic/texts/*.txt` for Radonezh, Sergius, Sorski, Volokolamsk, Volotski, Beloozero, Solovetsk, Perm and Pachomius, then opening the hits. Proposed rows are in the lead's `crosslinks.yaml`.

- **Stoglav, French (Duchesne 1920), `stoglav_stoglav-fra_duchesne1920.txt`** (bucket: Stoglav to Nikon). Tier: same time-place. Duchesne's introduction names Joseph Volotski as founder of the Volokolamsk house and Nil Sorski as the best-known partisan of the other side, and says they met at the council of 1503 (lines 1146–1180). The council's own roll of the saints (lines 2494–2497) names the great Sergius of Radonezh and Cyril of Beloozero beside Antony and Theodosius of the Caves. Proposed row: context / assigned.
- **Stoglav, Russian (Kozhanchikov 1863), `stoglav_stoglav-chu_kozhanchikov1863.txt`.** Tier: same time-place. The council's chapters on monasteries are a retrospective on this movement from a century later. Proposed row: context / provisional; the monastery chapters were not read.
- **Herberstein, Notes upon Russia vol. 1 (Major 1851), `herberstein_notes-upon-russia-v1_major1851.txt`.** Tier: same place, just after the window (his visits fall in 1517–1549). He calls the Holy Trinity house "the principal monastery in Moscow ... where St. Sergius was buried, and is said to perform many miracles" (line 11127). Proposed row: context / assigned.
- **Fletcher, Of the Russe Common Wealth (Bond 1856), `fletcher-giles-elder_russe-common-wealth-with-horsey-travels_bond1856.txt`.** Tier: out-of-window (1591). The chapter on the church describes the Trinity house, with about 700 friars, and the empress's yearly pilgrimage on foot to Saint Sergius (lines 10660–10675). Proposed row: context / provisional.
- **Avvakum, the Life (English and Russian), `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` and `avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`** (bucket: the Old Believers). Tier: out-of-window. The census calls this world the parent of the Old Believers' tradition, and Avvakum names Sergius and the Solovetsky house. A child world's text staged as transmission on its parent is a placement the lead should rule on, so the row is proposed as transmission / needs-ruling.
- **Rycaut, Present State of the Greek and Armenian Churches (1679), `rycaut_present-state-greek-armenian-churches_1679.txt`.** Noted, no row: it covers the Greek and Armenian churches under the Ottomans, not Muscovy.
- **Noted, no row proposed:** `olearius_voyages-and-travels-of-the-ambassadors_davies1662.txt` (a seventeenth-century embassy; not opened for monastic matter) and `kyiv-synopsis_sinopsis-chu_1762.txt` (Kyivan, eighteenth-century).

## 3. Verified acquisition leads

Each lead was checked on its host. Item records were read for date, `possible-copyright-status`, licence and the text file. Texts fetched were sampled at opening, middle and end. All are public domain by date unless a row says otherwise.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Великие Минеи Четии, собранные митрополитом Макарием, Сентябрь, дни 25–30 (Life of Sergius, Praise by Epiphanius) | Macarius (compiler) | none (Slavonic) | 1883 (OCR title page reads 1888) | archive.org `velikiemineichetiisobrannyevserossijski92` | pd-us-by-date; no rights field | metadata read; 3.1 MB fetched and sampled; readable Slavonic with letter substitutions; October 2026. **Vendored.** |
| Предание и Устав | Nil Sorsky; ed. M. S. Borovkova-Maikova | none (Slavonic) | 1912 | archive.org `predanieiustav79` | pd-us-by-date; no rights field | metadata read; 0.43 MB fetched and sampled; readable Cyrillic; October 2026. **Vendored.** |
| A History of the Church of Russia | A. N. Mouravieff | R. W. Blackmore | 1842 | archive.org `historyofchurcho00mouriala` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata and title page read; 1.2 MB fetched and sampled; clean English; October 2026. **Vendored.** |
| Исследование о сочинениях Иосифа Санина, преп. игумена Волоцкого | Ivan P. Khrushchov | none (Russian) | 1868 | archive.org `issledovanieosochinenijahiosifasaninapr91` | pd-us-by-date on the host date; no rights field | metadata read; text not fetched; October 2026. Scholarship on Joseph; not vendored. |
| Древнерусские жития святых как исторический источник | Vasily O. Klyuchevsky | none (Russian) | 1871 | archive.org `drevnerusskiezhitijasvjatyhkakistoriches61` | pd-us-by-date on the host date; no rights field | metadata read; text not fetched; October 2026. Scholarship on the lives; not vendored. |
| История русской церкви, том 1 | Evgeny E. Golubinsky | none (Russian) | 1901 (part 1) and 1881 (part 2) | archive.org `golubinsky11` | pd-us-by-date on the host date; no rights field | metadata read; text not fetched; October 2026. Scholarship; the Nil file cites it. Not vendored. |
| Историческое описание ставропигиального первоклассного Соловецкого монастыря | Meletius | none (Russian) | 1881 | archive.org `istoricheskoeopisaniestavropigialnogope93` | pd-us-by-date on the host date | metadata read; text not fetched; October 2026. A later monastery history; not vendored. |
| Историко-статистическое описание Кирилло-Белозерского монастыря | Gerontius and Kurganovsky | none (Russian) | 1897 | archive.org `istorikostatisticheskoeopisaniekirillo57` | pd-us-by-date on the host date | metadata read; text not fetched; October 2026. A later monastery history; not vendored. |
| Зыряне и просветитель их святой Стефан, первый епископ Пермский | Alexander V. Krasov | none (Russian) | 1896 | archive.org `krasovavzyrjaneiprosvetitelihsvjatojs40` | pd-us-by-date on the host date | metadata read; text not fetched; October 2026. Scholarship on Stephen of Perm; not vendored. |
| Russian Dissenters | F. C. Conybeare | none (English) | 1921 | archive.org `russiandissente00conyuoft` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata read; text not fetched; October 2026. Old Believers, a later era; not vendored. |
| Some links in the chain of Russian church history | Walter H. Frere | none (English) | 1918 | archive.org `somelinksinchain00freruoft` | pd-us-by-date on the host date; no rights field | metadata read; text not fetched; October 2026. Judged by title only; not vendored. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Joseph of Volokolamsk, Prosvetitel' (Kazan 1857 and 1882) | The possessors' own statement; named in the task | Searched archive.org by the Russian title, "обличение ереси жидовствующих", "Иосиф Санин", "Иосифа Санина Просветитель" and "Iosif Sanin Prosvetitel". No edition found. The only Joseph hits were Khrushchov's study (above) and a 1959 Soviet edition of his letters (`poslaniya_iosifa_volotskogo`, Zimin, in copyright). |
| Epiphanius the Wise, Life of Sergius, as a stand-alone text (Tikhonravov 1892) | The founding hagiography | Searched by Russian and transliterated titles; no Tikhonravov volume or stand-alone Life found. The Menaion (vendored) carries the Pachomian redaction and Epiphanius's Praise. English: Zenkovsky's *Medieval Russia's Epics, Chronicles, and Tales* is on the host (`medievalrussiase0000unse`) but flagged restricted (borrow-only) and is in copyright. |
| Life of Sergius, Nikon (1904, `zhitieipodvigiprepodobnogoibogonosnogoot63`) and a Life of 1894 (`zhitieprepodobnogosergijaigumenaradonezh8`) | Titles read as Lives of Sergius | The 1904 item (898 KB) is a modern biography by its title and was not read through; the Menaion has the older texts. The 1894 text file returns a server error from the host (HTTP 500). |
| The other volumes of Macarius's Great Menaion | The lives of Kirill of Beloozero (June), Zosima (April), Savvatii (September), Stephen of Perm (April) | The host holds only September and October volumes: `velikiemineichetiisobrannyevserossijski38` (September 1–13), `...49` (September, second issue), `...92` (September 25–30) and three October items (`...21`, `...50`, `...70`). Kirill, Zosima and Stephen fall in months not on the host. Savvatii's day was not located in the September 25–30 volume. |
| Nikon Chronicle (PSRL 9–12, `9_20241124_20241124_1125`, `10_..._1131`, `11_..._1136`, `12_..._1139`) | Named in the task; the chronicle that records Sergius's death and the council of 1503 | Volumes 10, 11 and 12 fetched (1.6, 1.0 and 1.3 MB) and sampled. The Cyrillic comes out as noise, and the names Sergius and Nil count at or near zero. Unusable. |
| Stoglav (Kozhanchikov 1863 and Duchesne 1920) | Named in the task | Already on the shelf (`stoglav_stoglav-chu_kozhanchikov1863.txt`, `stoglav_stoglav-fra_duchesne1920.txt`) and staged for the Stoglav-to-Nikon world. A second Russian scan (`stohlav1860`, 657 KB; `stoglav78`, 604 KB) is a duplicate edition. |
| Goldfrank, Nil Sorsky: the Authentic Writings (2008); Goldfrank, Monastic Rule of Iosif Volotsky (1983); Maloney, Spirituality of Nil Sorsky (1964); Zenkovsky (1963) | The English for Nil and Joseph | In copyright. The hosts hold them as borrow-only (`restricted true` on `nilsorskyauthent0000nils`, `spiritualityofni0000geor`, `medievalrussiase0000unse`). Not downloaded. |
| Poslaniya Iosifa Volotskogo (Zimin and Lur'e, 1959) | Joseph's letters | Soviet edition of 1959; in copyright as a foreign publication of 1931 or later. |
| Velikie Minei Chetii and PSRL as English | A public-domain English of the lives | None exists in the public domain that the host or the searches show. |
| Miller, Saint Sergius of Radonezh (2010); Rock in the Cambridge History of Christianity vol. 5 | Named in the task as secondary and reference | In copyright. Not searched on the host. |
| Mouravieff duplicates (`historyofchurcho0000anmo`, `bwb_Y0-DUS-211`, `bwb_T3-CBS-824`) | Other scans of the 1842 book | Duplicates of a vendored edition; the Berkeley copy was used. |

## 5. Open cross-world questions

- **The Stoglav boundary.** The council of 1551 looks back on the monastic movement, and the census puts the Stoglav world at 1517–1650. Where this world ends and that one starts is a Step 0 question for both. The 1503 council on monastic land is in this window; the Stoglav's chapters on monasteries are in the next.
- **Parent and child with the Old Believers.** Avvakum is staged as transmission, needs-ruling (see §2). The question is whether a child world's text should be named on its parent at all.
- **The hesychast line.** The census gives the parents as Kyiv and the hesychast line. The Palaiologan world (V.15) carries the Greek side. Nil learned his skete rule from Athos, but the vendored Slavonic does not say so in the pages read; the question is how much of Athos belongs here.
- **What counts as Epiphanius.** The census says Epiphanius's own Life survives only through Pachomius. Doc_01 should say whether the Pachomian Life counts as the world's founding text and how the Representative speaks of its authorship.
- **Language rule.** Both own-voice texts are Slavonic with no public-domain English. Under the September 2026 rule a clean original can be primary. These two are not clean (§1). Doc_02 should say which parts are quotable.
- **Rublev.** The census lists the icon painter as a voice. No text from him exists in the library, and an icon is not a quotable source.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says "No question". Nothing found disturbs that. The Life of Sergius names the Holy Trinity in its first column (near file line 1451), and Nil's rule quotes the Fathers (Isaac and the Ladder appear in the lines sampled). I did not read either for doctrine.

**Sourcing (B1).** The census says "Moderate-to-rich", and for Sergius and Nil that holds. The founding hagiography is in the library as a printed Menaion in Slavonic (about 313,000 characters for the Life and 35,000 for the Praise), and Nil's rule is there in the 1912 edition. Joseph's text, the Lives of Kirill, Zosima and Stephen, and the chronicles are not usable on the host. The possessors speak only through the Stoglav and through Mouravieff.

**Ecology (B2).** The movement speaks in two voices of its own: the Sergius hagiographers and Nil. A third, Joseph, is missing. The outside voices are Herberstein and Fletcher (both foreign visitors), Mouravieff (a nineteenth-century official) and Duchesne (a French editor). The danger the sources show is that the non-possessor side speaks and the possessor side is summarised.

**Uniqueness (B3).** Against the Stoglav-to-Nikon world the overlap is the monastic chapters of 1551. Against the Palaiologan world and the Kyivan parent it is the hesychast prayer. Against the Old Believers it is the descent of the northern houses into the schism. Each is a boundary to state, not a reason to merge.

**Audiences (B4).** The Trinity-Sergius monastery is a working lavra. The possessor and non-possessor argument is a live topic in Russian religious writing. The audience is large and reachable.

**Scale (B5).** About 4.8 MB vendored in three files. Three placements in this world's bucket and five secondary placements on neighbouring worlds. Five cross-link rows are proposed. The Joseph gap needs one more acquisition pass before the build counts the possessor side as secure.

**Recommendation: build.** The movement speaks in its own voice in two vendored Slavonic texts. The floor is clear. The audience is large. The conditions are plain. The OCR is second-witness, so a Doc_02 must check each quote against the page images. There is no public-domain English for the voices, so the English a Representative speaks would come from the Slavonic. Joseph's text is not available, so a Representative should not speak for the possessors beyond what the Stoglav and Mouravieff report. This is a recommendation for Mark to weigh, not a decision.
