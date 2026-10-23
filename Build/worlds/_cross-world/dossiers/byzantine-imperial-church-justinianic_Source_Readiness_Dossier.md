# Source Readiness Dossier — The Byzantine Imperial Church (Justinianic)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.13
**Corpus-map slug:** `byzantine-imperial-church-justinianic`
**Time window:** 451-622
**Region(s):** Constantinople, Anatolia, the imperial Mediterranean
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of October 2026 (checked at `9675d7e3` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. The census entry has no `sources` field, so tiers are judged against its `voices` and `why` fields.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, October 2026).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Codex Encyclius (457-458), in Mansi tom. 7 | codex-encyclius | tradition | provisional | index at file line 396; file 576,457 words | `mansi_sacrorum-conciliorum-collectio-tomus-7-451-492-lat_welter-facsimile1901.txt` |
| The Council of Chalcedon (451): Extracts from the Acts, Definition of Faith, Canons | council-of-chalcedon-451 | tradition | assigned | div1 11 — acts extracts, Definition 11.13, canons 11.18 (the; file 434,289 words | `npnf214_seven-ecumenical-councils.xml` |
| The Second Council of Constantinople (553): Extracts from the Acts, Sentence, Capitula, Anathemas Against Origen | council-of-constantinople-553 | tradition | assigned | div1 12 — sentence 12.6, capitula 12.7, anathemas 12.9-12.10; file 434,289 words | `npnf214_seven-ecumenical-councils.xml` |
| The Ecclesiastical History of Evagrius (431-594), Greek text with scholia (Bidez and Parmentier, 1898) | evagrius-scholasticus | tradition | provisional | whole file; Book I chapter headings on Nestorius from file l; file 155,678 words | `evagrius-scholasticus_historia-ecclesiastica-grc_bidez-parmentier1898.txt` |
| The Ecclesiastical History of Evagrius (A.D. 431-594) | evagrius-scholasticus | tradition | assigned | whole file; file 76,846 words | `evagrius-scholasticus_ecclesiastical-history_walford1846.txt` |
| The Encyclical Letter of Gennadius of Constantinople and his synod | gennadius_constantinople | tradition | assigned | div2 17.32 (~179 words); file 434,289 words | `npnf214_seven-ecumenical-councils.xml` |
| Register of the Epistles of St. Gregory the Great (Books I-VIII selection) | gregory | context | assigned | div2 3.5 — Register of the Epistles, Books I-VIII; continued; file 483,662 words | `npnf212_leo-great-gregory-great.xml` |
| Register of the Epistles of St. Gregory the Great (Books IX-XIV selection) | gregory | context | assigned | div2 2.5-2.10 — Books IX-XIV; continuation of the Register b; file 322,488 words | `npnf213_gregory-great-ephraim-syrus-aphrahat.xml` |
| The Letters of Leo the Great | leo | tradition | provisional | div2 2.4 — Letters (including Letter XXVIII, the Tome); file 483,662 words | `npnf212_leo-great-gregory-great.xml` |

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- Romanos the Melodist, Cantica (Pitra 1888; 67,855 words): vendored earlier but in no bucket until this pass. Wired as tradition, second witness only (the Greek OCR is unusable).
- John of Ephesus, Lives 47-48 (Theodora's communities, raw ~35474-39190) and HE Part III: context. Zachariah IX: context. Nikiu: context. Wired.
- Bernard 1896's editorial notes citing Procopius on Justinian's rebuilding of the Holy Places; Gregory of Tours; Prosper/Chronica minora on Belisarius: low.
- npnf214 div1 'vi', the editor's excursus on Roman law: scholarship; not to be wired.

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Patrologia Graeca 88: Dorotheus of Gaza, Barsanuphius and John (questions), John Climacus, Agathias, Cosmas, John the Faster (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt`) | Dorotheus of Gaza; John Climacus; Agathias; and others | Migne (Greek with Latin) | 1860 | https://archive.org/details/pg-88 | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (no copyright field; 1860 imprint); running heads 'S. DOROTHEI ABBATIS' and 'S. JOANNIS CLIMACI' and the Barsanuphius 'Interrogatio' section located in the fetched text, October 2026 |
| The Akathist Hymn and Little Compline (Greek text with English rendering) (`akathist-hymn_little-compline-grc-eng_london1919.txt`) | anonymous (Akathistos hymn) | unnamed (Greek Church in London series) | 1919 | https://archive.org/details/akathisthymnlitt00londuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT, 1919); title page read in the fetched text, October 2026 |
| Boethius, The Theological Tractates and The Consolation of Philosophy (Loeb) (`boethius_theological-tractates-consolation_stewart-rand1918.txt`) | Boethius | H. F. Stewart; E. K. Rand | 1918 | https://archive.org/details/theologicaltrac00testgoog | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Heinemann 1918), October 2026 |
| Collectio Avellana, pars I (epistulae I-CIV), CSEL 35.1 (`collectio-avellana_epistulae-imperatorum-pontificum-v1-lat_guenther1895.txt`) | Collectio Avellana (popes and emperors, 367-553) | Otto Guenther (ed.) | 1895 | https://archive.org/details/epistulaeimperat01gnth | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (1895 Tempsky; no copyright field); title page read in the fetched text, October 2026 |
| Collectio Avellana, pars II (epistulae CV-CCXLIV), CSEL 35.2 (`collectio-avellana_epistulae-imperatorum-pontificum-v2-lat_guenther1898.txt`) | Collectio Avellana (Justinian, Vigilius and others) | Otto Guenther (ed.) | 1898 | https://archive.org/details/epistulaeimperat02gnth | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Tempsky; no copyright field); 'Exemplum epistolae Iustiniani' located in the fetched text, October 2026 |
| Corpus Iuris Civilis vol. III: Novellae (Justinian's Novels) (`justinian_novellae-corpus-iuris-civilis-v3-lat-grc_schoell-kroll1895.txt`) | Justinian I | Rudolf Schoell and Wilhelm Kroll (eds.) | 1895 | https://archive.org/details/corpusiuriscivil03krueuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Weidmann 1892-95), October 2026 |
| Patrologia Latina 68 (Liberatus, Victor of Tunnuna, Primasius, Junillus) (`liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866.txt`) | Liberatus; Victor of Tunnuna; Primasius; Junillus | J.-P. Migne (compiler) | 1866 | https://archive.org/details/patrologiaecur68mign | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (date field 1800; Migne PL printed 1844-1866); the contents list located in the fetched text, October 2026 |
| Chronica minora II (MGH Auctores antiquissimi 11): Marcellinus Comes, Victor of Tunnuna, John of Biclaro, Isidore, Marius of Avenc (`chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt`) | Marcellinus Comes; Victor of Tunnuna; John of Biclaro; Isidore of Sevi | Theodor Mommsen (ed.) | 1894 | https://archive.org/details/chronicaminorasa11momm | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Weidmann 1894; no copyright field); the Marcellinus, Victor and Biclaro headings located in the fetched text, October 2026 |
| The Library of Photius, vol. I (`photius_library-v1_freese1920.txt`) | Photius | J. H. Freese | 1920 | https://archive.org/details/libraryofphotius00phot | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; SPCK 1920); codex 3 located in the fetched text, October 2026 |
| History of the Wars, Books I and II: The Persian War (`procopius_wars-1-2-persian_dewing1914.txt`) | Procopius of Caesarea | H. B. Dewing | 1914 | https://www.gutenberg.org/ebooks/16764 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 'First Printed 1914' and PD statement read, October 2026 |
| History of the Wars, Books III and IV: The Vandalic War (`procopius_wars-3-4-vandalic_dewing1916.txt`) | Procopius of Caesarea | H. B. Dewing | 1916 | https://www.gutenberg.org/ebooks/16765 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 'First Printed 1916' and PD statement read, October 2026 |
| History of the Wars, Books V and VI: The Gothic War (`procopius_wars-5-6-gothic_dewing1919.txt`) | Procopius of Caesarea | H. B. Dewing | 1919 | https://www.gutenberg.org/ebooks/20298 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 1919 imprint and PD statement read, October 2026 |
| Procopius, History of the Wars, Books VI.16-VII.35 (Loeb vol. IV) (`procopius_wars-6-16-7-35-gothic-grc-eng_dewing1924.txt`) | Procopius of Caesarea | H. B. Dewing | 1924 | https://archive.org/details/procopiuswitheng04procuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); the volume's own 'First printed 1924' leaf read in the fetched text, October 2026 |
| Procopius, History of the Wars, Books VII.36-VIII (Loeb vol. V) (`procopius_wars-7-36-8-gothic-grc-eng_dewing1928.txt`) | Procopius of Caesarea | H. B. Dewing | 1928 | https://archive.org/details/procopiuswitheng05procuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); the volume's own 'First printed 1928' leaf read in the fetched text, October 2026 |
| Of the Buildings of Justinian (`procopius_buildings_stewart1888.txt`) | Procopius of Caesarea | Aubrey Stewart | 1888 | https://www.gutenberg.org/ebooks/65404 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 1888 imprint and PD statement read, October 2026 |
| Library of the Palestine Pilgrims' Text Society, vol. II (Eucherius, Breviarius, Theodosius, Procopius Buildings, Antoninus of Pia (`ppts-v2_eucherius-breviary-theodosius-procopius-antoninus_stewart1890-97.txt`) | Theodosius; Antoninus of Piacenza; Eucherius (attrib.); Procopius | Aubrey Stewart | 1896 | https://archive.org/details/p2libraryofpales01paleuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT); the four parts' title pages read in the fetched text, October 2026 |
| The Secret History of the Court of Justinian (`procopius_secret-history_athenian-society1896.txt`) | Procopius of Caesarea | anonymous (Athenian Society) | 1896 | https://www.gutenberg.org/ebooks/12916 | pd-us-by-date | Claude (Library thread, Era III): Gutenberg book page and text fetched directly; 1896 imprint and PD statement read, October 2026 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Lethaby and Swainson, The Church of Sancta Sophia (churchsanctasop00swaigoog, 1894): a modern study with English renderings of Paul the Silentiary; row only the translated passages. Verified, not vendored.
- Akathist, Birkbeck and Woodward verse (acathisthymnofho00orth, 1917): verified; the 1919 prose edition is the one vendored.
- Evagrius in Greek, Bidez and Parmentier 1898 (ecclesiasticalhi00evag): the text file returned HTTP 500; retry.

**Gaps (no public-domain English, or no own voice):**

- Justinian's own church law in English: Scott 1932 needs a renewal check and is not on archive.org. Romanos has no PD English (el.wikisource was rate-limited; retry the author page). The emperor's letters exist only in Latin (Collectio Avellana).

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Scott, The Civil Law (1932); Loeb Procopius Buildings (1940) and Anecdota (1935); Atwater's Secret History (1927) | Justinian and Procopius in English | Renewal checks needed; the Gutenberg and archive.org Procopius editions cover the works. |
| Price and Gaddis, Chalcedon (2005); Dawes and Baynes (1948) | Acts and saints in English | In copyright. |
| Mansi vol. IX (Constantinople II); Pseudo-Dionysius (Parker) | Councils and mystical theology | Not located; Parker deferred as a cross-world question. |
| Malalas, Chronicon Paschale, Theophylact, Menander, Leontius (PG 86), Theodore Lector, Corippus | Byzantine historians | Greek or Latin only, no PD English, not verified this pass. The next batch. |
| Hypatius of Ephesus | A Justinianic bishop | No edition located. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Romanos: transmission or tradition here? Wired as tradition, provisional.
- John of Ephesus and Zachariah IX are anti-Chalcedonian voices against this church; context, never tradition.
- The 610-634 seam with the Heraclian sibling (Sophronius, Maximus).
- The Three Chapters material (Avellana, Victor of Tunnuna) is shared with latin-africa-under-byzantium.
- A `contested_claim` record is needed for the Akathist's date and authorship.

## 6. Build or atlas-only recommendation

**Recommendation: build.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

Several hundred thousand words of vendored public-domain English: Evagrius (~77,000), Procopius (the Wars in five volumes, the Secret History ~44,000, Buildings ~55,000), the Akathist, the council extracts, plus Justinian's Novels and Avellana letters in Latin. It leans on a court historian rather than clergy; lay life is thinly documented, as the census warns. Strong ecology and scale.
