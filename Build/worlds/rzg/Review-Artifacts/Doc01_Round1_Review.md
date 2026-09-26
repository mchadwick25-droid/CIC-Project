# Doc_01 Round 1 — Independent Adversarial Review: The Reformed Cities — Zurich & Geneva

**Document under review:** `World-Builds/Reformed-Zurich-and-Geneva/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, Revision 1, 2026-09-15)
**Review date:** 2026-09-15
**Reviewer:** independent adversarial review, run in isolation per `cic-build-cycle`. No drafting context seen.

**Sources checked against, directly and in full:**

- `Build/reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` — Articles 20, 21, 22, 23, 29, extracted from `word/document.xml` (zipfile + regex strip); internal text is V2.3, as the draft states
- `Build/reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — Part I and Step 1, same extraction method
- `cic-website/data/world-census.json` — entries V.5, VI.1, VI.2, VI.3, VI.9, VI.11, VI.14, VI.22, VI.26, and the `latin-pastoral-congregational-christianity` → `the-reformed-cities-zurich-and-geneva` transmission edge, read as parsed JSON field by field
- `World-Builds/Reformed-Zurich-and-Geneva/Step0_Movement_Scope_Confirmation.md`
- `World-Builds/Lutheran-Wittenberg/Step0_Movement_Scope_Confirmation.md`
- `world-build-docs/_cross-world/dossiers/the-reformed-cities-zurich-and-geneva_Source_Readiness_Dossier.md`
- `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`
- `CLAUDE.md`; the `cic-build-cycle` skill
- Prior Doc_01s for comparison: Donatism, Imperial-Juridical Christianity, Alexandria; `World-Builds/Donatism/Review-Artifacts/Doc01_Round1_Review.md`
- `records/`, `packages/`, `records/WORLDS_REGISTRY_LOG.md` for the file-code check
- Historical verification against standard Reformation scholarship (Gordon, *Calvin* and *The Swiss Reformation*; Potter, *Zwingli*; Kingdon; Stayer/Packull/Deppermann on Anabaptist polygenesis; the standard Dort literature)

---

## Setup discrepancy (report, not a reason to review something else)

The document under review is **not** on this worktree's branch. Worktree HEAD is `3bf4126` (merge of PR #227). The draft is commit `1b96352` on branch `reformed-cities-doc01`; its parent `d3bab94` carries the vendored texts and the corpus map. Neither commit is on `main`. On `main`, `World-Builds/Reformed-Zurich-and-Geneva/` contains only `Step0_Movement_Scope_Confirmation.md`, and `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml` does not exist at all.

The brief stated the draft would be the tip commit of the current branch. It is not. I reviewed against `reformed-cities-doc01` throughout, which is the right content; but anyone re-running this review from a default checkout will not find the file, and the corpus map the draft cites is not yet on the canonical branch.

---

## Verdict

**SUBSTANTIAL REVISION REQUIRED.**

**6 high, 13 medium, 13 low.**

The historical spine of this draft is largely sound. Every date in the §2 catalyst chain that I could check independently is correct — Zwingli's 1 January 1519 start, Bullinger 1531–1575, the two Zurich Disputations of 1523, the Sausage Affair 1522, Bern 1528, Kappel 11 October 1531, Calvin's 1536 arrival and 1538–41 Strasbourg exile, the 1541 Ordinances, the Consensus Tigurinus 1549, Bolsec 1551, Servetus 1553, the Perrinist resolution 1555, the Academy 1559, the Psalter 1562, Heidelberg 1563, the Second Helvetic 1566, the Zurich Bible 1531. The observation that Geneva was not a Confederacy member in this period is correct and carefully hedged. The Anabaptist correction to the dossier is a real and valuable finding. And almost every verbatim quotation from the Constitution, the census, the corpus map, the dossier and the two Step 0 documents is character-exact — I checked each one against the primary file and list the clean ones at the end of this review.

The failures are not in the dates. They are of four kinds:

1. **The document's two central judgments — the Strand Determination (§4) and the Dort scoping decision (§6) — both fail on their own reasoning.** §4 marshals evidence that argues for two *worlds* and reads it as two *strands*, without ever running the Framework's World Separation Criteria, which is the test that decides that question and which the document omits entirely. §6 claims to be applying an already-made portfolio decision; the census records the opposite — Dort is named in two entries with the scope question expressly left open, and this world's own Step 0 assigned the decision to Doc_01 to *make*.
2. **§8's escalation assessment is wrong on both of the above**, and also on the fact that this document was drafted at all: its own Step 0 says in terms that no build thread should open on its strength.
3. **Confidence calibration is inverted.** The project's five-level vocabulary appears nowhere. The single claim the draft hedges (the Genevan delegation to Dort) is correct; several claims asserted flat are wrong.
4. **Four citation claims overstate what the cited file actually says** — one of them ("quoted in full") about the Constitution, one about the corpus map that converts an open sourcing item into a closed one.

Findings H1, H3 and H5 are each a recurrence of a defect this project has already recorded once. H3 in particular is the same failure shape as Donatism's own Doc01 Round 1 H1: the strand finding does not clear Article 21 on the reasoning given, and the strongest evidence adduced cuts against it.

---

## High-severity findings

### H1. Doc_01 was drafted before Step 0 cleared review, against Step 0's own explicit instruction — and §8 does not name this

**What Step 0 says about itself** (`Step0_Movement_Scope_Confirmation.md`, status line and §6, verbatim):

> "**This document has not been independently reviewed** — treat every finding below as a considered first pass, not a verified conclusion. **Not self-disposed. Not Approved to proceed.** Advisory work product for Mark's own consideration; **no build thread has been opened under `cic-build-cycle`**."

> "**Recommended next step:** an actual independent adversarial review round... **No build thread should open on the strength of this document alone.**"

**What `cic-build-cycle` says:**

