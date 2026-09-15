# Step 0 — Movement-Scope Confirmation: Latin Pastoral-Congregational Christianity
## Round 3 Independent Adversarial Review

**Document reviewed:** `worlds/lpc/Step0_Movement_Scope_Confirmation.md` (second revision, commit `94a28404`, dated 2026-09-01)
**Review date:** 2026-09-01
**Reviewer:** independent adversarial review thread; did not draft the document under review and did not write the Round 1 or Round 2 reviews
**Governed by:** `cic-build-cycle` (CO-022) *Review* section, and this project's standing rule that a revision's own claim to have fixed something is not evidence of a fix. Every Round 2 finding was re-checked directly against the actual source file — the Constitution extract, the Methodology extract, the Step 0 Conclusion extract, CF V7.4, the three corpus-map files, IJC's and Hieronymian's built documents and record sets, the Donatism sibling-branch draft read via `git show`, and the `cic-build-cycle` SKILL text — not against Round 1's or Round 2's account of any of them. The Round 1 and Round 2 review files were re-read in full before §6's revision history was assessed.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Nine of the ten Round 2 findings are verified genuinely fixed on independent re-check against source, including all three residues of H5.** The A1 floor enumeration is now word-for-word Article 4 on all five commitments; the Cyprian/IJC verification claim is now accurate at the scope it claims; the Antiochene carry-forward is real and its three quotations are exact; the Optatus pre-judgment is gone and replaced with the three actual options; the §5 item flagging IJC's identical A1 defect exists and its claims about IJC check out. This is a careful revision and the verdict is not a judgment on its quality.

It nonetheless needs another round, for three findings that meet CO-022's own "substantial" test (*"changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary"*):

- **N3 is only partly discharged.** The Optatus/blanket-rule correction landed in §3 B3 and §4 item 2 but was **not propagated to §2 A5**, which still states the blanket form — *"never 'the schism-crisis angle'"* — two sentences after the paragraph that binds Doc_02 to reconstruct the Donatist schism using Augustine's anti-Donatist corpus. §3 B3 now explicitly names that reading as wrong and as conflicting with §2 A5's own obligation, while §2 A5 continues to assert it. That is N3(b)'s contradiction surviving at its source location (NEW-1).
- **A quotation in that same §2 A5 sentence is not a quotation.** *"The ordinary pastor navigating persecution"* is presented in quotation marks and attributed to the Step 0 Conclusion. That string appears nowhere in the Step 0 Conclusion, or anywhere else in this repository. The Conclusion reads *"working pastor navigating the Decian persecution and its aftermath."* Missed by Round 1 and by Round 2's explicit "every quotation traced to source" pass — logged below as a disagreement with Round 2 (NEW-4).
- **§6's disposition sentence, fixed for N5, sets a lower bar than CO-022 in its next clause.** It says the eligibility and tier conclusions *"may still inform Doc_01 once escalation is acknowledged."* CO-022 stage 4 says escalate "and wait"; stage 5 says the next document begins only once this one has "reached at least 'Approved to proceed'" (NEW-3).

The required work is again small and localized — essentially two sentences in §2 A5 and one clause in §6. **None of it touches the document's conclusions, which survive this round intact: World #8 clears Section A, and Tier 1 is the right tier.** Because the document already cannot self-dispose (correctly — see the disposition assessment below), this verdict does not change its destination; it means the three edits should be made and re-reviewed before the document goes to the project lead, not that the escalation is in doubt.

---

## Part 1 — Round 2 findings re-verified against source

### H5-r (High residue) — **ALL THREE RESIDUES FIXED; VERIFIED GENUINE**

Checked word by word against `docx_extract/constitution.txt`, "On the Scope of 'Movement'" (commitments at lines 161–165).

**Residue 1 — verbatim enumeration.** §2 A1 now reads *"Article 4's five commitments, quoted exactly, not paraphrased or abridged:"* followed by all five. I diffed each of the five against the Constitution programmatically:

| # | Result |
|---|---|
| 1 | **verbatim, byte-identical** |
| 2 | **verbatim, byte-identical** |
| 3 | verbatim; the Constitution's nested curly doubles around *"became truly human"* render as straight singles |
| 4 | verbatim; the Constitution's curly apostrophe in *Christ's* renders straight |
| 5 | **verbatim, byte-identical** — "together" restored |

The only deltas are the document's house straight-quote/apostrophe convention, which is the same convention Round 2 examined at C1 and declined to press, applied consistently across the whole file. On that convention the enumeration is exact, the "not paraphrased or abridged" claim is now true, and the abridgement Round 2 tabulated is gone. Article 4's own prohibition sentence is still quoted exactly ahead of it, and the document still disclaims restating the floor on its own authority — quoting Article 4 verbatim with attribution is not the "restate it independently" the Article forbids, and is exactly what Round 1's H5 fix instruction authorised.

