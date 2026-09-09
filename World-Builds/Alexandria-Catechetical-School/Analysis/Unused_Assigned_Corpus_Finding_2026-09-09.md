# Unused Assigned Corpus — Peter of Alexandria, Theognostus, Pierus

**Alexandria (Catechetical-School) Formation World · finding document · 2026-09-09**

**Status:** Verified finding, independently reviewed, **escalated to the project lead — not
self-disposed.** No world-build document, no `records/alx/` record, and no compiled package
was changed by this pass. See §7.

**Scope of this pass.** A read-only discovery pass earlier this week raised a question distinct
from the citation-*accuracy* audit that closed with PR #133: not "are the existing citations
right," but "is there vendored, corpus-map-assigned source material that no `records/alx/`
record has ever drawn on, and if so, would drawing on it *change Doc_04's gravity
classifications* rather than merely add texture." That pass named two candidates. This document
verifies both from the primary sources directly, and states a disposition.

**Governing discipline.** `cic-build-cycle` (review-gated, one-document-at-a-time; four
escalation categories; a build thread never assigns Frozen and never self-disposes an
escalation-category finding) and `cic-gravity-index` (six tests; Confidence/Gravity
Cross-Check; Article 21 substitute; Interaction Matrix completeness). Both were read in full
before any file was opened.

---

## 1. Headline

**The discovery pass's central hypothesis is NOT borne out. This material is not structural.**

Nothing found here changes the Primary / Supporting / Tensional classification of any Doc_04
gravity. C1 and C2 remain Primary (literate-attested); C3, C4, C5 remain Supporting; T1–T4
remain Tensional. The six-test verdicts survive intact.

**But it is not merely supplemental either.** Three verifiable defects surfaced, one of them
**substantial by this project's own definition** (`cic-build-cycle`: a revision is substantial
if it changes "a claim's substance, a confidence rating, a sourcing conclusion, or a scope
boundary"). Two of the three are sourcing/scope errors *inside a cleared document*. They are
listed in §5.

**And the discovery pass's own load-bearing premise is wrong.** Its T1 case rested on Peter of
Alexandria being a "unique teacher+bishop+martyr overlap" — a head of the catechetical school
who was also bishop and martyr. **That claim is not attested anywhere in the vendored
material**, and the parallel claim for Pierus is **actively contradicted** by this world's own
vendored Eusebius. See §4. This is recorded as a finding in its own right, because the
corpus-map notes repeat the same overstatement and will otherwise propagate it.

---

## 2. Verification method

Everything below was read directly, not taken from the discovery pass's characterization.

| Item | Where verified |
|---|---|
| Doc_04 Gravity Discovery | `Doc_04_Gravity_Discovery.md`, read in full (all 9 sections) |
| Doc_02 Source Ecology | `Doc_02_Source_Ecology.md`, §1–§7 incl. all twelve streams |
| Corpus assignments | `cic/corpus-map/alexandria-catechetical.yaml` lines 600–740 |
| Peter — Canonical Epistle (15 canons) | `anf06…xml` div2 `ix.iv` (lines 26588–27732), Balsamon/Zonaras commentary separated out programmatically and excluded |
| Peter — doctrinal fragments (I–IX) | `anf06…xml` div2 `ix.vi` (lines 27779–28157) |
| Peter — introductory notices | `anf06…xml` div2 `ix.ii` (lines 25667–25834) |
| Theognostus — 3 *Hypotyposes* fragments + notice | `anf06…xml` div2 `vi.v` (lines 15787–15957) |
| Pierus — 2 fragments + notice | `anf06…xml` div2 `vi.vi` (lines 15957–16119) |
| Eusebius control checks | `npnf201_eusebius-church-history-life-of-constantine.xml` |
| Record absence | `grep -ri` over all of `records/alx/` |

---

## 3. What the discovery pass got right — verified

**3.1 The absence is real.** `records/alx/` contains **zero** figure records and **zero** source
records for Peter of Alexandria, Theognostus, or Pierus. A case-insensitive grep for all three
names across every record type (figure, source, gravity, story, term, quote, force,
contested_claim, doctrinal_witness, honest_limit, demonstration, voice_craft, search_record,
world_core) returns nothing. Confirmed.

**3.2 The assignment is real.** All three are assigned to this world in
`cic/corpus-map/alexandria-catechetical.yaml` at `confidence: assigned` (not provisional), all
sourced to the already-vendored `anf06` file:

