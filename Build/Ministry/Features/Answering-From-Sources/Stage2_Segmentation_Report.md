# Stage 2 Segmentation Report: Library thread

Run of 2026-10-29T18:48:41Z (UTC). Code: `Sandbox/answering-library/`, git hash `f1fad6fd501fa6dc7452b9dcfe563bdbd483e75b`. Everything below is measured by that run over the union of the twelve built worlds' shelves (alx, cappadocian, desert, don, gallic, hal, ijc, lpc, pahc, rzg, syr, witt). No model call of any kind was made.

## 1. Run facts

| Item | Value |
|---|---|
| Files in the union | 338 (305 plain-text `.txt`, 33 `.xml`) |
| Bytes | 617,746,628 |
| Output | `out/passages/<file-stem>.jsonl` (one per file) and `out/manifest.json`, both in the gitignored `out/` directory of the `answering-library` package under `Sandbox/`, rebuilt by `python -m answering_library.run` |
| Passages written | 354,589 |
| Words in passages | 80,950,920 |
| Apparatus passages / words | 39,070 / 3,859,835 |
| Workers (processes) | 4 |
| Vocabulary pass (seconds) | 26.2 |
| Segmentation pass (seconds) | 291.1 |
| Whole run, wall clock (seconds) | 357.0 |
| Run started / finished (UTC) | 2026-10-29T18:42:43Z / 2026-10-29T18:48:41Z |

Words are whitespace-delimited tokens. The earlier planning figure of about 154M tokens was bytes divided by four; the measured word count is smaller because most of the bytes are multi-byte Greek and markup.

Passage length (words), all passages:

| Band | Passages | Share |
|---|---|---|
| under 150 | 77,535 | 21.9% |
| 150 to 400 | 277,054 | 78.1% |
| over 400 | 0 | 0.0% |

Passages under 150 words are whole divisions shorter than 150 words (a passage never crosses a division). No passage exceeds 400 words.

## 2. Headline: how many plain-text files segment by script

Class definitions (measured per file, thresholds in `manifest.json` under `parameters`):

- **clean**: divisions found by visible markers, at least 3, at most 10% of the marked words in divisions over 5,000 words, markers covering at least 80% of the text, numbering sequential (0.6 or better) in every numbered marker family, at least 80% of division addresses distinct, and not resting on all-caps headings alone. For markup files (ThML, TEI/EpiDoc) the file's own `div` structure is the marker, with at least 3 divisions, at most 10% oversize and at least 80% distinct addresses.
- **partial**: at least 2 divisions found, but one or more clean tests failed. The failed tests are listed per file in `manifest.json` (`not_clean_because`) and in the curation list below.
- **none**: no usable marker family (or one division). The file is cut into paragraph blocks addressed by line number.

**Caveat on `clean` (found 2026-10-31).** `clean` means the markers are many, sequential and not oversize. It does not mean the addresses are numbers the edition prints for its divisions. Two files measured and read by independent readers showed it: in `augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2` all 1,018 marker divisions are Migne column numbers or misreadings of them, and none of the 134 printed tractate heads is addressable; in `augustine_enarrationes-in-psalmos-lat_migne-pl36-37` only 22 of 151 psalm heads open a division and none is addressed by psalm number. Do not quote the clean count as proof that a division address is citable. The measured count of plain-text files the segmenter calls clean is 41 (the figure of 38 earlier came from subtracting the 30 markup `.txt` files from 68); their audit is in `Curation_Ledger.md`, section 'Audit of the clean plain-text files'.

| Class | Files | Share of files | Words | Share of words |
|---|---|---|---|---|
| clean | 68 | 22.3% | 11,894,482 | 18.6% |
| partial | 186 | 61.0% | 44,338,436 | 69.3% |
| none | 51 | 16.7% | 7,735,086 | 12.1% |
| all | 305 | 100% | 63,968,004 | 100% |

Reading the table: of the 305 plain-text files, **68 segment cleanly by script**, 186 segment in part and 51 have no usable markers. The files that need hand curation of some or all divisions (partial plus none) number **237 of 305** (77.7% of files, 81.4% of words). Every one of them was still cut into addressable passages (line-number loci or the partial scheme); the class says how far the division addresses can be trusted as citations, not whether passages exist.

Sensitivity: 47 of the partial files fail only because their sole marker family is all-caps headings. If all-caps headings were accepted as sufficient, clean would rise to 115 files and curation would fall to 190. The all-caps family is the least reliable one (it picks up running heads and OCR noise), so the strict figure is the headline.

Of the 305 `.txt` files, 30 carry TEI/EpiDoc markup inside the `.txt` (the `-tei.txt` editions and the Perseus-style Greek editions); they were read with the markup reader, and 30 are clean, 0 partial, 0 none. The remaining 275 are true plain text: clean 38, partial 186, none 51.