**Residue 2 — "the fifth" → "the first".** Fixed. The parenthetical now reads *"because the first commitment is directly at issue for this world (immediately following)"*, and the argument that follows is the anti-Manichaean one about the first commitment. No contradiction remains. I re-verified the supporting claim independently: `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` exists and the LPC corpus map assigns ten rows out of that file to this world.

**Residue 3 — the IJC propagation flag.** Fixed, and its claims check out. New §5 item 5 exists. I confirmed both of its factual assertions directly: `Imperial-Juridical-Christianity/Step0_Movement_Scope_Confirmation.md` §2 A1 (line 26) still carries the identical four-item restatement — *"full divinity and consubstantiality of Christ, true humanity, the Passion/resurrection/ascension/return, and the Spirit as Lord and giver of life, worshiped and glorified with the Father and Son"* — and that document's status line reads *"Cleared review (Round 3, COSMETIC ONLY) — Approved to proceed."* The scope disclaimer ("outside this thread's write scope") matches the SKILL's own line, *"A build thread's write access is scoped to its own world's build folder."*

### N1 (Medium) — Cyprian's appearance in IJC's Doc_01 — **FIX VERIFIED GENUINE**

Re-run independently, not inherited from Round 2. A case-insensitive search of the whole IJC build folder returns three "Cyprian" hits: the thread-launch file, IJC's own Step 0 §3, and `Doc_01_World_Identification_Boundaries_Orientation.md` line 98. That line falls under the heading at line 91, **`## 6. World Continuity & Distinction`** — so the document's "§6's World Continuity & Distinction section" is exactly right. `Doc_02_Source_Ecology.md` returns zero. The quoted fragment *"World #8 (Latin Pastoral-Congregational Christianity, not yet built — Cyprian and Augustine): already confirmed distinct..."* matches the source. The bullet's conclusion — named as this world's own figure, never as an IJC actor, therefore **distinct** — is correct and now earned.

### N2 (Medium) — the "no other world has run a per-world Step 0" contradiction — **FIX VERIFIED GENUINE**

The replacement clause reads: *"not as evidence toward any prior world's own score — the only prior per-world Step 0 confirmations, IJC's and the parallel Donatism draft, each score only their own world, never another world's B1, and neither Hieronymian nor Desert Monasticism has a Step 0 confirmation of this kind at all."* No longer contradicts §0, §5 item 1 or §5 item 2.

Substance re-checked rather than accepted: a repository-wide search returns exactly two `Step0_Movement_Scope_Confirmation.md` files in this working tree (IJC and this one), plus the single-file Donatism directory on the sibling branch. IJC's Section B scores only World #6; Donatism's scores only World #4. Donatism's B1 does *reference* "World #6's B1 disclosure" as a comparison — that is a citation, not a score, so the claim survives the check. The CF grounding is also correct: *"Assess Formation Narrative Sources"* sits at `cf_v74.txt` line 608, inside the **Step 2 — Source Ecology and Source Registry** activity list (and so does *"Name the Affirmative Duty... (Article 20)"*, which independently re-confirms M2's routing).

One wording looseness noted at NEW-9 below; not a defect in the fix.

### N3 (Medium) — the Optatus material — **THREE OF FOUR SUB-ITEMS FIXED; N3(b) SURVIVES IN §2 A5**

Fixed and verified:

- **N3(a), in §3 B3.** The parenthetical is now correctly scoped: *"sits inside the sentence characterizing Cyprian specifically, not a blanket rule excluding all schism-related material from this world."* Verified against Step 0 Conclusion line 20 — the parenthetical does sit inside the Cyprian clause.
- **N3(c).** *"Should very likely be re-homed there"* is gone from §4 item 2(a) (I confirmed it was there in the prior revision and is absent now). Both §3 B3 and §4 item 2(a) now name the three actual options — re-home to Donatism / hold here as the Catholic-side tradition per the map's stated reason / double-place as the Council of Carthage row is — and say Doc_02 "must actually resolve, not inherit silently and not pre-decide." The corpus-map row itself re-verified: `author: optatus`, `role: tradition`, `confidence: provisional`, note *"Provisional only because the entry choice is inferred from region and date - Mark may prefer another Latin home for a Numidian polemicist"* — quoted exactly, and the document's gloss ("a question about which *Latin* world, not a proposal that it move to Donatism specifically") is a fair reading of that note.
- **N3(d).** Re-attribution done correctly. *"THE primary source for Donatism"* is verbatim in `cic/texts/README.md` line 135 and is now credited there. Donatism's own §3 B1 is now described as listing Optatus *first among its own documentary assets*; I read the branch file and confirmed Optatus is the first bullet, that *"the earliest substantial Catholic polemical treatise against the schism"* is exact, and that *"by far the largest body of surviving evidence"* is exact and attaches to Augustine's anti-Donatist corpus.
- **The supporting counter-argument checks out.** All three Augustine anti-Donatist works the document names — *On Baptism, Against the Donatists*; *Answer to the Letters of Petilian*; *The Correction of the Donatists* — are `confidence: assigned` to this world in the LPC corpus map (lines 82–86, 192–196, 550–554). The document's claim that a blanket reading would exclude them is therefore sound, and it does **not** contradict the Article 23 obligation; §3 B3 and §4 item 2 are now internally consistent with §2 A5's obligation paragraph.

