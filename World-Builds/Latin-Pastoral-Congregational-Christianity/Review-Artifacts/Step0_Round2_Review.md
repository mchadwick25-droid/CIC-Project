# Step 0 — Movement-Scope Confirmation: Latin Pastoral-Congregational Christianity
## Round 2 Independent Adversarial Review

**Document reviewed:** `World-Builds/Latin-Pastoral-Congregational-Christianity/Step0_Movement_Scope_Confirmation.md` (revision after Round 1, dated 2026-09-01)
**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread; did not draft the document under review and did not write the Round 1 review
**Governed by:** `cic-build-cycle` (CO-022) *Review* section, and this project's standing rule that a revision's own claim to have fixed something is not evidence of a fix — every Round 1 finding was re-checked directly against the actual source file, not against Round 1's account of it

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

This is a genuinely good revision and the verdict should not be read as a judgment on its quality. **Four of five high findings and all ten medium findings are verified fixed on independent re-check against source.** H1's replacement bullet is the strongest single piece of work in the document — the boundary breach it reports is real, exactly as described, and I confirmed it independently from IJC's own record files. No new fabrication was found anywhere in the new material; every quotation I could trace (and I traced all of them) matched its source.

The revision nonetheless requires another round, because it introduces five findings that meet this project's own "substantial" test — a claim's substance, a sourcing conclusion, or a scope boundary changes — plus one Round 1 high finding (H5) that is only partially discharged:

- one **false verification claim** in the new §3 B3 text ("Cyprian appears nowhere in IJC's Doc_01 or Doc_02"), which Round 1 itself asserted it had verified and which is wrong (N1) — logged here as a **disagreement with Round 1**, not a silent correction;
- one **internal contradiction** in the new B1 text, denying the existence of prior per-world Step 0 confirmations the same document names three times elsewhere (N2);
- an **over-read plus a pre-judgment** in the new Optatus material, which drives a binding §4 instruction to Doc_02 that conflicts with this document's own Article 23 reasoning (N3);
- an **unaddressed portfolio-level differentiation flag naming World #8 by name** in the Step 0 Conclusion, missed by both rounds, in the criterion (B3) it belongs to (N4);
- a **disposition-authority gap**: §6 correctly triggers escalation category 4 but does not state the consequence CO-022 attaches to it (N5);
- **H5 residue**: the A1 floor enumeration is presented as "quoted... not paraphrased" when four of five commitments are silently abridged; the parenthetical says "the fifth is directly at issue" while the sentence that follows argues the first; and Round 1's instruction to flag the identical defect in IJC was not carried out.

The required work is narrow and localized — roughly six targeted edits, none of which touches the document's conclusions. **Both top-line conclusions remain correct and should be retained: World #8 clears Section A, and Tier 1 is the right tier.**

---

## Part 1 — Round 1 findings re-verified against source

### HIGH

#### H1 — false IJC live-cross-check concealing a boundary breach — **FIX VERIFIED GENUINE**

Re-checked every object the new bullet names, by path, without relying on Round 1's account:

- `records/ijc/source/ijc.source.augustine-confessions.md` — its `work:` field does read "Confessions, Book 9 ch. 7 ONLY", and its BOUNDARY note reads verbatim: *"Augustine's formation, theology, and the rest of the Confessions belong to the Latin Pastoral-Congregational world (World #8, not yet built); do not extend this license."* The document quotes both **exactly**.
- `cic/corpus-map/imperial-juridical-christianity.yaml` — contains exactly **two** `author: augustine` rows, both `confidence: provisional`: *City of God* (`div1 4 — City of God, esp. Books I-V and XIX`) and *The Correction of the Donatists* (`div2 5.6`). The two note-fragments the document quotes ("evidence for ijc's themes rather than a work from inside it"; "Augustine is a North African pastor, not a participant in the Rome-Constantinople-Milan imperial church") are **exact**. The double-placement claim is confirmed from the other side: the LPC map's own Letter-185 note reads "Also assigned to imperial-juridical-christianity below."
- `records/ijc/quote/ijc.quote.take-up-and-read.md` — locus `Confessions VIII.12`, `evidentiary_weight: load-bearing`, `retrieval.tier: 1`. **Confirmed.**
- `records/ijc/quote/ijc.quote.i-scorned-to-be-a-little-one.md` — locus `Confessions III.5`, `evidentiary_weight: load-bearing`, `retrieval.tier: 1`. **Confirmed.**

**Additional verification Round 1 did not perform, which strengthens rather than weakens the finding.** Fifteen IJC records cite `ijc.source.augustine-confessions`. I checked the locus field of every one. The other eleven — `ijc.contested.office-holder-scope`, `ijc.dw.ancient-custom`, `ijc.figure.ambrose`, `ijc.gravity.episcopal-independence`, `ijc.limit.f5-ordinary-day`, `ijc.limit.reading-alone`, `ijc.story.vigil-in-basilica`, `ijc.term.imperator-intra-ecclesiam`, and the two 9.7 quotes — all stay inside IX.7. **The breach is exactly the two quote records the document names, and no more.** The document's characterization is therefore not merely accurate but complete: it neither understates nor inflates the scope of the contradiction.

§6 now escalates this under CO-022's fourth category rather than asserting no tension exists. The escalation is substantively correct and correctly scoped ("outside this thread's write scope" matches the skill's own line: "A build thread's write access is scoped to its own world's build folder"). Two smaller problems with *how* it is escalated are at N5 and N7 below; the finding itself is properly discharged.

