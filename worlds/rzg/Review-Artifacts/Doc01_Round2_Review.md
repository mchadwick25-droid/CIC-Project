# Doc_01 Round 2 — Independent Adversarial Review: The Reformed Cities — Zurich & Geneva

**Document under review:** `World-Builds/Reformed-Zurich-and-Geneva/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, Revision 2, 2026-09-15)
**Prior round:** `World-Builds/Reformed-Zurich-and-Geneva/Review-Artifacts/Doc01_Round1_Review.md` — SUBSTANTIAL REVISION REQUIRED, 6 high / 13 medium / 13 low
**Review date:** 2026-09-15
**Reviewer:** independent adversarial review, run in isolation per `cic-build-cycle`. No drafting context seen. Scope per `CLAUDE.md`'s Round-2+ discipline: a targeted recheck of the 32 Round 1 findings plus a hunt for defects Revision 2 itself introduces — not a re-review from scratch.

**Re-verification method.** Every Round 1 finding was re-checked against the same primary source Round 1 used, not against Revision 2's own account of what it fixed, and not against Round 1's summary of what the source said. Where Revision 2 states a corrected fact with new specificity, that new statement was treated as a new claim requiring its own verification.

**Sources re-opened directly for this round:**

- `reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` — Articles 20, 21, 22, 23, 29, extracted from `word/document.xml`
- `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — Part I in full
- `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Blueprint_V7.3.docx` — §17 (new citation in Revision 2, not checked in Round 1)
- `reference/L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — Step 1 entry and Section 5 (not checked in Round 1)
- `cic-website/data/world-census.json` — VI.2, VI.9, VI.26, read as parsed JSON, field by field, with quotations diffed programmatically
- `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml` — all nine work rows
- `World-Builds/Reformed-Zurich-and-Geneva/Step0_Movement_Scope_Confirmation.md`; `World-Builds/Lutheran-Wittenberg/Step0_Movement_Scope_Confirmation.md`
- `world-build-docs/_cross-world/dossiers/the-reformed-cities-zurich-and-geneva_Source_Readiness_Dossier.md`
- `records/`, `records/worlds/`, `records/WORLDS_REGISTRY_LOG.md`, `packages/`
- `World-Builds/Donatism/Doc_01...md` and `don_Decision_Log.md`; `World-Builds/Imperial-Juridical-Christianity/` (folder contents and launch record)
- The two new supporting files: `Open_Gaps_Tracking.md`, `rzg_Decision_Log.md`
- `CLAUDE.md`; the `cic-build-cycle` skill
- Historical verification against standard Reformation scholarship for every newly-specified fact

---

## Verdict

**SUBSTANTIAL REVISION REQUIRED.**

**3 high, 9 medium, 11 low — all new.** Of the original 32: **20 fixed, 9 partially fixed, 1 not fixed, 2 fixed-but-on-a-false-premise.**

**Revision 2 is a real revision, not a wording pass, and the two re-arguments it claims are genuinely attempted.** H2 (Dort) is substantially fixed and the fix is honest: I re-read VI.9 and VI.26 myself and diffed the quotations character by character, and Revision 2 now represents the census accurately — the VI.26 `why` quotation is character-exact *and* complete, the truncation Round 1 caught is gone, and the document does not quietly re-resolve the question anywhere else in its own text. H4 is fixed outright: the new §4 exists, sits before Strand Determination, and runs the Framework's six named sub-questions, which I confirmed verbatim against V7.4 Part I. H6 is fixed and genuinely threaded through §1 and §5. M10 is fixed against a citation (Blueprint V7.3 §17) that I verified exists and says exactly what Revision 2 says it says — three criteria, including project-lead confirmation with a date. M2, M3, M5, M6, M7, M8, M12 and M13 are all correct now on the merits. That is real work.

The revision fails for three reasons, and only three:

1. **A quotation is attributed to a named file that does not contain it** (H1). In the course of *correcting* a citation error, §7 asserts that Lutheran Wittenberg's Step 0 "does call Trent its own 'direct doctrinal rival.'" That phrase does not occur anywhere in that document. This is the project's most-recorded failure class, appearing inside fix text written to close a finding about exactly this.

2. **The new §4 contradicts §5 on the same evidence** (H2). §4 clears the single-world premise partly by finding that formation differs "in mechanism rather than in what formation is for" and "not in underlying logic." §5, three paragraphs later, establishes the strand finding partly on "genuinely different formation logics." Same two instruments, same evidence, opposite characterization, the same word. And the strongest separation datum Round 1 named — two independent origins — is never weighed in §4 at all, while still standing in §6.

3. **The disposition reasoning misapplies `cic-build-cycle`'s own escalation rule** (H3). The Decision Log holds the Dort item PENDING "regardless of Round 2's outcome on everything else, the same pattern Living Tradition Status already uses." Living Tradition Status is not an escalation category; a portfolio-level decision is. The skill says a live category stops disposition of the document, not of one item in it. Donatism's own Doc_01 — the precedent cited — carries LTS as PENDING *and* concludes "No escalation category applies." The analogy inverts the rule it cites.

The medium findings share one shape, and it is the shape this project has already written down for itself. Donatism's `don_Decision_Log.md` records it as a "standing process note": *"when a fix adds new explanatory content (not just a numeric or wording correction), check that content against every document it touches for both accuracy and overclaiming."* Six of the nine mediums below are new content introduced by a Round 1 fix — a precedent claim about `don`'s registration that the repo contradicts, a corrected fact folded silently into a quotation from a source that says something else, a date correction that over-corrects into a new error, and a new supporting file that restates the very error it was written to record as fixed.

---

## High-severity findings

### H1. §7 attributes a quotation to Lutheran Wittenberg's Step 0 that does not appear in it — inside the fix text for L9

**Revision 2, §7, Tridentine bullet:**

> "...distinct from Lutheran Wittenberg's own Step 0, **which does call Trent its own 'direct doctrinal rival'** — a phrase belonging to that document, not repeated here as this world's own finding."

**What that document actually says.** `World-Builds/Lutheran-Wittenberg/Step0_Movement_Scope_Confirmation.md` §2 A3(3), verbatim:

> "**The Tridentine Church (VI.22, same batch)** — the direct doctrinal **target of, and respondent to,** this movement; Doc_02 for both worlds should expect to cite each other as the primary named rival."

The phrase "direct doctrinal rival" occurs nowhere in that file. I grepped the entire `World-Builds/` tree: it appears in exactly four places — this world's own Step 0 (which asserts the attribution), Round 1's review (which repeats the assertion as a description of this world's Step 0), Revision 2, and the new Decision Log. It never appears in the document all four attribute it to.

**Why this is High and not Low.** Round 1's L9 said only that this world's Step 0 *attributes* the phrase to Wittenberg's Step 0 — a true statement about this world's Step 0, and Round 1 did not itself claim to have found the phrase in Wittenberg's file. Revision 2 goes further: it asserts affirmatively, in its own voice, that Wittenberg's Step 0 "does call" Trent that, and puts the words in quotation marks. That is a new claim, and it is false. `CLAUDE.md`: "Every quote must be re-verified verbatim against the vendored source file before a record passes review. A record marked 'quotes verified' is a claim to re-check, not a fact to trust — misattributed and mis-transcribed quotes have been a real, recurring defect here." The failure is aggravated by where it sits: in a sentence whose entire purpose is to correct a mis-attribution, in a revision whose masthead says all 32 findings are addressed.

**What the correct handling is.** Either drop the second half of the sentence, or state what is actually true and checkable: this world's own Step 0 §3 B3 attributes the phrase "direct doctrinal rival" to Lutheran Wittenberg's Step 0; Wittenberg's Step 0 in fact says Trent is "the direct doctrinal target of, and respondent to, this movement." That is a second, previously-unrecorded defect in this world's Step 0, and it belongs in `Open_Gaps_Tracking.md` as such.

### H2. The new §4 and §5 give contradictory characterizations of the same formation evidence, and §4 never weighs the strongest separation datum

The section exists, is correctly placed, and runs the right six questions — H4 of Round 1 is genuinely closed (see the table). The problem is what the section does with the evidence once it has it.

**(a) A direct contradiction between §4 and §5, in the same vocabulary.**

§4, "Has formation changed substantially?":

> "Real variation in instrument — the Prophezei's public scholarly exposition against the Genevan Catechism's fixed instruction backed by Consistory discipline — but **not in underlying logic**: both are scripture-centered, communal, and civically embedded formation programs, **differing in mechanism rather than in what formation is for**."

§5, Strand Determination, limb 3:

> "**Formation emphasis.** Zurich's own formation instrument was the Prophezei; Geneva's was the fixed Genevan Catechism paired with the Consistory's own direct, individualized moral oversight — **genuinely different formation logics**."

These are the same two instruments, adduced from the same evidence base, characterized in flatly opposite terms four paragraphs apart, using the same noun. §4 needs "not different logics" to reach one world; §5 needs "genuinely different logics" to reach two strands. The document does not notice, reconcile, or disclose the tension. §5's sentence is inherited unchanged from Revision 1; §4's is new. This is precisely the failure the `cic-build-cycle` naming-and-propagation rule exists to catch — "a fix that lands in the narrative document without the index being updated to match is not a complete fix" — applied within one document.

Note that Article 21's four dimensions and the Framework's six separation questions genuinely are different tests, so it is *possible* for the same evidence to clear one and not the other. But that is an argument the document has to make explicitly, and it is exactly the argument Round 1's H3 said had to be made. Asserting "not in underlying logic" in one section and "genuinely different formation logics" in the next is not that argument; it is the absence of it.

**(b) The worship-convergence evidence is used in §4 and withheld from §5.**

§4's worship answer does real, honest work, and it is the best new reasoning in the revision:

> "This difference did not remain permanent on the Zurich side: by most accounts, congregational psalm-singing was adopted across the Swiss Reformed churches generally, including Zurich, within this world's own window — a convergence, not confirmed here against a vendored primary source, flagged at Dominant Modern Reconstruction confidence."

That is correct (Zurich reintroduced congregational psalm-singing in 1598, inside the 1519–1650 window), properly hedged, and it materially weakens the separation case. But §5 then deploys the *same* worship divergence as the lead limb of the strand finding with no mention of the convergence at all — "Geneva's worship, by direct contrast, built congregational singing into the center of its own devotional life." Evidence that cuts one way is disclosed where it helps the single-world finding and omitted where it would weaken the two-strand finding. The convergence belongs in both sections or neither.

**(c) The authority answer substitutes an out-of-scope convergence for an in-scope one.**

> "Has authority changed substantially? Real variation... but **the wider Reformed world's own later convergence** toward a Geneva-influenced consistorial/presbyterian pattern (in the French, Scottish, and Dutch Reformed churches this world transmits to) suggests Geneva's model became the general Reformed pattern rather than a permanently rival one."

The convergence named is convergence of *third parties* toward Geneva. Zurich is not among them, and §4 does not claim it is. Zurich's church remained council-governed through this world's entire window — which is, on the document's own §5 account, the whole point of the Zurich/Geneva authority contrast. So the honest answer to the question as asked is that authority did diverge substantially between the two cities and did not converge within the window. §4 concedes "real variation" and then answers a different question. The worship answer shows the document knows how to do this properly; the authority answer does not do it.

**(d) Two independent origins — Round 1's strongest separation datum — is never put to the test.**

Round 1's H3 rested most heavily on two things: "two independent local triggers, not one shared cause" and "a negotiated agreement between two already-distinct parties." The second phrase has been removed from §5 by rewording. The first is still in the document, twice — §6's "two independent local triggers, not one shared cause" and Cell 1B's "two independent origins, not one" — and §4 never mentions it. The Framework's list is explicitly non-exhaustive ("Questions include:"), so separate origin was available to be weighed and was not. Running the six named questions while leaving the strongest counter-evidence outside the frame is a narrower test than the one Round 1 asked for, and the unweighed datum now sits two sections downstream of a finding it bears on.

**What the correct handling is.** Reconcile §4 and §5 explicitly — say in terms why the same divergence clears Article 21's dimension test without clearing the separation test, or change one of the two characterizations. Carry the worship-convergence finding into §5. Answer the authority question about Zurich and Geneva rather than about their descendants, and if the honest answer is "diverged and did not converge," say so and let the finding rest on the other five. Weigh the two-independent-origins evidence inside §4. If, once all of that is on the page, the finding comes out genuinely ambiguous, that is Round 1's own instruction and `cic-build-cycle`'s fourth category — escalate, do not choose the framing that keeps the world intact.

**Credit where it is due.** §4's closing disclosure — "if a reviewer reads the worship/authority evidence as more decisive than this document does, that disagreement should be named rather than absorbed silently" — is the right instinct and the right practice, and this review takes it up rather than treating it as a formality. The finding above is that named disagreement.

### H3. The disposition reasoning misapplies `cic-build-cycle`'s escalation rule, on a precedent that says the opposite

**Revision 2, `rzg_Decision_Log.md`, Doc_01 entry:**

> "The document does not claim readiness for 'Approved to proceed' while the Dort escalation remains open — **that item stays PENDING regardless of Round 2's outcome on everything else, the same pattern Living Tradition Status already uses.**"

And Doc_01's own masthead: "**One item is escalated, not self-disposed** (§7's Dort portfolio-boundary question) — **the rest of this document is otherwise ready** for Round 2 review."

**What the skill actually says:**

> "Before disposing of any document, check it against these four categories. **If any apply, stop and escalate directly to the project lead — do not self-dispose,** regardless of how clean the review came back."
> "A document only becomes eligible for disposition when it has cleared an independent review without that review calling for substantial revision, **and none of the four escalation categories applies.**"

The unit the rule operates on is the document, not the finding. A live Category-2 item does not carve itself out and leave the remainder disposable; it blocks disposition of Doc_01 until the project lead rules. The Decision Log's "regardless of Round 2's outcome on everything else" formulation describes a document proceeding around a standing escalation, which is the thing the category exists to prevent.

**The cited precedent is the reverse of the claim.** Living Tradition Status is a constitutional freeze-eligibility gate under Article 29 — it is not one of the four escalation categories, which is exactly why it can sit PENDING without blocking anything. Donatism's Doc_01 §1 carries "**Status: PENDING**" for LTS, and its §8 Disposition concludes in terms: "**No escalation category applies.**" That world's Doc_01 could self-dispose *because* nothing in the four categories was live, not because a live category had been isolated into a PENDING item. The analogy Revision 2 draws licenses the opposite of what the precedent shows.

**What the correct handling is.** Say plainly that Doc_01 is not eligible for self-disposition at all while the Dort escalation stands, that it is escalated to the project lead as a whole, and that it waits. Round 2's own outcome does not change this — under the skill, a document with a live Category-2 item waits on the project lead whether the review comes back CLEARED or not. (This does not prevent Round 2 review from running, which is the right next step regardless; it prevents disposition after it.)

**Two smaller defects in the same assessment, recorded here rather than separately.** §9's fourth bullet resolves the Step 0 sequencing question into "a disclosed, authorized exception rather than an unresolved tension" on the strength of the masthead's out-of-document authorization (see M1 below), then hedges: "If that reading is wrong, that itself is the kind of tension this category exists to catch." A category assessment that names the condition under which its own conclusion fails, and then adopts the conclusion anyway, has not made the assessment. And §9's closing — "All findings from `Review-Artifacts/Doc01_Round1_Review.md` are addressed above" — is a self-certification of the kind `CLAUDE.md` names directly ("A blocking review finding can't be dismissed by self-certification — it needs independent re-confirmation"), and it is not accurate: L6 is untouched, and nine findings are partial (table below).

---

## Medium-severity findings

### M1. The Step 0 "authorized exception" rests on an out-of-repo instruction described as a verifiable record — and the corroborating claim is contradicted by this document's own §7

Revision 2 discloses the Step 0 sequencing problem properly in four places (masthead, §9, `Open_Gaps_Tracking.md` item 1, Decision Log), which is a real improvement over Revision 1's silence. The disclosure is honest about the facts. The **authorization** is not established.

**Masthead:**

> "This build thread opened anyway, under **this thread's own 2026-09-15 launch instruction**, which named that exact unreviewed status directly and explicitly directed proceeding... **That instruction is this exception's own verifiable record;** it is not this document's own self-certification."

Nothing in the repository records that instruction. It is not quoted, not filed, not dated to a document, and a reader cannot check it. `cic-build-cycle`: "**Nothing is attributed to 'the project lead' anywhere in any document — a quote, a decision, an instruction — without a verifiable record that the project lead actually said or wrote it.** Hold this to the same bar as Frozen: a real, checkable record, not a claim." Calling an unrecorded instruction "this exception's own verifiable record" does not make it one; it is the claim the rule distinguishes from a record.

**This project has a working precedent for exactly this and did not follow it.** `World-Builds/Imperial-Juridical-Christianity/CiC_Imperial_Juridical_Christianity_World_Build_Thread_Launch_2026-07-19.md` is that world's launch prompt, committed to its build folder, readable, and citable by path. That is what a verifiable launch record looks like in this repo.

**The supporting claim is also unsupported, and this document contradicts it.** The masthead cites "the pattern the sibling Lutheran Wittenberg build thread was launched under the same day." `World-Builds/Lutheran-Wittenberg/` contains exactly one file — its Step 0. No Wittenberg build thread has produced any build output, and Revision 2's own §7 says so: "no Lutheran Wittenberg Doc_01 yet exists in this repository (only its own Step 0 draft is present)." An unverifiable authority claim is being propped up by a second unverifiable claim that the same document elsewhere undercuts.

**One further point on the authority cited.** `CLAUDE.md`'s "Scaling the build" launch pattern is quoted accurately — "self-govern per its own rules" is real — but that same sentence ends "**stop only for an escalation category or a missing input.**" A Step 0 that states in its own terms that it has not been reviewed and that no build thread should open on it is a strong candidate for "a missing input." The pattern is cited as authorizing the exception when its own stop-condition is at least as easily read as forbidding it.

**What the correct handling is.** File the launch instruction in this world's build folder as IJC did, and cite it by path; or, if it cannot be filed, drop the word "verifiable," drop the Wittenberg corroboration, and treat the sequencing problem as what §9's own hedge says it might be — an unresolved tension for the project lead, escalated alongside Dort.

### M2. §6 claims an exemption from Article 23 and cites Article 23 for it — the correct authority exists and is not cited

**Revision 2, §6**, immediately after quoting Article 22's full text including the Writing-From-Inside sentence:

> "The sketch below is preliminary, Layer-1-only orientation for Step 2's scope, and — **per Article 23's own instruction quoted above** — is understood to be written at **the external, orienting register this preliminary step requires**, not the inhabited voice Doc_08's own eventual compilation and the Representative's own future speech must use."

The sentence quoted above is Article 22's, and it instructs the opposite: forces "are documented from within the world's own formation logic — as the world experienced and understood them — **never as an external analytic overlay imposed on it,** consistent with the Writing-From-Inside Principle (Article 23)." The document restores the sentence Round 1 caught it dropping, and then cites that restored sentence as licensing the register it forbids.

**The substance is defensible; the authority is wrong and available.** `CiC_L3A_Forces_Framework_V1.1.docx`, Section 5, verbatim: "**Modern analytical categories are appropriate at Layer 1, where the historical event is documented using scholarly vocabulary.** They must not govern Layer 2, where the world's own consciousness is the subject." Since §6's table is explicitly labelled "Layer 1 only — Historical Event," the external register really is permitted — by the Forces Framework, which Revision 2 does not cite here. This is the same defect class as Round 1's M10 (a provision attributed to the Constitution that lives in the Blueprint), recurring in a revision that fixed M10.

### M3. The `rzg` registration fix rests on a precedent claim the repository contradicts, and cites a path that does not exist

**Masthead:**

> "Not yet entered in `records/worlds.yaml` or `WORLDS_REGISTRY_LOG.md` — **per Donatism's own precedent (`don` likewise is not yet in either), that registration happens at compile stage, not Doc_01.**"

Both halves fail.

1. **`records/worlds.yaml` does not exist.** The registry is a directory, `records/worlds/`, holding one file per world code: `alx.yaml`, `cappadocian.yaml`, `desert.yaml`, `don.yaml`, `fix.yaml`, `gallic.yaml`, `hal.yaml`, `ijc.yaml`, `pahc.yaml`, `syr.yaml`. (`WORLDS_REGISTRY_LOG.md`'s own header still refers to a single `worlds.yaml`, which is where the stale path comes from — but the split has happened, and the file cited is not on disk. Round 1's L11 used the same stale path; Revision 2 inherited it rather than checking.)
2. **`don` is registered.** `records/worlds/don.yaml` exists — 2,384 bytes, `world_id: donatism`, full doorway text. So the precedent claim "`don` likewise is not yet in either" is false on the registry-data half, and the inference built on it — that registration happens at compile stage rather than at Doc_01 — has no support. (`don` *is* absent from `WORLDS_REGISTRY_LOG.md`, which has no `## don` section; that half is correct.)

