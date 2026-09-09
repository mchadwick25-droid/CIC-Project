# Unused Assigned Corpus — Peter of Alexandria, Theognostus, Pierus

**Alexandria (Catechetical-School) Formation World · finding document · 2026-09-09**

**Version:** Round 6 draft (revised after five adversarial rounds). Revision log: **§11**.

- **Round 1** (`Review-Artifacts/Unused_Assigned_Corpus_Finding_Round1_Review.md`) — **SUBSTANTIAL
  REVISION REQUIRED**, 8 substantial + 8 cosmetic. Headline upheld.
- **Round 2** (`…_Round2_Review.md`) — **SUBSTANTIAL**, 8 + 10. Headline upheld; Round 2 ran the C4
  route itself and found it also fails. Of Round 1's 8: 4 resolved, 3 partial (2 introducing new
  errors), 1 not resolved.
- **Round 3** (`…_Round3_Review.md`) — **SUBSTANTIAL**, 4 + 12. Headline upheld a third time. Of
  Round 2's 8: **7 resolved**, 1 partial (its fix having introduced a new error). Round 3 ran C3
  Dependency and T2 itself, and additionally ran the **generation step** — a route no prior round
  had named — and found that too fails.
- **Round 4** (`…_Round4_Review.md`) — **SUBSTANTIAL**, 3 + 15. Headline upheld a fourth time. Of
  Round 3's 4: **3 resolved**, 1 partial (its fix having introduced a new error). Round 4 ran the
  **Tensional** generation step — confessor/martyr authority vs episcopal authority, outside every
  prior round's frame — and found it fails too, and stated plainly that it **cannot find any route,
  inside or outside prior frames, to a Doc_04 classification change on this material.**
- **Round 5** (`…_Round5_Review.md`) — **SUBSTANTIAL**, **1** + 19. Headline upheld a fifth time.
  Round 3's four all **RESOLVED** — the first round with no partial and no fix-introduced
  substantial error. Round 5 verified the Eusebius-independence claim at both ends rather than
  accepting it, and ran two further routes (record-confidence; a second assigned Eusebius-independent
  canonical text, Dionysius to Basilides at npnf214 `div2 17.5`) — both fail, and the second
  **empirically confirms §7's root-cause thesis in a second volume**.

All five are AI review, each marked in its own artifact *"Simulated review — informational only,
not an Article 31 substitute"* (Article 31). **Round 6 review pending — this document is NOT
cleared, and no disposition has been assigned to it.**

*Trajectory, stated because it is the honest summary: **8 → 8 → 4 → 3 → 1** substantial findings,
falling monotonically, with the headline upheld at every round and each round **narrowing** the
case under it rather than strengthening it. Across all five rounds the defects have been
overwhelmingly in this document's **self-description**, not in its evidence work.*

**Status:** Verified finding, **escalated to the project lead — not self-disposed.** No
**construction document** (Doc_01–Doc_09), no `records/alx/` record, no corpus-map entry and no
compiled package was changed by this pass. The only world-build file modified is
`Open_Gaps_Tracking.md`, which gains the OG-6 ledger entry this finding requires. See §10.

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

**But it is not merely supplemental either.** Five defects are recorded in §5, of which **three
are produced by this unused corpus and are substantial** by this project's own definition
(`cic-build-cycle`: a revision is substantial if it changes "a claim's substance, a confidence
rating, a sourcing conclusion, or a scope boundary") — §5.1, §5.3 and §5.4. Two further items are
recorded but are **not** produced by this corpus and are not counted toward the finding: §5.2 (a
pre-existing contradiction between two live records) and §5.5 (a missing companion workbook).

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
(Control note, corrected at Round 5: a bare grep for `peter` returns two Origen commentary
records, but **neither mentions any Peter** — both matches are the *filename*
`anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` inside an `edition:` field. A grep for
`peter of alexandria` returns nothing.)

**3.2 The assignment is real — and covers four Peter works across two volumes.**
*Corrected at Round 1 review, which caught a factual error here: the first draft said all
assignments were sourced to anf06. They are not.*

From **anf06**, at `confidence: assigned`: Peter's *Canonical Epistle* (`div2 9.4`), Peter's
doctrinal *Fragments* (`div2 9.6`), Theognostus's *Hypotyposes* fragments (`div2 6.5`), Pierus's
*Fragments* (`div2 6.6`). At `provisional`: Peter's *Genuine Acts* (`div2 9.3`, correctly
flagged as **about** Peter, not **by** him).

