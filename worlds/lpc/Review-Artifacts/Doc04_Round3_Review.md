# Doc_04 — Gravity Discovery: Latin Pastoral-Congregational Christianity
## Round 3 Independent Adversarial Review — fix-pass verification of Round 2's 27 findings, plus a fresh adversarial read

**Documents reviewed (working tree, branch `lpc-doc04-round2`, at `1e6bbc04`, tree clean):**
- `worlds/lpc/Doc_04_Gravity_Discovery.md` (227 lines) — read in full; both tables parsed programmatically cell-by-cell; all 28 Interaction Matrix pairs machine-checked for symmetry and then checked cell-by-cell against each candidate's own §3 Interaction bullet; the pre-fix state retrieved from git (`775b6299`) and diffed against HEAD (`1e6bbc04`) at `-U0`, all 30 hunks read individually, so that "not fixed" could be distinguished from "reworded" and from "byte-identical", and so that every site Round 2 named could be checked for whether it was touched at all
- `Review-Artifacts/Doc04_Round2_Review.md` (412 lines) — read in full; every one of the 27 findings (H1–H7, M1–M7, L1–L10, C1–C3) checked individually at its own named site, against the pre-fix text and against source. Round 2's own quotations were **not** trusted either: where the fix pass reproduces a quotation Round 2 supplied, the quotation was re-derived from the cited file (this caught one, see L1 below)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines) — read in full at §2 (the transition-criteria summary), §4 (all three authority axes, the "what stays constant" pair of paragraphs, the two deferred World Separation questions, the Conclusion), §5 (Strand Determination, all three Article 21 criteria, the Article 3 argument, the governing-consequence paragraph and the reopening caveat), §6 (the "what was it refusing" and "what was it responding to" paragraphs, the six-cell table, the placement note), §8 items 6, 7, 10; direct greps run for `does not clearly touch`, `closest call`, `right of communion`, `proper right of judgment`, `not yet closed`, `with particular weight`, `once made, governs`, `not fully closed`
- `Doc_02_Source_Ecology.md` — §1 (the 256-preface quotation, split on sentence boundaries and read clause-by-clause), §2 (both Influence dimensions in full), §5, §6, §7, §8 (the Confidence Map bracket) read verbatim; grepped for `right of communion` (**0**), `proper right of judgment` (1, §1), `lay-confessor` (0)
- `Doc_03_Lexicon_Candidate_List.md` — rows 26, 27, 28, 40, 46, 47, 55, 63 parsed cell-by-cell from the raw table (term, definition, phase, tags, Registry sources, evidentiary ground, Tier 1); the `preaching` and `catechesis` tag cells, the 119, 31 and 687 figures and each figure's own scope qualifiers re-derived from the cell each sits in
- `Source_Registry.md` — confidence letters for rows 1, 2, 4, 12, 13, 15, 18, 19, 21, 22, 23, 65, 192 parsed by field rather than read from prose; rows 1 and 65 read in full
- `lpc_Decision_Log.md` — the new 2026-09-13 (later) Doc_04 Round 2 fix-pass entry read in full and tested against the file it describes
- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — extracted verbatim (python `zipfile` + regex on `word/document.xml`); Part III read in full: the gravity definition, Candidate Gravity Generation, all six test statements, Gravity Classification (all three paragraphs), the Confidence/Gravity Cross-Check
- `L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — same extraction; Layer 3 and Section 4's Step 4 entry read verbatim
- `L1-Foundation/CiC_L1_Constitution_V2_2.docx` — same extraction; Articles 21 and 22 read verbatim, and the whole file grepped for `reopen` and `revisit`
- `worlds/ijc/Doc_04_Gravity_Discovery.md` — Candidates 4 and 5, the summary table and Open Item 4 spot-checked against the five IJC precedent claims Round 2 cleared, to confirm the fix pass did not disturb them

**Review date:** 2026-09-13
**Reviewer:** independent adversarial review thread. Did not draft Doc_04, did not draft the Round 2 review or the Round 2 fix pass, did not draft Doc_01, Doc_02, Doc_03 or the Registry, and ran no prior round in this world's build history.

**Method note.** This is a fix-pass verification plus a fresh adversarial read, run under this build's own documented failure mode: *"a search too strict for the text it was run against, then trusted because it returned something."* The Round 2 fix pass states, in its commit message, its Document Log entry and its Decision Log entry, that it re-derived every governing quotation at source and read the full word-level diff hunk by hunk. **That claim was tested, not credited.** Every quotation in the changed text was re-extracted from its own file — the two `.docx` frameworks and the Constitution unzipped and read directly, Doc_03's tag and frequency cells parsed per-row rather than grepped document-wide, the Registry's confidence column parsed by field. Every site Round 2 named was additionally checked *for whether the fix pass touched it at all*, since a fix can be announced at a site that was never opened. Corpus sweeps were **not** re-run; Doc_03's disclosed sweep results were checked as citations only.

Marking per Constitution Article 31: **Simulated review — informational only, not an Article 31 substitute.**

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 6 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC — 20 in total.**

**Fix-pass verification tally, against Round 2's 27 findings: 22 genuinely fixed · 4 partially fixed · 0 not fixed · 1 properly escalated.** Of the 4 partials, **3 additionally introduced or left standing a new defect** (H3, H6, H7); three findings recorded as genuinely fixed also introduced a smaller new defect (M1, L1, C1).

**This is the best fix pass this document has had, and its certification is still not true.** Nothing was left byte-identical this time. The three findings the previous pass never touched are genuinely fixed. Every quotation the commission asked to be independently re-derived — Doc_01 §4's three conciliar-authority sentences, Doc_01 §5's two caveat clauses, Doc_02 §1's "proper right of judgment", Doc_02 §8's bracket, the Framework's Primary and Tensional paragraphs, the Forces Framework's Step 4 rule, Constitution Article 21, Doc_03's `preaching`/`catechesis` tag cells — checks out verbatim at source, and the new text uses each in a way its own surrounding paragraph supports. The Article 21 claim is not only right, it is right in the strong form: the string `reopen` occurs **zero** times in the entire Constitution.

**And the same mechanism is present anyway, in a new form.** It has moved from quotations to *pointers about the document's own internals*. Three times, the fix pass states that a fix was carried to a place in this document, and that place was never opened:

- Candidate 5's restored Cross-Check says its divergence is **"Carried to §7 Open Item 1."** Open Item 1 is byte-identical and carries only Candidate 3's divergence (H2 below).
- §3's escalation says every downstream use of "Tensional" — **"§4's summary row, §5's non-reopening argument, §6's matrix inclusion, §7 Open Item 2"** — "is provisional with it." All four are byte-identical and all four still assert the classification as reached, tested and confirmed (H1 below).
- The Decision Log states the same thing in the stronger form — "with every downstream use (§4, §5, §6, §7 Open Item 2) **flagged** provisional with it" — which is a claim about marks on the page that are not there.

The verification the pass describes — the word-level diff read hunk by hunk — would not catch any of these, because all three failures are in text the diff does not contain. The remedy this build adopted answers the previous round's mechanism, not this one.

**Nine things were checked hard and found clean, and should be stated before the findings:**

1. **Both tables are structurally clean, and the fix pass did not break either.** Machine-parsed: pipe counts uniform (6 across all ten Classification Summary lines, 10 across all ten Interaction Matrix lines), `**` and backtick nesting balanced on every table line.
2. **All 28 Interaction Matrix pairs are symmetric**, machine-checked at HEAD: 1↔5 "Reinforcing, weakly" in both cells, 2↔8 "Competing" in both, the one deliberate asymmetry (2↔7 "Reshaped by" / 7↔2 "Reshapes") correctly directional, every other pair matched. All eight §3 Interaction bullets were then checked cell-by-cell against their own matrix rows: **all eight agree, with no omission and no over-claim.** §6's assertion that no candidate's row is entirely "no demonstrated relationship" is true against the table. The fix pass's own count of Candidate 5's row — three reinforcing, four none, zero competing or reshaping — is exactly right.
3. **H1's fix is exact at source, and the paragraph supports the use.** Doc_01 §4 reads, verbatim: *"The conciliar-authority axis is different in kind, and this document does not fold it into that same account"*; *"That is closer to this world's own ordinary exercise of office than the other two axes are"*; *"it is the axis this document finds the closest call."* All three are now quoted accurately and deployed in the direction Doc_01 actually runs. The borrowed sentence about the other two axes is gone.
4. **H4's fix is exact at source, in the strong form.** Constitution Article 21, extracted verbatim, is four sentences: strand is a finding never a presupposed universal schema; the determination *"once made, governs all subsequent strand attribution"*; strand defined as a meaningfully distinct pattern of formation emphasis, practice, authority structure or ecological orientation; determination accountable to evidence. **There is no reopening trigger.** `reopen` and `revisit` each occur 0 times in the whole Constitution. Doc_01 §5's caveat clauses are verbatim: *"as its own discipline rather than as a rule either governing text states"* and *"on the one axis §4 discloses as not fully closed."*
5. **M1's fix is exact.** `grep -c "right of communion" Doc_02_Source_Ecology.md` returns **0**; Doc_02 §1's 256-preface quotation is *"neither does any of us set himself up as a bishop of bishops... every bishop, according to the allowance of his liberty and power, has his own proper right of judgment"* — reproduced character-for-character, ellipsis included. The "right of communion" clause is correctly re-homed: it is present at Doc_01 §4, Doc_01 §5 and Registry row 4, and absent from Doc_02.
6. **M3's fix is exact, and its parenthetical is true.** Doc_01 §4's Conclusion reads *"because neither touches this world's own recurring gravities as established at §3"* — flat, as now quoted. And the hedged *"does not clearly touch"* genuinely belongs to the conciliar-authority axis alone: it occurs twice in Doc_01, at §2 and at §5's authority-structure bullet, in both cases of that axis. Round 1's M8 is closed at last.
7. **Every Framework and Forces Framework quotation re-extracted from the `.docx` files is verbatim.** CF V7.4 Part III: *"Primary Gravities organize the ecology broadly. Multiple dimensions depend on them. They shape formation pervasively"* (L5's fix — *formation*, not *participants*, exactly as now quoted); *"Supporting Gravities organize significant portions of the ecology"*; the Tensional paragraph; the Cross-Check's *"noted explicitly rather than resolved by upgrading the classification"*; the Repetition Test's one-line statement; the Author Gravity "at the point of generation, before it is tested" rule; the Interaction-Test warning about impression-generated lists. Forces Framework V1.1 Section 4, Step 4: *"A gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete"* — verbatim, and genuinely in Step 4 (L8's fix).
8. **Doc_02 §8's bracket and Doc_03's tag cells are verbatim.** The bracket reads *"Documented / Widely Accepted: ... the existence and basic content of the major primary texts named at §1"*, now cited at all four Confidence-B Cross-Checks. Doc_03's `preaching` row carries `[SC], [RT]` and its catechesis row `[SC], [TC], [RT]`, exactly as the L10 fix now states, with 119 belonging to `preaching` alone and catechesis grounded on dedicated treatises — each re-derived by parsing the row, not by a document-wide grep.
9. **Nothing Round 2 certified clean was broken.** The three corrected `[CT]` tag cells (`[AS], [TC], [PV]`, `[SC], [TC], [PV]`, `[SC], [TC], [DR]`) are untouched and still exact; all ten Doc_03 figures are unchanged and still correct as values; the five IJC precedent claims were not edited and spot-check accurate against IJC's own Candidates 4 and 5, summary table and Open Item 4; Doc_01 §3's four-candidate mapping at §5 is untouched and still correct in order; §2's fragmentation reading holds against Doc_01 §6's parenthetical, re-read whole. `grep -c "Article 3" Doc_02_Source_Ecology.md` still returns 0.

**Where the findings are.** As at Round 2, they cluster on Candidate 5 — but the subject has changed. Round 2's HIGHs were about whether the classification was earned. The fix pass did the honest thing and stopped arguing it, escalating instead. **Five of six HIGHs here are about the escalation not having been carried into the document it was made in.** Sections §4, §5, §6 and §7 continue to state, to a downstream reader who will not read §3, that Candidate 5 was tested, reaches Tensional on the Framework's own definition, and is confirmed — and §5 builds an unreopened Article 21 finding on top of that. The sixth is the certification, for the fourth consecutive round.

---

## HIGH

### H1 — The escalation is declared at §3 and carried nowhere: §4's summary row, §5, §6 and §7 Open Item 2 are byte-identical and still state the classification as tested, reached and confirmed — and §3's own closing paragraph does too

**Sites:** line 105 (the declaration); lines 164, 173, 186, 203, 208 (the sites it names, all byte-identical to `775b6299`); line 107 (inside the escalation subsection itself).

Line 105 states the governing intent, and states it well:

> *"**What this means for everything downstream.** "Tensional" stands below as the **provisional label of record**, and every use of it in this document — §4's summary row, §5's non-reopening argument, §6's matrix inclusion, §7 Open Item 2 — is provisional with it and should be read as pending."*

Diffed against `775b6299`: **none of the four named sites was touched.** What they say at HEAD:

- **Line 164, §4's summary row, Classification column:** *"**Tensional** — tested against Supporting and Primary and reaches neither; **reaches Tensional on the Framework's own "unresolved pressure within the ecology" definition** (see §3, §5)."* No provisional marker, no escalation, no "pending". This asserts exactly the proposition §3 says was never earned by the test.
- **Line 173, §5:** *"What it is not, on §3's own corrected classification, is **Primary or Supporting**: it is **Tensional**, an unresolved pressure within the ecology that does not organize broadly."* §5 contains no mention of the escalation at all.
- **Line 186, §5's survival bullets:** Candidate 5 *"tested here for the first time as a candidate gravity and **found Tensional**, a genuine, bounded result rather than a foregone one"*; line 188: *"one axis Doc_01 flagged for particular weight is **tested and found Tensional** without reopening the finding that flagged it."*
- **Line 203, §6:** *"Candidate 5's own row is included on the same footing as any Tensional gravity's, since it was **fully tested**."*
- **Line 208, §7 Open Item 2 — the item that carries the claim to Doc_05/Doc_07/Doc_08:** *"it remains real, substantial, and directly quoted evidence of a live theological difference between this world's own two anchor figures, **tested and confirmed as its own bounded, unresolved pressure within the ecology**."* Open Item 2 is the one place a downstream builder is *guaranteed* to read, and it instructs them on a classification it presents as settled, with no pointer to Open Item 7 five lines below it.

And the defect reaches inside the escalation subsection itself. Line 107 — the old pre-escalation paragraph, left in place beneath the two new ones:

> *"The claim that this constitutes a genuine, if bounded, gravity rests on the two formulas' own Documented existence and **on the Tensional test run above**..."*

Line 103, four lines earlier: *"The Framework's definition has two limbs; this document argues the first... and **never runs the second**... and on Round 2's finding neither was earned by the test rather than by assertion."* The document says in one paragraph that the test was not run and in the next that the classification rests on the test having been run.

**Why HIGH.** Template §4's stated purpose for the Classification Summary is to let a downstream builder confirm what each candidate received *without reading the full document* — which is precisely what line 164 now defeats, and precisely where an escalated classification most needs a mark. The Decision Log's account of this is not merely optimistic but false as a statement of fact about the file: *"'Tensional' stands in the document as the provisional label of record, marked as such in the candidate's own heading, with every downstream use (§4, §5, §6, §7 Open Item 2) **flagged** provisional with it."* Only the heading is flagged. This is the build's own mechanism in its newest form: a claim about a target that was never opened, made in a pass whose verification discipline reads only the diff — which by construction cannot contain an untouched site.

**Fix:** mark each of the four sites. In line 164's Classification cell: "**Tensional (provisional — escalated, §7 Open Item 7)**", and strike or qualify "reaches Tensional on the Framework's own ... definition", which is the disputed step. At §5 line 173 and the two survival bullets, replace "is Tensional" / "found Tensional" with the provisional-and-escalated form and cross-reference Open Item 7. At §6 line 203, note that Candidate 5's inclusion does not depend on the escalated label. At Open Item 2, replace "tested and confirmed" with the pending form and point to Open Item 7 in its first sentence. Then delete or rewrite line 107, which contradicts lines 103–105 in the same subsection. Correct the Decision Log's "flagged provisional" sentence to what was actually done.

### H2 — Candidate 5's restored Cross-Check says its divergence is "Carried to §7 Open Item 1"; Open Item 1 is byte-identical and carries only Candidate 3's

**Sites:** line 96 (Candidate 5, Cross-Check — new in this pass); line 207 (§7 Open Item 1 — untouched); line 221 (Document Log).

Round 2's H3 found the Candidate 5 divergence note deleted in the same pass that raised the classification, and its fix asked for three things: restore it at §3, restore it in the summary-table cell, and *"add it to §7 Open Item 1 alongside Candidate 3's, or as its own item."* Two of the three were done, and done well. Line 96 now reads:

> *"**Divergence flagged rather than resolved, per CF V7.4's own Cross-Check rule that where attestation and organizing strength diverge the discrepancy is "noted explicitly rather than resolved by upgrading the classification":** the formulas are Documented; their *organizing breadth* is not supported at the same level... **Carried to §7 Open Item 1.**"*

Line 207, at HEAD, in its entirety:

> *"1. **Candidate 3's Confidence/Gravity Cross-Check divergence** (underlying facts Documented; the one-gravity synthesis itself Widely Accepted) is carried forward explicitly to Doc_05 and Doc_08, not resolved here, per the Cross-Check's own governing rule."*

Diffed against `775b6299`: unchanged. Candidate 5's divergence is nowhere in §7. The Document Log then certifies the third limb anyway: *"H3 (the Confidence/Gravity Cross-Check divergence note... restored at §3 and in the summary table **and carried to Open Item 1**)."*

**Why HIGH.** This is Round 2's H2 mechanism exactly — a pointer that now survives inspection because it names a real target, attached to a claim the target does not support — reproduced inside the fix for the finding that named it. The consequence is live: Open Item 1 is the mechanism by which a Cross-Check divergence reaches Doc_05 and Doc_08, and the Framework's rule is that a divergence is carried and made visible rather than resolved. Candidate 5's is the more consequential of the two divergences, on the document's most contested candidate, and it does not travel.

**Fix:** add Candidate 5's divergence to Open Item 1, or give it its own item, in the terms line 96 now uses. Then correct the Document Log entry, which currently certifies a limb that was not done.

### H3 — §5's non-reopening finding is still stated unconditionally, on the one axis the reopening caveat is scoped to, after the same pass disclosed that its search on that axis is bounded and the decisive source unread

**Sites:** lines 90, 94, 212 (the H6 disclosure, new in this pass); lines 171, 173 (§5, edited in this pass, not reconciled with it).

The H6 fix is good work, and accurate at source. Registry row 65 was read in full and confirms every element of it: the *Gesta* is vendored in the shared corpus as `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, assigned to this world's corpus-map entry on 2026-09-13 at `role: context`, `confidence: provisional`, with Augustine speaking in at least fourteen numbered acts, and the row's closing words are exactly as quoted: *"available to Doc_04, and not yet drawn on by it."* Candidate 5's Persistence bullet now says plainly: *"Whether it bears on this test is untested, not settled."* Open Item 6 calls a targeted read *"the single piece of evidence most likely to settle Candidate 5's Persistence test."*

