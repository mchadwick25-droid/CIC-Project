# Step 0 — Movement-Scope Confirmation: Latin Pastoral-Congregational Christianity
## Round 1 Independent Adversarial Review

**Document reviewed:** `World-Builds/Latin-Pastoral-Congregational-Christianity/Step0_Movement_Scope_Confirmation.md` (DRAFT, dated 2026-09-01)
**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread; did not draft the document under review
**Governed by:** `cic-build-cycle` (CO-022) *Review* section — factual/historical accuracy of every substantive claim, internal consistency, source-attribution discipline, and whether the document does the job this stage requires

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

Five high-severity findings. The document is well-organized, honest in tone, and correct in its top-line conclusions (World #8 clears Section A; Tier 1 is the right tier). It is also correct on every verbatim quotation of the Step 0 Conclusion, on every specific claim it makes about the IJC precedent document, and on every corpus figure it draws from the corpus-map. Those are real strengths and they were checked, not assumed.

But the document fails on the one thing this stage most needs it to get right: **it asserts three independent verification claims that are false when actually checked, and one of them conceals a live cross-world boundary breach in an already-built world.** Two further high findings concern the document's own reasoning: its riskiest interpretive move (the A5 "routing" argument) is an over-reading achieved through an elision that removes the disqualifying clause, and its A1 restatement of the doctrinal floor is both prohibited by Article 4's own text and incomplete.

The pattern across the high findings is consistent and worth naming plainly: **the document is confident in exactly the places where it did the least checking.** "Confirmed distinct, on a live check," "No live overlap check needed," and "strengthened Hieronymian and Desert Monasticism's own B1 scores" are all stated flatly, and all three are wrong. This is CO-022 failure mode (b) — content described as checked that wasn't checked at the scope claimed — plus one fabricated prior finding.

The escalation assessment in §6 ("creates no unresolved cross-review tension of its own") cannot stand, because the check it rests on (H1) was wrong and the correct result of that check is a category-4 item.

---

## HIGH SEVERITY

### H1. The "live cross-check" against IJC is false, and it conceals a live boundary breach in a built world

**Where.** §3, B3, first bullet:

> "Live cross-check possible now that IJC is built: no material overlap found in a scan of IJC's own Doc_01/Doc_02 — Cyprian and Augustine (as pastoral, congregational figures) do not appear as IJC actors; Augustine appears in IJC's own source corpus only glancingly, via `Confessions` 9.7 (Ambrose's antiphonal singing, `ijc.source.augustine-confessions`), a single scene bearing on Ambrose's own liturgical innovation at Milan, not on Augustine's own pastoral office at Hippo — a different figure's story, not this world's. **Confirmed distinct, on a live check.**"

**What's wrong.** Three separate problems, in ascending order of seriousness.

1. *The scope of the check does not match the scope of the claim.* The check performed was "a scan of IJC's own Doc_01/Doc_02." The claim made is about "IJC's own source corpus" — a different and much larger object. IJC's source corpus is `records/ijc/` plus `cic/corpus-map/imperial-juridical-christianity.yaml` plus `Source_Registry.md`. None of those was scanned, on the evidence of what the document reports.

2. *The claim is false against the corpus map.* `cic/corpus-map/imperial-juridical-christianity.yaml` assigns **two** Augustine works to imperial-juridical-christianity, neither of them *Confessions* 9.7: *City of God* (`div1 4 — City of God, esp. Books I-V and XIX`, role `tradition`, confidence `provisional`) and *The Correction of the Donatists* (*De Correctione Donatistarum*, Letter 185, role `tradition`, confidence `provisional`). The second of these is also assigned to this world in `latin-pastoral-congregational-christianity.yaml`, whose note says so explicitly: "Also assigned to imperial-juridical-christianity below." The document cites that same corpus-map file approvingly four times elsewhere. A Letter-185 double-placement across exactly the #6/#8 boundary the bullet is adjudicating is the single most relevant fact in the file, and the bullet reports its absence.

3. *The claim is false against IJC's own built records, and what it misses is a boundary breach.* `records/ijc/source/ijc.source.augustine-confessions.md` scopes itself narrowly — `work:` reads "Confessions, Book 9 ch. 7 ONLY" — and carries this binding note:

   > "BOUNDARY (binding, from the legacy Registry rows 8/26): ... Augustine's formation, theology, and the rest of the Confessions belong to the Latin Pastoral-Congregational world (World #8, not yet built); do not extend this license."

   Four quote records cite that source. Two are 9.7 (`ijc.quote.hymns-and-psalms-should-be-sung`, `ijc.quote.augustine-vigil-hymns`). The other two are not:

   - `ijc.quote.take-up-and-read` — locus `Confessions VIII.12`, the *tolle lege* conversion scene. `evidentiary_weight: load-bearing`, `retrieval.tier: 1`, canon cells `F2-P` and `C-P`.
   - `ijc.quote.i-scorned-to-be-a-little-one` — locus `Confessions III.5`, Augustine on being repelled by the plainness of scripture. `evidentiary_weight: load-bearing`, `retrieval.tier: 1`, canon cell `F2-P`.

   Both are Augustine's own formation, in his own voice, held as load-bearing tier-1 retrieval material inside a built world — i.e. precisely the license IJC's own source record says must not be extended, and precisely the material IJC's `Source_Registry.md` row 26 marks `Excluded / Named Comparandum` as belonging "natively to World #8." `records/ijc/world_core/ijc.core.imperial-juridical.md` still asserts "only Confessions 9.7," which is no longer true of its own world.

**Why it matters.** Three ways.

- The B3 finding "Confirmed distinct, on a live check" is unearned. The live check, actually run, returns the opposite: there is real, load-bearing, disclosed-as-out-of-bounds World #8 material sitting inside World #6's built record set.
- Step 0 is the natural and cheapest place to catch this. Once Doc_01 and Doc_02 are drafted on the premise that the #6/#8 line is clean, the cost of finding it rises.
- §6 states the document "creates no unresolved cross-review tension of its own" and that "No standing escalation category applies." A built world holding load-bearing material against its own declared boundary with the world now being built is a contradiction between two documents each claiming to govern the same territory — CO-022 escalation category 4 ("a contradiction between two already-cleared master documents, or a finding that cuts against an earlier decision"). §6's conclusion is not necessarily wrong once the finding is properly stated, but it currently rests on a check that returned the wrong answer, so it cannot be relied on as written.

**Fix.** Replace the bullet with what the check actually returns, at the scope actually checked, and name each object checked by path. State: (a) Cyprian appears nowhere in IJC's Doc_01 or Doc_02 — that part is true and was verified here; (b) Augustine appears in IJC's corpus-map at *City of God* and *De Correctione Donatistarum* (both `provisional`), and the latter is already double-placed with this world; (c) IJC's built records hold two load-bearing Augustine-formation quotes (`Confessions` VIII.12 and III.5) against IJC's own written boundary note. Then either escalate (c) under category 4, or state explicitly why it does not qualify — but do not leave §6 resting on "no material overlap found."

---

### H2. "Jerome does not appear in this world's own corpus-map assignment" is false, on the boundary the document calls its most load-bearing

**Where.** §3, B3, second bullet:

> "This is the single most load-bearing differentiation finding in this world's own history, since it *is* the reason this world has its current shape. No live overlap check needed beyond noting it: Jerome does not appear in this world's own corpus-map assignment."

**What's wrong.** `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` contains this row:

> `- work: 'Letters of St. Augustin: the Augustine-Jerome correspondence'`
> `  locus: div3 letters XXVIII, XXXIX, XL, LXVII, LXVIII, LXXI, LXXII, LXXIII, LXXV, LXXXI, LXXXII, CXXIII, CLXVI, CLXVII, CLXXII, CXCV, CCII (17 letters, ~52,892 words)`

with a note reading, in part: "`tradition` for BOTH entries deliberately - the exchange contains Jerome's own letters, which are the Hieronymian world's voice, and Augustine's, which are the Latin pastoral world's. A two-sided correspondence has voice on both sides. It is also the largest single thing in this volume after the Confessions."

The mirror row sits in `cic/corpus-map/hieronymian-ascetic-literary.yaml`, which additionally holds *City of God* XVIII.42–44 (role `context`) as "the other side of this entry's central argument," naming Jerome directly.

So: Jerome is in this world's corpus-map assignment; the assignment is a deliberate, reasoned, already-modeled double-placement at the #8/#9 boundary; and it is the second-largest item in npnf101.

**Compounding it:** Hieronymian's built Doc_01 contains an explicit, unmet request addressed to this world. `hal_Doc_01_World_Identification_Boundaries_Orientation.md` §8.1:

> "*(This world's own evidence, not World #8's content, grounds this argument — World #8 has not been built and its documents have not been read.)*"

and closes:

> "...but this document limits itself to establishing what is true of *this* world, and leaves the comparison's other half to World #8's own, independently-sourced construction."

That section also records that an earlier hal draft was **corrected for a methodology violation** — asserting specific facts about Augustine without an independent basis. So the #8/#9 boundary is not only live, it has an on-record failure history, and a built world is formally waiting on World #8 to supply its half.

**Why it matters.** The document identifies this boundary as "the single most load-bearing differentiation finding in this world's own history" and then, on a false premise, declares no check needed. Doc_02's Source Registry will inherit a 17-letter, ~53k-word body that two worlds both claim as `tradition`, with no Step 0 flag telling it so — while §4 item 2 goes to some trouble to install exactly that kind of flag for World #4.

**Fix.** Correct the factual claim. Add a §4 carry-forward binding Doc_01/Doc_02 on the #8/#9 boundary: the Augustine–Jerome correspondence's deliberate two-world `tradition` assignment must be honored, not silently claimed as exclusively Native; and hal Doc_01 §8.1's outstanding request (that World #8 supply the other half of the authority-mode contrast from its own sources) should be logged as a specific Doc_01 obligation.

---

### H3. Fabricated citation: a prior Step 0 finding that does not exist

**Where.** §3, B1, fourth bullet:

> "Pontius's *Life of Cyprian* and Cyprian's own letters together supply the same "formation narrative source" category (Framework Part II) that strengthened Hieronymian and Desert Monasticism's own B1 scores."

**What's wrong.** The category is real; the citation around it is not.

- "Formation Narrative Sources" is a genuine Construction Framework term — but it is a **Step 2 / Doc_02** activity, not a Step 0 Section B criterion. In CF V7.4, "Assess Formation Narrative Sources" appears in the activity list under "Step 2 — Source Ecology and Source Registry," and the evaluation guidance ("For each formation narrative source evaluate: authorship and date, proximity to the events or persons described, genre conventions...") sits in Part II — Evidence Development, which is Step 2's part, not Step 0's. Step 0 is described in CF V7.4 at the top of the step sequence and produces a seed list only.
- **Neither Hieronymian nor Desert Monasticism has a B1 score.** Neither world has a per-world Step 0 confirmation document — the only two files of this type in the entire repository are `World-Builds/Imperial-Juridical-Christianity/Step0_Movement_Scope_Confirmation.md` and the document under review. A repository-wide search for Section-B "B1" reasoning returns exactly those two files (all other `B1` hits are Facilitation Brief section headings, an unrelated business-plan item, and one Atlas spec line that explicitly says "A signal, not a B1 score"). The portfolio-level Step 0 Conclusion records no per-criterion scores for any of the nine selected worlds.
- The two places "formation narrative source" is genuinely used for these worlds confirm the misattribution: `records/hal/source/hal.source.jerome-vita-hilarionis.md` and `...vita-malchi.md` both give `discovery_channel: "prior HAL build Doc_02 section 5 (formation narrative sources)"` — Doc_02, not Step 0.

**Why it matters.** This is a bare fabrication of a prior project finding, offered as corroboration in the criterion the document rates most strongly ("arguably the strongest of any world confirmed so far"). CO-022 exists in its current form partly because of this exact failure class; the Step 0 Conclusion itself adopted a "Provenance-accuracy discipline" rule in direct response to one instance of it: "A finding may not be described as 'confirmed against' a source, or as a pre-existing mechanism rather than a new proposal, unless that is actually verifiable in the named source."

**Fix.** Delete the claim about B1 scores. If the underlying point is worth keeping — that Pontius's *Life* is a formation-narrative source and therefore a Doc_02 asset — say that, cite CF V7.4's Step 2 activity list as the source of the category, and drop the comparison to other worlds' nonexistent scores.

---

### H4. The A5 "routing" ground for the century-gap question is an over-reading, achieved through a load-bearing elision

**Where.** §2, "The century-gap question, honestly held open," ground 2:

> "2. **A5 itself routes this exact shape of question downstream, not to Section A.** *"Where a movement contains multiple internal strands under Article 21, eligibility is assessed at the world level against its established strands as a whole... never strand-by-strand in a way that lets one divergent internal strand exclude an otherwise-eligible world."*"

**What's wrong.** Four things, and they compound.

1. **The ellipsis removes the clause that disqualifies the argument.** A5's full sentence reads: "eligibility is assessed at the world level against its established strands as a whole — **including whichever strand(s) meet the floor** — never strand-by-strand..." The elided clause fixes A5's subject as *the doctrinal floor*. With it restored, A5 is a rule about how Article 4 eligibility is assessed when strands exist. Without it, A5 reads as a general strand-handling rule that could plausibly reach an Article 3 coherence question. The document elides exactly the words that make it not reach.

2. **The document has already conceded the point that defeats its own ground 2.** One paragraph earlier, in ground 1: "There is no confessional content in either phase that fails Article 4; the open question is about historical coherence (Article 3), not doctrinal floor (Article 4)." If the open question is not about the floor, and A5's strand clause is about the floor, then A5 is not on point. Grounds 1 and 2 are in tension with each other as written.

3. **A5 does not "route" anything.** Nothing in A5's text mentions Step 1, Doc_01, deferral, or downstream work. It is an instruction about how to assess eligibility, not about where to send an unanswered question. "Routes this exact shape of question downstream" is the document's characterization, not the text's content, and it is presented as though it were the text's content — italicized quotation immediately following the bolded claim.

4. **The Construction Framework half of the ground is correctly quoted but does different work.** "Strand is a finding, never a presupposed schema... This determination is made at Step 1" is verbatim from CF V7.4 (the ellipsis elides only "Not every formation world contains internal strands"), and it does establish that *strand determination* is Step 1's job. It does not establish anything about Article 3 historical coherence, which is the actual open question.

**Why it matters — and why this specific finding is the sharpest one in the document's own terms.** IJC's Step 0 Round 1 review found and removed, from IJC's first draft, "an invented, non-textual rationale for excluding A2 outright," and IJC's cleared text now says of that episode: "this world's build did not initially consult it and instead reached for an invented rationale ... which was a drafting error in this document's first pass." This document reaches for a non-textual rationale in the same slot — the Section A subtest treatment for its hardest case — while §5 asserts: "the pattern held up **without needing invention**. No structural gap found in Section A or Section B's own text for this world's use case." That claim is falsified by the document's own §2.

**The honest argument was available and is stronger.** Nothing in Section A tests Article 3 historical coherence. A1 is the floor; A2 is pre-Nicene continuity to the floor; A3 is contemporary interpretive fidelity to the floor; A4 is a bounded waiver *of the floor*; A5 governs how the floor interacts with Articles 20/21/23. The Procedure's own screening step is "Test each candidate against A1 (and A2 or A3 as applicable)" — nothing else. Section B's five criteria are Sourcing, Ecology, Uniqueness, User Needs, Scale — no coherence test. **The Article 3 question is simply outside Step 0's instrument.** That reading needs no routing rule, no elision, and no interpretive stretch, and it reaches the same conclusion the document wants.

**Fix.** Drop ground 2's A5 argument. Replace it with the plain reading above. Keep the CF "Strand is a finding" quotation, but attach it to the narrower and true claim it actually supports: *if* the Cyprian/Augustine relationship turns out to be an Article 21 strand question, that determination is Step 1's, per CF. Restore the elided clause wherever A5 is quoted. Then revise §5 finding 1 and §6, both of which currently describe this reasoning as textual application rather than interpretation.

---

### H5. A1 restates the doctrinal floor independently, which Article 4 forbids, and drops one of its five commitments

**Where.** §2, A1:

> "Article 4's floor tests whether a movement's own confession affirms, in its plain historical sense, the content drawn from the Nicene-Constantinopolitan Creed (381) — full divinity and consubstantiality of Christ, true humanity, the Passion/resurrection/ascension/return, and the Spirit as Lord and giver of life, worshiped and glorified with the Father and Son."

**What's wrong.** Two things, and the first is a governance point, not a nitpick.

1. **Article 4 expressly forbids this.** `CiC_L1_Constitution_V2_2.docx`, "On the Scope of 'Movement'": "This is the authoritative statement of the floor's content; the Construction Framework's Step 0 operationalizes it procedurally and **must not restate it independently** — where the two differ, this Article governs." The Step 0 Methodology complies: "The floor is stated in Article 4 of the Constitution (Movement-Scope scoping section) and is not restated here." This document restates it — in a document whose entire purpose is confirming a world against Article 4.

2. **The restatement is incomplete.** Article 4's list is five items:
   - "One God, the Father, the Almighty, maker of heaven and earth, of all that is, seen and unseen."
   - Christ as only Son, eternally begotten, "of one Being with the Father."
   - Christ as "truly human."
   - Death under Pilate, burial, bodily resurrection on the third day, ascension, return in glory to judge.
   - "The Holy Spirit as Lord and giver of life, worshiped and glorified together with the Father and the Son."

   The document lists four. **The omitted item is the first** — the one God, maker of all that is, seen and unseen. §2's A4 then refers to "Article 4's five commitments," so the document knows the count is five while enumerating four.

**Why it matters.** The dropped commitment is not a rounding error for *this* world specifically. The first commitment is the anti-dualist clause — the one the Step 0 Conclusion itself uses to exclude Manichaeism ("A dualist cosmology of two eternal, co-original principles, directly denying 'one God... maker of... all that is'"). Augustine's own anti-Manichaean corpus is the whole of npnf104's first half and a substantial share of what this build's corpus-map assigns to this world; Augustine was himself a Manichaean auditor for nine years. A1 for this world is the one place in the portfolio where that commitment does the most visible work, and it is the one the restatement drops.

Note also that this defect is inherited verbatim from IJC's Step 0 §2 A1, which uses the identical sentence. That does not excuse it — it means the second document in this pattern has now propagated it, and per CO-022's naming-and-term-propagation rule, a fix should go to both.

**Fix.** Do not restate the floor. Cite Article 4 and, if a summary is genuinely needed for readability, quote Article 4's five bullets verbatim rather than paraphrasing them, and flag the IJC instance for the same correction.

---

## MEDIUM SEVERITY

### M1. "Ecclesiastes-style subordinationist" — A2's rival list is misquoted, and the substitute is not a real category

**Where.** §2, A2: "...rather than divergence toward a rival current (Gnostic, Marcionite, **Ecclesiastes-style subordinationist**, or similar)?"

**What's wrong.** A2's actual text reads: "rival movements (Gnostic, Marcionite, **Ebionite**, and similar groups) whose beliefs diverged from it." "Ecclesiastes" is a book of the Hebrew Bible; there is no Ecclesiastes-style subordinationist current, in this methodology or in the scholarship it tracks. This is a corruption of "Ebionite," and it occurs inside the sentence that states the test the section is applying.

**Confirming it is unique to this document:** IJC's Step 0 §2 renders the same list correctly ("Gnostic, Marcionite, Ebionite, or similar"), and so does the parallel Donatism Step 0 draft on the sibling branch.

**Why it matters.** A2 is the operative subtest for half of this world. Getting its enumerated rival currents wrong — and inventing one — in the sentence that frames the test undermines the section's claim to be applying the text as written. It is also, on its face, the kind of error that reads as generated rather than checked.

**Fix.** "Ebionite."

### M2. Article 20's affirmative duty is flagged to the wrong document, with a false "per the Framework's own text" grounding

**Where.** §2, A5: "Article 20's affirmative duty (marginalized voices within an included movement) and Article 21's strand determination are both explicitly Step 1 work per the Framework's own text — flagged forward to Doc_01, not resolved here."

**What's wrong.** In CF V7.4, "Name the Affirmative Duty: whose voices does the source record structurally suppress and why? (Article 20)" appears in the activity list under **"Step 2 — Source Ecology and Source Registry,"** not Step 1. Step 1's activity list covers boundaries, strand determination, and preliminary forces. Only the Article 21 half of the sentence is Step-1 grounded; the Article 20 half is Step 2 / Doc_02.

This is also internally inconsistent: §4 item 3 correctly binds the source-skew disclosure to Doc_02, which is the same body of work.

**Why it matters.** §4's whole rationale is that obligations be "checkable rather than only asserted." An obligation filed against the wrong document is not checkable at the right point, and "per the Framework's own text" is a provenance claim the text does not support.

**Fix.** Split the sentence: Article 21 strand determination → Doc_01 (CF Step 1); Article 20 affirmative duty → Doc_02 (CF Step 2), merged with §4 item 3.

### M3. §5's process finding ignores IJC's still-open Finding 3 and the Methodology's own "never a per-world process" text

**Where.** §5, item 1: "This is the second per-world Step 0 confirmation run against the codified Methodology text (after World #6/IJC), and the pattern held up without needing invention. **No structural gap found in Section A or Section B's own text for this world's use case**, beyond the pre-existing, already-logged Article 3 gap..."

**What's wrong.** Three omissions.

1. The Methodology states, in its own Section B scope paragraph: "this is a phase-level process, run once when the project opens a new release phase, **never a per-world process**." Its Procedure heading likewise reads "Procedure (phase-level, run once per new release phase)," and its opening line says Step 0 is "run once per release phase, before any individual world's Step 1 begins." IJC's §0 confronted this directly and gave a reason the per-world pass was nonetheless warranted (the codified Methodology postdated the portfolio review). This document's §0 does not engage the text at all — it simply asserts the per-world job is "narrow" and cites IJC as precedent.

2. **IJC's §5 Finding 3 is a still-open Methodology gap and it is not reported on.** IJC logged: "No explicit Step 0 per-world output template exists... the Methodology assumes Step 0 happens once, before any specific world is chosen, not as a per-world gate re-run later... **Recommend naming this pattern (or a revised one) explicitly if per-world Step 0 confirmations are expected to recur for future worlds selected from an existing seed list rather than freshly surveyed.**" They have now recurred — twice more, counting the Donatism draft. Nothing in the repository indicates System Hub acted on the recommendation. A second instance of the pattern is precisely the occasion to report that the recommendation is outstanding, and instead §5 reports no gap.

3. **IJC's §5 Finding 2 goes unmentioned, and it is materially pointed at this world.** IJC logged that the Step 0 Conclusion's "Criterion 2" (the person-defined-movement test) "has no home in the formally codified Section A," and disposed of it for World #6 explicitly ("would not exclude a multi-figure, century-spanning institutional world like this one even if applied"). The Step 0 Conclusion, which this document treats as binding grounding, says Criterion 2 is now part of Section A screening: "Section A screening now applies a second, separate test alongside the doctrinal floor: whether a movement's whole authority claim rests on a small number of named individuals' personal revelation or teaching, rather than a broader communal interpretive tradition. A movement can clear the doctrinal floor and still be excluded on this second ground alone." World #8's portfolio entry is two named individuals. The answer is almost certainly that it clears (episcopal office is a communal institutional tradition, not personal revelation) — but this document's §2 walks A1–A5 and declares "World #8 clears Section A" without addressing the one screening ground its own governing conclusion says now sits alongside them.

**Fix.** In §0, engage the "never a per-world process" text and state why the pass is nonetheless run (IJC's §0 is a usable model). In §5, report IJC's Finding 3 as still open and note this is now the second-or-third recurrence. Add a short A-section paragraph disposing of Criterion 2 for World #8 on the record, as IJC did for World #6.

### M4. The corpus-map characterization of the World #4 shared-inheritance rows is wrong for two of the three named works

**Where.** §3, B3, third bullet ("per the corpus-map's own provisional rows (the Council of Carthage under Cyprian on rebaptism; the anonymous anti-Novatianist and anti-rebaptism treatises)") and §4 item 2 ("Doc_02's Source Registry must mark the shared-inheritance sources (the Council of Carthage under Cyprian; the anonymous anti-rebaptism and anti-Novatianist treatises) **with the same double-placement honesty the corpus-map already models**").

**What's wrong.** Checking each named row in `cic/corpus-map/latin-pastoral-congregational-christianity.yaml`:

- **The Acts of the Council of Carthage under Cyprian (256).** Correct. `confidence: provisional`, and the note says exactly what the document claims: "Donatism is included as shared ancestry rather than heresiology: the Donatists claimed this council's baptismal doctrine as their patrimony, so it is tradition claimed by both sides... Provisional on that double placement."
- **Anonymous Treatise Against the Heretic Novatian.** The double placement is with **novatianism**, not donatism: "Assigned to novatianism as the movement it argues against, and to the Latin pastoral entry as its likely milieu."
- **Anonymous Treatise on Re-baptism (*De Rebaptismate*).** The corpus map **explicitly declines** a donatism assignment: "Its bearing on donatism's prehistory is noted but **not assigned** - same antecedent question as the Cyprian flags."

So the corpus map does not "already model" Donatism double-placement for two of the three works; for one it models a different double-placement, and for the other it models a deliberate refusal.

**Why it matters.** §4 item 2 instructs Doc_02 to follow a model that does not exist for two-thirds of the works it names. Doc_02 will either follow the instruction and introduce assignments the corpus map deliberately withheld, or notice the mismatch and have to re-derive the boundary itself — which is what §4 was supposed to prevent.

**Fix.** Name the Council of Carthage row as the double-placement precedent. Describe the two anonymous treatises accurately: one is double-placed to novatianism, the other has a *noted but unassigned* Donatism bearing that Doc_02 should either resolve or preserve as unassigned, with reasons.

### M5. Optatus is omitted entirely — the most boundary-relevant row in the asset the document calls "unusually mature"

**Where.** §3, B1, third bullet describes the corpus-map as "mapping every relevant work to its vendored file and locus, with confidence ratings and cross-world boundary notes already reasoned through for the shared Cyprian/Donatism material," and §4 item 4 makes it "required input to Doc_02's own Source Registry work."

**What's wrong.** The corpus-map's single most consequential unresolved row is never mentioned:

> `- work: Against the Donatists (De Schismate Donatistarum, Books I-VII)`
> `  author: optatus` ... `role: tradition` ... `confidence: provisional`
> note: "Optatus, Bishop of Milevis... the North African Catholic voice answering Parmenian, c. 366-393. Tradition for the Catholic side of the schism; **this entry** (Carthage / Hippo Regius, c. 240s-430) is the census's home for that tradition. Provisional only because the entry choice is inferred from region and date - Mark may prefer another Latin home for a Numidian polemicist."

A seven-book anti-Donatist polemic is currently assigned to **this world**, as `tradition`, on a provisional basis its own note flags as inferred. `cic/texts/README.md` describes the same file as "THE primary source for Donatism, one of the census's three 'Selected - Not Yet Built' worlds" and "THE single most strategically valuable item identified" in its vendoring survey.

**Why it matters.** The document's load-bearing World #4 line is that this world holds "the ordinary pastor navigating persecution" and never "the schism-crisis angle." Optatus is nothing but the schism-crisis angle, and it is currently inside this world's assignment. This is the concrete instance of the boundary §2 and §4 spend the most words on, and it is the one the document does not name. The corpus-map row also carries an open question addressed to the project lead ("Mark may prefer another Latin home"), which is exactly the sort of thing a Step 0 carry-forward exists to surface.

**Fix.** Add Optatus to §3 B3's World #4 bullet and to §4 item 2 as a specific, named, currently-provisional assignment Doc_02 must resolve — noting that the corpus-map itself flags the placement as inferred and open.

### M6. §0 and §3/§4 contradict each other on whether IJC is the only prior instance of this pattern

**Where.** §0: IJC is "**the only other world so far** to run this per-world confirmation pattern against the formal Methodology text." §3 B3 and §4 item 2: Donatism "is, per this session's own discovery, under active parallel construction on a sibling branch not visible to this working tree."

**What's wrong.** The Donatism build was verified during this review and the claim about it is true — `World-Builds/Donatism/` exists on `origin/claude/record-native-world-build-v2-e2s0dt`. But the entire contents of that directory is **one file**: `Step0_Movement_Scope_Confirmation.md`, dated 2026-09-01, in this same format, following the same IJC precedent (its §0 cites `World-Builds/Imperial-Juridical-Christianity/Step0_Movement_Scope_Confirmation.md` by path as "the first per-world confirmation run against the formally codified Section A/B text").

So the discovery §3 reports *is* the discovery of a third instance of the pattern — which §0 denies in the same document.

**Why it matters.** §0's "only other world" claim is load-bearing for the document's framing of itself as second-in-a-series, and §5 item 1 repeats it ("the second per-world Step 0 confirmation"). If the session knew about the Donatism build well enough to cite it twice, §0 is stating something the document elsewhere knows to be false.

**Fix.** Reconcile the two. Either §0 says "the only other world in this working tree, with a third (Donatism) in parallel on `…-e2s0dt`," or §3/§4 explain why the Donatism draft does not count as an instance.

### M7. "No live cross-document check is possible" for World #4 is an unverified impossibility claim, and CO-022 specifically forbids resting on one

**Where.** §2, A5: "so no live cross-document check is possible; the boundary is logged here as binding on Doc_01/Doc_02, to be reconciled against Donatism's own build when the two branches are eventually merged." Repeated in §3 B3 and §4 item 2.

**What's wrong.** The branch is fetched into this repository and its contents are readable without merging or checking out — `git show origin/claude/record-native-world-build-v2-e2s0dt:World-Builds/Donatism/Step0_Movement_Scope_Confirmation.md` returns the file. "Not visible to this working tree" is true of the working directory and false of the repository.

CO-022's *Review* section: "**A review finding is never dismissed as a tooling or environment artifact — a stale cache, a mount discrepancy, and so on — without independent re-verification that actually confirms the dismissal.**" The same standard applies to a builder dismissing a check as impossible for an environment reason.

**What the check actually returns**, having been run here: the Donatism Step 0's own §3 says of World #8, "Not built yet, so no live cross-document check was possible; the boundary is logged here as binding on Doc_01," and its §4 item 4 says World #8 "is not yet built and cannot itself hold the line from its side." Both documents were drafted on 2026-09-01. **Two same-day drafts are each excusing the same check on the other's absence.** That is a closable gap, and closing it is cheap.

There is also a substantive result worth having: the Donatism Step 0's A5 finding states that "once World #8 is built — Donatism will symmetrically need to be named as *its* internal opponent." This document's A5 discusses the #4 boundary but never states the reciprocal Article 23 obligation — that Donatism must appear *inside* World #8's own reconstruction as its named opponent, which is what A5's Article 23 clause actually requires and what Doc_02 will need.

**Fix.** Read the sibling-branch Donatism Step 0, cite it by branch and path, and state what the cross-check returned. Replace "no live cross-document check is possible" with an accurate statement of what was and wasn't checkable. Add the Article 23 reciprocal obligation (Donatism as this world's named internal opponent within its own reconstruction) to A5 and to §4.

### M8. No reciprocal World #6 obligation is carried forward, despite IJC's Step 0 explicitly asking for one

**Where.** §4 carries five obligations forward. None concerns World #6.

**What's wrong.** IJC's Step 0 §4 item 3 reads: "**Distinctness from World #8 (binding on Doc_01).** The authority-structure/state-power boundary named in §3 above must be stated explicitly in Doc_01, **since World #8 is not yet built and cannot itself hold the line from its side.**" IJC's Doc_01 §98 then states the boundary and cites this world's Step 0 by name as the reaffirmation. The condition IJC named ("not yet built") has now changed; World #8 is being built and can hold the line from its side. The same is true of hal Doc_01 §8.1 (see H2).

Two built worlds have logged, on the record, that they are holding a boundary unilaterally pending this world's construction. §4 is the correct and only place in Step 0 to pick those up, and it does not.

**Fix.** Add a §4 item binding Doc_01 to state the #6 authority-mode boundary from this world's side, and to supply the other half of hal Doc_01 §8.1's authority-mode contrast from this world's own sources — both citing the built documents that requested it.

### M9. "Cyprian's own theological vocabulary is a direct forerunner of the Latin tradition Augustine inherits" conflicts with the document's own governing sources

**Where.** §2, A2: "His own theological vocabulary is a direct forerunner of the Latin tradition Augustine inherits and writes within..."

**What's wrong.** The Step 0 Conclusion — which this document treats as binding grounding — assigns that role to Tertullian, not Cyprian: "**Tertullian's own voice**, distinct from Cyprian. With Cyprian now anchoring world #8 alongside Augustine, Tertullian — **credited with forging much of the Latin theological vocabulary the whole Western tradition depends on** — no longer has a clear home. A dropped voice, not just a dropped 'world.'"

The corpus-map the document relies on says the same thing at the level of individual works: *De Bono Patientiae* "reworks Tertullian's *De Patientia*"; *De Dominica Oratione* is "dependent on Tertullian's *De Oratione*"; *De Habitu Virginum* follows "Tertullian's dress treatises"; *Quod Idola Dii Non Sint* "compiles Tertullian and Minucius Felix." Cyprian is the transmitter and pastoral applier of that vocabulary, and a self-described reader of Tertullian; he is not its forger.

**Compounding it:** the Tertullian dropped-voice item is a Step 0 Conclusion disclosure *about World #8 specifically* — it exists because of this world's shape — and §4 does not carry it forward among its five obligations, though it carries forward the Primary-gravity-first item from the same list.

**Why it matters.** A2 is meant to establish continuity to the proto-orthodox strand, and Cyprian's dependence on Tertullian is a *better* continuity argument than the one made. The overstatement buys nothing and contradicts the governing document.

**Fix.** Rephrase to Cyprian's actual position (working within, and transmitting, the Latin theological vocabulary Tertullian forged), and add the Tertullian dropped-voice disclosure to §4 as an obligation on Doc_01/Doc_02 — it is a Step 0 Conclusion item naming a gap this world's own shape created.

### M10. B2 compresses three separate phases of Cyprian's episcopate into one

**Where.** §3, B2: "...and Cyprian's letters written from hiding during active persecution to a frightened, plague-stricken, schism-torn congregation are direct, first-person, lived-community evidence..."

**What's wrong.** These are three different moments, and only the first is "from hiding":

- Cyprian withdrew during the Decian persecution, c. early 250 to spring 251. The letters from hiding address the persecution, the lapsed, and the confessors' libelli.
- The Felicissimus schism and the Novatianist schism break out in 251, after his return, and are handled from Carthage.
- The Carthaginian plague and *De Mortalitate* belong to c. 252–253, also after his return.

As written, letters from hiding are addressed to a congregation that is simultaneously persecuted, plague-stricken, and schism-torn — a state of affairs that did not obtain at the time of the letters described.

**Why it matters.** B2's argument is that this world offers unusually direct lived-community evidence. That argument is correct and survives the correction easily — the three phases together are richer evidence than the compressed version. But the compressed version is a factual error in a document that will be cited downstream for its evidentiary characterizations.

**Fix.** Separate them: letters from hiding (250–251, persecution and the lapsed); post-return correspondence and *De Lapsis* (251, penitential discipline and schism); *De Mortalitate* and the plague (c. 252–253).

---

## LOW SEVERITY

### L1. "the complete NPNF Series I set (8 volumes, all vendored: `npnf101`–`npnf108`)"
NPNF Series I is fourteen volumes; volumes 1–8 are the Augustine set and 9–14 are Chrysostom. What is vendored, and what the document means, is the complete **Augustine** portion of NPNF1. As written the claim is wrong. (`cic/texts/` also holds `npnf109_chrysostom-...`, so the distinction is live in this repository.) — *Fix: "the complete Augustine set within NPNF Series I (volumes 1–8...)."*

### L2. "**Cyprian**: the complete surviving corpus — some 82 letters"
The figure matches the corpus map, but that entry's own note qualifies it in a way that bears directly on B1's first-person-voice argument: "the corpus embeds letters by others (Cornelius, the Roman clergy, Firmilian of Caesarea, the confessors) under Cyprian's name - CCEL attributes the whole body to cyprian." Two further omissions in the same bullet: "the acts of his own **councils** on rebaptism" is plural, but only the September 256 sententiae are vendored (the 255 and spring-256 councils are not extant as acts); and the corpus map's "Treatises attributed to Cyprian on questionable authority" body — four pseudo-Cyprianic pieces, two commonly given to Novatian — goes unmentioned in a B1 rated "exceptionally strong." — *Fix: note the embedded non-Cyprianic letters, singularize the council acts, and mention the pseudo-Cyprianic body as a named qualification rather than leaving B1 unqualified.*

### L3. B4's "Cyprian's and Augustine's own honesty about doubt"
Doubt is a *Confessions* register; Cyprian is not a witness to it, and the joint attribution is loose. Similarly, *De Lapsis* is a reckoning with lapsed laity and with clergy readmitting them too readily — "a church that failed under pressure" is a defensible gloss but stretches what the treatise is about. — *Fix: attribute doubt to Augustine specifically; characterize De Lapsis as a reckoning with mass lay lapse and contested penitential discipline.*

### L4. §6 repeats the self-characterization IJC's Round 2 review removed from IJC
§6: "applies existing Section A/A5 text to this specific case **rather than adding a new rule or waiving a stated requirement**, the same class of ordinary case-application judgment IJC's own Step 0 confirmation made." IJC's §6 records that its first revision "claimed the A1/A2 resolution was 'a direct application... rather than a novel methodology interpretation,' which contradicted §5 Finding 1's own, more honest characterization," and that the language was **removed, not just re-checked**. IJC's cleared text now says plainly: "this document's A1/A2 resolution is not a pure mechanical lookup." This document claims IJC as precedent while reproducing the framing IJC's review deleted. IJC's Round 3 also added a disclosure this document lacks — that its §5 recommendation, if adopted, would convert its own reading into the Methodology's codified precedent. — *Fix: adopt IJC's cleared framing (interpretation happened; it does not rise to a governance decision), which becomes straightforward once H4 is applied.*

### L5. "on any account of the Latin theological tradition, among the two or three most consequential expositors"
An unfalsifiable universal claim doing argumentative work in a section that should rest on the movement's confession, not on consensus rankings. A1 clears on *De Trinitate*, the Enchiridion, and the creedal catechesis alone; the ranking adds nothing testable. — *Fix: cut, or attribute to a named scholarly source.*

---

## COSMETIC

### C1. Quote-mark normalization in the §2 Article 3 quotation
The Step 0 Conclusion has curly double quotes around **"sufficient historical coherence"**; the document renders them as straight single quotes. Everything else in that quotation is exact, character for character. Trivial, but the passage is presented as verbatim and the surrounding quotation marks are the document's own.

### C2. "Construction Framework V7.4's Step 0 stub"
IJC's header calls the same document "Construction Framework V7.4 DRAFT's Step 0 stub"; the version status should be consistent across the two documents. "Stub" also undersells it slightly — CF V7.4's Step 0 section is a full paragraph with a pointer to the Methodology, plus the operative line "Nothing in Step 0 performs Step 1's own boundary-determination work," which is a text the document could usefully have cited in §2 (see H4's suggested replacement argument).

