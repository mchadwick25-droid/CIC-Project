# Doc_01 — World Identification, Boundaries, and Orientation: Latin Pastoral-Congregational Christianity
## Round 5 Independent Adversarial Review

**Document reviewed:** `worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT — revision responding to Round 4, 2026-09-01, commit `4d10afe9`, committed 18:53:30 UTC)
**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread. Did not draft the document under review, did not draft this world's Step 0, and did not write the Round 1–4 Doc_01 reviews. **Round 4's own findings, citations, quotations, arithmetic and suggested fix-texts were treated as claims to be re-derived, not as authority.** That discipline paid at three separate points this round: one of Round 4's own suggested fix-texts is defective and the revision applied it verbatim (M2); one of Round 4's own quantities is wrong and the revision transcribed it wrong in a different direction (C5); and Round 4's "everything else is clean" certification did not extend to a governing-document claim it never checked (see *What was checked and found clean*, item 2).
**Governed by:** `cic-build-cycle` (CO-022) *Review*, *Revision decision*, *Escalation categories*, *Disposition*, *Naming and term propagation*, *Cross-document fact consistency* and *Coach verification* sections; Construction Framework V7.4 Part I, Step 0/Step 1 boundary, Record Integrity Principle, Part III; Constitution V2.2 Articles 3, 4, 15, 21, 23, 29; `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx`; this world's own cleared `Step0_Movement_Scope_Confirmation.md`.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 2 HIGH · 3 MEDIUM · 9 LOW · 6 COSMETIC.**

**On the primary sources, this revision is clean, and by a wider margin than any prior round.** Every primary-source quotation I re-located this session is verbatim and correctly placed at a locus I recomputed from the XML `div` structure rather than accepted: the 256 Council of Carthage preface in full (now including both the opening clause and the closing "who is the only one that has the power both of preferring us…" continuation, both restored this round); *On Baptism* I.1.2, II.3, Book III ch. 2, Book VI ch. 2; Letter 185's Nebuchadnezzar passage (the spurious ellipsis is gone); Letter XCIII §17 to Vincentius; Cyprian's Ep. 67. Every governing-document quotation is exact, including two Round 4 never tested — Article 3's "sufficient historical coherence" (which *is* in Article 3, as a bulleted list item, contrary to what a plain grep suggests) and CF V7.4's "Nothing in Step 0 performs Step 1's own boundary-determination work," which the document deploys at §9 and which is real, correctly quoted, and — importantly — correctly used, since the CF sentence is about the portfolio-level Step 0 this document is construing. The cross-branch claims are, for the first time in three rounds, substantively accurate at every point I could check per-commit. **The stranded-duplicate-sentence bug did not recur**: a sentence-level and clause-level sweep of the whole file, plus a repeated-14-word-shingle scan, returns nothing but deliberate repetitions, and the end of §9 and the end of the document are clean. Twenty of Round 4's twenty-four findings are genuinely and often well fixed.

It fails at Round 5 on two grounds, both of which sit on the document's newest and most consequential material.

1. **The escalation conclusion does not hold, and the document's own governing Step 0 says so.** §9 names *two* items under CO-022 category 2 ("two items, both labeled") and *two* candidates under category 3, one of which it says "a coach pass or System Hub should settle" — and then concludes "No standing escalation category applies." CO-022's rule is "check it against these four categories. **If any apply, stop and escalate directly to the project lead — do not self-dispose**," and its Disposition section repeats it: eligibility requires that "none of the four escalation categories applies." Labeling is category 2's *additional* obligation, not an alternative to escalation. Decisively: **this world's own cleared Step 0 already ran this exact question and reached the opposite answer** — it found one category-4 limb-3 item, quoted the same CO-022 sentence, held that "**Because a standing escalation category applies, this document does not self-dispose, whatever any review round returns**," escalated to the project lead, obtained a decision, and recorded that self-disposition became available only "**With the escalation actually resolved — not merely disclosed**." Doc_01 does precisely what its own governing document says is insufficient: it discloses (§8 item 12, limb 3), asks "the project lead or a coach pass reviewing this disposition" to weigh the question, and then self-disposes so that the project lead is never asked. §9 never mentions the Step 0 precedent (**H1**).

2. **The Strand A inversion Round 4 found is announced as corrected at §7 and re-asserted four sentences later in the same section.** §7's own correction note reads: "an earlier draft of this revision's own gloss of Strand A as built on state power inverted what IJC's §4 actually says about it (Strand A is defined *independent of* imperial proximity, corrected here)." The next paragraph then says the boundary turns on "whether a bishop's *own office* derives its ground and legitimacy from a relationship to state power, the way Strand B's does explicitly **and Strand A's does through canon law backed by decretal authority**," and closes "where in IJC, on **two of its three strands**, state power … *is* the office's own claimed ground." On IJC Doc_01 §4's own text exactly *one* strand (B) grounds authority in state power; Strand A is "independent of a given see's political proximity to the emperor" and Strand C is "a claim about the church's independence from imperial command as such." The claim is propagated to §1 ("canon law backed by it") and to §9's category-2 paragraph ("the way two of IJC's own three strands' authority explicitly is") — and it is the sole support offered for the reading on which the whole no-escalation conclusion rests (**H2**).

Behind both sits the same underlying weakness: **the document's characterization of IJC is built entirely from a single parenthetical in IJC's Doc_01 §4 and does not consult IJC's own cleared Doc_04, which resolved that very parenthetical and reached a different picture** (M1).

---

## Method — what was actually checked

Nothing was taken on the document's, Round 4's, or any prior round's word.

- **`reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` extracted and read end to end** (89 paragraphs), not only the World #8 entry — specifically to see whether "orthogonality" appears anywhere else in the portfolio document that could disambiguate it (it does not; it appears exactly once), and to read the *Selection method* paragraph, which turns out to be the phrase's real interpretive context and which no prior round has quoted.
- **The live `cic-build-cycle` skill** at `/root/.claude/skills/synced/…/cic-build-cycle/SKILL.md`, read in full — the four escalation categories, the "if any apply, stop and escalate" rule at the head of that section, the Disposition eligibility sentence, the Record-Integrity-adjacent *Cross-document fact consistency* section, and the write-scope sentence in *Coach verification* ("A build thread's write access is scoped to its own world's build folder").
- **This world's own cleared Step 0 read in full**, including §6's complete disposition history — which is where the controlling escalation precedent is, and which no prior Doc_01 review has cited.
- **The vendored primary corpus, read directly**, with loci recomputed from the XML `div3`/`div4` structure rather than trusted: `anf05` — the 256 Council preface *in full context including the proœmium heading and both interpolated ANF editorial glosses*, and Ep. 67's congregational-rejection clause; `npnf104` — I.1.2 (Book I ch. 1), II.3 (Book II ch. 3, `div3 id="v.iv.iv"`), Book III ch. 2 (`v.iv.v`), Book VI ch. 2 (`v.iv.viii`), and Letter 185's censured-kings/Nebuchadnezzar passage in full; `npnf101` — Letter XCIII §17 (`div3 id="vii.1.XCIII" title="To Vincentius"`), read with 1,500 characters of surrounding context.
- **Governing text re-extracted from `.docx` this session:** `CiC_L1_Constitution_V2_2.docx` — Articles 3 (in full, including the bulleted "should possess sufficient: historical coherence…" list and the "influences nothing above it" paragraph), 15, 21, 29, plus an exhaustive `coheren` search across every XML part in the package; `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — the Step 0/Step 1 entry *with its surrounding context*, Part I's Distinct World Criteria, Temporal Scope, World Separation Criteria, Strand Determination and World Continuity & Distinction, and the Record Integrity Principle.
- **The sibling branch fetched fresh and interrogated per commit** — `git fetch origin claude/record-native-world-build-v2-e2s0dt`; the branch has moved again, to `c915ed69` (18:31 UTC). Marker counts computed at seven commits (`27314aa2`, `79f65c17`, `58ee86a5`, `cb178333`, `4788e5c5`, `9caf7bea`, `c915ed69`) plus `27314aa2^`; `cb178333`'s full commit message read; Donatism's Step 0 §3 B3 and §4 item 4 and its Round 2 review L8 read at the *current* head, not at the head the document names.
- **Neighbour-world documents at source:** IJC's `Doc_01` §4 (all three strand definitions and the closing governing-consequence paragraph) and §6; IJC's `Step0_Movement_Scope_Confirmation.md` §3 and §4 item 3; **IJC's `Doc_04_Gravity_Discovery.md`** — Candidate 2 in full and the whole Classification Summary table, which no prior round has consulted and which bears directly on §7's central claim; `hal_Doc_01…md` §4, §8.1 in full, and its bipolar-network/Aventine material; `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md`.
- **Both corpus-maps**, at the row level: the Letter 185 rows in `latin-pastoral-congregational-christianity.yaml` (`confidence: assigned`, "Also assigned to imperial-juridical-christianity below") and `imperial-juridical-christianity.yaml` (`confidence: provisional`, note read verbatim); the 17-letter Augustine–Jerome row (`~52,892 words`, the `tradition`-to-both note read to its end, including "A two-sided correspondence has voice on both sides. It is also the largest single thing in this volume after the Confessions."); the general-correspondence row that vendors Letter XCIII ("the remaining 138 letters"); the hal mirror row.
- **Every `§n` pointer extracted programmatically — 232 occurrences** — mapped to its containing section and checked mechanically for target existence and for above/below direction, then a sample of the evidentiary ones opened and tested for whether the target actually contains the claim. One direction failure (L1); zero non-existent targets; the M1 repoint verified landed.
- **A duplicate-sentence, duplicate-clause and repeated-shingle sweep** of the whole file (normalised sentences ≥60 chars, clauses ≥90 chars, 14-word shingles). **No stranded duplicates.** The end of §9 and the document's last two lines were read separately, character by character.
- **A full line-level and word-level diff of `e7c3251d` → `4d10afe9`**, so that "was this fix actually applied" was answered from the diff rather than from the revision log — which is how four of Round 4's six COSMETIC items were caught still unapplied (M3).
- **All four prior review artifacts' verdict lines**, to check the status line's and revision log's arithmetic.