§5 was edited in the same pass and says none of this. It states the governing test at line 171 —

> *"...and to reopen the strand-singular finding *if* this document's own independent testing, "weighing this axis directly" (§8 item 10's own directive), surfaces evidence Doc_01 has not already weighed."*

— and then closes it at line 173 without qualification:

> *"**Finding: Doc_01 §5's own strand-singular determination stands, unreopened.**... and this document's own independent testing is the confirmation Doc_01 §8 item 10 called for."*

Doc_01 §8 item 10, verified verbatim, makes the trigger turn on *"Doc_04's own formal six-test assessment, **weighing this axis directly**, surfac[ing] evidence this document has not weighed."* Doc_04 now concedes, in the two test bullets that constitute that assessment, that it has **not** weighed the most obvious source on the axis — a source Doc_01 never weighed either, and which the Registry records as available to this document specifically. "Unreopened" may well be the right answer; it is not an answer this document is currently entitled to state flatly, and §5 does not even record that the question is bounded.

**Why HIGH.** The reopening caveat is scoped by its own terms to *this axis alone* (Doc_01 §5: *"on the one axis §4 discloses as not fully closed"* — verified). A disclosed search bound on that axis is therefore not a general caveat: it lands exactly where the caveat lives. The fix pass disclosed it at §3 and left the governance consequence at §5 in the pre-disclosure form, which is the same shape as Round 2's H6 one level up.

