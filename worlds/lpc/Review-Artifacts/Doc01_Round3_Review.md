# Doc_01 — World Identification, Boundaries, and Orientation: Latin Pastoral-Congregational Christianity
## Round 3 Independent Adversarial Review

**Document reviewed:** `worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT — revision responding to Round 2, 2026-09-01, commit `675f7c0f`)
**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread. Did not draft the document under review, did not draft this world's Step 0, and did not write the Round 1 or Round 2 Doc_01 reviews. **Round 2's own findings, citations and quotations were treated as claims to be re-derived, not as authority** — including its citations to the vendored corpus, to the sibling branch, and to the governing `.docx` set. Where this review confirms a Round 2 finding it is because the source was re-read, not because Round 2 said so.

**Governed by:** `cic-build-cycle` (CO-022) *Review* and *Revision decision* sections; Construction Framework V7.4 Part I and Step 1; Constitution V2.2 Articles 3, 4, 15, 21, 23, 29; Forces Framework V1.1 Section 4; RCF V3.2 Part Four.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 1 HIGH · 10 MEDIUM · 9 LOW · 6 COSMETIC.**

**This is by a clear margin the best of the three drafts, and the improvement is of a specific and important kind: the sources were actually read this time.** Every primary-source quotation in the document was re-located in the vendored corpus this session and every one is verbatim and correctly placed — *On Baptism* I.1.2 (Book I, ch. 1, §2), II.3 (Book II, ch. 3, §4), the Book III "plenary or even regionary Council" passage, the Book VI "afterwards brought to light" passage, the 256 Council of Carthage preface, Cyprian's Ep. 67, Letter 185's Nebuchadnezzar and censured-kings material. Every governing-document quotation is exact where presented as exact (Articles 3, 15, 21, 29; CF Part I's six World Separation questions and four Distinct World Criteria; CF Part III's Candidate Gravity Generation rule; RCF Part Four's Temporal Horizon and thin-domain rule). The corpus-map rows are as described, in both worlds' YAML. **And the cross-branch claim — the one unusual move in this revision — checks out at source.** Round 2's H1 (the false "null" premise), H2 (the un-run conciliar candidate), H3 (the asserted defining gravity) and the whole of M2–M8 and M10 are genuinely fixed, several of them well. The process lesson Round 2 named — "a reviewer's suggested fix is a hypothesis, not a finding" — was learned.

It nonetheless fails at Round 3, on one dominant ground and a cluster of supporting ones, and the failure mode is the one this build has now logged eight times.

1. **The World #6 discharge answers half of a two-part binding obligation, and the half it drops is the half this revision's own new evidence now contradicts.** Step 0 §4 item 5 quotes IJC's Step 0 §4 item 3 verbatim: "The **authority-structure/state-power** boundary... must be stated explicitly in Doc_01." §7's rebuilt bullet is about the primacy dispute from first line to last and concludes that "the real boundary against World #6" is the episodic-versus-constitutive centrality of the *primacy* question. The word "state" does not occur in the bullet. Meanwhile §4 — new in this revision, and correct — establishes that Augustine "actively solicits and defends the Roman state's coercive power," that Letter 185 argues on a register of "the Christian ruler's own religious duty to legislate against error," and that the corpus-map's double placement of that letter into IJC "is the signal that this second register is real." The revision's M3 fix strands the revision's H4 fix (**H1**).

2. **The stranded-cross-reference pattern has migrated from mechanical pointers to evidentiary ones.** Round 2's twelve broken `§n` pointers are genuinely walked and fixed — I checked every pointer in the document individually. What replaces them is worse in kind: §5's two load-bearing Article 3 premises are cited to `(§4 above)` for evidence §4 does not contain, and the quotation §4 *does* supply is truncated one clause before the sentence that would have supplied one of them (**M1**).

3. **Three sections now hold three different postures on the same question, and two of them hold two different orderings of the same three axes.** §4's bullets say the disappeared-gravity question is "not resolved... not assumed either way"; §4's Conclusion takes a direction on it; §5 asserts formation emphasis is "the same in both phases" without reference to either (**M3**). §4's body numbers the three authority differences First/Second/Third; §4's Conclusion and §5 renumber them into a different order and then refer to them by ordinal (**M2**).

4. **Round 2's M10 was fixed where it was quoted and survives where it operates.** The fabricated "Article 21's own iterative-revision discipline" is gone from §2. But §5 and §8 item 10 now route the *strand determination itself* to Doc_04 for possible reversal — against Article 21's "once made, governs all subsequent strand attribution" and CF V7.4's "made at Step 1 and governs all subsequent work," both re-read at source this session, neither engaged anywhere in the document (**M4**).

**No standing escalation category is triggered by this review**, and §9's conclusion that none applies is, on the current record, correct. But it is reached through a limb-1 premise that is false (**M6**), a category-2 labelling obligation that is unmet (**M8**), and a limb-2 assessment that never names the contradiction it claims to have retired (**M9, M10**).

---

## Method — what was actually checked

Nothing was taken on the document's, Round 1's, or Round 2's word.

- **The vendored primary corpus, read directly this session, with book/chapter loci recomputed from the XML `div` structure rather than trusted from any review:** `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` — the ordination-in-schism passage (located to `<div3 type="Book" n="I">`, Chapter 1, §2 — the document's "I.1.2" is right); the councils-yield-to-plenary-councils passage (Book II, Chapter 3, §4 — "II.3" is right); the "not indeed by the authority of any plenary or **even** regionary Council" passage (Book III, Chapter 2, §2 — the Book II→III correction is right, and "even" is restored); the "afterwards brought to light... by the authority of a plenary Council" passage (Book VI — right); Augustine's own quotation of the 256 preface at Book II ch. 2; Letter 185's censured-kings and Nebuchadnezzar passages in full context, with the NPNF *editorial analysis*'s "the State as the servant of the Church" distinguished from Augustine's own text. `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` — the 256 Council of Carthage preface in full, including the ANF editorial gloss "Of course this implies a rebuke to the assumption of Stephen"; *De Unitate* 5 ("The episcopate is one, each part of which is held by each one for the whole"); Epistle LXVII in full, with its 37-bishop salutation confirming its synodal character.
- **Governing text, re-extracted from `.docx`:** `reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` — Article 3 (both the "sufficient historical coherence" clause and the "influences nothing above it / Causation runs downward" paragraph), Articles 15, 21, 23, 29 read in full. `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — Part I's Distinct World Criteria, Temporal Scope, World Separation Criteria, Strand Determination and World Continuity & Distinction entries; Part III's Candidate Gravity Generation; the Step 0/Step 1 boundary sentence; "No Tier 5." `reference/L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx` Part Four — Temporal Horizon and the thin-domain "natural quiet" rule.
- **The live `cic-build-cycle` skill**, read from `/root/.claude/skills/synced/.../cic-build-cycle/SKILL.md` — the four escalation categories and the *Naming and term propagation* rule quoted verbatim.
- **The sibling branch, fetched and read directly** (`git fetch origin claude/record-native-world-build-v2-e2s0dt`; head `4788e5c5`, 2026-09-01 17:13): Donatism's current `Step0_Movement_Scope_Confirmation.md` §3 B3 and §4 item 4; its current `Doc_01...md` §§1, 3, 4, 6; **and the full commit history of both files**, to test the "convergence" claim rather than accept it.
- **The Coach3 critique itself**, `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md`, which is present in *this* working tree — the quoted sentence located at source rather than at second hand through the sibling branch.
- **`cic/corpus-map/latin-pastoral-congregational-christianity.yaml`** (Letter 185, the 17-letter Augustine–Jerome row, the 419 Council row, the 256 Council row), **`imperial-juridical-christianity.yaml`** (the Letter 185 mirror row, `confidence: provisional`), **`hieronymian-ascetic-literary.yaml`** (the Jerome mirror row and *City of God* XVIII.42–44).
- **`worlds/ijc/Doc_01...md`** §4 (Strands A/B/C) and §6; **IJC's own `Step0_Movement_Scope_Confirmation.md` §4 item 3**; **`Hieronymian-Ascetic-Literary/hal_Doc_01...md`** §§3.3, 4, 8.1.
- **This world's own Step 0** in full, all eight §4 carry-forwards traced individually.
- **`Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_2.md`** — checkpoint M2 and its freeze-declaration listing confirmed at source.
- **Every `§n` pointer in the document**, extracted programmatically and checked one at a time against the current section numbering.