- Peter — *Canonical Epistle* (`div2 9.4`), doctrinal *Fragments* (`div2 9.6`), *Genuine Acts*
  (`div2 9.3`, provisional, correctly flagged as **about** Peter not **by** him)
- Theognostus — *Hypotyposes* fragments (`div2 6.5`)
- Pierus — *Fragments* (`div2 6.6`)

**3.3 The 254–296 interval is genuinely this world's thinnest.** Doc_04 §0 names it
explicitly as an inter-phase interval "dominated by no single surviving major voice." Doc_02
Stream 5 rates the teaching tradition's institutional form **Contested**. The
`alx.gravity.learning-formation` record hard-codes the school period as **"c. 150–254"** in its
own `name` field. So the interval is not merely under-evidenced; a stated scope boundary
depends on it.

**3.4 The material is substantive, not scraps.** Peter's *Canonical Epistle* is ~11,300 words
in the ANF printing (canon text plus the 12th-c. Byzantine commentary that must be stripped);
fifteen canons of first-person, contemporaneous, documentary episcopal legislation written in
306, in the fourth year of the Diocletianic persecution, by a bishop who was himself beheaded
in 311. It is not hagiography. That distinction turns out to matter — see §5.3.

---

## 4. What the discovery pass got wrong — and this is load-bearing

**4.1 Peter did not head the catechetical school, on this evidence.** The discovery pass's
whole T1 argument depended on Peter being simultaneously school head, bishop, and martyr. I
searched the entire Peter division of `anf06` (`div1 ix`, lines 25658–28332) for
*catechetical* / *school* / *didaskaleion*. **Every hit is the American editor's general
prose about Alexandria and Antioch as centres of learning. Not one attaches Peter to the
catechetical school.** Both introductory notices — the American editor's and the translator's,
the latter following Gallandi and quoting Eusebius directly — describe Peter as bishop
(300–311), as martyr, and as praised by Eusebius for "his diligent study and knowledge of the
Holy Scriptures" and as "that excellent doctor of the Christian religion." Neither says he led
the school.

The school-headship tradition for Peter descends from Philip of Side's late and notoriously
unreliable succession list, **which is not vendored in this corpus.** The corpus-map note
("the bishop-martyr who also headed the catechetical school") is therefore more confident than
its own cited source, and should be corrected.

**4.2 Pierus's school headship is contradicted by this world's own vendored Eusebius.** The
corpus-map note calls Pierus "Head of the catechetical school." The `anf06` translator's notice
hedges to "seems to have been." But `npnf201` — Eusebius, *HE* VII.32, already a load-bearing
source record in this world (`alx.source.eusebius-historia-ecclesiastica`) — carries the
editor's note that **Achillas**, made presbyter at the same time as Pierus, "was principal of
the school," and concludes: *"Eusebius' statement must be accepted as correct, and in that case
it is difficult to believe the report of Photius… It is more probable that Photius' report is
false and rests upon a combination of the accounts of Eusebius and Jerome."* Pierus-as-school-head
is a Photian (9th-c.) report the world's own corpus already rebuts.

**4.3 Theognostus's school headship is an inference, not an attestation.** The `anf06` notice is
explicit: Theognostus is titled ἐξηγητής, and *"Dodwell and others are of opinion that by this
term* exegete *is meant the presidency of the Catechetical school."* That is a scholarly
inference from a word, offered as opinion. It is plausible — the title *Hypotyposes* is itself
taken from Clement, his predecessor in office, which is a real continuity signal — but it is not
attestation and must not be recorded as one.

**4.4 The teacher+bishop overlap is already covered.** `alx.figure.heraclas` exists precisely
for this, with the bridge line *"the pupil who took first the teacher's chair and then the
bishop's — the school and the office joined in one man,"* and its note says it is "load-bearing
for the teacher-to-bishop structural pattern (T1)." Peter would not have been the first or the
unique instance even if his headship were attested.

**Net effect on the discovery pass's case:** the "school continuity across 254–296" argument is
substantially weaker than presented. Of three claimed school heads in the interval, one is
unattested, one is contradicted, and one rests on an inference from a single word. What
survives is real but smaller, and is stated in §5.

---

## 5. The three defects that are real

