# Source Readiness Dossier — The Latin Apologists

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** I.43 (absorbed I.17, "Tertullian's Voice" — see
`Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` §2 A5)
**Corpus-map slug:** `latin-apologists`
**Time window:** c. 197–320 CE
**Region(s):** Carthage; Rome and Ostia; Sicca in Numidia; Nicomedia and
Trier
**Dossier author / date:** source-acquisition research thread, 2026-09-21;
refreshed 2026-09-29 (see the refresh note below)
**Corpus-map / `cic/texts/` state as of:** the working tree of branch
`claude/busy-pasteur-4sx229` on 2026-09-29 (HEAD `d1140c9f`). The
2026-09-21 pass was made against `main` @ commit `820550b`.

**Refresh, 2026-09-29.** This dossier was brought up to the Library as it
stood on that date. Since the 2026-09-21 pass, the original-language
witnesses for this shelf were vendored (§1), Commodian's *Carmen
apologeticum* joined the shelf in Latin, the approved window slate was
applied to the corpus map, and the Step 0 was revised with the dating
research. Findings of the 2026-09-21 pass that still hold are kept and
dated. Findings that changed are rewritten.

This candidate has five recorded rounds of independent adversarial
review (`Build/worlds/latap/Review-Artifacts/Step0_Round1_Review.md`
through `Step0_Round5_Review.md`), followed by a ruling pass, at the Step 0
(Movement-Scope Confirmation) stage:
`Build/worlds/latap/Step0_Movement_Scope_Confirmation.md`. The Step 0
did extensive, source-verified work on sourcing (B1), ecology (B2), and
built-world uniqueness (B3). Its word count of 1,194,575 was derived for
40 works, the original seven, Tertullian's 32 and the English Passion of
Perpetua; §1 says which works it does not cover. The Step 0 was revised
on 2026-09-29, and that revision has not yet been independently reviewed.
This dossier does not repeat the Step 0's work. It adds the one thing the
Step 0 does not do: a corpus-wide sweep for vendored material the Step 0
had no reason to go looking for, and a check of public-domain acquisition
candidates against the corpus-map's own live gaps.

## 1. Already assigned

All 43 works currently on `cic/corpus-map/latin-apologists.yaml`, counted
by distinct work on 2026-09-29. The generated map file has 96 rows, one
for each witness of each work: 42 rows on the ANF English volumes and 54
on original-language files. By author: Tertullian 32; Lactantius 4;
Commodian 2; Cyprian 2; Arnobius 1; Minucius Felix 1; the Passion of
Perpetua and Felicitas 1 (anonymous, transmitted with Tertullian's
corpus). Six works are `provisional` on every row and 37 are `assigned`.
Ninety-four rows have the role `tradition` and two have `transmission`.
Word counts are Step 0's own directly-recounted figures (§3 B1,
div2-boundary text extraction from the vendored ANF XML) where it states
them. A dash means Step 0 states no separate figure for that work.