**What is not fixed — see NEW-1.** §2 A5's final paragraph still deploys the parenthetical unscoped, and in a stronger form than the Conclusion itself uses.

### N4 (Medium) — the Antiochene primary-gravity contrast — **FIX VERIFIED GENUINE**

A new final B3 bullet exists, and a new §4 item 7. Every quotation re-derived from `docx_extract/step0_conclusion.txt`:

- *"pending a validated primary-gravity contrast against world #8 that doesn't rely on geography or language"* — **exact** (line 67). The document's ellipsis after "held out of Phase One" elides only "— carried forward to Possible Future Worlds below,"; non-distorting.
- *"its distinctiveness from world #8 is not yet demonstrated once geography and language are set aside"* — **exact** (line 73).
- *"rich ordinary-lay ethical-formation material"* — **exact** (line 73).
- The claim that the Conclusion names this world "by number, twice" — **confirmed**; lines 67 and 73 both say "world #8".
- The B3 framing ("B3's own test is 'judged relative to what is already selected or built for the phase,' which does not reach an unselected candidate directly") matches the Methodology's B3 line exactly, and Antiochene is indeed carried to Possible Future Worlds rather than selected.
- The document's honest note that B2's superlative is "scoped to the *confirmed* portfolio and stands as written" is accurate to B2's own wording.

**The compounding half of N4 is also fixed.** The World #5 / World #2 bullet now reads *"no adjacency this close to **either** was flagged in the Step 0 Conclusion for this pairing."* I checked every "world #8" occurrence in the Conclusion: the flagged #8 adjacencies are World #6 (in the #8 entry), World #9, Donatism (via the Primary-gravity-first rule at line 55), Antiochene (lines 67, 73), and the Tertullian dropped-voice item. None concerns World #5 or World #2. The scoped claim is true.

### N5 (Medium) — §6 does not state CO-022's disposition consequence — **FIXED IN SUBSTANCE; TWO RESIDUES**

§6 now carries, in bold: *"Because a standing escalation category applies, this document does not self-dispose, whatever any review round returns."* That is the sentence Round 2 asked for, and it is correct against the SKILL: *"A document only becomes eligible for disposition when it has cleared an independent review without that review calling for substantial revision, and none of the four escalation categories applies."* The substance of N5 is discharged.

Two problems with the fix itself: the rule is misquoted (NEW-2), and the sentence that follows re-opens part of what it just closed (NEW-3). Both below.

### N6 (Low) — branch-state rationale in §2 A5 — **FIX VERIFIED GENUINE**

The branch-unmergedness rationale is gone. §2 A5 now reads: *"What actually limits full cross-checking is not branch-unmergedness — the sibling branch is fully readable via `git show`, and was read that way for this document (§0) — but that Donatism currently has only its own Step 0 confirmation to check against, not yet a Doc_01 or Doc_02."* I re-ran `git show origin/claude/record-native-world-build-v2-e2s0dt:worlds/don/Step0_Movement_Scope_Confirmation.md` myself (132 lines, byte-identical to the copy already extracted for this session). Its §3 B3, line 94, reads *"Not built yet, so no live cross-document check was possible"* — the document now quotes that exactly and attributes the reason correctly to the other document. Fixed.

I also re-diffed the long Donatism A5 quotation in §2 A5 against the branch file: **exact**, with three ellipses eliding only the Caecilian/Optatus apposition, the "(a persecuted 'Church of the Martyrs'...)" parenthetical plus "not merely cite Optatus and Augustine as neutral sources", and "(Homoian Christianity as World #6's internal opponent)". None changes the meaning.

### N7 (Low) — CO-022 category 4 misquoted — **FIX VERIFIED GENUINE**

"Discovered" is gone. §6 now quotes *"a contradiction between two already-cleared master documents, or a finding that cuts against an earlier decision"* — **exact** against SKILL.md line 59 — and correctly identifies the finding as fitting the "cuts against an earlier decision" limb rather than the master-documents limb. One residual numbering ambiguity at NEW-7.

### N8 (Low) — the duplicated Council of Carthage rows — **FIX VERIFIED GENUINE**

§4 item 2(b) now names both rows and the divergence. Verified directly in `cic/corpus-map/latin-pastoral-congregational-christianity.yaml`:

