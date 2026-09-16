# Source Readiness Dossier — The Second-Century Greek Apologists

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** I.35
**Corpus-map slug:** `greek-apologists-second-century`
**Time window:** c. 124-200 CE
**Region(s):** Athens, Rome, Sardis, Antioch (the census's own note: this
is a genre-world, not a settlement — see §5)
**Dossier author / date:** Claude (source-research thread), 2026-09-16
**Corpus-map / `cic/texts/` state as of:** commit `48e8bd470` (`main`,
2026-09-16)

## 1. Already assigned

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Apology of Aristides the Philosopher | aristides | tradition | assigned | full work | anf09_gospel-of-peter-diatessaron-origen-commentaries.xml |
| Fragments of Aristo of Pella | aristo-of-pella | tradition | assigned | fragments | anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml |
| A Plea for the Christians | athenagoras | tradition | assigned | full work | anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml |
| The Resurrection of the Dead | athenagoras | tradition | assigned | full work | anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml |
| Dialogue with Trypho | justin_martyr | tradition | assigned | full work | anf01_apostolic-fathers-justin-irenaeus.xml |
| Hortatory Address to the Greeks | justin_martyr | tradition | provisional | full work | anf01_apostolic-fathers-justin-irenaeus.xml |
| On the Sole Government of God | justin_martyr | tradition | provisional | full work | anf01_apostolic-fathers-justin-irenaeus.xml |
| The Discourse to the Greeks | justin_martyr | tradition | provisional | full work | anf01_apostolic-fathers-justin-irenaeus.xml |
| The First Apology | justin_martyr | tradition | assigned | full work | anf01_apostolic-fathers-justin-irenaeus.xml |
| The Second Apology | justin_martyr | tradition | assigned | full work | anf01_apostolic-fathers-justin-irenaeus.xml |
| Epistle to Diognetus | mathetes | tradition | assigned | full work | anf01_apostolic-fathers-justin-irenaeus.xml |
| Fragments of Melito of Sardis | melito-of-sardis | tradition | assigned | fragments | anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml |
| Fragments of Quadratus | quadratus | tradition | assigned | fragments | anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml |
| Address to the Greeks | tatian | tradition | assigned | full work | anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml |
| Theophilus to Autolycus | theophilus | tradition | assigned | full work | anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml |

The three `justin_martyr` rows marked `provisional` (Hortatory Address,
On the Sole Government of God, the Discourse to the Greeks) are the
well-known Pseudo-Justin cluster — modern scholarship doubts Justin's
own authorship of all three, and the corpus-map's own `provisional`
tag already reflects that correctly. Not a new finding; noted here so
a build thread doesn't need to re-derive it.

This is a genuinely strong base: eight of the nine authors named or
implied by standard handbook treatments of this period (Aristides,
Justin, Tatian, Athenagoras, Theophilus, Melito, Quadratus, the
Epistle to Diognetus) are already present, several as complete works
rather than fragments.

## 2. Cross-link opportunities

- **Claudius Apollinaris of Hierapolis's own apologetic material**,
  currently vendored in `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml`
  (div2 `x.x`, titled in the source itself "Claudius Apollinaris,
  Bishop of Hierapolis, **and Apologist**"). Currently assigned only to
  `post-apostolic-house-church` (role: tradition) and
  `montanism-the-new-prophecy` (role: context, for his separate
  anti-Montanist testimony) — **not** to this entry. The passage
  directly states he "addressed his *Apology* ... to M. Antoninus, the
  emperor" and also wrote *Adversus Gentes* and *De Veritate*; the
  actual surviving fragment quoted here (via Eusebius, *HE* v.5) is the
  "Thundering Legion" narrative — an apologetic argument that a
  Christian-soldiers' prayer, not the emperor's virtue, brought the
  rain that saved Marcus Aurelius's army against the Quadi (174 CE).
  This is real, on-topic, second-century Greek apologetic material
  distinct from his anti-Montanist writing, which correctly stays with
  the other two entries. `CORPUS-USE.md` tier: **named-never-opened**
  (the fragment sits inside an already-vendored volume under a
  different author's own div, not yet linked here at all).
- Do **not** cross-link Claudius Apollinaris's or Apollonius's
  anti-Montanist fragments (same anf08 volume, div2 `10.10` and
  `10.14`) here — checked directly, and both are inward-facing
  polemic against a Christian rival movement, not apologetic writing
  addressed to a pagan or imperial audience. A same-author,
  wrong-genre trap worth naming so a future pass doesn't assume the
  whole Apollinaris entry belongs here.

## 3. Verified acquisition leads

None found this pass. See §4 for one specific lead searched and not
resolved.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Hermias, *Irrisio Gentilium Philosophorum* ("The Mockery of Gentile Philosophers") | A genuine second-century (some date it third-century) Greek apologetic-satire work, traditionally grouped with Tatian/Athenagoras/Theophilus in older English-translation series, and currently absent from this corpus entirely (confirmed via direct search of `anf02`, the volume that already holds its usual companions). | No public-domain English translation surfaced via two archive.org title/creator searches this pass. Closed for this session, not permanently — a dedicated search under the Marcus Dods ANCL-series translation title, or the Greek text alone (Migne PG 6, alongside Tatian and Athenagoras in that volume), is worth a future pass rather than repeating these same two queries. |

## 5. Open cross-world questions

- The genre-vs-community tension is inherited from the census's own
  "why" field for this entry, not something this dossier resolves:
  "apologetic is a genre rather than a community... this is a body of
  people doing one thing in one direction for eighty years, not a
  settlement with a bishop." Nothing found this pass changes that
  framing either way — the corpus supports a genuinely coherent
  eighty-year apologetic corpus, which is a fact about the sources,
  not an answer to the constitutional question the census itself
  leaves open.
- Aristides' Apology is addressed to Hadrian (or, in one recension, to
  Antoninus Pius) and is usually dated earliest in this cluster
  (c. 124-140 CE) — worth confirming this world's own Doc_01, when
  written, states which imperial dedicatee/dating tradition it follows,
  since more than one survives in the manuscript tradition and this
  dossier doesn't adjudicate that question.