| work | author | role | confidence | approx. scale | source file (key below) |
|---|---|---|---|---|---|
| The Seven Books of Arnobius Against the Heathen (Adversus Gentes) | arnobius | tradition | assigned | 140,826 words | ANF06; CSEL 4 scan; CSEL 4 TEI |
| Carmen apologeticum (Commodian) | commodian | tradition | provisional (dating disputed — see §5) | — (Latin only; not counted) | CSEL 15 TEI; CSEL 15 scan |
| The Instructions of Commodianus (Instructiones) | commodian | tradition | provisional (dating disputed — see §5) | 15,008 words | ANF04; CSEL 15 scan; CSEL 15 TEI |
| An Address to Demetrianus (Ad Demetrianum) | cyprian | tradition | assigned | — (not separately recounted) | ANF05; Hartel CSEL 3 |
| On the Vanity of Idols (Quod Idola Dii Non Sint) | cyprian | transmission | provisional (authorship disputed: compiles Tertullian and Minucius Felix) | — (not separately recounted) | ANF05; Hartel CSEL 3 |
| The Octavius of Minucius Felix | felix (Minucius Felix) | tradition | assigned | 23,819 words | ANF04; Boenig; CSEL 2 TEI; Waltzing |
| A Treatise on the Anger of God | lactantius | tradition | assigned | 20,382 words | ANF07; CSEL 27 scan |
| Fragments of Lactantius | lactantius | tradition | assigned | 3,932 words | ANF07; CSEL 27 scan |
| On the Workmanship of God | lactantius | tradition | assigned | 18,840 words | ANF07; CSEL 27 scan |
| The Divine Institutes | lactantius | tradition | assigned | 241,990 words | ANF07; CSEL 19 scan; CSEL 19 TEI |
| The Passion of the Holy Martyrs Perpetua and Felicitas | passion_of_perpetua | tradition | assigned | 7,299 words | ANF03; Robinson |
| A Treatise on the Soul (De Anima) | tertullian | tradition | assigned | 49,399 words | ANF03; CSEL 20 scan; Oehler II |
| Ad Martyras | tertullian | tradition | assigned | 2,700 words | ANF03; Oehler I |
| Ad Nationes | tertullian | tradition | assigned | 34,840 words | ANF03; CSEL 20 scan |
| Against Hermogenes | tertullian | tradition | assigned | 22,941 words | ANF03; CSEL 47 scan; Oehler II |
| Against Praxeas | tertullian | tradition | assigned | 31,174 words | ANF03; CSEL 47 scan; Oehler II |
| Against the Valentinians | tertullian | tradition | assigned | — | ANF03; CSEL 47 scan; Oehler II |
| An Answer to the Jews | tertullian | tradition | assigned | 21,645 words | ANF03; Oehler II |
| Apology (Apologeticus) | tertullian | tradition | assigned | 38,392 words | ANF03; Oehler I |
| Appendix of poems ascribed to Tertullian (Strains of Jonah, Sodom, Genesis, the Judgment; Five Books in Reply to Marcion) | tertullian | tradition | assigned | 31,817 words | ANF04 |
| De Fuga in Persecutione (Flight in Persecution) | tertullian | tradition | provisional (Montanist marker weak) | — | ANF04; Oehler I |
| On Baptism | tertullian | tradition | assigned | — | ANF03; CSEL 20 scan |
| On Exhortation to Chastity (De Exhortatione Castitatis) | tertullian | tradition | provisional | — | ANF04; Oehler I |
| On Fasting, in Opposition to the Psychics (De Jejunio) | tertullian | tradition | assigned | — | ANF04; CSEL 20 scan |
| On Idolatry | tertullian | tradition | assigned | — | ANF03; CSEL 20 scan |
| On Modesty (De Pudicitia) | tertullian | tradition | assigned | 25,582 words | ANF04; CSEL 20 scan |
| On Monogamy (De Monogamia) | tertullian | tradition | assigned | 13,554 words | ANF04; Oehler I |
| On Patience | tertullian | tradition | assigned | — | ANF03; CSEL 47 scan |
| On Prayer | tertullian | tradition | assigned | — | ANF03; CSEL 20 scan |
| On Repentance | tertullian | tradition | assigned | — | ANF03; Oehler I |
| On the Apparel of Women (De Cultu Feminarum) | tertullian | tradition | assigned | — | ANF04; Oehler I |
| On the Flesh of Christ | tertullian | tradition | assigned | 20,055 words | ANF03; Oehler II |
| On the Pallium (De Pallio) | tertullian | tradition | assigned | — | ANF04; Oehler I |
| On the Resurrection of the Flesh | tertullian | tradition | assigned | 45,592 words | ANF03; CSEL 47 scan; Oehler II |
| On the Veiling of Virgins (De Virginibus Velandis) | tertullian | tradition | provisional | — | ANF04; Oehler I |
| Scorpiace | tertullian | tradition | assigned | — | ANF03; CSEL 20 scan |
| The Chaplet (De Corona) | tertullian | tradition | assigned | — | ANF03; Oehler I |
| The Five Books Against Marcion | tertullian | tradition | assigned | 183,788 words (his largest work) | ANF03; CSEL 47 scan; Oehler II |
| The Prescription Against Heretics | tertullian | tradition | assigned | 20,653 words | ANF03; Oehler II |
| The Shows (De Spectaculis) | tertullian | tradition | assigned | — | ANF03; CSEL 20 scan |
| The Soul's Testimony | tertullian | tradition | assigned | — | ANF03; CSEL 20 scan |
| To His Wife (Ad Uxorem) | tertullian | tradition | assigned | — | ANF04; Oehler I |
| To Scapula | tertullian | tradition | assigned | — | ANF03; Oehler I |

**Source-file key.** ANF03 = `anf03_tertullian.xml`; ANF04 =
`anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`; ANF05 =
`anf05_hippolytus-cyprian-caius-novatian.xml`; ANF06 =
`anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml`;
ANF07 = `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`.
The other names are the original-language files in `cic/texts/`, listed
under **Original-language witnesses** below.