- line 604 — *The Acts of the Council of Carthage under Cyprian (256, on baptism)*, `author: council-of-carthage-under-cyprian`, `source_file: npnf214_seven-ecumenical-councils.xml`, `confidence: provisional`, with the shared-ancestry Donatism note.
- line 736 — *The Seventh Council of Carthage under Cyprian (on the baptism of heretics)*, `author: cyprian`, `source_file: anf05_hippolytus-cyprian-caius-novatian.xml`, `confidence: assigned`, **no** Donatism note.

Same event, same 87 bishops, same September 256 sententiae. The document's parenthetical attributions (`npnf214`/`council-of-carthage-under-cyprian` versus `anf05`/`cyprian`) are correct, and its claim that §3 B1 cites the anf05 edition is correct — B1's Cyprian bullet closes "All vendored (`cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`)".

### N9 (Low) — "quoted here in full" — **FIX VERIFIED GENUINE**

Now reads *"(with the previously elided clause restored; an earlier draft of this document elided exactly the words that fix A5's subject as the floor, which overstated what A5 does)."* The A5 strand clause itself remains quoted with the disqualifying "— including whichever strand(s) meet the floor —" intact, and matches `step0_methodology.txt` exactly.

### Round 2's remaining low/cosmetic items

- **L5 (ranking claim) — now fully applied.** "Two or three most consequential" appears nowhere in the document. Round 1's preferred fix (a clean cut) has been taken.
- **C2 (CF version status) — applied.** The header now reads "Construction Framework V7.4 DRAFT's Step 0 stub", matching IJC's.
- **C1 (nested quote marks) — still not applied, and I agree with Round 2 that it should not be pressed.** I note, in the document's favour, that the same house convention is what makes A1's five commitments read as non-identical to the Constitution extract at the byte level; treating C1 as acceptable and H5-r residue 1 as fixed is the consistent position, and it is the one I take.

---

## Part 2 — New findings in this revision (and in material both prior rounds passed)

### NEW-1 (Medium) — the N3 correction was not propagated to §2 A5, which still states the blanket rule the document elsewhere calls wrong

**Where.** §2, A5, final paragraph (line 70), versus §2 A5's own preceding paragraph (line 68), §3 B3's World #4 bullet (line 108), and §4 item 2 (line 135).

**What's wrong.** §2 A5 says, in adjacent paragraphs:

> (line 68) "…this world's own Doc_02 **must reconstruct the Donatist schism as this world's own internal rival** — Cyprian's baptismal-controversy inheritance as Donatism later claims it, and **Augustine's own extensive anti-Donatist activity as this world's own pastoral response to a rival communion** — from inside this world's own perspective…"

> (line 70) "…this world (#8) holds 'the ordinary pastor navigating persecution' and 'ordinary sacramental administration,' **never** 'the schism-crisis angle,' which belongs to World #4."

§3 B3 then states the opposite of line 70 explicitly, and names line 70's own paragraph as the thing it would conflict with:

> "…not a blanket rule excluding all schism-related material from this world — read as a blanket rule it would also exclude Augustine's own *On Baptism, Against the Donatists*, *Answer to the Letters of Petilian*, and *The Correction of the Donatists*… all necessary to the Article 23 reconstruction obligation just established above (§2 A5)."

So the document now contains, in one section, both the reading it adopts and the reading it rejects — and the rejected one is stated in the *stronger* form ("never"), unhedged, in the paragraph a reader will treat as the boundary's authoritative statement. §4 item 2's opening sentence was scoped in this revision ("this is a characterization of Cyprian's own primary gravity, not a blanket exclusion"); §2 A5's was not. This is N3(b) surviving at its source, and CO-022's naming-and-term-propagation rule is directly on point: *"Whenever a name or term changes, check every file it appears in… A fix that lands in the narrative document without the index being updated to match is not a complete fix."* Within a single document, the same standard applies across sections.

**Why it matters.** Doc_02's Optatus decision, and the whole Article 23 reconstruction, run off exactly this line. A reader who takes §2 A5 at its word cannot carry out §4 item 2(d).

**Fix.** Rewrite line 70's first sentence to scope the parenthetical to Cyprian, as §3 B3 already does, and drop "never" as a world-level rule. Combine with NEW-4's fix, since both live in the same sentence.

### NEW-2 (Low) — the CO-022 rule added to fix N5 is itself misquoted, in the same section where N7 was found

**Where.** §6, closing paragraph.

The document writes: Per `cic-build-cycle`: *"If any [escalation category] applies, stop here and escalate directly to the project lead — do not self-dispose."*

The SKILL's actual text (line 54) is: *"Before disposing of any document, check it against these four categories. **If any apply, stop and escalate** directly to the project lead — do not self-dispose, **regardless of how clean the review came back**."*

Three unmarked alterations inside quotation marks: **"here" is inserted**; "apply" is silently conjugated to "applies" (the bracket covers the noun, not the verb); and the sentence is closed with a period where the source has a comma plus a further clause, with no ellipsis. Nothing substantive changes — the dropped clause is in fact paraphrased faithfully *outside* the quotation as "whatever any review round returns" — but this is the same defect class as N7, one paragraph later, in the fix written to answer N5, and it is the one quotation on which the document's own disposition rests. **Fix:** quote it as written, or mark the insertion and the truncation.

