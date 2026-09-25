# Source Readiness Dossier — The Latin Apologists

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** I.43 (absorbed I.17, "Tertullian's Voice," by Mark's
2026-09-10 ruling — see `worlds/latap/Step0_Movement_Scope_Confirmation.md`
Rev. 6)
**Corpus-map slug:** `latin-apologists`
**Time window:** c. 197–320 CE
**Region(s):** Carthage; Rome and Ostia; Sicca in Numidia; Nicomedia and
Trier
**Dossier author / date:** source-acquisition research thread, 2026-09-21
**Corpus-map / `cic/texts/` state as of:** `main` @ commit `820550b`, plus
one staging fix made during this dossier pass (§2 below).

This candidate already carries six full rounds of independent adversarial
review and a project-lead ruling at the Step 0 (Movement-Scope
Confirmation) stage — `worlds/latap/Step0_Movement_Scope_Confirmation.md`,
Revision 6 — which did extensive, source-verified work on sourcing (B1),
ecology (B2), and built-world uniqueness (B3), including a full,
independently re-derived word count for all 40 (now 43; see §2 and the
2026-09-25 correction note in §1) works.
This dossier does not repeat that work. It adds the one thing Step 0
doesn't do: a corpus-wide sweep for vendored material Step 0 had no reason
to go looking for, and a check of public-domain acquisition candidates
against the corpus-map's own live gaps.

## 1. Already assigned

All 43 works currently on `cic/corpus-map/latin-apologists.yaml`
(40 before this dossier pass, 41 after this dossier pass's own §2 fix; two
more — Cyprian's *An Address to Demetrianus* and *On the Vanity of
Idols* — were already cross-linked onto the corpus-map file by a separate,
earlier "Cross-link two apologetic works flagged by their own Source
Readiness Dossiers" pass, but this table had never been updated to show
them; corrected 2026-09-25 against a direct re-read of the corpus-map
file, no new research). Word counts are Step 0's own directly-recounted
figures (`§3 B1`, div2-boundary text extraction from the vendored XML)
where it states them.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Seven Books of Arnobius Against the Heathen | arnobius | tradition | assigned | 140,826 words | `anf06_...arnobius.xml` |
| The Instructions of Commodianus (Instructiones) | commodian | tradition | provisional (dating disputed — see §5) | 15,008 words | `anf04_...commodian...xml` |
| The Octavius of Minucius Felix | felix | tradition | assigned | 23,819 words | `anf04_...felix...xml` |
| A Treatise on the Anger of God | lactantius | tradition | assigned | 20,382 words | `anf07_lactantius...xml` |
| Fragments of Lactantius | lactantius | tradition | assigned | 3,932 words | `anf07_lactantius...xml` |
| On the Workmanship of God | lactantius | tradition | assigned | 18,840 words | `anf07_lactantius...xml` |
| The Divine Institutes | lactantius | tradition | assigned | 241,990 words | `anf07_lactantius...xml` |
| An Address to Demetrianus (Ad Demetrianum) | cyprian | tradition | assigned | — (not separately recounted) | `anf05_hippolytus-cyprian-caius-novatian.xml` |
| On the Vanity of Idols (Quod Idola Dii Non Sint) | cyprian | transmission | provisional (disputed authorship — compiles Tertullian and Minucius Felix) | — (not separately recounted) | `anf05_hippolytus-cyprian-caius-novatian.xml` |
| The Passion of the Holy Martyrs Perpetua and Felicitas (English) | passion_of_perpetua | tradition | assigned | 7,299 words | `anf03_tertullian.xml` |
| **The Passion of the Holy Martyrs Perpetua and Felicitas (Latin/Greek, second witness) — added this pass, §2** | passion_of_perpetua | tradition | assigned | pp. 60–95 of the printed volume | `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` |
| A Treatise on the Soul (De Anima) | tertullian | tradition | assigned | 49,399 words | `anf03_tertullian.xml` |
| Ad Martyras | tertullian | tradition | assigned | 2,700 words | `anf03_tertullian.xml` |
| Ad Nationes | tertullian | tradition | assigned | 34,840 words | `anf03_tertullian.xml` |
| Against Hermogenes | tertullian | tradition | assigned | 22,941 words | `anf03_tertullian.xml` |
| Against Praxeas | tertullian | tradition | assigned | 31,174 words | `anf03_tertullian.xml` |
| Against the Valentinians | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| An Answer to the Jews | tertullian | tradition | assigned | 21,645 words | `anf03_tertullian.xml` |
| Apology (Apologeticus) | tertullian | tradition | assigned | 38,392 words | `anf03_tertullian.xml` |
| Appendix of poems ascribed to Tertullian | tertullian (pseudonymous verse) | tradition | assigned | 31,817 words | `anf04_...xml` |
| De Fuga in Persecutione | tertullian | tradition | provisional (Montanist marker weak) | — | `anf04_...xml` |
| On Baptism | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| On Exhortation to Chastity | tertullian | tradition | provisional | — | `anf04_...xml` |
| On Fasting, in Opposition to the Psychics | tertullian | tradition | assigned | — | `anf04_...xml` |
| On Idolatry | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| On Modesty | tertullian | tradition | assigned | 25,582 words | `anf04_...xml` |
| On Monogamy | tertullian | tradition | assigned | 13,554 words | `anf04_...xml` |
| On Patience | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| On Prayer | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| On Repentance | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| On the Apparel of Women | tertullian | tradition | assigned | — | `anf04_...xml` |
| On the Flesh of Christ | tertullian | tradition | assigned | 20,055 words | `anf03_tertullian.xml` |
| On the Pallium | tertullian | tradition | assigned | — | `anf04_...xml` |
| On the Resurrection of the Flesh | tertullian | tradition | assigned | 45,592 words | `anf03_tertullian.xml` |
| On the Veiling of Virgins | tertullian | tradition | provisional | — | `anf04_...xml` |
| Scorpiace | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| The Chaplet | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| The Five Books Against Marcion | tertullian | tradition | assigned | 183,788 words (his largest work) | `anf03_tertullian.xml` |
| The Prescription Against Heretics | tertullian | tradition | assigned | 20,653 words | `anf03_tertullian.xml` |
| The Shows | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| The Soul's Testimony | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |
| To His Wife | tertullian | tradition | assigned | — | `anf04_...xml` |
| To Scapula | tertullian | tradition | assigned | — | `anf03_tertullian.xml` |