**What the 1,194,575 figure covers.** Step 0's total (464,797 for the
original seven works plus 729,778 for Tertullian's 32 works and the
English Passion) is a count of the ANF English text of 40 works. It does
not count three works now on the shelf: Cyprian's *Address to Demetrianus*
and *On the Vanity of Idols* (English in ANF05, Latin in Hartel's CSEL 3),
and Commodian's *Carmen apologeticum* (Latin only). It counts no Latin
file. This dossier states no new total and no new count. The words of
the 40 works were derived once, in Step 0, by extraction from the ANF XML,
and this dossier did not re-derive them.

**Original-language witnesses.** Header status is as each file's own
header and the `cic/texts/README.md` row state it. Under the rule in
`cic/texts/INTAKE.md`, section 2, a clean public-domain original can be
primary evidence, scan quality decides whether it can be quoted, and a
garbled scan stays a second witness until a clean witness of the same
work is vendored. Quoting from any of them still waits on verbatim
verification of each quote against the file.

- *Machine-corrected TEI* (Open Greek and Latin, University of Leipzig,
  2014; CC BY-SA 4.0; vendored 2026-09-29): CSEL 4 (Arnobius,
  Reifferscheid 1875); CSEL 15 (Commodian's *Instructiones* and *Carmen
  apologeticum*, Dombart 1887); CSEL 19 (Lactantius' *Divine Institutes*,
  Brandt 1890, without the *Epitome*); CSEL 2 (Minucius Felix's
  *Octavius*, Halm 1867, the only CSEL 2 witness). Each header says the
  OCR was corrected by the project, not a fresh human edition. They are
  the preferred base for quoting, and the scan is the check on the
  printed page. Attribution and share-alike travel with any quotation.
- *Raw OCR scans of public-domain critical editions* (left as found,
  apparatus interleaved; vendored 2026-09-29 unless stated): Arnobius,
  CSEL 4; Commodian, CSEL 15 (both poems, with Dombart's preface and
  commentary); Lactantius, CSEL 19 (*Institutes* and *Epitome*) and CSEL 27
  part 2 fascicle 1 (*On the Workmanship of God*, *On the Anger of God*, the
  fragments); Minucius Felix in Boenig (Teubner 1903) and Waltzing
  (Teubner 1912); Tertullian in CSEL 20 (Reifferscheid and Wissowa 1890;
  ten works) and CSEL 47 (Kroymann 1906; six works); and Cyprian in
  Hartel's CSEL 3, parts I and II (vendored 2026-09-05, now also assigned
  here for *Ad Demetrianum* and *Quod idola*). The Hartel header says the
  running text reads cleanly, the apparatus is noisier, and any claim
  resting on a manuscript variant needs a second source.
- *Oehler 1853* (Tertullian, *Quae supersunt omnia*, volumes 1 and 2): an
  older recension than CSEL, and the only public-domain Latin witness on the
  shelf for 15 of Tertullian's works, because the later CSEL volumes that
  carry them are in copyright. Where a work is also in CSEL 20 or 47, the
  CSEL text is the better base.
- *Robinson 1891* (Passion of Perpetua, pp. 60–95 of the printed volume,
  Latin and Greek; vendored 2026-09-08): carried on the map as the second
  witness to the English. Its header warns of scan-level noise.

Sixteen of Tertullian's 32 works have a CSEL witness and 15 more have
Oehler only; one, the *Appendix of poems*, has no Latin witness. The
*Carmen apologeticum* has no English.

**Other homes.** Several of these works are also on other shelves.
Tertullian's *Against Praxeas*, *De Fuga*, *On Exhortation to Chastity*,
*On Fasting*, *On Modesty*, *On Monogamy* and *On the Veiling of Virgins*
carry a `montanism-the-new-prophecy` co-assignment (seven works; the map's
own count, verified 2026-09-29). Praxeas is also on
`modalist-monarchianism`; *Against Marcion*, the Prescription, the Flesh of
Christ and the *Appendix of poems* are on `marcion-marcionism`; *Against the
Valentinians*, the Flesh of Christ and the Prescription are on
`valentinian-and-other-gnostic-christianities`; the *Apology* and
*Against Marcion* are on `post-apostolic-house-church`; the *Appendix of
poems* is on `apocryphal-and-pseudepigraphal-literature`; and both Cyprian
works are on `latin-pastoral-congregational-christianity` (LPC).
Lactantius' *De Mortibus Persecutorum* is on
`imperial-juridical-christianity` and not on this shelf.

## 2. Cross-link opportunities

**Checked using `CORPUS-USE.md`'s tier method against the full `cic/texts/`
directory listing, not just the volumes Step 0 already used.**