From **npnf214** (`npnf214_seven-ecumenical-councils.xml`), at `confidence: assigned`: **"The
canons of Peter of Alexandria, from his Sermon on Penitence"** (`div2 17.6`, ~551 words in the
corpus map's count; ~456 words of actual canon text) — a **second vendored witness to the same
text**, split out on 2026-08-26 and carrying its own note that this duplicates the anf06
Canonical Epistle. *Per Round 2: it is a brief epitome, not a parallel full translation* — useful
as corroboration of the canons' reception into Eastern canon law (the Council in Trullo confirmed
them), not as an independent text. Any remediation must handle both witnesses or explicitly
decline one; §9's options are written accordingly.

**3.3 The 254–296 interval is genuinely this world's thinnest.** Doc_04 §0 names it as an
inter-phase interval "dominated by no single surviving major voice." Confirmed.

*Scope limit restored per Round 2, which caught a truncation here.* Doc_02 Stream 5's Contested
rating is **not** open-ended: it applies to whether there was "a *formal institution with a
continuous head-succession* **before c. 215–230**." It therefore does **not** cover Theognostus,
Pierus or Peter, all of whom are later. The thinness of 254–296 is an *evidential* thinness in
Doc_04's phase scheme, not an extension of Stream 5's institutional Contested rating.

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

*Round 2 caught a truncation here that changed the meaning, and the claim is narrowed
accordingly.* `alx.contested.didaskaleion-institution` concedes: *"A real tradition of learned
Christian teaching in Alexandria across the whole horizon is not in doubt… What is contested is
its INSTITUTIONAL form and continuity **before Origen's era**."* The first draft dropped those
last three words. They matter: the record's Contested rating is **scoped to the pre-Origen
period**, so it does **not** by itself rule on Theognostus, Pierus or Peter, all post-Origen.

What survives, and is enough: the record's stated **voice consequence** is unscoped — "the
Representative may speak of teachers and the teaching tradition freely, but never of 'the School'
as a documented continuous institution." The three corpus-map notes calling these men "Head of
the catechetical school" assert exactly the documented-continuous-institution framing that
consequence forbids, and they do so on sources that (per §4.1–§4.3) do not carry it. That is the
charge — an overstatement against their own sources, in tension with the record's voice rule —
not the stronger "contradicts a Contested finding" claim the first draft made.

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
perfected." That is C3 Divine Pedagogy vocabulary from inside the gap interval.

*Round 3 correction, and it matters.* The first draft called this "a **non-Origen** voice." It is
not. ANF's own notice states: *"That he was a disciple of Origen, or at least a devoted student of
his works, is clear from Photius."* Theognostus is therefore **inside** the Origen SYSTEMIC screen
(Doc_04 §0, Discipline One), not independent of it, and **cannot lift it**. Combined with the
Athanasius mediation caveat in §5.1, the corroboration frag. III offers C3 is considerably weaker
than the first draft implied: an Origen disciple, quoted selectively by Athanasius in post-Nicene
polemic. It corroborates C3 and reclassifies nothing (§6.2).

### 5.3 [SUBSTANTIAL — omission] T4's manifestations carry no witness outside Eusebius's selection