### NEW-3 (Medium) — §6's next clause sets a lower bar for starting Doc_01 than CO-022 does

**Where.** §6, closing paragraph, immediately after the (correct) bolded no-self-disposition sentence.

> "This document goes to the project lead for the IJC finding above; the eligibility and tier conclusions themselves (World #8 clears Section A; Tier 1) **may still inform Doc_01 once escalation is acknowledged**, since they do not depend on the escalated finding's resolution, but the document as a whole is not self-assigned Approved to proceed by this build thread."

CO-022 is more restrictive in two places. Stage 4: *"If one applies, escalate directly to the project lead **and wait**."* Stage 5: *"A document has reached at least 'Approved to proceed.' **Only now** does the next document in sequence begin,"* reinforced by *"Don't skip ahead. If a document earlier in the sequence hasn't reached at least 'Approved to proceed' yet, don't start drafting, outlining, or even thinking through a later one."*

Acknowledgement of an escalation is not a disposition. As written, the clause authorises Doc_01 work on a condition CO-022 does not recognise, in the same paragraph that correctly says this thread cannot self-assign Approved to proceed. It is a narrow point, but it is a scope-boundary statement in the disposition section — the exact slot N5 was raised about — and it partially undoes N5's fix.

**Fix.** Replace "once escalation is acknowledged" with the CO-022 condition: the conclusions do not depend on the escalated finding's resolution, but Doc_01 does not begin until this document has reached at least "Approved to proceed" by the project lead's own disposition.

### NEW-4 (Medium) — a phrase presented as a Step 0 Conclusion quotation is not in the Step 0 Conclusion

**Where.** §2, A5, final paragraph (line 70), same sentence as NEW-1.

> "**The Step 0 Conclusion's own boundary** is the load-bearing line for this same relationship in the other direction: this world (#8) holds **"the ordinary pastor navigating persecution"** and "ordinary sacramental administration," never "the schism-crisis angle," which belongs to World #4."

Two of the three quoted fragments are verbatim from Conclusion line 20 — *"ordinary sacramental administration"* and *"the schism-crisis angle"*. The third is not. The Conclusion reads *"Cyprian as working pastor navigating the Decian persecution and its aftermath."* I searched `step0_conclusion.txt`, all four extracted governing documents, and the whole repository: **"ordinary pastor" occurs nowhere except inside this document and one unrelated archived Doc_02.** The string was constructed, placed in quotation marks, and attributed to a named source in the same clause.

It is not a harmless paraphrase, either: "ordinary" narrows the world's remit further than the Conclusion does, and "persecution" drops "the Decian" and "and its aftermath" — the very words that make the phrase a *characterization of Cyprian's phase* rather than a rule about the world. It therefore reinforces NEW-1's blanket reading. The project's own Provenance-accuracy discipline is the applicable rule.

**This is pre-existing, not introduced by this revision** — it is identical in the first revision, so Round 1 and Round 2 both passed it. Logged as a disagreement with Round 2 below rather than as a defect of the current edit.

**Fix.** Quote the Conclusion accurately, attributing each half to the figure it characterizes; e.g. Cyprian as *"working pastor navigating the Decian persecution and its aftermath (not the schism-crisis angle, which belongs to world #4)"* and Augustine's side as *"preaching, catechesis, and ordinary sacramental administration for his own congregation at Hippo."*

### NEW-5 (Low) — §6's disagreements log records two of Round 2's three logged disagreements with Round 1

Round 2's "Disagreements with Round 1, logged per protocol" section holds three items: (1) the Cyprian certification, (2) the missed Antiochene flag, (3) *"Round 1's L4 was half right"* — IJC's cleared §6 retains the "without adding a new test, waiving a stated requirement" formulation, so reproducing that half was never the defect. §6's disagreements paragraph carries (1) and (2) and omits (3). CO-022's instruction is unconditional: *"If two reviews on the same document disagree with each other, log that disagreement explicitly rather than quietly siding with whichever review happened most recently."* Item (3) does not change any disposition, but it is a logged inter-round disagreement and belongs in the log. **Fix:** one clause.

