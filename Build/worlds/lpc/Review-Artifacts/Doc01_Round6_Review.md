# Doc_01 — World Identification, Boundaries, and Orientation: Latin Pastoral-Congregational Christianity
## Round 6 Independent Adversarial Review

**Document reviewed:** `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT — the Round 5 revision at commit `847708cf`, 19:24:58 UTC, as further revised at commit `b6441e89`, 2026-09-01, 20:02:27 UTC, on direct project-lead guidance rather than a review finding)
**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread. Did not draft the document under review, did not draft this world's Step 0, and did not write the Round 1–5 Doc_01 reviews. **Round 5's own findings, quotations, suggested fix-texts and its recommendation to escalate were treated as claims to be re-derived, not as authority** — and so was the project lead's reported instruction. That an instruction came from the project lead settles what the build thread was told to do; it does not settle whether the document that resulted is accurate, internally consistent, or eligible for disposition under CO-022. Both questions were run separately.
**Governed by:** `cic-build-cycle` (CO-022) *Escalation categories*, *Disposition*, *Revision decision*, *Naming and term propagation*, *Cross-document fact consistency* and *Coach verification* sections, read in full at the live skill this session; Construction Framework V7.4 Part I, Record Integrity Principle; Constitution V2.2 Articles 3, 15, 21, 23, 29; `CiC_Step0_Conclusion_FINAL_v2.docx`; this world's own cleared `Step0_Movement_Scope_Confirmation.md`, especially §6.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 3 HIGH · 4 MEDIUM · 9 LOW · 6 COSMETIC.**

**On the primary sources this document remains clean, and I want that stated before anything else.** Every primary-source and governing-document quotation I re-located this session is verbatim and correctly placed at a locus I recomputed from the source rather than accepted: Letter XCIII §17 (both the §4 and the §7 rendering), the 256 Council of Carthage preface in full including the closing clause, *On Baptism* I.1.2, II.3, Book III ch. 2 and Book VI ch. 2, Letter 185's censured-kings/Nebuchadnezzar passage, Cyprian's Ep. 67. Constitution Articles 3 and 15 are exact against the extracted `.docx`. The Step 0 Conclusion's World #8 entry and its *Selection method* paragraph are exact. IJC Doc_01 §4's three strand definitions and IJC Doc_04's Candidate 2 findings are exact. The Coach3 quotation is verbatim at its own source. Both corpus-map rows check out at the row level. **Round 5's H2 (the Strand A inversion) and M2 (the inverted 256-preface bracket) are genuinely and correctly fixed**, at the operative site and in the propagated locations. **The stranded-duplicate-sentence bug did not recur**: a sentence-level sweep (≥60 chars) and a 14-word-shingle scan of the whole file return no stranded duplicates, only deliberate repetitions.

It fails at Round 6 on three grounds, all of them sitting on the material changed after Round 5.

1. **The withdrawal's own foundation is not on the record.** The document now attributes a governing principle, an instruction, and a characterization of the project lead's own view to the project lead, in three places, with no date, no quoted words, no decision artifact and no pointer to anything a reader can check. CO-022 states the rule in its strongest available terms — "Nothing is attributed to 'the project lead' anywhere in any document — a quote, a decision, an instruction — without a verifiable record that the project lead actually said or wrote it. Hold this to the same bar as Frozen" — and names "content fabricated-attributed to 'the project lead'" as one of four failure modes this version of the skill exists to close. This world's own Step 0 §6 shows exactly what compliance looks like, one file away. Round 5's own clean list certified that Doc_01 contained no such attribution; all three are new (**H1**).

2. **§9 states two opposite conclusions about the same escalation item, four paragraphs apart.** §9's category-3 paragraph says in the document's own voice that a live category-3 item is being decided, used, and referred out at once, and that "CO-022 routes a live category-3 item to the project lead, not to 'a coach pass or System Hub.'" §9's closing paragraph then calls it "Category 3's *live* item," routes it to a coach pass or System Hub, and concludes "No standing escalation category applies." Verified by diff: the category-3 paragraph is unchanged from the Round-5 revision that escalated; only the closing paragraph was rewritten. This is the series' dominant defect — a fix landing in one paragraph while its neighbour still asserts the superseded conclusion — recurring inside the escalation assessment itself (**H2**).

3. **The "documented arc" that the whole reframing rests on is falsified by Letter 185's own account, in the same letter §4 relies on.** §7 reports Augustine's relationship to state power as "present, but late, argued, and reached by a change of mind rather than assumed from the start." Letter 185 ch. 7 §25 — vendored, and the very text §4 mines for its two registers — records Augustine's *earlier* position as an active solicitation of imperial law: "it seemed to certain of the brethren, of whom I was one… that they should rather content themselves with ordaining that those who either preached the Catholic truth… should no longer be exposed to the furious violence of the heretics… yet we carried our point, to the effect that the measure which I have described above should be sought in preference from the emperors: it was decreed in our council, and envoys were sent to the court of the Count." The change Letter XCIII §17 records (a.d. 408 by NPNF's own heading) is a change in the *scope* of coercion Augustine would ask for, not the arrival of state power in his practice. The words "envoy," "Theodosius," "edict," "404," "405" and "previous emperors" occur zero times in Doc_01. The error is propagated to §1's Core Identity and, worse, into §8 item 12, where it becomes a binding instruction to Doc_02 and Doc_08 to carry the arc forward (**H3**).

---

## Method — what was actually checked

Nothing was taken on the document's, Round 5's, or the reported instruction's word.

- **The live `cic-build-cycle` skill read in full** at `/root/.claude/skills/synced/…/cic-build-cycle/SKILL.md` — all four escalation categories verbatim, the "if any apply, stop and escalate" sentence at the head of that section, the *Disposition* eligibility sentence, the project-lead-attribution rule in *Disposition*, the CO-022 note listing the four closed failure modes, and the *Coach verification* write-scope sentence.
- **This world's own cleared Step 0 read at §5, §6 and its close in full**, including the paragraphs Round 5 quoted and the three Round 5 did not: the escalation paragraph, the paragraph recording the escalation actually taken to the project lead (with its date, its quoted words, its verified fix and its pointer to `Open_Gaps_Tracking.md` item 16), and the disposition paragraph.
- **The `847708cf` → `b6441e89` diff read line by line**, so that "what did the project-lead revision actually change" was answered from the diff rather than from §9's account of it. Fifteen insertions, nine deletions, across ten places. This is how H2, M3 and L5 were found: three of the paragraphs that depend on the rewritten ones were not touched.
- **The vendored primary corpus, read directly.** `npnf101` — Letter XCIII §17 read with 1,500 characters of surrounding context, plus its NPNF date heading; `npnf104` — Letter 185's Nebuchadnezzar and censured-kings passage, **Letter 185 ch. 7 §§23–27 read in full** (which is where H3 came from, and which no prior round has read), *On Baptism* I.1.2, II.3, Book III ch. 2, Book VI ch. 2; `anf05` — the 256 Council preface in full with the proœmium heading and its ANF editorial gloss, and Ep. 67's congregational-rejection clause. **A negative check was also run**: every occurrence of "proconsul," "magistrate," "emperor" and "imperial" in the whole ANF05 volume (50 hits) read for any instance of Cyprian soliciting or contemplating civil power. There is none — §7's "absent by circumstance" survives.
- **Governing text re-extracted from `.docx` this session:** `CiC_L1_Constitution_V2_2.docx` — Article 15 in full (both paragraphs, including the one running the other way), Article 3 including the bulleted "should possess sufficient: historical coherence…" list; `CiC_Step0_Conclusion_FINAL_v2.docx` — the World #8 entry, the *Selection method* paragraph in full, the "Status: Closed" header, and an exhaustive search confirming "orthogonality" occurs exactly once.
- **Neighbour-world documents at source:** IJC's `Doc_01` §4 (all three strand definitions, printed whole) and §6 (the monepiscopal-inheritance sentence, word for word against §7's carry-across); **IJC's `Doc_04_Gravity_Discovery.md`** — Candidate 2's Explanatory test, the Classification Summary row, and the cross-strand confirmation paragraph; `Syriac-Build/CiC_Coach3_Step0_Critique_2026-07-06.md` line 25 in full.
- **Both corpus-map rows re-read verbatim** — `latin-pastoral-congregational-christianity.yaml` (`confidence: assigned`, "Also assigned to imperial-juridical-christianity below") and `imperial-juridical-christianity.yaml` (`confidence: provisional`, the "Direct evidence for the ijc world's core question — the church's use of imperial law" note).
- **The sibling branch fetched fresh.** It has moved again, to `d3e5b953`. §5's pinned claim is about `9caf7bea` and explicitly disclaims currency, so it cannot go stale — Round 5's L2 fix is sound and worked. I verified the substance independently at the *current* head: the Cyprian-scoped reading stands and the marker count is still 0.
- **Every `§n` directional pointer extracted programmatically — 69 of them** — mapped to its containing section and checked mechanically for above/below direction. One genuine failure, in this round's own new text (L1). One false positive (a quoted description of a prior fix). Zero non-existent targets. Bare "(below)" pointers checked by hand (L2).
- **A duplicate-sentence, duplicate-clause and repeated-shingle sweep** of the whole file (normalised sentences ≥60 chars; 14-word shingles). **No stranded duplicates.** All 74 repeated shingles are deliberate — quotations restated across sections, and the four cross-section restatements the document flags as such.
- **A residual-framing grep** for the withdrawn three-readings vocabulary — "reading this document adopts," "ground reading," "organizing-axis," "three readings," "precisif," "which reading," "whichever reading." Three live hits outside the revision log; one of them is a substantive survival (L3).
- **All five prior review artifacts' verdict lines**, to check the status line's arithmetic. All five match exactly.

---

## THE ESCALATION-WITHDRAWAL QUESTION — independent analysis and conclusion

This is the document's central new reasoning and the thing Round 6 was convened to test, so it gets its own section. My conclusion is stated first.

> ### Conclusion: **the withdrawal does not hold. A standing escalation category still applies on the document's own words, and self-disposition remains unavailable.**
>
> **This is not a finding that the project lead's instruction was wrong, or that "report the documented arc rather than adjudicate a portfolio phrase" is a bad posture.** On the merits I think it is the *better* posture — plainly closer to Article 15's own register than the three-readings vote it replaced, and a real improvement on what Round 5 reviewed. My conclusion would not change if the instruction were spelled out in full and I agreed with every word of it. It rests on three things the instruction does not reach: what §9 itself still concedes, what §7 and §8 item 12 still do, and what CO-022 requires before an attributed instruction may be relied on at all.

### 1. Category 3 is conceded live in the document's own voice, and the reframing does not touch it

This is decisive by itself and requires no judgment about the state-power question.

§9's category-3 paragraph (unchanged from the Round-5 revision — verified by diff):

> *"§5's own reading of Article 21 as reaching successive as well as coexisting patterns of divergence — a departure from IJC's own Doc_01 §4's narrower 'genuinely simultaneous' gloss — is not [applied rather than decided]: §5 adopts the broader reading and makes a strand determination on it that, on Article 21's and CF V7.4's own text, governs all subsequent work. **A methodology question with acknowledged portfolio-wide reach that is decided and used cannot simultaneously be treated as merely referred out; CO-022 routes a live category-3 item to the project lead, not to 'a coach pass or System Hub.'**"*

§9's closing paragraph, four paragraphs later:

> *"Category 3's **live** item is §5's Article 21 reading-divergence from IJC Doc_01 §4, assessed above and **correctly referred to a coach pass or System Hub**…"*

These cannot both be true. And CO-022's rule does not admit degrees:

> *"Before disposing of any document, check it against these four categories. **If any apply, stop and escalate directly to the project lead — do not self-dispose, regardless of how clean the review came back.**"*
> *"A document only becomes eligible for disposition when it has cleared an independent review without that review calling for substantial revision, **and none of the four escalation categories applies**."*

Note what the document itself says the instruction accomplished: the reframing "removes **the category-2 and category-4 triggers** that reading previously created." Category 3 is not mentioned, and nothing in §9 claims the instruction reached it. Category 3 arose from §5's reading of Article 21, which has nothing to do with state power and was not before the project lead. So on the document's own account of its own authority, an escalation category applies and self-disposition is unavailable — regardless of everything else in this section.

### 2. Category 2 is narrowed by the reframing, but not removed — and the substance has not actually been withdrawn

Category 2 covers "portfolio-level or cross-world strategic decisions — anything decided for a reason external to this specific world's own ecology."

I accept a real part of the document's argument here. Reporting that Cyprian had no state power to solicit and that Augustine argued his way to soliciting it *is* ecology-grounded Step 1 work, and it is not a decision about what a portfolio phrase means. If that were all §7 did, category 2 would be discharged by labelling, exactly as the document says.

It is not all §7 does. Three further moves are on the page:

**(a) §7 rules on the portfolio instrument's interpretive weight.** Line 158: *"A three-word screening-level compression, written before this world's own construction began, is not the kind of instrument that can carry a single settled theory of a bishop's relationship to state power across a 184-year span… and this document does not owe it one."* That is not a report of what the sources document. It is a determination that a clause of a closed portfolio determination has no determinate content Doc_01 owes deference to — grounded in a proposition about what Step 0 screening phrases are and what Step 1 owes them. That reason is external to this world's ecology in precisely CO-022's sense. Declining to choose among readings and ruling that there is nothing determinate to choose among are different acts, and the second is the larger one.

**(b) §7 displaces the portfolio's own characterization for downstream purposes.** Line 162: *"It is a claim about what Doc_02's own Source Ecology work and Doc_08's own Forces analysis must carry forward accurately: **not a static characterization borrowed unexamined from a portfolio-level screening pass**, but the documented arc itself."* That instructs later documents in this build to carry this document's arc in place of the portfolio's stated ground for the World #6 distinctness finding. And §7 line 156 records that the same clause sits in IJC's own cleared Doc_01 §6 — so the consequence has cross-world reach the build thread has no write scope to record where it actually lands.

**(c) §8 item 12 forecloses reconsideration.** *"[Whoever next relies on this] should not read this item as an open interpretive question awaiting resolution — **it is a record of a choice already made**, to report rather than adjudicate."* A choice, on the document's own word, closed against the next reader. Compare what Round 5 praised and asked to be kept: §8 item 12 previously *invited* the check. The reframing has converted an open disclosure into a closed one. That is a real loss, and it is the opposite direction from where the escalation categories point.

**And the first-order claim was never actually withdrawn — it moved.** §7 stopped asserting the ground-versus-instrument reading. §1 and §5 did not:

- §1, Core Identity: *"…where here a bishop's office is grounded in ordination and territorial charge and **state power is, at most, an instrument** later solicited against a rival, and only after a documented change of mind — the actual, undogmatic shape of this world's own relationship to state power is reported rather than assumed at §7 below."* That parenthesis both asserts the narrow ground reading and, in the same breath, says the shape is only reported at §7.
- §5, Ecological orientation: *"…not as a substitute source of the bishop's own standing, which remains grounded throughout in ordination and territorial charge."* This is the answer that closes the last of Article 21's four criteria.

So the honest description of what happened is: §7 withdrew the *label* on the reading, and §1 and §5 kept *applying* it. The brief asked whether the new §7 text still, in substance, makes a claim about how "orthogonality to state power" should be understood. §7 makes a second-order one (the phrase cannot bear a settled sense; downstream work must carry the arc instead). §1 and §5 make the first-order one outright.

### 3. Limb 3 of category 4 is weaker than Round 5 found it, but not clearly not met

Here the document has the better of Round 5. Round 5's limb-3 finding rested on the document's *own conditional* — that on one reading its finding cut against the portfolio determination. That conditional is gone, and I would not sustain limb 3 on Round 5's reasoning alone.

But CO-022's verb is "cuts against," not "contradicts." The Step 0 Conclusion offered "orthogonality to state power" as one of three named grounds for a closed distinctness finding. Doc_01 now holds that ground incapable of carrying a settled sense and instructs downstream work to carry something else in its place. Whether that "cuts against" the determination is genuinely arguable both ways — which is itself the point. It is not a call a build thread should be making alone. I do not rest on this limb.

### 4. What CO-022 requires before an attributed instruction can be relied on at all

Separately from everything above: the withdrawal is licensed, on the page, entirely by an instruction attributed to the project lead. CO-022 permits that only where there is "a verifiable record that the project lead actually said or wrote it," held "to the same bar as Frozen: a real, checkable record, not a claim." There is none in this build folder, and the document points at none (**H1**).

This world's own Step 0 §6 shows the standard being met, one file away: a date, the project lead's actual words in quotation marks, the action authorized, the fix independently verified, and a pointer to the artifact where it is logged. Doc_01 gives none of these, and its most expansive attribution goes beyond a reported instruction into an inference about the project lead's reasoning — *"the project lead does not treat that as a call for the project lead alone to make case by case, but as a standing instruction for how this build (and this document specifically) should have framed the question from the start."* That sentence is doing the heaviest lifting in the section, and nothing supports it.

### 5. Reframing is a third thing, and it is weaker than either of the two Step 0 named

Step 0 §6 set this world's own standard on the record: *"**With the escalation actually resolved — not merely disclosed** — no standing category-4 tension remains open."* Round 5 correctly held that Doc_01's disclose-and-self-dispose was the move Step 0 rejects. The revision's answer is neither of those two things: it neither resolves nor discloses, it *reclassifies* — and, at §8 item 12, closes the disclosure that used to stand in the disclosure's place. Nothing in CO-022 makes reclassification an alternative to escalation, and this world's own precedent runs the other way.

### 6. What I recommend

Not a re-escalation of the state-power question. The project lead's instruction, as reported, disposes of that: the honest thing to carry forward is the documented arc, and I agree. What is required is narrower and mostly mechanical:

1. **Create the record.** A dated decision artifact in this world's build folder recording the instruction in the project lead's own words, cited from §8 item 12 and §9 — the same form Step 0 §6 used. Until it exists, CO-022 forbids relying on the attribution.
2. **Fix H3 first.** An arc reported inaccurately is worse than a phrase left unconstrued, and §8 item 12 currently makes the inaccurate arc binding on Doc_02 and Doc_08.
3. **Reconcile §9's category 3 with itself and escalate that item.** One paragraph; §9 line 245 has already written it.
4. **Apply the reframing at §1 and §5**, or state plainly that the ground/instrument reading is being applied there and label it. Right now the document reports in §7 and adjudicates in §1.
5. **Reopen §8 item 12's disclosure.** Keep the report; drop "should not read this item as an open interpretive question awaiting resolution." The candour Round 5 praised was worth keeping, and closing it buys nothing.

---

## Round 5 disposition — what was actually fixed

**Genuinely fixed, verified at source:**

- **H2 (the Strand A inversion).** Fixed, and well. §7 now reads the three strands correctly against IJC Doc_01 §4 — "three strands, of which only one (B) grounds authority directly in the state relationship, one (A) is defined expressly independent of it, and one (C) is constituted by opposition to it" — with all three quotations verbatim at source. Propagated to §1 in the same pass. The inverted "two of its three strands" survives only inside §9's own account of the defect. This is the best-executed fix in the revision.
- **M2 (the inverted 256-preface bracket).** Fixed, by Round 4's second option and Round 5's recommendation: the clause is now quoted whole. Verbatim against ANF05 across the elision.
- **L1 (the §5 direction failure).** Fixed — §5 now reads "§7 below."
- **L2 (the branch-state currency claim).** Fixed properly, and it worked: §5 pins "as at commit `9caf7bea`" and explicitly disclaims currency. The branch has since moved twice more (to `d3e5b953`); the claim is still true because it no longer asserts anything about the head. Third round of trying, correct on the third.
- **L3, L5, L6** — all three fixed and verified in place (the axis-width reconciliation at §5; the independence-inference sentence's logic corrected; the Step 0 write-scope framing corrected at §8 item 11).
- **C1, C2, C4, C5-cosmetic, C6** — all verified applied: the fresh label collision disambiguated ("Round 4's M8, Round 3's C1"); "107 minutes"; Step 0 §3 B2's italics restored to "plausibly the *richest*" (checked against Step 0's own text); ANF05's 258 proœmium date disclosed at §4; IJC §6's monepiscopal wording carried across word for word (checked against IJC Doc_01 line 93).

**Fixed and then substantially reverted, unlogged (1):** **M1** — §9 logs "the whole IJC characterization rebuilt on IJC's own completed `Doc_04`." It was, at `847708cf`; the paragraph that did it was deleted at `b6441e89`. §7 no longer mentions Doc_04, and §1's claim that depends on it is now unsupported anywhere in the live text (M3 below).

**Claimed fixed and not fixed (1):** **L7** — §9 logs "limb 2's dropped third candidate… given a pointer rather than left silently uncounted." Limb 2 contains no such pointer (L4 below). Fourth consecutive round in which the "All addressed" list carries a false fixed-claim.

**Fixed, then made moot by the deletion (2):** **L9** (the universal negative) and **C3/C5** (the double-placed *letter* not "register") were both applied at `847708cf` in the paragraph subsequently deleted. C5's substance survives correctly at §4; L9's does not — §7 introduced a fresh unbounded negative in its place (L6 below).

---

## What was checked and found clean

Recorded because this project's reviews document both sides.

1. **Every primary-source quotation is verbatim and correctly located**, at loci recomputed this session. Letter XCIII §17 is exact in both §4 and §7, with §4's ellipsis covering only "lest we should have those whom we knew as avowed heretics feigning themselves to be Catholics." The 256 preface is complete at both ends and matches ANF05 character for character across three sentences; §7's un-bracketed rendering is exact and its ellipsis covers only the "tyrannical terror" clause. *On Baptism* I.1.2's ordination sentence, II.3's councils passage with both ellipses, Book III ch. 2's "not indeed by the authority of any plenary or even regionary Council," and Book VI ch. 2's "afterwards brought to light… by the authority of a plenary Council" are all exact. Letter 185's Nebuchadnezzar and censured-kings material supports §4's characterization of the second register precisely as stated. Ep. 67's clause is exact.
2. **Article 15 and Article 3 are exact.** Article 15's quoted sentence is verbatim in `CiC_L1_Constitution_V2_2.docx`. Article 3's "sufficient historical coherence" is a fair compression of a bulleted list and correctly attributed (the trap Round 5 flagged is real — a plain grep returns nothing).
3. **The portfolio Step 0 Conclusion is exact.** The World #8 entry including the "orthogonality to state power" clause; "orthogonality" occurs exactly once in the document; "Status: Closed" is on the header; the *Selection method* paragraph reads as Round 5 reported it.
4. **IJC's own documents are exact.** Doc_01 §4's three strand definitions, quoted whole; §6's monepiscopal-inheritance sentence carried across word for word. Doc_04's Candidate 2 — "Church-State Alliance and Its Limits," **Primary**, "Confirmed cross-strand (precondition for all three strands)," and the Explanatory test's "the single most load-bearing explanatory claim in this world's entire construction record to date" — all verbatim, so §9's account of it is accurate even though §7 no longer carries it.
5. **Coach3 is verbatim** at its own source in this working tree, and correctly labelled portfolio-level per CO-022 at both §5 and §9.
6. **Both corpus-map rows are exact**, including the IJC row's `confidence: provisional` and its note.
7. **"Absent by circumstance" survives a real check.** I ran every occurrence of "proconsul," "magistrate," "emperor" and "imperial" across the whole ANF05 volume looking for a counter-instance to §7's claim about Cyprian. There is none: his engagement with civil power is uniformly as its object — awaiting the proconsul's return, reporting Valerian's rescript, banished to Curubis. §7's Cyprian half is accurate. It is the Augustine half that fails (H3).
8. **No stranded duplicate sentence or clause anywhere in the file**, including at the end of §9 and at the document's close. The bug that recurred in two earlier revisions has now stayed absent for two consecutive rounds.
9. **The status line's arithmetic is honest.** Round 1 (9/12/9/3), Round 2 (4/10/9/6), Round 3 (1/10/9/6), Round 4 (1/8/9/6) and Round 5 (2/3/9/6) match the five review artifacts exactly. DRAFT is claimed; Frozen is not; Living Tradition Status is PENDING and correctly routed to the project lead as a project-lead act.
10. **The post-Round-5 change is honestly *segregated*, whatever else is wrong with it.** §9 line 239 states plainly that this was a distinct step on different authority, "so that the record shows accurately what changed, when, and why — rather than folding it into 'Round 5' as though a review found it," and the status line says the same. That discipline is right, and it is why this review could reconstruct exactly what happened. It should be kept.
11. **§9's closing "Pending" line invites this review's own scrutiny of the withdrawal by name** — "including whether withdrawing an escalation on the strength of a reframing, rather than a resolution, is itself sound." That is the correct instinct and it is the reason this review's escalation section could be written against a target the document itself named.
12. **The Donatism cross-branch material still holds at the sibling branch's current head.** I re-fetched (`d3e5b953`) and re-derived: §3 B3 still attaches the parenthetical to Cyprian's Decian-persecution material; the provenance marker count is still 0. §5's pinned claim and its "on the current record" statement are both true as of this session.

---

# HIGH

### H1 — three project-lead attributions with no verifiable record, against CO-022's explicit rule, carrying the entire escalation withdrawal

**Where.** Status line (line 3); §8 item 12; §9's post-Round-5 paragraph and its closing paragraph. Against CO-022's *Disposition* section and the CO-022 note, read at the live skill this session, and against this world's own `Step0_Movement_Scope_Confirmation.md` §6.

**What's wrong.** CO-022, verbatim:

> *"**Nothing is attributed to 'the project lead' anywhere in any document — a quote, a decision, an instruction — without a verifiable record that the project lead actually said or wrote it.** Hold this to the same bar as Frozen: a real, checkable record, not a claim."*

And the skill's own CO-022 note lists, among the four failure modes this version exists to close, "**content fabricated-attributed to 'the project lead'**."

The document now attributes three things:

- §8 item 12: *"This document does not certify what it means, **on the project lead's own instruction** that this build's governing principle is to report what the sources document rather than resolve them into a single reading for the sake of a tidy portfolio-level fit."*
- §9: *"**Put to the project lead directly, the answer was not a choice among the three**: this project's own governing principle is to report what the sources document, including real change over time… **and the project lead does not treat that as a call for the project lead alone to make case by case, but as a standing instruction for how this build (and this document specifically) should have framed the question from the start**."*
- §9's closing paragraph: *"prompted directly by **the project lead's own instruction** not to let this document force a single reading of the sources where the honest answer is that the sources themselves show real change over time."*

None of the three carries a date, a quoted word, a decision artifact, or a pointer. There is no decision-log file in this world's build folder — the folder contains Doc_01, Step 0, and `Review-Artifacts/` and nothing else.

**Contrast this world's own Step 0 §6, which meets the bar exactly, one file away:**

> *"**The escalation was taken to Mark directly, 2026-09-01**, rather than resolved by this thread's own judgment. He authorized this thread to fix IJC's boundary breach outright (**"the old thread that did this is retired"**). The fix… is complete and independently verified… Logged in full, with root cause, at `World-Builds/Imperial-Juridical-Christianity/Open_Gaps_Tracking.md` item 16 — the record files themselves carry no added commentary, **per Mark's standing instruction (2026-09-01)** that world records hold content only."*

Date, actual words, action, verification, artifact pointer. Doc_01 has none of these.

The third attribution is the worst of the three, and it is not a reported instruction at all: *"the project lead does not treat that as a call for the project lead alone to make case by case, but as a standing instruction for how this build (and this document specifically) should have framed the question from the start."* That is a claim about the project lead's own reasoning and its intended scope, asserted in the document's voice, and it is the sentence that converts "guidance on framing" into "the escalation is withdrawn." That is precisely the shape of the failure mode CO-022 names.

**Why it matters.** Four ways. (i) It is a direct violation of a rule CO-022 states at Frozen-level strength. (ii) It is load-bearing: strip it and §9's withdrawal has no stated authority at all. (iii) Round 5's own clean list, item 11, certified that "nothing is attributed to 'the project lead' or 'Mark' as a quote, decision or instruction anywhere in Doc_01" — so all three are new, and the document has moved from compliance to non-compliance on a checked property. (iv) The commit message ("on project-lead guidance") is not a document-side record either; it is authored by the same thread and is not what CO-022 means by checkable.

**This is not a finding that the project lead did not say it.** I have no visibility into that and take no view. The finding is that the document does not point at anything a reader can check, on a rule that exists specifically because this project has been burned by exactly this before.

**Fix.** (a) Create the decision artifact in this world's build folder — dated, with the project lead's own words, on the model Step 0 §6 already set — and cite it from §8 item 12 and §9. (b) Delete or source the inference about how the project lead "treats" the class of decision; a reported instruction about framing does not license a claim about the project lead's meta-view of escalation. (c) Until (a) exists, do not rely on the attribution to close anything.

---

### H2 — §9's category-3 paragraph and §9's closing paragraph state opposite conclusions about the same item; the reframing did not reach category 3 at all

**Where.** §9's Category 3 paragraph against §9's "No standing escalation category applies" paragraph. Verified against the `847708cf` → `b6441e89` diff.

**What's wrong.** The category-3 paragraph, which the project-lead revision did not touch:

> *"**A methodology question with acknowledged portfolio-wide reach that is decided and used cannot simultaneously be treated as merely referred out; CO-022 routes a live category-3 item to the project lead, not to 'a coach pass or System Hub.'**"*

The closing paragraph, four paragraphs later, which it did:

> *"**Category 3's live item** is §5's Article 21 reading-divergence from IJC Doc_01 §4, assessed above and **correctly referred to a coach pass or System Hub**, since it is a methodology question about how a Constitution Article should generally be read, not a decision this document needs the project lead to make about its own disposition… **No standing escalation category applies.**"*

The first paragraph is the Round-5 revision's concession of Round 5's finding. The second is the project-lead revision's conclusion. They contradict on the same item, in the same section, and the second calls the item "live" while concluding that nothing applies.

**Why it matters.** Three ways.

1. **The reframing does not reach this item and does not claim to.** The document's own statement of what the instruction accomplished is that it "removes the **category-2 and category-4** triggers that reading previously created." Category 3 arose from §5's reading of Article 21 — a question about whether Article 21's test reaches successive as well as coexisting patterns. It has nothing to do with state power and was never before the project lead. So even granting the reframing in full, and granting the project lead's instruction in full, a category applies.
2. **CO-022's rule is unconditional and stated twice.** "If any apply, stop and escalate directly to the project lead — do not self-dispose, regardless of how clean the review came back," and "A document only becomes eligible for disposition when… none of the four escalation categories applies." A *live* item, on the document's own adjective, is one that applies.
3. **It is the series' signature defect, in the worst possible place.** Round 5's process observation 3 named it: "after writing [a correction note], grep the section for the claim it disclaims." The project-lead revision rewrote §9's closing paragraph and limb 3 and left the category-3 paragraph standing four paragraphs above, asserting the opposite. Stranded fixes have now been found at Step 0 in sentences, at Doc_01 Rounds 2–3 in sections, at Round 4 in list limbs, at Round 5 in adjacent paragraphs, and here in the escalation assessment itself.

**Fix.** Either withdraw the category-3 concession with stated reasons, or — the honest course, since I can find no reason to withdraw it — restate the conclusion: a standing category-3 item applies, this document does not self-dispose, and the item goes to the project lead in the same note as the H1 record. The paragraph making the case is already written.

---

### H3 — "present, but late… reached by a change of mind" is falsified by Letter 185's own account, in the same letter §4 relies on; the error is propagated to §1 and made binding on Doc_02/Doc_08 at §8 item 12

**Where.** §7's state-power paragraph; §1's Core Identity; §8 item 12. Against `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`, Letter 185 ch. 7 §25, read in full this session.

**What's wrong.** §7 states:

> *"That is **the actual, documented shape** of this world's own relationship to state power: absent by circumstance in Cyprian's phase; **present, but late, argued, and reached by a change of mind rather than assumed from the start**, in Augustine's."*

The evidence offered is Letter XCIII §17 — Augustine's "originally my opinion was, that no one should be coerced into the unity of Christ." That quotation is verbatim and correctly placed; I re-located it and read 1,500 characters around it. The problem is what the document did not read: Letter 185 ch. 7 §25, in the same volume, in the very letter §4 mines for its two registers.

> *"However, **before those laws were sent into Africa** by which men are compelled to come in to the sacred Supper, it seemed to certain of the brethren, **of whom I was one**, that although the madness of the Donatists was raging in every direction, yet we should not ask of the emperors to ordain that heresy should absolutely cease to be, by sanctioning a punishment to be inflicted on all who wished to live in it; but that they should **rather content themselves with ordaining** that those who either preached the Catholic truth with their voice, or established it by their study, should no longer be exposed to the furious violence of the heretics. And this they thought might in some measure be effected, **if they would take the law which Theodosius, of pious memory, enacted generally against heretics of all kinds**… and confirm it in more express terms against the Donatists… yet **we carried our point, to the effect that the measure which I have described above should be sought in preference from the emperors: it was decreed in our council, and envoys were sent to the court of the Count**."*

Three things follow, none of which the document reports.

1. **Augustine's earlier position was not abstention from state power.** It was a *narrower solicitation* of imperial law — the Theodosian fine, applied against Donatist clergy in districts where Catholics suffered violence. He argued for it, "carried [his] point," and had it "decreed in our council" with "envoys… sent to the court." So the change Letter XCIII §17 records is a change in the *scope* of the coercion he was willing to request, not the arrival of state power in his practice.
2. **"Late" is wrong.** Letter XCIII is a.d. 408 on NPNF's own heading; Augustine was bishop from 395/396. The council petition of §25 precedes "those laws" (the compulsion legislation), so it sits earlier still. The document gives no dates at all in this paragraph, which is how the characterization passes.
3. **This world's own record attests recourse to imperial law before Augustine.** §25 also records the older bishops arguing from "a time when men were compelled to come in to the Catholic communion by **the laws of previous emperors**." The African Catholic communion's relationship to state power did not begin with Augustine's change of mind.

Confirmed absent from Doc_01: "envoy," "Theodosius," "edict," "404," "405," "previous emperors" — zero occurrences each.

**Why it matters.** Four ways, and this is the most consequential finding in the review.

1. **It is the finding the entire reframing rests on.** §9's category-2 and limb-3 reasoning both cite "Augustine's own argued change of position, held after he judged his earlier view overturned by results" as the thing §7 reports instead of adjudicating. If the arc is wrong, the reframing is resting on a mis-report, and the project lead's instruction — report what the sources document — has not in fact been carried out.
2. **It is propagated into a binding downstream instruction.** §8 item 12: *"state power is absent from the question for Cyprian by circumstance… and present but late, argued, and reached only after Augustine's own documented change of mind for Augustine… **Whoever next builds on this document's own World #6 boundary section should carry that arc forward** rather than a single static label."* An inaccurate arc made binding on Doc_02 and Doc_08 is a worse outcome than an unconstrued phrase, which is what the reframing was meant to avoid.
3. **It reverses the direction of the finding.** The arc as stated makes state power a late arrival in this world. The fuller record shows it present in a narrower form from early in Augustine's episcopate and in the African church before him — which strengthens the reading the document sets aside and weakens the ground/instrument proposition §1 and §5 still assert (M1).
4. **It takes an apologetic self-report as the historical record.** §7 hedges once ("by his own account") and then asserts flatly that this is "the actual, documented shape." Letter XCIII is a polemical letter to a Rogatist bishop justifying a position; Letter 185 is Augustine's own fuller narration of the same history, and it complicates his own summary. A document that elsewhere insists "an absence of attested change is not the same claim as attested continuity" (§4) should not collapse a retrospective self-narration into "the actual, documented shape."

**What is not wrong.** The Cyprian half survives. I ran a corpus-wide negative check across ANF05 and found no instance of Cyprian soliciting or contemplating civil power against a rival. "Absent by circumstance" is accurate.

**Fix.** State the arc as the sources give it, with dates: Cyprian — no recourse available, the question does not arise. Augustine — from early in his episcopate, an *argued, limited* solicitation of imperial law (Letter 185 §25: the council decree and the envoys to court, before the compulsion laws reached Africa); then, by a.d. 408 and by his own account overturned by results, the broader compulsion position (Letter XCIII §17), defended at length thereafter on two registers (Letter 185). Note that §25 also records earlier imperial compulsion the African church had already benefited from. Correct §1's "only after a documented change of mind" and §8 item 12's carry-forward instruction in the same change set, per CO-022's *Naming and term propagation* rule.

---

# MEDIUM

### M1 — the reframing is not applied at §1 or §5, both of which still assert the ground-versus-instrument reading §7 now declines to assert

**Where.** §1's Core Identity parenthetical; §5's Ecological-orientation bullet; against §7's own new text and §8 item 12.

**What's wrong.** §7 now says, twice:

> *"**This document does not adjudicate what the portfolio phrase 'really means'**…"*
> *"This is not a claim about which of several competing readings of 'orthogonality to state power' is correct, and **this document does not put one forward**."*

§1 puts one forward:

> *"…where here a bishop's office is grounded in ordination and territorial charge and **state power is, at most, an instrument** later solicited against a rival, and only after a documented change of mind — the actual, undogmatic shape of this world's own relationship to state power is reported rather than assumed at §7 below."*

So does §5, in the sentence that closes the last of Article 21's four criteria:

> *"…the coercion is solicited on behalf of recovering a rival claim on the *same* local flock, **not as a substitute source of the bishop's own standing, which remains grounded throughout in ordination and territorial charge** (§7 below, which reports Cyprian's and Augustine's own differing, documented relationships to state power without resolving them into a single characterization)."*

"State power is, at most, an instrument" and "not a substitute source of the bishop's own standing" *are* the narrow ground reading. The revision changed §5's parenthetical (from "the same ground-versus-instrument distinction the World #6 boundary now turns on" to "reports… without resolving them") and left the proposition the parenthetical was attached to entirely intact. §1's was changed the same way and to the same effect.

**Why it matters.** Three ways. (i) It means the withdrawal is partial in the way that matters most: the document reports in §7 and adjudicates in §1, which is the paragraph a reader of the World #6 boundary meets first. (ii) §1's parenthesis is internally incoherent — it asserts the characterization and, in the same breath, says the characterization is only reported downstream. (iii) It bears directly on the escalation question: a document that still applies the ground reading as its operative World #6 contrast has not stopped making a claim about how "orthogonality to state power" should be understood; it has stopped *labelling* the claim.

**Fix.** Either restate §1 and §5 on the reported arc (§1: "state power is absent from the question for Cyprian and, for Augustine, solicited — first narrowly, then broadly after an argued change of position — against a rival communion, §7 below") or keep the ground/instrument proposition and say plainly that the document applies it, labelled as its own reading, with §9 reassessed accordingly. What cannot stand is asserting it and disclaiming it in the same sentence.

---

### M2 — §7's central premise about the portfolio phrase is asserted without engaging the portfolio document's own paragraph defining the criterion the phrase belongs to

**Where.** §7's "does not adjudicate" paragraph; §9's category-2 paragraph. Against `CiC_Step0_Conclusion_FINAL_v2.docx`, *Selection method*, extracted and read in full this session.

**What's wrong.** The load-bearing premise of the whole reframing is a claim about the phrase:

> *"**A three-word screening-level compression, written before this world's own construction began, is not the kind of instrument that can carry a single settled theory** of a bishop's relationship to state power across a 184-year span containing a persecuted-illegal phase and an established-imperial one — and this document does not owe it one."*

The portfolio document's own *Selection method* paragraph, which no live text in Doc_01 engages:

> *"…the final worlds were chosen by prioritizing two criteria over a third: strength of sourcing… and genuine distinctiveness from the other selected worlds (formation-logic, **authority structure, relationship to power**) — prioritized over even geographic completeness. Two further tests were used to resolve edge cases: whether two candidate currents were sequential, causally-linked phases of one process… or **independent, temporally-overlapping formations with different authority structures and relationships to power**."*

The World #8 entry's three-item formula — "non-overlapping authority structure, orthogonality to state power, temporal overlap rather than sequence" — maps one-to-one onto that test. So the phrase is not a free-floating compression; it names the second of three stated separation criteria, and the portfolio document says what that criterion is and what it is for.

**Why it matters.** The document is entitled to conclude that the criterion is still too coarse for Doc_01 to construe. It is not entitled to reach that conclusion without engaging the portfolio's own definition of it, which is the single most relevant piece of evidence about the phrase's register and which sits eleven paragraphs above the World #8 entry in the same file. The only place the *Selection method* paragraph appears anywhere in Doc_01 is inside §9's summary of Round 5's review — where it is reported as an argument Round 5 made and the document then does not answer. This is the same defect pattern as Round 5's M1 (building on a Step-1 parenthetical without consulting the cleared document that resolved it), operating on the portfolio document instead of the neighbour world's.

**Fix.** Quote the *Selection method* paragraph in §7 and say why the criterion it defines still does not settle the question — or, if it does narrow the question usefully, say that instead. Either way the paragraph has to be on the page before a claim about the phrase's interpretive capacity can stand.

---

### M3 — §1's IJC Doc_04 claim lost its only support when §7 was rewritten, and §9's log still credits the Round-5 M1 fix as standing

**Where.** §1's Core Identity parenthetical; §7 (absence); §9's Round-5 log entry for §7.

**What's wrong.** §1 states, as the World #6 contrast:

> *"…and **whose own completed construction finds the church-state relationship a defining, cross-strand concern in its own right**…"*

This is true. I verified it at source: IJC's `Doc_04_Gravity_Discovery.md` records Candidate 2, "Church-State Alliance and Its Limits," as **Primary**, "Confirmed cross-strand (precondition for all three strands)," with an Explanatory test reading "the single most load-bearing explanatory claim in this world's entire construction record to date."

But the paragraph that cited Doc_04 was deleted at `b6441e89`. Doc_04 is now named nowhere in §7 — the section §1's own parenthesis points to — and appears only twice in the whole document, both times inside §9's retrospective account of Round 5. Meanwhile §9's Round-5 log still reads:

> *"**the whole IJC characterization rebuilt on IJC's own completed `Doc_04`**, which found the church-state relationship a co-equal, cross-strand Primary gravity rather than 'one of two routes' to a shared juridical-fixity concern…"*

That fix was applied and then largely reverted, and the log records only the application.

**Why it matters.** (i) Round 5's M1 was one of the three MEDIUMs the revision was required to fix; it is now half-undone with no disclosure. (ii) §1 makes a substantive claim about a neighbour world's cleared construction record with no citation anywhere in the live body of the document, in the paragraph most likely to be quoted forward. (iii) CF V7.4's Record Integrity Principle addresses exactly this — "A fix described as applied is not confirmed until the actual deployed artifact is checked directly and found to contain it" — and the reverse case, a fix described as applied that was subsequently removed, is worse, because the log now actively misdescribes the file.

**Fix.** Either restore the Doc_04 citation to §7 (it is compatible with the reframing — reporting that IJC's own completed construction found the church-state relationship a Primary cross-strand gravity is a report, not an adjudication) or move the citation into §1 itself. Then correct §9's log entry to say what survives and what did not.

---

### M4 — the reframing removed evidence, not only argument: the corpus-map's own IJC note is now nowhere in the document

**Where.** §7 (absence); against `cic/corpus-map/imperial-juridical-christianity.yaml`, read verbatim this session.

**What's wrong.** The deleted §7 paragraph carried this world's own corpus-map's characterization of Letter 185's significance for IJC:

> *"Direct evidence for the ijc world's core question — the church's use of imperial law — written to an imperial officer to justify coercive legislation."*

I verified the note is real and verbatim. The phrase "core question" now occurs **zero** times in Doc_01. §4 retains the bare fact of double-placement and the observation that it "is the signal that this second register is real," but not the corpus-map's own statement of what the letter evidences.

**Why it matters.** §7's stated purpose is now to report "what the sources actually document" and to instruct Doc_02 and Doc_08 to "carry forward accurately… the documented arc itself." The single strongest documented datum on the side the reframing does not favour — this world's own corpus-map filing one of its two anchor figures' texts as direct evidence for the neighbour world's *core question* — was removed along with the argument it was serving. Under the project lead's own stated principle, that cuts the wrong way: the instruction was to report more of what the sources show, not less. This is also the second time in this document's history that a disclosure has been deleted rather than re-aimed when the argument around it changed (compare Round 2's M8, the deleted Augustine–Jerome disclosure, and Round 5's L8).

**Fix.** Restore the corpus-map note to §7's report of the arc. It belongs there on the reframing's own terms — it is a documented fact about this world's own corpus, not an interpretation of a portfolio phrase.

---

# LOW

**L1 — §8 item 12's cross-reference direction is wrong, and newly wrong in this revision.** The item heading reads "(§7, **§9 above**)." §9 follows §8. The prior version read "(§7, §9 below)" and was correct; the revision changed it in the wrong direction while rewriting the heading. Of 69 directional pointers extracted and checked mechanically, this is the sole genuine failure — and, exactly as at Round 5's L1, it is in this round's own new text. Fix: "(§7 above, §9 below)."

**L2 — §7's "(below)" pointer now points at nothing.** §7: *"…where it is *constitutive* of two of IJC's own three strands' own stated grounds (**below**)."* Nothing below that point in §7 discusses IJC's strand grounds — the material it pointed to went with the deleted paragraph. The support for the claim is in fact *above*, in the same paragraph (the three strand definitions). Fix: "(above)," or delete the pointer.

**L3 — §7 still asserts that this document adopts a reading of the phrase.** §7: *"…IJC's Doc_01 §6 inherits it from the same source rather than asserting it independently, and would itself be re-glossed by **whichever reading of the phrase this document adopts** — a cross-world consequence this document does not have the write scope to record inside IJC's own file, and names here instead."* Two paragraphs later §7 says it puts no reading forward; §8 item 12 says it "does not certify what it means." This clause is the Round-5 L8 discharge, left standing unchanged when the framing it depends on was withdrawn — so it is now both self-contradictory and, on the new framing, vacuous (there is no adopted reading with which to re-gloss IJC's §6). A residual-framing grep for the withdrawn vocabulary returns this as the one substantive survival. Fix: restate the consequence on the new framing — the same clause sits in IJC's cleared §6, and whatever this document reports about the arc bears on how that clause reads there too — or state plainly that on the reporting posture there is no re-glossing consequence, and say so.

**L4 — Round 5's L7 is logged as fixed and is not fixed.** §9: *"limb 2's dropped third candidate (the Article 21 reading-divergence, moved to category 3) given a pointer rather than left silently uncounted (L7)."* Limb 2 reads in full: *"One live candidate: the Donatism reading divergence, closed on the substance and carried forward as a record-correction item (§8 item 11) rather than a live contradiction. Not met. The World #6 boundary question belongs at limb 3, not here, since this document is a DRAFT rather than one of 'two already-cleared master documents.'"* No pointer to category 3, no mention of Article 21. Fourth consecutive round in which the "All addressed" list carries a false fixed-claim, against CF V7.4's Record Integrity Principle. Fix: one clause in limb 2, and write the next "All addressed" list from the diff.

**L5 — §9's Round-5 log describes a §7 that no longer exists, with no forward-pointer, contrary to the document's own established convention.** The §7 bullet still reads: *"…the section restructured to present three live readings of 'orthogonality to state power' honestly rather than resolve to one — the narrow ground reading is argued but not asserted as settled, and the organizing-axis reading IJC's own Doc_04 now supports is stated as live rather than argued away (M1, H1)."* That framing was withdrawn one paragraph later. The document's own practice everywhere else attaches a parenthetical forward-pointer to superseded log entries — see the Round-2 §7 bullet ("The 256-preface bracket compression this round's own log credited to a 'C1' fix was in fact only half-restored… see the Round 4 entry below"), the Round-3 §7 bullet, and the Round-4 §7 bullet, each of which does exactly this. This entry has none, so a reader working forward through §9 meets it as a live description of the current file. Fix: add the forward-pointer the document's own convention supplies.

**L6 — a new unbounded negative, one round after the last one was narrowed.** §7: *"the question of soliciting state power does not arise for him because **the option does not exist**."* Round 5's L9 required exactly this class of claim ("nowhere in this world's own corpus…") to be narrowed to what the document had actually examined; the fix was applied and then deleted with the paragraph, and the replacement paragraph carries a fresh one. I ran the check and found no counter-instance, so the claim is probably true — but it is an unqualified universal about a period this document has not inventoried, in the sentence that now carries the most weight in the section, and it is stated about circumstance rather than evidence. The honest form is available and no weaker: on the evidence this document has examined, no surviving text shows Cyprian soliciting or contemplating civil power against a rival, and the political situation of a proscribed religion gives him none to solicit.

**L7 — "quoted in full at §4 above" overstates what §4 quotes.** §7 cites Letter XCIII §17 as "quoted in full at §4 above." §4's quotation elides "lest we should have those whom we knew as avowed heretics feigning themselves to be Catholics," and §17 continues for several hundred further words past where §4 stops. Round 5's L4 required the removal of one "in full" claim a quotation did not support, and the revision applied it; this revision introduced another in new text. Fix: "quoted more fully at §4 above."

**L8 — Article 15 is deployed to license a conclusion it does not reach, and quoted from only the limb that suits.** §7 and §9 both use Article 15 — verified verbatim: "historically developing ecclesial realities shaped, to the degree the evidence attests, through instability, adaptation, and incomplete continuity" — to support the proposition that reporting the arc "is ordinary Step 1/Step 2 construction work… **not a decision about what a portfolio-level determination means**." Article 15 licenses the first half. It says nothing whatever about whether a portfolio-level clause must be construed, which is the half the argument actually needs. Note also that Article 15's second paragraph runs both ways — *"Where a formation world's evidence attests continuity and stability rather than dispute or upheaval, that finding is recorded honestly as the result of the assessment, **never displaced by an assumption that instability must be present**"* — and the document quotes only the instability limb, in a paragraph whose whole point is that the record does not hold still. Fix: keep Article 15 for what it licenses, and argue the second half on its own.

**L9 — the status line no longer states the document's disposition posture, which is a regression on this world's own practice.** The prior status line said explicitly: "this document does not self-dispose: a standing escalation category (4, limb 3, and 2) applies and this document is escalated to the project lead." It now says only "further revised after direct project-lead guidance… Pending Round 6." A reader of the status line alone cannot tell that §9 concedes a live category-3 item, or what disposition state the document is in. Step 0's own §6 states the consequence explicitly in every version of its disposition paragraph. Fix: say what the posture is, whatever it turns out to be after H2 is resolved.

---

# COSMETIC

**C1 — "a three-word screening-level compression."** "Orthogonality to state power" is four words. The error appears twice (§7 and §9), both times in text new to this revision, both times in the sentence carrying the reframing's central premise.

**C2 — §7 restates §4's Cyprian sentence in near-identical but differently-worded form.** §4: "with no coercive backing **whatsoever**." §7: "with no coercive backing **available to him at all**." CO-022's *Cross-document fact consistency* section asks that the same claim from the same material either carry its exact wording across or state why it differs; the discipline is worth applying within a document too, especially where the second instance is explicitly a summary of the first.

**C3 — §9 line 241's inventory of what the document does omits §7.** *"This document performs genuine Step 1 construction work — the World Separation Criteria and Strand Determination findings at §4–§5, and the beginning/ending-point boundary reasoning at §2 — rather than redeciding anything already settled."* The World Continuity & Distinction discharge at §7 is the section the entire escalation question is about, and it is not in the list.

**C4 — §9's post-Round-5 paragraph dates nothing.** Every other revision-history paragraph in §9 dates its round and names the commit reviewed ("2026-09-01, against commit `4d10afe9`"); Step 0 §6 dates its own escalation to the day. The paragraph recording the most consequential change in the document's history gives no date at all.

**C5 — "the actual, undogmatic shape" (§1).** "Undogmatic" is an evaluative adjective doing no evidentiary work, in the clause that states the World #6 boundary, in a document that elsewhere polices exactly this kind of word.

**C6 — §9's closing paragraph refers to "the correction above" without saying which.** *"…this document applies its own reading (which does not depend on the state-power question and is unaffected by **the correction above**)…"* Several corrections are described above it. One clause fixes it.

---

## Required actions before Round 7

**Must fix (HIGH):**

- **H1 — create the record.** A dated decision artifact in this world's build folder carrying the project lead's instruction in the project lead's own words, on the model `Step0_Movement_Scope_Confirmation.md` §6 already set, cited from §8 item 12 and §9. Delete or source the inference about how the project lead "treats" the class of decision. Until the artifact exists, CO-022 forbids relying on the attribution for anything, including the withdrawal.
- **H2 — reconcile §9 with itself and escalate the category-3 item.** The category-3 paragraph and the closing paragraph cannot both stand. On the reasoning §9 itself gives, a category applies and self-disposition is unavailable. The escalation note is already drafted in §9's own category-3 paragraph.
- **H3 — correct the arc, at all three sites.** §7, §1, and §8 item 12. Read Letter 185 ch. 7 §§23–27 before rewriting, not after. Add the dates (Letter XCIII, a.d. 408; Augustine bishop 395/396; the council petition and the envoys preceding the compulsion laws). This must be done first, because §8 item 12 currently makes the inaccurate arc binding on Doc_02 and Doc_08.

**Must fix (MEDIUM):** all four. **M1** is the reframing's own incompleteness and bears directly on the escalation conclusion. **M2** puts the portfolio's own criterion-defining paragraph on the page before a claim about the phrase's interpretive capacity is allowed to stand. **M3** restores a Round-5 fix that was reverted unlogged and gives §1's cross-world claim a citation. **M4** restores evidence the reframing removed, which the reframing's own stated principle requires.

**Apply directly:** all LOW and COSMETIC. L1 is a one-word direction fix in this round's own new text and should not survive to Round 7 — this is the third consecutive round in which a direction failure has appeared in the round's own new material. L4 and L5 are the two places where this round's log is out of step with what the file does.

**Three process observations for the revision pass, not findings:**

1. **The verification discipline for texts is now excellent and has held for three rounds; the discipline for *contexts* has not caught up.** Every quotation I re-located this round was verbatim and correctly placed, including two the prior rounds never tested. What is still not being done is reading the paragraph *around* the quotation for what it says about the claim being built on it. H3 was found by reading eight sections further into a letter the document already relies on; M2 was found by reading eleven paragraphs up in a portfolio document the document already quotes. Both were one scroll away. The rule that would have caught both: before a quotation is made load-bearing, read the whole section it sits in, and say what else is in it.
2. **A rewrite is a search string, exactly as a correction note is.** Round 5's process observation 3 said: after writing a correction note, grep the section for the claim it disclaims. The same applies to a rewrite made on instruction. This revision rewrote §7's state-power paragraphs, §9's limb 3 and §9's conclusion, and left standing: §9's category-3 paragraph asserting the opposite conclusion (H2), §1 and §5 still applying the withdrawn reading (M1), §7's own "whichever reading this document adopts" (L3), §7's now-dangling "(below)" (L2), and §9's log describing the deleted text as current (L5). Five stranded dependents from ten edits. The mechanical remedy: after any rewrite, diff the file and read every paragraph that shares a noun phrase with what changed.
3. **An instruction about method is not a disposition, and the document should not let the two run together.** The project lead's reported instruction concerns how to treat the sources. §9 converts it into a conclusion about escalation categories — a different question, under a rule the instruction does not mention. The document's own segregation of this change from Round 5 was exactly right and should be kept; what it needs to segregate next is *what the instruction settled* from *what the build thread inferred from it*. As written, the second is presented in the project lead's voice.

**Escalation check performed by this review.** Category 1 (Representative identity): not touched; §1's Living Tradition Status remains PENDING and correctly routed to the project lead as a project-lead act. Category 2: **applies, narrowly.** The Coach3 item is correctly labelled and, being applied rather than decided, is discharged by labelling. The portfolio-phrase item is not fully discharged: §7 rules on the phrase's interpretive capacity, directs downstream documents to carry the arc in place of the portfolio's own ground, and §8 item 12 closes the question to reconsideration — while §1 and §5 continue to apply the narrow ground reading outright. Category 3: **applies, on the document's own words and untouched by the reframing** — §9 concedes it in one paragraph and denies it four paragraphs later; this is the decisive ground, and it requires no view about state power at all. Category 4: limbs 1 and 2 are not met and are correctly reasoned. **Limb 3 is arguable and I do not rest on it**; the document has the better of Round 5 here, since Round 5's finding rested on a conditional the document has now removed. **This review does not itself escalate**; it returns the question to the build thread with the record corrected, and states that §9's "No standing escalation category applies" cannot stand — not because the project lead's instruction was wrong, and not because reporting a documented arc is the wrong posture (it is the right one), but because the instruction does not reach category 3, because the document has not in fact stopped adjudicating in §1 and §5, because the arc as reported is inaccurate on the sources, and because CO-022 does not permit an instruction attributed to the project lead to be relied on until there is a verifiable record that the project lead gave it.
