# Unused Assigned Corpus — Peter of Alexandria, Theognostus, Pierus

**Alexandria (Catechetical-School) Formation World · finding document · 2026-09-09**

**Version:** Round 2 draft (Round 1 revised). **Round 1 review:**
`Review-Artifacts/Unused_Assigned_Corpus_Finding_Round1_Review.md` — **SUBSTANTIAL REVISION
REQUIRED**, 8 substantial + 8 cosmetic, headline conclusion upheld. All 8 substantial findings
are addressed below and the revision log is §9. AI review, marked in its own artifact
*"Simulated review — informational only, not an Article 31 substitute"* (Article 31).
**Round 2 review pending — this document is not cleared.**

**Status:** Verified finding, **escalated to the project lead — not self-disposed.** No
world-build document, no `records/alx/` record, and no compiled package was changed by this
pass. See §8.

**Scope of this pass.** A read-only discovery pass earlier this week raised a question distinct
from the citation-*accuracy* audit that closed with PR #133: not "are the existing citations
right," but "is there vendored, corpus-map-assigned source material that no `records/alx/`
record has ever drawn on, and if so, would drawing on it *change Doc_04's gravity
classifications* rather than merely add texture." That pass named two candidates. This document
verifies both from the primary sources directly, and states a disposition.

**Governing discipline.** `cic-build-cycle` (review-gated; four escalation categories; a build
thread never assigns Frozen and never self-disposes an escalation-category finding) and
`cic-gravity-index` (six tests; Confidence/Gravity Cross-Check; Article 21 substitute;
Interaction Matrix completeness). Both were read in full before any file was opened.

---

## 1. Headline

**The discovery pass's central hypothesis is NOT borne out. This material is not structural.**

Nothing found here changes the Primary / Supporting / Tensional classification of any Doc_04
gravity. C1 and C2 remain Primary (literate-attested); C3, C4, C5 remain Supporting; T1–T4
remain Tensional. The six-test verdicts survive intact, and so does the Article 21
cross-stratum substitute (§6 — run explicitly, at Round 1 review's direction).

**But it is not merely supplemental either.** Four verifiable defects surfaced, three of them
**substantial by this project's own definition** (`cic-build-cycle`: a revision is substantial
if it changes "a claim's substance, a confidence rating, a sourcing conclusion, or a scope
boundary"). See §5.

**The discovery pass's own load-bearing premise is wrong, and its wrongness protects Doc_04.**
Its T1 case rested on Peter of Alexandria being a "unique teacher+bishop+martyr overlap." That
claim is unattested in the vendored material, and the parallel claim for Pierus is contradicted
by this world's own vendored Eusebius (§4). Round 1 review supplied the sharper consequence,
adopted here: **had the pass been right, it would have been evidence *against* T1, not for it**
— Doc_04 §3.6 requires a Tensional gravity to have "two genuinely distinct poles with real
population, institutional, or practice-cluster separation (**not a polarity within one
person**)." A single man who was simultaneously school head and bishop is the disqualifying
case. §4 therefore defends T1 rather than extending it.

**The gap is wider than the pass reported, and has a single identifiable cause** (§3.5, §7).

---

## 2. Verification method

Everything below was read directly, not taken from the discovery pass's characterization.

| Item | Where verified |
|---|---|
| Doc_04 Gravity Discovery | `Doc_04_Gravity_Discovery.md`, read in full (all 9 sections) |
| Doc_02 Source Ecology | `Doc_02_Source_Ecology.md`, §1–§7 incl. all twelve streams |
| Corpus assignments | `cic/corpus-map/alexandria-catechetical.yaml`, parsed programmatically (all 14 anf06-sourced rows enumerated; the npnf214 row found by the same parse) |
| Peter — Canonical Epistle | `anf06…xml` div2 `ix.iv` (lines 26588–27732); Balsamon/Zonaras commentary separated programmatically. **Canon IX re-extracted separately from line 27036** after Round 1 review's canon-count finding exposed that the first pass's regex had silently dropped it |
| Peter — doctrinal fragments I–IX | `anf06…xml` div2 `ix.vi` (lines 27779–28157) |
| Peter — introductory notices + Elucidations | `anf06…xml` div2 `ix.ii` (25667–25834) and `ix.vii` (28157–28332) |
| Theognostus — 3 fragments + notice | `anf06…xml` div2 `vi.v` (lines 15787–15957) |
| Pierus — 2 fragments + notice | `anf06…xml` div2 `vi.vi` (lines 15957–16119) |
| Eusebius control checks | `npnf201_eusebius-church-history-life-of-constantine.xml` |
| Record absence + record-store cross-checks | `grep -ri` over all of `records/alx/`; `alx.figure.didymus`, `alx.figure.heraclas`, `alx.contested.didaskaleion-institution`, `alx.search.unopened-volume-sweep`, `alx.source.alexandrian-canonical-answers` read in full |
| Freeze status | `Open_Gaps_Tracking.md`; `Ministry/Technology/Pass2/gates/S6.2_ALX_FREEZE_DECLARATION.md` |

---

## 3. What the discovery pass got right — verified

**3.1 The absence is real.** `records/alx/` contains **zero** figure records and **zero** source
records for Peter of Alexandria, Theognostus, or Pierus, across all fourteen record types.
(Control note: a bare grep for `peter` returns two Origen commentary records — the apostle and
the *Gospel of Peter*, not the bishop. A grep for `peter of alexandria` returns nothing.)

**3.2 The assignment is real — and covers four Peter works across two volumes.**
*Corrected at Round 1 review, which caught a factual error here: the first draft said all
assignments were sourced to anf06. They are not.*

From **anf06**, at `confidence: assigned`: Peter's *Canonical Epistle* (`div2 9.4`), Peter's
doctrinal *Fragments* (`div2 9.6`), Theognostus's *Hypotyposes* fragments (`div2 6.5`), Pierus's
*Fragments* (`div2 6.6`). At `provisional`: Peter's *Genuine Acts* (`div2 9.3`, correctly
flagged as **about** Peter, not **by** him).

