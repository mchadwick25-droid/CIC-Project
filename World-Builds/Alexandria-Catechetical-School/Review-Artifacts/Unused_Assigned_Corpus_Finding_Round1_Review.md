# Unused Assigned Corpus Finding (Peter / Theognostus / Pierus) — Round 1 Independent Adversarial Review

**Simulated review — informational only, not an Article 31 substitute.**

World: Alexandria (Catechetical-School) Formation World · Reviewed: `Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md`
Reviewer role: independent adversarial (did not author the finding document, the discovery pass it verifies, or any Doc_04 round). Brief: try to break the document, not to confirm it; re-derive every citation from primary sources rather than accepting the document's characterisation of them.
Method: every locus in the document's §2 verification table re-opened directly; ANF06 and NPNF201 tag-stripped and read; `records/alx/` grepped and the individual records read; the corpus map read across the full range the document cites; `Open_Gaps_Tracking.md`, `Doc_04`, `Doc_02`, the S6.2 gate directory, `records/worlds.yaml`, and the System Hub Decision Log checked independently.
Date: 2026-09-09

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**The headline conclusion is correct and survives adversarial testing.** This material is **not structural**. I tried hard to build the opposing case (§B below) and it fails on every route — including one route the document never tested, where it fails for a reason the world's own records already supply. The document is right, and on the decisive question it is *too timid rather than too bold*: the strongest arguments for its own conclusion are ones it does not make.