> "Don't skip ahead. If a document earlier in the sequence hasn't reached at least 'Approved to proceed' yet, don't start drafting, outlining, or even thinking through a later one."

The draft's masthead acknowledges the problem — "Tier 1, DRAFT — not yet independently reviewed itself, per that document's own disposition" — and then proceeds anyway. §8 concludes: "No escalation category applies on the content of this draft."

That conclusion is wrong even on its own terms. Building Doc_01 on a Step 0 that (a) has not cleared review, (b) explicitly forbids a build thread opening on its strength, and (c) is the sole source of five of this document's six carried-forward binding items, is an "unresolved tension the pipeline can't close on its own" — the fourth escalation category. The document cannot self-certify past the instruction of the document it is built on. §8's careful hedge ("this assessment is itself subject to independent review") does not close this, because the gate is procedural and sits *before* drafting, not after.

**What the correct handling is:** either Step 0 goes through its own review round first, or the conflict is escalated to the project lead as a named tension. Not both drafted and self-disposed.

### H2. The Dort scoping decision misrepresents the census as having settled a question the census records as open — and it is a portfolio-level decision requiring escalation

**Draft text (§6):**

> "That decision is not, on inspection, this document's own to invent: the census's own already-adopted portfolio design gives Dort itself a named home."

> "...i.e., the portfolio itself already treats Dort, the Remonstrance, the Canons, and the exiled Remonstrant Brotherhood as VI.26's own story, not this world's. **Finding, applying that already-made portfolio decision rather than redeciding it:** the Synod of Dort's own event... belongs to VI.26's own future construction, not this world's."

**Draft text (§8):**

> "...this document makes one substantive new decision — the Dort scoping question (§6) — but does so by directly applying an already-made portfolio-level decision... not by deciding a new cross-world question on this document's own authority."

**What the census actually says.** Three things, all of which cut against this:

1. **VI.26's own `relationsSummary`:** "...gives Dort itself a named home (**paired with VI.9's scope line**)". Not "its exclusive home." Explicitly paired with a scope line elsewhere.
2. **VI.9 (Dutch Further Reformation & Refuge Culture), `relationsSummary`:** "**Dort (1618-19) is named here and in the Remonstrants' own entry** — with the standing scope line: whether this entry is supporting-context or its own tradition remains **a real Step 0 call**". And VI.9's `why`: "Whether this is a tradition in its own right or supporting context for others is a genuine open call, and **the Freeze left it open rather than settling it**."
3. **VI.26's own status fields:** `statusWord` is "Researched — **deferred**, richer window later (Era 7 Step 0)". Its `why` field, which the draft quotes, reads in full: "Proposed by the completeness sweep: a real surviving communion born of a synod that had no named home anywhere in the census. **Tier 3 signal; awaiting the gate.**" The draft quotes the first sentence character-exact and drops the second — the clause that says the decision has not been taken.

So Dort is named in **two** census entries, neither built, with the scope question recorded in the census's own words as an open Step 0 call the Era 7 Freeze deliberately did not settle. There is no already-made portfolio decision here to apply. The draft's §6 reads the *existence* of a VI.26 entry as a *scope ruling*, and then quotes selectively around the text that says otherwise.

**What this world's own Step 0 assigned.** §4 item 2, binding on Doc_01:

> "**The Dort/Remonstrants scoping question (binding on Doc_01, before drafting proceeds).** **Decide** whether the Synod of Dort (1618–19) belongs inside this candidate's own story or should be left for a separate build of VI.26 **if that ever happens** — a real scope decision, not a floor or continuity question."

Step 0 treats VI.26 as conditional and unbuilt ("if that ever happens") and assigns the decision to Doc_01 to make. §6 reverses this: "That decision is not, on inspection, this document's own to invent." The binding instruction is evaded by reframing a decision as pre-made.

**Why this is an escalation.** `cic-build-cycle`: "**Portfolio-level or cross-world strategic decisions** — anything decided for a reason external to this specific world's own ecology. Label it explicitly as portfolio-level in whatever document records it." `CLAUDE.md` default-action table: "Cross-world or portfolio-level decision | **Always ask**." The draft's stated reason for excluding Dort is entirely external to this world's ecology — another census entry exists. By the skill's own definition that is a portfolio-level decision. §8's "No escalation category applies" is wrong.

**A further internal inconsistency.** The draft handles the analogous cases in the opposite way. Marburg (§6, versus VI.1) is treated as jointly engaged by two worlds, with reciprocal cross-reference owed. Trent (§6, versus VI.22) is treated as jointly engaged: "Doc_02 for both worlds should expect to cite each other as the primary named rival." Only Dort is treated as exclusively one world's, and it is the only one of the three where the census itself names the event in two entries. Nothing in §6 explains why Dort is the exception.

**What the correct handling is:** escalate the scope question to the project lead as a portfolio-level decision, presented as named options with trade-offs (Dort wholly out; Dort's Reformed side in-window for this world with the Remonstrant side to VI.26; Dort deferred pending VI.9's own scope call), and state plainly that the census left it open. Do not self-dispose.

### H3. The Strand Determination's evidence argues for two worlds, not two strands — and the document never runs the World Separation Criteria test that decides that

**What Article 21 actually says** (`CiC_L1_Constitution_V2_2.docx`, Art. 21, verbatim — checked character-exact):

> "Strand is defined as a meaningfully distinct pattern of formation emphasis, practice, authority structure, or ecological orientation **within a single world**, not merely a variation in detail."

The phrase "within a single world" is a **precondition** of the strand test, not an output of it. Article 21 tells you how to sort variation *once you already know you are inside one world*. It cannot itself establish that you are.

**What the draft does.** §4 marshals divergence on three of Article 21's four named dimensions — practice (organ and singing), authority structure (council versus Consistory), formation emphasis (Prophezei versus catechism-plus-discipline) — and presents the count as strengthening:

> "The evidence clears Article 21's bar on **more than one of its own named dimensions independently**, not on a single contestable point."