---

## The cross-branch claim, tested at source

This is the revision's most unusual move and the parent thread asked for it to be re-verified directly rather than accepted. It was. **The substance is accurate; it is not a fabrication.** Specifically:

- **Donatism's Step 0 §3 B3 does state the Coach3 axis, and the quotation is exact:** "External-management-within-unity versus internal-schism-into-division — different gravity, not just different century."
- **Donatism's Doc_01 does bind that axis to its own World #8 boundary statement, and §6 is the right section** ("World Continuity & Distinction," beginning at line 89; the World #8 bullet at line 97). The longer Coach3 quotation the document reproduces is accurate word-for-word against Donatism's Doc_01 — and, checked one level further back, accurate against `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md` itself, which is in this working tree.
- **Donatism's Step 0 §3 B3 really has stopped stating the both-figures reading.** Its current text attaches the parenthetical to "Cyprian's Decian-persecution pastoral material" and says so explicitly. The Cyprian-scoped reading this document reaches on grammar is now the sibling branch's reading too.
- **Round 2's M9(2) divergence is genuinely retired at source.** The sentence Round 2 quoted — "a different axis from World #8's ordinary episcopal pastoral care, not a variant of it" — no longer appears anywhere in Donatism's current Step 0 or Doc_01. I grepped both files for it and for its components. It was removed between Donatism Step 0 v1 (`4f420cbb`) and later revisions.

**But the branch history establishes something the document says the record cannot establish, and the document did not look.** See M9 and M10 below. The correction was made at commit `27314aa2` ("Donatism Step 0: revise to v3 after Round 2 adversarial review," 15:03 UTC) and the corrected sentence **carries its own inline provenance marker in the very text this document quotes**: *"(**scope corrected, v3 — Round 2 L8**)"*. Donatism's own `Review-Artifacts/Step0_Round2_Review.md` L8 states the finding in full: *"the 'not the schism-crisis angle, which belongs to world #4' quotation is still applied beyond its scope. In the source it is a parenthesis attached specifically to Cyprian's Decian-persecution ma[terial]."* The convergence is real, and it is *more* independent than the document claims — two adversarial reviews on two branches reached the same grammatical reading separately. The document declines credit it has not earned, which is right; it also declines a verification it could have performed in one `git show`, which is not.

---

## Round 2 disposition — what was actually fixed

**Genuinely fixed, verified at source (24):**

