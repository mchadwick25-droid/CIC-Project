# Step 0 — Eras 8 and 9 global completeness sweep, by region and by river · V1.0

**Status: draft for Mark's gate; nothing changes the census until he rules; eras 8 and 9 are frozen, so every addition is a change order.** This record is P2-G89. It gathers five research passes into one record: four regional passes (Africa; Latin America and the Caribbean; Asia and the Pacific; the Middle East, Caucasus, Russia and Eastern Europe) and one rivers pass, which cross-checked the four across every river and settled where they disagreed. The pass files sit in `Build/Ministry/Operations/Audits/2026-11-10_g89-sweep/passes/`. Each pass body is reproduced in sections 3 to 7 as it was written. The only changes are British to American spelling in the passes' own prose, heading levels, and a one-line note at the head of each candidate the rivers pass gave a new home. The questions in section 8 are numbered G89-1 onward. Nothing here is decided. An independent review comes next, capped at three rounds.

---

## 0. What governs the sweep

### Mark's rulings

- **Scope (2026-11-09).** "eras 8 - 10 for now". Era 10's sweep is done (data release 25). This record covers eras 8 and 9, 1650 to 1906.
- **By region and by river (2026-11-09).** Mark chose "1 and across the rivers too". So the sweep runs region by region, and within each region river by river: Catholic; Orthodox (Eastern and Oriental); Protestant and Evangelical, Anglican included; Syriac and other Eastern churches; Eastern Catholic churches; and independent, indigenous or slave-born Christianity where present. The rivers pass then checked each river across all regions.
- **Non-English sources (2026-11-09).** "look at non-english sources too, like we have in other eras". Each pass searched its region's own languages beside English. What each reached, and what it did not, is stated in its body and in section 9.
- **The timeline breaks (2026-11-10).** Mark ruled to log the breaks, not sweep them on their own (option c), "but check that they are unique and not tied to other movements, like jesuites moving around the world, that is a single movement". The breaks are in Open-Gaps 142, and Open-Gaps 135 holds the gaps waiting for sources (both in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`). Every break that falls in 1650-1906 is answered in section 2b, with the result of that uniqueness test.

### The evidence rule for these eras

These eras fall before about 1930, so the Library rule applies, as in eras 1 to 9. Texts come first from `cic/texts/` and `cic/corpus-map/`. Public-domain editions online (archive.org and the like) count only when opened raw and read. WebFetch output is a model's summary. It is never quoted and never counts as read. Studies come next, ideally by scholars from or of the region. Only a verified item carries a sentence.

### The four marks

A movement outside church bodies counts only as "a defined movement, not just a trend". It needs four marks: a beginning, carriers, a name, and recognition as a movement in a study. A church body, or a religious order or society inside a church, clears the floor without them. The passes apply the marks where a candidate is a movement (for example LA8-3 Canudos, AF-6, AP10, AP13 and RV-9).

### Rulings that do not apply here

The era 10 online-evidence rules were made for era 10 links: the cap at Widely Accepted, the `verified-online` state, and membership rolls. So was the later ruling that a "member of" link may be Widely Accepted on the council's own dated membership record (Open-Gaps 146). None of these applies in eras 8 and 9 unless Mark extends them. No pass used them.

### Verification-state legends, as each pass wrote them

The five passes did not use one legend. Each is given exactly as written. An [S] item never counts as verified in any of them.

**Africa**

> **Verification states** (the brief's own).
> - **V**: I opened the item in this run and confirmed the detail. Library files are named by file; online items were opened raw with curl from archive.org (`_djvu.txt` derivative), and the item identifier is given.
> - **V-s**: a study's details only (bibliographic record or a citation in the repo), not its content.
> - **[S]**: snippet, summary, memory or unopened. An [S] item never counts as verified.
> - Only V carries a sentence.
> - **Quotes from OCR.** Quoted words come from raw OCR text. The long s is read as s, and plain OCR letter slips (for example "wich" for "with") are mended. Each quote should be checked against the page image before any census use. Every V source below is pre-1930 and public domain by date. Most are outside witnesses (missionaries, travelers, consuls); that is said for each.

**Latin America and the Caribbean**

> **Verification key (as the brief sets it).** **V** = I opened the item in this run (a Library file
> in `cic/texts/`, or a public-domain edition fetched raw with curl) and confirmed the detail; file and
> line, or URL, given. **V-s** = the detail is seen only in a study's own statement (in the repo or in
> an opened study), not in the primary. **[S]** = snippet, summary, memory, or unopened. Only V carries a
> sentence. Original-language titles come first, with an English gloss; renderings marked
> [my rendering] are this researcher's own.

Latin America added one state of its own, "V (bib)", set out in its Library check:

> Open Library catalog records, fetched raw as JSON, confirm bibliographic details only; such items are marked **V (bib)**, and nothing in their contents counts as read.

**Asia and the Pacific**

> **Verification key.** **V** = I opened the item in this run (a Library file in `cic/texts/`, or a
> public-domain edition opened raw with curl) and confirmed the detail; the locus is given. **V-s** = a
> study's bibliographic details only, confirmed in this run from a catalog record opened raw
> (archive.org metadata, NDL Search); its contents were not read. **[S]** = snippet, summary, memory or
> unopened; never counts as verified. **wanted** = searched for, not found. Only V carries a sentence.
> English renderings of French, Latin or Japanese marked [my rendering] are this researcher's own.

**Middle East, Caucasus, Russia and Eastern Europe**

> **Verification states.**
> - **V** = I opened the item in this run (a Library file in `cic/texts/`, or a public-domain edition fetched raw with curl) and read the detail there. Where the item is a study (for example a 1908-1912 Catholic Encyclopedia article), "V" means the study says it; the study's own stance is named.
> - **V-s** = the detail rests only on a study's report of an item I did not open.
> - **[S]** = snippet, summary, memory or unopened. Never verified.
> - Only V carries a sentence.

**Rivers cross-check**

> - **V**: opened in this run (a `cic/texts/` file, or a public-domain edition fetched raw with
>   curl) and the detail confirmed. Raw downloads sit in the session scratchpad, not the repo.
> - **V-s**: a study's bibliographic details only (a catalog or search record seen).
> - **[S]**: snippet, summary, memory or unopened. Never verified.
> - Only V carries a sentence. Quotes from OCR keep the source's spelling; check the page image
>   before any census use. Every V source below is before 1930 and public domain by date.
> - "V (pass)" means a regional pass opened it; this pass relies on that pass's record.

**Reading across.** All five passes use V, V-s and [S], and in all five only V carries a sentence. But V-s does not mean the same thing in each.
- In Africa, Asia and the rivers pass, V-s means a study's bibliographic details only. Asia and the rivers pass add that they come from a catalog or search record.
- In Latin America and the Middle East, V-s means a detail seen only in a study's report of a primary that was not opened.
- Latin America's "V (bib)" is close to what Africa, Asia and the rivers pass call V-s.
- Asia adds **wanted**, for an item searched for and not found.
- The rivers pass adds **V (pass)**, for an item a regional pass opened, relied on through that pass's record.

---

## 1. Where the roster stood

Computed from `cic-website/data/world-census.json`, data release 28 (2026-11-10): 322 movements. An entry with more than one region value is counted in each of its regions, so the region counts add up to more than the entries.

| Era | Entries | North Europe | North America | Mediterranean | Asia Minor | Middle East | Caucasus | Greater Asia | Pacific | Africa | Latin America |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 (1650-1815) | 30 | 18 | 2 | 9 | 4 | 2 | 1 | 1 | 0 | 1 | 1 |
| 9 (1815-1906) | 51 | 24 | 21 | 4 | 3 | 1 | 1 | 7 | 2 | 5 | 1 |

Era 8 has 30 entries, and 18 of them carry North Europe. Africa, Latin America and Greater Asia have one each. Era 9 has 51 entries and 69 region tags; 45 of the tags are North Europe or North America. Africa has 5, Greater Asia 7 and Latin America 1.

The rivers show the same lean. In era 8, the Protestant and Evangelical river has 12 entries, 10 of them in North Europe. In era 9 it has 23 entries, carrying 17 North Europe tags and 12 North America tags. The Syriac East and Asia lane has no entry in era 8 and one in era 9. The Africa lane has one entry in era 8 and four in era 9.

The atlas IDs follow the eras: VI.x is era 7, VII.x era 8, VIII.x era 9 and IX.x era 10.

---

## 2. Summary of findings

Every candidate from the five passes is listed once: 9 from Africa, 11 from Latin America (10 candidates and the Moravian question G-LA8-M), 17 from Asia (15 candidates and two cross-region questions), 22 from the Middle East (11 candidates and 11 named lines and routings) and 9 from the rivers pass. That is 68 rows. The ID is the pass's own. Section A states and recommendations are the passes', condensed; the full text is in sections 3 to 7.

**The rivers pass's resolutions are applied.** Where it gave a regional item a new home, the row says so. A row whose item now lives inside another candidate is marked "not counted" in the Class column, so nothing is counted twice. Six rows are marked so: LA8-2, LA8-M, AP-X1, ME-11, ME-12 and ME-22. Where a regional pass and the rivers pass differ, the Recommendation column gives the rivers pass's answer and names the regional one.

**Classes.** Each counted row takes one of five classes:
- **enter**: a new row is recommended now (for some, one part now and the other part later);
- **enter once (condition)**: entry waits on a named condition;
- **named line**: a line in an existing row or in another candidate, not a row;
- **hold**: held for sources or for a Section A ruling;
- **out of scope / already carried**: no addition.

| ID | Candidate | Kind | River / lane | Dates | Era | Tier | Section A state | Recommendation | Class |
|---|---|---|---|---|---|---|---|---|---|
| AF-1 | Ethiopian Christianity: Gondar to the Zemene Mesafint (logged break) | church body | 4 Africa | 1650-1855 | 8-9 | 1 | clear by precedent (same church as VI.25 and VIII.49); no dated own statement read | enter a new row between VI.25 and VIII.49; Ge'ez-rite Catholics (AF-7) and the CMS mission of 1830 (AF-9) as named lines; an "in contact with" link to AF-2 (rivers §1e) | enter |
| AF-2 | The Coptic church under the Ottomans: the patriarchate and the archons (logged break) | church body | 4 Africa | 1517-1854 | (7)-8-9 | 1 (whole break); 2 if 1650-1854 only | clear by precedent (VIII.13 floorNote "No question") | enter, from 1517, with 1300-1517 logged as its own break; archons and Coptic Catholics as named lines. Rivers: the American Mission in Egypt goes to RV-4, with a link from VIII.13 | enter |
| AF-3 | Kongo Christianity after 1650: the Capuchin century and the Kongolese lay church (new break) | church body (regional window of the Catholic Church) | 4 Africa, or 4-5 bridge | 1650-c. 1880s | 8-9 | 1 (1650-1720); 2 later, on sources | clear (Catholic) | enter a new row, with VII.11 inside its span | enter |
| AF-4 | The Dutch Reformed Church at the Cape | church body | 6 Protestant & Evangelical | 1652-1906 | 8-9 | 1 | clear: Heidelberg Catechism, Belgic Confession, Canons of Dort (McCarter 1869, V) | enter a row; Huguenots, the Trek churches and 1857/1881 as lines. Rivers: Southern Africa's home is settled once, with AF-5 (G89-5) | enter |
| AF-5 | Southern African mission churches: Khoikhoi, Xhosa and Sotho Christianity | regional set of mission-born church bodies | 6 Protestant & Evangelical | 1737-1906 | 8-9 | 2 as a VIII.7 wing; 1 as its own row | clear (mainline Protestant) | Africa: a fifth wing in VIII.7 and a VII.4 Cape line. **Re-homed by the rivers pass (§1c):** its own entry, not a VIII.7 wing; the Moravian Cape mission is a line in VII.4 before 1815 and in RV-5 after. Its own row, or one Cape row with AF-4 (G89-5) | enter |
| AF-6 | The Catholic mission revival in nineteenth-century Africa | movement inside one church (missionary congregations) | 5 Latin West & Catholicism | c. 1830-1906 | 9 | 2 | clear (Catholic) | named line in VIII.29, with an edge VIII.29 to IX.59. Rivers: the line is widened to the worldwide Catholic mission revival (Africa, Asia, Oceania), and MEP, the Lazarists and the restored Jesuits sit in it | named line |
| AF-7 | Eastern Catholic lines: Coptic Catholics and Ge'ez-rite Catholics | two small Eastern Catholic bodies | 4-5 bridge | 1741-1906 | 8-9 | 3 as rows | clear | named lines in AF-2 and in AF-1 / VIII.49 | named line |
| AF-8 | West Africa before the mission societies: forts, chaplains, first African clergy | set of figures and small congregations | (not stated) | 1650-1793 | 8 | hold | clear (Reformed, Anglican, Baptist, Methodist) | hold as named lines (VII.20, VII.16) for sources | hold |
| AF-9 | Protestant missions in Egypt and Ethiopia | mission churches | (not stated) | 1752-1906 | 8-9 | lines | clear | Africa: named lines in VIII.13, VII.4 and AF-1 / VIII.49 / IX.20. **Partly re-homed by the rivers pass:** the Egypt mission goes into RV-4 (VIII.13 keeps a link); the Moravians in Cairo and Algiers stay a VII.4 line; the CMS and Swedish lines stay as Africa proposed | named line |
| LA8-1 | The Caribbean churches of slavery and emancipation | cross-church regional row | Protestant & Evangelical | 1815-1906 | 9 | 1 | no question for the mission churches; Native Baptists not yet assessable (line only) | enter one cross-church row; Native Baptists and the 1860-61 revival as lines. Rivers: the Moravians in it are RV-5's lines, linked from LA8-1 | enter |
| LA8-2 | The Jesuit reductions of Paraguay and the expulsions from the Americas | named line (fails the uniqueness test as its own row) | Latin West & Catholicism | 1609-1768 | 8 | 1 inside a Jesuit row | no question | **Re-homed by the rivers pass into RV-1**, as a line in the Society of Jesus row (G89-1) | not counted (in RV-1) |
| LA8-3 | Canudos (Belo Monte); Juazeiro and Tomóchic as lines | movement within popular Catholicism (four marks met) | Latin West & Catholicism | 1893-1897 | 9 | 2 (1 if era 9 is to carry one popular Catholic movement) | no question | enter its own movement row; Juazeiro and Tomóchic as lines in VIII.48 | enter |
| LA8-4 | Colonial Brazil's Catholicism: rosary brotherhoods, Vieira, mill chapels | church body strand | Latin West & Catholicism | 1650-1822 | 8 | 1 strand | no question | named strand in VII.17 by change order (Brazil added to its text, voices, place and countries) | named line |
| LA8-5 | Priests in the wars of independence: Hidalgo and Morelos | seam line | Latin West & Catholicism | 1810-1815 | 8/9 | 1 line | no question | line in VIII.48, with VIII.48's start moved to 1810 | named line |
| LA8-6 | Haiti before 1804 and after 1860 (Holly) | lines | Latin West & Catholicism | 1685-1804; 1860-1906 | 8-9 | 2 | no question | hold for sources | hold |
| LA8-7 | Protestant beginnings in Latin America | lines | Protestant & Evangelical | 1818-1906 | 9 | 2 | no question | lines in VIII.41 (Brazil's Lutherans) and a pre-1916 line in IX.63 | named line |
| LA8-8 | Cuba and Puerto Rico under Spain | line | Latin West & Catholicism | 1815-1898 | 9 | 2 | no question | hold; then a line in VIII.48 | hold |
| LA8-9 | The Bethlemites (Guatemala) | line | Latin West & Catholicism | 1650s-1820 | 8 | 2 | no question | hold; then a line in VII.17 | hold |
| LA8-10 | The Virgin of Cancuc (1712) and the Talking Cross (1850-1901) | indigenous movements | Latin West & Catholicism | 1712; 1850-1901 | 8-9 | 2 | Cancuc Catholic in form; the Talking Cross a real Section A question | hold for sources | hold |
| LA8-M | The Moravian church after 1815 (a break this pass found; gate G-LA8-M) | continuation of VII.4 | Protestant & Evangelical | 1815-1906 | 9 | — | VII.4's floor | Latin America: log it in Open-Gaps 142 now. **Answered by the rivers pass as RV-5** | not counted (in RV-5) |
| AP1 | The St Thomas Christians: two obediences (logged break) | church body | Syriac East & Asia | 1665-1815 | 8 | 1 | clears on dated texts of both parties (Whitehouse App. D: Mar Evanius 1678) | enter one era 8 row for both parties; a link to ME-1 for Mar Gabriel, who reached Malabar in 1708 (rivers §1e) | enter |
| AP2 | Chinese Catholicism: the court mission, the Rites controversy and the hidden provinces (logged break) | church body | Latin West & Catholicism | 1650-1906 | 8-9 | 1 | clears (Catholic, Nicene) | enter a China-church row; the Jesuit court mission and the Rites as named lines; the era 9 half after one verified era 9 source. Rivers: AP2 is the one home of the Rites controversy; RV-1 links to it; MEP named in it as a carrier | enter |
| AP3 | Japan's hidden Christians (Sempuku Kirishitan) (logged break) | church body without clergy | Latin West & Catholicism | 1650-1865 | 8-9 | 1 | not assessable on a dated statement; world-level per A5 as continuation of VI.13b | enter one row across the era line | enter |
| AP4 | Vietnamese Catholicism | church body | Latin West & Catholicism | 1650-1906 | 8-9 | 1 | clears (Catholic; de Rhodes, *Cathechismus*, 1651) | enter as two segments split at 1815; MEP named as carrier (rivers §1b) | enter |
| AP5 | Protestant churches of the VOC world: the Moluccas, Batavia, Ceylon | church body | Protestant & Evangelical | 1650-1815 | 8 | 2 | clears (teachers bound to the Heidelberg Catechism and the Dutch Reformed Confession) | enter an era 8 row (or a line in VIII.26) | enter |
| AP6 | The Catholics of Ceylon under Dutch rule and the Goan Oratorians | church body | Latin West & Catholicism | 1658-1806 | 8 | 2 | clears (Catholic) | enter: a Ceylon row (better evidenced), or the first line of a wider South Asian Catholic row, 1650-1906, if one telling is wanted | enter |
| AP7 | Catholic St Thomas Christians and the Chaldean Syrian body at Thrissur | church body | Syriac East & Asia | 1815-1906 | 9 | 2 | clears [S on a dated text] | hold; then extend AP1 to 1906; a link to VIII.40 for the Chaldean bishops sent to Thrissur in 1861 and 1874 (rivers §1e) | hold |
| AP8 | The Tamil Lutheran church of Tranquebar and Tanjore after Ziegenbalg | church body | Protestant & Evangelical | 1706-1815 | 8 | 3 | clears [S on a dated statement] | named line in VII.2 | named line |
| AP9 | The Karen Baptist movement in Burma | church body | Protestant & Evangelical | 1828-1906 | 9 | 3 | clears [S] | Asia: a named line in VIII.7. **Re-homed by the rivers pass (§1c):** a named line in VIII.27, whose hill revivals already hold that kind | named line |
| AP10 | The Cofradía de San José (Hermano Pule) | movement inside a church body | Latin West & Catholicism | 1832-1841 | 9 | 3 | (not stated) | hold; then a line in VIII.39, once a dated primary is read | hold |
| AP11 | The Russian Ecclesiastical Mission in Peking and the Albazinians | church body | Greek East & Orthodoxy | 1685/1715-1906 | 8-9 | 3 | (not stated) | hold; then a line in VIII.31 (ME-18 also routes Peking to Asia; rivers: consistent) | hold |
| AP12 | Christianity in colonial Australia and New Zealand | church bodies | several | 1788-1906 | 9 | 3 | (not stated) | hold; then lines in the parent rows | hold |
| AP13 | Māori Christianity and the prophetic movements: Pai Mārire and Ringatū | cross-church movement | (beyond the floor, register) | 1862-1906 | 9 | 2 | not assessable; likely beyond the floor [S] | hold for a Māori source, with an era 9 movement row as the target | hold |
| AP14 | The Pacific Christian kingdoms: Tahiti, Hawai'i, Tonga, Fiji, Samoa | church bodies | Protestant & Evangelical | 1797-1906 | 9 | — | — | carried by VIII.7 | out of scope / already carried |
| AP15 | Korea, 1884/1886-1906 | church bodies | Protestant & Evangelical / Latin West & Catholicism | 1884-1906 | 9 | 3 | (not stated) | hold; then named lines | hold |
| AP-X1 | Does the Society of Jesus need an era 8 continuation? (cross-region question) | church body (order) | Latin West & Catholicism | 1650-1814 | 8 | — | — | Asia: decide at the merge, leaning no. **Answered by the rivers pass as RV-1** | not counted (in RV-1) |
| AP-X2 | A Missions Étrangères de Paris / Propaganda row? (cross-region question) | church body (society) | Latin West & Catholicism | 1658-1906 | 8-9 | — | — | carrier lines only, no row. Rivers (§1b) agrees: Propaganda as named lines in VII.19 and VIII.29; MEP named in AP2, AP4, VIII.21 and VIII.45, and inside AF-6's widened line | named line |
| ME-1 | The Church of the East: three patriarchates, from Diyarbakır to the Chaldean union (logged break) | church body | 1 Syriac East & Asia | 1650-1815 | 8 | 2 | no floor question; own statement: Yohannan Hormizd's autobiography (Badger's translation) | enter a new era 8 row between VI.30 and VIII.40; a link to AP1 for Mar Gabriel (rivers §1e) | enter |
| ME-2 | The Maronite Church: from Duwayhī and the Synod of Mount Lebanon to the Mutasarrifate (logged break) | church body (Eastern Catholic) | 1 Syriac East & Asia | 1650-1815; 1815-1906 | 8, 9 | 1 (era 9), 2 (era 8) | no floor question | enter era 9 now; era 8 after the 1736 synod acts are opened; 1517-1650 to the era 7 owner | enter |
| ME-3 | The Georgian Church between Persia, the Ottomans and Russia, to the end of the catholicate; and the Exarchate (logged break) | church body | 2 Caucasus | 1650-1811; 1811-1906 | 8 (9 as a line) | 2 | no floor question | enter an era 8 row; the Exarchate as a named line in VIII.31, linked to IX.40 | enter |
| ME-4 | The two Melkite churches in the nineteenth century; and the Melkite held gap | church bodies | 3<->5 bridge | 1815-1906 (row); 1650-1724 (line) | 9 (8 as a line) | 1 (Catholic side), 2 (with the Orthodox side) | no floor question | enter one era 9 row for both churches; Macarius III and Euthymius as a named line in VII.23; 1009-1650 stays held | enter |
| ME-5 | The Old Believers in the nineteenth century: Nicholas I, the Belokrinitsa hierarchy and the toleration of 1905 (logged gap) | church body | 3 Greek East & Orthodoxy | 1815-1906 | 9 | 1 | no floor question (pre-Nikonian Nicene Creed; assessed at VII.7) | enter an era 9 row continued from VII.7 | enter |
| ME-6 | The spiritual Christians of Russia: Dukhobors, Molokans and the mystic sects | family of dissenting bodies | 8 Beyond the Floor, or 6 | c. 1760s-1906 | 8-9 | 2 (pending A) | not yet assessable; a floor question body by body (Khlysty and Skoptsy likely outside) | hold for Section A, body by body; then enter what clears | hold |
| ME-7 | The Syriac Orthodox Church and the Syriac Catholic split (held gap) | church bodies | 1 Syriac East & Asia | c. 1650-1906 | 9 | 2-3 | no floor question | hold for one in-region source, then an era 9 row | hold |
| ME-8 | The Romanian Greek Catholic Church of Transylvania: the union of Alba Iulia to Blaj | church body (Eastern Catholic) | 3<->5 bridge | 1698-1906 | 8 (+9) | 1 (era 8), 2 (era 9) | no floor question; dated own statement: the union act of 7 October 1698 | enter an era 8 row; an era 9 row or named line; linked to IX.73; the Carpathian Ruthenian union as a line in VII.28 / VIII.38. Rivers: ME-8 keeps its own Jesuit line | enter |
| ME-9 | Hungarian and Transylvanian Protestantism: the "decade of mourning" to the Patent of Toleration and 1848 | church bodies | 6 Protestant & Evangelical | 1650-1906 | 8 (+9) | 2 | no floor question | enter an era 8 row; an era 9 row later. Rivers: no duplicate in any pass; the Unitarian side is RV-7 | enter |
| ME-10 | Polish and Lithuanian Catholicism under the partitions | church body | 5 Latin West & Catholicism | 1815-1906 (roots 1772-1795) | 9 | 1 | no floor question | enter an era 9 row, parent of IX.70; the Commonwealth church of 1650-1772 as a named line in VII.19 or a held era 8 row | enter |
| ME-11 | The Arab Evangelical churches and the American mission in Syria and Lebanon | church body | 6 Protestant & Evangelical | 1819/1823-1906 | 9 | 2 | no floor question | Middle East: a fifth wing in VIII.7. **Merged by the rivers pass into RV-4**, with AF-9's Egypt line | not counted (in RV-4) |
| ME-12 | The Jesuits in Russia, 1773-1814 | named line | Latin West & Catholicism | 1773-1814 | 8 | — | — | a line in a Jesuit home, or VII.19. **Re-homed by the rivers pass into RV-1** | not counted (in RV-1) |
| ME-13 | The Bulgarian church revival from Paisii of Hilendar (1762) | named line | (the receiving rows') | from 1762 | 8-9 | — | — | named line in VII.18, running into VIII.28's Exarchate | named line |
| ME-14 | The Armenian church in the Russian Empire: the Polozhenie of 1836 | named line | (VIII.32's) | 1836 | 9 | — | — | named line in VIII.32 | named line |
| ME-15 | The Armenian Catholic schism of 1870 and the bull *Reversurus* (1867) | named line | (VIII.32's) | 1867-1870 | 9 | — | — | named line in VIII.32 | named line |
| ME-16 | The Holy Places and the Latin Patriarchate of Jerusalem (1847) | gate note | (not stated) | 1847 | 9 | — | not a movement by the four marks | hold as a gate note; it may become named lines in VIII.28 and VIII.29 | hold |
| ME-17 | Karlovci, Montenegro, Sibiu | named lines | (the receiving rows') | 1765; 1864 | 8-9 | — | — | named lines in VII.18 (Karlovci, Montenegro) and VIII.28 (Sibiu, 1864) | named line |
| ME-18 | Russian Orthodox missions inside the empire: Siberia, the Volga, Il'minskii's schools | named lines | (the receiving rows') | (not stated) | 8-9 | — | — | named lines in VII.21 and VIII.31 once a source is opened; the Beijing mission to Asia (AP11). Rivers added a V source (Blackmore's preface to Mouravieff, 1842) | named line |
| ME-19 | Urmia: the Assyrian evangelical church and the Russian Orthodox mission of 1898 | named line | (not stated) | 1898 | 9 | — | — | named line in VIII.40 ([S]) | named line |
| ME-20 | The Tolstoyans | movement | (lane 8 if entered) | 1880s-1906 | 9 | — | a floor question (Tolstoy denied Christ's divinity [S]) | out of scope under A1, unless Mark chooses a lane 8 entry | out of scope / already carried |
| ME-21 | The Hebrew Christians of Kishinev (Joseph Rabinowitz, 1884) | congregation | (not stated) | 1884 | 9 | — | — | hold for sources; it would be the earliest parent of IX.13 | hold |
| ME-22 | Mennonites and Hutterites in the Russian Empire | routing | Protestant & Evangelical | 1789-1874 | 9 | — | — | route to the rivers pass. **Answered by the rivers pass as RV-2** | not counted (in RV-2) |
| RV-1 | The Society of Jesus: the reductions, the rites, the expulsions and the survival | church body (Catholic religious order), continues VI.11 | Latin West & Catholicism | 1650-1814 | 8 | 1 | no question (Catholic) | enter; LA8-2 and ME-12 become its lines; the Rites' home is AP2; ME-8 keeps its own Jesuit line (G89-1) | enter |
| RV-2 | Mennonites and Hutterites in the Russian Empire | church bodies | Protestant & Evangelical | 1789-1906 | 9 (from 1789) | 2 as a regional row; 1 as a chapter | no question | enter as the in-scope chapter of one Anabaptist continuation row, 1650-1906; the rest of that row to a North Europe pass; or a regional row alone if Mark wants only this part now | enter once (Mark rules the row's shape) |
| RV-3 | Catholics of the Ottoman Balkans: the Bosnian Franciscans, Albanian and Bulgarian Catholics | church body | Latin West & Catholicism | 1650-1878 | 8-9 | 2 | no question (Catholic) | enter the era 8 part on the V items; the era 9 part after one more source; the Bulgarian union of 1860-61 as a line here or in VIII.28 | enter |
| RV-4 | The Arab evangelical churches: Syria, Lebanon and Egypt | church bodies | Protestant & Evangelical | 1823-1906 | 9 | 2 | no question (Reformed) | enter one row; merges ME-11 and AF-9's Egypt line | enter once (G89-3 takes option b) |
| RV-5 | The Moravian Church, 1815-1906 | church body, continues VII.4 | Protestant & Evangelical | 1815-1906 | 9 | 1 | no question (VII.4's floor) | enter; the Caribbean, Cape, Suriname, Labrador and Nyasa as its lines; LA8-1 keeps a link; answers LA8-M | enter |
| RV-6 | Liberia's settler churches and the Black Atlantic links | church bodies | Protestant & Evangelical | 1792-1906 | 8-9 | 3 | no question (Baptist, Methodist) | a named line in VIII.7's West Africa wing, with links from VIII.1 | named line |
| RV-7 | The Transylvanian Unitarians after the Polish exile | church body | Non-Nicene Traditions (lane 8) | 1660-1906 | 8-9 | 3 now | a floor question (anti-trinitarian; lane 8 precedent in VI.14) | hold for sources; then a lane 8 row, or a named line closing VI.14 | hold |
| RV-8 | The Czech lands after 1627: the hidden Protestants and the Toleration Patent of 1781 | church bodies | Protestant & Evangelical | 1627-1906 | 8-9 | 2-3 | no question | a named line in VII.4 for the hidden Unity before 1722; the 1781-1906 churches to a North Europe pass | named line |
| RV-9 | Kosmas the Aitolian | a person and his preaching mission | Greek East & Orthodoxy | 1714-1779 | 8 | — | not a movement by the four marks on present evidence | hold; then a named line in VII.18 | hold |

### Counts by class

| Class | Africa | Latin America | Asia | Middle East | Rivers | All |
|---|---|---|---|---|---|---|
| enter | 5 | 2 | 6 | 8 | 3 | 24 |
| enter once (condition) | 0 | 0 | 0 | 0 | 2 | 2 |
| named line | 3 | 3 | 3 | 6 | 2 | 17 |
| hold | 1 | 4 | 6 | 4 | 2 | 17 |
| out of scope / already carried | 0 | 0 | 1 | 1 | 0 | 2 |
| **Counted** | **9** | **9** | **16** | **19** | **9** | **62** |
| not counted (inside another candidate) | 0 | 2 | 1 | 3 | 0 | 6 |
| **Rows listed** | **9** | **11** | **17** | **22** | **9** | **68** |

Five of the 24 "enter" rows enter one part now and leave the other for later: AP2 and RV-3 (the era 9 half, after one more source), ME-2 (the era 8 half, after the 1736 acts are opened), ME-9 (an era 9 row later) and ME-8 (the era 9 part, as a row or a named line). AF-4 and AF-5 may become one row, if G89-5 takes option (b). Then "enter" falls to 23.

**Carried already, not candidates.** Each pass also named what the roster already holds. Africa: Ethiopianism (IX.4), Madagascar (VIII.42), Buganda (VIII.43), Sierra Leone, the Niger and Liberia (VIII.7), the Antonian movement (VII.11). Asia: Taiping (VIII.44), the Philippines and the Aglipayans (VII.29, VIII.39), Japan after 1865 (VIII.45), the Batak and Javanese churches (VIII.26), the Mar Thoma and Malankara churches and the hill revivals (VIII.27), the China coast, the CIM, Serampore and the Pacific teachers (VIII.7). Latin America: the California missions, Guadalupe and the colonial saints (VII.17); the Reforma, García Moreno and the 1899 Plenary Council (VIII.48). Rivers: the Ecumenical Patriarchate under the Ottomans (VII.18); the autocephalies of 1850, 1870 and 1879 (VIII.28); Peć and Karlovci (VII.18); the Armenian Apostolic and Armenian Catholic churches (VII.24a, VII.24, VIII.32); Alaska (VII.21, VIII.47).

**Out of scope, not candidates.** Latin America: Vodou, Santería, Candomblé and Kardecist Spiritism (not Christian movements under A1); Túpac Amaru II; the Malê rising. Africa: North Africa before 1830 (no African church body); Kitawala (era 10). Asia: the Dalit mass movements, whose documented phase the era 10 sweep put in era 10 (GS-A3).

### Not swept

Places and sources the sweep did not cover, so that each gap is explicit.

- **North Europe and North America.** Outside this sweep's scope, except as links. The rivers pass sends three pieces there: the Anabaptist river outside Russia (RV-2), the Czech toleration churches of 1781-1906 (RV-8), and the two North Europe breaks of Open-Gaps 135 (section 2b).
- **Mediterranean Europe.** No pass covered it. Three items were noted and not assessed: the Waldensians after 1655 (VI.10 ends "1655+" and has no successor); the Church of Cyprus under the Ottomans [S]; and the Greek Orthodox Patriarchate of Alexandria (noted by the Africa pass in AF-2; it has no row [S]).
- **Africa.** The Armenians in Egypt and Ethiopia, which "sit inside the Armenian rows [S]"; not checked. The 1300-1517 part of the Coptic break, which belongs to the era 6 owner.
- **Latin America and the Caribbean.** Before 1650, Brazil, New Granada and the Caribbean have no era 7 entry (outside this sweep). The Library holds nothing for the region from 1815 to 1906, and no file on Brazil, Paraguay or Haiti in any year of the window. The Maronite and Syriac diasporas of the 1880s are held for era 10 (the era 10 sweep's LA-13).
- **Asia and the Pacific.** The Armenian merchant churches of India and Southeast Asia: Asia left a named line to the Middle East pass, which did not take it up. The era 9 roots of the Dalit mass movements are not sourced. Chinese, Japanese, Vietnamese, Malayalam, Malay, Tamil, Sinhala and Māori originals were searched for and not found raw (section 9).
- **Middle East, Caucasus, Russia and Eastern Europe.** Cossack and Ukrainian Orthodoxy under Russia after 1686 (VII.21 names the transfer). Georgian, Syriac and Armenian originals were not opened. The pass's other unswept items (Kosmas the Aitolian, the Balkan Franciscans, the Czech lands) were taken up by the rivers pass as RV-9, RV-3 and RV-8.

---

## 2b. The timeline breaks, answered

Every break in Open-Gaps 135 and 142 that falls in 1650-1906, with Mark's uniqueness test applied ("check that they are unique and not tied to other movements, like jesuites moving around the world, that is a single movement"). The breaks the passes found are listed after them.

| Break (Open-Gaps entry) | Uniqueness test | Answer |
|---|---|---|
| Ethiopian church, 1650-1855 (142) | Unique. The Jesuit story ends in VI.25 (1634); the later Capuchin and Franciscan attempts are Propaganda's and appear only as the church's response. Its tie to the Copts (the abun) is a link between two church rows, not one movement. | AF-1, with an "in contact with" link to AF-2 |
| Coptic church, 1517-1854 (142) | Unique; not tied to any cross-world row. The Africa pass found the real gap starts c. 1300, where IV.26 ends. | AF-2, from 1517; 1300-1517 logged as its own break for the era 6 owner |
| Church of the East, 1650-1815 (142) | Unique: the middle of VI.30 to VIII.40. Capuchin and Propaganda work is a strand inside it. | ME-1, with a link to AP1 (Mar Gabriel, 1708) |
| St Thomas Christians, 1665-1815 (142) | Unique. The Carmelite-Jesuit rivalry is a strand inside it, not the subject. | AP1 |
| Catholic missions in China, 1650-1793, and the Chinese Rites controversy (142) | Tied to the Jesuits only in part. The Jesuits carried the court mission (1650-1773); Propaganda, the Holy Office and two popes decided the Rites; after 1724 Chinese priests, Lazarists and MEP ran the provincial church. The China church is unique; the Jesuits' own story is the single movement. | AP2 for the China church and the Rites (their one home); RV-1 for the Jesuit side, linked to AP2. The gap runs to 1906, not 1793 |
| Japan's hidden Christians, 1650-1865 (142) | Unique. They kept the faith without priests; not the Jesuits' story, and not VIII.45's, which starts on 17 March 1865. | AP3 |
| Maronite church, 1517-1900 (142) | Unique: IV.10 and V.22 carried on. Rome is part of the story, as for every Eastern Catholic church. | ME-2 (era 9 now, era 8 after the 1736 acts); 1517-1650 to the era 7 owner |
| Georgian church, 1245 onward (142) | Unique for 1650-1811. The Exarchate (1811-1917) sat inside the Russian Synod. | ME-3 (era 8 row), with the Exarchate as a named line in VIII.31, linked to IX.40; 1245-1650 to the era 6 and 7 owners |
| Latin America, thin for 1492-1900 (142, closing note) | Real but uneven. Tied to other movements: the reductions (RV-1), the Caribbean missions before 1815 (VII.4, VII.16), colonial Brazil (VII.17), 1810-15 (VIII.48), the Protestant beginnings (IX.63, VIII.41). Unique: the Caribbean churches after 1815 and Canudos. | LA8-1 and LA8-3 enter; LA8-4, LA8-5, LA8-7 lines; LA8-6, LA8-8, LA8-9, LA8-10 held; LA8-2 inside RV-1 |
| Melkites, 1009-1724, held (135) | Only 1650-1724 falls here: Macarius III's world, the same church as VII.23. | A named line in VII.23 (ME-4); 1009-1650 stays held. New finding: nothing after 1815 (ME-4's era 9 row) |
| Syriac Orthodox church after 1300, held (135) | Unique. The Syriac Catholic split is its own strand. | ME-7, still held: both items opened are outsiders (Badger, Fortescue) |
| Old Believers after 1815, with the Belokrinitsa hierarchy (135) | Unique: VII.7 carried on. VIII.31 names Belokrinitsa as "separate". | ME-5 |
| **Scottish church after 1650 (135)** | — | **Not answered here.** North Europe, outside every pass's region |
| **Swedenborgian New Church after 1815 (135)** | — | **Not answered here.** North Europe and North America, outside every pass's region |

Open-Gaps entries outside 1650-1906 are not answered here: the Armenian church 1441-1517 and the Greek Catholics of Galicia 1906-1946 (142); the medieval English church and the medieval Scandinavian church (135).

**New breaks found by the passes**

| Break | Found by | Uniqueness test | Answer |
|---|---|---|---|
| Kongo and Angola, 1650-c. 1880s | Africa | Unique. The Capuchins have no row, and the subject is a Kongolese church. | AF-3 |
| The Copts, c. 1300-1517 | Africa | The front of the Coptic break; IV.26 has no `continuesAs` | Logged for the era 6 owner; AF-2 starts at 1517 |
| The Moravian church after 1815 | Latin America (and the rivers pass) | Not a new movement: the same movement as VII.4, across the world. Splitting it by place is what Mark's test warns against. | RV-5, one era 9 row continuing VII.4 |
| Southern Africa, 1652-1906 | Africa | The Dutch Reformed Church is unique (AF-4). The missions were judged by Africa to belong to existing rows; the rivers pass gives them their own entry, by VIII.7's own rule. | AF-4 and AF-5 (G89-5) |
| China, 1650 to 1906, not to 1793 | Asia | The roster is empty for China's Catholics until 1906, not only to 1793. | AP2 covers 1650-1906 |

---

## 3. Africa

The pass's `candidates.md`, as written, with its headings demoted two levels. Changes: British to American spelling in the pass's own prose, and a merge note at the head of each candidate the rivers pass gave a new home.

### Eras 8 and 9 completeness sweep (P2-G89): AFRICA, 1650-1906, every river

Sweep run 2026-11-10 under `Sweep_Brief.md` (this audit folder), Mark's scope ruling "eras 8 - 10 for now" (2026-11-09), his ruling on the timeline breaks (2026-11-10: log them, "but check that they are unique and not tied to other movements, like jesuites moving around the world, that is a single movement"), and the rule that a movement outside church bodies is "a defined movement, not just a trend".

**Phase: divergent.** Nothing here is decided. Eras 8 and 9 are frozen, so every addition below reaches Mark's gate as a change order.

**Scope.** All of Africa: Ethiopia and Eritrea, Egypt and the Copts, North Africa, West, Central, East and Southern Africa, Madagascar and the Indian Ocean islands.

**Verification states** (the brief's own).
- **V**: I opened the item in this run and confirmed the detail. Library files are named by file; online items were opened raw with curl from archive.org (`_djvu.txt` derivative), and the item identifier is given.
- **V-s**: a study's details only (bibliographic record or a citation in the repo), not its content.
- **[S]**: snippet, summary, memory or unopened. An [S] item never counts as verified.
- Only V carries a sentence.
- **Quotes from OCR.** Quoted words come from raw OCR text. The long s is read as s, and plain OCR letter slips (for example "wich" for "with") are mended. Each quote should be checked against the page image before any census use. Every V source below is pre-1930 and public domain by date. Most are outside witnesses (missionaries, travelers, consuls); that is said for each.

**Library check.** `cic/texts/` holds strong Africa holdings for this window that no era 8 or 9 row uses: Ludolf (1682, 1691), Telles (1710), Lobo (1735) for Ethiopia; Carli (1671), Cavazzi (1687), Merolla (1692) and Zucchelli (1715) for Kongo and Angola (mapped only to VI.13a and VII.11, as context); Volney vol. 2 (1788, Syria only); Latrobe (1771) and Cranz (1780) for the Moravian missions. Nothing vendored covers Egypt after 1500, Southern Africa, or nineteenth-century West Africa. Items opened raw online in this run are listed per candidate; the raw files sit in the session scratchpad, not in the repo.

**One roster finding to flag first.** The Coptic break is longer than Open-Gaps 142 says. IV.26 (Coptic Christianity, Fatimid to Mamluk) ends c. 1300 and has no `continuesAs`. No era 6 or 7 row carries the Copts. So the Coptic church has no row from c. 1300 to 1854, not 1517 to 1854. The 1300-1517 part lies outside this sweep's eras; it is noted for the owner of era 6.

---

#### 1. River-by-river table

| River | What the roster has (Africa, 1650-1906, with era 7 and 10 neighbors) | Gap | Candidate |
|---|---|---|---|
| **Oriental Orthodox** | VI.25 Ethiopia to 1650. VIII.49 Ethiopia 1855-1900. VIII.13 Copts 1854-1906. IV.26 Copts to c. 1300. IX.10, IX.20 after 1900. | Ethiopia 1650-1855 (Gondar, the christological councils, the Zemene Mesafint). The Copts c. 1300-1854 (this sweep: 1650-1854; the Ottoman archons, the patriarchate, the abun sent to Ethiopia). Both logged in Open-Gaps 142. | **AF-1** Ethiopia, Gondar to the Zemene Mesafint. **AF-2** The Copts under the Ottomans. |
| **Eastern Catholic** | Nothing in Africa. (VII.23 Melkites is the precedent for a uniate row.) | The Coptic Catholics (first Catholic metropolitan for the Copts, 1741; patriarchate 1824 and 1895 [S]). The Ge'ez-rite Catholics of Ethiopia and Eritrea (de Jacobis, from 1839; Ghebre Mikael, died 1855 [S]). | **AF-7**, named lines in AF-2 and AF-1. |
| **Catholic (Latin)** | VI.13a Kongo to 1650. VII.11 Antonian movement 1704-06. VIII.43 Buganda (White Fathers from 1879). VIII.29 Rome's century (names "the growth of missionary Catholicism"). IX.59 Africa from 1906. | (a) Kongo and Angola after 1650: the Capuchin century and the Kongolese lay church to the 1880s. Not logged as a break. (b) The nineteenth-century Catholic mission revival in Africa (Lavigerie and Algiers 1867, the White Fathers 1868, Comboni's plan 1864/67, the Spiritans, Laval in Mauritius). IX.59 has only VIII.43 behind it. | **AF-3** Kongo Christianity after 1650. **AF-6** Catholic mission revival (named line in VIII.29, or a row). |
| **Protestant, Evangelical, Anglican** | VIII.7 (Sierra Leone and the Niger wing; Crowther; "Liberia sits inside its orbit"). VII.16 (David George to Sierra Leone). VII.4 (a gap story on Rebecca Protten in West Africa). VIII.42 Madagascar. VIII.43 East Africa. VIII.49 (Basel men at Gafat). IX.60 apartheid struggle from 1960. | (a) **Southern Africa has no row at all before 1960** except IX.4's Ethiopian Church (1892). The Dutch Reformed Church at the Cape (from 1652) is the predecessor IX.60 lacks. (b) The Southern African mission churches: Genadendal (Moravian, 1737), Bethelsdorp (LMS, 1803), Ntsikana (d. c. 1821), the Paris mission with Moshoeshoe (1833), Tiyo Soga (ordained 1856). (c) Protestant Egypt (American Mission from 1854). (d) West Africa before 1793 (Capitein, Quaque). | **AF-4** The Dutch Reformed Church at the Cape. **AF-5** Southern African mission churches (a fifth wing of VIII.7, plus a VII.4 line). **AF-8** West Africa before the societies (lines). **AF-9** Protestant missions in Egypt and Ethiopia (lines). |
| **Syriac and other Eastern** | None in Africa, and none expected. Armenians in Egypt and Ethiopia sit inside the Armenian rows [S]. | None. | None. |
| **Independent, indigenous, slave-born** | VII.11 Antonian. IX.4 African-initiated churches, from the 1880s (Tile; Mokone's Ethiopian Church, November 1892). VIII.42's self-carried church. | Ethiopianism (1880s-1906) is carried by IX.4. The Kongolese lay church after the Capuchins left (c. 1835-1880s) is AF-3's last chapter. Ntsikana is AF-5's first African voice. No separate defined movement found that IX.4, VII.11 or VIII.42 does not already hold. | No new row. Notes in AF-3 and AF-5. |

---

#### 2. Candidates, ranked by importance to the eras' global story

##### AF-1. Ethiopian Christianity: Gondar to the Zemene Mesafint (1650-1855) — logged break

- **Kind:** church body (the Ethiopian Orthodox Tewahedo Church), a window of the same church as VI.25 and VIII.49.
- **Era:** 8 and 9 (a span row, 1650-1855).
- **Dates:** 1650 (VI.25's end; Fasilides reigned on to 1667 [S]) to 1855 (Tewodros II, VIII.49's start).
- **Region / countries / lane:** Africa. Ethiopia, Eritrea. Lane 4 Africa.
- **What it holds.** The Gondar monarchy and its churches; the christological quarrels that VIII.49 says "had split Ethiopian scholars for two centuries" (Tewahedo against the "unction" and "three births" parties [S for the party names]); clergy convocations that tried Catholic missionaries; the Itchege and the monks of Debre Libanos against the Eustathian houses; the Zemene Mesafint from 1769, when regional lords ruled and the emperors were figureheads; and the abun, always an Egyptian monk sent by the Coptic patriarch.
- **Section A:** clear by precedent. Same church as VI.25 and VIII.49, both on the roster under the floor's handling of the Oriental Orthodox. No dated own statement was read this run. The Boru Meda ruling (1878) falls in VIII.49.
- **B1 Sourcing:** moderate to good, and better than the gap suggests. Own-voice royal chronicles exist in Ge'ez with Latin or French translation (Guidi's annals of Yohannes I, Iyasu I and Bakaffa, 1903-05; of Iyasu II and Iyo'as, 1910-12 [S]), but the archive.org copies are lending-library only, so not read. Outside witnesses read in this run: Ludolf (1682), Bruce (1790), Gobat (1834). Source asymmetry: the readable record is mostly European; the chronicles are court voices; the monks' and laity's own voices are thin.
- **B2 Ecology:** full. Court and church at Gondar, monastic parties, councils, the abun's arrival from Egypt, Marian devotion, church-building, war and the collapse of central rule.
- **B3 Uniqueness:** high. No row carries these two centuries. The Jesuit story ends in VI.25 (1634). The later Capuchin and Franciscan attempts (to 1716) are Propaganda's story and appear here only as the Ethiopian church's response. The christological councils are the church's own.
- **B4 Audience:** Ethiopian and Eritrean Orthodox believers and their diaspora; historians of Oriental Orthodoxy; readers asking how an African church governed itself without Europe.
- **B5 Scale:** tiebreak only.
- **Tier:** 1.
- **Evidence:**
  1. Bruce, *Travels to Discover the Source of the Nile* (Edinburgh, 1790), vol. 3 (archive.org `travelstodiscov03bruc`). **V.** Bruce, at Gondar in 1770-71, writes that the Abuna "is looked upon as the patriarch of the Abyssinian church", that he "very seldom understands the language", and that the Itchege, chief of the monks of Debra Libanos, is "in troublesome times, of much greater consequence than the Abuna". He calls the Eustathian monks of Gojam "the Low Church of Abyssinia", "much inclined to turbulence in religious matters". He also names the Abuna as "a coptish monk bred in the desert of St Macarius". Outside witness; Bruce's reliability is itself debated [S].
  2. Bruce, vol. 2 (1790) (archive.org `travelstodiscov02bruc`), the reign of David, 1714-1719. **V.** Monks demand "a convocation of the clergy"; Bruce says such assemblies are "particularly expected at the accession of a new prince", and that "the arrival of a new Abuna from Egypt is also a very principal reason for the convocation". The assembly asks Catholic missionaries whether they receive the council of Chalcedon and Pope Leo; on their yes, they are stoned "behind the church of Abbo". Outside witness, decades later.
  3. Samuel Gobat, *Journal of a Three Years' Residence in Abyssinia* (London: Hatchard and Seeley, 1834), preface quoting the CMS missionary Kugler (archive.org `journalthreeyea01gobagoog`). **V.** Girgis and the chief priest of Tigray, Guebra Mariam, bring "the decision of the Coptic Patriarch concerning their religious quarrels"; Guebra Messih, "who held the opinion of three births of Christ", accepts it, and "the dispute about Religion was regularly adjusted, in the presence of Dejasmat Sebagadis" on 28 September. The year (1830) is not on the page read [S].
  4. Hiob Ludolf, *A New History of Ethiopia* (London, 1682), `cic/texts/ludolf_new-history-of-ethiopia_jp1682.txt`. **V.** Basilides (Fasilides) expelled the Jesuits "together with their Patriarch"; "Neither do we know any thing more of certainty concerning him, he refusing any farther Commerce with the Europeans". Also embassies to Constantinople in 1660 and 1661. Outside witness, from Abba Gregorius; it shows how little Europe knew after 1634.
  5. Ignazio Guidi, ed. and trans., *Annales Iohannis I, Iyāsu I, Bakāffā* (CSCO, Scriptores Aethiopici, 1903-05). **V-s** (archive.org metadata seen: `annalesiohannisi0022znhl_5`, a 1955 reprint of the 1903-05 edition; lending only). Content [S]. Also Guidi, *Annales regum Iyasu II et Iyo'as* [S].
  6. Donald Crummey, *Priests and Politicians: Protestant and Catholic Missions in Orthodox Ethiopia, 1830-1868* (Oxford, 1972). **V-s** (cited on VIII.49). Covers the last 25 years of the window.
  7. Adrian Hastings, *The Church in Africa, 1450-1950* (Oxford, 1994). **V-s** (verified in the era 10 sweep). The standard survey for every African candidate here.
  8. Wanted: H. Weld Blundell, *The Royal Chronicle of Abyssinia, 1769-1840* (Cambridge, 1922), an English translation of the Zemene Mesafint chronicle; searched on archive.org, not found [S]. Studies by scholars from the region (Merid Wolde Aregay; Getatchew Haile on the christological disputes) [S].
- **Living today:** yes, the same church as IX.20 (living:true). This window needs no separate living evidence.
- **Overlap:** VI.25 (ends 1650; it holds the Jesuit expulsion); VIII.49 (from 1855; it holds Boru Meda 1878); VIII.13 (the Coptic side of the abun link, from 1854); AF-2 (the Coptic side before 1854). No other row names Ethiopia in 1650-1855.
- **Mark's test (unique, or inside a cross-world row?):** unique. After 1634 the Jesuits are gone; the Capuchin and Franciscan attempts are Propaganda's story, which has no row in this era, and the Ethiopian church's trials of them are its own acts. The tie that matters is to the Copts (the abun), which is a link between two church rows, not one movement. Recommend an "in contact with" edge to AF-2, as VIII.13 to VIII.49 does now.
- **Recommendation:** enter, Tier 1, as a church row from 1650 to 1855, with the Ge'ez-rite Catholics (AF-7) and the CMS mission of 1830 (AF-9) as named lines.
- **Gate question G-AF89-1:** How should the break be filled?
  - (a) A new row, 1650-1855, between VI.25 and VIII.49 (`continuesAs` chain VI.25 -> new -> VIII.49).
  - (b) Stretch VI.25 to 1769 (the start of the Zemene Mesafint) and VIII.49 back to 1769. No new row, but both frozen rows change dates and text.
  - (c) Hold for sources until Guidi's annals or Weld Blundell can be read.
  - **Recommendation: (a).** It is one coherent period with its own name in the scholarship, and (b) rewrites two frozen rows. Draft only from V items, and add Guidi to the wants list.

##### AF-2. The Coptic church under the Ottomans: the patriarchate and the archons (1517-1854) — logged break

- **Kind:** church body (the Coptic Orthodox Church), a window of the same church as IV.26 and VIII.13.
- **Era:** 7 to 9 as written in Open-Gaps 142 (1517-1854). This sweep's share is 1650-1854. See the gate question for the start date.
- **Dates:** 1517 (the Ottoman conquest of Egypt) to 1854 (Cyril IV, VIII.13). The real gap starts c. 1300, where IV.26 ends.
- **Region / countries / lane:** Africa. Egypt (with the abun's see in Ethiopia). Lane 4 Africa.
- **What it holds.** A church that lived as a tax-paying minority under the beys. Its lay notables, the *arākhina* (archons), Coptic scribes who ran land registers and finance, paid for churches and monasteries (Ibrahim al-Jawhari, d. 1795, and his brother Girgis [S for dates]). The patriarchs, the desert monasteries, the Arabic shift away from Coptic, the patriarch's court for Copts, the abun sent to Ethiopia, the Catholic missions of Propaganda among the Copts, and Coptic soldiers and notables in the French occupation of 1798-1801 [S].
- **Section A:** clear by precedent. Same church as IV.26 and VIII.13 (VIII.13's floorNote reads "No question"). No dated own statement read this run.
- **B1 Sourcing:** moderate. Own-voice: the *History of the Patriarchs* continuation into the Ottoman centuries exists in Arabic [S] (the Library holds only Evetts vol. 1, early). Outside witnesses read this run: Volney (1787), Bruce (1790), Lane (1836, 1860 edition). Study read: Butcher (1897). Modern standard: Guirguis and van Doorn-Harder (2011), cited on VIII.13. Source asymmetry: the archons' own letters and the waqf deeds are known to scholars [S] but not to the Library.
- **B2 Ecology:** good. Patriarch and bishops, monks, lay notables and their endowments, scribes in government, village Copts in Upper Egypt, the Catholic minority, the link to Ethiopia.
- **B3 Uniqueness:** high. No row carries the Copts for five and a half centuries. VI.18 names a Coptic patriarch only in passing (Ahatallah). VIII.13 starts at 1854 and calls the church before it "reduced in the eyes of most outsiders to a survival". The archon story is the church's own and is not told anywhere.
- **B4 Audience:** Coptic believers and the large Coptic diaspora; historians of Christians under Islamic rule; readers comparing the millet churches (VI.17, VII.18).
- **B5 Scale:** tiebreak. Lane reckoned the Copts at about 150,000 in the 1830s (V, below).
- **Tier:** 1 for the whole break; 2 if limited to 1650-1854 alone.
- **Evidence:**
  1. C.-F. Volney, *Travels through Syria and Egypt, in the Years 1783, 1784, and 1785*, vol. 1 (London: G. G. J. and J. Robinson, 1787) (archive.org `travelsthroughsy01voln`). **V.** The Copts "are become the depositaries of the registers of the lands and tribes. Under the name of writers, they are at Cairo the intendants, secretaries, and collectors of government". He says the land tax "is entrusted with the Copt writers". He calls them "Eutychians". Hostile outside witness. (The Library holds only Volney's vol. 2, on Syria.)
  2. E. L. Butcher, *The Story of the Church of Egypt*, vol. 2 (London, 1897) (archive.org `storyofchurchofe02butc`). **V** (a nineteenth-century study, public domain). Benedict XIV consecrated "the first Roman Catholic Metropolitan who owned any real jurisdiction in Egypt", a Copt of Jerusalem named Athanasius, "and the date of his appointment is 1741". In a footnote at A.D. 1787, "Moallem Ibrahim-el Johari, chief clerk of the finance department", won leave for churches and monasteries to be restored and "gave a great deal of land and money for the support of the National Church".
  3. E. W. Lane, *An Account of the Manners and Customs of the Modern Egyptians*, written 1833-35, 5th edition (London, 1860) (archive.org `accountofthemann031193mbp`). **V.** Lane's reckoning: "Christian Egyptians (Copts) . . . 150,000". "The Coptic Patriarch, who is the head of his church, judges petty causes among his people in the metropolis". Outside witness.
  4. Bruce, vol. 3 (1790) (archive.org `travelstodiscov03bruc`). **V.** The Catholic missionaries among the Copts laid a case before "the College of Cardinals de propaganda fide, at Rome". Outside witness.
  5. Andrew Watson, *The American Mission in Egypt, 1854 to 1896* (Pittsburgh: United Presbyterian Board of Publication; entered 1897, host date 1898) (archive.org `americanmission00wats`). **V** for its chapter heading: efforts "to secure a friendly intercourse with the Christians of the Nile valley from 1752-1854 — The Moravians — The Church Mission Society Missionaries". A mission's view.
  6. Magdi Guirguis and Nelly van Doorn-Harder, *The Emergence of the Modern Coptic Papacy* (Cairo: AUC Press, 2011). **V-s** (cited on VIII.13 and in the repo). Its coverage of the Ottoman centuries [S].
  7. Otto Meinardus, *Two Thousand Years of Coptic Christianity* (AUC Press, 1999). **V-s** (cited on VIII.13).
  8. Wanted: the Arabic *History of the Patriarchs* for the Ottoman patriarchs; J. M. Vansleb, *Histoire de l'Eglise d'Alexandrie* (Paris, 1677), not found on archive.org by title [S]; studies by Coptic historians of the archons (Magdi Guirguis's work on the Jawhari brothers [S]).
- **Living today:** yes, the same church as IX.10 (living:true).
- **Overlap:** IV.26 (to c. 1300); VIII.13 (from 1854); VI.18 (a passing name); AF-1 (the abun link); VII.18 and VI.17 (the Greek Orthodox under the Ottomans, a parallel, not this church). The Greek Orthodox Patriarchate of Alexandria has no row either [S]; it is noted, not proposed.
- **Mark's test:** unique. The Coptic church is its own body. The only cross-world thread inside it is Propaganda's Catholic mission, which leads to the Coptic Catholics (AF-7), a named line here.
- **Recommendation:** enter as a church row. Tier 1 if it starts at 1517 (or c. 1300); named lines for the archons and for the Coptic Catholics (AF-7).
- **Gate question G-AF89-2:** Where should the new Coptic row start?
  - (a) 1517, the Ottoman conquest, as Open-Gaps 142 logged it. Era 7 to 9.
  - (b) 1650, the start of era 8, so it stays inside this sweep's eras. The years 1300-1650 stay a gap.
  - (c) c. 1300, where IV.26 ends, with one long row (Mamluk and Ottoman) or two.
  - **Recommendation: (a)**, with the 1300-1517 Mamluk years logged in Open-Gaps as their own break. 1517 is a real change of masters, and the Ottoman centuries hang together. Starting at 1650 cuts a story in the middle for a reason that is only the era line.

##### AF-3. Kongo Christianity after 1650: the Capuchin century and the Kongolese lay church (1650-c. 1880s) — new break, not logged

- **Kind:** church body, as a regional window of the Catholic Church (the shape of VI.13a, VIII.42 and IX.59).
- **Era:** 8 and 9 (a span row).
- **Dates:** 1650 (VI.13a's end) to the 1880s, when the Baptist Missionary Society (from 1878-79) and Portuguese Catholic missions returned to São Salvador [S for the exact years]. The Antonian movement (VII.11, 1704-06) falls inside it.
- **Region / countries / lane:** Africa. Angola (the old kingdom of Kongo, Soyo, Matamba and Portuguese Angola), DR Congo (the lower Congo). Lane 4 Africa, or a 4 to 5 bridge as IX.59 uses.
- **The break.** Open-Gaps 142 did not log it. VI.13a ends at 1650. VII.11 tells two years, 1704-06, against a background its own text gives ("Christian for two centuries"). Then nothing names Kongo until IX.4's Kimbangu in 1921. That is roughly 270 years with one two-year entry.
- **What it holds.** The Capuchin mission (from 1645 [S]); the war that broke the kingdom at Mbwila in 1665 [S]; a church kept by Kongolese catechists and lay nobles across a divided kingdom; the queen Njinga of Matamba and her return to the Church [S for the date]; the Antonian crisis (VII.11) and the restoration under Pedro IV; the long decades with few or no priests after the Capuchins faded (c. 1835 [S]); and the Baptist and Catholic return of the 1880s, when the capital split between the two.
- **Section A:** clear. It is the Catholic Church, as VI.13a and IX.59.
- **B1 Sourcing:** good for 1650-1715, and the texts are already in the Library: four Capuchin eyewitnesses (Carli 1671, Cavazzi 1687, Merolla 1692, Zucchelli 1715), plus Proyart's Loango mission of the 1760s in Pinkerton vol. 16 (1814). Thin for 1720-1870. Good again for the 1880s (Bentley 1900). Source asymmetry is severe: almost every text is a missionary's, as VI.13a says of its own period. Kongolese letters survive in the Lisbon and Propaganda archives [S].
- **B2 Ecology:** full. Baptism and catechesis, the friars as *nganga*, the confraternities and schoolmasters [S], the court and the rival claimants, war and the slave trade, a prophetic movement, and a church that ran on lay leaders.
- **B3 Uniqueness:** high. The roster holds Kongo only in 1491-1650 and 1704-06. It is also the oldest continuous Christian kingdom south of the Sahara outside Ethiopia, which makes the gap more visible.
- **B4 Audience:** Angolan and Congolese Christians; historians of Atlantic Christianity (Kongo Christianity in the Americas, which VI.13 names as a legacy); readers asking whether African Christianity began with nineteenth-century missions.
- **B5 Scale:** tiebreak only.
- **Tier:** 1 for 1650-1720; the later stretch is Tier 2 on sources alone.
- **Evidence:**
  1. Dionigi Carli and Michelangelo Guattini, *Viaggio ... nel regno del Congo* (1671), `cic/texts/carli_viaggio-nel-regno-del-congo-ita_guattini1671.txt`. **V.** In a village of Bamba, the headman sends word to bring children "a battezzare, perche l'adulti sono tutti battezzati" ("for baptism, because the adults are all baptized" *(my rendering)*); the people call the Capuchin "Ngamga" (nganga). Outside, missionary witness, late 1660s.
  2. Giovanni Antonio Cavazzi, *Istorica descrizione de' tre regni Congo, Matamba, et Angola* (Bologna, 1687), `cic/texts/cavazzi_istorica-descrizione-tre-regni-congo-matamba-angola-ita_alamandini1687.txt`. **V.** Of the queen Njinga ("la Regina Zinga"), Cavazzi writes that she cast off "la vera Legge" and for twenty-eight years ("nello spazio di ventotto Anni") kept the Jaga statutes. Her later return to the Church, which Cavazzi witnessed as her confessor, is [S] (not located in the OCR this run). Hostile missionary witness.
  3. Girolamo Merolla, *Breve, e succinta relatione del viaggio nel regno di Congo* (Naples, 1692), and Antonio Zucchelli, *Merckwürdige Missions- und Reise-Beschreibung nach Congo* (1715), both in `cic/texts/`. **V-s** (Library content notes: Soyo in the 1680s; Soyo and Kongo 1698-1704 and Pedro IV). Not reread for a quoted detail this run.
  4. W. Holman Bentley, *Pioneering on the Congo* (London, 1900) (archive.org `pioneeringoncong01bent_0`). **V.** A Baptist missionary at San Salvador writes of "the strong party-feeling of our friends and followers in San Salvador" against "the Portuguese priests, with their images, crucifixes, and saints", and judges "the support of the people is pretty equally divided, numerically, between the priests and ourselves". Partisan witness.
  5. John K. Thornton, *The Kongolese Saint Anthony: Dona Beatriz Kimpa Vita and the Antonian Movement, 1684-1706* (Cambridge, 1998). **V-s** (cited on VII.11 and in the repo). Thornton's wider Kongo scholarship covers the whole window [S].
  6. Hastings 1994. **V-s.** Its Kongo chapters [S].
  7. Wanted: Kongolese letters of the period (the kings' and nobles' correspondence with Rome and Lisbon); Antonio de Teruel and Bernardo da Gallo (Capuchin manuscripts) [S].
- **Living today:** yes, by the same reasoning as VI.13a (living:true): the Catholic Church in Angola and the lower Congo continues. IX.59 carries the region from 1906.
- **Overlap:** VI.13a (ends 1650); VII.11 (an event inside this window; keep it as its own row); IX.4 (Kimbangu came out of the Baptist mission that returned in the 1880s [S]); IX.59 (from 1906). VI.13 (the parent family row).
- **Mark's test:** unique. The Capuchins were Propaganda's friars and served in many places, but there is no Capuchin or Propaganda row, and the Kongo church is not their story. It is a Kongolese church that they served. Its life without priests after c. 1835 makes that plain. The test favors a Kongo row, not a cross-world mission row.
- **Recommendation:** enter as a church row, 1650 to the 1880s, Tier 1, built first from the four vendored Capuchin texts. Make VII.11 sit inside it with a "gave rise to" or "in contact with" edge.
- **Gate question G-AF89-3:** How should the Kongo gap be filled?
  - (a) A new row, 1650 to the 1880s, with VII.11 inside its span as its own entry.
  - (b) Extend VI.13a to 1720 (the Capuchin witnesses and the restoration), and log 1720-1880s as a break held for sources.
  - (c) Log it in Open-Gaps 142 only, as a break found by this sweep.
  - **Recommendation: (a)**, if Mark accepts a thin middle stated plainly; else (b). The Library already holds the texts for its best-documented part.

##### AF-4. The Dutch Reformed Church at the Cape (1652-1906) — regional absence, not logged

- **Kind:** church body (the Nederduitse Gereformeerde Kerk and its daughters in the Boer republics).
- **Era:** 8 and 9 (a span row).
- **Dates:** 6 April 1652 (the Dutch East India Company's settlers at Table Bay; V) to 1906. A clean inner turn is the first synod of 1824 (V).
- **Region / countries / lane:** Africa. South Africa (Cape, Natal, Orange Free State, Transvaal). Lane 6 Protestant & Evangelical, region Africa.
- **The gap.** South Africa has no row in eras 8 or 9. The only South African body on the roster before 1960 is IX.4's Ethiopian Church (1892). IX.60 (the church struggle, 1960-94) and its Belhar Confession come out of this church's mission daughter, but nothing on the tree shows where that church came from. VI.9 says Dutch piety "may also have gone with Dutch Reformed emigrants to South Africa ... though no early account shows it". VIII.50 names South Africa only for later apartheid theology. VI.6 names Cape Town only as a Huguenot refuge.
- **What it holds.** A Company church with ministers sent from Amsterdam; the baptism of slaves and what it meant for their freedom; Huguenot refugees absorbed from 1688 [S]; the first synod (1824); Scottish ministers brought in, Andrew Murray among them [S for the date]; the hymnbook quarrel with the "Doppers" and the Trek (1830s); separate churches in the Transvaal (1853, 1859 [S]); the liberal controversy and the Burgers case in the Cape Supreme Court (1865); the revival of 1860 [S]; the synod resolution of 1857 that allowed separate worship "because of the weakness of some" [S]; and the Dutch Reformed Mission Church (Sendingkerk) of 1881 [S], the body that later wrote Belhar.
- **Section A:** clear on dated standards. McCarter (1869): "Its Standards are the Heidelberg Catechism, the Belgic Confession, and the Canons of the Synod of Dort" (V). These are Nicene and trinitarian, as on VI.26 and VI.9.
- **B1 Sourcing:** moderate. A dated church history of 1869 by a minister at Ladysmith, Natal (McCarter, read; which church he served was not checked [S]); synod acts and the Cape Supreme Court record of 1863-65 exist [S]; Andrew Murray's own published works are public domain [S]; Afrikaans and Dutch church histories (for example the NG Kerk's own jubilee histories) [S]. Studies: Elphick and Davenport (1997), V-s (cited in the era 10 sweep). The voices of slaves, Khoikhoi members and "coloured" congregants are the thin side.
- **B2 Ecology:** good. Parish and consistory, catechism and psalm-singing, slave baptism, frontier congregations, synod politics, revival, mission, and the courts.
- **B3 Uniqueness:** high. The only Reformed church planted in Africa in era 8 that became a national church, and the predecessor of IX.60's main actors on both sides.
- **B4 Audience:** Reformed Christians; South Africans of every community; historians of church and race; readers of IX.60, who meet Belhar with no back story.
- **B5 Scale:** tiebreak only.
- **Tier:** 1.
- **Evidence:**
  1. John McCarter, *The Dutch Reformed Church in South Africa, with Notices of the Other Denominations: An Historical Sketch* (Edinburgh: W. and C. Inglis; Cape Town: N. H. Marais, 1869) (archive.org `dutchreformedchu00mcar`). **V.** "On the 6th of April 1652 three Dutch vessels, with a small body of settlers on board, came to anchor in Table Bay." The first minister, van Arckel, "on his arrival in 1665, he baptised eight heathen children"; "from 1665 to 1731, there stand recorded in the Church books the baptisms of 1121 slave children, and forty-six adults"; "A Government regulation was passed in 1683, that whenever a slave was received into the Christian Church, he was ipso facto free". In 1824, "a Synod or General Assembly was held". The church's standards (Section A, above). The hymnbook "was obstinately opposed" by "those popularly called the 'Doppers'". The Burgers case came before the Supreme Court on 26 May 1865, with "the Rev. Andrew Murray, jun." summoned "as Moderator of the Synod". The title page names him "the Rev. John M'Carter, Ladismith, Natal"; whether he was a minister of this church or a Scottish Presbyterian was not checked [S]. A sympathetic account of 1869.
  2. Richard Elphick and Rodney Davenport, eds., *Christianity in South Africa: A Political, Social and Cultural History* (1997). **V-s.**
  3. Hastings 1994. **V-s.**
  4. The 1857 synod resolution and the founding of the Sendingkerk (1881): [S]. Not in McCarter. Wanted: the *Acta Synodi* of 1857 in Dutch, and a pre-1930 history that prints the resolution.
- **Living today:** yes. The NG Kerk continues, and the Uniting Reformed Church (from 1994 [S]) continues the Sendingkerk. For an era 9 row the living mark needs a dated item graded CD or CR; none was read this run, so **CR at most, pending a dated item**.
- **Overlap:** VI.9 and VI.26 (the Dutch parent; no African content); VI.6 (the Huguenots' refuge); VIII.50 (Kuyper's later influence); IX.60 (the successor story); AF-5 (the missions beside it). IX.4 (the Ethiopian Church left the Methodists, not this church).
- **Mark's test:** unique. It is not a mission movement and not part of any cross-world row. It is the settler church of one colony that became a national church.
- **Recommendation:** enter, Tier 1, as a church row, 1652-1906, with the Huguenots, the Trek churches and the 1857/1881 separation as named lines. Draft the 1857 line only once a pre-1930 source is read.
- **Gate question G-AF89-4:** How should Southern Africa enter eras 8 and 9?
  - (a) Two rows: the Dutch Reformed Church (AF-4) and the mission churches (AF-5, as a wing of VIII.7).
  - (b) One row, "Christianity at the Cape and in Southern Africa, 1652-1906", holding the settler church and the mission churches together.
  - (c) The Dutch Reformed row only; leave the mission churches to VIII.7 as a line.
  - **Recommendation: (a).** They are different stories with different carriers, and the 1857 separation is the point where they meet. One row would blur the very division IX.60 is about.

##### AF-5. Southern African mission churches: Khoikhoi, Xhosa and Sotho Christianity (1737-1906) — regional absence

> **Merge note (rivers pass).** Re-homed: Southern Africa gets its own entry, not a fifth VIII.7 wing (rivers §1c); the Moravian Cape mission is a VII.4 line before 1815 and an RV-5 line after. See G89-3 and G89-5.

- **Kind:** cross-church grouping of mission-born churches (Moravian, London Missionary Society, Glasgow and Free Church of Scotland, Wesleyan, Paris Evangelical, Anglican), the same kind as VIII.7's four wings. Not a movement with its own name, so the four marks do not apply; it is a regional set of church bodies.
- **Era:** 8 and 9.
- **Dates:** 1737 (Georg Schmidt's Moravian mission among the Khoikhoi [S for the year; McCarter quotes his letter of the end of 1740]) to 1906. VIII.7's own start is 1793.
- **Region / countries / lane:** Africa. South Africa, Lesotho, Botswana [S]. Lane 6 Protestant & Evangelical.
- **What it holds.** Genadendal, the Moravian station abandoned and restored (1792 [S]); van der Kemp and Bethelsdorp (LMS, from 1803 [S]) and John Philip's campaign for Khoikhoi rights (1828); Ntsikana, the first well-known Xhosa Christian, and his hymn; the Glasgow mission and Lovedale [S]; Moshoeshoe and the Paris missionaries (1833); Tiyo Soga, "the first ordained preacher of his race"; Robert Moffat at Kuruman and Livingstone's first years [S]; and the African clergy whose quarrels with the missions produced the Ethiopian churches of the 1880s-90s (already in IX.4).
- **Section A:** clear. Mainline Protestant mission bodies, each on a dated confession of its sending church [S per body]; same floor as VIII.7.
- **B1 Sourcing:** good. Public-domain own-voice and mission texts read this run: Philip (1828), Casalis (1861), Chalmers's life of Tiyo Soga (1877, with Soga's own words), McCarter (1869), Latrobe (1771, Library). Ntsikana's hymn survives in Xhosa [S]. Tiyo Soga's own writings (his Xhosa *Pilgrim's Progress*, 1867 [S]).
- **B2 Ecology:** full. Mission stations, schools and printing, conversion and its costs, frontier war, land and labor law, African evangelists and the first African clergy.
- **B3 Uniqueness:** high as a region; moderate as a kind, since VIII.7 already holds the pattern elsewhere.
- **B4 Audience:** Southern African Christians; historians of mission and colonialism; readers of IX.4 and IX.60.
- **B5 Scale:** tiebreak only.
- **Tier:** 2 as a fifth wing of VIII.7; 1 if Mark wants a Southern African row.
- **Evidence:**
  1. Benjamin La Trobe, *A Succinct View of the Missions ... of the Church of the Brethren* (London, 1771), `cic/texts/latrobe-benjamin_succinct-view-of-the-missions_1771.txt`. **V.** "An attempt has also been made to bring the Gospel among the Hottentots at the Cape of good Hope. Our Brethren lived five years among them, begun a school with the children, and baptized also seven adult Hottentots. But certain circumstances interfering, this Mission could not be continued." The church's own summary.
  2. McCarter 1869. **V.** Schmidt "could only address them through an interpreter"; at the end of 1740 he wrote: "The whole congregation consists of ten men, ten women, seven boys and five girls. Of these thirty-two, fifteen read the New Testament (in Dutch)."
  3. John Philip, *Researches in South Africa*, vol. 1 (London: James Duncan, 1828) (archive.org `10432272bsb`). **V.** "It was among the people that had been engaged in this insurrection against the farmers, that Dr. Vanderkemp began his labours; and the other missionary stations of the London Missionary Society within the colony, sprang out of Bethelsdorp". Advocate's account.
  4. Eugène Casalis, *The Basutos; or, Twenty-Three Years in South Africa* (London: James Nisbet, 1861) (archive.org `basutosortwentyt00casa`). **V** (chapter "Moshesh (in 1833)", the missionaries' first meeting with him). Missionary witness.
  5. John A. Chalmers, *Tiyo Soga: A Page of South African Mission Work* (1877) (archive.org `tiyosogapageofso00chal`). **V.** Ntsikana, the head man of a village, "kept up religious services with his people" after the missionary Williams died, and "before his death, about the beginning of 1821, he enjoined his people to remove to the station on the Gwali". In his letter to Dr Somerville dated 23 July 1861, on the laying of the foundation of the Mgwali mission church, Soga writes that he opened the service "by giving out the great hymn of the first notable Kafir convert Ntsikana". Chalmers calls Soga "the first ordained preacher of his race". ("Kafir" is the source's period term; it is a slur today and would not be used in census copy.)
  6. Elphick and Davenport 1997; Hastings 1994. **V-s.**
  7. Wanted: Ntsikana's hymn in Xhosa from a pre-1930 printing; Tiyo Soga's journal and letters (published 1983 [S], so not public domain).
- **Living today:** yes; the Moravian Church in South Africa, the Uniting Presbyterian, Methodist and Lesotho Evangelical churches continue [S]. CR at most, pending a dated item.
- **Overlap:** VII.4 (the Moravians: Genadendal is their work, and Mark's own test puts a worldwide order's work in its one row); VIII.7 (the mission-society family; it names four wings and says "East Africa, Madagascar and Alaska each have an entry of their own", so Southern Africa is the one region it neither holds nor sends elsewhere); IX.4 (the Ethiopian churches that left these missions); AF-4 (the settler church beside them).
- **Mark's test:** the missions are cross-world movements, so this belongs inside existing rows: Genadendal and the 1740s mission as a named line in **VII.4**, and the LMS, Scottish, Paris and Wesleyan churches as a fifth wing in **VIII.7**. What is unique is the African converts' story (Ntsikana, Soga), which a wing can carry.
- **Recommendation:** named lines: a Southern African wing in VIII.7 (rename to five wings), and a Cape line in VII.4. Not a new row unless Mark prefers one (option b).
- **Gate question G-AF89-5:** Where do the Southern African mission churches go?
  - (a) A fifth wing in VIII.7, plus a named line in VII.4 for the Moravian Cape mission.
  - (b) A new row, "Southern African mission Christianity, 1737-1906".
  - (c) Leave them out until AF-4 is settled.
  - **Recommendation: (a).** It follows Mark's test (one movement, one row) and VIII.7's own design. It changes VIII.7's name, which is a frozen field, so it is a change order either way.

##### AF-6. The Catholic mission revival in nineteenth-century Africa (c. 1830-1906)

> **Merge note (rivers pass).** The line in VIII.29 is widened from Africa to the whole nineteenth-century Catholic mission revival; MEP, the Lazarists and the restored Jesuits sit in it (rivers §1b). See G89-2.

- **Kind:** cross-church movement inside one church (Catholic missionary congregations: the Spiritans under Libermann, the Society of African Missions of Lyon, Lavigerie's White Fathers, Comboni's institutes, the Lazarists and Jesuits [S for most foundings]).
- **Era:** 9.
- **Dates:** c. 1830 (the French in Algiers [S]) or 1840s (the Spiritan revival [S]) to 1906 (IX.59's start).
- **Region / countries / lane:** Africa. Algeria, Tunisia, Sudan, Uganda and Tanzania, Senegal, Gabon, Nigeria and Dahomey, Mauritius and Réunion [S per country]. Lane 5 Latin West & Catholicism, or the 4 to 5 bridge IX.59 uses.
- **The gap.** IX.59 (from 1906) "carries on the Catholic half of the Uganda Martyrs' story", so its only predecessor is VIII.43 (Buganda). VIII.29 names "the growth of missionary Catholicism" in one clause and nothing African. Lavigerie, the White Fathers outside Buganda, Comboni, the Sudan mission under the Mahdi, Père Laval in Mauritius and the West African missions are on no row.
- **Section A:** clear (the Catholic Church).
- **Four marks (as a movement inside the church):**
  - **Beginning:** Lavigerie reached Algiers on 16 May 1867 (V); Comboni's *Piano* (read in its 1867 printing; first issued 1864 [S]).
  - **Carriers:** named missionary congregations (White Fathers, V by name in Clarke; others [S]).
  - **Name:** no single name of its own in the sources read. Scholars speak of a nineteenth-century Catholic missionary revival [S]. This mark is weak.
  - **Recognition:** Hastings 1994 treats it [S for the chapter].
  - Three marks shown, the name mark weak. As a movement it is closer to a trend than a defined movement; as a set of named congregations it is defined.
- **B1 Sourcing:** good for its leaders (public-domain lives and writings). Thin for African Catholics' own voices before 1906, apart from the Uganda martyrs (VIII.43).
- **B2 Ecology:** good. Mission villages for freed slaves, catechists, sisters, schools, the antislavery campaign of 1888 [S], and martyrdom.
- **B3 Uniqueness:** moderate. It is the African face of a worldwide Catholic movement that VIII.29 names.
- **B4 Audience:** Catholics in Africa; historians of mission and antislavery.
- **B5 Scale:** tiebreak only.
- **Tier:** 2.
- **Evidence:**
  1. Richard F. Clarke, ed., *Cardinal Lavigerie and the African Slave Trade* (London: Longmans, Green, 1889) (archive.org `cardinallaviger01clargoog`). **V.** "By a decree dated January 12, 1867, Mgr. Lavigerie was nominated to the see of Algiers"; "The new Archbishop reached Algiers on May 16, 1867"; the famine of 1868, in which official statistics "attest that no less than 500,000 succumbed to famine and fever". The book names "the White Fathers". Admiring editor.
  2. Daniele Comboni, *Piano per la rigenerazione dell'Africa* (1867 printing) (archive.org `bub_gb_PmnxiMyev9UC`). **V.** The heading reads "Rigenerazione dell'Africa coll'Africa", and the text asks: "Non si potrebbe promuovere la conversione dell'Africa per mezzo dell'Africa?" ("Could the conversion of Africa not be promoted by means of Africa?" *(my rendering)*). The founder's own words.
  3. Hastings 1994. **V-s.**
  4. Jacques-Désiré Laval in Mauritius (1841-64); the Spiritans and François Libermann; Josef Ohrwalder's *Ten Years' Captivity in the Mahdi's Camp* (1892), not found on archive.org by title this run: all [S].
- **Living today:** yes (the Catholic Church in Africa; IX.59).
- **Overlap:** VIII.29 (the parent: Rome's century); VIII.43 (Buganda, the White Fathers' best-known field); IX.59 (the successor); VIII.42 (Catholic missions in Madagascar, a passing mention).
- **Mark's test:** this is the clearest case of a single worldwide movement, like the Jesuits. The nineteenth-century Catholic mission revival is one movement across Africa, Asia and Oceania, and VIII.29 already claims it in a clause. So it belongs inside **VIII.29**, as a named line, with an edge from VIII.29 to IX.59. Only the White Fathers are an Africa-only body.
- **Recommendation:** named line in VIII.29 (Lavigerie, the White Fathers, Comboni, Laval), and a new "gave rise to" edge VIII.29 to IX.59, graded on a read source. Not a new row.
- **Gate question G-AF89-6:** Where does the Catholic mission revival in Africa go?
  - (a) A named line in VIII.29, plus an edge to IX.59.
  - (b) A new era 9 row, "The Catholic Church in Africa, 1830-1906", as IX.59's predecessor.
  - (c) Extend IX.59 back to 1867 or so.
  - **Recommendation: (a).** It passes Mark's test only as part of the worldwide Catholic movement. (b) is defensible later if the region's Catholic story before 1906 grows past what a line can hold.

##### AF-7. Eastern Catholic lines: the Coptic Catholics and the Ge'ez-rite Catholics (1741-1906)

- **Kind:** two small Eastern Catholic church bodies.
- **Era:** 8 and 9.
- **Dates and places:** Coptic Catholics in Egypt: first Catholic metropolitan with jurisdiction, Athanasius, appointed 1741 (V, Butcher); a patriarchate named in 1824 and filled in 1895 [S]. Ge'ez-rite Catholics in Ethiopia and Eritrea: Justin de Jacobis, Lazarist, from 1839; Ghebre Mikael, died in custody 1855 [S]; the community at Halai and Akkele Guzay [S].
- **Lane:** Greek East / Latin West bridge is the precedent (VII.23 Melkites), but these are Oriental, not Greek, rites; a 4 to 5 bridge fits better.
- **Section A:** clear (in communion with Rome; Chalcedonian).
- **B1 Sourcing:** thin in what was read: one V line (Butcher on 1741); Bruce on the Propaganda missions among the Copts (V); Crummey 1972 for de Jacobis (V-s, cited on VIII.49). No own-voice text read.
- **B3 Uniqueness:** real (no row), but small.
- **Tier:** 3 as rows; fine as named lines.
- **Living today:** yes, the Coptic Catholic Church and the Eritrean and Ethiopian Catholic Churches [S]. CR at most.
- **Mark's test:** both are fruit of Propaganda's worldwide mission. Their communities are local. They are best told inside the church they came out of.
- **Recommendation:** named lines: Coptic Catholics in AF-2; Ge'ez-rite Catholics in AF-1 (to 1855) and VIII.49 (after). Hold any row for sources.
- **Gate question G-AF89-7:** (a) Named lines in AF-2 and AF-1/VIII.49; (b) one Eastern Catholic row for Africa, on the VII.23 model; (c) hold. **Recommendation: (a).**

##### AF-8. West Africa before the mission societies (1650-1793): forts, chaplains and the first African clergy

- **Kind:** not one body. A set of figures and small congregations at the Gold Coast forts and the first settler churches.
- **Era:** 8.
- **What is there.** Jacobus Capitein, a Gold Coast-born former slave ordained in the Dutch Reformed Church, whose Leiden dissertation of 1742 argued that slavery did not contradict Christian freedom, and who served at Elmina [S]. Philip Quaque, ordained for the SPG in 1765 and chaplain at Cape Coast Castle until 1816 [S]. Rebecca Protten in West Africa (already a gap story in VII.4). The Nova Scotian settlers' churches at Freetown from 1792 (VII.16 names David George). Liberia from 1822 ("sits inside" VIII.7's orbit).
- **Section A:** clear (Reformed, Anglican, Baptist, Methodist).
- **Evidence:** no item opened this run for Capitein or Quaque. The only public-domain-era lead found is a modern translation of Capitein (2001), not public domain. All [S].
- **Mark's test:** each figure belongs to a cross-world body already on the roster: Capitein to the Dutch Reformed (AF-4's parent church; no era 8 Dutch row), Quaque to VII.20 (the Church of England; the SPG), Protten to VII.4, George to VII.16, Liberia to VIII.7.
- **Recommendation:** named lines only, in VII.20 (Quaque) and VII.16 (Freetown), once a pre-1930 source is read; Capitein waits on AF-4 or a Dutch line. Hold for sources.
- **Gate question G-AF89-8:** (a) Hold all as named lines for sources (recommended); (b) a West African era 8 row; (c) out of scope.

##### AF-9. Protestant missions in Egypt and Ethiopia (1752-1906)

> **Merge note (rivers pass).** Partly re-homed: the American Mission in Egypt goes into RV-4, with a link from VIII.13; the Moravians in Cairo and Algiers stay a VII.4 line (rivers §1c, §1e). See G89-3.

- **Kind:** mission churches. The American (United Presbyterian) Mission in Egypt from 1854 and the Evangelical Church that grew from it [S for its synod date]; the Moravians in Cairo (V, Latrobe 1771: "three Brethren are now resident at Cairo in Egypt" with "the Copts in Egypt and Abyssinia" as the special object); the CMS in Ethiopia from 1830 (Gobat, Kugler, Krapf; V for Gobat's journal); the Chrischona men at Gafat (already in VIII.49); the Swedish mission in Eritrea from 1866 and Onesimos Nesib's Oromo Bible (1899) [S], the roots of IX.20's Mekane Yesus.
- **Era:** 8 and 9.
- **Evidence:** Watson 1898 (V, as above); Latrobe 1771 (V); Gobat 1834 (V); Crummey 1972 (V-s).
- **Mark's test:** the Moravians and the CMS are cross-world movements (VII.4; VIII.7's family). The American Mission is one society's work. None is a separate story apart from the churches it worked among.
- **Recommendation:** named lines: the American Mission in VIII.13; the Moravians in Cairo and Algiers in VII.4 (La Trobe also names Brother Richter, who went to the Christian slaves of Algiers in 1740 and died of the plague, V); the CMS and the Swedish mission in AF-1, VIII.49 and IX.20. No new row.
- **Gate question G-AF89-9:** (a) Named lines as above (recommended); (b) an "Evangelical Church of Egypt" row from 1854; (c) out of scope.

---

#### 3. Carried already, or out of scope (stated so the reasoning is kept)

- **Ethiopianism (1880s-1906).** Carried by IX.4 (Tile in the 1880s; Mokone's Ethiopian Church, November 1892). The AME union of 1896 [S] could be a line in IX.4 or VIII.1. No new row.
- **Madagascar.** VIII.42 (1818-1895). The Lazarist attempt at Fort-Dauphin in the 1640s-1670s [S] is too small for a row. After 1895 the gap to IX (no Malagasy row in era 10) was raised in the era 10 sweep (its C6).
- **Buganda and East Africa.** VIII.43 (1844-1906).
- **Sierra Leone, the Niger, Crowther, Liberia.** VIII.7 (its West African wing; "Liberia sits inside its orbit").
- **The Antonian movement.** VII.11.
- **Nubia.** The Nubian church ends with V.18 (c. 1484). Nothing in 1650-1906.
- **North Africa before 1830.** The Christians there were European captives, consuls and the redemptionist friars, with the Moravian Richter in Algiers (V, above). No African church body. Out of scope; a line in VII.19 at most.
- **Kitawala and Watch Tower bodies.** Era 10, and held out of scope by the era 10 sweep (its C12, on the Jehovah's Witness precedent).

#### 4. Notes for existing rows (not candidates; flagged, not touched)

- **IV.26 has no `continuesAs`,** and no row carries the Copts from c. 1300 to 1854. Open-Gaps 142 dates the break from 1517. The 1300-1517 part belongs to the era 6 owner.
- **VI.13a's relationsSummary** says the Antonian movement "may have grown out of it, as one modern study holds"; the edge VI.13a to VII.11 is graded Inferential-Thin. AF-3 would give that edge a home with real context.
- **VIII.7 says its "four named wings have fixed boundaries".** Adding a Southern African wing (AF-5) is a change to that sentence and to the row's name.
- **IX.59 has one predecessor (VIII.43).** AF-6's edge from VIII.29 would add the second.
- **IX.60 has no predecessor in South Africa.** AF-4 would be it.

---

## 4. Latin America and the Caribbean

The pass's `candidates.md`, as written, with its headings demoted two levels. Changes: British to American spelling in the pass's own prose, and a merge note at the head of each candidate the rivers pass gave a new home.

### Eras 8 and 9 completeness sweep (P2-G89) — Latin America and the Caribbean, 1650 to 1906

Researcher: Opus 5.5, regional pass "latam". Read only outside this folder; no commits; no metered
model calls. Census read: `cic-website/data/world-census.json` on branch `claude/p2-g89-sweep`.
Scratch research for the gate, not census copy.

**Verification key (as the brief sets it).** **V** = I opened the item in this run (a Library file
in `cic/texts/`, or a public-domain edition fetched raw with curl) and confirmed the detail; file and
line, or URL, given. **V-s** = the detail is seen only in a study's own statement (in the repo or in
an opened study), not in the primary. **[S]** = snippet, summary, memory, or unopened. Only V carries a
sentence. Original-language titles come first, with an English gloss; renderings marked
[my rendering] are this researcher's own.

**Library check.** For Latin America and the Caribbean, 1650-1906, `cic/texts/` holds: Spanish
colonial texts mapped to VII.17 (Villagómez, Lima 1662; Hansen on Rose of Lima, 1664, with Faber's
English 1855; Peña Montenegro 1668; Toro 1689; Juana Inés 1700; Paredes 1759; Palóu 1787 and its
English 1913; Florencia 1688 in the 1895 edition; Gage 1648); and Caribbean Protestant texts mapped
to VII.4 and VII.16 (Oldendorp, *Geschichte der Mission der evangelischen Brüder auf den
caraibischen Inseln* ["History of the Brethren's mission on the Caribbean islands"], Barby 1777;
the Moravian *Periodical Accounts* vol. I, 1790; Rippon's *Baptist Annual Register* 1790-1793, with
George Liele's letters from Kingston, 1791-1793). **Nothing vendored covers Latin America or the
Caribbean between 1815 and 1906.** No file covers Brazil, Paraguay, Haiti or the French islands in
any year of the window. For era 9, every primary below was fetched raw from archive.org this run
into the scratchpad, not vendored. Open Library catalog records, fetched raw as JSON, confirm
bibliographic details only; such items are marked **V (bib)**, and nothing in their contents counts
as read.

---

#### 1. River table

| River | What the roster has, 1650-1906 (with era 7 and 10 neighbors) | Gap | Candidate |
|---|---|---|---|
| Catholic (Spanish America) | VI.13d to 1650; VII.17 colonial devotional Catholicism (c. 1600-1810; countries: Peru only); VIII.48 nineteenth-century Latin American Catholicism (1815-1906); IX.62 from 1906. VII.19 and VIII.29 are Rome-centered. | The independence wars of 1810-1815 fall between VII.17 (ends 1810) and VIII.48 (starts 1815); the priest-insurgents Hidalgo and Morelos are on no row. Cuba and Puerto Rico, Spanish colonies to 1898, are on no row. Popular Catholic movements of the 1890s (Tomóchic) are absent. Bethlemites (first order founded in the Americas) absent. | **LA8-5** (independence line in VIII.48); **LA8-8** Cuba line; **LA8-9** Bethlemites line in VII.17; Tomóchic and Juazeiro lines in VIII.48 (see LA8-3) |
| Catholic (Portuguese America) | VI.11 names Brazil once as a Jesuit field. VII.17's sources mention Afro-Brazilian rosary brotherhoods; its text and countries are Spanish America only. VIII.48 carries Brazil 1815-1906 (the religious question of the 1870s). | Colonial Brazil, 1650-1822, has no row: Vieira and the Jesuit Amazon missions, the Black brotherhoods, the Minas Gerais church. Canudos (1893-97) and Juazeiro (1889-) are absent. | **LA8-4** (Brazil in VII.17); **LA8-3** Canudos |
| Catholic, Jesuit missions | VI.11 Society of Jesus ends 1650. VII.19 tells the 1759-1773 expulsions and suppression as a European story. | The Paraguay reductions (1609-1768) and the Guaraní War (1754-56); the expulsions from Brazil (1759) and Spanish America (1767). | **LA8-2** (Jesuit continuation row, shared with the China break) |
| Catholic (French Caribbean, Haiti) | VIII.46 Haiti 1804-1860. | Saint-Domingue before 1804 and Haiti 1860-1906 (the concordat church; J. T. Holly's Episcopal mission, 1861-). | **LA8-6** hold |
| Protestant and Evangelical (Caribbean) | VII.4 Moravians (St Thomas 1732, Suriname; ends 1815). VII.16 Baptists (Liele to Jamaica; ends 1815). VII.5 Methodists (no Caribbean text). Era 9: nothing. VIII.35 (Baptists) and VIII.34 (Methodists) carry North America and Britain only. | The Caribbean churches of slavery and emancipation, 1815-1906: Jamaica's Baptist War (1831-32), emancipation (1834/1838), free villages, Calabar College, the 1860-61 revival, Morant Bay (1865); Demerara (1823). Also: the Moravian church has no row at all after 1815. | **LA8-1**; Moravian break noted (§3) |
| Protestant and Evangelical (Latin America) | IX.63 from 1916 (Panama). | Nineteenth-century beginnings: Bible Society and Lancasterian schools (Thomson, 1818-), immigrant Lutherans in Brazil (1824-), Kalley in Rio (1855-), the Presbyterian mission (Simonton, 1859), the Waldensians in Uruguay (1857). | **LA8-7** |
| Orthodox (Eastern and Oriental) | Nothing in the region before 1906. | Syrian and Lebanese Orthodox immigrants arrive from the 1880s; no in-window body is attested in the Library. | Out of window (era 10 LA-13 hold) |
| Eastern Catholic | Nothing. | Maronite immigrants from the 1880s [S]. | Out of window (era 10 LA-13 hold) |
| Syriac and other Eastern | Nothing. | Nothing in 1650-1906. | None |
| Independent, indigenous, slave-born | VII.17 names Úrsula de Jesús and Black brotherhoods; VIII.46 the Catholic-Vodou world of Haiti. | Jamaica's Native Baptists (from Liele's churches) and the 1860-61 revival; the Tzeltal Virgin of Cancuc (1712); the Talking Cross of the Caste War (1850-1901). | Native Baptists in **LA8-1**; **LA8-10** hold (Cancuc, Talking Cross) |

---

#### 2. Candidates, ranked by importance to the eras' global story

##### LA8-1. The Caribbean churches of slavery and emancipation (1815-1906)

- **Kind:** cross-church regional row (Baptist, Moravian, Methodist, Anglican, and the Black-led
  Native Baptist churches), told as one story, as VIII.1 tells the Black church in the United States.
- **Era:** 9 (1815-1906). Its era 8 roots are already on VII.4 (Moravians on St Thomas, 1732) and
  VII.16 (Liele to Jamaica).
- **Dates:** 1815-1906. Anchors: Demerara rising and John Smith's death (1823) [S]; the Jamaica
  rising led by the Baptist deacon Samuel Sharpe, Christmas 1831, and his execution at Montego Bay on
  23 May 1832 (V); emancipation in force 1 August 1834 [S], full freedom 1 August 1838 (V); free
  villages from 1838 (V); the 1860-61 revival [S]; Morant Bay, 1865, led by the Native Baptist
  Paul Bogle [S].
- **Region and countries:** Latin America (Caribbean). Jamaica; Guyana (Demerara); Barbados; Antigua
  and Barbuda; Trinidad and Tobago; US Virgin Islands; Suriname.
- **Lane:** Protestant & Evangelical.
- **Section A:** no question for the mission churches (Baptist, Moravian, Methodist, Anglican: all
  trinitarian on their own confessions). The Native Baptists and later Revival Zion are not yet
  assessable on a dated statement; they would enter as a named line under this row, not as their own.
- **B1 Sourcing:** Rich on the missionary side, thin on the enslaved side. Missionary memoirs and
  periodicals; the 1832 House of Commons and Lords committee evidence [S]; Sharpe's words survive
  only as a Methodist missionary reported them. Asymmetry: the Black deacons and leaders speak through
  white witnesses.
- **B2 Ecology:** Full: the class-leader and deacon system on the estates, the Christmas rising, the
  planters' attacks on chapels, emancipation's liturgy (the "funeral" of slavery at Falmouth), free
  villages bought by congregations, a Jamaican mission to Africa [S], revival, Morant Bay.
- **B3 Uniqueness:** High. No row in era 9 carries the Caribbean. VIII.35 and VIII.34 carry Britain
  and North America only. VIII.1 is the United States. The churches' part in ending slavery is told
  here from the inside (items 1-2), which no other row can carry.
- **B4 Audiences:** Caribbean Christians and diaspora (Britain, North America), historians of
  slavery, Baptist and Methodist readers, seekers asking whether the church upheld or broke slavery.
- **B5 Scale:** large (tiebreak only).
- **Tier:** Tier 1.
- **Four marks:** not required as a church row; it would meet them in any case (beginning; carriers;
  a name in the studies; Turner 1982 and Dayfoot 1999 below).
- **Evidence:**
  1. *eyewitness (Methodist missionary)* — Henry Bleby, *Death Struggles of Slavery*, 3rd ed.
     (London, 1868), ch. X, "Origin of the Revolt", pp. 128-130: Sharpe "had learnt from his Bible,
     that the whites had no more right to hold black people in slavery, than the black people had to
     make the white people slaves"; "I would rather die upon yonder gallows than live in slavery";
     executed at Montego Bay "on the 23rd of May, 1832"; "Sharpe was a Baptist" and used estate prayer
     meetings to spread the plan. **V** (raw djvu text, OCR lines ~5785-5915; OCR is noisy and the
     wording must be re-checked against page images before any quote enters a record) —
     https://archive.org/download/b24870109/b24870109_djvu.txt (item rights: Public Domain Mark).
  2. *memoir with Knibb's own letters* — John Howard Hinton, *Memoir of William Knibb, Missionary in
     Jamaica*, 2nd ed. (London: Houlston and Stoneman, 1849), pp. 260-262: the watchnight at the
     Falmouth Baptist chapel on 31 July 1838, Knibb's "The monster is dead: the negro is free", and the
     burial of a chain, a whip and an iron collar in a coffin the next morning; and Knibb to Joseph
     Sturge, Falmouth, 30 November 1838, on buying land for a village he "calls ... Birmingham". **V**
     (raw djvu text, lines ~11895-11975 and ~13890-13905) —
     https://archive.org/download/memoirofwilliamk00hint/memoirofwilliamk00hint_djvu.txt
     (possible-copyright-status NOT_IN_COPYRIGHT).
  3. *own text, era 8 root (Library)* — George Liele's letter, Kingston, Jamaica, 12 April 1793, in
     Rippon, *Baptist Annual Register* (`cic/texts/rippon_baptist-annual-register-1790-1793_1793.txt`,
     line 41617). **V** (location only). Already mapped to VII.16.
  4. *own text, era 8 root (Library)* — Oldendorp, *Geschichte der Mission ... auf den caraibischen
     Inseln S. Thomas, S. Croix und S. Jan* (Barby, 1777) (`cic/texts/oldendorp_...bossart1777.txt`).
     **V** (title and scope). Already mapped to VII.4.
  5. *study (regional)* — Arthur Charles Dayfoot, *The Shaping of the West Indian Church, 1492-1962*
     (University of the West Indies Press, 1999). **V (bib)** (Open Library record).
  6. *study* — Mary Turner, *Slaves and Missionaries: The Disintegration of Jamaican Slave Society,
     1787-1834* (University of Illinois Press, 1982). **V (bib)** for author, title, 1982; subtitle
     [S].
  7. *study (Demerara)* — Emilia Viotti da Costa, *Crowns of Glory, Tears of Blood: The Demerara
     Slave Rebellion of 1823* (Oxford University Press, 1994). **V (bib)** for author, title, publisher,
     1994; subtitle [S]. By a Brazilian historian.
  8. Wanted, not opened: James M. Phillippo, *Jamaica: Its Past and Present State* (London, 1843),
     on archive.org (jamaicaitspastpr00phil) [S]; Edwin Angel Wallbridge, *The Demerara Martyr* (1848)
     [S]; the 1832 parliamentary committee evidence [S]; Catherine Hall, *Civilising Subjects* (2002)
     [S]; the Jamaica Baptist Union's own records [S].
- **Living today:** yes in substance (the Jamaica Baptist Union, the Moravian Church in Jamaica, the
  Methodist Church in the Caribbean and the Americas) but no dated item after 2010 was read. Grade:
  none yet.
- **Overlap:** VII.4 and VII.16 hold the era 8 roots and end at 1815. VIII.35 holds the BMS and
  Carey, not Jamaica. VIII.1 is the United States. VIII.30 (Victorian Church of England) names the
  campaign against slavery in Britain, not the Caribbean churches. IX.20 names the Ethiopian Orthodox
  Church in Jamaica from 1970. No row carries any of it after 1815.
- **Recommendation:** enter (era 9 change order).
- **Gate question G-LA8-1. How should the Caribbean churches of 1815-1906 enter?** (a) One regional
  cross-church row, 1815-1906, with the Native Baptists and the 1860-61 revival as named lines.
  (b) Named lines in VIII.35 (Baptists) and VIII.34 (Methodists), with Caribbean regions added.
  (c) A Jamaica-only row. **Recommended: (a).** The story is shared across the churches (Moravians,
  Baptists and Methodists worked the same estates, and Sharpe's rising touched them all), and
  (b) would split one story across two North-Atlantic rows. (c) leaves out Demerara (1823), on Viotti da
  Costa's study.

##### LA8-2. The Jesuit reductions of Paraguay and the Jesuits' expulsion from the Americas (1609-1768) — tested against the Society of Jesus

> **Merge note (rivers pass).** Re-homed into RV-1, the Society of Jesus row, 1650-1814, as one of its lines (rivers §1a). See G89-1.

- **Kind:** first, Mark's uniqueness test. The reductions were founded, run and staffed by the
  Society of Jesus, under its own Paraguay province, and they ended because the Society was expelled
  (Portugal and Brazil 1759; Spain and its empire 1767) [S on both dates]. That is the Jesuits'
  worldwide work, which Mark ruled is "a single movement". So the reductions are **not** a separate
  movement. They belong inside a Society of Jesus continuation row, the same home the China break
  needs (Open-Gaps 142, "Catholic missions in China, 1650 to 1793").
  - What is the Guaraní's own, and is not the Jesuits'? The Guaraní Christian towns outlived the
    Jesuits in part after 1768 [S], and the Guaraní fought the Treaty of Madrid in the Guaraní War of
    1754-56 [S]. Neither has a Library voice, and no Guaraní-written source was opened this run. On
    present evidence it is a line in the Jesuit row, not a separate church row.
- **Era:** 8 (the row would run 1650-1814: from VI.11's end to the restoration of 1814, which VII.19
  already names).
- **Dates (reductions):** first reductions in Guairá and the Uruguay valley from about 1609-1610 [S];
  "nearly thirty" towns by Muratori's time (V); the bandeirante raids (V, Muratori); the 1741 bull
  (V); expulsion 1767-68 [S].
- **Region and countries:** Latin America; Paraguay, Argentina (Misiones), Brazil (Rio Grande do
  Sul), Uruguay, Bolivia (Chiquitos and Moxos) [S].
- **Lane:** Latin West & Catholicism.
- **Section A:** no question (Catholic).
- **B1 Sourcing:** Moderate-rich, almost all Jesuit and European. Muratori never saw the missions.
  Guaraní-language imprints from the mission presses exist [S]; none opened.
- **B2 Ecology:** Full: the town plan, music and liturgy, the Guaraní militias, the bandeirante raids,
  the 1750 treaty, the war, the expulsion.
- **B3 Uniqueness:** Medium as its own row (fails Mark's test); high as part of a Jesuit row, because
  no row tells the Society's work between 1650 and 1814 except as a European suppression story
  (VII.19).
- **B4 Audiences:** Paraguayan and Argentine Catholics, Jesuit readers, historians of mission and of
  indigenous peoples.
- **B5 Scale:** moderate (tiebreak only).
- **Tier:** Tier 1 inside the Jesuit row; Tier 2 alone.
- **Evidence:**
  1. *contemporary account (Italian)* — Lodovico Antonio Muratori, *Il cristianesimo felice nelle
     missioni de' padri della Compagnia di Gesù nel Paraguai* ("Happy Christianity in the missions of
     the Jesuit fathers in Paraguay"), Venice: Pasquali, 1743. **V** (raw djvu, OCR lines ~2995-3170):
     the name *Riduzione* was given because the people had been "radunato e ridotto ... a vivere in
     forma di Società e Repubblica" [my rendering: "gathered and brought ... to live as a society
     and a commonwealth"]; the towns grew "fin presso a trenta" [my rendering: "to nearly thirty"];
     the "Mammalucchi" (bandeirantes of São Paulo) destroyed fourteen Christian reductions in the
     Guaraní country. Long-s OCR; re-check against page images. —
     https://archive.org/download/A118051/A118051_djvu.txt (Public Domain Mark).
  2. *papal act (Library)* — Benedict XIV, bull *Immensa pastorum principis*, 20 December 1741, to
     the bishops of Brazil, Paraguay and the Río de la Plata, condemning those who enslave Indians,
     even baptized ones, in Brazil's interior. **V** —
     `cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`, no. 454, lines
     ~22852-22870.
  3. *study (Latin American scholarship)* — Guillermo Furlong Cárdiff, *Misiones y sus pueblos de
     guaraníes* ("The missions and their Guaraní towns"), Buenos Aires: Theoria, 1962. **V (bib)**.
  4. *study* — Barbara Ganson, *The Guaraní under Spanish Rule in the Río de la Plata* (Stanford
     University Press, 2003). **V (bib)**. Tells the Guaraní side, including after 1768 [S on content].
  5. *study* — Magnus Mörner, *The Political and Economic Activities of the Jesuits in the La Plata
     Region* (Stockholm, 1953). **V (bib)**.
  6. Wanted: Antonio Ruiz de Montoya, *Conquista espiritual* (Madrid, 1639), and his Guaraní *Tesoro*
     (1639) [S]; Martin Dobrizhoffer, *Historia de Abiponibus* (Vienna, 1784; English 1822) [S];
     the Pragmatic Sanction of 2 April 1767 [S]; R. B. Cunninghame Graham, *A Vanished Arcadia*
     (1901) [S].
- **Living today:** the reductions, no (ruins; a UNESCO site [S]). The Society, yes.
- **Overlap:** VI.11 (to 1650; names Brazil only); VII.19 (the 1759-1773 expulsions and the 1773
  suppression, told from Europe; the 1814 restoration). The China break (Open-Gaps 142) asks for
  the same home. No row carries the reductions.
- **Recommendation:** named line in a new **Society of Jesus, 1650-1814** continuation row (a
  change order that also answers the China break), not a row of its own.
- **Gate question G-LA8-2. Where do the Paraguay reductions go?** (a) A named line in a Society of
  Jesus continuation row, 1650-1814, which would also carry the Chinese Rites and the expulsions from
  the Americas. (b) Their own church row, 1609-1768, as a mission-born Christianity like VI.13d.
  (c) A named line in VII.17. **Recommended: (a).** It meets Mark's test: one Jesuit movement, one
  row, worldwide. (b) would split the Jesuits' story by place, which is what Mark warned against.
  (c) mislabels it: VII.17 is the settled diocesan and lay piety of Spanish America, not a mission
  enterprise. If the Library later gains Guaraní-written texts, (b) can be reopened as a Guaraní
  Christian row after 1768.

##### LA8-3. Canudos (Belo Monte), the Catholic holy town of the Bahia backlands (1893-1897); Juazeiro and Tomóchic as lines in VIII.48

- **Kind:** cross-church movement? No: a movement inside popular Catholicism, outside the church's
  own structures (a lay *beato*'s community, not a diocese or an order). So it needs the four marks.
- **Era:** 9.
- **Dates:** Antônio Conselheiro preaching in the Bahia backlands by 1876 (V); settles at Canudos,
  which he names Belo Monte, in 1893 (V); four army expeditions, 1896-97 [S on the count]; the town
  falls on 5 October 1897 (V for "the 5th"; month [S] in the passage read).
- **Region and countries:** Latin America; Brazil (Bahia). Related but separate (proposed as named
  lines in VIII.48, not in this row, because they are not tied to Canudos): Juazeiro do Norte, Ceará
  (Padre Cícero; the 1889 host miracle of Maria de Araújo) [S]; Tomóchic, Chihuahua, Mexico
  (followers of Teresa Urrea, "the Saint of Cabora", 1891-92) [S].
- **Lane:** Latin West & Catholicism.
- **Section A:** no question on confession: the community kept Catholic prayer, litanies and
  sacraments where it could get a priest (V for the litanies). Its apocalyptic preaching against the
  Republic is a matter for B2, not for A.
- **Four marks:**
  1. *Beginning:* the settlement at Canudos in 1893 (V, Euclides).
  2. *Carriers:* Antônio Vicente Mendes Maciel, "Antônio Conselheiro", and his followers (V).
  3. *Name:* Canudos, and Belo Monte, the community's own name for it (V, Euclides prints «Bello
     Monte» in quotation marks).
  4. *Recognition as a movement in a study:* Robert M. Levine, *Vale of Tears: Revisiting the Canudos
     Massacre in Northeastern Brazil, 1893-1897* (1992). **V (bib)** for author, title, University
     of California Press, 1992; subtitle [S].
  It is a defined movement, not a trend: one founder, one place, one community, one war.
- **B1 Sourcing:** Moderate. The great contemporary account is hostile (Euclides calls the
  Conselheiro "um gnostico bronco", a "crude gnostic"). The Conselheiro's own manuscript sermons
  survive [S] but were printed only in 1974 [S], so they fall outside the pre-1930 Library rule as
  an edition; the manuscripts are 1890s. Asymmetry: the backlanders speak through soldiers and
  journalists.
- **B2 Ecology:** Full: lay holiness, processions and litanies, the prophecies against the Republic,
  the rejection of civil marriage and new taxes [S on civil marriage; V on taxes], the church's
  distance, and the army's destruction of the town.
- **B3 Uniqueness:** High. VIII.48's ordinary Catholics keep "confraternities, patronal feasts and
  household saints" with few priests; no row tells a lay-led Catholic holy community. It is also the
  best-known Latin American religious movement of the century in its own literature.
- **B4 Audiences:** Brazilian Catholics, readers of Brazilian literature, historians of popular
  religion and millennialism, seekers asking about faith and the poor.
- **B5 Scale:** tens of thousands at Canudos [S] (tiebreak only).
- **Tier:** Tier 2 (a bounded movement) — Tier 1 if Mark wants era 9 to carry one popular Catholic
  movement for Latin America.
- **Evidence:**
  1. *contemporary account (Portuguese)* — Euclydes da Cunha, *Os Sertões (Campanha de Canudos)*
     ("The Backlands: the Canudos campaign"), 3rd corrected ed., Rio de Janeiro: Laemmert, 1905
     (first ed. 1902 [S]). **V** (raw djvu text; OCR lines given): the Conselheiro at Itapicuru de
     Cima in 1876 (~7195); his arrival at Canudos "em 1893" (~8026); his preaching against the
     Republic from 1893 over the new municipal taxes (~7933-7945); prophecies printed as the
     community's, «Em 1896 hade rebanhos mil correr da praia para o certão; então o certão virará
     praia e a praia virará certão» [my rendering: "In 1896 a thousand flocks will run from the coast
     to the backlands; then the backlands will become coast and the coast will become backlands"]
     (~7503-7506); «Canudos não se rendeu» [my rendering: "Canudos did not surrender"], falling "no
     dia 5, ao entardecer" [my rendering: "on the 5th, at dusk"] (~25566-25568). —
     https://archive.org/download/004518-completo/004518_COMPLETO_djvu.txt (Public Domain Mark).
     Where Euclides took the prophecies from is cited in a footnote not checked.
  2. *study* — Levine 1992, above. **V (bib)**.
  3. *study (Juazeiro line)* — Ralph Della Cava, *Miracle at Joaseiro* (Columbia University Press,
     1970 [S on year; Open Library lists 1968]); Portuguese, *Milagre em Joaseiro* (Paz e Terra,
     1976). **V (bib)**.
  4. *study (Tomóchic line)* — Paul J. Vanderwood, *The Power of God against the Guns of Government*
     (Stanford University Press, 1998). **V (bib)**.
  5. Wanted: Heriberto Frías, *Tomóchic* (1893; rev. 1906) [S]; Manuel Benício, *O rei dos jagunços*
     (1899) [S]; the Conselheiro's manuscript notebooks (1895, 1897) [S].
- **Living today:** Canudos, no (the town was destroyed; the site was flooded by a dam [S]). The
  Juazeiro pilgrimage, yes in substance; no dated item read. Grade: none yet.
- **Overlap:** VIII.48 (the church-state fight of the Republic; ordinary Catholic life); nothing
  carries Canudos, Juazeiro or Tomóchic. IX.62 (from 1906) does not name them.
- **Recommendation:** enter as its own movement row (era 9 change order); Juazeiro and Tomóchic as
  named lines in VIII.48. If Mark prefers fewer rows, Canudos too becomes a named line in VIII.48.
- **Gate question G-LA8-3. How should Canudos enter?** (a) Its own movement row, 1893-1897; Juazeiro
  (1889-) and Tomóchic (1891-92) as named lines in VIII.48. (b) A named line in VIII.48. (c) A row for
  "popular Catholic holy towns of the 1890s" covering all three equally. **Recommended: (a).** Canudos
  meets the four marks on its own. (c) fails Mark's test the other way: the three are unconnected
  [S on no contact], so a family row would group a trend, not a movement. (b) is the lighter fallback.

##### LA8-4. Colonial Brazil's Catholicism: the Black rosary brotherhoods, Vieira, and the sugar-mill chapels (1650-1822)

- **Kind:** church body (Portuguese America's share of colonial Catholicism). The question is
  whether it is a gap in VII.17 or a row of its own.
- **Era:** 8 (to independence in 1822 [S]; VIII.48 already carries Brazil after 1815).
- **Dates:** Vieira's rosary sermons, preached from 1633 and printed in *Maria Rosa Mystica* (Lisbon,
  1686 and 1688) (V); Antonil's account of the sugar-mill feasts (Lisbon, 1711) (V); Benedict XIV's
  bull on the enslavement of Indians in Brazil (1741) (V, Library).
- **Region and countries:** Latin America; Brazil (Bahia, Pernambuco, Minas Gerais, Maranhão).
- **Lane:** Latin West & Catholicism.
- **Section A:** no question (Catholic).
- **B1 Sourcing:** Moderate-rich. Sermons, a planter's manual, brotherhood statutes [S], Inquisition
  visitations [S]. Asymmetry: the brotherhoods' own books are unopened; the enslaved speak through
  priests and planters.
- **B2 Ecology:** Full: Black and mulatto brotherhoods of the Rosary and of St Benedict, their elected
  kings and judges of the feast, the mill chapel, the gold-rush church of Minas, the Jesuit Amazon
  missions (which belong to the Jesuit row, LA8-2).
- **B3 Uniqueness:** Medium-high. VII.17's name ("Colonial Latin American") covers Brazil, and its
  sources already list "Afro-Brazilian rosary confraternities"; but its text, voices, place label
  ("New Spain · Peru") and countries (Peru only) are Spanish America only. So Brazil is named in the
  sources and missing from the story. That makes it a gap in VII.17, not a new movement.
- **B4 Audiences:** Brazilian and Afro-Brazilian Catholics, historians of slavery, Lusophone readers.
- **B5 Scale:** large (tiebreak only).
- **Tier:** as a named strand of VII.17, Tier 1.
- **Evidence:**
  1. *own text (sermons, Portuguese)* — António Vieira, S.J., *Maria Rosa Mystica* (Lisbon: Miguel
     Deslandes, 1686), Sermão XIV, headed «Na Bahia, à Irmandade dos Pretos de hum Engenho em dia de
     São João Evangelista, anno de 1633» ("In Bahia, to the brotherhood of the Blacks of a sugar mill,
     on the feast of St John the Evangelist, 1633"), raw OCR line ~40116; and the passage (~42149-42160)
     «Não ha trabalho, nem genero de vida no mundo mais parecido á Cruz, & Payxão de Christo, que o
     vosso em hum destes Engenhos» [my rendering: "There is no labor or way of life in the world more
     like the Cross and Passion of Christ than yours in one of these sugar mills"]. **V** (OCR, long-s;
     re-check on page images). Which sermon number holds the second passage was not confirmed. —
     https://archive.org/download/mariarosamystica00viei/mariarosamystica00viei_djvu.txt
  2. *contemporary manual (Portuguese)* — André João Antonil (João António Andreoni, S.J. [S on the
     identification]), *Cultura e opulencia do Brasil por suas drogas e minas* (Lisbon: Officina Real
     Deslandesiana, 1711): masters leave enslaved people unbaptized for long periods (~1415-1420); the
     enslaved crown their own kings and hold "suas festas de Nossa Senhora do Rosario, de São
     Benedito, & do Orago da Capella do Engenho" [my rendering: "their feasts of Our Lady of the
     Rosary, of St Benedict, and of the patron of the mill chapel"], with elected "Juizes, & Juizas da
     Festa" (~1545-1552). **V** (raw OCR). —
     https://archive.org/download/culturaeopulenci00anto/culturaeopulenci00anto_djvu.txt
  3. *papal act (Library)* — *Immensa pastorum principis* (1741), as in LA8-2. **V**.
  4. *study (Latin American scholarship)* — Eduardo Hoornaert et al., *História da Igreja no Brasil*
     ("History of the church in Brazil"), CEHILA, Petrópolis: Vozes, 1977. **V (bib)** (first author,
     title, publisher, 1977).
  5. *study* — C. R. Boxer, *The Golden Age of Brazil, 1695-1750* (University of California Press,
     1962). **V (bib)**.
  6. Wanted: A. J. R. Russell-Wood on the Black brotherhoods (1974) [S]; Elizabeth Kiddy, *Blacks of
     the Rosary* (2005) [S]; a brotherhood *compromisso* (statute) printed before 1930 [S].
- **Living today:** the Rosary brotherhoods and the Congado/Reinado feasts of Minas Gerais, yes in
  substance [S]; no dated item read. Grade: none yet.
- **Overlap:** VII.17 (name and sources cover it; text does not). VI.11 (Brazil as a Jesuit field).
  VIII.48 (Brazil after 1815). Vieira's Amazon mission and his fight with the settlers over Indian
  slavery belong to the Jesuit row (LA8-2).
- **Recommendation:** named strand in VII.17, by change order: Brazil added to its text, voices,
  place label and countries.
- **Gate question G-LA8-4. Where does colonial Brazil go?** (a) A named strand in VII.17, with Vieira's
  rosary sermons and the Black brotherhoods, and Brazil added to its countries and place label.
  (b) Its own row, "Colonial Brazilian Catholicism, 1650-1822". (c) Leave VII.17 as it is.
  **Recommended: (a).** VII.17's own name and sources already claim Brazil; the fix is to make its
  story match them. (b) is possible if Mark wants Portuguese America to stand beside Spanish America
  in era 8 as Kongo stands beside Japan in VI.13.

##### LA8-5. Priests in the wars of independence: Hidalgo and Morelos (1810-1815) — the VII.17 / VIII.48 seam

- **Kind:** not a church body or a movement of its own; a seam between two rows. VII.17 ends at
  1810 and VIII.48 starts at 1815. The years the parish priests Miguel Hidalgo (1810-11) and José
  María Morelos (1811-15) led the Mexican insurgency, under the banner of Our Lady of Guadalupe [S],
  sit in neither, and neither names them.
- **Era:** 8/9 boundary. **Region:** Latin America; Mexico (also the clergy in the South American
  wars [S]). **Lane:** Latin West & Catholicism.
- **Section A:** no question. **B1-B5:** sourcing rich (insurgent decrees, the bishops' edicts of
  excommunication [S]); ecology full; uniqueness high as a line (no row has it); audiences Mexican
  Catholics and historians; tier: a Tier 1 line, not a row.
- **Evidence:**
  1. Carlos María de Bustamante, *Cuadro histórico de la revolución mexicana, comenzada en 15 de
     septiembre de 1810 por el ciudadano Miguel Hidalgo y Costilla* (Mexico: J. Mariano Lara, 1843).
     **V** for title, imprint, and its own framing of 1810 (raw metadata and djvu of one volume:
     https://archive.org/download/cuadrohistorico01bustgoog/cuadrohistorico01bustgoog_djvu.txt).
     The volume read is a later one; nothing on Hidalgo's own acts was confirmed in it.
  2. *study* — Nancy M. Farriss, *Crown and Clergy in Colonial Mexico, 1759-1821* (London: Athlone,
     1968). **V (bib)**.
  3. *study* — D. A. Brading, *The First America* (Cambridge University Press, 1991). **V (bib)**.
  4. Wanted: J. E. Hernández y Dávalos, *Colección de documentos para la historia de la guerra de
     independencia de México* (1877-82) [S]; Abad y Queipo's edict against Hidalgo (24 September
     1810) [S]; Morelos, *Sentimientos de la Nación* (1813) [S].
- **Living today:** n/a (a line). **Overlap:** VII.17 (Guadalupe), VIII.48 (the patronato fights).
- **Recommendation:** named line in VIII.48, with its start moved to 1810 by change order (the same
  kind of era-boundary fix Open-Gaps 142 proposes for the Armenian church, 1441-1517).
- **Gate question G-LA8-5.** (a) Move VIII.48's start to 1810 and add the insurgent priests as a
  named line. (b) Keep 1815; add the line to VIII.48 as background. (c) Extend VII.17 to 1815.
  **Recommended: (a).** The church's crisis of independence begins in 1810, and VIII.48 is the row
  that tells its sequel.

##### LA8-6. Haiti before 1804 and after 1860 (hold)

- **Gap:** VIII.46 runs 1804-1860 only. Before it: the church of Saint-Domingue under the Code Noir
  (1685) [S], the Jesuits' expulsion from the colony (1763) [S], and the religious side of the 1791
  rising (Bois Caïman, whose sources are contested [S]). After it: the concordat church run by
  French and Breton clergy [S], and the Episcopal mission of James Theodore Holly, who led
  African American emigrants to Haiti in 1861 and was consecrated bishop of Haiti in 1874 [S].
- **Evidence:** Anne Greene, *The Catholic Church in Haiti: Political and Social Change* (Michigan
  State University Press, 1993) — **V (bib)**; David M. Dean, *Defender of the Race: James Theodore
  Holly* (Boston: Lambeth Press, 1978) — **V (bib)** for author, short title, publisher, 1978. No
  French or Kreyòl primary was opened this run; no Library file covers Haiti.
- **Section A:** no question (Catholic; Episcopal). **Tier:** Tier 2 lines.
- **Recommendation:** hold for sources. When sourced: Holly as a named line in VIII.46 (with its end
  moved to 1906) or in VIII.1; Saint-Domingue as a named line in VII.17 or VII.19.
- **Gate question G-LA8-6.** (a) Hold, with the Code Noir (1685), a French account of the concordat
  church, and Holly's own writings on the wanted list. (b) Extend VIII.46 to 1906 now, on Greene and
  Dean. (c) Nothing. **Recommended: (a).** Two studies, no primary opened.

##### LA8-7. Protestant beginnings in Latin America (1818-1906)

- **Kind:** cross-church (Bible Society agents, immigrant churches, missions). **Era:** 9.
- **Dates:** James ("Diego") Thomson, Bible Society agent and Lancasterian schoolman, arrives at
  Buenos Aires on 6 October 1818 and works on to Chile, Peru and Colombia (V); German Lutheran
  colonists in Brazil from 1824 [S]; Robert Reid Kalley's Igreja Evangélica Fluminense, Rio, 1858
  [S]; Ashbel Simonton's Presbyterian mission, Rio, 1859 [S]; the Waldensian colonies in Uruguay
  from 1857 [S]; Allen Gardiner's Patagonian mission and death (1851) [S].
- **Region and countries:** Latin America; Argentina, Chile, Peru, Colombia, Brazil, Uruguay, Mexico.
- **Lane:** Protestant & Evangelical.
- **Section A:** no question (trinitarian Protestant bodies).
- **B1:** moderate; the agents' and missionaries' letters, mission reports, Brazilian Protestant
  historiography. **B2:** schools and Bibles, religious-liberty laws, immigrant enclaves, the first
  Latin American converts and pastors. **B3:** medium-high: IX.63 starts at Panama 1916, and its
  own why ("Few of them were Latin Americans") presumes a prior century no row tells. **B4:** Latin
  American Protestants, historians. **B5:** small before 1906 (tiebreak only). **Tier:** Tier 2.
- **Evidence:**
  1. *own text* — James Thomson, *Letters on the Moral and Religious State of South America, written
     during a residence of nearly seven years in Buenos Aires, Chile, Peru, and Colombia* (London,
     1827): Buenos Aires, 5 June 1820 ("I arrived on the 6th October, 1818"; proposals to the
     government for "the Lancasterian System of education"); Santiago de Chile, 8 October 1821
     ("Through the gracious providence of the God of the Bible Society"). **V** (raw djvu, lines
     ~232-262, ~725-750) — https://archive.org/download/lettersonmorala00thomgoog/lettersonmorala00thomgoog_djvu.txt
     (NOT_IN_COPYRIGHT).
  2. *study (Latin American scholarship)* — Jean-Pierre Bastian, *Historia del protestantismo en
     América Latina* (Mexico: CUPSA, 1990). **V (bib)**.
  3. *study (Brazil)* — Émile-G. Léonard, *O protestantismo brasileiro* (São Paulo: ASTE, 1963).
     **V (bib)**.
  4. Wanted: Kalley's and Simonton's own journals [S]; Bastian, *Los disidentes* (1989) [S].
- **Living today:** yes (IX.63 carries it from 1916). Grade: n/a here.
- **Overlap:** IX.63 (from 1916). VIII.7 (missions; no Latin America). VIII.41 (confessional
  Lutheran emigrations; its regions are North America, North Europe and the Pacific, not Brazil).
- **Recommendation:** named lines, not a row: the immigrant Lutherans in VIII.41 (Brazil added),
  and the Bible-Society and mission beginnings as an opening line of IX.63, reached across the
  1906 line as IX.62 reaches back to VIII.48. Or its own era 9 row if Mark wants Latin American
  Protestantism to have a nineteenth-century entry.
- **Gate question G-LA8-7.** (a) Named lines (VIII.41 for Brazil's Lutherans; a "before 1916"
  line in IX.63). (b) An era 9 row, 1818-1906. (c) Nothing. **Recommended: (a).** Before 1906 it is
  small, foreign-led and scattered; the roster tells it best as the prelude of IX.63.

##### LA8-8. Cuba and Puerto Rico under Spain (1815-1898): a line in VIII.48

- **Gap:** VIII.48 is the story of the independent republics and Brazil. Cuba and Puerto Rico stayed
  Spanish colonies to 1898 [S], with a church still under the crown's patronage. Antonio María
  Claret was archbishop of Santiago de Cuba, 1851-1857, and founded the Claretians in 1849 [S].
- **Evidence:** none opened this run. **Recommendation:** named line in VIII.48, held for sources.
- **Gate question G-LA8-8.** (a) Hold; a line in VIII.48 when a source is opened (Claret's
  *Autobiografía* is a lead [S], but its first printing may be after 1930). (b) Nothing.
  **Recommended: (a).**

##### LA8-9. The Bethlemites, the first religious order founded in the Americas (Guatemala, 1650s-1820): a line in VII.17

- **Gap:** Pedro de San José de Betancur (d. 1667, Santiago de Guatemala) [S] founded the hospital
  brotherhood that became the Order of Bethlehem, approved in 1687 [S]. VII.17 names Lima and
  Mexico, not Central America.
- **Evidence:** none opened this run. **Recommendation:** named line in VII.17, held for sources.
- **Gate question G-LA8-9.** (a) Hold; a line in VII.17 when sourced. (b) Nothing. **Recommended: (a).**

##### LA8-10. Indigenous Christian movements: the Virgin of Cancuc (1712) and the Talking Cross (1850-1901) (hold)

- **Cancuc (Tzeltal Maya, Chiapas, 1712).** A Virgin's appearance at Cancuc; Maya leaders ordained
  their own priests and rose against Spanish rule [S]. Four marks: beginning 1712 [S]; carriers
  (María de la Candelaria, Sebastián Gómez de la Gloria) [S]; name (the Cancuc or Tzeltal rebellion)
  [S]; study: Kevin Gosner, *Soldiers of the Virgin: The Moral Economy of a Colonial Maya Rebellion*
  (University of Arizona Press, 1992) — **V (bib)** for author, short title, publisher, 1992;
  Victoria Reifler Bricker, *The Indian Christ, the Indian King* (University of Texas Press, 1981) —
  **V (bib)**. Section A: Catholic in form; an indigenous priesthood not ordained by any bishop [S].
  It is a defined movement on Gosner's terms.
- **The Talking Cross (Maya of Yucatán, Chan Santa Cruz, 1850-1901).** A speaking cross guided the
  rebel Maya of the Caste War [S]. Study: Nelson Reed, *The Caste War of Yucatan* (Stanford
  University Press, 1964) — **V (bib)**; Bricker 1981. Section A is a real question: whether the Cross
  cult confesses Christ in A1's sense is not assessable on any dated statement read.
- **Living today:** the Cruzob shrines in Quintana Roo, yes in substance [S]; nothing dated read.
- **Overlap:** none. VII.17 and VIII.48 do not name indigenous movements.
- **Recommendation:** hold for sources. Cancuc, when sourced, as a named line in VII.17 (Tier 2);
  the Talking Cross needs Section A settled first.
- **Gate question G-LA8-10.** (a) Hold both, with Ximénez's chronicle (for Cancuc) and a dated
  Cruzob text on the wanted list. (b) Cancuc as a line in VII.17 now, on Gosner. (c) Nothing.
  **Recommended: (a).** No primary for either was opened; no Maya-language source is in the Library.

---

#### 3. The timeline breaks, answered

**"Latin America, thin for 1492-1900" (Open-Gaps 142, closing note).** The roster has VI.13d
(1524-1650), VII.17 (c. 1600-1810), VIII.46 (1804-1860) and VIII.48 (1815-1906); the note counted
three because VIII.46 carries the region "North America". Checked against every overlapping row by
name, place and text (VI.11, VII.4, VII.16, VII.19, VIII.29, VIII.34, VIII.35, VIII.41, IX.62,
IX.63). The thinness is real but uneven. Each gap was put to Mark's test ("check that they are
unique and not tied to other movements, like jesuites moving around the world, that is a single
movement"):
- **Tied to another movement — not separate rows:**
  - Paraguay reductions and the 1759/1767 expulsions: the Society of Jesus. Home: a Jesuit
    continuation row, 1650-1814 (new; the same row the China break needs). VI.11 ends at 1650;
    VII.19 tells only the European suppression. (LA8-2)
  - Moravian and Baptist missions in the Caribbean before 1815: already on VII.4 and VII.16.
  - Colonial Brazil: already claimed by VII.17's name and sources; a gap in its text. (LA8-4)
  - Hidalgo and Morelos: the VII.17 / VIII.48 seam; a line in VIII.48. (LA8-5)
  - Nineteenth-century Protestant beginnings: the prelude to IX.63; lines. (LA8-7)
- **Unique — not carried by any row, and not part of a wider movement:**
  - The Caribbean churches of slavery and emancipation, 1815-1906. (LA8-1; enter)
  - Canudos, 1893-1897. (LA8-3; enter)
- **Unique but held for sources:** Haiti before 1804 and after 1860 (LA8-6); Cuba and Puerto Rico
  (LA8-8); the Bethlemites (LA8-9); Cancuc and the Talking Cross (LA8-10).
- **Before 1650 (outside this sweep, flagged):** VI.13d covers New Spain and the Andes only; Brazil,
  New Granada (Pedro Claver at Cartagena, d. 1654 [S]) and the Caribbean have no era 7 entry.

> **Merge note (rivers pass).** The Moravian question G-LA8-M is answered by RV-5, one era 9 Moravian row continuing VII.4 (rivers §1d). See G89-4.

**A break this pass found.** **The Moravian church has no row after 1815.** VII.4 ends in 1815, and
no era 9 or era 10 row is Moravian (VIII.7, VIII.9 and VIII.35 name the Moravians only as a model
for others). VII.4's own legacy says most of its members are now "in Tanzania and the Caribbean".
The church is the same movement, not a new one, so the answer is a continuation (a VII.4 era 9
segment, or Caribbean and African lines in LA8-1 and the Africa pass), not a new movement. This
belongs to whichever pass owns the North Europe river; it is noted here because the Caribbean is
half of it. Gate question **G-LA8-M.** (a) A Moravian era 9 continuation row. (b) Caribbean lines
in LA8-1, Tanzanian lines in the Africa pass. (c) Log it in Open-Gaps 142 for a later pass.
**Recommended: (c)** now, with (b) as the content route if LA8-1 enters.

**The other logged breaks** (Ethiopia, Copts, Church of the East, St Thomas Christians, China,
Japan, Maronites, Georgia, Melkites, Syriac Orthodox, Old Believers, Galicia) lie outside this
region. None has a Latin American or Caribbean part before 1906. The Maronite and Syriac
diasporas in Brazil, Argentina and Mexico begin in the 1880s [S] and are held for era 10 (the era 10
sweep's LA-13).

---

#### 4. Out of scope (stated, so the reasoning is kept)

- **Vodou, Santería, Candomblé, Kardecist Spiritism (Brazil from the 1860s [S]).** Not Christian
  movements under A1. VIII.46 already names the Catholic-Vodou world of Haiti.
- **Túpac Amaru II (1780-81).** A political rising with Catholic symbols [S], not a church movement.
- **The Malê rising in Bahia (1835).** A Muslim rising [S]; not Christian.
- **Junípero Serra and the California missions.** VII.17 carries them.
- **Guadalupe, Rose of Lima, Martín de Porres, Sor Juana, Úrsula de Jesús.** VII.17 carries them.
- **Mexico's Reforma, García Moreno, Brazil's religious question, the 1899 Plenary Council.** VIII.48
  carries them.

#### 5. Doc-hygiene flags (not touched)

- VIII.46 (Haiti) carries the region "North America", not "Latin America". That is why the
  Open-Gaps 142 note counts only three Latin American entries.
- VII.17's countries list Peru only, and its place label is "New Spain · Peru", while its name says
  "Latin American" and its sources name Afro-Brazilian brotherhoods.
- VIII.48's countries list Brazil only, while its text names Mexico and Ecuador.
- VI.13d has no countries, no longDescription, no voices, no legacy and no sources.
- VII.17's dates read "c. 1600-1810" and overlap VI.13d (to 1650).

#### 6. Wanted (for the source-research thread)

1. Montoya, *Conquista espiritual* (1639) and *Tesoro de la lengua guaraní* (1639); Dobrizhoffer
   (1784; English 1822); the 1767 Pragmatic Sanction.
2. Phillippo, *Jamaica: Its Past and Present State* (1843) — on archive.org; Wallbridge, *The
   Demerara Martyr* (1848); the 1832 parliamentary evidence on the Jamaica rising. Bleby (1868) and
   Hinton (1849), opened this run, are ready to vendor.
3. Euclides da Cunha, *Os Sertões* (1902/1905) — opened this run, ready to vendor; Frías, *Tomóchic*.
4. Vieira, *Maria Rosa Mystica* (1686) and Antonil (1711) — opened this run, ready to vendor; a
   Brazilian brotherhood *compromisso* printed before 1930.
5. Hernández y Dávalos, *Colección de documentos* (1877-82), for Hidalgo and Morelos.
6. Thomson, *Letters* (1827) — opened, ready to vendor; Kalley's and Simonton's journals.
7. For Haiti: the Code Noir (1685); a French account of the concordat church; Holly's own writings.
8. For Cancuc: Francisco Ximénez's chronicle of the Dominican province of Chiapas and Guatemala.
9. Muratori, *Il cristianesimo felice* (1743) — opened, ready to vendor.

---

## 5. Asia and the Pacific

The pass's `candidates.md`, as written, with its headings demoted two levels. Changes: British to American spelling in the pass's own prose, and a merge note at the head of each candidate the rivers pass gave a new home.

### P2-G89 eras 8 and 9 sweep — Asia and the Pacific (1650–1906), every river

Scratch research for the gate, not census copy. Written as it went; the river table and the
ranking were added at the top once the pass ended.

**Verification key.** **V** = I opened the item in this run (a Library file in `cic/texts/`, or a
public-domain edition opened raw with curl) and confirmed the detail; the locus is given. **V-s** = a
study's bibliographic details only, confirmed in this run from a catalog record opened raw
(archive.org metadata, NDL Search); its contents were not read. **[S]** = snippet, summary, memory or
unopened; never counts as verified. **wanted** = searched for, not found. Only V carries a sentence.
English renderings of French, Latin or Japanese marked [my rendering] are this researcher's own.

Region scope: South Asia (with the St Thomas Christians of Kerala), China, Japan, Korea, Southeast
Asia (the Philippines, Vietnam, Siam, Burma, the Dutch East Indies), Australia, New Zealand and the
Pacific islands. The Church of the East in Persia and Mesopotamia belongs to the Middle East pass;
it is touched here only where it reaches Kerala.

Roster read: `cic-website/data/world-census.json`, rows of eras 7–10 touching the region (era field
7 = VI.x, 8 = VII.x, 9 = VIII.x, 10 = IX.x). Rows that carry the region in eras 8 and 9: VII.29
(Philippines 1650–1815); VIII.7 (Protestant native churches: Serampore, Pacific Islands, China coast
and CIM); VIII.21 (Korean Catholic origins 1784–1886); VIII.26 (Indonesia 1861–1906); VIII.27
(Mar Thoma reform and Northeast India 1836–1906); VIII.39 (Philippines 1815–1906); VIII.44 (Taiping);
VIII.45 (Japan 1865–1906). Rows that name the region in passing: VII.2 (Ziegenbalg to Tranquebar,
1706), VII.19 (Jesuit suppression, told as European), VIII.31 (missions to the Altai and to Japan
from 1861), VIII.41 (Old Lutherans to South Australia, 1838), VIII.25 (Azariah and Cheng Jingyi at
Edinburgh 1910). A text search of every row found no mention at all of Vietnam, Tonkin, Cochinchina,
Ceylon or Sri Lanka, Burma or the Karen, Siam (outside era 6), Taiwan or Formosa, Ambon or Batavia,
Tahiti, Hawai'i (as a place), Ringatū or Pai Mārire, the Boxer year, Goa after era 7, the Padroado,
Kangxi, Schall or Verbiest, the Russian mission in Peking, or the Missions Étrangères de Paris.

#### River table (1650–1906)

| River | Roster has (eras 8–9, region) | Gap | Candidate(s) |
|---|---|---|---|
| Catholic | VII.29, VIII.39 (Philippines); VIII.21 (Korea to 1886); VIII.45 (Japan from 1865); VII.19 and VIII.29 (Rome-centered, Mediterranean) | China 1650–1906 (logged break); Japan's hidden centuries 1650–1865 (logged break); Vietnam (absent in every era); Ceylon and Goa (absent after era 7); Korea 1886–1906; the Cofradía de San José | AP2, AP3, AP4, AP6, AP15, AP10; cross-region AP-X1 (Jesuits), AP-X2 (MEP) |
| Orthodox (Eastern and Oriental) | VIII.31 names the Japan mission (from 1861) and VIII.45 Nikolai; the Syriac Orthodox tie of Kerala only from 1836 (VIII.27) | Kerala's Syriac Orthodox party 1665–1815 (in AP1); the Russian mission in Peking and the Albazinians | AP1, AP11 |
| Protestant and Evangelical (incl. Anglican) | VIII.7 (Serampore, Pacific Islands, China coast, CIM); VIII.26 (Indonesia from 1861); VIII.27 (hill revivals); VII.2 names Tranquebar; VIII.41 names South Australia | The VOC churches (Moluccas, Batavia, Ceylon) 1650–1815; the Tamil Lutheran church after 1750; the Karen Baptists; colonial Australia and New Zealand; Korea 1884–1906 | AP5, AP8, AP9, AP12, AP15; AP14 (carried in VIII.7) |
| Syriac and other Eastern churches | VI.18 (to 1665); VIII.27 (Mar Thoma and Malankara from 1836) | St Thomas Christians 1665–1815 (logged break); the Chaldean Syrian body at Thrissur | AP1, AP7 |
| Eastern Catholic | none in eras 8–9 for the region | The Catholic St Thomas Christians (Romo-Syrians) 1665–1906 | AP1, AP7 |
| Independent, indigenous | VIII.44 (Taiping); VIII.39 (Aglipayan church, 1902); VIII.26 (Sadrach); VIII.45 (Kakure, named) | Japan's hidden Christians as a church without clergy; Māori prophetic churches (Pai Mārire, Ringatū); the Cofradía de San José | AP3, AP13, AP10 |

#### Ranked list (importance to the eras' global story)

| Rank | ID | Candidate | Era | Recommendation |
|---|---|---|---|---|
| 1 | AP2 | Chinese Catholicism 1650–1906, court mission, Rites, hidden provinces (logged break) | 8–9 | enter; China-church row, Jesuits and Rites as lines |
| 2 | AP1 | St Thomas Christians 1665–1815, two obediences (logged break) | 8 | enter |
| 3 | AP4 | Vietnamese Catholicism 1650–1906 | 8–9 | enter (two segments) |
| 4 | AP3 | Japan's hidden Christians 1650–1865 (logged break) | 8–9 | enter |
| 5 | AP5 | VOC Protestant churches: Moluccas, Batavia, Ceylon 1650–1815 | 8 | enter (or line in VIII.26) |
| 6 | AP6 | Catholics of Ceylon under the Dutch and the Goa Oratory 1658–1806 | 8 | enter (or a wider South Asian Catholic row) |
| 7 | AP7 | Catholic St Thomas Christians and the Thrissur body 1815–1906 | 9 | hold; then extend AP1 |
| 8 | AP13 | Māori prophetic movements 1862–1906 | 9 | hold for a Māori source |
| 9 | AP9 | Karen Baptists 1828–1906 | 9 | named line in VIII.7 |
| 10 | AP8 | Tamil Lutheran church after Ziegenbalg | 8 | named line in VII.2 |
| 11 | AP10 | Cofradía de San José 1832–41 | 9 | hold; then line in VIII.39 |
| 12 | AP15 | Korea 1884/1886–1906 | 9 | hold; then named lines |
| 13 | AP12 | Colonial Australia and New Zealand churches | 9 | hold; then lines in parent rows |
| 14 | AP11 | Russian mission in Peking, Albazinians | 8–9 | hold |
| 15 | AP14 | Pacific Christian kingdoms | 9 | carried by VIII.7 |
| — | AP-X1 | Jesuit era 8 continuation (cross-region) | 8 | decide at merge; Asia evidence says no |
| — | AP-X2 | MEP / Propaganda row (cross-region) | 8–9 | carrier lines only |

#### How the logged breaks were answered

- **St Thomas Christians, 1665–1815:** a real, unique gap. Answered by AP1 (enter, era 8 row, both
  parties). Two community texts of the window are in the Library (Whitehouse App. D and App. E).
- **Catholic missions in China, 1650–1793, with the Rites controversy:** the roster is empty for
  China's Catholics from 1650 to 1906, not only to 1793. Mark's test applied: the Jesuits are one
  carrier (the court, 1650–1773); the Rites were decided by Propaganda, the Holy Office and two
  popes; after 1724 the provincial church ran under Chinese priests, Lazarists and MEP. Right home:
  a China-church row (AP2) with the Jesuit court mission and the Rites as named lines. Not VI.11
  continued (it would end at 1773), and not an MEP/Propaganda row (AP-X2: a carrier, not the
  subject). A worldwide Jesuit era 8 row is a cross-region choice (AP-X1).
- **Japan's hidden Christians, 1650–1865:** a real, unique gap. Not the Jesuits' story; not
  VIII.45's (which starts on 17 March 1865). Answered by AP3 (enter).

---

#### Candidate sections (in the order assessed; the ranking is above)

##### G89-AP1 — The St Thomas Christians, 1665–1815: two obediences (logged break)

- **Kind:** church body (one community in two parties: the Catholic "Romo-Syrian" party, Pazhayakūr,
  under Carmelite vicars apostolic of Verapoly and the Padroado see of Cranganore; and the Malankara
  party, Puthenkūr, under its own Mar Thoma metropolitans with Syriac Orthodox bishops from 1665).
- **Era:** 8 (1665–1815).
- **Dates:** 1665, Mar Gregorios of Jerusalem, sent by the Syriac Orthodox patriarch, reaches
  Malabar (V, Whitehouse App. D). 1708, the East Syriac bishop Mar Gabriel arrives (V, App. D).
  1751, three Syriac Orthodox bishops arrive; 1772, Mar Thoma VI consecrated as Mar Dionysius I (V,
  App. B notes). 1 February 1787, the Angamaly document signed by 84 churches (V, App. E). 1806,
  Buchanan meets Mar Dionysius at Kandanad (V). 1815/16: the CMS "Mission of Help" begins and VIII.27
  takes the story from 1836.
- **Region / countries:** Greater Asia — India (Kerala: Travancore, Cochin, the Malabar coast).
- **Lane:** Syriac East & Asia (the lane of VI.18 and V.23).
- **Section A:** Both parties clear on dated texts of their own period. The Catholic party is under
  Rome (Nicene creed). The Malankara party's own "Brief History" says Mar Evanius (1678) "taught that
  Christ has one nature and that the Holy Ghost is equal with the Father and the Son" (Whitehouse,
  App. D, file line ~19245, V, in English translation): a Trinitarian, Miaphysite statement inside
  the window, the Syriac Orthodox confession.
- **B1:** Strong. In-window primary texts are vendored: Raulin, *Historia Ecclesiae Malabaricae*
  (Rome 1745, Latin), the Carmelite Sebastiani's two *Speditione* (1666, 1672, Italian), and two
  documents the community wrote itself, in translation in Whitehouse (1873): App. D, the Malankara
  party's "Brief History", and App. E, the Catholic party's Angamaly document of 1787. Buchanan's
  eyewitness of 1806 opened raw. Studies: Brown 1956, Bayly 1989 (1700–1900, exactly this period),
  Neill 1985 (1707–1858) — all V-s. Malayalam own-voice: Paremmakkal Thoma Kathanar's
  *Varthamanappusthakam* (c. 1790, the first Malayalam travel book, about the 1778–86 journey to
  Rome) is wanted; no pre-1930 printing was found.
- **B2:** Strong: liturgy changing rite (East Syriac to West Syriac for one party), hereditary
  bishops of the Pakalomattam family, rival bishops excommunicating each other's priests, the Dutch
  and then the British as arbiters, Tipu's invasion (1789).
- **B3:** High. The break is real and unique: VI.18 ends at 1665, VIII.27 starts at 1836, and the
  1665 turn to Antioch — the root of today's Malankara Orthodox, Jacobite, Mar Thoma and Thozhiyur
  churches — has no row. Not tied to another movement: the Carmelites and the Syriac Orthodox
  bishops are agents here, but the story is the community's own (App. E is its own voice).
- **B4:** Thoughtful believers (unity and rite), Eastern Christians, academic users, learners.
- **B5:** Mid (one regional community). The Angamaly document is signed for "eighty-four churches"
  of the Catholic party alone (App. E, line ~19405); no total for both parties was verified.
- **Tier:** Tier 1 (a logged break on a frozen era's only Indian church line).
- **Evidence:**
  - Whitehouse, *Lingerings of Light in a Dark Land* (London 1873), App. E, "The document signed by
    all the Church people of Malankara ... in the Large Church of Angamale, on the first of February
    ... 1787" — `cic/texts/whitehouse_lingerings-of-light-in-a-dark-land_1873.txt`, lines 19283–19415
    — *community's own text, in translation* — **V**.
  - Same, App. D, "Abstract of a brief history of the Syrians in Malabar, preserved among themselves"
    — lines 19012–19280 (1665, 1678, 1708, 1751 entries read at 19232–19262) — *community's own
    text, in translation* — **V**.
  - Same, App. B notes on the bishops (1761, 1772, 1806, d. c. 1814; 1816) — lines 18815–18835 —
    *secondary, 1873* — **V**.
  - Same, ch. XII, the arrival of Mar Gregorios in 1665 — lines 11815–11865 — *secondary* — **V**.
  - Claudius Buchanan, *Christian Researches in Asia* (London: G. Sidney, 1811), "Cande-nad, a Church
    of the Syrian Christians, November 23, 1806" — archive.org `christianresearc0000clau`, djvu text,
    lines ~4350–4535 — *eyewitness* — **V**.
  - Raulin, *Historia Ecclesiae Malabaricae cum Diamperitana Synodo* (Rome 1745) —
    `cic/texts/raulin_historia-ecclesiae-malabaricae-cum-diamperitana-synodo-lat_1745.txt` —
    *in-window Latin* — present in the Library; mapped to VI.18 and V.23; not read for this window
    in this run — **[S]** for content.
  - Sebastiani, *Prima* and *Seconda speditione all'Indie Orientali* (Rome 1666, 1672) —
    `cic/texts/sebastiani_*` — present; the 1657–63 missions fall mostly inside VI.18 — **[S]**.
  - E. Philipos, *The Syrian Christians of Malabar* (ed. Howard, 1869), by a Kerala Syrian priest —
    `cic/texts/philipos_syrian-christians-of-malabar_howard1869.txt` — present, not read this run —
    **[S]**.
  - L. W. Brown, *The Indian Christians of St Thomas* (Cambridge UP, 1956) — archive.org
    `indianchristians0000lesl` — **V-s**.
  - Susan Bayly, *Saints, Goddesses and Kings: Muslims and Christians in South Indian Society,
    1700–1900* (Cambridge UP, 1989) — archive.org `saintsgoddessesk0000bayl` — **V-s**.
  - Stephen Neill, *A History of Christianity in India, 1707–1858* (Cambridge UP, 1985) — archive.org
    `historyofchristi0000neil` — **V-s**.
  - Frykenberg, *Christianity in India* (OUP 2008) — repo-cited — **[S]** in this run.
  - Paremmakkal Thoma Kathanar, *Varthamanappusthakam* (Malayalam, c. 1790) — **wanted**.
- **Quote (V, in translation):** "we will have no Bishop but from among ourselves" — Angamaly
  document, 1 Feb 1787, Whitehouse App. E (line ~19385). English as printed in 1873; the Malayalam
  original was not seen.
- **Living today:** yes, through its heirs (IX.39, IX.38, and the Syro-Malabar Church); for this
  row, n/a (historical segment). No dated item graded.
- **Overlap:** VI.18 (to 1665; its relationsSummary names the heirs but not the period); VIII.27
  (from 1836); IX.39 (from 1912). Corpus-map `the-malankara-churches-orthodox-and-jacobite.yaml`
  already places Whitehouse ch. XII ("the arrival of Mar Gregory and the alliance with the Jacobites
  after 1665") on IX.39 — a sign the content wants a home before 1912. None carries 1665–1815.
- **Recommendation:** enter (era 8 row, change order).
- **Gate question:** How should the St Thomas Christians' 1665–1815 enter?
  - (a) One era 8 row for the whole community, both parties, 1665–1815, in the Syriac East lane.
  - (b) Extend VI.18's end date to 1815 (one row 1599–1815).
  - (c) Two era 8 rows, one per party.
  - **Recommended:** (a). The two parties share one story of a community choosing its bishops; (b)
    stretches an era 7 row across an era boundary, and (c) splits what App. E and App. D tell as one
    history.

##### G89-AP2 — Chinese Catholicism, 1650–1906: the court mission, the Rites controversy and the hidden provinces (logged break)

- **Kind:** church body (the Catholic Church in China: the Beijing court mission, the provincial
  communities, Chinese priests, catechists and consecrated "virgins").
- **Era:** 8 and 9 (1650–1906). The logged break is 1650–1793; the roster is in fact empty for
  Chinese Catholics from 1650 to 1906 (VIII.7's China wing is Protestant; VIII.44 is the Taiping;
  IX.65 starts in 1906).
- **Dates (V unless marked):** 23 March 1656, the Holy Office answers the Jesuits' 1645 queries and
  "censuit permittendas sinensibus christianis" the Confucius ceremonies, "quia videtur cultus esse
  mere civilis et politicus" (Collectanea I, file lines 7131–7490). 1659, Propaganda's instruction
  to the new vicars apostolic: "Quid enim absurdius quam Galliam, Hispaniam, aut Italiam ... in Sinas
  invehere?" (lines 8185–8200). A toleration edict obtained on St Joseph's day (Lettres édifiantes
  III, line ~8717; the OCR prints "1602", and the context — Verbiest's successors, the Kangxi reign —
  points to 1692 [S on the year]). 22 November 1723, the Fujian viceroy's memorial asks that the
  Europeans stay at court but leave the provinces for Macao, and the Christian religion is
  proscribed (de Mailla, Peking, 16 Oct 1724, Lettres édifiantes III, lines 41805–42690). 4 October
  1726, Propaganda rules that native priests, "sinenses, cocincinenses, tunquinenses", must also
  swear the oath of *Ex illa die* (Collectanea I, lines 18645–18660; the OCR prints "17236" between
  entries of 1726), and notes that *Ex illa die* is recited inside Benedict XIV's *Ex quo* of
  11 July 1742 (line ~18763). 1773 suppression of the Jesuits: carried by VII.19. 1844–46 treaty
  toleration, 1870 Tianjin, 1900 Boxer killings: **[S]**, not verified in this run.
- **Region / countries:** Greater Asia — China (Beijing, Fujian, Sichuan, Jiangnan; Macao).
- **Lane:** Latin West & Catholicism (the lane of VI.13c and IX.65).
- **Section A:** Clears: Catholic, Nicene. The Rites dispute was about practice, not the creed.
- **B1:** Good for era 8. In-window primary texts V: the Propaganda *Collectanea* (vendored) and the
  Jesuit *Lettres édifiantes* (opened raw). Studies V-s: Bays 2012, Minamiki 1985, Mungello 1994.
  Chinese-language sources wanted: Huang Bolu (黃伯祿), 正教奉褒 *Zhengjiao fengbao* ("Records of
  imperial favor to the true religion", Shanghai 1883), the Chinese text of the 1692 edict, and the
  Chinese text of the 1723 memorial. None was found raw. Era 9 evidence is thin in this run.
- **B2:** Strong: the court astronomers; ancestor rites and Confucius halls; a church that lived a
  century (1724–1840s) with few priests, held by Chinese priests, catechists and lay "virgins"; the
  French protectorate; the Boxer year.
- **B3:** High. The longest-lived Catholic mission in East Asia has no row for 256 years.
- **B4:** Historically interested learners, Catholics, academic users; the rites question (can a
  Christian honor ancestors?) is one participants still ask.
- **B5:** Large [S on numbers; none verified].
- **Tier:** Tier 1.
- **Mark's test (unique, not tied to another movement):** The break is tied to the Jesuits only
  in part. The Jesuits are the carriers of the court mission (1650–1773), and the Rites controversy
  began with their method. But the Rites decisions were made by Propaganda, the Holy Office and two
  popes against Dominicans, Franciscans and MEP priests as well, and their subject was Chinese
  practice. After 1724 the story is the provincial communities' own, under Chinese priests (the 1726
  ruling shows them already ordained) and, after 1773, Lazarists and MEP. A Jesuit row would carry
  only the court half and would end at 1773; the communities run on to IX.65. So the unique story is
  the China church, and the Jesuit court mission is one line in it.
- **Evidence:**
  - *Collectanea S. Congregationis de Propaganda Fide*, vol. I (Rome 1907) —
    `cic/texts/propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt`, lines
    7131–7490 (1656), 8120–8200 (1659), 18645–18763 (1726, 1742) — *in-window decrees, Latin* — **V**.
  - Lettre du P. de Mailla, "Proscription de la religion chrétienne", Peking, 16 October 1724, in
    *Lettres édifiantes et curieuses concernant l'Asie, l'Afrique et l'Amérique*, ed. Aimé-Martin,
    vol. 3 (Paris 1838) — archive.org `lettresdifiantes03jesu`, djvu lines 41805–42690 — *in-window
    letter, French, quoting the viceroy's memorial in translation* — **V**.
  - Same volume, the toleration edict passage — line ~8717 — **V** for the passage; the year **[S]**.
  - Daniel H. Bays, *A New History of Christianity in China* (Wiley-Blackwell, 2012) — archive.org
    `newhistoryofchri0000bays` — **V-s**.
  - George Minamiki, *The Chinese Rites Controversy from Its Beginning to Modern Times* (Loyola UP,
    1985) — archive.org `chineseritescont0000mina` — **V-s**.
  - D. E. Mungello, *The Forgotten Christians of Hangzhou* (University of Hawai'i Press, 1994) —
    archive.org `forgottenchristi0000demu` — **V-s**.
  - VI.13c's Library voices (Trigault 1615, Purchas) stop before 1650 — checked in corpus-map.
  - Huang Bolu, 正教奉褒 (1883); Kangxi edict of 1692 (Chinese); the 1723 memorial (Chinese) —
    **wanted**.
- **Quote (V, Latin, then [my rendering]):** "Quid enim absurdius quam Galliam, Hispaniam, aut
  Italiam, aut aliam Europae partem in Sinas invehere?" — "For what could be more absurd than to
  carry France, Spain, Italy or some other part of Europe into China?" — Propaganda's instruction of
  1659, Collectanea I, lines ~8196–8198.
- **Living today:** the church lives on in IX.65 (era 10). For this row, n/a.
- **Overlap:** VI.11 (Jesuits, to 1650: names the China mission's start); VI.13c (to 1650);
  VII.19 (suppression of 1773, as a European story); VIII.7 (Protestant China coast); VIII.21
  (names Beijing for Yi Sung-hun's baptism, 1784); IX.65 (from 1906). None carries 1650–1906.
- **Recommendation:** enter. Era 8 for certain; era 9 either in the same row or a second segment,
  after one verified era 9 source (the 1840s toleration or the 1900 killings).
- **Gate question:** Where does China's Catholic story of 1650–1906 go?
  - (a) A China-church row, 1650–1906 (or two segments split at 1815), with the Jesuit court
    mission and the Rites controversy as named lines inside it.
  - (b) An era 8 continuation of VI.11, the Society of Jesus 1650–1814, carrying the court mission
    and the Rites (and, from other regions, the Paraguay reductions and the Malabar rites), plus a
    smaller China-church row from 1724.
  - (c) A named line in VII.19.
  - **Recommended:** (a). It passes Mark's test: the China church is a single story that outlives
    the Jesuits, while the Jesuits are one of its carriers. (b) is right only if Mark wants the
    Jesuits' worldwide work kept as one movement after 1650 too; that is a cross-region question for
    the merge (see AP-X1).

##### G89-AP3 — Japan's hidden Christians (Sempuku Kirishitan), 1650–1865 (logged break)

- **Kind:** church body without clergy (village communities keeping baptism and prayer under a
  ban), assessed as a church row; not a movement outside church bodies.
- **Era:** 8 and 9 (1650–1865).
- **Dates:** The ban runs from 1614 (VI.13b). The annual image-trampling test, *e-fumi*, was used to
  find Christians (V, Marnas, lines ~3345–3352). 17 March 1865, three women from Urakami tell
  Petitjean "Notre cœur à nous tous ... est le même que le vôtre" and ask "Sancta Maria no gozowa
  doko?" (V, Marnas, lines 21260–21280, from Petitjean's letters of 18 and 22 March 1865). VIII.45
  takes the story from that day.
- **Region / countries:** Greater Asia — Japan (Urakami and Sotome near Nagasaki, the Gotō islands,
  Ikitsuki, Hirado).
- **Lane:** Latin West & Catholicism (the lane of VI.13b and VIII.45).
- **Section A:** Not assessable on a dated statement of the period: the communities kept prayers
  and a baptismal formula orally and in hidden books, and no dated confession of theirs was opened.
  Assessed at the world level per A5: they are the continuation of a church that clears (VI.13b).
  Whether the later Kakure (after 1873) still clear is a separate question VIII.45 already flags.
- **B1:** Adequate. Marnas (1896) is a pre-1930 study built on the MEP archive and Petitjean's
  letters, opened raw. Their own scripture, 天地始之事 *Tenchi hajimari no koto* ("The Beginning of
  Heaven and Earth", known from copies of the 1820s [S]), is the communities' own voice: the
  Japanese text was not found raw; Whelan's English translation (1996) is V-s; Japanese studies of
  it (Mase-Hasegawa 2015; Kajita) V-s from NDL Search. Urakawa Wasaburō (浦川和三郎), 『切支丹の復活』
  *Kirishitan no fukkatsu* ("The Resurrection of the Kirishitan", 1927–28), a Japanese priest's
  pre-1930 study, V-s from NDL Search; not opened.
- **B2:** Strong: lay offices (prayer leader and baptizer, Marnas lines 22335–22362), a hidden
  liturgical calendar, Marian images disguised as Kannon [S], the e-fumi, the 1865 discovery.
- **B3:** High. Survival of a church for two centuries with no priest is a case the world history of
  Christianity always cites; the roster says so in VI.13b and VIII.45 but gives the years no row.
- **B4:** Broad: thoughtful believers (faith without clergy), pastors, learners, academic users.
- **B5:** Small to mid. Within weeks of 17 March 1865 the missionaries counted "3800 chrétiens":
  about 1,300 at Urakami and 2,500 in the hills and nearby islands (Marnas I, lines 22180–22184, V).
  VIII.45's figure of about 30,000 who came forward later was not checked here.
- **Tier:** Tier 1 (a logged break with a strong story).
- **Mark's test:** Unique. Not the Jesuits' story: the order had no priest in Japan after the 1640s
  [S], and the communities kept the faith on their own. Not VIII.45's story, which begins on
  17 March 1865.
- **Evidence:**
  - Francisque Marnas, *La "Religion de Jésus" (Iaso ja-kyō) ressuscitée au Japon dans la seconde
    moitié du XIXe siècle*, vol. 1 (Paris and Lyon: Delhomme et Briguet, 1896; approbations dated
    Lyon 16 Nov 1896 and Rome 3 Dec 1896) — archive.org `lareligiondejsus01marn`, djvu text; lines
    3345–3365 (e-fumi), 21260–21290 (17 March 1865), 22335–22362 (the village offices) — *pre-1930
    study quoting primary letters, French* — **V**.
  - Christal Whelan (trans.), *The Beginning of Heaven and Earth: The Sacred Book of Japan's Hidden
    Christians* (University of Hawai'i Press, 1996) — archive.org `beginningofheave0000unse` —
    **V-s**.
  - Stephen Turnbull, *The Kakure Kirishitan of Japan* (Japan Library 1998; Routledge reissue,
    archive.org `kakurekirishitan0000step`, 2016) — **V-s**.
  - 浦川和三郎 Urakawa Wasaburō, 『切支丹の復活』 (日本カトリック刊行会, 1927–28) — NDL Search record
    R100000136-I1970586434864565008 — **V-s**.
  - 長谷川(間瀬)恵美 Mase-Hasegawa Emi, 「キリシタン神学の可能性 : 『天地始之事』を巡って」 (2015) — NDL
    Search — **V-s**.
  - 天地始之事 (Japanese text) — **wanted**.
  - Léon Pagès, *Histoire de la religion chrétienne au Japon*, annexes (1870), vendored, stops at 1651
    — checked in corpus-map (kirishitan-japan.yaml).
- **Quote (V, French, then [my rendering]):** "Notre cœur à nous tous, qui sommes ici, est le même
  que le vôtre." — "The heart of all of us here is the same as yours." — Marnas I, lines
  21268–21269, after Petitjean's letters of 18 and 22 March 1865. (Fits VIII.45 more than this row;
  for this row, the village-office passage is the better anchor.)
- **Living today:** the Kakure line lives on in a few communities (VIII.45 says "remain separate to
  this day"). No dated item after 2010 was opened: grade none.
- **Overlap:** VI.13b (to 1650; its relationsSummary names the 250 years); VIII.45 (from 1865).
- **Recommendation:** enter (era 8 row running to 1865, or era 8 and era 9 segments).
- **Gate question:** How should the hidden centuries enter?
  - (a) One row, 1650–1865, crossing the era 8/9 line, in the Latin West lane.
  - (b) Extend VIII.45 back to 1650.
  - (c) Extend VI.13b forward to 1865.
  - **Recommended:** (a). The hidden period is its own form of church life; (b) and (c) would bury it
    in rows about a mission and a re-emergence.

##### G89-AP4 — Vietnamese Catholicism, 1650–1906

- **Kind:** church body (the Catholic communities of Tonkin and Cochinchina, under vicars apostolic
  of the MEP and Spanish Dominicans, and Padroado/ex-Jesuit communities).
- **Era:** 8 and 9 (with era 7 roots from 1615/1627 that no row carries either).
- **Dates (V unless marked):** 1651, Alexandre de Rhodes's *Cathechismus* in Latin and Vietnamese
  ("Cathechismum Latinum, Tunchinensem"), Rome, Propaganda press; license dated Rome 8 July 1651.
  1658, Propaganda names Pallu and Lambert de la Motte vicars apostolic "dans les Missions de Chine et
  les pays voisins" (Launay 1894, I, lines 3407–3415). 1664–65, the Ayutthaya *Monita ad
  Missionarios*, which plans native priests drawn from the catechists (Launay I, 8560–9410). 1670,
  Lambert founds the Lovers of the Cross (Amantes de la Croix) (Launay 1893, lines 2741–2744); 1675,
  Propaganda grants indulgences to their confraternities "in Tunkino et Cocincina" (Collectanea I,
  lines 13795–13805). 1796, Philiphê Bỉnh sails from Tonkin to Lisbon for his ex-Jesuit community
  (Dutton 2017). 6 January 1833, Minh Mạng's first great edict of persecution (Launay 1893, lines
  2903–2925). 1832, the West Tonkin mission counts 160,000–170,000 Christians, about 60 Vietnamese
  priests, several hundred catechists and some 30 convents with 400 sisters (Launay 1893, lines
  2735–2744). 1858–85 French conquest; 1885 killings of Christians [S].
- **Region / countries:** Greater Asia — Vietnam (Tonkin, Cochinchina, Annam).
- **Lane:** Latin West & Catholicism.
- **Section A:** Clears: Catholic, Nicene; de Rhodes's *Cathechismus* (1651) is a dated catechism of
  the community's first generation.
- **B1:** Strong for a pass of this kind: an in-window primary in Latin and Vietnamese (1651), the
  Propaganda decrees (vendored), Launay's two pre-1930 MEP histories opened raw, and Dutton 2017
  (open access, opened raw), which reads Philiphê Bỉnh's own quốc ngữ writings. Vietnamese-language
  own voice: Bỉnh's *Sách sổ sang chép các việc* (1822) [S], no pre-1930 printing found — wanted.
- **B2:** Strong: a Romanized script (quốc ngữ) born in mission catechesis; the Lovers of the Cross,
  Asia's oldest native women's congregation still active [S]; catechist "houses"; martyrdom under
  Minh Mạng and Tự Đức; the colonial tie that cost the church later.
- **B3:** High. Vietnam had one of Asia's largest Catholic churches by 1800 [S on rank], and the
  roster names it nowhere, in any era.
- **B4:** Catholics, historically interested learners, academic users (religion and colonialism).
- **B5:** Large: 160,000–170,000 in one of the vicariates alone in 1832 (V).
- **Tier:** Tier 1.
- **Mark's test:** Unique. The Jesuits began it (1615/1627) and the MEP organized it, but the
  continuous carriers were Vietnamese catechists, priests and sisters. Dutton shows a Vietnamese
  ex-Jesuit community defending its own heritage after 1773 — the church, not the order, is the
  subject.
- **Evidence:**
  - Alexandre de Rhodes, *Cathechismus pro iis, qui volunt suscipere Baptismum in octo dies
    divisus / Phép giảng tám ngày* (Rome: Propaganda Fide, 1651) — archive.org `bub_gb_p8UC5ZZ21Q8C`
    (title page and license read in the djvu text) — *in-window primary, Latin and Vietnamese* —
    **V** (title page); content not read.
  - Adrien Launay, *Histoire générale de la Société des Missions-Étrangères*, vol. 1 (Paris: Téqui,
    1894) — archive.org `cihm_54000`, lines 3407–3415, 8560–9410 — **V**.
  - Adrien Launay, *Mgr Retord et le Tonkin catholique, 1831–1858* (1893) — archive.org
    `mgrretordetleton00laun`, lines 2735–2925 — **V**.
  - *Collectanea* I (vendored), line 13795 (1675, "Amatorum Crucis ... in Tunkino et Cocincina") and
    lines 18645–18660 (1726, Tonkinese and Cochinchinese native priests) — **V**.
  - George E. Dutton, *A Vietnamese Moses: Philiphê Bỉnh and the Geographies of Early Modern
    Catholicism* (Oakland: University of California Press, 2017; open access) — archive.org
    `oapen-20.500.12657-31953`, djvu text (back-cover summary, lines ~17530–17545; Tonkin estimates
    of 1639 and 1663, lines 833–836) — *scholarly study* — **V**.
  - Philiphê Bỉnh, *Sách sổ sang chép các việc* (1822) — **wanted**.
- **Quote (V, French, then [my rendering]):** "Il y avait une soixantaine de prêtres indigènes,
  plusieurs centaines de catéchistes, une trentaine de couvents avec 400 religieuses" — "There were
  some sixty native priests, several hundred catechists, some thirty convents with 400 sisters" —
  Launay 1893, lines 2740–2742 (West Tonkin, 1832).
- **Living today:** yes (the Catholic Church in Vietnam); no dated item after 2010 opened: grade
  none. Era 10 has no Vietnam row either (the era 10 sweep's Asia section raised Vietnam; no row
  carries it in release 27).
- **Overlap:** none in any era. VIII.21 and VIII.29 do not name it.
- **Recommendation:** enter (one row 1650–1906, or two segments).
- **Gate question:** How should Vietnam's Catholics enter?
  - (a) One row, 1650–1906, opening with the Jesuit and MEP beginnings as background.
  - (b) Era 8 and era 9 segments (1650–1815, 1815–1906), like the Philippine rows VII.29 and VIII.39.
  - (c) A named line in an MEP row (see AP-X2).
  - **Recommended:** (b). It matches how the roster already handles the Philippines across the same
    eras, and the 1833 edicts make a natural era 9 story. (a) is fine if Mark prefers fewer rows.

##### G89-AP5 — The Protestant churches of the Dutch East India Company world: the Moluccas, Batavia and Ceylon, 1650–1815

- **Kind:** church body (the Reformed church of the VOC settlements, with its native teachers and
  congregations: Ambon and the Lease islands, Batavia, Makassar, Semarang, Kupang; the Dutch Reformed
  church in Ceylon, 1658–1796).
- **Era:** 8 (1650–1815), with era 7 roots from 1605 and an era 9 tail (the *Indische Kerk*, 1817,
  until VIII.26 begins in 1861).
- **Dates:** 1605, the VOC takes Ambon from the Portuguese (V, Aritonang & Steenbrink, lines
  ~2431–3074). 1673, Ambon's teachers ordered to the central town (V, line ~6013). 1700, 95 of the
  VOC's 18,117 personnel serve religious needs, not counting "the native teachers, evangelisers ...
  and sacristans in East Indonesia (Ambon, Ternate, Kupang)" (V, lines 7054–7059). 1719–22, Werndly
  at Makassar translates the Heidelberg Catechism and helps correct the Leijdecker Malay Bible (V,
  lines 7060–7064). 1753, Semarang's congregation of 1,767 Christians (V, line ~7069). Ceylon:
  plakaat of 19 September 1658 against harboring Catholic priests (V, Casie Chitty, line ~609).
- **Region / countries:** Greater Asia — Indonesia (Moluccas, Java, Sulawesi, Timor), Sri Lanka.
- **Lane:** Protestant & Evangelical.
- **Section A:** Clears. School teachers "had to agree with the Heidelberg Catechism and the
  Confession of Faith of the Dutch Reformed Churches" (V, Aritonang & Steenbrink, lines ~6918–6921):
  a Reformed, Trinitarian confession binding the church's teachers in the window.
- **B1:** Good: one major open-access study opened raw (Aritonang & Steenbrink 2008, ch. 5,
  "The Arrival of Protestantism and the Consolidation of Christianity in the Moluccas 1605–1800").
  Primary texts in Dutch (Valentijn, *Oud en Nieuw Oost-Indiën*, 1724–26; the Leijdecker Malay Bible,
  1733) are [S], not opened. Malay-language own voice: wanted.
- **B2:** Good: a church of Ambonese village teachers (*guru*), Malay liturgy and psalm-singing, a
  company chaplaincy beside native congregations, Catholics forced underground in Ceylon.
- **B3:** Mid-high. Before 1800 this was the largest Protestant community in Asia [S on rank]; the
  Moluccan church (GPM) and the Indonesian Protestant Church descend from it [S]. VIII.26 mentions
  the VOC only as background.
- **B4:** Academic users, historically interested learners, Reformed believers.
- **B5:** Mid [S on totals].
- **Tier:** Tier 2.
- **Evidence:**
  - Jan Sihar Aritonang and Karel Steenbrink (eds.), *A History of Christianity in Indonesia*
    (Leiden: Brill, 2008; open access) — archive.org `oapen-20.500.12657-45624`, ch. 5 (lines
    5661–7100) — *scholarly study* — **V**.
  - Simon Casie Chitty, *A Sketch of the Rise and Progress of the Catholic Church in Ceylon*
    (Colombo, 1848) — archive.org `ASketchOfTheRiseAndProgress`, line ~609 (the 1658 plakaat) —
    *pre-1930 study by a Ceylonese author* — **V**.
  - William Campbell, *Formosa under the Dutch* (London 1903) — archive.org `cu31924023514403` —
    located, not opened (Formosa's Dutch church ends in 1662, so it is era 7) — **[S]**.
  - Valentijn (1724–26); Leijdecker Malay Bible (1733) — **[S]**.
- **Living today:** the heirs live (e.g. the Protestant Church of the Moluccas) [S]; no dated item
  graded.
- **Overlap:** VIII.26 (from 1861; its text names the VOC as background). Nothing else.
- **Recommendation:** enter, or a named line opening VIII.26 (see gate question).
- **Gate question:** Where does the VOC-era Protestant church go?
  - (a) An era 8 row, 1650–1815, Moluccas, Batavia and Ceylon.
  - (b) A named line in VIII.26, extending its story back (its dates stay 1861–1906).
  - (c) Hold for a Dutch or Malay primary text.
  - **Recommended:** (a), since era 8 has only one Greater Asia row and this church was a society's
    faith, not a mission's outpost. (b) if Mark wants fewer era 8 rows.

##### G89-AP6 — The Catholics of Ceylon under Dutch rule and the Goan Oratorians, 1658–1806

- **Kind:** church body (the Catholic community of Sri Lanka, kept by Konkani priests of the Oratory
  of St Philip Neri at Goa).
- **Era:** 8 (1658–1806).
- **Dates (V):** 19 September 1658, the Dutch plakaat forbids "harbouring or concealing Catholic
  Priests on pain of DEATH"; a second plakaat of 11 January 1715 (Casie Chitty, lines 605–612).
  Joseph Vaz of the Goa Oratory enters Jaffna "disguised as a mendicant" (OCR "J690"), is jailed at
  Kandy for nearly two years, then makes Kandy his base, visiting Catholics in Dutch territory
  "from house to house" (lines 750–815). He dies at Kandy on 17 January 1711 (line ~896). By 1717,
  about 70,000 converts, more than 15,000 communicants in Jaffna alone, 15 large and over 400 small
  churches (lines 905–911). 27 May 1806, the British regulation lifts the Dutch restraints (lines
  1060–1075).
- **Region / countries:** Greater Asia — Sri Lanka; India (Goa).
- **Lane:** Latin West & Catholicism.
- **Section A:** Clears: Catholic, Nicene.
- **B1:** Adequate. Casie Chitty 1848 (opened raw) is a Ceylonese Catholic's own pre-1930 history.
  Boudens, *The Catholic Church in Ceylon under Dutch Rule* (Rome 1957) is V-s. Portuguese-language
  life of Vaz (Sebastião do Rego, 1745) [S]; Tamil and Sinhala Catholic texts of the period (e.g.
  Jacome Gonçalves's Tamil and Sinhala works) [S] — wanted.
- **B2:** Good: an Asian clergy (the Goa Oratorians were Indian priests) running a hidden church
  under a Protestant power, protected by a Buddhist king.
- **B3:** Mid-high. Unique in pattern: an Asian-led Catholic mission, not a European order. Nothing
  on the roster names Sri Lanka in any era.
- **B4:** Catholics, learners, academic users.
- **B5:** Mid (70,000 by 1717, V).
- **Tier:** Tier 2.
- **Mark's test:** Unique: the Goa Oratory is a local Indian congregation, not a worldwide order,
  and the story is the island church's own.
- **Evidence:**
  - Casie Chitty 1848 (as AP5), lines 600–1140 — **V**.
  - Robrecht Boudens, *The Catholic Church in Ceylon under Dutch Rule* (Rome, 1957) — archive.org
    `catholicchurchin0000robr` — **V-s**.
- **Quote (V, English, 1848):** "he occasionally visited the Catholics in the Dutch territories, and
  administered to them the sacraments privately, going from house to house" — Casie Chitty, lines
  ~806–808.
- **Living today:** yes (the Catholic Church in Sri Lanka); no dated item graded.
- **Overlap:** none in any era.
- **Recommendation:** enter as a row, or a named line in a wider South Asian Catholic row (see gate).
- **Gate question:** How should South Asian Latin Catholicism (Goa, Ceylon, the Tamil coast) enter
  eras 8–9?
  - (a) A Ceylon row, 1658–1806, as assessed.
  - (b) One wider row, "Catholicism in South Asia under the Padroado and Propaganda, 1650–1906"
    (Goa and its Oratory, Ceylon, the Madurai and Tamil coast missions, the Goa schism of the
    1830s–1886 [S]), with Ceylon as its first named line.
  - (c) Hold until a Portuguese or Tamil primary is opened.
  - **Recommended:** (b) if Mark wants South Asian Catholicism told once; (a) is the better-evidenced
    single story today. The wider row's era 9 half (the double jurisdiction) is not yet sourced.

##### G89-AP7 — The Catholic St Thomas Christians and the Chaldean Syrian Church, 1815–1906

- **Kind:** church body (the Romo-Syrian or Syro-Malabar community under Latin vicars apostolic; and
  the small body at Thrissur that turned to the Church of the East).
- **Era:** 9 (1815–1906).
- **Dates:** 1896, "three Roman-Syrian priests were consecrated as bishops of titular sees, and sent
  to Travancore and Cochin as Vicars-Apostolic directly subject to the Pope", ending foreign rule
  after "a constant effort to obtain ... bishops of Syrian descent" (V, Richards 1908, lines
  2636–2650). "A small body of about 8,000, mostly at Trichur ... who have left the Roman-Syrians",
  called Nestorians (V, Richards, line 2630). 1861 and 1874 Chaldean bishops (Roccos, Mellus), 1887
  separate vicariates, Kuriakose Elias Chavara and the first Indian religious congregation (1831)
  — **[S]**.
- **Region / countries:** Greater Asia — India (Kerala).
- **Lane:** Syriac East & Asia (the Eastern Catholic line in the Syriac lane, as VI.18 sets it).
- **Section A:** Clears: Catholic (Nicene); the Thrissur body holds the Church of the East's creed
  (Nicene) — **[S]** for a dated text of either in the window.
- **B1:** Thin-to-adequate: two pre-1930 Protestant studies opened raw (Richards 1908; Rae 1892, the
  latter's relevant passage not read). No Catholic or Malayalam source opened.
- **B2:** Good: the long fight for native bishops, Syriac kept in the liturgy, a schism to the
  Church of the East.
- **B3:** Mid-high. VIII.27 carries only the Mar Thoma and Malankara side; the larger Catholic
  half of the same community has no era 9 row.
- **B4:** Eastern Catholics, learners, academic users.
- **B5:** Large within Kerala [S].
- **Tier:** Tier 2.
- **Evidence:**
  - W. J. Richards, *The Indian Christians of St. Thomas, otherwise called the Syrian Christians of
    Malabar* (London: Bemrose, 1908) — archive.org `cu31924029361379`, lines 2605–2660 —
    *pre-1930 study by a CMS missionary* — **V**.
  - G. Milne Rae, *The Syrian Church in India* (Edinburgh 1892) — archive.org `syrianchurchinin00raeg`
    — opened, relevant passage not located — **[S]**.
  - Chavara's own writings (Malayalam, the *Chronicles*); Syro-Malabar sources — **wanted**.
- **Living today:** yes (Syro-Malabar Church; Chaldean Syrian Church) [S]; no dated item graded.
- **Overlap:** VIII.27 (Mar Thoma and Malankara only); IX.39 (Malankara churches from 1912).
- **Recommendation:** named line in AP1's row if Mark extends it to 1906, or hold for a Catholic
  or Malayalam source.
- **Gate question:** Where does the Catholic half of the St Thomas Christians go in era 9?
  - (a) Extend AP1 into one St Thomas row, 1665–1906, both parties, beside VIII.27.
  - (b) A named line in VIII.27, renamed to cover the whole community.
  - (c) Hold for sources.
  - **Recommended:** (c) for now, with (a) as the target once one Catholic source is opened.

##### G89-AP8 — The Tamil Lutheran church of Tranquebar and Tanjore, 1706–1815 (and on)

- **Kind:** church body (the congregations the Danish-Halle mission gathered, with Tamil catechists
  and, from 1733, Tamil pastors).
- **Era:** 8.
- **Dates (V):** 28 December 1733, the catechist Aaron is ordained, the first Indian Lutheran
  pastor, before eleven clergymen; he then preached on Galatians 4:4 (Fenger 1863, lines 5753–5850).
  Ziegenbalg's landing (1706) and Tamil New Testament are carried by VII.2.
- **Region / countries:** Greater Asia — India (Tamil Nadu).
- **Lane:** Protestant & Evangelical.
- **Section A:** Clears (Lutheran confessions) — the mission's own texts are vendored
  (`cic/texts/ziegenbalg_propagation-of-the-gospel-in-the-east_boehm1718.txt`), not re-read for a
  creedal line this run — **[S]** for the dated statement.
- **B1:** Adequate: Ziegenbalg 1718 (vendored); Fenger 1863 opened raw; Neill 1985 V-s.
- **B2:** Good: the first Protestant church with native clergy in Asia; caste inside the church;
  the poet Vedanayagam Sastri [S].
- **B3:** Mid. VII.2 holds the founding as a Pietist mission story and ends at 1750.
- **Tier:** Tier 3 (named line).
- **Evidence:** J. Ferd. Fenger, *History of the Tranquebar Mission* (Eng. trans., Tranquebar 1863)
  — archive.org `historyoftranque00fengrich`, lines 5753–5850 — **V**. Ziegenbalg 1718 (vendored) —
  present. Neill 1985 — **V-s**.
- **Living today:** the Tamil Evangelical Lutheran Church [S]; no dated item.
- **Overlap:** VII.2 carries Ziegenbalg, Tranquebar and the Tamil New Testament (its story text
  and voices line). VIII.7 starts in 1793 with Serampore.
- **Recommendation:** named line in VII.2 (the Tamil church after Ziegenbalg).
- **Gate question:** (a) named line in VII.2; (b) its own era 8 row; (c) leave as carried.
  **Recommended:** (a): VII.2 already tells the founding, and one line keeps the Tamil church from
  vanishing at 1750.

##### G89-AP9 — The Karen Baptist movement in Burma, 1828–1906

> **Merge note (rivers pass).** Re-homed: a named line in VIII.27, whose hill revivals already hold this kind, not in VIII.7 (rivers §1c). See G89-3.

- **Kind:** church body (Karen Baptist congregations; a people movement with its own evangelists).
- **Era:** 9.
- **Dates (V):** 16 May 1828, Boardman baptizes Ko Thah-byu at Tavoy, and "the baptism of Ko
  Thah-byu, in 1828, was the commencement of the mission" (Mason, *The Karen Apostle*, lines
  405–420, 2890–2900). Judson's mission from 1813 [S].
- **Region / countries:** Greater Asia — Myanmar (Burma); Thailand [S].
- **Lane:** Protestant & Evangelical.
- **Section A:** Clears (Baptist, Trinitarian) [S on a dated statement].
- **B1:** Adequate: Mason 1843/1847 (a missionary memoir, opened raw). A modern study was not
  verified this run — wanted.
- **B2:** Good: a minority people's mass turn, carried by Karen preachers; the "lost book" tradition
  [S].
- **B3:** Mid. Burma appears on the roster only as a country tag on the hill-revival rows.
- **Tier:** Tier 3 (named line).
- **Evidence:** Francis Mason, *The Karen Apostle: or, Memoir of Ko Thah-byu, the First Karen
  Convert* (1843; ed. used: 1847, archive.org `karenapostleorme00maso`) — **V**.
- **Overlap:** VIII.7 (the missionary movement's native churches) is the natural home; VIII.35
  (nineteenth-century Baptists) is North Atlantic.
- **Recommendation:** named line in VIII.7.
- **Gate question:** (a) named line in VIII.7; (b) own row; (c) hold for a study.
  **Recommended:** (a), and add one modern study before drafting.

##### G89-AP10 — The Cofradía de San José (Hermano Pule), 1832–1841

- **Kind:** a movement inside a church body: a lay Catholic confraternity that the colonial church
  refused and the state crushed. Not a cross-church movement.
- **Era:** 9.
- **Four marks:** beginning — founded by Apolinario de la Cruz, 1832 [S]; carriers — Tagalog
  peasants of Tayabas, barred from Spanish orders [S]; name — Cofradía de San José [S];
  recognition — Ileto 1979 (V-s), which reads it through the pasyon.
- **Evidence:** Reynaldo C. Ileto, *Pasyon and Revolution: Popular Movements in the Philippines,
  1840–1910* (Ateneo de Manila UP, 1979) — archive.org `pasyonrevolution00reyn` — **V-s**. Blair &
  Robertson vols. vendored do not include the 1841 papers (vols. 7–50 partial; not searched for it)
  — **[S]**.
- **Overlap:** VIII.39 (Philippine Catholicism 1815–1906) does not name it; VII.29 carries the pasyon.
- **Recommendation:** named line in VIII.39, after one primary is opened.
- **Gate question:** (a) named line in VIII.39; (b) hold. **Recommended:** (b) now, (a) once a
  dated primary is read. It is "a defined movement", but this run verified only the study's details.

##### G89-AP11 — The Russian Ecclesiastical Mission in Peking and the Albazinians, 1685/1715–1906

- **Kind:** church body (the small Orthodox community of Beijing, descended from Albazin captives,
  with the Russian mission; the Chinese Orthodox martyrs of 1900).
- **Era:** 8 and 9.
- **Evidence:** none opened this run. Studies wanted: Eric Widmer, *The Russian Ecclesiastical
  Mission in Peking during the Eighteenth Century* (Harvard 1976) [S]. Searched archive.org; not
  found.
- **Overlap:** VII.21 and VIII.31 (Russian church; they name Siberia, Alaska and Japan, not China);
  VIII.45 names Nikolai's Japan mission.
- **Recommendation:** hold for sources; named line in VIII.31 once a source is opened.
- **Gate question:** (a) named line in VII.21/VIII.31; (b) hold. **Recommended:** (b).

##### G89-AP12 — Christianity in colonial Australia and New Zealand, 1788–1906

- **Kind:** church bodies (the Anglican establishment from the First Fleet chaplaincy; Irish
  Catholicism and its hierarchy; Presbyterians and Methodists; missions to Aboriginal people and to
  Māori).
- **Era:** 9 (1788–1906, with era 8 roots).
- **Evidence:** Ian Breward, *A History of the Churches in Australasia* (OUP, 2001) — archive.org
  `historyofchurche0000brew` — **V-s**. T. L. Suttor, *Hierarchy and Democracy in Australia,
  1788–1870: The Formation of Australian Catholicism* (Melbourne UP, 1965) — archive.org
  `hierarchydemocra0000unse` — **V-s**. No primary opened.
- **B3:** Mid. Most of it is transplanted British and Irish church life (VIII.30, VIII.29, VIII.34
  carry the parents). The distinct pieces are Aboriginal missions, the Catholic school system, and
  Māori Christianity, which is a separate candidate (AP13).
- **Overlap:** VIII.41 (Old Lutherans to South Australia, 1838); VIII.30, VIII.29, VIII.34 (parent
  churches).
- **Recommendation:** hold for sources; then named lines in the parent rows rather than a new row.
- **Gate question:** (a) named lines in VIII.29/VIII.30/VIII.34; (b) an Australasia row; (c) hold.
  **Recommended:** (c), then (a).

##### G89-AP13 — Māori Christianity and the prophetic movements: Pai Mārire and Ringatū, 1862–1906

- **Kind:** cross-church movements (Māori prophetic churches arising from mission Christianity).
- **Era:** 9.
- **Four marks:** beginning — Te Ua Haumēne's Pai Mārire, 1862 [S]; Te Kooti's Ringatū, 1868 [S];
  carriers — Taranaki and East Coast iwi; Te Ua's "prophets" (Cowan names Patara Raukatauri sent
  by Te Ua "to preach ... the Pai-marire among the East Coast tribes", V); name — Pai Mārire,
  Ringatū [S for Ringatū]; recognition — Clark, *"Hauhau": The Pai Marire Search for Maori Identity*
  (Auckland UP, 1975), V-s; Binney on Te Kooti — not found on archive.org, [S].
- **Section A:** Not assessable; likely beyond the floor (as IX.26's Rātana is handled) [S].
- **Evidence:** James Cowan, *The New Zealand Wars*, vol. 1 (Wellington, 1922) — archive.org
  `newzealandwarshi01cowa`, lines 11845–11905 — *pre-1930 settler history, hostile ("fanatic
  gospel")* — **V** for the passage. Clark 1975 — **V-s**. Māori-language texts (Te Ua's *Ua Rongopai*;
  Ringatū's *Pukapuka*) — **wanted**.
- **Living today:** Ringatū Church [S]; no dated item.
- **Overlap:** IX.26 (Rātana and Pacific adjustment movements, from 1925) — none before 1906.
- **Recommendation:** hold for sources (a Māori-language or Māori-authored source first).
- **Gate question:** (a) an era 9 movement row (beyond-floor register); (b) a named line in IX.26,
  which starts in 1925, so the line would sit before its own row's dates;
  (c) hold. **Recommended:** (c), with (a) as the target.

##### G89-AP14 — The Pacific Christian kingdoms: Tahiti, Hawai'i, Tonga, Fiji, Samoa, 1797–1906

- **Kind:** church bodies (LMS, Wesleyan and ABCFM churches that became national churches under
  converted chiefs; the Free Church of Tonga, 1885 [S]).
- **Era:** 9.
- **Evidence:** none opened this run beyond the roster's own (VIII.7's voices name Ta'unga and
  Joeli Bulu). Ellis, *Polynesian Researches* (1829–31) located on archive.org; the volume opened
  (vol. 1, 2nd ed.) does not carry the conversions — **[S]**.
- **Overlap:** **Carried** by VIII.7, whose name includes "Pacific Islands" and whose text tells the
  Polynesian teachers' island-to-island work.
- **Recommendation:** carried by VIII.7. Ask only whether the Pacific wing should become its own row.
- **Gate question:** (a) leave in VIII.7; (b) split a Pacific row out of VIII.7 (a change order on
  a frozen row). **Recommended:** (a) for this sweep.

##### G89-AP15 — Korea, 1884/1886–1906: the Protestant beginnings and the Catholic years after toleration

- **Kind:** church bodies (Korean Protestant congregations; the Korean Catholic Church after 1886).
- **Era:** 9.
- **Evidence:** none opened this run. VIII.21's text says "Protestant missionaries came to Korea a
  hundred years after it began, from 1884"; IX.64 opens at 1907 and IX.2 at 1904.
- **Overlap:** VIII.21 (to 1886), IX.2 (1904–10), IX.64 (from 1907). The gap is 1886–1906 for
  Catholics and 1884–1906 for Protestants (the Ross translation, the Nevius plan, the first
  congregations) [S].
- **Recommendation:** named lines (Catholic: end of VIII.21's story; Protestant: a line in VIII.7),
  hold for sources.
- **Gate question:** (a) named lines; (b) hold. **Recommended:** (b), then (a).

##### G89-AP-X1 — Cross-region question: does the Society of Jesus need an era 8 continuation?

> **Merge note (rivers pass).** Answered by RV-1, one Society of Jesus row, 1650-1814; the China church stays its own row (AP2), the one home of the Rites (rivers §1a). See G89-1.

- **Why it is asked here:** the China break was logged as "tied to the Jesuits". VI.11 ends at 1650;
  VII.19 tells the 1759–73 expulsions and the 1814 restoration as a European story.
- **What the Asia pass found:** in Asia the Jesuits after 1650 are carriers inside stories whose
  subject is a local church: the Beijing court (AP2), the Vietnamese communities and their
  "ex-Jesuit" party after 1773 (AP4, Dutton 2017, V), the Madurai and Malabar-rites missions in
  Tamil India [S], and the Carmelite-Jesuit rivalry over the St Thomas Christians (AP1, App. E, V:
  "these two religious orders oppressed our forefathers"). None of these needs a Jesuit row to be
  told.
- **Recommendation:** no Jesuit continuation row from this region. If the Latin America pass makes
  the case for one (the Paraguay reductions), Mark rules it once for all regions at the merge.
- **Gate question:** (a) no era 8 Jesuit row; the order appears as named lines in the local rows
  and VII.19; (b) an era 8 Jesuit row, 1650–1814, worldwide; (c) decide at the merge.
  **Recommended:** (c), leaning (a) on the Asian evidence.

##### G89-AP-X2 — Cross-region question: a Missions Étrangères de Paris / Propaganda row?

- **Four marks (as a Catholic society, not a movement outside church bodies):** beginning — 13 May
  1658, Propaganda names Pallu and Lambert de la Motte vicars apostolic for "les Missions de Chine
  et les pays voisins" (V, Launay 1894, I, lines 3407–3415); carriers — secular priests of the Paris
  seminary and the vicars apostolic; name — Société des Missions-Étrangères; recognition — Launay
  1894 (V; an in-house history, pre-1930). A modern study was not verified.
- **Mark's test:** like the Jesuits, it is one body moving across many countries (Siam, Tonkin,
  Cochinchina, Sichuan, Korea, Japan). It is "tied to other movements" in exactly the way he warned
  about: it is the carrier, not the subject, of AP2, AP4, VIII.21 and VIII.45.
- **Recommendation:** out of scope as a row; name it as a carrier line in AP2 and AP4 (and VIII.21,
  VIII.45 already name its priests' work implicitly [S]).
- **Gate question:** (a) carrier lines only; (b) its own era 8–9 row. **Recommended:** (a).

##### Checked and out of scope, or carried

- **Armenian merchant churches in India and Southeast Asia** (Madras, Calcutta, Dhaka, Singapore):
  VI.28 says the New Julfa network "seeded Armenian communities and churches from India to the
  Mediterranean"; Seth, *History of the Armenians in India* (1897), is vendored and mapped to
  VI.28, VII.24 and VIII.32. Carried in outline; a named line is the Middle East pass's call.
- **Taiping:** carried by VIII.44.
- **Philippine Catholicism and the Aglipayan church:** carried by VII.29 and VIII.39.
- **Japan 1865–1906 (Catholic re-emergence, Protestant bands, Nikolai's Orthodox mission):**
  carried by VIII.45 (and VIII.31 names the Japan mission).
- **Batak and Javanese churches 1861–1906:** carried by VIII.26.
- **Mar Thoma reform, Malankara church, Khasi-Mizo-Naga revivals:** carried by VIII.27.
- **Protestant China coast, the CIM, Pastor Xi; Serampore; Pacific teachers:** carried by VIII.7.
- **Dalit mass movements (1870s on):** era 10 sweep GS-A3 dated their documented phase to era 10;
  their era 9 roots are not separately sourced here [S]. Left to the era 10 decision.
- **The Boxer year (1900):** belongs inside AP2's era 9 half (Catholic) and VIII.7 (CIM); no row of
  its own.

---

## 6. Middle East, Caucasus, Russia and Eastern Europe

The pass's `candidates.md`, as written, with its headings demoted two levels. Changes: British to American spelling in the pass's own prose, and a merge note at the head of each candidate the rivers pass gave a new home.

### Eras 8 and 9 global completeness sweep (P2-G89): the Middle East, Caucasus, Russia and Eastern Europe, 1650-1906

Scratch research for Mark's gate. Not census copy. Branch `claude/p2-g89-sweep`, read only. Census read: `cic-website/data/world-census.json` (322 movements; era 8 = atlas VII.x, 1650-1815; era 9 = atlas VIII.x, 1815-1906). No metered model calls. Eras 8 and 9 are frozen, so every addition below is a change order.

**Verification states.**
- **V** = I opened the item in this run (a Library file in `cic/texts/`, or a public-domain edition fetched raw with curl) and read the detail there. Where the item is a study (for example a 1908-1912 Catholic Encyclopedia article), "V" means the study says it; the study's own stance is named.
- **V-s** = the detail rests only on a study's report of an item I did not open.
- **[S]** = snippet, summary, memory or unopened. Never verified.
- Only V carries a sentence.

**The Catholic Encyclopedia (1907-1912).** Several items below are its articles, read raw from the New Advent transcription (newadvent.org/cathen/). They are public-domain studies inside or near the era, by named scholars (Jérôme Labourt on the Syriac churches, Siméon Vailhé, Cyril Charon and others). They write from a Catholic standpoint and call the non-Catholic churches "schismatic" or "heretical". They are usable as dated studies, not as neutral ones, and each candidate still wants a study from or of the region.

**Non-English sources used.** Arabic (Duwayhī, OCR locator only), Russian and Church Slavonic (Subbotin, Denisov, Barskov, Paisius), French (Charon 1911, Brosset, Labourt), Latin (Assemani), Bulgarian (Paisii Hilendarski). Georgian, Syriac and Armenian originals were not opened in this run; the Georgian and Syriac items are French, Latin or English studies.

---

#### 1. River by river

| River | Roster has (region, 1650-1906) | Gap | Candidate |
|---|---|---|---|
| **Orthodox — Russian** | VII.21 (to 1815), VIII.31 (1815-1906), VII.8, VIII.11, VIII.47 (Alaska) | Missions inside the empire (Siberia, Volga) unnamed | ME-18 named lines in VII.21 / VIII.31 |
| **Orthodox — Old Believers** | VII.7 (1666-1815) | **Break after 1815** (Belokrinitsa 1846, 1905) | **ME-5** era 9 row |
| **Orthodox — Ottoman, Greek, Balkan** | VII.18, VII.8, VIII.12, VIII.28 | Paisii's Bulgarian revival, Karlovci, Montenegro, Sibiu unnamed | ME-13, ME-17 named lines |
| **Orthodox — Antiochian (Arab)** | VII.23's Orthodox side (to 1815), via VII.18 | Nothing after 1815; the Arab patriarch | **ME-4** (with the Melkite Catholics) |
| **Orthodox — Georgian** | IV.15 (to 1245), IX.40 (from 1917) | **Break 1245-1917**; 1650-1811 and the Exarchate in this window | **ME-3** era 8 row + named line in VIII.31 |
| **Oriental Orthodox — Armenian** | VII.24a, VII.24, VIII.32 | Etchmiadzin under Russia (1836); the 1870 Catholic schism | ME-14, ME-15 named lines in VIII.32 |
| **Oriental Orthodox — Syriac** | none after IV.21 (1300) until IX.19 (1915) | **Held break**; 1650-1906 in this window | **ME-7** hold, then era 9 row |
| **Church of the East** | VI.30 (to 1650), VIII.40 (1815-1906) | **Break 1650-1815** | **ME-1** era 8 row |
| **Eastern Catholic — Maronite** | IV.10, V.22 (to 1517) | **Break 1517-1900** | **ME-2** era 8 and era 9 rows |
| **Eastern Catholic — Melkite** | VII.23 (1724-1815) | Nothing after 1815; 1650-1724 held | **ME-4** era 9 row; named line in VII.23 |
| **Eastern Catholic — Chaldean** | VIII.40 (1830 consolidation) | the Josephite line 1681-1830 | in **ME-1** |
| **Eastern Catholic — Syriac Catholic** | none | 1781 split, 1830 millet | in **ME-7** |
| **Eastern Catholic — Armenian Catholic** | VII.24 (1742, Bzommar), VIII.32 (mention) | 1867-1870 schism | ME-15 |
| **Eastern Catholic — Ruthenian** | VI.20, VII.28, VIII.38 | Carpathian union (Uzhhorod 1646, Mukachevo) unnamed | named line in VII.28 / VIII.38 (in ME-8) |
| **Eastern Catholic — Romanian** | IX.73 (from 1948) only | **No parent**: 1698 union to 1906 | **ME-8** era 8 row (+ era 9) |
| **Catholic — Latin, Poland and Lithuania** | VI.22, VII.19, VIII.29 (Rome-centered); IX.70 (from 1918) | **No row** for the partition-era church; IX.70 has no parent | **ME-10** era 9 row |
| **Catholic — missions in the Ottoman lands** | none as a movement | Capuchins, Jesuits, Propaganda brokered most unions | not a row; told inside each church (see notes) |
| **Catholic — Jerusalem** | IV.25 (to 1291) | Latin Patriarchate 1847; Holy Places | ME-16 gate note |
| **Jesuits** | VI.11 (to 1650), VII.19 (suppression, restoration) | Russian survival 1773-1814 | **ME-12**: named line in a Jesuit home (Mark's test) |
| **Protestant — Hungarian and Transylvanian** | VI.14 (Unitarians, to 1650) | **No row** for the Reformed and Lutherans | **ME-9** era 8 row (+ era 9) |
| **Protestant — Russian evangelical** | VIII.51 (1860-1906) | none | — |
| **Protestant — Middle East missions** | VIII.32 (Armenian Evangelicals), VIII.40 (Urmia) | **Arab Evangelicals** of Syria and Lebanon | **ME-11** wing in VIII.7 |
| **Protestant — Anabaptist in Russia** | none after VI.3 | Mennonites, Hutterites | ME-22 → rivers pass |
| **Independent / dissenting (Russia)** | none | Dukhobors, Molokans, Khlysty, Skoptsy; Tolstoyans | **ME-6** (Section A open); ME-20 out under A1 |
| **Jewish-Christian** | IX.13 (from 1960) | Rabinowitz, Kishinev 1884 | ME-21 hold |

---

#### 2. Candidates (sections in the order assessed; the ranking is in §3)

##### ME-1. The Church of the East: three patriarchates, from Diyarbakır to the Chaldean union (1650-1815)

- **Answers the logged break:** Church of the East, 1650-1815 (Open-Gaps 142).
- **Kind:** church body (the communion and its rival lines). **Era:** 8.
- **Dates:** 1650-1815 (the story's own markers: Joseph of Diyarbakır's break, 1672; his patriarchate, 1681; Yohannan Hormizd's profession, 1778).
- **Region / countries:** Middle East; Turkey (Diyarbakır, Hakkari), Iraq (Mosul, Alqosh), Iran (Urmia). **Lane:** 1 Syriac East & Asia.
- **What it carries that no row does:** the three lines between VI.30 and VIII.40. The Eliya line of Alqosh and Mosul, recognized by the Porte. The Shemʿon line in the Hakkari mountains (Qudshanis), outside Ottoman control. The Catholic "Josephite" line at Diyarbakır (Amid), founded with Capuchin help and Rome's sanction, five patriarchs named Joseph. And the end of the old Alqosh line, when Mar Eliya's nephew Hormizd (Yohannan Hormizd) took Rome's faith on 30 April 1778, the day after his uncle died of plague.
- **Section A:** No floor question. The Church of the East confesses the Nicene Creed (the same body assessed at II.3, V.17, VI.30). Dated own statement inside the era: Mutran Hanna (Yohannan Hormizd)'s autobiography, from his Syriac manuscript, in Badger's translation (V; see below). A3: none.
- **B1 Sourcing:** Moderate to strong. An in-era own voice (the Hormizd autobiography, as translated), an in-era Roman catalog (Assemani 1725-1728), a near-era outside witness who met the patriarchs (Badger 1852), and a 1908 study (Labourt). The asymmetry is marked: the Roman and Anglican sides wrote most of what survives; the mountain line's own records are thin.
- **B2 Ecology:** Moderate. Patriarchal family, mountain tribes and emirs, Ottoman firmans, Capuchin and Dominican missions, monastery (Rabban Hormizd), village plague. Ordinary believers are visible only through outsiders.
- **B3 Uniqueness:** High. The Syriac East river's only break. No other row holds the Josephite line or the 1778 change.
- **B4 User needs:** history learners, academically minded users, Assyrian and Chaldean inquirers; pastors interested in church unity.
- **B5 Scale:** small; tiebreak only.
- **Tier:** 2 (clear on Section A and sourcing; ecology moderate).
- **Evidence:**
  1. George Percy Badger, *The Nestorians and their Rituals*, vol. 1 (London, 1852), `cic/texts/badger_nestorians-and-their-rituals-v1_1852.txt`, file lines ~7940-8060 — **V**. "Pope Innocent XI. proceeded to effect a new schism : which he did by appointing Yoosef, the first of that name, as Patriarch of the Chaldeans at Diarbekir, a.d. 1681." The Mosul and Alqosh patriarchs "were recognized by the Sublime Porte", while the mountain patriarchs "were not thus recognized by the Turkish government". Hormizd's autobiography (as translated): "I Hormuzd, son of deacon Hanna, the brother of Mar Elia the Patriarch of the East, was born a.d. 1760"; his uncle died in the plague at Alkosh "on the 29th of April" 1778, and "on the 30th of April I embraced all that the holy Church believes". Badger is an Anglican missionary and hostile to Rome; his framing ("schism", "machinations") is his own.
  2. Jérôme Labourt, "Chaldean Christians", *Catholic Encyclopedia* vol. 3 (1908), newadvent.org/cathen/03559a.htm — **V** (study). "In 1672, Joseph, the Nestorian Archbishop of Diarbekir, following the advice of the Capuchin missionaries, withdrew from communion with the Patriarch Elias IV." "Innocent XI granted him the pallium (1681) and the title of patriarch." Lists Joseph II-V to 1826, and "Owing to the scarcity of documents the history of this period is little known." Then John Hormizd "reconciled with Rome in 1830".
  3. Giuseppe Simone Assemani, *Bibliotheca orientalis* III.1 and III.2 (Rome, 1725 and 1728), in the Library — **[S]** for this period: not searched in this run for the Josephite or Eliya lines. An in-era Roman source; Latin; OCR long-s.
  4. George David Malech, *History of the Syrian Nation and the Old Evangelical-Apostolic Church of the East* (Minneapolis, 1910), `cic/texts/malech_history-of-the-syrian-nation-and-old-evangelical-apostolic-church-of-the-east_1910.txt`, ch. XXXII, file lines ~16775-16810 — **V**. A Church of the East author from Urmia (born 1837), so a voice from inside the tradition. He gives the patriarch lists of both lines for "the seventeenth-nineteenth century", and: "Denkah Shimon XV transferred (removed) the patriarchal residence from the village of Raban Dadishu to Kudchanis, in the Turkish territory where it has been for more than 200 years". The OCR garbles some regnal numbers and dates; use the lists as a locator, not for exact years.
  5. W. A. Wigram, *The Assyrians and their Neighbours* (1929), in the Library — **[S]** (not read here).
- **Living:** yes, as the bodies it divides into (the Chaldean Catholic Church, the Assyrian Church of the East). IX.19's text names both in 1994 (a 1994 date is in-era 10; no dated item after 2010 read here). Grade: none read; CR at best until a dated item is opened.
- **Mark's test (unique, or part of another movement?):** It is its own story. The Capuchin, Dominican and Propaganda work that produced the Josephite line is the same Roman policy seen in the other unions (VI.20, VII.23, VII.24), but no row tells that policy as a movement, and the Church of the East's own division (begun at VI.30) is the frame. It is the middle of one story that runs VI.30 → [gap] → VIII.40, not a piece of a Jesuit or mission row.
- **Overlap:** VI.30 (to 1650; two patriarchates from 1552). VIII.40 (from 1815; the 1830 consolidation and Qudshanis). IX.19 (from 1915). The new row carries only 1650-1815, and names the other three.
- **Recommendation:** **enter** (an era 8 church row), unless Mark prefers the date-change route below.
- **Gate question G-ME1.** How should the Church of the East's 1650-1815 years enter?
  - (a) A new era 8 row, 1650-1815, between VI.30 and VIII.40, with "continued as" links on both sides. **Recommended**: it keeps each row inside its era, and the Josephite line has its own beginning (1672/1681) and end (1830).
  - (b) Extend VIII.40 back to 1672 or 1681, so it opens with the Josephite line. Simpler, but VIII.40 would cross the era line, and its 1650-1672 years stay empty.
  - (c) Hold for sources until Assemani III and Malech are read for these years.

##### ME-2. The Maronite Church: from Duwayhī and the Synod of Mount Lebanon to the Mutasarrifate (1650-1906)

- **Answers the logged break:** Maronite church, 1517-1900 (Open-Gaps 142). This pass covers 1650-1906. The years 1517-1650 (the Maronite College in Rome, 1584; the councils of 1596 and 1616) fall in era 7 and are flagged for that era's owner (see the gate question).
- **Kind:** church body (an Eastern Catholic church). **Era:** 8 and 9 (two rows, or one row per era).
- **Dates:** 1650-1815 (era 8) and 1815-1906 (era 9).
- **Region / countries:** Middle East; Lebanon (Qannubin, Bkerke, Kisrawan), with Aleppo and Cyprus. **Lane:** 1 Syriac East & Asia (the lane of IV.10 and V.22).
- **What it carries that no row does:**
  - Era 8: Patriarch Isṭifān al-Duwayhī (died 1704), who wrote the church's own history of its patriarchs; the monastic congregations approved in 1732, 1740 and 1770; the national council of 1736, led by Rome's delegate Joseph Simeon Assemani, which brought the Council of Trent into the Lebanon; the Hindiyya affair (her convent and its condemnation, the patriarch put under interdict in 1779).
  - Era 9: the Druze-Maronite wars from 1841 and 1845, the massacres of 1860, the French intervention and the single governor of the Lebanon from 1861; Patriarch Būlus Masʿad (1855-1890); Elias Hoayek (elected 1899).
- **Section A:** No floor question. The Maronites confess the Nicene Creed and are in communion with Rome (assessed at IV.10, V.22). Dated own statement in the era: Duwayhī's *Tārīkh al-ṭāʾifa al-mārūniyya* (Library; OCR damaged, locator only). The 1736 council's acts (Mansi) were not opened. A3: none.
- **B1 Sourcing:** Moderate now, strong once the 1736 acts and a clean Duwayhī are vendored. In-era outside witnesses (Volney 1788; Churchill 1862), a 1910 study (Labourt), and the church's own historian (Duwayhī, locator only).
- **B2 Ecology:** Strong: patriarch and monasteries, shaykhs and emirs, peasants and silk, Rome and its delegates, the Jesuit and Lazarist schools, the French protectorate, a woman visionary and her convent, war and massacre.
- **B3 Uniqueness:** High. Four centuries with no entry; the one Eastern church that holds it never left communion with Rome.
- **B4 User needs:** history learners, Catholics, Lebanese and diaspora inquirers, academically minded users.
- **B5 Scale:** moderate.
- **Tier:** 1 for the era 9 row (the 1860 crisis is a regional turning point and well documented); 2 for the era 8 row until the 1736 acts are opened.
- **Evidence:**
  1. Jérôme Labourt, "Maronites", *Catholic Encyclopedia* vol. 9 (1910), newadvent.org/cathen/09683c.htm — **V** (study). "Stephen of Ehdem (d. 1704) composed a history of his predecessors from 1095 to 1699." "Under Joseph IV (1733-42) was held a second national council, which is of highest importance. Pope Clement XII delegated Joseph Simeon Assemani ... with an express mandate to cause the Council of Trent to be promulgated in the Lebanon." The Antonian congregation "was approved in 1732", the division into Aleppines and Baladites "approved by Clement XIV in 1770", the Isaian congregation "approved in 1740". "In 1860 the Druses ... massacred a large number of Maronites at Damascus and in the Lebanon." "In 1861 the present system, with a single governor for all the Lebanon, was inaugurated." Patriarchs to "Mgr. Elias Hoysk, elected in 1899". Also: "All competent authorities agree as to the history of the Maronites as far back as the sixteenth century, but beyond that period the unanimity ceases."
  2. C.-F. Volney, *Travels through Syria and Egypt*, vol. 2 (London, 1788), `cic/texts/volney_travels-through-syria-and-egypt-v2_1788.txt`, chapter "Of the Maronites" — **V**. An in-era Enlightenment witness, openly hostile to monks. "In religious matters, the Maronites are dependent on Rome. Though they acknowledge the supremacy of the Pope, their clergy continue, as heretofore, to elect a head, with the title of Batrak, or patriarch of Antioch." (Long s modernized.) He tells the Hindiyya story at length ("Hendia"; the convent "called the Kourket").
  3. Charles Henry Churchill, *The Druzes and the Maronites under the Turkish Rule from 1840 to 1860* (London, 1862), archive.org item druzesmaronitesu00churuoft, raw djvu text opened — **V** (title, date, contents: "An Affray at Deir-el-Kamar, 1841"; "June 3, 1860, appalling Slaughter of the Males at Hasbeya"). A British officer sympathetic to the Druzes; partisan.
  4. Isṭifān al-Duwayhī, *Tārīkh al-ṭāʾifa al-mārūniyya*, ed. Rashīd al-Shartūnī (Beirut, 1890), `cic/texts/duwayhi_tarikh-al-ta-ifa-al-maruniyya-ara_shartuni1890.txt` — **V** as a held file; its OCR is "heavily damaged ... Treat as a locator only" (registry). No sentence can rest on it.
  5. The acts of the Synod of Mount Lebanon (1736), in Mansi vol. 38 (per Labourt) — **[S]**, wanted. archive.org title searches for "synodus libanensis" found nothing in this run.
- **Living:** yes (the Maronite Church). No era 10 row carries the Maronites: the era 10 sweep proposed E6 (the Maronite Church, 1920-c. 2010), and it is not on the roster. No dated item after 2010 read here.
- **Mark's test:** Unique. Rome is part of this church's story (the College, the 1736 council, Propaganda), as it is for every Eastern Catholic church, but the Maronites' union predates Propaganda (IV.10, V.22). Their story is not a piece of a Jesuit or mission movement. It is the same church as IV.10 and V.22, carried on.
- **Overlap:** IV.10, V.22 (to 1517); VII.23 names the Maronites only as an earlier union. VIII.29 (the Catholic world) does not name them. No era 10 row.
- **Recommendation:** **enter** the era 9 row (1815-1906). **Enter** the era 8 row (1650-1815) once the 1736 acts are opened; until then, hold it for one source.
- **Gate question G-ME2.** How should the Maronite church's missing centuries enter?
  - (a) One row per era: era 8 (1650-1815) and era 9 (1815-1906), with the era 7 years (1517-1650) sent to the era 7 owner as a separate change order. **Recommended**: each era's row stays inside its era, as the Armenian and Russian rows do.
  - (b) One long row, 1517-1900, across three eras. Fewer rows, but it breaks the era pattern every other church follows.
  - (c) The era 9 row now; era 8 and era 7 held for sources (the 1736 acts, a clean Duwayhī).

##### ME-3. The Georgian Church: between Persia, the Ottomans and Russia, to the end of the catholicate (1650-1811), and the Exarchate (1811-1906)

- **Answers the logged break:** Georgian church, none after 1245 (Open-Gaps 142). This pass covers 1650-1906. The years 1245-1650 (eras 6 and 7) fall outside it and are flagged.
- **Kind:** church body. **Era:** 8 (1650-1811), with the era 9 Exarchate as a second piece.
- **Dates:** 1650-1811; 1811-1906 (the Exarchate runs on to the 1917 restoration told in IX.40).
- **Region / countries:** Caucasus; Georgia (Mtskheta, Tbilisi, Imereti, Kakheti). **Lane:** 2 Caucasus.
- **What it carries that no row does:** the Georgian church under Safavid and Ottoman pressure; Capuchin and Theatine missions in Tbilisi and Akhaltsikhe; Catholicos Antoni I, made to leave Georgia in 1755 when the king suspected him of leaning to Rome, cleared by the Russian Synod, and later restored; the catholicos given a seat in the Russian Holy Synod; the sack of Tbilisi by the Persians in 1795; and the end of the catholicate in 1811, when the church became an exarchate of the Russian Synod.
- **Section A:** No floor question (Orthodox; the Creed; assessed at II.10, IV.15, IX.40). Dated own statement in the era: Antoni I's confession of faith submitted to the Russian Synod (V-s, from Ioseliani; not opened). A3: none.
- **B1 Sourcing:** Moderate. A Georgian historian's church history (Ioseliani, Tiflis, in Malan's 1866 English), a 1912 English sketch (Dowling), Brosset's French editions of the Georgian chronicles (Library holds part 1 only; the modern volumes of 1856-1858 are on archive.org). No Georgian-language original was opened.
- **B2 Ecology:** Moderate: kings and catholicoi, Persian and Ottoman overlords, Catholic missionaries, Athonite and Jerusalem houses, writers such as Sulkhan-Saba Orbeliani (named in Ioseliani's contents), and the Russian Synod.
- **B3 Uniqueness:** High. Nothing after 1245 until IX.40 (1917). IX.40 says only that autocephaly was "abolished in 1811".
- **B4 User needs:** history learners, Orthodox inquirers, Georgian users, academically minded users.
- **B5 Scale:** small to moderate.
- **Tier:** 2.
- **Evidence:**
  1. P. Ioseliani, *A Short History of the Georgian Church*, translated from the Russian by S. C. Malan (London, 1866), archive.org item MalanGeorgianChurch, raw djvu text opened — **V**. Ioseliani was a Georgian scholar ("published in Georgian by P. Ioselian at Tiflis in 1852", translator's note). Contents of ch. XI-XII: "Efforts of Western missionaries in Georgia, and banishment of the Catholicos Antoni I. into Russia"; "The Catholicos of Georgia becomes, ex officio, member of the Holy Synod of all the Russias"; "Sack of Tiflis by the Persians in 1795". Text: "Antoni left Georgia in 1755, placing himself under the protection of the Holy Synod of all the Russias, and submitted to the inquiry thereof his confession of faith". The catholicos's title "continued attached to that dignity and in Georgia until the year 1811". On the Exarchate: the head of the clergy took "the title of 'Member of the Synod, and Exarch of Georgia'"; "On the 30th of August, 1814, the exarchate of Imereth was given by the Emperor, to the Georgian exarch Balaam"; "In December 1818 ... one exarchy alone was established". (The OCR prints the end of the catholicate as "1711" at one point and "1811" at another; 1811 agrees with IX.40 and with the text's own list "from 1811".) Ioseliani writes from inside the Russian synodal church and calls the Catholic missionaries' work "perverting".
  2. Dowling, *Sketches of Georgian Church History* (1912), archive.org item DowlingGeorgianChurchHist, raw text fetched — **[S]** for content (fetched, not read here).
  3. M.-F. Brosset, *Histoire de la Géorgie*, part 1 (St Petersburg, 1849), `cic/texts/brosset_histoire-de-la-georgie-pt1-fra_1849.txt` — **[S]** for this period (part 1 is the ancient history; the modern volumes, archive.org items such as histoiredelagor00fgoog, 1858, were not opened).
- **Living:** yes (the Georgian Orthodox Church, IX.40).
- **Mark's test:** Unique. The Exarchate years (1811-1917) are tied to the Russian church (VIII.31), but VIII.31 never names Georgia, and the Georgian church kept its own language, saints and memory, which is why it restored itself in 1917 (IX.40). The 1650-1811 years belong to no other movement.
- **Overlap:** II.10, III.20, IV.15 (to 1245); IX.40 (from 1917). VII.24a and VIII.32 are Armenian. VIII.31 is the Russian church.
- **Recommendation:** **enter** an era 8 row (1650-1811); put the Exarchate (1811-1917) as a **named line in VIII.31**, with a link to IX.40.
- **Gate question G-ME3.** How should Georgia's church re-enter the tree before 1917?
  - (a) An era 8 row, 1650-1811, and the Exarchate as a named line in VIII.31 with a "continued as" link to IX.40. **Recommended**: it closes the era 8 break on a Georgian historian's account, and tells the Exarchate where its government sat.
  - (b) An era 8 row and an era 9 row (the Exarchate, 1811-1906). Fuller, but the era 9 row has thin sources until Dowling and Brosset's modern volumes are read.
  - (c) Hold both until a Georgian-language source is vendored, and send 1245-1650 to the era 6 and 7 owners.

##### ME-4. The two Melkite churches in the nineteenth century: Catholic emancipation and the Arab Orthodox patriarchate (1815-1906); and the Melkite held gap (1009-1724)

- **Answers the logged break:** Melkites, 1009-1724, held for sources (Open-Gaps 135 and 142). Inside this pass's window that gap is only 1650-1724. The pass also found a second break: neither Melkite church has any entry after VII.23 ends in 1815.
- **Kind:** church bodies (the Melkite Greek Catholic Church; the Greek Orthodox Patriarchate of Antioch). **Era:** 9 (the row); 8 (the 1650-1724 named line).
- **Dates:** 1815-1906.
- **Region / countries:** Middle East; Syria (Damascus, Aleppo), Lebanon (Shuwayr, ʿAyn Trāz), with Egypt and Palestine for Maximos III's titles. **Lane:** 3<->5 bridge (Greek East / Latin West), as VII.23; the Orthodox side is lane 3.
- **What it carries that no row does:** Maximos III Mazlūm (patriarch 1833-1855), the synod of ʿAyn Trāz (1835), the berat of 7 January 1848 that freed the Catholic Melkites from the Orthodox and Armenian civil tutelage, the Jerusalem council of 1849, Gregory II Yūsuf (1865-1897) at the First Vatican Council [S for Vatican I]; and on the Orthodox side, the end of Greek control at Antioch, with an Arab patriarch recognized "after a schism with Constantinople" (Fortescue; the first Arab patriarch, Meletios Doumani, 1899, is [S]).
- **For 1650-1724:** Patriarch Macarius III and his son Paul of Aleppo's journey to Moscow and Kyiv in the 1650s; Euthymius of Tyre and Sidon and the union-leaning bishops before 1724.
- **Section A:** No floor question. Both churches confess the Nicene Creed (assessed at III.2, VII.23). Dated own statements: the 1848 berat in Charon's French (V); Paul of Aleppo's journal (V, Library).
- **B1 Sourcing:** Strong for the Catholic side (Charon, a near-contemporary study built on the documents; Fortescue 1911). Thin for the Orthodox side (Fortescue only, a hostile Catholic witness; no Orthodox source opened).
- **B2 Ecology:** Strong: patriarchs and synods, Basilian monks of Shuwayr and Saint Saviour, Aleppo merchants, seminaries, the Porte, France and Russia, the Arabic press.
- **B3 Uniqueness:** High. Both Melkite churches vanish from the tree between 1815 and the present.
- **B4 User needs:** history learners, Eastern Christian inquirers, Arab Christian users, academically minded users.
- **B5 Scale:** moderate.
- **Tier:** 1 for the Catholic side; 2 if the Orthodox side is included before an Orthodox source is read.
- **Evidence:**
  1. Cyrille Charon (Korolevskij), *Histoire des patriarcats melkites*, t. II-III (Rome, 1910-1911), `cic/texts/charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt`, file lines ~352-358, ~10360-10370 — **V**. « Son nom est resté attaché à l'émancipation de la communauté unie à Rome de la tutelle civile des orthodoxes » ("His name remains tied to the emancipation of the community united to Rome from the civil tutelage of the Orthodox", my rendering). The new berat « est daté de la fin de moharram 1264 (7 janvier 1848) » and « consacre l'émancipation civile définitive des Melkites catholiques » ("is dated the end of Muharram 1264 (7 January 1848)"; "consecrates the definitive civil emancipation of the Catholic Melkites", my rendering). Charon was a Byzantine-rite Catholic priest of Lviv.
  2. Adrian Fortescue, "Melchites", *Catholic Encyclopedia* vol. 10 (1911), newadvent.org/cathen/10157b.htm — **V** (study). Euthymius of Tyre and Sidon and Athanasius IV "approached the Holy See"; in 1722 a Constantinople synod sent "a warning letter with a list of Latin heresies"; Mazlūm "in 1835 ... held a national synod at Ain-Traz"; "During his reign at last the Melchites obtained recognition as a separate millet from the Porte"; for the Orthodox side, "At Antioch they have now succeeded in the recognition of their native Patriarch, Gregory IV (Hadad) after a schism with Constantinople."
  3. Paul of Aleppo, *The Travels of Macarius, Patriarch of Antioch*, tr. F. C. Belfour, vol. 1 (London, 1836), `cic/texts/paul-of-aleppo_travels-of-macarius-v1_belfour1836.txt` — **V** (held; the registry describes the 1650s journey). Already mapped in the corpus to VII.18, VII.21, VI.21 and VII.23.
  4. Volney, *Travels*, vol. 2 (1788), Library — **V** (registry content note: the Melkite Basilian monastery at Shuwayr and its Arabic press). For VII.23's era, not this row.
- **Living:** yes (both churches). No dated item after 2010 read here.
- **Mark's test:** Unique. The 1724 split is VII.23's; this is what both churches did next. It is not part of a mission or Jesuit movement, though Propaganda appears in it (Tanas had studied there, per Fortescue).
- **Overlap:** III.2 (to 1009); VII.23 (1724-1815; its corpus map already lists Charon's 1833-1855 volume); VII.18 (the Ottoman Orthodox, which VII.23 says the Orthodox side stayed part of); VIII.28 (national churches; does not name Antioch).
- **Recommendation:** **enter** an era 9 row for both Melkite churches (1815-1906). Put **Macarius III and Euthymius as a named line in VII.23** for 1650-1724. Keep **1009-1650 held** for sources, as Open-Gaps 135 has it.
- **Gate question G-ME4.** How should the Melkites after 1815 enter?
  - (a) One era 9 row for both churches of the Antiochene see, Catholic and Orthodox, as VII.23 tells the split. **Recommended**: VII.23 already frames them as one community in two churches, and the Orthodox side is too thin for its own row.
  - (b) An era 9 Melkite Catholic row now; the Antiochian Orthodox side held until an Orthodox source (for example on the 1899 election) is opened.
  - (c) Extend VII.23 to 1906. It would cross the era line.

##### ME-5. The Old Believers in the nineteenth century: Nicholas I, the Belokrinitsa hierarchy and the toleration of 1905 (1815-1906)

- **Answers the logged break:** Old Believers after 1815, with the Belokrinitsa hierarchy of 1846 (Open-Gaps 135 and 142).
- **Kind:** church body (a family of communities: priestly Popovtsy, priestless Bezpopovtsy). **Era:** 9.
- **Dates:** 1815-1906.
- **Region / countries:** North Europe (the census tag for Russia, as VII.7); Russia, with Belaya Krinitsa in Austrian Bukovina (now Ukraine) and the Danube settlements (Romania). **Lane:** 3 Greek East & Orthodoxy (as VII.7).
- **What it carries that no row does:** the persecution under Nicholas I from 1827 (the Irgiz monasteries, the sealed altars of the Rogozhskoe cemetery in Moscow); the search for a bishop that ended when Ambrose, the deposed metropolitan of Sarajevo, came to Belaya Krinitsa on 12 October 1846; the priestless communities and their arguments over marriage; the decree of 17 April 1905 that gave the "Old Ritualists" legal standing, and the Popovtsy synod of 25 August 1905.
- **Section A:** No floor question. The Old Believers keep the Nicene Creed in its pre-Nikonian Slavonic text (assessed at VII.7). The priestless strands differ on sacraments, not on the Creed; under A5 the world is assessed as a whole.
- **B1 Sourcing:** Moderate to strong. A 1921 study by a careful scholar who read the Russian literature (Conybeare, in the Library), an in-era witness for the start of the period (Pinkerton's 1814 appendix), and the Old Believers' own earlier texts (Denisov, Filippov, Subbotin's documents) for continuity. No own-voice document of 1846 or 1905 was opened (wanted: the Belokrinitsa statute, the Okruzhnoe poslanie of 1862, the 1905 decree's text).
- **B2 Ecology:** Strong: merchant patrons in Moscow, peasant villages, monasteries, émigré settlements, priestless elders, state police, the Synod's missionaries.
- **B3 Uniqueness:** High. VII.7 ends at 1815. VIII.31 names Belokrinitsa only as "separate".
- **B4 User needs:** history learners, Orthodox inquirers, academically minded users; readers of Russian literature.
- **B5 Scale:** large (millions; Conybeare discusses the count).
- **Tier:** 1.
- **Evidence:**
  1. F. C. Conybeare, *Russian Dissenters* (Harvard Theological Studies X, 1921), `cic/texts/conybeare_russian-dissenters_1921.txt` — **V**. Ch. III, "The Persecution of the Raskol by Nicholas I": "These attempts began in 1827 with a threat on the part of Prince Golitsyn, Governor of Saratov, to break up the monastery of Nizhni-Voskresenski, unless they became Uniats." (OCR's "GoUtsyn" read as Golitsyn.) On Belokrinitsa: Ambrose "on April 10th, 1846, accepted the position", and "was at Bielo-Krinits on October 12th, 1846." On 1905: "an imperial Ukase of April 17, 1905, suppressed the offensive Raskol, and distinguished among Russian dissenters three categories: 1. of Old Ritualists ..." and "in a Synod held on August 25th of that year decreed that that day should be for ever feasted as a holy day in their Church." Conybeare draws on Ivanovski, a Synodal anti-Raskol writer, and says so ("if we can believe Ivanovski").
  2. Platon, *The Present State of the Greek Church in Russia*, tr. R. Pinkerton (Edinburgh, 1814), Library — **V**. Its appendix lists the Old Believer and other groups as known in 1814 (contents: "Of Bezpopoftschins ... Pomoryans ... Theodosians ... Philipoftschins").
  3. Andrei Denisov, *Pomorskie otvety* (*Поморские ответы*, "The Pomorian Answers", 1723; ed. 1911), Library — **V** (held; an era 8 own voice of the priestless, for continuity only).
  4. P. S. Smirnov, I. Ivanovskii and N. Subbotin's histories of the Austrian hierarchy (in Russian) — **[S]**, wanted. An archive.org search in this run found no scan.
- **Living:** yes (the Russian Orthodox Old-Rite Church of the Belokrinitsa line; priestless communities). No dated item after 2010 read here.
- **Mark's test:** Unique. It is VII.7's own story carried on; it is not part of VIII.31, which names it as separate.
- **Overlap:** VII.7 (to 1815; mentions 1846 in its relations line, so the change order must also check that line); VIII.31 (names Belokrinitsa); ME-6 (the spiritual Christians, a different family). Conybeare treats both in one book; the census should not.
- **Recommendation:** **enter** (era 9 church row).
- **Gate question G-ME5.** How should the Old Believers after 1815 enter?
  - (a) An era 9 row, 1815-1906, "continued as" from VII.7. **Recommended**: the sources in hand verify the three turning points (1827, 1846, 1905).
  - (b) Hold until a Russian own-voice text (the Belokrinitsa statute or the 1862 Okruzhnoe poslanie) is vendored, so the row can carry the Old Believers' own words.
  - (c) A named line in VIII.31. Not recommended: it would tell the Old Believers from inside the church they left.

##### ME-6. The spiritual Christians of Russia: Dukhobors, Molokans, and the mystic sects (c. 1760s-1906)

- **Answers no logged break.** A gap found by this pass.
- **Kind:** cross-church family of dissenting bodies, outside the Orthodox Church. Each (Dukhobors, Molokans) is a defined body with a name, carriers and a beginning. **Era:** 8 and 9 (one row in era 9, with era 8 roots; or one row per era).
- **Dates:** the name "Dukhobortsy" in 1788 (Pinkerton); settlement at Molochnye Vody, 1804; the move to Transcaucasia from 1841 [S]; the burning of arms, 1895 [S]; the Dukhobor migration to Canada, 1899 (archive.org title, 1899); to 1906.
- **Region / countries:** North Europe and the Caucasus; Russia, Ukraine (Tauria), Georgia and Armenia (Transcaucasia), with Canada after 1899. **Lane:** 8 Beyond the Floor (see Section A) or 6 Protestant & Evangelical for the Molokans.
- **Section A — a floor question.** The Dukhobors rejected the outward church, sacraments and icons; Pinkerton (1814) reports that "The Duhobortsi affirm that every external rite ..." (file line ~11037, not read in full). Whether their own confession affirms Christ's full divinity was not checked. The Molokans kept Scripture and rejected the rites; their confession (Conybeare's Part II, ch. II, "The Evidence of their Confession of Faith") was not read here. The Khlysty and Skoptsy (Conybeare, Part III) likely fall outside the floor. **Not yet assessable** for each body; it must be decided body by body under A1, A4 and A5.
- **B1 Sourcing:** Moderate. An in-era witness (Pinkerton 1814), a 1921 study (Conybeare), and the 1899 and 1903 Canadian and Quaker accounts on archive.org (titles only).
- **B2 Ecology:** Strong: village communes, psalm-singing ("living book"), exile, the Caucasus frontier, pacifism, the Canadian prairie.
- **B3 Uniqueness:** High. No row names any of them. The roster has only one Russian dissent outside Orthodoxy (VIII.51, the Stundists).
- **B4 User needs:** history learners, deconstructing Christians, pacifist and Anabaptist-minded users, academically minded users.
- **B5 Scale:** small to moderate.
- **Tier:** 2 (pending Section A).
- **Four marks (as a family):** a beginning (the 1760s-1780s; the name by 1788); carriers (Dukhobor and Molokan communes, their leaders); a name (spiritual Christians, *dukhovnye khristiane*, as a group label is [S]); recognition in a study (Conybeare 1921, Part II, "The Rationalist Sects of South Russia" — V). The family label is a scholar's grouping, so each body should be assessed on its own.
- **Evidence:**
  1. Platon, *The Present State of the Greek Church in Russia*, tr. Pinkerton (1814), `cic/texts/platon_present-state-of-the-greek-church-in-russia_pinkerton1814.txt`, appendix, file lines ~10930-10960 and ~11919 — **V**. "In 1801, the senators Lopuhine and Neledinskoy ... were the first who represented these people to the emperor in a true light." "Here the Duhobortsi formed two settlements in 1804". "The name Duhobortsi was already given to this sect in 1788, probably by the then Archbishop of Ekaterinoslav". "They are called Molokans, on account of their eating milk on the usual days of fasting." (OCR errors in names are the scan's.)
  2. Conybeare, *Russian Dissenters* (1921), Library — **V** for its structure (Part II: "The Dukhobortsy", "The Molokanye"; Part III: "The Khlysty", "The Skoptsy") and for the 1905 categories ("Sectaries, e.g. the Molokani, Stundists and Dukhobortsi"; "the 'pernicious' sects, e.g. the Khlysty ... and the Skoptsy"). The chapters themselves were not read in this run.
  3. Joseph Elkinton, *The Doukhobors, their History in Russia, their Migration to Canada* (Philadelphia, 1903), archive.org item doukhoborstheirh00elki — **[S]** (title and date from the search listing only).
- **Living:** yes (Dukhobor and Molokan communities in Canada, the United States, Russia and the Caucasus) [S]; no dated item read.
- **Mark's test:** A family of separate bodies, not one movement. They are not part of the Old Believers (Pinkerton files the Dukhobors among the priestless, but Conybeare separates them) or of the Stundists (VIII.51). Tolstoy's support for the 1899 migration ties them to the Tolstoyans (see notes), but they were older.
- **Overlap:** none on the roster. VIII.51 and IX.12 are Baptist and evangelical. VII.7 is the Old Believers.
- **Recommendation:** **hold** for Section A, then **enter** the bodies that clear it (most likely the Molokans) and route the Dukhobors to Mark under A4 if they do not.
- **Gate question G-ME6.** How should Russia's non-Orthodox spiritual Christians be handled?
  - (a) Assess the Dukhobors and the Molokans one by one under Section A, then enter an era 9 row for what clears, with the Khlysty and Skoptsy noted as out of scope. **Recommended**: the floor must be applied to each body's own confession, not to a family label.
  - (b) One era 9 "Beyond the Floor" row for the whole family, researched and explained, as lane 8 does for others.
  - (c) Out of scope for now; note them in VIII.51's relations line only.

##### ME-7. The Syriac Orthodox Church and the Syriac Catholic split (c. 1650-1906)

- **Answers the logged break:** the Syriac Orthodox church after 1300, held for sources (Open-Gaps 135). Inside this window, 1650-1906. The years 1300-1650 stay held.
- **Kind:** church bodies (the Syriac Orthodox patriarchate of Antioch; the Syriac Catholic patriarchate from 1781/1783). **Era:** 9 (with era 8 roots), or one row per era.
- **Dates:** c. 1650-1906. Fortescue dates the Catholic Syrian church "from 1781"; the patriarch's seat at Sharfeh in Lebanon is [S] for its date.
- **Region / countries:** Middle East; Turkey (Mardin, Deir al-Zaʿfarān, Tur Abdin, Diyarbakır, Urfa), Iraq (Mosul, Mar Mattai), Syria (Aleppo), Lebanon (Sharfeh), Jerusalem. **Lane:** 1 Syriac East & Asia.
- **What it carries that no row does:** the Syriac Orthodox patriarchate at Deir al-Zaʿfarān near Mardin, its bishops at Mosul, Urfa, Jerusalem and Tur Abdin; the Catholic party's election of Ignatius Michael Jarweh (Fortescue's "Giarve") and the two rival successions from then on; the Catholic Syrians' recognition as a separate millet (Fortescue: 1830); the fight over churches between the two (Badger, 1840s). The patriarchate's tie to Malabar (from 1665) belongs to the Asia pass and VI.18.
- **Section A:** No floor question. The Syriac Orthodox Church confesses the Nicene Creed and rejects Chalcedon, as II.2, III.17 and IV.21 were assessed; the Syriac Catholics are in communion with Rome.
- **B1 Sourcing:** Thin to moderate. A near-era outside witness who knew the patriarch and bishops (Badger 1852, V) and a 1909 study (Fortescue, V, a Catholic writer). No Syriac Orthodox own-voice text of the period opened. Wanted: Bar Hebraeus's continuators beyond 1369 (the held gap), Parry, *Six Months in a Syrian Monastery* (1895) [S], Assemani BO II (not vendored).
- **B2 Ecology:** Moderate: monastery and patriarch, Tur Abdin villages, Mosul merchants, Capuchin and Jesuit missions, Ottoman millet law.
- **B3 Uniqueness:** High. The Syriac Orthodox Church has no entry from 1300 to IX.19 (1915). IX.19 says Syriac history "had gone quiet after about 1300" (Open-Gaps 147).
- **B4 User needs:** history learners, Syriac Christian users and diaspora, academically minded users.
- **B5 Scale:** small.
- **Tier:** 2 (3 until an own-voice or in-region source is opened).
- **Evidence:**
  1. Badger, *The Nestorians and their Rituals*, vol. 1 (1852), Library, chapter "The Syrian Jacobites", file lines ~3320-3345 and ~3790-3810 — **V**. "The present hierarchy of the Jacobites in Turkey consists of a patriarch, who claims the title of 'Patriarch of Antioch and successor of S. Peter,' eight metropolitans, and three bishops." "The late patriarch Elias, whom I met at Constantinople in 1844 ... his time and attention were so absorbed in seeking to regain possession of the churches which the Syrian Romanists had seized upon". He visited "the patriarchal residence at Deir (convent) Zaaferan". Badger is an Anglican with his own aims and is harsh on the new patriarch.
  2. Adrian Fortescue, "Eastern Churches", *Catholic Encyclopedia* vol. 5 (1909), newadvent.org/cathen/05230a.htm, §5 "Syrians" — **V** (study). "The Catholic Syrian Church dates from 1781. At that time a number of Jacobite bishops, priests, and lay people, who had agreed to reunion with Rome, elected one Ignatius Giarve to succeed the dead Jacobite patriarch, George III." "From this time there have been two rival successions. In 1830 the Catholic Syrians were acknowledged by the Turkish Government as a separate millet."
  3. Andrew Akhijan's patriarchate at Aleppo (1662) as the first Syriac Catholic line — **[S]** (memory; not in either item read).
- **Living:** yes (both churches). No dated item after 2010 read.
- **Mark's test:** Unique. The Syriac Catholic split follows the same Roman pattern as the other unions, but the Syriac Orthodox Church's own story is what is missing, and no other row tells it.
- **Overlap:** II.2, III.17, IV.21 (to 1300); IX.19 (from 1915); IX.39 and VI.18 (Malabar). None carries 1300-1915.
- **Recommendation:** **hold for sources** (one own-voice or in-region item), then **enter** as an era 9 row with the Catholic split as a named line. If Mark wants the break closed now, an era 9 row on Badger and Fortescue alone would be Tier 3.
- **Gate question G-ME7.** What should close the Syriac Orthodox break before 1915?
  - (a) Hold, with a named want for the source-research thread (a Syriac or Arabic chronicle of the patriarchate after 1369, or Parry 1895), then an era 9 row. **Recommended**: the two items in hand are both outsiders, one Anglican and one Catholic.
  - (b) An era 9 row now (c. 1650/1781-1906) on Badger and Fortescue, with the asymmetry named.
  - (c) A short named line in IX.19 pointing back, and no row.

##### ME-8. The Romanian Greek Catholic Church of Transylvania: the union of Alba Iulia to the metropolitanate of Blaj (1698-1906)

- **Answers no logged break directly**, but it is the missing parent of IX.73 (which starts at the 1948 dissolution with no earlier entry).
- **Kind:** church body (Eastern Catholic). **Era:** 8 and 9 (one row per era, or one era 8 row with an era 9 named line).
- **Dates:** the union act of 7 October 1698 at Alba Iulia; Bishop Athanasius Anghel confirmed in 1701 (Nilles's section titles); to 1906. The see at Blaj (Balázsfalva), Inochentie Micu-Klein and the "Transylvanian School" (Școala Ardeleană) are [S] for their dates; the metropolitanate of 1853 is [S].
- **Region / countries:** North Europe (the tag IX.73 uses); Romania (Transylvania: Alba Iulia, Blaj, Făgăraș). **Lane:** 3<->5 bridge (Greek East / Latin West), as IX.73.
- **What it carries that no row does:** how most of Transylvania's Romanian Orthodox clergy entered communion with Rome under the Habsburgs, with the Jesuits of Alba Iulia as brokers; the church's role in Romanian national and scholarly life in the eighteenth and nineteenth centuries; and the Orthodox resistance to the union (the movement around the monk Visarion and Sofronie, [S]).
- **Section A:** No floor question (Nicene; Byzantine rite; in communion with Rome). Dated own statement: the union act of 7 October 1698 (V).
- **B1 Sourcing:** Moderate to strong. The union's own acts in Nilles's 1885 documentary edition (Latin and Romanian, V); a 1909 study for scale (Fortescue). Wanted: a Romanian study (for example Nicolae Iorga or Augustin Bunea, both pre-1930 [S]).
- **B2 Ecology:** Strong: bishops, protopopes, village priests, Jesuit advisers, the Habsburg court and Transylvanian estates, schools and the press at Blaj, Orthodox resisters.
- **B3 Uniqueness:** High. The roster has this church only from 1948 (IX.73). VI.14 is the Transylvanian Unitarians; the Ruthenian rows (VI.20, VII.28, VIII.38) are a different union.
- **B4 User needs:** history learners, Romanian users, Eastern Catholics, academically minded users.
- **B5 Scale:** large (Fortescue: "about a million and a half" Romanian Catholics in 1909).
- **Tier:** 1 for an era 8 row on the union; 2 for era 9 until a Romanian study is opened.
- **Evidence:**
  1. Nicolaus Nilles, *Symbolae ad illustrandam historiam ecclesiae orientalis in terris coronae S. Stephani* (Innsbruck, 1885), archive.org item symbolaeadillus00nillgoog, raw djvu text — **V**. The act, in Latin beside its Romanian text: «Nos infrascripti Vladica, protopresbyteri ac presbyteri ecclesiarum Valachicarum ... libere cum Ecclesia Romano-Catholica unionem inimus, ejusdem Sanctae Romano-Catholicae Ecclesiae commembra nos per has literas testimoniales declaramus» ... «Datum Albae-Juliae anno Domini 1698 die 7. Octobris.» ("We the undersigned bishop, archpriests and priests of the Wallachian churches ... freely enter into union with the Roman Catholic Church, and by this letter of witness declare ourselves fellow members of the same holy Roman Catholic Church ... Given at Alba Iulia, 7 October 1698", my rendering; OCR damage silently read through, e.g. «inimus» from «i n i m u s»). Section headings: «Acta sub Athanasio nondum confirmato 1698—1701» and «Acta sub Athanasio rite confirmato 1701—1713». A synod text cited: «Octavus jam volvitur annus, quod opera ac solertia Patrum S. J., Albae-Juliae degentium, de unione cum Sancta Romano-catholica Ecclesia agere coepimus» ("The eighth year is now turning since, by the work and skill of the Jesuit Fathers living at Alba Iulia, we began to treat of union with the holy Roman Catholic Church", my rendering). Nilles was a Jesuit canonist; a Catholic documentary edition.
  2. Fortescue, "Eastern Churches", *Catholic Encyclopedia* vol. 5 (1909) — **V** (study): "Rumanian Catholics (about a million and a half) in Rumania, but chiefly in Transylvania. They have bishops and use their own language in the liturgy."
  3. Inochentie Micu-Klein, Blaj, the Transylvanian School, the 1853 metropolitanate — **[S]**.
- **Living:** yes (IX.73 carries it to c. 2010).
- **Mark's test — this is the closest case to his Jesuit example.** The Jesuits of Alba Iulia brokered the union, by the synod's own words. But the church that came out of it is a separate body with its own bishops, rite and language, alive today (IX.73), and the Jesuits' worldwide work is not its story. So: the Jesuits are a named line inside this row; the row is not part of a Jesuit row, and a Jesuit continuation row (if Mark wants one) would only point here.
- **Overlap:** IX.73 (from 1948); VII.19 (the Catholic church of the ancien régime; does not name Transylvania); VIII.28 (Romania's Orthodox church from 1885; the Transylvanian Orthodox see at Sibiu, 1864, is named only in Fortescue's list).
- **Recommendation:** **enter** an era 8 row (1698-1815), with the era 9 years (Blaj, the metropolitanate, the national revival) as an era 9 row once a Romanian study is opened, or as a named line until then. Name the **Carpathian Ruthenian union** (Uzhhorod, 1646; Mukachevo, a see by Nilles's "primus episcopus Munkacsiensis" entry, date [S]) as a **named line in VII.28 / VIII.38** (the Ruthenian rows), not here.
- **Gate question G-ME8.** How should the Romanian Greek Catholic Church before 1948 enter?
  - (a) An era 8 row from the 1698 union, and an era 9 row (or named line) to 1906, both linked to IX.73. **Recommended**: the union act is in hand in its own words, and IX.73 has no parent.
  - (b) One composite row, "The Greek Catholic churches of the Hungarian crown" (Romanians and Carpathian Ruthenians), 1646/1698-1906. Tidier, but it joins two peoples with separate stories and separate era 10 heirs (IX.73, IX.21).
  - (c) A named line in VII.19 only.

##### ME-9. Hungarian and Transylvanian Protestantism: the "decade of mourning" to the Patent of Toleration and 1848 (1650-1906)

- **Answers no logged break.** A gap found by this pass.
- **Kind:** church bodies (the Reformed Church in Hungary and Transylvania; the Lutheran Church of Hungary). **Era:** 8 and 9.
- **Dates:** 1650-1906. Markers: the trials of Protestant preachers in the 1670s and their sale to the Naples galleys, freed by Admiral de Ruyter's fleet on 11 February 1676 (Bauhofer, V); Joseph II's toleration of 24 October 1781 (Bauhofer, V); the equality of confessions decreed by the Diet in 1848 (Catholic Encyclopedia, V).
- **Region / countries:** North Europe (the tag VI.14 uses); Hungary, Romania (Transylvania), Slovakia. **Lane:** 6 Protestant & Evangelical.
- **What it carries that no row does:** the largest Protestant churches of East-Central Europe, under Habsburg Counter-Reformation pressure and Ottoman retreat; the galley-slave preachers, a famous martyrology; Debrecen and Sárospatak as Reformed centers [S]; the 1781 toleration and the 1848 equality; the Lutheran Slovaks and Germans of Upper Hungary [S].
- **Section A:** No floor question (Reformed and Lutheran confessions; the Second Helvetic and Augsburg confessions [S for the Hungarian adoption dates]).
- **B1 Sourcing:** Moderate. A Hungarian Protestant church history of 1854 in English (Bauhofer, V), a 1910 Catholic study (CE "Hungary", V). Wanted: a Hungarian-language source and the galley-slaves' own narratives (for example the account of Bálint Kocsi Csergő, [S]).
- **B2 Ecology:** Strong: nobles and towns, colleges, village pastors, Habsburg courts and Jesuits, Ottoman and Transylvanian princes, peasants.
- **B3 Uniqueness:** High. The roster's only East-Central European Protestant rows are VI.14 (anti-Trinitarians, to 1650) and VI.24 (the Czech churches, to 1627).
- **B4 User needs:** Reformed and Lutheran users, history learners, academically minded users.
- **B5 Scale:** large.
- **Tier:** 2 (1 once a Hungarian source is in hand).
- **Evidence:**
  1. [Johann] Bauhofer, *History of the Protestant Church in Hungary, from the Beginning of the Reformation to 1850; with special reference to Transylvania*, tr. J. Craig, intro. Merle d'Aubigné (Boston, 1854), archive.org item historyofprotest00bauh, raw djvu text — **V**. "On the 11th of February, 1676, the chaplain of the Dutch fleet, accompanied by several superior officers, went on board the boats, and, as in a dream, the prisoners forsook the place of their confinement, singing the 46th, the 114th, and 125th Psalms." Joseph II's edict reached the Protestants "on the 24th of October, 1781". A Protestant apologetic history; the author's name is [S] as the title page in this OCR shows only the translator.
  2. "Hungary", *Catholic Encyclopedia* vol. 7 (1910), newadvent.org/cathen/07547a.htm — **V** (study, Catholic): "The Diet of 1848 decreed the equality and reciprocity of all recognized confessions."
- **Living:** yes (the Reformed Church in Hungary; the Lutheran churches) [S]; no dated item read.
- **Mark's test:** Unique. These are national churches of the Reformation, not part of the German Pietist or Moravian movements, though Halle shaped some Hungarian Lutherans [S].
- **Overlap:** VI.14 (Transylvanian Unitarians, to 1650); VI.2 (the Reformed cities, the parent tradition); VIII.41 (German confessional Lutherans). None names Hungary's Protestants after 1650. This may also fall to the rivers pass (Protestant and Evangelical): flag it to the merge.
- **Recommendation:** **enter** an era 8 row (1650-1815), with era 9 as a named line or a second row.
- **Gate question G-ME9.** How should Hungarian Protestantism enter?
  - (a) An era 8 row (1650-1815: persecution to toleration), with 1815-1906 (1848, the autonomy struggles) as an era 9 row once a Hungarian source is opened. **Recommended**: era 8 is where the galley-slave story and 1781 sit, and both are verified now.
  - (b) A named line in VI.2's descendants (the Reformed) and VIII.41 (Lutherans). Not recommended: neither runs east of Germany.
  - (c) Leave it to the rivers pass.

##### ME-10. Polish and Lithuanian Catholicism under the partitions (1772/1815-1906)

- **Answers no logged break**, but IX.70 (Polish Catholicism, from 1918) has no parent, and no row carries the Catholic Church of the Polish-Lithuanian lands at all between VI.22 (to 1650) and IX.70.
- **Kind:** church body (the Latin Catholic Church in the partitioned Polish and Lithuanian lands). **Era:** 9 (with the 1772-1795 partitions at the end of era 8).
- **Dates:** 1815-1906 (the row); era 8 roots from the partitions of 1772, 1793 and 1795.
- **Region / countries:** North Europe (the tag IX.70 uses); Poland, Lithuania, with Belarus and Ukraine for the dioceses Russia held. **Lane:** 5 Latin West & Catholicism.
- **What it carries that no row does:** the church as the carrier of a nation without a state; Russian measures after 1831 and 1863 (convents suppressed, church property taken by the 1864 order, the clergy put under a St Petersburg commission in 1867); the Prussian Kulturkampf in Poznań and Gniezno (Archbishop Ledóchowski's imprisonment, [S]); the 1905 toleration; the Lithuanian press ban of 1864-1904 and the book-smugglers (*knygnešiai*), a defined movement of its own ([S] in this run).
- **Section A:** No floor question (Catholic).
- **B1 Sourcing:** Moderate. A 1911 study by a Polish Catholic author (Kołodziejczyk, CE "Poland", V); papal documents to the 1770s in the Library (Theiner, *Vetera monumenta Poloniae et Lithuaniae*, vol. 4, V as held, not read here). Wanted: Polish pastoral letters of the period and a Lithuanian source on the press ban.
- **B2 Ecology:** Strong: bishops in exile, parish priests, convents, insurgents, peasants, pilgrimages (Częstochowa, [S] for this period), smugglers, three empires' police.
- **B3 Uniqueness:** High. The only Polish Catholic row is IX.70 (from 1918). The Greek Catholic rows (VI.20, VII.28, VIII.38) are a different church.
- **B4 User needs:** Catholics, Polish and Lithuanian users, history learners.
- **B5 Scale:** large.
- **Tier:** 1.
- **Evidence:**
  1. E. Kołodziejczyk, "Poland", *Catholic Encyclopedia* vol. 12 (1911), newadvent.org/cathen/12181a.htm — **V** (study). "After the three partitions (1773, 1793, 1795), the Government of Russia strove to extirpate, not only Polish nationality, but also the Catholic Church." "Even harsher measures were adopted after 1863: by a cabinet order of 1864, the property of the Church was confiscated, the convents still in existence suppressed; in 1867 the clergy were placed under the authority of a commission at St. Petersburg". "Not until after the war with Japan was an edict of toleration proclaimed in Russia". "Obstacles raised by the Government to hinder vocations were so effective that in the seven years immediately following 1863 not more than ten priests were ordained in Lithuania". On Prussia: "The Catholic clergy in Prussian Poland was subordinated to the temporal power." (The article dates the first partition 1773; 1772 is the usual date.)
  2. Augustin Theiner, *Vetera monumenta Poloniae et Lithuaniae*, vol. 4 (Rome, 1864), Library — **V** as a held file; its coverage of the later eighteenth century was not checked.
- **Living:** yes (IX.70).
- **Mark's test:** Unique. VIII.29 (the Catholic world) and VIII.33 (Old Catholics, whose legacy line names Poland among its national churches) do not tell it. It belongs to no cross-world movement.
- **Overlap:** VIII.38 (the Greek Catholic church the same Russian policy dissolved in 1839 and 1875; CE's "the Uniats were forced into apostasy" is that story); IX.70 (from 1918); VII.19 and VIII.29 (Rome-centered).
- **Recommendation:** **enter** an era 9 row (1815-1906), with the partitions as its opening; the Commonwealth church of 1650-1772 (the 1655 defense of Jasna Góra, the Marian Fathers) as a **named line in VII.19** or a held era 8 row.
- **Gate question G-ME10.** How should the Polish-Lithuanian Catholic church before 1918 enter?
  - (a) An era 9 row, 1815-1906, parent of IX.70, with the Lithuanian book-smugglers as a named line once a source is opened. **Recommended**: the verified item covers exactly these years.
  - (b) An era 8 row as well (1650-1815: the Commonwealth church to the partitions). Fuller, but its sources are not yet opened.
  - (c) Named lines in VIII.29 only.

##### ME-11. The Arab Evangelical churches and the American mission in Syria and Lebanon (1819/1823-1906)

> **Merge note (rivers pass).** Merged into RV-4, one row for the Arab evangelical churches of Syria-Lebanon and Egypt, not a fifth VIII.7 wing (rivers §1c). See G89-3.

- **Answers no logged break.** A gap found by this pass.
- **Kind:** church body (the evangelical churches of Syria and Lebanon) with the mission that planted them. **Era:** 9.
- **Dates:** missionaries instructed in November 1819; arrival at Beirut 10 July 1823; the first native evangelical church organized in Beirut in 1848; the Arabic Bible completed 10 March 1865; the Syrian Protestant College 1866 [S for its date in this run].
- **Region / countries:** Middle East; Lebanon, Syria. **Lane:** 6 Protestant & Evangelical.
- **What it carries that no row does:** the Arabic Protestant church and its Bible (the Smith-Van Dyck translation, with Butrus al-Bustānī and Nāṣīf al-Yāzijī [S for Bustānī's role, V for Yāzijī as "assisting"]), schools and press; converts from the Maronite, Melkite and Orthodox churches; the Ottoman Protestant millet of 1850 (VIII.32 names it for the Armenians).
- **Section A:** No floor question (Reformed evangelical).
- **B1 Sourcing:** Moderate. A missionary's own fifty-year history (Jessup 1910, V); Rufus Anderson's 1872 history of the ABCFM missions to the Oriental churches (archive.org; the text fetch failed in this run, [S]). Wanted: an Arabic source from the church itself (for example Bustānī's own writings).
- **B2 Ecology:** Moderate to strong: missionaries, Arab teachers and translators, converts and their excommunication, the press, schools, the 1860 war.
- **B3 Uniqueness:** High. No row carries Arab Protestants. VIII.32 carries the Armenian Evangelicals; VIII.40 carries Urmia; VIII.7 carries other mission churches but not the Middle East.
- **B4 User needs:** evangelical users, Arab Christian users, history learners.
- **B5 Scale:** small.
- **Tier:** 2.
- **Evidence:**
  1. Henry Harris Jessup, *Fifty-three Years in Syria*, vol. 1 (New York, 1910), archive.org item fiftythreeyearsi011832mbp, raw djvu text — **V**. Pliny Fisk sailed "November 3, 1819"; "He arrived in Beirut July 10, 1823"; "Friday, March 10, 1865, a celebration took place at the American Press, in honour of the printing of the Old Testament, thus completing the new Arabic translation of the Bible"; Van Dyck's translation began in 1848, "assisted by Sheikh Nasif el Yazigy"; a chapter headed "Organization of a Native Evangelical Church (1848)". Jessup is a Presbyterian missionary, openly hostile to the Eastern churches ("Their reform hopeless").
  2. Rufus Anderson, *History of the Missions of the American Board ... to the Oriental Churches* (Boston, 1872) — **[S]** (archive.org listing only).
- **Living:** yes (the National Evangelical Synod of Syria and Lebanon) [S]; no dated item read.
- **Mark's test:** It is part of one cross-world movement in a sense, the American Board's missions, which also made the Armenian Evangelical Church (VIII.32) and the Urmia work (VIII.40). But no row tells the American Board as a movement; VIII.7 is the mission-born native churches of India, Africa, the Pacific and China. **Option to weigh:** a single era 9 row, "The Protestant missions to the Oriental churches and the evangelical churches they made" (Beirut, Constantinople, Urmia), with VIII.32 and VIII.40 keeping their own pieces.
- **Overlap:** VIII.32 (Armenian Evangelicals, 1846/1850); VIII.40 (Urmia mission); VIII.7 (other mission churches).
- **Recommendation:** **enter** as an era 9 row for the Arab evangelical church, or as a new wing of VIII.7 (see the gate question).
- **Gate question G-ME11.** Where do the Arab Protestant churches go?
  - (a) A fifth wing in VIII.7, "Syria and Lebanon", beside its four. **Recommended**: VIII.7 is already the row for churches born of the Protestant missionary societies, and this is one, so the census keeps one story.
  - (b) A new era 9 row for the Arab evangelical church alone.
  - (c) A new era 9 cross-world row for the American missions to the Oriental churches, with the Armenian and Urmia pieces as named lines pointing to VIII.32 and VIII.40.

##### ME-12 to ME-22. Named lines, routings and smaller items

Each is short: what it is, the row that should carry it, the evidence state, and a recommendation. None needs its own row on present evidence.

> **Merge note (rivers pass).** ME-12 is re-homed into RV-1 as one of its lines (rivers §1a). See G89-1.

- **ME-12. The Jesuits in Russia, 1773-1814 (Mark's Jesuit test).** After Clement XIV suppressed the Society in 1773, its members in the Russian Empire carried on. Pius VII's bull of 1814 recites that "Francis Kareu ... and other secular Priests resident for many years in the vast empire of Russia, and who had been members of the Company of Jesus" had asked to unite, and that "the then reigning Emperor Paul I. had recommended the said Priests in his gracious dispatch, dated the 11th of August, 1800" (`cic/texts/clement-xiv_bulls-suppression-and-restoration-of-the-jesuits-lat-eng_1814.txt`, file lines ~140-158 — **V**). This is the Jesuits' own story, one worldwide movement, exactly Mark's example. **Recommendation:** a named line in whatever Jesuit home Mark rules for the China break (a Society of Jesus era 8 continuation of VI.11), or in VII.19, which already tells the 1773 suppression and 1814 restoration. Not a regional row.
- **ME-13. The Bulgarian church revival from Paisii of Hilendar (1762).** Paisii's *Istoriia slavianobolgarskaia* (*История славянобългарская*, "Slavo-Bulgarian History", 1762; ed. Ivanov 1914), `cic/texts/paisii-hilendarski_istoriia-slavianobolgarskaia-bul_ivanov1914.txt` — **V** (held; the registry says he complains "of Greek domination of their church"). The corpus map already lists it for VII.18 and VIII.28, but neither row's text names it. **Recommendation:** a named line in VII.18, running into VIII.28's Exarchate (1870).
- **ME-14. The Armenian church in the Russian Empire: the Polozhenie of 1836.** Malachia Ormanian, *The Church of Armenia* (1912), Library, file line ~4758 — **V**: "the regulation (pologenia) which was specially enacted (1836) for the purpose of establishing connection with the patriarchal administration, opened very wide the door for the interference of the political authority." Ormanian was Armenian patriarch of Constantinople, a voice from inside the church. VIII.32 is Constantinople-centered and does not name Etchmiadzin under Russia (VII.24a ends with 1810). **Recommendation:** a named line in VIII.32.
- **ME-15. The Armenian Catholic schism of 1870 and the bull *Reversurus* (1867).** Labourt, CE "Chaldean Christians" — **V** (study): "the Bull 'Reversurus' had provoked (1867) a schism in Armenia". VIII.32 names an Armenian Catholic patriarchate only "alongside". **Recommendation:** a named line in VIII.32; [S] for the details of Hassun and the Hassunite schism.
- **ME-16. The Holy Places and the Latin Patriarchate of Jerusalem (1847).** Fortescue, CE "Jerusalem (After 1291)" (1910) — **V** (study): "It was the dispute between Catholics and Orthodox as to the keys of the Holy Sepulchre that immediately caused the Crimean War (1853)"; the Franciscan Custos was "till 1847 the supreme authority for Catholics in Palestine", until Pius IX made the titular patriarchate "a real see again at Jerusalem" (the article misprints "Pius III" once). A cross-church story with no row since IV.25 (Latin Outremer) and VII.18. **Recommendation:** hold as a gate note; it may be a named line in VIII.28 (the Orthodox side) and VIII.29 (the Catholic side). Not a movement by the four marks.
- **ME-17. Orthodox church bodies the census lists nowhere: Karlovci, Montenegro, Sibiu.** Fortescue, CE "Eastern Churches" (1909) — **V** (study), in his list of autocephalous churches: "Carlovitz (1765), formed of Orthodox Serbs in Hungary"; "Czernagora (1765), with one independent diocese of the Black Mountain"; "Hermannstadt (Nagy-Szeben, 1864), the Church of the Vlachs in Hungary, with three sees" (Fortescue's dates are for their independence as he reckons it). VII.18 names Karlovci; nothing names Montenegro's prince-bishops or Andrei Șaguna's Transylvanian metropolis. **Recommendation:** named lines in VII.18 (Karlovci, Montenegro) and VIII.28 (Sibiu, 1864).
- **ME-18. Russian Orthodox missions inside the empire: Siberia, the Volga and Il'minskii's schools; the Beijing mission (1715).** VII.21 names Valaam and Alaska; VIII.31 names the Altai and Japan. No source opened in this run — **[S]**. The Beijing mission falls to the Asia pass. **Recommendation:** named lines in VII.21 and VIII.31 once a source is opened (for example Mouravieff 1842, in the Library, for Siberia; not searched here).
- **ME-19. Urmia: the Assyrian evangelical church and the Russian Orthodox mission of 1898.** VIII.40 names the American mission and the Canterbury mission. The Russian mission and the Assyrians' turn to Orthodoxy are **[S]** (Wigram 1929, in the Library, not read). **Recommendation:** a named line in VIII.40.
- **ME-20. The Tolstoyans (1880s-1906).** A defined movement on its face (a beginning in the 1880s, carriers around Vladimir Chertkov, a name, and studies), tied to the Dukhobors by the 1899 migration. Section A is a floor question: Tolstoy denied Christ's divinity [S; his own words not opened]. **Recommendation:** out of scope under A1 unless Mark chooses a lane 8 "Beyond the Floor" entry; noted with ME-6.
- **ME-21. The Hebrew Christians of Kishinev (Joseph Rabinowitz, 1884).** A small, named Jewish-Christian congregation in Bessarabia. **[S]** only. It would be the earliest parent of IX.13 (Messianic Judaism), which starts in 1960. **Recommendation:** hold for sources.

> **Merge note (rivers pass).** ME-22 is answered by RV-2 (rivers §2). See G89-49.

- **ME-22. Mennonites and Hutterites in the Russian Empire (1789-1874).** The Anabaptist river after VI.3 (to 1650) has no Mennonite row in eras 8-9. The Russian colonies are named in VIII.51 only as the Stundists' German neighbors. The Library holds the Hutterite chronicles (V as held). **Recommendation:** route to the rivers pass (Anabaptist), as a single movement across Europe and Russia, not a regional row.

---

#### 3. Ranked list (importance to the eras' global story)

| Rank | ID | Candidate | Era | Tier | Recommendation |
|---|---|---|---|---|---|
| 1 | ME-5 | Old Believers, 1815-1906 | 9 | 1 | Enter |
| 2 | ME-2 | Maronite Church, 1650-1906 | 8, 9 | 1 (era 9), 2 (era 8) | Enter era 9; era 8 after the 1736 acts |
| 3 | ME-10 | Polish and Lithuanian Catholicism under the partitions | 9 | 1 | Enter |
| 4 | ME-8 | Romanian Greek Catholic Church, 1698-1906 | 8 (+9) | 1 | Enter era 8; era 9 row or named line |
| 5 | ME-4 | The two Melkite churches, 1815-1906 | 9 | 1-2 | Enter one row for both; 1650-1724 named line in VII.23 |
| 6 | ME-1 | Church of the East, 1650-1815 | 8 | 2 | Enter |
| 7 | ME-3 | Georgian church, 1650-1811 (+ Exarchate) | 8 | 2 | Enter era 8; Exarchate as named line in VIII.31 |
| 8 | ME-9 | Hungarian and Transylvanian Protestantism | 8 (+9) | 2 | Enter era 8 |
| 9 | ME-11 | Arab Evangelical churches of Syria and Lebanon | 9 | 2 | Fifth wing of VIII.7 |
| 10 | ME-6 | Dukhobors, Molokans and other spiritual Christians | 9 | 2 | Hold for Section A, body by body |
| 11 | ME-7 | Syriac Orthodox and the Syriac Catholic split | 9 | 2-3 | Hold for one in-region source |
| — | ME-12 to ME-22 | Named lines and routings | 8, 9 | — | See §2 |

#### 4. How each logged break was answered

| Break (Open-Gaps 135/142) | Unique, or part of another movement? | Answer |
|---|---|---|
| Church of the East, 1650-1815 | Unique: the middle of VI.30 → VIII.40. Capuchin and Propaganda work is a strand inside it, not a movement row. | ME-1, era 8 row (V: Badger, Malech, Labourt) |
| Maronites, 1517-1900 | Unique: IV.10 and V.22 carried on. Rome is part of the story, as for every Eastern Catholic church. | ME-2, era 8 and era 9 rows; 1517-1650 flagged to the era 7 owner |
| Georgian church, none after 1245 | Unique for 1650-1811. The Exarchate (1811-1917) sat inside the Russian Synod, so it is a named line in VIII.31 leading to IX.40. | ME-3; 1245-1650 flagged to the era 6 and 7 owners |
| Melkites, 1009-1724 (held) | Only 1650-1724 falls here: Macarius III's world, the run-up to VII.23's 1724 split. Same church as VII.23. | Named line in VII.23 (V: Paul of Aleppo, Fortescue); 1009-1650 stays held. New finding: nothing after 1815 (ME-4). |
| Syriac Orthodox after 1300 (held) | Unique. The Syriac Catholic split is its own strand. | ME-7, still held: both items opened are outsiders (Badger, Fortescue) |
| Old Believers after 1815 | Unique: VII.7 carried on. VIII.31 names Belokrinitsa as "separate". | ME-5, era 9 row (V: Conybeare, Pinkerton) |

---

#### 5. Notes

1. **The Catholic Encyclopedia is the workhorse here, and it is one-sided.** Its Middle Eastern articles are by real scholars (Labourt, Fortescue, Charon) and are inside the era, but they call the other churches "schismatics". Every row that leans on one needs a second, non-Catholic study.
2. **Propaganda Fide and the Capuchins brokered most of this region's unions** (Diyarbakır 1672/1681, Alba Iulia 1698, Damascus 1724, Mosul 1778, Aleppo 1781). Under Mark's test this could look like one movement. It is not one in the four-marks sense: it is a policy of one church, carried out by several orders, and each union made a separate living church. The policy belongs in VII.19 and VIII.29; each church gets its own row.
3. **The Jesuits appear twice in this region**: as brokers of the Romanian union (ME-8, the synod's own words) and as survivors in Russia after 1773 (ME-12). Both support one Jesuit continuation home for era 8, if Mark rules one for the China break.
4. **VII.23's corpus map already lists Charon's 1833-1855 volume**, and VII.18's lists Paisii (1762), but neither row's text uses them. Part of this region's gap is unused Library holdings, as CORPUS-USE.md expects.
5. **Era 10 parents.** ME-8 would give IX.73 a parent, ME-10 gives IX.70 one, ME-2 would give the era 10 sweep's proposed Maronite row (E6, not on the roster) one, and ME-3 gives IX.40 one.
6. **Section A is open only for ME-6 and ME-20.** All other candidates confess the Nicene Creed.
7. **Not swept in this pass:** Kosmas the Aitolian and Greek itinerant preaching; Albanian and Bosnian Catholics (the Franciscans); the Czech lands after 1627 (the hidden Protestants, the 1781 toleration), which sit between this region and North Europe; Cossack and Ukrainian Orthodox under Russia after 1686 (VII.21 names the transfer).
8. **Wanted list for the source-research thread:** the 1736 Maronite synod acts (Mansi 38); a clean Duwayhī; Assemani BO III for the Josephite years; a Syriac Orthodox chronicle after 1369 or Parry 1895; Brosset's modern Georgian volumes (1856-1858); a Belokrinitsa own-voice text; Anderson 1872; a Romanian pre-1930 study (Bunea, Iorga); a Hungarian Protestant source in Hungarian.

---

## 7. Rivers cross-check

The pass's `candidates.md`, as written, with its headings demoted two levels. Changes: British to American spelling in the pass's own prose, and a merge note at the head of each candidate the rivers pass gave a new home.

### P2-G89 rivers pass: the cross-check, 1650-1906, every river, all regions

Scratch research for the gate, not census copy. **Phase: divergent.** Nothing here is decided.
Eras 8 and 9 are frozen, so every addition reaches Mark's gate as a change order.

#### Summary (put here because this folder may not take a summary.md)

**Conflicts the merge must present as one question each**

| # | Conflict | Recommendation |
|---|---|---|
| a | A Jesuit era 8 row? (LA yes; ME possible; AP no) | **RV-1: one Society of Jesus row, 1650-1814, continuing VI.11.** It carries the reductions, the expulsions, Russia and 1814. The China church stays its own row (AP2), as era 7 has VI.11 beside VI.13c. The Rites have one home: AP2. |
| b | Propaganda Fide / MEP | **No row for either.** Propaganda is a Roman office: named lines in VII.19 (1650-1815) and VIII.29. MEP is a carrier: named in AP2, AP4, VIII.21, VIII.45, and in one worldwide "Catholic mission revival" line in VIII.29 (AF-6, widened beyond Africa). |
| c | VIII.7: three new wings or lines | **Keep VIII.7 at four wings.** Its own status text sends other regions to their own entries. Southern Africa: a row (AF-5 option b, or one Cape row with AF-4). Arab Evangelicals: RV-4, one row for Syria-Lebanon and Egypt (merges ME-11 and AF-9's Egypt line). Karen: a named line in VIII.27, not VIII.7. |
| d | Moravians after 1815 | **RV-5: one Moravian era 9 row, continuing VII.4.** Caribbean, Cape, Suriname, Labrador and Nyasa become its lines, not pieces of regional rows. |
| e | Duplicates and row homes | Six joins to settle (§1e). No body is proposed twice under two names, but the Jesuits, Moravians, Egypt Protestants, Rites, Catholic mission revival and Southern Africa each have two homes. |

**New candidates (ranked)**

| ID | Candidate | Era | Recommendation |
|---|---|---|---|
| RV-1 | Society of Jesus, 1650-1814 | 8 | Enter (answers conflict a) |
| RV-5 | Moravian Church, 1815-1906 | 9 | Enter (answers conflict d) |
| RV-4 | Arab evangelical churches, Syria-Lebanon and Egypt, 1823-1906 | 9 | Enter (answers conflict c) |
| RV-3 | Catholics of the Ottoman Balkans (Bosnian Franciscans; Albanian and Bulgarian Catholics) | 8-9 | Enter era 8 on V items; era 9 after one more source |
| RV-2 | Mennonites and Hutterites in the Russian Empire, 1789-1906 | 9 (from 1789) | Enter as the in-scope chapter of one Anabaptist continuation row; ask the North Europe owner |
| RV-6 | Liberia's settler churches and the Black Atlantic links | 9 | Named line in VIII.7 plus links from VIII.1 |
| RV-7 | Transylvanian Unitarians after the Polish exile, 1660-1906 | 8-9 | Hold (Section A lane 8 question; sources thin) |
| RV-8 | Czech lands after 1627: hidden Protestants and the 1781 toleration | 8-9 | Named line in VII.4 now; the 1781-1906 churches to a North Europe pass |
| RV-9 | Kosmas the Aitolian | 8 | Hold; then a named line in VII.18 |

**Carried already (no candidate):** the Ecumenical Patriarchate under the Ottomans (VII.18); the
Greek autocephaly of 1850, the Bulgarian Exarchate of 1870, Serbia 1879 (VIII.28); Peć 1766 and
Karlovci (VII.18; ME-17 adds Karlovci after 1815 and Montenegro); the Armenian Apostolic church
(VII.24a, VIII.32, plus ME-14) and the Armenian Catholics (VII.24, VIII.32, plus ME-15); the
Coptic-Ethiopian tie (AF-1 and AF-2, one "in contact with" link); Alaska (VII.21 from 1794,
VIII.47); Siberia (ME-18's named lines in VII.21 and VIII.31; this pass adds a V source).

**Timeline breaks (Open-Gaps 135 and 142) in 1650-1906:** every break was answered by some
pass except two, both North Europe: **the Scottish church after 1650** and **the Swedenborgian
New Church after 1815** (Open-Gaps 135). Neither is in any regional pass's scope, so neither is
answered. See §3.

**Noted, not assessed (outside every pass's region):** the Waldensians after 1655 (VI.10 ends
"1655+", no successor; Mediterranean Europe had no pass); the Church of Cyprus under the Ottomans
[S]; the Greek Orthodox Patriarchate of Alexandria (noted by the Africa pass).

---

#### Verification key (the brief's)

- **V**: opened in this run (a `cic/texts/` file, or a public-domain edition fetched raw with
  curl) and the detail confirmed. Raw downloads sit in the session scratchpad, not the repo.
- **V-s**: a study's bibliographic details only (a catalog or search record seen).
- **[S]**: snippet, summary, memory or unopened. Never verified.
- Only V carries a sentence. Quotes from OCR keep the source's spelling; check the page image
  before any census use. Every V source below is before 1930 and public domain by date.
- "V (pass)" means a regional pass opened it; this pass relies on that pass's record.

Roster note: `atlasId` VI.x is era 7, VII.x era 8, VIII.x era 9, IX.x era 10.

---

#### 1. The cross-region conflicts

##### 1a. A Society of Jesus row for era 8

**What the three rows say.**
- **VI.11** (1540-1650) is the order as one movement: "a mobile body of preachers, confessors,
  schoolmasters and missionaries ... sending men to India, Japan, China, Brazil and Canada". It
  has no `continuesAs`. Its links are "gave rise to" Kirishitan Japan, Ming China and the
  Philippines, and "broke with" from Ethiopia and the St Thomas Christians.
- **VII.19** (1650-1815) is Rome and the Catholic monarchies. It tells the Jesuits only as an
  object: the expulsions "from Portugal, France, Spain and Naples", the suppression of 1773 and
  the restoration of 1814. It carries a link "argued against" to VI.11.
- **VIII.29** (1815-1906) does not name the Jesuits. It names "new congregations" and "the growth
  of missionary Catholicism".

So the order Mark named as "a single movement" stops on the tree in 1650. From 1650 to 1814 it is
told only from Rome's side, and only in Europe.

**What the passes found.**
- Latin America: the Paraguay reductions are Jesuit work under the Society's own province; they
  end with the expulsions (LA8-2; Muratori 1743, V (pass); Benedict XIV's bull of 1741, V (pass)).
- Middle East: the Jesuits brokered the Romanian union of 1698 (ME-8; Nilles 1885, V (pass)) and
  survived in Russia after 1773 (ME-12).
- Asia: after 1650 the Jesuits are carriers inside local churches (Beijing court, Vietnam, Madurai
  [S], the Carmelite-Jesuit quarrel in Kerala). The China church outlives them (AP2, AP-X1).

**What this pass opened.**
- Clement XIV, *Dominus ac Redemptor* (1773), English in
  `cic/texts/clement-xiv_bulls-suppression-and-restoration-of-the-jesuits-lat-eng_1814.txt`,
  file lines ~1190-1280. **V.** The bull sums up a century of charges against the order across
  "Europe, Africa, and America", including disputes "concerning the meaning and practice of
  certain idolatrous ceremonies adopted in certain places". It says the kings of "France, Spain,
  Portugal, and Sicily" were driven to expel them. The papal act itself ties the rites, the
  missions and the expulsions together as one order's story.
- Pius VII's bull of 1814, same file, lines ~140-158. **V.** "Francis Kareu ... and other secular
  Priests resident for many years in the vast empire of Russia, and who had been members of the
  Company of Jesus" asked to unite, and Paul I had recommended them "in his gracious dispatch,
  dated the 11th of August, 1800".

**Against Mark's test.** His words: "check that they are unique and not tied to other movements,
like jesuites moving around the world, that is a single movement". Two things follow.
1. A story that is only Jesuit work does not get a row of its own by place. The reductions fail
   the test as a separate row; so would a "Jesuits in Russia" row.
2. A story that a local church owns is unique even where Jesuits served in it. The China church
   (AP2), Japan's hidden Christians (AP3) and the Romanian Greek Catholics (ME-8) pass.

The roster already works this way in era 7: VI.11 stands beside VI.13b and VI.13c, joined by
"gave rise to" links. The open question is only whether the single movement gets its own era 8
row, or lives as scattered lines.

**Options.**
- **(a) No Jesuit row.** Lines in VII.19 (expulsions, Russia, 1814) and in local rows. Cost: the
  reductions have no fitting home (VII.17 is settled diocesan piety, as LA8-2 says); a single
  movement is split across five rows, which is what Mark warned against.
- **(b) A Society of Jesus row, 1650-1814, continuing VI.11 (RV-1).** It carries the reductions,
  the court mission's Jesuit side, the Malabar and Madurai rites [S], the expulsions of 1759-67,
  the suppression (VII.19 keeps Rome's act), Russia 1773-1814 and the restoration. The China
  church, Japan's hidden Christians and the Romanian union stay their own rows, linked to it.
- **(c) A Jesuit row that also carries China's church to 1724** (AP2's option b). It cuts the
  China church in two at 1724. AP2's evidence (the 1726 ruling on Chinese priests) shows that
  church already had its own clergy.
- **(d) Stretch VI.11 to 1814.** It rewrites a frozen era 7 row across an era line.

**Recommendation: (b).** It keeps the single movement whole, as Mark asked, and it keeps every
local church its own. One home for the Rites controversy: **AP2**. Its subject is Chinese
practice and its deciders were Propaganda, the Holy Office and two popes (AP2, V (pass)). RV-1
names the Jesuit side in one line and links to AP2. ME-12 and LA8-2 become RV-1's lines. ME-8
keeps its Jesuit line (brokers of a union that made a separate church).

##### 1b. Propaganda Fide and the Missions Étrangères de Paris

- **Propaganda Fide** is a Roman congregation, an office of the papacy. It is a policy-maker, not a
  movement with carriers of its own. ME's note: it and the Capuchins brokered the unions of 1672,
  1698, 1724, 1778 and 1781, and each union made a separate living church.
- **MEP** is a society of secular priests, founded in 1658 (AP-X2; Launay 1894, V (pass)). By
  Mark's test it is one body "moving around the world" (Siam, Tonkin, Sichuan, Korea, Japan). But
  unlike the Jesuits, nothing in its story stands apart from the churches it served. No
  suppression, no reductions, no expulsion arc of its own.

**Options.** (a) Carrier lines only; (b) one MEP row, eras 8-9; (c) one "Propaganda missions" row.

**Recommendation: (a).** Propaganda gets named lines in VII.19 (the 1659 instruction to the vicars
apostolic and the Rites rulings, both V (pass) in the *Collectanea*) and VIII.29. MEP is named in
AP2, AP4, VIII.21 and VIII.45. Widen AF-6's named line in VIII.29 from Africa to the whole
nineteenth-century Catholic mission revival (Africa, Asia, Oceania), as AF-6 itself says it is
"one movement". MEP, the Lazarists and the restored Jesuits sit in that one line.

**Why the Jesuits get a row and MEP does not.** Both are worldwide. The test for a row is B3: the
Jesuits have a story between 1650 and 1814 that no row tells and that is not any local church's
(the reductions, the expulsions, survival in Russia). MEP has none that is not its fields' story.

##### 1c. VIII.7 and the three proposed wings

VIII.7's status text: "Its four named wings have fixed boundaries. Liberia sits inside its orbit,
while East Africa, Madagascar and Alaska each have an entry of their own." The row already has a
rule for regions outside its four wings: they get their own entries (VIII.42, VIII.43, VIII.47).

The three proposals are not one kind.
- **Southern Africa (AF-5).** Same kind as the four wings (mission churches among peoples new to
  the faith), but a whole region with its own span (1737-1906) and a settler church beside it
  (AF-4). VIII.7's rule points to its own entry. AF-4 already offers option (b), "Christianity at
  the Cape and in Southern Africa, 1652-1906", holding settler and mission churches together.
- **Arab Evangelicals (ME-11).** A different kind. These churches were made from converts out of
  the Maronite, Melkite and Orthodox churches, not out of other faiths. VIII.7's frame (Carey's
  Enquiry, 1792) is mission to the unevangelized. The Egypt mission (AF-9) is the same kind: its
  own history's chapter is on "friendly intercourse with the Christians of the Nile valley" (AF-9,
  Watson 1898, V (pass)).
- **Karen Baptists (AP9).** A people movement of a hill minority under the American Baptist
  mission. VIII.27 already holds that kind: its hill revivals list "American Baptist records (Naga
  hills, Assam)" and Myanmar is in its country list.

**One coherent proposal.**
1. VIII.7 stays at four wings. Its name and status text are not changed.
2. Southern Africa gets its own entry: either AF-5 as a row, or AF-4's one Cape row (settler and
   mission churches together). The Moravian Cape mission is a line in VII.4 before 1815 and in RV-5
   after it.
3. The Arab evangelical churches get one era 9 row, Syria-Lebanon and Egypt together (**RV-4**).
   The Armenian Evangelicals stay in VIII.32 and the Urmia work in VIII.40.
4. The Karen are a named line in VIII.27 (preferred), or held for a modern study as AP9 asks.

**Gate question (one for all three).** Where do mission churches outside VIII.7's four wings go?
- (a) New wings in VIII.7 (renames a frozen row; three change orders to one row).
- (b) VIII.7's own rule: own entries where a region or kind has row weight (Southern Africa, the
  Arab churches), named lines in the nearest row of the same kind where it does not (Karen in
  VIII.27).
- (c) Hold all three until AF-4 is ruled.
- **Recommended: (b).** It follows the row's own text, and it keeps unlike kinds apart.

##### 1d. The Moravian church after 1815

VII.4 ends at 1815. No era 9 or 10 row is Moravian. VIII.7, VIII.9 and VIII.35 name the Moravians
only as a model. VII.4's own legacy says most members are now "in Tanzania and the Caribbean". The
Moravians are exactly Mark's case: one movement across the world. Splitting them into Caribbean
lines (LA8-1) and African lines (AF-5, AF-9) is what his test warns against. **Recommendation:
RV-5**, one era 9 row continuing VII.4. LA8-1 keeps the Moravians as one of its churches by a
link; AF-5 and AF-9's Moravian lines move to VII.4 (before 1815) and RV-5 (after).

##### 1e. Duplicates and conflicting row homes

No body is proposed twice under two names. Six things have two homes and need one.

| Item | Homes proposed | One home |
|---|---|---|
| Chinese Rites controversy | AP2 (named line); LA8-2's Jesuit row | AP2; RV-1 links |
| Jesuits in Russia; Paraguay reductions | ME-12 (Jesuit home or VII.19); LA8-2 | RV-1 |
| Moravians, Cape and Cairo, Caribbean after 1815 | AF-5 (VII.4 line), AF-9 (VII.4 line), LA8-1 (inside a cross-church row), LA8-M | VII.4 before 1815; RV-5 after; LA8-1 links |
| Egypt's American Mission | AF-9 (line in VIII.13); ME-11 leaves Egypt out | RV-4 (VIII.13 keeps a link) |
| Catholic mission revival, nineteenth century | AF-6 (Africa only, line in VIII.29); AP-X2 (MEP lines) | One worldwide line in VIII.29 |
| Southern African mission churches | AF-5 (VIII.7 wing) and AF-4 option (b) | One Southern African entry (§1c) |

Joins the merge should carry as links, not new rows:
- ME-1 (Church of the East, 1650-1815) and AP1: Mar Gabriel, the East Syriac bishop who reached
  Malabar in 1708 (AP1, V (pass)).
- AP7 and VIII.40: the Chaldean bishops sent to Thrissur (1861, 1874; AP7, V (pass)).
- AP11 (Russian mission in Peking) and ME-18: both route Peking to Asia. Consistent.
- AF-1 and AF-2: the abun, one "in contact with" link.
- ME-9 (Hungarian Protestants) asks the rivers pass to check the Protestant river: no other pass
  proposes a Hungarian row, so there is no duplicate. RV-7 is the Unitarian side, which ME-9 does
  not hold.

---

#### 2. Gaps no region covered, river by river

| River | Checked | Roster carries | Result |
|---|---|---|---|
| Catholic | Jesuits after 1650 | VI.11 to 1650; VII.19 (object only) | **RV-1** |
| Catholic | Balkan Franciscans, Albanian and Bulgarian Catholics | nothing after V.20 (to 1463) | **RV-3** |
| Catholic | Propaganda, MEP | VII.19, VIII.29 (clauses) | lines (§1b) |
| Orthodox (Eastern) | Ecumenical Patriarchate under the Ottomans | VII.18 | carried |
| Orthodox (Eastern) | Greek autocephaly 1850; Bulgarian Exarchate 1870; Serbia | VIII.28 | carried |
| Orthodox (Eastern) | Peć 1766; Karlovci | VII.18 (both named) | carried; ME-17 for after 1815 |
| Orthodox (Eastern) | Kosmas the Aitolian | none | **RV-9** (hold) |
| Orthodox (Eastern) | Alaska | VII.21 (1794), VIII.47 (1824-1906) | carried |
| Orthodox (Eastern) | Siberia | VII.7 names Siberia for Old Believers only; VIII.31 the Altai | ME-18 lines; V source added below |
| Oriental Orthodox | Armenian Apostolic 1650-1906 | VII.24a, VIII.32 | carried; ME-14 line |
| Oriental Orthodox | Coptic-Ethiopian links | none before 1854 | AF-1 and AF-2 with one link |
| Eastern Catholic | Armenian Catholics | VII.24, VIII.32 ("alongside") | carried; ME-15 line; Mekhitarists after 1815 unnamed (a line in VIII.32) |
| Eastern Catholic | Bulgarian Greek Catholics 1860-61 | none | a line in RV-3 (or VIII.28) |
| Protestant | Mennonites and Hutterites in Russia | VI.3 to 1650; VIII.51 names the colonies as neighbors | **RV-2** |
| Protestant | Moravians after 1815 | VII.4 to 1815 | **RV-5** |
| Protestant | Arab and Egyptian evangelicals | none | **RV-4** |
| Protestant | Czech lands after 1627 | VI.24 `continuesAs` VII.4 (the hidden seed) | **RV-8** |
| Non-Nicene (lane 8) | Transylvanian Unitarians after 1650 | VI.14 to 1650 | **RV-7** (hold) |
| Independent, slave-born | Black churches' links to Africa | VIII.7 ("Liberia sits inside its orbit"); VII.16 (David George to Sierra Leone); VIII.1 names no African tie | **RV-6** |
| Syriac | Church of the East, Thomas Christians, Syriac Orthodox | ME-1, AP1, AP7, ME-7 | answered by passes; links in §1e |

**Siberia, source added.** R. W. Blackmore, translator's preface to A. N. Mouravieff, *A History of
the Church of Russia* (Oxford, 1842), `cic/texts/mouravieff_history-of-the-church-of-russia_blackmore1842.txt`,
lines ~215-224. **V.** He notes "the growing efficiency and marked success of their missions in
Siberia, and the Aleoutine Islands, in which last a new diocese has lately been founded, and the
pious and zealous missionary, Veniamineff ... has been appointed their first Bishop". An Anglican
outside witness. Supports ME-18's lines in VII.21 and VIII.31; no row.

---

##### RV-1. The Society of Jesus, 1650-1814: the reductions, the rites, the expulsions and the survival

- **Kind:** church body inside the Catholic Church (a religious order), the same kind as VI.11. As
  a Catholic order it clears the floor as VI.11 did; the four marks are not required.
- **Era:** 8. **Dates:** 1650 (VI.11's end) to 7 August 1814 (the restoration) [S on the day].
- **Region, countries, lane:** worldwide; Italy (Rome), Spain, Portugal, France, Paraguay,
  Argentina, Brazil, Bolivia, Mexico, China, India, Vietnam, Russia, Belarus (Polotsk) [S on the
  list]. Lane: Latin West & Catholicism.
- **Section A:** no question (Catholic).
- **B1:** good. Papal acts in the Library (1741, 1773, 1814, V); the *Collectanea* (V (pass));
  Muratori 1743 (V (pass)); Lettres édifiantes (V (pass)). Wanted: Dobrizhoffer (1784), the
  Pragmatic Sanction of 1767, a Polotsk source.
- **B2:** full. Colleges, missions, court science, rites, reductions, kings, a pope's suppression,
  a tsar's protection.
- **B3:** high. No row tells the order's own story after 1650.
- **B4:** Catholic and Jesuit readers; Latin American, Chinese and Indian Catholics; historians of
  mission and of the Enlightenment.
- **B5:** large; tiebreak only. **Tier:** 1.
- **Evidence:**
  1. Clement XIV, *Dominus ac Redemptor* (1773), Library file above, lines ~1190-1280. **V.**
  2. Pius VII, bull of restoration (1814), same file, lines ~140-158. **V.**
  3. Benedict XIV, *Immensa pastorum principis* (1741), in Mirbt 1911, no. 454. **V (pass).**
  4. Muratori, *Il cristianesimo felice* (1743). **V (pass).**
  5. Propaganda *Collectanea* I (1907), 1656 and 1726 entries. **V (pass).**
  6. Nilles 1885, the 1698 union act naming the Jesuits as brokers. **V (pass).**
  7. Studies wanted: a modern history of the suppression; John W. O'Malley's later surveys [S].
- **Living:** yes (the Society). No dated item after 2010 read; VI.11's own legacy names 2013.
- **Overlap:** VI.11 (before); VII.19 (Rome's side of 1759-1814); AP2 (the China church, the
  Rites' home); LA8-2 and ME-12 (become its lines); ME-8 (keeps its own line).
- **Recommendation:** enter.
- **Gate question G-RV-1:** see §1a. Recommended (b).

##### RV-2. Mennonites and Hutterites in the Russian Empire, 1789-1906

- **Kind:** church bodies (the Mennonite congregations and the Hutterite community) of the
  Anabaptist river. A church body, so the four marks are not required.
- **Era:** 9, with roots from 1789 (era 8). **Dates:** first settlers "anno 1788 oder 89" (Wiebe,
  V); emigration 1873-74 over military service (Wiebe, V).
- **Region, countries, lane:** East Europe; Ukraine (Chortitza, Molotschna), Russia (the Volga);
  for the Hutterites, Romania (Wallachia) and Ukraine (Vishenka). Lane: Protestant & Evangelical
  (the lane of VI.3).
- **Section A:** no question (the Dordrecht confession of 1632 is in the Library [S on which file
  holds it; the REGISTRY lists it]).
- **The river problem.** The Anabaptist river has no row at all after VI.3 (1650). The Dutch,
  Prussian and North American Mennonites lie in North Europe and North America, outside this
  sweep. By Mark's test the Mennonites moving from Prussia to Russia to America are one movement.
  The Russian colonies are the in-scope chapter of that one story.
- **B1:** moderate, with an own voice. **B2:** good (colonies, elders, schools, the 1860 Mennonite
  Brethren split [S], the conscription crisis). **B3:** high (no row). **B4:** Mennonite readers
  across the Americas; historians of Russia's colonists. **B5:** tiebreak only. **Tier:** 2 as a
  regional row; 1 as the chapter of an Anabaptist continuation row.
- **Evidence:**
  1. Gerhard Wiebe, *Ursachen und Geschichte der Auswanderung der Mennoniten aus Russland nach
     Amerika* (Winnipeg: Druckerei des Nordwesten, 1900), archive.org `P002546`, raw djvu, lines
     ~870-890. **V.** By the elder of the Bergthal congregation, an inside voice. The first went
     from Prussia "anno 1788 oder 89"; by 1790 eight villages; on 1 January 1856 the colony had
     18 villages and 8,651 souls; in the Molotschna colony 39 villages were settled from 1804 to
     1824, with 20,088 souls in 1860. Later chapters tell the 1872-74 deputations over
     "Wehrpflicht" (military service).
  2. Josef Beck, ed., *Die Geschichts-Bücher der Wiedertäufer in Oesterreich-Ungarn* (Vienna,
     1883), `cic/texts/hutterite-brethren_geschichts-buecher-oesterreich-ungarn-deu_beck1883.txt`,
     lines ~960-1005. **V** (the editor's preface, a study). The Hutterites in Hungary and
     Transylvania dissolved into the Catholic church by about 1757-1762; some families "zogen nach
     Wischenka in Russland"; refugees joined them in 1784; later they moved on, and a community
     stood in 1855 under a grandson of the last bishop. Beck also says Joseph II settled
     Mennonites in Galicia in 1784.
  3. Wanted: P. M. Friesen, *Die Alt-Evangelische Mennonitische Brüderschaft in Russland
     (1789-1910)* (1911) [S]; the 1800 charter of privileges [S].
- **Living:** yes (Mennonite and Hutterite churches) [S]; no dated item read.
- **Overlap:** VI.3 (to 1650); VIII.51 (names the colonies only as the Stundists' neighbors); VII.16
  and VII.3 name Mennonites in passing.
- **Recommendation:** enter as a chapter of one Anabaptist continuation row, 1650-1906 (owner of
  the North Europe river to supply the rest), or as a regional row if Mark wants only the in-scope
  part now.
- **Gate question G-RV-2:** (a) one Anabaptist continuation row, 1650-1906, with the Russian
  colonies and the Hutterites as named chapters; (b) a Russian Mennonite row, 1789-1906, alone;
  (c) a named line in VIII.51. **Recommended: (a)**, by Mark's test; log the non-Russian part for a
  North Europe pass. (c) mislabels it: the Mennonites were the Stundists' neighbors, not their
  church.

##### RV-3. Catholics of the Ottoman Balkans: the Bosnian Franciscans, Albanian and Bulgarian Catholics, 1650-1878

- **Kind:** church body (the Catholic communities of Bosnia, Herzegovina, Slavonia, Albania and
  Bulgaria under Ottoman rule, served above all by the friars of the Bosnian province).
- **Era:** 8 and 9. **Dates:** 1650 to 1878 (Austria-Hungary takes Bosnia) [S on the end year];
  the Bulgarian union movement of 1860-61 inside it.
- **Region, countries, lane:** Mediterranean / Asia Minor (as VII.18); Bosnia and Herzegovina,
  Croatia (Slavonia), Albania, Bulgaria. Lane: Latin West & Catholicism.
- **Section A:** no question (Catholic).
- **Mark's test.** The Franciscans are a worldwide order, but this is not their worldwide story. The
  friars of "Bosna Argentina" were the parish clergy of one people under one empire. The church
  they served is the subject. Unique.
- **B1:** moderate, Library-held. **B2:** good (friaries, parishes, jurisdiction fights with
  bishops, Ottoman and Habsburg rule, schools). **B3:** high: no row names Bosnia after V.20 (to 1463).
  **B4:** Croatian, Bosnian and Albanian Catholics; historians of the Ottoman Balkans. **B5:**
  small. **Tier:** 2.
- **Evidence:**
  1. Fermendžin, *Acta Bosnae potissimum ecclesiastica* (Zagreb, 1892),
     `cic/texts/fermendzin_acta-bosnae-potissimum-ecclesiastica-lat_fermendzin1892.txt`. **V.**
     Regest MCCCCLX (Požega, 1 January 1689), lines ~24876-24900: the fathers of the Bosnian
     province, met at Požega, declare for clergy and people that no bishop but the bishop of Bosnia
     had ruled the church between the Sava and the Drava "a centum septuaginta annis" (for 170
     years). Regest MCCCCXCIV (Vienna, 5 July 1746), line ~25822: Franjo Ivanović, "minister
     provincialis Bosnae argentinae", asks for testimonies to defend the province's rights to its
     Slavonian parishes. Roman and Franciscan record; the volume ends at 1752.
  2. Arthur J. Evans, *Through Bosnia and the Herzegovina on Foot* (London, 1877),
     `cic/texts/evans_through-bosnia-and-the-herzegovina-on-foot_1877.txt`, lines ~4458-4470 and
     ~9243. **V.** In 1875 the Catholics' children went to school "under the Franciscan priest"
     (Evans quoting "a recent observer"); he stays at the Franciscan monastery of Gučja Gora.
     Outside witness, openly critical of all the clergy.
  3. J. Lins, "Bulgaria", *Catholic Encyclopedia* vol. 3 (1908), newadvent.org/cathen/03046a.htm,
     raw HTML. **V** (study). On 30 December 1860, 120 deputies petitioned the apostolic delegate for
     union with Rome; "Pius IX himself, 21 January, 1861, consecrated a priest named [Sokolski] its
     first Vicar Apostolic of Uniat Bulgaria"; Sokolski "embarked for Odessa on a Russian vessel"
     in June 1861; most went over to the Exarchate. A Catholic study.
  4. Wanted: the Albanian council of 1703 (*Concilium Albanum*) [S]; a Bosnian Franciscan chronicle
     in Croatian (for example the Fojnica or Sutjeska chronicles) [S]; a non-Catholic study.
- **Living:** yes (the Franciscan province and the Catholic Church in Bosnia) [S].
- **Overlap:** VII.18 and VIII.28 (the Orthodox side); VII.19 (Rome); V.20, the Bosnian Church (c. 1230s-1463, era 6)
  (a different body). None carries these Catholics.
- **Recommendation:** enter the era 8 part on the V items; the era 9 part after one more source.
  The Bulgarian union of 1860-61 is a named line here, or in VIII.28 beside the Exarchate.
- **Gate question G-RV-3:** (a) one row, 1650-1878; (b) a named line in VII.19 and VIII.29; (c) hold
  for a Croatian-language source. **Recommended: (a)**; (b) would tell a local church as Rome's
  story, the error Mark's test guards against in reverse.

##### RV-4. The Arab evangelical churches: Syria, Lebanon and Egypt, 1823-1906

- **Kind:** church bodies (the evangelical churches of Syria-Lebanon and of Egypt, with the missions
  that planted them). **Merges ME-11 and the Egypt part of AF-9.**
- **Era:** 9. **Dates:** arrival at Beirut 10 July 1823; first native evangelical church at Beirut
  1848; American (United Presbyterian) mission in Egypt from 1854; Arabic Bible completed 10 March
  1865 (all ME-11 and AF-9, V (pass), except Egypt's synod date [S]).
- **Region, countries, lane:** Middle East and Africa; Lebanon, Syria, Egypt. Lane: Protestant &
  Evangelical.
- **Section A:** no question (Reformed).
- **Why one row.** Both are Arabic-speaking Protestant churches made from Eastern Christian converts.
  They share one Bible (the Smith-Van Dyck translation). Neither is VIII.7's kind (§1c).
- **B1:** moderate; mission-weighted (Jessup 1910, Watson 1898, both V (pass)). Wanted: an Arabic
  own voice (Bustānī) and Anderson 1872. **B2:** good. **B3:** high: no row carries Arab
  Protestants. **B4:** Arab Christians, evangelicals. **B5:** small. **Tier:** 2.
- **Evidence:** ME-11's and AF-9's lists. No new item opened in this run.
- **Living:** yes [S] (National Evangelical Synod of Syria and Lebanon; the Evangelical Church of
  Egypt). No dated item read.
- **Overlap:** VIII.32 (Armenian Evangelicals stay there); VIII.40 (Urmia stays there); VIII.13 (the
  Coptic church the Egyptian converts left; a link).
- **Recommendation:** enter, if Mark takes §1c option (b).
- **Gate question G-RV-4:** (a) one row for Syria-Lebanon and Egypt; (b) ME-11 as a row and Egypt as
  a line in VIII.13 (AF-9); (c) a fifth wing in VIII.7. **Recommended: (a).**

##### RV-5. The Moravian Church, 1815-1906

- **Kind:** church body (the Unity of the Brethren), continuing VII.4.
- **Era:** 9. **Dates:** 1815 to 1906.
- **Region, countries, lane:** worldwide; Germany (Herrnhut), the Caribbean (Jamaica, Antigua, the
  Danish islands), Suriname, South Africa, Tanzania (from 1891 [S on the year]), Labrador,
  Greenland, Nicaragua, Ladakh [S on the list]. Lane: Protestant & Evangelical.
- **Section A:** no question (VII.4's floor).
- **B1:** good, inside-voiced. **B2:** full. **B3:** high: the church most of whose members are now
  in Tanzania and the Caribbean has no row after 1815. **B4:** Moravians worldwide; Caribbean and
  Tanzanian Christians. **B5:** moderate. **Tier:** 1.
- **Evidence:**
  1. J. Taylor Hamilton, *A History of the Missions of the Moravian Church during the Eighteenth
     and Nineteenth Centuries* (Bethlehem, Pa.: Times Publishing Co., 1901), archive.org
     `historyofmission00hami`, raw djvu. **V.** The preface calls the author "a member of the
     Executive Board of the Moravian Church, North" (an inside voice). Lines ~5395-5402:
     "Emancipation Day, August 1, 1834", spent by "the liberated multitudes" in thronged churches.
     Lines ~9783-9806: on 7 February 1897 at Rungwe, by Lake Nyasa, a woman named Fiabarema rose
     after the sermon and said, "I have risen to say that I belong to God"; she was baptized that
     evening. Within nine years four stations were manned in the Nyasa country.
  2. The Library holds the Moravian *Periodical Accounts* vol. 1 (1790) and Oldendorp (1777), both
     before 1815; nothing after 1815 is vendored. Hamilton 1901 is a vendoring candidate.
- **Living:** yes [S]; no dated item read.
- **Overlap:** VII.4 (before); LA8-1 (the Caribbean churches; Moravians as one of them, by link);
  AF-5 and AF-9 (their Moravian lines move here after 1815); VIII.7 (names the Moravians as model).
- **Recommendation:** enter.
- **Gate question G-RV-5:** (a) one era 9 row continuing VII.4; (b) Caribbean lines in LA8-1 and
  African lines in the Africa rows; (c) log in Open-Gaps 142 for later. **Recommended: (a)**, by
  Mark's test; (b) splits one movement by place.

##### RV-6. Liberia's settler churches and the Black Atlantic links, 1792-1906

- **Kind:** church bodies (the churches Black American and Nova Scotian settlers carried to Sierra
  Leone and Liberia). Not a new row.
- **Era:** 8-9. **Region:** Africa and North America; Liberia, Sierra Leone, United States.
  **Lane:** Protestant & Evangelical.
- **What is missing.** VIII.7 says "Liberia sits inside its orbit" but its text never names Liberia
  or the settlers' own church. VIII.1 (the Black Church in America) names no African tie at all.
  VII.16 carries David George to Sierra Leone (1792).
- **Section A:** no question (Baptist, Methodist).
- **Evidence:**
  1. J. B. Taylor, *Biography of Elder Lott Cary, Late Missionary to Africa* (Baltimore, 1837),
     archive.org `biographyofelder00tay`, raw djvu. **V.** Cary's letter from "Free Town, March 13th,
     1821": "Before we left the United States, we formed ourselves into a church, consisting of
     seven members." His letter from "Monrovia, August 16th, 1823": "Our little church has been
     wonderfully blessed of late. I baptized two yesterday". Cary's own words, in a white Richmond
     pastor's book.
  2. The AME church's tie to South Africa's Ethiopian Church (1896) [S]; Daniel Coker (1820) [S].
- **B1-B5, tier:** a named line; Tier 3.
- **Living:** yes [S] (Providence Baptist Church, Monrovia [S]).
- **Overlap:** VIII.7 (West Africa wing); VII.16; VIII.1; IX.4.
- **Recommendation:** a named line in VIII.7's West Africa wing ("Liberia's settler church"), with
  links VIII.1 → VIII.7 ("gave rise to" or "in contact with") and, once sourced, VIII.1 → IX.4.
- **Gate question G-RV-6:** (a) named line and links; (b) a row for the Black Atlantic return
  churches; (c) nothing. **Recommended: (a).** The row weight sits in VIII.1 and VIII.7 already.

##### RV-7. The Transylvanian Unitarians after the Polish exile, 1660-1906 (hold)

- **Kind:** church body (the Unitarian Church of Transylvania, with the Polish Brethren exiles).
- **Era:** 8-9. **Region:** East Europe; Romania (Transylvania), Hungary. **Lane:** Non-Nicene
  Traditions (lane 8), as VI.14, VII.27 and VIII.37.
- **Section A:** a floor question (anti-trinitarian). The roster already enters VI.14 and the
  American Unitarian rows in lane 8, so there is precedent.
- **Evidence:**
  1. Thomas Rees, historical introduction to *The Racovian Catechism* (London, 1818),
     `cic/texts/racovian-catechism_racovian-catechism_rees1818.txt`, lines ~1842-2000. **V** (a
     Unitarian study). At the Diet of Warsaw in 1658 a decree passed against the Polish Unitarians;
     of the exiles "about four hundred proceeded to Transylvania and Hungary"; "Thus was terminated
     the public profession of Unitarianism in the kingdom of Poland".
  2. Wanted: a Transylvanian Unitarian source for 1660-1906 in Hungarian or Latin.
- **B3:** high (VI.14 ends at 1650). **Tier:** 3 now, for want of in-window sources.
- **Living:** yes [S] (the Hungarian Unitarian Church).
- **Recommendation:** hold for sources; then a lane 8 row, or a named line closing VI.14.
- **Gate question G-RV-7:** (a) hold; (b) a lane 8 row now on Rees alone; (c) out of scope.
  **Recommended: (a).**

##### RV-8. The Czech lands after 1627: the hidden Protestants and the Toleration Patent of 1781

- **Kind:** church bodies (the hidden Brethren and Utraquist heirs; from 1781 the Lutheran and
  Reformed "toleration" congregations of Bohemia and Moravia).
- **Era:** 8-9. **Region:** North Europe (as the roster tags VI.24). **Lane:** Protestant &
  Evangelical.
- **What the roster carries.** VI.24 ends c. 1627 and `continuesAs` VII.4. VII.4 tells the hidden
  Unity in its own words ("survived in hiding for nearly a century"). So the Herrnhut branch is
  carried. The Protestants who stayed in Bohemia and Moravia, and the churches of 1781, are not.
- **Evidence:** Count Lützow, *Bohemia: An Historical Sketch* (1920),
  `cic/texts/lutzow_bohemia-historical-sketch_1920.txt`, lines ~17181-17196. **V** (study). In
  1781 Joseph II's "decree of tolerance" granted freedom to the "Helvetic and Augsburg Confessions",
  excluding "even the unity of the Bohemian Brethren"; "the people of Bohemia — many of whom had
  secretly remained Protestants — were very grateful".
- **Tier:** 2-3. **Living:** yes [S] (the Evangelical Church of Czech Brethren, 1918, is era 10).
- **Recommendation:** a named line in VII.4 for the hidden Unity before 1722 (it already tells it);
  the Toleration churches of 1781-1906 go to a North Europe pass, since this sweep's scope excludes
  North Europe except as a link.
- **Gate question G-RV-8:** (a) VII.4 line now, the rest logged; (b) a Czech Protestant row,
  1627-1906, now; (c) log only. **Recommended: (a).**

##### RV-9. Kosmas the Aitolian (1714-1779) (hold)

- **Kind:** a person and his preaching mission (an itinerant Athonite monk who founded schools
  across Epirus, Albania and Macedonia; killed 1779 [S on all details]). Not a movement by the four
  marks on present evidence.
- **Era:** 8. **Region:** Greece, Albania. **Lane:** Greek East & Orthodoxy.
- **Evidence:** nothing in the Library. archive.org holds only modern studies: Constantine
  Cavarnos, *St. Cosmas Aitolos* (1971), item `stcosmasaitolosg0000cava`. **V-s** (search record
  only). No pre-1930 text found raw.
- **Overlap:** VII.18 (neomartyrs, the patriarchate); VIII.12 (the Kollyvades, a related Athonite
  current [S on the tie]).
- **Recommendation:** hold; then a named line in VII.18.
- **Gate question G-RV-9:** (a) hold, then a VII.18 line; (b) a VIII.12 line; (c) nothing.
  **Recommended: (a).**

---

#### 3. The logged timeline breaks in 1650-1906

| Break | Answered by | Status |
|---|---|---|
| Ethiopian church 1650-1855 (142) | AF-1 | answered |
| Coptic church to 1854 (142) | AF-2 (finds the gap starts c. 1300) | answered |
| Church of the East 1650-1815 (142) | ME-1 | answered |
| St Thomas Christians 1665-1815 (142) | AP1 | answered |
| China 1650-1793 and the Rites (142) | AP2; RV-1 for the Jesuit side | answered |
| Japan's hidden Christians 1650-1865 (142) | AP3 | answered |
| Maronites 1517-1900 (142) | ME-2 | answered (1517-1650 to the era 7 owner) |
| Georgian church after 1245 (142) | ME-3, plus a VIII.31 line | answered for 1650-1906 |
| Latin America thin (142) | the LA pass | answered |
| Melkites 1009-1724 (135) | ME-4 / VII.23 line | answered for 1650-1724 |
| Syriac Orthodox after 1300 (135) | ME-7 | answered: still held |
| Old Believers after 1815 (135) | ME-5 | answered |
| **Scottish church after 1650 (135)** | none | **not answered** (North Europe; no pass's region) |
| **Swedenborgian New Church after 1815 (135)** | none | **not answered** (North Europe and North America) |
| Armenian 1441-1517; Galicia 1906-1946; English and Scandinavian medieval (135, 142) | — | outside 1650-1906 |

Found by passes, not logged: the Moravians after 1815 (LA pass; RV-5 here).

---


## 8. Gate questions for Mark

Numbered G89-1 to G89-55. The six cross-cutting questions come first, because many candidate questions depend on them. Then one question per counted candidate, by pass: the regional passes in their own ranked order, and the rivers candidates in ID order. A candidate whose answer a cross-cutting question already gives has no question of its own, and its entry says so. The options and recommendations are the passes' own, with the rivers pass's resolutions applied; where a recommendation is the merge's, it says so. Each recommendation matches the class in section 2. Every addition is a change order to a frozen era (G89-6).

### Cross-cutting

- **G89-1. A Society of Jesus row for era 8 (RV-1; LA8-2, ME-12, AP-X1; the Rites in AP2).** VI.11, the order as one movement, ends at 1650. VII.19 tells the Jesuits only from Rome's side, and VIII.29 does not name them. Latin America wanted a Jesuit row (LA8-2), the Middle East allowed one (ME-12), and Asia leaned against one (AP-X1). (a) No Jesuit row; lines in VII.19 and in local rows. (b) Enter RV-1 as a new row, 1650-1814, continuing VI.11: the reductions, the Jesuit side of the court mission, the expulsions of 1759-67, Russia from 1773 and the restoration. The China church (AP2), Japan's hidden Christians (AP3) and the Romanian union (ME-8) stay their own rows, linked to it. (c) A Jesuit row that also carries China's church to 1724 (cuts the China church in two). (d) Stretch VI.11 to 1814 (rewrites a frozen era 7 row across an era line). **Rec. (b)** It keeps the single movement whole, as Mark asked, and keeps every local church its own. The Rites controversy has one home, AP2; RV-1 names the Jesuit side in one line and links to it. LA8-2 and ME-12 become RV-1's lines. Tied to G89-23 (AP2) and G89-49 (RV-2, the same "one movement" test).
- **G89-2. Propaganda Fide and the Missions Étrangères de Paris (AP-X2; AF-6; Middle East note 2).** (a) Carrier lines only: Propaganda as named lines in VII.19 (the 1659 instruction to the vicars apostolic, the Rites rulings) and VIII.29; MEP named in AP2, AP4, VIII.21 and VIII.45; AF-6's line in VIII.29 widened to the whole nineteenth-century Catholic mission revival, with MEP, the Lazarists and the restored Jesuits in it. (b) One MEP row, eras 8-9. (c) One "Propaganda missions" row. **Rec. (a)** Propaganda is a Roman office, not a movement with carriers of its own. MEP is worldwide, but none of its story stands apart from the churches it served. The Jesuits get a row and MEP does not by B3: only the Jesuits have a 1650-1814 story no row tells. Tied to G89-1 and G89-10 (AF-6).
- **G89-3. Mission churches outside VIII.7's four wings (AF-5, ME-11 and RV-4, AP9).** VIII.7's status text says its "four named wings have fixed boundaries" and sends other regions to their own entries. Three passes proposed additions to it: Southern Africa (AF-5), the Arab evangelicals (ME-11) and the Karen (AP9). (a) New wings in VIII.7 (renames a frozen row; three change orders to one row). (b) VIII.7's own rule: own entries where a region or kind has row weight (Southern Africa; the Arab churches as RV-4), and named lines in the nearest row of the same kind where it does not (the Karen in VIII.27). (c) Hold all three until AF-4 is ruled. **Rec. (b)** It follows the row's own text and keeps unlike kinds apart: the Arab churches were made from Eastern Christian converts, not converts from other faiths. VIII.7's name and status text do not change. Tied to G89-5, G89-31 (AP9) and G89-50 (RV-4).
- **G89-4. The Moravian church after 1815 (RV-5; LA8-M; the Moravian lines in AF-5 and AF-9).** VII.4 ends at 1815, and no era 9 or 10 row is Moravian. (a) Enter RV-5 as one era 9 row continuing VII.4, with the Caribbean, the Cape, Suriname, Labrador and Nyasa as its lines; LA8-1 keeps the Moravians by a link; the Cape and Cairo lines sit in VII.4 before 1815. (b) Caribbean lines in LA8-1 and African lines in the Africa rows. (c) Log it in Open-Gaps 142 for later (Latin America's own recommendation). **Rec. (a)** By Mark's test: one movement across the world, which (b) would split by place. Tied to G89-14 (LA8-1) and G89-5.
- **G89-5. The home of Southern Africa (AF-4, AF-5).** Southern Africa has no row before 1960 except IX.4's Ethiopian Church (1892). Under G89-3(b) the mission churches get their own entry, not a VIII.7 wing. (a) Two rows: the Dutch Reformed Church at the Cape, 1652-1906 (AF-4), and the Southern African mission churches, 1737-1906 (AF-5's option b). (b) One row, "Christianity at the Cape and in Southern Africa, 1652-1906", holding settler and mission churches together (AF-4's option b). (c) The Dutch Reformed row only; the mission churches held. **Rec. (a)** This is the merge's reading. The rivers pass left (a) and (b) open. The Africa pass kept the settler church and the mission churches apart (its G-AF89-4 recommended two homes), and (a) keeps that once the VIII.7 wing is ruled out. (b) is defensible if Mark wants one Southern African story. The Moravian Cape mission is a VII.4 line before 1815 and an RV-5 line after, whichever is chosen. Tied to G89-3 and G89-4.
- **G89-6. How the frozen-era additions are handled.** Eras 8 and 9 are frozen. Every new row, named line, link and field change admitted at this gate is a change order. Several touch settled rows: VIII.48's start (LA8-5), VII.17's text and countries (LA8-4), VIII.29's lines (AF-6, G89-2), VII.4's and VII.19's lines. (a) Name each admitted item as its own change order in one register, draft them together, review them together under the three-round cap, and ship them in one data release. (b) One change order, review and data release per region. (c) Admit new rows now, and hold every change to an existing frozen row's fields for a later pass. **Rec. (a)** This recommendation is the merge's; Mark's call. It keeps each change named and reasoned, as a change order must be, while paying for one review cycle and one release, as CLAUDE.md asks of related slices. (c) would split linked work: RV-1 needs lines in VII.19, and AF-1 needs links to VI.25 and VIII.49.

### Africa

- **G89-7. The Ethiopian church, 1650-1855 (AF-1).** (a) A new row between VI.25 and VIII.49 (`continuesAs` chain VI.25 to the new row to VIII.49). (b) Stretch VI.25 to 1769 and VIII.49 back to 1769 (both frozen rows change dates and text). (c) Hold until Guidi's annals or Weld Blundell can be read. **Rec. (a)** One coherent period with its own name in the scholarship; draft only from V items, and add Guidi to the wanted list. An "in contact with" link to AF-2 for the abun. Tied to G89-8.
- **G89-8. Where the Coptic row starts (AF-2).** (a) 1517, as logged. (b) 1650, the era line. (c) c. 1300, where IV.26 ends. **Rec. (a)** With 1300-1517 logged as its own break for the era 6 owner. Archons and Coptic Catholics as named lines (G89-11). The Egypt mission goes to RV-4 (G89-50). Tied to G89-7.
- **G89-9. The Kongo gap (AF-3).** (a) A new row, 1650-1880s, with VII.11 inside its span. (b) Extend VI.13a to 1720 and log the rest. (c) Log it in Open-Gaps only. **Rec. (a)**, else (b).
- **G89-10. The Catholic mission revival (AF-6).** (a) A named line in VIII.29, widened to the worldwide revival under G89-2, plus a "gave rise to" edge from VIII.29 to IX.59. (b) A new era 9 row, "The Catholic Church in Africa, 1830-1906", as IX.59's predecessor. (c) Extend IX.59 back to about 1867. **Rec. (a)** It passes Mark's test only as part of the worldwide Catholic movement. (b) is defensible later if the region's Catholic story outgrows a line. Tied to G89-2.
- **G89-11. The Coptic Catholics and the Ge'ez-rite Catholics (AF-7).** (a) Named lines in AF-2 and in AF-1 / VIII.49. (b) One Eastern Catholic row for Africa, on the VII.23 model. (c) Hold. **Rec. (a)** Tied to G89-7 and G89-8.
- **G89-12. West Africa before the mission societies (AF-8).** (a) Hold all as named lines (Quaque in VII.20, Freetown in VII.16) until a pre-1930 source is read; Capitein waits on AF-4 or a Dutch line. (b) A West African era 8 row. (c) Out of scope. **Rec. (a)**
- **G89-13. Protestant missions in Egypt and Ethiopia (AF-9).** (a) Named lines: the Moravians in Cairo and Algiers in VII.4; the CMS and the Swedish mission in AF-1, VIII.49 and IX.20. The Egypt mission moves to RV-4 under G89-50 (rivers), with a link from VIII.13. (b) An "Evangelical Church of Egypt" row from 1854. (c) Out of scope. **Rec. (a)**, as re-homed. Tied to G89-3 and G89-50.

AF-4 and AF-5 are answered by G89-5.

### Latin America and the Caribbean

- **G89-14. The Caribbean churches of slavery and emancipation (LA8-1).** (a) One regional cross-church row, 1815-1906, with the Native Baptists and the 1860-61 revival as lines. (b) Lines in VIII.35 and VIII.34. (c) A Jamaica-only row. **Rec. (a)** Under G89-4 the Moravians are RV-5's lines, linked from this row.
- **G89-15. Canudos (LA8-3).** (a) Its own movement row, with Juazeiro and Tomóchic as lines in VIII.48. (b) A line in VIII.48. (c) A family row of 1890s holy towns. **Rec. (a)** It meets the four marks; Juazeiro and Tomóchic are not tied to it.
- **G89-16. Colonial Brazil (LA8-4).** (a) A named strand in VII.17 by change order (Brazil added to its text, voices, place and countries). (b) Its own row, 1650-1822. (c) Leave it. **Rec. (a)** VII.17's name and sources already claim Brazil. Tied to G89-6 and to the flag on VII.17's countries (section 10).
- **G89-17. Hidalgo and Morelos (LA8-5).** (a) Move VIII.48's start to 1810 and add the line. (b) The line, keeping 1815. (c) Extend VII.17 to 1815. **Rec. (a)** Tied to G89-6.
- **G89-18. Haiti before 1804 and after 1860 (LA8-6).** (a) Hold for sources. (b) Extend VIII.46 to 1906 now. (c) Nothing. **Rec. (a)**
- **G89-19. Protestant beginnings (LA8-7).** (a) Lines in VIII.41 (Brazil's Lutherans) and a pre-1916 line in IX.63. (b) An era 9 row. (c) Nothing. **Rec. (a)**
- **G89-20. Cuba and Puerto Rico under Spain (LA8-8).** (a) Hold, then a line in VIII.48. (b) Nothing. **Rec. (a)**
- **G89-21. The Bethlemites (LA8-9).** (a) Hold, then a line in VII.17. (b) Nothing. **Rec. (a)**
- **G89-22. Cancuc and the Talking Cross (LA8-10).** (a) Hold both. (b) A Cancuc line in VII.17 now. (c) Nothing. **Rec. (a)** The Talking Cross raises a real Section A question.

LA8-2 is answered by G89-1, and LA8-M by G89-4.

### Asia and the Pacific

- **G89-23. China's Catholic story, 1650-1906 (AP2).** (a) A China-church row, 1650-1906 (or two segments), with the Jesuit court mission and the Rites as named lines. (b) An era 8 continuation of VI.11 plus a smaller China row from 1724. (c) A named line in VII.19. **Rec. (a)** The era 9 half enters after one verified era 9 source. AP2 is the one home of the Rites; MEP is named as a carrier (G89-2). Tied to G89-1.
- **G89-24. The St Thomas Christians, 1665-1815 (AP1).** (a) One era 8 row, both parties. (b) Extend VI.18 to 1815. (c) Two rows, one per party. **Rec. (a)** With a link to ME-1 for Mar Gabriel, the East Syriac bishop who reached Malabar in 1708. Tied to G89-29 and G89-43.
- **G89-25. Vietnam's Catholics (AP4).** (a) One row, 1650-1906. (b) Two segments, split at 1815. (c) A line in an MEP row. **Rec. (b)** (c) falls away under G89-2.
- **G89-26. Japan's hidden centuries (AP3).** (a) One row, 1650-1865. (b) Extend VIII.45 back. (c) Extend VI.13b forward. **Rec. (a)**
- **G89-27. The VOC-era Protestant churches (AP5).** (a) An era 8 row. (b) A line in VIII.26. (c) Hold. **Rec. (a)**
- **G89-28. South Asian Latin Catholicism (AP6).** (a) A Ceylon row, 1658-1806. (b) A wider Padroado and Propaganda South Asia row, 1650-1906, with Ceylon as its first line. (c) Hold. **Rec.** Asia's own: (b) if one telling is wanted; (a) is better evidenced. Both enter a row, as section 2 classes it; Mark chooses the shape.
- **G89-29. The Catholic half of the St Thomas Christians in era 9 (AP7).** (a) Extend AP1 to 1906. (b) A line in VIII.27. (c) Hold. **Rec. (c)**, then (a). A link to VIII.40 for the Chaldean bishops sent to Thrissur (1861, 1874). Tied to G89-24.
- **G89-30. The Māori prophetic churches (AP13).** (a) An era 9 movement row (beyond-floor register). (b) A line in IX.26, which starts in 1925. (c) Hold. **Rec. (c)**, with (a) as the target once a Māori-language or Māori-authored source is read.
- **G89-31. The Karen Baptists (AP9).** (a) A named line in VIII.27, whose hill revivals already hold this kind (rivers). (b) A named line in VIII.7 (Asia's own recommendation). (c) Its own row. (d) Hold for a modern study. **Rec. (a)**, with one modern study added before drafting, as Asia asked. Tied to G89-3.
- **G89-32. The Tamil Lutheran church (AP8).** (a) A line in VII.2. (b) Its own row. (c) Treat it as carried. **Rec. (a)**
- **G89-33. The Cofradía de San José (AP10).** (a) A line in VIII.39. (b) Hold. **Rec. (b)**, then (a) once a dated primary is read.
- **G89-34. Korea, 1884-1906 (AP15).** (a) Named lines. (b) Hold. **Rec. (b)**, then (a).
- **G89-35. Colonial Australia and New Zealand (AP12).** (a) Lines in the parent rows (VIII.29, VIII.30, VIII.34). (b) An Australasia row. (c) Hold. **Rec. (c)**, then (a).
- **G89-36. The Orthodox of Peking (AP11).** (a) A line in VII.21 / VIII.31. (b) Hold. **Rec. (b)**
- **G89-37. The Pacific Christian kingdoms (AP14).** (a) Leave them in VIII.7. (b) Split a Pacific row out of VIII.7 (a change order on a frozen row). **Rec. (a)**

AP-X1 is answered by G89-1, and AP-X2 by G89-2.

### Middle East, Caucasus, Russia and Eastern Europe

- **G89-38. The Old Believers after 1815 (ME-5).** (a) An era 9 row, 1815-1906, continued from VII.7. (b) Hold for a Russian own-voice text. (c) A named line in VIII.31. **Rec. (a)**
- **G89-39. The Maronites (ME-2).** (a) One row per era (8 and 9); 1517-1650 to the era 7 owner. (b) One long row, 1517-1900. (c) Era 9 now; eras 7 and 8 held. **Rec. (a)** The era 9 row enters now; the era 8 row after the 1736 synod acts are opened.
- **G89-40. Polish and Lithuanian Catholicism (ME-10).** (a) An era 9 row, 1815-1906, parent of IX.70. (b) Also an era 8 row, 1650-1815. (c) Named lines in VIII.29 only. **Rec. (a)**
- **G89-41. The Romanian Greek Catholic Church (ME-8).** (a) An era 8 row, and an era 9 row or named line, linked to IX.73. (b) One composite row for the Greek Catholics of the Hungarian crown. (c) A named line in VII.19 only. **Rec. (a)** It keeps its own Jesuit line (the brokers of the 1698 union), under G89-1.
- **G89-42. The two Melkite churches (ME-4).** (a) One era 9 row for both churches. (b) The Catholic row now, the Orthodox side held. (c) Extend VII.23 to 1906. **Rec. (a)** With Macarius III and Euthymius as a named line in VII.23; 1009-1650 stays held.
- **G89-43. The Church of the East, 1650-1815 (ME-1).** (a) A new era 8 row between VI.30 and VIII.40. (b) Extend VIII.40 back to 1672/1681. (c) Hold for Assemani III and Malech. **Rec. (a)** With a link to AP1 (Mar Gabriel). Tied to G89-24.
- **G89-44. The Georgian church (ME-3).** (a) An era 8 row, with the Exarchate as a named line in VIII.31. (b) An era 8 row and an era 9 Exarchate row. (c) Hold for a Georgian-language source. **Rec. (a)**
- **G89-45. Hungarian and Transylvanian Protestantism (ME-9).** (a) An era 8 row, and an era 9 row later. (b) Named lines in the Reformed and Lutheran rows. (c) Leave it to the rivers pass. **Rec. (a)** The rivers pass found no duplicate; the Unitarian side is RV-7 (G89-53).
- **G89-46. The spiritual Christians (ME-6).** (a) Assess each body under Section A, then an era 9 row for what clears. (b) One lane 8 row for the family. (c) Out of scope; a note in VIII.51. **Rec. (a)**
- **G89-47. The Syriac Orthodox and Syriac Catholics (ME-7).** (a) Hold with a named want, then an era 9 row. (b) An era 9 row now, on Badger and Fortescue. (c) A named line in IX.19 only. **Rec. (a)** Both sources opened are outsiders.
- **G89-48. The Middle East pass's named lines and routings (ME-13 to ME-21).** The pass gave each a recommendation but no gate question. (a) Take each as the pass recommends: named lines for ME-13 (VII.18 into VIII.28), ME-14 and ME-15 (VIII.32), ME-17 (VII.18, VIII.28), ME-18 (VII.21, VIII.31, now with the rivers pass's V source) and ME-19 (VIII.40); ME-16 and ME-21 held; ME-20 out of scope under A1 unless Mark wants a lane 8 entry. (b) Hold them all for sources. (c) Leave them out. **Rec. (a)** This grouped question is the merge's; Mark can rule any item apart.

ME-11 is answered by G89-50 (RV-4), ME-12 by G89-1, and ME-22 by G89-49 (RV-2).

### Rivers cross-check

- **G89-49. Mennonites and Hutterites in the Russian Empire (RV-2; ME-22).** (a) One Anabaptist continuation row, 1650-1906, with the Russian colonies and the Hutterites as named chapters; the non-Russian part logged for a North Europe pass. (b) A Russian Mennonite row, 1789-1906, alone. (c) A named line in VIII.51. **Rec. (a)**, by Mark's test (one movement from Prussia to Russia to America). (c) mislabels it: the Mennonites were the Stundists' neighbors, not their church. Tied to G89-1.
- **G89-50. The Arab evangelical churches (RV-4; ME-11; AF-9's Egypt line).** (a) One row for Syria-Lebanon and Egypt, 1823-1906. (b) ME-11 as a row, and Egypt as a line in VIII.13 (AF-9). (c) A fifth wing in VIII.7. **Rec. (a)**, if G89-3 takes (b). The two churches share one Arabic Bible and were both made from Eastern Christian converts. The Armenian Evangelicals stay in VIII.32 and the Urmia work in VIII.40. Tied to G89-3 and G89-13.
- **G89-51. Catholics of the Ottoman Balkans (RV-3).** (a) One row, 1650-1878. (b) A named line in VII.19 and VIII.29. (c) Hold for a Croatian-language source. **Rec. (a)** The era 8 part enters on the V items; the era 9 part after one more source. (b) would tell a local church as Rome's story.
- **G89-52. Liberia's settler churches (RV-6).** (a) A named line in VIII.7's West Africa wing ("Liberia's settler church"), with links from VIII.1. (b) A row for the Black Atlantic return churches. (c) Nothing. **Rec. (a)** The row weight sits in VIII.1 and VIII.7 already.
- **G89-53. The Transylvanian Unitarians (RV-7).** (a) Hold. (b) A lane 8 row now, on Rees alone. (c) Out of scope. **Rec. (a)** Tied to G89-45.
- **G89-54. The Czech lands after 1627 (RV-8).** (a) A VII.4 line now, the rest logged for a North Europe pass. (b) A Czech Protestant row, 1627-1906, now. (c) Log only. **Rec. (a)**
- **G89-55. Kosmas the Aitolian (RV-9).** (a) Hold, then a line in VII.18. (b) A line in VIII.12. (c) Nothing. **Rec. (a)**

RV-1 is answered by G89-1, and RV-5 by G89-4.

---

## 9. Wanted list for the source-research thread

Everything the passes named for source research, grouped by pass. Each item keeps the pass's own evidence state; the full item and its locus are in sections 3 to 7. No item here was searched again for this record.

### Across all passes

- **OCR quotes to be checked against page images.** Every quote taken from raw OCR must be checked against the page image before it enters census copy. The Africa, Latin America and rivers passes say so in their keys. Latin America flags Bleby 1868, Muratori 1743 and Vieira's sermons by name. Asia flags OCR misreadings of dates: "1602" for the 1692 toleration edict, "17236" in the *Collectanea*, and "J690" for Vaz's entry into Jaffna.
- **Raw downloads.** The items opened raw online sit in the passes' session scratchpads, not in the repo. They must be fetched again to be vendored.
- **Living marks.** No pass graded a living mark on a dated item after 2010. Each living mark needs one before census use.

### Africa

- Ignazio Guidi's Ge'ez annals with Latin translation: *Annales Iohannis I, Iyāsu I, Bakāffā* (CSCO, 1903-05) and *Annales regum Iyasu II et Iyo'as* (1910-12). The archive.org copies are lending-only (a 1955 reprint seen as metadata, V-s; the fetch returned 401). The pass asks that Guidi go on the wants list before AF-1 is drafted.
- H. Weld Blundell, *The Royal Chronicle of Abyssinia, 1769-1840* (Cambridge, 1922): searched on archive.org, not found [S].
- Studies by scholars from the region: Merid Wolde Aregay; Getatchew Haile on the christological disputes [S].
- For the Copts: the Arabic *History of the Patriarchs* for the Ottoman patriarchs; J. M. Vansleb, *Histoire de l'Eglise d'Alexandrie* (Paris, 1677), not found by title [S]; Coptic historians of the archons (Magdi Guirguis on the Jawhari brothers) [S].
- For Kongo: the kings' and nobles' letters to Rome and Lisbon; the Capuchin manuscripts of Antonio de Teruel and Bernardo da Gallo [S].
- For the Cape: the Dutch *Acta Synodi* of 1857, and a pre-1930 history that prints the 1857 resolution and the founding of the Sendingkerk (1881).
- For the mission churches: Ntsikana's hymn in Xhosa from a pre-1930 printing. Tiyo Soga's journal and letters were published in 1983 [S], so they are not public domain.
- For the Catholic mission revival: Laval in Mauritius, the Spiritans and Libermann, and Ohrwalder's *Ten Years' Captivity in the Mahdi's Camp* (1892), not found by title [S].
- For West Africa: a pre-1930 source for Capitein and for Quaque. The only Capitein lead found is a modern translation (2001), not public domain.
- **Library holdings no era 8 or 9 row uses:** Ludolf (1682, 1691), Telles (1710) and Lobo (1735) for Ethiopia; Carli (1671), Cavazzi (1687), Merolla (1692) and Zucchelli (1715) for Kongo and Angola; Latrobe (1771) and Cranz (1780) for the Moravian missions.

### Latin America and the Caribbean

The pass's own list (§6 of its body), as written in substance:
1. Montoya, *Conquista espiritual* and *Tesoro de la lengua guaraní* (both 1639); Dobrizhoffer (1784; English 1822); the 1767 Pragmatic Sanction.
2. Phillippo, *Jamaica: Its Past and Present State* (1843), on archive.org; Wallbridge, *The Demerara Martyr* (1848); the 1832 parliamentary evidence on the Jamaica rising.
3. Frías, *Tomóchic*.
4. A Brazilian brotherhood *compromisso* printed before 1930.
5. Hernández y Dávalos, *Colección de documentos* (1877-82), for Hidalgo and Morelos.
6. Kalley's and Simonton's journals.
7. For Haiti: the Code Noir (1685); a French account of the concordat church; James Theodore Holly's own writings.
8. For Cancuc: Francisco Ximénez's chronicle of the Dominican province of Chiapas and Guatemala.

**Ready to vendor (opened raw this run, public domain by date):** Bleby, *Death Struggles of Slavery* (1868); Hinton, *Memoir of William Knibb* (1849); Euclides da Cunha, *Os Sertões* (1905); Vieira, *Maria Rosa Mystica* (1686); Antonil (1711); Thomson, *Letters* (1827); Muratori, *Il cristianesimo felice* (1743). The pass notes that the Library holds nothing for the region from 1815 to 1906.

### Asia and the Pacific

Original-language texts, searched for and not found raw (**wanted**):
- **Malayalam:** Paremmakkal Thoma Kathanar, *Varthamanappusthakam* (c. 1790), the first Malayalam travel book; no pre-1930 printing found. Chavara's own writings (the *Chronicles*) and other Syro-Malabar sources.
- **Chinese:** Huang Bolu (黃伯祿), 正教奉褒 *Zhengjiao fengbao* (Shanghai, 1883); the Chinese text of the 1692 Kangxi edict; the Chinese text of the 1723 memorial.
- **Japanese:** 天地始之事 (*Tenchi hajimari no koto*), the hidden Christians' own text.
- **Vietnamese:** Philiphê Bỉnh, *Sách sổ sang chép các việc* (1822); no pre-1930 printing found.
- **Malay:** an own voice for the VOC-era churches. Valentijn, *Oud en Nieuw Oost-Indiën* (1724-26), and the Leijdecker Malay Bible (1733) are [S], not opened.
- **Portuguese, Tamil and Sinhala:** Sebastião do Rego's life of Joseph Vaz (1745) [S]; Jacome Gonçalves's Tamil and Sinhala works [S].
- **Māori:** Te Ua's *Ua Rongopai* and Ringatū's *Pukapuka*. Binney on Te Kooti was not found on archive.org [S].

Studies and other items:
- A modern study of the Karen Baptists, to be added before AP9 is drafted.
- Eric Widmer, *The Russian Ecclesiastical Mission in Peking during the Eighteenth Century* (Harvard, 1976): searched, not found [S].
- The 1841 papers on the Cofradía de San José (not in the vendored Blair and Robertson volumes searched) [S], or another dated primary.
- G. Milne Rae, *The Syrian Church in India* (1892): opened, passage not located [S].
- Ellis, *Polynesian Researches* (1829-31): the volume opened does not carry the conversions [S].
- One verified era 9 source for AP2's era 9 half; primary sources for AP12 (Australasia) and AP15 (Korea).

### Middle East, Caucasus, Russia and Eastern Europe

The pass's own list (its note 8): the 1736 Maronite synod acts (Mansi vol. 38; archive.org title searches found nothing); a clean Duwayhī; Assemani, *Bibliotheca orientalis* III, for the Josephite years (in the Library, not searched for them); a Syriac Orthodox chronicle after 1369, or Parry, *Six Months in a Syrian Monastery* (1895); Brosset's modern Georgian volumes (1856-1858); a Belokrinitsa own-voice text; Rufus Anderson's 1872 history of the ABCFM missions to the Oriental churches (the fetch failed); a Romanian pre-1930 study (Bunea, Iorga); a Hungarian Protestant source in Hungarian.

Also named in the candidate sections:
- For the Old Believers: the Belokrinitsa statute, the *Okruzhnoe poslanie* of 1862, the text of the 1905 decree; the Russian histories of the Austrian hierarchy by Subbotin, Ivanovskii and Smirnov (no scan found).
- For the Syriac Orthodox: the continuators of Bar Hebraeus beyond 1369; Assemani, *Bibliotheca orientalis* II (not vendored).
- For Hungary: the galley-slaves' own narratives, such as Bálint Kocsi Csergő's account [S].
- For Poland and Lithuania: Polish pastoral letters of the period; a Lithuanian source on the press ban. Theiner's *Vetera monumenta Poloniae et Lithuaniae*, vol. 4, is held, not read.
- For the Arab evangelicals: an Arabic source from the church itself, such as Bustānī's own writings.
- For Urmia: Wigram, *The Assyrians and their Neighbours* (1929), held in the Library, not read.
- For the Russian missions: Mouravieff 1842 (in the Library) for Siberia; the rivers pass has since opened its translator's preface (V).
- For every row that leans on the Catholic Encyclopedia: a second, non-Catholic study.
- Georgian, Syriac and Armenian originals were not opened.
- **Library holdings the rows do not use:** Charon's 1833-1855 volume (listed in VII.23's corpus map) and Paisii's *Istoriia slavianobolgarskaia* (listed for VII.18).

### Rivers cross-check

- For RV-1: Dobrizhoffer (1784); the Pragmatic Sanction of 1767; a Polotsk source; a modern history of the suppression; John W. O'Malley's later surveys [S].
- For RV-2: P. M. Friesen, *Die Alt-Evangelische Mennonitische Brüderschaft in Russland (1789-1910)* (1911) [S]; the 1800 charter of privileges [S]; which Library file holds the Dordrecht confession [S].
- For RV-3: the Albanian council of 1703 (*Concilium Albanum*) [S]; a Bosnian Franciscan chronicle in Croatian, such as the Fojnica or Sutjeska chronicles [S]; a non-Catholic study.
- For RV-4: an Arabic own voice (Bustānī); Anderson 1872.
- For RV-5: J. Taylor Hamilton, *A History of the Missions of the Moravian Church during the Eighteenth and Nineteenth Centuries* (1901), opened raw, is a vendoring candidate. Nothing Moravian after 1815 is vendored.
- For RV-6: the AME church's tie to South Africa's Ethiopian Church (1896) [S]; Daniel Coker (1820) [S].
- For RV-7: a Transylvanian Unitarian source for 1660-1906, in Hungarian or Latin.
- For RV-9: a pre-1930 text on Kosmas the Aitolian; none found raw.

---

## 10. Data flags noticed and not touched

The passes flagged these in existing rows and in the Open-Gaps list. None was changed. Each is for the row's owner, or for G89-6 where a candidate depends on it.

**Census rows**
- **VIII.46 (Haiti)** carries the region "North America", not "Latin America". That is why Open-Gaps 142 counts only three Latin American entries (Latin America).
- **VII.17** lists Peru as its only country, and its place label is "New Spain · Peru", while its name says "Latin American" and its sources name Afro-Brazilian brotherhoods (Latin America). LA8-4 would change it.
- **VII.17's dates** read "c. 1600-1810" and overlap VI.13d, which runs to 1650 (Latin America).
- **VIII.48** lists Brazil as its only country, while its text names Mexico and Ecuador (Latin America).
- **VI.13d** has no countries, no longDescription, no voices, no legacy and no sources (Latin America).
- **VIII.7's status text** says its "four named wings have fixed boundaries". Any added wing changes that sentence and the row's name, a frozen field (Africa; rivers §1c). Under G89-3(b) it stays as it is.
- **VIII.7** says "Liberia sits inside its orbit" but never names Liberia or the settlers' church; VIII.1 names no African tie (rivers, RV-6).
- **IV.26** (the Copts, Fatimid to Mamluk) has no `continuesAs`, and no row carries the Copts from c. 1300 to 1854 (Africa).
- **VI.13a's relationsSummary** says the Antonian movement "may have grown out of it, as one modern study holds"; the edge VI.13a to VII.11 is graded Inferential-Thin. AF-3 would give it context (Africa).
- **IX.59** has one predecessor (VIII.43); AF-6's edge would add a second. **IX.60** has no South African predecessor; AF-4 would be it (Africa).
- **VI.11** has no `continuesAs`, and **VIII.29** does not name the Jesuits (rivers §1a).
- **VII.23's and VII.18's corpus maps** list Library works their text does not use: Charon's volume and Paisii (Middle East, note 4).

**Open-Gaps entries**
- **Open-Gaps 142** dates the Coptic break from 1517; the real gap starts c. 1300 (Africa).
- **Open-Gaps 142** dates the China break to 1793; the roster is empty for China's Catholics to 1906 (Asia).
- **Open-Gaps 142** has no entry for the Moravian church after 1815, nor for Kongo or Southern Africa (Latin America, Africa).

**Within the passes**
- Fortescue's Catholic Encyclopedia article "Jerusalem (After 1291)" misprints "Pius III" once for Pius IX (Middle East, ME-16).