#### H2 — false Jerome-absence claim — **FIX VERIFIED GENUINE**

- `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` holds the Augustine–Jerome correspondence row: 17 letters, `~52,892 words`, `role: tradition`, `confidence: assigned`. Its note reads "`tradition` for BOTH entries deliberately - the exchange contains Jerome's own letters, which are the Hieronymian world's voice, and Augustine's, which are the Latin pastoral world's" and "It is also the largest single thing in this volume after the Confessions." The document quotes both fragments **exactly**.
- `cic/corpus-map/hieronymian-ascetic-literary.yaml` carries the identical mirror row, plus `The City of God, Book XVIII, chapters 42-44` at `role: context`, whose note reads "Augustine is the other side of this entry's central argument." The document's quotation ("the other side of this entry's central argument") is **exact**.
- `hal_Doc_01_World_Identification_Boundaries_Orientation.md` §8.1 — all three quoted fragments verified **exact**: "This world's own evidence, not World #8's content"; "World #8 has not been built and its documents have not been read"; "leaves the comparison's other half to World #8's own, independently-sourced construction." The section also records, as the document says, that an earlier hal draft was corrected for asserting facts about Augustine without independent basis.

Carried forward correctly at §4 items 2 and 5. The corrective framing ("**Correction to an earlier draft of this document, which claimed... false**") is honest and specific.

#### H3 — fabricated B1-scores citation — **FIX VERIFIED GENUINE (removal), but the replacement introduces a new error**

The strings "B1 score", "Desert Monasticism", and "strengthened" do not appear anywhere in the current document. The claim is deleted, not reworded to still imply it, and the replacement correctly re-homes the "Formation Narrative Sources" category to CF V7.4's Step 2 activity list / Doc_02. **The fabrication is gone.**

However, the replacement clause's stated *reason* is itself false — see **N2** below.

#### H4 — A5 elision and the "routing" over-read — **FIX VERIFIED GENUINE**

Checked against `docx_extract/step0_methodology.txt`, the actual Section A text:

- A5's sentence (methodology line 24) reads: "Where a movement contains multiple internal strands under Article 21, eligibility is assessed at the world level against its established strands as a whole — including whichever strand(s) meet the floor — never strand-by-strand in a way that lets one divergent internal strand exclude an otherwise-eligible world." The document now quotes **"eligibility... assessed at the world level against its established strands as a whole — including whichever strand(s) meet the floor"** — the previously elided, disqualifying clause is **restored**, and A5 is quoted only once in the document, so there is no second, un-restored instance.
- The "routing" claim is gone. The word "routing" survives only inside a disavowal ("no routing rule, elision, or interpretive stretch is needed").
- The replacement argument is the plain reading Round 1 recommended, and every textual support it cites checks out: the Procedure's screening instruction is verbatim "Test each candidate against A1 (and A2 or A3 as applicable)" (line 45); Section B's five criteria are Sourcing, Ecology, Uniqueness, User Needs, Scale (lines 28–42); nothing in Section A or B tests Article 3 coherence. **Correct.**
- §5 item 1 now removes the falsified "the pattern held up without needing invention" claim and says so explicitly. §6 now describes the move as interpretation, "honestly stated as interpretation rather than pure mechanical lookup," matching IJC's cleared framing.

One low-severity residue at N9.

#### H5 — Article 4 floor restatement — **PARTIALLY FIXED; three residues remain**

Checked against `docx_extract/constitution.txt`, "On the Scope of 'Movement'" (lines 157–168).

**What is fixed.** The prohibited sentence is gone; Article 4's own prohibition is now quoted **exactly** ("This is the authoritative statement of the floor's content; the Construction Framework's Step 0 operationalizes it procedurally and must not restate it independently — where the two differ, this Article governs"); the first commitment is no longer dropped — all five are present; and the anti-dualist first commitment is now given the substantive treatment this world's anti-Manichaean corpus warrants, which is a real improvement, not a patch. I verified the supporting claim independently: `npnf104_augustine-anti-manichaean-anti-donatist.xml` exists and the LPC corpus map assigns seven anti-Manichaean works from it to this world.

**Residue 1 — the enumeration is described as quoted when it is abridged.** The text reads "Article 4's five commitments (quoted here only because... not paraphrased)". Checked word by word against the Constitution:

| # | Article 4 | Document | Status |
|---|---|---|---|
| 1 | "One God, the Father, the Almighty, maker of heaven and earth, of all that is, seen and unseen." | identical | verbatim |
| 2 | "Jesus Christ as the only Son of God, eternally begotten of the Father, God from God, Light from Light, true God from true God, begotten not made, of one Being with the Father." | "Christ as the only Son, eternally begotten, of one Being with the Father" | **abridged, no ellipsis** |
| 3 | "Jesus Christ as truly human — incarnate of the Holy Spirit and the Virgin Mary, 'became truly human.'" | "Christ as truly human" | **abridged, no ellipsis** |
| 4 | "Christ's death under Pontius Pilate, burial, bodily resurrection on the third day, ascension, and his return in glory to judge the living and the dead." | "Christ's death, burial, bodily resurrection, ascension, and return in glory" | **abridged, no ellipsis** |
| 5 | "The Holy Spirit as Lord and giver of life, worshiped and glorified together with the Father and the Son." | "...worshiped and glorified with the Father and Son" | **"together" dropped** |

