# Source Readiness Dossier — St Thomas Christians, 1300–1517

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.23
**Corpus-map slug:** `st-thomas-christians-1300-1517`
**Time window:** 1300–1517
**Region(s):** The Malabar coast (Cranganore, Quilon, Cochin, Kayamkulam), with the patriarchate in Mesopotamia as the distant authority
**Dossier author / date:** Era VI library session, V.23 world agent (oriental batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. Before this pass the bucket held four rows staged by the Era VII session, all `provisional`. The bucket for the earlier world (`st-thomas-christians-of-india`) was read for cross-links and not edited. Ten files were vendored this pass (Assemani III.1, Cathay vol. III, Budge and Chabot are shared with the Timur-to-Hakkari world), each with a staging file validated with `corpus_map_merge.py --check`. Their registry entries, seed rows and cross-link rows sit in the lead's fragment files until merged.

**Who speaks.** The community speaks in a few short places. A colophon of 1301 from Cranganore (in Mingana's English), the colophons of the bishop Mar Jacob and his companions in the 1490s and 1510, the history of their mission and their letter of 1504 (in Assemani's Latin). Everything else is an outsider: a Dominican bishop of Columbum, a Franciscan legate, a Venetian merchant, an Italian traveller from Bologna, a Portuguese author of a book on the Indian Ocean, and da Gama's crew. The 1504 bishops were ordained in Mesopotamia, so the letter is the voice of the church's clergy, not of the Malabar-born laity.

## 1. Already assigned

The first four rows were there before this pass. The rest are the files vendored and staged this pass. Scale is counted characters of the whole vendored file.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Bibliotheca Orientalis III.2, the dissertation De Syris Nestorianis (Malabar bishops, the Thomas Christians) | assemani | context | provisional | 2,894,936 | `assemani_bibliotheca-orientalis-tomus3-pars2-de-syris-nestorianis-lat_1728.txt` |
| Historia Ecclesiae Malabaricae, Historia Synodi Diamperitanae, chapter I (Latin) | raulin | context | provisional | 1,668,001 | `raulin_historia-ecclesiae-malabaricae-cum-diamperitana-synodo-lat_1745.txt` |
| The Acts and Decrees of the Synod of Diamper (English, 1694) | geddes | context | provisional | 907,616 | `geddes_history-of-the-church-of-malabar-synod-of-diamper_1694.txt` |
| Lingerings of Light in a Dark Land, chapters I to VI | whitehouse | context | provisional | 1,046,973 | `whitehouse_lingerings-of-light-in-a-dark-land_1873.txt` |
| Bibliotheca Orientalis III.1, De scriptoribus Syris Nestorianis (the 1490 history of the Malabar bishops and the 1504 letter) | assemani | tradition | assigned | 2,694,057 | `assemani_bibliotheca-orientalis-tomus3-pars1-de-scriptoribus-syris-nestorianis-lat_1725.txt` |
| The Early Spread of Christianity in India (with translated colophons of 1301, the 1490s and 1504) | mingana | context | assigned | 217,178 | `mingana_early-spread-of-christianity-in-india_mingana1926.txt` |
| Mirabilia descripta (Friar Jordanus, bishop of Columbum) | jordanus | context | assigned | 274,882 | `jordanus_mirabilia-descripta-wonders-of-the-east_yule1863.txt` |
| Cathay and the Way Thither, vol. III (Marignolli at Quilon, Montecorvino's letters) | yule | context | provisional | 739,356 | `cathay-and-the-way-thither_vol3-missionary-friars-pegolotti-marignolli_yule-cordier1914.txt` |
| India in the Fifteenth Century (Conti, Nikitin and others) | india-in-the-fifteenth-century | context | provisional | 514,429 | `india-in-the-fifteenth-century_narratives-of-voyages_major1857.txt` |
| Journal of the First Voyage of Vasco da Gama, 1497–1499 | velho | context | provisional | 549,077 | `velho_journal-of-the-first-voyage-of-vasco-da-gama_ravenstein1898.txt` |
| The Travels of Ludovico di Varthema, 1503–1508 | varthema | context | assigned | 1,178,786 | `varthema_travels-of-ludovico-di-varthema_jones-badger1863.txt` |
| The Book of Duarte Barbosa, vol. II (about 1518) | barbosa | context | provisional | 902,513 | `barbosa_book-of-duarte-barbosa-vol2_dames1921.txt` |
| The Monks of Kublai Khan, life of Mar Yahballaha III (English) | yahballaha-sauma | antecedent | assigned | 483,699 | `yahballaha-sauma_monks-of-kublai-khan_budge1928.txt` |
| Histoire de Mar Jabalaha III et du moine Rabban Çauma (French) | yahballaha-sauma | antecedent | assigned | 917,776 | `yahballaha-sauma_histoire-de-mar-jabalaha-iii-et-rabban-cauma-fra_chabot1895.txt` |

What kind of witness each is:

- Mingana: scholarship that translates primary colophons. The translated colophons are the nearest thing in the library to the community's own written voice. The argument around them is twentieth-century.
- Assemani III.1: Latin, with the long s read as f. Printed Latin of a Syriac letter and a short history, within an eighteenth-century catalogue.
- Jordanus, Marignolli, Conti, Varthema, Barbosa, the Roteiro: outsiders in clean English. Jordanus, Marignolli and Varthema have short paragraphs on the Christians of St Thomas. The Roteiro's "Christians" at Calicut are a Portuguese mistake about Hindu temples.
- Budge and Chabot: the life of the patriarch in whose time the 1301 colophon was written; ends in 1317. The antecedent, not the window.

## 2. Cross-link opportunities

- **`barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt`** (Latin, 759,749 characters; bucket: Timur to Hakkari and others). Lamy's appendix reports the three bishops ordained in 1504 and sent to India, the Dabek islands and China, and says Simeon died in 1503 and that Elias succeeded in 1504 and died the same year (file lines 29186 to 29196, in a two-column passage the OCR interleaves). That is the patriarchal side of the 1504 letter. Tier: same time-place. Proposed role: context, assigned, since I read the passage.
- **`malech_history-of-the-syrian-nation-and-old-evangelical-apostolic-church-of-the-east_1910.txt`** (English, 1910; bucket: Timur to Hakkari). Its chapter XXX is staged as about Timur and "the visits of Indian Christians to the patriarch". The staging note says it was placed on the contents entry and not read through. Tier: same time-place. Proposed role: context, provisional.
- **`liturgies-eastern_mark-james-clement-chrysostom-basil-malabar_neale-1870s.txt`** (English, 532,498 characters; bucket: the earlier world). Neale's translation of the Malabar rite in use before Diamper. The rite was not changed in the window, but the file has no dated witness for 1300 to 1517. Tier: same place, adjacent period. Proposed role: context, provisional.
- **`vincenzo-maria_viaggio-indie-orientali-ita_1672.txt`** (Italian, 2,035,076 characters; bucket: the earlier world and the Schism of 1552). Libro Secondo chapters 1 to 3 give the Carmelites' account of the apostle tradition and the history to 1599. A seventeenth-century Catholic reading, after the window. Tier: out-of-window. Proposed role: context, provisional.
- **`whitehouse_lingerings-of-light-in-a-dark-land_1873.txt`** (already in this bucket, chapters I to VI). It cites Jordanus 14 times and Marignolli 13 times, so it is a convenient finding aid for the outsider witnesses now vendored.
- **`scher_notice-manuscrits-syriaques-patriarcat-chaldeen-mossoul-fra_1907.txt`**. A colophon of 1497 from the Seert diocese names Mar Simeon, patriarch. It is staged for the Timur-to-Hakkari world in the proposed cross-link rows, not for this one.
- **`hough_history-of-christianity-in-india-v2_1839.txt`**, **`geddes_...`**, **`francis-xavier_monumenta-xaveriana-v1-lat_1899-1900.txt`**. All concern the Portuguese period after the window. Out-of-window. Not proposed.

## 3. Verified acquisition leads

Every row was checked on archive.org this pass: item metadata read, year read, rights field read, text file present. "Vendored" means the file is now in `cic/texts/`.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Bibliotheca Orientalis Clementino-Vaticana, tomus III pars 1 | Giuseppe Simone Assemani | none (Latin) | 1725 | https://archive.org/details/de-scriptoribus-syris-nestorianis | pd-us-by-date; title-page year read | Metadata read; text file fetched (2.7 MB), October 2026. Vendored; the 1504 letter and the 1490 history start at file line 93562. See the Timur-to-Hakkari dossier for details. |
| The Early Spread of Christianity in India | Alphonse Mingana | Mingana | 1926 | https://archive.org/details/earlyspreadofchr00ming_0 | pd-us-by-date; MCMXXVI read on the title page | Metadata read; text file fetched (217 KB) and sampled at opening, middle and end, October 2026. Vendored. |
| Mirabilia descripta: the Wonders of the East | Friar Jordanus Catalani | Henry Yule | 1863 | https://archive.org/details/mirabiliadescrip00jord | pd-us-by-date; host NOT_IN_COPYRIGHT; the Hakluyt report for 1863 opens the volume | Metadata read; text file fetched (273 KB) and sampled at opening, middle and end, October 2026. Vendored. |
| Cathay and the Way Thither, vol. III | Yule and Cordier | Yule, revised by Cordier | 1914 | https://archive.org/details/cathaywaythither03yule | pd-us-by-date; 'issued for 1914' read | Metadata read; text file fetched (738 KB) and sampled, October 2026. Vendored. |
| India in the Fifteenth Century | Conti, Abd-er-Razzak, Nikitin, Santo Stefano | ed. R. H. Major | 1857 | https://archive.org/details/indiainfifteenth00majo | pd-us-by-date; M.DCCC.LVII read; host NOT_IN_COPYRIGHT | Metadata read; text file fetched (513 KB) and sampled at opening, middle and end, October 2026. Vendored. Other scans (indiainfifteenth00majorich, indiainfifteent00nikigoog and more) were not compared. |
| A Journal of the First Voyage of Vasco da Gama, 1497–1499 | Álvaro Velho (attributed) | E. G. Ravenstein | 1898 | https://archive.org/details/ajournalfirstvo00ravegoog | pd-us-by-date; M.DCCC.XCVIII read; host NOT_IN_COPYRIGHT | Metadata read; text file fetched (549 KB) and sampled at opening, middle and end, October 2026. Vendored. Other scans (bub_gb_13stAAAAMAAJ with the Public Domain Mark, 634 KB) exist. |
| The Travels of Ludovico di Varthema | Ludovico di Varthema | J. Winter Jones, ed. G. P. Badger | 1863 | https://archive.org/details/travelsofludovic00vartrich | pd-us-by-date; M.DCCC.LXIII read; host NOT_IN_COPYRIGHT | Metadata read; text file fetched (1.18 MB) and sampled at opening, middle and end, October 2026. Vendored. |
| The Book of Duarte Barbosa, vol. II | Duarte Barbosa | M. L. Dames | 1921 | https://archive.org/details/in.ernet.dli.2015.47303 | pd-us-by-date; 'issued for 1921' read; Hakluyt second series No. XLIX | Metadata read; text file fetched (904 KB) and sampled at opening, middle and end, October 2026. Vendored. Volume I (in.ernet.dli.2015.47302) covers the northern coasts and was not opened. |
| The Monks of Kublai Khan / Histoire de Mar Jabalaha III | Syriac life | Budge (1928) / Chabot (1895) | 1928 / 1895 | https://archive.org/details/monksofkublaikha0000unse and https://archive.org/details/histoiredemarja00chab | pd-us-by-date | See the Timur-to-Hakkari dossier. Both vendored. |
| Cathay and the Way Thither, vol. II (Odoric of Pordenone and others) | Odoric of Pordenone | Yule, revised by Cordier | 1913 | https://archive.org/details/cathaywaythither02yule | pd-us-by-date; 'issued for 1913' read | Metadata read; text file fetched (1.1 MB) and word-counted, October 2026. Not vendored: Odoric's Polumbum (Quilon) paragraphs describe nakedness and ox-worship but no Christians; the volume's Nestorians are in China, so it belongs to the Mongol-era world. |
| Christianity in Travancore | Gordon Thomson Mackenzie | Mackenzie | 1901 | https://archive.org/details/ChristianityInTravancore | pd-us-by-date; host Public Domain Mark 1.0 | Metadata read; text file fetched (310 KB), October 2026. Not vendored: a state-commissioned history of the missions, scholarship rather than a source. |
| The Syrian Church in India | George Milne Rae | Rae | 1892 | https://archive.org/details/syrianchurchinin00raegrich | pd-us-by-date; host NOT_IN_COPYRIGHT | Metadata read; text file present (562 KB); not fetched, October 2026. Not vendored: nineteenth-century scholarship. |
| Die Kirche der Thomaschristen | Wilhelm Germann | Germann (German) | 1877 | https://archive.org/details/diekirchedertho00germgoog | pd-us-by-date; host NOT_IN_COPYRIGHT | Metadata read; text file present (2.05 MB); not fetched, October 2026. Not vendored: German scholarship using the same sources. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Assemani BO III.1 as the "1504 letter" | The census names the bishops' letter of 1504. | Not closed: vendored. The Latin of the letter is in III.1 at file line 93562. The Syriac original is not in the library. No English translation of the whole letter was found; Mingana prints parts of the colophons. |
| Vatican Syriac 22, the Cranganore colophon of 1301, as a manuscript text | The census names it as the oldest dated Syriac manuscript from India. | The manuscript is not on archive.org. Mingana's article translates the colophon (file lines 3520 to 3547). Check against the Syriac before quoting. |
| Mingana's numbering of the patriarch | The census says the 1301 colophon names Yahballaha III. | Mingana's translation reads "Mar Yahb Alaha V., the Turk". The patriarch is the same person whichever numeral is used; flagged for Doc_01 as a name to settle. |
| Giamil, Genuinae relationes (Rome, 1902) | Mingana cites it for the colophons' printed texts. | Not searched on archive.org beyond one title query; not found. Lead only. |
| Marco Polo, Book of Ser Marco Polo, ed. Yule and Cordier (1903) | He describes the shrine of St Thomas at Maabar. | Found on archive.org (for example bookofsermarcopo02polouoft); not opened. The book dates from about 1300, the edge of the window. Lead only. |
| Pedro Álvares Cabral's voyage and the narrative of Joseph the Indian | The Portuguese met a Malabar priest in 1501 and took him to Portugal. | The Hakluyt edition of Cabral's voyage is of 1938 (in copyright). The 1507 Italian collection (Paesi novamente retrovati) that prints Joseph's account was not found as a text. Lead only. |
| Cathay vol. II (Odoric) | A traveller who passed Quilon in the 1320s. | See section 3. Not vendored. |
| Hough, History of Christianity in India (1839) | A standard Protestant history. | After the window and already on the shelf; the part on the earlier church was not searched for Jordanus or Marignolli (no hits for either). |
| Francis Xavier's letters (Monumenta Xaveriana) | The Portuguese missionary view. | After the window; on the shelf for other worlds. |

## 5. Open cross-world questions

- **Timur-to-Hakkari world (V.17).** The Indian province is "the one Timur never reached", so each world reads the other. Which world owns the 1504 letter, Mingana and the Budge and Chabot lives of Yahballaha III is for Step 0 on both. The files are staged for both.
- **The earlier world (`st-thomas-christians-of-india`, 849–1054), and the later one (`st-thomas-christians-under-portuguese-pressure-d`, 1599–1665).** Neale's Malabar rite, Raulin and Vincenzo Maria sit across the windows. Where one world ends and the next begins is a boundary to state.
- **The patriarch's numeral.** The census says Yahballaha III; Mingana's translation of the 1301 colophon says V. Which numbering the program uses is for Doc_01.
- **Mar Jacob.** The census names "Mar Jacob" as one of the bishops sent after the delegation of about 1490. The colophon of 1301 also names a Metropolitan Mar Jacob in the time of Yahballaha. These are probably two different men. Do not merge them.
- **Portuguese-period fiction about Christians.** The Roteiro reports "Christians" at Calicut that were Hindus. The record of that mistake is the evidence, not a record of the Malabar church.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says "No question — the same communion this church has always been in." Nothing found disturbs that. The 1301 colophon prays for the patriarch of the East by name, and Varthema records that the Christians "keep Easter like ourselves ... but they say mass like the Greeks" and that a priest comes from Babylon every three years. The church's belief is that of the Church of the East; whether the Malabar church in this window held anything beyond it is not suggested by these files. I did not read the Assemani Latin through for Christology.

**Sourcing (B1).** The census says "Thin, though richer than in the previous period", and that fits. The window has an unusually good run of outsiders in public-domain English: Jordanus (in the East from about 1321, bishop by 1330), Marignolli (legate; back at Avignon in 1353), Conti (twenty-five years in the East, home in 1444), the Roteiro (1498), Varthema (1503 to 1508) and Barbosa (about 1518). It has a short run of the community's own colophons in Mingana's English and the Latin of the bishops' history and letter. It has no full English translation of the 1504 letter.

**Ecology (B2).** Outsiders from several directions look at one community: a Latin missionary bishop, a papal legate, a Venetian merchant, a traveller from Bologna, a Portuguese author. The community speaks through scribes and bishops in short pieces. The shape is good for a conversation that tests whose account is believed: the outsiders' pictures disagree about what the Christians know and how they live, and the colophons give the community's own account of what it is. The risk is that the Representative could be made to sound more fluent than the colophons allow.

**Uniqueness (B3).** The earlier world is the church before the Mongols, the later one is the church under Portugal. Against V.17 the difference is the place and the survival. Each overlap is a boundary to state.

**Audiences (B4).** Several million Christians in Kerala and abroad trace themselves to the Thomas tradition and to the churches that came out of this community: the Syro-Malabar and Syro-Malankara Catholics, the Malankara Orthodox and Jacobite Syrian churches, the Mar Thoma Church. The audience is large and reachable.

**Scale (B5).** About 7.1 MB vendored in this pass for V.23 (eight files, not counting Budge and Chabot, which are counted in the Timur-to-Hakkari dossier). The attached outsiders are all short passages inside larger books, so the Doc_02 reader should work from the contents entries.

**Recommendation: build.** The church speaks in its own voice in short pieces (the 1301 colophon, Mar Jacob's colophons, the bishops' letter) and six outsider witnesses speak about it in clean English. The audience is large. The cost to say up front: the community's own voice runs to a few pages, and the 1504 letter is Latin with no English. A Doc_02 should read the Assemani Latin and Mingana's colophons first and decide, before the build counts the voice as secure, how much a Representative can say beyond them. If the pages prove too few, the nearest alternative is to treat the Malabar church as the Indian province of the Timur-to-Hakkari world rather than a world of its own. This is a recommendation for Mark to weigh, not a decision.