---

## THE ESCALATION QUESTION — independent analysis and conclusion

This is the document's central new reasoning and the single most consequential judgment in it, so it gets its own section. My conclusion is stated first.

> ### Conclusion: **this document's "no escalation" reasoning does not hold. Doc_01 should be escalated to the project lead rather than self-disposed "Approved to proceed."**
>
> **This is not because the document's "ground versus instrument" reading of "orthogonality to state power" is wrong.** On the merits I think that reading is *more likely right than wrong*. My conclusion does not depend on it being wrong, and would not change if the project lead agreed with it. It rests on who is entitled to make the call, what CO-022 actually says, and what this world's own Step 0 already established as the controlling practice.

### 1. Where the phrase actually comes from — confirmed, and Round 4 was right

I extracted `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` directly. The World #8 entry reads, in full and verbatim:

> *"8. Latin Pastoral-Congregational Christianity. c. 240s–430 CE. Carthage and Hippo Regius. Cyprian as working pastor navigating the Decian persecution and its aftermath (not the schism-crisis angle, which belongs to world #4), Augustine's preaching, catechesis, and ordinary sacramental administration for his own congregation at Hippo. Ordinary lay formation, preaching, and sacramental life under episcopal office — **confirmed distinct from world #6 (non-overlapping authority structure, orthogonality to state power, temporal overlap rather than sequence)**. Cyprian and Augustine confirmed to hold together despite the roughly century-long gap between them (with Donatism occupying and contesting the interval)…"*

Provenance, checked in all four places the brief names:

| Document | What it does with the phrase |
|---|---|
| `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` | **Originates it.** Sole occurrence of "orthogonality" in the whole document. |
| This world's own Step 0 §1 (line 18) | Quotes the entry verbatim in a block quotation, as "quoted verbatim from the Step 0 Conclusion." |
| This world's own Step 0 §3 B3 (line 103) | Quotes the three-item formula again, attributing it to the Step 0 Conclusion "and independently re-affirmed in IJC's own Step 0 confirmation (§3 of that document)." |
| IJC's own Step 0 §3 | Quotes the three-item formula, attributing it to "the Step 0 Conclusion itself." |
| IJC's `Doc_01` §6 | Repeats it with an added parenthetical gloss on the first item only, expressly as "already confirmed distinct in the Step 0 Conclusion and reaffirmed in `Step0_Movement_Scope_Confirmation.md` §3." |

**§7's corrected attribution is exactly right, and the correction is well made.** The phrase originates at the portfolio level; this world's own cleared Step 0 quotes it twice; IJC repeats it. Round 4's H1 was correct on the facts, and the revision has fixed the mislocation cleanly. Credit where due: this is the best-executed part of the revision.

### 2. Is the "ground, not engagement" reading defensible? — my own view

**Arguments for it (stronger than the document itself makes them):**

1. *The metaphor is an independence metaphor, not a zero-contact one.* "Orthogonal" means at right angles — varying independently — not "absent." Two orthogonal axes can both carry non-zero values. Read straight, "orthogonality to state power" says this world's formation logic is not a function of the state-power axis, which is much closer to the ground reading than to any non-engagement reading.
2. *The portfolio document's own Selection-method paragraph fixes the register.* It says worlds were chosen for "genuine distinctiveness from the other selected worlds (formation-logic, authority structure, **relationship to power**)," and that temporally-overlapping candidates are kept separate where they are "independent, temporally-overlapping formations **with different authority structures and relationships to power**." The World #8 formula's three items map one-to-one onto that test: authority structure, relationship to power, overlap-not-sequence. So the middle item is a *comparative claim about the kind of relationship to power*, in service of a separation test — not a historical claim that the relationship is null. **This is the single best argument available for the document's reading, and the document does not make it.** No prior round has quoted this paragraph either.
3. *CF V7.4 genuinely licenses Step 1 to do the real work.* "Step 1 begins only once a specific seed has been selected from Step 0's output. Nothing in Step 0 performs Step 1's own boundary-determination work." I verified this at source and read its context: the Step 0 it describes is the portfolio-level, run-once-per-phase screening step, which is exactly the document whose phrase is at issue. §9's use of it is fair.

**Arguments against it, which the document does not engage:**

1. **The document's binary is a straw man.** §7 tests its reading against exactly one alternative: "Read as a claim that this world's episcopal office never *touches* state power, it is false." Nobody would hold that reading, and defeating it establishes nothing. The reading the portfolio's own words most naturally bear is a *middle* one: **this world's formation is not organized along the state-power axis** — a centrality claim, not a contact claim and not a narrow claim about the juridical ground of the office. The document never states this reading, never tests it, and never says why it prefers its own narrower one.
2. **Round 4's M6 fix removed the only argument that answered the middle reading.** At Round 4 the state-power half ran a centrality-versus-episodicity argument ("episodically solicited… the same centrality-of-organizing-force criterion already used above for primacy"). Round 4's M6 correctly found that argument unsupported by duration evidence, and the revision *dropped the frequency framing entirely* and rebuilt "on kind (instrument versus ground)." That fix is right on its own terms — but it leaves the centrality question unanswered rather than answered, and the ground/instrument argument does not reach it. The document is now narrower than it was, at exactly the point where the portfolio phrase is broadest.
3. **The narrowing is achieved by reading a portfolio-level phrase through a downstream document's categories — and the downstream reading is wrong.** §7 says the ground reading is "the claim IJC's own §4 shows the boundary actually turns on." IJC Doc_01 §4 is about IJC's strands; it says nothing about World #8's boundary. That inference is this document's own and is not marked as such. Worse, the §4 material it rests on is mis-stated in two ways (H2, M1).
4. **IJC's own cleared Doc_04 contradicts the "one organizing concern, two routes" framing outright.** §7 unifies both halves of the boundary on the proposition that "Primacy and state power, on IJC's own text, are two different *routes* to that single organizing concern — the juridical fixing and defensibility of ecclesiastical authority." IJC's Doc_04 `Classification Summary` records **three** confirmed Primary gravities, of which "Church-State Alliance and Its Limits" is one — cross-strand, "precondition for all three strands," and described in its own Explanatory test as "the single most load-bearing explanatory claim in this world's entire construction record to date." On IJC's own completed construction the state relationship is not a *route to* juridical fixity; it is an organizing force in its own right. Which means the axis "orthogonality to state power" names is, on IJC's own record, exactly as central as the plain reading of the phrase implies.
5. **On this world's own evidence, the projection onto that axis is not trivial.** §4 establishes that Augustine "actively solicits and defends the Roman state's coercive power"; that *The Correction of the Donatists* is a sustained letter-treatise defending it; that it runs a second, non-pastoral register arguing from the Christian ruler's own duty to legislate against error; and — new at Round 3, and still in the document — that Letter XCIII §17 records a *considered, argued change of position* held thereafter. And the corpus-map itself files the letter with IJC as "direct evidence for the ijc world's core question — the church's use of imperial law." A world one of whose two anchor figures produces direct evidence for a neighbour world's *core question* is not obviously orthogonal to that neighbour's axis, whatever is true of the ground of his office.

