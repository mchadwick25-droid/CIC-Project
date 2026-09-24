# Doc_01 Round 3 — Independent Adversarial Review: The Reformed Cities — Zurich & Geneva

**Document under review:** `World-Builds/Reformed-Zurich-and-Geneva/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, Revision 4, 2026-09-15), at commit `f7b5028` on branch `reformed-cities-doc01`.
**Prior rounds:** `Doc01_Round1_Review.md` — SUBSTANTIAL REVISION REQUIRED, 6 high / 13 medium / 13 low, against Revision 1. `Doc01_Round2_Review.md` — SUBSTANTIAL REVISION REQUIRED, 3 high / 9 medium / 11 low, all new, against Revision 2.
**Review date:** 2026-09-15
**Reviewer:** independent adversarial review, run in isolation per `cic-build-cycle`. No drafting context seen.

**Scope, per `CLAUDE.md`'s Round-2+ discipline and this project's cost rules.** A targeted recheck, not a re-review from scratch. The bulk of the effort went to Revision 4's own diff from Revision 3 (`git diff 647c1ca f7b5028`), on the premise this project has now had confirmed twice — that a fix round is where the next round's defects live. Round 1 and Round 2 findings were spot-checked against their original primary sources, not re-litigated.

**Sources re-opened directly for this round:**

- `reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` — Articles 21, 22, 29, extracted from `word/document.xml`
- `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — Part I, World Separation Criteria
- `reference/L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — Section 5
- `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Blueprint_V7.3.docx` — §17
- `cic-website/data/world-census.json` — VI.2, VI.9, VI.26, read as parsed JSON, quotations diffed character by character in Python
- `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml` — all nine work rows, source files counted
- `World-Builds/Lutheran-Wittenberg/Step0_Movement_Scope_Confirmation.md` §2 A3
- `World-Builds/Reformed-Zurich-and-Geneva/CiC_Reformed_Zurich_Geneva_World_Build_Thread_Launch_2026-09-15.md` (read in full — new since Round 2)
- `World-Builds/Donatism/Doc_01...md` §1 and §8; `don_Decision_Log.md`
- `World-Builds/Gallic-Monastic-Ascetic-Christianity/` (full listing + grep); `World-Builds/Cappadocian/CAPPADOCIAN_BUILD_LEDGER.md`; `Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md`; `records/worlds/`
- `world-build-docs/_cross-world/` (listing, `NEEDS-RULING.md`)
- `Open_Gaps_Tracking.md`, `rzg_Decision_Log.md`; `CLAUDE.md`; the `cic-build-cycle` skill

---

## Verdict

**SUBSTANTIAL REVISION REQUIRED.**

**2 high, 4 medium, 8 low.**

This is a different kind of verdict from the two before it, and the difference should be stated plainly rather than buried under the finding count. **Rounds 1 and 2 found the document's central judgments wrong. This round does not.** The substance of Revision 4 is sound, the confirmations are incorporated faithfully where they are incorporated, and the remaining work is bounded and largely mechanical. Nothing below asks for a re-argument.

**What Revision 4 gets right, verified rather than assumed:**

- **The Dort scope boundary is stated identically in all six places it appears.** I checked §1's masthead, §7's options list, §7's confirmation paragraph, §8 item 3, §9's Disposition bullet, `Open_Gaps_Tracking.md` item 2 and `rzg_Decision_Log.md`'s standing-exceptions item 2. Every one draws the line the same way — international Reformed dimension (the Canons, the Zurich/Geneva delegate participation, the Beza throughline) in this world's transmission; the Dutch domestic controversy (the Remonstrance, Oldenbarnevelt, the exiled Brotherhood) to VI.26; VI.9's own scope call untouched. There is no drift in the boundary's wording anywhere. This was the thing most likely to go wrong and it did not.
- **§1, §4, §5, §7 and §9 agree with each other about what was confirmed and why.** The masthead, §1's Short Description, §4's finding paragraph, §4's closing architecture line, §5's opening premise sentence, §5's finding, §7's Dort section and §9's Disposition all state one world / two strands and option 2, in compatible terms.
- **§4's evidence paragraph was not retro-fitted.** This deserves specific credit. A fix round incorporating a confirmation that matched its own tentative reading had every opportunity to go back and soften the evidence that cut the other way. Revision 4 left it exactly as Revision 3 wrote it — formation and authority still "favor treating them as two separate worlds," authority still "permanently unconverged-within-window," independent origins still named as "the single strongest fact cutting against a single-world reading." The confirmed answer is recorded without the argument for it being quietly improved. That is the discipline Round 1's H3 and Round 2's H2 were asking for.
- **§5 correctly drops "Provisional finding" and the two-world convertibility clause**, and §5's opening now rests Article 21 on a settled premise rather than a disclosed close call.
- **The Decision Log's new Living-Tradition-Status note is a *correct* use of the precedent Round 2 found inverted.** Line 40 now reads: LTS is "Not an escalation category; does not block Doc_01's own disposition, same pattern Donatism's own Doc_01 uses." I checked Donatism's Doc_01: §1 carries "**Status: PENDING**" for LTS and §8 concludes "**No escalation category applies.**" The analogy now runs the way the precedent actually runs. Round 2's H3 is genuinely closed.
- **Spot-checks on Round 1/Round 2 fixes hold after this round's edits.** Forces Framework V1.1 Section 5's Layer-1 sentence, quoted in §6 — character-exact ✓ (Round 2 M2). Article 21's two fragments in §5 — character-exact ✓. Article 22's full quotation in §6, including the Writing-From-Inside tail — character-exact ✓ (Round 1 M1a). Article 29's fragment in §1 — character-exact ✓. The Framework's six World Separation questions, run in §4 in the Framework's own order ✓ (Round 1 H4). Corpus map: nine work rows across seven distinct source files, matching §8 item 7's count ✓ (Round 2 L10); the *Selected Works* remainder still one collective row, matching §8 item 6 ✓ (Round 1 M7). Geneva 1526 alliance / 1536 break, correct in §2 Geographic Centers ✓ (Round 2 M7). Grebel baptizing Blaurock, Blaurock baptizing the rest, Blaurock not extended into Zwingli's circle — correct in §2, §7 and `Open_Gaps` item 8 ✓ (Round 2 M5, M6). *Leutpriester* for Zwingli, *Antistes* for Bullinger, explicitly not interchangeable ✓ (Round 2 L3). Wittenberg's Step 0 §2 A3(3) quoted correctly in §7, with this world's own Step 0 defect logged rather than repeated ✓ (Round 2 H1).

**The revision fails on two things, and both sit in the seam between the confirmed decisions and the document that records them.**

1. **Two portfolio-level project-lead decisions are attributed, nine times across three files, with no filed record of any kind** (H1) — and §9 defends the attribution by citing a precedent whose defining feature is the filed verbatim record it omits. This is the rule `cic-build-cycle` holds "to the same bar as Frozen," it is what discharges the escalation category the whole revision turns on, and the remedy is already sitting in this world's own folder as a worked precedent from Revision 3.

2. **Three sections still say both questions are live and escalated** (H2) — §2 twice and §6's Cell 3B — in flat contradiction of §7, §9, `Open_Gaps` items 2 and 12, and the Decision Log. One of the three leaves a Framework-required Temporal Scope answer stating the opposite of the document's own finding.

The mediums share the shape this project has now recorded three rounds running: new explanatory content added by a fix, not checked against the document it lands in. Two of the four (M1, M4) are new sentences written in Revision 4's own confirmation text.

**On the escalation-category reassessment (§9), checked independently against all four categories rather than against the document's claim about itself: §9's conclusion is correct — no category is live.** Its reasoning for one of the four is not (M2). Details under "Independent escalation-category check" below.

---

## High-severity findings

### H1. Two project-lead confirmations are attributed with no verifiable record — and the precedent §9 cites in support is one that requires exactly the record Revision 4 omits

**What the document asserts.** Revision 4 attributes both decisions to the project lead in nine places: Doc_01's masthead; §1's Short Description; §4's finding paragraph; §4's closing architecture line; §5's opening; §7's Dort heading; §7's confirmation paragraph; §9's two Disposition bullets; plus `Open_Gaps_Tracking.md` items 2 and 12 and three lines in `rzg_Decision_Log.md`. The formula is consistent: "confirmed by the project lead, 2026-09-15, in this build thread's own session."

**What `cic-build-cycle` requires:**

> "**Nothing is attributed to 'the project lead' anywhere in any document — a quote, a decision, an instruction — without a verifiable record that the project lead actually said or wrote it.** Hold this to the same bar as Frozen: a real, checkable record, not a claim."

The skill lists "content fabricated-attributed to 'the project lead'" as one of the four named failure modes CO-022 was written to close. It is not a stylistic rule.

**What exists on disk.** Nothing. `git show --stat f7b5028` shows the commit touches exactly three files — Doc_01, `Open_Gaps_Tracking.md`, `rzg_Decision_Log.md`. No confirmation record was filed. Grepping this world's folder for the project lead's words returns nothing. The confirmation is not quoted anywhere, in any of the three files, in any form. A reader has the assertion and the date and nothing to open.

**Why this is High rather than Medium: §9 invokes a precedent that sets the opposite standard.**

> "Neither confirmation is this document's own self-certification; both are the project lead's own word, given directly in response to the specific options this document presented, **the same evidentiary standard this project's other build threads use for a project-lead decision (e.g. Gallic's own "ADMITTED... Mark's own word, in session")**."

I checked every instance of that standard in the repository. **All three record the project lead's verbatim words alongside the date:**

- `Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md` (the actual home of the quoted phrase — see L3): "**ADMITTED, 2026-09-13.** Mark's own word, in session, in direct response to the M3 report above: **'yes, admit it.'**"
- `World-Builds/Gallic-Monastic-Ascetic-Christianity/gallic_Representative_Construction_Notes_Renatus.md` §285: "CONFIRMED, 2026-09-12. Mark's own word, in session, in response to the presentation below: **'Confirm as drafted.'**"
- `World-Builds/Cappadocian/CAPPADOCIAN_BUILD_LEDGER.md` §188: "**Status: CONFIRMED, 2026-08-31.** Mark's own word, in session, in response to the presentation above: **'Confirm as drafted.'**"

And Gallic's own file states the discipline in terms, at line 488:

> "Section 6's Living Tradition Status Confirmation updated in place from PRESENTED to CONFIRMED, **with the date and the verbatim confirmation recorded there and here** (this project's own standing discipline: nothing is attributed to the project lead anywhere without a verifiable record that he actually said it)."

Revision 4 cites this standard and meets neither half of it — no verbatim confirmation, no record. The claim "the same evidentiary standard this project's other build threads use" is false as stated: the standard those threads use is strictly higher than what Revision 4 supplies, and the sentence asserting the match is itself new in Revision 4.

**This is the third round running in which a precedent claim, offered in support of a fix, turns out to say something other than what the document says it says.** Round 2's H3 (the Donatism LTS analogy, which inverted the rule it cited) and Round 2's M3 (the `don` registration precedent, which the repository contradicted) are the same shape. This instance is worse than either, because what rests on it is not a formatting question — it is the discharge of the escalation category that barred disposition of the entire document.

**One thing this finding is not.** I am not asserting the confirmations are untrue. Three files record them consistently, the commit message records them in the same terms, and nothing in the repository contradicts them. The probability that they are genuine is high. But `cic-build-cycle`'s rule is deliberately indifferent to that: the bar is a checkable record, "not a claim, however specific or confident it sounds." A reviewer, a coach thread, or the project lead six months from now has no way to check what was actually asked and what was actually answered — and §4's own finding paragraph makes clear the evidence was genuinely balanced, so what exactly was put and what exactly came back is load-bearing, not ceremonial.

**What the correct handling is.** Exactly what Revision 3 did for the launch instruction two commits ago, and what Gallic and Cappadocian do for theirs: file the confirmation in this world's build folder as its own dated record, reproducing the project lead's own words verbatim alongside the options as they were actually presented, and cite it by path from each of the nine places that currently assert it. The precedent is `CiC_Reformed_Zurich_Geneva_World_Build_Thread_Launch_2026-09-15.md`, in this same folder, written to close the lesser version of this same defect (Round 2's M1). If the exact wording cannot be reproduced, say so plainly in that record and state what can be attested — but do not leave the attribution standing on the formula Round 2 already rejected ("this thread's own session," unfiled).

### H2. Three sections still state both questions are live and escalated, contradicting §7, §9 and both supporting files — and one of the three leaves a Framework-required answer stating the opposite of the document's own finding

Revision 4 updated §1, §4, §5, §7, §8 item 3 and §9. It did not update §2 or §6. Three statements survive unchanged and now say the opposite of the document's own settled findings.

**(a) §2, Temporal Scope — the most consequential of the three.**

> "Transitional — the Synod of Dort (1618–19) is the one development inside this window whose own status as internal-to-this-world versus a hand-off to a neighboring, differently-scoped world **is a live, escalated question (§7 below)**, precisely because Dort marks the point at which the Reformed movement's own doctrinal self-definition becomes an international and specifically Dutch-political affair."

§7 says it is confirmed. §9 says the category is "discharged, not live." `Open_Gaps` item 2 says "CONFIRMED 2026-09-15." A reader who follows the §7 pointer this sentence supplies finds the contradiction immediately.

This is not only stale labelling. This sentence is the document's answer to one of Part I's Temporal Scope questions — "What developments indicate transition?" — which Round 1's H4 flagged as unanswered and specifically identified as "where Dort belongs as a Doc_01 question." The confirmation now supplies the answer directly: the international Reformed dimension is internal to this world's transmission, and the hand-off point is the Dutch domestic controversy. Revision 4 leaves a required Framework answer reading "this is an open escalated question" when the document elsewhere records the answer. Under `cic-build-cycle`'s own revision test, correcting this "changes... a scope boundary" and is substantial by definition.

**(b) §2, Historical Pressures.**

> "...and, at the window's far end, the Synod of Dort (1618–19), **addressed as an escalated scoping question in §7 below**."

Same defect, second location, same false cross-reference.

**(c) §6, Cell 3B of the six-cell sketch.**

> "The Dort scoping question and the Zurich/Geneva architecture question (§7, §9 below) **mark real, escalated boundaries** this world transmits toward — Cell 3B."

Worse than (a) and (b), because the architecture question is no longer a question at all — §4 closes it with "**Confirmed architecture: one world, two strands.**" Cell 3B describes a settled premise as a live escalation. This cell is Layer-1 forces content that Doc_08 will compile from, so the stale characterization propagates forward into a later document rather than staying inside Doc_01.

**Why this is High.** Round 2 graded the §4/§5 contradiction High on the reasoning that a document stating opposite things in two places has not made the finding it claims. The same reasoning applies with more force here, because what is contradicted is the *disposition*: §9's category-2 clearance ("Both questions that triggered this category are now confirmed rather than open") is directly denied by the document's own §2 and §6, which state that both questions are open. §9's escalation reassessment — the sentence on which "Approved to proceed" is to be self-applied — is contradicted by the document it assesses. A reviewer reading §2 and §6 alone would conclude the escalation still stands.

`cic-build-cycle`'s propagation rule is the governing one and it is stated for exactly this: "Whenever a name or term changes, check every file it appears in... A fix that lands in the narrative document without the index being updated to match is not a complete fix." Round 2 applied it within a single document; it applies again here, within a single document, to the same document, one revision later.

**What the correct handling is.** Rewrite §2's Temporal Scope "Transitional" answer to state the confirmed boundary as the transition test's actual answer, citing §7. Correct §2's Historical Pressures pointer. Rewrite Cell 3B so it records what the confirmed boundary means for the Ending/Transforming cell rather than describing two escalations that no longer exist. Then grep the whole document and both supporting files for "escalat", "PENDING" and "provisional" once more before committing — the residuals at L6 below are what that grep turns up after these three are fixed.

---

## Medium-severity findings

### M1. The Dort delegate evidence is upgraded from hedged to "documented" inside the new confirmation text, contradicting §8 item 3 two pages later

**What §7 establishes, correctly hedged** (unchanged from Revision 3):

> "Separately, **per standard Reformation historiography — not independently verified against a primary vendored source this pass** — an international Reformed delegation attended the Synod of Dort, including two delegates from Geneva itself... and a joint delegation from the Swiss Reformed cantons..."

**What Revision 4's new confirmation paragraph says**, four lines later:

> "Doc_02 may cite the Canons of Dort as a document with **documented** Zurich/Geneva delegate participation and the Beza throughline as this world's own transmission..."

**And `Open_Gaps_Tracking.md` item 2, also new in Revision 4:**

> "Dort's international Reformed dimension (the Canons, **the documented Zurich/Geneva delegate participation**, the Beza throughline) is this world's own transmission, citable in Doc_02..."

**And §8 item 3, in the same revision:**

> "The Swiss/Genevan delegation to Dort **remains unconfirmed against a primary source** and should be researched properly before Doc_02 relies on it at higher confidence than stated here."

The same claim is "not independently verified" in one place, "unconfirmed against a primary source" in another, and "documented" twice in between. Both "documented" instances are new in Revision 4. The sentence that upgrades the claim is also the sentence that licenses Doc_02 to cite it — so the upgrade lands precisely where it does the most work, and `Open_Gaps_Tracking.md`, which is the file Doc_02 will actually read for the standing caveat, carries the upgraded version rather than the hedged one.

This is the same asymmetry Round 2's H2(b) recorded: evidence stated at one confidence where it supports the finding and at another where it constrains it. The historiography is almost certainly right — Round 1 independently confirmed Diodati and Tronchin, and contributed the Swiss cantonal delegation itself — but `CLAUDE.md`'s rule is about calibration, not about whether the claim happens to be true: "Never present a disputed claim as settled," and "Every quote must be re-verified verbatim against the vendored source file."

**What the correct handling is.** Use one formulation everywhere: the delegate participation is attested in standard Reformation historiography and is not yet verified against a vendored primary source. Carry that wording into §7's confirmation paragraph and `Open_Gaps` item 2 verbatim, per the cross-document fact-consistency rule. Note that the confirmed scope decision does not depend on the delegate claim's confidence level — so nothing is lost by stating it honestly.

### M2. §9's fourth-category clearance rests on "no objection has been raised," which is circular, inaccurate as a description of the review record, and replaces a disclosure Revision 3 carried

**Revision 4, §9:**

> "**Unresolved tension the pipeline can't close on its own: does not apply.** The Step 0 sequencing question is treated as a disclosed, filed exception (`CiC_Reformed_Zurich_Geneva_World_Build_Thread_Launch_2026-09-15.md`), named plainly in this document's own masthead rather than smoothed over; **no reviewer or project-lead objection to that framing has been raised.**"

Three problems.

**(a) It is circular.** The "disclosed, filed exception" framing was introduced in Revision 3 and has never been reviewed — Round 3 is the first review to see it. Asserting that no reviewer has objected, inside a document submitted to the review that would object, is the self-certification `CLAUDE.md` names directly: "A blocking review finding can't be dismissed by self-certification — it needs independent re-confirmation." Round 2's H3 made the same finding about the previous version of this same bullet.

**(b) It is not an accurate description of the review record.** Objections to treating the Step 0 sequencing problem as a non-escalation *were* raised, twice. Round 1's H1 found it squarely: "Building Doc_01 on a Step 0 that (a) has not cleared review, (b) explicitly forbids a build thread opening on its strength... is an 'unresolved tension the pipeline can't close on its own' — the fourth escalation category." Round 2's M1 offered escalation as one of its two acceptable remedies. Revision 3 took the other remedy — filing the launch record — which is legitimate and which I find sufficient (see the independent check below). But "no reviewer... objection to that framing has been raised" is not what the record shows, and the accurate sentence is both available and stronger: *Round 1 H1 and Round 2 M1 each raised this; Revision 3 closed it by filing the launch instruction, the first of the two remedies Round 2 named; the filed record shows the project lead authorized the exception directly, which is the disposition category 4 routes to.*

**(c) It removes a disclosure rather than completing an assessment.** Revision 3's version of this bullet ended: "If the project lead's own reading of that record differs, that disagreement is itself the kind of tension this category exists to catch, and should be named directly rather than assumed resolved by this document's own citation of it." Round 2's H3 criticized the *hedge-then-adopt* pattern — naming the condition under which the conclusion fails and adopting it anyway. Revision 4 resolved that by deleting the hedge and keeping the conclusion, which is the wrong half to delete: Round 2's point was that the assessment had not been made, not that the disclosure was surplus. What replaces it is an assertion of no objection, which is weaker than what it replaced. The removal is not disclosed anywhere.

**What the correct handling is.** State the actual ground for the clearance: the filed launch record shows the project lead — the person category 4 escalates *to* — directly authorized this build despite Step 0's own instruction, in Step 0's own words, which closes the tension rather than merely disclosing it. Drop the "no objection" sentence. That reasoning is sound, checkable against a filed path, and does not depend on what any reviewer has or has not said.

### M3. The confirmed cross-world boundary is recorded only in this world's own three files — nothing a future VI.26 or VI.9 build would read carries it

§7's confirmed option 2 places a standing obligation on a world that has not been built:

> "...requires Doc_02 to hold a line (international-Reformed-dimension in, Dutch-domestic-politics out) **that VI.26's own eventual build must also respect**."

I checked where that obligation is actually recorded. It appears in Doc_01 §1/§7/§8/§9, `Open_Gaps_Tracking.md` item 2, and `rzg_Decision_Log.md` — all inside `World-Builds/Reformed-Zurich-and-Geneva/`. Nowhere else. The census entries themselves are untouched: VI.26's `relationsSummary` still reads "gives Dort itself a named home (paired with VI.9's scope line)" and VI.9's still carries "the standing scope line: whether this entry is supporting-context or its own tradition remains a real Step 0 call." `world-build-docs/_cross-world/` holds nothing on it (`NEEDS-RULING.md` is a generated corpus-assignment register, not the right home). A build thread opening VI.26 would read the census, find the scope question described as open, and have no way to discover that part of it was decided on 2026-09-15.

This is `cic-build-cycle`'s propagation rule applied at portfolio scope — "check every file it appears in... A fix that lands in the narrative document without the index being updated to match is not a complete fix" — and it is the specific reason the skill requires portfolio-level decisions to be "label[led] explicitly as portfolio-level in whatever document records it." §7 does label it. The label just does not reach the documents that need it.

**This is not a request that the build thread edit the census.** The skill scopes a build thread's write access to its own world's build folder, and the census and `_cross-world/` are outside it. The correct handling is to name the propagation obligation explicitly — in `Open_Gaps_Tracking.md` as its own numbered entry, and in §8 — as an item owed to the project lead or a coach thread: the confirmed boundary needs registering where VI.26's and VI.9's future builds will actually encounter it. Right now the obligation is asserted on VI.26 and recorded nowhere VI.26 will look.

### M4. §9 re-introduces the "all findings addressed" self-certification Round 2 named — and it is again not accurate

**Revision 4, §9:**

> "This document has been through two independent adversarial review rounds (`Review-Artifacts/Doc01_Round1_Review.md`, `Round2_Review.md`), both SUBSTANTIAL REVISION REQUIRED, **with all findings from both addressed in the revisions that followed.**"

Round 2's H3 recorded this exact sentence shape in Revision 2 — "All findings from `Review-Artifacts/Doc01_Round1_Review.md` are addressed above" — as "a self-certification of the kind `CLAUDE.md` names directly... and it is not accurate." Revision 4 restores it in new text, with the scope widened to both rounds.

It is again not accurate. Two Round 2 Low findings are still open, which I verified directly rather than inferring:

- **Round 2's L1** — the VI.9 `relationsSummary` quotation in §7 is still not character-exact. Diffed in Python against the parsed census: the census's plain hyphen in "its own tradition **-** a real Step 0 call" is still rendered as an em dash, and the curly apostrophe in "Remonstrants**’** own entry" is still a straight one. Unchanged since Revision 2.
- **Round 2's L11** — `rzg_Decision_Log.md` line 23 still records the review rounds as "model=Opus," which neither review artifact states; and `Open_Gaps_Tracking.md`'s trailing Doc_01 status block is still unnumbered, against `CLAUDE.md`'s "Entries are append-only and numbered."

`rzg_Decision_Log.md` line 27 carries the same claim ("All 23 Round 2 findings are addressed"). Under `cic-build-cycle`'s coach-verification standard — "that the Decision Log matches what's actually on disk" — this is the same failure Round 2 recorded at its M9: a log that records a finding as closed when it is not is no longer an audit trail.

**What the correct handling is.** Fix L1 and L11 (both are one-line changes), or record them as outstanding. Then state what is true — that both rounds' findings were worked through and which, if any, remain — rather than certifying completeness in the document's own voice.

---

## Low-severity findings

**L1.** The masthead's revision line was not updated: "**Date drafted:** 2026-09-15. Revised: 2026-09-15 (Revision 2); 2026-09-15 (Revision 3)." Revision 4 is missing, in a document whose status line two lines above says "DRAFT, Revision 4."

**L2.** `Open_Gaps_Tracking.md`'s trailing status block still reads "**Doc_01 — World Identification, Boundaries, and Orientation.** DRAFT, **Revision 3** as of 2026-09-15" — immediately above a bullet describing Revision 4.

**L3.** §9's precedent citation is pathless and mislocated. "Gallic's own 'ADMITTED... Mark's own word, in session'" — the elided quotation is character-exact on both retained fragments, and the entry it comes from is genuinely about Gallic, but it lives in `Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md` (a fleet-level file), not in `World-Builds/Gallic-Monastic-Ascetic-Christianity/`, where a reader told it is "Gallic's own" would look. Gallic's own build folder uses "CONFIRMED," not "ADMITTED." Every other source in this document is path-cited; this one is not. (The substantive problem with this citation is H1; this is the locus half.)

**L4.** Round 2's L1 is unfixed — VI.9's `relationsSummary` quotation in §7 is still not character-exact (see M4 for the diff). Round 2 noted that the VI.26 quotations in the same bullet list *are* exact, which makes the inconsistency internal to one bullet.

**L5.** Two census field attributions in §7 are wrong or vague. VI.26's addition date is cited to "the census's own `dateRationale`-adjacent field" — it is in `statusDescription` ("Proposed by the Era 7 Step 0 run. Added at the Era 7 Freeze (Mark, 2026-08-02)"), and VI.26 has no `dateRationale`. And VI.9 is said to have been "Reviewed at the same **2026-08-02** Era 7 Step 0 run per its own `statusDescription`" — VI.9's `statusDescription` dates nothing; 2026-08-02 is the Freeze date, and VI.26's own field names the Step 0 run and the Freeze as two distinct events. This is Round 2's L2 recurring in a new form.

**L6.** Residual provisional vocabulary after the architecture was confirmed. §5: "This world's own coherence, **on the single-world premise**, rests on Bullinger's mediation." §8 item 2: "the strand bridge this world's **single-world premise** rests on." "Premise" reads as a working assumption; §4 now calls it settled. Cosmetic in isolation, but these are what a grep for residuals turns up after H2's three are fixed.

**L7.** §7's confirmed boundary says "VI.9 continues to hold the broader Dutch Reformed devotional culture." VI.9's own census `why` names more than that — "where the era's sharpest intra-Reformed contest was fought out and decided — and the culture of refuge that made the Netherlands the printing-house and shelter of a good part of the era's dissent." The narrower characterization was acceptable as one option's description in Revision 3; now that option 2 is the recorded scope decision, a description of what a neighbouring entry holds ought to match that entry's own text, per the cross-document fact-consistency rule.

**L8.** Round 2's L11 is unfixed in both halves: `rzg_Decision_Log.md` still records "model=Opus" for reviews whose artifacts record no model, and `Open_Gaps_Tracking.md`'s trailing status block is still unnumbered. Separately, the Decision Log's section heading "Standing exceptions and escalations" now lists two items (2 and 3) that are confirmed rather than standing — the heading no longer describes its contents.

---

## Independent escalation-category check

Run against all four categories fresh, on the document's own final content, not on §9's claim about itself.

**1. Representative identity, name, or title decisions — not live.** §5's cross-strand paragraph is the only place this comes near. It establishes that the two-strand structure is real and substantial, states that this "directly bears on the Representative-construction question... a single Representative versus a genuine multi-figure Representative," and then declines it explicitly: "This document does not decide the Representative question itself; per this build's own escalation categories, that decision is reserved for the project lead directly, at Step 10." I checked this against the filed launch record, whose stop-condition 2 names this world's one-versus-multi-figure choice specifically as "exactly the kind of framing decision this stop condition exists for." Doc_01 neither makes nor prejudges it. **Correctly assessed; the category does not attach.** Worth noting that the confirmed two-strand finding materially shapes that Step 10 decision, and §5 says so — which is the right handling, since informing a reserved decision is not making it.

**2. Portfolio-level or cross-world strategic decisions — discharged in substance, but the discharge rests on an unfiled attribution.** Both questions genuinely are portfolio-level (each turns on facts about other census entries, external to this world's own ecology), both are labelled portfolio-level where recorded, as the skill requires, and both are confirmed by the project lead rather than self-resolved. On the facts as I have been able to establish them, the category is discharged and §9's conclusion is right. Two qualifications: the discharge is evidenced only by the document's own assertion (H1), and the resulting cross-world obligation on VI.26 is recorded nowhere VI.26 would find it (M3). Neither re-opens the category; both are conditions on it being properly closed. Note also the contrast with Donatism's own Doc_01 §8, which makes a point of "no obligation placed on World #8's own future build" — here an obligation *is* placed on VI.26's future build, which is what the confirmation decided and is therefore legitimate, but it raises the propagation duty at M3 rather than lowering it.

**3. Governance or methodology decisions — not live.** Nothing in Revision 4 changes how the build process works. The masthead's registry-timing point is the closest: it withdraws Revision 2's false `don` precedent and "names the question as open" rather than deciding when a world code enters `records/worlds/`. Naming a governance question as open, without resolving it, is not a governance decision. **Correctly assessed.**

**4. Unresolved tension the pipeline can't close on its own — not live, but not for the reason §9 gives.** I tested all three of the skill's named instances plus the general case:

- *Two reviews disagreeing with each other* — Rounds 1 and 2 do not disagree; Round 2 re-verified Round 1's findings independently and confirmed them. This round disagrees with the document, not with a prior review. No.
- *A contradiction between two already-cleared master documents* — Step 0 is DRAFT and not cleared, so the Step 0 defects logged at `Open_Gaps` items 8 and 11 cannot trigger this limb. No.
- *A finding that cuts against an earlier decision* — the two logged Step 0 defects (the superseded "no figure overlap" claim; the Trent misquotation) are citation and factual errors in Step 0's distinctness section. Neither bears on Step 0's Tier-1 viability rating, which is the earlier decision in play; the filed launch instruction asked for exactly this kind of finding to be "report[ed] plainly," and Doc_01 reports both. No.
- *The Step 0 sequencing exception* — this is the one §9 addresses, and its conclusion is right: the filed launch record shows the project lead authorized this build directly, having been shown Step 0's own unreviewed status in Step 0's own words. Category 4 routes unresolved tensions *to* the project lead; here the project lead already ruled, and the ruling is filed and citable by path. That closes the tension rather than disclosing it. §9's stated reasoning ("no reviewer or project-lead objection to that framing has been raised") does not establish this and is separately defective (M2), but the underlying clearance holds on better grounds than the ones given.

**Conclusion: no escalation category is live against Doc_01's current content.** §9 reaches the right answer on all four. Its reasoning is sound on two, thin but adequate on one, and unsound on one (M2). H2 is the sharpest problem here: §9's category-2 clearance is flatly denied by §2 and §6, which still tell a reader both questions are open — so the assessment is correct but the document does not currently support it.

---

## What would close this round

None of this is a re-argument. All of it is bounded.

1. **File the confirmation record** in this world's build folder — the project lead's own words, the options as actually presented, the date — and cite it by path from all nine places that currently assert it. Follow `CiC_Reformed_Zurich_Geneva_World_Build_Thread_Launch_2026-09-15.md`, in this same folder, and Gallic's `gallic_Representative_Construction_Notes_Renatus.md` §285/§488. Correct or drop §9's "same evidentiary standard" sentence — as written it claims a match with a standard the document does not meet. (H1)
2. **Update §2's two Dort statements and §6's Cell 3B.** §2's Temporal Scope answer should state the confirmed transition boundary as the answer to Part I's "what developments indicate transition," not as an open escalation. Then re-grep the document and both supporting files for "escalat", "PENDING", "provisional" and "premise" and clear what remains. (H2, L6)
3. **Use one confidence formulation for the Dort delegate evidence** in §7's confirmation paragraph, §8 item 3 and `Open_Gaps` item 2 — the hedged one, carried across verbatim. (M1)
4. **Rewrite §9's category-4 bullet** to rest on the filed launch record rather than on the absence of objections, and restore or replace the disclosure Revision 4 removed. (M2)
5. **Add an `Open_Gaps_Tracking.md` entry** for the cross-world propagation duty: the confirmed Dort boundary is recorded only in this world's folder and needs registering where VI.26's and VI.9's future builds will encounter it — owed to the project lead or a coach thread, since the census and `_cross-world/` are outside this thread's write scope. (M3)
6. **Fix Round 2's L1 and L11** (the VI.9 quotation, "model=Opus", the unnumbered status block), then correct the "all findings from both addressed" claim in §9 and the Decision Log to say what is actually true. (M4, L4, L8)
7. **Apply L1, L2, L3, L5, L7** — the revision line, the Open_Gaps status block, the Gallic citation path, the two census field attributions, and the VI.9 characterization.

Items 2 through 7 are wording and citation work. Item 1 is a file that needs writing. On my reading, a Revision 5 doing these would clear, and this document is much closer to that than the finding count alone suggests.

---

*Filed per `cic-build-cycle`: review rounds exist as files, not claims. Three procedural notes, none a finding against the document's content. (1) `Review-Artifacts/Doc01_Round1_Review.md` and `Round2_Review.md` both entered git history in the same commits as the revisions they prompted (`58b30b0`, `647c1ca`); Round 2 flagged this as a pattern worth a coach thread's attention, and it recurs. This artifact is written before any Revision 5 exists, which is the handling the skill's "review rounds exist as files" rule reads most naturally. (2) Round 1's note on the `Ministry/` versus `Review-Artifacts/` placement inconsistency in `CLAUDE.md` stands unresolved through three rounds; this review follows the same precedent both prior rounds did. (3) This review was run from an isolated worktree at detached `f7b5028`; the branch `reformed-cities-doc01` is checked out elsewhere. The reviewed content is the branch tip as the brief specified.*