---

## Checked and found clean — stated explicitly, not omitted

The following were verified directly rather than assumed, and no defect was found in any of them.

**Verbatim quotation accuracy (checked programmatically, character by character, against the extracted source text):**
- §1's block quotation of the Step 0 Conclusion's World #8 entry is **exact**. Diffed against the source line; zero differences.
- §2's quotation of Section A's framing paragraph ("This section is the procedural home... not a scored criterion") is exact.
- §2's quotation of the Step 0 Conclusion's "Constitutional ambiguity flagged, not resolved" passage is exact but for C1's quote marks.
- §2's quotation of CF V7.4's "Strand is a finding, never a presupposed schema... This determination is made at Step 1" is exact; the ellipsis elides only "Not every formation world contains internal strands," which changes nothing.
- §4 item 5's quotation of the Primary-gravity-first hedge ("though partly mitigated there, since Cyprian's ecclesiology and pastoral crisis-management are historically fused rather than cleanly separable") is exact, and its account of the rule's provenance (adopted in response to a review finding about the #8/#9 split's use of neighbor-protection) matches the Step 0 Conclusion's Methodological-rules entry and its Decision 4.
- The A5 fragments quoted in §2 are individually exact; the problem there is the elision's effect, not misquotation (H4).

**Claims about the IJC precedent document — every specific one checked, all true:**
- IJC's §3 does independently re-affirm distinctness from World #8, and the "non-overlapping authority structure, orthogonality to state power, temporal overlap rather than sequence" formulation is quoted correctly.
- IJC's §5 Finding 1 does recommend a worked example for the straddling-date case: "Recommend Section A gain a short worked example of a straddling case."
- IJC does carry a naming note in §1, so "unlike World #6's naming note" is accurate.
- IJC does treat 312–451 as one continuous trajectory phase-split by the 325 line, so §2's contrast is accurate.
- IJC's §6 does hold its judgment call short of escalation, so §6's characterization of that precedent is accurate.
- IJC was, in this working tree, the only prior document of this type (subject to M6).