*(Independently checked: Round 2 is right about IJC's cleared §6. IJC line 143 does retain "without adding a new test, waiving a stated requirement, or contradicting any cleared text." The current LPC §6 reproduces the same formulation and, per Round 2, is entitled to.)*

### NEW-6 (Low) — "all fifteen IJC records citing the Confessions source" over-counts, inheriting a loose figure from Round 2

§6 credits Round 2 with *"checking the locus of all fifteen IJC records citing the Confessions source."* My own count: fifteen **files** under `records/ijc/` contain the string `augustine-confessions`, but one of them is `ijc.source.augustine-confessions.md` itself (matching its own id) and two are search records. Fourteen records cite the source; twelve are neither the source record nor a search record. Round 2's own H1 text is internally inconsistent here too — it says "the other eleven" and then enumerates ten. Nothing substantive turns on it: I re-verified the underlying finding independently and it is exactly as the document states.

### NEW-7 (Low) — "the category's second limb" points at the wrong limb of the category as CO-022 actually writes it

§6 says the finding *"fits the category's second limb most precisely."* CO-022's category 4 has three limbs: *"two reviews disagreeing with each other, a contradiction between two already-cleared master documents, or a finding that cuts against an earlier decision."* The document quotes only limbs 2 and 3, without a leading ellipsis, and then numbers within its own truncated quotation — so "second limb" reads, against the source, as the master-documents limb the same sentence is explicitly rejecting. **Fix:** quote all three limbs, or say "the last of the three limbs."

### NEW-8 (Cosmetic) — §6 reverses the source order of the IJC boundary note inside an ellipsis

§6 renders it *"do not extend this license... [the rest] belong[s] to the Latin Pastoral-Congregational world."* The source record reads the other way round: *"Augustine's formation, theology, and the rest of the Confessions belong to the Latin Pastoral-Congregational world (World #8, not yet built); do not extend this license."* The bracketed editorial marks are proper, but an ellipsis signals elision, not reordering. §3 B3 quotes the same note in the correct order, so this is inconsistency within the document as well. Trivial; noted only because the surrounding sentence is the escalation.

### NEW-9 (Cosmetic) — "the only **prior** per-world Step 0 confirmations, IJC's and the parallel Donatism draft"

§3 B1 groups the same-day Donatism draft under "prior" while labelling it "parallel" in the same clause, and §0 dates it to this same day. Self-labelled, so not a contradiction; "existing" would be cleaner.

---

## Part 3 — Checked and found clean

**Verbatim quotation accuracy — every quotation re-derived from source, not accepted from Round 2.** I re-checked, programmatically and with quote/apostrophe/YAML-escape normalization: §1's Step 0 Conclusion block quotation (**exact**); the Tertullian dropped-voice disclosure (**exact**, modulo the extract's italic-marker asterisk); Section A's framing paragraph (**exact**); Article 4's prohibition sentence (**exact**); the Article 3 "Constitutional ambiguity flagged, not resolved" passage (**exact**, same asterisk artifact); A5's strand clause with the restored disqualifying clause (**exact**); the Procedure's screening instruction (**exact**); both Methodology "phase-level / never a per-world process" fragments (**exact**); the Criterion 2 sentence (**exact**); CF's "Strand is a finding" and "This determination is made at Step 1" (**exact**); A5's Article 23 rivals clause (**exact**); the Primary-gravity-first hedge (**exact**); IJC's §4 item 3 and §5 Finding 3 (**exact**); hal Doc_01 §8.1's three fragments (**exact**); the IJC source record's `work:` field and BOUNDARY note (**exact**); the Donatism A5 passage and its two B1 fragments (**exact**); the README's "THE primary source for Donatism" (**exact**); and every corpus-map note fragment the document quotes — the two IJC Augustine rows, the Jerome-correspondence double-placement note and its "largest single thing in this volume after the Confessions", the hal mirror row's "the other side of this entry's central argument", the embedded-letters note, the pseudo-Cyprianic "questionable authority" body, all three Tertullian-dependence notes, the shared-ancestry/novatianism/not-assigned rulings, and the Optatus note (**all exact**).

**The one exception is NEW-4**, which is not a misquotation of a source so much as a quotation with no source.

**Corpus and disk facts — re-verified, not inherited.** `npnf101`–`npnf108` are the Augustine volumes and `npnf109` is Chrysostom, on disk. `anf05_hippolytus-cyprian-caius-novatian.xml`, `npnf104_...`, `npnf214_...` and `optatus_against-the-donatists.txt` all exist. ~97 sermons, ~695,000-word *Enarrationes* as "the largest single body in the vendored corpus", the 17-letter/~52,892-word Jerome sub-corpus, 82 Cyprianic epistles, the September 256 sententiae of 87 bishops — all match their corpus-map rows. *On the Creed: A Sermon to Catechumens* is a real assigned row (line 324), so A1's supporting claim holds.

