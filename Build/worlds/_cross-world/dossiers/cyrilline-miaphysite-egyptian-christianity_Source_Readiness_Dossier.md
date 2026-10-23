# Source Readiness Dossier — Cyrilline / Miaphysite Egyptian Christianity

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.1
**Corpus-map slug:** `cyrilline-miaphysite-egyptian-christianity`
**Time window:** 451-642
**Region(s):** Egypt
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of 2026-10-23 (checked at `469dd9b2` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. A sibling bucket, `cyrilline-miaphysite-egyptian-tradition` (era 2, 431-450s), holds the Ephesus and Chalcedon acts, Cyril's and Leo's letters and Theodoret's Eranistes; three of its own notes ask which id carries the corpus.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, 2026-10-23).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Council of Chalcedon (451), sessions V onward, in Mansi tom. 7 | council-of-chalcedon-451 | context | provisional | Actio quinta at file line 9189; file 576,457 words | `mansi_sacrorum-conciliorum-collectio-tomus-7-451-492-lat_welter-facsimile1901.txt` |
| The Ecclesiastical History of Evagrius (A.D. 431-594) | evagrius-scholasticus | context | assigned | whole file; file 76,846 words | `evagrius-scholasticus_ecclesiastical-history_walford1846.txt` |
| The Ecclesiastical History of Evagrius, Greek (Bidez and Parmentier, 1898) | evagrius-scholasticus | context | provisional | Books I-II; file 155,678 words | `evagrius-scholasticus_historia-ecclesiastica-grc_bidez-parmentier1898.txt` |
| The History of Joseph the Carpenter | history-of-joseph-the-carpenter | transmission | assigned | div2 7.7; file 781,893 words | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| The Chronicle of John, Bishop of Nikiu | john-nikiu | tradition | assigned | whole file; file 102,005 words | `john-nikiu_chronicle_charles1916.txt` |
| Liturgy of S. Mark | liturgy-of-st-mark | context | needs-ruling | file lines about 2259-3050; file 81,210 words | `liturgies-eastern_mark-james-clement-chrysostom-basil-malabar_neale-1870s.txt` |
| The Divine Liturgy of Mark | liturgy-of-st-mark | tradition | provisional | div2 12.3; file 647,404 words | `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` |
| History of the Patriarchs of the Coptic Church of Alexandria | severus-al-muqaffa | tradition | assigned | whole file, esp. the Benjamin I entry; file 167,073 words | `severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt` |
| Theopistus, History of Dioscorus (Syriac version of a Coptic anti-Chalcedonian history), French with Syriac (Nau, Journa | theopistus | tradition | provisional | the article from file line 162; Dioscorus's stories of Chalc; file 155,731 words | `theopistus_histoire-de-dioscore-journal-asiatique-1903-fra_nau1903.txt` |
| Timothy Aelurus, Refutation of the doctrine defined at Chalcedon (and of Leo's Tome), Classical Armenian text (Ter-Meker | timothy-aelurus | tradition | provisional | whole file; Chalcedon named from file line 207; the sections; file 120,986 words | `timothy-aelurus_widerlegung-der-lehre-von-chalcedon-xcl_ter-mekerttschian-ter-minassiantz1908.txt` |

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- Severus of Antioch, Select Letters Book VI (parts 1-2): to Dioscorus II (516), on the feast of Dioscorus, in defence of Timothy Aelurus (part 2 raw lines ~1465, ~2118-2128, ~2390-2400; part 1 ~5200-5590). Tier 1. Wired this pass as tradition, provisional.
- Zachariah Rhetor, Chronicle Books III-VI (~37,100 words, Alexandria 451-491, Timothy Aelurus's consecration at III.2) and Book IX (Julianists). Tier 1. Wired as tradition (III-VI) and context (IX).
- John of Ephesus, Ecclesiastical History Part III Book IV (~28,600 words: Theodosius in exile, the Alexandrian succession 566-578, Damian, the Gaianites) and Lives 47-48 (PO 18). Tier 1. Wired as tradition (provisional) and context.
- Basset's Coptic Synaxarium bound inside the PO 17 file (Theodosius, Dioscorus, the murder of Proterius, Benjamin). Transmission, tier 4. Wired this pass.
- Gregory the Great's letters to Eulogius of Alexandria (npnf212, npnf213). Context, tier 3. Wired.
- Nikiu's chapters on Constantinople (raw lines ~8490-9150) as context. Wired.
- Not wired: Palladius and Anan-Isho (antecedent, tier 4); Bell's Meletian papyri (4th c.).

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Origins of the Islamic State (Kitab Futuh al-Buldan), vol. I (`baladhuri_origins-of-the-islamic-state-v1_hitti1916.txt`) | al-Baladhuri | Philip Khuri Hitti | 1916 | https://archive.org/details/originsislamics00hittgoog | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Columbia 1916); the Nubia chapter located in the fetched text, 2026-10-23 |
| Recueil des inscriptions grecques-chretiennes d'Egypte (`lefebvre_recueil-inscriptions-grecques-chretiennes-egypte-grc-fra_1907.txt`) | anonymous (Christian inscriptions of Egypt and Nubia) | Gustave Lefebvre (ed., Greek with French) | 1907 | https://archive.org/details/recueildesinscri00egyp | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (IFAO 1907; no copyright field), 2026-10-23 |
| The Christian Topography of Cosmas, an Egyptian Monk (`cosmas-indicopleustes_christian-topography_mccrindle1897.txt`) | Cosmas Indicopleustes | J. W. McCrindle | 1897 | https://archive.org/details/christiantopogra00cosm | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Hakluyt 1897; no copyright field); the Adulis/Elesbaan passage located in the fetched text, 2026-10-23 |
| Coptic Apocrypha in the Dialect of Upper Egypt (with the Life of Bishop Pisentius) (`coptic-apocrypha-upper-egypt-life-of-pisentius_budge1913.txt`) | John the Elder and anonymous | E. A. Wallis Budge | 1913 | https://archive.org/details/copticapocryphai00budguoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; British Museum 1913); the Pisentius Life located in the fetched text, 2026-10-23 |
| The Monastery of Epiphanius at Thebes, Part II: Coptic Ostraca and Papyri (`monastery-of-epiphanius-thebes-pt2-coptic-ostraca_crum1926.txt`) | monks of the monastery of Epiphanius; Patriarch Damian; Bishop Pesynth | W. E. Crum; H. G. Evelyn White | 1926 | https://archive.org/details/monasteryofepiph02winl | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1926; no copyright field); the Damian text no. 53 located in the fetched text, 2026-10-23 |
| Patrologia Orientalis I: Le Synaxaire arabe jacobite (Tout, Babeh); Le Synaxaire ethiopien (Sane) (`synaxaire-arabe-jacobite_po1-thout-babeh-synaxaire-ethiopien-fra_basset-guidi1907.txt`) | Coptic and Ethiopian Synaxaria (anonymous) | R. Basset; I. Guidi (French) | 1907 | https://archive.org/details/patrologiaorient01pari | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Firmin-Didot 1907; no copyright field), 2026-10-23 |
| Patrologia Orientalis XI: Le Synaxaire arabe jacobite (Toubeh, Amchir) (`synaxaire-arabe-jacobite_po11-toubeh-amshir-fra_basset1915.txt`) | Coptic Synaxarion (anonymous) | R. Basset (French) | 1916 | https://archive.org/details/patrologiaorient11pariuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); Basset's title line read in the fetched text, 2026-10-23 |
| Miscellaneous Coptic Texts in the Dialect of Upper Egypt (with the Encomium of Theodosius of Alexandria on St Michael) (`miscellaneous-coptic-texts-upper-egypt_budge1915.txt`) | Theodosius of Alexandria (attrib.); Timothy (attrib.); anonymous | E. A. Wallis Budge | 1915 | https://archive.org/details/miscellaneouscop00budguoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; British Museum 1915); the Theodosius encomium located in the fetched text, 2026-10-23 |
| Patrologia Orientalis II: Vie de Sévère par Zacharie le Scholastique; Vie de Sévère par Jean de Beith-Aphthonia (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt`) | Zacharias Scholasticus; John of Beth Aphthonia | M.-A. Kugener (Syriac text with French translation) | 1903 | https://archive.org/details/patrologiaorient02pariuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); 'VIE DE SEVERE, PAR ZACHARIE LE SCHOLASTIQUE' title line read in the fetched text, 2026-10-16 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Monastery of Epiphanius at Thebes, Part I (archive.org monasteryofepiph01winl, 1926): the excavators' narrative; scholarship, not a source.
- Oeuvres de Schenoudi (archive.org oeuvresdeschenou01shen, 02shen; Amelineau 1907-14, French): Shenute is mostly before 451.

**Gaps (no public-domain English, or no own voice):**

- No public-domain English of Dioscorus or Timothy Aelurus in their own words: the Life of Dioscorus (Nau 1903) is French, and Timothy's Refutation (Ter-Mekerttschian 1908, already vendored by another thread) is an Armenian text with German preface.
- The Synaxarium volumes are French; the Arabic is not recovered by the OCR.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Timothy Aelurus, Refutation (timotheuslurusde0000timo, Leipzig 1908) | Timothy in his own words | Armenian text with German preface only; no PD English (Ebied and Wickham 1970 is in copyright). Already vendored on main by another thread as timothy-aelurus_widerlegung-der-lehre-von-chalcedon-xcl_ter-mekerttschian-ter-minassiantz1908.txt. |
| Maspero, Papyrus grecs d'epoque byzantine (papyrusgrecsdp01masp, NOT_IN_COPYRIGHT) | The Dioscorus of Aphrodito papyri the census names | Greek with French notes ('traduction' appears 4 times); a scholar's tool, not vendored. |
| Evetts, History of the Patriarchs, continuation (PO 5.1, PO 10.5) | More patriarchs | Starts at 661; belongs to coptic-christianity-under-early-islam. |
| Life of John the Almsgiver (Dawes and Baynes, Oxford 1948) | Chalcedonian patriarch 610-619 | Non-US 1948; presumed in copyright. |
| John Moschus, Spiritual Meadow; Liberatus, Breviarium | Alexandrian stories c. 600; the Chalcedonian account of the Theodosius/Gaianus split | Moschus has no PD English; Liberatus is Latin only (now vendored in PL 68 under Latin Africa). |
| Severus, Cathedral Homilies (later PO fascicles) | Severus's own preaching | Preached at Antioch; later fascicles post-date 1930. PO 8's fascicle is vendored by another thread. |
| Frend 1972, Davis 2004, Cambridge History of Egypt vol. 2 | The census's secondary sources | Modern scholarship, in copyright. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Duplicate ids: `cyrilline-miaphysite-egyptian-tradition` (era 2) and this entry both carry parts of the corpus. One id should carry it, or era 2 becomes the 431-451 antecedent world. needs-ruling.
- Severus's letters, Zachariah and John of Ephesus are tradition in `syriac-orthodox-west-syriac-christianity` and now also here; whether they are Egypt's tradition (ally voices) or context is a project-lead placement, flagged provisional.
- Chalcedon (npnf214 div1 11) sits in the `-tradition` sibling as tradition; here it is context. See the duplicate-id question.
- The 642 boundary: Baladhuri Part VII serves this entry and coptic-christianity-under-early-islam.
- Dioscorus's and Timothy's Lives overlap the Gaza anti-Chalcedonian circle (chalcedonian-monasticism-judean-desert-and-gaza).

## 6. Build or atlas-only recommendation

**Recommendation: build.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

Floor is clear (the dispute is over Chalcedon's formula). Own voice: John of Nikiu in window (~43,000 words), the History of the Patriarchs for the window (~20,000 English words), Pisentius's Life, the Epiphanius documents with Damian's festal letter, and ally voices (Severus ~142,000 words, Zachariah III-VI ~37,000, John of Ephesus IV ~29,000). The gap is Dioscorus and Timothy in public-domain English.
