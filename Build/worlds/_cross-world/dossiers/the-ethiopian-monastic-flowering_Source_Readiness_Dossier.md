# Source Readiness Dossier — The Ethiopian Monastic Flowering

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.7
**Corpus-map slug:** `the-ethiopian-monastic-flowering`
**Time window:** c. 1270–1517
**Region(s):** The Ethiopian highlands (Shewa, Tigray, the northern monastic houses, the royal court)
**Dossier author / date:** Era VI library session, V.7 world agent (oriental batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. Before this pass the bucket held two rows, both `provisional`: the Budge Synaxarium volumes. Eight files were vendored this pass (one of them, Al-'Umari, is shared with the Nubian world), each with a staging file validated with `corpus_map_merge.py --check`. Their registry entries, seed rows and cross-link rows sit in the lead's fragment files until merged.

**Who speaks.** This world mostly speaks for itself, but through the crown. The Ethiopian texts in the library are the dynasty's charter myth, the court's chronicle, hagiography written by the houses the crown patronised, and Marian miracle literature. The persecuted side of the Sabbath quarrel, the Ewostathians and the monks of Estifanos, is not in the library in any form. Two outside witnesses are vendored: a Muslim geographer writing in Cairo and a Portuguese priest writing just after the window.

## 1. Already assigned

The first two rows were there before this pass. The rest are the files vendored and staged this pass. Scale is counted characters of the whole vendored file.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Ethiopic Synaxarium, months Maskaram, Tekemt, Khedar (English) | ethiopian-synaxarium | tradition | provisional | 819,853 | `ethiopian-synaxarium_book-of-saints-ethiopian-church-v1-maskaram-khedar_budge1928.txt` |
| Ethiopic Synaxarium, months Takhshash, Ter, Yakatit (English) | ethiopian-synaxarium | tradition | provisional | 793,023 | `ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-takhshash-yakatit_budge1928.txt` |
| Kebra Nagast (The Glory of Kings), English, Budge 1922 | kebra-nagast | tradition | assigned | 738,524 | `kebra-nagast_queen-of-sheba-and-her-only-son-menyelek_budge1922.txt` |
| Life and Miracles of Takla Haymanot (Dabra Libanos version), English | gadla-takla-haymanot | tradition | assigned | 735,970 | `gadla-takla-haymanot_life-and-miracles-of-takla-haymanot_budge1906.txt` |
| Lives of Maba' Seyon and Gabra Krestos, English | gadla-maba-seyon | tradition | provisional | 563,417 | `gadla-maba-seyon_lives-of-maba-seyon-and-gabra-krestos_budge1898.txt` |
| Chronicles of Zar'a Ya'eqob and Ba'eda Maryam (Ge'ez, with French introduction and appendix) | zara-yaqob | tradition | assigned | 417,123 | `zara-yaqob_chroniques-zara-yaeqob-baeda-maryam-gez-fra_perruchon1893.txt` |
| Wars of Amda Syon, French translation (inside Journal asiatique 1889) | amda-syon | context | provisional | 744,839 | `amda-syon_guerres-amda-syon-journal-asiatique-8e-serie-t14-fra-gez_perruchon1889.txt` |
| Miracles of the Virgin Mary, Life of Hanna, English | taamra-maryam | tradition | provisional | 934,750 | `taamra-maryam_miracles-of-the-blessed-virgin-mary-life-of-hanna_budge1900.txt` |
| Narrative of the Portuguese Embassy to Abyssinia, 1520–1527 | alvares | context | assigned | 1,006,780 | `alvares_narrative-of-the-portuguese-embassy-to-abyssinia_stanley1881.txt` |
| Masalik el absar, chapter VIII, Abyssinia (French) | umari | context | assigned | 992,998 (whole volume; the Abyssinia chapter is file lines 3609 to 5950) | `umari_masalik-el-absar-afrique-moins-egypte-fra_gaudefroy-demombynes1927.txt` |

What kind of witness each is:

- Kebra Nagast, Takla Haymanot, Maba' Seyon, Miracles of Mary: English translation, clean OCR. Primary voices once each quote is checked against the scan.
- Zar'a Ya'eqob chronicle: the Ge'ez OCR is unusable, so this file is a second witness for the Ge'ez. The French introduction, notes and appendix of translated passages read cleanly. The volume holds no full translation.
- Amda Syon chronicle: French translation, second-grade OCR with scattered errors. Quote only after checking the page image.
- Alvares and Al-'Umari: outsiders. Alvares is a Portuguese priest writing 1520 to 1526, after the window. Al-'Umari is a fourteenth-century Muslim geographer working from informants in Cairo.

## 2. Cross-link opportunities

Texts already on the shelf that name this world's figures or practices but are not yet linked to it. Tiers follow `CORPUS-USE.md`.

- **`mendes_expeditio-aethiopica-liber-1-2-lat_beccari1908.txt`** (Latin, the Catholic patriarch's account, 1620s to 1630s; bucket: Gragn to Fasilides). File lines 6544 to 6560 name Takla Haymanot and an Abbot Eustatheus as the two founders of the monastic movement and say the movement split into two bodies, the larger at Debra Libanos under Takla Haymanot and his successor the Ichegue, the smaller under Eustatheus. The word "Sabbath" in Latin forms occurs 23 times. The Eustathius at line 10021 is the bishop of Antioch, not Ewostatewos. Tier: same place, later period (out-of-window). Proposed role: context, provisional.
- **`ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt`** (Latin, 17th-century scholar's synthesis; bucket: Gragn to Fasilides). Sabbath forms occur 96 times and Amda forms 16 times, with three notices of Takla Haymanot (for example file lines 29999 and 30311). It is a scholar's reconstruction from Ethiopian informants, not a voice of the window. Tier: same place, later period. Proposed role: context, provisional.
- **`telles_travels-of-the-jesuits-in-ethiopia_1710.txt`** (English, Telles's digest of Paez's history; bucket: Gragn to Fasilides). It names the Emperor Zara Jacob three times (file lines 6303, 8357, 8967) and Takla Haimanot once (10717). Line 8357 reports Ethiopians sent by Zara Jacob to the Council of Florence. Thin. Tier: same place, later period. Proposed role: context, provisional.
- **`paez_historia-aethiopiae-liber-3-4-por_beccari1906.txt`** (Portuguese; bucket: Gragn to Fasilides). Five Sabbath hits and nine Amda hits, no Zara Jacob or Takla Haymanot. Named-never-opened. Not proposed.
- **`pachomius_rules-ethiopic_schodde1885.txt`** (English, 43,419 characters, the Rules of Pachomius from the Ethiopic). The Ethiopic translation is undated in the file and the monastic houses of this world may or may not have used this version. Tier: named-never-opened. Not proposed; flagged for the Doc_02 reader.
- The two Synaxarium files already in the bucket: the Takhshash-to-Yakatit volume lists Takla Haymanot in its table of contents (file line 470). The Abba Eustathius entry at line 16598 is Eustathius of Antioch, not Ewostatewos, so do not read it as the Ewostathian founder. The feast of Takla Haymanot's death falls in volume 4, which is not vendored (see section 4).
- **`arab-faqih_futuh-al-habasha-conquete-de-labyssinie-fra_basset1897.txt`** (French, the Muslim chronicle of the conquest of Ethiopia in the 1530s). It is after the window and outside this world. Tier: out-of-window. Not proposed.
- **The Era VII and Nubian files vendored in this pass** serve neighbours: `umari_...` is shared with the Nubian world (V.18).

## 3. Verified acquisition leads

Every row was checked on archive.org this pass: item metadata read, year read, rights field read, text file present. "Vendored" means the file is now in `cic/texts/`.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Les chroniques de Zar'a Yâ'eqôb et de Ba'eda Mâryâm | Jules Perruchon (editor) | Perruchon (French introduction and appendix) | 1893 | https://archive.org/details/leschroniquesde00perrgoog | pd-us-by-date; host possible-copyright-status NOT_IN_COPYRIGHT; title page read | Metadata read; text file fetched (433 KB) and sampled at opening, middle and end, October 2026. Vendored. A second scan, leschroniquesdez00perr (449 KB), was compared and not used. |
| The Queen of Sheba and her only son Menyelek (Kebra Nagast) | Anonymous | E. A. Wallis Budge | 1922 | https://archive.org/details/queenofshebahero00kebr | pd-us-by-date; title page read: Medici Society, first edition February 1922 | Metadata read; text file fetched (742 KB) and sampled at three points, clean, October 2026. Vendored. |
| The Life of Takla Haymanot ... and the Miracles of Takla Haymanot | Anonymous (Gadla Takla Haymanot) | E. A. Wallis Budge | 1906 | https://archive.org/details/lifeoftaklahymnt00budg | pd-us-by-date; title page read: privately printed for Lady Meux, 1906 | Metadata read; text file fetched (748 KB) and sampled at three points, English clean, October 2026. Vendored. |
| The Lives of Maba' Seyon and Gabra Krestos | Anonymous | E. A. Wallis Budge | 1898 | https://archive.org/details/b28037650 | pd-us-by-date; title page read: London 1898 | Metadata read; text file fetched (598 KB) and sampled at three points, English clean, October 2026. Vendored. |
| The Miracles of the Blessed Virgin Mary, the Life of Hanna and the Magical Prayers of 'Aheta Mika'el | Anonymous | E. A. Wallis Budge | 1900 | https://archive.org/details/gri_33125008690600 | pd-us-by-date; host NOT_IN_COPYRIGHT; title page read | Metadata read; text file fetched (1.25 MB) and sampled at three points, October 2026. Vendored. |
| Narrative of the Portuguese Embassy to Abyssinia, 1520–1527 | Francisco Alvares | Lord Stanley of Alderley | 1881 | https://archive.org/details/narrativeofportu00alvarich | pd-us-by-date; host NOT_IN_COPYRIGHT; title page read | Metadata read; text file fetched (1.0 MB) and sampled at three points, clean, October 2026. Vendored. |
| Histoire des guerres d'Amda Syon (Journal asiatique, 8th series, vol. 14) | Jules Perruchon (translator) | Perruchon | 1889 | https://archive.org/details/in.ernet.dli.2015.530741 | pd-us-by-date; title page read | Metadata read; text file fetched (762 KB) and sampled at three points, October 2026. Vendored as the whole periodical volume. |
| Masalik el absar, I: L'Afrique moins l'Égypte | Ibn Fadl Allah al-'Umari | Gaudefroy-Demombynes | 1927 | https://archive.org/details/india.history.resource.91094 | pd-us-by-date (published 1930 or earlier); title page read | Metadata read; text file fetched (1.0 MB) and sampled at three points, October 2026. Vendored; shared with V.18. |
| Historia Aethiopica | Hiob Ludolf | none (Latin) | 1681 | https://archive.org/details/bub_gb_JFZEAAAAcAAJ | pd-us-by-date; host licence Public Domain Mark 1.0 | Metadata read; text file present (873 KB); not fetched, October 2026. Not vendored: a seventeenth-century synthesis, after the window; the Commentarius of 1691 is already on the shelf. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Huntingford, The Glorious Victories of 'Amda Seyon (Oxford, 1965) | The census names it as the royal chronicle of Amda Seyon in English. | In copyright (1965). An uploaded copy exists on archive.org (the-glorious-victories-of-amda-seyon-1); not vendored. Perruchon's French of 1889 is the only public-domain translation found. |
| Il libro della luce (Mashafa Berhan), ed. Getatchew Haile, CSCO 1964 | Zar'a Ya'eqob's own book, an inside voice for the reform. | In copyright (1964). The archive.org items (illibrodellaluce0261zare and a second) are lending-restricted. Borrow-only. |
| The Ge'ez Acts of Abba Estifanos of Gwendagwende (Haile, CSCO 2006) | The census calls the Estifanosite acts the counterweight to the royal sources. | In copyright (2006). An uploaded copy exists (the-geez-acts-of-abba-estifanos-of-gwendagwende); not vendored. This is the largest gap in the world's voices. |
| Gadla Ewostatewos, CSCO 1955 (Vitae sanctorum indigenarum) | The founder of the Sabbath movement. | In copyright and lending-restricted (vitaesanctorumin0000gadl, access-restricted). Ge'ez with a Latin version. Borrow-only. |
| Conti Rossini and Turaev, Vitae sanctorum indigenarum (CSCO, 1904; six archive.org items, vitaesanctorumin01cont to 06cont) and Vitae sanctorum antiquiorum (1904) | Ethiopian saints' lives, pre-1931. | Ge'ez text only. Sampled two items: the OCR is noise. No English leg. The antiquiores volume covers the Aksumite saints, before the window. |
| Dillmann, Chrestomathia Aethiopica (1866) | Ge'ez extracts from the chronicles. | Ge'ez OCR is noise (sampled); no translation. Second-witness grade at best and too poor to cite. |
| Budge, Book of the Saints of the Ethiopian Church, volumes 3 and 4 (via bookofsaintsofet00yait, a 2.7 MB microform item that holds volumes 2 to 4) | The Synaxarium; the death feast of Takla Haymanot is in volume 4. | Checked for the window's figures: Takla Haymanot appears once, in a hymn line; Ewostatewos and Estifanos do not appear. It duplicates volume 2, which is already vendored. A separate volume 4 item is lending-restricted. Not vendored. |
| Basset, Études sur l'histoire d'Éthiopie (1881–82) | The standard French translations of the Ethiopian annals. | Journal asiatique 1881, vol. 18 (in.gov.ignca.26211) holds the part on Galawdewos, the sixteenth century. The Zar'a Ya'eqob part is in vol. 17, which was not found. Not vendored. |
| Dillmann, Ueber die Regierung, insbesondere die Kirchenordnung des Königs Zar'a-Jacob (Berlin, 1884) | Zar'a Ya'eqob's church order, with German translation. | Searched several ways; not found on archive.org. Lead only. |
| Kebra Nagast, German edition by Bezold (1905) | Original-language edition with German translation. | Not found on archive.org. Budge's English is vendored. |
| Taddesse Tamrat, Church and State in Ethiopia, 1270–1527 (Oxford, 1972) | The standard account for exactly this window. | In copyright and scholarship, not a source. An uploaded copy exists (church-and-state-in-ethiopia); not vendored. |
| Budge, A History of Ethiopia, Nubia and Abyssinia (1928) | A pre-1931 narrative of Ethiopia. | Found by search; not opened. Scholarship, not a source. |
| Budge, One Hundred and Ten Miracles of Our Lady Mary (1933) | Ethiopic Marian miracles in English. | British publication of 1933: assume in copyright. The 1900 Meux volume is vendored instead. |

## 5. Open cross-world questions

- **Zagwe and early Solomonic world (1137–1270) and Gragn to Fasilides (1517–1650).** The Kebra Nagast, the Marian miracles and Alvares each straddle a boundary. The files carry staging rows for both neighbours as well as V.7. Where each dynasty-myth or Marian passage belongs in Doc_04 is a mapping question, not decided here.
- **Nubian world (V.18).** Al-'Umari's volume serves both. The Abyssinia chapter is here, the Nubia chapter there.
- **Church of the East and Malabar worlds.** None.
- **The Ethiopian community in Jerusalem and Rome.** Telles reports Ethiopians at Florence under Zar'a Ya'eqob. Whether a world about the highlands should draw on the Council of Florence record is a scope question for Step 0.
- **Royal sponsorship and the gravity.** The census warns that royal sponsorship needs care. Four of the six inside voices in the library are crown-sponsored or Dabra Libanos hagiography. Whether that makes sponsorship a Primary or a Tensional gravity is Doc_04's question, not this dossier's.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says "No question". Nothing found disturbs that. The Takla Haymanot life has the baptism in the name of the Father, the Son and the Holy Spirit (file line 4966), and Perruchon's appendix reports Zar'a Ya'eqob ordering "Of the Father, of the Son, of the Holy Spirit" written on his subjects' foreheads. The Sabbath, the Marian cult and the monastic houses are practices and disputes about practice, not disputes about the creed. I did not read any file through for Christology.

**Sourcing (B1).** The census says "RICH". That holds for what exists in Ge'ez and fails for what a public-domain reader can use. Five voices speak in clean English: the dynastic myth (Kebra Nagast), the founder-saint's life (Takla Haymanot), the life of a saint of Zar'a Ya'eqob's reign (Maba' Seyon), and the Marian miracle collection. Amda Syon's wars are in French with rough OCR. The chronicle of Zar'a Ya'eqob is in Ge'ez only, with a French apparatus. Zar'a Ya'eqob's own book, the Estifanos acts and the Ewostatewos life are in copyright or lending-restricted.

**Ecology (B2).** The shape is lopsided. The crown (chronicle, charter myth), the monastic house the crown patronised (Dabra Libanos) and two outsiders (a Muslim geographer, a Portuguese priest) are in the library. The persecuted dissenters are not. A Representative drawn from these files would hear the monks who won and the king who pressed them, and would have nothing from the monks who refused. That is a screen risk to name in Doc_02, and honest-limit records should carry the absence.

**Uniqueness (B3).** The neighbours on the Ethiopian line are the Zagwe and early Solomonic world before and Gragn to Fasilides after. Against the first the difference is the dynasty (1270) and the monastic movement. Against the second it is the Muslim wars and the Portuguese. Each overlap is a boundary to state.

**Audiences (B4).** The Ethiopian Orthodox Tewahedo Church has tens of millions of members and keeps the outcome of the Sabbath argument. The audience is large and the world's practices are still alive.

**Scale (B5).** About 6.6 MB vendored in this pass for V.7 (eight files), plus the two Synaxarium volumes already there. The pass held to files that speak for or about the window.

**Recommendation: build.** The world speaks in its own voice in four clean English texts and a French chronicle, so a Representative can draw on first-hand material, which is more than the other worlds in this batch can say. The audience is large and the floor is clear. The cost to say up front: the persecuted side of the Sabbath quarrel is not in the library, and the Zar'a Ya'eqob chronicle is Ge'ez with no usable translation. A Doc_02 should treat the Estifanos acts (in copyright, borrow-only) as the first acquisition decision before the build counts the dissent as covered. This is a recommendation for Mark to weigh, not a decision.
