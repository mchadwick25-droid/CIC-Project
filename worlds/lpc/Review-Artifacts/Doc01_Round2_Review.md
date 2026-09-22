# Doc_01 — World Identification, Boundaries, and Orientation: Latin Pastoral-Congregational Christianity
## Round 2 Independent Adversarial Review

**Document reviewed:** `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT — revision responding to Round 1, 2026-09-01)
**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread. Did not draft the document under review, did not draft this world's Step 0, did not write the Step 0 review rounds, and **did not write the Round 1 Doc_01 review** — Round 1's own findings and its suggested fixes were treated as claims to be re-derived, not as authority. (This matters: two defects below are Round 1's own errors, imported into the revision on trust.)
**Governed by:** `cic-build-cycle` (CO-022) *Review* and *Revision decision* sections; Construction Framework V7.4 Part I and Step 1; Constitution V2.2 Articles 3, 4, 15, 21, 22, 23, 29; Forces Framework V1.1 Section 4; RCF V3.2 Part Four.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 4 HIGH · 10 MEDIUM · 9 LOW · 6 COSMETIC.**

This is a much better document than the one Round 1 reviewed. Twenty-eight of Round 1's thirty-three findings are genuinely fixed, several of them well — the Article 15 quotation is now verbatim and its gloss is marked as a gloss; the *De Baptismo* characterization is not merely corrected but corrected into a sharper argument; the World #9 discharge is rebuilt on Cyprian's own Ep. 67, which I verified word-for-word in the vendored ANF05; the reading divergence is actually resolved instead of deferred; the freeze checkpoint is now M2 and the process document really does say M2. The document also does something rare and creditable: it narrates its own two largest Round 1 errors in the body text rather than burying them in a revision log.

It nonetheless fails at Round 2, on one dominant ground and three supporting ones.

1. **The rebuilt argument's load-bearing premise is false, and falsified by the document's own new material.** §4's "what stays constant" claim is that Augustine's judgment on a rival consecration is "structurally the same one Cyprian applies to Novatian — a rival consecration outside the one episcopate is *null*." *On Baptism* I.1.2, in this world's own vendored `npnf104`, says the opposite in as many words: "he who is ordained, if he depart from the unity of the Church, does not lose the sacrament of conferring baptism" (H1). Everything downstream — the World Separation finding, the strand-singular finding that "applies rather than re-derives" it, and §5's Article 3 answer — rests on that sentence. This is the stranded-sentence pattern in its purest form: the fix to §5 (correcting how *On Baptism* is characterized) left the newly-written §4 asserting the thing §5's correction disproves.

2. **Round 1's H3 gap is relocated rather than closed.** §4 does now engage the coercion candidate directly, which Round 1 asked for. But it engages *only* that candidate, and the document's own new evidence surfaces a stronger one it never tests: Cyprian's "no one of us sets himself up as a bishop of bishops... [no bishop] can be judged by another" against Augustine's "the Councils held in the several districts must yield... to the authority of plenary Councils... and even of the plenary Councils, the earlier are often corrected by those which follow." Both texts are in this world's own vendored corpus; Augustine's is in the very treatise §5 relies on. That is a change in the *ground* of authority, not the instrument — Article 21's third criterion, exactly (H2).

3. **Round 1's H8 circularity is relocated, not removed.** "Mode of pastoral life" has been replaced by "primary gravity," and the replacement is honest about the concession. But the distinguishing gravity is asserted, not derived: it contradicts the document's own concession about Cyprian's baptismal rigor, it is not the gravity §3 names, and it is an axis on which the document's own evidence shows the two anchor figures *differing* — which is prima facie strand-plural evidence under Article 21 (H3).

4. **The World #6 discharge now rests on true evidence but a criterion that proves too much, and its central citation is misplaced** — *episcopatus unus est* is *De Unitate* 5 (c. 251, Novatian/Felicissimus context), not Cyprian against Stephen; the actual anti-Stephen text sits vendored in the same volume, uncited (H4).

**No standing escalation category is triggered by this review.** §8/§9's escalation assessment is materially improved and the false Round 1 claim is gone; but it runs only two of CO-022 category 4's three limbs and does not disclose a real contradiction with Donatism's own Step 0 (M9).

---

## Method — what was actually checked

Nothing was taken on either the document's or Round 1's word. Re-derived from source in this session:

- **Governing text, re-extracted from `.docx`:** `L1-Foundation/CiC_L1_Constitution_V2_2.docx` (Articles 3, 4, 15, 20, 21, 22, 23, 29 read in full); `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` (Part I criterion sets, Part III Gravity Discovery, the Step 1 entry); `L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` (Layer 1–3 definitions, Section 4 Step 1 entry); `L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx` Part Four (Temporal Horizon, Depth Calibration).
- **The live `cic-build-cycle` skill** (CO-022 and CO-024b), extracted from the `.skill` archives — the four escalation categories read verbatim.
- **The vendored primary corpus, read directly, not from memory:** `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` — *On Baptism* I.1.2 (ordination in schism), II.3 (councils corrected by plenary councils; Cyprian's 256 preface quoted by Augustine), III.2 and VI (**both quotations in §5 located to their actual books** — one of them is not where the document says it is), Ep. 185's Nebuchadnezzar/kings-enact-laws argument. `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` — *De Unitate* 5 ("The episcopate is one, each part of which is held by each one for the whole"), the Council of Carthage 256 preface ("bishop of bishops"), and Epistle LXVII (= Oxford Ep. lxvii, a.d. 257) in full context.
- **This world's own Step 0** in full, all eight §4 carry-forwards traced individually against the revision.
- **`World-Builds/Imperial-Juridical-Christianity/Doc_01_...md`** §4 (Strands A/B/C), §6, §8; **IJC Step 0 §4 item 3**; **`World-Builds/Hieronymian-Ascetic-Literary/hal_Doc_01_...md`** §3.3, §4, §8.1.
- **Donatism's sibling-branch Step 0**, read via `git show origin/claude/record-native-world-build-v2-e2s0dt:...` — §2 A5, §3 B3, §4 item 4.
- **`cic/corpus-map/latin-pastoral-congregational-christianity.yaml`** — the Ep. 185 row (`confidence: assigned`, confirmed) and the Council of Carthage 419 row.
- **`Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_2.md`** — checkpoint M2 confirmed at source.

---

## Round 1 disposition — what was actually fixed

**Genuinely fixed, verified at source (23):**

- **H1 (Article 15).** Now quoted verbatim — "historically developing ecclesial realities shaped, to the degree the evidence attests, through instability, adaptation, and incomplete continuity" — with "quoted exactly" stated and the timeframe reading marked as this document's own gloss. Clean.
- **H2 (*De Baptismo*).** Substantively fixed and improved. The "argues *with* Cyprian, disputing his ruling while claiming his communion" formulation is right, and the Donatist-citation-as-proximate-occasion point is correctly carried into §6's table. (Citation defect at M2; consequential collateral damage at H1 below.)
- **H4(i) (reading divergence).** Actually resolved, with a stated grammatical argument and an on-record finding. Discharges Step 0 §4 item 2(e).
- **H4(ii) (primary-gravity-first).** The work is now performed here (§3, §4, §5) rather than reassigned; §8 item 7 no longer restates the assignee as Doc_04. (Discipline breach at M7.)
- **H5 (false escalation claim).** Deleted. §9 no longer says the divergence "was already identified and escalated at Step 0." Correct — Step 0's only escalation was the IJC Confessions breach.
- **H7 (hal discharge).** Rebuilt honestly and well. Ep. 67's quotation is verbatim against ANF05 ("have the power either of choosing worthy priests, or of rejecting unworthy ones"), the Felicissimus counterexample is named as the hard case it is, hal's own authority-mode terms are used verbatim, and the asymmetry is restated as office-and-procedure vs. charisma-and-patronage. This is the best fix in the revision.
- **H9 (missing criterion sets).** All six World Separation questions are now run under their own heading, in the Framework's own words and order; both missing Temporal Scope questions are answered at §2. (Qualified at M4, M6.)
- **M1** (ordination relocated to Carthage) — gone; Hippo/Valerius/391 correct, the preaching-licence detail accurate. **M2** (419 council) — now "codified the African church's own canon law in the context of the Apiarius appeal to Rome," and the jurisdictional complication is flagged rather than smoothed. **M3** (Hippo province) — hedge replaced by the civil/ecclesiastical split (sourcing issue at L1). **M4** (Felicissimus timing) — now "opening during Cyprian's own absence... condemned at the council he convened after his return." **M5** (hal characterization) — hal's terms verbatim, bipolarity and Marcella's pre-Jerome formation named. **M6** (subject inversion) — corrected; "this world 'is not yet built and cannot itself hold the line from its side'" now attaches to the right party. **M7** (uncredited reuse) — credited to IJC Doc_01 §6 and given a shared-inheritance gloss. **M8** ("G4") — replaced by checkpoint M2, verified in the process document, with the Article 29 / build-documents chain stated correctly. **M9** (IJC simultaneity) — the divergence is named, and IJC's "genuinely simultaneous" gloss is verbatim. **M11** (self-contradicting sentence) — deleted. **M12** (internal/external axes) — glossed at first collision.
- **L1, L3, L4, L6, L7, L9** — all applied as instructed and verified.
- **C3** (ungrammatical IJC sentence) — rewritten.

**Fixed in form, defective in substance (3):** H3 → see H2 below. H6 → see H4 below. H8 → see H3 below.

**Not fixed (4):**

- **L8.** §9 still says the "temporal/geographic boundaries... were already settled at the portfolio level and at Step 0; this document applies and... discharges them, rather than redeciding them" — while §2 sets c. 246 on a specific new argument and CF V7.4's own Step 0 entry says "Nothing in Step 0 performs Step 1's own boundary-determination work." Carried below as L2.
- **C1.** §2 still reads "Tertullian's own **forged** theological vocabulary" — the adjective still reads as counterfeit.
- **C2.** §6 and §7 both now credit "Tertullian's own **generation**"; the Step 0 Conclusion credits Tertullian himself, and this world's Step 0 §2 A2 was corrected in review on precisely this attribution. The drift has spread from one place to two.
- **M10 residue.** The formation-pathway claim was correctly moved out of the Article 21 test — but its pointer was not: §2 now cites "(§5 below)" for a claim §5 no longer contains, and the actual intervals Round 1 asked for (Cyprian ~2–3 years; Augustine ~9–10) are still unstated. Carried at L7.

---

## What was checked and found clean

Recorded because this project's reviews document both sides.

- **Every quotation from a governing document is now exact where it is presented as exact.** Article 15 (verified), Article 21's "a finding, never a presupposed universal schema" / "accountable to evidence" / "never assigned to satisfy an architectural preference for plurality" (verified), Article 29's freeze-eligibility gate and "the method of confirmation... governed by the build documents" (verified; trivial ellipsis noted at C4), hal Doc_01 §8.1's authority-mode formula and "drove him from Rome within months with no institutional recourse" (both verbatim), IJC Doc_01 §4's "genuinely simultaneous" (verbatim), Step 0 §3 B2's "*plausibly* the richest..." (verbatim), Cyprian Ep. 67 (verbatim against ANF05), Donatism Step 0's "a persecuted 'Church of the Martyrs' facing a state-favored rival" (verbatim against the sibling branch).
- **The six World Separation questions are the Framework's own six**, in its own order and wording. The Distinct World Criteria are its own four. The Forces Framework Step 1 entry asks four questions and all four are answered substantively.
- **Historical facts re-checked and clean:** Cyprian's conversion c. 246 and election between roughly July 248 and April 249 over five presbyters' opposition; the *libelli* system; the Felicissimus schism's placement during the absence and its condemnation at the 251 council; Novatian's rival consecration in the same months; the plague c. 249–262 and *De Mortalitate* c. 252–253; the 255–256 rebaptism councils; martyrdom 258; the Diocletianic persecution's active African phase c. 303–305 against the longer legal state to 311/313; Augustine's nine Manichaean years, 386 conversion, 391 presbyterate at Hippo under Valerius with the preaching licence contrary to African custom, 395/396 episcopate, consecration by the primate of Numidia, Numidian provincial councils; 410 and *City of God*; the Vandal crossing 429 and the siege; death 28 August 430; the 258→391 interval as 133 years; 279 Donatist against 286 Catholic bishops at the 411 Conference of Carthage; Donatism as the majority church across large parts of Numidia.
- **Ep. 185 is `confidence: assigned` in this world's corpus-map**, as §4 states, and does argue from Luke 14:23 — both confirmed at source.
- **CO-022 failure-mode checks:** (a) nothing is attributed to "the project lead" or "Mark" anywhere; (b) the revision log's account of what changed is, section by section, an accurate description of what actually changed — no fix is described as landed that did not land; (d) canonical folder correct; status line honest ("DRAFT... pending Round 2", Frozen not claimed, Living Tradition Status PENDING).
- **The self-correcting prose in §5** ("corrected here from an error in this document's own earlier draft") is real, not performative, and is the right way to carry a correction that a downstream reader needs to see.

---

# HIGH

### H1 — §4's "what stays constant" premise is false, and is falsified by *On Baptism* — the same treatise §5 relies on, in this world's own vendored corpus

**Where.** §4, "Has authority changed substantially?", second paragraph — the pivot of the whole section:

> *"the theological **judgment** Augustine applies to the Donatists is structurally the same one Cyprian applies to Novatian a century earlier — **a rival consecration outside the one episcopate is null**, not a legitimate parallel jurisdiction to be out-ranked or negotiated with."*

**What's wrong.** Augustine's central anti-Donatist position is precisely that a rival consecration is *not* null. *On Baptism* I.1.2, in `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` (read this session):

> *"For the sacrament of baptism is what the person possesses who is baptized; and the sacrament of conferring baptism is what he possesses who is ordained. And as the baptized person, if he depart from the unity of the Church, does not thereby lose the sacrament of baptism, so also **he who is ordained, if he depart from the unity of the Church, does not lose the sacrament of conferring baptism**. For neither sacrament may be wronged."*

That is the whole architecture of Augustine's answer to Donatism: the sacrament is Christ's and remains real outside unity; what is lost is its profit, not its reality. It is why the African church received Donatist clergy *in their orders* rather than re-ordaining them — a practice the African canon collection the 419 council promulgated addresses directly, and which §2 already gestures at. Cyprian held the opposite: no baptism and no ordination outside the church, hence rebaptism. The two judgments are not "structurally the same"; they are the two sides of the exact dispute *On Baptism* exists to settle.

The clause "not a legitimate parallel jurisdiction to be **negotiated with**" fails on the same evidence: the 411 Conference of Carthage was a formally convened, state-supervised negotiation between two episcopates, at which the Catholic side offered terms for shared or alternating sees to converting Donatist bishops.

**Why it matters.** Three ways, ascending.

1. **The document already knows the fact that falsifies it.** §5, forty lines later, says: *"Augustine argues at length that Cyprian's specific ruling — that baptism outside the unity of the church must be repeated — was **not** binding and was **wrong**."* A treatise cannot hold that Cyprian's ruling was wrong *and* apply "structurally the same" judgment. This is the stranded-sentence failure the build has logged five times at Step 0 and once already at Doc_01: the corrected sentence and the sentence it strands are in adjacent sections of the same revision.
2. **It is load-bearing all the way down.** §4's conclusion ("none of them... indicates a transition to a different world") rests on it; §5's strand bullet says explicitly *"That finding is not re-derived here; it is applied"*; §5's Article 3 answer then builds on the strand finding. One false premise propagates through all three of the document's hardest claims.
3. **The true fact is more useful.** Augustine's position — the rival's orders are *valid but unfruitful outside unity* — is a genuinely different theology of office from Cyprian's, and naming it honestly is what the World Separation question is for. It does not by itself force a strand-plural finding; it forces the argument to be made on the right axis (see H2).

**Fix.** Delete the "null" claim outright. If a continuity claim is wanted here, the defensible one is narrower and checkable: both bishops treat a rival consecration as *outside the one communion and therefore without lawful standing in it*, while differing — substantially and on the record — about whether it is sacramentally void. State the difference; do not assert its absence.

---

### H2 — The strand-plural candidate the revision's own new evidence surfaces is never tested; Round 1's H3 gap is relocated, not closed

**Where.** §4's finding that only "the external political capacity" changed while "the *ground* of episcopal authority — ordination, territorial responsibility for one see's own flock, **collegial standing among fellow African bishops answerable to one another in council**, no jurisdiction claimed over other sees — is unchanged across the shift"; applied, not re-derived, at §5's Authority-structure bullet.

**What's wrong.** Two of this world's own vendored texts, one of them the treatise §5 builds on, state the two phases' positions on that exact ground — and they are opposed.

**Cyprian**, opening the Council of Carthage of September 256 (ANF05, and quoted *by Augustine* inside *On Baptism* II.3):

> *"judging no man, nor rejecting any one from the right of communion, if he should think differently from us. For neither does any of us set himself up as **a bishop of bishops**, nor by tyrannical terror does any compel his colleague to the necessity of obedience; since every bishop, according to the allowance of his liberty and power, has his own proper right of judgment, and **can no more be judged by another than he himself can judge another**. But let us all wait for the judgment of our Lord Jesus Christ."*

**Augustine**, *On Baptism* II.3 (`npnf104`, read this session):

> *"all the letters of bishops... are liable to be refuted... by the weightier authority and more learned experience of other bishops, **by the authority of Councils**; and further, that the Councils themselves, which are held in the several districts and provinces, **must yield, beyond all possibility of doubt, to the authority of plenary Councils** which are formed for the whole Christian world; and that even of the plenary Councils, **the earlier are often corrected by those which follow them**."*

Cyprian's ground: each bishop is answerable to Christ alone and to no colleague; a council records opinions and binds no one. Augustine's ground: a bishop is corrigible by conciliar authority, and conciliar authority is itself hierarchically ordered. That is a change in **authority structure** in Article 21's own sense — and it is *not* the "external instrument" the section engaged. The document's own phrase "answerable to one another in council," offered as the unchanging ground, is the specific proposition Cyprian's most famous statement of collegiality denies.

**Why it matters.** Round 1's H3 asked for the strongest strand-plural candidate to be engaged. The revision engages the candidate *Round 1 named* — the coercion axis — and adopts, nearly verbatim, the resolution Round 1 sketched for it ("the ground... is unchanged; what changes is the external instrument available to it... argued in pastoral-corrective terms"). Round 1's instruction was that the argument "has to be made, **against the actual sources**." It was not: the sources were not re-read, and when they are, the same section's own new material (the *De Baptismo* quotations imported into §5) contains the counter-evidence. The gap has moved from "the candidate was not named" to "a candidate was named, resolved on a premise the document's own sources contradict, and the stronger candidate went unnoticed."

Note also the shape of the argument: §4 engages one candidate, finds it not disqualifying, and concludes categorically that "none of them, singly or together, indicates a transition." A one-candidate test does not license an all-candidates conclusion.

**Fix.** Run the conciliar-authority candidate explicitly, quoting both texts. A defensible strand-singular finding may still be available — the parties, sees, ordination, territorial charge and pastoral function are unchanged, and what changes is the *appellate* structure above the individual bishop, which arguably belongs to the wider church's development rather than to this world's own formation ecology. But that has to be argued, and if the evidence supports two strands, Article 21 is a finding in both directions. Either way, delete "answerable to one another in council" from the list of constants; it is the one item on that list Cyprian expressly rejects.

---

### H3 — The Donatism distinction still does the work by assertion; "primary gravity" is not derived, and the axis chosen is one on which the document's own evidence has the two anchor figures differing

**Where.** §5, "Corrected finding":

> *"that shared recurrence is exactly why the two are separate worlds distinguished by their own primary gravities rather than by a legitimacy verdict... Donatism's own defining gravity is the rigorist maintenance of a purity boundary against a state-favored rival... **This world's own defining gravity**, on the preliminary reading at §3 and §4 above, **is closer to the opposite: a readiness to readmit the compromised and to remain in communion with those one disagrees with**... That is an ecology-grounded distinction... **not circular**."*

**What's wrong.** The concession is genuinely better than Round 1's version, and the acknowledgment that both communions practised the same pastoral mode is correct and creditable. But the replacement distinguisher is asserted at three separate points where it needed to be derived.

1. **It is not the gravity §3 names.** §3's preliminary list is *pastoral office as flock-keeping*, *penitential discipline and the reintegration of the failed*, and *preaching and catechesis*. "Readiness to readmit the compromised **and to remain in communion with those one disagrees with**" is a different, composite formulation whose second half appears nowhere in §3. §6 is careful to call the same resonance a candidate "if it holds under Doc_04's six tests." §5 promotes it to "this world's own **defining** gravity" and then leans the Article 3 answer on it. The document's hardest constitutional claim rests on a gravity determination the document elsewhere twice says has not been made.
2. **It is contradicted by the document's own concession, two paragraphs earlier.** §5 concedes that "on the narrow question of baptismal rigor specifically, Cyprian's own historical position sits closer to the Donatist position than to Augustine's." Cyprian *did* police a purity boundary at the sacramental frontier — that is what rebaptizing every convert from schism is — and Cyprian's own council of 256 exists to enforce it. The distinguishing gravity therefore holds cleanly for Augustine's phase and not for Cyprian's. The paragraph concedes the Donatist claim on Cyprian and then, five sentences later, states a world-defining gravity that only Augustine's half supports. That is the same structural move Round 1's H8 identified, performed with a new noun.
3. **The neighbour's half is asserted about a world that has not determined it.** Donatism has a Step 0 and no Doc_01 or Doc_04; it has no gravity finding. The phrase quoted — "a persecuted 'Church of the Martyrs' facing a state-favored rival" — is, at source (Donatism Step 0 §2 A5), an instruction about how *Doc_02* must reconstruct the Catholic opposition from inside, i.e. a self-understanding statement, not a gravity determination. Under the discipline hal's own Doc_01 was corrected for breaching, and which this document correctly applies to World #9 four sections later, the neighbour's own construction governs how the neighbour is characterized.

**And the consequence the document does not notice.** If the two anchor figures genuinely diverge on the axis nominated as this world's *defining* gravity — Cyprian policing a sacramental purity boundary, Augustine refusing to — that is direct evidence under Article 21's "formation emphasis" and "ecological orientation" criteria, on the world's own most central axis. §5 finds strand-singular and then, in its own next argument, supplies a divergence it never carries back to the strand test.

**Fix.** Either (a) narrow the distinguisher to something both anchor figures actually share and Donatism actually does not — the most promising candidate on this document's own evidence is *refusal to break communion over disagreement*, which is what Augustine praises Cyprian for and is genuinely absent on the Donatist side, but it must be stated as that and not as a general anti-purity orientation Cyprian does not hold; or (b) state plainly that the Article 3 coherence question cannot be closed at Step 1 because it depends on a gravity determination Doc_04 has not made, and carry it forward as an open item. Route (b) is honest and available; route (a) requires the Cyprian half to be argued, not conceded and then set aside. In either case, drop the claim about World #4's own defining gravity and cite Donatism's Step 0 §3 B3 for what it actually says (see M9).

---

### H4 — The World #6 discharge holds a true fact with a misplaced citation and a criterion that would place Cyprian *inside* IJC

**Where.** §7, World #6 bullet: *"against Stephen's claim to Petrine authority over other sees, **Cyprian holds that episcopatus unus est**... the direct opposite of IJC's own Strand A (Roman apostolic-primacy) claim, not a variant of it. **Augustine's own church, on the same anti-primacy model... inherits and holds the same position.** This world's own bishops contest and refuse primacy claims from the inside of the same profession IJC's own actors make them from; that is the boundary."*

Round 1's H6 is genuinely fixed — the false correspondence claim is gone, the Stephen dispute is named openly, and Step 0 §3 B1's embedded-letters note is quoted accurately. What replaces it does not hold up.

**(a) The citation is misplaced.** *Episcopatus unus est* is *De Unitate Ecclesiae* 5 — in ANF05, "The episcopate is one, each part of which is held by each one for the whole" — written c. 251 against Novatian and Felicissimus, four to five years *before* the Stephen controversy. It is not Cyprian's answer to Stephen. The text that is his answer to Stephen sits in the same vendored file, unused: the preface to the Council of Carthage of 256, *"neither does any of us set himself up as a bishop of bishops, nor by tyrannical terror does any compel his colleague to the necessity of obedience"* — which the ANF editor's own note glosses as "a rebuke to the assumption of Stephen." A discharge of a built world's reciprocal obligation should cite the text that actually does the work, particularly when it is vendored to this world.

**(b) The criterion proves too much.** "Contests and refuses primacy claims from inside the same profession" is not a world boundary — it is a description of a position *within* a debate. IJC's own Doc_01 §4 settles this: Strand A (Petrine primacy), Strand B (imperial-proximity primacy) and Strand C (Ambrosian sacramental independence, which is expressly "not a claim about which see outranks which") are three *opposed* positions on the ground of episcopal authority, and IJC treats them as three strands of **one** world. On the criterion §7 states, Cyprian's anti-primacy position is a fourth position in that same debate — i.e. an argument for putting him inside IJC, not outside it.

The boundary that actually works is available and is nearly stated elsewhere in the document: the primacy question is *episodic* in this world's corpus (two years of Cyprian's ten-year episcopate; the Apiarius affair at the edge of Augustine's) and *constitutive* in IJC's, whose entire strand structure is built from it. Distinctness is a matter of what organizes the ecology, not of which side of a shared dispute a figure took.

**(c) The Augustine half is not established and is contradicted in-document.** "Augustine's own church... inherits and holds the same position" is asserted without evidence, and §5's own quotation from *On Baptism* VI has Augustine settling an African question by the authority of "the whole Church, confirmed and strengthened by the authority of a plenary Council" — a supra-episcopal authority claim Cyprian's 256 preface explicitly refuses. The 419 Apiarius council, which §2 names, supports African resistance to Roman *appellate* jurisdiction and is the right evidence for a narrower claim; it does not support "the same position."

**Fix.** Cite the 256 council preface for the anti-Stephen position and reserve *De Unitate* 5 for what it is. Restate the boundary as centrality-of-organizing-force rather than position-in-a-shared-dispute. Narrow the Augustine claim to what the African record supports (resistance to Roman appellate jurisdiction, evidenced at 419) and drop "the same position."

---

# MEDIUM

### M1 — Inserting the new §4 broke at least twelve cross-references, and the document is now internally mis-navigable

Round 1's H9 fix added a new §4 (World Separation Criteria) and pushed every later section down one. §9's revision log uses the new numbering correctly; §§2–6 largely do not. Verified instances:

| Location | Says | Actually is |
|---|---|---|
| §2, Carthage bullet ("returned to at §6 below") | §6 | §7 (World #6 bullet) |
| §2, Diocletianic bullet ("documentary gap, §4 below") | §4 | §5 |
| §2, Donatist bullet ("Forces-Framework sense (§5 below)") | §5 | §6 |
| §2, Donatist bullet ("Article 23 reconstruction sense (§6 below)") | §6 | §7 |
| §2, Catalysts ("[documentary gap, §4 below]") | §4 | §5 |
| §2, beginning point ("(§5 below)") | §5 | **nothing** — see L7 |
| §3, gravities bullet ("see §4 and §6 below") | §6 | §7 |
| §4, new-gravity bullet ("§5's own preliminary forces observation") | §5 | §6 |
| §4, authority bullet ("Stephen of Rome's own claim over Cyprian, §6 below") | §6 | §7 |
| §5, reading divergence ("carrying it in the Forces sketch at §5") | §5 | §6 |
| §5, reading divergence ("not a category-4 escalation (§8 below)") | §8 | §9 |
| §6, generation ("vocabulary this world inherits (§6 below)") | §6 | §7 (self-reference) |
| §6, table ("noted for orientation, §6 below") | §6 | §7 (self-reference) |

This is squarely CO-022's *Naming and term propagation* rule ("a fix that lands in the narrative document without the index being updated to match is not a complete fix"), and it is the same stranded-neighbour pattern Step 0 logged five times. Individually cosmetic; collectively a navigation failure in a document whose whole argument runs by cross-reference — §2's reader is sent to Strand Determination for the Forces sense and to World Separation Criteria for the documentary gap, neither of which is there.

**Fix.** Re-walk every `§n` pointer against the current numbering in one pass.

---

### M2 — The *De Baptismo* Book citation in §5 is wrong, and it is wrong because it was taken from Round 1's review rather than from the text

**Where.** §5: *"Cyprian and his colleagues did not act 'by the authority of any plenary or regionary Council' that could bind the whole church **(Book II)**."*

**What's wrong.** Located in the vendored `npnf104` this session: the passage — "not indeed by the authority of any plenary or **even** regionary Council, but by a mere epistolary correspondence... a custom which had no sanction from the ancient custom of the Church" — occurs exactly once in the volume, inside `<div3 ... shorttitle="Book III">`, at Chapter 2, §2. It is **Book III**, not Book II. (The companion quotation *is* correctly placed: "afterwards brought to light... by the authority of a plenary Council" is in Book VI, verified by offset against the same div structure.) The quotation also silently drops "even" from inside the quotation marks.

**Why it matters.** Round 1's H2 gave the same passage as "Book II." The revision imported the attribution rather than checking it — which is precisely the failure CO-022's *Review* section exists to catch, and precisely what H2 above shows happened to Round 1's suggested *argument* as well. A reviewer's citation is a claim, not a source.

**Fix.** "(Book III)", restore "even", and re-verify the Book VI locus in the same pass (it is correct as written).

---

### M3 — "Framed throughout in pastoral-corrective terms" over-reads Ep. 185, and the omitted half of its argument is World #6's own register

**Where.** §4: *"Augustine's own argument for coercion is framed **throughout** in pastoral-corrective terms (bringing a wayward member of the one family back), continuous with the logic Cyprian applies to the lapsed."* This is the sentence that keeps the illegal-to-established change classified as instrument-only.

**What's wrong.** Ep. 185 argues on two registers, not one. The pastoral-corrective register is real. But in the same treatise, read this session in `npnf104`: whoever "despises the laws of the emperors which are enacted in behalf of truth, wins for himself great condemnation"; the Old Testament kings "who did not prohibit nor annul the ordinances which were issued contrary to God's commands are all of them censured"; Nebuchadnezzar, "converted by a miracle from God, enacted a pious and praiseworthy law on behalf of the truth"; and the summary of Augustine's own position in the NPNF apparatus — "we do recognize **the State as the servant of the Church**." That is an argument from the Christian ruler's own religious duty to legislate — a claim about the relation of ecclesiastical to imperial authority, which is World #6's defining subject matter, and which the corpus-map registers by double-placing Ep. 185 with `imperial-juridical-christianity`.

**Why it matters.** "Throughout" is doing the load-bearing work: if the coercion argument is purely pastoral, the change is instrument-only; if it also runs on the emperor's duty to serve God by law, then a second, non-pastoral ground of episcopal action has appeared inside this world's own corpus, and the World Separation question has a second live limb. The document raises the honesty bar correctly by naming Ep. 185 at all; it then reads only half of it.

**Fix.** Drop "throughout". Name both registers, and say why the imperial-duty register does not (or does) bear on the world-separation finding — with the double placement in the corpus-map named as the corroborating signal it is.

---

### M4 — §4 concludes a six-question test on which it expressly declined to answer two questions, and routes Step 1 work to Doc_04

**Where.** §4's first bullet ends "**Not resolved here.**"; its second ends "A real question for Doc_04, **not assumed settled by this document either way**." The section's Conclusion then states: *"none of them, singly or together, indicates a transition to a different world under this test's own six questions."*

**What's wrong.** Two of the six questions — "Has a new gravity emerged?" and "Has a major gravity disappeared?" — are answered "possibly / not resolved / Doc_04's." A conclusion covering "this test's own six questions" cannot be reached from four of them. And CF V7.4 places World Separation Criteria in **Part I, Step 1**; Doc_04 is Step 4 and its own Part III discipline is candidate generation from the Source Ecology, which does not exist yet. Round 1's H4 penalized exactly this move — deferring Step 1's assigned work downstream — and it recurs here in the section written to answer that finding.

**Fix.** Either answer both questions on the evidence now available (both are answerable at a preliminary level, as the bullets themselves nearly do), or mark the Conclusion explicitly as provisional on the two unresolved limbs. Do not do the first thing in the bullets and the second in the conclusion.

---

### M5 — Doc_01 instructs Doc_04 not to "re-derive from zero," which is the opposite of what CF Part III requires of Gravity Discovery

**Where.** §3: *"this document establishes the primary characterization on this world's own ecological terms first, per Step 0 §4 item 8, **which Doc_04 then formally tests rather than re-derives**."* §5: *"Doc_04 confirms or revises this document's preliminary reading; **it does not re-derive it from zero**."* §8 item 7: *"not re-derived from zero, not skipped either."*

**What's wrong.** CF V7.4 Part III, Candidate Gravity Generation: *"Before candidates are tested, they must be generated from traceable evidence rather than general impression. Candidates should be drawn from elements that recur across multiple Source Ecology evidence streams... **A candidate list produced without traceable reference to specific recurring evidence — for example, a list generated from general familiarity with a world rather than from the Source Ecology itself — should not be treated as Gravity Discovery output, regardless of how plausible the candidates appear.**"*

A Step 1 characterization is, by construction, produced before any Source Ecology exists. Binding Doc_04 to test that list rather than generate its own from Doc_02 is an instruction to do the thing Part III names as disqualifying. Step 0 §4 item 8 asks Doc_01 to establish the characterization *first* — it does not ask Doc_01 to constrain Doc_04's candidate generation.

**Fix.** Keep the characterization; drop the constraint. "Doc_04 generates its candidates from Doc_02's Source Ecology per CF Part III and should say explicitly whether this document's preliminary characterization survives that independent derivation."

---

### M6 — §2 grounds a Step 1 boundary decision in RCF Part Four, which derives its own rule *from* Doc_01, and which Article 3 forbids reaching upward

**Where.** §2, ending point: *"the Representative construction discipline this project follows (**RCF Part Four**) grounds a world's outer temporal edge in its own anchor figures' documented lives, not an arbitrary round date."*

**What's wrong.** RCF V3.2 Part Four, Temporal Horizon, read this session: *"Every Representative speaks from within the world's own temporal horizon — its full historical span, **as the world's own boundaries establish it (Doc_01)**... determined during construction from **the world's own outer edges** — where **its** documented life begins and ends."* The rule runs from Doc_01 to the Representative, not back; and it speaks of the *world's* documented life, not its anchor figures' — the same Part Four opens by insisting the Representative is "not one bounded person's biography."

Constitution Article 3: *"The Representative is the highest world-specific output and influences nothing above it... Causation runs downward through this hierarchy only; no derivative structure shapes what stands above it."* Citing Representative methodology as the warrant for a Step 1 boundary is upward causation, in the one Article the document elsewhere leans on hardest.

**Why it matters.** The ending point does not need this ground: reason (2) — the ecological-rupture symmetry between Decius and the Vandals — is a genuine Step 1 argument and carries the bullet on its own.

**Fix.** Delete ground (1)'s RCF citation, or restate it as this document's own reasoning without attributing the rule to a downstream framework.

---

### M7 — Step 0 §4 item 8 is claimed as discharged while §5 derives this world's "defining gravity" precisely from the need to distinguish it from World #4

**Where.** §8 item 7 (*"This document performs the primary-gravity-first, ecology-grounded characterization Step 0 assigned to Doc_01"*) against §5's derivation of the defining gravity inside the Donatism-distinction argument.

**What's wrong.** Step 0 §4 item 8's text: *"Doc_01's own gravity-orientation work should establish Cyprian's and Augustine's primary characterization **on this world's own ecological terms first**, and treat **neighbor-distinctiveness (from World #4 in particular) as a tiebreak only where genuinely needed**."* Step 0 records why the rule exists: the original World #8/#9 split used neighbour-protection as an unstated tiebreaker instead of reasoning to Cyprian's own characterization first.

§5's "defining gravity" is not reached from this world's ecology and then found to distinguish; it is reached *inside* the paragraph whose purpose is to distinguish this world from Donatism, and it is defined by opposition to Donatism ("closer to the opposite"). The one place in the document where a world-defining gravity is actually named is the place where neighbour-distinctiveness is doing the deriving — the specific error the rule was written to prevent, on the specific pairing that produced it.

**Fix.** State the primary characterization at §3, from this world's own ecology, in the form §5 needs; then let §5 *apply* it to the World #4 comparison rather than derive it there. If the characterization cannot be stated without the Donatism contrast, that is itself the finding.

---

### M8 — The Augustine–Jerome double-placement disclosure has been deleted rather than corrected, leaving CF's shared-material question unanswered on the World #9 boundary

**Where.** §7's World #9 bullet, and Round 1's L2.

**What's wrong.** Round 1 found the *pointer* to the 17-letter Augustine–Jerome correspondence miscited (Step 0 §4 item 2 instead of item 5) while confirming the substance as verified in the YAML. The revision fixed it by removing the sentence. "Jerome" now appears in exactly one place in the document, and the correspondence appears nowhere.

That removes the only concrete piece of shared material on this boundary — deliberately double-placed `tradition` in both worlds' corpus-maps, "the largest single thing in this volume after the Confessions," with hal's corpus-map carrying the mirror row plus *City of God* XVIII.42–44. CF V7.4 Part I, World Continuity & Distinction, is explicit that *"Adjacent worlds may share material... Boundary management requires attention to both differentiation and continuity."* Step 0 §3 B3 surfaced this specifically as a **correction to an earlier Step 0 draft** that had wrongly claimed Jerome does not appear in this world's corpus-map. It is now uncarried in Doc_01 and absent from §8's forward items.

**Fix.** Restore one sentence, with the corrected pointer (Step 0 §3 B3 / §4 item 5): name the double placement, say why it is deliberate rather than a boundary breach, and carry the Doc_02 consequence.

---

### M9 — §9's escalation assessment runs two of category 4's three limbs, and does not disclose a real divergence from Donatism's own Step 0 boundary statement

**Where.** §9: *"...which is a reconciliation matter for whenever the branches merge, **not two reviews disagreeing with each other and not a contradiction between two already-cleared master documents** — it does not meet CO-022's fourth category on the record as it now stands."*

**Two problems.**

1. **The third limb is not run.** CO-022's fourth category, verbatim from the live skill: *"two reviews disagreeing with each other, a contradiction between two already-cleared master documents, **or a finding that cuts against an earlier decision**."* §9 addresses limbs one and two and stops. Round 1's H5 specifically named the second and third limbs as the ones with a claim. The limb Round 1 flagged is the limb the revision omits. Whether it is met is arguable in both directions — but it has to be argued, not skipped.
2. **A larger divergence is undisclosed.** Donatism's Step 0 §3 B3, read at source this session, states its World #8 boundary as: *"This world's own primary gravity — a rigorist rival communion's claim to be the one pure church... — is a different axis from **World #8's ordinary episcopal pastoral care**, not a variant of it,"* and §4 item 4 binds that statement to Donatism's own Doc_01. §5 of this document finds that "ordinary episcopal pastoral care" **does not distinguish the two worlds at all** and expressly replaces it. Two same-day, unmerged confirmations now hold incompatible accounts of what the World #4/#8 boundary rests on, each binding its own Doc_01. That is a materially bigger divergence than the parenthetical-scope one §9 does disclose, and it is not mentioned anywhere in the document.

**Fix.** Run limb three explicitly and reach a stated conclusion. Disclose the boundary-basis divergence with Donatism Step 0 §3 B3 quoted, in §7's World #4 bullet and §9 both. If the two are judged reconcilable, say how; if not, that is the category-4 assessment the section owes.

---

### M10 — Article 21 is credited with an "iterative-revision discipline" it does not contain, and which sits against what it does say

**Where.** §2: *"If Doc_04's later, formal gravity testing finds otherwise, that finding supersedes this one, **per Article 21's own iterative-revision discipline**."*

**What's wrong.** Article 21, read in full: *"Whether a world contains distinct internal strands is a construction finding that, **once made, governs all subsequent strand attribution**."* CF V7.4's Strand Determination entry: *"This determination is made at Step 1 and **governs all subsequent work**."* Neither text contains an iterative-revision discipline; both state the opposite direction of authority, from Step 1 forward.

This is the same class as Round 1's H1 — a governing document credited with content it does not carry — in softer form (an attributed doctrine rather than a fabricated quotation), and it is used to license a downstream override in the same document that elsewhere (M5) tells Doc_04 not to re-derive. The two instructions to Doc_04 point in opposite directions.

**Fix.** Drop the attribution. If a revisability caveat is wanted, hal's own Doc_01 §4 models a defensible one — a finding held "provisionally... must be reopened, not defended past the evidence" — stated as this document's own discipline, not as Article 21's.

---

# LOW

**L1 — Hippo's civil province is now asserted without a source, on a point that is not uncontested.** §2 replaces Round 1's criticized hedge with the flat claim "Civilly, Hippo sat in the province of Africa Proconsularis." The ecclesiastical half (Numidia; consecration by the primate of Numidia; Numidian councils) is secure and well attested. The civil half is a scholarly reconstruction that not all authorities share — Hippo Regius is routinely described simply as a Numidian city, and the point turns on where the late-imperial Proconsularis/Numidia boundary ran near the coast. The claim came into the document from Round 1's fix text and carries no citation. Hedge it or source it; do not state a contested provincial assignment flatly in a boundaries section.

**L2 — Round 1's L8 is unfixed.** §9 still describes the temporal boundaries as "already settled at the portfolio level and at Step 0," while §2 determines the beginning point on a fresh argument and CF's own Step 0 entry states "Nothing in Step 0 performs Step 1's own boundary-determination work." The added sentence about §4–§5 being "new construction work proper to Step 1" covers the two new sections but not §2.

**L3 — Augustine's own documented change of mind on coercion is omitted from the section whose question is whether authority changed inside the world's span.** Augustine states plainly (Ep. 93 to Vincentius) that his original view was against coercion and that he was changed by the results. That is first-person evidence of a shift in what a bishop of this world thought his office could licitly do, occurring *inside* Augustine's own episcopate — directly relevant to the World Separation question, and more interesting than a static account.

**L4 — RCF's "natural quiet" is applied to a temporal stretch, not a thin domain.** §5 directs Doc_05/the Representative to hold the 258–391 gap "the way RCF Part Four requires: as natural quiet." RCF's rule is about *domains where the ecology is thin* — "a matter it did not dwell on, argue over, or return to" — while the same Part Four says the Representative "draws on anything within its world's own history — early, middle, or late." A 133-year stretch inside the world's own declared span, containing events §2 lists among this world's own Historical Pressures, is not a thin domain. The instruction may still be right in effect; the authority cited does not reach it.

**L5 — §1 asserts the unhedged distinctiveness claim and then says it keeps the hedge.** "No other confirmed world... reconstructs ordinary congregational and lay formation... as richly as this one; Step 0 §3 B2 calls it '*plausibly* the richest...', a hedge this document keeps rather than sharpens." The hedge is quoted but the assertion preceding it is unhedged. Restate the claim in the hedged form, then the disclosure lands.

**L6 — *De Unitate* is used as the anti-primacy proof text without naming its two-recension problem.** The treatise survives in two recensions of chapter 4, one of which (the *Textus Receptus* "Primacy Text") reads as a support for Roman primacy; the ANF apparatus in this world's own vendored file glosses the neighbouring passage "i.e., the universal episcopate is the chair of Peter." A document holding a boundary against World #6 on this treatise's ecclesiology should name the textual question rather than let a reader discover it in the same file.

**L7 — Round 1's M10 is half-applied.** The formation-pathway claim was correctly removed from the Article 21 test and moved to §2, where it is now load-bearing for the c. 246 beginning point — but its "(§5 below)" pointer dangles (M1), the actual intervals Round 1 asked for are still unstated, and "rising to episcopal office by popular election... a pathway Augustine's own formation will independently, if differently, recapitulate" glosses over the fact that popular acclamation produced Augustine's *presbyterate*, while his episcopate came by Valerius's designation and Megalius's consecration. "If differently" is carrying more weight than one hedge can.

**L8 — the reading-divergence resolution rests on grammar alone.** §5 resolves it "on the sentence's own grammar," which is a real argument, but does not engage the other side's reasoning at all — Donatism's Step 0 §3 B3 attaches the parenthetical to both figures and gives its own account of why. Step 0 §4 item 2(e) asked for the divergence to be resolved "explicitly, not inherit[ing] either side's reading by default"; adopting this world's own Step 0's reading with one added argument is close to the line. One paragraph engaging the world-level reading on its merits would put it clearly over.

**L9 — the six-cell sketch places a force in the Internal column whose proximate cause it names as external.** The Ongoing/Internal cell reads "Augustine's own explicit engagement with Cyprian's conciliar acts, **prompted by the Donatists' own citation of them**" — a correct and honest addition (it is H2's fix from Round 1), but a force whose trigger is a rival communion's polemic is not straightforwardly internal. Either split it or note the placement judgment.

---

# COSMETIC

**C1 — Round 1's C1 unfixed.** §2 still reads "Tertullian's own **forged** theological vocabulary"; as an adjective this reads as counterfeit. §7's construction ("the Latin theological vocabulary Tertullian's own generation forged") is the intended sense.

**C2 — Round 1's C2 unfixed, and now duplicated.** §6 and §7 both credit "Tertullian's own **generation**"; the Step 0 Conclusion credits Tertullian himself ("credited with forging much of the Latin theological vocabulary the whole Western tradition depends on"), and this world's Step 0 §2 A2 was corrected in review on this exact attribution. One drift has become two.

**C3 — §7 contains an unparseable clause.** *"a bishop who loses his own congregation's confidence is deposed, or schisms against, through a process bishops answer to each other for"* — "or schisms against" has no grammatical anchor.

**C4 — §1's Article 29 ellipsis replaces a verb.** *"the method of confirmation... governed by the build documents"*; the Article reads "The method of confirmation **is** governed by the build documents." Harmless, but an ellipsis inside a constitutional quotation should elide content, not grammar.

**C5 — "any plenary or regionary Council" drops "even" from inside quotation marks** (§5); the text reads "any plenary or **even** regionary Council." (Same sentence as M2.)

**C6 — §9's revision log cites a "Cell 2B" the document no longer labels.** The §6 table carries no cell identifiers, unlike IJC's Doc_01, which labels Cells 3A/3B. Either restore the labels or name the cell by its row and column.

---

## Required actions before Round 3

**Must fix (HIGH):** H1 (delete the "rival consecration is null" premise and restate the actual continuity, checking every sentence downstream that applies it — §4's conclusion, §5's Authority-structure bullet, §5's Article 3 paragraph); H2 (run the conciliar-authority strand candidate against both vendored texts, and delete "answerable to one another in council" from the constants); H3 (derive the distinguishing gravity or carry Article 3 forward as open; drop the claim about World #4's own defining gravity); H4 (recite the 256 council preface for the anti-Stephen position, restate the World #6 criterion as centrality rather than position, narrow the Augustine half).

**Must fix (MEDIUM):** all ten. M1 and M2 are mechanical. M3, M4, M5, M6, M10 are corrections to instructions or attributions that will otherwise propagate into Doc_02 and Doc_04. M7, M8, M9 are discipline and disclosure.

**Apply directly:** all LOW and COSMETIC. C1 and C2 are second-round misses — they were listed as "apply directly" at Round 1 and were not applied.

**Three process observations for the revision pass, not findings:**

1. **The revision imported this review series' own suggested reasoning instead of deriving it.** Round 1's H3 fix sketched an argument ("the ground of episcopal authority... is unchanged; what changes is the external instrument... argued in pastoral-corrective terms") and required it to be made "against the actual sources." The revision adopted the sketch nearly verbatim and did not go to the sources — which is how both the false "null" premise (H1) and the un-run conciliar candidate (H2) survived, and how Round 1's own miscitation of *De Baptismo* Book II (M2) was inherited. A reviewer's suggested fix is a hypothesis, not a finding. This is worth naming in the revision log, because the same pattern will otherwise recur at Doc_02.

2. **The stranded-sentence pattern remains the dominant defect mode in this build, and it is now operating at section scale, not sentence scale.** H1 is a correction in §5 stranding a paragraph in §4. M1 is a section insertion stranding twelve pointers. M8 is a deletion stranding an obligation. The Step 0 record logs five consecutive rounds of the same thing. A mechanical pass — for each edit, list the sentences that depend on it, and check each — is cheaper than another round.

3. **The document's honesty is genuinely improving and should not be traded away in the next pass.** §5's two in-text self-corrections and §4's refusal to minimize the coercion evidence are the right instincts. H1–H3 are not failures of candour; they are failures of verification. The fix is to check the sources, not to hedge the prose.

**Escalation check performed by this review.** Category 1 (Representative identity): not touched. Category 2 (portfolio-level/cross-world): §5's characterization of World #4's own defining gravity is a cross-world claim about an unbuilt world and should either be removed or labelled as portfolio-level — see H3(3). Category 3 (governance/methodology): not created by this document; §8 item 9's referral of the World Separation Criteria / Layer-1 gaps to a coach pass is correctly scoped and this review endorses it. Category 4 (unresolved tensions): the Donatism boundary-basis divergence found at M9 has a real claim on the third limb and must be assessed rather than omitted; this review does not itself escalate — it returns the question to the build thread with the record corrected.
