# Source Readiness Dossier — The Second-Century Greek Apologists

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** I.35
**Corpus-map slug:** `greek-apologists-second-century`
**Time window:** c. 124–200 CE
**Region(s):** Athens, Rome, Sardis, Antioch
**Dossier author / date:** source-acquisition research thread, 2026-09-21
**Corpus-map / `cic/texts/` state as of:** `main` @ commit `820550b`, plus
one staging fix made during this dossier pass (see §2 note on `The Passion
of the Holy Martyrs Perpetua and Felicitas` — actually latin-apologists'
own fix; not applicable here, left out of this world's own table).

This candidate already carries five full rounds of independent adversarial
review at the Step 0 (Movement-Scope Confirmation) stage —
`worlds/grkap/Step0_Movement_Scope_Confirmation.md`, Revision 7 — which did
extensive, source-verified work on sourcing (B1), ecology (B2), and
built-world uniqueness (B3). This dossier does not repeat that work. It
adds the one thing Step 0 doesn't do: a corpus-wide sweep for vendored
material Step 0 had no reason to go looking for, and a check of public-domain
acquisition candidates against the corpus-map's own live gaps. Step 0's own
§3 B1 and B3 are the authoritative source for word counts, attribution
flags, and built-world overlap; this dossier's §1 table below is a direct
re-extraction from `cic/corpus-map/greek-apologists-second-century.yaml`
rather than a paraphrase of Step 0's prose, so a builder can trust it
without cross-checking both documents.

## 1. Already assigned

All 17 works currently on `cic/corpus-map/greek-apologists-second-century.yaml`
(corrected from 16 — the table below previously omitted *Fragments of
Claudius Apollinaris*, which was already present on the corpus-map file
itself; not a change made by this pass, only a documentation fix bringing
this table in line with what was already there).
"Scale" is drawn from Step 0's own directly-recounted word figures where
Step 0 states them; otherwise marked not recounted here.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The First Apology | justin_martyr | tradition | assigned | part of Justin's corpus (not separately recounted) | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| The Second Apology | justin_martyr | tradition | assigned | " | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| Dialogue with Trypho | justin_martyr | tradition | assigned | ~75,000 words (Step 0 §2 A5) | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| The Discourse to the Greeks | justin_martyr (transmitted; authenticity long doubted) | tradition | provisional | — | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| Hortatory Address to the Greeks | justin_martyr (transmitted; widely doubted) | tradition | provisional | — | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| On the Sole Government of God | justin_martyr (transmitted; widely doubted) | tradition | provisional | — | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| A Plea for the Christians | athenagoras | tradition | assigned | — | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| The Resurrection of the Dead | athenagoras | tradition | assigned | — | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| Theophilus to Autolycus | theophilus | tradition | assigned | — | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| Address to the Greeks | tatian | tradition | assigned | — (also assigned to `post-apostolic-house-church` and `syriac-edessa-nisibis`; see §6) | `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` |
| Epistle to Diognetus | mathetes (anonymous) | tradition | assigned | — | `anf01_apostolic-fathers-justin-irenaeus.xml` |
| Fragments of Quadratus | quadratus | tradition | assigned | fragment | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| Fragments of Melito of Sardis | melito-of-sardis | tradition | assigned | fragment (the ANF fragment only — not the 20th-c.-recovered *Peri Pascha*; see §5) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| Fragments of Claudius Apollinaris | claudius-apollinaris | tradition | assigned | fragment (the Thundering Legion narrative, via Eusebius HE v.5) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| Fragments of Aristo of Pella | aristo-of-pella | tradition | assigned | fragment (triple-assigned with `post-apostolic-house-church` and `ebionite-nazoraean-current`) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |
| The Apology of Aristides the Philosopher | aristides | tradition | assigned | — | `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` |
| Ambrose: a memorial (hypomnemata) addressed to the Greeks | ambrose-hypomnemata (transmitted) | tradition | provisional | — (Greek apology surviving only in Syriac translation; also assigned to `syriac-edessa-nisibis`) | `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml` |

**Note on what B1 already verified and this dossier doesn't re-derive:** Step 0
§3 B1 independently recounted this roster against the vendored XML directly
(not the corpus map's own summary) and found a strong pass, with the
attribution and dating flags on the pseudonymous-Justin works, Aristo of
Pella, and the Ambrose *hypomnemata* already named precisely — see that
document rather than this table for the reasoning behind each `provisional`
flag.

## 2. Cross-link opportunities

**Checked using `CORPUS-USE.md`'s tier method (named-never-opened / same
time-place / same time-different-region / out-of-window) against the full
`cic/texts/` directory listing, not just the volumes Step 0 already used.**

- **No new cic/texts/ file found that should be cross-linked to this
  candidate.** The vendored corpus's other Greek/Latin-original apologetic
  material (the `anf0x` volumes) is already fully accounted for in §1
  above, and Step 0's own B3 already ran a direct, file-by-file overlap
  check against every built world (PAHC, Alexandria, Desert, Hieronymian,
  Imperial-Juridical, Cappadocian, Syriac) — see that document's §3 B3
  rather than repeating it here.
- **Routh's *Reliquiae Sacrae*, vol. 5 (Oxford, 1846; `archive.org` id
  `reliquiaesacraes05rout`) is a genuine, not-yet-checked second-witness
  candidate for Melito specifically, named here rather than added
  unilaterally.** It is a Greek/Latin critical compilation of 2nd–3rd
  century fragments — confirmed directly against the archive.org host,
  not title-matched — covering (among ~25 authors) Melito of Sardis,
  Julius Africanus, Hegesippus, and Gregory Thaumaturgus, several already
  represented in this corpus only via the English ANF fragment collections.
  This candidate's own Step 0 (§3 B3) already flags Melito's fragment chain
  as running through a 7th-century intermediary (Anastasius of Sinai) and
  carrying only `contested` weight in PAHC's own gravity record — Routh's
  own critical Greek/Latin text, if it prints Melito's fragment with fuller
  source-critical apparatus than the ANF headnote does, could strengthen
  that chain's own disclosure without changing anything already assigned.
  **Not vendored, not verified page-by-page against Melito's own fragment
  specifically** — this is a tier "same time-place, unopened" candidate
  worth a follow-up pass to locate Melito's own pages inside the volume,
  not a ready acquisition lead in its own right yet.

