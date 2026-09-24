# Doc_01 Round 4 — Independent Adversarial Review: The Reformed Cities — Zurich & Geneva

**Document under review:** `World-Builds/Reformed-Zurich-and-Geneva/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, Revision 5, 2026-09-15), at commit `6c5a615` on branch `reformed-cities-doc01`.
**Prior rounds:** `Doc01_Round1_Review.md` — SUBSTANTIAL REVISION REQUIRED, 6 high / 13 medium / 13 low, against Revision 1. `Doc01_Round2_Review.md` — SUBSTANTIAL REVISION REQUIRED, 3 high / 9 medium / 11 low, all new, against Revision 2. `Doc01_Round3_Review.md` — SUBSTANTIAL REVISION REQUIRED, 2 high / 4 medium / 8 low, against Revision 4, with the reviewer's own verdict that the substance had stabilized.
**Review date:** 2026-09-15
**Reviewer:** independent adversarial review, run in isolation per `cic-build-cycle`. No drafting context seen.

**Scope, per `CLAUDE.md`'s Round-2+ discipline and this project's cost rules.** A targeted recheck. The effort went to two places: whether each of Round 3's fourteen findings is actually fixed, re-verified against primary sources rather than against Revision 5's own account of itself; and what Revision 5's own diff (`git diff f7b5028 6c5a615`) introduces, since a fix round producing the next round's defects is the pattern that has held in all three prior rounds. Round 1 and Round 2 findings were spot-checked, not re-litigated.

**Sources re-opened directly for this round:**

- `cic-website/data/world-census.json` — VI.2, VI.9, VI.26 and the `latin-pastoral-congregational-christianity` → `the-reformed-cities-zurich-and-geneva` transmission edge, read as parsed JSON, quotations diffed character by character in Python
- `reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` — Articles 21, 22, 29, extracted from `word/document.xml`
- `reference/L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — Section 5
- `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — Part I
- `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml` — parsed; rows and distinct source files counted
- `World-Builds/Reformed-Zurich-and-Geneva/CiC_Reformed_Zurich_Geneva_Doc01_Scope_Confirmations_2026-09-15.md` (read in full — new this revision)
- `World-Builds/Reformed-Zurich-and-Geneva/CiC_Reformed_Zurich_Geneva_World_Build_Thread_Launch_2026-09-15.md` (read in full)
- `Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md`; `World-Builds/Gallic-Monastic-Ascetic-Christianity/gallic_Representative_Construction_Notes_Renatus.md` §285/§488; `World-Builds/Cappadocian/CAPPADOCIAN_BUILD_LEDGER.md` §188; `World-Builds/Desert-Monasticism/CiC_W3_Representative_Identity_Preliminary_Decision.md`; `World-Builds/Imperial-Juridical-Christianity/Open_Gaps_Tracking.md`
- `Open_Gaps_Tracking.md`, `rzg_Decision_Log.md`; `CLAUDE.md`; the `cic-build-cycle` skill

---

## Verdict

**COSMETIC ONLY.**

**0 high, 4 medium, 6 low** — and the grading of that finding count needs saying plainly, because a count of ten could easily be misread as another substantial round. It is not one, and the distinction is the skill's own, not a courtesy.

`cic-build-cycle` defines the line: *"A revision is **substantial** if it changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary — anything a careful reader would notice as actually different. A revision is **not substantial** if it's wording, tone, formatting, or a typo fix."* I tested every finding below against that sentence. **None of them changes a substantive claim, a finding, a confidence rating as Doc_01 states it, or a scope boundary.** Every one is a record-keeping defect — a citation pointing at the wrong numbered item in its own cited source, a self-certification of a fix that was not performed, a quotation normalized where it should have been reproduced, a claim about provenance that cannot be checked. All four mediums sit in the record layer — the newly filed confirmation record and `Open_Gaps_Tracking.md` — and none is in the document's argument.

**Round 3's two high findings are genuinely closed, verified independently rather than accepted on Revision 5's account.**

- **H1 — the unfiled attribution.** `CiC_Reformed_Zurich_Geneva_Doc01_Scope_Confirmations_2026-09-15.md` now exists, is dated, reproduces both questions with three named options apiece and an explicit trade-off for each, records a selection against each, and is cited by path from most of the places that assert the confirmation. It follows a real, existing project precedent shape — `World-Builds/Desert-Monasticism/CiC_W3_Representative_Identity_Preliminary_Decision.md`, which likewise preserves the grounded-options presentation a decision was made from and marks the selected option inline. The two precedent quotations the record cites in its own opening (`Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md`'s "ADMITTED, 2026-09-13. Mark's own word, in session... 'yes, admit it.'" and Gallic's §285 "CONFIRMED, 2026-09-12... 'Confirm as drafted.'") I re-opened and diffed: both character-exact, both now correctly path-cited, which also closes Round 3's L3. This is a real remedy, not a re-assertion in a new file. It has two defects (M1, M4 below), neither of which returns the document to the unfiled state H1 described.
- **H2 — the three stale sections.** I ran the grep Round 3 asked for rather than trusting that it had been run, and checked every hit in context. `escalat` now returns seven occurrences in Doc_01: two in the masthead's account of Revision 3's escalation history, one in §5's reservation of the Representative question to Step 10, and four in §9's own escalation-category assessment. **None describes either confirmed question as open.** `PENDING` returns three, all Living Tradition Status — §1's own status line, §1's comparison to Donatism's LTS finding, and §8 item 10 — which is correct and is not one of the four categories. `provisional` returns two: §3's "Provisionally:" on the Doc_04 gravity candidates, which is correct, and §4's "on this now-settled premise, not a provisional one," which is the fix. `premise` returns three, in §4 and §5, all now stating the premise as settled or confirmed. §2's Temporal Scope answer now supplies the Framework's transition answer directly ("**Confirmed answer (§7 below):** the international Reformed dimension of Dort... remains internal to this world's own transmission; the specifically Dutch domestic controversy is the actual point of hand-off, to VI.26"), §2's Historical Pressures pointer is corrected, and §6's Cell 3B now records both boundaries as settled rather than escalated. Closed.

**The other twelve Round 3 findings, checked one by one:**

- **M1 (Dort delegate confidence) — fixed inside Doc_01 and `Open_Gaps_Tracking.md`, broken in the new file.** §7's option 1 now reads "(historiographically attested, not vendor-verified)", option 2 "attested Zurich/Geneva delegate participation", the confirmation paragraph "attested (not vendor-verified)", §8 item 3 "attested only in standard historiography, not confirmed against a primary source", and `Open_Gaps` item 2 "attested in standard historiography but not yet vendor-verified". Five locations, one formulation. Then the confirmation record, committed in the same commit, says "documented" twice. See M2 below.
- **M2 (§9's category-4 reasoning) — fixed, and fixed well.** The "no objection has been raised" sentence is gone. The replacement rests on the filed launch record, and I checked that record actually says what §9 now claims: it does — "Mark has directly authorized starting the build anyway — that's this launch," immediately after quoting Step 0's own "No build thread should open on the strength of this document alone." §9 also now describes the review record accurately ("Round 1 review's H1 and Round 2 review's M1 each raised this question directly"), which was the second half of M2. Round 3's suggestion that the deleted Revision-3 disclosure be restored was offered as an alternative, not as the remedy; the remedy given was taken.
- **M3 (cross-world propagation duty) — named accurately.** I checked `Open_Gaps_Tracking.md` item 13 against what Round 3 actually said was missing, not against Doc_01's summary of it. Item 13 names the obligation on VI.26, names the two places it needs to reach (the census entries and `world-build-docs/_cross-world/`), states that both are currently unchanged and still describe the scope question as fully open, quotes the skill's write-scope rule, and flags it to the project lead or a coach thread. That is the finding, not a softened version of it. It is carried in four further places (Doc_01 §7, §8 item 3, §9's category-2 bullet, Decision Log standing item 5), and §9 explicitly declines to treat the category as fully closed on its account. Correct handling.
- **M4 / L4 (Round 2's L1, the VI.9 quotation) — fixed, verified by my own character-by-character diff** against the live census JSON, not by trusting the log. `relationsSummary` is now reproduced verbatim, including the plain hyphen in "its own tradition - a real Step 0 call" and the curly apostrophe in "Remonstrants’ own entry". VI.26's `why` and `statusWord` and VI.2's `why` and `legacy` fragments also re-diffed: all verbatim.
- **M4 / L8 (Round 2's L11) — half fixed, and the unfixed half is certified as fixed.** See M3 below.
- **L1** (masthead revision line) — fixed; Revisions 4 and 5 both added.
- **L2** (Open_Gaps status block revision number) — fixed.
- **L3** (Gallic citation locus) — fixed; the claim moved out of §9 and into the confirmation record, correctly path-cited to both `Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md` and Gallic's own file, and §9's overreaching "same evidentiary standard" sentence is deleted rather than patched.
- **L5** (census field attributions) — fixed, both halves, verified against the parsed JSON: VI.26's addition is now cited to `statusDescription` with the correct quotation, and VI.9's undated `statusDescription` is now described accurately with the 2026-08-02 date attributed to VI.26 where it belongs.
- **L6** ("premise" residuals) — fixed in both named locations.
- **L7** (VI.9 characterization) — fixed; §7 now describes VI.9's scope as "the era's sharpest intra-Reformed contest and the refuge culture that sheltered much of the era's dissent, per VI.9's own `why` field," which matches that field.

**Primary-source spot-checks on earlier rounds' fixes, re-run rather than assumed.** Article 22's long quotation in §6, including the Writing-From-Inside tail; Article 21's two fragments in §5; Article 29's trigger clause and closing "method of confirmation" sentence in §1; the Forces Framework Section 5 Layer-1 register sentence in §6; the Framework's "When does one world become another?" and its "Questions include:" non-exhaustive framing — all verified against the `.docx` sources and all substantively exact. The corpus map parses to nine work rows across seven distinct source files, matching §8 item 7's count, with the *Selected Works* remainder still a single collective row and the Sixty-Seven Articles itemized separately, matching §8 items 1 and 6.

**§4 was not retro-fitted a second time.** Round 3 gave Revision 4 specific credit for leaving the counter-evidence honest after a confirmation that matched its own tentative reading. The word-level diff of Revision 5 against Revision 4 shows §4's finding paragraph changed in exactly one respect: the record path was added. Formation and authority still "favor treating them as two separate worlds," authority is still "permanently unconverged-within-window," independent origins is still "the single strongest fact cutting against a single-world reading." A second opportunity to quietly improve the argument for a settled conclusion was again declined. That is worth recording, because it is the failure Rounds 1 and 2 both found and it has now not recurred twice running.

**The shape of what remains.** Three of the four mediums are in the two files written for the record layer, and all three are the same defect in different clothes: a record that says something slightly other than what the document citing it says, or than what is actually on disk. That is the pattern this project has now recorded four rounds running — Round 2's H3 and M3, Round 3's H1 — and it is worth a coach thread's attention as a standing tendency rather than four unrelated slips. But the scope has collapsed: in Round 1 it reached the document's central judgments, in Round 2 its internal consistency, in Round 3 its attributions, and here only its cross-references.

---

## Medium-severity findings

### M1. The filed confirmation record says "Selected: Option 1"; five places in the build record say the project lead confirmed "option 2" — and they cite that record as their authority

This is the first check anyone would run against the new file, and it fails.

**What the record says,** for both questions:

> **Selected:** Option 1, "International Reformed dimension only (recommended)."
>
> **Selected:** Option 1, "One world, two strands (tentative reading, recommended to keep)."

**What the documents that cite it say:**

- Doc_01 §7: "**Confirmed: option 2** — Dort's international Reformed dimension treated as part of this world's own transmission."
- Doc_01 §9: "confirmed — option 2, Dort's international Reformed dimension in this world's own transmission."
- `Open_Gaps_Tracking.md` item 2: "**The project lead confirmed option 2, 2026-09-15... — record filed at `CiC_Reformed_Zurich_Geneva_Doc01_Scope_Confirmations_2026-09-15.md`**."
- `rzg_Decision_Log.md` line 29: "Dort's international Reformed dimension in this world's own transmission (option 2 of 3)."
- `rzg_Decision_Log.md` standing item 2: "option 2, international Reformed dimension in, Dutch domestic controversy to VI.26."

The two lists are inverted. Doc_01 §7 numbers them: 1 = Dort wholly out, 2 = international dimension (confirmed), 3 = defer. The record numbers them: 1 = international dimension (selected), 2 = Dort entirely out, 3 = defer. **A reader who follows the path to check "option 2 was confirmed" opens the record and finds that Option 2 is "Dort entirely out of this world's story" and that it was not selected.** The substance travels correctly alongside the number in all five places, so nobody is actually misled about the decision — which is why this is Medium and not High — but the number is false against the source it cites, and making the confirmation checkable was the entire purpose of filing the record.

**A second, related problem in the same seam.** Doc_01's masthead, §4 and §9 each state that the record reproduces "the options exactly as presented" (§4: "reproducing the options and trade-offs exactly as presented and the selection exactly as given"). §7 separately states that "Three options were presented, each with its own trade-off," and then gives three options whose order, numbering and trade-off wording all differ from the record's. Both accounts cannot be exact reproductions of the same presentation. §7's is plainly the document's own summary — its option 3 trade-off reads "avoided, since a real decision was available and taken," which is a retrospective gloss, not something that could have been put to the project lead before the decision. The document should say so rather than let two incompatible "as presented" claims stand.

**What the correct handling is.** Treat the record as authoritative on what was presented, and stop citing a bare option number from a list that no longer matches it. In all five places, name the option by its content and, if a label is wanted, use the record's own ("Option 1, 'International Reformed dimension only'"). In §7, mark the list as this document's own summary of the options rather than a reproduction, and drop or reconcile the "exactly as presented" claims in the masthead, §4 and §9 accordingly.

### M2. "Documented" is reintroduced twice inside the new confirmation record — the exact upgrade Round 3's M1 was filed against, and Doc_01 §7 expressly promises it does not occur there

Revision 5 unified the Dort-delegate confidence language across five locations. I verified every one. Then, in the same commit, the new record says:

> 1. *International Reformed dimension only (recommended)* — "Cite the Canons of Dort and the **documented** Zurich/Geneva delegate participation..."
>
> 2. *Dort entirely out of this world's story* — "...Drops the **documented** delegate presence from this world's own record even though both strands were physically represented there."

And Doc_01 §7, new in this revision, says:

> "This confidence level — attested in standard historiography, not yet checked against a vendored primary source — applies consistently wherever this delegation claim is repeated in this document and in `Open_Gaps_Tracking.md`; it is **not upgraded to 'documented' in the confirmation below or elsewhere**, since the scope decision itself does not depend on the delegation claim's own confidence level."

"Or elsewhere" is unbounded, and the record filed in the same commit is elsewhere. The sentence is false as written.

The harder half is not the wording. If the record is an accurate reproduction, then **the options actually put to the project lead described the delegate participation as documented** — which is to say, the confirmed decision was taken against an evidentiary description one confidence level higher than the one Doc_01 now carries. Doc_01's own mitigation is correct and I accept it — the scope decision genuinely does not turn on the delegate claim's confidence — but that is an argument for disclosing the discrepancy, not for a sentence asserting it does not exist.

**What the correct handling is.** Do not edit the reproduced options; a record's value is that it is not rewritten. Add a short note in the record stating that the options as presented used "documented" and that Doc_01 §7, §8 item 3 and `Open_Gaps` item 2 carry the calibrated confidence (attested in standard historiography, not vendor-verified), with the reason the decision does not depend on it. Then narrow §7's sentence to the scope it can actually hold — this document and `Open_Gaps_Tracking.md` — rather than "or elsewhere."

### M3. `Open_Gaps_Tracking.md` item 15 certifies a fix that was not performed — inside the entry filed to record Revision 4's certifying a fix that was not performed

Item 15, new this revision, reads:

> "**Two Decision Log inaccuracies — found 2026-09-15, Doc_01 Round 2 review (L11), still open after Revision 4.** `rzg_Decision_Log.md` recorded the Round 1 and Round 2 reviews as 'model=Opus'... and **this file's own trailing Doc_01 status block was left outside the numbered-entry, append-only structure the rest of this file uses**, against `CLAUDE.md`'s 'Entries are append-only and numbered.' **Both corrected in Revision 5 / this pass.**"

The trailing status block is still outside the numbered structure. It sits below the horizontal rule after item 15, beginning "**Doc_01 — World Identification, Boundaries, and Orientation.** DRAFT, Revision 5 as of 2026-09-15," followed by six unnumbered bullets. Nothing in the Revision 5 diff of that file touches its structure. The first half was handled — "model=Opus" is retained in the Decision Log but now carries an accurate disclosure of what it is and is not ("a fact about how the review was requested, not a claim the review artifacts themselves make") — which is a legitimate discharge of Round 2's L11. The second half was not, and is certified as if it were.

This matters more than a numbering convention would on its own. Round 3's M4 was specifically that Revision 4 had certified findings closed that were not, and items 14–15 exist because of that finding. An entry written to correct a false closure claim, containing a false closure claim, is the third occurrence of this shape. `cic-build-cycle`'s coach-verification standard is "that the Decision Log matches what's actually on disk"; here it does not.

**What the correct handling is.** Either bring the trailing status block inside the numbered structure, or — if it is deliberately a document-status footer rather than a gap entry, which is a defensible reading — say that in item 15 and in the file's own header convention note, and stop recording it as corrected. Either is a one-edit fix. Do not leave the claim standing.

### M4. The record explains the absence of the project lead's own words by asserting a "decision tooling" mechanism that nothing in the repository documents — where Round 3 asked for either the verbatim words or a plain statement that they cannot be supplied

The record's closing paragraph:

> "Both selections were made directly by the project lead, in this build thread's own session, via the options exactly as reproduced above — not paraphrased or reconstructed after the fact. **This is the mechanism this project's decision tooling uses for an in-session choice among named options; it is not a chat message this document is separately attesting to.**"

Round 3's H1 set out two acceptable remedies: reproduce the project lead's own words verbatim alongside the options, *or* — "if the exact wording cannot be reproduced, say so plainly in that record and state what can be attested." The record takes neither. It asserts a third thing: that a mechanism exists which makes verbatim words inapplicable.

I looked for it. The phrase "decision tooling" appears nowhere else in the repository. No project document describes a structured option-selection mechanism. Every project-lead decision record I could find records a chat message quoted verbatim — the three the record itself cites (`WORLDS_REGISTRY_LOG.md`, Gallic §285, Cappadocian §188), plus `World-Builds/Imperial-Juridical-Christianity/Open_Gaps_Tracking.md`, which preserves Mark's own words even where he overrode the build thread's recommendation ("my name is Mark and i don't want to identify with this world"). Desert Monasticism's identity decision record is the one precedent that does not quote him directly — and it says so, reporting "the project lead's own stated reasoning" as reported reasoning and noting that the options below are "preserved verbatim for the record."

I am not asserting the claim is untrue; such a mechanism is entirely plausible and the confirmations themselves are corroborated across four files and a commit message, with nothing anywhere contradicting them. The problem is narrower and it is the same one H1 identified: **the sentence that explains why the record is not checkable in the ordinary way is itself not checkable.** This is the fourth round in which a supporting claim offered in aid of a fix — Round 2's `don`-registration precedent, Round 2's Donatism LTS analogy, Round 3's "same evidentiary standard" — does not verify as stated.

**What the correct handling is.** Name the mechanism concretely enough that a reader can identify it, or replace the sentence with the plain statement Round 3's fallback asked for: no verbatim text of the project lead's reply is available; what is attested is that the selection was made in-session on 2026-09-15 against the options as reproduced. The record is not weakened by saying that — it is what makes it a record rather than an assertion.

---

## Low-severity findings

**L1.** §6's quotation of the census transmission edge is not character-exact, in the same way Revision 5 just finished fixing for VI.9. The census note (`latin-pastoral-congregational-christianity` → `the-reformed-cities-zurich-and-geneva`) uses double hyphens: "irresistible grace **--** Calvin named Augustine" and "no institutional continuity **--** influence, not identity." Doc_01 renders both as em dashes, inside quotation marks presented as the census's own words. The same passage also inserts an ellipsis ("Scripture itself**...** A direct theological line") where the census has a full stop and nothing is elided. Diffed in Python against the parsed JSON. This is Round 2's L1 recurring in a location nobody swept — one bullet list away from the one that was fixed.

**L2.** `Open_Gaps_Tracking.md`'s trailing Doc_01 status block remains unnumbered (the substance of M3 above, recorded separately here because it is also a live `CLAUDE.md` convention breach independent of the false closure claim).

**L3.** `rzg_Decision_Log.md` line 31 states "All 14 Round 3 findings are addressed," and Doc_01 §9 carries the parallel claim that Round 3's findings "were bounded citation, propagation, and consistency work, addressed in this revision (Revision 5)." On this round's checking, Round 3's L8 is addressed in two of three parts and its M4 in two of three. Round 3's M4 named this exact certification habit; Revision 5 softened §9's version but did not remove it from the log. Line 27's "All 23 Round 2 findings are addressed" carries the same form. State what is true and name the exceptions, which is a stronger record than a completeness claim.

**L4.** Three of the places asserting the confirmation still do not carry the record's path: Doc_01 §1's Short Description, Doc_01 §5's opening premise sentence, and `rzg_Decision_Log.md` line 29's "Both confirmed by the project lead" paragraph. Each is within a short reach of a location that does cite the path, so this is minor — but Round 3's remedy was to cite it from each of the nine, and the Decision Log paragraph in particular is one of the nine Round 3 enumerated.

**L5.** Doc_01 silently normalizes the Constitution's and Forces Framework's curly apostrophes (U+2019) to straight ones inside quotations presented as verbatim — Article 21's "a gravity's centrality," Article 22's "the world's own formation logic," the Forces Framework's "the world's own consciousness." This is consistent across the document and clearly a file convention rather than a transcription error, and I do not treat it as a defect on its own. It becomes one only against Revision 5's own handling of the census apostrophe, where the opposite normalization was graded a finding and fixed. Pick one stated convention — either reproduce source punctuation exactly everywhere, or state the normalization in the document's header and apply it everywhere — rather than holding one source to a standard the others are exempt from.

**L6.** *Procedural, not a finding against the content.* `Review-Artifacts/Doc01_Round3_Review.md` entered git history in commit `6c5a615`, the same commit as the Revision 5 that answers it. Round 2 flagged this pattern, Round 3 flagged it recurring, and it has now recurred a third time. The artifacts do exist and do say what they are cited for — I read Round 3 in full before reading Revision 5 — so `cic-build-cycle`'s "review rounds exist as files, not claims" rule is met in substance. But a review artifact and the revision answering it landing in one commit means the file's existence cannot be independently dated ahead of the fix, which is the property the rule is protecting. Worth a coach thread's attention as a standing habit across this world's build. This artifact is written before any Revision 6 exists.

---

## Independent escalation-category check

Run fresh against all four categories, on Doc_01 Revision 5's own final content, not on §9's claim about itself — and, per the brief, testing whether §9's *conclusion* is right, not only whether its reasoning hangs together.

**1. Representative identity, name, or title decisions — not live.** §5's cross-strand paragraph is again the only approach to this category, and it is unchanged in Revision 5. It establishes that the two-strand structure is real and substantial, states that this "directly bears on the Representative-construction question... a single Representative versus a genuine multi-figure Representative," and declines it: "This document does not decide the Representative question itself; per this build's own escalation categories, that decision is reserved for the project lead directly, at Step 10." Checked against the filed launch record, whose stop-condition 2 names this world's one-versus-multi-figure choice specifically. Doc_01 neither makes nor prejudges it. Nothing in Revision 5's diff touches this. **Correctly assessed.**

**2. Portfolio-level or cross-world strategic decisions — discharged.** Both questions are genuinely portfolio-level, both are labelled as such where recorded (§7 quotes the skill's own definition; §9's bullet repeats it), and both are now confirmed by the project lead against a filed, dated record rather than self-resolved. The two defects I found in that record (M1's option numbering, M4's provenance sentence) are conditions on how well it is written, not on whether the decision was the project lead's — nothing anywhere in the repository contradicts either confirmation, and the substantive boundary is stated identically in all six prose locations I checked. M3's propagation obligation remains owed and is correctly named rather than absorbed: §9 explicitly declines to treat the category as fully closed on its account, which is the right handling given that the census and `world-build-docs/_cross-world/` are outside this build thread's write scope. **Discharged; §9's conclusion is right, and this time its reasoning is too.**

**3. Governance or methodology decisions — not live.** Nothing in Revision 5 changes how the build process works. The masthead's registry-timing question is still named as open rather than answered, which is not a governance decision. Filing a decision record of this shape is not a methodology change — it follows `CiC_Reformed_Zurich_Geneva_World_Build_Thread_Launch_2026-09-15.md` in this same folder and Desert Monasticism's own identity decision record. M4's "decision tooling" sentence is a descriptive claim about how one decision was taken, not a change to how decisions are taken. **Correctly assessed.**

**4. Unresolved tension the pipeline can't close on its own — not live, and now for the right reason.** I tested all three of the skill's named instances plus the general case and plus this round's own findings:

- *Two reviews disagreeing with each other* — Round 3 and this round do not disagree. Round 3 found the substance sound and asked for bounded record work; I independently reach the same finding on the substance and find the record work largely done. Rounds 1 and 2 did not disagree with each other either. No.
- *A contradiction between two already-cleared master documents* — Step 0 is DRAFT and uncleared, so the Step 0 defects at `Open_Gaps` items 8 and 11 cannot trigger this limb. The census is live data rather than a cleared build document, and §7's confirmation does not contradict it: the census leaves the question open and the confirmation settles part of it, with the gap between them already named as the propagation duty at item 13. No.
- *A finding that cuts against an earlier decision* — the two logged Step 0 defects are citation and factual errors in Step 0's distinctness section; neither bears on Step 0's Tier-1 rating, and the filed launch instruction asked for exactly this kind of finding to be "report[ed] plainly," which Doc_01 does in §7 and §8 item 4. No.
- *The Step 0 sequencing exception* — §9's reasoning is now sound, which it was not in Revision 4. I verified the launch record independently: it quotes Step 0's own "No build thread should open on the strength of this document alone" verbatim and then records "Mark has directly authorized starting the build anyway — that's this launch." Category 4 routes unresolved tensions *to* the project lead; here the project lead ruled, having been shown the thing in its own words, and the ruling is filed and citable by path. That closes the tension. No.
- *This round's own findings* — none of the four mediums is an unresolved tension. Each is a correctable inconsistency between two files inside this build thread's own write scope, with an obvious remedy. No.

**Conclusion: no escalation category is live against Doc_01 Revision 5's content.** Round 3 reached the same conclusion against Revision 4 and found §9's reasoning unsound on one of the four; that defect is repaired, and §9 now reaches the right answer for the right reason on all four.

---

## What this means for disposition

Per `cic-build-cycle`'s *Revision decision* stage: **"If cosmetic only: apply it directly, note that it was applied, and move on without a fresh review cycle."** That is this round's verdict, so no Round 5 is required.

Doc_01 has cleared an independent review without that review calling for substantial revision, and no escalation category applies. **The build thread may self-apply "Approved to proceed"** — the skill is explicit that this disposition "does not require a per-document reply from the project lead" when no escalation category is live, and it "claims nothing about the document being complete, correct, or closed." It unblocks Doc_02 and nothing more.

Three conditions on that, none of which blocks it:

1. **Apply the ten findings above first, and note in `rzg_Decision_Log.md` that they were applied as cosmetic under the skill's own rule** — not "addressed," and not certified as a complete sweep. M3 exists because that habit produced a false record twice.
2. **Frozen is not in reach and is not being claimed.** Living Tradition Status remains PENDING under Article 29 and is a freeze-eligibility gate, correctly tracked at `Open_Gaps` item 10 as non-blocking at this stage.
3. **The propagation duty (`Open_Gaps` item 13) does not go quiet.** It cannot be discharged from inside this build thread's write scope, and it is the one finding in this round with consequences outside this world: a future VI.26 or VI.9 build thread reading the census today would find the Dort scope question described as fully open and would have no way to learn that part of it was settled on 2026-09-15. It should reach the project lead or a coach thread as an item in its own right, not only as a line in this world's own gap log.

---

*Filed per `cic-build-cycle`: review rounds exist as files, not claims. Two procedural notes, neither a finding against the document's content. (1) The review-artifact commit-timing pattern is recorded at L6 above rather than here, because it has now recurred three times and is worth a coach thread's attention. (2) Round 1's note on the `Ministry/` versus `Review-Artifacts/` placement inconsistency in `CLAUDE.md` stands unresolved through four rounds; this review follows the precedent all three prior rounds set. This review was run from an isolated worktree at `6c5a615`; the branch `reformed-cities-doc01` is checked out elsewhere. The reviewed content is the branch tip as the brief specified.*