And it characterizes each divergence in maximal terms: "two cities within the same reforming movement reaching **opposite conclusions**... about whether congregational song belongs in worship at all"; "**two different authority structures**, not one structure under two names"; "**genuinely different formation logics**."

§5 then adds the decisive material, in the document's own words:

> "**two independent local triggers, not one shared cause**... The two triggers are connected only retrospectively, by the Consensus Tigurinus — this world's own coherence is a documented later bridge across two separate beginnings, **not a single common origin**."

And §4 describes the bridge itself as a treaty between separate parties:

> "it is a negotiated agreement between **two already-distinct parties** on their most contested point of doctrine."

**What the Framework's own test asks** (`CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`, Part I, World Separation Criteria, verbatim):

> "**World Separation Criteria** — When does one world become another? Questions include: Has a new gravity emerged? Has a major gravity disappeared? **Has formation changed substantially? Has worship changed substantially? Has authority changed substantially?** Has interpretation changed substantially?"

The draft answers three of those six affirmatively — in those exact categories, in those words — and never names the test. Separate origin, separate authority structure, opposite worship conclusions, separate formation instrument, and a *negotiated agreement between already-distinct parties* is the profile the World Separation Criteria exist to catch.

**So the argument is structurally backwards.** Every additional dimension of divergence §4 establishes makes its own unstated single-world premise weaker, not its conclusion stronger. "Clears the bar on more than one dimension independently" is not a strengthening claim here; it is an accumulation of separation evidence presented as strand evidence.

This is the same failure shape as Donatism's Doc01 Round 1 H1 — "the central Step 1 deliverable does not clear Article 21's own definitional test on the reasoning given, and the strongest piece of evidence it cites actually cuts against the finding."

**What the correct handling is.** The two-strand conclusion may well be right — there are real arguments for it that §4 gestures at but does not develop: a shared confessional core, a shared civic-reform ecology, the Consensus as a *doctrinal* rather than *institutional* settlement, the Second Helvetic and Heidelberg both later speaking for the movement as a whole, and a continuous Reformed transmission downstream that does not fork by city. But those arguments have to be made *as* the single-world argument, under World Separation Criteria, **before** Article 21 can be applied at all. The document has to establish the premise it currently assumes.

The census itself shows the project expects exactly this argument to be made. VI.5 (Scottish Reformation), `why` field: "Its real test is distinctness from its Genevan parent... **Whether that suffices to make it a separate tradition rather than a Genevan province is precisely what a build would have to argue.**" If Scotland-versus-Geneva has to be argued, Zurich-versus-Geneva does too.

If the separation test comes out genuinely ambiguous, that is an unresolved tension for the project lead, not something a build thread settles by choosing the framing that keeps the world intact.

### H4. World Separation Criteria — a required Part I element — is missing entirely

The Framework's Part I lists six elements: Distinct World Criteria; Temporal / Geographic / Cultural Scope; **World Separation Criteria**; Strand Determination; Preliminary Forces Identification; World Continuity & Distinction.

The draft covers five. It has no World Separation Criteria section and never uses the phrase. §6's "Distinctness from adjacent worlds, examined directly rather than assumed" is not it: that answers the Distinct World Criteria question ("What distinguishes this world from adjacent worlds?"), which §3 already forwards to §6. The separation question — "when does one world become another," with its six named change tests — is not asked of anything, internal or external.

This is not a formatting quibble. Alexandria's Doc_01 masthead names its own Part I coverage explicitly and includes "**the World Separation Criteria**" in the list. The element exists in prior Doc_01s in this repo; it is absent here; and its absence is exactly what lets H3 through.

**Two Temporal Scope questions are also unanswered.** Part I, Temporal Scope: "What developments remain internal? What developments indicate transition?" §2 answers "What beginning point is appropriate?" and "What ending point is appropriate?" but neither of the other two. This matters directly: "what developments indicate transition" is where Dort belongs as a Doc_01 question, and routing it to §6 and then outsourcing it to the census (H2) is what happens when that question is never put.

### H5. Confidence calibration is inverted, and the project's five-level vocabulary is used nowhere

`CLAUDE.md`, Source fidelity:

> "Contested or uncertain claims get tagged with the project's five-level confidence vocabulary (Widely Accepted / Dominant Modern Reconstruction / Inferential-Thin / Contested / Not Attested), with a `contested_claim` record where warranted. **Never present a disputed claim as settled.**"

None of the five levels appears anywhere in the draft. There is exactly one hedge in the whole document — §6, on the Genevan delegation to Dort:

> "per standard Reformation historiography — **not independently verified against a primary vendored source this pass, and flagged here rather than asserted as settled** — an international Reformed delegation attended the Synod of Dort including representatives from Geneva itself (commonly identified as Giovanni Diodati and Theodore Tronchin)"

**The hedge is honestly worded and correctly placed — and the claim it hedges is true.** Giovanni Diodati and Theodore Tronchin were Geneva's two delegates to Dort. This is not a case of a hedge covering a shaky claim.

The defect is that it is the *only* hedge, and it sits on one of the few claims in the document that does not need one, while M2–M6 and M13 below are asserted flat and are wrong or genuinely contested. A single hedge in a document of this density reads as a compliance gesture rather than a calibration discipline. Under `CLAUDE.md`'s rule the tagging obligation attaches to the contested claims, not to whichever claim the drafter happened to feel least sure about.

**One substantive addition on the same point, which cuts against §6's conclusion.** Geneva was not the only delegation from this world at Dort. The Swiss Reformed cantons — Zurich, Bern, Basel and Schaffhausen — sent a joint delegation, led on the standard accounts by Johann Jakob Breitinger, Antistes of Zurich. I flag this at the same confidence the draft's own Diodati/Tronchin note uses: standard historiography, not verified here against a vendored primary. If it holds, **both** of the strands §4 identifies were represented at Dort in person, and §6's exclusion of Dort from this world's story becomes substantially harder to sustain. §6 does not mention the Swiss delegation at all, which is the piece of evidence most damaging to its own finding.