`alx.gravity.martyrdom-contemplative-tension` states the martyr pole's "interior is preserved in
**hagiography and martyrology only** (Inferential-Thin)"; Doc_04 §3.6 T4 says the same. *Round 1
correction accepted:* three of that record's four `manifestations` are Eusebius/Dionysius-derived,
not all four — the fourth is the contemplative pole (*Stromateis* / the *Address*).

*Round 3 correction — the charge is narrowed from "contradiction" to "omission," and it was right
to insist.* Both loci scope the claim to the martyr's **interior** ("**its interior** is preserved
in hagiography and martyrology only"), and this document concedes that the interior verdict
stands. So the wording is **not contradicted** — Peter's canons supply no martyr's interior, and
nothing here licenses filling that silence.

*Round 4 correction — the replacement claim was itself false, and this is the fourth consecutive
round to narrow this finding.* The Round 3 draft said T4's `manifestations` carry "no documentary
witness at all." They do: manifestation 3 is **"Dionysius's persecution letters — flight,
confession, the lapsed"** — first-person episcopal correspondence on the identical subject, held by
this world at `Documented` / `verified-direct` / citation-specificity A. (Manifestation 4,
*Stromateis* / the *Address*, is likewise neither narrated nor hagiographic.)

**Two narrower claims survive, and either carries the finding. The second is the stronger.**

1. *No juridical witness.* Dionysius's letters are pastoral correspondence; Peter's canons are
   **legislation** — graded penalties, deposition from office, a bishop's ruling on who counts as
   a confessor. That is a different evidential kind, and it is absent.
2. *No witness outside Eusebius's selection.* `alx.source.dionysius-extant-fragments` concedes in
   its own `work` field that the letters survive "mostly through **Eusebius's quotation** and later
   catenae: **doubly mediated** (his selection, then his quoters')." So **every** manifestation on
   T4's martyr pole passes through Eusebius — whom Doc_04 §0 screens at **HIGH risk** and §3.6
   applies by name to T1 and T3. Peter's canons reach us through an **entirely independent
   channel**: the Byzantine canonical tradition (Balsamon and Zonaras) and the canon law the
   Council in Trullo confirmed. For a gravity whose evidence is otherwise wholly Eusebius-selected,
   an independently-transmitted witness is the thing most worth having, and it is unused.

The finding is that the record is *incomplete*, not that it is *wrong*:

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
- **Fragment I** — Meletius, "giving proof of his desire for pre-eminence, has ordained in the
  prison several unto himself"; Peter interdicts communion with him. *Round 5 correction: earlier
  drafts glossed this as confessor-prestige asserting ordaining authority against the office. That
  is wrong. Meletius is a rival **bishop** (of Lycopolis) "invading my parish," the complaint is
  jurisdictional — separating presbyters and deacons "from my authority" — and the letter of "the
  most holy bishops and martyrs" is cited **on Peter's side**, as something Meletius is not
  contented with. The prison setting is where he ordained, not the source of his claim.*

Together: the Alexandrian church **deliberately de-absolutizing martyrdom-as-formation** —
flight legitimate, bribery legitimate, self-offering discouraged from Christ's own example,
lapse forgivable on a set scale, and, in Canon XIV, **the bishop deciding who is reckoned among
the confessors**. That last point is what carries the T1×T4 argument below; it rests on the canons
themselves, not on Fragment I.

**A qualification that must travel with this, from ANF's own Elucidation II** (searched but not
read in Round 1). The editor writes of Peter's canons that "Like the famous Canonical Epistles of
St. Basil, however, these are **compilations of canons accepted by the churches of his
jurisdiction**," and then quotes Dupin *on Basil's* canons for the principle: they are "not to be
considered as the particular opinions of St. Basil, but as the laws of the Church in his time…
not written in the form of personal letters, but after the manner of synodical decisions."
*(Attribution stated precisely per Round 2: the second clause is Dupin on Basil, applied by the
editor to Peter by analogy — not a direct statement about Peter.)*

