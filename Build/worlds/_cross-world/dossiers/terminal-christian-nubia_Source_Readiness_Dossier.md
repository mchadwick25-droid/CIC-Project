# Source Readiness Dossier — Terminal Christian Nubia (Late Makuria and Dotawo)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.18
**Corpus-map slug:** `terminal-christian-nubia`
**Time window:** 1054–c. 1484
**Region(s):** The Nile above Egypt: Dongola, Qasr Ibrim, Gebel Adda, Lower Nubia
**Dossier author / date:** Era VI library session, V.18 world agent (oriental batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. No bucket file existed for this world before the pass, and none exists for the two earlier Nubian worlds either. Five files were vendored this pass, each with a staging file validated with `corpus_map_merge.py --check`. Their registry entries, seed rows and cross-link rows sit in the lead's fragment files until merged.

**Who speaks.** Almost no one speaks for this world. The library now holds one body of Nubia's own words, the Old Nubian documents in Griffith's 1913 edition: a miracle of Saint Mena, a lectionary, a sale, and graffiti, among them the Gebel Adda inscription of King Joel. Everything else is an outside voice: Arabic geographers and historians seen through nineteenth- and early twentieth-century translators, and an archaeological survey. No Nubian account of the church's ending survives, and none is in the library.

## 1. Already assigned

No row existed before this pass. These are the files vendored and staged this pass. Scale is counted characters of the whole vendored file.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Nubian Texts of the Christian Period (Old Nubian documents with English translation and notes) | griffith | tradition | assigned | 289,963 | `griffith_nubian-texts-of-the-christian-period_griffith1913.txt` |
| Mémoire sur la Nubie, in Mémoires géographiques et historiques sur l'Égypte, tome 2 (French) | quatremere | context | provisional | 884,486 (whole volume; the Nubia memoir is file lines 190 to about 4732) | `quatremere_memoires-geographiques-et-historiques-sur-l-egypte-tome2-fra_quatremere1811.txt` |
| The Churches and Monasteries of Egypt, Abu Salih (English), Nubia section | abu-salih | context | assigned | 1,258,914 (whole volume; the Nubia section starts at file line 13107) | `abu-salih_churches-and-monasteries-of-egypt_evetts1895.txt` |
| Masalik el absar, chapter IX, Nubia (French) | umari | context | assigned | 992,998 (whole volume; the Nubia chapter starts at file line 5950) | `umari_masalik-el-absar-afrique-moins-egypte-fra_gaudefroy-demombynes1927.txt` |
| Churches in Lower Nubia (architectural survey) | mileham | context | assigned | 235,135 | `mileham_churches-in-lower-nubia_randall-maciver1910.txt` |

What kind of witness each is:

- Griffith 1913: the nearest thing to Nubia's own voice. The English translations and notes read cleanly. The Old Nubian wording, printed in Greek and Coptic letters, is partly garbled, so no Old Nubian quotation is safe from this file. The editor's notes are scholarship.
- Quatremère 1811: the early collection of what the Arabic authors say of Nubia, with the Mamluk campaigns of the thirteenth century. French, readable with scattered errors. A nineteenth-century translator stands between the reader and the Arabic.
- Abu Salih and Al-'Umari: outsiders. Abu Salih writes from Egypt in the Ayyubid period; Al-'Umari from Cairo in the fourteenth century. Both are clean in English or French.
- Mileham: an archaeological survey of the church buildings. A context layer, not a voice.

## 2. Cross-link opportunities

- **`ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt`** (Latin; bucket: Gragn to Fasilides). The word "Nubia" and its Latin forms occur about 60 times. It is a seventeenth-century scholar's compilation of what the Arabic and Ethiopian sources say about the Nubian kingdom beside Ethiopia. Tier: same region, later period (out-of-window). Proposed role: context, provisional. Not opened beyond the word counts.
- **`mendes_expeditio-aethiopica-liber-1-2-lat_beccari1908.txt`** (Latin; bucket: Gragn to Fasilides). About 27 Nubia hits, from the Jesuit patriarch's seventeenth-century account. Tier: out-of-window. Not proposed.
- **`michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt`** (French, to 1196). Six Nubia hits, mostly the sixth-century Nobadites and the eighth-century war of Marwan. Before the window. Not proposed.
- **The earlier Nubian worlds.** The census lists `nubian-christianity` (543–652) and `makurian-nubian-christianity` (697–1054). No bucket exists for either. The staging rows for Griffith, Quatremère, Abu Salih and Mileham name `makurian-nubian-christianity` as a second atlas id because the same books describe the earlier church. Whether that placement is right is for the neighbour world's dossier to decide.
- **The Coptic worlds.** `abu-salih_...` is also staged for `coptic-christianity-fatimid-to-mamluk` (c. 1054–1300), which has its own Egyptian reading of the book.
- **Ethiopian world (V.7).** `umari_...` is shared with the Ethiopian world; its Abyssinia chapter is there.

## 3. Verified acquisition leads

Every row was checked on archive.org this pass: item metadata read, year read, rights field read, text file present. "Vendored" means the file is now in `cic/texts/`.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Nubian Texts of the Christian Period | F. Ll. Griffith (editor) | Griffith | 1913 | https://archive.org/details/nubiantextsofchr00grif | pd-us-by-date; host NOT_IN_COPYRIGHT; title page read | Metadata read; text file fetched (297 KB) and sampled at opening, middle and end, October 2026. Vendored. |
| Mémoires géographiques et historiques sur l'Égypte, tome 2 | Étienne Quatremère | Quatremère | 1811 | https://archive.org/details/mmoiresgographi04quatgoog | pd-us-by-date; host NOT_IN_COPYRIGHT; 'Tome second' and the year read on the title page | Metadata read; text file fetched (909 KB) and sampled at opening, middle and end, October 2026. Vendored. Three other scans (mmoiresgographi01, 02 and 03quatgoog) were opened: 01 is the same tome 2 with poorer OCR; 02 and 03 are tome 1. |
| The Churches and Monasteries of Egypt, attributed to Abu Salih | Abu Salih the Armenian (attributed) | B. T. A. Evetts | 1895 | https://archive.org/details/churchesmonaster00abusuoft | pd-us-by-date; host NOT_IN_COPYRIGHT; title page read | Metadata read; text file fetched (1.26 MB) and sampled at opening, middle and end, October 2026. Vendored. |
| Masalik el absar, I: L'Afrique moins l'Égypte | Ibn Fadl Allah al-'Umari | Gaudefroy-Demombynes | 1927 | https://archive.org/details/india.history.resource.91094 | pd-us-by-date (published 1930 or earlier); title page read | Metadata read; text file fetched (1.0 MB) and sampled at opening, middle and end, October 2026. Vendored; shared with V.7. |
| Churches in Lower Nubia | Geoffrey S. Mileham | ed. D. Randall-MacIver | 1910 | https://archive.org/details/churchesinlowern00mileuoft | pd-us-by-date; host NOT_IN_COPYRIGHT; title page read | Metadata read; text file fetched (234 KB) and sampled, October 2026. Vendored. |
| Histoire des sultans mamlouks de l'Égypte (Maqrizi), tome 1 parts 1 and 2 | Taqi al-Din al-Maqrizi | Étienne Quatremère | 1837 and 1845 | https://archive.org/details/bub_gb_y1QoAAAAYAAJ and https://archive.org/details/histoiredessulta01maqr | pd-us-by-date; part 1 carries the Public Domain Mark 1.0, part 2 has no rights field | Metadata read; both text files fetched (1.9 MB and 961 KB) and checked: 24 Nubia hits in each, about the Nubian wars of the Mamluk sultans, none for Dongola by name. Not vendored: Quatremère's own Nubia memoir (above) already gathers these accounts. |
| The Miracle of Saint Mina — Gis Miinan Nokkor | Old Nubian text, edited by El-Shafie El-Guzuuli and Vincent W. J. van Gerven Oei | the editors (Dongolawi and English) | 2012 | https://archive.org/details/7be9aa8c-b8af-4b2f-96ff-16e4532f2b83 (also oapen-20.500.12657-25413) | Creative Commons BY-NC-ND 3.0 on the first item's record; the publisher is punctum books | Metadata read; text file present (116 KB); not fetched, October 2026. Not vendored: the description dates the text to about 1000, before the window, and the NonCommercial and NoDerivatives terms need a rights ruling from the project lead. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Griffith, Christian Documents from Nubia (Proceedings of the British Academy, 1928) | The census lead names it; it carries the Dongola texts. | Not found on archive.org by title, series or author (several searches). British publication of 1928, so it would be public domain by date if a scan existed. Lead only. |
| Monneret de Villard, Storia della Nubia cristiana (1938) | The standard history of the Nubian church. | Italian publication of 1938: assume in copyright. An archive.org item exists (storiadellanubia0000monn); lending-restricted. Borrow-only. Scholarship, not source. |
| Vantini, Oriental Sources Concerning Nubia (1975) | The collected Arabic and other oriental sources in translation. | In copyright (1975). Not on archive.org by search. Borrow-only. |
| Plumley, Old Nubian Texts from Qasr Ibrim (1988) | The Qasr Ibrim documents. | In copyright (1988); lending-restricted items only. |
| The Barshambu stela of 1317 and the Gebel Adda letter of 1484 | The census's archaeology-grade anchors at the two ends. | The stela and the letter are published only in twentieth-century scholarship (not found in the library or on archive.org by search). Griffith's 1913 volume has the earlier Gebel Adda graffiti that name King Joel and Dotawo, not the 1484 letter. |
| Budge, The Egyptian Sudan, its history and monuments (1907; archive.org items egyptiansudanits01budg and 02budg, egyptiansdni01budguoft and 02budguoft) | The census lead names it. | A narrative history and travel handbook by an Egyptologist, about 1.5 MB per volume. Scholarship, not a source. Pre-1931 and clean enough, so a later pass could vendor it if Doc_02 wants an English survey. Not vendored. |
| Somers Clarke, Christian Antiquities in the Nile Valley (1912) | The census lead names it. | Searched by title and author; not found on archive.org. Lead only. |
| Ibn Khaldun, Histoire des Berbères, trans. de Slane (1852–56; four volumes on archive.org) | Ibn Khaldun wrote of Nubia. | Checked all four volumes for Nubia: seven hits in volume 2, two for Dongola, a single ethnographic paragraph (file line 6699 onward in that item). The Nubia chapter of the Kitab al-Ibar is not in this translation. Not vendored. |
| Reinaud, Géographie d'Aboulféda (introduction, 1848) | A fourteenth-century geographer's account of Nubia. | The archive.org item (geographie-d-aboulfeda-traduite-de-larabe-en-francais) is the introduction only. A note in it says the Nubians gave up Christianity only after the thirteenth century; it carries no Nubian chapter. Not vendored. The translation volume was not found. |
| Burckhardt, Travels in Nubia (1819–22) | Early eyewitness of the ruins. | Nineteenth-century traveller; describes the ruins, not the church. Out of window. Not vendored. |
| Browne, Old Nubian texts and the Miracle of St Mina (1994) and other Browne editions | Old Nubian texts with translation. | In copyright. The 2012 open edition of Saint Mina is in section 3 as a rights question. |
| Kunst und Geschichte Nubiens in christlicher Zeit (1970) | The Warsaw volume on Faras. | In copyright (1970); lending-restricted. Borrow-only. |

## 5. Open cross-world questions

- **Earlier Nubian worlds.** `nubian-christianity` and `makurian-nubian-christianity` have no bucket and, so far as the library goes, no files except those staged here under a second atlas id. Whether this world should hold the Griffith edition alone or share it is for the neighbours' dossiers.
- **Ethiopian world (V.7).** The Nubian and Ethiopian kingdoms appear together in Al-'Umari's geography and in the Ludolf Commentarius. How much the Nubian world should lean on Ethiopian-side files is a boundary question.
- **Coptic worlds.** Abu Salih belongs first to the Egyptian reading of the same book. Which Coptic world owns the Nubian appendix is not decided here.
- **Rights ruling on the Saint Mina edition.** A Creative Commons BY-NC-ND text of about the year 1000. Whether the library can carry it is a decision for the project lead, and the NonCommercial term is the reason it was not vendored.
- **Record of an absence.** Whether a world defined by documented silence belongs in the program at all is a governance question, not decided here.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says "No question". Nothing found disturbs that. The Gebel Adda inscription that names King Joel opens "Through the name of the Father, the Son and the Ghost (sic)" (Griffith, file line 4090). That is the only Nubian creedal statement in the library. I did not read the files through for Christology. The church's relation to the Coptic patriarchate in this period belongs in Doc_01.

**Sourcing (B1).** The census says the inside literary voice is thin, and that holds. The Old Nubian texts in Griffith are a miracle story of Saint Mena, a lectionary, a record of a sale and a set of wall inscriptions. They are church books and graffiti, not testimony. Every account of the kingdom's political history, its king at Dongola and its ending comes from Arabic authors writing in Cairo or Egypt, or from nineteenth-century collectors who translated them. The archaeological record (Mileham) shows the buildings.

**Ecology (B2).** The ecology is outsiders looking at a church that left almost no words. The Mamluk and Ayyubid-period authors describe it with the interest of neighbours and, in places, of conquerors. A Representative drawn from these files would speak mostly in other people's descriptions of Nubia. That is a screen risk to name in Doc_02, and the right records for it are the absence kinds already in the schema.

**Uniqueness (B3).** The neighbours are the earlier Nubian worlds (Makuria before 1054), the Coptic world in Egypt, and the Ethiopian world upriver of the Blue Nile. Each overlap is a boundary to state.

**Audiences (B4).** There is no continuing church, as the census says. The audience is people interested in lost churches, Coptic and Ethiopian Christians who share the region's history, and archaeology readers.

**Scale (B5).** About 3.7 MB vendored in five files. Several scholarly leads are in copyright or lending-restricted, so there is little more to acquire in the public domain beyond the open question of Saint Mina.

**Recommendation: atlas only.** Reason: no person speaks in the library. The nearest Nubian voice is a short run of church books and graffiti in Old Nubian, quotable only in English after checking the scan, and everything about the kingdom's politics and its ending comes through outsiders. The rest of the evidence that would matter, the Barshambu stela, the Gebel Adda letter and the Qasr Ibrim archive, sits in twentieth-century scholarship that is in copyright. A Representative here would have almost nothing derivable from the completed world to say about itself. If the project wants a world defined by its documented silence, that is a question for the project lead to settle together with the Saint Mina rights ruling, not a build. This is a recommendation for Mark to weigh, not a decision.
