# Source Readiness Dossier — Merovingian Gallic Christianity

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** II.7
**Corpus-map slug:** `merovingian-gallic-christianity`
**Time window:** c. 480-620
**Region(s):** Gaul
**Dossier author / date:** source-research thread (Library, Era III), 2026-10-23
**Corpus-map / `cic/texts/` state as of:** branch `library/era-iii-2026-10` after the Era III vendoring, merged with `origin/main` of October 2026 (checked at `9675d7e3` and the commits that follow it on this branch)

**This entry's status.** Census status: Pre-Survey Candidate. Four vendored-file defects were found and are flagged, not touched, because they belong to the threads that own the files: the Dalton file's header and its bucket locus say Books VI-X but the file holds all ten books ("HERE BEGINS THE FIRST BOOK" at raw line 225; "HERE ENDS THE TENTH BOOK" at 22761); PL 39 is vendored twice (augustine_sermones-341-396-et-appendix-lat_migne-pl39.txt and the Caesarius file); and `capitulatio-de-partibus-saxoniae_pertz1881.txt` is the whole MGH Capitularia regum Francorum I, its preface dated 1883.

## 1. Already assigned

Every work the corpus map listed for this entry before this pass (`origin/main`, October 2026).

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Sermones (Pseudo-Augustinian, attributed to Caesarius of Arles) | caesarius-arles | tradition | assigned | Sermo XIII, Sermo LXXIV confirmed by header; Sermo L-LIX ran; file 549,664 words | `caesarius-arles_sermons-pseudo-augustinian_migne-pl39.txt` |
| Gennadius, Lives of Illustrious Men (continuation) | gennadius | tradition | assigned | div2 4.4 — Gennadius. Lives of Illustrious Men.; file 579,470 words | `npnf203_theodoret-jerome-gennadius-rufinus.xml` |
| Register of the Epistles of St. Gregory the Great (Books I-VIII selection) | gregory | context | assigned | div2 3.5 — Register of the Epistles, Books I-VIII; continued; file 483,662 words | `npnf212_leo-great-gregory-great.xml` |
| Register of the Epistles of St. Gregory the Great (Books IX-XIV selection) | gregory | context | assigned | div2 2.5-2.10 — Books IX-XIV; continuation of the Register b; file 322,488 words | `npnf213_gregory-great-ephraim-syrus-aphrahat.xml` |
| The History of the Franks, Volume II | gregory-tours | tradition | assigned | whole file (Books VI-X plus Dalton's translator's notes); file 288,746 words | `gregory-tours_history-of-the-franks-v2_dalton1927.txt` |
| On Easter (De Pascha) | venantius | tradition | assigned | div1 4 — Venantius; file 647,404 words | `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` |

## 2. Cross-link opportunities

Texts already vendored elsewhere in the corpus that serve this entry, checked by reading the file content and not the filename (`CORPUS-USE.md` tiers). Items marked *wired* were assigned in this pass's staging files; the rest are named and left.

- The Capitularia volume's Merovingian section includes Clovis's own letter to the bishops (507-511, ~500 words, raw lines ~617-675), Childebert I, Guntram (585) and Chlothar II's edict (614). Tier 1. Wired as tradition.
- Ruricius of Limoges's letters (~34,000 words, raw ~20013-25132), bound into the Faustus of Riez volume (CSEL 21), c. 485-507. Wired as tradition, needs-ruling.
- Gallic Chronicle of 511 in the Prosper/Chronica minora file. Context. Wired.
- Columbanus's Letter I to Gregory (npnf213 ~4172-4596) and Jonas's Life of Columban (written for Luxeuil): wired as tradition and context.
- Gregory the Great's Brunhild letters (Turchi, locus not pinned): context, provisional.
- Not wired: Sulpicius, Salvian, Constantius's Vita Germani (antecedents, tier 4); Duchesne III ch. XV (scholarship).

## 3. Verified acquisition leads

Public-domain editions not previously vendored, each confirmed against its host (archive.org `/metadata` and the item's own text file, or Gutenberg's book page and text) and **vendored in this pass** under `INTAKE.md` §§1-9. Each file's registry entry records how it labels its sections, the credit line and the republishing scope.