**Fix:** carry the bound to §5. State that the strand-singular finding stands **on the evidence weighed**, name the *Gesta* as the disclosed unread route on this axis, and say what would follow if a targeted read surfaced conciliar-authority material operative among clergy beyond the two anchor figures — pointing at Open Item 6, which already says it. Two sentences.

### H4 — §5 misstates the Framework's Tensional definition at the sentence that carries the non-reopening argument, dropping the limb §3 says runs the other way

**Site:** line 173 (§5; the paragraph was edited in this pass and this sentence left standing). Present in the draft; missed at Rounds 1 and 2.

CF V7.4 Part III, extracted verbatim:

> *"Tensional Gravities function as persistent counter-forces, alternatives, or unresolved pressures within the ecology. They **may** not organize as broadly as primary gravities **but they prevent the ecology from being reducible to its primary forces.**"*

Doc_04 line 173:

> *"**A Tensional gravity, by the Framework's own definition, is precisely one that does not organize the ecology broadly enough to touch the Primary gravities' own recurring organization**; the conciliar-authority disagreement being real, Documented, and now classified as its own bounded, unresolved pressure is weaker, not stronger, evidence for strand-plurality than Doc_01's own hedged treatment already assumed."*

That is not the definition. The Framework's first clause is hedged ("may not organize as broadly") and its second clause is the operative one, and it runs the opposite way: a Tensional gravity is defined by the fact that the ecology **cannot** be reduced to its primary forces because of it. Doc_04 converts a hedged comparative into a categorical disqualifier and then uses it as the load-bearing premise of the non-reopening argument — "*That distinction is what carries the non-reopening argument.*"