**Corpus total per Step 0's own direct recount: 1,194,575 words** (464,797
original four authors + 729,778 Tertullian's corpus including the Passion).
This dossier's own single addition (§2) is a second-witness original-language
file, not new prose content, so it does not change that figure. The two
Cyprian works above were cross-linked by a separate, earlier pass and were
never part of Step 0's own four-author recount either; their word counts
are not separately stated anywhere in this build and are not included in
the 1,194,575 figure.

## 2. Cross-link opportunities

**Checked using `CORPUS-USE.md`'s tier method against the full `cic/texts/`
directory listing, not just the volumes Step 0 already used.**

- **A real defect found and fixed this pass, not merely named.**
  `cic/corpus-map/_staging/perpetua-scillitan-martyrs-lat-grc_robinson1891.yaml`
  carries the Latin/Greek critical-edition second witness (Robinson, 1891)
  for the Passion of Perpetua, already vendored and already correctly
  role/confidence-matched to the English witness — but its `atlas_ids`
  still pointed to `tertullian-s-voice`, the census entry Mark's
  2026-09-10 ruling merged into this candidate (`worlds/latap/Step0_Movement_Scope_Confirmation.md`
  Rev. 6). Every one of Tertullian's own 32 works in the `anf03`/`anf04`
  staging files was repointed by that ruling's own merge run; this one
  sibling file, holding a different work by a different (transmitted)
  author but assigned to the same then-existing entry, was missed.
  Re-pointed to `latin-apologists` and re-merged (scoped
  `corpus_map_merge.py --write-only`) as part of this dossier pass — see
  `cic/corpus-map/latin-apologists.yaml`'s new row in §1 above. This is
  exactly the shape of drift `worlds/_cross-world/README.md`'s own
  regeneration discipline exists to catch; flagged here for the record,
  not treated as a new decision, since it only completes an
  already-made ruling.