| title (vendored file) | author | translator / editor | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| MGH AA VI.2: Avitus of Vienne, Opera (`avitus-vienne_opera-mgh-aa-6-2-lat_peiper1883.txt`) | Avitus of Vienne | Rudolf Peiper (ed.) | 1883 | https://archive.org/details/p2monumentagerma06geseuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; MGH AA VI.2); the Contra Arianos fragments located in the fetched text, October 2026 |
| MGH SRM II: Fredegar, Liber historiae Francorum, Lives of Clothild and Radegund (`fredegar-liber-historiae-francorum-vitae-mgh-srm-2-lat_krusch1888.txt`) | Fredegar; anonymous; Baudonivia | Bruno Krusch (ed.) | 1888 | https://archive.org/details/monumentagerman02hann | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Hahn; the title page 1888); the contents list located in the fetched text, October 2026 |
| Patrologia Latina 67 (Facundus, Ferrandus, Dionysius Exiguus, Caesarius) (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt`) | Facundus of Hermiane; Ferrandus; Dionysius Exiguus; Caesarius of Arles | J.-P. Migne (compiler) | 1865 | https://archive.org/details/patrologiaecursu67mign | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (date field 1800; the title leaf reads 1865); Facundus, Ferrandus and the Caesarian rules located in the fetched text, October 2026 |
| Bruns, Canones apostolorum et conciliorum, pars altera (`bruns_canones-apostolorum-et-conciliorum-pars-altera-lat_1839.txt`) | Gallic and Spanish councils (anonymous acts) | Hermann Theodor Bruns (ed.) | 1839 | https://archive.org/details/canonesapostolo01brungoog | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Reimer 1839); the Spanish and Gallic councils located in the fetched text, October 2026 |
| MGH SRM I: Gregory of Tours, Opera (Latin) (`gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt`) | Gregory of Tours | W. Arndt; B. Krusch (eds.) | 1885 | https://archive.org/details/monumentagerman01hann | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Hahn 1885; no copyright field); Pars II and the Gloria martyrum located in the fetched text, October 2026 |
| Gregory of Tours, History of the Franks (Brehaut, selections) and Miracles (`gregory-tours_history-of-the-franks-selections_brehaut1916.txt`) | Gregory of Tours | Ernest Brehaut | 1916 | https://archive.org/details/historyoffranks00greguoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Columbia 1916); the Miracles selections located in the fetched text, October 2026 |
| Life of St. Columban (Jonas), tr. Munro (`jonas-bobbio_life-of-st-columban_munro1895.txt`) | Jonas of Bobbio | Dana C. Munro | 1895 | https://archive.org/details/lifeofstcolumban0207jona | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; Penn 1895), October 2026 |
| Chronica minora II (MGH Auctores antiquissimi 11): Marcellinus Comes, Victor of Tunnuna, John of Biclaro, Isidore, Marius of Avenc (`chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt`) | Marcellinus Comes; Victor of Tunnuna; John of Biclaro; Isidore of Sevi | Theodor Mommsen (ed.) | 1894 | https://archive.org/details/chronicaminorasa11momm | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Weidmann 1894; no copyright field); the Marcellinus, Victor and Biclaro headings located in the fetched text, October 2026 |
| MGH Concilia I: Concilia aevi merovingici (`concilia-aevi-merovingici-mgh-concilia-1-lat_maassen1893.txt`) | Frankish councils (anonymous acts) | Friedrich Maassen (ed.) | 1893 | https://archive.org/details/conciliaaevimero01maas | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Hahn 1893; no copyright field); the Council of Orleans (511) located in the fetched text, October 2026 |
| MGH SRM III: Passiones vitaeque sanctorum aevi merovingici (`passiones-vitaeque-sanctorum-merovingici-mgh-srm-3-lat_krusch1896.txt`) | anonymous hagiographers | Bruno Krusch (ed.) | 1896 | https://archive.org/details/passionesvitaequesanctorum1 | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (Krusch 1896; CC Public Domain Mark 1.0); the Vitae Caesarii listed in the fetched contents, October 2026 |
| MGH AA IV: Venantius Fortunatus, Opera (`venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt`) | Venantius Fortunatus | Friedrich Leo; Bruno Krusch (eds.) | 1885 | https://archive.org/details/monumentagermani04geseuoft | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (NOT_IN_COPYRIGHT; MGH AA IV); Opera pedestria and the Vita Radegundis located in the fetched text, October 2026 |
| The Life of St. Samson of Dol (`samson-of-dol_life-of-st-samson_taylor1925.txt`) | anonymous | Thomas Taylor | 1925 | https://archive.org/details/lifeofstsamsonof00sams | pd-us-by-date | Claude (Library thread, Era III): archive.org /metadata read (SPCK 1925; no copyright field); title page read, October 2026 |

Verified and **not** vendored (duplicate, redundant or low value), so nobody re-verifies them:

- Gregory of Tours Dalton vol. I (introduction, scholarship).
- Henderson, Select Historical Documents (cu31924014186161), with the Salic Law in English at pp. 176-189; Hefele vol. 4 (scholarship); the Lex Salica of Kern: not confirmed.

**Gaps (no public-domain English, or no own voice):**

- Caesarius of Arles, the census's signature voice, exists in Latin only (the rules in PL 67, the Life in MGH SRM III, the sermons in PL 39). Morin 1937 and Mueller's FOTC sermons are in copyright.
- Gregory's miracle books, Venantius, the Radegund lives, Avitus, Fredegar, the Liber historiae Francorum and the councils have no public-domain English beyond Brehaut's short selections.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Thorpe 1974; the Liverpool miracle-book translations; Wallace-Hadrill 1960; Shanzer and Wood 2002; Mathisen 1999; Klingshirn 1994 | Modern English editions | In copyright. |
| Mueller vol. 1 (1956); McCarthy, Rule for Nuns (1960; rule-for-nuns_202301) | Caesarius in English | Need renewal checks; the uploader's PD Mark is not a rights determination. |
| bub_gb_GBhoAAAAMAAJ | SRM 2 | A 1984 reprint scan; the 1888 volume is used instead. |

## 5. Open cross-world questions

Named and passed on; none is decided here.

- Ruricius sits in an era-2 volume but wrote inside this window.
- Columbanus and Jonas: here or only in insular-irish-monastic-christianity?
- The Capitularia file serves both this entry and carolingian-reform-christianity; the loci should be split.

## 6. Build or atlas-only recommendation

**Recommendation: build.** This is a recommendation against the existing Step 0 tests (Section A: the doctrinal floor and rivals; Section B: sourcing depth, ecology, uniqueness, audience, scale). The portfolio decision is Mark's and does not block the library work.

Own voice in English: Gregory of Tours complete (~192,600 words, already vendored) plus modest extras (Brehaut selections, Munro's Columban). Large own-voice Latin is vendored (Gregory's miracle books, Venantius, the lives, the councils, Avitus, Fredegar). The main gap is Caesarius, Latin only. Rich ecology; distinct from siblings; strong audience fit.