The document's own §3 says so, at line 103: *"The Framework's definition has two limbs; this document argues the first... and never runs the second — 'prevent the ecology from being reducible to its primary forces' — against which this candidate's own results run the other way."* §5 not only runs the second limb, it runs it backwards, and states the result as the Framework's own definition.

**Why HIGH.** This is the sentence on which an Article 21 determination is left standing. It is also a misquotation of a governing framework presented inside quotation-free "by the Framework's own definition" framing, which is harder to catch than a bad quotation and does the same work. And it is inconsistent with the escalation the same document now makes: if the Tensional label is escalated because the second limb was never argued, §5 cannot simultaneously derive a finding from a claim about what that limb means.

**Fix:** strike the clause. The non-reopening argument does not need it: what it needs is Doc_01 §8 item 10's own trigger ("surfaces evidence this document has not weighed") plus Article 21's "once made, governs all subsequent strand attribution" — the route Round 2 recommended and the route §3 now claims §5 takes. Rebuild line 173's closing on that, with H3's bound stated.

### H5 — §3 and §5 give different and incompatible accounts of what carries the non-reopening finding, and the ground §3 attributes to §5 is not recorded at §5 at all

**Sites:** line 105 (§3, new in this pass); line 173 (§5, edited in this pass).

§3, line 105, the sentence that lets the escalation proceed without stalling the document:

> *"**What does not depend on the outcome**, and is stated here so the escalation does not stall the rest: Doc_01 §5's strand-singular determination stands either way, on Doc_01 §8 item 10's own trigger ("surfaces evidence this document has not weighed") — this document re-weighs Doc_01's own two quotations and surfaces none. **The non-reopening finding at §5 is therefore independent of how this classification resolves.**"*

§5, line 173:

> *"**That distinction is what carries the non-reopening argument**, not the absence of a gravity: Article 21's authority-structure criterion is tested here through Doc_01 §4/§5's own routing... A Tensional gravity, by the Framework's own definition, is precisely one that does not organize the ecology broadly enough to touch the Primary gravities' own recurring organization..."*

"That distinction" is the Primary/Supporting-versus-Tensional distinction — i.e. the classification under escalation. §5 says the non-reopening rests on it; §3 says the non-reopening is independent of it. Both cannot be true. Worse, the ground §3 attributes to §5 — that this document re-weighed Doc_01's two quotations and surfaced no new evidence — **appears nowhere in §5**. §5 states the trigger (line 171) and then jumps to the finding (line 173) without ever recording that the trigger was not met. So the argument §3 says is doing the work is not on the page, and the argument that is on the page is the one §3 disclaims.

**Why HIGH.** The escalation's whole containment depends on this sentence: it is the basis for advancing an Article 21 determination while the classification it was argued from is pending. If §5 does not actually stand on the item-10 trigger, then a reader following §5 finds the determination resting on an escalated label, which is exactly what §3 promises it does not.

**Fix:** move §3's argument into §5 and make it §5's own: state at §5, in terms, that this document re-weighed Doc_01 §4's two quotations, surfaced no evidence Doc_01 has not weighed **within its disclosed search bound** (H3), and that the finding therefore stands on item 10's own trigger and Article 21's "once made, governs" — independently of Candidate 5's classification. Then delete "That distinction is what carries the non-reopening argument."

### H6 — The certification is wrong again, in three checkable ways, in the pass that adopted the anti-certification remedy