### H6. A binding-on-Doc_01 item from Step 0 is silently dropped

Step 0 §4 item 1, first on its list of "Required disclosure obligations and decisions carried forward (binding, not discharged here)":

> "**The Zwingli/Bullinger/Calvin continuity structure (binding on Doc_01).** State plainly that this candidate's coherence rests on **Bullinger's own mediation** (the Consensus Tigurinus) and not on any direct relationship between Zwingli and Calvin, **who never met and whose ministries did not overlap**."

And Step 0 §2 A2: "**There is no direct personal link between Zwingli and Calvin.**... Doc_01 **must state this plainly** rather than imply direct contact between Zwingli and Calvin that did not happen."

The draft never states that Zwingli and Calvin never met. It never states that their ministries did not overlap. And it locates the bridge in the *document* rather than in *Bullinger's mediation* — §4: "The Consensus Tigurinus itself is the documented evidence..."; §1: "formally bridged, not merged, by the Consensus Tigurinus (1549)." Bullinger appears throughout as a figure but never as the mediator whose mediation the coherence rests on, which is the specific claim Step 0 binds Doc_01 to make.

§1's "joined — not founded — by John Calvin" and §5's "two independent local triggers" are in the right neighbourhood, but they are not the plain statement required, and a reader could come away from §1 with exactly the implication Step 0 warns against.

**This is the only one of Step 0 §4's six items that is neither discharged nor carried forward.** Items 2, 3, 4, 5 and 6 are all cited by number in §6 and §7 (and all five citations are numerically correct — see the verified list below). Item 1 appears nowhere: not discharged in the body, not listed in §7's ten carried-forward items. `cic-build-cycle`: "If the world being built has known open issues on record, address them in this document rather than deferring them silently."

---

## Medium-severity findings

### M1. "Quoted in full" is false for Article 22; and §4's pointer for Article 21 points at content that is not there

**(a) §5 claims a full quotation it does not give.**

Draft (§5): "Constitution Article 22 (**quoted in full**): 'Every formation world is situated against the forces that shaped it across both external and internal dimensions, and across the duration of its life... Where a world's formation continues unbroken into a living tradition, or where no internal fracture is attested by the evidence, that finding is recorded honestly as the result of the assessment — never inferred, never supplied to satisfy the requirement that the assessment occur.'"

Article 22 continues for two further sentences the draft drops without any marker:

> "These forces are documented from within the world's own formation logic — as the world experienced and understood them — never as an external analytic overlay imposed on it, consistent with the Writing-From-Inside Principle (Article 23). The methodology of forces analysis, including the cells across which forces are identified, is governed by the Forces Framework."

So it is not "in full," and the omitted tail is the part most relevant to what §5 is doing — §5's six-cell sketch is written in flat external-analytic register throughout ("The late-medieval Latin church's own sacramental and clerical order, contested from within the Swiss Confederacy's own decentralized city-state structure"), which is precisely the register the dropped sentence forbids. The quoted portions themselves are character-exact ✓; the claim about their completeness is not.

**(b) §4 cites Article 21 to a location where it does not appear.**

Draft (§4, opening): "Per Constitution Article 21 (**quoted verbatim above and in full at §5's own heading**)..."

Article 21 is not quoted anywhere above §4 in this document. §5's heading quotes Article **22**, not Article 21. The two Article 21 fragments §4 itself quotes are character-exact ✓ — but the pointer to where they were supposedly established is false in both halves. This is the same class of defect Donatism's Doc_01 Round 1 recorded as "fabricated/miscited governance references."

### M2. The Marburg break is described anachronistically as including Calvin's position

Draft (§5): "Zwingli's own memorial reading **and Calvin's own spiritual-presence position** both refuse Luther's real-presence formula, **the specific and irreducible content of the Marburg break (1529)**."

The Marburg Colloquy (1–4 October 1529) was Luther and Melanchthon against Zwingli and Oecolampadius. Calvin was about twenty, still a law student, not a reformer, not present, and his spiritual-presence doctrine post-dates Marburg by at least a decade. Geneva was not reformed until 1536. Calvin's position is not "the content of the Marburg break"; it is a later development that made the 1549 Consensus possible.

Draft (§1) carries the same problem: the Supper is "the specific point of doctrine that separated **this world** from Wittenberg's own Lutheran Reformation at Marburg (1529)." In 1529, "this world" — as the draft itself defines it in §5, with Geneva's origin in 1536 — was Zurich alone.

### M3. Beza's double predestination is dated after Calvin's death; it is not, and the Remonstrance claim overstates

Draft (§6): "Theodore Beza's own systematized double-predestination theology, **developed at the Genevan Academy after Calvin's death** and **the direct target the Remonstrance itself was written against**."

Two errors.

**(a)** Beza's *Tabula praedestinationis* — the supralapsarian double-predestination scheme — was published in 1555. Calvin died in 1564. Beza did become rector of the Academy (1559) and Calvin's successor as moderator (1564), but the doctrine predates both by years. "Developed at the Genevan Academy after Calvin's death" is wrong on both the institution and the date.

**(b)** The 1610 Remonstrance's five articles were framed against the Belgic Confession and the Heidelberg Catechism as construed by the Dutch Contra-Remonstrants. Arminius's immediate opponents were Franciscus Gomarus and Franciscus Junius at Leiden. Beza had been Arminius's teacher at Geneva and is a target at one remove; "the direct target the Remonstrance itself was written against" collapses that distance. This claim is doing real work in §6 — it is the throughline offered as what this world "legitimately transmits" to Dort — and it is asserted flat on the same line as the correctly-hedged Diodati/Tronchin claim.

### M4. The Grossmünster organ date appears wrong, and it is the lead evidence for the strand finding

