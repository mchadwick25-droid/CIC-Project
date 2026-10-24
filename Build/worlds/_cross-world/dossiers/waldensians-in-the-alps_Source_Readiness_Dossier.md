# Source Readiness Dossier — The Waldensians in the Alps

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.16
**Corpus-map slug:** `waldensians-in-the-alps`
**Time window:** 1300–1517
**Region(s):** Cottian Alps (Piedmont and Dauphiné), Provence, Apulia, Germany
**Dossier author / date:** Era VI library session, latinwest batch, October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. Before this pass the bucket held five rows, all `provisional`, for Gilles, Léger, Morland and two Perrin files. This pass vendored nine files for it with staging files (validated with `corpus_map_merge.py --check`). Their registry entries, seed rows and the cross-link rows sit in the lead's snippet files until merged.

## 1. Already assigned

The first five rows were there before this pass. The last nine are the files vendored this pass. Scale is the vendored file size in characters, header included.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Histoire ecclésiastique des Églises Vaudoises, Tome I, the chapters on the valleys before 1532 (Gilles, 1881) | gilles | tradition | provisional | ~740K chars | `gilles_histoire-ecclesiastique-eglises-vaudoises-v1-fra_1881.txt` |
| Histoire générale, Livre premier, the "ancient" documents of the valleys (Léger, 1669) | leger | tradition | provisional | ~1.20M chars | `leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt` |
| The ancient manuscripts of the valleys as printed by Morland, Book I chapters V–VIII (1658) | morland | tradition | provisional | ~2.35M chars | `morland_history-evangelical-churches-piemont_1658.txt` |
| Histoire des Vaudois, Part I, the medieval chapters (Perrin, 1619) | perrin | tradition | provisional | ~432K chars | `perrin_histoire-des-vaudois-fra_1619.txt` |
| History of the Old Waldenses anterior to the Reformation (Perrin, English, 1847) | perrin | tradition | provisional | ~1.90M chars | `perrin_history-ancient-christians-valleys-alps_1847.txt` |
| La Nobla Leiçon, Old Occitan poem, critical text (De Stefano, 1909) | waldensians | tradition | assigned | ~310K chars | `waldensians_nobla-leicon-pro_destefano1909.txt` |
| La Nobla Leiçon with French translation (Montet, 1888) | waldensians | tradition | assigned | ~267K chars | `waldensians_nobla-leicon-pro_montet1888.txt` |
| The Waldensian catechism, critical text, and the Brethren's catechism (Zezschwitz, 1863) | zezschwitz | tradition | assigned | ~679K chars | `zezschwitz_katechismen-der-waldenser-und-boehmischen-brueder-deu_1863.txt` |
| The Romaunt (Waldensian) version of the Gospel of John (Gilly, 1848) | waldensians | tradition | assigned | ~479K chars | `waldensians_romaunt-gospel-of-john-pro_gilly1848.txt` |
| Histoire littéraire des Vaudois du Piémont, with extracts of the barbes' manuscripts (Montet, 1885) | montet | context | assigned | ~471K chars | `montet_histoire-litteraire-des-vaudois-du-piemont-fra_1885.txt` |
| Valdesi, Catari e Streghe in Piemonte, new archive documents (Gabotto, 1900) | gabotto | context | assigned | ~58K chars | `gabotto_valdesi-catari-streghe-in-piemonte-ita_1900.txt` |
| Über die Inquisition gegen die Waldenser in Pommern und der Mark Brandenburg (Wattenbach, 1886) | wattenbach | context | provisional | ~232K chars | `wattenbach_inquisition-gegen-die-waldenser-in-pommern-deu_1886.txt` |
| Waldenserthum und Inquisition im südöstlichen Deutschland (Haupt, 1890) | haupt | context | provisional | ~364K chars | `haupt_waldenserthum-und-inquisition-im-suedoestlichen-deutschland-deu_1890.txt` |
| Quellen und Untersuchungen zur Geschichte der Böhmischen Brüder, I: the Brethren and the Waldensians (Goll, 1878) | goll | context | provisional | ~478K chars | `goll_quellen-bohmische-bruder-v1-deu_1878.txt` |

