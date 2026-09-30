# Source Readiness Dossier — Latin Pastoral-Congregational Christianity

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** I.8
**Corpus-map slug:** `latin-pastoral-congregational-christianity`
**Time window:** c. 246–430 CE (Doc_01/Manifest scope line; the census's own
"c. 240s-430" is the same window stated less precisely)
**Region(s):** Carthage and Hippo Regius, Latin-speaking Roman North Africa
**Dossier author / date:** source-research thread, 2026-09-21
**Corpus-map / `cic/texts/` state as of:** commit `009caaf0`, 21 September 2026

**A status note this dossier exists to correct, not just record.** The
census (`cic-website/data/world-census.json`) currently lists this world as
**"Selected - Not Yet Built,"** with its own `why` field stating
"Construction has not yet begun." That is stale. A full build is already in
progress at `Build/worlds/lpc/`: Step 0 through Doc_05 (Ecological Reconstruction)
are drafted, Doc_05 has cleared two independent review rounds and is judged
"adequate to proceed to Doc_06," and the world's own
Decision Log runs to 928 lines across eleven build-thread entries. This
dossier was written the way `SOURCE-READINESS.md` directs for a world whose
"own research already happened" — from the existing `Doc_02_Source_Ecology.md`,
`Source_Registry.md`, `Source_Acquisition_Manifest.md`, and
`Step0_Movement_Scope_Confirmation.md`, not re-derived from a cold search —
because those documents already represent 30+ independently-reviewed rounds
of exactly this kind of work, done to a depth this pass does not attempt to
repeat. Flagging the census/build-status mismatch is a separate item, not
folded into this document further; see the accompanying session report.

## 1. Already assigned

