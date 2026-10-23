# Source Readiness Dossier — The Union of Brest & Ruthenian Greek Catholic Christianity

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.20
**Corpus-map slug:** `the-union-of-brest-and-ruthenian-greek-catholic-` (the census id is truncated and ends in a hyphen; it is also the bucket filename)
**Time window:** 1596–c. 1700
**Region(s):** Ruthenia (today's Ukraine and Belarus), inside the Polish-Lithuanian Commonwealth
**Dossier author / date:** source-research thread (Era VII one-world agent), October 2026. First written in this pass; no earlier dossier existed.
**Corpus-map / `cic/texts/` state as of:** October 2026. The bucket holds two Mogila rows (merged). Nine files vendored in this pass sit in `cic/corpus-map/_staging/` until the lead merges them.

## 1. Already assigned

**Merged in `cic/corpus-map/the-union-of-brest-and-ruthenian-greek-catholic-.yaml` (two rows, both `context`, `provisional`):**

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Orthodox Confession (Confessio Orthodoxa), Greek with Latin | mogila | context | provisional | one third of a two-volume Latin/Greek collection | `monumenta-fidei-ecclesiae-orientalis_confessions-grc-lat_kimmel1850.txt` |
| The Orthodox Confession, English version | mogila | context | provisional | one work in a short volume | `mogila_orthodox-confession_overbeck1898.txt` |

Both were placed on window and place, and the staging notes say the text was not checked for its treatment of the union. This pass checked: the English file has no hits for Brest, Ruthenian or Uniate. Kimmel's Latin prolegomena mention the "Ruthenicae provinciae" under Sigismund III (about file line 1713). The confession is the Orthodox answer to the situation the union created, not a text about the union. `provisional` is right.

**Vendored and staged in this pass (nine files, October 2026 to October 2026):**

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Vetera monumenta Poloniae et Lithuaniae, tomus III (1585–1696): the 1595 articles, the bull *Magnus Dominus et laudabilis*, the professions of faith and the acts of the Synod of Brest, in contemporary Latin versions | theiner | tradition (Brest); context (Tridentine Church VI.22); context (later Ruthenian letters) | assigned / provisional | ~551,000 words, clean OCR | `theiner_vetera-monumenta-poloniae-lithuaniae-v3-lat_1863.txt` |
| Annales Ecclesiae Ruthenae (Lviv, 1862) | harasiewicz | context | assigned (Brest); provisional (18th and 19th c. Uniate entries) | ~327,000 words, readable Latin | `harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt` |
| Saulus et Paulus (life of Smotryc'kyj, Susza, ed. Martinov 1864) | susza | tradition (Brest); context (Kyiv-Mohyla) | assigned / provisional | ~33,000 words, clean | `susza_saulus-et-paulus-ruthenae-unionis-lat_martynov1864.txt` |
| Cursus vitae et certamen martyrii B. Josaphat Kuncevicii (Susza, ed. Martinov 1865) | susza | tradition | assigned | ~52,000 words, clean | `susza_cursus-vitae-josaphat-kuncevicii-lat_martynov1865.txt` |
| Un apôtre de l'union des Églises au XVIIe siècle (Guépin, 2nd ed., 2 vols, 1897) | guepin | context | assigned | ~432,000 words, clean French | `guepin_apotre-de-l-union-des-eglises-fra_1897.txt` |
| Geschichte der Union der ruthenischen Kirche mit Rom, vol. 2 (Pelesz, 1880) | pelesz | context | assigned (Brest); provisional (two later Uniate entries) | ~398,000 words, readable German | `pelesz_geschichte-der-union-bd2-deu_1880.txt` |
| Russian Historical Library vol. 7, Monuments of polemical literature in Western Rus', book 2 (1882): Skarga's 1577 treatise and 1596 Brest defence, the Uniate pamphlets of 1595 and 1608, the *Apokrisis* of Christopher Philalethes, Vasyl of Ostroh 1588, the 1603 Orthodox questions and answers, a Herbest brochure | skarga and others | tradition (Uniate texts); context (Orthodox replies); tradition provisional (Kyiv-Mohyla) | assigned / provisional | ~188,000 words; **second witness**, Cyrillic partly garbled, Polish badly | `russkaya-istoricheskaya-biblioteka_pamyatniki-polemicheskoi-literatury-zapadnoi-rusi-t7-rus_giltebrandt1882.txt` |
| Smotryc'kyj, *Threnos* (Polish, 1610) | smotrycki | context (Brest); antecedent (Kyiv-Mohyla) | assigned / provisional | ~94,000 tokens; **second witness**, black-letter OCR badly garbled | `smotrycki_threnos-pol_1610.txt` |
| Smotryc'kyj, *Apologia* of his journey to the East (Polish, 1628) | smotrycki | tradition (Brest); context (Kyiv-Mohyla) | assigned / provisional | ~58,000 tokens; **second witness**, garbled | `smotrycki_apologia-peregrinatiey-pol_1628.txt` |

Total about 2.1 million words. The brief asked for roughly four to seven files; nine were vendored because the two Smotryc'kyj prints and the Susza lives are short and each carries a distinct voice.

What the set gives a build:

- **The union's own acts.** Theiner prints the bishops' conditions of 1595, the bull, the professions of faith at Rome and the Synod of Brest decree. These are Latin versions made at the time from Ruthenian and Polish originals. The originals are not in the volume. This is the cleanest primary material in the set.
- **Polemic as a native genre, both sides.** Skarga (Jesuit, pro-union), the 1595 and 1608 Uniate pamphlets, and the Orthodox replies (*Apokrisis*, Vasyl of Ostroh, the 1603 handbook) are in one volume. Smotryc'kyj appears on both sides: the *Threnos* (Orthodox, 1610) and the *Apologia* (after his turn, 1628).
- **The saint's life.** Susza's two Latin lives (1664–66 originals, here in the 1864 and 1865 editions with editorial additions not separated) and Guépin. Josaphat Kuntsevych's own words are not in the set (see §4).
- **Narrative history.** Harasiewicz, Pelesz, Guépin. All are written from inside the union. They help a build find sources and are not primary voices.

**Language, honestly stated.** Nothing vendored in this pass is in English. Latin (Theiner, Harasiewicz, Susza) is clean enough to quote after a page-image check. French, German and the Cyrillic and Polish texts are original-language witnesses under the September 2026 ruling. Three files are second witnesses because of OCR (RIB vol. 7, Threnos, Apologia); each header and each staging note says so.

## 2. Cross-link opportunities

Checked October 2026 by searching the `Title:`/`Creator:` header lines of `cic/texts/*.txt` for Ruthenian, Brest, Lithuanian, Polish, Mogila, Smotryc'kyj, Skarga, Josaphat, Possevino and Vitebsk, then counting body hits for the same words and opening every file with a plausible hit. Proposed rows are in `crosslink_fragment.yaml` in the agent's scratch folder.

- **RIB vol. 4, Monuments of polemical literature in Western Rus', book 1 (1878).** `russkaya-istoricheskaya-biblioteka_pamyatniki-polemicheskoi-literatury-zapadnoi-rusi-t4-rus_giltebrandt1878.txt`, vendored by the Kyiv-Mohyla pass during this same session. Per its own header it holds Lev Krevza's *Oborona uni* (1617, Uniate), the Brest hegumen Afanasii Filippovich's *Diarius* (1646), the acts of the Kyiv council of 1640 and Kopystenskii's *Palinodiia*. Rows proposed for this world: Krevza `tradition`, Filippovich `context`, the Kyiv council `context`, all `provisional` (read from the header, not the text). Tier: same time-place. This pass did not open the text.
- **`acta-et-scripta-wirtembergensium_jeremias-ii-correspondence-lat_1584.txt`.** Patriarch Jeremias II's replies to the Tübingen theologians, 1576–1581. Nine hits for Russian and Polish words, none for Ruthenia or Lithuania. No row. Tier: same time-different-region (Constantinople); context for the Patriarch whom the union bishops left, not for this world.
- **`jeremias-ii_censura-orientalis-ecclesiae-lat_socolovius1582.txt`.** Present in the working tree as an unstaged change by another pass. Not opened here; flagged for the lead.
- **`monumenta-fidei-ecclesiae-orientalis_confessions-grc-lat_kimmel1850.txt` and `mogila_orthodox-confession_overbeck1898.txt`.** Already assigned (§1). Tier: same time-place.
- **Jesuit letter series** (`lainez_*`, `borgia_*`, `salmeron_*`, `nadal_*`): scattered mentions of Vilna and a "Rutheni collegium" in the 1550s–60s. Out of window; no rows. Tier: out-of-window.
- **Golubev, Petr Mogila i ego spodvizhniki (vols. 1–2)** and the other new Era VII files in the tree are the Kyiv-Mohyla agent's. Not opened. Tier: same time-place for Kyiv-Mohyla; the lead should check them for Brest rows when that agent's staging is merged.
- **Sibling entries that the new files also serve** (rows already written): `the-tridentine-church` (VI.22) for the Theiner papal instruments; `the-society-of-jesus` for Skarga; `the-kyiv-mohyla-orthodox-revival` (VI.21) for the Orthodox polemic and Smotryc'kyj; `ruthenian-uniate-18th-century` and `ruthenian-greek-catholic-polotsk-to-galicia` for Harasiewicz and Pelesz.

## 3. Verified acquisition leads

Every row checked on archive.org by metadata fetch on the dates shown. Rows marked **Vendored** are in `cic/texts/` (§1). No English-language public-domain translation of any vendored text was found (§4).

| title | author | translator/ed. | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Vetera monumenta Poloniae et Lithuaniae, tomus III | Augustin Theiner (ed.) | none | 1863 | archive.org `veteramonumentap03thei` | pd-us-by-date; no host rights field; Princeton copy | metadata, title page ("18G3" in the OCR), five-point OCR sample, Brest documents located, October 2026 and October 2026. **Vendored.** |
| Annales Ecclesiae Ruthenae | Michael Harasiewicz | none | 1862 (preface dated 29 June 1862; title-page year garbled; body mentions 1864) | archive.org `annales-ecclesiae-ruthenae-gratiam-et-co-1` | pd-us-by-date; host licenseurl Public Domain Mark 1.0 | metadata, title page, preface date, five-point sample, October 2026. **Vendored.** The host catalogue date "1600" is wrong. |
| Saulus et Paulus Ruthenae unionis sanguine B. Josaphat transformatus | Jacob Susza | ed. Joannes Martinov S.J. | 1864 | archive.org `saulusetpaulusr00martgoog` (also `bub_gb_MbOEfXzhy5kC`, CC Public Domain Mark) | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata, title page, five-point sample, October 2026. **Vendored.** |
| Cursus vitae et certamen martyrii B. Josaphat Kuncevicii | Jacob Susza | ed. Joannes Martinov S.J. | 1865 | archive.org `cursusvitetcert00martgoog` | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata, title page, five-point sample, October 2026 (a first fetch returned an error page; the retry succeeded). **Vendored.** |
| Un apôtre de l'union des Églises au XVIIe siècle, 2nd ed., 2 vols | Alphonse Guépin | none | 1897 | archive.org `unapotredelunion01guuoft` (a second scan, `unapotredelunio00guepgoog`, Harvard) | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata, title page, five-point sample, October 2026. **Vendored.** |
| Geschichte der Union der ruthenischen Kirche mit Rom, vol. 2 | Julian Pelesz | none | 1880 | archive.org `geschichtederuni0002pele` | pd-us-by-date; no host rights field | metadata, title page, five-point sample, October 2026. **Vendored.** Volume 1 (to 1595) is `geschichtederuni0001pele` (also `geschichtederuni01pele`, Toronto, 1878); not vendored, it ends before the union. |
| Russkaia istoricheskaia biblioteka, vol. 7 | P. A. Giltebrandt (ed.) | none | 1882 | archive.org `russkajaistoricheskajabibliotekaizdavae14` | pd-us-by-date; no host rights field | metadata, title page, contents, five-point sample, October 2026. **Vendored as second witness.** |
| Threnos (Polish) | Meletij Smotryc'kyj ("Theophilus Orthologus") | none | 1610 | archive.org `jbc.bj.uj.edu.pl.NDIGSTDR013226` (Jagiellonian Digital Library) | host record: "Domena publiczna (public domain)"; 1610 print | metadata, five-point sample, October 2026. **Vendored as second witness.** |
| Apologia Peregrinatiey (Polish) | Meletij Smotryc'kyj | none | 1628 | archive.org `jbc.bj.uj.edu.pl.NDIGSTDR013215` | host record: "Domena publiczna (public domain)"; 1628 print | metadata, title page, five-point sample, October 2026. **Vendored as second witness.** |
| Unia brzeska (r. 1596) | Edward Likowski | none | 1907 | archive.org `uniabrzeskar00likogoog` (also `uniabrzeskar159600liko`, 1896; French `likowski-union-de-l-eglise-1903`) | pd-us-by-date; host NOT_IN_COPYRIGHT (Michigan) | metadata only, October 2026. Not vendored: Polish scholarship; a build may want it as a second narrative. |
| Synod Brzeski: namowa posłów Króla I. M. i obrona Synodu Brzeskiego (Skarga) | Piotr Skarga | none | 1874 reprint | archive.org `rcin.org.pl.WA248_275734_F-5641_skarga-synod_o_240101` | host: "Public Domain"; 1874 imprint | metadata only, October 2026. Not vendored: a 34-page reprint of the Skarga text that RIB vol. 7 already carries, in Polish, and a clean-looking Polish witness for the passages that are garbled in RIB vol. 7. A good candidate for a later pass. |
| Cursus vitae, further editions; *Saulus et Paulus* of 1666 (Rome) | Susza | none | 1666 | archive.org `bub_gb_NKN07ohWr7kC` | not checked | search listing only, October 2026. Not opened. The 1666 original would let a build separate Susza's text from Martinov's additions. |
| Vetera monumenta Poloniae et Lithuaniae, tomus II (1410–1572) and tomus IV (1697–1775) | Augustin Theiner | none | 1861, 1864 | archive.org `veteramonumentap02thei`, `veteramonumentap04thei` | pd-us-by-date | search listing only, October 2026. Not opened; outside the window (before 1595 and after 1697). |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| English translation of Theiner vol. 3 (`vetera-monumenta-poloniae-lithuaniae-theiner-vol3-english`) | The only English rendering of the Brest documents | The item's own description says it was "translated from Latin to English by churchlatin.ai, a product of Boyne Archives", uploaded in 2026 by a private account that applies a Public Domain Mark to its own machine translation. No human translator, no rights statement beyond the uploader's. Not vendored, and not a fact base for quotation. Closed October 2026. |
| Welykyj, *Documenta Unionis Berestensis* (1970) and *Epistolae Metropolitarum Kioviensium Catholicorum* (1956) | The modern critical editions of the union documents and Rutsky's letters | Foreign publications of 1931 or later; in copyright under the project's rule. Not searched on any host. The public-domain path to the same documents is Theiner vol. 3 (§1). Closed. |
| Ipatii Potii's own writings | The union's architect; the brief names RIB vols. 4, 7 and 19 | Searches on archive.org by creator spellings (Potii, Pociej, Potij, Hipacy, Pocey) returned one unrelated 1774 letters item. RIB vol. 7 prints a 1595 pamphlet the editors attribute to Potii only by conjecture; it is in the vendored volume and its staging row says so. RIB vol. 19 (1903) did not turn up in searches for the series title with volume number; not on the host as far as these searches show. Potii's *Antirrisis* (1599) and letters remain a gap. Closed October 2026. |
| Josaphat Kuntsevych's own words | The saint's voice | No printing of his letters or sermons found in public-domain form. His voice survives in the vendored lives (Susza, Guépin), which quote the Polotsk process. Contieri (the 1867 beatification process): archive.org creator search for "contieri" returned only unrelated items. Closed October 2026. |
| Lviv Stauropegion Brotherhood statutes (*Monumenta Confraternitatis Stauropigianae Leopoliensis*, Milkowicz 1895–98) | The brotherhood records the census names | Searches on archive.org for the title, "stauropigian", "stauropegian", "ставропигийск*" and the editor's name returned no edition of the monuments; hits were an unrelated newspaper and two modern studies (`khudash`, a 1961 vocabulary study; `bendasjuksjuobscherusskijpervopechatni65`, 1934). Not on the reachable hosts. Closed October 2026. Also relevant to Kyiv-Mohyla. |
| Public-domain English of any Ruthenian union text | The brief asks for an English beside each original | None found for the Brest acts, Skarga, the Apokrisis, Smotryc'kyj, Susza, Guépin, Pelesz or Harasiewicz. Items seen and rejected: Skarga, *The Eucharist* (Dworaczyk, 1939; a different work and a 1939 US publication that would need a renewal check), *Kazania swietowe* (1917, listed as English but a Polish title; not opened), and a modern web item on Smotryc'kyj and the Filioque. Closed October 2026. |
| Meletij Smotryc'kyj, *Threnos* and *Apologia* in Church Slavonic or Ruthenian | The original-language prints | Only the Polish versions of 1610 and 1628 were found (Jagiellonian items, vendored). The Threnos was first printed in Polish (the title page says translated from the Slavonic, which was from the Greek). Closed October 2026. |
| Pierling, *La Russie et le Saint-Siège* and Possevino's *Missio moscovitica* (1882) | Roman and Jesuit contact with the Orthodox East | Moscow-centred and mostly 1580s; they belong to the Russian Church and Society of Jesus entries, not this window. Items: `larussieetlesai00paugoog`, `antoniipossevin00gallgoog` (NOT_IN_COPYRIGHT). Not opened. Closed for this world October 2026. |
| The 1596 and 1595 original Ruthenian and Polish documents (the articles, the synod decree) | The originals behind Theiner's Latin versions | Theiner's Argumenta say the originals are omitted. Printings of them sit in Russian and Ukrainian archival series (Akty, Arkhiv Yugo-Zapadnoi Rossii), not searched individually. Open as a lead for a later pass; not closed on evidence. |
| Harasiewicz as "Annales Ecclesiae Ruthenae" under other catalogue records | Possible cleaner scan | Search by title and by creator found the one item; the creator search returned only a different Michał Harasiewicz (a 1790s newspaper editor). Closed October 2026. |

## 5. Open cross-world questions

- **Mohyla file placement.** The Kimmel and Overbeck rows for this world stay `provisional`. The confession answers the union; it is not about it. The lead may want to leave them there or drop them once Kyiv-Mohyla carries both. Not decided here.
- **RIB vol. 4 and vol. 7 split.** The Kyiv-Mohyla pass vendored vol. 4 (Krevza, Filippovich, Kopystenskii) and this pass vol. 7 (Skarga, the *Apokrisis*, the Uniate pamphlets). The Orthodox polemic is on both sides of the line between the two worlds. Rows proposed in both directions are `provisional`; the build threads decide the weight.
- **Window mismatch for early polemic.** The *Apokrisis* (1597–99), Vasyl of Ostroh (1588), the 1603 handbook and the *Threnos* (1610) sit before Kyiv-Mohyla's 1615 start. They are assigned there as `tradition` or `antecedent`, `provisional`. The Kyiv-Mohyla thread may prefer `antecedent` for all; a mapping decision for the lead.
- **Susza's two lives are 17th-century texts in 19th-century editions.** The originals are of 1664–66 and the Martinov editions are "emendatior et auctior". The additions are not marked in the file. The lead should decide whether the staging rows (`tradition`) stand until the 1666 Rome print (`bub_gb_NKN07ohWr7kC`, §3) is checked.
- **Sibling later-period entries** (`ruthenian-uniate-18th-century`, `ruthenian-greek-catholic-polotsk-to-galicia`, the Ukrainian Greek Catholic underground) will want Harasiewicz, Pelesz and Theiner IV. The first two carry `provisional` rows for them. Their own threads decide.
- **Double dates in the record.** The first fetch of the seven early files was on October 2026 (before the usage limit stopped the pass). The files were re-fetched on October 2026 with the same byte counts; the two Smotryc'kyj prints were fetched on October 2026. The registry fragment keeps `date_added` as the brief gives it for the first seven and October 2026 for the last two.

## 6. Step 0 scope notes and recommendation

**Floor question (census floorNote): "No question."** This pass read nothing that disturbs that. The union is a communion with Rome that keeps the Byzantine liturgy; Nicene and Chalcedonian standing is not in doubt. The Filioque is the live doctrinal point in the sources, and the union's makers argued it as a matter of Roman primacy and authority. The floor test is A1 and clears.

**Sourcing (B1).** The census says "moderate: synodal acts, brotherhood records, polemical literature". The first and third are in hand: the acts as Latin versions in Theiner, the polemic of both sides in RIB vol. 7 and the two Smotryc'kyj prints. Brotherhood records are not (§4). The union's architects speak only through the polemic and the acts: Potii's own writings are a gap, and Josaphat's and Rutsky's own words are not in public domain. The saint is seen through hagiography written for his canonisation cause.

**Ecology (B2).** The shape is polemical and two-sided, which the census calls native. The main risks are named: (1) no English anywhere; every quote is an original-language quote and the voice a participant hears is a modern rendering made from Latin, Polish, Ruthenian or French; (2) three of the nine files are second witnesses, so the most characteristic Ruthenian and Polish voices cannot be quoted until the page images are checked; (3) the lives and histories are written from the union's side, and the Orthodox view comes through the *Threnos*, the *Apokrisis* and RIB vol. 4, which are partly garbled.

**Uniqueness and overlap (B3).** The overlap with Kyiv-Mohyla (VI.21) is large in sources and small in story. The two worlds share the polemical volumes and Smotryc'kyj, who stands on both sides. The Tridentine Church (VI.22) shares only the papal instruments. The two later Uniate entries continue this one. The census calls the Kyiv-Mohyla world its sibling-rival, which fits.

**Audiences (B4) and scale (B5).** Not argued here. The vendored corpus is about 2.1 million words, comparable to the Anabaptist set, with a higher share in original languages other than English. No Atlas world speaks for a communion that is Eastern in rite and Roman in obedience; the census says this "restores a whole absent communion family".

**Recommendation, for Mark to decide, not a decision: build.** Floor (A1) clears with no question. Sourcing (B1) is enough: the union's acts and both sides of the polemic are in the corpus, with Latin text clean enough to quote after a page-image check. Ecology (B2) is workable but must be stated plainly in Doc_02, including the lack of Potii, Josaphat and Rutsky in their own voices and the need for page-image checks on the garbled files. Uniqueness (B3) holds because no sibling tells the story of a communion born inside an argument. If Mark reads the lack of any English and of the architects' own words as too heavy, the fallback is **part of another world**: Kyiv-Mohyla, as its two-sided partner. That fallback is weaker, since the two worlds' sources and stories point in opposite directions.