**Sites:** line 3 (Status); lines 220–221 (Document Log, the two 2026-09-13 entries); line 225 (Disposition); the Decision Log's 2026-09-13 (later) entry.

The Status line is a real improvement and is honest about the previous pass. It is still not a count this document has verified.

**(a) The Document Log's own enumeration is short by one against the number it certifies.** The 2026-09-13 fix-pass entry lists: HIGH `H1, H2, H3, H4, H6, H7` (6, with H5 escalated); MEDIUM `M1`–`M7` (7); LOW *"L1 (...); L2 (...); L3, L4, L5, L7, L8, L9, L10"* — **nine; L6 is absent**; COSMETIC `C1, C2, C3` (3). Total enumerated as addressed: **25**, plus one escalated, against a headline of "26 of 27 addressed". L6 *was* in fact fixed — the 2026-09-10 Round 1 review round is now logged as its own Document Log line, exactly as Round 2 asked — so the substance is right and the record is wrong. That is the same defect class the Status line claims to have retired: *"this line states a count it has verified rather than one taken from a fix list."* A verified count would have named ten LOW findings.

**(b) The Disposition still describes this pass as answering the wrong round.** Line 225: *"**Not yet self-disposed.** **This fix pass answers Round 1's findings**; per CO-022, a substantial revision returns to independent review before any disposition..."* This is the Round 2 fix pass. The C1 fix removed the duplicated CO-022 sentence from the Status line and left the surviving copy's now-false subject in place — the fix pass edited one half of a duplicated pair and did not re-read the half it kept.

**(c) The Decision Log asserts marks on the page that are not there.** *"with every downstream use (§4, §5, §6, §7 Open Item 2) **flagged** provisional with it"* — verified false at all four sites (H1). The same entry's claim that **"Every governing quotation [was] re-derived at source, not taken from the review"** is falsified by at least one case: the 687 scope qualifier at line 111 reproduces Round 2's own composite rendering rather than Doc_03's cell (L1 below).

**Why HIGH.** CLAUDE.md's governance rule is that *"a record marked 'quotes verified' is a claim to re-check, not a fact to trust."* This pass's Decision Log entry is a long, detailed and largely accurate account of its own method — which is precisely what makes the three false elements dangerous: a reader who trusts it inherits a belief that four downstream sites are marked, that Open Item 1 carries Candidate 5's divergence, and that every quotation was re-derived. None is true. The remedy adopted here (read the word-level diff hunk by hunk) is a good remedy for the *previous* mechanism and cannot detect any of these three, all of which live in text the diff does not contain.

**Fix:** correct the LOW enumeration to include L6; restate the headline as a count derived from the enumeration. Rewrite line 225's opening clause to name Round 2. Correct the Decision Log's "flagged provisional" sentence and narrow the "every governing quotation re-derived" claim to what was done. And add to the next pass's discipline the check this round's failures all needed: **for every fix that names a destination in this document, open the destination and read it.**

---

## MEDIUM

### M1 — The Governed-by line names Constitution Article 22 as "Cross-Strand Gravity testing"; Article 22 is the Forces Principle

**Site:** line 6.

> *"**Governed by:** ... Constitution Articles 21 and 22 (**Strand Determination, Cross-Strand Gravity testing**)..."*

Article 22, extracted verbatim, is headed *"Forces Principle"* and concerns situating a world against the forces that shaped it across external and internal dimensions. Cross-strand gravity testing is inside **Article 21**: *"where strands exist, convergence across them is a test of a gravity's centrality."* Round 1's C1 found Article 22 omitted and the fix pass added the number; the gloss attached to it is wrong. Article 22 is genuinely a governing authority for this document — it is what the forces-connection notation discharges — so the citation is right and only its label is false, which is the harder kind to notice.

**Fix:** *"Constitution Articles 21 (Strand Determination, including cross-strand gravity testing) and 22 (Forces Principle, discharged at each candidate's forces-connection notation)."*

### M2 — The new Confidence-B boilerplate is applied identically at four Cross-Checks and is false at two of them, where it contradicts the sentence immediately before it

**Sites:** lines 49 (Candidate 2), 79 (Candidate 4), 136 (Candidate 7), 151 (Candidate 8).

The L1 fix inserts the same clause at all four: *"the specific loci sit at Registry Confidence B."* Registry confidence letters, parsed by field rather than read from prose:

| Candidate | Loci the Cross-Check rests on | Registry confidence |
|---|---|---|
| 2 | Row 1 (Epistles), Row 2 (*De Lapsis*), Row 7 (Pontius) | **A**, B, **A** |
| 4 | Rows 15, 18, 19, 21, 5 | B, B, B, B, B |
| 7 | Row 23 | B |
| 8 | Row 1 (Epistles XX–XXI), Row 2 (*De Lapsis*) | **A**, B |

At Candidates 4 and 7 the clause is exactly right. At Candidates 2 and 8 it is false of the principal locus, and at Candidate 2 it directly contradicts the sentence it is appended to: *"Evidence reaches Documented for Cyprian's own conduct and correspondence, directly quoted and re-verified across Doc_01's nine rounds... the specific loci sit at Registry Confidence B."* Round 2's L1 named the Confidence-B rows precisely (row 2 for Candidates 2 and 8); the fix generalized a row-specific qualifier into a blanket one.

A second, smaller point on the same clause: Doc_02 §8's bracket is headed *"Documented / **Widely Accepted**"* — a two-name band. Using it to certify a flat "Documented" is a mild over-read, mitigated by the fact that Doc_04 quotes the label in full.

**Fix:** at Candidates 2 and 8, name the row: "…the *De Lapsis* locus (Registry row 2) sits at Confidence B; the Epistles and Pontius loci (rows 1, 7) at A."

### M3 — §4's summary row attributes "closest call" to Doc_01 §8 item 10, which does not contain the phrase

**Site:** line 164 (Cross-Strand column).

> *"Strand-singular world; the axis **Doc_01 §8 item 10 names as the "closest call"** — see §5 for the full treatment"*

Doc_01 §8 item 10, read verbatim, is headed *"…held subject to this document's own reopening caveat, not yet closed"* and describes the two theories as *"real, substantial differences this document argues do not clearly touch this world's own formation-relevant ground, but does not consider fully settled."* It does not contain "closest call". The phrase occurs three times in Doc_01 — twice in §4 (*"it is the axis this document finds the closest call"*; *"which this document finds the closest call"*) and once in §5 (*"which §4 flags as the closest call"*). Candidate 5's own *Generated from* line at 86 attributes it correctly, to §4, so the document is internally inconsistent about it. This cell was not touched by the fix pass, and both prior rounds missed it — but it is the same defect shape as Round 1's M8 and Round 2's L3: a real quotation hung on the wrong section.