Round 1's L11 asked only where the code is to be registered. Revision 2 answered by asserting a precedent it did not check. This is a governance-provenance claim stated as settled.

### M4. The Dentière correction is folded silently into a sentence attributing it to the census

**Revision 2, §8 item 9:**

> "The census's own `"voices"` field names Theodore Beza and Marie Dentière (**a former prioress of an Augustinian house at Tournai**, turned Genevan reformer, who published in her own name arguing women could speak about scripture) as this world's own figures..."

The census `voices` field, read as parsed JSON, says: "Marie Dentière — **former abbess** turned Genevan reformer, who published in her own name arguing that women could speak about Scripture."

The historical correction is right — Round 1 made it, and she was prioress of an Augustinian house at Tournai. But it is inserted inside a parenthetical presented as what the census names, replacing the census's actual word without a marker. A reader checking the census will not find "prioress of an Augustinian house at Tournai" there. `cic-build-cycle`'s cross-document fact-consistency rule asks for exactly the opposite handling: "carry the exact wording across, **or state plainly why the wording differs.**" Elsewhere in the same revision the document does this properly — §7 discloses that it is correcting the dossier and Step 0 rather than silently substituting. Here it does not.

### M5. `Open_Gaps_Tracking.md` item 8 restates the Anabaptist error the revision was correcting, and disagrees with Doc_01

