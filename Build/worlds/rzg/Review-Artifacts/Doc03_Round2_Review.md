# Doc_03 (Lexicon Candidate List) — Round 2 Independent Adversarial Re-Review

**World:** The Reformed Cities — Zurich & Geneva (`rzg`)
**Document under review:** `Doc_03_Lexicon_Candidate_List.md`, DRAFT, Revision 2
**Reviewed against:** `Doc_01_World_Identification_Boundaries_Orientation.md` (Approved to proceed, Rev. 5), `Doc_02_Source_Ecology.md` (Approved to proceed, Rev. 3), `Source_Registry.md`, and the vendored primary texts in `cic/texts/` (`calvin_institutes-christian-religion-vol3_beveridge1845.txt`, `calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt`), per `Review-Artifacts/Doc03_Round1_Review.md`'s own Findings 1–9.
**Scope:** targeted recheck per this project's Round 2+ discipline — not a full re-review from scratch. Each of Round 1's Findings 1–9 was independently re-verified against the same primary sources Round 1 used (not taken on Doc_03's own revision-note claim), plus a check for fix-introduced new errors, focused on the row 14 citations, the CT quotation, and the Consistory/Elder language.

**Reviewer's own note on where this review was run:** run in an isolated worktree not checked out on `reformed-cities-doc01` (that branch is checked out elsewhere). Doc_01/02/03, the Source Registry, and the vendored primary texts were all read via `git show reformed-cities-doc01:<path>` — git objects are shared across worktrees even though the branch itself is checked out elsewhere, the same method Round 1's own reviewer used. This file was written into this review's own worktree filesystem, not `reformed-cities-doc01` directly, and was copied onto that branch by the main build thread, exactly as Round 1's own artifact was.

---

## Verdict: Clear with cosmetic notes

All nine substantive Round 1 findings (1–9) are genuinely fixed — independently re-verified against the actual vendored texts and upstream documents, not accepted on Doc_03's own say-so. No fabrication, no misattributed cross-reference, and no wrong Registry row number survives anywhere in Revision 2. One new, narrow defect was introduced by the Finding 4 fix: a specific Institutes locus citation ("IV.3.9") is off by one section — the quoted text is actually in IV.3.8. The quotation itself is verbatim-accurate and the substance (general lay-elder doctrine, Confidence A, Book IV) is correct; only the pinpoint section number is wrong. This is a citation-precision defect, not a fabrication or an overclaim, and does not require another full round — noted as a cosmetic correction below.

---

## Findings 1–9: verification against Revision 2

### 1. [CRITICAL — fabricated Doc_01 §5 Beza/Genevan Academy quotation] — **Genuinely fixed**

**Checked:** full-text search of Doc_03 Revision 2 for "Beza" and "Genevan Academy." Read §4 (the CT candidate's contest description) in full.

**Found:** the fabricated sentence is gone entirely. §4 now reads: *"Sign and the Thing Signified — Contest Type: Meaning... Contest: whether the Consensus Tigurinus represents a genuine theological synthesis or a diplomatically ambiguous formula... Confidence: Widely Accepted that a live scholarly debate of this shape exists in Reformation historiography generally; the debate's own resolution is itself Contested."* No quotation is attributed to Doc_01 §5, no claim about Beza's Eucharistic positions appears anywhere in the document, and the one remaining "Beza" reference in the document (§0, listing Registry rows 13–17's unacquired contents) is a plain, accurate mention of Beza's own unvendored works (Registry row 16) — unrelated to the fabricated claim. Re-checked Doc_01 §5 and §7 directly: neither contains the phrase "developed at the Genevan Academy" or any claim about Beza's Eucharistic positions, confirming there was never real Doc_01 support to salvage — full removal was the correct fix, and that is what happened.

### 2. [CRITICAL — fabricated Doc_02 §8 "Contested" finding on the Supper/memorial question, repeated twice] — **Genuinely fixed**

**Checked:** §1 Cluster 3 (Memorial/Commemoration row) and §6 (Open Items) in Revision 2; re-read Doc_02 §8 (Confidence Map) in full.

**Found:** both instances now explicitly disclaim any Doc_02 attribution. §1: *"Whether the Consensus's own mature statement fully preserves or substantially softens Zwingli's original emphasis is not resolved by any document in this world's build so far (Doc_02 does not address this question; this is this document's own open judgment call, not an inherited finding) — carried forward as PV rather than settled here."* §6: *"...is not addressed anywhere in Doc_02 — this is this document's own open judgment call (corrected at Doc_03 Round 1 review, which found no such finding in Doc_02 §8), not an inherited finding from an earlier document."* Doc_02 §8 was re-read directly and still contains only its original three Contested items (Heidelberg joint-authorship, Heidelberg predestination development, Bullinger's corpus-thinness) — no Supper/memorial finding exists there, confirming Doc_03 no longer claims one does. The claim is now correctly owned as Doc_03's own judgment, not laundered through a fabricated upstream citation.

### 3. [HIGH — Registry row 13 cited three times, plus a stray "row 16," for content that is row 14] — **Genuinely fixed**

**Checked:** every Registry row-number citation in Revision 2 (§0, §1 Consistory row, §1 Elder row, §2, Cluster 4 header, §6), against `Source_Registry.md`'s actual rows (independently re-read: row 13 = Consistory registers, Confidence D; row 14 = Ecclesiastical Ordinances, Confidence E).

**Found:** every citation to the Ecclesiastical Ordinances now correctly reads "row 14," and every one correctly pairs it with Confidence E, matching the Registry exactly:
- §0: "...rests on the still-unacquired Ecclesiastical Ordinances (**row 14**)."
- §1, Consistory: "...rests on Registry row 14, not itself vendored (**Confidence E**)." — matches Registry row 14 exactly (Type P, Confidence E).
- §1, Elder: "...is not yet vendored (**row 14**)."
- §2: "...the Ecclesiastical Ordinances themselves remain unacquired (**Registry row 14**)."
- §6: "...Source Registry **row 14**/Manifest G1" — and Registry row 14's own Verification Note does in fact name Manifest item G1, confirming the pairing is now internally consistent as well as correct.
- Cluster 4 header: now reads "Registry rows 1–3, 9, and **row 14** not yet acquired" — the stray "16" is gone; no remaining reference to Beza's row (16) appears in the Cluster 4 header or anywhere else it doesn't belong.

A full-text search of Revision 2 for "row 13" returns zero matches. This finding is fully and consistently corrected.

### 4. [HIGH — Consistory/Elder characterized as having zero vendored grounding] — **Genuinely fixed, with one new narrow citation error (see "Newly introduced errors" below)**

**Checked:** the Consistory and Elder rows (§1), §0, §2, and §6, against `calvin_institutes-christian-religion-vol3_beveridge1845.txt` directly.

**Found:** Doc_03 now draws exactly the distinction Round 1 asked for — general Reformed doctrine (vendored, Confidence A) versus Geneva's specific 1541 institutional practice (unvendored, Confidence E) — consistently across §0, §1, §2, and §6. Both quotations were independently re-verified verbatim against the vendored file:
- *"the consistory of elders, which was in the Church what a council is in a city"* — confirmed verbatim at line 10503–10504 of the vendored file.
- *"seniors selected from the people to unite with the bishops in pronouncing censures and exercising discipline"* — confirmed verbatim at line 2830–2832.
- The claimed count ("9 occurrences" of "consistory") was independently re-counted: `grep -c` confirms exactly 9 occurrences in the vendored file.

Critically, the fix does **not** overclaim in the other direction: §1's Consistory row and Elder row, §2, and §6 all explicitly and repeatedly state that Geneva's own specific 1541 institutional practice (composition, weekly sessions, case history) is "not itself vendored," "not yet vendored," or "unverified against a primary source," each time correctly citing Registry row 14/Confidence E for that specific claim. The general-doctrine/specific-practice line is held cleanly throughout; nowhere does the revised text imply the Ecclesiastical Ordinances themselves, or Geneva's actual institutional history, are text-grounded.

### 5. [MEDIUM — CT Contest Type never labeled] — **Genuinely fixed**

**Checked:** §4.

**Found:** §4 now opens with *"Contest Type: Meaning (per the Deployment Lexicon Chunk Template's four recognized types)."* This is the correct classification (a live disagreement about what the Consensus Tigurinus's formula actually meant and accomplished, not a scope, application, or present-day-relationship question), matching Round 1's own independent classification.

### 6. [MEDIUM — CT contest's "scholarly opinion is divided" premise carried no confidence tag] — **Genuinely fixed**

**Checked:** §4's Confidence sentence.

**Found:** now reads *"Confidence: Widely Accepted that a live scholarly debate of this shape exists in Reformation historiography generally; the debate's own resolution is itself Contested. No secondary scholarship on the Consensus Tigurinus is vendored for this world (Doc_02 §3), so this characterization rests on the builder's own general knowledge of the historiography, not a specific cited source — flagged accordingly rather than presented as text-grounded."* This correctly uses two of the project's five Article 17 confidence levels (Widely Accepted, Contested) and honestly discloses the absence of vendored secondary scholarship, exactly as Round 1 asked.

### 7. [MEDIUM — Excommunication's Geneva Strand assignment rested on an unstated argument] — **Genuinely fixed**

**Checked:** the Excommunication row (§1, Cluster 4), against Doc_01 §5's three named strand dimensions (Practice, Authority structure, Formation emphasis).

**Found:** the row now states the reasoning explicitly: *"The underlying doctrine is discussed in Calvin's Institutes (Book IV) in general, universal-church terms (SC); the Geneva strand tag reflects the specific historical application this document highlights — the authority Calvin fought to keep independent of the civil council during the Perrinist crisis (Doc_01 §5) — not a claim that the doctrine itself is Zurich-absent."* This maps cleanly onto Doc_01 §5's Authority-structure dimension (which names exactly this fight to keep Consistory discipline independent of civil-council control), closing the previously-implicit reasoning gap.

### 8. [LOW — Confession (of Faith) Strand=Shared illustrated only by Zurich content] — **Genuinely fixed**

**Checked:** the Confession (of Faith) row (§5, Cluster 5).

**Found:** now explicitly discloses: *"No Geneva-side confessional document (e.g. a Geneva Confession) is vendored for this world; 'Shared' is a genre-level claim about the wider Reformed tradition, not yet demonstrated from this world's own two strands directly."* The Flags column carries a matching note: *"Geneva-side confessional analog not vendored — flag for Doc_06."* This is the disclosure Round 1 asked for, in the same style used elsewhere in the document (e.g. the Genevan Psalter).

### 9. [LOW — imprecise CT ninth-Head-of-Agreement quotation, appended unquoted "them"] — **Genuinely fixed**

**Checked:** the Sign and the Thing Signified row (§1, Cluster 3), against the vendored Consensus Tigurinus text directly.

**Found:** Doc_03 now quotes: *"though we distinguish, as we ought, between the signs and the things signified, yet we do not disjoin the reality from the signs"* — confirmed verbatim against the vendored file (`...Wherefore, though we distinguish, as we ought, between the signs and the things signified, yet we do not disjoin the reality from the signs, but acknowledge...`, lines 768–770). The quotation now closes at "the signs," inside the quotation marks, with no appended unquoted word changing the grammatical object. The defect is fully corrected.

---

## Newly introduced errors

**[LOW] Elder row cites "Institutes IV.3.9" for a quotation that is actually in IV.3.8.** The Elder row (§1, Cluster 4) states: *"Calvin's own vendored, Confidence-A text (Institutes IV.3.9) states the general doctrine almost verbatim to this definition — 'seniors selected from the people to unite with the bishops in pronouncing censures and exercising discipline.'"* Independently re-checked against the vendored file's own paragraph numbering: the quoted sentence falls within paragraph **8** ("8. In giving the name of bishops, presbyters, and pastors... By these governors I understand seniors selected from the people to unite with the bishops in pronouncing censures and exercising discipline...") — paragraph 9, which immediately follows, begins "The care of the poor was committed to deacons..." and is a different topic entirely. Book and chapter (IV.3) are correct; the section number is off by one. The quotation itself is verbatim-accurate and the substantive claim (general lay-elder doctrine, Confidence A, Book IV) is sound — this is a locus-pinpoint error, not a fabrication or a second instance of the overclaiming failure mode this world's build has previously been caught on. Given this project's own discipline that every citation be independently re-verified rather than trusted, this should be corrected to IV.3.8 before this document is treated as fully closed, though it does not by itself require another full review round — a targeted one-line fix, verified, is sufficient. (Note: Round 1 review's own prose independently described this same passage as "Book IV ch. 3 §9" without Doc_03 itself citing a section number at the time — Revision 2 is the first place this specific pinpoint citation appears, and it inherited the same off-by-one error rather than independently re-deriving it.)

No other new errors were found. The row-14 citations (Finding 3) were independently re-verified against the actual Registry rows and are all correct, including the Confidence-letter pairings. The CT quotation (Finding 9) is verbatim-accurate through its full new closing point. The Consistory/Elder language (Finding 4) does not overclaim Geneva-specific institutional grounding in either direction — the general-doctrine/specific-practice distinction is held consistently everywhere it appears.

---

## Summary

All nine Round 1 findings — including both CRITICAL fabricated cross-references and the repeated wrong Registry row number — are genuinely and consistently fixed in Revision 2, independently re-verified against Doc_01, Doc_02, the Source Registry, and the vendored primary texts rather than accepted on the document's own revision note. One new, narrow defect was introduced by the Finding 4 fix (an Institutes section citation off by one, IV.3.9 instead of IV.3.8) — a citation-precision issue, not a fabrication, and correctable as a one-line fix without a further full review round.

No escalation category applies. This is ordinary sourcing-fidelity correction work — verifying quotations, cross-references, and Registry row numbers against source — not a Representative identity/title/voice decision, a cross-world or portfolio-level decision, or a governance/methodology change.