So this is not one bishop's private opinion. That *strengthens* the ecclesial reading — it is the
church's received discipline — while forbidding any framing of it as Peter's personal interior
voice. It also slightly qualifies §3.4's "first-person": the canons speak in the first person
("as I have heard," "have written to me"), but their standing is synodical.

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
boundary-maintenance against a central Origenian doctrine, from a bishop of 300–311.

**Two corrections from Round 2, both of which narrow this finding.**

*(a) The date claim was wrong.* The first draft said this sits "inside the very interval Doc_04
calls thin." It does not. Doc_04 §0's thin inter-phase interval is **254–296**; Peter's episcopate
(300–311) falls in the **Late / post-Nicene phase (c. 296–400)**, which Doc_04 treats as
well-attested. The accurate and narrower claim: Peter is **pre-Nicene and pre-homoousian**, so
Fragment VI shows Alexandrian anti-Origenist boundary-drawing **roughly a quarter-century earlier
than the evidence Doc_04 actually rests T3 on** ("the homoousian boundary, the Origenist
controversy"). It moves the *start* of the late-horizon chain earlier; it does not fill the gap.

*(b) The transmission was unscreened, which §5.1 makes mandatory.* ANF's own note gives Fragment
VI as *"Ex Leontii et Joannis Rer. Sacr., lib. ii. Apud Mai"* — the *Sacra Parallela*, a
**7th–8th-century florilegium**. Screened consistently with the Athanasius caveat applied to
Theognostus in §5.1, this is late-mediated excerpted quotation, not a directly transmitted text,
and cannot be carried at better than the confidence that transmission supports. Exempting this
document's own best find from the discipline it demands of others would be exactly the failure
mode it exists to catch.

Net: this **modestly strengthens T3's evidential base; it does not reclassify it.** T3 already
PASSes and is already Tensional. Recorded because Doc_04 makes an explicit, checkable claim about
*where* T3's confirmation rests, and that claim is incomplete against the world's own assigned
corpus. Note also §3.5: Alexander of Alexandria's *Epistles on the Arian Heresy* — unopened, and
directly transmitted rather than florilegium-mediated — is the stronger end of this same chain.

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
record, and because §9's Option B would otherwise leave a reader wondering whether it was
checked.

### 6.1 C4 Logos-Centered Unity

*Added at Round 2's direction, which found this route asserted-by-omission rather than tested,
and ran it independently.*

Peter's doctrinal **Fragments II, III, IV and VIII** are a Logos witness: "the Word was made
flesh"; "God the Word is with thee"; "He was God by nature, and… man by nature." Doc_04 §3.4
grounds C4's integrating-center function as **Widely Accepted** on "all three figures" (Clement,
Origen, Athanasius). Peter would be a **fourth witness, episcopal, and independent of both Origen
and Eusebius** — on its face the strongest corroboration in this corpus.

**Two corrections from Round 3, which found this section had repaired one defect while committing
another.**

*(a) It is one saying, not four fragments.* Fragments III, IV and VIII carry the **same sentence**
in three witnesses — III: "Both things therefore are demonstrated, that He was God by nature, and
that He was man by nature"; IV: "Both therefore is proved, that he was God by nature, and was made
man by nature"; VIII: "both things therefore are together proved, that He was God by nature, and
was made man by nature." Counting them as three independent attestations inflates the evidence.

*(b) The transmission is late-polemical throughout, and §5.1's screen was not applied here.* Per
ANF's own provenance notes: **II** = the *Acts of the Council of Ephesus* (431); **III** = Leontius
of Byzantium, *contra Nestorianos et Eutychianos*; **IV** = Leontius of Jerusalem, *contra
Monophysitas*; **VIII** = the Emperor Justinian's treatise against the Monophysites. Every one is a
**5th–6th-century christological-controversy excerpt**, quoted because it was useful against
Nestorius, Eutyches or the Monophysites. That is heavier selection pressure than either the
Eusebius or the Athanasius mediation screened elsewhere in this document, and it must be applied
here on the same terms.