From **npnf214** (`npnf214_seven-ecumenical-councils.xml`), at `confidence: assigned`: **"The
canons of Peter of Alexandria, from his Sermon on Penitence"** (`div2 17.6`, ~551 words) — a
**second vendored witness to the same text**, split out on 2026-08-26 and carrying its own note
that this duplicates the anf06 Canonical Epistle. Any remediation must handle both witnesses or
explicitly decline one; §7's options are written accordingly.

**3.3 The 254–296 interval is genuinely this world's thinnest.** Doc_04 §0 names it as an
inter-phase interval "dominated by no single surviving major voice." Doc_02 Stream 5 rates the
teaching tradition's institutional form **Contested**. Confirmed.

**3.4 The material is substantive, not scraps.** Peter's *Canonical Epistle* is documentary,
first-person, and contemporaneous — written in 306, "since the fourth passover of the
persecution has arrived," by a bishop beheaded in 311. It is not hagiography, and that
distinction is what §5.3 turns on.

*Two measurement corrections from Round 1 review, both accepted.* (a) The ANF section totals
~11,300 words, but most of that is the interleaved 12th-century commentary of Balsamon and
Zonaras; **Peter's own canon text is ~3,900 words.** (b) ANF prints **fifteen** numbered
canons, but Canon XV is on the Wednesday/Friday fast and Sunday non-kneeling, not on the
lapsed — so the corpus map's and NPNF's "**fourteen penitential canons**" is the correct
description and is used here. Canon XI is additionally marked in ANF's own apparatus as
disputed in the parallel Gregory series; Peter's Canon XI is not so marked.

**3.5 The gap is wider than the pass reported.** Of **14 works assigned to Alexandria from
anf06, only 2 are opened** by any source record (`alx.source.gregory-address-to-origen`,
`alx.source.dionysius-extant-fragments`). Twelve are unopened. Beyond the three named by the
discovery pass, the unopened set includes at `confidence: assigned`:

- **Alexander of Alexandria, *Epistles on the Arian Heresy and the Deposition of Arius*** —
  Peter's successor-but-one, and the primary documents of the Arian controversy's opening *in
  Alexandria*. Doc_04 §3.6 grounds T3's confirmation on exactly this late-horizon,
  Eusebius-independent boundary-drawing material. **Zero records.**
- **Dionysius of Alexandria, *Exegetical Fragments*** — a second Dionysius work, distinct from
  the *Extant Fragments* the world does open.