Doc_01 §7 states the sequence correctly: "performed by **Conrad Grebel, baptizing Georg Blaurock, who then baptized the others present, including Manz**."

`Open_Gaps_Tracking.md` item 8, written in the same commit:

> "the first Swiss Brethren baptisms (21 January 1525) were **performed by Conrad Grebel and Georg Blaurock**, **both** formerly of Zwingli's own Zurich circle, at Felix Manz's house."

This is the same error shape Round 1's M5 caught in Revision 1 ("performed by Conrad Grebel and Felix Manz") — two names conjoined as joint administrants, the sequence that was the whole content of the correction dropped — with one name swapped. It also contradicts Doc_01 on the count ("both" vs. Doc_01's "all three"). The file created to record that a finding was fixed re-states the finding.

### M6. "All three formerly members of Zwingli's own reform circle" overclaims for Blaurock

Doc_01 §2 and §7 both say Grebel, Blaurock and Manz were "all three formerly members of Zwingli's own reform circle."

Grebel and Manz were — that is the substance of the correction and it is right. Georg Blaurock (Jörg vom Haus Jakob) was a former priest from Chur who came to Zurich in 1524–25 already moving in radical circles; he is not, on the standard accounts, described as a member of Zwingli's own humanist reform circle. Revision 1 named only Grebel and Manz, both of whom genuinely were; the fix that added Blaurock extended the circle claim to him without checking it. I flag this at Dominant Modern Reconstruction confidence, not certainty — but it is a claim asserted flat, in a document that now has the confidence vocabulary available, and it does load-bearing work in the sentence that establishes the schism as internal to this world.