- **A real defect found and fixed in the 2026-09-21 pass, not merely
  named; re-verified 2026-09-29.**
  `cic/corpus-map/_staging/perpetua-scillitan-martyrs-lat-grc_robinson1891.yaml`
  carries the Latin/Greek critical-edition second witness (Robinson, 1891)
  for the Passion of Perpetua. Its `atlas_ids` had still pointed to
  `tertullian-s-voice`, the census entry merged into this candidate
  (`Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` §2 A5), because
  the merge run had repointed every one of Tertullian's own 32 works in the
  `anf03`/`anf04` staging files and missed this sibling file. It was
  repointed to `latin-apologists` and re-merged on 2026-09-21. On
  2026-09-29 the row is on the generated shelf (the Robinson row of the
  table in §1). The map file `tertullian-s-voice.yaml` no longer exists, so
  no stale slug remains on this shelf's own rows.
- **Hartel's CSEL 3, parts I–II, is one file on two shelves.** It is
  assigned to `latin-pastoral-congregational-christianity` as a
  whole-volume row and to this shelf for two works, *Ad Demetrianum* and
  *Quod idola*. It is the Latin original of the English ANF05 rows for
  both. Tier: same time-place, already vendored. Named here, not decided.
- **Monceaux, *Histoire littéraire de l'Afrique chrétienne*, volumes I and
  III** (`monceaux_histoire-litteraire-afrique-chretienne-tome1_1901.txt`
  and `...tome3_1905.txt`) are vendored and assigned to LPC's map, not this
  shelf. They are the one vendored secondary source that reports the
  dating debates on Minucius Felix (volume I), and on Commodian and
  Arnobius (volume III), and Step 0 §4 cites them by line. Tier: same
  time-place. Named here, not decided.
- **CIL8 (Corpus Inscriptionum Latinarum VIII), Supplementum: Inscriptiones
  Provinciae Numidiae (Cagnat/Schmidt, 1894) is vendored and assigned to
  `donatism` only (role `context`, `provisional`), not to this candidate —
  named here, not decided.** Arnobius' own city, Sicca, is in Numidia,
  and this candidate's own B5 scale claim (Step 0) already names Numidia
  as one of its regions. The epigraphic corpus's own staging note is
  explicit that it is `provisional` there too and "supports nothing on its
  own until a specific inscription is located and read" — no inscription
  has been checked against any claim either world makes. This dossier does
  not do that verification work (it is substantial and belongs to
  whichever Doc_02 reaches it first); it names the candidate cross-link so
  a future Doc_02 doesn't have to rediscover that the file exists. (Step 0
  §4 item 1 cites the Cirta inscriptions *CIL* VIII 6996 and 7095–7098
  through Monceaux; that is a different use, and CIL8's own file was not
  opened for it.)

## 3. Verified acquisition leads