and at `provisional`: Phileas (eyewitness material on the Alexandrian martyrs), Theonas,
Anatolius, Pamphilus, Methodius. All have zero records.

Alexander is arguably a stronger candidate than anything the discovery pass named. It is
**named here and not pursued** — running it properly is its own pass, and this document should
not quietly expand into an audit it has not done.

---

## 4. What the discovery pass got wrong

**4.1 Peter did not head the catechetical school, on this evidence.** I searched the entire
Peter division of `anf06` (`div1 ix`, lines 25658–28332, including the *Genuine Acts*) for
*catechetical* / *school* / *didaskaleion*. **Every hit is the American editor's general prose
about Alexandria and Antioch as centres of learning. Not one attaches Peter to the school.**
Both introductory notices describe Peter as bishop (300–311), as martyr, and as praised by
Eusebius for "his diligent study and knowledge of the Holy Scriptures" and as "that excellent
doctor of the Christian religion." Neither says he led the school.

The school-headship tradition for Peter descends from Philip of Side's late and unreliable
succession list, **which is not vendored in this corpus.** The charge here is precise and
limited: the corpus-map note ("the bishop-martyr who also headed the catechetical school")
states as fact something its own cited source does not carry.

**4.2 Pierus's school headship is contradicted by this world's own vendored Eusebius.** The
corpus-map note calls Pierus "Head of the catechetical school"; `anf06`'s translator hedges to
"seems to have been." But `npnf201` — Eusebius, *HE* VII.32, already load-bearing here as
`alx.source.eusebius-historia-ecclesiastica` — carries the editor's note that **Achillas**, made
presbyter at the same time as Pierus, "was principal of the school," and concludes: *"Eusebius'
statement must be accepted as correct… It is more probable that Photius' report is false and
rests upon a combination of the accounts of Eusebius and Jerome."*

**4.3 Theognostus's school headship is an inference, not an attestation.** `anf06`'s notice is
explicit: he is titled ἐξηγητής, and *"Dodwell and others are of opinion that by this term*
exegete *is meant the presidency of the Catechetical school."* Scholarly opinion about a word.
Plausible — the title *Hypotyposes* is taken from Clement, his predecessor in office, a real
continuity signal — but not attestation, and it must not be recorded as one.

**4.4 The teacher+bishop overlap is already carried.** `alx.figure.heraclas` exists for exactly
this, with the bridge line *"the pupil who took first the teacher's chair and then the
bishop's — the school and the office joined in one man,"* noted as "load-bearing for the
teacher-to-bishop structural pattern (T1)."

**4.5 Net effect — restated, because the first draft overstated it.** *Round 1 review was right
that the original wording ("the school continuity argument is substantially weaker") overreached.*
The vendored Eusebius **does** attest school continuity through this interval: *HE* VII.32
places **Achillas** over the catechetical school in precisely the window at issue. What is
weakened is narrower and should be stated as exactly that: **the headships of these three
particular men.** One is unattested (Peter), one is contradicted (Pierus), one is an inference
from a single word (Theognostus).

This lands on ground the record store already holds. `alx.contested.didaskaleion-institution`
carries the institutional succession at **Contested**, and concedes precisely the right thing:
*"A real tradition of learned Christian teaching in Alexandria across the whole horizon is not
in doubt… What is contested is its INSTITUTIONAL form and continuity."* The three corpus-map
notes calling these men "Head of the catechetical school" therefore do not merely overstate
their own sources — **they contradict a record this world already holds**, and its stated voice
consequence ("the Representative may speak of teachers and the teaching tradition freely, but
never of 'the School' as a documented continuous institution").

---

## 5. The defects that are real

### 5.1 [SUBSTANTIAL — sourcing error in a cleared document] Doc_04 §0 misattributes Theognostus to Eusebius

Doc_04 §0 states that Dionysius's episcopate and "the post-Origen teachers (Heraclas,
Theognostus) sit here, **reaching us largely through Eusebius (HIGH-risk)**."

False for Theognostus. Verified two ways:

1. `anf06`'s biographical notice opens: *"Of this Theognostus we have no account by either
   Eusebius or Jerome. Athanasius, however, mentions him more than once with honour."*
2. Control check: **`grep -c "Theognostus"` against `npnf201_eusebius-church-history…xml`
   returns 0.** He does not appear in the vendored *Ecclesiastical History* at all.