### M7. §2's Geographic Centers bullet now dates Geneva's break from Savoy and the Prince-Bishop to 1526 — wrong, and contradicted three times in the same document

**Revision 2, §2, Geneva bullet:**

> "Geneva's own **break from the Prince-Bishop of Geneva and the Duchy of Savoy, and its *combourgeoisie* alliance with Bern and Fribourg, dates from 1526** — a decade before Calvin's own arrival, not the same year."

The *combourgeoisie* with Bern and Fribourg does date from 1526 — that part is Round 1's L1 correctly applied. The break from the Prince-Bishop and Savoy does not: the bishop left Geneva in 1533, and Savoyard authority was ended in 1536 with Bernese military intervention. Round 1's L1 said this plainly ("1536 is Bern's military intervention and Vaud campaign, and Geneva's reformation vote of 21 May"); the fix swept the break into 1526 along with the alliance.

The document gets it right everywhere else, which makes it an internal contradiction as well as an error: §2 Historical Pressures ("the 1526 alliance with Bern and Fribourg, **the 1536 break from Savoy and the Prince-Bishop**"), §2 Historical Catalysts ("Geneva's 1526 alliance with Bern **and 1536 break from Savoy**"), and §6 ("Geneva's 1526 alliance with Bern **and 1536 political break from Savoy and the Prince-Bishop**"). Only the Geographic Centers bullet — the one Round 1 named — carries the new error.