Draft (§4, first evidentiary limb): "the Grossmünster's own **organ was destroyed in 1524**."

The Grossmünster organ is conventionally dated to its removal in **1527**. 1524 is the year of Zurich's image-removal ordinance and the stripping of church ornaments; the abolition of singing in Zurich worship came with the abolition of the Mass in 1525. I flag this at Dominant Modern Reconstruction confidence rather than as a certainty, but at minimum it needs a source.

What makes it a Medium rather than a Low: this is the **first named piece of evidence** under the Practice limb, which is the limb §4 leads with, in a section that is the document's central Step 1 deliverable. It is not vendored, not cited to anything, and asserted to the year. See also M12 on the unvendored status of §4's other pillars.

### M5. The first Anabaptist baptism is misattributed

Draft (§2): "the 1525 first believer's baptism in Zurich **by Conrad Grebel and Felix Manz**". Draft (§6): "the first Anabaptist believer's baptisms in Zurich (January 1525) were **performed by Conrad Grebel and Felix Manz**."

On the standard account — 21 January 1525, at Felix Manz's house — **Conrad Grebel baptized Georg Blaurock**, and Blaurock then baptized the others present. Manz hosted and was among those baptized; he did not perform the first baptism. Blaurock, who was both the first recipient and the administrant of the rest, is not named anywhere in the draft. (The census's own VI.3 `voices` field is also imprecise here — "Conrad Grebel — Zurich radical, **among the first to be re-baptised** in January 1525" — and the draft does not check it.)

**The substance of §6's correction stands and is valuable.** Grebel and Manz were members of Zwingli's Zurich circle and broke from him over infant baptism, tithes and the church's dependence on civil authority; the Swiss Brethren origin genuinely is an internal schism from the Zurich strand; and the draft is right to scope this to the *Swiss Brethren* rather than to Anabaptism generally, which keeps it consistent with the polygenesis scholarship the census's own VI.3 entry names as current standard. The dossier §5 quotation — "no figure overlap with Lutheran Wittenberg, the Jesuits, the Anabaptists, or Lollardy" — is character-exact ✓. The correction is right; the detail carrying it is wrong.

**Propagation gap.** The same "no figure overlap" claim also appears in **this world's own Step 0 §3 B3** ("no figure overlap with the Jesuits, the Anabaptists, the Tridentine Church, or Lollardy"). §6 corrects the dossier and does not mention that Step 0 carries the identical now-superseded claim, and §7 item 4 does not flag it either. `cic-build-cycle`: "Whenever a name or term changes, check every file it appears in... A fix that lands in the narrative document without the index being updated to match is not a complete fix."

### M6. "No documented direct contact" with the Jesuits is borrowed from a different world and is weak on the merits

Draft (§6): "The Society of Jesus (VI.11) and Lollardy (V.5): no figure or doctrinal overlap identified; the Jesuits are founded (1540) a full generation into this world's own window **with no documented direct contact**."

The phrasing tracks **Lutheran Wittenberg's** Step 0 §3 B3: "no figure overlap with the Society of Jesus (VI.11, founded 1540, a full generation after Luther's own death in 1546, no direct contact)." That is a finding made about Wittenberg — and it is itself wrong on its face there, since 1540 precedes 1546. The draft silently re-applies a sibling world's conclusion to a different world with a different window, correcting the temporal direction but carrying the conclusion across unverified.

`cic-build-cycle`: "don't reach for content, sourcing, or characterizations that belong to a different formation world, even one that seems similar."

On the merits, for a Reformed world running to 1650, "no documented direct contact" over 110 years is not a finding this document has evidence for. Bellarmine's *Disputationes* were the standard Jesuit reply to Reformed theology — the census's own VI.22 entry names him as "the era's standard Catholic reply to Protestant theology." Jesuits were established at Fribourg from 1580, directly facing Reformed Bern and Geneva. The Catholic reconquest of the Chablais in the 1590s was fought on Geneva's doorstep. At minimum this needs downgrading to "not assessed this pass."

### M7. §7 item 6 overstates corpus-map progress against the corpus map's own text

Draft (§7 item 6): "The corpus-map (`cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`, from PR #229) now individually itemizes the Sixty-Seven Articles as their own row **and separately rows the letter to Erasmus, the petition to the Bishop of Constance, and the Acts of the Zurich Disputations** — real progress since Step0's drafting. The *Selected Works* row **still lumps 'other shorter writings' together** rather than itemizing every individual piece; Doc_02 should treat this as a **residual, much-narrowed** completeness question, not a closed one."

**What the file actually contains.** The Sixty-Seven Articles is its own row ✓ — that part is correct and is genuine progress. But the Erasmus letter, the Constance petition and the Acts of the Disputations are **all inside a single row**:

> `work: Selected Works (letter to Erasmus; the petition to the Bishop of Constance on clerical marriage; the Acts of the First and Second Zurich Disputations; and other shorter writings)`
> `note: "The volume's remaining shorter selections, **kept as one collective row rather than individually itemized** — letters, petitions, and disputation records..."`

Nothing beyond the 67 Articles is separately rowed. The corpus map says so in terms. So the un-itemized remainder is not a "residual" tail of "other shorter writings" — it is the entire row, four named items plus the remainder.

This converts an open sourcing item into a substantially-closed one on a misreading of the file. Under `cic-build-cycle`'s revision test that is substantial: it changes a sourcing conclusion.

### M8. The corpus-asymmetry statement misdescribes which volumes are shared

Draft (§7 item 1): "Calvin's vendored corpus (three full Institutes volumes plus the Geneva Catechism) is far larger than Zwingli's (**two volumes, one shared with the Heidelberg Catechism and Second Helvetic Confession**)."

The Calvin half checks out ✓ — three Institutes source files (Books I; II–III; IV) plus `calvin_geneva-catechism_waterman1815.txt`.

