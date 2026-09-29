# Source Readiness Dossier — The Second-Century Greek Apologists

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** I.35
**Corpus-map slug:** `greek-apologists-second-century`
**Time window:** c. 124–200 CE
**Region(s):** Athens, Rome, Sardis, Antioch
**Dossier author / date:** source-acquisition research thread, 2026-09-21.
**Refresh, 2026-09-29:** not yet independently reviewed. Sections 1 to 5
are restated to the library as it stands: the corpus-map shelf (17 works),
the original-language witnesses added to `cic/texts/`, the Apologists
window slate and the Tatian ruling in
`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` (four entries of that
date), and the revised Step 0. The refresh corrects four statements of the
first version: the Dialogue word count credited to Step 0 (Step 0 states
no word counts), the claim that Step 0 recounted the roster
"independently", the "Revision 7" label (Step 0 carries no revision
number), and Routh's *Reliquiae sacrae* vol. V as a Melito lead (it holds
Archelaus and creeds; Melito is in vol. I, which is vendored).
**Corpus-map / `cic/texts/` state as of:** 2026-09-29, the working tree on
top of commit `d1140c9f`. The first version was checked against `main` @
`820550b`.

This candidate already carries five rounds of independent adversarial
review of its Step 0 (Movement-Scope Confirmation),
`Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md`
(`Review-Artifacts/Step0_Round1_Review.md` through `Step0_Round5_Review.md`),
and a later revision that awaits its next independent review. Step 0 did
extensive, source-verified work on sourcing (B1), ecology (B2), and
built-world uniqueness (B3). This dossier does not repeat that work. It
adds what Step 0 doesn't do: a corpus-wide sweep for vendored material
Step 0 had no reason to go looking for, and a check of public-domain
acquisition candidates against the corpus-map's own live gaps. Step 0's
§3 B1 and B3 are the authoritative source for the roster's attribution and
dating flags and for built-world overlap. Step 0 asserts no word counts,
and neither does this dossier. The §1 table below is a direct extraction
from `cic/corpus-map/greek-apologists-second-century.yaml` and its
`_staging/` feeders rather than a paraphrase of Step 0's prose, so a builder
can trust it without cross-checking both documents.

## 1. Already assigned

All 17 works on `cic/corpus-map/greek-apologists-second-century.yaml`, in 39
rows. Method: parse the shelf; distinct `work` titles = 17; rows = 39. Each
work has one row for its English ANF witness (17 rows). The other 22 rows
are original-language witnesses: 6 rows point to clean primary originals and
16 to second witnesses. Seventeen files under `cic/corpus-map/_staging/`
feed the shelf. Roles: 37 rows `tradition`, 2 rows `context`.

"Scale" is `whole` or `fragments`. No word count is asserted here.

| work | author | role | confidence | scale | English witness (ANF) |
|---|---|---|---|---|---|
| The First Apology | justin_martyr | tradition | assigned | whole | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| The Second Apology | justin_martyr | tradition | assigned | whole | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| Dialogue with Trypho | justin_martyr | tradition | assigned | whole | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| The Discourse to the Greeks | justin_martyr (transmitted; authenticity long doubted) | tradition | provisional | whole | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| Hortatory Address to the Greeks | justin_martyr (transmitted; widely doubted) | **context** (per the window slate) | provisional | whole | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| On the Sole Government of God | justin_martyr (transmitted; widely doubted) | tradition | provisional | whole | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| A Plea for the Christians | athenagoras | tradition | assigned | whole | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| The Resurrection of the Dead | athenagoras | tradition | assigned | whole | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| Theophilus to Autolycus | theophilus | tradition | assigned | whole | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| Address to the Greeks | tatian | tradition | assigned | whole; co-owned with `syriac-edessa-nisibis` (also assigned to `post-apostolic-house-church`); see §5 | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| Epistle to Diognetus | mathetes (anonymous) | tradition | assigned | whole | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| Fragments of Quadratus | quadratus | tradition | assigned | fragments | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| Fragments of Melito of Sardis | melito-of-sardis | tradition | assigned | fragments (the ANF fragments only, not the twentieth-century-recovered *Peri Pascha*; see §4) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| Fragments of Claudius Apollinaris | claudius-apollinaris | tradition | assigned | fragments (the Thundering Legion narrative, via Eusebius *HE* V.5). The staging file has two further English rows for him, not on this shelf: one in `post-apostolic-house-church`, one in `montanism-the-new-prophecy` (`context`, his anti-Montanist witness) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| Fragments of Aristo of Pella | aristo-of-pella | tradition | assigned | fragments (triple-assigned with `post-apostolic-house-church` and `ebionite-nazoraean-current`) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| The Apology of Aristides the Philosopher | aristides | tradition | assigned | whole (Greek and Syriac recensions in the ANF volume) | `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` |
| Ambrose: a memorial (hypomnemata) addressed to the Greeks | ambrose-hypomnemata (transmitted) | **context** (per the window slate) | provisional | whole (a Greek apology surviving only in Syriac translation; leaves the roster and stays in `syriac-edessa-nisibis` as `transmission`) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |

**Original-language witnesses on the shelf** (status
read from each file's header and from `cic/texts/README.md`).

Clean primary originals. Hand-keyed Greek in the Perseus / Open Greek and
Latin TEI, CC BY-SA 4.0 as a digital edition (attribution and share-alike
travel with any quotation). Each quotation is still to be verified verbatim
against the file before use (`cic/texts/INTAKE.md`).

| work | file | printed edition |
|---|---|---|
| First Apology | `justin-martyr_first-apology-grc_rauschen1911.txt` | Rauschen 1911 |
| Second Apology | `justin-martyr_second-apology-grc_rauschen1911.txt` | Rauschen 1911 |
| Dialogue with Trypho | `justin-martyr_dialogue-with-trypho-grc_archambault1909.txt` | Archambault 1909 (Greek only; about 1 percent of Greek tokens carry a stray Latin letter) |
| Epistle to Diognetus | `pseudo-justin_epistle-to-diognetus-grc_lake1917.txt` | Lake 1917, Loeb (Greek only) |
| A Plea for the Christians | `athenagoras_legatio-grc_otto1857.txt` | Otto 1857 |
| The Resurrection of the Dead | `athenagoras_de-resurrectione-grc_otto1857.txt` | Otto 1857 |

Second witnesses only. Internet Archive scans read by OCR, public domain by
date. Not to be quoted as the original until a clean witness is vendored or
the page image is checked.

| file | works on the shelf | what is real text |
|---|---|---|
| `tatian_oratio-ad-graecos-grc-lat_otto1851.txt` | Tatian, *Address* | Greek layer present (about 309,000 Greek characters) at the noise level of the other Otto scans; Otto's Latin translation |
| `apologists-fragmentary_reliquiae-corpus-apologetarum-vol9-grc-lat_otto1872.txt` | Quadratus, Aristo, Melito, Claudius Apollinaris | Greek about 97,000 characters, about three in four tokens matched in a test on the series' Athenagoras volume; Otto's Latin and commentary |
| `apologists-fragmentary_reliquiae-sacrae-vol1-lat-grc_routh1846.txt` | Quadratus, Aristo, Melito, Claudius Apollinaris | Greek about 129,000 characters, two columns interleaved; Routh's Latin notes |
| `justin-martyr_opera-addubitata-grc-lat_otto1879.txt` | *Discourse*, *Hortatory Address*, *Sole Government*, *Diognetus* (Latin) | zero Greek-script characters; Otto's Latin translation and prolegomena |
| `theophilus_ad-autolycum-grc-lat_otto1861.txt` | Theophilus, *To Autolycus* | zero Greek-script characters; Otto's Latin translation and notes |
| `aristides_apology-syriac-grc-eng_harris-robinson1893.txt` | Aristides | zero Syriac-script and zero Greek-script characters; Harris's English translation, so an apparatus and collation witness, never an original-language witness |
| `goodspeed_aeltesten-apologeten-grc-lat-deu_1914.txt` | Aristides | zero Greek-script characters; German introductions, Latin apparatus, a Latin rendering of the Syriac |

The Ambrose *hypomnemata* has no original-language row; only the ANF English
translation of the Syriac is vendored.

**Shelf items for the Library thread, named and not decided here.** The
Otto 1879 row for the *Hortatory Address* is `role: tradition` while the
English row is `context`. The shelf note on Tatian's *Address* says
"Provisional because he was also later branded an Encratite", but the row is
`confidence: assigned`. The Aristides English row states "c. 125, Athens, to
Hadrian per the Introduction", one side of a Contested date. The *Diognetus*
note names only the late side of its date range. Step 0 §4 item 8 lists the
same four.

**Note on what Step 0 already covers and this dossier doesn't re-derive:**
Step 0 §3 B1 checks this roster against the vendored files and finds a
strong pass, with the attribution and dating flags on the pseudonymous-Justin
works, Aristo of Pella, the Ambrose *hypomnemata*, Aristides, the *Diognetus*
author, Quadratus and Melito named in §4 item 4. See that document rather
than this table for the reasoning behind each `provisional` flag and for the
slate outcomes.

## 2. Cross-link opportunities

**Checked using `CORPUS-USE.md`'s tier method (named-never-opened / same
time-place / same time-different-region / out-of-window) against the full
`cic/texts/` directory listing, not just the volumes Step 0 already used.**