All three fragments come through **Athanasius** — *De Decretis* 25 (frag. I, the ἐκ τῆς οὐσίας
passage deployed against the Arians) and *Ep.* 4 *ad Serapionem* 11 (frags. II, III).

*Grounding corrected per Round 1 review.* The first draft called the Eusebius screen "one of
[Doc_04's] two governing disciplines." It is not: Doc_04 §0's two named disciplines are the
**Origen SYSTEMIC screen** and the **desert cross-build constraint**, with Eusebius a distinct
subordinate screen inside Discipline One. The finding stands on narrower and firmer ground —
it is a false sourcing statement about a named figure, which `cic-build-cycle` classes as
substantial ("a sourcing conclusion"), and it obscures that this world holds an
**Eusebius-independent** witness from inside its thinnest interval.

**Counter-weight, which must travel with it.** Theognostus reaches us *because Athanasius
quoted him in anti-Arian polemic*, and Doc_02 Stream 12 carries an explicit author-gravity note
on exactly that: "Athanasius's post-Nicene concentration risks making doctrinal conflict appear
more central to *ordinary* formation than it was." Trading a HIGH Eusebius screen for an
unexamined Athanasius mediation would be no gain. The fragments are selected, post-Nicene,
polemically-framed quotation.

### 5.2 [SUBSTANTIAL — pre-existing internal contradiction, not produced by this corpus] The C5 school-period boundary

*Materially restated per Round 1 review, which found the original framing both weaker than the
evidence and wrongly attributed to the unused corpus.*

`alx.gravity.learning-formation` fixes the school period at **"c. 150–254"** in its `name`, and
Doc_04 §3.5 grounds C5's Persistence PARTIAL PASS on "strongly operative early/mid (c.
150–254)." But `alx.figure.didymus` — already in the record store — describes Didymus as
**"head of the Alexandrian teaching tradition for roughly half a century, to 398,"** with the
bridge line "the blind teacher who held the school's chair for fifty years."

**Two live records contradict each other on the school's own duration, and neither Peter,
Theognostus, nor Pierus is needed to see it.** The unused corpus adds Theognostus (fl. c. 260)
and Pierus (fl. c. 275) in the middle of the disputed span, but the contradiction is
pre-existing and stronger than the version this document reported in Round 1.

**This does not flip C5's Persistence verdict, and the disproof is also already in the record
store.** If Persistence measured whether advanced teachers existed, Didymus-to-398 would have
flipped it long ago. It does not: Doc_04 §3.5 and the record's own description make the test
about *formation's centre of gravity moving to the episcopal-doctrinal channel* under the
post-Nicene authority shift. Two more mid-interval teachers cannot move that, and neither can
Didymus. **C5 remains Supporting (temporally qualified).** What needs reconciling is the
date-boundary wording across two records — which is a scope boundary, hence substantial.

*Texture, offered as corroboration and explicitly not as a classification argument:*
Theognostus frag. III is a pedagogical passage — "the Saviour converses with those not yet able
to receive what is perfect, condescending to their littleness, while the Holy Spirit communes
with the perfected… the Son condescends to the imperfect, while the Spirit is the seal of the
perfected." That is C3 Divine Pedagogy vocabulary in a non-Origen voice from the gap interval.
It corroborates C3; subject to the Athanasius caveat in §5.1, it reclassifies nothing.

### 5.3 [SUBSTANTIAL — evidential characterization] T4's evidence base is described as narrower than it is

`alx.gravity.martyrdom-contemplative-tension` states the martyr pole's "interior is preserved in
**hagiography and martyrology only** (Inferential-Thin)"; Doc_04 §3.6 T4 says the same. *Round 1
correction accepted:* three of that record's four `manifestations` are Eusebius/Dionysius-derived,
not all four — the fourth is the contemplative pole (*Stromateis* / the *Address*).

The **Inferential-Thin verdict on the martyr's interior is correct and stands.** Peter's canons
give no martyr's inner experience, and nothing here licenses filling that silence. But
"hagiography and martyrology only," as a description of *the evidence this world holds on the
martyrdom pole*, is contradicted by its own assigned corpus:

- **Canon IX** — *the strongest datum in the epistle, and missed in Round 1* (a regex silently
  dropped it; recovered from line 27036 only because Round 1 review's canon-count finding forced
  a re-extraction). On those who "as it were from sleep, themselves leap forth upon a contest":
  they are to be communed with, but they "take no heed unto His words" — Christ "often retired
  from those who would lay snares for Him," "delivered not up Himself," and the decisive
  clause: *"they will deliver you up, and **not, ye shall deliver up yourselves**."* This is
  explicit, argued discouragement of voluntary martyrdom.
- **Canon X** — clergy who volunteered, lapsed, then resumed the contest are **permanently
  barred from office** for having "left destitute the flock of the Lord" (argued from Phil.
  1:23–24).
- **Canon XII** — those who **paid bribes** to be left alone are not accusable.
- **Canon XIII** — those who **fled** are "not at all to be blamed" (Paul at Ephesus; Peter's
  escape; the flight into Egypt).
- **Canons I–V** — a graded penitential scale calibrated to how much torture preceded yielding.
- **Canon XIV** — Peter cites letters he personally received from imprisoned martyrs ("as from
  their prison the thrice-blessed martyrs have written to me respecting those in Libya").
- **Fragment I** — Meletius "has ordained in the prison several unto himself"; Peter interdicts
  communion with him.

Together: the Alexandrian church **deliberately de-absolutizing martyrdom-as-formation** —
flight legitimate, bribery legitimate, self-offering discouraged from Christ's own example,
lapse forgivable on a set scale, and the bishop rather than confessor-prestige deciding who
counts as a confessor. Fragment I is confessor-prestige asserting ordaining authority against
the office.

**A qualification that must travel with this, from ANF's own Elucidation II** (searched but not
read in Round 1): "Like the famous Canonical Epistles of St. Basil, however, these are
**compilations of canons accepted by the churches of his jurisdiction**… not written in the
form of personal letters, but after the manner of synodical decisions." So this is not one
bishop's private opinion. That *strengthens* the ecclesial reading — it is the church's
received discipline — while forbidding any framing of it as Peter's personal interior voice.

**Why this is worth recording though it changes no classification.** It sits at the **T1 × T4
intersection** — T1's bishop-authority pole adjudicating T4's martyrdom pole — and Doc_04 §6's
Interaction Matrix has **no T1↔T4 cell**. §6 names C1↔C2, C1→C3/C4/C5, C2→C3/C4/C5, C4 as
super-integrator, C5↔T2, C2↔T3, T3↔C4, T4↔C2, and T1↔C5. T1 and T4 are never related. Under
`cic-gravity-index`'s Interaction Test a demonstrable relationship left unstated is a gap in a
required deliverable — though not the Framework's named red flag, since T4 carries other
relationships.

### 5.4 [SUBSTANTIAL — omitted in Round 1] T3 was never examined, and Peter bears on it directly

*Added at Round 1 review's direction.*

Doc_04 §3.6 T3 (Speculative-Freedom vs Doctrinal-Boundary) states that the mid-horizon
Origen–Demetrius instance is "HIGH-risk and thin," so "the confirmation is deliberately
**shifted to the late-horizon evidence** (the homoousian boundary, the Origenist controversy)
which is well-attested and *independent of Eusebius*."

Peter's **Fragment VI** ("Of the Soul and Body," headed in ANF *"From his demonstration that
the soul was not pre-existent to the body"*) argues that man "was not formed by a conjunction of
the body with a certain **pre-existent** type." That is Alexandrian episcopal
boundary-maintenance against the central Origenian doctrine, **c. 300 — pre-Nicene,
Eusebius-independent, and sitting inside the very interval Doc_04 calls thin.** T3's evidence is
therefore not the "thin middle, strong late" shape Doc_04 describes.

This **strengthens T3's evidential base; it does not reclassify it.** T3 already PASSes and is
already Tensional. Recorded because Doc_04 makes an explicit, checkable claim about *where* T3's
confirmation rests, and that claim is incomplete against the world's own assigned corpus. Note
also §3.5: Alexander of Alexandria's *Epistles on the Arian Heresy* — unopened — is the
late-horizon end of this same evidential chain.

### 5.5 [Separate pre-existing defect, flagged not fixed] `Gravity_Index.xlsx` is not in the repository

Doc_04 cites a companion workbook throughout — carrying the full six-test grid for all four
Tensionals, the complete pairwise Interaction Matrix, the By-Classification and
By-Cross-Check-Flag sheets, and the Cross-Build sheet — "last confirmed synced against this
narrative: 2026-07-17."