`cic/corpus-map/latin-pastoral-congregational-christianity.yaml` (1,220
lines, ~90 distinct work entries) is unusually mature — independently
re-verified through Doc_02's own 30 review rounds, and
already treated by the world's own Step 0 as "a real, reasoned starting
inventory," not a first pass. What follows groups those ~90 entries by
cluster for navigability; it does not attempt to re-transcribe every row
(locus, exact confidence, and per-work note) — that detail lives in the
corpus-map file and in `Build/worlds/lpc/Source_Registry.md` (329 lines, the
build's own authoritative registry), and duplicating it here by hand would
risk introducing a transcription error the corpus-map itself doesn't have.

| cluster | representative works | role | confidence | source file(s) |
|---|---|---|---|---|
| Cyprian — English (ANF05) | *De Unitate*, *De Lapsis*, *De Mortalitate*, *De Dominica Oratione*, *Ad Demetrianum*, *Ad Fortunatum*, *Testimonia*, the 82 Epistles (one body), the 256 rebaptism council's sententiae, four disputed-authorship treatises | tradition | assigned (a few provisional, e.g. *Quod Idola*) | `anf05_hippolytus-cyprian-caius-novatian.xml` |
| Cyprian — Latin critical (Hartel, CSEL 3) | *Opera omnia*, Pars I–II (treatises + Ep. I–LXXXI); Pars III (spuria, *Vita*, *Acta Proconsularia*) | tradition | assigned | `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`, `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` |
| Pontius / Possidius (formation narratives) | *Life and Passion of Cyprian* (ANF05 + Hartel Latin); *Sancti Augustini Vita* (Weiskotten, bilingual) | tradition | assigned | `anf05…`, `cyprian_opera-spuria…`, `possidius_vita-augustini_weiskotten1919.txt` |
| Augustine — major works, English (NPNF1 01–08) | *Confessions*, *City of God*, *On Christian Doctrine*, *On the Holy Trinity*, Enchiridion, *On the Catechising of the Uninstructed*, ~97 sermons (one body), *Enarrationes in Psalmos* (~695k words, one body), 124 Tractates on John, homilies on 1 John, *Harmony of the Gospels*, *Soliloquies* | tradition | assigned (Soliloquies provisional) | `npnf101`–`npnf108` |
| Augustine — letters (English) | Jerome correspondence (17 letters, ~52.9k words); general correspondence (138 letters, ~258k words) | tradition | assigned | `npnf101_augustine-confessions-letters.xml` |
| Augustine — anti-Manichaean/anti-Donatist (English, NPNF1-04) | *On Baptism Against the Donatists*, *Answer to Petilian*, *Correction of the Donatists* (also imperial-juridical-christianity), *Contra Faustum*, *Against Fortunatus*, *De Moribus* (both halves), *Against the Epistle of Manichaeus*, *On Two Souls*, *On the Profit of Believing* (also manichaeism) | tradition | assigned | `npnf104_augustine-anti-manichaean-anti-donatist.xml` |
| Augustine — anti-Pelagian (English, NPNF1-05) | eleven treatises, *De gestis Pelagii*, *De praedestinatione sanctorum* / *De dono perseverantiae* (split; also gallic-monastic-ascetic-christianity as the provoked-reply's provoking text) | tradition | assigned (two provisional on the Gallic re-pointing) | `npnf105_augustine-anti-pelagian-writings.xml` |
| Augustine — pastoral/moral treatises (English, NPNF1-03) | *Of Holy Virginity*, *Of the Work of Monks*, *On Continence*, *On Lying*/*Against Lying* (also priscillianist-asceticism), *On the Good of Marriage/Widowhood*, *On Care to Be Had for the Dead*, *Treatise on Faith and the Creed*, Enchiridion (2nd copy), *Concerning Faith of Things Not Seen* | tradition | assigned | `npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml` |
| Augustine — Latin critical editions | *City of God* I–XIII / XIV–XXII (Hoffmann, CSEL 40); *Confessions* (Knoll, CSEL 33); *Epistulae* 1–123 / 124–184A / 185–270 (Goldbacher, CSEL 34/44/57); *Enarrationes* (Migne PL 36–37); *Retractationes* (Knoll, CSEL 36); *De Doctrina*/Enchiridion (Bruder 1838) | tradition | assigned | six standalone `augustine_*` files |
| Conciliar / institutional | *Codex Canonum Ecclesiae Africanae* (419), English (NPNF2-14) and Latin (Bruns); Council of Carthage under Cyprian (256, double-placed with novatianism-adjacent shared inheritance); *Gesta Collationis Carthaginiensis* (411 conference acts, also latin-pastoral per row-65 of the ruling) | tradition/context | assigned/provisional | `npnf214…`, `codex-canonum…`, `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` |
| Optatus, *Against the Donatists* (English; boundary-adjacent, provisional; open placement question, see §6) | Optatus of Milevis, Books I–VII | tradition | provisional | `optatus_against-the-donatists.txt` |
| Anonymous, *Treatise Against the Heretic Novatian* (c. 255) and *Treatise on Re-baptism (De Rebaptismate)* (ANF05; boundary-adjacent, provisional) | *Treatise Against the Heretic Novatian*; *De Rebaptismate* | tradition | provisional | `anf05_hippolytus-cyprian-caius-novatian.xml` |
| *Codex Theodosianus* (Imperatori Theodosiani Codex), full text, as transcribed at The Latin Library (boundary-adjacent, provisional; context, imperial legal backdrop) | Latin Library text | context | provisional | `codex-theodosianus_latinlibrary.txt` |
| Modern scholarship (context, consultation-only) | Delehaye (genre theory), Harnack (Pontius commentary), Monceaux *Histoire littéraire* I–III, von Soden ×2 (letter transmission; prosopography) | context | assigned | six standalone files, all closing named Manifest gaps (see §4) |

**Scale note:** this is, by the build's own B1/B2 assessment (Step 0 §3),
among the richest primary-source bases in the fleet — the complete Augustine
portion of NPNF Series I (eight volumes) plus the complete ANF05 Cyprian
volume, both fully vendored, plus a Latin critical-edition original behind
nearly every major English work, which most other worlds in the corpus do
not have at all.

## 2. Cross-link opportunities

**A cross-link with the Donatism world.**
The Donatism world has vendored two Latin critical
editions directly relevant to this world's own anchor author (Augustine)
and to a work already sitting in this world's own corpus-map:

- **`augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt`**
  (Petschenig's CSEL 51/52 critical edition of Augustine's anti-Donatist
  corpus) is currently linked only to `donatism.yaml`. Two of its contents
  are **the Latin original of works this world already vendors in English
  and assigns `confidence: assigned`**: *De Baptismo* (= "On Baptism,
  Against the Donatists," npnf104) and material behind "Answer to the
  Letters of Petilian." That is exactly the same-work-different-language
  pairing this world has already done systematically for Cyprian (Hartel)
  and for six of Augustine's own other major works (City of God,
  Confessions, Letters, Enarrationes, Retractationes, Enchiridion) — this
  one pairing was simply not available yet when those links were made. Two
  further contents of the same file — *Contra Cresconium* and *Contra
  Epistulam Parmeniani* — have **no English translation vendored anywhere
  in the corpus at all**: genuinely new primary Augustine content (his own
  words, in the controversy this world's own Doc_02 has already committed,
  under the Article 23 reciprocal obligation with Donatism recorded at Step
  0 §2 A5, to reconstruct "from inside this world's own perspective"), not
  presently reachable from this world's own bucket in any form.
- **`optatus_libri-vii-critical_ziwsa1893.txt`** (Ziwsa's CSEL 26 critical
  edition of Optatus) is the Latin original standing behind the English
  Optatus translation this world's own corpus-map already carries
  (`optatus_against-the-donatists.txt`, `confidence: provisional`) — the
  same pairing pattern, currently linked only to `donatism.yaml`.

Both are same-time-place (Carthage/Numidia, 4th century, Augustine's and
Optatus's own hands) by `CORPUS-USE.md`'s tier method, and both sit inside a
world this dossier's author has already independently verified reads and
cites the sibling Donatism corpus-map directly (Step 0 §2 A5, §3 B3). This
is not a new finding about *whether* the two worlds' material overlaps —
that is already fully worked out and cross-referenced — it is a finding
that **one specific pair of vendored files, added after most of that
cross-referencing happened, was never linked into this world's own bucket**.
Named here rather than assigned, per this dossier's own scope: whether to
double-place (the pattern the corpus-map already uses for the Council of
Carthage under Cyprian and for the Augustine–Jerome letters), single-place,
or leave as-is is Doc_02's or the project lead's call, not this dossier's.

**No further cross-link sweep attempted.** Given the density of the
existing review record (30 Doc_02 rounds alone), a fresh from-scratch sweep
of the whole corpus for this world would very likely re-derive work already
done and independently verified multiple times over; this pass targeted
only what changed in the corpus *since* that record was last current
(files added after the sibling Donatism build's own vendoring pass,
checked by git-log date against the whole `cic/texts/` tree) rather than
re-running the full search.

## 3. Verified acquisition leads

None beyond what the world's own Manifest already tracks. `Source_Acquisition_Manifest.md`'s
G1–G9 candidates are eight of nine closed (each independently fetched,
opened, and verified by the build thread itself once network access was
confirmed working); the ninth, **G4's remaining CSEL 58**
(Augustine *Epistulae*, praefatio and indices only — no letter text of its
own), stays open as a low-value residual the build thread deliberately
deprioritized. This dossier did not run a fresh acquisition search given
that disposition; re-running one would very likely just re-find CSEL 58 and
nothing else, since the world's own primary-source base is already
described by its own Step 0 as among the most complete in the fleet.

## 4. Checked and closed

Carried forward from the world's own Manifest, so this dossier doesn't
re-open them:

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Pellegrino's 1955 *Ponzio: Vita e martirio di San Cipriano* | Alternative critical edition of Pontius's *Life* | Confirmed in copyright; not a public-domain acquisition candidate |
| CCSL 3 / 3A / 3B–D (Weber, Bévenot, Simonetti, Moreschini, Diercks — modern Cyprian critical edition) | Current scholarly-standard Cyprian text | In copyright (Brepols); consultation-only, never a vendoring candidate |
| Mandouze's *Prosopographie chrétienne du Bas-Empire* | Prosopography of the African episcopate | Range begins 303 CE, 45 years after Cyprian's death — doesn't reach the bishops this world needs (von Soden's 1909 study, G8, was acquired instead) |
| CSEL 34/1, 34/2, 44, 57 (Goldbacher, Augustine *Epistulae*) at a single combined identifier | One-shot acquisition of the full critical letters | No single identifier exists; acquired instead as four separate, independently-verified archive.org items (G4, now closed except CSEL 58) |
| `archive.org/details/PossidiusAug` | Apparent hit for Possidius's *Vita Augustini* | Independently confirmed to be a 2008 audio recording, not a text scan; the actual scanned edition (`sanctiaugustiniv00possrich`) was found and used instead |
| "sourcelibrary.org" (unlicensed *Codex Theodosianus* "translation") | Appeared to offer a usable English rendering | Sibling Donatism build found a systematic invisible-Unicode payload on direct inspection; flagged corpus-wide as a source never to use |

## 5. Open cross-world questions

- **Optatus's world placement** — currently `provisional` in this world's
  own corpus-map, self-flagged as inferred from region and date alone
  ("Mark may prefer another Latin home for a Numidian polemicist"). The
  world's own Step 0 (§4 item 2a) names three live options — re-home to
  Donatism, hold here as the Catholic-side tradition, or double-place, the
  way the Council of Carthage under Cyprian already is — as a real,
  a placement the source ecology has to settle; it is not pre-decided. The two
  Petschenig/Ziwsa Latin critical editions (§2 above) sharpen this rather
  than resolve it: linking them here before Optatus's own placement is
  settled would make the placement harder to settle, not easier.
- **The Hilary-identity contested question**, shared with
  `gallic-monastic-ascetic-christianity`: the correspondent Augustine's *De
  correptione et gratia* and *De praedestinatione sanctorum* both address is
  Contested, not confirmed "Hilary of Arles" — this world's own corpus-map
  notes carry the correction but the identity question itself belongs to
  neither world alone.
- **The Article 3 century-gap question** (Cyprian d. 258; Augustine b. 354,
  Donatism actively contesting the interval) — the world's own Step 0
  explicitly declines to resolve this, carrying it forward as Doc_01's own
  Strand Determination work, already logged in the portfolio-level Step 0
  Conclusion as a standing, unresolved Constitutional ambiguity. Not a
  sourcing question, named here only because it bears on how §1's material
  eventually gets organized.
- **A resolved item, noted so nobody re-opens it:** the world's own Step 0
  surfaced and, with Mark's direct authorization, fixed a genuine boundary
  breach in the already-built Imperial and Juridical Christianity world's
  own records (two load-bearing quote records citing *Confessions* material
  outside IJC's own declared license). Logged in full at
  `Build/worlds/ijc/Open_Gaps_Tracking.md` item 16; mentioned here only for
  cross-reference, not reopened.
