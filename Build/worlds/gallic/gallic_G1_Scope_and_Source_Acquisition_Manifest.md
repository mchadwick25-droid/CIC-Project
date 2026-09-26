# G1 — Scope & Source Acquisition Manifest
## Gallic Monastic-Ascetic Christianity (gallic-monastic-ascetic-christianity, Atlas I.27, era 2, c. 360–450)

**Status: self-disposed under V3** (`CiC_New_World_Build_Record_Native_Launch_V3_2026-09-08.md`, on
`origin/claude/v3-launch-prompt-streamline`) — G1 no longer requires Mark's per-row approval; the
build thread finds, rights-checks, fetches, and vendors sources directly, escalating only a source
genuinely inaccessible to it. This document records what was found and decided, for the record, not
as a stop.

**Confidence key**, this project's convention: **[M]** measured/policy figure from committed
documents; **[E]** estimated from comparable fleet-build shapes; **[S]** speculative, no comparable
data.

---

## Part A — Scope

**Window:** c. 360–450. **Claim:** Atlas I.27, era 2 — `gallic-monastic-ascetic-christianity`,
status "Possible Future World (on record)" per Mark's ruling 2026-08-26
(`Build/worlds/_cross-world/CASE-gallic-monasticism.md`). G0 is pre-cleared by that record; this
document does not reopen it.

**What this world is, per the case document §4:** the monastic-ascetic ecology of Martin's Tours, the
island community at Lérins, and Cassian's houses at Marseilles — a lived ecology of people moving
between institutions (Sulpitius knew Martin; Vincent and Cassian were both of the Lérins–Marseilles
circle), with its own formation literature (Cassian's *Conferences*, Vincent's *Commonitory*), and a
distinctive theological position held under pressure (the Gallic resistance to Augustinian
predestination). Hilary of Poitiers is deliberately excluded (case §4) — a Nicene controversialist
whose Gallic location is incidental to *De Trinitate*'s actual subject.

**Open question carried into Doc_04, not settled here:** whether Martin's Tours (d. 397) and
Cassian's/Vincent's Lérins–Marseilles (Vincent d. c. 445) are one continuous formation gravity or a
lineage of two, two generations apart. The case document names this as a real six-test question, not
an assumed answer either way.

**Correction, 2026-09-08, after Doc_01's Round 1 review (finding S3):** the case document's own §4
states that removing Hilary of Poitiers "drops the figure to 366,371 words." That arithmetic is
wrong — 731,019 − 228,578 (Hilary) = **502,441**, not 366,371. **366,371 = 731,019 − 364,648
(Cassian)** — the case document's own §4 and §5 use two different, inconsistent subtractions, and §4
is the one in error (§5's "366k without him [Cassian]" is the figure's actual meaning). This document
inherited the wrong figure without checking it; the total below is corrected accordingly. The case
document itself is not this build thread's file to edit (it is a decision record, not a build
artifact), so the error is flagged here and in Doc_01 rather than silently corrected at the source.

---

## Part B — Source Acquisition Manifest

**Headline finding: no new acquisition was needed.** The entire citable library for this world was
already vendored by Mark on 2026-08-15, in the same batch that supplied the desert-monasticism and
Cappadocian libraries. What G1's work actually was: verifying the corpus-map's assignment matched
what the case document had already counted, and it did not — three real gaps, closed below.