### 5.1 [SUBSTANTIAL — sourcing error in a cleared document] Doc_04 §0 misattributes Theognostus to Eusebius

Doc_04 §0, in the inter-phase paragraph, states that Dionysius's episcopate and "the
post-Origen teachers (Heraclas, Theognostus) sit here, **reaching us largely through Eusebius
(HIGH-risk)**."

This is false for Theognostus. Verified two ways:

1. `anf06`'s own biographical notice opens: *"Of this Theognostus we have no account by either
   Eusebius or Jerome. Athanasius, however, mentions him more than once with honour."*
2. Control check: **`grep -c "Theognostus"` against `npnf201_eusebius-church-history…xml`
   returns 0.** Theognostus does not appear in Eusebius's *Ecclesiastical History* at all.

All three surviving Theognostus fragments come through **Athanasius** — *De Decretis Nicaenae
Synodi* 25 (frag. I, the ἐκ τῆς οὐσίας passage Athanasius deploys against the Arians) and
*Epistula* 4 *ad Serapionem* 11 (frags. II and III).

This matters beyond tidiness, because Doc_04's Eusebius HIGH-risk screen is one of its **two
governing disciplines**, applied by name to T1 and T3. Sweeping Theognostus under it both
overstates the risk on a source that does not carry it and, worse, obscures that this world
holds an **Eusebius-independent** witness from inside its thinnest interval. Under
`cic-build-cycle` this is a change to "a sourcing conclusion" — substantial, not cosmetic.

### 5.2 [SUBSTANTIAL — scope boundary] The "c. 150–254" school-period boundary is narrower than the world's own assigned corpus supports

`alx.gravity.learning-formation` fixes the school period at **c. 150–254** in its `name`, and
Doc_04 §3.5 grounds C5's Persistence PARTIAL PASS on "strongly operative early/mid (c.
150–254)."

Against the world's own assigned corpus that endpoint is too early. Theognostus (fl. c. 260)
wrote a seven-book systematic *Hypotyposes*, deliberately titled after Clement's, Origenian in
cast, and Athanasius cites him as a learned authority. Pierus (fl. c. 275) is described by
Eusebius (*HE* VII.32) as renowned for voluntary poverty, philosophical erudition, skill in
scriptural exposition, and *discoursing to the public assemblies of the Church*; Jerome calls
him "Origen the younger." Whatever their institutional titles — and §4 shows those are shaky —
the *characteristic activity C5 names* (advanced Christian teaching as itself formation)
demonstrably continues to c. 296.

Note carefully what this does **not** do. It does not touch C5's classification, and it does
not rescue the late-horizon attenuation on which the PARTIAL PASS actually rests — Theognostus
and Pierus both sit *before* 296, and the post-Nicene shift toward episcopal-doctrinal
formation is untouched. **C5 remains Supporting (temporally qualified).** What changes is a
stated date boundary and the evidential base under it. That is a scope boundary, hence
substantial.

One genuinely interesting content note, offered as texture and not as a classification
argument: Theognostus frag. III is a *pedagogical* passage — "the Saviour converses with those
not yet able to receive what is perfect, condescending to their littleness, while the Holy
Spirit communes with the perfected… the Son condescends to the imperfect, while the Spirit is
the seal of the perfected." That is C3 Divine Pedagogy vocabulary (graded capacity,
condescension, progression toward τέλειοι) in a non-Origen, non-Eusebius voice from the gap
interval. It corroborates C3; it does not reclassify it.

### 5.3 [SUBSTANTIAL — evidential characterization] T4's evidence base is described as narrower than it is

`alx.gravity.martyrdom-contemplative-tension` states that the martyr pole's "interior is
preserved in **hagiography and martyrology only** (Inferential-Thin)," and its four
`manifestations` are all Eusebius- or Dionysius-derived. Doc_04 §3.6 T4 says the same: "its
interior is Tier-3 hagiography / Coptic martyrology."

