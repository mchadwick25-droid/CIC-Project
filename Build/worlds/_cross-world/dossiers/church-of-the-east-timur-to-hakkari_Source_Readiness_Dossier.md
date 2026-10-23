# Source Readiness Dossier — The Church of the East: Timur's Catastrophe and the Hakkari Remnant

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.17
**Corpus-map slug:** `church-of-the-east-timur-to-hakkari`
**Time window:** 1317–1517
**Region(s):** Mesopotamia (Baghdad, Mosul, Arbela), then the Hakkari, Lake Van and Urmia triangle; the Malabar province as the one that outlasted it
**Dossier author / date:** Era VI library session, V.17 world agent (oriental batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. Before this pass the bucket held four rows staged by the Era VII session, all `provisional`. Five files were vendored this pass (four of them also staged for the Malabar world, three also for the Mongol-era world), each with a staging file validated with `corpus_map_merge.py --check`. Their registry entries, seed rows and cross-link rows sit in the lead's fragment files until merged.

**Who speaks.** The church speaks for itself only at the two ends of the opening years: the life of Yahballaha III, which stops at his death in 1317, and the acts and canons of Timothy II's synod of 1318. After that the library holds a patriarchal succession list, eighteenth-century Latin lives, a few manuscript colophons and a 1910 history by a member of the church. The catastrophe itself, Timur's campaigns, is told from outside, and the outside accounts in the library are weak on the church.

## 1. Already assigned

The first four rows were there before this pass. The rest are the files vendored and staged this pass. Scale is counted characters of the whole vendored file.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Bibliotheca Orientalis III.2, the dissertation De Syris Nestorianis (patriarchal line, hereditary succession, Malabar bishops) | assemani | context | provisional | 2,894,936 | `assemani_bibliotheca-orientalis-tomus3-pars2-de-syris-nestorianis-lat_1728.txt` |
| Lamy's appendix to Bar Hebraeus III, Series catholicorum Nestorianorum continuata (Timothy II, 1318, to Simeon VII, d. 1551) | barhebraeus | context | provisional | 759,749 (whole volume; the appendix starts at file line 29078) | `barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt` |
| History of the Syrian Nation and the Old Evangelical-Apostolic Church of the East, chapter XXX (Timur, Indian Christians' visits to the patriarch) | malech | tradition | provisional | 908,158 (whole volume; the chapter starts at file line 16390) | `malech_history-of-the-syrian-nation-and-old-evangelical-apostolic-church-of-the-east_1910.txt` |
| The Assyrians and their Neighbours, chapter VII (Tamerlane, the move to Hakkari) | wigram | context | provisional | 408,070 (whole volume; the chapter starts at file line 6529) | `wigram_assyrians-and-their-neighbours_1929.txt` |
| Ebedjesu's canon collection with the acts and canons of Timothy II's synod, 1318 (Mai's Latin) | mai | tradition | assigned | 2,114,856 (whole volume; acts at file line 11610, canons at 11801) | `mai_scriptorum-veterum-nova-collectio-tomus10-ebedjesu-synodus-timothei-lat_mai1838.txt` |
| Bibliotheca Orientalis III.1, De scriptoribus Syris Nestorianis (lives of the writers and patriarchs, the 1504 letter of the Malabar bishops) | assemani | tradition | assigned | 2,694,057 | `assemani_bibliotheca-orientalis-tomus3-pars1-de-scriptoribus-syris-nestorianis-lat_1725.txt` |
| The Monks of Kublai Khan, life of Mar Yahballaha III and Rabban Sauma (English) | yahballaha-sauma | antecedent | assigned | 483,699 | `yahballaha-sauma_monks-of-kublai-khan_budge1928.txt` |
| Histoire de Mar Jabalaha III et du moine Rabban Çauma (French, with appendices) | yahballaha-sauma | antecedent | assigned | 917,776 | `yahballaha-sauma_histoire-de-mar-jabalaha-iii-et-rabban-cauma-fra_chabot1895.txt` |
| Cathay and the Way Thither, vol. III (Montecorvino's letters, Marignolli) | yule | context | provisional | 739,356 | `cathay-and-the-way-thither_vol3-missionary-friars-pegolotti-marignolli_yule-cordier1914.txt` |

What kind of witness each is:

- Mai 1838: Latin translation of the acts and canons of Timothy II's synod, inside the canon collection of Ebedjesu of Soba. The Latin is clean; the Syriac is garbled. This is the church's own administrative voice. Not read through.
- Assemani III.1 (1725): eighteenth-century scholarship with printed extracts and the Latin of the 1504 letter. The Latin reads well; the long s is read as f. Quotes need the project's long-s handling.
- Budge and Chabot: two translations of the same Syriac life. The life ends at the patriarch's death in 1317.
- Lamy's appendix: a modern editor's list, compiled from Assemani and others. It is not Bar Hebraeus.
- Malech and Wigram: twentieth-century, by a member of the church and an Anglican missionary. Context, not testimony.

## 2. Cross-link opportunities

- **How far Bar Hebraeus's continuation runs.** The vendored file is the third volume of the Chronicon Ecclesiasticum (Abbeloos and Lamy, 1877). Bar Hebraeus himself stops in the thirteenth century. Lamy's appendix then lists the Nestorian catholicoi onward: Timothy II is consecrated in February 1318 (file line 29168), and the series goes on through the hereditary Simeons and Eliases to Elias VIII, elected in 1591 (file line 29245). The Timothy II entry points the reader to Mai's volume for the synod's canons, which is now vendored. The appendix is already in the bucket as context; the cross-link is to the Malabar world (below).
- **`scher_notice-manuscrits-syriaques-patriarcat-chaldeen-mossoul-fra_1907.txt`** (French, 70,396 characters; buckets: Chaldean consolidation and the Schism of 1552). A catalogue of the Mosul patriarchate's manuscripts with their colophons. One manuscript was finished in the Seleucid year 1806, which is AD 1497, in the village of Org in the diocese of Seert, in the time of Mar Simeon the patriarch and Mar Yohannan, bishop of Athel (file line 404). Another notice carries the note "in the time of Mar Yahballaha III, patriarch (died 15 November 1317)" (file line 986). These are colophons from inside the window. Tier: same time and place. Proposed role: context, provisional. Not read through.
- **`amr-ibn-matta_de-patriarchis-nestorianorum-commentaria-pars-altera-ara-lat_gismondi1896-1897.txt`** (Latin, Gismondi; fourteenth-century Amr and Sliba on the patriarchs). Its Latin pages read in descending file order. The header says it covers the patriarchs from the fifth century; I did not find out whether Sliba's text reaches Yahballaha III and Timothy II. Tier: named-never-opened. Proposed role: context, provisional, with the coverage question left for Doc_02.
- **`synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt`** (Chabot's 1902 Synodicon, bucket: the Silk Road). It prints the synods up to the eighth century and mentions Timothy II once. Not proposed.
- **`abdisho-iv_approbatio-et-professio-fidei-concilio-tridentino-lat_1562.txt`** (the patriarch Abdisho IV's profession of faith, 1562, bucket: the Schism of 1552). After the window. Not proposed.
- **Malabar world (V.23).** Assemani III.1 is shared with it, since the 1504 letter and the bishops' history are there. The Lamy appendix also reports the three bishops ordained in 1504 and sent to India, the Dabek islands and China (file lines 29186 to 29196, in a two-column passage the OCR interleaves). Proposed in the cross-link rows: Bar Hebraeus III and Malech for V.23, since they name the Indian mission.
- **Mongol-era world (`church-of-the-east-under-the-mongols`).** The Budge and Chabot files are staged for it too, as its core record. That world has no bucket yet.

## 3. Verified acquisition leads

Every row was checked on archive.org this pass: item metadata read, year read, rights field read, text file present. "Vendored" means the file is now in `cic/texts/`.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Scriptorum veterum nova collectio e Vaticanis codicibus, tomus X | Angelo Mai (editor) | Mai (Latin) | 1838 | https://archive.org/details/bub_gb_eBGyokOPhwcC | pd-us-by-date; host licence Public Domain Mark 1.0; title page read | Metadata read; text file fetched (2.2 MB) and sampled at opening, middle and end, October 2026. Vendored. Another 1838 Google scan of the series (bub_gb_ssNAAAAAcAAJ, 2.2 MB) is listed on archive.org; its tome was not checked. |
| Bibliotheca Orientalis Clementino-Vaticana, tomus III pars 1 | Giuseppe Simone Assemani | none (Latin) | 1725 | https://archive.org/details/de-scriptoribus-syris-nestorianis | pd-us-by-date; title-page year read | Metadata read; text file fetched (2.7 MB) and sampled at opening, middle and end, October 2026. Vendored. The Digital Library of India copy india.history.resource.71763 (2.75 MB) was compared and has the same OCR quality. |
| The Monks of Kublai Khan, Emperor of China | Syriac life | E. A. Wallis Budge | 1928 | https://archive.org/details/monksofkublaikha0000unse | pd-us-by-date (published 1930 or earlier); 'First published in 1928' read on the title page | Metadata read; text file fetched (486 KB) and sampled at opening, middle and end, October 2026. Vendored. Two other scans (0000eawa and 0000eawa_y9c1) were opened and not used. |
| Histoire de Mar Jabalaha III et du moine Rabban Çauma | Syriac life | J.-B. Chabot | 1895 | https://archive.org/details/histoiredemarja00chab | pd-us-by-date; title-page year read | Metadata read; text file fetched (937 KB) and sampled at opening, middle and end, October 2026. Vendored. |
| Cathay and the Way Thither, vol. III | Yule and Cordier | Yule, revised by Cordier | 1914 | https://archive.org/details/cathaywaythither03yule | pd-us-by-date; 'issued for 1914' read | Metadata read; text file fetched (738 KB) and sampled, October 2026. Vendored; shared with V.23 and the Mongol-era world. |
| The Nestorians and their Rituals (2 vols) | George Percy Badger | Badger | 1852 | https://archive.org/details/nestorianstheirr0001badg and https://archive.org/details/nestorianstheirr0002badg (also bub_gb_Oo8AAAAAcAAJ, Public Domain Mark) | pd-us-by-date; 1852 | Metadata read; text files present (1.03 MB and 1.07 MB); not fetched, October 2026. Not vendored: a mid-nineteenth-century traveller's account of the Hakkari church, well after the window. A candidate if Doc_02 wants an outside picture of the survivors and their hereditary patriarchate. |
| The Bondage and Travels of Johann Schiltberger | Johann Schiltberger | J. Buchan Telfer | 1879 | https://archive.org/details/bondagetravelsof00schirich | pd-us-by-date; host NOT_IN_COPYRIGHT | Metadata read; text file fetched (697 KB) and word-counted, October 2026. Not vendored: a Bavarian captive in Timur's army, 1402 to 1427; the notes mention the Nestorians a dozen times but the church is not his subject. |
| Narrative of the Embassy of Ruy Gonzalez de Clavijo to the Court of Timour, 1403–6 | Ruy González de Clavijo | Clements R. Markham | 1859 | https://archive.org/details/narrativeembass00markgoog | pd-us-by-date; host NOT_IN_COPYRIGHT | Metadata read; text file fetched (487 KB) and word-counted, October 2026. Not vendored: an embassy to Timur's court; the Christians it meets are Armenians and Georgians, almost none Nestorian. |
| Histoire de Timur-Bec (Pétis de la Croix's French of Sharaf al-Din Yazdi's Zafarnama, 4 volumes) | Sharaf al-Din 'Ali Yazdi | F. Pétis de la Croix | 1722 | https://archive.org/details/histoiredetimur00yazdgoog (and 01, 02, 03yazdgoog) | pd-us-by-date; host NOT_IN_COPYRIGHT | Metadata read; four text files fetched (374 KB to 694 KB) and sampled, October 2026. Not vendored: the standard court narrative of Timur's wars in an eighteenth-century French, but the OCR is poor (long s as f, many broken words; zero hits for Mardin and Mosul). |
| Catalogue of Syriac Manuscripts in the British Museum acquired since 1838 (3 volumes) | William Wright | Wright | 1870–72 | https://archive.org/details/catalogueofsyria01brituoft and https://archive.org/details/catalogueofsyria03brituoft | pd-us-by-date; host NOT_IN_COPYRIGHT | Metadata read; text files present (1.3 MB each); not fetched, October 2026. Not vendored: a catalogue whose colophons could supply the scribes' names the census mentions. A candidate for a colophon pass, not read. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Bedjan, Histoire de Mar Jabalaha (1888) and Histoire de Mar Jabalaha, de trois autres patriarches (1895) | The Syriac original of the life of Yahballaha III. | Searched several ways on archive.org; no Bedjan volume found. Syriac OCR would be unusable even if found. Budge's English and Chabot's French are vendored. |
| `histoire-de-mar-yahballaha-et-rabban-sauma` (archive.org, 820 KB, no year or rights field) | A second upload of Chabot's translation. | Not opened. The host record carries no date; Chabot 1895 is vendored from an item with a dated title page. |
| Assemani, Bibliotheca Orientalis, other volumes and scans (BO I, BO II, the Beth Mardutho copy of III.2) | More of the same collection. | III.1 and III.2 hold the Nestorian material. Volume I and II concern other churches. |
| Wigram, The Cradle of Mankind: Life in Eastern Kurdistan (1914; several items, for example cu31924028549925, 830 KB) | The Anglican missionary's account of the Hakkari highlands. | A travel and ethnography book of the 1900s. Out of the window by five centuries. Not vendored; Wigram's 1929 history is already in the bucket. |
| Mai, Scriptorum veterum, other tomes | Mai's collection also has Eastern texts. | Only tomus X carries the synod of Timothy II. The others were not opened. |
| Michael the Syrian, Chabot 1899–1910 | A Syriac Orthodox chronicle with Nestorian news. | Ends in 1196, before the window. Already on the shelf. |
| The 1318 synod in English | A public-domain English translation of the canons. | None found. The Latin of Mai (1838) is the only public-domain rendering located. |

## 5. Open cross-world questions

- **The Mongol-era world (`church-of-the-east-under-the-mongols`, c. 1220–1317).** The Budge and Chabot lives and Yule's Cathay vol. III are its core record and V.17's antecedent. The census treats them as separate worlds at the 1317 boundary. How the library files each is a mapping question; both are staged for both.
- **The Malabar world (V.23).** The Indian province is "the one Timur never reached", so each world reads the other. Which world owns Assemani III.1, Mingana and the 1504 letter is for Step 0 on both to settle.
- **The Schism of 1552 world (`church-of-the-east-schism-of-1552`, 1517–1650).** The Hakkari patriarchate that became hereditary is the same line, and Assemani III.2, Bar Hebraeus III and Malech are in both buckets. Where the boundary of the two worlds falls is not decided here.
- **The Chaldean consolidation world (1815–1906).** The Scher catalogue and Malech are in that bucket as well.
- **The Armenian Cilicia worlds.** Timur's campaigns and the Cilician kingdom's end overlap. Not examined.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says "No question — the same communion this church has always been in". Nothing found disturbs that. I did not read Mai's synod acts through for Christology; the canons of an Eastern synod will touch christological language, and Doc_01 should read them for it. The Church of the East's historic christological position is not a question the census raises for this window.

**Sourcing (B1).** The census says "Thin and partly late", and that is right. What the library holds: one synod of 1318 in Latin translation, the life of Yahballaha III in English and French (ending at his death), an eighteenth-century catalogue of writers and patriarchs, a modern editor's succession list, a few colophons, and two twentieth-century histories. What it does not hold: any first-person record of Timur's campaigns from the church's side, any text from the Hakkari century in the church's own voice, or an English translation of the synod. The outside accounts of Timur in the library (Schiltberger, Clavijo, Pétis de la Croix) say little about the church.

**Ecology (B2).** One voice, then silence. The church is heard in the opening years, speaks about itself in canon-law terms, and then reaches the reader through other people's lists. A Representative would speak as a patriarch or bishop of the 1310s, not as a member of the Hakkari remnant. That is a screen risk to name in Doc_02.

**Uniqueness (B3).** Against the Mongol-era world the difference is the catastrophe. Against the Malabar world the difference is the place. Against the Schism of 1552 world the difference is the window. Each overlap is a boundary to state.

**Audiences (B4).** The Assyrian Church of the East and the Chaldean Catholic Church run to the present and are reachable. The audience is real but small and dispersed.

**Scale (B5).** About 7.1 MB vendored in five files, of which Assemani III.1 and Mai X are the two largest. Five further leads are listed in section 3 as not vendored.

**Recommendation: open question.** The library speaks in the church's own voice in only two places, the life of Yahballaha III (which ends in 1317) and the acts and canons of Timothy II's synod (Latin, 1318). The century and a half after the synod is covered by lists and by outsiders. A project lead has to decide whether a world can open with one synod and run on a succession list, or whether the Hakkari remnant is a gap to keep on the atlas. The fastest ways to settle it are to read Mai's synod acts for the church's actual concerns in 1318 and to read the colophon evidence (Scher, Wright's catalogue) for what the scribes of the fifteenth century said about themselves. This is a recommendation for Mark to weigh, not a decision.