The abridgements are not substantively misleading — nothing affirmed is altered. But Round 1's fix instruction was explicit: "quote Article 4's five bullets **verbatim** rather than paraphrasing them." The document does the opposite and then asserts it did not. That is a provenance-accuracy defect in the exact section Round 1 flagged, and the "not paraphrased" parenthetical makes it a claim about the text rather than a stylistic choice. **Fix: either quote all five verbatim, or mark the abridgements with ellipses and drop the "not paraphrased" claim.**

**Residue 2 — internal contradiction inside the same sentence-pair.** The parenthetical says the five are quoted "only because **the fifth** is directly at issue for this world." The very next sentence argues that "The **first** commitment... is not incidental for this world specifically," and the entire supporting argument (anti-Manichaean corpus, nine years as an auditor) is about the first. Nothing in A1 makes the Spirit-clause "directly at issue." This reads as an uncorrected artifact of the edit and should say "the first."

**Residue 3 — Round 1's IJC-propagation instruction not carried out.** Round 1's H5 closed: "flag the IJC instance for the same correction." I confirmed the defect is still live there — `Imperial-Juridical-Christianity/Step0_Movement_Scope_Confirmation.md` §2 A1 still carries the identical four-item restatement, and that document is at *Approved to proceed*. Nothing in this revision's §5 (process findings for System Hub) or §6 flags it. Fixing IJC's file is correctly outside this thread's write scope, but flagging it in §5 is not — and §5 is precisely where this document already routes three other cross-world process items. **Fix: add a §5 item.**

### MEDIUM