**It still fails to move C4, and it fails on Doc_04's own stated criterion.** C4 is classified
Supporting not for want of attestation — it already passes all six tests — but on the
**practice-cluster criterion**: "the Logos produces **no distinct practice-cluster of its own** —
it is the theological *centre* that makes the other gravities cohere." Peter's fragments are
christological confession; they generate no practice-cluster. Adding a fourth witness to a
function already rated Widely Accepted raises nothing and reclassifies nothing. **C4 remains
Supporting (integrating centre).**

### 6.2 The remaining routes — C3, T2, and the generation step

*Run at Round 3, which correctly objected that §6.1's "last untested route" framing was
contradicted by this document's own closing paragraph. Recorded as results, not as reasoning.*

- **C3 Divine Pedagogy — Dependency re-run. Unchanged; C3 confirmed Supporting.** Theognostus
  frag. III generates no practice. The only real practice-cluster in this corpus is Peter's
  penitential canons, and those ground themselves on **episcopal authority and Scripture**, not on
  divine pedagogy — remove C3 and they stand intact. The new material *confirms* the existing
  classification.
- **T2 Learning–Community — fails** on the same reasoning as §6: a bishop legislating for the
  whole church attests the community pole's *conditions*, not its formation logic.
- **The generation step — a route no round had named.** The prior rounds all asked whether this
  corpus moves an *existing* candidate. Round 3 asked the prior question: should it have
  **generated a candidate Doc_04 §1 never generated?** It should have been asked, and the answer
  is that one is genuinely available — **penitential-reintegrative discipline** (Doc_02 Streams 3,
  7 and 8; a real chain from Dionysius through Peter to Timothy and Theophilus; and, unusually for
  this world, a genuine practice-cluster). Tested against the six tests: **Repetition PASSES**;
  **Persistence is at best PARTIAL** (it is invisible in the early phase — the same partial result
  Doc_04 records for C5, which is a *Supporting gravity*, so this alone decides nothing); and
  **Dependency FAILS decisively**, on Doc_04 §2's own precedent for Askesis and the
  Participation↔Perception dynamic — it is what the ecology *does under persecution*, not an
  independent organiser. **Dependency is the deciding test**, and on it this does not reach gravity
  status. Nothing existing moves.

With the generation step run and failing, this document knows of **no remaining untested route**
to a Doc_04 classification change.

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
volume-granularity sweep and the least likely to look exposed.

*Round 2 correction, accepted.* The first draft contrasted this with the instrument that found
`alx.source.alexandrian-canonical-answers` the same day, calling that one "work-granular." That
was wrong: its own `discovery_channel` reads "observed no record here had **opened the volume**"
— volume-granular too. npnf214 was caught not because the instrument was finer but because
Alexandria had opened *no* record against that volume at all. Both instruments observe at volume
level, which is why anf06 — opened for two works — was invisible to both.

The remedy does not exist yet, and that is the point: **the corpus map is already work-granular
data** (it assigns individual works, with `locus` and `confidence`), so a work-level diff is
buildable from what is on disk. Nothing currently performs it.

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