**Fix:** *"the axis Doc_01 §4 calls "the closest call" and §8 item 10 heads "not yet closed""*, matching the corrected form already used at lines 86 and 88.

### M4 — The M1 fix breaks Candidate 3's *Generated from* citation list: the Doc_02 §2 pointer now hangs off the correction rather than off Doc_02 §1

**Site:** line 56.

The corrective sentence was inserted mid-list, and the list was not re-read around it:

> *"*Generated from:* Doc_02 §1 (the 256 preface's own "proper right of judgment" — "..."; the whole rebaptism dispute, where disagreement does not sever fellowship)**. The companion "right of communion" clause ("...") is Doc_01 §4's and §5's, and Registry row 4's, not Doc_02's — corrected here, since Doc_02 does not contain the phrase, §2 (Cyprian's Influence: "Augustine arguing *with* Cyprian, disputing his ruling while claiming his communion")**; Doc_01 §5 (...), §3 (fourth-named candidate gravity)."*

The `§2 (Cyprian's Influence…)` item is now grammatically attached to *"since Doc_02 does not contain the phrase"*, and the sentence boundary after the first parenthesis severs it from the `Doc_02 §1` it belongs to. The Doc_02 §2 quotation itself is correct — verified verbatim at Doc_02 §2's Cyprian Influence entry — so this is a structural defect in a generation-grounds list, at the candidate whose independence from Doc_01 the document's own §8-item-7 obligation turns on.

**Fix:** put the correction in a trailing sentence after the whole list, or in a parenthesis inside the `Doc_02 §1` item, so the `§2` and `Doc_01 §5` items still read off their own heads.

### M5 — The header's list of Registry rows "which this document cites" names seven; Doc_04 cites at least fifteen

**Site:** line 7.

> *"...rows 1, 4, 12, 13, 22, 23 and 192, **which this document cites**, are unaffected, and row 65's correction is engaged at Candidate 5's Repetition and Persistence above"*

Doc_04 also cites rows 2 (*De Lapsis*, Candidates 2 and 8), 5 (*De Dominica Oratione*, Candidates 1 and 4), 7 (Pontius, Candidate 2), 15, 18, 19, 21 (Candidate 4), and 65. The seven named are precisely the subset Round 2 re-verified and reported in its own parenthesis — the fix pass carried Round 2's list across as if it were a statement about Doc_04's citations. The substantive point survives (none of the additional rows is among the seven corrected on 2026-09-13: rows 37, 44, 56, 64, 65, 206, 208), but the sentence as written is a false statement about this document's own citation set, in the line that certifies companion-document currency.

**Fix:** either enumerate the rows actually cited, or rewrite as "none of the rows this document cites, other than row 65, is among those corrected."

---

## LOW

### L1 — The 687 scope qualifier is imported from the wrong Doc_03 row
Line 111. Doc_04: *""baptism" occurs 687 times within *On Baptism* itself per Doc_03's own sweep, **markup stripped** and scoped to the treatise's own div2 boundaries **rather than the larger volume it sits inside**."* Doc_03's `heresy` row (the cell the 687 figure sits in) reads: *""baptism" occurs 687 times within the treatise itself, **markup stripped**, scoped to its own div2 boundaries — **the length at which the question is argued**."* The phrase *"rather than the larger volume it sits inside"* occurs exactly once in Doc_03, in the **"plenary Council"** row, attached to the 31 figure, which carries no "markup stripped". The fix pass reproduced Round 2's L7 composite rather than opening Doc_03's cell — direct evidence against the "every governing quotation re-derived at source" certification (H6). Substantively harmless; both counts are div2-scoped inside the same volume. **Fix:** quote the cell the figure comes from.

### L2 — §5 still points at a column name the L9 fix removed
Line 171: *"every candidate above is tested independently across the Cyprian and Augustine phases (**the Article 21 column in each §3 entry**, and the Persistence test specifically)."* §3's entries are bullet lists with no columns, and the §4 table's fourth column was renamed by this pass from "Article 21 status" to the Template's "Cross-Strand (or declared substitute) status" — so the reference now names a column that exists nowhere. **Fix:** "the Cross-Strand (or declared substitute) status column at §4, and the Persistence test at each §3 entry."

### L3 — §2's parenthetical reads as though "does not clearly touch" is §4's phrase; it is §2's and §5's
Line 18: *"Doc_01 §4 already tested this shift... and its Conclusion is flat rather than hedged on this axis: ... (the hedged "does not clearly touch" formulation belongs to the conciliar-authority axis alone, and is not this axis's verdict)."* The attribution to the conciliar-authority axis is correct and verified. The phrase itself does not occur in §4 at all: its two occurrences are in §2's transition-criteria summary and §5's authority-structure bullet. **Fix:** name where it occurs.

### L4 — "Article 21's own 'once made, governs'" is truncated past the object that scopes it
Line 175 gives the full clause once — *"once made, governs all subsequent strand attribution"* — and then re-quotes it twice in short form as the thing that "disposes of that leg." Article 21's clause governs **strand attribution**, not the revisability of the determination; Doc_01 §5 leans on it the same way, so Doc_04 is applying a routing it inherits rather than inventing one, but the short form drops exactly the words that make the reach visible. **Fix:** use the full clause at the operative sentence, and say in one clause that this document reads it, with Doc_01 §5, as governing revisitation and not only attribution.