The **Inferential-Thin verdict on the martyr's interior is correct and should stand** — Peter's
canons do not give us a martyr's inner experience, and nothing here licenses filling that
silence. But "hagiography and martyrology only," as a description of *the evidence this world
holds on the martyrdom pole*, is not accurate against its own assigned corpus. Peter's
*Canonical Epistle* is documentary, first-person, contemporaneous (306, "since the fourth
passover of the persecution has arrived"), and written by a bishop who was martyred five years
later. Concretely, it contains:

- **Canons I–V** — a graded penitential scale for the lapsed, calibrated to how much torture
  was endured before yielding; those who dissembled (passed by the altars, sent substitutes)
  get six months.
- **Canon X** — clergy who *volunteered* for martyrdom, lapsed, and then resumed the contest
  are **permanently barred from sacred office** for having "left destitute the flock of the
  Lord," argued from Philippians 1:23–24: Paul knew it was better to depart and be with Christ,
  yet "to abide in the flesh is more needful for you."
- **Canon XII** — those who **paid bribes** to be left alone are not accusable; they sacrificed
  goods to save the soul.
- **Canon XIII** — those who **fled** are "not at all to be blamed," argued at length from
  Paul at Ephesus, Peter's escape from prison, and the flight into Egypt.
- **Canon XIV** — Peter cites letters *he personally received* from imprisoned martyrs
  ("as from their prison the thrice-blessed martyrs have written to me respecting those in
  Libya").
- **Fragment I** (*Letter to the Church at Alexandria*) — Meletius "has ordained in the prison
  several unto himself," and Peter interdicts communion with him.

Read together, this is the Alexandrian episcopate **deliberately de-absolutizing
martyrdom-as-formation**: flight legitimate, bribery legitimate, voluntary martyrdom by clergy
punished, lapse under torture forgivable on a scale the bishop sets, and the bishop — not
confessor-prestige — deciding who counts as a confessor. The Melitian schism in Fragment I is
exactly confessor-prestige asserting ordaining authority against the office.

**Why this is worth recording even though it changes no classification.** It sits at the
**T1 × T4 intersection** — the bishop-authority pole of T1 adjudicating the martyrdom pole of
T4 — and Doc_04 §6's Interaction Matrix has **no T1↔T4 cell**. The prose §6 states pairwise
relationships for C1↔C2, C1→C3/C4/C5, C2→C3/C4/C5, C4 as super-integrator, C5↔T2, C2↔T3,
T3↔C4, T4↔C2, and T1↔C5. T1 and T4 are never related to each other. Under `cic-gravity-index`
the Interaction Test requires that each candidate's relationship to *every other* candidate be
nameable; a demonstrable relationship left unstated is a gap in a required deliverable — though
it is not the Framework's named red flag, since T4 does carry other relationships.

### 5.4 [Separate pre-existing defect, found incidentally — flagged, not fixed here]

Doc_04 cites a companion workbook `Gravity_Index.xlsx` throughout — as carrying the full
six-test grid for all four Tensional gravities, the complete pairwise Interaction Matrix, the
By-Classification and By-Cross-Check-Flag sheets, and the Cross-Build sheet — and states it was
"last confirmed synced against this narrative: 2026-07-17."

**No such file exists anywhere in the repository.** A repo-wide `find -iname "*Gravity_Index*"`
returns only `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Gravity_Index_FINAL.xlsx` and
`world-build-docs/pahc/generate_gravity_index.py` — both World #1's.

This is outside the scope of this pass and is **not** asserted to be a fabricated-artifact
finding: the file may exist outside the repo, or may never have been committed. But it is
material to §5.3, because Doc_04 §6 explicitly defers full pairwise coverage to that workbook
("the companion `Gravity_Index.xlsx` carries this as a grid; prose summary here"). If the
workbook is absent, the T1↔T4 cell is not documented anywhere, and Doc_04's own claim of "full
pairwise coverage" has nothing standing behind it. Logged for the project lead.

---

## 6. Disposition reasoning

**Is this structural?** No. Stated plainly because the discovery pass framed it as the test:
adding these records would not move any gravity between Primary, Supporting, and Tensional, and
would not flip any of the six tests. The honest answer is that the pass **overstated its case**,
and its Peter-as-school-head premise is unsupported (§4.1) while its Pierus premise is
contradicted (§4.2).

**Is it merely supplemental?** Also no. §5.1 is a false sourcing statement in a cleared
document. §5.2 is a scope boundary narrower than the corpus supports. §5.3 is an evidential
characterization ("hagiography and martyrology only") that its own assigned corpus contradicts.
All three meet `cic-build-cycle`'s substantial threshold.

**Why this pass stopped rather than editing.** Four independent reasons:

1. **The trigger did not fire.** The brief authorized adding records and revising Doc_04 *if
   the material proved structural*. It did not. Proceeding anyway would substitute this
   thread's judgment for the condition it was given.
2. **Escalation category 4 applies.** `cic-build-cycle` sends to the project lead "a finding
   that cuts against an earlier decision." §5.1 and §5.2 cut against statements inside Doc_04,
   which cleared three independent adversarial review rounds. A build thread does not
   self-dispose these regardless of how clean its own reasoning looks.
3. **Alexandria is Frozen, not merely Approved to proceed.** The System Hub Decision Log
   records Alexandria among the frozen worlds with a signed freeze declaration
   (`Ministry/Technology/Pass2/gates/S6.2_<WORLD>_FREEZE_DECLARATION.md`), live in production.
   `cic-build-cycle`: reopening a Frozen document "may [be] require[d]… and that is normal
   process" — but Frozen is the project lead's disposition, and unfreezing is theirs to make.
4. **The change is outward-facing.** `records/alx/` is compiled by `engine/m2/compiler.py`
   into the package pinned at `packages/alx/2026-09-04T16-41-49Z` in `records/worlds.yaml` and
   served live. Any record change means recompiling and re-running the M3 admission battery
   against a deployed world. That is not a step to take on a finding the project lead has not
   seen.

**Precedent acknowledged, and why it does not settle it.**
`alx.source.alexandrian-canonical-answers.md` was added on 2026-08-27 — after the 2026-08-01
freeze — by exactly this discovery route ("found by the cross-world corpus assignment… which
assigned six npnf214 works to this world and observed no record here had opened the volume").
So post-freeze *additive source records* are established practice here, and a Peter source
record alone would fall squarely inside it. What has no precedent is the part that actually
matters: correcting sourcing and scope statements *inside* a thrice-reviewed Doc_04. Those
travel together — adding Peter while leaving §5.3's "hagiography and martyrology only" standing
would be the "bolting new citations underneath an unchanged conclusion" failure mode
explicitly named as the thing to avoid.

---

## 7. Recommendation to the project lead

Presented as grounded options with a recommendation, per `cic-build-cycle`.

**Recommended — Option B (scoped reopen).** Authorize a scoped reopen of Doc_04 covering only
§5.1, §5.2, §5.3, run through the normal revision → independent review → disposition cycle;
add three source records and up to three figure records to `records/alx/` (Peter as `figure` +
`source` on the Canonical Epistle and the doctrinal fragments; Theognostus and Pierus as
`source`, with school-headship recorded at the confidence §4 actually supports and **not** as
attested fact); correct the three overstated corpus-map notes; then recompile and re-run M3
before anything reaches production. Estimated as small in content and non-trivial in process —
the process is the point.

**Option A — record only, no Doc_04 change.** Add the source records so the corpus stops being
silently unused, and leave Doc_04 as it stands. Cheapest, and it has the 2026-08-27 precedent.
Not recommended: it leaves a false sourcing statement (§5.1) and a contradicted evidential
characterization (§5.3) in place, and produces exactly the bolt-on failure mode named above.

**Option C — log and defer.** Leave everything as it is; this document stands as the durable
record and OG-6 carries it. Defensible if Article 31 external review (OG-4) is close, since a
qualified subject-matter reviewer would see these same texts. Not recommended: §5.1 is a plain
factual error and is cheap to fix.

**Open question that is genuinely the project lead's, not this thread's.** Whether a
sourcing-and-scope correction that changes no gravity classification clears the bar for
unfreezing a live, compiled, deployed world. This thread has no basis for deciding that, and
`cic-build-cycle` is explicit that it should not try.

---

## 8. What this pass did *not* do

Stated so no later reader has to reconstruct it:

- No edit to `Doc_04_Gravity_Discovery.md` or any other Doc_01–Doc_09 file.
- No addition, edit, or deletion in `records/alx/`.
- No corpus-map edit (the three overstated notes in §4 are reported, not corrected).
- No recompile via `engine/m2/compiler.py`; no M3 battery run; `records/worlds.yaml` untouched.
- No claim that any of the above was reviewed or approved by the project lead.

Only two files are added by this pass: this document, and its independent review artifact
(`Review-Artifacts/Unused_Assigned_Corpus_Finding_Round1_Review.md`), plus the OG-6 entry in
`Open_Gaps_Tracking.md`.