## 3. Verified acquisition leads

None cleared the bar this pass. Routh's *Reliquiae Sacrae* (§2 above) is a
real, confirmed-reachable public-domain volume, but this pass did not
locate and read Melito's own specific page range inside it, so it stays a
named cross-link opportunity rather than a verified lead per this
dossier's own bar (§4 of `SOURCE-READINESS.md`: "an explicit
not-in-copyright/public-domain determination actually fetched and read").

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Melito of Sardis, *Peri Pascha* (On the Pascha) | Step 0 §3 B1 names this directly: the census's own `voices` field credits Melito with "a Paschal homily recovered in the twentieth century," and the vendored ANF fragment predates and is not that text | Checked against `archive.org` (title and creator search, 2026-09-21): no public-domain edition exists. The work was recovered from Papyrus Bodmer XIII, first published by Campbell Bonner in 1940; the standard critical editions (Perler 1966, Hall 1979 Oxford) are 20th-century and still in copyright. There is no 19th-century translation to find, because the text wasn't known when ANF/NPNF were made. Nothing to acquire by this route; the gap Step 0 names is real and durable, not a research gap. |
| Commodian, *Carmen Apologeticum* | Latin's own dossier work (see the sibling `latin-apologists` dossier) names this as the one Commodian work explicitly not vendored; checked here too since Commodian's dating question touches this candidate's own era-1/era-3 boundary indirectly | Checked against `archive.org` (title search, 2026-09-21): zero results. What surfaces under "Commodianus" is the already-vendored *Instructiones* in other 19th-century editions (e.g. the 1869 Oldham/Pusey Tertullian-and-Victorinus-and-Commodianus set, ANCL vol. 18, 1870) — the same text already in `cic/texts/`, not the *Carmen*. No public-domain English translation of the *Carmen apologeticum* was found. |

## 5. Open cross-world questions

- **The Tatian figure-sharing ruling is still open.** Step 0 (§4 item 2)
  names this as the one remaining condition on this candidate's own Tier 1
  status: Tatian is a built, live figure in Syriac Christianity
  (`records/syr/figure/syr.figure.tatian.md`, `evidentiary_weight:
  corroborating`, `narratable: false`), and whether his voice is shared on
  the Justin/Antony co-ownership model or stays native to Syriac alone is
  Mark's call, not this dossier's or Step 0's own to make. Named here so a
  future Doc_02 doesn't have to re-locate where the question lives.
- **The duplicate census entry noted in `NEEDS-RULING.md`** —
  `cyrilline-miaphysite-egyptian-tradition` vs.
  `cyrilline-miaphysite-egyptian-christianity` — does not touch this
  candidate's own roster and is not repeated here beyond this pointer.
