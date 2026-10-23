# Source Readiness Dossier — The Church of the East under Persia

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.3
**Corpus-map slug:** `the-church-of-the-east-under-persia`
**Time window:** 424-651
**Region(s):** Persian Mesopotamia
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of October 2026 (checked at `9675d7e3` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. A sibling bucket, `persian-church-of-the-east-early` (c. 300-451, deferred at Step 0), overlaps 424-451. Other threads vendored the Synodicon Orientale in French and German, the Chronicle of Seert II.1 (PO 5), Barhadbeshabba's History (PO 9), Elias of Nisibis, Mari and Amr, Labourt's study and the Persian martyr acts; their staging gives this entry 18 rows.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, October 2026).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| De patriarchis Nestorianorum (Amr and Sliba), the lives of the patriarchs of the East, Arabic text | amr-ibn-matta | tradition | provisional | whole file; the synod of forty bishops under Isaac and Marut; file 34,295 words | `amr-ibn-matta_de-patriarchis-nestorianorum-pars-altera-textus-ara_gismondi1896.txt` |
| De patriarchis Nestorianorum commentaria (Amr and Sliba), the lives of the patriarchs of the East, Gismondi's Latin vers | amr-ibn-matta | tradition | provisional | Latin version, pages in reverse order; Dadisho 14072 to 1409; file 68,935 words | `amr-ibn-matta_de-patriarchis-nestorianorum-commentaria-pars-altera-ara-lat_gismondi1896-1897.txt` |
| Barhadbeshabba 'Arbaya, Ecclesiastical History, part 2 (Diodore, Theodore, Nestorius, Ephesus 431), French with Syriac ( | barhadbeshabba-arbaya | tradition | provisional | fascicle V from file line 31511; chapters XX-XXX listed at 3; file 319,518 words | `po09_barhadbeshabba-ecclesiastical-history-part2-and-others-fra_1913.txt` |
| Chronicle of Seert (Histoire nestorienne), first part, fascicle 2, Arabic text with French translation | chronicle-of-seert | tradition | provisional | file lines 10710 to about 15846; Yazdgard 15411; Mar Isaac, ; file 363,133 words | `chronicle-of-seert_histoire-nestorienne-premiere-partie-fasc2-patrologia-orientalis-5-ara-fra_scher-dib1910.txt` |
| The Second Council of Constantinople (553): Extracts from the Acts, Sentence, Capitula, Anathemas Against Origen | council-of-constantinople-553 | context | provisional | div1 12; file 434,289 words | `npnf214_seven-ecumenical-councils.xml` |
| The Council of Ephesus (431): Extracts from the Acts, Decree, Canons | council-of-ephesus-431 | context | provisional | div1 10; file 434,289 words | `npnf214_seven-ecumenical-councils.xml` |
| Opus chronologicum (Chronography of Elias of Nisibis, 1018/19), Latin translation, both parts | elias-of-nisibis | tradition | provisional | whole file; the synod of Isaac and Marutha dated A.Gr. 721 a; file 103,967 words | `elias-of-nisibis_opus-chronologicum-lat_brooks-chabot-csco1910.txt` |
| Le christianisme dans l'empire perse sous la dynastie sassanide, 224-632 (1904) | labourt | context | provisional | whole file; 'Le concile de Séleucie (410)' 5728; Dadisho's s; file 121,584 words | `labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` |
| The Liturgy of the Blessed Apostles (Adaeus and Maris) | liturgy-of-addai-and-mari | tradition | provisional | div2 12.4; file 647,404 words | `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` |
| History of the Syrian Nation and the Old Evangelical-Apostolic Church of the East (1910), the whole history to the prese | malech | context | provisional | whole file; the Mongol chapter XXIX from file line 15667; file 158,270 words | `malech_history-of-the-syrian-nation-and-old-evangelical-apostolic-church-of-the-east_1910.txt` |
| De patriarchis Nestorianorum commentaria (Mari), the lives of the catholicoi of the East, Gismondi's Latin version; the  | mari-ibn-sulayman | tradition | provisional | Latin version, file lines about 9280 to 16306, pages in reve; file 112,409 words | `mari-ibn-sulayman_de-patriarchis-nestorianorum-commentaria-pars-prior-ara-lat_gismondi1899.txt` |
| Le livre d'Héraclide de Damas, French (Nau, 1910) | nestorius | transmission | provisional | whole file; file 187,950 words | `nestorius_livre-d-heraclide-de-damas-fra_nau1910.txt` |
| The Bazaar (Book) of Heracleides, English (Driver and Hodgson, 1925) | nestorius | transmission | provisional | whole file; file 189,853 words | `nestorius_bazaar-of-heracleides_driver-hodgson1925.txt` |
| Ausgewählte Akten persischer Märtyrer: selected Syriac acts of the Persian martyrs in German, with an appendix on East S | persian-martyr-acts | tradition | provisional | whole file; contents 81; Yazdgard I in the introduction 488;; file 112,905 words | `persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt` |
| Auszüge aus syrischen Akten persischer Märtyrer: German excerpts from the Syriac acts of the Persian martyrs with topogr | persian-martyr-acts | tradition | provisional | whole file; Narsai 2038; acts in the days of King Yazdgard 2; file 133,960 words | `persian-martyr-acts_auszuge-aus-syrischen-akten-persischer-martyrer-deu_hoffmann1880.txt` |
| Das Buch der Synhados: the synods from Akak (486) onward, German translation | synodicon-orientale | tradition | provisional | file line 2973 (Synode des Katholikos Mar Akak) to the end o; file 137,211 words | `synodicon-orientale_das-buch-der-synhados-deu_braun1900.txt` |
| Synodicon Orientale: the synods from Acacius (486) to Henanisho II (775), Syriac text and French translation | synodicon-orientale | tradition | provisional | French from file line 19437 (Acacius) through 34739 (Henanis; file 304,737 words | `synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt` |
| An Introduction to the History of the Assyrian Church, 100-640 A.D. (1910) | wigram | context | provisional | whole file; chapter V, Council of Mar Isaac (410), 3882; cha; file 98,507 words | `wigram_introduction-to-the-history-of-the-assyrian-church-100-640_1910.txt` |

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- Mansi vol. 4 (the 424 Markabta synod, file lines ~55606-55684; the 420 synod ~44134-44307) and vol. 3 (the 410 synod and creed ~111148-111948): vendored, previously assigned only to the Latin pastoral and Donatist buckets. Wired this pass as tradition (424, provisional) and antecedent (410, 420, needs-ruling).
- Bar Hebraeus, Chronicon ecclesiasticum III (catholicoi from Dadisho to Ishoyahb, ~3405-7430). Context (hostile Jacobite author), tier 4. Wired.
- John of Ephesus, Lives, Life 10 (Simeon of Beth Arsham debating the catholicos Babai, ~8279-9423). Context, tier 2. Wired.
- Zachariah XII.7 (the catholicos Joseph as Khosrau's physician, ~16502-16515); Chronicle of Edessa section 73 (the school of the Persians eradicated); Evagrius VI.21 (Khosrau II and Sira); Socrates VII.8, 18, 21 and Theodoret V.38-39. Context. Wired.
- Not wired: Duchesne III ch. XIII (scholarship); Thomas of Marga extracts in Budge's Paradise introduction.

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Patrologia Orientalis IV: Barhadbeshabba, La Cause de la fondation des ecoles (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt`) | Barhadbeshabba 'Arbaya | Addai Scher (French) | 1908 | https://archive.org/details/patrologiaorien00unkngoog | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Firmin-Didot 1908); the Cause located in the fetched text, October 2026 |
| Patrologia Orientalis XIII: Chronique de Seert, seconde partie (II.2) (`chronicle-of-seert_histoire-nestorienne-seconde-partie-po13-ara-fra_scher1919.txt`) | Chronicle of Seert (anonymous) | Addai Scher (French) | 1919 | https://archive.org/details/patrologiaorien13pari | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Firmin-Didot; no copyright field); the Seert chapters located in the fetched text, October 2026 |
| The Christian Topography of Cosmas, an Egyptian Monk (`cosmas-indicopleustes_christian-topography_mccrindle1897.txt`) | Cosmas Indicopleustes | J. W. McCrindle | 1897 | https://archive.org/details/christiantopogra00cosm | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Hakluyt 1897; no copyright field); the Adulis/Elesbaan passage located in the fetched text, October 2026 |
| Chronica minora, pars prior (CSCO Scriptores Syri), Latin version (`chronica-minora-pars-prior-versio-lat_guidi1903.txt`) | anonymous Syriac chroniclers | Ignazio Guidi (ed.) | 1903 | https://archive.org/details/chronicaminorapa00guid | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Guidi 1903; no copyright field), October 2026 |
| The Liturgical Homilies of Narsai (`narsai_liturgical-homilies_connolly1909.txt`) | Narsai | R. H. Connolly | 1909 | https://archive.org/details/liturgicalhomili00narsuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; CUP 1909); the homilies located in the fetched text, October 2026 |
| History of the Wars, Books I and II: The Persian War (`procopius_wars-1-2-persian_dewing1914.txt`) | Procopius of Caesarea | H. B. Dewing | 1914 | https://www.gutenberg.org/ebooks/16764 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 'First Printed 1914' and PD statement read, October 2026 |
| Gli statuti della Scuola di Nisibi (Giornale della Societa Asiatica Italiana 4) (`school-of-nisibis_statuti-della-scuola-di-nisibi-syr-ita_guidi1890.txt`) | School of Nisibis (anonymous) | Ignazio Guidi (ed., Syriac with Italian) | 1890 | https://archive.org/details/GiornaleDellaSocietaAsiaticaItaliana4 | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1890; CC Public Domain Mark 1.0), October 2026 |
| Histoire d'Heraclius par l'eveque Sebeos (`sebeos_histoire-d-heraclius-fra_macler1904.txt`) | Sebeos | Frederic Macler (French) | 1904 | https://archive.org/details/HistoireDheracliusParLevequeSebeos | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (no date or copyright field); the OCR title page MDCCCCIV and Macler's name read in the fetched text, October 2026 |
| The Book of Governors (Thomas of Marga), vol. II, English (`thomas-of-marga_book-of-governors-v2-english_budge1893.txt`) | Thomas of Marga | E. A. Wallis Budge | 1893 | https://archive.org/details/bookgovernorshi00thomgoog | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Kegan Paul 1893), October 2026 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Hoffmann, Auszuege aus syrischen Akten persischer Maertyrer (1880): already vendored by another thread.
- Ishoyahb III's letters (Duval, 1904-05): not verified, mostly after 651.

**Gaps (no public-domain English, or no own voice):**

- The institutional core is French or German only: the Synodicon (Chabot, Braun), the Chronicle of Seert, Barhadbeshabba, Braun's Mar Aba, the Khuzistan Chronicle. No PD English.
- Own voice in PD English is Narsai (~36,600 words), Thomas of Marga's Book of Governors (~30,000-40,000 relevant words, written in 840) and the Addai and Mari liturgy (~6,000 words).

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Voobus, Statutes of the School of Nisibis (1961); Becker, Sources for the School of Nisibis (2008) | Named in the census; English | Non-US 1961 and in copyright. Guidi 1890 (vendored) gives the Syriac. |
| Chabot, L'ecole de Nisibe (Journal asiatique 1896) | A French translation of the statutes | Not located on archive.org. Open lead. |
| Babai, Liber de unione (Vaschalde 1915, babaimagniliberd00bbai) | Babai is a census voice | Only the Syriac volume found; the Latin volume was not located. Open lead. |
| Mar Aba's own writings; Henana of Adiabene | Census voices | None survive; known only through Seert, Barhadbeshabba and Braun's martyr acts. |
| Mingana, Narsai (Mosul 1905) | The complete Narsai | Syriac only, no translation. |
| Rycaut; Philoxenus; Severus's letters | Nearby sources | Nothing on this window. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Two Persian buckets overlap 424-451 (`persian-church-of-the-east-early`); which holds the 410 and 420 synods?
- Bar Hebraeus is tradition in `syriac-edessa-nisibis` and context here.
- West Syriac bishops working inside Persia (Simeon of Beth Arsham, Ahudemmeh): placement rule.
- Overlap with `st-thomas-christians-of-india` through Cosmas and the Synodicon.

## 6. Build or atlas-only recommendation

**Recommendation: build.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

Floor: the 'Nestorian' label can be answered in the church's own words (the 410 creed, the 612 statement). Own voice: Narsai, the Book of Governors, the liturgy, plus a large institutional record (synods, school statutes, monastic rules, martyr acts) in French and German. Distinct from every sibling; strong audience fit.
