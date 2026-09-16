# Source Readiness Dossier — The Latin Apologists

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** I.43
**Corpus-map slug:** `latin-apologists`
**Time window:** c. 197-320 CE
**Region(s):** Carthage; Rome and Ostia; Sicca in Numidia; Nicomedia and
Trier
**Dossier author / date:** Claude (source-research thread), 2026-09-16
**Corpus-map / `cic/texts/` state as of:** commit `48e8bd470` (`main`,
2026-09-16)

## 1. Already assigned

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Seven Books of Arnobius Against the Heathen (Adversus Gentes) | arnobius | tradition | assigned | full work (~140,000 words) | anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml |
| The Instructions of Commodianus (Instructiones) | commodian | tradition | provisional | full work | anf04_tertullian4-minucius-felix-commodian-origen1-2.xml |
| The Octavius of Minucius Felix | felix | tradition | assigned | full work | anf04_tertullian4-minucius-felix-commodian-origen1-2.xml |
| A Treatise on the Anger of God | lactantius | tradition | assigned | full work | anf07_lactantius-apostolic-constitutions-didache-liturgies.xml |
| Fragments of Lactantius | lactantius | tradition | assigned | fragments | anf07_lactantius-apostolic-constitutions-didache-liturgies.xml |
| On the Workmanship of God | lactantius | tradition | assigned | full work | anf07_lactantius-apostolic-constitutions-didache-liturgies.xml |
| The Divine Institutes | lactantius | tradition | assigned | full work (7 books) | anf07_lactantius-apostolic-constitutions-didache-liturgies.xml |
| The Passion of the Holy Martyrs Perpetua and Felicitas | passion_of_perpetua | tradition | assigned | full work | anf03_tertullian.xml |
| ~30 works of Tertullian (near-complete corpus: apologetic, disciplinary, and polemical treatises) | tertullian | tradition | mostly assigned, 4 provisional | full corpus | anf03_tertullian.xml, anf04_tertullian4-minucius-felix-commodian-origen1-2.xml |

Tertullian's row is collapsed here for space — see
`cic/corpus-map/latin-apologists.yaml` directly for the full 30-line
listing (Apology, Ad Nationes, the anti-Marcion books, the disciplinary
treatises, etc.). This is, by a wide margin, the best-resourced of the
recent dossier backlog: a near-complete Tertullian, a complete Divine
Institutes, and the full Octavius are already primary-text-grounded,
not general-knowledge claims.

## 2. Cross-link opportunities

- **Cyprian's *Ad Demetrianum* ("An Address to Demetrianus")**,
  vendored in `anf05_hippolytus-cyprian-caius-novatian.xml`
  (`div3` under 4.5, Treatise V). Currently assigned only to
  `latin-pastoral-congregational-christianity`. The corpus-map's own
  note on this row already describes it in these exact terms: "Reply
  to a pagan critic blaming Christians for the empire's disasters -
  **apologetic** from inside the Latin pastoral world." Demetrianus
  was a pagan proconsul blaming Christians for plague, famine, and
  war; Cyprian's reply is squarely an apology addressed to a hostile
  outsider, the same genre this entire entry exists to hold. `CORPUS-USE.md`
  tier: **named-never-opened**.
- **Cyprian's *On the Vanity of Idols* (Quod Idola Dii Non Sint)**,
  same volume, same locus area (Treatise VI). Currently assigned only
  to `latin-pastoral-congregational-christianity`, confidence
  `provisional` — the corpus-map's own note already flags that
  authenticity is disputed because "it compiles Tertullian and
  Minucius Felix." That dependency cuts both ways for this entry: it
  is a derivative work, but derivative specifically of two authors
  *already primary here* (Tertullian, Felix), which makes it a
  plausible transmission-tier link even if its own authorship stays
  contested. `CORPUS-USE.md` tier: **named-never-opened**. Recommend
  linking with `role: transmission` rather than `tradition`, given the
  disputed authorship, if a build thread takes this up.

## 3. Verified acquisition leads

None found this pass — the entry's own resourcing is unusually strong
already, and no specific unfilled primary-text need was identified to
search against (contrast the Reformed Cities world, where a named
Doc_01 strand had no primary source at all).

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Novatian's *De Trinitate* and Caius/Gaius of Rome's fragments (same `anf05_hippolytus-cyprian-caius-novatian.xml` volume that supplied the Cyprian cross-links above) | Same era, same Rome/Carthage axis, same volume already contributing to this entry. | Checked directly: Novatian's surviving work is dogmatic theology (the Trinity) addressed to fellow Christians, not apologetic to pagans; Caius/Gaius's fragments are anti-heretical polemic (against Cerinthus and the Montanists), the same wrong-genre trap noted for Claudius Apollinaris in the Greek Apologists dossier. Neither belongs here. |

## 5. Open cross-world questions

- This entry's own census "why" field already names its central
  tension without resolving it: the five authors gathered here "are
  not one another's contemporaries, Tertullian least of all," and the
  one direct link between two of them (Arnobius to Lactantius) "rests
  on a single line in Jerome." Nothing found this pass changes that -
  the sourcing is strong precisely because each author's own corpus is
  well-preserved individually, which is a different question from
  whether they cohere as one formation-world. Not this dossier's call.
- The Passion of Perpetua and Felicitas sits in this entry with
  `role: tradition`, but it is also the founding narrative for North
  African martyr-piety more broadly and could plausibly serve a
  Carthaginian-congregational or Cyprianic-era entry too, if one
  exists and doesn't already carry it - not checked this pass, flagged
  for whichever thread owns that adjacent territory.
- If Cyprian's two apologetic works are cross-linked here per §2, worth
  noting for whoever does it: Cyprian himself is not one of this
  entry's four core authors (Tertullian, Felix, Arnobius, Lactantius,
  plus Commodian) and this would be the first Cyprian material in the
  bucket - a judgment call about whether a fifth/sixth author widens
  this entry's own already-disputed coherence question, worth a
  conscious decision rather than a silent addition.