| # | Finding | Verdict | Verification performed |
|---|---|---|---|
| **M1** | "Ecclesiastes-style subordinationist" → "Ebionite" | **FIX VERIFIED GENUINE** | Methodology line 10 reads "(Gnostic, Marcionite, Ebionite, and similar groups)". §2 A2 now reads "(Gnostic, Marcionite, **Ebionite**, or similar)". Not presented as a verbatim quote, so the "or similar" variant is fine. "Ecclesiastes" appears nowhere in the document. |
| **M2** | Article 20 misrouted to Doc_01 | **FIX VERIFIED GENUINE** | §2 A5 now splits the sentence correctly (Article 21 → Step 1; Article 20 → "Construction Framework Step 2 activity (Doc_02)") and names the correction. §4 item 3 carries the Article 20 duty and states it "belongs here, not at Doc_01 (correcting §2 A5's earlier misrouting)." Internally consistent; the false "per the Framework's own text" grounding for the Step 1 claim is gone. |
| **M3** | §0 ignores "never a per-world process"; IJC Findings 2 and 3 unreported | **FIX VERIFIED GENUINE** | §0 now quotes both Methodology fragments **exactly** — "a phase-level process, run once when the project opens a new release phase, never a per-world process" (line 27) and "phase-level, run once per new release phase" (line 43) — and gives the reason the pass runs anyway. §5 item 2 reports IJC Finding 3 as still open, quoting it **exactly** against IJC's §5 (verified). §5 item 3 reports Finding 2. §2 disposes of Criterion 2 on the merits, quoting the Step 0 Conclusion's Criterion-2 sentence **exactly** (conclusion line 8). I independently confirmed §5 item 2's claim that System Hub has not acted: no per-world Step 0 output template exists anywhere in the repository. |
| **M4** | Corpus-map characterization of the two anonymous treatises | **FIX VERIFIED GENUINE** | Checked all three rows directly. *Acts of the Council of Carthage under Cyprian (256)* — `confidence: provisional`, note reads "Donatism is included as shared ancestry rather than heresiology... tradition claimed by both sides"; the document's quotation is **exact**. *Anonymous Treatise Against the Heretic Novatian* — note reads "Assigned to novatianism as the movement it argues against"; the document now correctly says novatianism, **not** donatism. *Anonymous Treatise on Re-baptism* — note reads "Its bearing on donatism's prehistory is noted but **not assigned**"; the document now correctly reports it as "noted but left unassigned." §4 item 2(b)/(c) match. All three corrections are real. One incompleteness at N8. |
| **M5** | Optatus omitted | **FIXED, BUT OVERSHOT** | The row is now present and accurately transcribed: `author: optatus`, `confidence: provisional`, and the note's "Mark may prefer another Latin home for a Numidian polemicist" is quoted **exactly** (this is a legitimate verbatim corpus-map quotation, not a CO-022 (a) attribution violation). The omission is genuinely fixed. But the surrounding argument and the §4 instruction built on it introduce a new problem — see **N3**. |
| **M6** | §0 vs §3/§4 on "only other world" | **FIX VERIFIED GENUINE** | §0 now reads "a third instance of the same pattern exists in parallel... on a sibling branch (`origin/claude/record-native-world-build-v2-e2s0dt`, not merged into this working tree) — read directly via `git show`". §5 item 1 matches ("the second... in this working tree... with a third (Donatism) in parallel"). No contradiction remains. |
| **M7** | "No live cross-document check is possible" | **FIX VERIFIED GENUINE** | I ran `git show origin/claude/record-native-world-build-v2-e2s0dt:World-Builds/Donatism/Step0_Movement_Scope_Confirmation.md` myself. The file exists (132 lines, dated 2026-09-01) and is the only file in that directory on that branch. The impossibility claim is gone; the check was actually run and is cited by branch and path. The reciprocal Article 23 obligation is now stated at §2 A5 and §4 item 2(d). **The long quotation of Donatism's A5 finding is exact** — I diffed it against §2 A5 of the branch file; the ellipses elide only "Caecilian's Carthaginian communion, and above all Optatus and Augustine, whose writings supply nearly the entire surviving documentary record", "(a persecuted 'Church of the Martyrs' facing a state-favored rival), not merely cite Optatus and Augustine as neutral sources", and "(Homoian Christianity as World #6's internal opponent)" — none of which changes the meaning. One low residue at N6. |
| **M8** | Missing reciprocal obligations from two built worlds | **FIX VERIFIED GENUINE** | §4 item 5 is new and correct. IJC's §4 item 3 is quoted **exactly** ("The authority-structure/state-power boundary... must be stated explicitly in Doc_01, since World #8 is not yet built and cannot itself hold the line from its side"), the condition-has-changed reasoning is right, and hal Doc_01 §8.1's outstanding request is separately and distinctly carried. |
| **M9** | Cyprian/Tertullian vocabulary misattribution | **FIX VERIFIED GENUINE** | §2 A2 now says Cyprian "works *within*, and directly transmits into the Latin pastoral tradition, the vocabulary Tertullian himself forged," and cites three corpus-map notes. All three verified **exact**: "reworks Tertullian's De Patientia" (line 658), "dependent on Tertullian's De Oratione" (line 686), "following Tertullian's dress treatises" (line 667). The Tertullian dropped-voice disclosure is now carried at §1 and §4 item 6, and the Step 0 Conclusion quotation behind it is **exact** (conclusion line 79). |
| **M10** | B2 compresses three phases of Cyprian's episcopate | **FIX VERIFIED GENUINE** | §3 B2 now separates them exactly as Round 1 specified: hiding during the Decian persecution (c. early 250–spring 251, persecution/lapsed/*libelli*); post-return Felicissimus and Novatianist schisms and *De Lapsis* (251); plague and *De Mortalitate* (c. 252–253). Historically correct. |

### LOW / COSMETIC

- **L1 (NPNF volume count) — FIXED.** Now "the complete **Augustine** portion of NPNF Series I — volumes 1 through 8 of that fourteen-volume series... volumes 9–14 are Chrysostom." Verified on disk: `npnf101`–`npnf108` are Augustine, `npnf109` is Chrysostom.
- **L2 (Cyprian corpus qualifications) — FIXED.** All three named qualifications are present and accurately quoted: embedded letters by Cornelius/Roman clergy/Firmilian/confessors; the council acts singularized with the 255 and earlier-256 councils named as non-extant; the four pseudo-Cyprianic treatises with the "two of them commonly given to Novatian" note and the 2026-08-26 ruling.
- **L3 (B4 doubt / *De Lapsis*) — FIXED.** Doubt is now attributed to Augustine specifically with Cyprian expressly excluded; *De Lapsis* is recharacterized as Round 1 specified.
- **L4 (§6 self-characterization) — FIXED.** §6 now says "honestly stated as interpretation rather than pure mechanical lookup," which matches IJC's cleared text ("not a pure mechanical lookup"). *Note, in fairness to the document:* IJC's cleared §6 **does** retain the "without adding a new test, waiving a stated requirement" formulation, so reproducing that half was never the defect — only the "direct application rather than novel interpretation" framing was removed there, and this document does not reproduce it. The secondary half of L4 (IJC's Round 3 codification disclosure) has no exact analogue here; §5 item 4 does make a process recommendation whose adoption would change practice, and disclosing that would be tidier, but this is not a defect.
- **L5 (ranking claim) — PARTIALLY FIXED.** Round 1 said "cut, or attribute to a named scholarly source." The document retains "one of the two or three most consequential" and appends a disclaimer ("not on the strength of a ranking claim, but on his own corpus's own terms"). The argument no longer *rests* on the claim, which addresses the substance, but the unfalsifiable assertion is still made. Low; a clean cut would be better.
- **C1 (quote marks) — NOT APPLIED, and defensibly so.** §2 still renders the Step 0 Conclusion's curly doubles around "sufficient historical coherence" as single quotes. Since the whole passage now sits inside a double-quoted italic block, nested single quotes are ordinary typographic convention rather than a misquotation. I would not press this.
- **C2 (CF version status) — NOT APPLIED.** The header still reads "Construction Framework V7.4's Step 0 stub"; IJC's header reads "V7.4 DRAFT's Step 0 stub." Cosmetic, and the naming-and-term-propagation rule makes consistency across the two documents of this type worth one word.

---

## Part 2 — New findings

### N1 (Medium) — "Cyprian appears nowhere in IJC's Doc_01 or Doc_02" is false, and Round 1 was wrong to certify it

**Where.** §3 B3, first sub-bullet: "Cyprian appears nowhere in IJC's Doc_01 or Doc_02. **True, and distinct.**"

**What's wrong.** A case-insensitive search of the entire IJC build folder returns three hits for "Cyprian." One of them is `World-Builds/Imperial-Juridical-Christianity/Doc_01_World_Identification_Boundaries_Orientation.md` §6 ("World Continuity & Distinction"):

> "- **World #8 (Latin Pastoral-Congregational Christianity, not yet built — Cyprian and Augustine):** already confirmed distinct in the Step 0 Conclusion and reaffirmed in `Step0_Movement_Scope_Confirmation.md` §3 — non-overlapping authority structure..."

`Doc_02_Source_Ecology.md` has zero occurrences, so half the claim holds. **Doc_01 does not.**

**Disagreement with Round 1, logged rather than silently resolved.** This wording is not the drafter's invention — Round 1's H1 *Fix* instruction dictated it verbatim and certified it: *"State: (a) Cyprian appears nowhere in IJC's Doc_01 or Doc_02 — that part is true and was verified here."* Round 1's "Checked and found clean" section also lists its IJC-precedent claims as all verified. **Round 1 was wrong on this specific point.** The revision did the right thing by following its reviewer; the reviewer had not run the check it said it ran. Per this project's rule that disagreements between rounds are logged rather than decided by recency, both facts are recorded here: Round 1 asserted a verification it did not perform, and the current document inherited the error in good faith.

**Why it still matters.** The bullet's bolded verdict ("**True, and distinct.**") presents this as the product of a live check, in the very bullet whose Round 1 defect was a live-check claim at the wrong scope. It is CO-022 failure mode (b) reappearing one level down.

**The substantive conclusion is unaffected and is in fact strengthened.** Cyprian appears in IJC's Doc_01 *only* in the boundaries section, *only* as the neighbour world's named figure, and *never* as an IJC actor — which is exactly what "distinct" means. **Fix:** "Cyprian appears in IJC's Doc_01 only once, in §6's boundary bullet naming World #8's own figures, and nowhere in Doc_02 — he is named as this world's figure, never as an IJC actor."

### N2 (Medium) — the replacement for H3's fabrication asserts something the document itself contradicts three times

**Where.** §3 B1, final bullet: Pontius's *Life* is "noted here as a real Doc_02 asset, not as evidence toward any prior world's own score, **since no other world in this portfolio has yet run a per-world Step 0 confirmation of this kind**."

**What's wrong.** Another world has. IJC's is at `World-Builds/Imperial-Juridical-Christianity/Step0_Movement_Scope_Confirmation.md`, it is cited by path in this document's own §0, and it contains a full Section B walkthrough with its own B1 reasoning. Donatism's is on the sibling branch. The same document says so at §0 ("the one prior document of this exact type"), §5 item 1 ("the second per-world Step 0 confirmation... with a third (Donatism) in parallel"), and §5 item 2 ("They have recurred — this document, and the parallel Donatism draft").

The *conclusion* is right — neither Hieronymian nor Desert Monasticism has a B1 score, because neither has a Step 0 confirmation of this kind. The *reason given* is false as written, and it is false in the direction that matters: the document is at its most careful about not over-claiming prior-world findings, and the sentence it uses to be careful denies a fact it relies on elsewhere.

**Fix.** "…not as evidence toward any prior world's own score, since the only prior per-world Step 0 confirmations (IJC, and the parallel Donatism draft) assign no Section B scores to other worlds, and neither Hieronymian nor Desert Monasticism has one at all."

### N3 (Medium) — the Optatus material over-reads its source, pre-judges an open question, and contradicts this document's own Article 23 reasoning

**Where.** §3 B3, World #4 bullet, and §4 item 2(a).

Three distinct problems, in ascending order of consequence.

**(a) The portfolio-entry parenthetical is scoped to Cyprian, not to the world.** The document writes: "Optatus is nothing but the schism-crisis angle this world's own portfolio entry says explicitly does *not* belong here." The entry's actual sentence (Step 0 Conclusion, verified line 20) reads: "**Cyprian as working pastor navigating the Decian persecution and its aftermath (not the schism-crisis angle, which belongs to world #4)**, Augustine's preaching, catechesis, and ordinary sacramental administration…" The parenthetical sits inside the Cyprian clause and qualifies *Cyprian's characterization*. It is not a blanket rule that schism-crisis material cannot live in World #8.

**(b) Read as a blanket rule, it contradicts the document elsewhere.** If "the schism-crisis angle does not belong here" excluded Optatus, it would equally exclude Augustine's *On Baptism, Against the Donatists*, *Answer to the Letters of Petilian*, and *The Correction of the Donatists* — all assigned to this world in the corpus map at `confidence: assigned`, all listed by this document's own §3 B1 as this world's assets, and all necessary to the obligation §2 A5 and §4 item 2(d) impose: that Doc_02 "must reconstruct the Donatist schism as this world's own internal rival… from inside this world's own perspective (an ordinary episcopal communion defending its own continuity and communion)." **Optatus is the paradigm text for exactly that reconstruction.** The corpus map says so in its own terms: "Tradition for the Catholic side of the schism; this entry… is the census's home for that tradition."

**(c) §4 item 2(a) pre-judges the answer, going past Round 1's instruction.** Round 1's M5 fix asked for Optatus to be added "as a specific, named, currently-provisional assignment Doc_02 must resolve — noting that the corpus-map itself flags the placement as inferred and open." The document adds it and then decides it: Optatus "**should very likely be re-homed there**, not defaulted into this world's Source Registry." That is a binding instruction to Doc_02 resting on (a) and cutting against (b). The corpus map's own open question is narrower than the document's answer — "Mark may prefer another **Latin home**" contemplates a different Latin world, and does not name Donatism at all.

**(d) A supporting attribution does not match its cited source.** The document says the check "confirms that document's own §3 B1 lists Optatus as *Donatism's* primary documentary asset," and §4 item 2(a) repeats "per Donatism's own Step 0 confirmation." Donatism's §3 B1 lists Optatus **first** and calls it "the earliest substantial Catholic polemical treatise against the schism" whose appendix is "this world's closest analogue to World #6's imperial legal material" — while naming Augustine's anti-Donatist corpus as "**by far the largest body of surviving evidence**." "Primary documentary asset" is a defensible gloss on the appendix argument, and `cic/texts/README.md` independently calls the file "THE primary source for Donatism" — but that is not what the cited document says, and the citation is the one the sentence leans on.

**Fix.** Keep the Optatus row, its provisional status, and the instruction that Doc_02 must resolve it. Drop "should very likely be re-homed there" in favour of naming the actual options (re-home to Donatism / hold here as the Catholic-side tradition per the corpus map's stated reason / double-place, as the Council of Carthage row is). Scope the portfolio-entry parenthetical to Cyprian. Attribute "primary source for Donatism" to `cic/texts/README.md`, and describe Donatism's own §3 B1 as listing Optatus first among its documentary assets.

### N4 (Medium) — an on-record portfolio-level differentiation flag naming World #8 is not carried forward, and B3's last bullet leans on the grounds it discounts

**Where.** §3 B3, final bullet, and §4 (which carries no such obligation).

**What's missing.** The Step 0 Conclusion — which §0 calls "supporting evidence and required grounding" — holds a standing, unresolved differentiation question addressed to this world by number, in two places:

> "8. Antiochene Christianity (Chrysostom-centered) proposed, reviewed, and held out of Phase One — carried forward to Possible Future Worlds below, **pending a validated primary-gravity contrast against world #8 that doesn't rely on geography or language**."

> "…**Held out of Phase One because its distinctiveness from world #8 is not yet demonstrated once geography and language are set aside.** Genuine strengths not currently represented in the nine: rich ordinary-lay ethical-formation material…"

The document mentions Antiochene Christianity nowhere. §1 explicitly frames this document as sweeping the Conclusion for obligations this world's own entry created ("A disclosure obligation this world's own portfolio entry created, not yet carried forward in this document until now"), and §4 carries forward the Tertullian item and the Primary-gravity-first item from that same list — but not this one.

**Why it matters, and the compounding problem.** B3's own final bullet dismisses Worlds #5 and #2 as "distinct on language (Latin vs. Greek), region (North Africa vs. Anatolia/Alexandria), and formation logic," and closes: "not elaborated further here **since no adjacency this close was flagged in the Step 0 Conclusion for this pairing**." The Conclusion *did* flag an adjacency this close for World #8 — with Antiochene — and flagged it precisely on the ground that **geography and language do not settle it**. So the document (i) makes a claim about what the Conclusion flagged that is incomplete on the one world it concerns, and (ii) rests its remaining differentiation reasoning on the two grounds the Conclusion set aside for this world's hardest adjacency case.

There is a substantive edge to it as well: the Conclusion names Antiochene's unrepresented strength as "rich ordinary-lay ethical-formation material," which is the same register §3 B2 claims as this world's distinctive strength ("plausibly the *richest* ordinary-believer, ordinary-worship, ordinary-formation world in the confirmed portfolio to date"). B2's superlative is safe as written, since it is scoped to the *confirmed* portfolio — but the adjacency is live and the document should know it.

I record that Round 1 did not catch this either; this is not a defect the revision introduced.

**Fix.** Add a short B3 sub-bullet: Antiochene Christianity is not selected for this phase, so B3's "relative to what is already selected or built" test does not reach it — but the Conclusion holds a standing, unresolved primary-gravity contrast against this world that geography and language may not settle, and it is logged here rather than assumed absent. Add a matching §4 carry-forward binding Doc_01/Doc_04's gravity work to state this world's primary gravity in terms that would survive that contrast. Correct the "no adjacency this close was flagged" clause.

### N5 (Medium) — §6 triggers escalation category 4 but does not state what CO-022 attaches to it

**Where.** §6, escalation paragraph and closing line.

**What's wrong.** §6 correctly concludes that "**One finding does escalate, under CO-022's fourth standing category**." The skill's own rule on that is unconditional: "Before disposing of any document, check it against these four categories. **If any apply, stop and escalate directly to the project lead — do not self-dispose, regardless of how clean the review came back.**" Disposition eligibility likewise requires "none of the four escalation categories applies."

The document does not say this. It says instead that the finding is "Flagged here for the project lead and/or System Hub's attention" and that "This document's own eligibility conclusion does not depend on how that contradiction is resolved" — a true statement about the *conclusion's soundness* that reads, in the disposition section, as though it also settles the *disposition question*. It closes with "**Pending:** independent adversarial review (Round 2)" and nothing further.

Compare IJC's §6, which is careful in exactly this place, and whose status line records self-disposition explicitly conditioned on "no escalation category applies."

**Why it matters.** The next decision after this review is a disposition decision. Getting the authority question right is the specific discipline CO-022 exists to enforce, and a reader reaching §6 after a clean Round 3 could reasonably conclude this document self-disposes.

**Fix.** One sentence in §6: because a category-4 item applies, this document goes to the project lead rather than being self-disposed by the build thread, whatever the review rounds return. It costs nothing and removes the ambiguity.

### N6 (Low) — a residue of M7's failure class in §2 A5

**Where.** §2, A5, final paragraph: "Both worlds' Step 0 confirmations, drafted the same day, independently name this boundary and independently note it cannot be *fully* cross-checked while the two branches remain unmerged."

Two problems. First, unmergedness blocked nothing: the entire Donatism directory on that branch is one file, and this document read it via `git show` — which is the fix M7 required. What limits the cross-check is that Donatism has only a Step 0, not that the branches are unmerged. Second, the Donatism document does not give that reason. Its §3 B3 says "**Not built yet**, so no live cross-document check was possible," and its §4 item 4 says World #8 "is not yet built" — neither mentions branches. Attributing a branch-state rationale to both documents is inaccurate to one of them. Minor, but it is an environment-based limitation claim in the same slot Round 1 flagged.

### N7 (Low) — CO-022's category 4 is misquoted

**Where.** §6: "specifically 'a contradiction **discovered** between two already-cleared master documents.'"

The skill's text reads: "a contradiction between two already-cleared master documents, or a finding that cuts against an earlier decision." "Discovered" is inserted inside quotation marks.

Worth noting alongside it: the **second** limb is the better fit for this finding and goes uncited. What §3 B3 found is a contradiction *inside one world's* record set — the document says so itself ("a contradiction inside IJC's own already-built record set") — between a source record's binding boundary note and two later quote records. That is squarely "a finding that cuts against an earlier decision," and less squarely "two already-cleared master documents," since IJC's records are records rather than master documents. The escalation is right; the limb quoted is the weakest available and is misquoted. **Fix:** quote the category accurately and cite both limbs.

### N8 (Low) — the Council of Carthage under Cyprian is modelled twice in the corpus map, and only one row carries the Donatism note

**Where.** §4 item 2(b): "the Council of Carthage under Cyprian (256) is a genuine, corpus-map-modeled double-placement with Donatism and should be carried as such."

True of the row the document means — `The Acts of the Council of Carthage under Cyprian (256, on baptism)`, `author: council-of-carthage-under-cyprian`, `source_file: npnf214_seven-ecumenical-councils.xml`, `confidence: provisional`, with the shared-ancestry note. But the same conciliar text is modelled a second time in the same file as `The Seventh Council of Carthage under Cyprian (on the baptism of heretics)`, `author: cyprian`, `source_file: anf05_hippolytus-cyprian-caius-novatian.xml`, `confidence: assigned` — same event, same 87 bishops, same September 256 sententiae, different vendored edition, and **no Donatism double-placement note**. §3 B1's Cyprian bullet cites the anf05 edition; §4 item 2(b) relies on the npnf214 row's note.

Not a false claim — a genuine duplication in the corpus map that Doc_02 will hit and that this is the cheapest place to flag. **Fix:** one clause naming both rows and the divergence between them.

### N9 (Low) — "quoted here in full" is not quite true of A5

§2 says the strand clause is "quoted here in full." What is quoted in full is the *clause*; A5's sentence also contains "Where a movement contains multiple internal strands under Article 21," and "never strand-by-strand in a way that lets one divergent internal strand exclude an otherwise-eligible world." The reading the document builds is unaffected, and the previously-elided disqualifying words are genuinely restored — but after an H-severity elision finding, "in full" invites the exact check it does not survive. **Fix:** "with the previously elided clause restored."

---

## Part 3 — Checked and found clean

Stated explicitly rather than omitted, since Round 1 set that precedent.

**Verbatim quotation accuracy — every quotation in the document traced to source.** §1's block quotation of the Step 0 Conclusion's World #8 entry: **exact**, character for character. The Tertullian disclosure: **exact**. The Criterion 2 sentence: **exact**. The Article 3 "Constitutional ambiguity flagged, not resolved" passage: **exact** but for C1's nested quote marks. The Primary-gravity-first hedge at §4 item 7: **exact**, and its provenance account (adopted in response to a review finding about the #8/#9 split's use of neighbour-protection) matches the Conclusion's own entry. Section A's framing paragraph: **exact**. Article 4's "must not restate it independently" sentence: **exact**. The Methodology's "never a per-world process," "phase-level, run once per new release phase," and "Test each candidate against A1 (and A2 or A3 as applicable)": all **exact**. IJC's §4 item 3 and §5 Finding 3: both **exact**. hal Doc_01 §8.1's three fragments: all **exact**. The Donatism A5 passage: **exact**, with non-distorting ellipses. The IJC source record's `work:` field and BOUNDARY note: **exact**. All corpus-map note fragments (City of God, Correction of the Donatists, the Jerome correspondence, the three anonymous/council rows, Optatus, the three Tertullian-dependence notes, the pseudo-Cyprianic ruling): **exact**.

**Corpus figures — re-checked, not inherited from Round 1.** ~97 sermons "preached to his own congregations at Hippo and Carthage" (matches the row's own wording); *Enarrationes* at ~695,000 words, "the largest single body in the vendored corpus," c. 392–420 = "nearly three decades"; 168 letters; the 17-letter / ~52,892-word Jerome sub-corpus; 82 epistles of Cyprian; the September 256 sententiae of 87 bishops. All match. `anf05_hippolytus-cyprian-caius-novatian.xml`, `npnf101`–`npnf108`, `npnf104`, and `optatus_against-the-donatists.txt` all exist on disk. `Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_2.md`, cited in the header, exists.

**CO-022 named failure modes, re-run against the revised text.**
- **(a) Attribution to "the project lead"/"Mark" without a verbatim sourced quote — CLEAN.** The single "Mark" occurrence is a verbatim quotation of the Optatus corpus-map note, correctly marked as such. That is the legitimate surfacing Round 1 anticipated, not an attribution.
- **(b) Content described as checked that wasn't — ONE INSTANCE, N1.** Every other "check" claim in the revision was independently re-run here and holds: the IJC record-set check, the corpus-map checks on both sides, the hal Doc_01 check, the Donatism branch check.
- **(c) Fabricated citation or fact — CLEAN.** No fabrication found anywhere in the new material. Every identifier, path, branch, figure, and quotation resolves. N2 is an internally-contradicted rationale, not a fabricated source.
- **(d) Build output outside the canonical folder — CLEAN.**

**Disposition discipline — CLEAN in the status line.** "DRAFT — Round 1... returned SUBSTANTIAL REVISION REQUIRED... this is the revision, pending Round 2." No disposition self-assigned, "Frozen" not claimed, §6 closes "Pending: independent adversarial review (Round 2)." The forward-looking gap is N5, not the status line.

**§6's revision history is accurate.** I checked each of its fifteen specific "addressed" claims against the corresponding text. Fourteen are accurate. The one that is not — "A1 no longer restates the floor and covers all five commitments" — is half right: all five are now covered, but A1 does still enumerate the floor while asserting it does not, which is H5's residue.

**Internal consistency across the document — checked as a whole, not section by section.** §6's escalation matches what §3 B3 found, in scope and in wording. §5 item 4's process finding matches §3 B3 and §6. §4 item 3's Article 20 routing matches §2 A5's correction. §0's account of the Donatism parallel matches §2 A5, §3 B3, §4 item 2 and §5 items 1–2. §2's century-gap resolution matches §4 item 1 and §6's escalation-category assessment. B1's qualifications match B2's and B4's characterizations. The four inconsistencies found are N1, N2, N3(b), and H5's residue 2; nothing else in the document contradicts anything else in it.

**Conclusions that survive review.** World #8 clears Section A, on the reasoning as now rebuilt. Tier 1 is correct against the Methodology's own rubric (verified against Procedure step 4's Tier 1 definition). B2, B4 and B5 are sound. §4 items 1, 5, 6 and 7 are well-grounded and accurately sourced. The H1 escalation is the document's best work and should survive revision untouched.

---

## Summary of required actions

| # | Severity | Action |
|---|---|---|
| H5-r | High (residue) | A1: quote all five commitments verbatim or mark the abridgements; change "the fifth is directly at issue" to "the first"; add a §5 item flagging IJC's identical A1 restatement for the same correction |
| N1 | Medium | Correct "Cyprian appears nowhere in IJC's Doc_01 or Doc_02" — he appears once, in Doc_01 §6's World #8 boundary bullet, never as an IJC actor |
| N2 | Medium | Correct "no other world in this portfolio has yet run a per-world Step 0 confirmation of this kind" — IJC has, and Donatism has |
| N3 | Medium | Optatus: scope the portfolio-entry parenthetical to Cyprian; replace "should very likely be re-homed there" with the named options Doc_02 must choose between; re-attribute "primary source for Donatism" to `cic/texts/README.md` |
| N4 | Medium | Carry forward the Step 0 Conclusion's standing Antiochene primary-gravity contrast against World #8; correct "no adjacency this close was flagged" |
| N5 | Medium | State in §6 that an applicable escalation category bars self-disposition per CO-022 |
| N6–N9 | Low | Branch-state rationale in §2 A5; CO-022 category-4 quotation and limb; the duplicated Council of Carthage rows; "quoted here in full" |
| L5, C1, C2 | Low/Cosmetic | Ranking claim; nested quote marks (defensible as is); CF "V7.4 DRAFT" wording |

Per `cic-build-cycle`, H5's residue and findings N1–N5 each change a claim's substance, a sourcing conclusion, or a scope boundary, so the revision required is **substantial** and the revised document requires a fresh review round rather than direct application. The work itself is small and localized; none of it touches the document's conclusions, and none of it revisits ground Round 1 already closed.

## Disagreements with Round 1, logged per protocol

1. **Round 1 was wrong that "Cyprian appears nowhere in IJC's Doc_01 or Doc_02."** It stated this as verified in both its H1 *Fix* and its "Checked and found clean" section. IJC's `Doc_01_World_Identification_Boundaries_Orientation.md` §6 names him. See N1. The revision followed its reviewer correctly; the reviewer had not run the check.
2. **Round 1 missed the Antiochene flag.** The Step 0 Conclusion holds an explicit, unresolved differentiation question naming World #8 twice, on grounds that expressly exclude geography and language, and Round 1's B3 assessment did not surface it. See N4. Recorded as a Round 1 gap, not a revision defect.
3. **Round 1's L4 was half right.** IJC's *cleared* §6 retains the "without adding a new test, waiving a stated requirement" formulation; only the "direct application rather than a novel methodology interpretation" framing was removed there. Reproducing the former was never the defect. This does not change L4's disposition — the fix Round 1 asked for was the right one and has been applied — but the characterization of IJC's cleared text was inexact.