A repo-wide `find -iname "*Gravity_Index*"` returns only World #1's
(`World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Gravity_Index_FINAL.xlsx`) and
`world-build-docs/pahc/generate_gravity_index.py`. **No Alexandria workbook exists anywhere in
the repository.**

This is outside this pass's scope and is **not** asserted to be a fabricated-artifact finding —
the file may exist outside the repo, or may never have been committed. But it is material to
§5.3: Doc_04 §6 explicitly defers full pairwise coverage to that workbook ("the companion
`Gravity_Index.xlsx` carries this as a grid; prose summary here"). If it is absent, the T1↔T4
cell is documented nowhere, and Doc_04's claim of "full pairwise coverage" has nothing standing
behind it.

---

## 6. The Article 21 substitute (Cross-Stratum Test) — run explicitly

*Added at Round 1 review's direction; the one route to a structural change this document had
not tested.*

Doc_04 §5 declares the **Cross-Stratum Test** as its Article 21 substitute, asks of each
gravity whether it is "attested across registers (literate/non-literate, Greek/Coptic,
urban/desert), or only within the literate-Greek stratum," and finds every Primary and
Supporting gravity attested within the literate-Greek stratum only. That divergence is OG-4,
the build's highest-stakes open item, deferred to Article 31.

**Peter's canons are the strongest candidate in this corpus for crossing that line**, and must
be tested rather than assumed. They legislate for the whole church under persecution — Christian
slaves sent to sacrifice by their masters (Canon VI) and the masters themselves (Canon VII),
those who bribed (XII) and fled (XIII), and Canon XV's ordinary rhythm of the Wednesday and
Friday fast and not kneeling on the Lord's day. That is closer to ordinary-believer conditions
than almost anything else the world holds.

**It still fails, and the reasoning is already in the record store.** A literate Greek bishop
ruling *about* the lapsed is evidence of the *conditions* of ordinary believers' lives, not
evidence of what the majority *organized around*. This is exactly the distinction
`alx.source.alexandrian-canonical-answers` already draws for the closely-parallel Timothy
canons: "This is a bishop's desk, not a school… It is evidence about the conditions of ordinary
believers' lives, which this world says it lacks," and explicitly not a filling of the honest
limit it sits next to. The same discipline applies here, and Doc_02 §6's governing warning
governs: "evidential visibility must not be silently converted into ecological visibility."

**Result: the Cross-Stratum Test outcome is unchanged. OG-4 stands exactly where it stood.**
Recorded because a negative result on the highest-stakes open item is worth having on the
record, and because §7's Option B would otherwise leave a reader wondering whether it was
checked.

---

## 7. Root cause — why this was missed

Alexandria **did** receive a discovery sweep: `alx.search.unopened-volume-sweep` (2026-08-27).
It is not a missing gate. Its **query** is the cause:

> "Every vendored volume on cross_world's second-hand-source list for this world — **volumes
> whose principal author this world NAMES while never opening that author's own works.**"