Comparison with the earlier survey figure (about 281 of 1,484 plain-text files, library-wide, needing hand curation, 19%): this measurement over the 305 union files finds 237 (77.7%) in partial or none, and 51 (16.7%) with no usable markers at all. The two figures measure different things (a different file set, and this run's partial class includes files whose markers are present but whose addresses repeat or whose divisions are very long), so they are not a like-for-like change; this run's numbers are the ones to use for the union.

Why files are not clean (a file can fail more than one test; markup files included):

| Test failed | Files |
|---|---|
| division addresses repeat | 91 |
| oversize divisions hold more than 10% of marked text | 79 |
| only all-caps headings | 64 |
| no divisions found | 51 |
| half the divisions are under 30 words | 16 |
| markers cover under 80% of the text | 5 |

## 3. By script and language class

Plain-text and TEI `.txt` files, grouped by the script and language that carry most of each file's words:

| Script | Language | Files | Clean | Partial | None | Words | Clean share of words |
|---|---|---|---|---|---|---|---|
| Latn | lat | 111 | 36 | 61 | 14 | 26,026,532 | 25.7% |
| Latn | eng | 98 | 12 | 60 | 26 | 13,679,266 | 17.4% |
| Grek | grc | 31 | 7 | 22 | 2 | 11,496,361 | 2.8% |
| Latn | fra | 35 | 9 | 23 | 3 | 8,001,481 | 25.1% |
| Latn | deu | 24 | 3 | 18 | 3 | 3,226,940 | 6.5% |
| Latn | swe | 4 | 1 | 2 | 1 | 1,380,446 | 20.7% |
| Armn | und | 1 | 0 | 0 | 1 | 120,863 | 0.0% |
| Latn | gmh | 1 | 0 | 0 | 1 | 36,115 | 0.0% |

Scripts present in the whole union, by passage words:

| Script | Words | Share |
|---|---|---|
| Latn | 69,277,068 | 85.6% |
| Grek | 11,525,424 | 14.2% |
| Armn | 120,505 | 0.1% |
| Zyyy | 27,421 | 0.0% |
| Hebr | 502 | 0.0% |

Latn is Latin script (English, Latin, French, German and the other Latin-script languages), Grek is Greek, Armn is Armenian, Hebr is Hebrew, Zyyy is text with no letters. No Cyrillic, Syriac, Arabic or Ethiopic script was found in any passage of the union: the Syriac, Arabic and Ethiopic works in the union are present as Latin-script editions or translations. The Russian-language file in the library at large is not on any of the twelve shelves.

Passage language, by words (from the filename code, per passage choice among the codes in the name; files with no code are English unless stopword counts show another Latin-script language clearly dominating):

| Language | Words | Share |
|---|---|---|
| eng | 30,612,955 | 37.8% |
| lat | 25,838,278 | 31.9% |
| grc | 11,525,424 | 14.2% |
| fra | 8,245,246 | 10.2% |
| deu | 3,160,532 | 3.9% |
| swe | 1,383,942 | 1.7% |
| und | 148,428 | 0.2% |
| gmh | 36,115 | 0.0% |

Language source per file: filename code 186, default English 127, inferred from stopwords 25. The inferred files are listed in `manifest.json` (`language_source`, `language_codes`).

## 4. Per world

A file shared by several worlds is counted once in each world that claims it, so the world rows add up to more than the union.

| World | Files | of which .txt | Passages | Words | .txt files clean/partial/none | .txt word share clean/partial/none |
|---|---|---|---|---|---|---|
| alx | 36 | 25 | 56,588 | 13,189,856 | 2/18/5 | 13.5% / 69.3% / 17.2% |
| cappadocian | 37 | 30 | 52,137 | 12,504,221 | 3/21/6 | 1.9% / 96.0% / 2.1% |
| desert | 17 | 10 | 20,765 | 4,766,177 | 0/6/4 | 0.0% / 73.5% / 26.5% |
| don | 34 | 29 | 45,332 | 9,393,891 | 10/17/2 | 26.7% / 63.1% / 10.2% |
| gallic | 8 | 5 | 9,331 | 1,866,631 | 0/3/2 | 0.0% / 94.7% / 5.3% |
| hal | 11 | 4 | 18,512 | 4,159,476 | 0/1/3 | 0.0% / 12.3% / 87.7% |
| ijc | 58 | 42 | 80,532 | 19,186,950 | 7/28/7 | 19.7% / 71.9% / 8.4% |
| lpc | 112 | 101 | 116,116 | 26,434,846 | 35/54/12 | 28.3% / 59.9% / 11.8% |
| pahc | 35 | 25 | 45,467 | 10,195,802 | 8/13/4 | 17.0% / 59.2% / 23.8% |
| rzg | 42 | 42 | 42,885 | 9,483,393 | 8/29/5 | 25.5% / 64.6% / 9.9% |
| syr | 27 | 18 | 32,297 | 7,318,909 | 3/12/3 | 15.7% / 52.2% / 32.1% |
| witt | 28 | 28 | 18,708 | 4,209,755 | 4/14/10 | 12.7% / 53.6% / 33.7% |

## 5. Hand-curation list

All 237 plain-text files whose class is partial or none, largest first (size in megabytes of the source file). The reasons column gives the tests failed; for none files it is the absence of any usable marker family.

| File | MB | Words | Class | Why not clean | Marker families used (n) | Worlds |
|---|---|---|---|---|---|---|
| `amphilochius-iconium_opera-pg39-grc-lat_migne1858.txt` | 9.91 | 919,665 | partial | only all-caps headings | caps:1422 | cappadocian |
| `basil_opera-omnia-pg31-grc-lat_migne1857.txt` | 9.46 | 845,189 | partial | only all-caps headings | caps:1893 | cappadocian |
| `augustine_sermones-ad-populum-lat_migne-gaume1841-t5.txt` | 9.41 | 1,280,238 | partial | division addresses repeat | numtitle:1904, kw:chapter:1594 | lpc |
| `basil_opera-omnia-pg29-grc-lat_migne1857.txt` | 8.50 | 783,444 | partial | only all-caps headings | caps:1063 | cappadocian |
| `athanasius_opera-omnia-pg26-grc-lat_migne1857.txt` | 8.32 | 774,888 | partial | only all-caps headings | caps:851 | alx,ijc |
| `gregory-nyssa_opera-omnia-pg44-grc-lat_migne1858.txt` | 7.74 | 682,809 | partial | only all-caps headings | caps:693 | cappadocian |
| `gregory-nazianzen_orationes-27-45-pg36-grc-lat_migne1858.txt` | 7.60 | 692,414 | partial | only all-caps headings | caps:747 | cappadocian |
| `athanasius_opera-omnia-pg25-grc-lat_migne1857.txt` | 7.50 | 677,981 | partial | only all-caps headings | caps:1023 | alx,ijc |
| `gregory-nyssa_opera-omnia-pg45-grc-lat_migne1858.txt` | 7.28 | 640,830 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:534 | cappadocian |
| `gregory-nazianzen_epistulae-carmina-pg37-grc-lat_migne1857.txt` | 7.22 | 653,547 | partial | only all-caps headings | caps:1360 | cappadocian |
| `gregory-nyssa_opera-omnia-pg46-grc-lat_migne1863.txt` | 6.71 | 605,892 | partial | only all-caps headings | caps:783 | cappadocian |
| `gregory-nazianzen_orationes-pg35-grc-lat_migne1857.txt` | 6.24 | 601,361 | partial | only all-caps headings | caps:636 | cappadocian |
| `epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt` | 6.06 | 542,236 | partial | only all-caps headings | caps:541 | cappadocian |
| `john-chrysostom_opera-pg47-palladius-dialogus-grc-lat_migne1863.txt` | 5.51 | 507,876 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:454 | desert |
| `crespin_histoire-des-martyrs-t3-fra_benoit-lelievre1889.txt` | 5.32 | 787,391 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:101, caps:440, numtitle:363 | rzg |
| `augustine_sermones-1-340-lat_migne-pl38.txt` | 5.27 | 745,026 | partial | division addresses repeat | numtitle:850, kw:chapter:1668 | lpc |
| `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` | 5.10 | 702,434 | partial | oversize divisions hold more than 10% of marked text | caps:530, bare:roman:402 | don,lpc |
| `john-chrysostom_opera-pg52-epistulae-grc-lat_migne1862.txt` | 5.10 | 462,329 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:495 | ijc |
| `marius-mercator_opera-omnia-lat_migne-pl48.txt` | 4.84 | 637,510 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:748 | ijc |
| `josephus_works-antiquities-wars-life_whiston1859.txt` | 4.70 | 834,481 | none | no divisions found | - | alx,pahc,syr |
| `mansi_sacrorum-conciliorum-collectio-tomus-5-431-441-lat_welter-facsimile1901.txt` | 4.25 | 694,564 | partial | only all-caps headings | caps:1100 | ijc |
| `augustine_epistulae-maurist-order-lat_migne-pl33.txt` | 4.24 | 587,627 | partial | division addresses repeat | kw:chapter:351, numtitle:1552 | lpc |
| `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt` | 4.00 | 570,866 | partial | division addresses repeat | bare:arabic:1509 | don,lpc |
| `tertullian_quae-supersunt-t2-polemica-lat_oehler1853.txt` | 3.98 | 526,455 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:401 | pahc |
| `hilary_opera-tomus-posterior-de-synodis-contra-constantium-fragmenta-historica-lat_migne-pl10-1844.txt` | 3.94 | 526,694 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:316 | ijc |
| `mansi_sacrorum-conciliorum-collectio-tomus-3-347-409-lat_welter-facsimile1901.txt` | 3.81 | 594,481 | partial | only all-caps headings | caps:1117 | lpc |
| `augustine_sermones-341-396-et-appendix-lat_migne-pl39.txt` | 3.65 | 547,712 | partial | division addresses repeat | numtitle:1510 | lpc |
| `mansi_sacrorum-conciliorum-collectio-tomus-7-451-492-lat_welter-facsimile1901.txt` | 3.64 | 574,888 | partial | only all-caps headings | caps:1292 | ijc |
| `theodosianus-16_mommsen-meyer1905.txt` | 3.55 | 463,602 | partial | only all-caps headings | caps:1934 | cappadocian,don,ijc |
| `npnf205_gregory-nyssa-dogmatic-treatises.txt` | 3.49 | 541,946 | partial | oversize divisions hold more than 10% of marked text; half the divisions are under 30 words | bracket:2872 | cappadocian |
| `didymus-alexandria_de-trinitate-lat-grc_mingarelli1769.txt` | 3.29 | 513,853 | partial | division addresses repeat | kw:chapter:139, caps:250, numtitle:1165 | alx |
| `zurich-council_actensammlung-zuercher-reformation-deu_egli1879.txt` | 3.25 | 455,157 | partial | division addresses repeat | bare:arabic:883 | rzg |
| `augustine_sermones-inediti-lat_caillau1842.txt` | 3.22 | 497,625 | partial | division addresses repeat | caps:387, numtitle:1144 | lpc |
| `beza_histoire-ecclesiastique-t2-fra_baum-cunitz1884.txt` | 3.01 | 430,914 | partial | division addresses repeat | numtitle:1277 | rzg |
| `beza_histoire-ecclesiastique-t1-fra_baum-cunitz1883.txt` | 2.99 | 424,177 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:9, numpara:626, kw:article:11 | rzg |
| `epiphanius_panarion-haer-48-69-corpus-haereseologicum-t2-pars-posterior-grc-lat_oehler1860.txt` | 2.97 | 380,722 | partial | only all-caps headings | caps:373 | alx |
| `patrologia-orientalis-tomus16_synaxaire-arabe-jacobite-barmahat-bachons-synaxaire-armenien-tre-fra_graffin-nau1922.txt` | 2.92 | 388,089 | partial | division addresses repeat | numtitle:426, numpara:621 | alx |
| `brandt_history-of-the-reformation-in-the-low-countries-v3_1722.txt` | 2.74 | 518,407 | none | no divisions found | - | rzg |
| `beza_histoire-ecclesiastique-t3-fra_baum-cunitz-reuss1889.txt` | 2.72 | 379,238 | partial | division addresses repeat | numpara:820 | rzg |
| `sozomen_historia-ecclesiastica-tomus2-libri-5-9-grc-lat_hussey1860.txt` | 2.71 | 285,263 | partial | only all-caps headings | caps:812 | cappadocian,ijc |
| `cil8-supplementum-numidiae_cagnat-schmidt1894.txt` | 2.69 | 444,754 | none | no divisions found | - | don |
| `chronica-minora-liber-genealogus_mommsen1892.txt` | 2.62 | 345,520 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat; half the divisions are under 30 words | numpara:1278, numtitle:1197 | don |
| `gsell_inscriptions-latines-de-lalgerie-tome1-proconsulaire-fra-lat_1922.txt` | 2.61 | 388,979 | none | no divisions found | - | lpc |
| `niemeyer_collectio-confessionum-lat_niemeyer1840.txt` | 2.59 | 339,965 | partial | oversize divisions hold more than 10% of marked text | caps:364, bare:roman:180 | rzg,witt |
| `book-of-concord_symbolical-books-evangelical-lutheran-church_jacobs1911.txt` | 2.39 | 372,297 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | kw:chapter:92, kw:article:114, numtitle:670 | witt |
| `augustine_sermones-post-maurinos-reperti-lat_morin1930.txt` | 2.36 | 366,874 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:533 | lpc |
| `gerlach_tage-buch-deu_1674.txt` | 2.31 | 403,088 | none | no divisions found | - | witt |
| `monumenta-fidei-ecclesiae-orientalis_confessions-grc-lat_kimmel1850.txt` | 2.26 | 271,341 | partial | division addresses repeat | numtitle:651 | rzg |
| `epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` | 2.26 | 241,411 | partial | division addresses repeat | numtitle:148, caps:317 | alx |
| `hefele_conciliengeschichte-bd1-deu_2e-aufl1873.txt` | 2.21 | 322,596 | partial | division addresses repeat | caps:88, numtitle:1767 | ijc |
| `prosper_chronica-minora-1-lat_mommsen1892.txt` | 2.20 | 345,654 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numpara:1287 | don,lpc |
| `monceaux_histoire-litteraire-afrique-chretienne-tomes6-7-fra_1922-1923.txt` | 2.18 | 297,793 | partial | division addresses repeat | bare:roman:43, numpara:653 | don,lpc |
| `rufinus-aquileia_origenes-werke-bd7-homilien-numeri_baehrens1921.txt` | 1.94 | 302,354 | partial | division addresses repeat | numtitle:263, caps:202 | alx |
| `lucifer-cagliari_opuscula-lat_hartel1886-csel14.txt` | 1.87 | 263,542 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:161, bare:roman:149 | alx,ijc |
| `benson_cyprian-his-life-his-times-his-work_1897.txt` | 1.85 | 267,697 | partial | oversize divisions hold more than 10% of marked text | kw:chapter:24, bare:roman:61, caps:234 | lpc |
| `augustine_epistulae-1-123-lat_goldbacher-csel34.txt` | 1.84 | 315,334 | partial | oversize divisions hold more than 10% of marked text | bare:roman:103, numtitle:21 | lpc |
| `tatian_oratio-ad-graecos-grc-lat_otto1851.txt` | 1.81 | 225,636 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numpara:1516 | pahc,syr |
| `codex-theodosianus_latinlibrary.txt` | 1.78 | 240,192 | none | no divisions found | - | don,ijc,lpc |
| `augustine_opera-sect-v-pars-iii-lat_zycha1900-csel41.txt` | 1.78 | 252,695 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:221 | lpc |
| `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt` | 1.78 | 301,236 | none | no divisions found | - | lpc |
| `suetonius_lives-of-the-caesars-loeb_rolfe1914.txt` | 1.76 | 279,988 | partial | division addresses repeat | caps:239, numtitle:1065 | pahc |
| `tertullian_opera-pars3-lat_kroymann-csel47.txt` | 1.76 | 236,220 | none | no divisions found | - | pahc |
| `libri-symbolici-ecclesiae-orientalis_confessions-grc-lat_kimmel1843.txt` | 1.75 | 207,088 | partial | division addresses repeat | numtitle:715 | rzg |
| `augustine_de-fide-et-symbolo-de-opere-monachorum-et-al-lat_zycha-csel41.txt` | 1.74 | 257,080 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:240, bare:roman:70 | lpc |
| `ribbeck_donatus-und-augustinus-erste-haelfte-deu_1857.txt` | 1.72 | 227,009 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | caps:31, numtitle:124 | don,lpc |
| `arndt_true-christianity_boehm-schaeffer1868.txt` | 1.70 | 304,625 | partial | division addresses repeat | section:43, numtitle:1431 | witt |
| `monceaux_histoire-litteraire-afrique-chretienne-tome4_1912.txt` | 1.69 | 227,402 | partial | division addresses repeat; half the divisions are under 30 words | caps:98, numtitle:2278 | don |
| `eusebius_werke-bd2-2-historia-ecclesiastica-vi-x-rufinus-x-xi-grc-lat_schwartz-mommsen1908.txt` | 1.62 | 187,565 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:178 | alx,ijc |
| `origen_commentarii-in-evangelium-joannis-tomus2-grc_lommatzsch1832.txt` | 1.60 | 173,261 | partial | division addresses repeat | numtitle:1595 | alx |
| `augustine_epistulae-124-184a-lat_goldbacher-csel44.txt` | 1.60 | 280,128 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:61 | lpc |
| `zurich-letters_first-series-1558-1579_robinson1842.txt` | 1.57 | 223,753 | partial | division addresses repeat | kw:letter:258, bare:roman:60 | rzg |
| `philo_works-v3_yonge1854.txt` | 1.55 | 236,041 | partial | division addresses repeat | numtitle:358 | alx,pahc,syr |
| `socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt` | 1.55 | 178,754 | partial | only all-caps headings | caps:388 | ijc |
| `monceaux_histoire-litteraire-afrique-chretienne-tome3_1905.txt` | 1.54 | 246,968 | partial | division addresses repeat; half the divisions are under 30 words | caps:143, numtitle:3357 | lpc |
| `philo_works-v1_yonge1854.txt` | 1.53 | 234,390 | partial | division addresses repeat | numtitle:538 | alx,pahc,syr |
| `ammianus-marcellinus_roman-history_yonge1862.txt` | 1.51 | 264,201 | partial | only all-caps headings | caps:416 | ijc |
| `philo_works-v2_yonge1854.txt` | 1.50 | 230,988 | partial | division addresses repeat | numtitle:413 | alx,pahc,syr |
| `evagrius-scholasticus_historia-ecclesiastica-grc_bidez-parmentier1898.txt` | 1.50 | 154,655 | none | no divisions found | - | ijc |
| `monceaux_histoire-litteraire-afrique-chretienne-tome1_1901.txt` | 1.49 | 238,916 | partial | only all-caps headings | caps:319 | lpc |
| `calvin_institutes-christian-religion-vol2_beveridge1845.txt` | 1.49 | 262,906 | partial | division addresses repeat | numtitle:834 | rzg |
| `faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt` | 1.49 | 200,360 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:131 | gallic |
| `acta-et-scripta-wirtembergensium_jeremias-ii-correspondence-lat_1584.txt` | 1.47 | 257,479 | partial | only all-caps headings | caps:570 | witt |
| `augustine_civitate-dei-14-22-lat_hoffmann-csel40-2.txt` | 1.46 | 244,160 | none | no divisions found | - | lpc |
| `calvin_institutes-christian-religion-vol1_beveridge1845.txt` | 1.42 | 246,693 | partial | division addresses repeat | bare:roman:21, numtitle:752 | rzg |
| `suetonius_lives-of-the-twelve-caesars_thomson-forester1909.txt` | 1.40 | 233,480 | partial | oversize divisions hold more than 10% of marked text | caps:34, numtitle:552 | pahc |
| `calvin_commentaries-genesis-vol1_king1847.txt` | 1.39 | 240,887 | partial | division addresses repeat; half the divisions are under 30 words | caps:191, numtitle:1433 | rzg |
| `calvin_commentaries-genesis-vol2_king1847.txt` | 1.38 | 242,538 | partial | only all-caps headings | caps:396 | rzg |
| `augustine_civitate-dei-1-13-lat_hoffmann-csel40-1.txt` | 1.36 | 220,201 | none | no divisions found | - | lpc |
| `mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912.txt` | 1.36 | 192,982 | none | no divisions found | - | lpc |
| `mesnage_afrique-chretienne-eveches-ruines-fra_1912.txt` | 1.35 | 191,310 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:311 | lpc |
| `duchesne_histoire-ancienne-de-leglise-tome3-fra_2e-ed1910.txt` | 1.33 | 182,417 | partial | only all-caps headings | caps:257 | lpc |
| `augustine_epistulae-critical_goldbacher-csel57-pars4.txt` | 1.33 | 229,912 | none | no divisions found | - | lpc |
| `augustine_augustinus-postille-auswahl-reden-kirchenjahr-deu_1861.txt` | 1.32 | 206,457 | partial | division addresses repeat | numtitle:536 | lpc |
| `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` | 1.32 | 221,295 | none | no divisions found | - | lpc |
| `collectio-avellana_epistulae-imperatorum-pontificum-pars1-lat_guenther1895-csel35.txt` | 1.31 | 190,454 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numpara:69, kw:chapter:50 | ijc |
| `turner_ecclesiae-occidentalis-monumenta-iuris-antiquissima-tom1-fasc1-lat_1899.txt` | 1.29 | 204,540 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:172 | lpc |
| `timothy-aelurus_widerlegung-der-lehre-von-chalcedon-xcl_ter-mekerttschian-ter-minassiantz1908.txt` | 1.27 | 120,863 | none | no divisions found | - | ijc |
| `apologists-fragmentary_reliquiae-corpus-apologetarum-vol9-grc-lat_otto1872.txt` | 1.27 | 170,136 | partial | division addresses repeat | numtitle:359 | pahc |
| `hefele_history-of-the-councils-v3-431-451_clark1883.txt` | 1.24 | 202,894 | partial | oversize divisions hold more than 10% of marked text | kw:part:75, caps:252, kw:canon:34 | ijc |
| `augustine_erorterungen-zum-johannis-evangelium-teil2-deu_hayd-bkv1878.txt` | 1.24 | 195,187 | partial | division addresses repeat | numtitle:951 | lpc |
| `olavus-petri_samlade-skrifter-v1-swe_hesselman1914.txt` | 1.20 | 195,532 | partial | oversize divisions hold more than 10% of marked text | numtitle:21, caps:80 | witt |
| `origen_commentarii-in-evangelium-matthaei-tomus3-grc-lat_lommatzsch1834.txt` | 1.19 | 120,807 | none | no divisions found | - | alx |
| `olavus-petri_samlade-skrifter-v2-swe_hesselman1915.txt` | 1.18 | 196,472 | none | no divisions found | - | witt |
| `gelasius-cyzicus_kirchengeschichte-historia-concilii-nicaeni-grc_loeschcke-heinemann1918.txt` | 1.17 | 120,985 | partial | oversize divisions hold more than 10% of marked text | caps:119, numtitle:58 | ijc |
| `apologists-fragmentary_reliquiae-sacrae-vol1-lat-grc_routh1846.txt` | 1.16 | 152,423 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:37 | pahc |
| `codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt` | 1.13 | 174,002 | partial | division addresses repeat | numpara:475 | don,lpc |
| `boyd_ecclesiastical-edicts-theodosian-code_1905.txt` | 1.12 | 159,173 | partial | oversize divisions hold more than 10% of marked text | kw:chapter:46, caps:152, numtitle:77 | don |
| `calvin_letters-vol4_bonnet1858.txt` | 1.11 | 195,242 | partial | only all-caps headings | caps:305 | rzg |
| `calvin_letters-vol1_bonnet1858.txt` | 1.11 | 195,870 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:215 | rzg |
| `duchesne_histoire-ancienne-de-leglise-tome1-fra_3e-ed1907.txt` | 1.10 | 149,429 | partial | only all-caps headings | caps:158 | lpc |
| `socrates_historia-ecclesiastica-tomus2-grc-lat_hussey1853.txt` | 1.09 | 122,473 | partial | only all-caps headings | caps:305 | ijc |
| `monceaux_histoire-litteraire-afrique-chretienne-tome5_1920.txt` | 1.07 | 146,023 | partial | division addresses repeat | bare:roman:23, numpara:326 | don |
| `harnack_mission-und-ausbreitung-des-christentums-band2-deu_2e-aufl1906.txt` | 1.06 | 138,459 | none | no divisions found | - | lpc |
| `theophilus_ad-autolycum-grc-lat_otto1861.txt` | 1.05 | 164,648 | partial | division addresses repeat | numpara:898 | pahc |
| `michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` | 1.05 | 175,093 | partial | division addresses repeat | numpara:442 | ijc |
| `calvin_letters-vol2_bonnet1858.txt` | 1.04 | 185,374 | partial | only all-caps headings | caps:274 | rzg |
| `cyprian_oeuvres-completes-tome1-traites-fra_guillon1837.txt` | 1.04 | 155,448 | partial | oversize divisions hold more than 10% of marked text | bare:roman:20, caps:91, kw:chapter:147 | lpc |
| `origen_commentarii-in-evangelium-matthaei-tomus4-grc-lat_lommatzsch1834.txt` | 1.04 | 131,148 | partial | division addresses repeat; half the divisions are under 30 words | numtitle:1039 | alx |
| `koch_cyprianische-untersuchungen-deu_1926.txt` | 1.03 | 153,719 | partial | division addresses repeat | numtitle:501 | lpc |
| `monceaux_histoire-litteraire-afrique-chretienne-tome2_1902.txt` | 1.03 | 166,307 | partial | division addresses repeat; half the divisions are under 30 words | numtitle:1165 | lpc |
| `dales_theologie-de-saint-cyprien-fra_1922.txt` | 1.00 | 156,659 | partial | division addresses repeat | caps:196, numtitle:777 | lpc |
| `gregory-great_epistolae-selectae_turchi1907.txt` | 1.00 | 140,461 | partial | only all-caps headings | caps:267 | don |
| `zwingli_latin-works-correspondence-vol3_heller1929.txt` | 0.97 | 172,109 | partial | oversize divisions hold more than 10% of marked text | bracket:28 | rzg |
| `augustine_confessiones-lat_knoll-csel33.txt` | 0.96 | 169,301 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:112 | lpc |
| `optatus_libri-vii-critical_ziwsa1893.txt` | 0.96 | 162,313 | partial | division addresses repeat | bare:roman:109, caps:67 | don |
| `hilary_collectanea-antiariana-parisina-fragmenta-historica-lat_feder1916-csel65.txt` | 0.95 | 151,201 | partial | division addresses repeat | numtitle:382 | ijc |
| `apollinaris-laodicea_fragmente-apollinaris-von-laodicea-und-seine-schule-grc-deu_lietzmann1904.txt` | 0.95 | 115,255 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:114 | cappadocian |
| `beza_job-expounded_legatt1589.txt` | 0.95 | 159,857 | partial | oversize divisions hold more than 10% of marked text | kw:chapter:30, caps:85 | rzg |
| `luther_works-v2-selected_jacobs-spaeth1916.txt` | 0.94 | 167,797 | none | no divisions found | - | witt |
| `origen_commentarii-in-epistolam-ad-romanos-libri-6-10-lat_lommatzsch1837.txt` | 0.92 | 152,290 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:42 | alx |
| `luther_works-v3-selected_various1930.txt` | 0.91 | 159,880 | none | no divisions found | - | witt |
| `jerome_eusebii-chronici-canones-lat_fotheringham1923.txt` | 0.91 | 160,429 | none | no divisions found | - | hal,ijc |
| `luther_works-v6-selected_various1932.txt` | 0.91 | 153,199 | none | no divisions found | - | witt |
| `nestorius_nestoriana-fragmenta-grc-lat-deu_loofs1905.txt` | 0.90 | 131,228 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:162, numpara:53 | ijc |
| `synod-of-dort_articles-with-history-of-events_scott1831.txt` | 0.90 | 133,527 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:arabic:28, caps:146, numtitle:274 | rzg |
| `anan-isho_paradise-v2-sayings_budge1907.txt` | 0.89 | 166,438 | partial | oversize divisions hold more than 10% of marked text | kw:chapter:11, numtitle:62 | desert,syr |
| `augustine_de-catechizandis-rudibus-lat-eng_christopher1926.txt` | 0.88 | 143,334 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat; markers cover under 80% of the text | numpara:849 | lpc |
| `luther_first-principles-reformation_wace-buchheim1885.txt` | 0.87 | 133,317 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:141 | witt |
| `justin-martyr_opera-addubitata-grc-lat_otto1879.txt` | 0.86 | 132,901 | partial | division addresses repeat | caps:149, numpara:945 | pahc |
| `basil_ascetic-works-longer-shorter-rules_clarke1925.txt` | 0.86 | 153,688 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:317, numtitle:199, numpara:33 | cappadocian |
| `goodspeed_aeltesten-apologeten-grc-lat-deu_1914.txt` | 0.85 | 137,743 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:117 | pahc |
| `council-of-ephesus-449_second-synod-of-ephesus-syriac-acts_perry1881.txt` | 0.84 | 138,197 | none | no divisions found | - | ijc |
| `kirk-of-scotland_book-of-common-order-and-westminster-directory_sprott-leishman1868.txt` | 0.81 | 140,735 | none | no divisions found | - | rzg |
| `ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-takhshash-yakatit_budge1928.txt` | 0.80 | 143,578 | partial | oversize divisions hold more than 10% of marked text; markers cover under 80% of the text | numtitle:26 | cappadocian |
| `luther_works-v1-selected_jacobs-spaeth1915.txt` | 0.80 | 141,690 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:6, numtitle:253, numpara:4 | witt |
| `luther_works-v4-selected_various1931.txt` | 0.79 | 140,943 | none | no divisions found | - | witt |
| `delehaye_passions-martyrs-genres-litteraires-fra_1921.txt` | 0.79 | 127,288 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:108 | lpc |
| `zwingli_latin-works-correspondence-vol2_hinke1922.txt` | 0.78 | 137,605 | none | no divisions found | - | rzg |
| `cyprian_oeuvres-completes-tome2-lettres-fra_guillon1837.txt` | 0.77 | 125,921 | none | no divisions found | - | lpc |
| `barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt` | 0.77 | 124,811 | partial | only all-caps headings | caps:249 | syr |
| `origen_commentarii-in-epistolam-ad-romanos-libri-1-5-lat_lommatzsch1836.txt` | 0.77 | 122,591 | none | no divisions found | - | alx |
| `gilles_histoire-ecclesiastique-eglises-vaudoises-v1-fra_1881.txt` | 0.76 | 108,736 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | kw:chapter:75 | rzg |
| `poschmann_abendlaendische-kirchenbusse-deu_1928.txt` | 0.75 | 109,665 | none | no divisions found | - | lpc |
| `augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869.txt` | 0.74 | 105,595 | partial | division addresses repeat | numtitle:183 | lpc |
| `origen_commentarii-in-evangelium-matthaei-tomus5-lat_lommatzsch1835.txt` | 0.70 | 107,041 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat; half the divisions are under 30 words | numtitle:773 | alx |
| `optatus_against-the-donatists.txt` | 0.70 | 123,097 | partial | half the divisions are under 30 words | caps:39, numtitle:81, numpara:1284 | don,ijc,lpc |
| `tyconius_liber-regularum_burkitt1894.txt` | 0.69 | 112,858 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:78, numpara:56 | don |
| `cyprian_ausgewaehlte-schriften-band1-deu_uhl-bkv1869.txt` | 0.67 | 101,149 | partial | division addresses repeat | numtitle:145 | lpc |
| `sulpicius-severus_libri-qui-supersunt-chronica-vita-martini-lat_halm1866-csel1.txt` | 0.67 | 107,116 | none | no divisions found | - | ijc |
| `council-of-ephesus-449_akten-der-ephesinischen-synode-449-deu_flemming-hoffmann1917.txt` | 0.67 | 88,976 | partial | only all-caps headings | caps:127 | ijc |
| `luther_bondage-of-the-will_cole1823.txt` | 0.67 | 117,268 | partial | oversize divisions hold more than 10% of marked text | bare:roman:12, caps:65, numtitle:5 | witt |
| `zwingli_latin-works-correspondence-vol1_jackson1912.txt` | 0.64 | 113,837 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:27, numtitle:124 | rzg |
| `vonsoden_cyprianische-briefsammlung-deu_1904.txt` | 0.64 | 104,123 | partial | division addresses repeat | numtitle:634 | lpc |
| `melanchthon_apology-augsburg-confession_bente-dau1921.txt` | 0.64 | 111,117 | partial | oversize divisions hold more than 10% of marked text | kw:part:37 | witt |
| `macarius_fifty-spiritual-homilies_mason1921.txt` | 0.64 | 117,591 | none | no divisions found | - | desert |
| `ephraim_prose-refutations_mitchell1912-1921.txt` | 0.64 | 118,297 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat; half the divisions are under 30 words | numpara:161 | syr |
| `zinzendorf_twenty-one-discourses-augsburg-confession_okely1753.txt` | 0.63 | 118,768 | partial | only all-caps headings | caps:290 | witt |
| `marot-beze_pseaumes-mis-en-rime-francoise-fra_1562.txt` | 0.62 | 105,346 | partial | only all-caps headings | caps:301 | rzg |
| `acta-martyrum-selecta_gebhardt1902.txt` | 0.60 | 65,693 | partial | oversize divisions hold more than 10% of marked text | bare:roman:20, caps:8 | lpc |
| `lauchert_kanones-altkirchlichen-concilien-lat-grc_1896.txt` | 0.59 | 81,673 | partial | division addresses repeat | bare:arabic:47, numtitle:488 | lpc |
| `zwingli_selected-works_jackson1901.txt` | 0.57 | 101,360 | none | no divisions found | - | rzg |
| `palladius_paradise-v1-syriac_budge1907.txt` | 0.55 | 100,835 | none | no divisions found | - | alx,desert,hal,syr |
| `koch_cathedra-petri-deu_1930.txt` | 0.54 | 81,403 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:71 | lpc |
| `toulotte_geographie-afrique-chretienne-numidie-fra_1894.txt` | 0.54 | 85,435 | partial | oversize divisions hold more than 10% of marked text | bare:arabic:28 | lpc |
| `liturgies-eastern_mark-james-clement-chrysostom-basil-malabar_neale-1870s.txt` | 0.53 | 80,783 | partial | only all-caps headings | caps:221 | cappadocian |
| `salvian_on-the-government-of-god_sanford1930.txt` | 0.53 | 91,548 | partial | division addresses repeat | numtitle:112 | gallic |
| `augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt` | 0.52 | 78,519 | partial | only all-caps headings | caps:143 | lpc |
| `bell_jews-christians-egypt-meletian-papyri_1924.txt` | 0.51 | 86,441 | partial | oversize divisions hold more than 10% of marked text | bracket:26, caps:128 | desert |
| `harris_odes-and-psalms-of-solomon_harris1911.txt` | 0.50 | 86,946 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:102 | syr |
| `origen_de-oratione-grc_koetschau1899.txt` | 0.50 | 53,617 | partial | division addresses repeat | numpara:83 | alx |
| `jeremias-ii_censura-orientalis-ecclesiae-lat_socolovius1582.txt` | 0.50 | 79,230 | none | no divisions found | - | witt |
| `palladius_dialogue-life-of-chrysostom_moore1921.txt` | 0.50 | 85,245 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat; half the divisions are under 30 words | numpara:6, numtitle:77 | ijc |
| `augustine_retractationes-lat_knoll-csel36.txt` | 0.49 | 87,757 | partial | oversize divisions hold more than 10% of marked text; half the divisions are under 30 words | kw:book:4, numtitle:66 | lpc |
| `rilliet_calvin-and-servetus_tweedie1846.txt` | 0.49 | 72,578 | partial | only all-caps headings | caps:152 | rzg |
| `koch_cyprian-und-der-roemische-primat-deu_1910.txt` | 0.49 | 63,750 | partial | division addresses repeat | numtitle:232 | lpc |
| `origen_philocalia_lewis1911.txt` | 0.47 | 85,158 | none | no divisions found | - | alx,cappadocian,desert,hal |
| `patrum-nicaenorum-nomina_subscription-lists-lat_gelzer-hilgenfeld-cuntz1898.txt` | 0.47 | 67,335 | partial | only all-caps headings | caps:212 | cappadocian,ijc |
| `yelverton_mass-in-sweden-lat-swe-eng_yelverton1920.txt` | 0.46 | 65,232 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | bare:roman:39, numtitle:93 | witt |
| `lucian_works-vol4-peregrine_fowler1905.txt` | 0.44 | 78,193 | partial | oversize divisions hold more than 10% of marked text | bare:roman:16, caps:43 | pahc |
| `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` | 0.43 | 64,574 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:42 | lpc |
| `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` | 0.41 | 62,214 | partial | division addresses repeat | numtitle:212 | lpc |
| `paulinus-milan_vita-ambrosii_kaniecka1928.txt` | 0.40 | 68,058 | partial | division addresses repeat | numtitle:246 | ijc |
| `cyril-alexandria_three-epistles-grc-eng_pusey1872.txt` | 0.38 | 57,031 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:91 | ijc |
| `possidius_vita-augustini_weiskotten1919.txt` | 0.33 | 54,959 | partial | oversize divisions hold more than 10% of marked text; markers cover under 80% of the text | kw:chapter:28 | lpc |
| `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` | 0.31 | 52,358 | partial | only all-caps headings | caps:100 | lpc |
| `aristides_apology-syriac-grc-eng_harris-robinson1893.txt` | 0.31 | 53,236 | none | no divisions found | - | pahc |
| `harnack_vita-cypriani-commentary-lat-deu_1913.txt` | 0.31 | 46,322 | partial | division addresses repeat | bare:arabic:13, numtitle:142 | lpc |
| `smith-thomas_collectanea-de-cyrillo-lucario-lat_1707.txt` | 0.30 | 44,383 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:58 | rzg |
| `egeria_pilgrimage-of-etheria_mcclure-feltoe1919.txt` | 0.29 | 45,034 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:75 | desert,syr |
| `dositheus_acts-and-decrees-synod-jerusalem_robertson1899.txt` | 0.27 | 45,855 | partial | oversize divisions hold more than 10% of marked text | kw:question:8, kw:chapter:23, numtitle:17 | rzg |
| `palladius_lausiac-history_clarke1918.txt` | 0.27 | 48,643 | partial | half the divisions are under 30 words | caps:35, numpara:250 | alx,desert,hal,syr |
| `luther_large-catechism_bente-dau1921.txt` | 0.27 | 48,425 | none | no divisions found | - | witt |
| `bardenhewer_geschichte-altkirchlichen-literatur-band2-cyprian-slice-deu_2e-aufl1914.txt` | 0.26 | 32,963 | partial | oversize divisions hold more than 10% of marked text; half the divisions are under 30 words | numtitle:94 | lpc |
| `morison_st-basil-and-his-rule_1912.txt` | 0.25 | 43,994 | none | no divisions found | - | cappadocian |
| `philostorgius_ecclesiastical-history_walford1855.txt` | 0.25 | 43,835 | partial | oversize divisions hold more than 10% of marked text | caps:38, numpara:114 | cappadocian,ijc |
| `monumenta-vetera-donatistarum-303-340_migne-pl8.txt` | 0.25 | 35,396 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:55 | don |
| `theologia-germanica_theologia-germanica_winkworth1893.txt` | 0.25 | 44,290 | partial | oversize divisions hold more than 10% of marked text | bare:roman:20, kw:chapter:43 | witt |
| `calvin_geneva-catechism_waterman1815.txt` | 0.21 | 38,160 | none | no divisions found | - | rzg |
| `theologia-germanica_theologia-deutsch-gmh_pfeiffer1851.txt` | 0.21 | 36,115 | none | no divisions found | - | witt |
| `luther_table-talk_bell1886.txt` | 0.19 | 33,548 | none | no divisions found | - | witt |
| `augustine_de-catechizandis-rudibus-lat_krueger1893.txt` | 0.19 | 27,543 | none | no divisions found | - | lpc |
| `danske-folkekirke_ordinatio-ecclesiastica-lat_vinitor1537.txt` | 0.19 | 29,134 | partial | oversize divisions hold more than 10% of marked text; only all-caps headings | caps:9 | witt |
| `gregory-nazianzen_first-invective-against-julian_king1888.txt` | 0.17 | 30,490 | none | no divisions found | - | cappadocian |
| `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` | 0.16 | 27,194 | partial | only all-caps headings | caps:29 | rzg |
| `luther_hymns_bacon-allen.txt` | 0.14 | 24,498 | partial | oversize divisions hold more than 10% of marked text; division addresses repeat | numtitle:418 | witt |
| `lucaris_confessio-and-synodal-censures-lat_1645.txt` | 0.12 | 22,813 | partial | only all-caps headings | caps:104 | rzg |
| `vonsoden_streit-rom-karthago-ketzertaufe-deu_1909.txt` | 0.12 | 15,874 | partial | only all-caps headings | caps:24 | lpc |
| `monumenta-vetera-donatistarum_migne-pl8.txt` | 0.11 | 14,578 | partial | only all-caps headings | caps:26 | don |
| `vonsoden_ketzertaufstreit-rom-karthago-deu_1909.txt` | 0.10 | 15,901 | partial | only all-caps headings | caps:24 | lpc |
| `calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt` | 0.10 | 17,459 | partial | only all-caps headings | caps:40 | rzg |
| `addai_doctrine-of-addai.txt` | 0.09 | 17,241 | partial | markers cover under 80% of the text | numpara:33 | syr |
| `hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907.txt` | 0.09 | 12,369 | partial | division addresses repeat | numpara:57 | lpc |
| `schaff_gallican-confession-fra-eng_1877.txt` | 0.09 | 13,126 | partial | division addresses repeat | caps:13, numtitle:62 | rzg |
| `gregory-nyssa_life-of-macrina_clarke1916.txt` | 0.08 | 14,188 | partial | only all-caps headings | caps:45 | cappadocian |
| `gregory-nazianzen_second-invective-against-julian_king1888.txt` | 0.07 | 13,088 | none | no divisions found | - | cappadocian |
| `hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt` | 0.07 | 10,719 | partial | only all-caps headings | caps:20 | gallic |
| `eucherius-lyon_de-contemptu-mundi_vaughan1654.txt` | 0.07 | 12,456 | none | no divisions found | - | gallic |
| `aphrahat_demonstrations-2-7_hallock1932.txt` | 0.07 | 12,651 | none | no divisions found | - | syr |
| `vonsoden_prosopographie-afrikanischer-episkopat-deu_1909.txt` | 0.05 | 8,987 | partial | only all-caps headings | caps:19 | lpc |
| `eunomius_first-apology_whiston1711.txt` | 0.05 | 9,298 | none | no divisions found | - | cappadocian |
| `evagrius_praktikos_dysinger.txt` | 0.05 | 8,288 | partial | division addresses repeat; half the divisions are under 30 words | bracket:32 | desert |
| `basil_address-to-young-men_padelford1902.txt` | 0.05 | 8,421 | partial | markers cover under 80% of the text; half the divisions are under 30 words | numpara:46 | cappadocian |
| `chronicle-of-edessa_cowper.txt` | 0.05 | 7,960 | partial | only all-caps headings | caps:3 | syr |
| `pachomius_rules-ethiopic_schodde1885.txt` | 0.04 | 7,298 | none | no divisions found | - | desert |
| `julian_letter-to-the-athenians_wright1913.txt` | 0.04 | 7,892 | none | no divisions found | - | cappadocian,ijc |
| `eucherius-lyon_de-laude-eremi_migne-pl50.txt` | 0.03 | 4,642 | none | no divisions found | - | gallic |
| `tacitus_annals-15-44_church-brodribb1876.txt` | 0.01 | 835 | none | no divisions found | - | pahc |

## 6. OCR score

Definition (`answering_library/ocr.py`, deterministic): score = 1 minus the smaller of 1 and the weighted sum of five rates over a passage: unknown words (alphabetic tokens of three letters or more that are not plausible words of the passage language, where plausible means seen at least 3 times in at least 3 files of that language in the union), stray symbols and long-s or ligature characters, stray single letters, tokens that fuse digits and letters or have inner capitals or are vowelless runs, and line-break hyphenations. The weights are in `manifest.json` under `parameters.ocr`.

| Score band | Passages | Share | Words | Share of words |
|---|---|---|---|---|
| 0.0 to 0.2 | 53,338 | 15.0% | 11,197,318 | 13.8% |
| 0.2 to 0.4 | 25,948 | 7.3% | 6,043,989 | 7.5% |
| 0.4 to 0.5 | 18,088 | 5.1% | 4,040,353 | 5.0% |
| 0.5 to 0.6 | 23,300 | 6.6% | 5,643,937 | 7.0% |
| 0.6 to 0.7 | 34,604 | 9.8% | 8,426,876 | 10.4% |
| 0.7 to 0.8 | 43,743 | 12.3% | 10,664,124 | 13.2% |
| 0.8 to 0.9 | 39,462 | 11.1% | 9,116,665 | 11.3% |
| 0.9 to 1.0 | 116,106 | 32.7% | 25,817,658 | 31.9% |

Score quantiles by passage language, non-apparatus passages:

| Language | Passages | p05 | p25 | median | p75 | p95 |
|---|---|---|---|---|---|---|
| eng | 111,221 | 0.567 | 0.906 | 0.976 | 1.000 | 1.000 |
| lat | 105,965 | 0.000 | 0.343 | 0.653 | 0.800 | 0.940 |
| grc | 41,871 | 0.000 | 0.000 | 0.271 | 0.575 | 0.784 |
| fra | 36,593 | 0.000 | 0.438 | 0.639 | 0.729 | 0.855 |
| deu | 13,205 | 0.000 | 0.491 | 0.631 | 0.755 | 0.874 |
| swe | 5,290 | 0.000 | 0.000 | 0.000 | 0.435 | 0.617 |
| und | 1,241 | 0.852 | 0.913 | 1.000 | 1.000 | 1.000 |
| gmh | 133 | 0.302 | 0.637 | 0.694 | 0.742 | 0.787 |

Share of words that fall below each candidate floor, overall and in the five largest languages:

| Floor | All words | eng | lat | fra | deu | grc |
|---|---|---|---|---|---|---|
| below 0.5 | 26.3% | 2.3% | 33.6% | 22.7% | 22.3% | 71.0% |
| below 0.6 | 33.3% | 3.9% | 42.8% | 36.2% | 40.9% | 78.9% |
| below 0.7 | 43.7% | 6.2% | 56.4% | 65.3% | 62.1% | 87.8% |
| below 0.8 | 56.8% | 10.7% | 76.2% | 94.0% | 84.8% | 97.3% |

Calibration: passages were drawn at random from the finished output (about 0.04% of passages, stratified by score band) and read against their scores. The listing below is that draw.

- 0.044 (grc, `basil_opera-omnia-pg29-grc-lat_migne1857.txt`): 20, Β6ΓΠΙΟ ργίπλυ8 2)6 ἠεὐμπῖο ἐχ ε)υ8 Μοταίϑιι8. --- ἸΙάδπὶ ἴῃ εοὐ. ΧΧΧΙΙ, πη. 9, ρίυι. 1, οἱ οοά. ΧΥ͂Ι, η. 4, Ρἷυι. 4. Υἱάς Βαπάϊι. Ιος. εἷ!., Ρ. 284, 294 οἱ ὅ41. ---Ὁ 
- 0.000 (lat, `cil8-supplementum-numidiae_cagnat-schmidt1894.tx`): iv vin 'aa; (m LII FETRA ES FE» o ceat dedicaNTE o iEG^ 4IVIRO n 19868 sra alts m. 1,80, Iatn m. 0,60, litteris cm. S—L0.— Ftep, Philippeville daus. lea fouilles entrepri
- 0.006 (lat, `cil8-supplementum-numidiae_cagnat-schmidt1894.tx`): Eadem est inter ansas ex ipsa Rhodo in musenm Britannienm trans eullil latas (Hiller inser. Graec. Rhod. 1462), reperitur etinm. Alexandriae (Nerutsos. p. 230, 163), in S
- 0.333 (eng, `anf04_tertullian4-minucius-felix-commodian-orige`): Homer’s Iliad, ii. 205. Dan. ii. 21. Ecclus. x. 4. (LXX.).
- 0.390 (grc, `athanasius_opera-omnia-pg26-grc-lat_migne1857.tx`): ἐαρίἰσαίωτ, εἰ Ρ. 1021, ἰ. υἱ, »γο τρέπονται ἐρίων κέχληνται, ἠϊ πε αμίεπι ροεῖ ας υετϑα, ἀπειθήσασί ποτε, ας αὐἰάμπίμν Οιυδημδάπιοάυπι ἰσἰἰαΓ γαχ, οὐπὶ ἰαϊγοπαπι ρῥγίη- 
- 0.307 (lat, `augustine_epistulae-critical_goldbacher-csel57-p`): in omnibns seruiturani. ne forte. nt ait apostolus, det illi dens paenitentiaru et resipiscat de 6 diaboli laqueis,aquo captiuustenetur seeundum ipsiu.« "oluntatem. filiu
- 0.482 (lat, `augustine_epistulae-1-123-lat_goldbacher-csel34.`): XV. Si Christianus debet in balneis lauare uel in thermis, 20 in quibus sacrificatur simulacris? si Christianus debet in balneis, quibus in die festo suo pagani loti sunt
- 0.409 (lat, `augustine_sermones-inediti-lat_caillau1842.txt`): IV. Prima igitur ejus {xiilio est contra superbiam , quando Deo dicimus : <■ SaiKiificciur nomeo tuum ; •> boc enim petimus , ut det nobis liuicre rt venerari no- mui suu
- 0.466 (fra, `duchesne_histoire-ancienne-de-leglise-tome3-fra_`): 686 TABLE DE.S MATIÈRES PA(l. Jj'uiiinioii rormiinc, le tome de Léon. — Le sec(uui crmcile d'Ephèse: n'habilitât ion d'Eutychès, condamnation de Flavien et des Orientaux.
- 0.549 (fra, `audollent_carthage-romaine-fra_1901.txt`): « Cothones appellantur por- tus in mari interiores arte et manu facti. » Acta sancti Maximiliani martyris (Ruinart, p. 300-302) : 3. « Et Pompeiana matrona cor- pus ejus 
- 0.574 (fra, `crespin_histoire-des-martyrs-t3-fra_benoit-lelie`): La grâce de noftre Seigneur lefus Chrift foit auec vous tous , Amen. Demeurez tous enfemble conftans au Seigneur, & vous donnez garde de la vaine aparence de faindeté , &
- 0.513 (grc, `epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1`): κατὰ γὰρ τὴν ἀκολουϑίαν, ὡς ἔφαμεν, " κ — s c ’ \ x x ” ’ ς ’ Ἢ ’ ς ’ μετὰ tag u (ημέρας) zei τὰς ἄλλας δυο ἑβδομαδας καὶ dvo ἡμέρας \ " x x > c τὰς (ἐν Ναζαρὲτ) πρὸς Ιωά
- 0.630 (lat, `augustine_in-ioannis-evangelium-tractatus-lat_mi`): 1983 IN EPISTOLAM JOANNIS AD nos justos esse dixerimus. Faciunt hoc impii et in- sani : Scio quidem quia justus sum, sed quiddictu- r us suni ante homines ? si me justum 
- 0.627 (grc, `basil_opera-omnia-pg31-grc-lat_migne1857.txt`): Ὅτι δεῖ προσεύχεσθα: ὑπὲρ τῆς προχοπῆς (Ὁ) τῶν πεπιστευχότων, χαὶ ἐπ᾽ αὐτῇ εὐχαριστεῖν. Κεράλ. 1Δ'. ΙΩΑΝΝΗΣ. Οὐ περὶ τούτων δὲ ἐρωτῶ μόνοΥ, ἀλλὰ καὶ περὶ τῶν πιστευόντων 
- 0.650 (fra, `beza_histoire-ecclesiastique-t1-fra_baum-cunitz1`): 2. «Desquels toutesfois il se développa» manque dans De la Planche. Trois catholiques y furent tués. Lambert, p. 88, dont le récit est fondé sur divers documents, est bea
- 0.768 (eng, `anf03_tertullian.xml`): Lavacro. See Ex. xxix. 7; Lev. viii. 12; Ps. cxxxiii. 2. i.e. “Anointed.” Aaron, or at least the priest, is actually so called in the LXX., in Lev. iv. 5, 16, ὁ ἱερεὺς ὁ 
- 0.700 (eng, `anf05_hippolytus-cyprian-caius-novatian.xml`): Oxford ed.: Ep. vii. a.d. circa 251. [Here, as elsewhere, spoken of in this way, in imitation of 1 Pet. v. 1.]
- 0.726 (lat, `augustine_civitate-dei-14-22-lat_hoffmann-csel40`): De temporibus prophetarum. Promissiones Dei, quae factae sunt ad Abraham, cuius 5 semini et gentem Israeliticam secundum carnem et omnes gentes deberi secundum fidem Deo 
- 0.854 (eng, `anf05_hippolytus-cyprian-caius-novatian.xml`): Ps. cx. 3; 2 Pet. i. 18, 19. In making the Logos a living principle in the prophets, and as speaking through them to the Church of God in all ages, Hippolytus agrees with
- 0.814 (eng, `anf05_hippolytus-cyprian-caius-novatian.xml`): As the Word formed. [He expounds Ps. xliv. (xlv.), Sept.] [“In a sense;” i.e., in logic, not time.] [Compare the Athanasian Confession.] [As in the Athanasian Confession.
- 0.853 (lat, `augustine_enarrationes-in-psalmos-lat_migne-pl36`): St pugno in columnam ferias, tu lxderis : et puus quia blaspliemia Deum percutiens non tu disrumperis ? nam nihil facis Deo. Sed inimici Dei aperte blasphe- matores sunt,
- 0.990 (eng, `anf01_apostolic-fathers-justin-irenaeus.xml`): Chapter VIII.—Let nothing be done without the bishop. See that ye all follow the bishop, even as Jesus Christ does the Father, and the presbytery as ye would the apostles
- 1.000 (eng, `anf01_apostolic-fathers-justin-irenaeus.xml`): Chapter II.—The world was not formed by angels, or by any other being, contrary to the will of the most high God, but was made by the Father through the Word. 1. Those, m
- 1.000 (eng, `anf01_apostolic-fathers-justin-irenaeus.xml`): LI. Now, however, inasmuch as the books of these men may possibly have escaped your observation, but have come under our notice, I call your attention to them, that for t

**Recommended floor: 0.70 for inserting a span from a passage (a quote that is shown or spoken); 0.50 for letting a passage into retrieval.** Reasoning from the draw: passages from 0.80 up read as clean or lightly marked text; the 0.60 to 0.80 band holds readable text with systematic long-s or f-for-s misreadings, apparatus lines and index runs, where an inserted span would reproduce scan errors; under 0.50 the draw is dominated by tables, inscriptions, critical apparatus and garbled Greek. The 0.70 floor is a judgement from this draw, not a validated cut: no gold labels exist yet, and Greek and Latin scores are depressed by inflection (a legitimate rare form counts as unknown). It should be confirmed on the gold set before it is used as a gate. The cost of the floor is in the table above: at 0.70 a share of the shelf equal to the 'below 0.7' row is not available for inserted spans (Latin, French, German and Greek lose most), at 0.60 the 'below 0.6' row. Which floor to hold is Mark's call.

## 7. Speaker state

| State | Passages | Share | Words | Share of words |
|---|---|---|---|---|
| known | 134,306 | 37.9% | 30,121,092 | 37.2% |
| mixed | 167,116 | 47.1% | 43,535,811 | 53.8% |
| unknown | 53,167 | 15.0% | 7,294,017 | 9.0% |

Rules (`answering_library/speaker.py`): known only when exactly one author id stands on the bucket rows that claim the file, the passage is not apparatus, and none of the mixed signals fire; mixed when the filename or division title names a dialogue, disputation, acts, council, synod, canons, letters or a polemic (contra, adversus, against), or when quotation marks cover 12% or more of the passage, or speech verbs, speaker labels or scripture references are dense, or markup quotation elements are dense; unknown otherwise (apparatus, multi-author volumes, anything not decided). The voice on a known passage is the corpus-map author id. The state is a file-level and passage-level heuristic; the signals that fired are not stored per passage.

## 8. XML and markup files

33 of the 33 `.xml` files carry `div` markers and 0 carry none.

| File | MB | Leaf divisions (non-apparatus) | Median words per division | Share of words in divisions over 5,000 | Apparatus divisions | Note-stream words | Class | Passages |
|---|---|---|---|---|---|---|---|---|
| `anf03_tertullian.xml` | 6.23 | 773 | 541 | 0.0 | 37 | 71785 | clean | 2,545 |
| `npnf108_augustine-exposition-psalms.xml` | 6.21 | 176 | 3186 | 0.4968 | 13 | 34360 | partial | 2,653 |
| `anf05_hippolytus-cyprian-caius-novatian.xml` | 5.78 | 712 | 289 | 0.2866 | 48 | 65431 | partial | 2,838 |
| `npnf204_athanasius-select-works-letters.xml` | 5.78 | 373 | 510 | 0.2721 | 45 | 105927 | partial | 2,593 |
| `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` | 5.74 | 921 | 373 | 0.152 | 53 | 43506 | partial | 2,815 |
| `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` | 5.66 | 1429 | 218 | 0.1836 | 47 | 57293 | partial | 3,592 |
| `npnf201_eusebius-church-history-life-of-constantine.xml` | 5.60 | 654 | 229 | 0.1203 | 40 | 299715 | partial | 2,756 |
| `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` | 5.44 | 458 | 630 | 0.1062 | 40 | 46078 | partial | 2,060 |
| `npnf111_chrysostom-homilies-acts-romans.xml` | 5.34 | 90 | 4661 | 0.5213 | 18 | 124328 | partial | 1,987 |
| `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` | 4.98 | 433 | 530 | 0.2169 | 32 | 45182 | partial | 2,190 |
| `npnf101_augustine-confessions-letters.xml` | 4.82 | 466 | 504 | 0.3144 | 26 | 69025 | partial | 2,305 |
| `npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml` | 4.66 | 307 | 999 | 0.2404 | 24 | 32352 | partial | 2,104 |
| `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` | 4.64 | 472 | 495 | 0.1272 | 17 | 33333 | partial | 1,767 |
| `anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml` | 4.63 | 819 | 306 | 0.1028 | 52 | 79233 | partial | 2,353 |
| `anf01_apostolic-fathers-justin-irenaeus.xml` | 4.51 | 909 | 309 | 0.0147 | 22 | 54008 | clean | 2,510 |
| `npnf105_augustine-anti-pelagian-writings.xml` | 4.49 | 1115 | 360 | 0.0747 | 32 | 23211 | clean | 2,763 |
| `npnf206_jerome-principal-works.xml` | 4.43 | 196 | 436 | 0.6749 | 27 | 41557 | partial | 1,967 |
| `npnf113_chrysostom-homilies-galatians-philemon.xml` | 4.43 | 115 | 4126 | 0.3161 | 18 | 41435 | partial | 2,185 |
| `npnf104_augustine-anti-manichaean-anti-donatist.xml` | 4.35 | 640 | 403 | 0.3228 | 31 | 21976 | partial | 2,443 |
| `npnf203_theodoret-jerome-gennadius-rufinus.xml` | 4.24 | 845 | 280 | 0.2136 | 43 | 65475 | partial | 2,641 |
| `npnf207_cyril-jerusalem-gregory-nazianzen.xml` | 4.23 | 160 | 547 | 0.6801 | 15 | 77377 | partial | 1,885 |
| `npnf102_augustine-city-of-god-christian-doctrine.xml` | 4.12 | 843 | 481 | 0.0368 | 20 | 13612 | clean | 2,389 |
| `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` | 4.04 | 1197 | 327 | 0.0 | 21 | 41646 | clean | 2,688 |
| `npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml` | 3.83 | 817 | 404 | 0.0459 | 17 | 21916 | clean | 2,261 |
| `npnf210_ambrose-select-works-letters.xml` | 3.83 | 369 | 789 | 0.139 | 17 | 36956 | partial | 1,695 |
| `npnf107_augustine-homilies-john-soliloquies.xml` | 3.68 | 144 | 2699 | 0.5086 | 17 | 20564 | partial | 1,893 |
| `npnf212_leo-great-gregory-great.xml` | 3.45 | 560 | 413 | 0.0291 | 14 | 47323 | clean | 1,769 |
| `npnf208_basil-letters-select-works.xml` | 3.29 | 397 | 332 | 0.0888 | 37 | 75295 | clean | 1,625 |
| `npnf202_socrates-sozomen-ecclesiastical-histories.xml` | 3.28 | 511 | 463 | 0.0752 | 17 | 34361 | clean | 1,796 |
| `npnf214_seven-ecumenical-councils.xml` | 3.18 | 687 | 304 | 0.0243 | 40 | 13900 | clean | 1,680 |
| `npnf209_hilary-poitiers-john-damascus.xml` | 3.08 | 102 | 574 | 0.0 | 32 | 28546 | clean | 1,534 |
| `npnf109_chrysostom-priesthood-ascetic-homilies-statutes.xml` | 3.00 | 65 | 5243 | 0.8142 | 47 | 29217 | partial | 1,487 |
| `npnf213_gregory-great-ephraim-syrus-aphrahat.xml` | 2.23 | 262 | 569 | 0.2776 | 19 | 19650 | partial | 1,161 |

Editorial notes (`<note>`) are cut into their own apparatus passages under a `<division>/notes` locus, so footnote text never enters the running text of a passage. Title pages, prefaces, introductions, indexes and bibliographies are flagged apparatus from the division title.

## 9. Checks on completeness

**Check A, words.** For each plain-text file the independent figure is `len(file_text.split())`; passages plus the words of suppressed page furniture must equal it. Equal in 275 of 275 plain files.

For the 63 markup files an exact figure does not exist (tags can glue or split words), so the independent figures are two bounds: tags deleted (lower) and tags turned into spaces (upper). Passage words lie within the bounds in 57 files; outside by a small margin in 6: `anf01_apostolic-fathers-justin-irenaeus.xml` (-139 of 508,245), `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` (-199 of 517,563), `npnf105_augustine-anti-pelagian-writings.xml` (-109 of 526,233), `npnf107_augustine-homilies-john-soliloquies.xml` (-26 of 511,323), `npnf108_augustine-exposition-psalms.xml` (-240 of 710,142), `pseudo-justin_epistle-to-diognetus-grc_lake1917.txt` (+1 of 3,213). The differences found in the one file examined by hand (npnf107) were words glued across a `<note>` removal and the `<!DOCTYPE>` line, not lost text.

**Check B, passage count.** After writing, each JSONL file was read back from disk: line count equals the in-memory passage count in 338 of 338 files (354,589 lines in all, equal to the manifest total 354,589); and for every division the passage count read back equals the independent arithmetic recount ceil(division words / 400), with 0 divisions out of agreement.

**Check C, verbatim text.** For every passage of a true plain-text file the bytes `byte_start:byte_end` of the source were re-read and split on whitespace: identical to the passage text in 224,522 passages; identical after removing words of suppressed page furniture (running heads, bare page numbers, symbol-only lines) that lie inside the range in 53,315 passages (every passage text is an in-order subsequence of its source range); not a subsequence in 0 passages. Markup passages cannot be compared byte for byte because tags and entities are removed; their byte ranges span the source markup from the first to the last word.

Suppressed page furniture in the plain-text files: 85,213 lines, 229,658 words (0.4% of their words). Kinds are counted per file in `manifest.json` (`furniture.kinds`).

**Check D, markers against an independent pattern.** A second, simpler detector (upper-case keyword plus upper-case Roman numeral at line start, over about twenty keywords) was run on the 26 plain-text files whose chosen scheme uses a keyword family. Of the 21 where the simple pattern finds any heading, the segmenter's count of keyword-family divisions lies within a factor of two of the simple count in 11 (median ratio 1.07); in 5 the simple pattern finds none (those files number their headings in Arabic numerals or in mixed case, which the simple pattern does not read). This is weak corroboration only: the simple pattern misses most numbering styles.

**Check E, determinism.** A complete earlier run of the preceding commit `80ae0d328035` (wall time 542.8 s; the later commit only deletes unused code) was kept and compared with this run, file by file: the sha256 of the output file is identical in 338 of 338 files.

## 10. What the tooling cannot do

- Row identifiers are file-level. Every passage carries all the `row_ids` and `worlds` that claim its file; the free-text `locus` on a bucket row (`div2 5.10`, `running heads from file line 6038`) is not parsed, so a passage is not narrowed to the one row that covers it. A volume claimed by many rows repeats the whole list on each passage.
- Division numbering is read as printed. Roman numerals damaged by OCR (for example `ARTICLE ni`) are not recovered; a missed heading merges two divisions, and a false one (a footnote number, a running head with a changing page number) splits a division. The checks (sequence, address uniqueness, coverage, oversize share) detect many of these but do not fix them.
- All-caps headings cannot be told from running heads and OCR noise by shape alone; the family is used only when most of its divisions are 60 words or longer, and a file resting on it alone is never counted clean.
- Greek numerals are read for simple forms only (alpha-prime to omega with up to four letters). Cyrillic and Greek heading keywords are matched; no Syriac, Arabic, Hebrew or Ethiopic heading vocabulary exists, and none of those scripts occurs in the union's passages.
- Parallel Greek-Latin and Latin-English editions (`grc-lat`, `lat-eng`) are cut as one text; a passage is assigned the script it mostly contains, so a bilingual page can yield passages of either language but the two columns are not paired.
- Sentence cutting uses punctuation and an abbreviation list. Latin and Greek editions that print sentence starts in lower case are cut at a full stop followed by a lower-case word only when the preceding word is four letters or longer. Where no sentence boundary lies inside the 150 to 400 word window, the cut falls on the nearest clause mark and then on any word boundary.
- The OCR score uses a vocabulary built from the union itself. A word that is legitimate but rare (a proper name, an uncommon inflected form) counts as unknown, which depresses Greek and Latin scores; a systematic misreading that recurs in many files counts as plausible.
- The speaker state is a heuristic. It does not read who is speaking inside a passage; it records whether the edition and the passage give grounds to call the voice known, and the voice is the author id of the bucket rows, not a verified attribution.
- Page furniture suppression removes lines from the passage text (never from the byte range). A running head that varies by OCR noise on every page, or a title repeated fewer than 8 times, stays in the text.
- Line-break hyphenation is left as printed (`word- continues`); it is scored, not repaired.
- Output is not yet versioned against the vendored file set beyond the per-file hashes in the manifest; a changed source file changes its hash but the run is whole-union, not incremental.

## 11. Three-level transparency and source access

Every passage record keeps the means to reach its source: `file` (the vendored file name under `cic/texts/`), `byte_start` and `byte_end` (the exact range in that file), `division_locus` and `division_title` (the citable address and its printed heading), `passage_id` (`cic:<file>:<locus>#<NN>`), `speaker`, `ocr_score`, `row_ids` and `worlds` (the bucket rows and worlds that claim the file) and the `apparatus` flag. A highlighted span in an answer can therefore carry a hover (division title, speaker state, OCR score) and open to a click-through page that links to the vendored file and the byte range. Nothing is removed from reach: header blocks, front matter, prefaces, notes and indexes are kept as apparatus passages rather than dropped, and the word-count check in section 9 shows no plain-text word lost except the page furniture it counts (markup files agree within the bounds stated there). Segmentation does not remove any source a reader can reach today.

## 12. Elapsed time for this stage

| Item | UTC |
|---|---|
| Stage started (first command) | 2026-10-29T17:16:49Z |
| Final run started | 2026-10-29T18:42:43Z |
| Final run finished | 2026-10-29T18:48:41Z |