The Zwingli half does not. Zwingli's two source files in the corpus map are `zwingli_selected-works_jackson1901.txt` and `zwingli_latin-works-correspondence-vol1_jackson1912.txt`. **Neither contains the Heidelberg Catechism or the Second Helvetic Confession.** Those two works share a third, entirely separate file — `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` — attributed to Bullinger and to Ursinus/Olevianus. No Zwingli volume is shared with anything.

This matters because §7 item 1 is the item that governs how Doc_02 weighs the Zurich strand's evidence, and it misstates the shape of the Zurich corpus in the direction of making it look more entangled than it is.

### M9. The Article 4 floor clearance is upgraded beyond what Step 0 verified

Draft (§1): "Article 4 commitments **(1)–(5)**, quoted in full in `Step0_Movement_Scope_Confirmation.md` header, are **affirmed throughout without qualification**."

Step 0 does quote all five commitments in its header ✓. But Step 0 §2 A1's actual verification is narrower: "the Second Helvetic Confession... **chapter III affirms the Trinity and chapter XI affirms Christ's full deity and humanity in terms matching Article 4's commitments (1)–(3) directly**; the Heidelberg Catechism (1563) is doctrinally consistent throughout."

Commitments (4) — the passion, resurrection, ascension and return — and (5) — the Holy Spirit — were not directly verified against a text. Step 0's "clears without qualification" is a conclusion about the floor; it is not a claim that all five commitments were individually checked. §1 states more than its cited source establishes.

### M10. "Per Article 29's own terms... a project-lead act" — Article 29 does not say that

Draft (§1): "Per Article 29's own terms, this world is not freeze-eligible until Living Tradition Status is confirmed — **a project-lead act this document cannot perform on its own behalf**." And §7 item 9: "**Per Article 29**, whether and how it is confirmed is the project lead's own act at freeze."

The freeze-eligibility half is correct and is Article 29's own ✓: "a world touching a living tradition is not freeze-eligible until its Living Tradition Status is confirmed." The Article 29 fragment §1 quotes verbatim is also character-exact ✓.

But Article 29's closing sentence is: "**The method of confirmation is governed by the build documents**; the requirement that it occur is constitutional." It does not assign confirmation to the project lead. Every prior Doc_01 in this repo cites a second authority for that framing, and none rests it on Article 29 alone:

- Donatism Doc_01 §1: "Per Constitution Article 29 **and Formation World Blueprint V7.3 §17**, Living Tradition Status confirmation is a project-lead act..."
- Imperial-Juridical Christianity Doc_01 §1: "Per Constitution Article 29 **and this project's established practice** (see `World-Builds/Syriac-Christianity-Edessa-Nisibis/Open_Gaps_Tracking.md`, item 10)..."
- Alexandria Doc_01 §9 records a dated, named project-lead confirmation as the mechanism.

The underlying claim is right as project practice; the citation is wrong. Given that the draft elsewhere insists it is checking the Constitution "directly against the governing document rather than carried forward from a prior document's own paraphrase," attributing to Article 29 a provision that lives in the Blueprint is the specific failure that sentence claims to be guarding against.

### M11. Episcopal vocabulary applied to three non-episcopal Reformed centers

Draft (§2): Zurich is "Zwingli's and then Bullinger's own **see**"; Geneva is "Calvin's **see** from 1536"; the Palatinate is "the **see** of Ursinus and Olevianus."

A see is a bishop's jurisdiction. None of these five men was a bishop. Zurich's office was the *Antistes*; Geneva was governed by the Company of Pastors and the Consistory; the Palatinate church was a Reformed territorial church. Abolishing episcopal jurisdiction is exactly what these churches did — and §1 makes the non-episcopal order this world's **Distinctive Contribution**: "church government by elected elders rather than by bishops" is the census's own summary of the legacy.

Under Article 23's Writing-From-Inside Principle this is an external category imposed on a world that defined itself against it, in a document that elsewhere argues the Consistory's lay-elder authority is what makes this world distinct. Prior Doc_01s in this repo use "see" for genuinely episcopal worlds; it looks like a template habit carried across an era boundary without adjustment.

### M12. Two of §4's three evidentiary pillars rest on unvendored documents, without disclosure

§4's Practice limb rests on the Genevan Psalter. Its Authority-structure limb rests on the 1541 Ecclesiastical Ordinances. **Neither appears in `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`.** The nine mapped works are: Second Helvetic Confession; Institutes Books I, II–III, IV; Geneva Catechism; Heidelberg Catechism; Zwingli Selected Works; Zwingli Latin Works vol. I; the Sixty-Seven Articles.

The Consensus Tigurinus — which §4 itself calls "the single document that most directly evidences the two-strand bridge this world's coherence rests on" — is also unvendored, and that one **is** properly disclosed (§7 item 2) ✓. The Psalter and the Ordinances are not disclosed anywhere. §4's characterizations of both are drawn from general knowledge plus the census's descriptive `sources` notes.

`CLAUDE.md`: "Every quote must be re-verified verbatim against the vendored source file before a record passes review." The document's central Step 1 deliverable should say plainly which of its evidence is text-verified and which is not. As drafted, a reader cannot tell that the strand finding rests substantially on documents the build does not yet hold.

### M13. Marie Dentière's 1539 Epistle is offered as an example of publishing "under her own name"

Draft (§7 item 8): "Marie Dentière (a former abbess turned Genevan reformer who **published under her own name** arguing women could speak about scripture)... assess whether Dentière's own known publications (**e.g., her 1539 *Epistle to Marguerite de Navarre***) are acquirable."

The first half faithfully carries the census's `voices` field ✓ ("former abbess turned Genevan reformer, who published in her own name arguing that women could speak about Scripture"). The example is the draft's own addition, and it is the wrong one: the *Epistre très utile* (1539) was published **anonymously**, by "une femme Chrestienne de Tornay." The Geneva authorities seized the edition and prosecuted the printer. Dentière's signed publication is the 1561 preface to Calvin's sermon on women's apparel. The composite asserts something false about the specific work it names.