- **No new `cic/texts/` file found that should be cross-linked to this
  candidate.** The vendored corpus's other Greek/Latin-original apologetic
  material (the `anf0x` volumes) is accounted for in §1 above, and the
  original-language editions now vendored are all on the shelf.
  Step 0's B3 already ran a direct, file-by-file overlap check against the
  built worlds (PAHC, Alexandria, Desert, Hieronymian, Imperial-Juridical,
  Cappadocian, Syriac); it was re-run read-only against `records/pahc/` and
  `records/syr/` (Step 0 §4 item 7). See that document rather
  than repeating it here.
- **Otto vol. IX (1872) and Routh vol. I (1846) hold more than the shelf
  uses.** `cic/texts/README.md` lists Aristides, Hermias and Miltiades in
  Otto vol. IX, and Aristides, Dionysius of Corinth and Hegesippus in Routh
  vol. I. The shelf has no Otto or Routh row for Aristides, and Hermias and
  Miltiades are not on this shelf. Dionysius and Hegesippus are PAHC's. This
  refresh did not open those sections. Named here rather than added
  unilaterally; tier "same time-place, unopened".
- **Routh's *Reliquiae sacrae* vol. V is not a lead.** It was checked in the
  vendoring pass and holds Archelaus and creeds, not the apologists
  (`cic/texts/README.md`, Routh vol. I entry); it is not vendored. Melito's
  fragments in Routh are in vol. I, which is vendored and on the shelf as a
  second witness.
- **Melito's fragment chain.** Step 0 (§3 B3) records that PAHC's own quote
  record for Melito's Fragment VII (`pahc.quote.melito-no-phantom.md`) is
  `Contested` because the fragment reaches us through Anastasius of Sinai
  (seventh century) rather than Eusebius. Otto vol. IX and Routh vol. I both
  print Melito's fragments with a Latin translation, and both are second
  witnesses. Neither has been checked for how it prints that fragment.

## 3. Verified acquisition leads