The instrument works at **volume granularity**. Alexandria already opens anf06 (for Gregory's
*Address* and Dionysius's *Extant Fragments*), so anf06 was never an "unopened volume" — and the
twelve other assigned works *inside* it were structurally invisible to the sweep. The sweep
found four volumes, opened one, and declined three with good reasoning.

Its own `divergence_note` reads the short result as a sign of health: *"The shortest list in the
fleet… and the reason is that this world had already opened twelve volumes including all three
of its own principals in their own editions. A short second-hand list is what a well-sourced
world looks like from this observer's angle."*

**That inference is backwards for this failure mode.** The more volumes a world opens, the more
of its assigned works hide *inside* opened volumes, and the smaller its unopened-volume list
becomes. Alexandria is the fleet's most-opened world, so it is the most exposed to a
volume-granularity sweep and the least likely to look exposed. The partial compensation came
from elsewhere: `alx.source.alexandrian-canonical-answers` was added the same day by a
*different* instrument — the cross-world corpus assignment, which is work-granular and "observed
no record here had opened the volume" for npnf214.

**This is the most portfolio-relevant thing in this document.** The remedy is a work-granularity
check — diff the corpus map's assigned works for a world against the works its source records
actually open — and it is mechanical, cheap, and runnable for every world, not just this one.
Whether to run it fleet-wide is a portfolio-level decision and therefore the project lead's
(`cic-build-cycle` escalation category 2).

---

## 8. Disposition reasoning

**Is this structural?** No — stated plainly, because the discovery pass framed it as the test.
No gravity moves between Primary, Supporting and Tensional; no test verdict flips; the Article
21 substitute is unchanged (§6). The pass **overstated its case**, its Peter premise is
unsupported (§4.1), its Pierus premise is contradicted (§4.2), and had its central premise been
right it would have damaged T1 rather than supported it (§1).

**Is it merely supplemental?** No. §5.1 is a false sourcing statement in a cleared document;
§5.2 is a live contradiction between two record-store records on a scope boundary; §5.3 and
§5.4 are evidential characterizations contradicted by the world's own assigned corpus. §7 is a
methodological finding with fleet-wide reach.

**Why this pass stopped rather than editing.** Four independent reasons, the third
*substantially corrected at Round 1 review*:

1. **The trigger did not fire.** The brief authorized adding records and revising Doc_04 *if the
   material proved structural*. It did not.
2. **Escalation categories 4 and 2 apply.** `cic-build-cycle` sends to the project lead "a
   finding that cuts against an earlier decision" — §5.1, §5.2 and §5.4 cut against statements
   inside a Doc_04 that cleared three adversarial rounds — and separately "portfolio-level
   decisions," which §7 is.
3. **Two different freezes, which Round 1 found the first draft had conflated.** The **world is
   NOT frozen**: `Open_Gaps_Tracking.md` says so repeatedly and gives the reason — Article 31
   external scholarly review (OG-4) is outstanding, and "because this is unresolved, the world
   is NOT frozen." Doc_04's own status line likewise reads "not 'Frozen.'" What *is* frozen is
   the **S6.2 record-store and deployment baseline**, declared 2026-07-28 (not 2026-08-01, which
   was the last world's): "The Alexandria record store (156 in-world records), the deployed
   chunks generated from it, the deployed Theon Permanent Prompt… are FROZEN." The conclusion
   survives the correction and is in fact cleaner: the *documents* are at "Approved to proceed"
   and reopening them is ordinary process, while the thing a record change would actually
   disturb is the **frozen deployment baseline**.
4. **The change is outward-facing.** `records/alx/` compiles via `engine/m2/compiler.py` into
   the package pinned at `packages/alx/2026-09-04T16-41-49Z` in `records/worlds.yaml` and served
   live. Any record change means recompiling and re-running the M3 admission battery
   (`engine/m3/`) against a deployed world.

**Precedent, and why it does not settle it.** `alx.source.alexandrian-canonical-answers.md` was
added 2026-08-27 — after the 2026-07-28 baseline freeze — by exactly this discovery route. So
post-freeze *additive source records* are established practice, and a Peter source record alone
falls inside it. What has no precedent is correcting sourcing and scope statements *inside* a
thrice-reviewed Doc_04 and across two live gravity/figure records. Those travel together: adding
Peter while leaving §5.3's "hagiography and martyrology only" standing would be the "bolting new
citations underneath an unchanged conclusion" failure mode the brief named as the thing to avoid.

---

## 9. Recommendation to the project lead

Grounded options, per `cic-build-cycle`.

**Recommended — Option B (scoped reopen).** Authorize a scoped reopen covering §5.1–§5.4 only,
through the normal revision → independent review → disposition cycle:

- **Doc_04:** correct §0's Theognostus/Eusebius attribution (§5.1); reconcile the C5 date
  boundary against `alx.figure.didymus` (§5.2); correct T4's "hagiography and martyrology only"
  (§5.3); note Peter Fragment VI in T3's evidence base (§5.4); add the T1↔T4 interaction cell.
- **Records:** add Peter as `figure` + `source`, **handling both vendored witnesses** (anf06
  `div2 9.4`/`9.6` and npnf214 `div2 17.6`) or explicitly declining one; add Theognostus and
  Pierus as `source`, with school-headship recorded at the confidence §4 supports and **not** as
  attested fact; align `alx.gravity.learning-formation` and `alx.figure.didymus`.
- **Corpus map:** correct the three overstated headship notes, which currently contradict
  `alx.contested.didaskaleion-institution`.
- **Then** recompile via `engine/m2/compiler.py` and re-run the M3 battery before anything
  reaches production.

Small in content, non-trivial in process — the process is the point.

**Option A — records only, no Doc_04 change.** Cheapest; has the 2026-08-27 precedent. Not
recommended: leaves a false sourcing statement (§5.1) and a contradicted characterization
(§5.3) in place, and produces the bolt-on failure mode above.

**Option C — log and defer.** This document stands as the durable record. Defensible if Article
31 external review (OG-4) is near, since a qualified reviewer would see these same texts. Not
recommended: §5.1 is a plain factual error and cheap to fix.

**Separate decision, genuinely portfolio-level (§7).** Whether to build and run the
work-granularity corpus-map-vs-records diff across all worlds. This document recommends it and
does not run it.

**Open question that is the project lead's, not this thread's.** Whether a
sourcing-and-scope correction that changes no gravity classification warrants recompiling and
re-admitting a live deployment baseline. `cic-build-cycle` is explicit that a build thread
should not decide this.

---

## 10. What this pass did *not* do

- No edit to `Doc_04_Gravity_Discovery.md` or any other Doc_01–Doc_09 file.
- No addition, edit, or deletion in `records/alx/`.
- No corpus-map edit (the overstated notes in §4 are reported, not corrected).
- No recompile; no M3 run; `records/worlds.yaml` untouched.
- **No §3.5 audit.** Alexander of Alexandria and the other unopened assigned works are named,
  not investigated.
- **No Round 2 review yet.** This document is revised-after-Round-1 and **not cleared**.
- No claim that any of this was seen or approved by the project lead.

Files added by this pass: this document, its Round 1 review artifact
(`Review-Artifacts/Unused_Assigned_Corpus_Finding_Round1_Review.md`), and an
`Open_Gaps_Tracking.md` entry.

---

## 11. Revision log — Round 1 → Round 2

Round 1 review returned **SUBSTANTIAL REVISION REQUIRED** (8 substantial, 8 cosmetic) while
upholding the headline. All eight substantial findings are accepted; none is disputed.

1. **Corpus-map error** — the fourth Peter work at npnf214 `div2 17.6` was missed; "all sourced
   to anf06" was false. Fixed in §3.2 and carried into §9's Option B.
2. **Freeze conflation** — the world is NOT frozen; the S6.2 record-store/deployment baseline is,
   from 2026-07-28. Rewritten in §8 reason 3.
3. **§5.1 grounding** — Eusebius is a subordinate screen inside Discipline One, not one of
   Doc_04's two governing disciplines. Corrected; the finding now rests on narrower ground.
4. **§5.2 misattribution** — the C5 boundary contradiction is pre-existing between
   `alx.gravity.learning-formation` and `alx.figure.didymus`, not produced by the unused corpus.
   Restated, and Didymus-to-398 is now used as the *disproof* of a Persistence flip.
5. **§4 overreach** — "school continuity argument substantially weaker" replaced with the
   precise claim (only these three men's headships), plus *HE* VII.32 on Achillas and the
   `alx.contested.didaskaleion-institution` contradiction. New §4.5.
6. **Cross-Stratum Test never run** — now run explicitly as §6; negative result recorded.
7. **T3 never examined** — new §5.4 (Peter Fragment VI), plus the Athanasius author-gravity
   counter-weight added to §5.1.
8. **Self-asserted status** — the Round 1 header claimed "independently reviewed" and pre-named
   its own review file and an "OG-6" that did not exist. Removed; the header now states the
   actual Round 1 outcome and that Round 2 is pending, and no OG number is pre-assigned.

Cosmetics applied: T4 manifestations are three Eusebius/Dionysius-derived, not four; "fourteen
penitential canons" (ANF prints fifteen; XV is on fasting); Peter's own canon text ~3,900 words
vs the section's ~11,300 with commentary; ANF Elucidation II's "compilations… after the manner
of synodical decisions" qualification added to §5.3.

**Found during revision, by neither Round 1 nor the original pass:** **Canon IX**, dropped by an
extraction regex and recovered only because Round 1's canon-count finding forced re-extraction.
It is the single strongest datum for §5.3 — *"they will deliver you up, and not, ye shall
deliver up yourselves."* Recorded here because a defect found by accident while fixing another
one is worth naming as such.