None as of 2026-09-29. See §4 for the candidates checked and closed, and
for what cannot be acquired.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Commodian, *Carmen Apologeticum*, in English | Step 0 §3 B1 names it as the one Commodian work with no English text in the library | Checked against `archive.org` (title search, 2026-09-21): zero results. What surfaces under "Commodianus" is the already-vendored *Instructiones* in other 19th-century editions (the 1869 Tertullian-Victorinus-Commodianus set; ANCL vol. 18, 1870) — the same text already in `cic/texts/`, not the *Carmen*. No public-domain English translation found. The Latin is no longer missing: it was vendored on 2026-09-29 (CSEL 15 scan and TEI, §1), and the English a Representative speaks would be rendered from it. |
| Lactantius' lost letters to Demetrianus | Step 0 §2 A2/§4 item 5 names these directly: Jerome's charge against Lactantius' pneumatology is "particularly" leveled at these letters, and they are "genuinely lost and not among the vendored texts" | Not a research gap — Step 0's own account is that the letters are lost to history, not merely unvendored. No acquisition is possible. Recorded here so a later pass doesn't re-search for something that doesn't survive. |
| Jerome's *Chronicle* (Chronicon), on Arnobius' dream-and-bishop conversion story (Step 0 records the entry as 2342 / a.d. 326 in the ANF06 editor's account and 2343 / a.d. 327 in Harnack's citation) | Step 0 §2 A2 names this as the source of a detail commonly but wrongly attributed to *De viris illustribus* 79, and notes it is not among the vendored texts in `cic/texts/` | Checked against `archive.org` (2026-09-21): Jerome's continuation of Eusebius' *Chronicle* exists in public-domain Latin editions (e.g. within Migne PL 27), but no English translation was located. On 2026-09-29 the research pass found the passage's Latin in Scaliger's 1658 *Thesaurus temporum* (archive.org id `thesaurustemporu00euse`; not vendored) and quoted by Harnack. It also found that the ANF06 introductory notice already quotes the passage in English (`anf06_…xml`, lines 39070–39080), which closes the English gap for the one passage that matters. A critical edition is still not on the shelf: the 2026-09-21 pass recorded that Helm's is not public domain, while the 2026-09-29 research says Helm 1913 is public domain by date but was not found on archive.org. That disagreement is unresolved here. Step 0's B1 does not rely on the passage for any claim, and the corpus map's own note attributes the story correctly to the *Chronicle*. Not pursued further. |
| Augustine, *De haeresibus*, on Tertullian's later career (chapter 86) | Step 0 §4 item 8 needs a report from a second ancient witness on Tertullian and the New Prophecy | Only an 1721 edition was found on archive.org (2026-09-29). It is not vendored, and Step 0 does not quote it. Nothing else in the library depends on it. Recorded so a later pass knows it was checked. |
| Tertullian, CSEL 69 and 70 (the later critical volumes) | They carry the *Apologeticum* and the other works that CSEL 20 and 47 do not | In copyright, per the `cic/texts/README.md` notes on the CSEL 47 and Oehler files. Not acquirable. Oehler 1853 (vendored) is the public-domain Latin witness for those works. |
| Lactantius, *De mortibus persecutorum*, CSEL 27 part 2 fascicle 2 (1897) | The Latin original of the work IJC uses | Seen on archive.org and not vendored, per the `cic/texts/README.md` note on the CSEL 27 file. The work belongs to IJC's side of the corpus-map split, not this shelf. |
| Ebert (1868) and Norden (1897) on Minucius Felix | The two most cited arguments for the earlier dating | Not vendored, and not opened in the 2026-09-29 research pass; their positions are cited from Monceaux and Schanz–Hosius–Krüger. Not an acquisition target unless Doc_02 needs the primary argument. |

## 5. Open cross-world questions

- **Minucius Felix's and Commodian's dating.** The research is now in Step 0
  §4 item 1: both `Contested`, each range with its sources. Minucius:
  c. 160–192 or c. 200–250; the earlier range lies outside this window
  and the later one inside it and inside `roman-church-third-century`
  (I.33)'s window. Commodian: mainstream mid-third century to 313, with
  the upper end of Harnack's range crossing 320 and a minority
  fifth-century thesis (Brewer, 1906) wholly outside. The Library decision
  log entry of 2026-09-29 records the approved slate that keeps both in
  this world. This dossier does not repeat the research and does not
  attempt its own dating judgment; it is a scholarship question, not a
  sourcing one.
- **I.33 and Minucius Felix.** Checked 2026-09-29: neither I.33's census
  entry nor its Source Readiness Dossier mentions Minucius Felix or the
  *Octavius*. One touchpoint remains: I.33's census story for Callistus
  lists Tertullian's *On Modesty* (a work on this shelf) as a source.
- **Shared with LPC: Cyprian's *Address to Demetrianus* and *On the Vanity
  of Idols*** (§1, §2). `records/lpc/` now has compiled records that use
  both. Named here, not decided; no LPC record is edited.
- **A fleet-level source record uses a work on this shelf.**
  `_fleet.source.tertullian-against-praxeas` cites the ANF03 English of
  *Against Praxeas* and states that the edition "does not carry the Latin
  text." The Latin is now vendored here (CSEL 47 and Oehler II). Not
  decided.
- **Stale references elsewhere.** LPC's `world_core` record still names
  `tertullian-s-voice` as the home of the Passion's Perpetua portion. The
  census's I.43 wording says Tertullian "opened the whole enterprise in
  197" and the edge note says his *Apology* "opens the Latin case," which
  the approved slate rules Doc_01 must not say. IJC's source record for
  *De mortibus* gives the author's dates as c. 250–325 without naming the
  authorship dispute (Step 0 §4 item 6). None is edited here; each belongs
  to its own document's owner.
- **The CIL8 Numidia cross-link (§2)** is real but unverified at the
  inscription level, shared with `donatism`'s own corpus map.
- **The duplicate census entry noted in `NEEDS-RULING.md`**
  (`cyrilline-miaphysite-egyptian-tradition` vs.
  `cyrilline-miaphysite-egyptian-christianity`) does not touch this
  candidate's own roster and is not repeated here beyond this pointer.