**Methodology conformity — re-checked against the Methodology's own text.** B1–B5's test statements track the Methodology's own "What this means for seed screening" lines. B4's six audiences are exactly the Essential Experience list the Methodology cites (*"curious seekers, thoughtful believers, pastors and teachers, historically interested learners, deconstructing Christians, academically minded users"*). B2's "eight lenses" is the Methodology's own phrase. The Tier 1 rubric quoted in §3's tier conclusion matches Procedure step 4 word for word. Section A's five subtests are correctly characterised, and the "Article 3 is outside Step 0's instrument" argument (Round 1's H4 replacement) still holds on re-inspection — nothing in Section A or Section B's five criteria tests historical coherence.

**Cross-reference integrity after the §4 renumbering.** Adding the Antiochene item as §4 item 7 pushed Primary-gravity-first to item 8. Every internal pointer still resolves: §1 → item 6 (Tertullian ✓), §2 A5 → item 2 (Donatism ✓), §3 B3 → items 2 and 5 (✓), §4 item 4 → item 2 (✓), §5 item 4 → §3 B3 and §6 (✓), §6 → §5 item 4 (✓). No stale reference found.

**CO-022 named failure modes, re-run against the current text.**
- **(a) Attribution to "the project lead"/"Mark" without a verbatim sourced quote — CLEAN.** The single "Mark" occurrence remains the verbatim Optatus corpus-map note, correctly marked.
- **(b) Content described as checked that wasn't — CLEAN.** N1 was the last instance and is fixed. I independently re-ran every check the document claims: the IJC record-set check (including all fifteen matching files' loci), the corpus-map checks on all three files, the hal Doc_01 check, the Donatism branch check via `git show`, and the IJC Doc_01/Doc_02 Cyprian search. All return what the document says they return.
- **(c) Fabricated citation or fact — CLEAN as to citations; one unsourced quoted phrase at NEW-4.** Every path, identifier, branch, figure and file resolves. NEW-4 is a constructed phrase in quotation marks, not a fabricated source.
- **(d) Build output outside the canonical folder — CLEAN.**

**Internal consistency, read whole rather than section by section.** §0's account of the Donatism parallel matches §2 A5, §3 B1, §3 B3, §4 item 2 and §5 items 1–2. §2's century-gap resolution matches §4 item 1 and §6's escalation assessment. §3 B1's qualifications match B2's and B4's characterizations. §4 item 3's Article 20 routing matches §2 A5 and CF's Step 2 list. §5 item 5's IJC claims match IJC's file. §6's escalation matches §3 B3 in scope and wording. **The only internal contradiction found in the whole document is NEW-1.**

**§6's revision history, re-checked against the actual Round 1 and Round 2 files rather than against its own summary.** The Round 1 paragraph's tally (five high, ten medium) and its characterization of each finding match Round 1's text; its enumeration of what was addressed is now accurate, including the item Round 2 called "half right" — A1 no longer restates the floor and does cover all five. The Round 2 paragraph accurately describes Round 2's verdict (14 of 15 genuine, H5 partial), its five new mediums and four new lows, and where each was addressed, and it correctly credits Round 2 with going beyond Round 1 on the IJC record sweep (subject to NEW-6's count). The disagreements paragraph accurately states Round 2's first two disagreements (both of which I re-verified independently and both of which Round 2 was right about) and correctly attributes them to Round 1 rather than to this document's drafting; it omits the third (NEW-5).

**Conclusions that survive review.** World #8 clears Section A, on the reasoning as now built. Tier 1 is correct against the Methodology's own rubric. B1's qualifications, B2's three-phase Cyprian account, B4's corrected attributions and B5 are all sound. §4 items 1, 3, 4, 5, 6, 7 and 8 are well-grounded and accurately sourced. The H1 escalation remains the document's strongest work and should survive this revision untouched.

---

## Part 4 — The disposition and escalation statement, assessed directly

**Is the escalated finding real?** Yes, independently re-verified. `records/ijc/source/ijc.source.augustine-confessions.md` narrows itself to *"Confessions, Book 9 ch. 7 ONLY"* and its binding BOUNDARY note reads *"Augustine's formation, theology, and the rest of the Confessions belong to the Latin Pastoral-Congregational world (World #8, not yet built); do not extend this license."* `ijc.quote.take-up-and-read` cites Confessions VIII.12 and `ijc.quote.i-scorned-to-be-a-little-one` cites Confessions III.5; both carry `evidentiary_weight: load-bearing` and `retrieval.tier: 1`. I checked the locus field of every record citing that source: no other record leaves IX.7, so the document's scoping is neither understated nor inflated. *(One incidental observation, outside this document's scope and not a finding against it: `ijc.limit.reading-alone` discusses Confessions III.5 in its prose while citing IX.7 as its locus. It corroborates rather than complicates the finding.)*

**Does it fit a CO-022 escalation category?** Yes. Category 4's third limb — *"a finding that cuts against an earlier decision"* — fits precisely: IJC's source record records a deliberate, disclosed Boundary Check decision, and its own later quote records cut against it. The document reaches this conclusion for the right reason and correctly declines the master-documents limb.

**Is the consequence correctly stated?** In its main clause, yes — and this is the material improvement over the prior revision. *"Because a standing escalation category applies, this document does not self-dispose, whatever any review round returns"* is exactly what CO-022 requires, and the accompanying "not self-assigned Approved to proceed by this build thread" is correct. The two defects are the misquotation of the rule (NEW-2) and the "once escalation is acknowledged" clause (NEW-3), which is a genuinely lower bar than CO-022's.