### L5 — Open Item 6 restates "fourteen" flat after correctly stating the floor
Line 212 opens correctly — *"at least fourteen numbered acts"* — and later says *"A targeted read of **those fourteen acts**..."* Registry row 65 states in terms: *"Still a floor: mid-line instances and heavier garblings are not counted, and **any restatement of this figure elsewhere should carry the floor with it rather than assert fourteen flat**"* (Round 29's own L7 there). **Fix:** "a targeted read of those acts."

### L6 — The *Gesta* is cited as "Registry row 65", whose Source cell is an unvendored in-copyright edition
Lines 90, 94, 212. Row 65's Source is *Serge Lancel (ed.), Actes de la Conférence de Carthage en 411*, SC 194/195/224/373 — Confidence **C**, *"Not currently vendored on this world's own branch"*, consultation-only. The vendored text Doc_04 actually needs is `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, named inside row 65's Verification Note. Citing the route as "row 65" without that distinction invites a later reader to conclude the source is unavailable. **Fix:** cite as "the Migne PL XI printing of the *Gesta* recorded at Registry row 65 (`cic/texts/pl11-…_migne.txt`)."

---

## COSMETIC

### C1 — Sentence-case defect introduced by the H2 fix
Line 44: *"Candidate 8 (confessor-authority tension) exists only because this gravity exists; **This** gravity's own resolution (readmission, not permanent exclusion) models Candidate 3's own logic..."* Capital after a semicolon, where the replaced clause began with a capitalised citation.

### C2 — The M7 replacement sentence is ungrammatical
Line 20: *"**It is not advanced as a generation-stage finding rather than a six-test result — it is not one candidate, in the unified form Doc_01 §6 poses it:**"*. The substance is right and is what Round 2's M7 asked for; the sentence reads as a negation of the disposition rather than a statement of it. **Fix:** "It is not advanced — as a generation-stage finding rather than a six-test result: in the unified form Doc_01 §6 poses it, it is not one candidate."

### C3 — The two Tensional headings now carry different annotation conventions
Line 84: *"### Candidate 5 [Tensional — provisional; classification escalated, see below] — Conciliar Authority Theory..."*; line 141: *"### Candidate 8 [Tensional] — Confessor-Authority..."*. C3's fix is discharged and the asymmetry is deliberate, but a reader scanning headings now sees one bracketed label that is a classification and one that is a classification plus a status note. A short form — `[Tensional — escalated]` — would carry the same information at heading length.

---

## Fix-pass verification table

| Round 2 finding | Status | Note |
|---|---|---|
| H1 — Cand. 5 Formation argued on a Doc_01 §4 sentence about the other two axes | **GENUINELY FIXED** | All three §4 quotations re-derived verbatim at source; the finding now rests on Doc_02 evidence and discloses it runs against Doc_01 §4's hedge. Exemplary |
| H2 — Cand. 2 Dependency claim false of Doc_01 §5 | **GENUINELY FIXED** | Claim restated as this document's own reading, attribution withdrawn, both matrix glosses (2↔3, 2↔6) corrected — verified in the parsed table. Minor case defect (C1) |
| H3 — Cand. 5's Cross-Check divergence deleted | **PARTIAL / NEW DEFECT** | Restored at §3 (line 96) and in the summary cell (line 164). "Carried to §7 Open Item 1" is false — Open Item 1 byte-identical; Document Log certifies the limb anyway (R3 H2) |
| H4 — "Article 21's reopening trigger" | **GENUINELY FIXED** | Article 21 extracted verbatim: no reopening trigger; `reopen` 0× in the Constitution. Caveat re-attributed to Doc_01 §5 with both clauses verbatim, conciliar-authority scope stated. Residual R3 L4 |
| H5 — Tensional quoted but never argued | **PROPERLY ESCALATED** | Recorded at §3 (lines 101–105), §7 Open Item 7, the Disposition and the Decision Log, with Round 2's contrary assessment recorded not suppressed. **But not propagated** to the four sites §3 names, and line 107 still asserts the test was run (R3 H1) |
| H6 — *Gesta* search bound undisclosed | **PARTIAL** | Disclosed at Repetition and Persistence and carried as Open Item 6; row 65 verified in full at source. Not carried to §5, where the non-reopening finding still reads unconditional (R3 H3) |
| H7 — "all 38 findings addressed" certification | **PARTIAL / NEW DEFECT** | Status line and Document Log rewritten honestly about the prior pass; Round 1's review round logged (L6). But the LOW enumeration is short by one against the headline, the Disposition still says "Round 1's findings", and the Decision Log asserts marks that are not on the page (R3 H6) |
| M1 — "right of communion" miscited to Doc_02 §1 | **GENUINELY FIXED** | Doc_02 §1's quotation reproduced character-for-character; `right of communion` 0 hits in Doc_02, correctly re-homed to Doc_01 §4/§5 and row 4. Citation list broken structurally (R3 M4) |
| M2 — ecological orientation claimed but not addressed | **GENUINELY FIXED** | Assessed in two sentences at line 173, against Doc_01 §5's own bullet, read at source; "That is a discharge, not a deferral" |
| M3 — coercive-capacity quotation spliced (R1 M8) | **GENUINELY FIXED** | Doc_01 §4's Conclusion quoted verbatim; the "does not clearly touch" attribution independently verified true. Minor locating imprecision (R3 L3) |
| M4 — Cand. 7's summary row hides a second narrow pass | **GENUINELY FIXED** | Line 166 now reads "narrow pass on Dependency and Interaction", matching §3 |
| M5 — new-gravity closure overstated | **GENUINELY FIXED** | Scoped to the Pelagian half, with Doc_01 §4's "anti-Manichaean **and** anti-Pelagian" quoted and Open Item 4 pointed to |
| M6 — Registry status stale | **GENUINELY FIXED** | Header records the return to independent review, per the Decision Log's own words. Row list inaccurate (R3 M5) |
| M7 — wrong failing test named for the unified candidate | **GENUINELY FIXED** | Restated as a generation-stage finding, which is what §2's heading is for. Sentence ungrammatical (R3 C2) |
| L1 — flat "Documented" over Confidence-B rows (R1 L5) | **GENUINELY FIXED** | Doc_02 §8's bracket quoted verbatim at all four Cross-Checks. Boilerplate false at two of them (R3 M2) |
| L2 — Cand. 7 quotes §6 prose as cell content (R1 L9) | **GENUINELY FIXED** | Cell quoted verbatim; prose cited separately and labelled as prose. Both verified against Doc_01 §6 |
| L3 — §8 item 10 quotation spliced | **GENUINELY FIXED** | Fixed at both sites (lines 88, 171); "not yet closed" verified as item 10's heading and "with particular weight" as §4's and §8 item 7's |
| L4 — "the document's own words above" | **GENUINELY FIXED** | Repointed to §7 Open Item 2 below and the forces notation above; both locations verified |
| L5 — Primary definition misquoted | **GENUINELY FIXED** | "They shape formation pervasively" verbatim from the extracted CF V7.4 Part III |
| L6 — Round 1 review round unlogged | **GENUINELY FIXED** | 2026-09-10 entry added with verdict and counts. Omitted from the fix pass's own enumeration (R3 H6) |
| L7 — 687 scope qualifiers dropped | **PARTIAL / NEW DEFECT** | "markup stripped" and div2 restored; the trailing qualifier imported from Doc_03's "plenary Council" row instead (R3 L1) |
| L8 — Forces Framework consequence unengaged | **GENUINELY FIXED** | Rule quoted verbatim from FF §4 Step 4 at the forces notation and again at Open Item 6, with the partial answer named as partial |
| L9 — summary column silently renamed | **GENUINELY FIXED** | Restored to Template §4's "Cross-Strand (or declared substitute) status". Stale back-reference at §5 (R3 L2) |
| L10 — two Doc_03 entries cited as one | **GENUINELY FIXED** | Both named, tags quoted per-row and verified exactly, grounds distinguished, and the 119 figure attributed to `preaching` alone |
| C1 — Status/Disposition duplication | **GENUINELY FIXED** | Duplicate CO-022 sentence removed from the Status line. The surviving copy's subject is now stale (R3 H6b) |
| C2 — V7.3/V7.4 pairing unnoted | **GENUINELY FIXED** | Stated in the Governed-by line, with what turns on it and what does not |
| C3 — Cand. 5's heading unmarked | **GENUINELY FIXED** | Heading now carries the label and the escalation |

**Totals, counted from the table above and checked to sum: 22 genuinely fixed · 4 partially fixed · 0 not fixed · 1 properly escalated = 27.**

- **Genuinely fixed (22):** H1, H2, H4; M1, M2, M3, M4, M5, M6, M7; L1, L2, L3, L4, L5, L6, L8, L9, L10; C1, C2, C3.
- **Partially fixed (4):** H3, H6, H7, L7 — of which **H3, H7 and L7 additionally introduced or left standing a new defect**; three of the "genuinely fixed" (M1, L1, C1) also introduced a smaller one.
- **Not fixed (0).** Nothing is byte-identical at a site the pass claims to have fixed — the previous round's signature failure is genuinely gone.
- **Properly escalated (1):** H5, honestly recorded at four places including the contrary Round 2 assessment — and not carried into the four downstream sites the escalation itself names (R3 H1).

**Against the document's own claim of "26 of 27 addressed":** the count is defensible as a headline and is not supported by the document's own enumeration (25 listed), and four of the 26 are partial rather than closed. This is the fourth consecutive round in which the fix pass's self-certification overstates, though by a much smaller margin than the previous pass's 38/38 over three untouched findings.

---

## Escalation-category assessment (CO-022)

Run against all four categories, with near-misses checked rather than assumed away.

**1. Representative-identity decisions — does not apply.** Nothing in Doc_04 names, titles, characterizes or constrains this world's Representative. The `[CT]` tag cells that constituted Round 1's near-miss remain correct, re-derived per-row this round.

**2. Portfolio-level / cross-world decisions — does not apply.** The five IJC precedent claims were not edited this pass and spot-check accurate; Open Item 3's withdrawal of the false second-world claim stands and is untouched. The *Gesta* corpus-map assignment is applied, not made, and was made on the record at PR #177. The Framework/Template mismatch is routed to IJC's existing System Hub item and no new one is opened.

**3. Governance / methodology decisions — TRIPPED, at low intensity, on one limb, and the limb has moved again.** Round 2 tripped this on H7's certification defect and recommended the word-level-diff discipline as a condition of the next pass rather than as a portfolio rule. That discipline **was** applied, and it worked for what it covers: nothing is byte-identical this round. What it cannot cover is the failure mode that replaced it — three claims about untouched destinations inside this document (R3 H1, H2), which by construction do not appear in a diff. This is a build-thread verification fix, not a methodology change for the portfolio: the additional check needed is one sentence long ("for every fix that names a destination, open the destination"), and it belongs as a condition of the next fix pass, not as a new rule. **Recommend it be added to the existing condition rather than escalated.**

**4. Unresolved tensions the pipeline can't close — occupied, and not this review's to settle.** Candidate 5's classification is escalated to the project lead on the project lead's own direction of 2026-09-13. This review takes no position on whether Tensional is earned and does not reopen the question; the commission excluded it and the escalation is live. What this review does assess is whether the escalation is *honestly recorded*, and the answer is **half**: it is recorded fully and fairly at §3, §7 Open Item 7, the Disposition and the Decision Log — including Round 2's contrary assessment, stated in Round 2's own terms and not softened — and it is recorded nowhere else, while four sections continue to present the classification as settled and one of them carries it downstream to Doc_05/Doc_07/Doc_08 (R3 H1). That gap is a build-thread fix within this document, not an additional escalation.

**Result: one category tripped (category 3, governance/methodology), at low intensity, on a verification-discipline limb inside this document's own fix cycle; category 4 is already occupied by a live escalation made outside the pipeline. Categories 1 and 2 do not apply. This review proposes no new escalation.**

---

## Note on disposition — deliberately not assessed

Consistent with this folder's practice across the Doc01, Doc02, Doc03 and Doc04 Round 1–2 series, this review does not recommend a disposition. Doc_04's Status line and Disposition both state that a substantial revision returns to independent review before disposition, and the sequencing is the build thread's and the project lead's to run.

Two observations offered without recommendations attached.

**First, on the shape of what is left.** Of 20 findings, 8 are internal-consistency defects (claims this document makes about its own other sections), 6 are citation- or attribution-accuracy defects, 3 are cosmetic, and 3 concern the reasoning. Not one is a misquotation of an external governing document — which is new, and is the strongest thing that can be said about this pass. Every governing quotation this round's commission asked to be independently re-derived checked out verbatim, including the ones the fix pass introduced. The document's hardest substantive judgments all continue to hold: §2's fragmentation reading, the demotion of Doc_01's third-named candidate, the refusal to let Candidate 2's cross-phase lean survive, the Framework/Template correction, and now the refusal to argue a contested classification a third time. What does not hold is the document's account of itself.

**Second, on the mechanism.** Four of this build's last five rounds have found the same class of error, and it has now migrated. Round 1: fabricated and misattributed quotations. Round 2: a pointer repointed to a real target with the claim carried across unchecked. Round 3: **a fix announced at a destination that was never opened** — Open Item 1, and the four sites §3 declares provisional. The common root is unchanged: *a check that proves something adjacent to the claim, then trusted because it returned something.* The previous remedy (read the full word-level diff) answers the previous form and is structurally blind to this one, because an untouched site produces no hunk. The next remedy is the mirror of it: for each finding, list the destinations the fix claims to reach, and read each destination at HEAD — not in the diff. On this round's evidence that single step would have caught R3 H1, H2 and half of H6.

---

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 6 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC, 20 in total. Fix-pass verification: 22 of Round 2's 27 findings genuinely fixed, 4 partially fixed, 0 not fixed, 1 properly escalated; 3 of the partials and 3 of the fixed introduced a new defect.**

**Simulated review — informational only, not an Article 31 substitute.**