Two smaller points in the same item. Article 20 does not "name women for special attention"; its scope is "**the marginalized within the community** — those whose voices the sources structurally suppress." Dentière plainly qualifies, so the Affirmative-Duty point is well made and should be kept — but the Article is being quoted for a specificity it does not have. And "abbess" is the census's loose term; she was prioress of an Augustinian house at Tournai.

---

## Low-severity findings

**L1.** §2 dates Geneva's Bern alliance to 1536. The *combourgeoisie* with Bern (and Fribourg) dates from 1526. 1536 is Bern's military intervention and Vaud campaign, and Geneva's reformation vote of 21 May. §2's "allied with Bern (1536)" and "the 1528 Bern Disputation... directly enabled Geneva's own 1536 break from Savoy" compress a decade of alliance into one year.

**L2.** §1 says "the Second Battle of Kappel." Standard usage is the Battle of Kappel (11 October 1531), fought during the Second War of Kappel. §2 gets it right.

**L3.** §1 uses "Ulrich Zwingli"; the census uses "Huldrych," the corpus map's source volumes "Huldreich." `cic-build-cycle`'s naming and term-propagation rule.

**L4.** §2 presents joint Ursinus–Olevianus authorship of the Heidelberg Catechism as settled. It is the traditional attribution; Olevianus's share is disputed in current scholarship, with Ursinus generally treated as principal author under Elector Frederick III's commission. The corpus map carries the same traditional attribution, so the draft matches its source — but this is a claim that warrants a confidence tag rather than flat assertion.

**L5.** The Source Readiness Dossier is cited four times (§6; §7 items 2, 6, 7) with **no path**, while every other source in the document is path-cited. It lives at `world-build-docs/_cross-world/dossiers/the-reformed-cities-zurich-and-geneva_Source_Readiness_Dossier.md` — not in this world's build folder, which is where a reader would look.

**L6.** §7 item 6 cites "(from PR #229)". A PR number is not a checkable in-repo citation. The file path is given alongside, which is the usable half.

**L7.** Unmarked borrowing of sibling-document wording. §2's Servetus parenthesis reproduces Step 0 §2 A1 almost verbatim ("Calvin's own theology is not in question, his conduct toward a rival current is a different matter") without quotation marks. §6's Tridentine line reproduces Lutheran Wittenberg's Step 0 §2 A3(3) ("Doc_02 for both worlds should expect to cite each other as the primary named rival") likewise. Both are accurate in substance; neither is marked as quoted.

**L8.** §2's Cultural Environment cites "(Step0 §2 A3; §6 below)" for the princely-patronage contrast with Wittenberg. Step 0 §2 A3 covers Marburg and Dort. The origin and church-order contrast is in Step 0 §0 and §3 B4.

**L9.** §6 reports Step 0 §3 B3 as having "named" Trent as "this world's own direct doctrinal rival." Step 0 B3 actually says Trent's decrees "will **almost certainly** need to be read directly against this candidate's own confessional documents," and attributes the phrase "direct doctrinal rival" to *Lutheran Wittenberg's* Step 0, not to its own finding. A probable future need is reported as a made determination.

**L10.** §5's inherited-transmission quotation is character-exact ✓, but the census text it quotes applies "total depravity, unconditional election, and irresistible grace" to Calvin's *Institutes*. Those are categories derived from the Canons of Dort (1619), sixty years after the 1559 Institutes. The draft adopts the anachronism without comment — worth a note in a document that elsewhere argues Dort is out of scope.

**L11.** `rzg` is assigned in the masthead and registered nowhere. The no-collision check is accurate ✓ — `packages/` and `records/` hold exactly `alx`, `cappadocian`, `desert`, `don`, `fix`, `gallic`, `hal`, `ijc`, `pahc`, `syr`, the ten codes listed. But neither `records/worlds.yaml` nor `records/WORLDS_REGISTRY_LOG.md` carries an `rzg` entry, and the masthead does not say where the code is to be registered.

**L12.** No `Open_Gaps_Tracking.md` exists for this world. `CLAUDE.md`: "Every known gap, open question, or review outcome belongs in that world's `Open_Gaps_Tracking.md` — never left to live only in a conversation thread. Entries are append-only and numbered." §7's ten open items — several of them binding on Doc_02 — live only inside Doc_01. Sibling worlds (Syriac, Alexandria) maintain the file and are cited by number from other documents.

**L13.** §2 describes the Prophezei as "a **daily** communal public exposition." It met on weekdays, roughly five days a week, not daily.

---

## Verified clean — checked directly against the primary file, no defect found

Listing these because the brief asked for character-exactness on every quotation and because several of these are the kind of claim that has failed in this project before.

**Constitution** (`CiC_L1_Constitution_V2_2.docx`, extracted from `word/document.xml`; internal text is V2.3 as the draft states ✓):
- Article 21, §4: "a meaningfully distinct pattern of formation emphasis, practice, authority structure, or ecological orientation within a single world, not merely a variation in detail" — **character-exact ✓**
- Article 21, §4: "never assigned to satisfy an architectural preference for plurality" — **character-exact ✓**
- Article 21, §4: "where strands exist, convergence across them is a test of a gravity's centrality" — **character-exact ✓**
- Article 22, §2: the elided quotation, with its ellipsis correctly placed — **character-exact ✓** (the §5 restatement is the problem, not this one; see M1)
- Article 29, §1: "where a formation world's reconstruction touches a tradition that continues into the present" — **character-exact ✓**