**But the document carries eight substantial defects**, and they are not all peripheral to its purpose. Two are factual errors about the very artefacts it is auditing (the corpus-map assignment set; Doc_04's governing structure). One is a governance-status error that would mislead the project lead about what disposition is even being asked for. One is a review status the document asserted before any review existed. Two are evidential — a finding credited to the unused corpus that the world's existing records already establish more strongly, and a net-effect claim the world's own vendored Eusebius contradicts. And two are omissions of coverage: the Article 21 substitute test was never run against this material, and **T3 — where this corpus comes closest to mattering — was never examined at all.**

The recommendation in §7 (Option B, scoped reopen, escalated) is **sound and should stand**, and the four reasons in §6 for not self-disposing are correct even after reason 3 is repaired. The revision required is to the document's evidence and its claims about status, not to its disposition.

Counts this round: **8 substantial, 8 cosmetic.**

---

## A. ACCURACY AUDIT — every checked claim, with what I found

I re-derived all nine claims put to this review. **Seven check out exactly. Two do not.**

| # | Claim | Verdict |
|---|---|---|
| (a) | `records/alx/` holds zero records for all three figures | **CONFIRMED** |
| (b) | ANF06 nowhere states Peter headed the catechetical school | **CONFIRMED** |
| (c) | "Theognostus" appears 0× in the vendored Eusebius | **CONFIRMED** |
| (d) | All three Theognostus fragments come via Athanasius | **CONFIRMED** |
| (e) | Vendored Eusebius says Achillas, not Pierus, was principal | **CONFIRMED — and understated** |
| (f) | Doc_04 §0 attributes the post-Origen teachers incl. Theognostus to Eusebius (HIGH-risk) | **CONFIRMED as to wording; the "false" label overreaches (C-5)** |
| (g) | Doc_04 §6 contains no T1↔T4 cell | **CONFIRMED — and understated** |
| (h) | No `Gravity_Index.xlsx` exists in the repo | **CONFIRMED** |
| (i) | Quotation/characterisation of Canons X, XII, XIII, XIV and Fragment I | **Quotations verbatim-accurate; three characterisations overread (C-2, C-6, C-8)** |

**(a) Record absence — confirmed.** `records/alx/` holds 192 files across 14 record types. `grep -ril "peter of alexandria\|theognostus\|pierus"` returns nothing; a bare `grep -ri "pier"` returns nothing; the only `\bpeter\b` hits are the *anf09* filename string inside two Origen source records (`alx.source.origen-comm-john.md`, `alx.source.origen-comm-matthew.md`), i.e. the volume title "Gospel of Peter," not the bishop. Control grep for "heraclas" returns four files, so the search is live and not silently failing. Absence is real.

**(b) Peter and the school — confirmed, and confirmed harder than the document did.** I extracted `div1 ix` (25658–28332) and searched *catechetical / didaskale· / school*. Five hits, all in the American editor's Introductory Notice (25667–25834): "the schools of Christendom"; Antioch's "School of Sciences" under Malchion; "for a final view of the great Alexandrian school, I shall gather up some fragments" (deferred to an elucidation under Alexander); "the school of Antioch (circa a.d. 350)." **Not one attaches Peter to the catechetical school.** The Translator's Introductory Notice gives Peter as bishop by succession after Theonas, beheaded in the ninth year of the persecution (311), and quotes Eusebius on "his diligent study and knowledge of the Holy Scriptures" and "that excellent doctor of the Christian religion" — both verbatim as the document renders them. I additionally searched the *Genuine Acts* (`ix.iii`, 25834–26588), which the document's §2 table does **not** list as read: no school-headship there either (the only near-misses are "this most gentle teacher" and "the advantage and instruction of the Church," neither institutional). §4.1 stands.

**(c) Theognostus in Eusebius — confirmed.** `grep -ci 'theognost'` against `npnf201_eusebius-church-history-life-of-constantine.xml` returns **0**. Corroborated by ANF06's own notice (15787 ff.): "Of this Theognostus we have no account by either Eusebius or Jerome."

**(d) All three fragments via Athanasius — confirmed.** Frag. I: "In Athanasius, *On the Decrees of the Nicene Council*, sec. xxv," with Athanasius's own framing quoted in the ANF text — "Learn then, ye Christ-opposing Arians, that Theognostus, a man of learning, did not decline to use the expression 'of the substance' (ἐκ τῆς οὐσίας)." Frag. II: "In Athanasius, *Epist.* 4, to Serapion, sec. 11." Frag. III: "From Athanasius, as above, p. 155." All three Athanasian. The document's identification of frag. III with *Ep. ad Serap.* 4.11 is the standard reading and defensible on "as above," though the ANF page reference (155 vs. 703) is internally inconsistent in the printing itself.

**(e) Achillas — confirmed, and the document understated its own evidence.** The document credits this to "the editor's note." It is stronger than that: at `npnf201` line ~43203, **Eusebius's own text** (*HE* VII.32.30) says of Achillas "He was placed over the school of the sacred faith, τῆς ἱερᾶς πίστεως τὸ διδασκαλεῖον." The editorial note the document quotes is verbatim accurate — I matched "Eusebius' statement must be accepted as correct, and in that case it is difficult to believe the report of Photius… It is more probable that Photius' report is false and rests upon a combination of the accounts of Eusebius and Jerome" word for word at ~43062–43078 — but it is *reasoning from* Eusebius's own sentence, not substituting for it. §4.2 is right and could have been argued more strongly.

**(f) Doc_04 §0 — wording confirmed.** Doc_04 line 36: "*Inter-phase interval c. 254–296* — dominated by no single surviving major voice; Dionysius of Alexandria's episcopate (c. 248–264) and the post-Origen teachers (Heraclas, Theognostus) sit here, reaching us largely through Eusebius (HIGH-risk)." Quoted accurately. See C-5 on the "false" label.

**(g) No T1↔T4 cell — confirmed, and understated.** Doc_04 §6 (line ~189) names exactly the relationships the document lists: C1↔C2, C1→C3/C4/C5, C2→C3/C4/C5, C4 super-integrator, C5↔T2, C2↔T3, T3↔C4, T4↔C2, T1↔C5. No T1↔T4. But nine classified candidates yield 36 pairs and the prose names about 13; T1↔T2, T1↔T3, T2↔T3, T2↔T4, T3↔T4, T1↔C1/C2/C3/C4, and more are equally unstated. The gap is systemic, not specific to T1↔T4 — which sharpens rather than blunts the document's §5.4 point, since §6's "full pairwise coverage" is deferred wholesale to a workbook that does not exist.

**(h) Gravity_Index.xlsx — confirmed absent.** `find . -iname "*Gravity_Index*"` returns only `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Gravity_Index_FINAL.xlsx` and `world-build-docs/pahc/generate_gravity_index.py`. A full `*.xlsx` sweep confirms nothing Alexandrian. Doc_04 §0, §3 (line 85), §6 (189), §8 (212) and §9 all cite it; **`Doc_04_Round2_Review.md` and `Doc_04_Round3_Review.md` both report reading its sheets and reproduce cell contents.** The document's restraint here — "not asserted to be a fabricated-artifact finding… Logged for the project lead" — is the right call and I endorse it, but the review artifacts' dependence on it is a further fact the project lead should have in front of them, and the document does not mention it.

**(i) Peter's canons — quotations verbatim, three characterisations overread.** I extracted `ix.iv.i`–`ix.iv.xv` with the Balsamon/Zonaras paragraphs and all endnotes programmatically stripped, and checked every quoted string:
- Canon I: "since the fourth passover of the persecution has arrived" — **verbatim**.
- Canon V: "passing by the altars, or giving a writing, or sending heathen to do sacrifice instead of themselves… let a penalty of six months' penance be imposed upon them" — **verbatim**; the document's paraphrase is exact.
- Canon X: "inasmuch as they have left destitute the flock of the Lord" — **verbatim**; "depart, and to be with Christ" / "to abide in the flesh is more needful for you" — **verbatim**, and correctly identified as Phil. 1:23–24. "Permanently barred from sacred office" is right ("they can no longer discharge their sacred ministry"), and the document is right that communion is retained.
- Canon XII: "Against those who have given money that they might be entirely undisturbed by evil, an accusation cannot be brought" — **verbatim**; paraphrase exact.
- Canon XIII: "these men that have withdrawn themselves are not at all to be blamed" — **verbatim**; the Ephesus / Peter-in-prison / Herod-and-the-infants argument is all there as described.
- Canon XIV: "as from their prison the thrice-blessed martyrs have written to me respecting those in Libya" — **verbatim**.
- Fragment I: "has ordained in the prison several unto himself" and the interdict on communion — **verbatim**.

No quotation is misrendered. The overreads are at C-2, C-6 and C-8 below.

---

## B. THE DECISIVE QUESTION — is "NOT STRUCTURAL" correct?

**Yes. I could not break it.** Here is the strongest opposing case I can construct, and why each branch fails.

**B-1. Could C5's Persistence verdict flip?** This is the only classification with a PARTIAL test result, so it is the obvious target. Theognostus (fl. c. 260) and Pierus (fl. c. 275) are real, substantive teaching activity inside the 254–296 hole; Pierus is described in Eusebius (*HE* VII.32) as skilled "in discoursing to the public assemblies of the Church"; Theognostus wrote a seven-book systematic *Hypotyposes* deliberately titled after Clement's. If C5's Persistence PARTIAL PASS rests on the school tradition thinning, does filling the hole flip it?

**No — and the disproof is already inside the record store, not in the unused corpus.** `alx.figure.didymus` records Didymus as "head of the Alexandrian teaching tradition for roughly half a century, to 398," bridge-line "the blind teacher who held the school's chair for fifty years." The world therefore **already holds a school head deep in the late horizon**, and C5 is still rated PARTIAL on Persistence alongside him. That proves the Persistence test is not measuring whether teachers existed. Doc_04 §3.5 and `alx.gravity.learning-formation` both say what it *is* measuring: "formation's center of gravity moves toward the episcopal-doctrinal channel" after the Origen rupture and the post-Nicene authority shift. Two more mid-interval teachers cannot move a centre-of-gravity claim that already tolerates a fifty-year late-horizon schoolmaster. C5 stays Supporting (temporally qualified). The document reaches the right answer by a weaker route.

**B-2. Is T1's pole separation threatened?** Doc_04 §3.6 requires "two genuinely distinct poles with real population, institutional, or practice-cluster separation (not a polarity within one person)." Here is the sharp version the document misses: **if the discovery pass had been right — if Peter really were simultaneously school head, bishop and martyr — that would have been evidence *against* T1, not for it.** A single man holding both poles at once is precisely the disqualifying case the test names. So §4's debunking does not merely deflate the discovery pass; it **protects T1**. And Heraclas, the world's existing instance, is *sequential* ("took first the teacher's chair and then the bishop's"), which is a succession pattern, not a collapse of the poles. T1 is safe on either reading, and safer on the document's. The document's §4.4 rebuttal ("Peter would not have been the first or the unique instance") is the weaker of the two available answers.

**B-3. Could Peter's canons move T4's confidence?** No. `alx.gravity.martyrdom-contemplative-tension` already carries `formation_confidence: Widely Accepted` at record level, with Inferential-Thin scoped specifically to *the martyr's interior*. Peter's canons are juridical and external throughout — they legislate about lapse, flight, bribery and reinstatement; they never narrate what it was like to be tortured. The document's own line — "Peter's canons do not give us a martyr's inner experience, and nothing here licenses filling that silence" — is exactly right and is the correct application of Article 20 discipline. Nothing moves.

**B-4. The one route that could have been structural — and that the document never tested.** Doc_04's declared Article 21 substitute is the **Cross-Stratum Test** (§5), and its named held-open majority-organizing candidates are "communal-liturgical belonging" and "martyrdom-as-formation." Peter's *Canonical Epistle* is the closest thing in this world's entire corpus to a non-school, whole-church, ordinary-believer document: it legislates for lapsed laypeople across Egypt and Libya, and **Canon XV** — which the document never mentions — is bare communal-liturgical practice ("No one shall find fault with us for observing the fourth day of the week, and the preparation… on the Lord's day… we have received it for a custom not even to bow the knee"). If any of this material could have been structural, it is here: it bears directly on the world's own thinness statement in `records/worlds.yaml` ("thinner on … ordinary believers") and on the single highest-stakes open item in the build (OG-4).

**It still fails, and the world already knows why.** `alx.source.alexandrian-canonical-answers.md` — added 2026-08-27 by the same discovery route — draws the exact distinction: bishops' canons are "evidence about the conditions of ordinary believers' lives," and treating them as the believers' own voice is "the opposite" of what they are. Peter's canons are a literate Greek bishop ruling *about* the lapsed, not the non-literate majority's own testimony to what it organised around. The Cross-Stratum Test asks whether a gravity is *attested across registers*; a bishop's ruling is the same register looking outward. The opposing case fails — but the document should have run it, and its silence here is the largest hole in an otherwise correct argument (S-6).

**B-5. Where the material comes closest to mattering — and the document never looked: T3.** See S-7. It does not move T3 out of Tensional either, so the conclusion holds.

**Verdict on question 2: the "not structural" conclusion is CORRECT.** It is not too conservative. If anything the document is too diffident about it, having left its two best supporting arguments (B-1's Didymus, B-2's pole-separation inversion) unstated and its one genuinely dangerous route (B-4) untested.

---

## C. SUBSTANTIAL FINDINGS

### S-1 [SUBSTANTIAL — factual error about the corpus map] §3.2 misstates the assignment set: there is a fourth assigned Peter work, and it is not in ANF06

§3.2 states that all three figures are assigned "all sourced to the already-vendored `anf06` file," and lists five works. The corpus map, in the very range §2 says was read (lines 600–740), carries a **fourth Peter work at `confidence: assigned`** that is not in ANF06:

> `- work: The canons of Peter of Alexandria, from his Sermon on Penitence` · `author: peter_alexandria` · `source_file: npnf214_seven-ecumenical-councils.xml` · `locus: div2 17.6 (~551 words)` · `confidence: assigned` (lines 634–646)

Its own note reads: *"NOTE A DUPLICATE… anf06 div2 9.4 carries 'The Canonical Epistle of Peter of Alexandria' with Balsamon's commentaries, already assigned to this entry. **Two vendored witnesses to one text.**"* It records a project-lead ruling ("Split 2026-08-26 on Mark's ruling").

This matters three ways. (1) The scope statement in §3.2 is false as written. (2) The §7 Option B remedy ("add three source records") does not cover it, and a source record for Peter's canons that cites only ANF06 would leave the second vendored witness silently unused — the same defect this whole pass exists to catch. (3) It sits inside the six npnf214 works whose assignment produced `alx.source.alexandrian-canonical-answers` on 2026-08-27; that record deliberately covers Dionysius, Timothy and Theophilus and **not** Peter, so the npnf214 Peter row is a *known* unused assignment the document does not report.

**Required:** correct §3.2; add the npnf214 witness to §7's remedy with the duplicate-witness handling the corpus map already prescribes.

### S-2 [SUBSTANTIAL — governance-status error] §6 reason 3 conflates the S6.2 artefact freeze with build-cycle document status; Doc_04 is not Frozen

§6 reason 3 asserts: "**Alexandria is Frozen, not merely Approved to proceed**," and then applies `cic-build-cycle`'s "reopening a Frozen document" language to Doc_04.

Three independent sources contradict the document-level half of that:
- **Doc_04's own Status line** (line 10): *"'Approved to proceed' unblocks Doc_05 and nothing more; **not 'Frozen.'**"*
- **`Open_Gaps_Tracking.md`** says the world is not frozen three separate times — line 140 ("The world is **NOT frozen**"), line 145 ("Because this is unresolved, the world is NOT frozen"), line 160 ("the world remains **NOT frozen**"), all keyed to the outstanding Article 31 gate (OG-4).
- The build log lists every Doc_01–Doc_09 disposition as **"Approved to proceed" (self-disposed)**; none is Frozen.

What *is* frozen is a different object: `Archive/Technology-Pass2-2026-08/Pass2/gates/S6.2_ALX_FREEZE_DECLARATION.md` (2026-07-28) freezes "the Alexandria record store (156 in-world records), the deployed chunks generated from it, the deployed Theon Permanent Prompt… as the S6.2 per-world baseline. Changes from here ride Change Orders against this declaration." The System Hub Decision Log explicitly reconciles the two senses (entry at line ~2601: Article 31 "not frozen" is "the same standing gap every other live world in this project carries").

So the document conflates an **engineering baseline freeze on `records/alx/` and the deployed artefacts** with a **build-cycle document status on Doc_04**. The distinction is not pedantic: it changes what the project lead is being asked for. The S6.2 declaration genuinely does govern the record additions in Option B (they ride a Change Order), and reason 4 already says so correctly. But Doc_04 itself is Approved-to-proceed and needs no unfreezing — which makes the §7 "Open question" ("whether a sourcing-and-scope correction… clears the bar for unfreezing a live, compiled, deployed world") frame the decision around the wrong artefact.

**Required:** split reason 3 into (i) the S6.2 record-store/prompt freeze, which does govern the `records/alx/` half of Option B via Change Order, and (ii) Doc_04's actual Approved-to-proceed status, which does not. Reason 3's conclusion (escalate, do not self-dispose) survives intact under (i); only its grounding needs repair.

### S-3 [SUBSTANTIAL — factual error about Doc_04's structure] The Eusebius screen is not "one of [Doc_04's] two governing disciplines"

§5.1 escalates its own finding on this ground: *"Doc_04's Eusebius HIGH-risk screen is one of its **two governing disciplines**, applied by name to T1 and T3."*

Doc_04 §0 is headed "Method, Phase Scheme, and **the Two Governing Disciplines**," and names them explicitly: **"Discipline One — the Origen SYSTEMIC screen"** and **"Discipline Two — the cross-build (desert) constraint."** Eusebius appears as the closing sentence *inside* Discipline One's paragraph — "**Eusebius** is a second, distinct HIGH-risk dependency for institutional/succession claims (Doc_02 §3.6) and is screened separately" — a subordinate screen, not one of the two named disciplines.

The §5.1 finding itself survives on its own ground (a sourcing conclusion is genuinely misstated), so this does not sink it. But a document whose entire authority rests on re-deriving its citations should not misdescribe the structure of the document it is auditing in the sentence that carries the finding's weight.

### S-4 [SUBSTANTIAL — evidential attribution] §5.2's finding is real, is stronger than stated, and is **not** produced by the unused corpus

§5.2 argues the "c. 150–254" school-period boundary in `alx.gravity.learning-formation`'s `name` field is too early, on the evidence of Theognostus (c. 260) and Pierus (c. 275).

The boundary is indeed wrong, and I verified the record's `name` field verbatim: `Learning-Formation Integration [SUPPORTING - temporally qualified: the school period, c. 150-254]`. But the decisive counter-evidence is already in the record store: **`alx.figure.didymus`** gives `floruit: head of the Alexandrian teaching tradition for roughly half a century, to 398` and `bridge_line: the blind teacher who held the school's chair for fifty years`. Two live records in the same store, compiled into the same package, disagree about whether the school period ends in 254 or runs to 398 — and the disagreement needs no unused corpus at all.

Two consequences the document should carry: (1) the defect is a **pre-existing internal inconsistency between two frozen records**, which is a materially stronger escalation item than "a boundary the assigned corpus outruns"; (2) §5.2 therefore does **not** support the document's §6 claim that this material is "not merely supplemental," because that particular finding is not a product of this material. §5.1 and §5.3 still do that work; §5.2 does not.

### S-5 [SUBSTANTIAL — overstated net effect, and an uncited existing record] §4 conflates "these three men's headship" with "the school's continuity," and re-derives a finding the world already holds

§4's closing "Net effect" reads: *"the 'school continuity across 254–296' argument is substantially weaker than presented."* The next sentence — "Of three claimed school heads in the interval, one is unattested, one is contradicted, and one rests on an inference from a single word" — is precise and correct. The first sentence is not.

**This world's own vendored Eusebius attests school continuity straight through the interval and out the far side.** *HE* VII.32.30 says of Achillas — presbytered alongside Pierius, bishop from 312 — "He was placed over the school of the sacred faith." The document *quotes the surrounding editorial note in §4.2 to debunk Pierus* and does not notice that the same passage supplies the continuity it declares weakened. Add the world's existing `alx.figure.heraclas` and `alx.figure.didymus` and the succession is attested at both ends and in the middle. What §4 actually damages is **these three men's headships**, not the school's continuity — a much narrower and entirely defensible result.

Second, and related: §4 never cites **`alx.contested_claim/alx.contested.didaskaleion-institution`**, which already holds, at `formation_confidence: Contested`: "The 'Catechetical School of Alexandria' existed as a formal institution with a continuous head-succession (Pantaenus, Clement, Origen, Heraclas, Dionysius…)" — held against Eusebian tidiness, with the voice consequence "the Representative may speak of teachers and the teaching tradition freely, but never of 'the School' as a documented continuous institution." Doc_02 Stream 5 carries the same finding ("**Contested** … for whether it was a *formal institution with a continuous head-succession*"). §4 presents as a novel corrective a position the world's records already hold. Citing it would have made §4's case against the corpus-map notes *stronger*, not weaker: those notes ("Head of the catechetical school"; "the bishop-martyr who also headed the catechetical school"; "Head of the catechetical school after Dionysius") do not merely outrun ANF06 — **they contradict a live `contested_claim` record in the compiled package.** That is the finding, and it is currently unstated.

### S-6 [SUBSTANTIAL — untested route] The Cross-Stratum Test (Doc_04 §5, the Article 21 substitute) was never applied to this material

Doc_04's §5 Cross-Stratum Test is "the central finding of this document" and OG-4 is "the highest-stakes open item in the build." It names two held-open majority-organizing candidates: **communal-liturgical belonging** and **martyrdom-as-formation**. This material touches both. Peter's *Canonical Epistle* is the corpus's most nearly non-school, whole-church, ordinary-believer document; **Canon XV** is bare communal-liturgical practice; the martyrdom pole is §5.3's whole subject.

The document runs its analysis against the six tests and the Interaction Matrix but **never asks the Article 21 substitute question of any of it**. That was the one route on which this material could conceivably have been structural (see B-4), and leaving it untested means the "not structural" conclusion is asserted without having tested the test that would have been most exposed. The answer is "still not structural," and the world's own `alx.source.alexandrian-canonical-answers` record supplies the reasoning — but the document must show the work, not skip it.

### S-7 [SUBSTANTIAL — missed gravity] T3 is never examined, and it is where this corpus comes closest to mattering

The document applies its evidential-base method to T4 (§5.3) and stops. Applied to **T3 — Speculative-Theological-Freedom vs Doctrinal-Boundary-Maintenance** it turns up more.

Doc_04 §3.6 T3 says: "the mid-horizon instance (Origen–Demetrius) is HIGH-risk and thin; the confirmation is deliberately **shifted to the late-horizon evidence** (the homoousian boundary, the Origenist controversy) which is well-attested and *independent of Eusebius*." §7 restates it: "T1 and T3 keep the Eusebius HIGH-risk screen… confirmation rests on structural (T1) and late-horizon Eusebius-independent (T3) evidence."

**Peter's Fragment VI, "Of the Soul and Body" (`ix.vi.vi`, lines 28084–28110), is an Alexandrian bishop's explicit doctrinal boundary against his own tradition's greatest teacher, pre-Nicene, and Eusebius-independent:**

> "…whence it is manifest that man was not formed by a conjunction of the body with a certain **pre-existent** type."

This is a direct repudiation of Origen's pre-existence of souls, from the episcopal chair, c. 306–311. The vendored NPNF201 apparatus says as much in its own voice: "Peter seems, to judge from the extant fragments, to have been in the main an Origenist, but to have **departed in some important respects from the teachings of Origen, especially on the subject of anthropology**."

This does not move T3 out of Tensional — the poles and their separation are unaffected — so the "not structural" conclusion holds. But it is the same *class* of finding as §5.3: an evidential-base characterisation ("confirmation rests on late-horizon evidence") that this world's own assigned corpus outruns, with a temporal consequence (Doc_04 §6 locates the boundary pole's hardening at Nicaea; here it is already hardening pre-Nicaea, from the bishop, against Origen, inside the thin interval). By the document's own §5.3 logic it belongs in §5. Its absence means the document's own claim to have tested this material against Doc_04 is incomplete.

A second, connected omission: the document argues that sweeping Theognostus under the Eusebius screen "overstates the risk on a source that does not carry it." True as to *Eusebius* — but the fragments reach us through **Athanasius's post-Nicene anti-Arian polemic** (*De Decretis* c. 350; *Ep. ad Serap.* c. 359), and Doc_02 Stream 12 carries an explicit Author-Gravity note on exactly that: "Athanasius's post-Nicene concentration risks making doctrinal conflict appear more central to *ordinary* formation than it was; this stream must be **temporally located** (post-325 for the Arian material) rather than smeared across the whole span." What survives of Theognostus survives because it was homoousian-useful in 350. "Eusebius-independent" is not "risk-free," and the document presents it as though it were.

### S-8 [SUBSTANTIAL — process] The document asserts a completed independent review it did not have

The Status header reads: **"Verified finding, independently reviewed, escalated to the project lead."** §8 then names the artefact: *"Only two files are added by this pass: this document, and its independent review artifact (`Review-Artifacts/Unused_Assigned_Corpus_Finding_Round1_Review.md`)."*

That file did not exist when the document was written; this review is it. Claiming "independently reviewed" as a completed fact, in the status line, before the review exists is the same class of defect as pre-claiming a disposition — and it is conspicuous in a document whose §6 and §8 are otherwise scrupulous about not claiming project-lead approval it does not have. The pre-assignment of the tracker ID "OG-6" (no OG-6 exists in `Open_Gaps_Tracking.md`) is the same habit in miniature.

**Required:** status line to read "Verified finding, pending independent review, escalated…" until a review artefact exists, and then to cite it by outcome.

---

## D. COSMETIC FINDINGS

- **C-1. §5.3 misdescribes the T4 record's manifestations.** "its four `manifestations` are all Eusebius- or Dionysius-derived." Three are; the fourth is *"the contemplative pole: the school's ascent language (Stromateis; the Address)"* — Clement and Gregory Thaumaturgus. "All four" is wrong; "the three martyr-pole manifestations" is right.
- **C-2. "Fifteen canons… written in 306" over-reaches.** ANF06 prints fifteen (`ix.iv.i`–`ix.iv.xv`); but **Canon XV** is on Wednesday/Friday fasting and Sunday non-kneeling, not the lapsed, and both the vendored NPNF201 ("**Fourteen Canons**, containing detailed directions in regard to the lapsed were drawn up by Peter in 306") and the corpus map ("Peter's **fourteen** penitential canons (306)") count fourteen. "Fifteen canons… written in 306, in the fourth year of the Diocletianic persecution" should read "fourteen penitential canons of 306, plus a fifteenth on fasting practice printed with them."
- **C-3. The "~11,300 words" figure is the inflated one.** I measured `ix.iv` with endnotes stripped: **10,871 words total, of which only 4,767 are non-Balsamon/Zonaras** — i.e. Peter's own text is roughly 4,800 words. The document is honest that the commentary is included, but it uses the composite number in the sentence arguing "the material is substantive, not scraps." Use the 4,800 figure; it is still ample and it is the honest one.
- **C-4. The freeze-declaration citation is a template placeholder and the date is wrong.** §6 cites `Archive/Technology-Pass2-2026-08/Pass2/gates/S6.2_<WORLD>_FREEZE_DECLARATION.md` — an unresolvable path; the actual file is `S6.2_ALX_FREEZE_DECLARATION.md`. It is dated **2026-07-28**, not "the 2026-08-01 freeze" §6 refers to (2026-08-01 is the System Hub *fleet-status* entry that lists Alexandria among five frozen worlds).
- **C-5. "False" overreaches on Doc_04 §0.** The sentence is a hedged collective — "the post-Origen teachers (Heraclas, Theognostus) sit here, reaching us **largely** through Eusebius" — about a set of which Dionysius and Heraclas genuinely are Eusebius-mediated. It is a **misleading collective attribution that must not be applied to Theognostus**, which is a real defect worth the substantial rating; it is not "a plain factual error" (§7 Option C) about the sentence as written.
- **C-6. "The bishop — not confessor-prestige — deciding who counts as a confessor" is one-sided.** Canon XIV admits men "**on the testimony of the rest of their brethren**," on the strength of letters "the thrice-blessed martyrs have written to me," and "as I have again heard from their fellow-ministers"; Fragment I's complaint is that Meletius "is not contented with **the letter of the most holy bishops and martyrs**." The bishop adjudicates *using* confessor testimony as much as against it. The Meletian conflict is the adversarial instance; Canon XIV is the cooperative one.
- **C-7. "Canons I–V — a graded penitential scale" flattens Canon IV.** Canon IV is not a grade on the scale; it is the refusal of one — "To those who are altogether reprobate, and unrepentant, who possess the Ethiopian's unchanging skin… 'Let no fruit grow on thee henceforward for ever.'" The scale is I–III and V; IV is the terminus.
- **C-8. The discovery pass and "PR #133" are not verifiable from this repository.** No discovery-pass artefact exists under `World-Builds/`, `Analysis/`, or the decision logs, and the only occurrence of "#133" anywhere is the document's own §Scope line. §4 spends a full section rebutting characterisations of a pass no later reader can check. Either attach or cite the pass artefact, or state plainly that its claims are reproduced from an unrecorded working session.

---

## E. FAIRNESS TO THE DISCOVERY PASS (question 3) — mostly fair, with one overreach

**On Peter and Philip of Side, the document is fair and I could not fault it.** §4.1's headline is properly scoped ("on this evidence"), the §1 statement is scoped to "the vendored material," and §4.1 **names the tradition and its source honestly**: "The school-headship tradition for Peter descends from Philip of Side's late and notoriously unreliable succession list, which is not vendored in this corpus." That is exactly right — Philip's *Christian History* fragment is the source of the Peter/Theognostus/Pierus headships alike, and its unreliability is the standard scholarly judgement. The document does not claim Peter *was not* head of the school; it claims the corpus-map note is "more confident than its own cited source," which is a precise and correct statement about a note whose `source_file` is `anf06`. That is the right target and the right charge. It is not the absence-of-attestation fallacy.

**§4.3 on Theognostus is likewise scrupulous** — I verified the ANF notice reads exactly as quoted ("Dodwell and others are of opinion that by this term *exegete* is meant the presidency of the Catechetical school"), and the document volunteers the countervailing point ("the title *Hypotyposes* is itself taken from Clement, his predecessor in office, which is a real continuity signal").

**The one overreach is the §4 "Net effect" paragraph** (S-5): declaring school continuity across 254–296 "substantially weaker" when the world's own vendored Eusebius attests a school head at the interval's far edge. And a smaller looseness: Peter is not a claimed school head *"in the interval"* — he is bishop from 300, outside 254–296 on any reading.

---

## F. DISCIPLINE COMPLIANCE (question 4)

| Requirement | Result |
|---|---|
| Declines to self-dispose | **PASS, and exemplary.** §1, §6 (four independent reasons), §7 and §8 all hold the line; §8's negative inventory ("no edit to Doc_04… no record change… no recompile… no claim that any of the above was reviewed or approved by the project lead") is the right instrument and is accurate — I verified `records/alx/` is untouched, no `Gravity_Index.xlsx` was created, and `records/worlds.yaml` still pins `packages/alx/2026-09-04T16-41-49Z`. |
| No unverifiable attribution to the project lead | **PASS.** No project-lead act is asserted anywhere. §6's freeze reference does point at a real, dated, Mark-authorised declaration; the path placeholder and date are wrong (C-4) but the underlying act is genuine. |
| Does not claim Frozen status for its own work | **PASS.** It claims no disposition for itself. |
| Grounded-options recommendation format | **PASS, and well executed.** Three options, each with cost, precedent and a stated reason for/against; a named recommendation; and an "Open question that is genuinely the project lead's, not this thread's" reserved rather than pre-answered. This is the format working as intended. |
| Status claims about itself | **FAIL — see S-8.** "independently reviewed" asserted before any review existed; "OG-6" pre-assigned. |

Net: the escalation discipline is followed correctly and the recommendation format is right. The one discipline failure is self-directed (S-8), not lead-directed.

---

## G. WHAT ELSE THE MATERIAL CONTAINS THAT THE DOCUMENT DOES NOT MENTION

Read directly from `ix.vi`, `ix.iv` and `vi.v`–`vi.vi`:

1. **Peter Fragment VI on pre-existence of souls → T3.** The single most gravity-relevant thing in the whole unused corpus. See S-7.
2. **Peter Fragments II, III, IV, VIII, IX → C4 Logos-Centered Unity.** A pre-Nicene Alexandrian *episcopal* Logos-incarnation witness: "the Word was made flesh"; "God the Word is with thee"; "He was God by nature, and… man by nature" (twice, III and IV, and again at VIII). Doc_04 rates C4 the "super-integrator" and grounds it in Clement/Origen/Athanasius; here is an Origen-independent, Eusebius-independent instance from inside the gap. Corroborating texture at minimum, and of the same kind the document was willing to record for C3.
3. **Canon XV → Doc_04 §5's held-open "communal-liturgical belonging."** Fasting on the fourth day and the preparation, "according to the tradition"; the Lord's day kept as joy with the custom "not even to bow the knee." Whole-church practice, stated as received custom rather than legislated novelty. It does not cross the stratum barrier (S-6/B-4), but it is the closest the corpus comes to the named gap, and the document does not mention it.
4. **ANF06 Elucidation II (`ix.vii`, 28157 ff.) qualifies §5.3's "first-person, documentary."** The American editor, quoting Dupin: "Like the famous Canonical Epistles of St. Basil, however, **these are compilations of canons accepted by the churches of his jurisdiction**… 'they are not written in the form of personal letters, but after the manner of synodical decisions.'" §5.3's core claim survives (they are still contemporaneous and non-hagiographic, and Canon I's "the fourth passover of the persecution has arrived" and Canon XIV's "have written to me" are genuinely first-person), but a document proposing to change an evidential characterisation in Doc_04 owes the reader the vendored apparatus's contrary characterisation. §2's method table lists `ix.ii`, `ix.iv` and `ix.vi` as read, and omits `ix.iii`, `ix.v` and `ix.vii` — §4.1's "I searched the entire Peter division" describes a keyword search, not a read.
5. **The Melitian schism has no census entry.** The corpus map flags this twice ("the immediate background of the Melitian schism (no census entry; noted)" at the Canonical Epistle row and again at the Phileas row). §5.3 makes the Melitian conflict load-bearing for its T1×T4 argument without noting that the schism itself is an acknowledged hole in the world's census.
6. **Phileas (`div2 6.8`, `confidence: provisional`) is a fourth unused assigned Alexandrian-martyrdom body** — "eyewitness material on the Alexandrian martyrs," bishop of Thmuis, martyred under Diocletian, imprisoned alongside the Melitian events. It is provisional, not assigned, so it falls outside the pass's stated scope; but a pass whose subject is unused assigned corpus on the martyrdom pole should say why it stops where it does.
7. **The review artifacts themselves depend on the missing workbook.** `Doc_04_Round2_Review.md` and `Doc_04_Round3_Review.md` both report reading `Gravity_Index.xlsx` sheets and quote cell values ("xlsx `Candidates` C1 cell reads…", "`Cross-Build` row 4"). §5.4 correctly declines to call this a fabricated-artifact finding, and I endorse that restraint — but the fact that two cleared review artifacts rest on an artefact no one can now open belongs in front of the project lead alongside §5.4, and is not there.

---

## H. SUMMARY

- **Overall verdict: SUBSTANTIAL REVISION REQUIRED.**
- **The headline conclusion is CORRECT.** "Not structural" survives every attack I could mount, including one route (the Cross-Stratum Test) the document never ran and one gravity (T3) it never examined. On the decisive question the document is right and under-argued, not wrong.
- **The recommendation (§7 Option B, scoped reopen, escalated) should stand**, expanded to cover the npnf214 Peter witness (S-1), the corpus-map-vs-`contested_claim` contradiction (S-5), the `learning-formation`↔`didymus` record inconsistency (S-4), and the T3 evidential-base item (S-7).
- **The four reasons for not self-disposing are sound**, with reason 3 requiring the repair at S-2. Reasons 1, 2 and 4 I verified independently and they hold.
- **Substantial: 8** — S-1 corpus-map assignment set; S-2 Frozen/Approved-to-proceed conflation; S-3 "two governing disciplines"; S-4 §5.2 not attributable to this corpus; S-5 §4 net-effect overstatement + uncited `contested_claim`; S-6 Cross-Stratum Test untested; S-7 T3 unexamined + Athanasian transmission risk unaddressed; S-8 self-asserted review status.
- **Cosmetic: 8** (C-1 … C-8).
- **What the document got right and should not lose in revision:** the record-absence grep, the ANF06/NPNF201 line loci (every one I re-derived landed exactly where stated), every direct quotation from Peter's canons and Fragment I, the Achillas/Photius rebuttal, the Theognostus-not-in-Eusebius control check, the missing-workbook finding and its deliberate under-claiming, the refusal to fill the martyr's interior, and the grounded-options escalation. That is a substantial body of correctly-verified work; the findings above are corrections to a document that is fundamentally doing the right thing.

*(This is a simulated AI review. It does not substitute for the Article 31 external scholarly review that OG-4 still requires — and a qualified subject-matter reviewer looking at Philip of Side, the Melitian chronology, and Peter's anthropology would be the accountable test of §4 and S-7.)*