| source_id | work / edition | rights_status | where | destination | why this edition | alternatives | scope note |
|---|---|---|---|---|---|---|---|
| gal-src-01 | *The Conferences of John Cassian* (Conferences I–XXIV), NPNF Series II, Vol. 11 | public-domain [M] — NPNF, 19th-c. translation, CCEL text | already vendored, supplied by Mark 2026-08-15 | `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` | the standard English NPNF translation; already load-bearing for desert-monasticism (srcDES026, cited by 4 of that world's documents) | none sought — this is the only open-domain English Conferences translation in the project's library | **corrected 2026-09-08 (Doc_01 review finding S17): only 22 of 24 conferences carry text in this edition** — Conference XII ("On Chastity") is marked "Not translated" and Conference XXII ("On Nocturnal Illusions") "is omitted" (verified directly in the XML, lines 37466–37475 and 46037–46045); both are sexuality/body material, a real edition-level gap worth naming alongside Doc_02's own Missing Voices work, not only a record-level one. Conference XIII (the *Protection of God* conference, central to this world's grace controversy) is in scope, no exclusion |
| gal-src-02 | *The Twelve Books on the Institutes of the Coenobia*, same volume | public-domain [M] | same file | same file | same volume, same translator; commended by Rule of Benedict ch. 73 (and ch. 42, which prescribes the *Conferences* as daily reading — an equally strong, easily overlooked half of the same link) | none sought | full text in scope. **Corrected 2026-09-08 (Doc_01 review finding S12): not "for Gallic monasteries" broadly.** The Preface itself (verified directly in the XML) addresses one named bishop, Castor of Apta Julia in Gallia Narbonensis, whose own province is described as "at present without monasteries" — a single addressee in the far Mediterranean south, not a general Gallic dedication, and it says nothing about Tours or the Loire |
| gal-src-03 | *On the Incarnation of the Lord, Against Nestorius (De Incarnatione)*, same volume | public-domain [M] | same file | same file | Cassian's own authored corpus (written from Marseilles); counted in the case document's 364,648-word Cassian figure but **not yet corpus-mapped to this world before this session** — closed today, see Part C | none sought | full seven books in scope |
| gal-src-04 | *On the Life of St. Martin*, Sulpitius Severus, same volume | public-domain [M] | same file | same file | written c. 397 in Aquitaine while Martin still lived; the founding hagiography of the world's central figure | none sought | full text in scope; hagiographic-tier caution applies at Doc_09, not here |
| gal-src-05 | *Dialogues of Sulpitius Severus*, same volume | public-domain [M] | same file | same file | continues the Martin material; Dialogue I also carries Postumianus' first-hand Egyptian-desert travel account | none sought | full text in scope |
| gal-src-06 | *The Doubtful Letters of Sulpitius Severus*, same volume | public-domain [M] | same file | same file | the edition's own attribution doubt, already ruled 2026-08-26: files under the attributed name AND as pseudepigraphal literature, both true at once | none sought | full text in scope, doubt disclosed at the record layer |
| gal-src-07 | *The Letters of Sulpitius Severus*, same volume | public-domain [M] | same file | same file | undisputed letters, distinct from the doubtful set above | none sought | full text in scope |
| gal-src-08 | *The Sacred History (Chronica)*, Sulpitius Severus, same volume | public-domain [M] | same file | same file | Sulpitius' own historical corpus; counted in his 109,539-word case-document figure but **not yet corpus-mapped to this world before this session** — closed today, see Part C | none sought | in scope as author-tradition; its Priscillianist-affair narrative (Book II) is the sharper fit for imperial-juridical-christianity and stays cross-assigned there too |
| gal-src-09 | *The Commonitory of Vincent of Lerins*, same volume | public-domain [M] | same file | same file | the classic rule for discerning catholic tradition ("quod ubique, quod semper, quod ab omnibus"), written 434 at Lérins — a genuine insider document of the school itself | none sought | full text in scope |
| gal-src-10 | *On Rebuke and Grace (De correptione et gratia)*, Augustine, NPNF Series I, Vol. 5 | public-domain [M] | already vendored, supplied by Mark 2026-08-15 | `cic/texts/npnf105_augustine-anti-pelagian-writings.xml` | the opponent's-side text that provoked the Gallic monks' objections reported to Augustine — provisional assignment, see Part C | none sought | addressed to Hadrumetum, not Gaul — in scope as context for the controversy this world holds under pressure, not as this world's own voice |
| gal-src-11 | *On the Predestination of the Saints (De praedestinatione sanctorum)*, same volume | public-domain [M] | same file | same file | Augustine's direct reply to Prosper of Aquitaine and a "Hilary" reporting the Gallic monks' objections — **corrected 2026-09-08 (Doc_01 review finding S6): this Hilary's identity is Contested, not Hilary of Arles.** This world's own vendored Commonitory introduction places Hilary of Arles among the Massilian party itself ("Honoratus and Hilary, afterwards successively bishops of Arles, and Faustus, afterwards bishop of Riez... opposed to St. Augustine's later teaching"), i.e. on the same side as the monks being reported on, not the reporter. The standard reference identification for Augustine's correspondent favors a Gallic lay monk over the bishop of Arles. Carried as Contested pending Doc_02's own resolution | none sought | full text in scope, opponent's-side witness |
| gal-src-12 | *On the Gift of Perseverance (De dono perseverantiae)*, same volume | public-domain [M] | same file | same file | companion/continuation of gal-src-11, same audience and same identity caveat | none sought | full text in scope, opponent's-side witness |

