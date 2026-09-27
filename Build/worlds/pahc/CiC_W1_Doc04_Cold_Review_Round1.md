**Simulated review — informational only, not an Article 31 substitute.**

# Cold Review — Doc_04 Gravity Discovery, World #1 (Post-Apostolic/Sub-Apostolic House-Church Christianity)

**Reviewer stance:** This review treats every claim in Doc_04's own Document Log (FINALIZED language, "seven independent adversarial review rounds," specific claimed fixes) as unverified narration until independently checked. Findings below are the result of independent re-derivation, not a re-reading of the document's own self-report.

**File reviewed:** `CiC_W1_Doc04_Gravity_Discovery_FINAL.docx` (36,148 bytes; 174 total paragraphs, 161 non-empty, 3 tables)

**Companion workbook located:** `CiC_W1_Gravity_Index_FINAL.xlsx` (note: filename differs slightly from the `CiC_W1_Gravity_Index.xlsx` named in the task brief, but it is the only Gravity Index workbook in the World #1 folder, contains exactly the five sheets Doc_04's text describes -- Gravity Index, Interaction Matrix, By Classification, By Cross-Check Flag, Cross-Build Dependencies -- and is dated same-day as the FINAL docx. Treated as the intended companion.)

**Context documents used:** `CiC_W1_Doc01_World_Identification_FINAL.docx`, `CiC_W1_Doc02_Source_Ecology_FINAL_v2.docx` + `CiC_W1_Source_Registry_FINAL_v2.xlsx`, `CiC_W1_Doc03_Lexicon_Candidate_List_FINAL_v2.docx`, `CiC_L3B_Formation_World_Construction_Framework_V7.3.docx` (canonical, non-worktree copy) and `CiC_L3B_Formation_World_Construction_Framework_V7.4_DRAFT.docx` (worktree copy -- the version Doc_04 actually cites), `CiC_L3A_Forces_Framework_V1.1.docx`, and the `Build/reference/L4-Templates/` directory.

---

## Findings

### Finding 1 (SUBSTANTIAL) -- Main Gravity Index sheet contains a stale Interaction Matrix count that contradicts the document's own round-6/7 corrections

The main **Gravity Index** sheet's G07 row, "Confidence/Gravity Cross-Check Outcome" cell, reads in part: *"ALSO PER ROUND-4: Interaction Matrix row is now thin (1 of 5 relationships demonstrated, see Interaction Matrix sheet) -- classification unaffected but flagged for Doc_05/Doc_08 to watch."*

This is the pre-round-6 figure. Doc_04's own body text (Section 2, G07 entry, and Section 6 item 9) states explicitly that round 6 corrected G05<->G07 from "No demonstrated relationship" to "Reinforcing (inferential)," which changes G07's demonstrated-relationship count from 1-of-5 to **2-of-5** ("G07's row: G01 and G05, both inferential -- two of five, up from the one of five stated in rounds 4 and 5"). The Interaction Matrix sheet itself and Doc_04's Section 4 table both correctly reflect the 2-of-5 state. Only this one cell in the main Gravity Index sheet was never updated.

This directly contradicts the Document Log's explicit claim: *"Companion Gravity Index workbook finalized to match (Gravity Index, Interaction Matrix, By Classification, By Cross-Check Flag, Cross-Build Dependencies sheets all current as of round 6's fixes...)."* The Gravity Index sheet -- the primary sheet, not a derived one -- is not in fact current as of round 6. This is exactly the class of silent post-edit desync the task asked to check for, found in the main sheet itself rather than only a derived view.

### Finding 2 (SUBSTANTIAL) -- "By Classification" derived sheet is out of sync with the main sheet and Doc_04's own text on G03's cross-strand status

The **By Classification** sheet's G03 row, "Cross-Strand Status" column, reads: *"Cross-strand (episodes discrete, not uniform) -- Rome, Bithynia-Pontus, Antioch/Asia Minor"* -- i.e., three regions/strands.

The main **Gravity Index** sheet's G03 row states the corrected position: *"CORRECTED per round-3 review: cross-strand confirmed via Strand B (Rome -- Tacitus/Nero) and Strand A (Antioch/Asia Minor -- Ignatius's arrest). Bithynia-Pontus (Pliny) corroborates the broader pattern but is not itself a strand, per Article 21 -- prior 'reasonably cross-strand... 3 regions' framing overstated this."* Doc_04's own body text (Section 2, G03 entry) states the identical correction in almost the same words, explicitly disclaiming the three-region framing as an overstatement.

The By Classification sheet's row for G03 still carries exactly the retracted three-region framing the main sheet and the document body say was corrected in round 3. This is a genuine derived-sheet desync of the kind the task specifically flagged as having precedent in this project (Doc_02's Source Registry). It also falsifies the Document Log's "all current as of round 6's fixes" claim for a second sheet.