**Census** (`cic-website/data/world-census.json`, read as parsed JSON):
- VI.2 `"start": 1519, "end": 1650` ✓
- VI.2 `dateRationale` — "continues-cap," "matched nothing," "(Era 7 Freeze, Mark, 2026-08-02)" ✓, and `"living": true` ✓. The "Mark, 2026-08-02" attribution is anchored to a real, checkable field, not asserted — **this is the one place the draft attributes something to the project lead, and it does so correctly.**
- VI.2 `why` — "one of the best ordinary-life archives in Christian history" ✓; "the ordinary conduct of ordinary people" ✓
- VI.2 `sources` note on the Genevan Psalter — "The movement's ordinary devotional voice" ✓
- VI.2 `sources` — Kingdon, Lambert & Watt, trans. McDonald, Eerdmans 2000, vol. 1 only, 1542–44 ✓
- VI.2 `legacy` — the four descendant traditions (Scottish Kirk, Huguenots, Dutch Reformed, English Puritanism) ✓
- VI.2 `voices` — Beza and Dentière as characterized ✓
- VI.14 status string "Floor Question (register)" ✓
- VI.26 `why` fragment — character-exact, **but truncated in a way that changes its meaning; see H2**
- VI.26 "added at the Era 7 Freeze (Mark, 2026-08-02)" ✓
- Transmission edge `latin-pastoral-congregational-christianity` → `the-reformed-cities-zurich-and-geneva`, type "transmitted to" — quotation character-exact, both ellipses correctly placed ✓

**Corpus map** (`cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`):
- Heidelberg Catechism note, "a distinct pastoral/catechetical voice alongside Calvin's Geneva Catechism, from the Reformed tradition's German wing" — **character-exact ✓**
- Sixty-Seven Articles as its own row ✓; Second Helvetic Confession vendored ✓

**Dossier** (`world-build-docs/_cross-world/dossiers/the-reformed-cities-zurich-and-geneva_Source_Readiness_Dossier.md`):
- §5 "no figure overlap with Lutheran Wittenberg, the Jesuits, the Anabaptists, or Lollardy" — **character-exact ✓**
- §1 confirming the Kingdon/Eerdmans registers edition as copyrighted and unusable ✓
- §4 confirming no PD English Consensus Tigurinus located ✓

**Step 0 documents:**
- All five of the draft's numbered citations to this world's Step 0 §4 — items 2, 3, 4, 5, 6 — are **numerically correct ✓** (item 1 is the one that is missing; see H6)
- `World-Builds/Lutheran-Wittenberg/Step0_Movement_Scope_Confirmation.md` §2 A3 names Marburg ✓ and §4 item 3 binds its own Doc_01 to engage it ✓
- Lollardy's 1380–1520 window per Wittenberg Step 0 §3 B3 ✓
- "no Lutheran Wittenberg Doc_01 yet exists in this repository (only its own Step 0 draft is present)" — **verified true ✓**; all five sibling Era VII world folders contain a Step 0 and nothing else

**History, independently checked and correct:**
- Zwingli as *Leutpriester* at the Grossmünster preaching *lectio continua* through Matthew from 1 January 1519 ✓
- Bullinger 1531–1575 ✓; Zwingli killed at Kappel 11 October 1531 ✓; Luther's natural death 1546 ✓
- First and Second Zurich Disputations, January and October 1523 ✓; Sixty-Seven Articles at the first ✓
- Sausage Affair 1522 ✓; Bern Disputation 1528 ✓; Zurich Bible 1531 ✓; Prophezei from 1525 ✓
- Calvin at Geneva from 1536 ✓; expelled with Farel 1538 ✓; Strasbourg under Bucer 1538–41 ✓; recalled 1541 with the Ecclesiastical Ordinances ✓
- Consensus Tigurinus 1549 ✓; Bolsec 1551 ✓; Servetus 1553 ✓; Perrinist resolution 1555 ✓; Academy 1559 ✓; Genevan Psalter complete 1562 ✓; Heidelberg 1563 ✓; Second Helvetic 1566 ✓
- Geneva never a member of the Swiss Confederacy in this period — **correct and appropriately hedged ✓**
- Huguenot and Marian-exile refugee inflow to Geneva ✓
- **Giovanni Diodati and Theodore Tronchin as Geneva's delegates to Dort — correct ✓.** The draft's hedge on this claim is honestly worded and correctly placed. See H5 for why it is nonetheless a calibration finding.
- File-code no-collision list — **accurate ✓** against `packages/` and `records/`

---

## What would close this round

Not a list of edits — the two central judgments need re-argument, not repair.

1. **§4**: run World Separation Criteria on Zurich versus Geneva explicitly, establish the single-world premise on the evidence, and only then apply Article 21. If the separation test comes out ambiguous, escalate rather than choose the framing that preserves the world.
2. **§6 and §8**: withdraw the "already-made portfolio decision" framing, state what the census actually records (Dort named in VI.9 and VI.26; scope expressly left open by the Freeze; VI.26 deferred and awaiting the gate), and escalate the scope question to the project lead as a portfolio-level decision with named options. Add the Swiss cantonal delegation to Dort to the evidence being weighed.
3. **§8**: reassess escalation against all four categories. On my reading at least two apply (portfolio-level decision; unresolved tension), and the Step 0 sequencing problem is a third.
4. **Add a World Separation Criteria section** and answer Temporal Scope's two unanswered questions.
5. **Apply the five-level confidence vocabulary** across §2, §4, §5 and §6 — not one hedge, and not on the claim that turned out to be correct.
6. **Discharge Step 0 §4 item 1** in the body: Zwingli and Calvin never met, their ministries did not overlap, and the coherence rests on Bullinger's mediation.
7. Correct M2–M8, M13 and the Low findings; re-check §7 items 1 and 6 against the corpus map line by line before restating them.

---

*Filed per `cic-build-cycle`: review rounds exist as files, not claims. One procedural note — `CLAUDE.md` places adversarial-review rounds in `Ministry/`, while the established precedent this review was asked to follow (`World-Builds/Donatism/Review-Artifacts/`) places them beside the document under review. I have followed the precedent and the instruction. The inconsistency between the two is pre-existing and is not a finding against this draft, but it is worth a coach thread's attention.*