**Total citable material: ≈597,700 words**, corrected 2026-09-08 (Doc_01 review finding S3) —
Cassian + Sulpitius Severus + Vincent of Lérins, Hilary of Poitiers removed: 731,019 − 228,578 =
**502,441w** [M, case document §3 table, arithmetic redone directly], plus Augustine's ≈95,295w
opponent-side material = **597,736w**. (The case document's own §4 states this figure as "366,371,"
which is actually the total with *Cassian* removed and *Hilary* still in — see the correction note
under Part A above.) All of it already inside `cic/texts/`; zero new downloads, zero new rights
determinations, zero licensing questions (NPNF is public domain throughout).

**Two gaps first logged as "not pursued now" have since been closed as located leads, not left open**
(corrected 2026-09-08, after Doc_01's Round 2 review finding N6b, which found this file disposing of
Faustus three incompatible ways): Prosper of Aquitaine's own writings and Faustus of Riez's *De
Gratia* were both originally flagged here as unvendored gaps; both are now independently located,
rights-checked, and carried in the single leads table below — **superseding, not duplicating, this
paragraph's original framing.** Faustus's own English-translation and rights situation stands as
first found (no public-domain English edition exists — only a licensed 2023 Brepols bilingual
edition — so the Latin original is what the table below carries, second-witness rule); the treatise's
own date is corrected to **c. 473–475** (matching Doc_01 §2.4's synod dating, not the single
unlabelled "474" this file first carried). **One disposition, stated once:** both are Doc_02's own
intake queue, not a G1-lane action ahead of it, and not a PRESS-style discovery item still to be
found — the discovery is done; the intake is what remains. No source in this world's citable window
is known to be paywalled, physical-only, or otherwise genuinely inaccessible — nothing to escalate
under V3's narrowed G1 exception.

**Leads located and rights-checked (sibling session, 2026-09-08, this build thread's own
verification noted per row), not yet vendored — ready for Doc_02's own intake pass, not chased
mid-Doc_01-review:**