### M8. The Dort escalation offers three named options without the trade-offs the escalation format requires

Round 1's prescribed handling: "escalate the scope question to the project lead as a portfolio-level decision, **presented as named options with trade-offs**." `cic-build-cycle`'s grounded-options format: "named alternatives, **an explicit trade-off for each**, a recommendation, and a dedicated decision artifact."

§7 gives three clearly-drawn options and a recommendation, which is most of the way there. What it does not give is a trade-off for any of them — no statement of what option 1 costs this world's Doc_02, what option 2 obliges VI.26's future build to honour, or what option 3 leaves unresolved and for how long. The project lead is asked to choose between three descriptions, not three consequences. The evidence that would populate the trade-offs is already in §7 (the Beza throughline, the two delegations, VI.9's own unsettled status); it simply is not attached to the options.

### M9. `rzg_Decision_Log.md` enumerates twelve of the thirteen Low findings while asserting thirteen — and the one it drops is the one Revision 2 did not fix

The Decision Log's Doc_01 entry closes: "Thirteen low findings (a compressed Bern-alliance date; 'Second Battle of Kappel'...; spelling inconsistency...; an unhedged Ursinus/Olevianus joint-authorship claim; missing path citations; unmarked verbatim borrowing...; a mis-located Step 0 citation; an overstated Trent...attribution...; an uncommented TULIP-vocabulary anachronism...; the `rzg` code not yet registered...; no `Open_Gaps_Tracking.md`...; and an imprecise 'daily' characterization of the Prophezei)."

That parenthetical lists twelve items. The missing one is Round 1's L6 — "§7 item 6 cites '(from PR #229)'. A PR number is not a checkable in-repo citation." L6 is also the single Round 1 finding Revision 2 leaves entirely untouched: `(from PR #229)` is still in §8 item 6. The log's record of what the review found silently omits the one item the revision did not address, which is the specific way a decision log stops being an audit trail. Under `cic-build-cycle`'s coach-verification standard — "that the Decision Log matches what's actually on disk" — this fails.

---

## Low-severity findings

**L1.** The VI.9 `relationsSummary` quotation in §7 is not character-exact. Diffed programmatically: the census's hyphen in "its own tradition **-** a real Step 0 call" is silently upgraded to an em dash, and the curly apostrophe in "Remonstrants**’** own entry" is changed to a straight one. Substance unaffected; but the VI.26 quotations in the same bullet list *are* exact, and Revision 2 makes quotation fidelity a stated point of this fix ("quoted in full this time rather than truncated").

**L2.** §7: "**Both entries** were added at the same 2026-08-02 Era 7 Freeze." The census records an addition date for VI.26 only ("Added at the Era 7 Freeze (Mark, 2026-08-02)"). VI.9's `statusWord` is "Researched — viable, secondary (Era 7 Step 0)" and its `statusDescription` says it was "**Reviewed** at the Era 7 Step 0 run and tiered," with the phrase "added at the same gate" grammatically modifying *the Remonstrant entry*, not VI.9. The argument §7 is making does not need this claim — what matters is that both entries leave the scope question open, which is verified and correct.

**L3.** §1 says Zwingli "held the office of *Antistes*"; §2 says his appointment was as *Leutpriester*. The *Antistes* title is conventionally associated with Bullinger's tenure, and §7 uses it correctly for Breitinger. The M11 fix extended it back to Zwingli without a hedge, in a document that now hedges the Grossmünster organ and the Heidelberg authorship.

**L4.** §4's finding paragraph: "the Framework's own six questions are **named as diagnostic together, not as a simple majority vote**." The Framework names no aggregation rule at all — Part I introduces them with "Questions include:" and stops. The reading is reasonable; attributing it to the Framework is not.

**L5.** §5: "Step 0 named this question directly (§2 A2)." Step 0 §2 A2 names the Zwingli/Bullinger/Calvin *continuity* question, not the strand question; and Step 0 §2 A5 says of Articles 20/21/23 that they are "not applicable in the developmental-tradition sense."

**L6.** §4's second answer — that the Second Helvetic Confession (1566) "affirms the same core commitments the Sixty-Seven Articles state in 1523" — is checkable against two texts this world has actually vendored (`schaff_second-helvetic-confession-heidelberg-catechism_1919.txt`, `zwingli_selected-works_jackson1901.txt` lines ~4485–4700). It is asserted without locus or verification, in a section whose sibling §8 item 8 makes a point of separating text-verified evidence from the rest.

**L7.** L8 of Round 1 is fixed by re-pointing rather than by correcting: §2's princely-patronage contrast now cites "this world's own §0/§3 B4." Step 0 §0 says the candidate is "genuinely different in origin, church order, and... internal structure"; §3 B4 names Reformed polity, predestination and Calvin's exegetical method. Neither mentions princely patronage, a territorial church, or Eucharistic theology — the three specifics §1 and §2 attach to the citation.

**L8.** L7 of Round 1 is half-fixed. The Trent borrowing is genuinely rewritten ("Doc_02 for both worlds should expect real mutual citation once Trent is vendored"). The Servetus line is still reproduced near-verbatim from Step 0 §2 A1 without quotation marks — now with an attribution ("per Step0 §2 A1") but still unmarked as quoted text.

**L9.** L5 of Round 1 is partly fixed: the dossier now carries its full path at §8 item 7, but §7's Anabaptist bullet and §8 item 2 still cite it pathless.

**L10.** §8 item 7 says the consistory registers are "not among the **seven works** vendored in PR #229." The corpus map carries **nine** work rows across seven source files. Minor, but it is a count restated from Revision 1 in a section otherwise rebuilt against the file.

**L11.** `Open_Gaps_Tracking.md`'s closing Doc_01 status block sits below the `---` and is unnumbered, while `CLAUDE.md` specifies "Entries are append-only and **numbered**." Sibling worlds' files were cited as the model; worth matching their handling of status blocks. Separately, the Decision Log records the Round 1 review as "model=Opus" — the review artifact itself records no model — and describes M11 as "episcopal vocabulary applied to **five** non-episcopal Reformed figures/institutions," conflating Round 1's three centers with its five men.

---

## Status of the 32 Round 1 findings

Re-verified independently against primary sources. **Fixed** means I checked the source myself and the defect is gone.

| # | Round 1 finding | Status | Note |
|---|---|---|---|
| H1 | Step 0 sequencing not named | **Partial** | Disclosed in 4 places ✓; authorization unverifiable — see M1 |
| H2 | Dort misrepresents census; needs escalation | **Fixed** | VI.26 quotes re-diffed: character-exact and complete ✓; escalated, PENDING, not re-resolved elsewhere ✓. Residuals: M8, L2, and the disposition rule at H3 |
| H3 | Strand evidence argues for two worlds | **Partial** | §4 added and honest in places; §4/§5 contradiction, asymmetric evidence use, origins unweighed — see H2 |
| H4 | World Separation Criteria missing | **Fixed** | §4 present, correctly placed, six sub-questions verified verbatim against V7.4 Part I ✓. Temporal Scope's two open questions now answered in §2 ✓ |
| H5 | Confidence calibration inverted | **Partial** | Vocabulary now used 3× — but only in §4/§5. §2, §6, §7 carry none; Round 1 asked for §2/§4/§5/§6. Prose hedges added in several spots ✓ |
| H6 | Bullinger mediation / never met dropped | **Fixed** | Stated plainly in §1 *and* §5, cited to Step0 §4 item 1; verified against Step 0 ✓ |
| M1a | "Quoted in full" false for Art. 22 | **Fixed** | Claim removed; both omitted sentences restored ✓. But see M2 |
| M1b | Art. 21 pointer false | **Fixed** | Article 21 now quoted at its point of use in §5; verified character-exact ✓ |
| M2 | Marburg/Calvin anachronism | **Fixed** | §6 states Calvin absent, ~20, law student, Geneva not yet reformed ✓; §1 reworded to "once developed on both sides" ✓ |
| M3 | Beza dating + Remonstrance target | **Fixed** | 1555, nine years before Calvin's 1564 death ✓; Gomarus/Junius at Leiden, Beza at one remove ✓ |
| M4 | Grossmünster organ date | **Fixed** | Now "mid-1520s," sources-vary hedge, Dominant Modern Reconstruction tag ✓ |
| M5 | First Anabaptist baptism misattributed | **Fixed** in Doc_01 | Sequence correct ✓; propagation to dossier §5 and Step0 §3 B3 both flagged ✓. But see M5/M6 above for the new file and the circle claim |
| M6 | Jesuit "no direct contact" borrowed | **Fixed** | Downgraded to "not assessed this pass" ✓; borrowing disclosed ✓; counter-evidence included ✓ |
| M7 | Corpus-map itemization overstated | **Fixed** | Re-read the yaml: one collective row confirmed; quote character-exact ✓ |
| M8 | Corpus-sharing misdescribed | **Fixed** | Verified against all nine rows — no Zwingli file shared ✓ |
| M9 | Article 4 clearance overstated | **Fixed** | (1)–(3) verified vs (4)–(5) not individually checked, matching Step0 §2 A1 ✓ |
| M10 | Art. 29 cited for a Blueprint provision | **Fixed** | Blueprint V7.3 §17 opened and verified: three criteria, incl. project-lead confirmation with a date ✓ |
| M11 | Episcopal "see" vocabulary | **Fixed** | §1 now makes the non-episcopal order explicit ✓. Minor: L3 |
| M12 | Unvendored pillars undisclosed | **Fixed** | Threaded through §3, §5, §8 item 8 and Open_Gaps item 4 ✓ — the best-executed fix in the revision |
| M13 | Dentière 1539 *Epistre* | **Fixed** on substance | Anonymous, printer prosecuted, 1561 signed preface named ✓; Article 20 scope corrected ✓. But see M4 |
| L1 | Bern alliance date | **Partial** | 1526 correct in 4 places; new error in the 5th — see M7 |
| L2 | "Second Battle of Kappel" | **Fixed** | "Battle of Kappel (fought during the Second War of Kappel)" ✓ |
| L3 | Zwingli forename | **Fixed** | "Ulrich (Huldrych)" ✓ |
| L4 | Ursinus/Olevianus unhedged | **Fixed** | Prose hedge added ✓ (no five-level tag, per H5) |
| L5 | Dossier path missing | **Partial** | Path given once; two citations still pathless — L9 |
| L6 | "(from PR #229)" | **Not fixed** | Still present in §8 item 6; also omitted from the Decision Log — M9 |
| L7 | Unmarked sibling borrowing | **Partial** | Trent line rewritten ✓; Servetus line attributed but unmarked — L8 |
| L8 | Mis-located Step 0 citation | **Partial** | Re-pointed, but the new locus does not carry the claim — L7 |
| L9 | Trent "direct doctrinal rival" | **Fixed → new defect** | This world's Step 0 now described correctly ✓, but the Wittenberg attribution is fabricated — H1 |
| L10 | TULIP anachronism | **Fixed** | Flagged in §6 rather than silently adopted ✓ |
| L11 | `rzg` unregistered | **Fixed → false premise** | Location now stated, on a precedent the repo contradicts — M3 |
| L12 | No `Open_Gaps_Tracking.md` | **Fixed** | File created ✓ (content defects at M5, L11) |
| L13 | Prophezei "daily" | **Fixed** | "meeting on most weekdays rather than daily" ✓ |

---

## The two new supporting files, checked against Round 1 and against Revision 2

**`Open_Gaps_Tracking.md`** — structurally correct and a genuine improvement: numbered, append-only, with a stated no-renumbering rule, and it carries the right ten gaps. Items 3, 4, 5, 9 and 10 were each checked against their underlying source (the dossier §1/§4, the corpus map, the census `sources` field, the Wittenberg folder, Blueprint §17) and are accurate. Item 2's account of the Dort correction matches both Round 1 and Revision 2 ✓. Defects: item 8 (M5 above); the unnumbered trailing status block (L11).

**`rzg_Decision_Log.md`** — the Round 1 summary is unusually thorough and, on the High and Medium findings, accurate: I checked its characterizations of H1–H6 and all thirteen Mediums against the review artifact and found no misstatement. Defects: the Low enumeration is twelve of thirteen and drops the one unfixed item (M9); the disposition reasoning misapplies the escalation rule (H3); "model=Opus" and "five figures/institutions" are unsupported details (L11). Its escalation-check line — "No other category applies" — depends on the Step 0 authorization holding (M1) and on the H3 reading.

---

## What would close this round

1. **§7's Tridentine bullet** — remove or correct the Wittenberg attribution. Log the discovery that this world's own Step 0 misquotes Wittenberg's Step 0 as a new `Open_Gaps_Tracking.md` entry. (H1)
2. **§4 and §5** — reconcile the formation characterization explicitly, carry the worship-convergence finding into §5, answer the authority question about Zurich and Geneva rather than their descendants, and weigh the two-independent-origins evidence inside §4. If it comes out ambiguous, escalate. (H2)
3. **§9 and the Decision Log** — state that a live Category-2 item bars self-disposition of Doc_01 as a whole, and withdraw the Living-Tradition-Status analogy. Check Donatism's Doc_01 §1/§8 before restating it. (H3)
4. **The masthead** — file the launch instruction in this world's build folder, as IJC's build folder already does, and cite it by path; or withdraw "verifiable" and the Wittenberg corroboration and escalate the sequencing question alongside Dort. (M1)
5. **Correct M2–M7 and M9**, each of which is a new claim introduced by a Round 1 fix. Per Donatism's own standing process note, re-verify each correction against every document it touches before applying — including the two new supporting files, which are now part of the surface a fix has to propagate across.
6. **Attach a trade-off to each of §7's three options** (M8), and extend the confidence vocabulary into §2, §6 and §7 as Round 1 asked (H5).
7. **Fix L6** — it is the one Round 1 finding untouched, and the Decision Log does not record it as outstanding.

---

*Filed per `cic-build-cycle`: review rounds exist as files, not claims. Two procedural notes, neither a finding against the document's content. (1) `Review-Artifacts/Doc01_Round1_Review.md` enters git history for the first time in the revision commit `58b30b0`, alongside the changes it prompted, rather than in its own commit before them. The artifact exists and its content is sound, so the skill's requirement is met — but a review artifact committed only together with its own fixes is weaker evidence of independence than one committed when it was produced, and worth a coach thread's attention as a pattern. (2) Round 1's own closing note on the `Ministry/` versus `Review-Artifacts/` placement inconsistency stands unresolved; this review follows the same precedent it did.*