**Corpus figures — every number in B1 checked against `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` and `cic/texts/`:**
- ~97 sermons, "preached to his congregations at Hippo and Carthage" — matches the corpus-map row exactly.
- *Enarrationes in Psalmos* at ~695,000 words, "the largest single body in the vendored corpus," preached and dictated c. 392–420 — all three match.
- 168 letters — matches.
- 82 epistles of Cyprian — matches (with L2's qualification).
- The Cyprianic treatise list (*De Unitate*, *De Lapsis*, *De Mortalitate*, *De Dominica Oratione*, *Ad Demetrianum*, *Ad Fortunatum*, *Testimonia*), Pontius's *Life and Passion* with its "often counted the earliest Christian biography" gloss, and the September 256 sententiae of 87 bishops — all present and accurately described.
- `anf05_hippolytus-cyprian-caius-novatian.xml` and `npnf101`–`npnf108` all exist on disk at `cic/texts/`.
- The corpus-map file exists, is dated as claimed, and is what the document says it is — a per-work assignment with loci, roles, confidence ratings, and cross-world notes.

**Historical dates and identifications — all correct:** Cyprian's episcopate 248/249–258; Augustine 354–430; Nicaea 325; Constantinople 381; the ~century gap between Cyprian's death and Augustine's birth; Carthage as the leading Latin see after Rome; Hippo Regius as a substantial provincial city; *De Trinitate* as the mature Latin statement of Nicene trinitarian theology; *On the Catechising of the Uninstructed* as a catechetical manual; Augustine's *On Baptism, Against the Donatists* arguing through the acts of Cyprian's baptismal councils.

**Build-status claims — all correct:** Alexandria (`alx`), Hieronymian (`hal`), and IJC (`ijc`) are built (present in `records/` and `packages/`); Donatism (#4) and Cappadocian (#5) are "Selected, Not Yet Built" per `cic/corpus-map/ATLAS-TARGETS.md` and the Atlas spec.

**The Donatism parallel-build claim is TRUE, not fabricated.** `World-Builds/Donatism/` exists on `origin/claude/record-native-world-build-v2-e2s0dt`. This was specifically suspected as an unverifiable session-assertion and checked; it holds up. The finding at M7 concerns the *impossibility* claim attached to it, not the existence claim.

**CO-022 named failure modes:**
- **(a) Attribution to "the project lead"/"Mark" without a verbatim, sourced quote — CLEAN.** The strings "Mark" and "project lead" do not appear anywhere in the document. Nothing is attributed to the project lead, directly or by implication. (Note for the revision: the Optatus row at M5 *does* carry an open question addressed to Mark in the corpus map — surfacing it would be a legitimate carry-forward, not an attribution.)
- **(b) Content described as "shown" or "checked" that wasn't — NOT clean.** See H1, H2, H3, and M7. The document's four "shown"/"as shown above" usages all refer accurately to its own §2 reasoning; the failures are in "on a live check," "No live overlap check needed," "strengthened... B1 scores," and "no live cross-document check is possible."
- **(c) Fabricated citation or fact — one instance, H3.** The `formation narrative source` / B1-scores claim. Everything else that looked like a candidate fabrication (the `ijc.source.augustine-confessions` identifier, the corpus-map file, the Donatism parallel build, the CF "Strand is a finding" quote, the "Framework Part II" attribution) turned out to be real; the identifier and the CF quotation in particular are correct. H3 is the sole clean fabrication.
- **(d) Build output outside the canonical folder — CLEAN.** The document is at `World-Builds/Latin-Pastoral-Congregational-Christianity/`, which is correct.

**Disposition discipline — CLEAN.** The status line reads "DRAFT — pending independent adversarial review," no disposition is self-assigned, "Frozen" is not claimed, and §6 correctly closes with "Pending: independent adversarial review (Round 1). Not yet dispositioned."

**Conclusions that survive review.** Both top-line conclusions are correct and should be retained: World #8 clears Section A (though H4/H5 mean the *reasoning* to that conclusion needs rebuilding), and Tier 1 is the right tier against the Methodology's own rubric. B2, B4, and B5 are sound, honestly scoped, and free of substantive defect beyond L3 and M10. §4 item 1 (the Article 3 ambiguity carried forward to Doc_01) and §4 item 5 (Primary-gravity-first discipline) are well-grounded, accurately sourced, and are the document's best work.

---

## Summary of required actions

| # | Severity | Action |
|---|---|---|
| H1 | High | Rerun the IJC cross-check at the scope claimed; report what it actually returns; dispose of the *Confessions* VIII.12 / III.5 boundary breach against escalation category 4 |
| H2 | High | Correct "Jerome does not appear in this world's corpus-map"; carry the Augustine–Jerome correspondence double-placement and hal Doc_01 §8.1's request forward to Doc_01/Doc_02 |
| H3 | High | Delete the fabricated "Hieronymian and Desert Monasticism's own B1 scores" claim |
| H4 | High | Drop the A5 routing argument and the elision; replace with the plain reading (Section A tests only Article 4); revise §5 item 1 and §6 accordingly |
| H5 | High | Stop restating Article 4's floor; if summarized, quote all five commitments verbatim; flag IJC's identical sentence for the same fix |
| M1 | Medium | "Ebionite," not "Ecclesiastes-style subordinationist" |
| M2 | Medium | Route Article 20's affirmative duty to Doc_02, not Doc_01 |
| M3 | Medium | Engage "never a per-world process" in §0; report IJC Finding 3 as still open; dispose of Criterion 2 for World #8 |
| M4 | Medium | Correct the corpus-map characterization of the two anonymous treatises |
| M5 | Medium | Add Optatus as a named, provisional, boundary-critical assignment |
| M6 | Medium | Reconcile §0's "only other world" with §3/§4's Donatism discovery |
| M7 | Medium | Actually run the Donatism cross-check from the sibling branch; add the Article 23 reciprocal obligation |
| M8 | Medium | Carry forward the reciprocal World #6 (and #9) boundary obligations the built worlds asked for |
| M9 | Medium | Correct the Cyprian/Tertullian vocabulary claim; carry the Tertullian dropped-voice disclosure forward |
| M10 | Medium | Separate Cyprian's three phases (hiding / schism / plague) |
| L1–L5 | Low | NPNF1 volume count; Cyprian corpus qualifications; B4 doubt/*De Lapsis*; §6 framing per IJC's cleared text; cut the "two or three most consequential" claim |
| C1–C2 | Cosmetic | Quote marks; CF version-status wording |

Per `cic-build-cycle`, findings H1–H5 and M1–M10 all change a claim's substance, a sourcing conclusion, or a scope boundary, so the revision is **substantial** and the revised document requires a fresh review round rather than direct application.