| work | author | where | rights | note |
|---|---|---|---|---|
| *De gratia libri duo* | Faustus of Riez | archive.org `corpusscriptorum21fausuoft` — catalogued title *"Fausti Reiensis Praeter sermones pseudo-eusebianos opera: accedunt Ruricii epistulae"* (ed. Engelbrecht, CSEL 21, 1891) [title corrected 2026-09-08 per Doc_01 Round 2 finding N5 — an earlier note here gave an invented short title] | public domain (`NOT_IN_COPYRIGHT`), independently re-verified by this build thread — see Doc_01 §2.4 | Latin only; second-witness rule applies; written c. 473–475 at the request of the synods of Arles and Lyons |
| *De Contemptu Mundi* | Eucherius of Lyon | `ccel.org/ccel/eucherius/contempt/contempt.i.html` (tr. Henry Vaughan, 1654) | public domain, CCEL's own page states so plainly | **English** — a genuine third Lérins-insider voice alongside Cassian and Vincent, different genre (epistolary renunciation essay); whether the CCEL page is complete or excerpted was not confirmed and should be checked at intake |
| *De Laude Eremi* (to Hilary of Arles, c. 428) | Eucherius of Lyon | archive.org `patrologiae_cursus_completus_lat_vol_050` (Migne PL 50, 1846), line 57093 of the OCR text | public domain (CC Public Domain Mark, genuine Google Books scan, verified) | Latin only |
| *Sermo de Vita Sancti Honorati* (Life of Honoratus, Lérins' founder) | Hilary of Arles | same Migne PL 50 volume, line 102068 (indexed at 101883) | same volume, same rights basis | Latin only; this world currently has **zero** Lérins-founding narrative in the primary corpus — this is the direct from-inside counterpart to Sulpitius's *Life of Martin*. Same volume carries further Hilary of Arles material near line 102186 worth mapping at intake |
| *Carmen de Ingratis* | Prosper of Aquitaine | archive.org `sanctiprosperiaq00prosuoft` (*Opera omnia*, Venice 1744), lines ~13774–18246 | public domain (`NOT_IN_COPYRIGHT`, University of Toronto scan) | Latin only |
| *Pro Augustino Responsiones* (= the *Responsiones ad Capitula* material later split by Migne) | Prosper of Aquitaine | same 1744 volume, lines ~19728–24516 and 87156 | same volume, same rights basis | Latin only; this older edition's internal division may not map one-to-one onto Migne's modern sub-titles — confirm at intake |

Together with Faustus, these give this world's own predestination controversy a genuinely three-sided
primary-source record once vendored: Augustine's treatises (outside rebuttal, already in hand),
Faustus (the Gallic monks' own defense), and Prosper (the Gallic-born dissenter arguing *for*
Augustine against his own milieu) — plus, independent of the controversy, Lérins' own founding
narrative (Hilary of Arles on Honoratus) and a third insider ascetic voice (Eucherius). None of this
is vendored yet. It is Doc_02's own intake queue, not this document's to execute mid-Doc_01-review.

**2026-09-09 addendum: the four rows above independently re-verified, plus two genuinely new leads
found.** A scheduled source-readiness routine flagged Salvian of Marseilles and Constantius of Lyon's
*Vita Germani* as unconfirmed candidates outside this table; both chased down directly this session
(URLs and rights bases verified against the actual host, not guessed), and added to the cross-world
`download-queue-seed.yaml` alongside the four rows above, which were themselves upgraded there from
sibling-flagged to directly re-verified (see that file and the Source Registry's own rows 24–27 for
the dated corrections). **Neither of the two new leads below has been boundary-checked against this
world's own window (Doc_01 §2) — that is a Doc_02-maintenance judgment call, not settled here.**

| work | author | where | rights | note |
|---|---|---|---|---|
| *On the Government of God (De Gubernatione Dei)* | Salvian of Marseilles | archive.org `SalvianOfMarseille.OnTheGovernmentOfGod` (tr. Eva M. Sanford, 1930) | public domain (pd-us-by-date, "opensource" collection, no lending restriction) | **English.** Salvian was a presbyter of Marseilles, Cassian's own city, writing c. 440s — squarely inside this world's temporal and geographic window on paper, but his own subject (Roman moral decline under the Vandal-era crisis) is a different register from the grace controversy or the ascetic-formation material this world's ecology has centered so far. Boundary Check and Licensed-For scope not yet done — a Doc_02-maintenance item, not decided here |
| *Vita Germani* (Life of Germanus of Auxerre) | Constantius of Lyon | archive.org `passionesvitaequesanctorum5` (MGH *Scriptores rerum Merovingicarum* VII, ed. Levison, 1920, pp. 225–283) | public domain ("Public Domain Mark 1.0") | Latin only — no public-domain English translation exists. The only English translation, F. R. Hoare's *The Western Fathers* (Sheed and Ward, 1954), is access-restricted (controlled digital lending) on every archive.org copy found and not confirmed public domain; a renewal check against Stanford's Copyright Renewal Database could not be completed this session (the host is blocked by this session's network egress proxy) — do not treat Hoare's translation as acquirable without that check actually being done. Germanus of Auxerre (not Provence/Lérins) is a looser geographic fit than Salvian's; Boundary Check not yet done |

**Vendoring, 2026-09-09 (same pass):** all six texts in this addendum and the leads table above
(Faustus, Eucherius ×2, Hilary of Arles, plus the two new leads Salvian and Germanus) fetched
directly and vendored to `cic/texts/`, headers verified by `texts_registry.py`, zero problems.
The four already-Native rows (Faustus, both Eucherius works, Hilary's Vita Honorati) are also
now corpus-map assigned to this world (`cic/corpus-map/_staging/`, merged and validated) — see
the Source Registry's own rows 24–27 for the per-row detail.

**Boundary Check, same day:** Salvian and Constantius's *Vita Germani* both received their
Boundary Check against Doc_01's own window (Doc_02 §13A, Source Registry rows 43–44), by
reading the vendored primary texts directly rather than reasoning from the geographic/temporal
coincidence alone. **Salvian: Native, Documented and corpus-map assigned** — Hilary of Arles's
own funeral sermon for Honoratus, already vendored in this world's own library, names Salvian
directly as one of Honoratus's own circle at Lérins, independently corroborated by Gennadius
(already vendored, row 30). **Constantius's *Vita Germani*: Excluded, Named Comparandum, not
corpus-map assigned** — no documented connection to Lérins, Honoratus, Cassian, or Vincent was
found in the text itself (Levison's own Prolegomena plus the edited work); the only real link
is literary (Constantius modelling his prose on Sulpitius Severus's *Life of Martin*), the same
kind of borrowed-form relationship this world's own Registry already treats as Excluded (row
34). The era-and-theme overlap with the grace controversy (Germanus fought Pelagianism in
Britain) is exactly the kind of plausible-seeming trap the Named Comparandum category exists
to flag, not evidence he belongs to this world.

---

## Part C — Corpus-map re-pointing done this session (2026-09-08)

Three real gaps between what the case document counted and what the corpus map actually held,
closed via `cic/corpus-map/_staging/` edits and a scoped `corpus_map_merge.py --write-only` run
(validated `--check` first in each case; `git diff --stat` confirmed only additive note changes to
the two other buckets each edit touched — no content removed from desert-monasticism,
imperial-juridical-christianity, latin-pastoral-congregational-christianity, or pelagianism):

1. **Cassian's *De Incarnatione*** — assigned to desert-monasticism and imperial-juridical-christianity
   only; not to this world, despite being counted in the case document's Cassian word figure. Added
   as `tradition`/`assigned`, on the same author-corpus basis already carrying the Institutes and
   Conferences.
2. **Sulpitius Severus' *Sacred History*** — assigned to imperial-juridical-christianity and
   priscillianist-asceticism only; not to this world, despite being counted in the case document's
   Sulpitius word figure. Added as `tradition`/`assigned` alongside his other three works.
3. **Augustine's *On Rebuke and Grace*, *On the Predestination of the Saints*, *On the Gift of
   Perseverance*** — the sibling-flagged item: already vendored via the Latin Pastoral-Congregational
   build, assigned to `pelagianism` and `latin-pastoral-congregational-christianity` only. Added to
   this world with a real distinction the case document's own summary had blurred: only the latter
   two are actually addressed to Prosper and a correspondent named "Hilary" (`assigned`) — **corrected
   2026-09-08, after Doc_01's Round 2 review (finding N6a): this correspondent's identity is
   Contested, not Hilary of Arles.** This world's own vendored Commonitory introduction places Hilary
   of Arles among the Massilian party itself, on the side being reported on, not among the reporters;
   the standard reference identification favors an otherwise-unknown Gallic lay monk. This corrects
   the same row this file itself first mis-stated two sections above the original fix (Round 1 finding
   S6) — the earlier correction had not been propagated to this paragraph. *On Rebuke and Grace* was
   addressed to Hadrumetum in North Africa, not Gaul, and is included `provisional` — it is the text
   that provoked the Gallic objections the other two answer, not itself a Gallic-addressed work. The
   distinction is disclosed in each work's own corpus-map note, not smoothed over.

   **Correction, 2026-09-08, after Doc_02's Round 1 review (finding S25):** the claim two paragraphs
   above — "the distinction is disclosed in each work's own corpus-map note, not smoothed over" — was
   itself false when written. The Round 2 (Doc_01) fix had landed in the generated corpus-map bucket's
   then-current copy but had never actually been applied to `cic/corpus-map/_staging/npnf105_augustine-anti-pelagian-writings.yaml`,
   the file that actually generates that bucket — so a later merge would have silently reverted it,
   and in fact the bucket still read "Hilary of Arles" when Doc_02's reviewer checked it. Fixed at the
   root in the staging file and re-merged (commit `188ebba`), verified clean. **This is the third
   instance in this build's own history of a correction being announced in one file without being
   propagated to the record it was actually about** (Doc_01 Round 2 finding N6 found the same shape of
   defect in this file once already; this is a second, independent occurrence). Flagged here as a
   standing pattern worth this fleet's coach-thread attention, not something this build thread can
   fully guard against by more careful writing alone — the actual fix is to grep the target file
   directly after any "corrected" claim, not to trust the claim.

**Not done, and not needed:** no `cic/texts/INTAKE.md` run — nothing new entered `cic/texts/` this
session, only corpus-map re-pointing of already-vendored, already-registered files.

---

## What Mark decides here

Under V3, nothing — this gate is self-disposed. Recorded for the audit trail. The one item worth
his eye if he wants it: the *On Rebuke and Grace* `provisional` call in Part C item 3, since it is a
judgment call (include the provoking text at lower confidence, vs. leave it out entirely) rather than
a mechanical fact. Not a blocker; Doc_04 will re-test it against the actual six-test assessment when
gravities are classified.