None cleared the bar this pass. The bar is `SOURCE-READINESS.md` §4: "an
explicit not-in-copyright/public-domain determination actually fetched and
read". Melito's *Peri Pascha* is closed (§4 below). This refresh did not
search for a clean Greek text of Theophilus, Tatian or Aristides, or for a
clean Greek witness of the Quadratus, Aristo, Apollinaris and pseudo-Justin
texts. They are recorded as missing in §5, not as searched and absent.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Melito of Sardis, *Peri Pascha* (On the Pascha) | Step 0 §3 B1 names this directly: the census's own `voices` field credits Melito with "a Paschal homily recovered in the twentieth century," and the vendored ANF fragment predates and is not that text | Checked against `archive.org` (title and creator search, 2026-09-21): no public-domain edition exists. The work was recovered from Papyrus Bodmer XIII, first published by Campbell Bonner in 1940; the standard critical editions (Perler 1966, Hall 1979 Oxford) are 20th-century and still in copyright. There is no 19th-century translation to find, because the text wasn't known when ANF/NPNF were made. Nothing to acquire by this route; the gap Step 0 names is real and durable, not a research gap. |
| Commodian, *Carmen Apologeticum* | Latin's own dossier work (see the sibling `latin-apologists` dossier) names this as the one Commodian work explicitly not vendored; checked here too since Commodian's dating question touches this candidate's own era-1/era-3 boundary indirectly | Checked against `archive.org` (title search, 2026-09-21): zero results. What surfaces under "Commodianus" is the already-vendored *Instructiones* in other 19th-century editions (e.g. the 1869 Oldham/Pusey Tertullian-and-Victorinus-and-Commodianus set, ANCL vol. 18, 1870) — the same text already in `cic/texts/`, not the *Carmen*. No public-domain English translation of the *Carmen apologeticum* was found. |
| Routh, *Reliquiae sacrae*, vol. V (`reliquiaesacraes05rout`) | Named in the first version of this dossier as a second-witness candidate for Melito | Holds Archelaus and creeds, not the apologists (`cic/texts/README.md`, Routh vol. I entry, from the vendoring pass; not re-fetched in this refresh). Not vendored. Melito's Routh fragments are in vol. I, already vendored. |

## 5. Open cross-world questions

- **Tatian is co-owned; the drafting that follows is not done.** The Greek
  Apologists' Step 0 (§3 B3, §4 item 2) records the ruling. Mark's words,
  quoted in `LIBRARY-DECISION-LOG.md`, in the entry "A voice may belong to several worlds of the same era; Tatian is co-owned": "if a voice influcences
  three worlds in the same era that is something they have in common. it
  doesn't have to be just one." Tatian is a built figure in Syriac
  Christianity (`records/syr/figure/syr.figure.tatian.md`,
  `evidentiary_weight: corroborating`, `narratable: false`). Per the log's
  entry on cross-world ownership (Mark: "that shouldnt be something he says,
  he talks from his own world perpsective only, it is noted in the
  references"), the co-ownership is written in the references and not in any
  world's figure or source record. No record of the Syriac world is edited.
  Still open, as Doc_01/Doc_02 work: the cited dating judgment for the
  *Address* (supplied in Step 0 §2 A2: c. 150–172, Contested; before his
  break with the Church, Dominant Modern Reconstruction; against Justin's
  death, Contested) and the Encratite disclosure (Step 0 §4 item 3). The
  Syriac source record's sentence "written before the events Eusebius
  describes" holds for the break with the Church and not for Justin's death;
  the record is not edited by this build.
- **Cross-build flags.** `records/pahc/figure/pahc.figure.justin.md` and
  `records/alx/figure/alx.figure.antony.md` already carry cross-build flags
  of the kind the log's entry on cross-world ownership excludes from new records.
  Whether they reach what a Representative says has not been checked; the
  log flags the question to Mark and edits neither record.
- **Slate items on the shelf.** The four shelf items listed in §1 belong to
  the Library thread. This candidate has no `Open_Gaps_Tracking.md` yet
  because it has no world file-code.
- **Clean Greek is missing for Theophilus, Tatian, Melito and Aristides.**
  Only OCR second witnesses are vendored (§1). The Quadratus, Aristo,
  Apollinaris and pseudo-Justin texts are in the same position. This
  refresh did not search for clean editions, except Melito's *Peri Pascha*
  (§4), which is not acquirable by this route.
- **The duplicate census entry noted in `NEEDS-RULING.md`** —
  `cyrilline-miaphysite-egyptian-tradition` vs.
  `cyrilline-miaphysite-egyptian-christianity` — does not touch this
  candidate's own roster and is not repeated here beyond this pointer.