- **CIL8 (Corpus Inscriptionum Latinarum VIII), Supplementum: Inscriptiones
  Provinciae Numidiae (Cagnat/Schmidt, 1894) is vendored and assigned to
  `donatism` only, not to this candidate — named here, not decided.**
  Arnobius' own city, Sicca, is in Numidia, and this candidate's own B5
  scale claim (Step 0) already names Numidia as one of its regions. The
  epigraphic corpus's own staging note is explicit that it is
  `provisional` there too and "supports nothing on its own until a
  specific inscription is located and read" — no inscription has been
  checked against any claim either world makes. This dossier does not do
  that verification work (it is substantial and belongs to whichever
  Doc_02 reaches it first); it names the candidate cross-link so a future
  Doc_02 doesn't have to rediscover that the file exists.

## 3. Verified acquisition leads

None. See §5 for the two candidates checked and closed.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Commodian, *Carmen Apologeticum* | Step 0 §3 B1 names this directly as the one Commodian work not vendored ("the *Carmen apologeticum* is not vendored and is not counted here") | Checked against `archive.org` (title search, 2026-09-21): zero results. What surfaces under "Commodianus" is the already-vendored *Instructiones* in other 19th-century editions (the 1869 Tertullian-Victorinus-Commodianus set; ANCL vol. 18, 1870) — the same text already in `cic/texts/`, not the *Carmen*. No public-domain English translation found. |
| Lactantius' lost letters to Demetrianus | Step 0 §2 A2/§4 item 5 names these directly: Jerome's charge against Lactantius' pneumatology is "particularly" leveled at these letters, and they are "genuinely lost and not among the vendored texts" | Not a research gap — Step 0's own account is that the letters are lost to history, not merely unvendored. No acquisition is possible. Recorded here so a later pass doesn't re-search for something that doesn't survive. |
| Jerome's *Chronicle* (Chronicon), ad ann. 327, on Arnobius' dream-and-bishop conversion story | Step 0 §2 A2 names this as the source of a detail commonly but wrongly attributed to *De viris illustribus* 79, and notes it is "itself not among the vendored texts in `cic/texts/`" | Checked against `archive.org` (2026-09-21): Jerome's continuation of Eusebius' *Chronicle* exists in public-domain Latin editions (e.g. within Migne PL 27, and Helm's critical edition is not PD), but no English translation was located, and this candidate's own B1 does not currently rely on the passage for any claim — the corpus map's own note already attributes the story correctly to the *Chronicle* rather than to Arnobius' own text, which is the fix that mattered. Not pursued further as an acquisition lead this pass; named so a future pass knows it was checked. |

## 5. Open cross-world questions

- **Minucius Felix's and Commodian's dating remains binding, unresolved
  Doc_01 work** (Step 0 §4 item 1): if either author's likely date falls
  outside this candidate's 197–320 window, they may need reassignment —
  Minucius Felix's placement against `roman-church-third-century` (I.33)
  specifically, if his date is judged mid-third-century. This dossier
  does not attempt that dating judgment; it is a scholarship question, not
  a sourcing one.
- **The CIL8 Numidia cross-link (§2)** is real but unverified at the
  inscription level, shared with `donatism`'s own corpus map.
- **The duplicate census entry noted in `NEEDS-RULING.md`**
  (`cyrilline-miaphysite-egyptian-tradition` vs.
  `cyrilline-miaphysite-egyptian-christianity`) does not touch this
  candidate's own roster and is not repeated here beyond this pointer.