- **H1 (the "null" premise).** Deleted and replaced with the correct account, quoting I.1.2 verbatim — I located the passage and confirmed both the wording and the Book I locus. The consequential sentence in §5's Authority-structure bullet and the §5 Article 3 paragraph were both updated to match, which is the part Round 2 was right to worry about. Clean.
- **H2 (the conciliar-authority candidate).** Now run explicitly, with both texts quoted. Both verbatim against source. "Answerable to one another in council" is gone from the constants list. §8 item 10 carries it forward as a named open item rather than leaving it findable only in prose. (Two residues: M4, M7.)
- **H3 (the Donatism distinguisher).** The "World #4's own defining gravity" claim is gone. §3 now states the fourth candidate gravity first, from this world's own ecology, with two named in-world instances. §5 applies it. This is the right structural fix. (Residues: M8, L5.)
- **H4 (World #6).** The citation is corrected — *De Unitate* 5 is correctly dated c. 251 and correctly withdrawn; the 256 preface is correctly identified as the anti-Stephen text, and the ANF gloss the document cites for that ("a rebuke to the assumption of Stephen") is real and sits at exactly that point in the vendored file. The criterion is restated as centrality-of-organizing-force. The Augustine half is narrowed to the 419 Apiarius evidence and the *On Baptism* II.3 tension is named rather than papered over. **All of that is right. It is nonetheless a partial fix — see H1.**
- **M1 (cross-references).** All twelve of Round 2's stranded pointers are corrected, and the revision found two more on its own. I re-extracted every pointer in the file and checked each: the mechanical sweep is real and complete. (Three evidentiary pointers remain wrong — M1 below.)
- **M2 (Book II→III).** Correct. The passage occurs once in the volume, inside the third Book's `div3`, Chapter 2 §2. "even" is restored inside the quotation.
- **M3 (Letter 185).** Fixed and improved. "Throughout" is gone; both registers are named; the imperial-duty register is evidenced from Augustine's own text (not from the NPNF analysis, which the document correctly does not quote); and the corpus-map double placement is named as the corroborating signal. I confirmed the IJC mirror row exists (`confidence: provisional`).
- **M5 (re-derive from zero).** Fixed at all three sites (§3, §5, §8 item 7), and the replacement language matches CF Part III's actual rule, which I read at source.
- **M6 (RCF for a Step 1 boundary).** Fixed. Article 3's "influences nothing above it" is verbatim, and RCF Part Four does run Doc_01 → Representative as the document now says.
- **M7 (gravity derived inside the boundary paragraph).** Fixed structurally: §3 states it, §5 applies it.
- **M8 (Jerome disclosure).** Restored, with the corrected pointer. The corpus-map quotation is verbatim in both YAMLs; the "~52,892 words," the 17 letters (I counted the loci), "the largest single thing in this volume after the Confessions," the hal mirror row and *City of God* XVIII.42–44 all check out. (Residue: L1.)
- **M10 (Article 21 iterative-revision).** The fabricated attribution is gone from §2 and replaced with an honest statement that Article 21 contains no such rule. Correct. (The substance survives elsewhere — M4.)
- **L1** (Hippo province) — hedged, as Round 2 permitted. **L2** — fixed; §9 now claims Step 1 construction work rather than mere application. **L4** — fixed; the document states its own instruction rather than over-reaching RCF's thin-domain rule, and its characterization of that rule is accurate against source. **L5** — fixed; the claim is now hedged before the hedge is quoted. **L8** — fixed by a better route than the one Round 2 proposed. **L9** — fixed; the placement judgment is named.
- **C1, C2** (Tertullian) — both fixed, and consistently across §2, §6, §7: "Tertullian himself is credited with forging," matching the Step 0 Conclusion's own attribution. Two rounds of drift closed. **C3** — the unparseable clause is rewritten and now parses. **C5** — "even" restored. **C6** — no live "Cell 2B" citation remains.

**Fixed in form, defective in substance (2):** H4 → see H1 below. M9 → see M6, M9, M10 below.

**Not fixed, and not mentioned (2):**

- **L3.** Augustine's own documented change of mind on coercion (Ep. 93 to Vincentius) is still absent. "Vincentius," "Ep. 93," and any statement of the shift do not appear anywhere in the document. Round 2 listed it under "apply directly."
- **L6.** The *De Unitate* two-recension problem is still unnamed. This is now largely moot — the treatise is no longer a proof text, only a withdrawn citation — but it is unmentioned in the revision log either way.

Both matter less for their own content than for what §9 claims about them (M5).

---

## What was checked and found clean

Recorded because this project's reviews document both sides.

- **Every primary-source quotation is verbatim and correctly located.** This is a first for this document and should be said plainly. The three quotations that carry the most weight — I.1.2's "he who is ordained, if he depart from the unity of the Church, does not lose the sacrament of conferring baptism"; II.3's "must yield, beyond all possibility of doubt, to the authority of plenary Councils"; the 256 preface's "neither does any of us set himself up as a bishop of bishops" — were each located in the XML and read in surrounding context, not pattern-matched.
- **The I.1.2 inference is sound and better sourced than the document claims.** §4's "which is why the African church could and did receive Donatist clergy back in their orders rather than re-ordaining them" is supported inside the same passage: "those who return, having been ordained before their secession, are certainly not ordained again... they retain the sacrament of their ordination."
- **Every governing-document quotation is exact.** Article 3's "influences nothing above it" and "Causation runs downward through this hierarchy only"; Article 3's "sufficient... historical coherence"; Article 15 verbatim; Article 21's three quoted phrases and its definition of strand; Article 29's full sentence; CF Part I's six World Separation questions **in the Framework's own order and wording** (I checked all six against the `.docx`); CF Part III's Candidate Gravity Generation paragraph; RCF Part Four's thin-domain rule; "No Tier 5."
- **The corpus-map claims are exact.** Ep. 185 `confidence: assigned` here and present in `imperial-juridical-christianity.yaml`; the Augustine–Jerome row's `tradition`-to-both-worlds note quoted word-for-word; the hal mirror row and *City of God* XVIII.42–44 present as described; the 419 Council row present.
- **The neighbour-world citations are exact.** IJC Doc_01 §4's three strands are as described, and Strand C really is "not a claim about which see outranks which" — so §7's argument that a shared-dispute criterion would place Cyprian *inside* IJC is correctly reasoned from IJC's own logic. IJC Doc_01 §6's monepiscopal inheritance from World #1 and its "noted for orientation, not developed" restraint are both real. hal Doc_01 §8.1's authority-mode formula, its "drove him from Rome within months with no institutional recourse," and its "leaves the comparison's other half to World #8's own, independently-sourced construction" are all verbatim; hal's bipolarity finding and Marcella's pre-Jerome Aventine formation are as characterized.
- **§8 item 9's process observation is correct.** I confirmed that neither IJC's Doc_01 nor Donatism's Doc_01 contains a World Separation Criteria section. The referral to a coach pass is correctly scoped and this review endorses it, as Round 2 did.
- **Ep. 67 is a synodal letter**, as §7 says — the salutation names Cyprian and 36 fellow bishops, and the ANF argument-header describes it as a judgment on deposed lapsed bishops and their replacement by legitimate election. §7's asymmetry claim (office-and-procedure versus charisma-and-patronage) is correctly built on it.
- **Checkpoint M2 is real**, and the process document does list it in the freeze declaration's RESOLVED-AT-THE-FREEZE section, as §1 says.
- **CO-022 failure-mode checks:** (a) nothing is attributed to "the project lead" or "Mark" as a quote, decision or instruction — §1's reference to a project-lead act is sourced to Article 29 and the process document, which is the right basis; (c) the canonical folder is correct; (d) the status line is honest — DRAFT, pending Round 3, Frozen not claimed, Living Tradition Status PENDING, and the Round 1 and Round 2 severity counts in the status line and §9 match the review artifacts exactly (9/12/9/3 and 4/10/9/6).
- **Historical facts spot-re-checked and clean:** Cyprian's c. 246 conversion, the July 248–April 249 election window, the five presbyters' opposition; Novatian's rival consecration and the Felicissimus schism both in 251; *De Unitate*'s c. 251 date and Novatian/Felicissimus occasion; the 255–256 councils; Valerianic martyrdom 258; Augustine's 386 conversion, 387 baptism, 391 Hippo presbyterate under Valerius with the preaching licence contrary to African custom, 395/396 episcopate by Valerius's designation and Megalius's consecration; 258→391 as 133 years; the Diocletianic persecution's African phase c. 303–305 against the longer legal state; 279 Donatist against 286 Catholic bishops at the 411 Conference; the Vandal crossing 429 and Augustine's death 28 August 430. The Donatism Step 0 §2 A2 quotation ("the Donatists revived Cyprian's own third-century position against Pope Stephen") is verbatim against the sibling branch.

---

# HIGH

### H1 — The World #6 discharge is half a discharge: it answers the primacy question and drops the state-power question, which is the half named in the binding obligation and the half §4's own new evidence contradicts

**Where.** §7, World #6 bullet, whole; against §4's *First* difference; against Step 0 §4 item 5; against §1's own framing.

**What's wrong.** The obligation Doc_01 is discharging is not open-ended. This world's Step 0 §4 item 5 quotes IJC's Step 0 §4 item 3, and I confirmed the wording at source in `worlds/ijc/Step0_Movement_Scope_Confirmation.md`:

> *"**Distinctness from World #8 (binding on Doc_01).** The **authority-structure/state-power** boundary named in §3 above must be stated explicitly in Doc_01, since World #8 is not yet built and cannot itself hold the line from its side."*

And the boundary IJC's own cleared Doc_01 §6 states, verbatim:

> *"non-overlapping authority structure (juridical/state-adjacent here; pastoral/sacramental/territorial-flock-care there), **orthogonality to state power**, temporal overlap rather than sequence."*

§7's rebuilt bullet discharges the first half well. It never touches the second. Across roughly 700 words the bullet argues about inter-episcopal correspondence, Stephen, Petrine primacy, IJC's Strand A/B/C logic, the Apiarius appeal, and *On Baptism* II.3 — and closes: *"What is common to both phases, and is the real boundary against World #6, is that the primacy question is one recurring pressure among several on this world's own ordinary pastoral office, not the axis this world's own ecology is organized around."* The word "state" does not appear in the bullet at all.

**Why it matters.** Three ways, ascending.

1. **The document's own §4 is the strongest available evidence against the dropped half.** §4 establishes, correctly and in this revision for the first time, that Augustine "holds episcopal office within an established, imperially-patronized religion, and **actively solicits and defends the Roman state's coercive power** against the Donatist rival communion," and that Letter 185 argues on "a second, non-pastoral register arguing from the Christian ruler's own religious duty to legislate against error." That is not orthogonality to state power. §4 then says the corpus-map's double placement of Letter 185 into IJC "is the signal that this second register is real, not a rhetorical flourish" — which I confirmed: `imperial-juridical-christianity.yaml` carries the row, noting the letter is "Direct evidence for the ijc world's core question — the church's use of imperial law." The document supplies the counter-evidence to its own boundary and never brings the two sections into contact.
2. **It contradicts the document elsewhere.** §1 frames the contrast as "Where World #6 asks how the church governed itself relative to the state" and "pastoral and sacramental before it is juridical." §7 then declares the "real boundary" to be about primacy. Two sections, two different accounts of what the World #6 boundary rests on.
3. **It is an undisclosed tension with an already-cleared master document** — IJC Doc_01 §6, which states the boundary on a ground this document's own §4 undercuts. §9's category-4 limb 2 claims the contradiction question was "re-examined directly rather than assumed"; it was re-examined only against Donatism. The IJC side, which §7 was in the middle of rebuilding in the same pass, was not examined at all.

The fix Round 2 supplied for the primacy half was right and should be kept. What is missing is the other half, and the document has the material for it: the honest answer is not that this world is orthogonal to state power (it demonstrably is not, in Augustine's phase) but that state power enters this world's corpus as an *instrument episodically solicited against a rival communion*, where in IJC it is the axis the entire strand structure is built from — the same centrality-of-organizing-force criterion §7 already uses for primacy, applied to the axis the obligation actually names.

**Fix.** Add the state-power half of the World #6 discharge, in §7, using §4's Letter 185 evidence and the corpus-map double placement rather than working around them; state explicitly that "orthogonality to state power" as IJC's Doc_01 §6 phrases it is not what this world's own evidence shows for the Augustine phase, and say what the boundary rests on instead; and disclose the divergence from IJC Doc_01 §6 at §9's category-4 limb 2, where the parallel Donatism question is already disclosed. Reconcile §1's framing with whatever §7 concludes.

---

# MEDIUM

### M1 — The mechanical cross-reference sweep succeeded; three *evidentiary* cross-references are wrong, and two of them carry the Article 3 finding

Round 2's M1 is genuinely fixed — I extracted every `§n` pointer in the file and checked each against the current numbering, and the twelve Round 2 listed are all correct now. What survives is a different and more serious class: pointers that send a reader to a section for a *fact* the section does not contain.

| Location | Says | Actually |
|---|---|---|
| §5: *"Cyprian disagreed with Stephen of Rome... and **never broke communion with Rome over it (§4 above)**"* | §4 | §4 contains no statement that Cyprian never broke communion with Rome. Nothing in the document does. |
| §5: *"Augustine argues at length against Cyprian's own specific ruling while explicitly refusing to let that disagreement touch Cyprian's own standing or his own communion with him **(§4 above, and §7 below)**"* | §4, §7 | Neither says this. The support is in **§5 itself**, four paragraphs earlier ("What Augustine treats as normative is not Cyprian's conclusion but Cyprian's own conduct: his charity, and above all his refusal to break communion"). |
| §7: *"**§5 above** records Augustine's own *On Baptism* **II.3** arguing that even plenary councils may correct one another"* | §5 | II.3 is quoted at **§4**. §5 does not contain the string "II.3". |

The first two are the load-bearing empirical premises of the rebuilt Article 3 argument, and the first one has no support anywhere in the document. **And the clause that would have supplied it was cut out of §4's own quotation.** The 256 preface, in ANF05, opens the sentence §4 quotes with exactly the words §5 needs:

> *"It remains, that upon this same matter each of us should bring forward what we think, **judging no man, nor rejecting any one from the right of communion, if he should think differently from us**. For neither does any of us set himself up as a bishop of bishops..."*

§4 begins its quotation at "neither does any of us." The revision therefore truncated, out of the one text it quotes twice, the clause that is both the strongest in-world evidence for §5's central claim and the reason Augustine cites the preface at all (he quotes it at *On Baptism* Book II ch. 2 and refers back to it at III.1 precisely for the communion clause: *"Judging no one, nor depriving any of the right of communion if he differ from us"*).

A fourth, milder instance: §4's opening says it asks whether "the developments **already named** (§2, §5)" mark a transition — §5 comes after §4, so nothing there is already named.

**Fix.** Restore the "judging no man, nor rejecting any one from the right of communion" clause to §4's quotation of the preface; repoint §5's two pointers to it (and to §5's own earlier paragraph for the Augustine half); correct §7's II.3 pointer to §4; correct §4's opening pointer.

---

### M2 — §4's three axes are numbered one way in the body and a different way in the Conclusion and §5, and both are then referred to by ordinal

**Where.** §4's body against §4's Conclusion and §5's Authority-structure bullet.

§4's body numbers them explicitly:
- *First:* coercive capacity / Letter 185's two registers
- *Second:* rival-consecration validity
- *Third:* conciliar-authority theory

§4's Conclusion re-lists them in a different order — *"(the sacramental status of a rival consecration; the theory of conciliar authority; coercive capacity against a rival communion, and the theological register available to defend it)"* — and then says *"On **the first and third** of these... On **the second** — conciliar-authority theory."* §5's bullet uses the Conclusion's order and repeats the same ordinals.

A reader who has just read "*Third:* the two bishops do not share the same theory of conciliar authority" is then told, forty words later, that the second is conciliar-authority theory and that the first and third are the ones that don't touch the world's gravities. §2 compounds it: it describes §4 as finding "two of them do not touch — and **the third** does not clearly touch," using the body's numbering. So the document's four references to these three items use two mutually inconsistent orderings.

This is CO-022's *Naming and term propagation* problem in its purest form, on the section that carries the World Separation finding.

**Fix.** Pick one order, use it in all four places, and prefer naming the axes over numbering them.

---

### M3 — §5 asserts formation emphasis is "the same in both phases" while §4 records the disappearance question as unresolved on exactly that evidence

**Where.** §4's second bullet against §5's second bullet.

§4: *"**Has a major gravity disappeared?** Not resolved at this step, and not assumed either way. The *acute, empire-wide, state-organized* form of the persecution-and-lapsed-reconciliation gravity **recedes after Cyprian's own era**... but whether the underlying concern... persists in a different register... or has genuinely lapsed is... Doc_04's own question, on evidence this document does not consider decisive either way."*

§5: *"**Formation emphasis and practice:** the same in both phases — preaching, catechesis, penitential discipline, and sacramental administration directed at the ordinary believer..."*

"Penitential discipline" is §3's second named gravity and the concrete content of the gravity §4 says may have receded. Article 21's test is explicitly on "formation emphasis" among other criteria, so §4's open question is direct evidence on §5's bullet — and §5 neither cites it nor engages it. §5's Authority-structure bullet does exactly the right thing (it applies §4's finding and inherits its qualification); the formation-emphasis bullet, twelve lines later, was not given the same treatment.

Round 2's process observation applies verbatim: "for each edit, list the sentences that depend on it, and check each." The H2 fix was carried into one of §5's three bullets and not the others.

**Fix.** Either qualify §5's formation-emphasis bullet the way its Authority-structure bullet is qualified, or state why §4's receding-gravity observation does not bear on Article 21's formation-emphasis criterion.

---

### M4 — Round 2's M10 was fixed where it was quoted and survives where it operates: the strand determination is now routed to Doc_04 for possible reversal, against Article 21 and CF, with no authority stated and the tension unnamed

**Where.** §5's closing "Governing consequence" paragraph and §8 item 10.

> §5: *"...states explicitly whether the primary characterization this document establishes... survives that independent derivation — including **whether the conciliar-authority axis this document leaves open (§8 item 10) changes the strand-singular finding itself**."*
> §8 item 10: *"...with **the possibility, disclosed rather than foreclosed, that it could support a strand-plural finding this document does not reach**."*

Against the two texts Round 2 established and I re-read at source:

> Article 21: *"Whether a world contains distinct internal strands is a construction finding that, **once made, governs all subsequent strand attribution**."*
> CF V7.4, Strand Determination: *"This determination is **made at Step 1 and governs all subsequent work**. Strand attribution applies only where Step 1 established strands."* And: *"**Record the finding explicitly:** strand-singular, or strands identified with named evidence for each."*

§2 now says, correctly and admirably, that the World Separation finding is held provisionally "as this document's own discipline... not because Article 21 itself states an iterative-revision rule, which it does not." That disclaimer is not carried to §5 or §8, where the same move is made about the *strand* finding — which is the finding Article 21 actually speaks to. The finding is also recorded as "strand-singular, **qualified**," which is not one of the two forms CF asks for.

This is not a demand that the document be more confident than the evidence allows. hal's own Doc_01 §4 shows the defensible version: it states the governing rule and then attaches the caveat explicitly — "This finding governs all subsequent strand attribution: this world is treated as strand-singular throughout Docs 02–10, subject to reopening if Doc_02 or Doc_04 surfaces..." This document states the caveat without the rule, and without noticing that CF says the determination governs Doc_04 rather than the other way round.

**Fix.** State the governing rule (Article 21 / CF's "governs all subsequent work"), record the finding in one of CF's two forms, and then attach the reopening caveat as this document's own discipline — the same construction §2 already gets right, and the same construction hal's cleared Doc_01 uses.

---

### M5 — "All addressed in this revision" is false: two Round 2 findings are neither fixed nor mentioned

**Where.** §9, the line introducing the section-by-section list.

The list covers every HIGH, every MEDIUM, and every COSMETIC, plus L1, L2, L4, L5, L7, L8, L9. It does not mention **L3** or **L6**, and neither is fixed:

- **L3** — Augustine's own documented change of mind on coercion (Ep. 93 to Vincentius: he was against coercion and was changed by the results). Grepped: "Vincentius," "Ep. 93," "change of mind" and equivalents are absent. This is not a decorative omission — §4's whole question is whether authority changed *inside* the world's span, and this is first-person evidence from one of the two anchor figures that it did, in his own episcopate. It also strengthens rather than weakens the document's own finding, since a bishop reasoning his way from one position to another inside one office is continuity of office under changed circumstance, not a change of world.
- **L6** — the *De Unitate* two-recension problem. Largely moot now that the treatise is a withdrawn citation rather than a proof text, but the record should say so rather than say nothing.

Round 2 listed both under "Apply directly." CO-022's own failure-mode list makes the revision log's accuracy a checked item; a heading that says "All addressed" over a list that omits two findings is the failure that check exists to catch. Round 2 verified this same property and found it clean; it is no longer clean.

**Fix.** Apply L3 (one sentence in §4 will do it) and dispose of L6 explicitly, or state in §9 that L3 and L6 were considered and not applied, with the reason.

---

### M6 — §9 disposes of category 4's first limb on a premise the document's own preceding paragraph contradicts

**Where.** §9, limb 1:

> *"*Two reviews disagreeing with each other:* not applicable — this is this document's first Round 2 disposition, and **Round 2 did not disagree with Round 1** so much as find that Round 1's own suggested fixes had been imported rather than independently re-checked against source (a process lesson Round 2's own report names directly, not a disagreement between the two reviews)."*

Round 2 did disagree with Round 1, twice, explicitly, on matters of fact — and said so in its own header: *"two defects below are Round 1's own errors, imported into the revision on trust."* Its M2: *"Round 1's H2 gave the same passage as 'Book II.'... It is **Book III**, not Book II."* Its L1: *"The claim came into the document from Round 1's fix text and carries no citation."* I verified the Book III locus independently; Round 2 is right and Round 1 was wrong. That is a disagreement between two reviews.

The document knows this. Two paragraphs earlier, §9's own Round 2 summary says: *"a citation Round 1 itself had wrong (Book II for Book III) which this revision imported without checking."* So §9 records the disagreement and then, in its escalation assessment, denies it occurred.

The *conclusion* is nonetheless right, and the correct reasoning is available and shorter: the two reviews did disagree, on two checkable points; the disagreement was closed by going to the source; a closed disagreement is not "an unresolved tension the pipeline can't close on its own," which is what category 4 covers. CO-022's *Revision decision* section separately requires that "if two reviews on the same document disagree with each other, log that disagreement explicitly rather than quietly siding with whichever review happened most recently" — which the document does in the summary and undoes in the assessment.

**Fix.** Rewrite limb 1 on the true premise: name the two disagreements, say they were resolved at source in favour of Round 2, and conclude that a resolved disagreement does not meet the limb.

---

### M7 — §4's "what stays constant" argument groups the conciliar-authority axis under a description that fits neither of the two texts it rests on

**Where.** §4, the "what stays constant" paragraph:

> *"All three differences instead concern a bishop's authority **relative to other bishops and to a rival, competing hierarchy**: whether a rival's sacraments are void, whether a plenary council can correct a provincial one or an individual bishop, and what tools exist against a rival communion... state coercion is invoked specifically against the *separate* Donatist hierarchy, not as how either bishop disciplines his own people."*

The rival-hierarchy framing carries the first and third axes cleanly. It does not reach the second. Both texts §4 quotes for the conciliar-authority axis are about authority *inside* one communion, not against a rival one:

- Cyprian's 256 preface is addressed to "my dearly beloved colleagues" — bishops of Africa, Numidia and Mauritania sitting in his own council — and (per the ANF gloss the document itself cites) to Stephen of Rome, a bishop in communion with him. Its subject is whether a fellow catholic bishop can be compelled.
- Augustine's II.3 is about "**all the letters of bishops** which have been written, or are being written, since the closing of the canon" and about councils "held in the several districts and provinces" — catholic bishops and catholic councils. He is arguing that *Cyprian himself*, a bishop of the same communion, was correctable.

So the second axis is a change in what a bishop of this world owes to, and can be overruled by, the church he belongs to. That is much closer to "the ordinary exercise of episcopal office" than the paragraph's framing allows, and the supporting sentence about state coercion being aimed at the separate hierarchy carries only the third axis. §4 discloses that the conciliar axis is "the closest call"; that disclosure does not repair a description that misplaces it.

A related over-read in the same bullet: *"Cyprian's ground is egalitarian and non-coercive — each bishop answerable to Christ alone, **no council empowered to compel a dissenting colleague**."* The preface says no *bishop* sets himself up over colleagues and none compels by tyrannical terror; the extension to councils is an inference, and a fair one, but it is stated as the text's content.

**Fix.** Split the grouping: say plainly that the first and third axes concern relations to a rival hierarchy while the second concerns a bishop's answerability inside his own communion, and make the argument for the second on its own terms — which is available (what changes is the *appellate* structure above the individual bishop, not the bishop's relation to his own flock) and is what the document is reaching for.

---

### M8 — The Coach3 axis is load-bearing without the portfolio-level label CO-022 category 2 requires, and it is not the axis §5 actually runs

**Where.** §5's "Corrected finding" paragraph; §5's reading-divergence paragraph; §9's category-2 assessment.

**(a) The label.** CO-022 category 2, verbatim from the live skill: *"**Portfolio-level or cross-world strategic decisions** — anything decided for a reason external to this specific world's own ecology. **Label it explicitly as portfolio-level in whatever document records it, distinct from an ecology-grounded finding.**"* The Coach3 axis is a coach's cross-world boundary/contrast pass over nine world pairings — the definition of a portfolio-level determination. §9's category-2 paragraph reasons only that this document is *applying* rather than *asserting* the framing, and concludes no escalation applies. That may be right as to escalation; it does not discharge the labelling requirement, which attaches to whatever document records the framing. Neither §5 nor §7 labels it.

**(b) It is not the same axis.** §5 says the Coach3 axis "is the same axis this document relies on above," and §9 repeats "is the same axis this document relies on at §5." Compare:

- **Coach3 / Donatism, verified at source:** *"#8's Cyprian is defined by **crisis pastoral management within one unified communion under external persecution**; #4 is defined by permanent schism into two rival hierarchies over a different, later crisis..."*
- **§5's own axis:** *"what a bishop of this world does when he **disagrees, sharply, with a fellow bishop** or with the wider church's own discipline — work to preserve communion despite the disagreement, or break communion..."*

The schism half maps. The #8 half does not. Coach3's #8 half is Cyprian-scoped by its own words ("#8's Cyprian"), is about crisis management **under external persecution**, and names martyr-cult identity as #4's organizing content. §5's half is about a disposition toward internal disagreement, across both anchor figures, in a phase where — on §4's own finding — external persecution has ended and this world's bishops have become the party soliciting state power. Taken at face value, Coach3's axis describes Cyprian's half of this world and not Augustine's, which is structurally the same defect Round 2's H3 identified, arriving through a different door.

§3's fourth candidate gravity does the work honestly and covers both figures, so the Article 3 answer is not hollow. What is wrong is the claim of identity between §3's axis and Coach3's, made twice, and used to say this document asserts nothing of its own.

**Fix.** Label the Coach3 axis portfolio-level where it is used. Drop "the same axis" and say what is true: §3's axis is this world's own, derived from this world's ecology, and it is *compatible with and adjacent to* the axis the sibling build has adopted, which is scoped to Cyprian and to the persecution frame.

---

### M9 — §5 declares the cause of the sibling branch's change "not established by anything in either branch's own record," when the sentence it quotes carries an inline provenance marker saying otherwise

**Where.** §5's reading-divergence paragraph:

> *"Whether that reflects the sibling branch's own subsequent correction, independent of this document, or simply a later draft this world's own Step 0 predates, **is not established by anything in either branch's own record**, and this document does not claim credit either way."*

Both disjuncts are answerable from the branch, and the answer is in the text the document quotes. Donatism's current Step 0 §3 B3 reads, in the same sentence the document reproduces:

> *"Cyprian's Decian-persecution pastoral material — *"not the schism-crisis angle, which belongs to world #4"* is the source's own parenthetical attached specifically to that clause, not to World #8's material as a whole **(scope corrected, v3 — Round 2 L8)** — and Augustine's ordinary preaching..."*

Donatism's own `Review-Artifacts/Step0_Round2_Review.md` L8 states the finding that produced it. And the chronology rules out the second disjunct: Donatism's correction landed at commit `27314aa2`, 15:03 UTC; this world's Step 0 was still being revised until 16:40 and cleared at 16:18. Donatism's correction *predates* this world's Step 0's final state; the sibling branch is not "a later draft this world's own Step 0 predates."

The direction of the error is modest — the document under-claims rather than over-claims, and the true record makes the convergence *more* independent, not less (two adversarial reviews on two branches reached the same grammatical reading separately). But this is a stated negative about a record, in the paragraph where the document is establishing that it verified the record rather than asserting a resolution. Asserting that something is unestablishable, without checking, is the same class of move the previous two rounds penalised.

**Fix.** Replace the sentence with what the record shows: Donatism's Step 0 was corrected on its own Round 2 review's L8 finding, at v3, marked inline; the two branches reached the Cyprian-scoped reading independently; neither took it from the other.

---

### M10 — A cleared master document now contains a statement this document knows to be false, and the document neither carries it forward nor assesses it under the limb it is running

**Where.** §5 and §9, the "now-dated paraphrase" formulation.

This world's Step 0 — cleared, Approved to proceed — states at §3 B3 and at §4 item 2(e), as a **binding disclosure obligation**: *"Donatism's own Step 0 confirmation reads the portfolio entry's 'not the schism-crisis angle' parenthetical as qualifying both Cyprian and Augustine together."* On the sibling branch's current and cleared state, that is false, as this document correctly reports.

So the record now holds: cleared master document A asserts a proposition about cleared master document B that B does not contain. That is, on its face, the shape of category 4's second limb — "a contradiction between two already-cleared master documents" — and it is a live inaccuracy in a document that binds this build. Doc_01 notices it (twice, calling it "now-dated") and then does three things with it: it declines to reopen Step 0 (correct); it declines to assess it under limb 2, which addresses only the *substantive* reading divergence rather than the *reportorial* error (a gap); and it does not carry it to §8 as an item for anyone downstream (a gap). §8's ten items contain nothing about it.

The same is true, in a smaller way, of Round 2's M9(2). Round 2 identified a specific contradiction — Donatism Step 0 §3 B3's "a different axis from World #8's ordinary episcopal pastoral care" against §5's finding that ordinary pastoral care does not distinguish the two worlds. **That contradiction is genuinely retired**: I grepped Donatism's current Step 0 and Doc_01 and the sentence is gone. But the document never names what it was. §9 asserts "there is no contradiction between the two branches' current positions" without stating the contradiction whose retirement it is reporting, so a reader cannot check the claim, and the record of what was verified is incomplete.

**Fix.** Carry the Step 0 inaccuracy forward at §8 as a record-correction item for whoever can touch Step 0 (or for the branch merge), and name Round 2's M9(2) contradiction explicitly at §9 before reporting that it is retired, quoting the sentence that is gone.

---

# LOW

**L1 — Round 2's M8 fix is complete in §7 and incomplete in §8.** The Augustine–Jerome double-placement disclosure is restored, well, with the corrected pointer and a verbatim corpus-map quotation. Round 2's fix instruction had three parts — name it, say why it is deliberate, "and carry the Doc_02 consequence." §7 discharges the third by saying Doc_02 "inherits [it] as given, not as a boundary breach to resolve," which is a defensible reading, but §8's ten forward items still contain nothing about it, which is the specific gap Round 2 named ("absent from §8's forward items"). One clause in §8 item 4 would close it.

**L2 — §1's C4 fix is half-applied, and the note attached to it is false about the sentence it annotates.** §1 still reads *"leaving 'the method of confirmation... governed by the build documents'"* — the same elision across the verb that C4 objected to — and then adds: *"(Article 29's actual text: 'The method of confirmation is governed by the build documents,' **quoted here in full rather than elided across its own verb**.)"* The parenthetical is true of itself and false of the main clause it is attached to. Either fix the main clause or reword the parenthetical.

**L3 — Round 2's L3 is substantively unaddressed.** See M5 for the log problem; the content gap is its own small finding. Augustine's Ep. 93 statement that he originally opposed coercion and was changed by its results is first-person evidence bearing directly on §4's own question, and the document's finding survives it comfortably.

**L4 — all three strand-plural candidates are on one of Article 21's four criteria.** §5 says the finding is "reached only after engaging the strongest available strand-plural candidates directly, not by omitting them," and §4 supplies three — all on authority structure. Formation emphasis, practice, and ecological orientation are then each disposed of with "the same in both phases," with no candidate engaged on either. Round 2's own note applies by analogy: three candidates on one criterion does not license a finding across four. (M3 identifies the specific candidate that is available and unengaged.)

**L5 — §5's axis is never tested against §4's own hardest instance for it.** The axis is "work to preserve communion despite the disagreement, or break communion." The document's most striking piece of evidence about how a bishop of this world treats a communion he disagrees with is Augustine soliciting imperial coercion against it. The answer is available in the document's own material — the Donatists had already separated, and Letter 185's pastoral-corrective register frames coercion as recovering the separated rather than expelling the dissenting — but §5 never makes the connection, and a reader who has just read §4 will reach §5's axis with the objection unaddressed.

**L6 — the two "intervals" §2 now states are of different events, set side by side without saying so.** Cyprian: "roughly two to three years from conversion to the episcopate." Augustine: "roughly five years after his own conversion," to the *presbyterate*. Round 2 asked for Cyprian ~2–3 and Augustine ~9–10 (conversion to episcopate); the ~9–10 figure is still unstated. The paragraph handles the presbyterate/episcopate distinction well otherwise — that part of L7 is genuinely fixed — but the two numbers it does give are not comparable and are presented as if they were.

**L7 — Coach3 is quoted "in full" with two elisions, and at second hand when the source is in this tree.** §5 says it is "quoting Coach3 in full" and then elides "(the Diocletian-era traditor controversy)" mid-sentence and drops the closing sentence. More substantively: `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md` is present in *this* working tree — I read it — so the document could have cited the source directly rather than routing the quotation through the sibling branch's quotation of it. Both are accurate; citing the source is cheaper and stronger.

**L8 — §4's Conclusion takes a direction on the two bullets that say "not assumed either way."** Round 2's M4 fix said: answer both questions, or mark the Conclusion provisional — "do not do the first thing in the bullets and the second in the conclusion." The revision now does something closer to the reverse: the bullets say "Not resolved at this step, and not assumed either way," and the Conclusion says the evidence "does not, on its most transition-favoring reading, describe an emergent or a vanished gravity so much as the same underlying concern in different circumstantial clothing." That is a direction. It is hedged and it defers to Doc_04, so this is much improved — but the bullets and the Conclusion still do not say the same thing about the same evidence.

**L9 — "the Apiarius affair (419) at the edge of Augustine's" episcopate.** Augustine's episcopate runs 395/396–430; 419 is roughly two-thirds of the way through it, and the Apiarius business ran on to c. 426. The point being made — that the primacy question is episodic in this world's corpus — is right and does not need "at the edge," which as written is inaccurate.

---

# COSMETIC

**C1 — §7's bracketed compression of the 256 preface changes the proposition.** *"[no bishop] can be judged by another"* stands for *"can no more be judged by another than he himself can judge another."* The original is a reciprocal claim; the compression is one-directional. The brackets signal editing, so this is not a misquotation, but the reciprocity is the interesting half.

**C2 — §4 elides the object out of Letter 185's quotation.** *"Nebuchadnezzar's own law 'enacted... on behalf of the truth'"*; the text reads "enacted **a pious and praiseworthy law** on behalf of the truth." The elided words are the ones that support "held up as a positive model," which the document then supplies in its own voice. An ellipsis inside a quotation should not remove the words the surrounding sentence is asserting.

**C3 — §9's limb-1 clause does not parse.** *"this is this document's first Round 2 disposition"* — the document has had one Round 1 and one Round 2 review; whatever this means, it is not a reason.

**C4 — §5 characterises Donatism's "defining act" one sentence before disclaiming that it characterises Donatism.** *"Donatism's own defining act, by contrast, was the opposite: a permanent, parallel episcopate formed over the *traditio* charge..."* immediately followed by *"This is not this document's own characterization of Donatism's own defining gravity — that is not this document's to make."* The characterisation is in fact well supported (Donatism's own Doc_01 §1 and Coach3's "permanent schism into two rival hierarchies," both verified), and the Coach3 citation follows two sentences later — so the disclaimer is over-broad rather than false. Reorder so the support precedes the claim.

**C5 — §9's revision log makes a stronger claim than §5 does.** The §5 bullet says the re-check found "the two branches **independently converged** rather than in tension"; §5 itself declines to establish whether the convergence was independent. As it happens the stronger claim is the true one (see M9), which is the argument for fixing §5 rather than softening §9.

**C6 — the Ongoing/Internal table cell is a single ~110-word run-on holding four distinct forces.** It is honest and its placement judgment is properly flagged (L9 fixed), but as a table cell it is unreadable. Split it, or move the placement-judgment note below the table.

---

## Required actions before Round 4

**Must fix (HIGH):** H1 — supply the state-power half of the World #6 discharge, using §4's own Letter 185 evidence and the corpus-map double placement; reconcile it with §1's framing; and disclose the divergence from IJC Doc_01 §6's "orthogonality to state power" at §9 limb 2 alongside the Donatism disclosure that is already there.

**Must fix (MEDIUM):** all ten. M1 and M2 are mechanical but land on the Article 3 finding and the World Separation finding respectively, and M1 requires restoring one clause to a primary-source quotation. M3, M4, M7 are corrections to findings and to instructions that will otherwise propagate into Doc_02 and Doc_04. M5, M6, M9, M10 are record accuracy — three of the four are cases of the document asserting something about a record it did not check, in sections whose whole purpose is to show that records were checked. M8 is a labelling obligation plus an axis-identity overclaim.

**Apply directly:** all LOW and COSMETIC. L3 is now a second-round miss (listed "apply directly" at Round 2, not applied, and not disclosed as unapplied).

**Three process observations for the revision pass, not findings:**

1. **The verification discipline worked and should be stated as the standing rule.** Every primary-source and governing-document quotation in this draft is exact and correctly located — that was not true at Round 1 or Round 2, and it is the single largest improvement in the series. The failures that remain are almost entirely failures to check *records* (§9's account of Round 1 vs Round 2; §5's claim about what the branch record establishes; §9's "All addressed"; Step 0's now-false statement) rather than failures to check *sources*. The same habit that produced the good result on texts has not yet been extended to the build's own paper trail. It is the cheaper of the two.

2. **The stranded-fix pattern has changed shape again, and the shape is diagnostic.** At Step 0 it was sentences. At Doc_01 Round 2 it was sections and pointers. Here it is *halves of obligations*: H1 is half of a two-part Step 0 obligation discharged; M4 is half of a finding fixed where it was quoted and left where it operates; M5 is a log heading that covers most of a list; L1 is a disclosure restored in one place and not the other; L2 is a cosmetic fix applied to the annotation and not the text. The mechanical pass Round 2 recommended should be run not per-edit but per-*obligation*: for each binding item, list its parts, and check each part separately.

3. **The cross-branch move is sound and worth keeping.** Grounding a boundary in what a sibling build has already adopted, rather than asserting a characterization of a world this build does not own, is the right instinct and it survived direct verification. The two defects it carries (M8's "same axis," M9's unchecked negative) are both fixable in a sentence each, and neither impugns the method.

**Escalation check performed by this review.** Category 1 (Representative identity): not touched. Category 2 (portfolio-level/cross-world): the Coach3 axis is portfolio-level and is used without the label CO-022 requires — see M8; this is a labelling defect to fix in the document, not an escalation. Category 3 (governance/methodology): not created by this document; §8 item 9's referral of the World Separation Criteria / Layer-1 gaps to a coach pass is correctly scoped, and I independently confirmed that neither IJC's nor Donatism's Doc_01 runs World Separation Criteria — this review endorses the referral, as Round 2 did. Category 4 (unresolved tensions): limb 1 is not met, though not for the reason §9 gives (M6); limb 2 is not met on the Donatism axis — verified at source — but the IJC Doc_01 §6 divergence (H1) and the now-false statement standing in this world's cleared Step 0 (M10) are both undisclosed and must be assessed rather than omitted; limb 3 is not met. **This review does not itself escalate** — it returns the questions to the build thread with the record corrected.