**Is it merely supplemental?** No — but the count must be stated honestly, and Round 2 caught the
first draft inflating it. **Three defects are actually produced by this unused corpus:** §5.1 (a
false sourcing statement in a cleared document), §5.3 (T4's manifestations carry no witness
independent of Eusebius's selection) and §5.4 (T3's evidence base incomplete against the world's own assigned corpus). §5.2 and §5.5 are **pre-existing defects found
along the way** — real, worth fixing, but they would be there whether or not this corpus were ever
drawn on, and they are not evidence for the value of drawing on it. §7 is a separate
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
Peter while leaving T4's manifestations wholly Eusebius-selected (§5.3) would be the "bolting new
citations underneath an unchanged conclusion" failure mode the brief named as the thing to avoid.

---

## 9. Recommendation to the project lead

Grounded options, per `cic-build-cycle`.

**Recommended — Option B (scoped reopen).** Authorize a scoped reopen covering §5.1–§5.4 only,
through the normal revision → independent review → disposition cycle:

- **Doc_04:** correct §0's Theognostus/Eusebius attribution (§5.1); reconcile the C5 date
  boundary against `alx.figure.didymus` (§5.2); add Peter's canons to T4's `manifestations` as its
  only witness independent of Eusebius's selection, leaving the Inferential-Thin interior verdict
  untouched (§5.3); note
  Peter Fragment VI, screened for its florilegium transmission, in T3's evidence base (§5.4); add
  the T1↔T4 interaction cell.
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
recommended: leaves a false sourcing statement (§5.1) and T4's Eusebius-only
martyr pole (§5.3) in place, and produces the bolt-on failure mode above.

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
- **Not cleared.** Four adversarial rounds have each returned SUBSTANTIAL REVISION REQUIRED
  (8 → 8 → 4 → 3), every one upholding the headline. This is the Round 5 draft; **no disposition
  has been assigned to it**, by this thread or anyone else.
- No claim that any of this was seen or approved by the project lead.

**Files this pass adds** — stated as of this revision, and verifiable on disk rather than
promised:

1. this document (`Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md`);
2. **every** review round, as a file, at
   `Review-Artifacts/Unused_Assigned_Corpus_Finding_Round*_Review.md` — that glob is the
   authoritative list. *Round 5 drift-proofing: this list previously enumerated the artifacts and
   went stale in three of four rounds. A glob cannot go stale; a hand-maintained count can, and
   did.*
3. the **OG-6** entry appended to `Open_Gaps_Tracking.md`.

*Disclosure, per Round 2 finding 1.* In the Round 2 draft this list asserted an
`Open_Gaps_Tracking.md` entry that **did not exist at the time the claim was made** — the entry
was intended and not yet written. Round 2 caught it by running `git show --stat` against both
commits. It is the same defect class as the Round 1 header finding, and it is precisely the
failure `cic-build-cycle` names ("content described as having been shown must actually be
included"). The entry (OG-6) has since been written, and appending it is also why item 3 above
means `Open_Gaps_Tracking.md` **is** now modified — which the Status line at the head of this
document accounts for by scoping its "no change" claim to world-build construction documents
(Doc_01–Doc_09), `records/alx/`, the corpus map, and the compiled package.

---

## 11. Revision log

### Round 5 → Round 6 (this revision)

Round 5 returned **SUBSTANTIAL REVISION REQUIRED** with **1 substantial** finding (19 cosmetic) and
upheld the headline a fifth time. It found **all three** of Round 4's resolved — the first round
with no partial and no fix-introduced substantial error — and it independently verified the
Eusebius-independence claim at both ends rather than accepting it.

1. **OG-6's closing "Reviews" paragraph had not been updated** — still naming three artifacts,
   "All three upheld," and "a Round 4 review is pending," while four were on disk. **This is the
   fourth consecutive round in which this document's self-description, not its evidence, was the
   defect** (Round 1: header; Round 2: phantom ledger entry; Round 4: §10; now OG-6). Fixed — and
   fixed *structurally* rather than a fourth time by hand: both the OG-6 reviews paragraph and
   §10's file list now point at the `Round*_Review.md` glob instead of restating a count that goes
   stale the moment another round lands.

Two carried cosmetics that were **materially misleading** are also fixed, both four rounds old:

- **§3.1's grep control note was false.** It claimed the two Origen records matching `peter` were
  "the apostle and the *Gospel of Peter*." Neither mentions any Peter: both matches are the
  *filename* `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` in an `edition:` field.
- **§5.3's Fragment I gloss was wrong**, and it had been a supporting plank of the T1×T4 argument.
  Meletius is a rival **bishop** "invading my parish"; the complaint is jurisdictional; and the
  letter of "the most holy bishops and martyrs" is cited **on Peter's side**. The T1×T4 point
  stands, but on **Canon XIV** — the bishop reckoning who is among the confessors — not on
  Fragment I.

Also: OG-6's heading demoted to `###` to match OG-1…OG-5; OG-6's generation-step summary
disentangled (Round 3's penitential-reintegrative candidate and Round 4's Tensional candidate were
conflated); stale "item 4" cross-reference fixed.

### Round 4 → Round 5

Round 4 returned **SUBSTANTIAL REVISION REQUIRED** (3 substantial, 15 cosmetic — 12 carried
unrepaired from Round 3) and upheld the headline a fourth time, verifying Round 3's four against
`git diff 09c23d6..a44648c`: **3 resolved**, 1 partial. All three new findings accepted.

1. **The §5.3 replacement claim was itself false** — the fourth consecutive round to narrow this
   finding. "T4's manifestations carry no documentary witness" is wrong: manifestation 3 is
   *Dionysius's persecution letters — flight, confession, the lapsed*, first-person episcopal
   correspondence on the identical subject, held at `Documented` / `verified-direct` / A. Recast to
   the two claims that survive, the stronger being that **every** manifestation on T4's martyr pole
   passes through **Eusebius's selection** (the Dionysius record concedes "doubly mediated" in its
   own `work` field), while Peter's canons come through an independent channel — the Byzantine
   canonical tradition and Trullo-confirmed canon law. Propagated to the heading, §1, §8, §9's
   Options A and B, and OG-6.
2. **§10 had not been updated at all** — still "Two adversarial rounds… the Round 3 draft," and its
   file list, whose own stated standard is "verifiable on disk rather than promised," omitted the
   Round 3 artifact committed alongside it. **Third occurrence of this defect class** (Round 1's
   header, Round 2's phantom OG entry, now this). Fixed, and named as a pattern rather than a
   one-off: this document's self-description has been its weakest part in every round.
3. **§6.2 over-reported the generation-step result.** Persistence was graded "at best PARTIAL," not
   "fails" — and C5 is a *Supporting gravity* carrying exactly that partial, so it decides nothing;
   Repetition PASSES and went unreported; and "Not a gravity; Supporting at most" is
   self-contradicting, since Supporting **is** a Doc_04 gravity class. Restated with Dependency
   named as the deciding test. The outcome is unchanged.

*Round 4 also confirmed the §5.3 scope concession was fully propagated, that §6.1's four fragment
provenances are verbatim to ANF, that "one saying in three witnesses" is right, and that the
Theognostus correction's consequence was drawn correctly.*

### Round 3 → Round 4

Round 3 returned **SUBSTANTIAL REVISION REQUIRED** (4 substantial, 12 cosmetic) and upheld the
headline a third time. It verified Round 2's eight against the patch (`git diff 48ca471..09c23d6`)
rather than against §11, finding **7 resolved** and 1 partially resolved whose fix introduced a new
error. It also ran C3 Dependency, T2, and the generation step itself. All four new findings are
accepted; none is disputed.

1. **§6.1's C4 section repaired one defect and committed another.** Peter's Fragments III, IV and
   VIII are **one saying in three witnesses**, not three attestations; and their transmission —
   II via the *Acts of Ephesus* (431), III via Leontius of Byzantium, IV via Leontius of Jerusalem,
   VIII via Justinian — is **5th–6th-c. christological polemic**, unscreened, in the very section
   added to fix Round 2's transmission finding. Both corrected in §6.1.
2. **"Non-Origen voice" was wrong.** ANF states Theognostus "was a disciple of Origen, or at least
   a devoted student of his works." He is **inside** the Origen SYSTEMIC screen and cannot lift it.
   §5.2's corroboration claim is weakened accordingly.
3. **§5.3's "contradicted" misread scope.** Both loci scope the claim to the martyr's **interior**,
   and this document concedes that verdict stands. Recast as an **omission** finding (T4's
   `manifestations` hold no documentary witness), retitled, and propagated to §1, §8 and §9's
   Option B wording.
4. **"The last untested route" was self-contradicting.** Removed; the remaining routes are now run
   and reported in a new **§6.2** (C3 Dependency, T2, and the generation step).

Also corrected: **OG-6's own defect list**, which Round 3 found listed the T1↔T4 cell as a
free-standing defect while omitting §5.4, yet recommended reopening "§5.1–§5.4." It now matches
the document's three-produced / two-pre-existing structure exactly, and carries the negative
route-test results.

*Round 3 confirmed §11 did not overstate the previous round — all 8 items and all 5 claimed
cosmetics had landed on disk. This entry is written to the same standard.*

### Round 2 → Round 3

Round 2 returned **SUBSTANTIAL REVISION REQUIRED** (8 substantial, 10 cosmetic), upheld the
headline, and independently ran the C4 route that this document had left untested. On Round 1's
eight it found 4 resolved, 3 partially resolved (2 of those having introduced *new* errors), and
1 not resolved. All eight new findings are accepted; none is disputed.

1. **Phantom `Open_Gaps_Tracking.md` entry (the most serious).** §10 listed a ledger entry that
   did not exist; Round 2 proved it with `git show --stat`. **The OG-6 entry has now been
   written**, and §10 rewritten to state what is on disk and to disclose the original false claim
   rather than quietly repair it.
2. **§5.4 date error.** "Sitting inside the very interval Doc_04 calls thin" was false — Peter
   (300–311) is in Doc_04's Late phase (c. 296–400), not the 254–296 inter-phase. Rewritten to the
   narrower true claim (pre-Nicene, pre-homoousian, earlier than the evidence T3 rests on).
3. **Two truncations at a scope limit.** §4.5 dropped "**before Origen's era**" from the
   `contested_claim`'s `concedes` field — the limitation that exempts all three post-Origen men;
   §3.3 dropped Doc_02 Stream 5's "**before c. 215–230**." Both restored, and both findings
   narrowed to what survives.
4. **C4 never tested.** New §6.1 runs it: Peter's Fragments II/III/IV/VIII are a fourth,
   episcopal, Origen- and Eusebius-independent Logos witness, and C4 still does not move, on
   Doc_04's own practice-cluster criterion. A half-route (C3 Dependency) is named as reasoned, not
   tested.
5. **§7's granularity contrast unsupported.** The instrument that found the npnf214 canons is
   *also* volume-granular. Corrected; the recommendation now rests on the corpus map being
   work-granular *data* from which no diff is currently run.
6. **Fragment VI transmission unscreened.** ANF gives it via the *Sacra Parallela* (7th–8th c.
   florilegium). Screened in §5.4 on the same discipline §5.1 demands of Theognostus.
7. **§1 count stale.** Corrected, and sharpened: **three** defects are produced by this corpus
   (§5.1, §5.3, §5.4); §5.2 and §5.5 are pre-existing and are no longer counted toward the finding.
8. **§8 residue of Round 1's S-4.** §8 had continued to count §5.2 toward "not merely
   supplemental." Fixed alongside 7.

Cosmetics applied: header's cross-reference corrected (§9 → §11); Elucidation II's attribution
shift stated precisely (editor-on-Peter, then Dupin-on-Basil by analogy); npnf214 `17.6` described
as a ~456-word epitome rather than a parallel translation; Status line scoped to construction
documents so it no longer conflicts with the OG-6 append; §7 cross-references corrected to §9.

*Round 2 also noted that four Round 1 cosmetics were silently declined while §11 claimed
"cosmetics applied." Recorded here rather than repaired by assertion: the Round 1 cosmetic list is
in that artifact, and this log now states only what actually landed.*

### Round 1 → Round 2

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