Both findings 1 and 2 are narrow (single-cell) but substantive: each directly contradicts a claim of confidence/correction the document makes elsewhere about itself, and both were introduced by exactly the failure mode the document's own Section 6 item 8 warns about -- a claimed "full" synchronization pass that did not actually touch every cell it should have.

### Finding 3 (COSMETIC) -- Doc_04 cites a non-canonical DRAFT framework version

Doc_04's governance line cites "Formation World Construction Framework **V7.4 (DRAFT)**." The canonical, non-worktree copy of the Construction Framework in the main project tree (`/CiC-Project/L3B-World-Build-Methodology/`) is **V7.3**; V7.4_DRAFT exists only inside `.worktrees/` branches and the separate Archive/Syriac-Build-2026-07 copy, not as an adopted top-level document. Direct comparison of the Step 4 (Gravity Discovery) sections of V7.3 and V7.4_DRAFT shows they are **word-for-word identical** -- so this citation choice has no substantive effect on Doc_04's content or governing rules. Flagged as cosmetic/process hygiene: a document that has "cleared review" should cite the adopted governing version, not a draft-branch copy, even when (as here) it happens not to matter.

### Finding 4 (VERIFIED, no issue) -- "No L4 template" claim holds up

Doc_04 states it "has no L4 template to build against, unlike its sibling steps." The project's `/CiC-Project/L4-Templates/` directory was inspected directly: it contains 12 templates (Deployment Lexicon Chunk, Story Repository Chunk, Voice Configuration, World Capsule Core, a Forces Document template for Doc_08, etc.) but **no template for Doc_04/Step 4/Gravity Discovery**. The claim is accurate, not self-serving narration.

### Finding 5 (VERIFIED, no issue) -- Interaction Matrix independently re-derived from scratch