**My own view on the merits, stated plainly:** the ground reading is probably the better reading of "orthogonality," for argument (1) and especially argument (2). But it is *one* of at least three readings, it is not obviously the most natural one, and the document reaches it by defeating a reading nobody holds and by leaning on a characterization of IJC that is wrong in detail (H2) and superseded in substance (M1). That is not a strained reading constructed in bad faith — the document's disclosure at §8 item 12 and at limb 3 is genuinely candid, and materially more candid than any prior round's version. But it is a reading reached backwards from what the document's own evidence could satisfy, rather than forwards from what the phrase says.

### 3. Why escalation is required regardless of who is right about the reading

**(a) The document's own §9 says three escalation-category subject-matters are present.**

- *Category 2*: "**two items, both labeled**." CO-022's category 2 reads: "Portfolio-level or cross-world strategic decisions — anything decided for a reason external to this specific world's own ecology. Label it explicitly as portfolio-level in whatever document records it, distinct from an ecology-grounded finding." The document treats the labeling sentence as the whole of the obligation. It is not: the sentence at the head of the section is "**Before disposing of any document, check it against these four categories. If any apply, stop and escalate directly to the project lead — do not self-dispose, regardless of how clean the review came back**," and the *Disposition* section repeats it independently ("A document only becomes eligible for disposition when it has cleared an independent review without that review calling for substantial revision, **and none of the four escalation categories applies**"). Labeling is an *additional* requirement for category-2 content, not an alternative route.
  There is a real steelman here and I have weighed it: one could read category 2's escalation trigger as reaching only portfolio-level decisions the document *makes*, with the labeling sentence covering portfolio-level material it merely *applies*. On that reading the Coach3 item is properly discharged by labeling, and I would accept that. **It does not rescue the second item.** The second item is not applied portfolio-level material; the document construes a clause of a closed portfolio determination, decides which of two readings governs, and declares the portfolio finding "precisified by this document's own deeper construction work" — and does so partly for reasons external to this world's ecology (another document's "most charitable construction"; "what IJC's own §4 shows"). §9 states the conclusion in its own voice: "This document's own conclusion — precisified, not contradicted — is stated here for the record." That is a decision about a portfolio-level determination, made by a build thread.
- *Category 3*: the document runs it for the first time and finds two candidates, the second of which it describes as "an interpretive question about how a Constitution Article's own test is to be read, **with reach beyond this world alone**," which "is not resolved by this document's own preference for the broader reading: it is named here as a live methodological question **a coach pass or System Hub should settle**." But §5 *did* adopt the broader reading, and made a strand determination on it which, on the document's own quoted authority, "governs all subsequent strand attribution" (Article 21) and "governs all subsequent work" (CF V7.4). The methodology question is therefore both decided and used while being referred out — and referred to "a coach pass or System Hub," which is not what CO-022 names. CO-022 names the project lead.

**(b) This world's own Step 0 already decided this question, the other way, and Doc_01 does not mention it.** Step 0 §6 found one category-4 limb-3 item (the IJC records boundary breach), quoted CO-022's escalation sentence verbatim, and held:

> *"**Because a standing escalation category applies, this document does not self-dispose, whatever any review round returns.** … This document goes to the project lead for the IJC finding above."*

and, after the escalation was actually taken to the project lead and answered:

> *"**With the escalation actually resolved — not merely disclosed** — no standing category-4 tension remains open, and review converged clean at Round 5. Per CO-022, this document is self-dispositioned **Approved to proceed**."*

That is the controlling practice, set in this world, in the document Doc_01's own header names as governing it, through five review rounds, with the project lead actually in the loop. **Doc_01 does the thing Step 0 expressly says is not enough**: it discloses the tension at §8 item 12 and at limb 3, and self-disposes on the disclosure. §9's escalation assessment does not cite Step 0's precedent anywhere. Note also that the channel demonstrably exists and has been used — Step 0 records the escalation being taken and answered the same day — so escalating here is a live option, not a procedural dead end.

**(c) Category 4's own header is met on the document's own words.** The category is "**Unresolved tensions the pipeline can't close on its own** — two reviews disagreeing with each other, a contradiction between two already-cleared master documents, or a finding that cuts against an earlier decision." Limb 3's closing sentence reads:

> *"This document states its own reasoning for the reading it adopts rather than asserting the conclusion, so that **the project lead or a coach pass reviewing this disposition can weigh the same evidence and reach a different call if the reading is wrong**."*

A document that says the project lead should weigh a question, and self-disposes so that the project lead is never asked to, has identified an unresolved tension it cannot close and then closed it anyway. And note the limb's verb: "cuts against," not "contradicts." A finding that requires a portfolio determination's stated ground to be re-read in a narrower sense than its plain words in order to remain true *cuts against* that determination even where it does not flatly contradict it. §7 concedes as much in its own terms: it holds one reading of the clause "false," and describes what it does as "a real precision of the portfolio phrase."

**(d) The instrument is out of reach.** `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` is marked "Status: Closed," sits at the portfolio level outside any world-build folder, and CO-022 provides that "**a build thread's write access is scoped to its own world's build folder**." A build thread therefore cannot amend the phrase, cannot annotate it, and cannot record its adopted reading anywhere the next reader of the portfolio document will see it. The document's chosen substitute — §8 item 12, "named here for whoever next reviews this document's disposition" — is a note inside the document whose own disposition is the thing in question. That is the definition of a tension the pipeline can't close on its own.

**(e) One further consequence nobody has recorded.** IJC's Doc_01 §6 repeats the same three-item formula. If the ground reading is adopted, IJC's own cleared boundary statement is re-glossed by it. Round 3's version of §7 at least flagged this ("for whoever next touches IJC's Doc_01"); Round 4 correctly found the flag mis-aimed, and the revision removed it rather than re-aiming it. Nothing in the document now records that a second cleared world's boundary statement is affected. That is a cross-world consequence of a portfolio-level reading — squarely category 2 — and it is unrecorded (L8).

### 4. What the document does well here, and should keep

The disclosure discipline in §8 item 12 and in limb 3's final sentences is genuinely good and materially better than any prior round's. The document names the reading its disposition turns on, states that a reasonable reader could take it the other way, states what follows if they do ("this document's own §7 finding does cut against it, and this limb is met"), and invites the check. **None of that should be removed in the revision.** The fix is not to delete the candour; it is to follow it to its own conclusion — the document has already written the argument for escalating and then declined to draw it.

### 5. What I recommend

Escalate to the project lead, with a short escalation note stating: (i) the phrase, its true provenance, and the two readings; (ii) that on the ground reading the portfolio finding is precisified and on the organizing-axis reading it is cut against; (iii) that this document's own evidence (Letter 185's two registers, Letter XCIII's argued change of position, the corpus-map's double placement into IJC's core question) is real either way and is not minimized; (iv) that on IJC's own Doc_04 the church-state relationship is a confirmed Primary gravity, which bears on how broadly the phrase should be read; and (v) that the distinctness finding itself is not in question on any reading. Then let the project lead settle the reading, and record the answer. §9's substantive analysis is most of that note already.

---

## The cross-branch claim, tested at source — and this time it holds

I fetched the branch fresh. **It has moved again**: the head is now `c915ed69` (18:31 UTC), one commit past the `9caf7bea` the document names.

Marker occurrences of "(scope corrected, v3 — Round 2 L8)" in `worlds/don/Step0_Movement_Scope_Confirmation.md`, counted per commit this session:

| commit | time (UTC) | marker |
|---|---|---|
| `27314aa2^` | — | **0** |
| `27314aa2` | 15:03 | **1** |
| `79f65c17` | 15:20 | 1 |
| `58ee86a5` | 16:30 | 1 |
| `cb178333` | 16:38 | **0** |
| `4788e5c5` | 17:13 | 0 |
| `9caf7bea` | 17:55 | 0 |
| `c915ed69` | 18:31 | 0 |

Every element of the revision's corrected account checks out:

- **"That correction was made at commit `27314aa2` (15:03 UTC)"** — correct; the marker is absent at `27314aa2^` and present at `27314aa2`, and the pre-correction sentence really did append the parenthetical after both clauses ("Cyprian's Decian-persecution pastoral material **and** Augustine's ordinary preaching, catechesis, and sacramental administration, *'not the schism-crisis angle, which belongs to world #4,'*").
- **"a later commit on the same branch (`cb178333`, moving that file's own revision and review history out of the build document into a separate decision log) removed the marker along with the rest of the file's own inline history"** — correct, and the commit message supports it in detail: "Step0_Movement_Scope_Confirmation.md and Doc_01 carried extensive inline 'Corrected in vN (Round X finding Y)' annotations… The full review-round history… now lives in the new don_Decision_Log.md."
- **"while leaving the corrected reading itself unchanged at the branch's current head"** — correct at `c915ed69`, verified directly; the §3 B3 sentence the document quotes is verbatim, including the em-dashed interpolation.
- **Donatism's Round 2 review L8 is now quoted exactly** — "In the source it is a parenthesis attached specifically to Cyprian's Decian-persecution material" — verbatim at source (Round 4's L5 fixed).
- **§8 item 11's three now-false Step 0 statements all verify.** This world's Step 0 §2 A5 does quote "Cyprian and Augustine's ordinary pastoral office and sacramental care" (zero occurrences on the sibling branch now) and does state that Donatism "makes that reading binding on its own Doc_01 (its §4 item 4)" — and Donatism's §4 item 4 now binds the Coach3 shared-Cyprianic-root adjacency instead. All three are false; all three are correctly carried forward.
- **The independence claim is now evidenced rather than asserted** (Round 4's L7 fixed), and the evidence is sound: this world's Step 0 reached its final cleared state at 16:40 still describing the both-figures reading, and its own Cyprian-scoped reading was already in place at §2 A5, so the reading was reached without sight of the 15:03 correction. Doc_01's first draft is `bf0094c0`, 16:48, after that. The inference holds — though the sentence states it backwards (L5).

**Only the currency label fails.** The document says "re-fetched for this revision, 2026-09-01, head `9caf7bea`" and §9 says "Re-checked against the sibling branch's own current head (`9caf7bea`, re-fetched for this revision)." `c915ed69` landed at 18:31; this revision was committed at 18:53:30. The named head was already 22 minutes stale at commit time. The substance is untouched (`c915ed69` changes only Doc_02, the Source Registry and the Acquisition Manifest), which is why this is LOW and not MEDIUM — but it is the third consecutive round in which a claim about this branch's *current* state was false when written, and Round 4's own process observation 3 warned about exactly this and recommended "as at `<hash>`" instead of "current head." The revision took the hash and kept the label (L2).

---

## Round 4 disposition — what was actually fixed

**Genuinely fixed, verified at source (20 of 24):**

- **H1 (the "orthogonality" counterparty).** Fixed, and well. The attribution is corrected to the portfolio Step 0 Conclusion, quoted at this world's own Step 0 §1 and §3 B3, with IJC's Doc_01 §6 correctly described as inheriting it. I verified all five locations. §9's category 2 gains the item; limb 3 is re-run rather than left asserting its old conclusion; limb 2 is corrected and given the cleaner DRAFT ground; §8 item 12 is added. **Every operational instruction Round 4 gave on H1 was followed. The disposition conclusion it was followed toward is still wrong** (H1 below) and the support the new reasoning rests on is not (H2, M1).
- **M1 (§7's II.3 pointer).** Fixed. §7 now reads "§4 above records Augustine's own *On Baptism* II.3…"; §4 contains II.3 and contains the plenary-council claim. Round 3's instruction, given in words and not executed at Round 4, is finally executed.
- **M2 (two competing "entire strand structure" claims).** Fixed cleanly. Both claims are gone; the only two surviving occurrences of the phrase are the correction note itself and the Round 4 summary in §9. §1 is reconciled. This is the best-drafted fix in the revision — and, unfortunately, the paragraph it produced is where M1 (below) now sits.
- **M4 (the marker claim).** Fixed, and verified per-commit above.
- **M5 (Letter 185's second register).** Fixed, and honestly. §5 now names the pastoral register's answer as "an easy answer" it does not rest on, engages the imperial-duty register directly, states the narrower ground the answer leaves the axis on, and concedes "This document does not claim the imperial-duty register is fully absorbed by that answer." The second half of Round 4's M5 is unaddressed (L3).
- **M6 (the "episodic" state-power framing).** Fixed. The frequency framing is gone and the argument runs on kind. §1 is reconciled to it.
- **M7 (the third unassessed divergence).** Fixed, by the second of the two routes Round 4 offered: the Article 21 reading-divergence is assessed at category 3. Limb 2's completeness claim was not updated to say where it went (L7).
- **L1** — fixed; §5's Ecological-orientation bullet now actually tests a candidate, closing the last of Article 21's four criteria. **L2** — fixed; §8 item 11 now names all three now-false Step 0 statements, with the direct quotation. **L3** — fixed; the support is now "Augustine argues *with* Cyprian, disputing his ruling while claiming his communion," which does support the claim about Augustine's conduct. **L4** — fixed ("in full" removed), unlogged (L4 below). **L5** — fixed; verbatim. **L6** — fixed; category 3 is run. **L7** — fixed; the independence evidence is supplied. **L8** — fixed; the citation is split correctly between where the quotation sits (Step 0 §3 B3, verified) and where the obligation is bound (§4 item 5, verified). **L9** — fixed; limb 2 is un-narrowed and supplied with the DRAFT ground.
- **C1 and C2** — both genuinely applied in §4 (the Nebuchadnezzar ellipsis removed; the 256 preface's closing clause restored, verbatim against ANF05). Both unlogged, under a bullet that denies anything landed in §4 (M3).

**Fixed in form but not at source (1):** **M3** — the Strand A quotation is corrected and a correction note added; the argument that uses it still asserts the inverted claim, in the same section (H2).

**Applied on a defective instruction (1):** **M8** — Round 4's suggested fix-text was applied verbatim and does not parse (M2 below).

**Claimed fixed and not fixed (4):** **C3, C4, C5, C6** — all four verified unapplied against the diff (M3 below).

---

## What was checked and found clean

Recorded because this project's reviews document both sides.

1. **Every primary-source quotation is verbatim and correctly located**, at loci I recomputed. The 256 preface is now complete at both ends in §4 and matches ANF05 character for character across three sentences, with only the two interpolated ANF editorial glosses silently dropped (correct practice, and the document invokes the first of them explicitly and accurately elsewhere). *On Baptism* I.1.2 sits in `div3 id="v.iv.iii"` (Book I) ch. 1; II.3 in `v.iv.iv` (Book II) ch. 3; the "not indeed by the authority of any plenary or even regionary Council" passage in `v.iv.v` (Book III) ch. 2; "afterwards brought to light… by the authority of a plenary Council" in `v.iv.viii` (Book VI) ch. 2. Letter XCIII §17 is in `div3 id="vii.1.XCIII" title="To Vincentius"` and the quotation is exact, with the ellipsis covering only "lest we should have those whom we knew as avowed heretics feigning themselves to be Catholics." Ep. 67's clause is exact. Letter 185's censured-kings and Nebuchadnezzar material supports §4's characterization of the second register precisely as stated.
2. **Two governing-document quotations no prior round tested both check out.** (i) Article 3's "sufficient historical coherence": a plain-text grep of the extracted Constitution returns nothing, because the words are split across a bulleted list — Article 3 reads "Formation worlds should possess sufficient: / historical coherence / ecological distinctiveness / evidential support / to justify treatment as distinct worlds of participation." The document's compression is fair and the attribution to Article 3 is correct. I flag this because it is a trap: a reviewer running the obvious check would report a fabricated quotation. (ii) CF V7.4's "Nothing in Step 0 performs Step 1's own boundary-determination work" is verbatim, and — read in context, where the Step 0 it names is the portfolio-level once-per-phase screening step — genuinely supports the use §9 puts it to.
3. **Article 21, Article 15, Article 29 and Article 3's "influences nothing above it" paragraph are all exact**, as are CF V7.4's Strand Determination sentences ("This determination is made at Step 1 and governs all subsequent work"; "Record the finding explicitly: strand-singular, or strands identified with named evidence for each") and its World Continuity & Distinction guidance.
4. **All corpus-map claims are exact**, at the row level: both Letter 185 rows and their confidences, the IJC note verbatim, the 17-letter row's `~52,892 words`, 17 loci, the `tradition`-to-both note quoted to its end including "A two-sided correspondence has voice on both sides" and "the largest single thing in this volume after the Confessions," and the hal mirror row's existence. Letter XCIII is genuinely inside this world's `general correspondence` row ("the remaining 138 letters"), so "vendored in this world's own corpus" is accurate.
5. **Coach3 is quoted verbatim** at its own source in this working tree, is correctly labelled portfolio-level per CO-022 at both §5 and §9, and the "compatible with and adjacent to" characterization is accurate against its actual wording.
6. **hal Doc_01 §8.1's three quotations are verbatim**, its §4 reopening construction is real and fairly cited, and its bipolar-network and pre-Jerome Aventine findings are genuinely that document's own.
7. **The grammatical argument at §5 is correct.** In the portfolio sentence the parenthesis does close before the comma that opens the independent Augustine clause.
8. **All eight Step 0 §4 carry-forwards are discharged or correctly forwarded**, traced individually: item 1 → §5; item 2 → §7/§8 item 2; item 3 → §8 item 3; item 4 → §8 item 4; item 5 → §7 (both halves); item 6 → §7/§8 item 5; item 7 → §7/§8 item 6; item 8 → §3/§8 item 7.
9. **Step 0 §3 B3's "live, currently-unresolved" IJC records boundary breach is not a Doc_01 gap.** I checked, because B3's summary line says it requires "action before Doc_01/Doc_02 close" and Doc_01 never mentions it. Step 0 §6 records that the escalation was taken to the project lead, authorized, executed and independently verified, and logged at IJC's `Open_Gaps_Tracking.md` item 16. It is closed. (Step 0's own §3 B3 is now stale on this point — Step 0's problem, not Doc_01's, and not worth a finding here.)
10. **The status line and revision log are numerically honest on round counts.** Round 1 (9/12/9/3), Round 2 (4/10/9/6), Round 3 (1/10/9/6) and Round 4 (1/8/9/6) match the four review artifacts exactly. DRAFT is claimed; Frozen is not; Living Tradition Status is PENDING and correctly routed to the project lead.
11. **CO-022 failure-mode checks:** nothing is attributed to "the project lead" or "Mark" as a quote, decision or instruction anywhere in Doc_01; the canonical folder is correct; no review content is described as shown without being shown.
12. **Historical facts spot-re-checked and clean:** Cyprian c. 246 conversion, July 248–April 249 election, five presbyters' opposition; Novatian and Felicissimus 251; *De Unitate* c. 251 and its genuine two-recension ("Primacy Text") problem; the 255–256 councils; martyrdom 258; Augustine 386/387/391/395–396, Valerius's preaching licence contrary to African custom, Megalius of Numidia; ~9 years a Manichee; 258→391 = 133 years; Diocletianic African phase c. 303–305 against a longer legal state; the Stephen controversy as roughly two years of a ten-year episcopate; Apiarius 419 running to c. 426 within a ~35-year episcopate; 279 v. 286 bishops at Carthage 411; Vandals 429, death 28 August 430.
13. **No stranded duplicate sentence or clause anywhere in the file**, including at the end of §9 and at the document's close. The bug that recurred in two consecutive prior revisions did not recur here.

---

# HIGH

### H1 — §9 names two category-2 items and two category-3 candidates and then concludes that no escalation category applies; this world's own cleared Step 0 already ran the identical question and held that a document in this position does not self-dispose

**Where.** §9's Escalation-category assessment, category 2, category 3, limb 3 and the closing sentence; §8 item 12; against CO-022's *Escalation categories* and *Disposition* sections and against this world's own `Step0_Movement_Scope_Confirmation.md` §6.

**What's wrong.** Three things, which compound.

*First, the document treats category 2's labeling clause as discharging category 2.* §9 heads the paragraph "**Category 2 (portfolio-level/cross-world determinations), two items, both labeled**" and closes the section "No standing escalation category applies." CO-022's rule, quoted from the live skill:

> *"Before disposing of any document, check it against these four categories. **If any apply, stop and escalate directly to the project lead — do not self-dispose, regardless of how clean the review came back.**"*
> *"A document only becomes eligible for disposition when it has cleared an independent review without that review calling for substantial revision, **and none of the four escalation categories applies**."*

Category 2's second sentence ("Label it explicitly as portfolio-level in whatever document records it") is an additional obligation on portfolio-level content, not a substitute for the escalation the section's own opening sentence requires. I have set out the steelman for the document above (§*The escalation question*, 3(a)) and it rescues the Coach3 item, which is applied rather than decided. It does not rescue the second item, where the document construes a clause of a closed portfolio determination, chooses between two readings of it, and declares the portfolio finding "precisified by this document's own deeper construction work" — in its own voice, "stated here for the record."

*Second, category 3 is identified as live and then routed to the wrong place.* §9 finds §5's reading of Article 21 to be "an interpretive question about how a Constitution Article's own test is to be read, with reach beyond this world alone," which "a coach pass or System Hub should settle." But §5 adopted that reading and made a strand determination on it that, on the document's own quoted authority, governs all subsequent work. A methodology question that is decided, used, and simultaneously referred out is a category-3 item that applies. CO-022 routes it to the project lead, not to a coach pass.

*Third, and decisively, this document's own governing Step 0 already answered this.* Step 0 §6 found a single category-4 limb-3 item, quoted CO-022's escalation sentence, and held: *"**Because a standing escalation category applies, this document does not self-dispose, whatever any review round returns.**"* It escalated, the project lead answered, the underlying defect was fixed and verified, and only then did Step 0 record: *"**With the escalation actually resolved — not merely disclosed** — no standing category-4 tension remains open… this document is self-dispositioned **Approved to proceed**."* Doc_01 discloses and self-disposes on the disclosure — the exact move Step 0's own text distinguishes and rejects. §9 does not cite the precedent.

**Why it matters.** Four ways.

1. **The document has written the argument for escalating and then declined to draw it.** Limb 3's own closing sentence asks that "the project lead or a coach pass reviewing this disposition can weigh the same evidence and reach a different call if the reading is wrong," and §8 item 12 states that on the other reading "CO-022's disposition rule would point toward escalation rather than self-disposition." A document that says the project lead should weigh a question, and disposes so that they are not asked, has identified a tension the pipeline cannot close and closed it anyway. That is category 4's own header.
2. **The instrument is out of reach either way.** `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` is marked "Closed," sits outside any world-build folder, and CO-022 scopes a build thread's write access "to its own world's build folder." The document cannot record its adopted reading anywhere a future reader of the portfolio document will encounter it. §8 item 12 is a note inside the very document whose disposition is at issue.
3. **The channel exists and has been used.** Step 0 records an escalation taken to the project lead and answered the same day. Escalation here costs one note, not a stall.
4. **The reading's support is defective.** See H2 and M1. Even a reader inclined to accept the ground reading should not accept it on the evidence currently offered for it.

**This is not a finding that the ground reading is wrong.** On the merits I think it is more likely right than wrong, and I have set out the best argument for it — including one the document does not make (the portfolio's own *Selection method* paragraph, which frames the criterion as "different authority structures and relationships to power"). The finding is that the call is not this document's to make on its own.

**Fix.** (a) Escalate to the project lead per CO-022, with a short note carrying the substance §9 has already drafted — the phrase and its true provenance, the two (better: three) readings, what follows on each, the fact that the distinctness finding itself is unaffected either way, and IJC Doc_04's bearing (M1). (b) Correct §9 to state that a category applies and that self-disposition is therefore unavailable, citing Step 0 §6's own precedent by name rather than reasoning past it. (c) Either escalate the category-3 Article 21 reading question in the same note, or state why a methodology question that has already been decided and used is not a category-3 decision. (d) Keep §8 item 12 and limb 3's disclosure language — it is the best thing in the section and it is what makes the escalation note easy to write.

---

### H2 — §7 announces that it has corrected the Strand A inversion and then re-asserts it four sentences later, and the false claim is propagated to §1 and to §9's category-2 paragraph

**Where.** §7, World #6 bullet, primacy paragraph (the correction note) against the state-power paragraph; §1's Core Identity parenthetical; §9's category-2 paragraph. Against IJC `Doc_01` §4, read at source this session.

**What's wrong.** §7's primacy paragraph states the correction:

> *"…and an earlier draft of this revision's own gloss of Strand A as built on state power inverted what IJC's §4 actually says about it (**Strand A is defined *independent of* imperial proximity, corrected here**)."*

The very next paragraph asserts the inverted claim again, twice:

> *"Read as the claim IJC's own §4 shows the boundary actually turns on — whether a bishop's *own office* derives its ground and legitimacy from a relationship to state power, the way Strand B's does explicitly **and Strand A's does through canon law backed by decretal authority** — it holds…"*
> *"…where in IJC, **on two of its three strands**, state power (or apostolic succession asserted independent of it, on the third) *is* the office's own claimed ground."*

IJC Doc_01 §4, verbatim:

> *"**Strand A — Roman/Apostolic-Primacy strand.** Authority grounded in claimed apostolic succession from Peter, exercised through office, decretal, and canon law, **independent of a given see's political proximity to the emperor**."*
> *"**Strand B — Constantinopolitan/Imperial-Proximity strand.** Authority grounded in a see's political proximity to imperial power, not apostolic succession."*
> *"**Strand C — Ambrosian/Sacramental-Independence strand.** Authority grounded in a bishop's sacramental and moral leverage over any ruler, regardless of that bishop's own see's rank or apostolic pedigree — **a claim about the church's independence from imperial command as such**…"*

Three separate defects follow.

1. **"Strand A's does through canon law backed by decretal authority" asserts exactly what the paragraph above says it corrected.** It says Strand A's office derives its ground from a relationship to state power. IJC says the opposite in the same clause the document quotes correctly one paragraph earlier. It is also internally incoherent: decretal authority is ecclesiastical, not state, so "backed by decretal authority" cannot be a route by which an office's ground becomes a relationship to *state* power.
2. **"two of its three strands" is false on IJC's own text, and self-contradictory within its own sentence.** Exactly one strand (B) grounds authority in state power. The parenthetical "(or apostolic succession asserted independent of it, on the third)" identifies Strand A as the odd one out — leaving B and C as the "two," but Strand C is defined *against* imperial command. So the sentence simultaneously counts Strand A in (via the preceding clause) and out (via its own parenthetical).
3. **It is propagated.** §1: World #6's "own strand structure grounds ecclesiastical authority's own legitimacy in a relationship to state power **or to canon law backed by it**" — "it" being state power, which is the same inversion in disguised form, in the document's Core Identity. §9's category-2 paragraph: "(not constituted by a relationship to state power, **the way two of IJC's own three strands' authority explicitly is**)."

**Why it matters.** This is the sole support offered for the proposition that the ground reading is "the one IJC's own §4 shows the boundary is actually built on" — which is the load-bearing premise of §9's category-2 conclusion and, through it, of limb 3 and the disposition. Correct it and the argument becomes: *one* of IJC's three strands grounds authority in state power, one grounds it in apostolic succession expressly independent of imperial proximity, and one grounds it in independence from imperial command. That is a weaker and more interesting picture — and one the boundary can still be built on, since a world with a strand defined *against* imperial command is doing something with state power that this world is not. But it is not the picture the document argues from.

This is also the exact failure mode Round 4's process observation 1 named ("the fix's own evidence was not checked") and process observation 2 named (a fix landing in one paragraph while its dependents are left standing), operating at the shortest possible distance: adjacent paragraphs, in the same bullet, one announcing the correction and the next undoing it.

**Fix.** Delete "and Strand A's does through canon law backed by decretal authority" and replace "on two of its three strands" with an accurate count. Then rebuild the contrast on what survives: Strand B's ground is imperial proximity; Strand C is constituted by its opposition to imperial command; Strand A is expressly indifferent to imperial proximity — so on IJC's own text, two of three strands are *defined by their relation to imperial power* (one positively, one negatively) where this world's office is grounded in ordination and territorial charge and reaches for state power only instrumentally and late. That is defensible on IJC's own words. Propagate the correction to §1 and §9 in the same pass, per CO-022's *Naming and term propagation* rule.

---

# MEDIUM

### M1 — §7 presents an illustrative "for example" from IJC Doc_01 §4 as IJC "stating plainly" what unites its three strands, and builds both halves of the World #6 boundary on it; IJC's own cleared Doc_04 has since resolved that candidate and reached a different result

**Where.** §7, World #6 bullet, primacy paragraph; the same unified statement carried into the state-power paragraph and into §9's category 2.

**What's wrong.** §7:

> *"IJC's own Doc_01 §4 **states plainly what unites its three strands** despite their real disagreements: 'the shared conviction that ecclesiastical authority *should* be juridically fixed and defensible'…"*
> *"Primacy and state power, on IJC's own text, are two different *routes* to that **single organizing concern** — the juridical fixing and defensibility of ecclesiastical authority…"*

The words are verbatim. Their status is not. In IJC Doc_01 §4 they appear inside a parenthetical example, in the section's forward-looking *Governing consequence for later steps* paragraph:

> *"per the Framework, cross-strand gravity testing occurs formally at Step 4. **A candidate gravity that holds across all three strands (for example, the shared conviction that ecclesiastical authority should be juridically fixed and defensible, even where the three strands disagree sharply about its ground) is a stronger candidate** for the world's irreducible core than one that holds only within one or two."*

That is an illustration of what a strong cross-strand *candidate* would look like, explicitly deferred to Step 4 — not a settled statement of what unites the strands. §7 promotes it to "states plainly," and then uses it as the single organizing concern from which both halves of the boundary run.

**And IJC ran Step 4.** `worlds/ijc/Doc_04_Gravity_Discovery.md` records three confirmed Primary gravities:

| Candidate | Cross-strand status | Classification |
|---|---|---|
| 1. Juridical Primacy-Claiming | cross-strand (A directly; B as the same underlying logic) | **Primary** |
| 2. **Church-State Alliance and Its Limits** | **cross-strand — "precondition for all three strands"** | **Primary** |
| 3. Orthodoxy-Enforcement Through Imperial Power | cross-strand to A and B | **Primary** |

Candidate 2's own Explanatory test reads: *"Explains why church office becomes a form of state-adjacent power at all — **the single most load-bearing explanatory claim in this world's entire construction record to date**."*

So on IJC's own completed construction, the church-state relationship is not a *route to* juridical fixity; it is a co-equal Primary gravity, and the "precondition for all three strands." §7's unification is contradicted by the neighbour world's own later, cleared document — which the revision did not consult.

**Why it matters.** Three ways.

1. It is the substantive core of the M2 fix. Round 4 asked the document to "say once, in one place, what IJC's strand structure is organized from, in terms IJC's own §4 supports." The document said it once, cleanly — and said something IJC's own record does not support.
2. It cuts directly at the escalation reasoning. If the state relationship is one of IJC's three Primary gravities and the precondition for all its strands, then the axis "orthogonality to state power" names is exactly as central to the IJC contrast as the plain reading of the phrase implies — which strengthens the reading the document sets aside and weakens the narrowing to "the ground of the office."
3. It is a straightforward instance of the two rules that govern this exact situation, both of which the document could have applied. CF V7.4's **Record Integrity Principle**: *"A finding, fix, or open question is not resolved merely because a later document says it was addressed"* — read the other way here, an open candidate is not settled merely because an earlier document floated it. And CO-022's **Cross-document fact consistency** section: where two documents state the same claim from the same underlying material, "check that they actually match, or that any difference is deliberate and disclosed."

**Fix.** Either (a) cite IJC's §4 parenthetical for what it is — a candidate offered at Step 1 and since tested — and state the boundary against IJC's *Doc_04* result, which is the current cleared position and is in some ways a better foil for this world; or (b) drop the single-organizing-concern framing and run the boundary off IJC's own three strand *grounds*, which is what H2's fix leaves standing anyway. Do not leave "states plainly" attached to a "for example."

---

### M2 — the 256 preface's bracketed quotation at §7 now inverts the source's sense; Round 4's own suggested fix-text was applied verbatim without checking that it parses, and this quotation has now been wrong in three consecutive rounds

**Where.** §7, World #6 bullet, primacy paragraph.

**What's wrong.** §7 reads:

> *Cyprian's actual anti-Stephen statement is the 256 Council of Carthage preface quoted at §4 above — "neither does any of us set himself up as a bishop of bishops… **[no bishop] can no more be judged by another than he himself can judge another**" —*

ANF05, verbatim (re-located this session, in full context):

> *"…since **every bishop**, according to the allowance of his liberty and power, has his own proper right of judgment, and **can no more be judged by another than he himself can judge another**."*

The elided subject is **"every bishop."** Substituting "[no bishop]" produces a double negative — "no bishop can no more be judged by another…" — which does not parse and, read literally, asserts the opposite of what Cyprian says. Cyprian's point is that every bishop is as unjudgeable by a colleague as he is unable to judge one; the bracketed version says no bishop enjoys that immunity.

**How it happened.** Round 4's M8 gave the fix in exactly these words: *"**Fix.** '…[no bishop] can no more be judged by another than he himself can judge another.' Or drop the brackets and quote the clause whole, as §4 already does."* The revision took the first option verbatim. Round 4's own text was defective; the revision applied it without checking. That is precisely the rule Round 2 stated, Round 3 certified learned, and Round 4's process observation 1 restated in bold — "a reviewer's suggested fix is a hypothesis, not a finding" — recurring one round later on the same sentence of the same quotation. Round 3 dropped "no more"; Round 4 found it and prescribed a defective repair; Round 5 finds the repair inverted. **Three consecutive rounds, one clause.**

**Why it matters.** It is a misquotation of a primary source inside quotation marks, in the load-bearing World #6 boundary discharge, and §9 logs it as corrected ("the 256-preface bracketed quotation corrected to restore 'no more'"). Two of CO-022's checked properties at once, on the sentence the whole anti-Stephen argument rests on.

**Fix.** Take Round 4's *second* option, which is correct and which §4 already models: drop the brackets and quote the clause whole — *"…since every bishop, according to the allowance of his liberty and power, has his own proper right of judgment, and can no more be judged by another than he himself can judge another."* If compression is wanted, "[every bishop]" is the accurate bracket.

---

### M3 — four of Round 4's six COSMETIC findings are logged as fixed and are not; the two that were fixed are unlogged under a bullet that denies anything landed in that section

**Where.** §9's Round 4 "All addressed in this revision" list, against §6's table, §7's text and §9's own Round 2 and Round 3 log entries. Verified against the `e7c3251d` → `4d10afe9` diff rather than against the log.

| Round 4 item | §9's Round-4 log says | What the file shows |
|---|---|---|
| **C3** (log claims a table cell was split that was not) | *"the Ongoing/Internal cell's own log description corrected from 'split' to what was actually done — its placement note moved below the table (C3)"* | **Not done.** §9's Round-3 §6 bullet still reads verbatim: *"the Ongoing/Internal cell split, with its placement-judgment note moved below the table…"* The §6 table still holds a single Ongoing/Internal cell with three semicolon-joined forces. |
| **C4** (two findings sharing one "(L6)" label) | *"the two Round 3 findings sharing one '(L6)' citation disambiguated by round (C4)"* | **Not done.** §9 line 205 still ends "(L6)" and line 210 still ends "(L6)", with no round marker on either. |
| **C5** (the corpus-map double-places a *register*) | *"'the corpus-map… double-places a register' corrected to 'double-places the letter' (C5)"* | **Not done.** §7 now reads "runs **a second** register — … — the corpus-map itself double-places into IJC's own file"; the only change was inserting "second," and the relative clause still takes "register" as its object. The phrase "double-places the letter" occurs exactly once in the document — in this log entry, describing a correction that was not made. |
| **C6** (two applied §7 fixes unlogged) | *"two applied Round 3 fixes (the Apiarius/episcopate accuracy correction, the World #4 status update) added to the Round 3 log entry they belong to (C6)"* | **Not done.** "Apiarius" occurs zero times in §9's Round-3 log block; no World #4 status entry was added. |
| **C1** (§4's spurious Nebuchadnezzar ellipsis) | not logged; the §4 bullet reads *"no new findings landed here at Round 4"* | **Fixed** — the ellipsis is gone and the quotation is verbatim. |
| **C2** (§4's 256-preface truncation) | not logged; same bullet | **Fixed** — the closing clause is restored and verbatim. |

So the log is wrong in both directions in the same list: four claimed fixes that did not land, and two real fixes denied by an affirmative statement that nothing landed in the section where they landed.

**Why it matters.** Individually these are cosmetic; collectively they are not, for three reasons. (i) The list is headed "All addressed in this revision," and that claim is now false for a third of Round 4's findings — the same false-completeness defect Round 3's M5 and Round 4's C3 both raised, recurring at four times the scale. (ii) CF V7.4's **Record Integrity Principle** addresses this by name: *"A fix described as applied is not confirmed until the actual deployed artifact is checked directly and found to contain it. **Describing an intended edit is not the same act as verifying the edit landed.**"* (iii) The revision log is one of the few properties CO-022 makes independently checkable, and it has now carried a false "fixed" claim in three consecutive rounds — Round 3's log on C1, Round 4's log on C3 and M8, and this round's on four items at once. The trend is the wrong way.

**Fix.** Apply C3, C4, C5 and C6 for real; log C1 and C2 where they landed and delete "no new findings landed here at Round 4" from the §4 bullet; and, before writing the next "All addressed" list, diff the file against the prior commit and write the list from the diff.

---

# LOW

**L1 — the round's own newest paragraph carries the only broken cross-reference in the document.** §5's new Ecological-orientation test (added this round to close Round 4's L1) ends: *"…which remains grounded throughout in ordination and territorial charge (**§7 above**, on the same ground-versus-instrument distinction the World #6 boundary now turns on)."* §7 follows §5. Of 232 `§n` pointers extracted and checked, this is the sole direction failure and the sole mechanical defect — and it is in text added this round. This is the same class Round 3 corrected at §4 ("the 'developments already named (§2, §5)' pointer corrected to §2 only, since §5 follows §4"). Fix: "§7 below."

**L2 — the branch-state claim was stale again at commit time, for the third round running.** §5 says "re-fetched for this revision, 2026-09-01, **head `9caf7bea`**" and §9 says "Re-checked against the sibling branch's own **current head** (`9caf7bea`, re-fetched for this revision)." The branch head at the moment this revision was committed (18:53:30) was `c915ed69`, landed 18:31. The substance is unaffected — `c915ed69` touches only Doc_02, the Source Registry and the Acquisition Manifest, and I verified Donatism's Step 0 §3 B3 and §4 item 4 unchanged there — which is why this is LOW. But Round 4's process observation 3 gave the exact remedy ("name the commit hash whose content is being described and say so ('as at `27314aa2`'), rather than 'current state, re-fetched'"), and the revision took the hash and kept the "current head" label, which is the half of the advice that does not work. Fix: "as at `<hash>`," with no claim about what the head is.

**L3 — Round 4's M5 second half is neither applied nor disclosed, and §9 implies it was.** Round 4 asked: "either state §3's axis in the narrower 'who initiates' form from the outset, or defend the broader form as stated." §3 is unchanged in this revision (the diff shows no §3 edit) and still states the axis as "a bishop working to preserve fellowship with those he sharply disagrees with, rather than break it." §5 still substitutes the narrower "the axis distinguishes who initiates a break in communion over disagreement, not who later uses what tools…" Neither option was taken; the two forms are never reconciled; and §9's log reports "the narrower reading this leaves the axis on stated explicitly rather than smuggled in as the full claim (M5)," which is true of the *ground of the answer* and not of the *width of the axis* Round 4 was pressing on.

**L4 — Round 4's L4 was fixed and is unlogged.** "Step 0 §4 item 5 quotes IJC's own Step 0 §4 item 3 **in full**" is corrected to "quotes IJC's own Step 0 §4 item 3:" — verified, and correct, since this world's Step 0 item 5 does elide "named in §3 above." Neither §9's §7 bullet nor any other bullet mentions L4. The mirror of M3's other direction.

**L5 — the independence inference is stated backwards.** §5: *"Chronology, checked directly rather than assumed: `27314aa2` (15:03 UTC) predates this world's own Step 0 reaching its final, cleared state (self-disposed 16:40 UTC), **which is itself the evidence for independence** this document offers rather than asserts without it — this world's own Step 0, in its own final text, still describes Donatism's draft as holding the both-figures reading…"* The priority of 15:03 over 16:40 is what makes the independence claim *need* evidence — it establishes that the correction was available to be seen. The evidence is the second clause (the Step 0 text still describing the uncorrected reading). As written, the antecedent of "which" points at the fact that creates the doubt rather than the fact that answers it. The underlying reasoning is sound and I verified it independently; only the sentence is inverted.

**L6 — §8 item 11 routes the Step 0 corrections outside a scope that in fact contains them.** It says the three now-false statements are carried "for **whoever can next touch Step 0**, or for the branch merge," on the ground that fixing them "is outside this document's own instrument." The first half is right — Doc_01 should not reopen Step 0 — but the framing implies the build thread lacks the access. It does not: `Step0_Movement_Scope_Confirmation.md` sits inside this world's own build folder, and CO-022 scopes "a build thread's write access… to its own world's build folder." The honest form is that this is a separate change to a different, cleared document, needing its own disposition — not that nobody here can reach it.

**L7 — limb 2's completeness claim silently drops a candidate rather than routing it.** §9 limb 2 opens *"One live candidate remains, not two: the Donatism reading divergence,"* and then explains why the World #6 boundary does not belong at that limb. It says nothing about the third candidate Round 4's M7 surfaced (the Article 21 reading-divergence from IJC Doc_01 §4), which has been moved to category 3. A reader tracking Round 4's M7 through the document finds limb 2's count reduced and no pointer to where the missing candidate went. One clause fixes it.

**L8 — nothing records that IJC's own cleared Doc_01 §6 is re-glossed by the reading this document adopts.** §7 correctly establishes that IJC Doc_01 §6 repeats the portfolio formula rather than originating it. It does not draw the consequence: if "orthogonality to state power" is henceforth read as a claim about the ground of episcopal office, IJC's own boundary statement now carries that reading too. Round 3's §7 at least flagged something to "whoever next touches IJC's Doc_01"; Round 4 found the flag mis-aimed and the revision deleted it rather than re-aiming it. §8 carries twelve items and none concerns IJC. This is a cross-world consequence of a portfolio-level reading and should be on the record somewhere.

**L9 — a universal negative over the whole corpus is asserted without any account of how it was checked.** §7: *"**nowhere in this world's own corpus** does Augustine, or Cyprian, claim that his own episcopal authority is *constituted by* the state's favor or proximity."* This is the affirmative core of the ground reading and therefore of the disposition. It may well be true, and I have no counter-instance. But an unbounded negative over a corpus this document has not yet inventoried — Doc_02's Source Ecology has not been written — is exactly the move Round 3's M9 and Round 4's L7 both penalised in the cross-branch paragraph, appearing here in the paragraph that carries the most weight in the document. The available honest form is narrower and still sufficient: on the evidence this document has examined (§4's Letter 185 both registers, Letter XCIII, the 256 preface, *On Baptism*), the claimed ground is ordination, territorial charge and apostolic succession throughout, and no passage examined grounds the office in the state — with the scope of "examined" stated.

---

# COSMETIC

**C1 — §9's Round-4 entry cites Round 4's C1 for a fix that answers Round 3's C1, creating a fresh cross-round label collision inside the fix for Round 4's collision finding.** §9's §7 bullet: *"the 256-preface bracketed quotation corrected to restore 'no more'… (**M8, C1**)."* In a list of Round 4 items, "C1" is Round 4's C1 — the §4 Nebuchadnezzar ellipsis — not Round 3's C1, which is the bracket. Round 4's C4 was raised for precisely this defect and was not applied (M3); this is a second instance created in the same round.

**C2 — §9's Round-4 entry gets Round 4's own arithmetic wrong in a new way.** It says the marker "had in fact been removed from that file **eighty-seven minutes** before this revision was committed." `cb178333` is 16:38; `e7c3251d` is 18:25; the interval is **107 minutes**, and Round 4 said "1 hour 47 minutes." "1h47m" appears to have been transcribed as "eighty-seven."

**C3 — the C5 wording defect itself survives** (its false log entry is counted at M3): §7 still has the corpus-map double-placing a *register* rather than a letter. Fix: "…runs a second register — the Christian ruler's own duty to legislate against error — in a letter the corpus-map itself double-places into IJC's own file…"

**C4 — §1's quotation of Step 0 §3 B2 moves the emphasis without marking it.** Step 0 reads "plausibly the *richest* ordinary-believer…"; §1 renders it "*plausibly* the richest ordinary-believer…". The relocation serves the document's point (the hedge is what it wants to keep) and changes no sense, but an italic inside a quotation is part of the quotation.

**C5 — the vendored edition dates the council differently from the document, undisclosed.** ANF05's own proœmium heading for the text §4 quotes reads *"…Who Assembled at Carthage in the Kalends of September, **a.d. 258**, This Third Council on the Same Matter of Baptism Was Then Celebrated."* The document calls it "the 256 Council of Carthage" throughout. 256 is right on modern reconstruction and the document should keep it — but a reader following the citation into ANF05 meets 258 with no note, in a document that elsewhere discloses far smaller divergences (the *De Unitate* recensions, the Hippo province question).

**C6 — §7 restates a neighbour-world fact in different words without disclosure.** §7: "**The general** monepiscopal office structure already visible in Post-Apostolic/Sub-Apostolic House-Church Christianity (World #1) — the same inheritance IJC's own Doc_01 §6 names for World #6." IJC §6: "the **emerging** monepiscopal office structure already visible in Post-Apostolic/Sub-Apostolic House-Church Christianity (World #1, c. 70–200)." Not a misquotation — nothing is in quotation marks — but CO-022's *Cross-document fact consistency* section asks that two documents stating the same claim from the same material either carry the exact wording across or say why it differs, and the sentence expressly invokes IJC's own naming of it.

---

## Required actions before Round 6

**Must fix (HIGH):**

- **H1 — escalate.** Take the "orthogonality to state power" reading to the project lead per CO-022's *Escalation categories*, following this world's own Step 0 §6 precedent, and correct §9 to state that a category applies and that self-disposition is therefore unavailable. §9's existing analysis is most of the escalation note already; almost nothing needs to be written from scratch. Keep §8 item 12 and limb 3's disclosure language intact.
- **H2 — correct the Strand A claim at its operative site**, not only in the correction note: delete "and Strand A's does through canon law backed by decretal authority," fix "two of its three strands," and propagate to §1 and §9's category-2 paragraph in the same change set.

**Must fix (MEDIUM):** all three. **M1** rebuilds the IJC characterization on IJC's own current record rather than on a superseded parenthetical, and it feeds directly into the escalation note. **M2** is a primary-source misquotation inside quotation marks in the boundary discharge, now wrong for a third consecutive round. **M3** is revision-log integrity across four unapplied items, against CF V7.4's Record Integrity Principle.

**Apply directly:** all LOW and COSMETIC. L1 is a one-word fix in this round's own new text and should not survive to Round 6. L3 and L4 are the two places where this round's log is out of step with what the file does.

**Three process observations for the revision pass, not findings:**

1. **The verification discipline is now excellent for texts and still absent for the document's own edits.** Every primary source, every governing quotation, every corpus-map row and every cross-branch fact I checked this round was right — including two the prior rounds never tested. What is not being checked is whether the *edits* landed: four of Round 4's six cosmetic fixes are logged as applied and were never made, and the two that were made are logged as not having happened. The remedy is mechanical and takes one command: before writing the "All addressed" list, run `git diff` against the prior commit and write the list from the diff rather than from the fix plan. CF V7.4 already states the rule the document needs — *"Describing an intended edit is not the same act as verifying the edit landed."*
2. **A reviewer's suggested wording is still being applied verbatim.** Round 4 named this in bold as process observation 1, gave three examples, and prescribed re-deriving each one. This revision re-derived the branch facts (M4 fixed, cleanly and completely) and did not re-derive the one thing Round 4 handed it in quotation marks — a fix-text for a primary-source quotation that does not parse (M2). Where a review hands over words to paste inside quotation marks, the source is the thing to check, not the review.
3. **The stranded-fix pattern has now reached its shortest possible range: adjacent paragraphs.** At Step 0 it was sentences; at Doc_01 Rounds 2–3, sections and pointers; at Round 4, limbs of the same list. Here §7 announces "corrected here" in one paragraph and re-asserts the corrected error in the next. A correction note that names what it corrected is a useful device, but it is also a search string: after writing one, grep the section for the claim it disclaims.

**Escalation check performed by this review.** Category 1 (Representative identity): not touched; §1's Living Tradition Status is correctly routed to the project lead and not decided. Category 2: **applies.** The Coach3 item is correctly labelled and, on the better reading of the category, discharged by labelling since it is applied rather than decided; the "orthogonality" item is not — the document construes and decides the reading of a clause in a closed portfolio-level determination and declares the portfolio finding precisified. Category 3: **applies on the document's own account** — §5's Article 21 reading is a methodology question with acknowledged portfolio-wide reach that the document has decided and used while referring it to "a coach pass or System Hub"; §8 item 9's referral remains correctly scoped and this review endorses it again. Category 4: limb 1 is not met and is correctly reasoned; limb 2 is not met, and its DRAFT-status ground is the right one; **limb 3 is met on the document's own conditional** — the document states that if the phrase is read as a claim about historical engagement rather than about the office's ground, its §7 finding cuts against a portfolio-level decision, and it hands that question to "the project lead or a coach pass" while disposing as though it were settled. **This review does not itself escalate**; it returns the question to the build thread with the record corrected, and states that §9's "No standing escalation category applies" cannot stand — not because the document's reading of "orthogonality" is wrong, but because the call is not the build thread's to make alone, and because this world's own cleared Step 0 has already established, on the record and with the project lead in the loop, that disclosure is not resolution.