**Voices.** The barbes speak in three genres in their own Old Occitan. *La Nobla Leiçon* is a poem of moral teaching (the De Stefano edition is clean; Montet's verse is garbled and is a second witness). The catechism is a barbes' teaching text of questions and answers (Zezschwitz prints it from the Dublin and Geneva manuscripts). The Romaunt Gospel of John is the Scripture the barbes carried and memorised. Montet's 1885 literary history and Morland's 1658 volume print extracts of the other books (*La Barca*, *Novel Sermon*, *Payre eternal* and others). No individual barba is named as a speaker; the church was built so that no single figure held it together, and the texts agree with the census on that.

**The 1487 crusade.** Pope Innocent VIII's bull of 1487 is listed in Morland's contents ("A Bull of Pope Innocent, against the Waldenses, in the year 1487", file line 4013) and in Léger's contents ("Une Bulle du Pape Innocent contre les Vaudois, de l'an 1487, en Latin", file line 4247). Léger's Livre premier prints the Latin text (the address to "Alberto de Capitaneis" is at file line 22499). Morland's narrative carries the commission to Albertus de Capitaneis and its aftermath (file lines 22329–22341 and 24419). Perrin's English of 1847 tells the same campaign (file lines 17885 ff.). These are seventeenth-century printings by Reformed Waldensians and their English patrons, not the bull's own register.

**Hostile records.** The Alpine valleys' own inquisition records are not on the shelf. What is vendored is Gabotto's offprint of dated Piedmont archive entries (Pinerolo accounts, fines, confiscations, prisoners), and, outside the Alps, the German protocols (Wattenbach 1886 on Pomerania and Brandenburg, Haupt 1890 on Bavaria, Austria and Bohemia). These are coerced answers recorded by their judges. The two German files stand on the census's "Germany" region; whether they belong to this entry is §5.

**Scan quality.** Clean: De Stefano. Readable: Zezschwitz, Gilly, Montet 1885, Gabotto, Haupt, Wattenbach 1886 (except a sideways table near its opening). Second witness: Montet 1888. Morland, Léger and Perrin are second witnesses for wording per the bucket notes.

## 2. Cross-link opportunities

Checked by searching the bodies of every `cic/texts/*.txt` for Waldensians, Vaudois, Valdenses, Pauperes de Lugduno, the barbes and the 1487 crusade, then opening the hits. Proposed rows are in the lead's `crosslinks.yaml`.

- **Bernard Gui, *Manuel de l'Inquisiteur*, tomes I and II** (Franciscan pass; placed on the Waldensians entry, not this one). Tome I has "[DE SECTA VALDENSIUM]" (file line 4807) and passages on the "Valdenses seu Pauperes de Lugduno" (file lines 2154–2162 and 3411). Tome II has the forms for abjuring the sect (file line 1880). A hostile inquisitor's description of the same community in Languedoc in the 1320s. Tier: same time-different-region. Proposed rows: context / provisional.
- **Limborch, *Liber sententiarum inquisitionis Tholosanae*** (Franciscan pass; placed on the Waldensians entry). Waldensian depositions ("pauperes de Lugduno") at file lines 22265–25522. Second witness (long s read as f). Tier: same time-different-region. Proposed row: context / provisional.
- **The Hussite files, Goll, *Quellen*, I** (vendored this pass; staged here as context). The Unity of the Brethren's dealings with Waldensians in the 1450s and later. Tier: same time-different-region.
- **Calvin's letters, Crespin's *Histoire des martyrs* and the union files** (bucket of the Waldensian-Reformed Union). They concern the Reformation union after 1532. Out-of-window for this entry.
- Noted, no row proposed: the bucket of the earlier Waldensians (`the-waldensians`) already holds the same Gilles, Léger, Morland and Perrin files as context.

## 3. Verified acquisition leads

Each lead was checked on the host: item record read, title page read in the OCR, text file fetched and sampled. The first eight rows are vendored (Goll's first part, the ninth vendored file, is listed on the Hussite dossier). Rights basis is public domain by date unless the row says otherwise.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| La noble leçon des Vaudois du Piémont. Texte critique, introduction et glossaire. Vendored as `waldensians_nobla-leicon-pro_destefano1909.txt`. | Antonino De Stefano (editor) | none (Old Occitan with French) | 1909 | https://archive.org/details/LaNobleLeconDesVaudoisDeStefa | pd-us-by-date; Public Domain Mark 1.0 on the item | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| La Noble leçon (Montet edition). Vendored as `waldensians_nobla-leicon-pro_montet1888.txt`. | Édouard Montet (editor) | none (Old Occitan with French) | 1888 | https://archive.org/details/lanobleleontex00mont | pd-us-by-date | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Histoire littéraire des Vaudois du Piémont. Vendored as `montet_histoire-litteraire-des-vaudois-du-piemont-fra_1885.txt`. | Édouard Montet | none (French) | 1885 | https://archive.org/details/histoirelittrai00montgoog | pd-us-by-date; NOT_IN_COPYRIGHT on the item | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Die Katechismen der Waldenser und Böhmischen Brüder. Vendored as `zezschwitz_katechismen-der-waldenser-und-boehmischen-brueder-deu_1863.txt`. | Gerhard von Zezschwitz | none (German with Old Occitan) | 1863 | https://archive.org/details/diekatechismende00zezs | pd-us-by-date | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| The Romaunt Version of the Gospel according to St John. Vendored as `waldensians_romaunt-gospel-of-john-pro_gilly1848.txt`. | William Stephen Gilly (editor) | none (Old Occitan) | 1848 | https://archive.org/details/MN41506ucmf_5 | pd-us-by-date | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Über die Inquisition gegen die Waldenser in Pommern und der Mark Brandenburg. Vendored as `wattenbach_inquisition-gegen-die-waldenser-in-pommern-deu_1886.txt`. | Wilhelm Wattenbach | none (German with Latin) | 1886 | https://archive.org/details/gtu_32400002864738 | pd-us-by-date | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Waldenserthum und Inquisition im südöstlichen Deutschland. Vendored as `haupt_waldenserthum-und-inquisition-im-suedoestlichen-deutschland-deu_1890.txt`. | Herman Haupt | none (German with Latin) | 1890 | https://archive.org/details/waldenserthumund00haup | pd-us-by-date | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |
| Valdesi, Catari e Streghe in Piemonte dal secolo XIV al XVI. Vendored as `gabotto_valdesi-catari-streghe-in-piemonte-ita_1900.txt`. | Ferdinando Gabotto | none (Italian) | 1900 | https://archive.org/details/gabotto-valdesi-catari-streghe | pd-us-by-date | October 2026: item metadata read; title page read in the OCR; full-text file fetched directly and sampled at opening, middle and end. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Comba, *History of the Waldenses of Italy* (Truslove and Shirley, 1889; `historyofwaldens00comb`, `cu31924029440512`) | Standard English history; named in the task | Scholarship, not a source. Fetched (1.16 MB) and sampled clean (0.83–0.9). Not vendored. |
| Muston, *The Israel of the Alps* (Montgomery's translation, 1866; `israelalpsacomp00montgoog`) | Complete English history including the 1487 crusade; named in the task | Scholarship, not a source. NOT_IN_COPYRIGHT; the 1.66 MB text file is listed and was not fetched. |
| Gilly, *Waldensian Researches* (1831; `waldensianresear00gill`) and *Narrative of an Excursion to the Mountains of Piemont* (1824–1827) | Named in the task; Gilly collected the Dublin manuscripts | A traveller's inquiry and argument. The 1831 volume was fetched (971 KB) and sampled clean; the 1824 narrative was listed only. The texts Gilly quotes are in the files already on the shelf; his Gospel of John is vendored. |
| Herzog, *Die romanischen Waldenser* (Halle, 1853; `dieromanischenwa00herz`) | Named in the task; documents on the pre-Reformation valleys | The Fraktur is read as noise, word-form coverage 0.22–0.42. OCR-unusable. Secondary in any case. Not vendored. |
| Dieckhoff, *Die Waldenser im Mittelalter* (1851; `diewaldenserimmi00diec`) and Müller, *Die Waldenser und ihre einzelnen Gruppen bis zum Anfang des 14. Jahrhunderts* (1886; `diewaldenserundi00mull`) | German scholarship on the medieval Waldensians | Scholarship. Müller ends at 1300, outside the window. Listed, not fetched. |
| Preger, *Ueber die Verfassung der französischen Waldesier in der älteren Zeit* (1890; `ueberdieverfassu00preg`) | The Waldensian organisation | About the earlier period; metadata only. Preger's *Beiträge zur Geschichte der Waldesier im Mittelalter* (1875) was not found on the host. |
| Raynouard's printing of *La Nobla Leiçon* (*Choix des poésies originales des troubadours*, 1817) | The earliest printed edition | Not searched on the host. Morland (1658) and Léger (1669) already print the poem. |
| Montet 1885, second scan (`histoirelitterai00mont`) | A cleaner scan | Every fetch returned a server error. The vendored scan (`histoirelittrai00montgoog`) reads well. |
| Goll, *Quellen*, Olms reprint of 1977 (`quellenundunter00gollgoog`) | Same book | A 1977 reprint of both parts as one volume; the 1878 and 1882 scans (`quellenundunters01goll`, `quellenundunters02goll`) were used instead. |
| Cattaneo's crusade and the Dauphiné inquisition records (Embrun, Freissinières, Val Louise) | The 1487 record and the Alpine inquisition | Searches by title and place on the host found nothing. The *Bulletin de la Société d'histoire vaudoise* was not found as a series; Gabotto's offprint of number 18 is vendored. A full-text search for the bull and the crusade found only secondary prose. |
| Döllinger, *Beiträge zur Sektengeschichte des Mittelalters* II (1890; `beitrgezursekt02dl`) | Documents on Waldensians, Cathars and Free Spirit heretics | A shared lead: the Franciscan pass had this item in its download folder when checked. Grep the shelf before relying on it. |

## 5. Open cross-world questions

- **Alps, Germany or Languedoc.** The census lists "Germany" and "Provence" among the regions. Wattenbach 1886 and Haupt 1890 are German records of German-speaking communities outside the Alps, and Gui and Limborch are Languedoc. Each is staged here as context (provisional) and the Gui and Limborch rows sit on the earlier Waldensians entry. Whether a Representative of the Alps can use them is for Step 0.
- **The earlier Waldensians (`the-waldensians`, c. 1173 onward) and the Union (`the-waldensian-reformed-union`, 1532 onward).** The five bucket files are also assigned to the earlier entry (context). The line between a medieval underground church and the 1532 union is the line between three entries. State it in Step 0.
- **The dating of the barbes' books.** The editions argue the Nobla Leiçon's date (1100 or 1400 by the manuscripts' readings), and Morland and Léger date their manuscripts to the twelfth century where modern scholarship dates most of them to the fifteenth and early sixteenth. Doc_01 should carry the contested date and say which manuscripts are inside the window.
- **Voice or context for the 1619–1669 histories.** Gilles, Léger, Morland and Perrin are the community's own account written a century or more after the window. The bucket notes already ask whether this is voice or context.
- **The Unity of the Brethren.** Goll's first part and Zezschwitz's Brethren catechism bear on the Hussite entry as well as this one. Placing a text in two worlds records that each reads a different part.
- **The Representative.** No barba is named. The census says the church's continuity rested on the circuit of preachers and the households that sheltered them. Whether a Representative can be built on an anonymous collective voice is a Representative-identity question.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says no question: the charge against them was discipline and obedience, not doctrine. This pass did not test it against the texts. Nothing found disturbs it. Doc_01 should read the catechism's and the Nobla Leiçon's treatment of the sacraments and the saints before the floor is confirmed.

**Sourcing (B1).** The census says the barbes' manuscript books and the inquisition records, with the 1487 bull from both sides. The books are on the shelf in Old Occitan (the poem, the catechism, the Gospel, extracts of the treatises). The inquisition records of the valleys themselves are not; Gabotto's archive entries and the German and Languedoc protocols stand in for them. The 1487 bull and crusade are on the shelf only as printed by Morland, Léger and Perrin.

**Ecology (B2).** Three layers: the barbes' own books, the hostile record that names the heretics, and the Reformed histories that preserved the manuscripts. The risk the sources show: the community's own voice is anonymous and the named individuals are defendants.

**Uniqueness (B3).** Against the earlier Waldensians the difference is the century of survival as an underground church and the 1487 crusade. Against the Union the difference is the choice of 1532, which falls after the window.

**Audiences (B4).** The Waldensian Evangelical Church still exists in the same valleys, with sister churches in South America and the United States. The audience is reachable and invested.

**Scale (B5).** About 3.3 million characters in nine vendored files, plus 6.6 million in the five bucket files that were already on the shelf.

**Recommendation: build.** The movement speaks in its own vendored texts in three genres, one of them in a clean critical edition (B1). A public-domain English leg exists for the poem and the catechism in Morland (1658) and Perrin (1847). The hostile record is thin for the Alps and thick for Germany and Languedoc. The cost to say up front is that the voice is a collective with no named speaker and that the dating of the books is contested; both belong in Step 0 and Doc_01. This is a recommendation for Mark to weigh, not a decision.