An independent, code-assisted re-derivation was performed: every candidate's own Section 2 six-test text was extracted and searched for every other candidate's ID string, then each of the 15 unique pairs was checked against the actual sentence(s) grounding it (not against the document's own summary claims). Result: the 9 inferential / 5 no-demonstrated-relationship / 1 plain split, and the specific cell values in both Doc_04's Section 4 table and the workbook's Interaction Matrix sheet, are internally consistent with each other and with the underlying six-test prose as it currently stands. No further undiscovered cross-reference (of the kind rounds 4-6 each found) was located in this pass. This does not retroactively validate the process narrative in the Document Log (which remains unverified narration), only the current end-state of the matrix.

### Finding 6 (VERIFIED, no issue) -- Confidence/Gravity Cross-Check applied independently to both Primary candidates

G02 (Translocal Correspondence Network): rests on three independently-attested primary voices/events (1 Clement, Ignatius's full corpus, Polycarp ch. 13) spanning both strands, with Widely Accepted/Documented confidence on the base claim itself (letters existed and were exchanged this way). No Contested layer is doing the organizing work. Primary classification holds under independent re-check.

G07 (Liturgical Practice): rests on three independent voices (Didache, Ignatius, Justin) across both strands. The Documented content -- a shared ritual, independently attested in related but non-identical forms -- is what earns Dependency/Explanatory/Formation; the Contested layer (which specific form is "representative") is not what the organizing work depends on. This set-aside-the-Contested-layer distinction was checked directly against G07's own six-test bullets and holds. Primary classification holds under independent re-check.

Both G01 and G03's Supporting reclassifications were also independently re-checked against their own Persistence/Dependency caveats and hold: in both cases, the six-test results actually crediting Dependency/Explanatory/cross-strand Persistence are earned by a Contested synthesis (Strand A/B differentiation for G01; cross-episode "one standing condition" reading for G03), not by the Documented core alone.

### Finding 7 (VERIFIED, no issue) -- Cross-strand status (Article 21) checked for every candidate; no world-level Primary rests on single-strand evidence

Both Primary candidates (G02, G07) are confirmed cross-strand by multiple independent voices in each strand. The three Strand-bound candidates (G04, G05 -- Strand A only; G06 -- not meaningfully assessable) are all classified Supporting, Tensional, or below gravity status, never Primary. G01 and G03 are cross-strand at the level of "the force exists" but strand-bound or Contested at the level of specific content, and both are correctly Supporting, not Primary. No violation of the cross-strand/Primary-classification rule was found -- subject to the caveat in Finding 2 that G03's own workbook representation of its cross-strand status is itself inconsistently stated across sheets.

### Finding 8 (VERIFIED, no issue) -- Primary-source citations independently checked against open-web texts

Four primary-source citations were fetched and checked verbatim against Doc_04's transcriptions/paraphrases:
- **Ignatius, Romans 4** ("food for wild beasts" / "food for the wild beasts") -- confirmed, matches Roberts-Donaldson translation exactly.
- **Ignatius, Philadelphians 4** ("one eucharist") -- confirmed: "Take ye heed, then, to have but one Eucharist..." Also confirms Doc_03's claimed correction (from Smyrnaeans 8 to Philadelphians 4) is textually correct -- the "one eucharist" language is in Philadelphians 4, not Smyrnaeans 8.
- **Polycarp to the Philippians ch. 13** (forwarded Ignatius's letters at the Philippians' request) -- confirmed verbatim: "Ye wrote to me, both ye yourselves and Ignatius, asking that if any one should go to Syria he might carry thither the letters... The letters of Ignatius which were sent to us by him... we send unto you, according as ye gave charge."
- **Martyrdom of Polycarp ch. 18** (dies natalis / relics "more precious than jewels") -- confirmed in substance: "we afterwards took up his bones which are more valuable than precious stones and finer than refined gold... to celebrate the birth-day [dies natalis] of his martyrdom." Minor translation-variant wording only (different published translations render "precious stones"/"jewels" differently); not a misquote.

Pliny, *Letters* 10.96-97, Tacitus *Annals* 15.44, and Suetonius were **not** independently fetched -- three attempts to reach open-web copies of Pliny's letter timed out or returned empty content during this review. This is a genuine verification gap, disclosed rather than papered over. However, the Source Registry's citation codes (P07=Pliny 10.96-97, P08=Tacitus Annals 15.44, P09=Suetonius) were cross-checked against Doc_04's in-text citations and match exactly, and these are among the most extensively attested, uncontested texts in the field (no serious scholarly dispute about their content, only about interpretation, which Doc_04 already flags as Contested).

### Finding 9 (VERIFIED, no issue) -- Cross-document sourcing chain checked against Doc_01/Doc_02/Doc_03

Every specific section citation sampled from Doc_04 was checked against the actual target document and found accurate: Doc_01 Section 6 (Strand Determination, including the verbatim "third Asia Minor profile" open item and the 1 Clement chs. 42/44 citation), Doc_01 Section 7 (eyewitness-generation-loss force), Doc_01 Section 8.3 (Marcionite/Valentinian/Montanist contemporaneity), Doc_02 Section 1.3 (Ignatius representativeness caveat), Doc_02 Sections 3, 4, and 9 (Institutional Evidence, Liturgical Evidence, Forces Lens), Doc_03's Tier 1 terms 2.1-2.2 (episkopos/presbyteros) and Section 3 (monepiscopacy and oikos/"house church" exclusions). No fabricated or misattributed citation was found in this sample.

### Finding 10 (SUBSTANTIAL -- mandatory truncation check) -- Document confirmed NOT truncated, by two independent methods, in a fresh call

- **Method 1 (python-docx):** 174 total paragraphs, 161 non-empty, 3 tables. Last non-empty paragraph ends: "...Revision count: 6 (round 7 was cosmetic-only per the revision-decision test and does not increment the count). Doc_05 may now begin." -- a complete, properly punctuated sentence.
- **Method 2 (pandoc-to-plain-text, re-run in a separate fresh bash call after the file write):** tail of plain-text output ends identically, mid-paragraph continuity intact, no truncation markers, no orphaned tags.
- **Method 3 (raw XML inspection):** `word/document.xml` (159,779 bytes) ends cleanly with `...Doc_05 may now begin.</w:t></w:r></w:p><w:sectPr /></w:body></w:document>` -- well-formed close tags, `zipfile.testzip()` returns no errors.

This finding is tagged SUBSTANTIAL only in the sense that a positive truncation verdict is itself a substantive conclusion this review is required to state plainly, not because a defect was found: **the document is complete and is not truncated.**

---

## Overall Verdict: **SUBSTANTIAL REVISION REQUIRED**

Doc_04's own analytical content -- candidate generation, six-test application, the Confidence/Gravity Cross-Check, cross-strand testing, and the Interaction Matrix as it currently stands -- held up well under independent re-derivation and cross-document/primary-source verification; no fabricated citation, no misapplied classification rule, and no truncation were found. However, the document's Document Log explicitly and repeatedly asserts that its companion Gravity Index workbook is "finalized to match" the document, "all current as of round 6's fixes." That claim is false: the main Gravity Index sheet itself retains a stale Interaction Matrix count for G07 (1-of-5 instead of the document's own claimed 2-of-5), and the By Classification derived sheet retains G03's pre-round-3, retracted three-region cross-strand framing that both the main sheet and Doc_04's own prose explicitly disclaim. Both are small, mechanical fixes, but the document cannot be finalized while it makes a specific, checkable claim about companion-workbook synchronization that is not true -- especially given this project's own stated pattern (invoked by Doc_04 itself as a cautionary lesson) of derived sheets silently drifting out of sync after a source edit. Fix both cells, verify no other sheet inherited the same round-3/round-6 staleness, and the document is very close to ready.