**One observation, not a required action.** Category 4's *first* limb is "two reviews disagreeing with each other." Round 2 logged three disagreements with Round 1, and §6 now records two of them. Whether that limb is "unresolved" is arguable — Round 2 closed each disagreement by going to source, and this revision adopted the corrections — so I do not press it as a finding. But §6's "**One** finding does escalate" is a stronger claim than the document needs to make, and one sentence acknowledging that the review-disagreement limb was considered and found closed on the merits would be tidier than leaving it unmentioned. The disposition outcome is unchanged either way.

**Consistency with the status line.** The header correctly reports Round 2's result and claims no disposition. §6 closes "**Pending:** independent adversarial review (Round 3)", which is accurate as of the version reviewed. No disposition is self-assigned anywhere; "Frozen" is not claimed. Disposition discipline is otherwise clean.

---

## Summary of required actions

| # | Severity | Action |
|---|---|---|
| N3-r / NEW-1 | Medium | §2 A5 (line 70): scope the "not the schism-crisis angle" parenthetical to Cyprian, as §3 B3 and §4 item 2 now do, and drop "never" as a world-level rule — otherwise §2 A5 contradicts its own preceding paragraph and §3 B3 |
| NEW-4 | Medium | §2 A5 (same sentence): "the ordinary pastor navigating persecution" is not in the Step 0 Conclusion. Quote the entry accurately, attributing each half to the figure it characterizes |
| NEW-3 | Medium | §6: replace "may still inform Doc_01 once escalation is acknowledged" with CO-022's actual bar — Doc_01 does not begin until this document reaches at least "Approved to proceed" |
| NEW-2 | Low | §6: quote CO-022's disposition rule as written ("If any apply, stop and escalate… regardless of how clean the review came back") or mark the insertion and truncation |
| NEW-5 | Low | §6: log Round 2's third disagreement with Round 1 (the L4/IJC-cleared-text point) alongside the two already recorded |
| NEW-6 | Low | §6: "fifteen IJC records citing the Confessions source" — fourteen records cite it; the fifteenth match is the source record itself |
| NEW-7 | Low | §6: "the category's second limb" — quote all three limbs, or say "the last of the three" |
| NEW-8, NEW-9 | Cosmetic | §6's reversed clause order inside an ellipsis; §3 B1's "prior" for a same-day parallel draft |

Per `cic-build-cycle`, NEW-1, NEW-3 and NEW-4 each change a claim's substance, a sourcing conclusion, or a scope boundary, so the revision required is **substantial** and the revised document requires a fresh review round rather than direct application. NEW-2 and NEW-5 through NEW-9 are cosmetic-to-low and could be applied in the same pass without independently triggering a round. The work is three sentences of substance plus five small corrections; none of it touches the document's conclusions, and none of it revisits ground Round 1 or Round 2 closed.

## Disagreements with prior rounds, logged per protocol

1. **With Round 2 (and with Round 1): "every quotation in the document traced to source" is not sustainable.** Round 2's Part 3 states that every quotation was traced and that §2's quotations are exact; Round 1's "Checked and found clean" makes the same claim for §2. The phrase *"the ordinary pastor navigating persecution"* in §2 A5 is presented as a Step 0 Conclusion quotation and appears nowhere in the Conclusion or anywhere else in this repository. It has been in the document since the first revision. See NEW-4. Recorded as a gap in both prior rounds, not as a defect this revision introduced.
2. **With Round 2, minor: the "fifteen records" count in its H1 verification.** Fifteen files match; one is the source record itself and two are search records, and Round 2's own enumeration lists ten items while calling them eleven. The finding Round 2 built on that sweep is nonetheless correct and I confirmed it independently. See NEW-6.
3. **With Round 2, minor: N3 was reported as fixable in three places and was fixed in two.** Round 2's fix instruction said "scope the portfolio-entry parenthetical to Cyprian" without naming §2 A5 as a second site; the revision scoped the site Round 2 pointed at. The residue at NEW-1 is therefore as much an incompleteness in Round 2's instruction as in the revision, and is recorded that way rather than charged solely to the drafter.
4. **Agreeing with Round 2 against Round 1, on independent re-check:** Round 2 was right that Round 1 wrongly certified "Cyprian appears nowhere in IJC's Doc_01 or Doc_02" (he is named once, in Doc_01 §6), and right that Round 1 missed the Step 0 Conclusion's standing Antiochene primary-gravity flag against World #8. Both re-verified here from source, not from Round 2's account.
5. **Agreeing with Round 2 on C1, and extending it:** the nested straight-quote convention is typographic, not a misquotation. That position is what makes H5-r residue 1 dischargeable, since A1's five commitments differ from the Constitution extract only in that convention. Treating C1 as acceptable and residue 1 as fixed is the consistent reading, and it is the one taken here.
